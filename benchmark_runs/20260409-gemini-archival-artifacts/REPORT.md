# Gemini Archival Benchmark Report

This report normalizes the preserved Gemini benchmark artifacts recovered from the archival benchmark branches. Identical logs across cloned branches were deduplicated; the rows below use the cleanest preserved copies from `anshul-benchmark-findings-clean`.

## Aggregate Table

| Benchmark | Mode | Runs | Success | Rows w/ Wall | Rows w/ Tokens | Avg Wall (s) | Median Wall (s) | Avg Input Tokens | Avg Output Tokens | Avg Total Tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Battle of the Bastards | LLM | 2 | 2/2 (100%) | 2 | 2 | 1.070 | 1.070 | 257.000 | 12.500 | 269.500 |
| Battle of the Bastards | RLM | 1 | 0/1 (0%) | 1 | 0 | 9.014 | 9.014 | - | - | - |
| AuthProxy Long Context | LLM | 2 | 2/2 (100%) | 2 | 2 | 1.295 | 1.295 | 1443.000 | 67.500 | 1510.500 |
| AuthProxy Long Context | RLM | 2 | 2/2 (100%) | 2 | 2 | 13.556 | 13.556 | 12326.500 | 1654.000 | 13980.500 |
| Clinical Long Context | LLM | 1 | 1/1 (100%) | 1 | 1 | 1.956 | 1.956 | 1841.000 | 283.000 | 2124.000 |
| Clinical Long Context | RLM | 1 | 1/1 (100%) | 1 | 1 | 15.507 | 15.507 | 7481.000 | 4290.000 | 11771.000 |
| Launch Note App | LLM | 1 | 1/1 (100%) | 1 | 1 | 8.013 | 8.013 | 256.000 | 1888.000 | 2144.000 |
| Launch Note App | RLM | 1 | 1/1 (100%) | 1 | 1 | 20.671 | 20.671 | 5854.000 | 5362.000 | 11216.000 |
| PDF Cersei Warning | LLM | 1 | 1/1 (100%) | 1 | 1 | 36.382 | 36.382 | 195096.000 | 13.000 | 195109.000 |
| PDF Cersei Warning | RLM | 1 | 1/1 (100%) | 1 | 1 | 134.761 | 134.761 | 74777.000 | 66229.000 | 141006.000 |
| Under-specified TSP | LLM | 4 | 4/4 (100%) | 4 | 4 | 75.014 | 96.018 | 190.000 | 4523.000 | 4713.000 |
| Under-specified TSP | RLM | 4 | 4/4 (100%) | 3 | 4 | 15.488 | 15.270 | 19410.750 | 634.250 | 20045.000 |
| Stochastic Adaptive TSP | LLM | 2 | 2/2 (100%) | 2 | 2 | 74.533 | 74.533 | 300.000 | 5540.500 | 5840.500 |
| Stochastic Adaptive TSP | RLM | 2 | 2/2 (100%) | 2 | 2 | 82.637 | 82.637 | 47421.500 | 7332.000 | 54753.500 |

## Graphs

Blue = `LLM`, Red = `RLM`.

![Gemini Archival Average Wall Time by Benchmark](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260409-gemini-archival-artifacts/graphs/avg_wall_time_by_benchmark.svg)

![Gemini Archival Average Total Tokens by Benchmark](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260409-gemini-archival-artifacts/graphs/avg_total_tokens_by_benchmark.svg)

![Gemini Archival Per-Run Wall Time](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260409-gemini-archival-artifacts/graphs/per_run_wall_time.svg)

![Gemini Archival Per-Run Total Tokens](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260409-gemini-archival-artifacts/graphs/per_run_total_tokens.svg)

## Raw Data

