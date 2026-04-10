# authproxy - LLM run 001

- Script: `llm-test/llm-test for long context problem - same as rlm , just modified for llm`
- Exit code: `0`

## Terminal Output

```text
No cooldown configured for this backend.

======================================================================
ANSWER
======================================================================
Backend: openai
Model:   qwen2.5:14b
Q1 [Single-hop retrieval]:
7

Q2 [Distractor robustness]:
7

Q3 [Misleading fact resistance]:
7

Q4 [Span extraction]:
This is the active production configuration as of 2025-01-09. It handles all inbound authentication requests for the main application cluster.

Q5 [Multi-hop reasoning]:
Since FAILOVER_ENABLED = false, if AuthProxy-Primary fails, there is no automatic failover to another instance based on the given information in the document.

======================================================================
LATENCY BREAKDOWN
======================================================================
  Total wall time:    53.955s

======================================================================
TOKEN USAGE
======================================================================
qwen2.5:14b: input=1,082, output=110, calls=1
======================================================================
```
