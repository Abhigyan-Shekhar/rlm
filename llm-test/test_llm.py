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
The Battle of the Bastards was fought between Jon Snow and Ramsay Bolton for control
of Winterfell. Jon's army included the Free Folk led by Tormund Giantsbane, soldiers
from House Mormont, and the giant Wun Wun. Before the battle, Sansa Stark warned Jon
that Ramsay would manipulate him, but Jon ignored her. Sansa secretly sent a raven to
Petyr Baelish requesting the Knights of the Vale.

During battle, Ramsay killed Rickon Stark, causing Jon to abandon his battle plan and
charge alone. The Bolton shield wall encircled Jon's forces. Tormund fought ferociously
and Wun Wun smashed through soldiers, but defeat was imminent.

At the last moment, the Knights of the Vale arrived — called by Sansa Stark. The Vale
cavalry routed the Boltons. Without Sansa's decision to contact Littlefinger, Jon's
entire army would have been massacred. Her action was the single most decisive factor.
"""

question = "Who was the central ally of the main character in the Battle of the Bastards?"

prompt = f"""{context}

QUESTION: {question}
Identify the main character and their most decisive ally. Give a short answer.
"""

backend_config = load_benchmark_backend(
    default_gemini_model="gemini-2.5-flash-lite",
    default_vllm_model="Qwen/Qwen2.5-7B-Instruct",
)

wait_for_benchmark_cooldown(backend_config)

client = get_benchmark_client(backend_config)

start = time.perf_counter()
response = client.completion(prompt)
end = time.perf_counter()

print("\n" + "=" * 70)
print("ANSWER")
print("=" * 70)
print(f"Backend: {backend_config.backend}")
print(f"Model:   {backend_config.model_name}")
print(response)

print("\n" + "=" * 70)
print("LATENCY")
print("=" * 70)
print(f"  Total time:        {end - start:.3f}s")

print("\n" + "=" * 70)
print("TOKEN USAGE")
print("=" * 70)
print_client_usage(client)
print("=" * 70)
