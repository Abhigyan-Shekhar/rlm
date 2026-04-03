# Benchmark Batch In Progress

- Backend: `ollama`
- Model: `qwen2.5:7b`
- Command:
  - `.venv/bin/python run_benchmark_pairs.py --backend ollama --model qwen2.5:7b --runs 30`
- Started from: `/Users/abhigyanshekhar/Desktop/RLM-FULL`

## Logging Behavior

- Each `LLM` run is saved immediately as `*/run_NNN_llm.md`
- Each `RLM` run is saved immediately as `*/run_NNN_rlm.md`
- `SUMMARY.md` is written when the full batch exits cleanly

## Current Pair Order

1. `got`
2. `authproxy`
3. `clinical`
4. `launch_note_app`
5. `pdf_cersei_warning`
6. `tsp_branch_bound`
7. `stochastic_tsp`

## Current State

- The batch is running.
- Completed logs are already appearing under this folder.
