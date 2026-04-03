import sys
import time
from pathlib import Path

from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark_backend import (
    build_messages,
    get_benchmark_client,
    load_benchmark_backend,
    print_client_usage,
    wait_for_benchmark_cooldown,
)

load_dotenv()

context = """
Goal: Launch a new AI-powered note-taking app in 30 days.

Constraints:
- Budget: $10,000
- Team: 3 engineers, 1 designer
- Target users: college students

Tasks:
1. Break this goal into a detailed execution plan
2. Decompose into weekly milestones
3. Further break each milestone into actionable tasks
4. Identify dependencies between tasks
5. Suggest tools/technologies for each step
6. Highlight risks and mitigation strategies
"""

question = """
Create a launch plan for the app.

Instructions:
- Use hierarchical decomposition (goal -> milestones -> tasks)
- Clearly show dependencies
- Optimize for speed and feasibility
"""

prompt = f"""{context}

QUESTION: {question}
Use the provided planning context directly.
Return a structured plan with:
- goal
- weekly milestones
- actionable tasks under each milestone
- dependencies
- recommended tools/technologies
- risks and mitigations
Do NOT use llm_query. Analyze the context variable directly with Python code.
"""

system_instruction = (
    "You are a helpful planning assistant. "
    "Always respond in plain text only. "
    "Do NOT use JSON, markdown code blocks, or any structured data format. "
    "Use plain prose, bullet points, and numbered lists where appropriate."
)

backend_config = load_benchmark_backend(
    default_gemini_model="gemini-2.5-flash-lite",
    default_vllm_model="Qwen/Qwen2.5-7B-Instruct",
)

wait_for_benchmark_cooldown(backend_config)

client = get_benchmark_client(backend_config)

wall_start = time.perf_counter()
response = client.completion(build_messages(prompt, system_instruction))
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
