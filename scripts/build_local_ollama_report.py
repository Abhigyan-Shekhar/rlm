from __future__ import annotations

import csv
import re
import statistics
from dataclasses import dataclass
from pathlib import Path


BATCH_DIR = Path(
    "/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260403-121151-ollama-qwen2.5-7b"
)
ROOT_DIR = Path("/Users/abhigyanshekhar/Desktop/RLM-FULL")
ROOT_REPORT = ROOT_DIR / "RLM_Setup_And_Test_Guide.md"
ROOT_PDF = ROOT_DIR / "RLM_Setup_And_Test_Guide.pdf"
BATCH_REPORT = BATCH_DIR / "REPORT.md"
RAW_CSV = BATCH_DIR / "raw_data.csv"
AGG_CSV = BATCH_DIR / "aggregate_metrics.csv"


PAIR_ORDER = [
    "got",
    "authproxy",
    "clinical",
    "launch_note_app",
    "pdf_cersei_warning",
    "tsp_branch_bound",
    "stochastic_tsp",
]

PAIR_LABELS = {
    "got": "Battle of the Bastards",
    "authproxy": "AuthProxy Long Context",
    "clinical": "Clinical Long Context",
    "launch_note_app": "Launch Note App",
    "pdf_cersei_warning": "PDF Cersei Warning",
    "tsp_branch_bound": "Under-specified TSP",
    "stochastic_tsp": "Stochastic Adaptive TSP",
}


@dataclass
class RunRow:
    pair: str
    run: int
    mode: str
    exit_code: int
    wall_s: float | None
    exec_s: float | None
    input_tokens: int | None
    output_tokens: int | None
    total_tokens: int | None
    script: str
    path: Path


def parse_run_file(path: Path) -> RunRow:
    text = path.read_text()
    pair = path.parent.name
    run = int(re.search(r"run_(\d+)_", path.name).group(1))
    mode = "llm" if path.name.endswith("_llm.md") else "rlm"
    exit_code = int(re.search(r"- Exit code: `([^`]+)`", text).group(1))
    script = re.search(r"- Script: `([^`]+)`", text).group(1)

    wall_s = None
    exec_s = None
    input_tokens = None
    output_tokens = None
    total_tokens = None

    if mode == "llm":
        wall_match = re.search(
            r"(?:Baseline wall time|Total wall time|Total time):\s*([0-9.]+)s",
            text,
        )
        if wall_match:
            wall_s = float(wall_match.group(1))
            exec_s = wall_s

        token_match = re.search(
            r"qwen2\.5:7b: input=([0-9,]+), output=([0-9,]+), calls=(\d+)",
            text,
        )
        if token_match:
            input_tokens = int(token_match.group(1).replace(",", ""))
            output_tokens = int(token_match.group(2).replace(",", ""))
            total_tokens = input_tokens + output_tokens
    else:
        wall_match = re.search(r"Total wall time:\s*([0-9.]+)s", text)
        exec_match = re.search(r"RLM execution time:\s*([0-9.]+)s", text)
        token_match = re.search(
            r"Input tokens:\s*([0-9,]+)\s*\n\s*Output tokens:\s*([0-9,]+)\s*\n\s*Total tokens:\s*([0-9,]+)",
            text,
        )
        if wall_match:
            wall_s = float(wall_match.group(1))
        if exec_match:
            exec_s = float(exec_match.group(1))
        if token_match:
            input_tokens = int(token_match.group(1).replace(",", ""))
            output_tokens = int(token_match.group(2).replace(",", ""))
            total_tokens = int(token_match.group(3).replace(",", ""))

    return RunRow(
        pair=pair,
        run=run,
        mode=mode,
        exit_code=exit_code,
        wall_s=wall_s,
        exec_s=exec_s,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
        script=script,
        path=path,
    )


def parse_rows() -> list[RunRow]:
    rows: list[RunRow] = []
    for pair in PAIR_ORDER:
        pair_dir = BATCH_DIR / pair
        for path in sorted(pair_dir.glob("run_*_*.md")):
            rows.append(parse_run_file(path))
    return rows


def fmt_float(value: float | None) -> str:
    if value is None:
        return "-"
    return f"{value:.3f}"


def fmt_int(value: int | None) -> str:
    if value is None:
        return "-"
    return f"{value:,}"


def bar(value: float, max_value: float, width: int = 24) -> str:
    if max_value <= 0:
        return ""
    filled = max(1, round((value / max_value) * width)) if value > 0 else 0
    return "#" * filled


