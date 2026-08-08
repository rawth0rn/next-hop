"""Cost ledger and budget guardrails.

Every LLM call appends one JSON line to costs/costs.jsonl. The month-to-date
sum drives the abort guardrail. NEXTHOP_TEST_MTD_SPEND overrides the
month-to-date value for guardrail testing.
"""

import json
import os
from datetime import datetime, timezone

from . import config


def record(run_id: str, stage: str, model: str, prompt_tokens: int,
           completion_tokens: int, cost_usd: float) -> None:
    config.ensure_dirs()
    row = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "run_id": run_id,
        "stage": stage,
        "model": model,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "cost_usd": round(cost_usd, 6),
    }
    with config.COSTS_FILE.open("a") as f:
        f.write(json.dumps(row) + "\n")


def _rows():
    if not config.COSTS_FILE.exists():
        return
    with config.COSTS_FILE.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def month_to_date() -> float:
    override = os.environ.get("NEXTHOP_TEST_MTD_SPEND")
    if override is not None:
        return float(override)
    month = datetime.now(timezone.utc).strftime("%Y-%m")
    return sum(r.get("cost_usd", 0.0) for r in _rows()
               if str(r.get("ts", "")).startswith(month))


def run_total(run_id: str) -> float:
    return sum(r.get("cost_usd", 0.0) for r in _rows()
               if r.get("run_id") == run_id)


def check_monthly_budget() -> float:
    """Return month-to-date spend; raise BudgetExceeded at the abort line."""
    mtd = month_to_date()
    if mtd >= config.MONTHLY_ABORT_USD:
        raise config.BudgetExceeded(
            f"month-to-date spend ${mtd:.2f} is at or over the "
            f"${config.MONTHLY_ABORT_USD:.2f} abort threshold"
        )
    return mtd
