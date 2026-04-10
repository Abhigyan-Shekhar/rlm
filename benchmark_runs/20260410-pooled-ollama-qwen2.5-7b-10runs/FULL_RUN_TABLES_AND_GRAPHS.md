# Full Run Tables And Graphs

This report covers the completed local Ollama `qwen2.5:7b` batch and shows all preserved run data plus red/blue comparison graphs.

## Aggregate Table

| Benchmark | Mode | Runs | Success | Avg Wall (s) | Median Wall (s) | Avg Input Tokens | Avg Output Tokens | Avg Total Tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Battle of the Bastards | LLM | 10 | 10/10 (100%) | 8.077 | 7.694 | 275.000 | 38.000 | 313.000 |
| Battle of the Bastards | RLM | 10 | 10/10 (100%) | 119.765 | 99.689 | 10281.400 | 506.300 | 10787.700 |
| AuthProxy Long Context | LLM | 10 | 10/10 (100%) | 23.135 | 22.226 | 1082.000 | 167.600 | 1249.600 |
| AuthProxy Long Context | RLM | 10 | 10/10 (100%) | 171.029 | 170.308 | 12244.500 | 1119.700 | 13364.200 |
| Clinical Long Context | LLM | 10 | 10/10 (100%) | 116.577 | 114.788 | 1645.000 | 1240.500 | 2885.500 |
| Clinical Long Context | RLM | 10 | 10/10 (100%) | 97.614 | 52.290 | 11083.400 | 679.500 | 11762.900 |
| Launch Note App | LLM | 10 | 10/10 (100%) | 103.273 | 97.576 | 257.000 | 1174.100 | 1431.100 |
| Launch Note App | RLM | 10 | 10/10 (100%) | 248.228 | 251.480 | 10504.600 | 1663.600 | 12168.200 |
| PDF Cersei Warning | LLM | 10 | 10/10 (100%) | 111.305 | 117.636 | 4096.000 | 768.200 | 4864.200 |
| PDF Cersei Warning | RLM | 10 | 9/10 (90%) | 200.657 | 203.066 | 18456.778 | 956.444 | 19413.222 |
| Under-specified TSP | LLM | 10 | 10/10 (100%) | 102.791 | 104.508 | 209.000 | 1131.700 | 1340.700 |
| Under-specified TSP | RLM | 10 | 10/10 (100%) | 514.593 | 491.597 | 20185.900 | 3829.900 | 24015.800 |
| Stochastic Adaptive TSP | LLM | 10 | 10/10 (100%) | 123.732 | 102.236 | 318.000 | 1115.100 | 1433.100 |
| Stochastic Adaptive TSP | RLM | 10 | 9/10 (90%) | 598.444 | 630.217 | 20316.778 | 3291.111 | 23607.889 |

## Graphs

Blue = `LLM`, Red = `RLM`.

![Average Wall Time by Benchmark](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260410-pooled-ollama-qwen2.5-7b-10runs/graphs/avg_wall_time_by_benchmark.svg)

![Average Total Tokens by Benchmark](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260410-pooled-ollama-qwen2.5-7b-10runs/graphs/avg_total_tokens_by_benchmark.svg)

![Per-Run Wall Time](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260410-pooled-ollama-qwen2.5-7b-10runs/graphs/per_run_wall_time.svg)

