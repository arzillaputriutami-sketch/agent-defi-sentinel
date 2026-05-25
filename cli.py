#!/usr/bin/env python3
"""Command-line operator console for DeFi Sentinel Swarm."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from backend.swarm import SCENARIOS, analyze_scenario, batch_analyze


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="DeFi Sentinel Swarm operator console")
    parser.add_argument("--scenario", choices=SCENARIOS, help="Scenario to analyze")
    parser.add_argument("--signals", type=Path, help="JSON file with optional scenario/signals override")
    parser.add_argument("--all", action="store_true", help="Run all built-in scenarios")
    parser.add_argument("--format", choices=("json", "markdown"), default="json", help="Output format")
    return parser


def load_signal_file(path: Path) -> tuple[str | None, dict[str, float]]:
    payload = json.loads(path.read_text())
    scenario = payload.get("scenario")
    signals = payload.get("signals", {})
    if not isinstance(signals, dict):
        raise SystemExit("signals must be an object of numeric values")
    return scenario, {str(k): float(v) for k, v in signals.items()}


def report_to_markdown(report: dict[str, Any]) -> str:
    findings = "\n".join(
        f"- **{f['agent']}** [{f['severity']} / {f['confidence']:.2f}] — {f['observation']} {f['recommendation']}"
        for f in report["findings"]
    )
    actions = "\n".join(f"{i + 1}. {action}" for i, action in enumerate(report["next_actions"]))
    return f"""# {report['project']} — {report['scenario']}

- Risk score: **{report['risk_score']}/100**
- Confidence: **{report['confidence']:.2f}**
- Verdict: **{report['verdict']}**
- Trace: `{report['trace_id']}`

## Agent findings
{findings}

## Next actions
{actions}
"""


def run(argv: list[str] | None = None) -> str:
    args = build_parser().parse_args(argv)
    scenario = args.scenario
    signals: dict[str, float] = {}
    if args.signals:
        file_scenario, signals = load_signal_file(args.signals)
        scenario = scenario or file_scenario
    payload: Any = batch_analyze() if args.all else analyze_scenario(scenario, signals).to_dict()
    if args.format == "markdown":
        if isinstance(payload, list):
            return "\n\n---\n\n".join(report_to_markdown(item) for item in payload)
        return report_to_markdown(payload)
    return json.dumps(payload, indent=2)


if __name__ == "__main__":
    print(run())
