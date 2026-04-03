import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark_backend import (
    get_benchmark_client,
    load_benchmark_backend,
    print_client_usage,
    wait_for_benchmark_cooldown,
)

load_dotenv()

text_path = os.path.abspath("e72f9f1f181a66887baa7270037c582e.txt")

with open(text_path, encoding="utf-8") as f:
    context = f.read()

prompt = f"""There is a brief moment where Cersei says something to Ned that, read carefully, is actually a veiled warning to leave King's Landing. Find it.

STRICT INSTRUCTIONS:
- Search ONLY within the provided text context for the answer.
- If you cannot find this exact moment in the context, reply with exactly: CONTEXT NOT ENOUGH
- Do NOT use any knowledge from outside the context.
- Do NOT guess, infer from memory, or fill gaps with what you think is true.
- Return only the exact quotation as it appears in the context.

TEXT CONTEXT:
{context}
"""

backend_config = load_benchmark_backend(
    default_gemini_model="gemini-2.5-flash-lite",
    default_vllm_model="Qwen/Qwen2.5-7B-Instruct",
)

wait_for_benchmark_cooldown(backend_config)

client = get_benchmark_client(backend_config)

wall_start = time.perf_counter()
response = client.completion(prompt)
wall_end = time.perf_counter()

print("\n" + "=" * 70)
print("ANSWER")
print("=" * 70)
print(f"Backend: {backend_config.backend}")
print(f"Model:   {backend_config.model_name}")
print(response)

print("\n" + "=" * 70)
print("LATENCY BREAKDOWN")
print("=" * 70)
print(f"  Total wall time:    {wall_end - wall_start:.3f}s")

print("\n" + "=" * 70)
print("TOKEN USAGE")
print("=" * 70)
print_client_usage(client)
print("=" * 70)
