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

- `backend/swarm.py` — pure Python reasoning core, safe for CI and static demos.
- `backend/app.py` — FastAPI wrapper for product integration.
- `cli.py` — terminal demo path for reviewers.
- `index.html` — front-facing dashboard surface.

## Agent responsibilities

- `Liquidity Sentinel`: owns one part of the analysis loop.
- `Oracle Divergence Analyst`: owns one part of the analysis loop.
- `Bridge Exposure Mapper`: owns one part of the analysis loop.
- `Liquidation Cascade Forecaster`: owns one part of the analysis loop.
- `Treasury Action Planner`: owns one part of the analysis loop.

## Production extension points

- Replace deterministic signals with live connectors.
- Persist reports in Postgres or SQLite.
- Add auth and organization workspaces.
- Add export hooks for Slack, Discord, Telegram, or email.
