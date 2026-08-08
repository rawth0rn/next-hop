"""Next Hop pipeline orchestrator.

Exit codes: 0 success, 1 hard failure, 2 partial, 3 budget guardrail abort.
"""

import argparse
import json
import sys
import traceback
from datetime import datetime, timezone

from . import (config, costs, digest, extract, fetch, publish, qa, triage,
               writer)


def _log_artifact(name: str, obj) -> None:
    config.ensure_dirs()
    (config.LOGS_DIR / name).write_text(json.dumps(obj, indent=1, default=str))


def _make_post(sector, picks, run_id, roundup=False):
    """Extract, write, QA (with one regen), or raise/drop. Returns post dict."""
    if roundup:
        materials = [extract.extract(i["url"]) for i in picks]
        post = writer.write_roundup(sector, picks, materials, run_id)
    else:
        item = picks
        material = extract.extract(item["url"])
        post = writer.write_post(sector, item, material, run_id)

    failures = qa.check_post(post)
    if failures:
        fb = "\n".join(f"- {f}" for f in failures)
        if roundup:
            post = writer.write_roundup(sector, picks, materials, run_id,
                                        feedback=fb)
        else:
            post = writer.write_post(sector, item, material, run_id,
                                     feedback=fb)
        failures = qa.check_post(post)
        if failures:
            raise ValueError("QA failed twice: " + "; ".join(failures))
    return post


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="python -m pipeline.run")
    ap.add_argument("--dry-run", action="store_true",
                    help="fetch + triage only; no writer calls, no writes, no push")
    ap.add_argument("--backfill", type=int, default=7, metavar="DAYS",
                    help="lookback window in days (default 7)")
    ap.add_argument("--max-per-sector", type=int, default=None)
    ap.add_argument("--sector", action="append",
                    help="limit to sector slug (repeatable)")
    ap.add_argument("--skip-push", action="store_true")
    ap.add_argument("--skip-notify", action="store_true")
    ap.add_argument("--pick-floor", type=int, default=None,
                    help="override standalone pick threshold (testing)")
    ap.add_argument("--roundup-floor", type=int, default=None,
                    help="override roundup threshold (testing)")
    ap.add_argument("--no-mark-seen", action="store_true",
                    help="do not record candidates in the seen ledger (testing)")
    args = ap.parse_args(argv)

    if args.max_per_sector is not None:
        config.MAX_PER_SECTOR = args.max_per_sector

    run_id = datetime.now(timezone.utc).strftime("run-%Y%m%dT%H%M%SZ")
    sectors = args.sector or list(config.SECTORS)
    for s in sectors:
        if s not in config.SECTORS:
            print(f"unknown sector: {s}", file=sys.stderr)
            return 1

    report = {"run_id": run_id, "status": "ok", "published": [], "skipped": [],
              "dropped": [], "warnings": [], "cost_run": 0.0, "cost_mtd": 0.0}

    # Budget guardrail: check before any LLM call.
    try:
        report["cost_mtd"] = costs.check_monthly_budget()
    except config.BudgetExceeded as e:
        report["status"] = "budget-abort"
        report["warnings"].append(str(e))
        report["cost_mtd"] = costs.month_to_date()
        digest.write(report)
        if not args.skip_notify:
            digest.notify(report)
        print(f"BUDGET ABORT: {e}")
        return 3

    print(f"[{run_id}] fetching feeds ({args.backfill}-day window)...")
    fetched = fetch.fetch_all(days=args.backfill)
    candidates = fetched["candidates"]
    _log_artifact("candidates.json", fetched)
    print(f"  {len(candidates)} new candidates; "
          f"{len(fetched['feed_errors'])} feed errors; "
          f"{len(fetched['disabled'])} feeds disabled")
    for e in fetched["feed_errors"]:
        report["warnings"].append(f"feed error: {e}")
    for d in fetched["disabled"]:
        report["warnings"].append(f"feed auto-disabled after repeated failures: {d}")

    triage_results = {}
    hard_errors = []
    for sector in sectors:
        try:
            res = triage.triage_sector(sector, candidates, run_id,
                                       pick_floor=args.pick_floor,
                                       roundup_floor=args.roundup_floor)
            triage_results[sector] = res
            print(f"  triage {sector}: {len(res['picks'])} picks, "
                  f"{len(res['roundup'])} roundup, {res['considered']} considered")
        except Exception as e:
            hard_errors.append(f"triage {sector}: {e}")
            triage_results[sector] = {"picks": [], "roundup": [],
                                      "considered": 0}
            traceback.print_exc()
    triage_results = triage.dedupe_across_sectors(triage_results)
    _log_artifact("triage.json", triage_results)

    if args.dry_run:
        report["status"] = "dry-run"
        report["cost_run"] = costs.run_total(run_id)
        report["cost_mtd"] = costs.month_to_date()
        _log_artifact("last_run.json", report)
        print(f"dry run complete: cost ${report['cost_run']:.4f}, "
              f"nothing written")
        return 0

    for sector in sectors:
        res = triage_results[sector]
        wrote_any = False
        # Per-run soft cap: stop starting new posts past the cap.
        if costs.run_total(run_id) > config.RUN_SOFT_CAP_USD:
            report["warnings"].append(
                "run soft cap reached; remaining sectors deferred")
            report["skipped"].append(f"{sector}: deferred (run soft cap)")
            continue
        try:
            if res["picks"]:
                for item in res["picks"]:
                    if qa.source_already_cited(item["url"]):
                        report["dropped"].append(
                            f"{sector}: {item['title'][:70]} "
                            "(source already covered by a published post)")
                        continue
                    try:
                        post = _make_post(sector, item, run_id)
                        rel = publish.write_post_file(sector, post)
                        report["published"].append(
                            {"sector": sector, "title": post["title"],
                             "path": rel})
                        wrote_any = True
                        print(f"  wrote {rel}")
                    except (ValueError, RuntimeError) as e:
                        report["dropped"].append(
                            f"{sector}: {item['title'][:70]} ({e})")
            elif res["roundup"]:
                post = _make_post(sector, res["roundup"], run_id, roundup=True)
                rel = publish.write_post_file(sector, post)
                report["published"].append(
                    {"sector": sector, "title": post["title"], "path": rel})
                wrote_any = True
                print(f"  wrote roundup {rel}")
        except config.BudgetExceeded as e:
            report["status"] = "budget-abort"
            report["warnings"].append(str(e))
            break
        except Exception as e:
            hard_errors.append(f"write {sector}: {e}")
            traceback.print_exc()
        if not wrote_any and not res["picks"] and not res["roundup"]:
            report["skipped"].append(
                f"{sector}: nothing scored above threshold "
                f"({res['considered']} considered)")
        elif not wrote_any:
            report["skipped"].append(f"{sector}: all candidates dropped by QA")

    # Mark what triage actually considered as seen so next week starts fresh.
    if not args.no_mark_seen:
        considered = set()
        for res in triage_results.values():
            considered.update(res.get("considered_ids", []))
        fetch.mark_seen([c for c in candidates if c["id"] in considered])

    report["cost_run"] = costs.run_total(run_id)
    report["cost_mtd"] = costs.month_to_date()
    if report["status"] != "budget-abort":
        if report["published"] and (hard_errors or report["dropped"] or
                                    any("soft cap" in w
                                        for w in report["warnings"])):
            report["status"] = "partial"
        elif not report["published"] and hard_errors:
            report["status"] = "failed"
    for e in hard_errors:
        report["warnings"].append(f"error: {e}")

    digest.write(report)
    n = len(report["published"])
    push_msg = publish.commit_and_push(
        f"posts: {n} new, {datetime.now().strftime('%Y-%m-%d')} run\n\n"
        f"Automated weekly run {run_id}.",
        push=not args.skip_push)
    print(f"publish: {push_msg}")
    if not args.skip_notify:
        digest.notify(report)

    print(f"[{run_id}] {report['status']}: {n} published, "
          f"cost ${report['cost_run']:.4f}, MTD ${report['cost_mtd']:.4f}")
    if report["status"] == "budget-abort":
        return 3
    if report["status"] == "failed":
        return 1
    if report["status"] == "partial":
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
