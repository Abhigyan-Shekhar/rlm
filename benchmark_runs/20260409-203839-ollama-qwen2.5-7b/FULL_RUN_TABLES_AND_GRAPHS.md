# Full Run Tables And Graphs

This report covers the completed local Ollama `qwen2.5:7b` batch and shows all preserved run data plus red/blue comparison graphs.

## Aggregate Table

| Benchmark | Mode | Runs | Success | Avg Wall (s) | Median Wall (s) | Avg Input Tokens | Avg Output Tokens | Avg Total Tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Battle of the Bastards | LLM | 5 | 5/5 (100%) | 8.351 | 7.631 | 275.000 | 37.400 | 312.400 |
| Battle of the Bastards | RLM | 5 | 5/5 (100%) | 131.152 | 116.849 | 11417.800 | 572.600 | 11990.400 |
| AuthProxy Long Context | LLM | 5 | 5/5 (100%) | 22.581 | 21.342 | 1082.000 | 169.200 | 1251.200 |
| AuthProxy Long Context | RLM | 5 | 5/5 (100%) | 162.951 | 131.030 | 12740.000 | 987.800 | 13727.800 |
| Clinical Long Context | LLM | 5 | 5/5 (100%) | 128.872 | 137.055 | 1645.000 | 1301.400 | 2946.400 |
| Clinical Long Context | RLM | 5 | 5/5 (100%) | 57.925 | 52.092 | 10663.000 | 341.800 | 11004.800 |
| Launch Note App | LLM | 5 | 5/5 (100%) | 115.264 | 107.300 | 257.000 | 1303.600 | 1560.600 |
| Launch Note App | RLM | 5 | 5/5 (100%) | 223.344 | 155.597 | 10052.400 | 1173.000 | 11225.400 |
| PDF Cersei Warning | LLM | 5 | 5/5 (100%) | 89.760 | 94.292 | 4096.000 | 624.000 | 4720.000 |
| PDF Cersei Warning | RLM | 5 | 4/5 (80%) | 185.983 | 204.865 | 17222.250 | 962.500 | 18184.750 |
| Under-specified TSP | LLM | 5 | 5/5 (100%) | 96.587 | 103.650 | 209.000 | 1147.800 | 1356.800 |
| Under-specified TSP | RLM | 5 | 5/5 (100%) | 518.505 | 492.472 | 20262.600 | 4253.800 | 24516.400 |
| Stochastic Adaptive TSP | LLM | 5 | 5/5 (100%) | 83.156 | 72.327 | 318.000 | 1177.600 | 1495.600 |
| Stochastic Adaptive TSP | RLM | 5 | 5/5 (100%) | 402.231 | 292.076 | 17058.200 | 3283.600 | 20341.800 |

## Graphs

Blue = `LLM`, Red = `RLM`.

![Average Wall Time by Benchmark](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260409-203839-ollama-qwen2.5-7b/graphs/avg_wall_time_by_benchmark.svg)

![Average Total Tokens by Benchmark](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260409-203839-ollama-qwen2.5-7b/graphs/avg_total_tokens_by_benchmark.svg)

![Per-Run Wall Time](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260409-203839-ollama-qwen2.5-7b/graphs/per_run_wall_time.svg)

![Per-Run Total Tokens](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260409-203839-ollama-qwen2.5-7b/graphs/per_run_total_tokens.svg)

## Raw Data By Benchmark

| Code | Benchmark |
| --- | --- |
| BOB | Battle of the Bastards |
| AUTH | AuthProxy Long Context |
| CLIN | Clinical Long Context |
| LNA | Launch Note App |
| PDF | PDF Cersei Warning |
| TSP | Under-specified TSP |
| STSP | Stochastic Adaptive TSP |

