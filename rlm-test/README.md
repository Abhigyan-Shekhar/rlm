# RLM Benchmark Scripts

This directory preserves the recursive benchmark scripts and the
captured markdown outputs produced by those runs.

Use these files when you want to inspect or rerun the `RLM` path and its
paired benchmark prompts outside the unit-test suite.

Contents:

- `test_*.py`: recursive benchmark scripts.
- `*.md`: saved prompts, notes, and captured outputs from those
  recursive runs.

The normalized paired benchmark artifacts live under `benchmark_runs/`,
where each run is recorded as matched `run_XXX_llm.md` and
`run_XXX_rlm.md` files.
