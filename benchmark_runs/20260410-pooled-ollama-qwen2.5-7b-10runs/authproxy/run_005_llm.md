# authproxy - LLM run 005

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
If AuthProxy-Primary fails, since the `FAILOVER_ENABLED` value is `false`, there will be no failover to another ServiceConfig instance. This means that inbound authentication requests for the main application cluster will not automatically transition to another configuration and may experience service disruptions until the issue with AuthProxy-Primary is resolved.

======================================================================
LATENCY BREAKDOWN
======================================================================
  Total wall time:    23.109s

======================================================================
TOKEN USAGE
======================================================================
qwen2.5:7b: input=1,082, output=187, calls=1
======================================================================
```
