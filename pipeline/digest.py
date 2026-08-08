"""Digest stage: DIGEST.md, logs/last_run.json, macOS notification."""

import json
import shutil
import subprocess
from datetime import datetime

from . import config


def post_url(rel_path: str) -> str:
    # content/<sector>/<file>.md  ->  <base>/<sector>/<file>/
    parts = rel_path.split("/")
    return f"{config.SITE_BASE_URL}/{parts[1]}/{parts[2][:-3]}/"


def build(report: dict) -> str:
    lines = [f"# Next Hop run digest", "",
             f"Run: {report['run_id']}  ",
             f"Status: {report['status']}  ",
             f"Run cost: ${report['cost_run']:.4f}  ",
             f"Month-to-date: ${report['cost_mtd']:.4f}", ""]
    if report.get("published"):
        lines.append("## Published")
        for p in report["published"]:
            lines.append(f"- [{p['sector']}] [{p['title']}]({post_url(p['path'])})")
        lines.append("")
    if report.get("skipped"):
        lines.append("## Sectors with no post this run")
        for s in report["skipped"]:
            lines.append(f"- {s}")
        lines.append("")
    if report.get("dropped"):
        lines.append("## Dropped by QA")
        for d in report["dropped"]:
            lines.append(f"- {d}")
        lines.append("")
    if report.get("warnings"):
        lines.append("## Warnings")
        for w in report["warnings"]:
            lines.append(f"- {w}")
        lines.append("")
    lines.append(f"Generated {datetime.now().astimezone().isoformat(timespec='seconds')}")
    return "\n".join(lines) + "\n"


def write(report: dict) -> None:
    config.ensure_dirs()
    config.DIGEST_FILE.write_text(build(report))
    config.LAST_RUN_FILE.write_text(json.dumps(report, indent=1))


def notify(report: dict) -> None:
    if not shutil.which("osascript"):
        return
    n = len(report.get("published", []))
    msg = f"{n} post(s) published, run ${report['cost_run']:.2f}, MTD ${report['cost_mtd']:.2f}"
    if report["status"] == "budget-abort":
        msg = "HALTED: monthly budget guardrail tripped"
    try:
        subprocess.run(
            ["osascript", "-e",
             f'display notification "{msg}" with title "Next Hop weekly"'],
            capture_output=True, timeout=10)
    except Exception:
        pass
