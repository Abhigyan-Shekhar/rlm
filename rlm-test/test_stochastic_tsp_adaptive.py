import sys
from pathlib import Path
from runpy import run_path

repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))
run_path(str(repo_root / "test_stochastic_tsp_adaptive.py"))
