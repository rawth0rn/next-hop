# Next Hop: agent operating manual

This repo is an autonomous blog. A deterministic Python pipeline researches,
writes, and publishes short posts about networking industry innovation to
https://rawth0rn.github.io/next-hop/ (GitHub Pages, repo rawth0rn/next-hop).

If you are the Hermes cron agent, your job is narrow: run the script for
your job, interpret its exit code, retry once on transient failure, and
report. The pipeline is the only thing that writes posts.

## Rules

- Never write, edit, or delete posts, style files, pipeline code, or config
  yourself. Only the scripts publish.
- Never bypass or edit the budget guardrail. If the pipeline reports a
  budget abort (exit 3), report it prominently and stop.
- Retry a failed script at most once, and only when the failure looks
  transient (network timeout, git push rejection, HTTP 5xx). Never a third run.
- Do not install anything. The venv at .venv/ is complete.

## Weekly job

1. Run `./scripts/weekly.sh`
2. Exit codes: 0 published fine, 2 partial (some sectors failed or deferred),
   3 budget guardrail abort, anything else is a failure.
3. Read `DIGEST.md` and `logs/last_run.json` for the details.
4. Report: posts published per sector with live URLs, sectors skipped and
   why, QA drops, run cost and month-to-date spend, feed warnings.

## Monthly calibration job

1. Run `./scripts/calibrate.sh`
2. Output NO_CHANGES means nothing to learn this month; report that in one line.
3. Otherwise report the change bullets and the commit hash so the owner can
   review with `git show` or undo with `git revert`.

## Key paths

- `pipeline/` the pipeline; `pipeline/sources.yaml` the feed registry
- `style/STYLE.md` voice contract (owner-editable), `style/samples/` few-shot samples
- `state/seen.jsonl` dedupe ledger, `costs/costs.jsonl` spend ledger
- `DIGEST.md` last run summary, `logs/last_run.json` machine-readable status
- Budget thresholds live in `pipeline/config.py` (abort at $20/month)

## Manual operations (for humans or interactive sessions)

- Weekly run now: `./scripts/weekly.sh`
- Dry run (no writes): `.venv/bin/python -m pipeline.run --dry-run`
- One sector only: `.venv/bin/python -m pipeline.run --sector telecom`
- Backfill: `.venv/bin/python -m pipeline.run --backfill 14`
- The site deploys automatically on push to main via GitHub Actions.
