# Pooled Local Batch Summary

This directory pools two completed local Ollama `qwen2.5:7b` benchmark batches into a single `10`-run dataset per benchmark and mode.

Source batches:
- `benchmark_runs/20260403-121151-ollama-qwen2.5-7b`
- `benchmark_runs/20260409-203839-ollama-qwen2.5-7b`

- Total raw rows: `140`
- Local runs per benchmark/mode: `10`

| Benchmark | Mode | Runs | Successes | Avg Wall (s) | Avg Total Tokens |
| --- | --- | ---: | ---: | ---: | ---: |
| Battle of the Bastards | LLM | 10 | 10 | 8.077 | 313.000 |
| Battle of the Bastards | RLM | 10 | 10 | 119.765 | 10787.700 |
| AuthProxy Long Context | LLM | 10 | 10 | 23.135 | 1249.600 |
| AuthProxy Long Context | RLM | 10 | 10 | 171.029 | 13364.200 |
| Clinical Long Context | LLM | 10 | 10 | 116.577 | 2885.500 |
| Clinical Long Context | RLM | 10 | 10 | 97.614 | 11762.900 |
| Launch Note App | LLM | 10 | 10 | 103.273 | 1431.100 |
| Launch Note App | RLM | 10 | 10 | 248.228 | 12168.200 |
| PDF Cersei Warning | LLM | 10 | 10 | 111.305 | 4864.200 |
| PDF Cersei Warning | RLM | 10 | 9 | 200.657 | 19413.222 |
| Under-specified TSP | LLM | 10 | 10 | 102.791 | 1340.700 |
| Under-specified TSP | RLM | 10 | 10 | 514.593 | 24015.800 |
| Stochastic Adaptive TSP | LLM | 10 | 10 | 123.732 | 1433.100 |
| Stochastic Adaptive TSP | RLM | 10 | 9 | 598.444 | 23607.889 |