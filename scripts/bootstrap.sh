#!/usr/bin/env bash
# One-time launch backfill: 21-day window so every sector starts populated.
set -uo pipefail
cd "$(dirname "$0")/.."
.venv/bin/python -m pipeline.run --backfill 21 "$@"
