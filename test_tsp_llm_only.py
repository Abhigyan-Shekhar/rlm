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

prompt = """You are solving a Traveling Salesman Problem with 8 cities.

Cities: A, B, C, D, E, F, G, H

Distance matrix is symmetric and satisfies triangle inequality.

Task:
- Find the optimal tour
- You MUST use a branch-and-bound or systematic search strategy

Solve the Traveling Salesman Problem below.

IMPORTANT:
You must NOT compute all permutations directly.
Instead:
- Use logical reasoning to eliminate impossible or suboptimal paths early
- Justify every pruning decision

STRICT REQUIREMENTS:
- Maintain a table of explored paths
- Track current best solution (upper bound)
- Prune paths that exceed current best
- Show recursive exploration clearly

After giving the answer, explain:
"Why is this solution guaranteed optimal?"

Output format:
1. Exploration steps
2. Pruned branches with reasons
3. Final optimal path and cost
"""

expected_result = (
    "The problem is under-specified. No optimal tour can be determined because "
    "the actual distance matrix values are missing."
)

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
print("EXPECTED CORRECT RESULT")
print("=" * 70)
print(expected_result)

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
