#!/usr/bin/env bash
# ProtoECGNet rhythm-branch seed sweep on a MacBook (Apple silicon).
#
# Usage (from the repo root):
#   bash experiments/protoecgnet/run_mac.sh            # full run: 3 seeds
#   bash experiments/protoecgnet/run_mac.sh smoke      # synthetic check, ~1 min
#
# Overridable via env vars, e.g.:
#   PTBXL_ROOT=~/data/ptb-xl EPOCHS=10 DEVICE=cpu SEEDS=0,1 bash .../run_mac.sh
#
# The run is resumable: if it stops (lid closed, Ctrl-C), run the same command
# again and finished (seed, variant) pairs are skipped.
set -euo pipefail

cd "$(dirname "$0")/../.."
PY="${PY:-.venv/bin/python}"
PTBXL_ROOT="${PTBXL_ROOT:-$HOME/workspace/dataset}"
BRANCH="${BRANCH:-rhythm}"
SEEDS="${SEEDS:-0,1,2}"
EPOCHS="${EPOCHS:-20}"
# MPS works with this model; set DEVICE=cpu to match the PR's MacBook numbers.
DEVICE="${DEVICE:-mps}"
OUT="${OUT:-experiments/protoecgnet/runs/${BRANCH}_mac}"
CACHE="${CACHE:-$HOME/.cache/pyhealth-ptbxl}"

# Waveform decoding needs the optional wfdb extra.
"$PY" -c "import wfdb" 2>/dev/null || uv pip install --python "$PY" "wfdb>=4.1.0"

if [[ "${1:-}" == "smoke" ]]; then
  exec "$PY" experiments/protoecgnet/branch_seed_sweep.py --synthetic \
    --seeds 0 --device "$DEVICE" --out-dir experiments/protoecgnet/runs/smoke
fi

mkdir -p "$OUT"
echo "branch=$BRANCH seeds=$SEEDS epochs=$EPOCHS device=$DEVICE -> $OUT"
# caffeinate keeps the Mac awake (on power) for the whole run.
caffeinate -i "$PY" experiments/protoecgnet/branch_seed_sweep.py \
  --root "$PTBXL_ROOT" \
  --branch "$BRANCH" \
  --seeds "$SEEDS" \
  --epochs "$EPOCHS" \
  --device "$DEVICE" \
  --cache-dir "$CACHE" \
  --out-dir "$OUT" 2>&1 | tee -a "$OUT/log.txt"

echo
echo "Summary: $OUT/summary.md"