def build_aggregates(rows: list[RunRow]) -> list[dict[str, str | int | float]]:
    aggregates: list[dict[str, str | int | float]] = []
    for pair in PAIR_ORDER:
        for mode in ("llm", "rlm"):
            subset = [r for r in rows if r.pair == pair and r.mode == mode]
            successful = [
                r
                for r in subset
                if r.exit_code == 0 and r.wall_s is not None and r.total_tokens is not None
            ]
            wall_values = [r.wall_s for r in successful if r.wall_s is not None]
            token_values = [r.total_tokens for r in successful if r.total_tokens is not None]
            input_values = [r.input_tokens for r in successful if r.input_tokens is not None]
            output_values = [r.output_tokens for r in successful if r.output_tokens is not None]
            aggregates.append(
                {
                    "pair": pair,
                    "label": PAIR_LABELS[pair],
                    "mode": mode.upper(),
                    "runs": len(subset),
                    "successes": len(successful),
                    "success_rate": (len(successful) / len(subset)) * 100 if subset else 0.0,
                    "avg_wall_s": statistics.mean(wall_values) if wall_values else None,
                    "median_wall_s": statistics.median(wall_values) if wall_values else None,
                    "avg_total_tokens": statistics.mean(token_values) if token_values else None,
                    "avg_input_tokens": statistics.mean(input_values) if input_values else None,
                    "avg_output_tokens": statistics.mean(output_values) if output_values else None,
                }
            )
    return aggregates


def write_csv(rows: list[RunRow], aggregates: list[dict[str, str | int | float]]) -> None:
    with RAW_CSV.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "pair",
                "label",
                "run",
                "mode",
                "exit_code",
                "wall_s",
                "exec_s",
                "input_tokens",
                "output_tokens",
                "total_tokens",
                "script",
                "path",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row.pair,
                    PAIR_LABELS[row.pair],
                    row.run,
                    row.mode.upper(),
                    row.exit_code,
                    row.wall_s if row.wall_s is not None else "",
                    row.exec_s if row.exec_s is not None else "",
                    row.input_tokens if row.input_tokens is not None else "",
                    row.output_tokens if row.output_tokens is not None else "",
                    row.total_tokens if row.total_tokens is not None else "",
                    row.script,
                    row.path.relative_to(BATCH_DIR),
                ]
            )

    with AGG_CSV.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "pair",
                "label",
                "mode",
                "runs",
                "successes",
                "success_rate",
                "avg_wall_s",
                "median_wall_s",
                "avg_total_tokens",
                "avg_input_tokens",
                "avg_output_tokens",
            ]
        )
        for row in aggregates:
            writer.writerow(
                [
                    row["pair"],
                    row["label"],
                    row["mode"],
                    row["runs"],
                    row["successes"],
                    f'{row["success_rate"]:.1f}',
                    fmt_float(row["avg_wall_s"]),
                    fmt_float(row["median_wall_s"]),
                    fmt_float(row["avg_total_tokens"]),
                    fmt_float(row["avg_input_tokens"]),
                    fmt_float(row["avg_output_tokens"]),
                ]
            )


