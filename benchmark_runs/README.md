# Benchmark Run Artifacts

This directory stores normalized benchmark outputs captured by the
paired harness.

Each run directory contains:

- `run_XXX_llm.md`: the plain baseline `LLM` terminal log for that run
- `run_XXX_rlm.md`: the corresponding `RLM` terminal log for the same
  benchmark input
- `SUMMARY.md`: run-level status table for the batch
- report markdown such as `REPORT.md`, `ACCURACY_REPORT.md`,
  `FRONTIER_REPORT.md`, or `FULL_RUN_TABLES_AND_GRAPHS.md` when they
  were generated for that batch

The preserved standalone script directories are:

- [`../llm-test/`](../llm-test): baseline-only benchmark scripts and
  saved markdown outputs
- [`../rlm-test/`](../rlm-test): recursive benchmark scripts and saved
  markdown outputs

The active paired entry points remain at the repository root as
`test_*.py`.
