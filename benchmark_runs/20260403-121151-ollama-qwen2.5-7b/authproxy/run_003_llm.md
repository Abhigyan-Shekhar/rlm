# authproxy - LLM run 003

- Script: `llm-test/llm-test for long context problem - same as rlm , just modified for llm`
- Exit code: `0`

## Terminal Output

```text
No cooldown configured for this backend.

======================================================================
ANSWER
======================================================================
Backend: openai
Model:   qwen2.5:7b
Q1 [Single-hop retrieval]:
7

Q2 [Distractor robustness]:
7

Q3 [Misleading fact resistance]:
7

Q4 [Span extraction]:
ServiceConfig instance "AuthProxy-Primary" has the following parameters:
  - MAX_RETRY_LIMIT = 7
  - TIMEOUT_MS = 8000
  - FAILOVER_ENABLED = false
This is the active production configuration as of 2025-01-09. It handles all inbound authentication requests for the main application cluster.

Q5 [Multi-hop reasoning]:
If AuthProxy-Primary fails, no failover occurs because the FAILOVER_ENABLED value for AuthProxy-Primary is set to false.

======================================================================
LATENCY BREAKDOWN
======================================================================
  Total wall time:    20.201s

======================================================================
TOKEN USAGE
======================================================================
qwen2.5:7b: input=1,082, output=149, calls=1
======================================================================
```