### Battle of the Bastards

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 10.512 | 10.512 | 275 | 36 | 311 | `llm-test/test_llm.py` | `got/run_001_llm.md` |
| 001 | RLM | 0 | 138.139 | 126.449 | 11,828 | 455 | 12,283 | `rlm-test/test_got.py` | `got/run_001_rlm.md` |
| 002 | LLM | 0 | 7.247 | 7.247 | 275 | 38 | 313 | `llm-test/test_llm.py` | `got/run_002_llm.md` |
| 002 | RLM | 0 | 116.849 | 106.258 | 11,914 | 407 | 12,321 | `rlm-test/test_got.py` | `got/run_002_rlm.md` |
| 003 | LLM | 0 | 10.503 | 10.503 | 275 | 33 | 308 | `llm-test/test_llm.py` | `got/run_003_llm.md` |
| 003 | RLM | 0 | 109.263 | 103.557 | 12,387 | 515 | 12,902 | `rlm-test/test_got.py` | `got/run_003_rlm.md` |
| 004 | LLM | 0 | 5.864 | 5.864 | 275 | 44 | 319 | `llm-test/test_llm.py` | `got/run_004_llm.md` |
| 004 | RLM | 0 | 73.804 | 73.478 | 8,762 | 450 | 9,212 | `rlm-test/test_got.py` | `got/run_004_rlm.md` |
| 005 | LLM | 0 | 7.631 | 7.631 | 275 | 36 | 311 | `llm-test/test_llm.py` | `got/run_005_llm.md` |
| 005 | RLM | 0 | 217.703 | 154.300 | 12,198 | 1,036 | 13,234 | `rlm-test/test_got.py` | `got/run_005_rlm.md` |

### AuthProxy Long Context

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 30.426 | 30.426 | 1,082 | 190 | 1,272 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_001_llm.md` |
| 001 | RLM | 0 | 316.270 | 256.959 | 14,016 | 1,921 | 15,937 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_001_rlm.md` |
| 002 | LLM | 0 | 25.545 | 25.545 | 1,082 | 192 | 1,274 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_002_llm.md` |
| 002 | RLM | 0 | 91.398 | 52.809 | 13,373 | 129 | 13,502 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_002_rlm.md` |
| 003 | LLM | 0 | 21.342 | 21.342 | 1,082 | 157 | 1,239 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_003_llm.md` |
| 003 | RLM | 0 | 171.021 | 110.262 | 14,000 | 1,087 | 15,087 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_003_rlm.md` |
| 004 | LLM | 0 | 20.940 | 20.940 | 1,082 | 150 | 1,232 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_004_llm.md` |
| 004 | RLM | 0 | 105.034 | 104.956 | 9,285 | 674 | 9,959 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_004_rlm.md` |
| 005 | LLM | 0 | 14.653 | 14.653 | 1,082 | 157 | 1,239 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_005_llm.md` |
| 005 | RLM | 0 | 131.030 | 88.606 | 13,026 | 1,128 | 14,154 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_005_rlm.md` |

