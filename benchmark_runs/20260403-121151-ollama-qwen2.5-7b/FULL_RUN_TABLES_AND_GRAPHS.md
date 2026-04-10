# Full Run Tables And Graphs

This report covers the completed local Ollama `qwen2.5:7b` batch and shows all preserved run data plus red/blue comparison graphs.

## Aggregate Table

| Benchmark | Mode | Runs | Success | Avg Wall (s) | Median Wall (s) | Avg Input Tokens | Avg Output Tokens | Avg Total Tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Battle of the Bastards | LLM | 5 | 5/5 (100%) | 7.803 | 7.756 | 275.000 | 38.600 | 313.600 |
| Battle of the Bastards | RLM | 5 | 5/5 (100%) | 108.379 | 73.517 | 9145.000 | 440.000 | 9585.000 |
| AuthProxy Long Context | LLM | 5 | 5/5 (100%) | 23.689 | 23.109 | 1082.000 | 166.000 | 1248.000 |
| AuthProxy Long Context | RLM | 5 | 5/5 (100%) | 179.107 | 173.042 | 11749.000 | 1251.600 | 13000.600 |
| Clinical Long Context | LLM | 5 | 5/5 (100%) | 104.282 | 111.993 | 1645.000 | 1179.600 | 2824.600 |
| Clinical Long Context | RLM | 5 | 5/5 (100%) | 137.302 | 52.487 | 11503.800 | 1017.200 | 12521.000 |
| Launch Note App | LLM | 5 | 5/5 (100%) | 91.281 | 81.166 | 257.000 | 1044.600 | 1301.600 |
| Launch Note App | RLM | 5 | 5/5 (100%) | 273.112 | 276.742 | 10956.800 | 2154.200 | 13111.000 |
| PDF Cersei Warning | LLM | 5 | 5/5 (100%) | 132.849 | 133.707 | 4096.000 | 912.400 | 5008.400 |
| PDF Cersei Warning | RLM | 5 | 5/5 (100%) | 212.396 | 191.413 | 19444.400 | 951.600 | 20396.000 |
| Under-specified TSP | LLM | 5 | 5/5 (100%) | 108.994 | 106.786 | 209.000 | 1115.600 | 1324.600 |
| Under-specified TSP | RLM | 5 | 5/5 (100%) | 510.680 | 369.738 | 20109.200 | 3406.000 | 23515.200 |
| Stochastic Adaptive TSP | LLM | 5 | 5/5 (100%) | 164.309 | 185.630 | 318.000 | 1052.600 | 1370.600 |
| Stochastic Adaptive TSP | RLM | 5 | 4/5 (80%) | 843.710 | 700.832 | 24390.000 | 3300.500 | 27690.500 |

## Graphs

Blue = `LLM`, Red = `RLM`.

![Average Wall Time by Benchmark](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260403-121151-ollama-qwen2.5-7b/graphs/avg_wall_time_by_benchmark.svg)

![Average Total Tokens by Benchmark](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260403-121151-ollama-qwen2.5-7b/graphs/avg_total_tokens_by_benchmark.svg)

![Per-Run Wall Time](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260403-121151-ollama-qwen2.5-7b/graphs/per_run_wall_time.svg)

![Per-Run Total Tokens](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260403-121151-ollama-qwen2.5-7b/graphs/per_run_total_tokens.svg)

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
| 001 | LLM | 0 | 9.832 | 9.832 | 275 | 56 | 331 | `llm-test/test_llm.py` | `got/run_001_llm.md` |
| 001 | RLM | 0 | 73.517 | 73.048 | 8,816 | 299 | 9,115 | `rlm-test/test_got.py` | `got/run_001_rlm.md` |
| 002 | LLM | 0 | 7.135 | 7.135 | 275 | 41 | 316 | `llm-test/test_llm.py` | `got/run_002_llm.md` |
| 002 | RLM | 0 | 244.427 | 197.253 | 13,982 | 936 | 14,918 | `rlm-test/test_got.py` | `got/run_002_rlm.md` |
| 003 | LLM | 0 | 7.756 | 7.756 | 275 | 33 | 308 | `llm-test/test_llm.py` | `got/run_003_llm.md` |
| 003 | RLM | 0 | 73.046 | 72.665 | 8,753 | 367 | 9,120 | `rlm-test/test_got.py` | `got/run_003_rlm.md` |
| 004 | LLM | 0 | 5.573 | 5.573 | 275 | 33 | 308 | `llm-test/test_llm.py` | `got/run_004_llm.md` |
| 004 | RLM | 0 | 60.789 | 60.714 | 5,483 | 289 | 5,772 | `rlm-test/test_got.py` | `got/run_004_rlm.md` |
| 005 | LLM | 0 | 8.717 | 8.717 | 275 | 30 | 305 | `llm-test/test_llm.py` | `got/run_005_llm.md` |
| 005 | RLM | 0 | 90.114 | 89.877 | 8,691 | 309 | 9,000 | `rlm-test/test_got.py` | `got/run_005_rlm.md` |

