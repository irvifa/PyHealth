"""Regenerates kaggle_cells.txt from branch_seed_sweep.py (run after edits)."""
from pathlib import Path

here = Path(__file__).parent
sweep = (here / "branch_seed_sweep.py").read_text()

CELLS = [
    ("1. Setup: Python 3.12 venv + PyHealth (pinned commit) with wfdb", r'''
# Settings (right panel): Accelerator = GPU T4 x1 (or x2), Internet = ON.
# PyHealth needs Python >= 3.12, so build a separate venv with uv instead of
# relying on the Kaggle image's Python.
!nvidia-smi --query-gpu=name,memory.total --format=csv
!pip install -q uv
!uv venv -q --clear -p 3.12 /tmp/venv
!uv pip install -q --python /tmp/venv/bin/python "pyhealth[ptbxl] @ git+https://github.com/irvifa/PyHealth.git@2d51acec1922800b9cd69c233c29b4a755abb0bd"
!/tmp/venv/bin/python -c "import torch, pyhealth, wfdb; print('torch', torch.__version__, 'cuda', torch.cuda.is_available())"
'''),
    ("2. PTB-XL 1.0.3: use an attached Kaggle dataset if present, else PhysioNet", r'''
import glob, os, subprocess
hits = glob.glob("/kaggle/input/**/ptbxl_database.csv", recursive=True)
if hits:
    PTBXL_ROOT = os.path.dirname(hits[0])
else:
    # Open access, about 1.7 GB; takes a few minutes.
    url = ("https://physionet.org/static/published-projects/ptb-xl/"
           "ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3.zip")
    subprocess.run(["wget", "-q", "-c", "-O", "/tmp/ptbxl.zip", url], check=True)
    subprocess.run(["unzip", "-q", "-o", "/tmp/ptbxl.zip", "-d", "/tmp/ptbxl"], check=True)
    PTBXL_ROOT = os.path.dirname(
        glob.glob("/tmp/ptbxl/**/ptbxl_database.csv", recursive=True)[0])
os.environ["PTBXL_ROOT"] = PTBXL_ROOT
print("PTBXL_ROOT =", PTBXL_ROOT, "| records100:", os.path.isdir(f"{PTBXL_ROOT}/records100"))
'''),
    ("3. Write the sweep script (verbatim copy of branch_seed_sweep.py)",
     "%%writefile /kaggle/working/branch_seed_sweep.py\n" + sweep),
    ("4. Helper + smoke test on synthetic data (about a minute)", r"""
import os, subprocess, sys

PY = "/tmp/venv/bin/python"
SCRIPT = "/kaggle/working/branch_seed_sweep.py"

# The notebook's inline matplotlib backend doesn't exist inside the venv.
ENV = {**os.environ, "MPLBACKEND": "Agg"}

def sweep(*args):
    # Stream the sweep's output, dropping tqdm progress-bar noise.
    proc = subprocess.Popen([PY, "-W", "ignore", SCRIPT, *map(str, args)],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            text=True, bufsize=1, env=ENV)
    for line in proc.stdout:
        if "it/s]" not in line and "s/it]" not in line and line.strip():
            print(line, end="")
    if proc.wait():
        raise RuntimeError(f"sweep exited with {proc.returncode}")

sweep("--synthetic", "--seeds", "0", "--out-dir", "/tmp/smoke")
"""),
    ("5. Full run: rhythm branch, 3 seeds", r"""
# Use the same EPOCHS on every machine if you plan to merge results.
# The run resumes: re-running this cell skips finished (seed, variant) pairs.
# /kaggle/working is kept when you "Save Version", so results survive the
# session as notebook output.
BRANCH, SEEDS, EPOCHS = "rhythm", "3,4,5", 20  # Mac ran 0,1,2
OUT = f"/kaggle/working/runs/{BRANCH}_kaggle"
sweep("--root", PTBXL_ROOT, "--branch", BRANCH, "--seeds", SEEDS,
      "--epochs", EPOCHS, "--device", "cuda",
      "--cache-dir", "/tmp/pyhealth-cache", "--out-dir", OUT)
"""),
    ("6. Show the summary and zip results for download", r"""
import shutil
from IPython.display import Markdown, display
display(Markdown(open(f"{OUT}/summary.md").read()))
# The checkpoints aren't needed for the summary, so leave them out of the zip.
staging = f"/tmp/results_{BRANCH}"
shutil.copytree(OUT, staging, ignore=shutil.ignore_patterns("checkpoints"),
                dirs_exist_ok=True)
print(shutil.make_archive(f"/kaggle/working/results_{BRANCH}", "zip", staging))
"""),
]

parts = [
    "ProtoECGNet rhythm-branch seed sweep for Kaggle. This file is GENERATED\n"
    "by build_kaggle.py; edit branch_seed_sweep.py and rebuild instead.\n\n"
    "How to use: create a new Kaggle notebook, set Accelerator = GPU T4 and\n"
    "Internet = ON, then paste each block below into its own code cell, in\n"
    "order. Paste only what is between the ===== lines.\n"
]
for i, (title, body) in enumerate(CELLS, 1):
    parts.append(f"\n{'=' * 30} CELL {i}: {title} {'=' * 30}\n{body.strip()}\n")
(here / "kaggle_cells.txt").write_text("".join(parts))
print("wrote kaggle_cells.txt")
