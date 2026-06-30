# Platform Layers

SalesWon AI **Operating System** (internal: **AIMS** — Enterprise AI Management System).

## Frozen Architecture (ADR-005)

Seven specifications. No 8th without ADR. Build **depth**, not breadth.

## Layer Stack

```text
/specifications     7 contracts
/policies           Enterprise rules (inherit only)
/runtime            Orchestration, decision engine, governance
/shared             Playbooks, organizational memory, workforce map
/agents             Digital Employees (22 files) + Workforce Manager spec
/platform           ServiceNow, DATA_DICTIONARY, RAG
/architecture       ADRs, roadmap, domain workspaces
Layer 4             Customer config (future)
Layer 5             CRM data (never in repo)
```

## Digital Workforce

```text
Workforce Manager (Phase 2 spec)
        ↓
Sales Manager → Sales Rep → Follow-Up
Parallel: Customer Service
Supporting: Account Research
```

## Accountability vs Authority

| Spec | Question | File |
|------|----------|------|
| Authority | Can I do this? | AUTHORITY.md |
| Accountability | Am I succeeding? | ACCOUNTABILITY.md |

## SDK Modules (Phase 2)

Runtime, Governance, Workforce orchestration, Memory, Prompt builder, Decision engine (weighted formulas), ServiceNow connector, Feedback/accountability loops.

See [contract-evolution.md](contract-evolution.md).
