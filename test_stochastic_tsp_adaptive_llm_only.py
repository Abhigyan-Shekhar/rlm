import os
import time

from dotenv import load_dotenv

from benchmark_backend import (
    get_benchmark_client,
    load_benchmark_backend,
    print_client_usage,
    wait_for_benchmark_cooldown,
)

load_dotenv()

prompt = """You are a salesman at city A. Cities are A, B, C, D, E. You must visit all cities and return to A.
Edge costs are stochastic — each edge has a base cost, but when you arrive at a city, you roll a private die and learn a local multiplier that applies to all edges leaving that city. This multiplier is unknown until you arrive.
Base edge costs (bidirectional):
EdgeBase CostA↔B4A↔C6A↔D5A↔E8B↔C3B↔D7B↔E2C↔D4C↔E5D↔E3
Multiplier distribution at each city (independent):

With probability 0.5 → multiplier = 0.5 (lucky city)
With probability 0.5 → multiplier = 2.0 (unlucky city)

The actual cost of traveling from city X to city Y = (X's multiplier) × (base cost of X↔Y)
You learn city X's multiplier only when you arrive at X, before deciding where to go next.
You start at A and immediately learn A's multiplier before your first move.
Question:
Derive the optimal adaptive policy — a complete decision tree of the form "at city X, having visited set S, with multiplier m, go to city Y" — that minimizes expected total cost. Then compute the exact expected cost of this optimal policy.
"""

backend_config = load_benchmark_backend(
    default_gemini_model="gemini-2.5-flash",
    default_vllm_model="Qwen/Qwen2.5-7B-Instruct",
)

wait_for_benchmark_cooldown(backend_config)

print("\n" + "=" * 70)
print("PROMPT")
print("=" * 70)
print(prompt)

print("\n" + "=" * 70)
print("BASELINE LLM")
print("=" * 70)
print(f"Backend: {backend_config.backend}")
print(f"Model:   {backend_config.model_name}")

client = get_benchmark_client(backend_config)
wall_start = time.perf_counter()
response = client.completion(prompt)
wall_end = time.perf_counter()

print(response)
print("\n" + "-" * 40)
print(f"Baseline wall time: {wall_end - wall_start:.3f}s")
print_client_usage(client)
