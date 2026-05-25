# Product Spec — DeFi Sentinel Swarm

## Problem

Protocol risk teams and treasury operators need fast, explainable decisions in DeFi risk intelligence workflows. Static dashboards are not enough; the product must show how agents reason, verify, produce action plans, and expose those reports through more than one usable surface.

## MVP included in this repo

- Deterministic scenario analysis.
- Multi-agent findings with confidence and severity.
- Traceable report IDs.
- CLI usage path with JSON and Markdown output.
- API boundary for hosted product integration.
- Static live dashboard using DeFiLlama data.
- CI tests that prove the reasoning shape and demo paths remain stable.

## Built-in scenarios

- stablecoin depeg pressure
- DEX pool depth collapse
- oracle feed divergence

## Operator paths reviewers can try

```bash
python3 cli.py --all
python3 cli.py --scenario "oracle feed divergence"
python3 cli.py --signals examples/operator_override.json --format markdown
python3 -m pytest -q
```

## Success metrics

- Report generated in under one second locally.
- Every report has findings from all specialist agents.
- Every report includes risk score, confidence, verdict, trace ID, and next actions.
- Product can be demoed without private keys or paid model access.
- CLI, API contract, and core runtime are covered by tests.
