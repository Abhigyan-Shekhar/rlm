# LLM Benchmark Scripts

This directory preserves the baseline-only benchmark scripts and the
captured markdown outputs that were collected alongside them.

Use these files when you want the plain `LLM` path without the recursive
runtime wrapper.

Contents:

- `test_*.py`: baseline benchmark scripts.
- `*.md`: saved prompts, notes, and captured outputs from those baseline
  runs.

The paired benchmark harness lives at the repo root and under
`benchmark_runs/`, where each recorded run is stored as matched
`run_XXX_llm.md` and `run_XXX_rlm.md` files.
