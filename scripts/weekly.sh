#!/usr/bin/env bash
# Next Hop weekly pipeline entry point. Exit codes:
# 0 ok, 1 failure, 2 partial, 3 budget guardrail abort.
set -uo pipefail
cd "$(dirname "$0")/.."
.venv/bin/python -m pipeline.run "$@"
