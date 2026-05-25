# DeFi Sentinel Swarm Architecture

## Purpose

Autonomous multi-agent risk desk for liquidity shocks, oracle anomalies, bridge stress, and liquidation cascades.

## Runtime loop

1. **Observe** — collect domain signals: pool_depth_change, oracle_spread_bps, bridge_outflow_usd, liquidation_queue_usd, governance_delay_hours.
2. **Orient** — map the active scenario to specialist agent responsibilities.
3. **Decide** — score severity, confidence, and operator urgency.
4. **Act** — emit next actions that a human operator can verify.
5. **Reflect** — attach trace IDs and deterministic evidence for review.

## Components

- `backend/swarm.py` — pure Python reasoning core, safe for CI and local demos.
- `backend/app.py` — FastAPI wrapper for hosted product integration.
- `cli.py` — terminal demo path with JSON and Markdown output.
- `index.html` — front-facing DeFi dashboard using live DeFiLlama data.
- `examples/operator_override.json` — high-stress scenario fixture.
- `tests/` — runtime, CLI, and API contract coverage.

## Agent responsibilities

- `Liquidity Sentinel`: owns pool-depth and capital-flight telemetry.
- `Oracle Divergence Analyst`: checks oracle spread and stale-feed risk.
- `Bridge Exposure Mapper`: maps bridge outflow stress and blast radius.
- `Liquidation Cascade Forecaster`: estimates liquidation queue pressure.
- `Treasury Action Planner`: converts findings into executable operator actions.

## Output contract

Every report returns:

- project
- domain
- scenario
- risk_score
- confidence
- verdict
- findings[]
- next_actions[]
- trace_id
- generated_at

## Production extension points

- Replace deterministic signals with live connectors.
- Persist reports in Postgres or SQLite.
- Add auth and organization workspaces.
- Add export hooks for Slack, Discord, Telegram, or email.
- Add human approval workflow for high-impact treasury actions.