def build_markdown(rows: list[RunRow], aggregates: list[dict[str, str | int | float]]) -> str:
    max_wall = max(
        row["avg_wall_s"] for row in aggregates if isinstance(row["avg_wall_s"], float)
    )
    max_tokens = max(
        row["avg_total_tokens"]
        for row in aggregates
        if isinstance(row["avg_total_tokens"], float)
    )

    lines: list[str] = []
    lines.append("# RLM Local Ollama Benchmark Guide And Results")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append(
        "This document covers only the local Ollama benchmark batch completed on `qwen2.5:7b`. It does not use or summarize any earlier Gemini runs."
    )
    lines.append("")
    lines.append("## Environment")
    lines.append("")
    lines.append("- Workspace: `/Users/abhigyanshekhar/Desktop/RLM-FULL`")
    lines.append("- Backend: `ollama` through the OpenAI-compatible local endpoint")
    lines.append("- Model: `qwen2.5:7b`")
    lines.append("- Batch folder: `/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260403-121151-ollama-qwen2.5-7b`")
    lines.append("- Run plan: `5` paired `LLM` / `RLM` runs for each benchmark")
    lines.append("")
    lines.append("## Setup")
    lines.append("")
    lines.append("```bash")
    lines.append("cd /Users/abhigyanshekhar/Desktop/RLM-FULL")
    lines.append("source .venv/bin/activate")
    lines.append("uv pip install -e .")
    lines.append("open -a Ollama")
    lines.append("/Applications/Ollama.app/Contents/Resources/ollama pull qwen2.5:7b")
    lines.append("export BENCHMARK_BACKEND=ollama")
    lines.append("export OLLAMA_BASE_URL=http://127.0.0.1:11434/v1")
    lines.append("export OLLAMA_MODEL_NAME=qwen2.5:7b")
    lines.append("export OLLAMA_API_KEY=ollama")
    lines.append("export BENCHMARK_COOLDOWN_SECONDS=0")
    lines.append("```")
    lines.append("")
    lines.append("## How The Run Artifacts Are Organized")
    lines.append("")
    lines.append(
        "The completed batch is already organized one folder per test. Each test folder contains the five `LLM` logs and five `RLM` logs as markdown files."
    )
    lines.append("")
    lines.append("Example layout:")
    lines.append("")
    lines.append("```text")
    lines.append("benchmark_runs/20260403-121151-ollama-qwen2.5-7b/")
    for pair in PAIR_ORDER:
        lines.append(f"  {pair}/")
        lines.append("    run_001_llm.md")
        lines.append("    run_001_rlm.md")
        lines.append("    ...")
    lines.append("  SUMMARY.md")
    lines.append("  aggregate_metrics.csv")
    lines.append("  raw_data.csv")
    lines.append("```")
    lines.append("")
    lines.append("## Commands Used")
    lines.append("")
    lines.append("Single pair example:")
    lines.append("")
    lines.append("```bash")
    lines.append(".venv/bin/python llm-test/test_tsp_llm_only.py")
    lines.append(".venv/bin/python rlm-test/test_tsp_branch_bound.py")
    lines.append("```")
    lines.append("")
    lines.append("Full paired batch:")
    lines.append("")
    lines.append("```bash")
    lines.append(".venv/bin/python run_benchmark_pairs.py --backend ollama --model qwen2.5:7b --runs 5")
    lines.append("```")
    lines.append("")
    lines.append("## Aggregate Results")
    lines.append("")
    lines.append("| Benchmark | Mode | Success | Avg Wall (s) | Median Wall (s) | Avg Input Tokens | Avg Output Tokens | Avg Total Tokens |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for row in aggregates:
        lines.append(
            f'| {row["label"]} | {row["mode"]} | {row["successes"]}/{row["runs"]} ({row["success_rate"]:.0f}%) | '
            f'{fmt_float(row["avg_wall_s"])} | {fmt_float(row["median_wall_s"])} | '
            f'{fmt_float(row["avg_input_tokens"])} | {fmt_float(row["avg_output_tokens"])} | {fmt_float(row["avg_total_tokens"])} |'
        )
    lines.append("")
    lines.append("## Wall Time Graph")
    lines.append("")
    lines.append("| Benchmark | Mode | Avg Wall (s) | Relative Bar |")
    lines.append("| --- | --- | --- | --- |")
    for row in aggregates:
        if row["avg_wall_s"] is None:
            continue
        lines.append(
            f'| {row["label"]} | {row["mode"]} | {fmt_float(row["avg_wall_s"])} | {bar(row["avg_wall_s"], max_wall)} |'
        )
    lines.append("")
    lines.append("## Token Usage Graph")
    lines.append("")
    lines.append("| Benchmark | Mode | Avg Total Tokens | Relative Bar |")
    lines.append("| --- | --- | --- | --- |")
    for row in aggregates:
        if row["avg_total_tokens"] is None:
            continue
        lines.append(
            f'| {row["label"]} | {row["mode"]} | {fmt_float(row["avg_total_tokens"])} | {bar(row["avg_total_tokens"], max_tokens)} |'
        )
    lines.append("")
    lines.append("## Raw Data Notes")
    lines.append("")
    lines.append(
        "- All values below come from the markdown logs inside the completed local batch folder."
    )
    lines.append(
        "- `stochastic_tsp` run `004` on the `RLM` side exited with `-9`, so it is included in the raw table but excluded from aggregate averages."
    )
    lines.append("")
    lines.append("## Raw Data Table")
    lines.append("")
    lines.append("| Benchmark | Run | Mode | Exit | Wall (s) | Exec (s) | Input | Output | Total | Log |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for row in rows:
        lines.append(
            f"| {PAIR_LABELS[row.pair]} | {row.run:03d} | {row.mode.upper()} | {row.exit_code} | "
            f"{fmt_float(row.wall_s)} | {fmt_float(row.exec_s)} | {fmt_int(row.input_tokens)} | "
            f"{fmt_int(row.output_tokens)} | {fmt_int(row.total_tokens)} | "
            f"`{row.path.relative_to(BATCH_DIR)}` |"
        )
    lines.append("")
    lines.append("## Output Files")
    lines.append("")
    lines.append(
        f"- Raw CSV: [`raw_data.csv`]({RAW_CSV})"
    )
    lines.append(
        f"- Aggregate CSV: [`aggregate_metrics.csv`]({AGG_CSV})"
    )
    lines.append(
        f"- Batch summary: [`SUMMARY.md`]({BATCH_DIR / 'SUMMARY.md'})"
    )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    rows = parse_rows()
    aggregates = build_aggregates(rows)
    write_csv(rows, aggregates)
    report = build_markdown(rows, aggregates)
    BATCH_REPORT.write_text(report)
    ROOT_REPORT.write_text(report)


if __name__ == "__main__":
    main()