| Benchmark | Run | Mode | Model | Artifact | Exit | Wall (s) | Exec (s) | Input | Output | Total | Source File | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Battle of the Bastards | 001 | LLM | `gemini-2.5-flash-lite` | complete | 0 | 1.153 | - | 257 | 12 | 269 | `anshul-benchmark-findings-clean/llm-test/llm-testing-1-parth.md` | - |
| Battle of the Bastards | 002 | LLM | `gemini-2.5-flash-lite` | complete | 0 | 0.987 | - | 257 | 13 | 270 | `anshul-benchmark-findings-clean/llm-test/llm-test2.py-parth.md` | - |
| Battle of the Bastards | 001 | RLM | `gemini-2.5-flash-lite` | partial | 1 | 9.014 | 6.818 | - | - | - | `anshul-benchmark-findings-clean/rlm-test/test2-rlms.md` | Script crashed while walking iteration metadata after printing latency; token counts were not preserved. |
| AuthProxy Long Context | 001 | LLM | `gemini-2.5-flash-lite` | complete | 0 | 1.463 | - | 1,443 | 69 | 1,512 | `anshul-benchmark-findings-clean/llm-test/output for llm long context training.md` | - |
| AuthProxy Long Context | 002 | LLM | `gemini-2.5-flash-lite` | complete | 0 | 1.127 | - | 1,443 | 66 | 1,509 | `anshul-benchmark-findings-clean/benchmark_rerun_authproxy.md` | Metrics copied from the later rerun note. |
| AuthProxy Long Context | 001 | RLM | `gemini-2.5-flash-lite` | complete | 0 | 13.171 | 13.005 | 9,323 | 1,680 | 11,003 | `anshul-benchmark-findings-clean/rlm-test/output for long context problem.md` | - |
| AuthProxy Long Context | 002 | RLM | `gemini-2.5-flash-lite` | complete | 0 | 13.941 | 11.613 | 15,330 | 1,628 | 16,958 | `anshul-benchmark-findings-clean/benchmark_rerun_authproxy.md` | Metrics copied from the later rerun note. |
| Clinical Long Context | 001 | LLM | `gemini-2.5-flash-lite` | complete | 0 | 1.956 | - | 1,841 | 283 | 2,124 | `anshul-benchmark-findings-clean/llm-test/clinical-llm-output.md` | - |
| Clinical Long Context | 001 | RLM | `gemini-2.5-flash-lite` | complete | 0 | 15.507 | 15.280 | 7,481 | 4,290 | 11,771 | `anshul-benchmark-findings-clean/rlm-test/clincal-rlm-output.md` | - |
| Launch Note App | 001 | LLM | `gemini-2.5-flash-lite` | complete | 0 | 8.013 | - | 256 | 1,888 | 2,144 | `anshul-benchmark-findings-clean/llm-test/test_launch_note_app.md` | - |
| Launch Note App | 001 | RLM | `gemini-2.5-flash-lite` | complete | 0 | 20.671 | 20.383 | 5,854 | 5,362 | 11,216 | `anshul-benchmark-findings-clean/rlm-test/test_launch_note_app.md` | - |
| PDF Cersei Warning | 001 | LLM | `gemini-2.5-flash-lite` | complete | 0 | 36.382 | - | 195,096 | 13 | 195,109 | `anshul-benchmark-findings-clean/llm-test/test_pdf_cersei_warning.md` | - |
| PDF Cersei Warning | 001 | RLM | `gemini-2.5-flash-lite` | complete | 0 | 134.761 | 134.297 | 74,777 | 66,229 | 141,006 | `anshul-benchmark-findings-clean/rlm-test/test_pdf_cersei_warning.md` | - |
| Under-specified TSP | 001 | LLM | `gemini-2.5-flash` | complete | 0 | 10.654 | - | 190 | 179 | 369 | `anshul-benchmark-findings-clean/rlm-test/test_tsp_branch_bound.md` | First complete pair in the archival TSP markdown. |
| Under-specified TSP | 001 | RLM | `gemini-2.5-flash` | complete | 0 | 13.053 | 12.768 | 17,033 | 486 | 17,519 | `anshul-benchmark-findings-clean/rlm-test/test_tsp_branch_bound.md` | First complete pair in the archival TSP markdown. |
| Under-specified TSP | 002 | LLM | `gemini-2.5-flash` | complete | 0 | 94.752 | - | 190 | 7,354 | 7,544 | `anshul-benchmark-findings-clean/rlm-test/test_tsp_branch_bound.md` | Later appended pair in the same archival markdown. |
| Under-specified TSP | 002 | RLM | `gemini-2.5-flash` | complete | 0 | 18.141 | 15.851 | 23,284 | 770 | 24,054 | `anshul-benchmark-findings-clean/rlm-test/test_tsp_branch_bound.md` | Later appended pair in the same archival markdown. |
| Under-specified TSP | 003 | LLM | `gemini-2.5-flash` | complete | 0 | 97.285 | - | 190 | 4,388 | 4,578 | `anshul-benchmark-findings-clean/llm-test/test_tsp_llm_only.md` | - |
| Under-specified TSP | 004 | LLM | `gemini-2.5-flash` | complete | 0 | 97.364 | - | 190 | 6,171 | 6,361 | `anshul-benchmark-findings-clean/llm-test/test_tsp_llm_only_additional_run.md` | - |
| Under-specified TSP | 003 | RLM | `gemini-2.5-flash` | complete | 0 | 15.270 | - | 12,959 | 275 | 13,234 | `anshul-benchmark-findings-clean/rlm-test/test_tsp_branch_bound_additional_run.md` | - |
| Under-specified TSP | 004 | RLM | `gemini-2.5-flash` | metrics_only | 0 | - | 20.250 | 24,367 | 1,006 | 25,373 | `anshul-benchmark-findings-clean/benchmark_rerun_tsp.md` | Later rerun note preserved execution time but not total wall time. |
| Stochastic Adaptive TSP | 001 | LLM | `gemini-2.5-flash` | complete | 0 | 85.612 | - | 300 | 6,132 | 6,432 | `anshul-benchmark-findings-clean/llm-test/test_stochastic_tsp_adaptive_llm_only.md` | - |
| Stochastic Adaptive TSP | 002 | LLM | `gemini-2.5-flash` | complete | 0 | 63.454 | - | 300 | 4,949 | 5,249 | `anshul-benchmark-findings-clean/rlm-test/test_stochastic_tsp_adaptive.md` | Baseline block preserved inside the paired RLM markdown. |
| Stochastic Adaptive TSP | 001 | RLM | `gemini-2.5-flash` | complete | 0 | 91.699 | 91.452 | 80,103 | 11,336 | 91,439 | `anshul-benchmark-findings-clean/rlm-test/test_stochastic_tsp_adaptive.md` | - |
| Stochastic Adaptive TSP | 002 | RLM | `gemini-2.5-flash` | complete | 0 | 73.576 | 73.378 | 14,740 | 3,328 | 18,068 | `anshul-benchmark-findings-clean/benchmark_rerun_stochastic_tsp.md` | Later rerun note with metric-only archival capture. |