![Per-Run Total Tokens](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260410-pooled-ollama-qwen2.5-7b-10runs/graphs/per_run_total_tokens.svg)

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
| 006 | LLM | 0 | 10.512 | 10.512 | 275 | 36 | 311 | `llm-test/test_llm.py` | `got/run_006_llm.md` |
| 006 | RLM | 0 | 138.139 | 126.449 | 11,828 | 455 | 12,283 | `rlm-test/test_got.py` | `got/run_006_rlm.md` |
| 007 | LLM | 0 | 7.247 | 7.247 | 275 | 38 | 313 | `llm-test/test_llm.py` | `got/run_007_llm.md` |
| 007 | RLM | 0 | 116.849 | 106.258 | 11,914 | 407 | 12,321 | `rlm-test/test_got.py` | `got/run_007_rlm.md` |
| 008 | LLM | 0 | 10.503 | 10.503 | 275 | 33 | 308 | `llm-test/test_llm.py` | `got/run_008_llm.md` |
| 008 | RLM | 0 | 109.263 | 103.557 | 12,387 | 515 | 12,902 | `rlm-test/test_got.py` | `got/run_008_rlm.md` |
| 009 | LLM | 0 | 5.864 | 5.864 | 275 | 44 | 319 | `llm-test/test_llm.py` | `got/run_009_llm.md` |
| 009 | RLM | 0 | 73.804 | 73.478 | 8,762 | 450 | 9,212 | `rlm-test/test_got.py` | `got/run_009_rlm.md` |
| 010 | LLM | 0 | 7.631 | 7.631 | 275 | 36 | 311 | `llm-test/test_llm.py` | `got/run_010_llm.md` |
| 010 | RLM | 0 | 217.703 | 154.300 | 12,198 | 1,036 | 13,234 | `rlm-test/test_got.py` | `got/run_010_rlm.md` |

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
| 006 | LLM | 0 | 30.426 | 30.426 | 1,082 | 190 | 1,272 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_006_llm.md` |
| 006 | RLM | 0 | 316.270 | 256.959 | 14,016 | 1,921 | 15,937 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_006_rlm.md` |
| 007 | LLM | 0 | 25.545 | 25.545 | 1,082 | 192 | 1,274 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_007_llm.md` |
| 007 | RLM | 0 | 91.398 | 52.809 | 13,373 | 129 | 13,502 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_007_rlm.md` |
| 008 | LLM | 0 | 21.342 | 21.342 | 1,082 | 157 | 1,239 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_008_llm.md` |
| 008 | RLM | 0 | 171.021 | 110.262 | 14,000 | 1,087 | 15,087 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_008_rlm.md` |
| 009 | LLM | 0 | 20.940 | 20.940 | 1,082 | 150 | 1,232 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_009_llm.md` |
| 009 | RLM | 0 | 105.034 | 104.956 | 9,285 | 674 | 9,959 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_009_rlm.md` |
| 010 | LLM | 0 | 14.653 | 14.653 | 1,082 | 157 | 1,239 | `llm-test/llm-test for long context problem - same as rlm , just modified for llm` | `authproxy/run_010_llm.md` |
| 010 | RLM | 0 | 131.030 | 88.606 | 13,026 | 1,128 | 14,154 | `rlm-test/test_long_context_authproxy.py` | `authproxy/run_010_rlm.md` |

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
| 006 | LLM | 0 | 173.678 | 173.678 | 1,645 | 1,569 | 3,214 | `llm-test/clinical-llm.py` | `clinical/run_006_llm.md` |
| 006 | RLM | 0 | 52.092 | 50.212 | 10,208 | 196 | 10,404 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_006_rlm.md` |
| 007 | LLM | 0 | 137.055 | 137.055 | 1,645 | 1,582 | 3,227 | `llm-test/clinical-llm.py` | `clinical/run_007_llm.md` |
| 007 | RLM | 0 | 51.368 | 38.129 | 10,459 | 314 | 10,773 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_007_rlm.md` |
| 008 | LLM | 0 | 71.576 | 71.576 | 1,645 | 743 | 2,388 | `llm-test/clinical-llm.py` | `clinical/run_008_llm.md` |
| 008 | RLM | 0 | 84.931 | 55.651 | 11,884 | 661 | 12,545 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_008_rlm.md` |
| 009 | LLM | 0 | 144.718 | 144.718 | 1,645 | 1,519 | 3,164 | `llm-test/clinical-llm.py` | `clinical/run_009_llm.md` |
| 009 | RLM | 0 | 58.383 | 44.139 | 10,644 | 320 | 10,964 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_009_rlm.md` |
| 010 | LLM | 0 | 117.333 | 117.333 | 1,645 | 1,094 | 2,739 | `llm-test/clinical-llm.py` | `clinical/run_010_llm.md` |
| 010 | RLM | 0 | 42.849 | 35.657 | 10,120 | 218 | 10,338 | `rlm-test/test_long_context_clinical_trial.py` | `clinical/run_010_rlm.md` |

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
| 006 | LLM | 0 | 107.300 | 107.300 | 257 | 1,390 | 1,647 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_006_llm.md` |
| 006 | RLM | 0 | 37.833 | 37.447 | 2,590 | 197 | 2,787 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_006_rlm.md` |
| 007 | LLM | 0 | 146.679 | 146.679 | 257 | 1,665 | 1,922 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_007_llm.md` |
| 007 | RLM | 0 | 516.793 | 513.733 | 12,879 | 1,269 | 14,148 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_007_rlm.md` |
| 008 | LLM | 0 | 97.669 | 97.669 | 257 | 949 | 1,206 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_008_llm.md` |
| 008 | RLM | 0 | 276.838 | 244.290 | 12,936 | 2,189 | 15,125 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_008_rlm.md` |
| 009 | LLM | 0 | 127.190 | 127.190 | 257 | 1,489 | 1,746 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_009_llm.md` |
| 009 | RLM | 0 | 129.657 | 123.546 | 12,485 | 942 | 13,427 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_009_rlm.md` |
| 010 | LLM | 0 | 97.483 | 97.483 | 257 | 1,025 | 1,282 | `llm-test/test_launch_note_app.py` | `launch_note_app/run_010_llm.md` |
| 010 | RLM | 0 | 155.597 | 155.469 | 9,372 | 1,268 | 10,640 | `rlm-test/test_launch_note_app.py` | `launch_note_app/run_010_rlm.md` |

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
| 006 | LLM | 0 | 119.110 | 119.110 | 4,096 | 816 | 4,912 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_006_llm.md` |
| 006 | RLM | -9 | - | - | - | - | - | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_006_rlm.md` |
| 007 | LLM | 0 | 64.506 | 64.506 | 4,096 | 603 | 4,699 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_007_llm.md` |
| 007 | RLM | 0 | 291.350 | 246.308 | 22,273 | 1,490 | 23,763 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_007_rlm.md` |
| 008 | LLM | 0 | 94.292 | 94.292 | 4,096 | 613 | 4,709 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_008_llm.md` |
| 008 | RLM | 0 | 203.066 | 189.306 | 21,905 | 1,285 | 23,190 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_008_rlm.md` |
| 009 | LLM | 0 | 75.969 | 75.969 | 4,096 | 426 | 4,522 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_009_llm.md` |
| 009 | RLM | 0 | 42.854 | 42.830 | 2,897 | 158 | 3,055 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_009_rlm.md` |
| 010 | LLM | 0 | 94.925 | 94.925 | 4,096 | 662 | 4,758 | `llm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_010_llm.md` |
| 010 | RLM | 0 | 206.664 | 159.939 | 21,814 | 917 | 22,731 | `rlm-test/test_pdf_cersei_warning.py` | `pdf_cersei_warning/run_010_rlm.md` |

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
| 006 | LLM | 0 | 73.841 | 73.841 | 209 | 881 | 1,090 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_006_llm.md` |
| 006 | RLM | 0 | 578.646 | 578.483 | 18,593 | 5,985 | 24,578 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_006_rlm.md` |
| 007 | LLM | 0 | 105.367 | 105.367 | 209 | 1,277 | 1,486 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_007_llm.md` |
| 007 | RLM | 0 | 604.700 | 249.397 | 23,194 | 2,225 | 25,419 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_007_rlm.md` |
| 008 | LLM | 0 | 103.650 | 103.650 | 209 | 1,026 | 1,235 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_008_llm.md` |
| 008 | RLM | 0 | 492.472 | 474.990 | 23,723 | 4,637 | 28,360 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_008_rlm.md` |
| 009 | LLM | 0 | 106.855 | 106.855 | 209 | 1,380 | 1,589 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_009_llm.md` |
| 009 | RLM | 0 | 425.986 | 425.691 | 19,388 | 4,053 | 23,441 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_009_rlm.md` |
| 010 | LLM | 0 | 93.224 | 93.224 | 209 | 1,175 | 1,384 | `llm-test/test_tsp_llm_only.py` | `tsp_branch_bound/run_010_llm.md` |
| 010 | RLM | 0 | 490.722 | 490.673 | 16,415 | 4,369 | 20,784 | `rlm-test/test_tsp_branch_bound.py` | `tsp_branch_bound/run_010_rlm.md` |

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
| 006 | LLM | 0 | 96.515 | 96.515 | 318 | 1,191 | 1,509 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_006_llm.md` |
| 006 | RLM | 0 | 873.264 | 819.806 | 21,953 | 5,586 | 27,539 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_006_rlm.md` |
| 007 | LLM | 0 | 59.780 | 59.780 | 318 | 858 | 1,176 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_007_llm.md` |
| 007 | RLM | 0 | 152.822 | 152.617 | 12,985 | 1,484 | 14,469 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_007_rlm.md` |
| 008 | LLM | 0 | 63.006 | 63.006 | 318 | 1,213 | 1,531 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_008_llm.md` |
| 008 | RLM | 0 | 483.570 | 451.265 | 24,592 | 4,634 | 29,226 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_008_rlm.md` |
| 009 | LLM | 0 | 124.153 | 124.153 | 318 | 1,655 | 1,973 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_009_llm.md` |
| 009 | RLM | 0 | 292.076 | 291.926 | 16,586 | 2,583 | 19,169 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_009_rlm.md` |
| 010 | LLM | 0 | 72.327 | 72.327 | 318 | 971 | 1,289 | `llm-test/test_stochastic_tsp_adaptive_llm_only.py` | `stochastic_tsp/run_010_llm.md` |
| 010 | RLM | 0 | 209.424 | 209.153 | 9,175 | 2,131 | 11,306 | `rlm-test/test_stochastic_tsp_adaptive.py` | `stochastic_tsp/run_010_rlm.md` |