### Clinical Long Context

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 173.678 | 173.678 | 1,645 | 1,569 | 3,214 | `llm-test/clinical-llm.py` | `clinical/run_001_llm.md` |
| 001 | RLM | 0 | 52.092 | 50.212 | 10,208 | 196 | 10,404 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_001_rlm.md` |
| 002 | LLM | 0 | 137.055 | 137.055 | 1,645 | 1,582 | 3,227 | `llm-test/clinical-llm.py` | `clinical/run_002_llm.md` |
| 002 | RLM | 0 | 51.368 | 38.129 | 10,459 | 314 | 10,773 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_002_rlm.md` |
| 003 | LLM | 0 | 71.576 | 71.576 | 1,645 | 743 | 2,388 | `llm-test/clinical-llm.py` | `clinical/run_003_llm.md` |
| 003 | RLM | 0 | 84.931 | 55.651 | 11,884 | 661 | 12,545 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_003_rlm.md` |
| 004 | LLM | 0 | 144.718 | 144.718 | 1,645 | 1,519 | 3,164 | `llm-test/clinical-llm.py` | `clinical/run_004_llm.md` |
| 004 | RLM | 0 | 58.383 | 44.139 | 10,644 | 320 | 10,964 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_004_rlm.md` |
| 005 | LLM | 0 | 117.333 | 117.333 | 1,645 | 1,094 | 2,739 | `llm-test/clinical-llm.py` | `clinical/run_005_llm.md` |
| 005 | RLM | 0 | 42.849 | 35.657 | 10,120 | 218 | 10,338 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_005_rlm.md` |

### Launch Note App

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 107.300 | 107.300 | 257 | 1,390 | 1,647 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_001_llm.md` |
| 001 | RLM | 0 | 37.833 | 37.447 | 2,590 | 197 | 2,787 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_001_rlm.md` |
| 002 | LLM | 0 | 146.679 | 146.679 | 257 | 1,665 | 1,922 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_002_llm.md` |
| 002 | RLM | 0 | 516.793 | 513.733 | 12,879 | 1,269 | 14,148 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_002_rlm.md` |
| 003 | LLM | 0 | 97.669 | 97.669 | 257 | 949 | 1,206 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_003_llm.md` |
| 003 | RLM | 0 | 276.838 | 244.290 | 12,936 | 2,189 | 15,125 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_003_rlm.md` |
| 004 | LLM | 0 | 127.190 | 127.190 | 257 | 1,489 | 1,746 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_004_llm.md` |
| 004 | RLM | 0 | 129.657 | 123.546 | 12,485 | 942 | 13,427 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_004_rlm.md` |
| 005 | LLM | 0 | 97.483 | 97.483 | 257 | 1,025 | 1,282 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_005_llm.md` |
| 005 | RLM | 0 | 155.597 | 155.469 | 9,372 | 1,268 | 10,640 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_005_rlm.md` |

### PDF Cersei Warning

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 119.110 | 119.110 | 4,096 | 816 | 4,912 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_001_llm.md` |
| 001 | RLM | -9 | - | - | - | - | - | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_001_rlm.md` |
| 002 | LLM | 0 | 64.506 | 64.506 | 4,096 | 603 | 4,699 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_002_llm.md` |
| 002 | RLM | 0 | 291.350 | 246.308 | 22,273 | 1,490 | 23,763 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_002_rlm.md` |
| 003 | LLM | 0 | 94.292 | 94.292 | 4,096 | 613 | 4,709 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_003_llm.md` |
| 003 | RLM | 0 | 203.066 | 189.306 | 21,905 | 1,285 | 23,190 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_003_rlm.md` |
| 004 | LLM | 0 | 75.969 | 75.969 | 4,096 | 426 | 4,522 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_004_llm.md` |
| 004 | RLM | 0 | 42.854 | 42.830 | 2,897 | 158 | 3,055 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_004_rlm.md` |
| 005 | LLM | 0 | 94.925 | 94.925 | 4,096 | 662 | 4,758 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_005_llm.md` |
| 005 | RLM | 0 | 206.664 | 159.939 | 21,814 | 917 | 22,731 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_005_rlm.md` |

### Under-specified TSP

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 73.841 | 73.841 | 209 | 881 | 1,090 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_001_llm.md` |
| 001 | RLM | 0 | 578.646 | 578.483 | 18,593 | 5,985 | 24,578 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_001_rlm.md` |
| 002 | LLM | 0 | 105.367 | 105.367 | 209 | 1,277 | 1,486 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_002_llm.md` |
| 002 | RLM | 0 | 604.700 | 249.397 | 23,194 | 2,225 | 25,419 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_002_rlm.md` |
| 003 | LLM | 0 | 103.650 | 103.650 | 209 | 1,026 | 1,235 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_003_llm.md` |
| 003 | RLM | 0 | 492.472 | 474.990 | 23,723 | 4,637 | 28,360 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_003_rlm.md` |
| 004 | LLM | 0 | 106.855 | 106.855 | 209 | 1,380 | 1,589 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_004_llm.md` |
| 004 | RLM | 0 | 425.986 | 425.691 | 19,388 | 4,053 | 23,441 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_004_rlm.md` |
| 005 | LLM | 0 | 93.224 | 93.224 | 209 | 1,175 | 1,384 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_005_llm.md` |
| 005 | RLM | 0 | 490.722 | 490.673 | 16,415 | 4,369 | 20,784 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_005_rlm.md` |

### Stochastic Adaptive TSP

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 96.515 | 96.515 | 318 | 1,191 | 1,509 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_001_llm.md` |
| 001 | RLM | 0 | 873.264 | 819.806 | 21,953 | 5,586 | 27,539 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_001_rlm.md` |
| 002 | LLM | 0 | 59.780 | 59.780 | 318 | 858 | 1,176 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_002_llm.md` |
| 002 | RLM | 0 | 152.822 | 152.617 | 12,985 | 1,484 | 14,469 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_002_rlm.md` |
| 003 | LLM | 0 | 63.006 | 63.006 | 318 | 1,213 | 1,531 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_003_llm.md` |
| 003 | RLM | 0 | 483.570 | 451.265 | 24,592 | 4,634 | 29,226 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_003_rlm.md` |
| 004 | LLM | 0 | 124.153 | 124.153 | 318 | 1,655 | 1,973 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_004_llm.md` |
| 004 | RLM | 0 | 292.076 | 291.926 | 16,586 | 2,583 | 19,169 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_004_rlm.md` |
| 005 | LLM | 0 | 72.327 | 72.327 | 318 | 971 | 1,289 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_005_llm.md` |
| 005 | RLM | 0 | 209.424 | 209.153 | 9,175 | 2,131 | 11,306 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_005_rlm.md` |
