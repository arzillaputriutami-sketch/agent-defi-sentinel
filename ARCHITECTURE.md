# Architecture — DeFi Sentinel Swarm

```mermaid
flowchart LR
  A[Protocol Signals] --> B[Ingestion Layer]
  B --> C1[Liquidation Agent]
  B --> C2[Bridge Agent]
  B --> C3[Whale Agent]
  B --> C4[Oracle Agent]
  C1 --> D[MiMo Reasoning Layer]
  C2 --> D
  C3 --> D
  C4 --> D
  D --> E[Consensus Engine]
  E --> F[Risk Dashboard]
  E --> G[Action Queue]
  E --> H[Incident Report Export]
```

## Components

- **Ingestion Layer:** normalizes synthetic protocol, bridge, whale, and oracle signals.
- **Specialized Agents:** each agent owns a risk dimension.
- **Reasoning Layer:** orders evidence into a reviewer-visible reasoning trace.
- **Consensus Engine:** merges agent votes into confidence and action recommendations.
- **Dashboard:** interactive UI for proof-of-usage screenshots.