### AuthProxy Long Context

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 30.373 | 30.373 | 1,082 | 178 | 1,260 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_001_llm.md` |
| 001 | RLM | 0 | 169.596 | 169.158 | 6,619 | 1,414 | 8,033 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_001_rlm.md` |
| 002 | LLM | 0 | 20.656 | 20.656 | 1,082 | 145 | 1,227 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_002_llm.md` |
| 002 | RLM | 0 | 219.642 | 173.374 | 13,844 | 1,741 | 15,585 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_002_rlm.md` |
| 003 | LLM | 0 | 20.201 | 20.201 | 1,082 | 149 | 1,231 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_003_llm.md` |
| 003 | RLM | 0 | 146.474 | 118.017 | 13,488 | 990 | 14,478 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_003_rlm.md` |
| 004 | LLM | 0 | 24.106 | 24.106 | 1,082 | 171 | 1,253 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_004_llm.md` |
| 004 | RLM | 0 | 173.042 | 112.295 | 13,385 | 937 | 14,322 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_004_rlm.md` |
| 005 | LLM | 0 | 23.109 | 23.109 | 1,082 | 187 | 1,269 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_005_llm.md` |
| 005 | RLM | 0 | 186.782 | 153.458 | 11,409 | 1,176 | 12,585 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_005_rlm.md` |

