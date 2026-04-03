# Ollama Pair Results

- Pair: `tsp_branch_bound`
- Backend: `ollama`
- Model: `qwen2.5:7b`
- Run folder: `benchmark_runs/20260403-114041-ollama-qwen2.5-7b`

## LLM

- Log: [tsp_branch_bound/run_001_llm.md](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260403-114041-ollama-qwen2.5-7b/tsp_branch_bound/run_001_llm.md)
- Exit code: `0`
- Wall time: `87.930s`
- Input tokens: `209`
- Output tokens: `1,138`
- Total tokens: `1,347`
- Calls: `1`
- Outcome: hallucinated a hypothetical distance matrix and a fake optimal tour instead of refusing the under-specified prompt.

## RLM

- Log: [tsp_branch_bound/run_001_rlm.md](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260403-114041-ollama-qwen2.5-7b/tsp_branch_bound/run_001_rlm.md)
- Exit code: `0`
- Total wall time: `263.746s`
- RLM execution time: `263.587s`
- Overhead: `0.158s`
- Input tokens: `13,263`
- Output tokens: `1,823`
- Total tokens: `15,086`
- API calls: `0`
- Outcome: also hallucinated a fake distance structure and returned an incorrect optimal tour and cost.

## Interpretation

- The local 7B model is usable for collecting benchmark traces.
- This run is not a quality pass for the benchmark itself.
- On this under-specified TSP prompt, both the plain `LLM` path and the `RLM` path failed to stay grounded.
