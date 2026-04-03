import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(frozen=True)
class PairSpec:
    name: str
    llm_script: str
    rlm_script: str


PAIR_SPECS = [
    PairSpec("got", "llm-test/test_llm.py", "rlm-test/test_got.py"),
    PairSpec(
        "authproxy",
        "llm-test/llm-test for long context problem - same as rlm , just modified for llm",
        "rlm-test/test_long_context_authproxy.py",
    ),
    PairSpec(
        "clinical",
        "llm-test/clinical-llm.py",
        "rlm-test/test_long_context_clinical_trial.py",
    ),
    PairSpec(
        "launch_note_app",
        "llm-test/test_launch_note_app.py",
        "rlm-test/test_launch_note_app.py",
    ),
    PairSpec(
        "pdf_cersei_warning",
        "llm-test/test_pdf_cersei_warning.py",
        "rlm-test/test_pdf_cersei_warning.py",
    ),
    PairSpec(
        "tsp_branch_bound",
        "llm-test/test_tsp_llm_only.py",
        "rlm-test/test_tsp_branch_bound.py",
    ),
    PairSpec(
        "stochastic_tsp",
        "llm-test/test_stochastic_tsp_adaptive_llm_only.py",
        "rlm-test/test_stochastic_tsp_adaptive.py",
    ),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run paired LLM/RLM benchmark scripts repeatedly and save markdown logs."
    )
    parser.add_argument(
        "--pairs",
        nargs="*",
        default=["all"],
        help="Pair names to run. Use 'all' to run every pair.",
    )
    parser.add_argument(
        "--runs",
        type=int,
        default=1,
        help="Number of repeated runs per pair.",
    )
    parser.add_argument(
        "--output-dir",
        default="benchmark_runs",
        help="Base directory for markdown logs.",
    )
    parser.add_argument(
        "--backend",
        default="ollama",
        choices=["vllm", "gemini", "ollama"],
        help="Backend passed through to the benchmark scripts.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Model name passed through as BENCHMARK_MODEL_NAME.",
    )
    parser.add_argument(
        "--vllm-base-url",
        default="http://127.0.0.1:8000/v1",
        help="vLLM OpenAI-compatible base URL.",
    )
    parser.add_argument(
        "--vllm-api-key",
        default="EMPTY",
        help="API key passed to vLLM-compatible OpenAI clients.",
    )
    parser.add_argument(
        "--ollama-base-url",
        default="http://127.0.0.1:11434/v1",
        help="Ollama OpenAI-compatible base URL.",
    )
    parser.add_argument(
        "--ollama-api-key",
        default="ollama",
        help="API key passed to Ollama OpenAI-compatible clients.",
    )
    parser.add_argument(
        "--cooldown-seconds",
        type=int,
        default=0,
        help="Cooldown between script calls.",
    )
    parser.add_argument(
        "--stop-on-error",
        action="store_true",
        help="Stop the suite immediately if any script exits non-zero.",
    )
    return parser.parse_args()


def sanitize_fragment(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-")


def selected_pairs(pair_names: list[str]) -> list[PairSpec]:
    if "all" in pair_names:
        return PAIR_SPECS
    selected = []
    wanted = set(pair_names)
    for pair in PAIR_SPECS:
        if pair.name in wanted:
            selected.append(pair)
    missing = wanted - {pair.name for pair in selected}
    if missing:
        raise ValueError(f"Unknown pair names: {sorted(missing)}")
    return selected


def run_script(repo_root: Path, script_relpath: str, env: dict[str, str]) -> tuple[int, str]:
    result = subprocess.run(
        [sys.executable, str(repo_root / script_relpath)],
        cwd=repo_root,
        env=env,
        text=True,
        capture_output=True,
    )
    combined_output = result.stdout
    if result.stderr:
        combined_output += "\n[stderr]\n" + result.stderr
    return result.returncode, combined_output


def write_markdown_log(
    output_path: Path,
    *,
    pair_name: str,
    role: str,
    run_index: int,
    script_relpath: str,
    exit_code: int,
    output: str,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "\n".join(
            [
                f"# {pair_name} - {role.upper()} run {run_index:03d}",
                "",
                f"- Script: `{script_relpath}`",
                f"- Exit code: `{exit_code}`",
                "",
                "## Terminal Output",
                "",
                "```text",
                output.rstrip(),
                "```",
                "",
            ]
        )
    )


def write_summary(output_dir: Path, rows: list[dict[str, str]]) -> None:
    lines = [
        "# Benchmark Run Summary",
        "",
        "| Pair | Run | LLM Exit | RLM Exit | LLM Log | RLM Log |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['pair']} | {row['run']} | {row['llm_exit']} | {row['rlm_exit']} | "
            f"[llm]({row['llm_log']}) | [rlm]({row['rlm_log']}) |"
        )
    output_dir.joinpath("SUMMARY.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent
    pairs = selected_pairs(args.pairs)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    model_fragment = sanitize_fragment(args.model or "default-model")
    run_root = (
        repo_root
        / args.output_dir
        / f"{stamp}-{args.backend}-{model_fragment}"
    )
    run_root.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    env["BENCHMARK_BACKEND"] = args.backend
    env["BENCHMARK_COOLDOWN_SECONDS"] = str(args.cooldown_seconds)
    if args.model:
        env["BENCHMARK_MODEL_NAME"] = args.model
    if args.backend == "vllm":
        env["VLLM_BASE_URL"] = args.vllm_base_url
        env["VLLM_API_KEY"] = args.vllm_api_key
    if args.backend == "ollama":
        env["OLLAMA_BASE_URL"] = args.ollama_base_url
        env["OLLAMA_API_KEY"] = args.ollama_api_key

    summary_rows: list[dict[str, str]] = []

    for pair in pairs:
        for run_index in range(1, args.runs + 1):
            pair_dir = run_root / pair.name
            llm_log = pair_dir / f"run_{run_index:03d}_llm.md"
            rlm_log = pair_dir / f"run_{run_index:03d}_rlm.md"

            print(f"[{pair.name}] run {run_index:03d} - LLM")
            llm_exit, llm_output = run_script(repo_root, pair.llm_script, env)
            write_markdown_log(
                llm_log,
                pair_name=pair.name,
                role="llm",
                run_index=run_index,
                script_relpath=pair.llm_script,
                exit_code=llm_exit,
                output=llm_output,
            )

            print(f"[{pair.name}] run {run_index:03d} - RLM")
            rlm_exit, rlm_output = run_script(repo_root, pair.rlm_script, env)
            write_markdown_log(
                rlm_log,
                pair_name=pair.name,
                role="rlm",
                run_index=run_index,
                script_relpath=pair.rlm_script,
                exit_code=rlm_exit,
                output=rlm_output,
            )

            summary_rows.append(
                {
                    "pair": pair.name,
                    "run": f"{run_index:03d}",
                    "llm_exit": str(llm_exit),
                    "rlm_exit": str(rlm_exit),
                    "llm_log": str(llm_log.relative_to(run_root)),
                    "rlm_log": str(rlm_log.relative_to(run_root)),
                }
            )

            if args.stop_on_error and (llm_exit != 0 or rlm_exit != 0):
                write_summary(run_root, summary_rows)
                raise SystemExit(
                    f"Stopping on error: {pair.name} run {run_index:03d} "
                    f"(llm_exit={llm_exit}, rlm_exit={rlm_exit})"
                )

    write_summary(run_root, summary_rows)
    print(f"Saved benchmark logs to {run_root}")


if __name__ == "__main__":
    main()
