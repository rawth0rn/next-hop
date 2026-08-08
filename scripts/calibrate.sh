#!/usr/bin/env bash
# Monthly style calibration. Prints NO_CHANGES or a change summary.
set -uo pipefail
cd "$(dirname "$0")/.."
.venv/bin/python -m pipeline.calibrate