### Clinical Long Context

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 137.570 | 137.570 | 1,645 | 1,583 | 3,228 | `llm-test/clinical-llm.py` | `clinical/run_001_llm.md` |
| 001 | RLM | 0 | 35.334 | 31.440 | 10,181 | 125 | 10,306 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_001_rlm.md` |
| 002 | LLM | 0 | 111.993 | 111.993 | 1,645 | 1,312 | 2,957 | `llm-test/clinical-llm.py` | `clinical/run_002_llm.md` |
| 002 | RLM | 0 | 52.487 | 44.638 | 10,392 | 351 | 10,743 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_002_rlm.md` |
| 003 | LLM | 0 | 112.244 | 112.244 | 1,645 | 1,234 | 2,879 | `llm-test/clinical-llm.py` | `clinical/run_003_llm.md` |
| 003 | RLM | 0 | 34.254 | 32.456 | 10,160 | 123 | 10,283 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_003_rlm.md` |
| 004 | LLM | 0 | 101.873 | 101.873 | 1,645 | 1,270 | 2,915 | `llm-test/clinical-llm.py` | `clinical/run_004_llm.md` |
| 004 | RLM | 0 | 343.306 | 281.513 | 15,177 | 2,883 | 18,060 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_004_rlm.md` |
| 005 | LLM | 0 | 57.730 | 57.730 | 1,645 | 499 | 2,144 | `llm-test/clinical-llm.py` | `clinical/run_005_llm.md` |
| 005 | RLM | 0 | 221.131 | 220.670 | 11,609 | 1,604 | 13,213 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_005_rlm.md` |

### Launch Note App

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 81.166 | 81.166 | 257 | 978 | 1,235 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_001_llm.md` |
| 001 | RLM | 0 | 226.218 | 147.923 | 11,223 | 2,144 | 13,367 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_001_rlm.md` |
| 002 | LLM | 0 | 88.222 | 88.222 | 257 | 1,129 | 1,386 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_002_llm.md` |
| 002 | RLM | 0 | 276.742 | 232.978 | 13,106 | 2,843 | 15,949 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_002_rlm.md` |
| 003 | LLM | 0 | 58.346 | 58.346 | 257 | 879 | 1,136 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_003_llm.md` |
| 003 | RLM | 0 | 102.077 | 101.825 | 5,808 | 1,416 | 7,224 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_003_rlm.md` |
| 004 | LLM | 0 | 72.258 | 72.258 | 257 | 837 | 1,094 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_004_llm.md` |
| 004 | RLM | 0 | 464.365 | 304.048 | 14,161 | 2,426 | 16,587 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_004_rlm.md` |
| 005 | LLM | 0 | 156.415 | 156.415 | 257 | 1,400 | 1,657 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_005_llm.md` |
| 005 | RLM | 0 | 296.160 | 291.026 | 10,486 | 1,942 | 12,428 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_005_rlm.md` |

### PDF Cersei Warning

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 135.947 | 135.947 | 4,096 | 728 | 4,824 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_001_llm.md` |
| 001 | RLM | 0 | 191.413 | 191.159 | 10,247 | 903 | 11,150 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_001_rlm.md` |
| 002 | LLM | 0 | 116.163 | 116.163 | 4,096 | 692 | 4,788 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_002_llm.md` |
| 002 | RLM | 0 | 231.660 | 184.283 | 21,579 | 899 | 22,478 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_002_rlm.md` |
| 003 | LLM | 0 | 133.442 | 133.442 | 4,096 | 816 | 4,912 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_003_llm.md` |
| 003 | RLM | 0 | 318.367 | 277.481 | 22,295 | 1,289 | 23,584 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_003_rlm.md` |
| 004 | LLM | 0 | 133.707 | 133.707 | 4,096 | 1,085 | 5,181 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_004_llm.md` |
| 004 | RLM | 0 | 139.048 | 116.216 | 21,496 | 777 | 22,273 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_004_rlm.md` |
| 005 | LLM | 0 | 144.988 | 144.988 | 4,096 | 1,241 | 5,337 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_005_llm.md` |
| 005 | RLM | 0 | 181.494 | 123.025 | 21,605 | 890 | 22,495 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_005_rlm.md` |

### Under-specified TSP

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 83.021 | 83.021 | 209 | 1,154 | 1,363 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_001_llm.md` |
| 001 | RLM | 0 | 253.519 | 253.280 | 12,514 | 2,661 | 15,175 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_001_rlm.md` |
| 002 | LLM | 0 | 85.607 | 85.607 | 209 | 1,055 | 1,264 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_002_llm.md` |
| 002 | RLM | 0 | 369.738 | 296.882 | 23,510 | 2,468 | 25,978 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_002_rlm.md` |
| 003 | LLM | 0 | 127.640 | 127.640 | 209 | 1,057 | 1,266 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_003_llm.md` |
| 003 | RLM | 0 | 705.174 | 697.629 | 22,245 | 4,097 | 26,342 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_003_rlm.md` |
| 004 | LLM | 0 | 141.916 | 141.916 | 209 | 1,103 | 1,312 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_004_llm.md` |
| 004 | RLM | 0 | 970.961 | 846.544 | 20,689 | 5,498 | 26,187 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_004_rlm.md` |
| 005 | LLM | 0 | 106.786 | 106.786 | 209 | 1,209 | 1,418 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_005_llm.md` |
| 005 | RLM | 0 | 254.008 | 192.689 | 21,588 | 2,306 | 23,894 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_005_rlm.md` |

### Stochastic Adaptive TSP

| Run | Mode | Exit | Wall (s) | Exec (s) | Input Tokens | Output Tokens | Total Tokens | Script | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | LLM | 0 | 98.209 | 98.209 | 318 | 1,059 | 1,377 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_001_llm.md` |
| 001 | RLM | 0 | 633.152 | 582.324 | 24,446 | 4,417 | 28,863 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_001_rlm.md` |
| 002 | LLM | 0 | 106.263 | 106.263 | 318 | 999 | 1,317 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_002_llm.md` |
| 002 | RLM | 0 | 1342.957 | 1238.970 | 24,535 | 3,297 | 27,832 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_002_rlm.md` |
| 003 | LLM | 0 | 224.292 | 224.292 | 318 | 1,170 | 1,488 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_003_llm.md` |
| 003 | RLM | 0 | 768.512 | 746.877 | 23,597 | 2,772 | 26,369 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_003_rlm.md` |
| 004 | LLM | 0 | 207.149 | 207.149 | 318 | 1,061 | 1,379 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_004_llm.md` |
| 004 | RLM | -9 | - | - | - | - | - | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_004_rlm.md` |
| 005 | LLM | 0 | 185.630 | 185.630 | 318 | 974 | 1,292 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_005_llm.md` |
| 005 | RLM | 0 | 630.217 | 589.147 | 24,982 | 2,716 | 27,698 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_005_rlm.md` |
