Unit tests for making sure the whole system is not broken, mainly for
local execution and non-isolated environments.

Benchmark-facing scripts and captured markdown artifacts are kept
outside this pytest suite:

- root `test_*.py`: paired benchmark entry points
- [`llm-test/`](../llm-test): preserved baseline-only scripts and `.md`
  outputs
- [`rlm-test/`](../rlm-test): preserved recursive scripts and `.md`
  outputs
- [`benchmark_runs/`](../benchmark_runs): normalized paired `LLM`/`RLM`
  run logs and reports
