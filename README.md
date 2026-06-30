# SalesWon AI Operator

**The reusable operating system for SalesWon AI** — not a single-customer implementation, but the contract-first foundation for every future SalesWon deployment (and reusable IP for Cohort, Axiom, and AI Council).

## Start Here

1. Read **[specifications/](specifications/)** — authoritative contracts (ISO-style)
2. Explore **[architecture/](architecture/)** — SalesWon AI Platform design workspace
3. Copy **[agents/_template/](agents/_template/)** to create a new agent

## Architecture

```text
/specifications          ← Contracts (platform, runtime, agent, governance, data)
        ↓
/shared                  ← Layer 1: Business standards (industry IP)
        ↓
/runtime                 ← Layer 2: Platform runtime
        ↓
/agents                  ← Layer 3: Agent specifications
        ↓
/platform                ← Integration surfaces (ServiceNow, RAG, data dictionary)
        ↓
/architecture            ← Blueprint workspace
        ↓
Customer Configuration   ← Layer 4 (per-deployment, not in this repo)
        ↓
Customer Data            ← Layer 5 (CRM — never in source control)
```

## Governed Response Pipeline

```text
Business Standards → Runtime → Agent → Customer Config → CRM Context → LLM → Governed Response
```

## Specification Index

| Spec | File |
|------|------|
| Platform | [specifications/platform-spec.md](specifications/platform-spec.md) |
| Runtime | [specifications/runtime-spec.md](specifications/runtime-spec.md) |
| Agent | [specifications/agent-spec.md](specifications/agent-spec.md) |
| Governance | [specifications/governance-spec.md](specifications/governance-spec.md) |
| Data | [specifications/data-spec.md](specifications/data-spec.md) |

## Adding a New Agent

```powershell
Copy-Item -Recurse agents\_template agents\your-agent-name
```

Fill domain files per [specifications/agent-spec.md](specifications/agent-spec.md). Do not redefine runtime or governance in the agent folder.

## Adding a New Business Domain

Add a top-level folder with a README charter (e.g. `/commercial/README.md`). Do not create empty placeholder trees.

## Documentation

- [docs/architecture/platform-layers.md](docs/architecture/platform-layers.md) — layer model and SDK vision
- [docs/architecture/contract-evolution.md](docs/architecture/contract-evolution.md) — path to executable specifications
- [docs/implementation/getting-started.md](docs/implementation/getting-started.md) — first agent walkthrough

## License & IP

SalesWon AI Agent Specification v1 is Power Tech intellectual property. See specifications for reuse terms across products.
