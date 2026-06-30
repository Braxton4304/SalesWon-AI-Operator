# Getting Started

## Digital Workforce v1

Five Digital Employees are ready for client demo review. Each has **22 contract files**.

| Agent | Demo prompt |
|-------|-------------|
| Customer Service | "Summarize INC0012345, SLA risk, draft empathetic reply" |
| Sales Rep | "Review Acme Expansion — MEDDIC gaps and next best action" |
| Sales Manager | "Pipeline summary for my team — forecast risks" |
| Account Research | "Brief me on Globex Corp before tomorrow's QBR" |
| Follow-Up | "What follow-ups am I overdue on? Draft top priority email" |

## Multi-Agent Demo Flow

1. **Account Research** produces `account_brief`
2. Human switches to **Sales Rep** with brief context
3. **Sales Rep** produces `opportunity_summary` + `next_best_action`
4. **Follow-Up** drafts `suggested_message` from opp context

Phase 1: handoffs are **human-mediated** (see each agent's COLLABORATION.md).

## Edit an Existing Employee

1. Read [specifications/agent-spec.md](../specifications/agent-spec.md) (22 files)
2. Read agent's AUTHORITY.md + ACCOUNTABILITY.md first
3. Schema changes to OUTPUT_SCHEMA.md may require ADR if contract-breaking
4. Cross-check COLLABORATION.md against [shared/DIGITAL_WORKFORCE.md](../shared/DIGITAL_WORKFORCE.md)

## Create a New Role

```powershell
Copy-Item -Recurse agents\_template agents\new-role-name
```

Fill all 22 files. **New roles require ADR** (architecture frozen per ADR-005).

## Key Questions Each Agent Answers

| File | Question |
|------|----------|
| AUTHORITY.md | Can I do this? |
| ACCOUNTABILITY.md | Am I succeeding? |
| EXPLAINABILITY.md | Why this recommendation? |
| TRUST_MODEL.md | Why trust this? |

## Specifications

Start with [specifications/README.md](../specifications/README.md) — 7 frozen specs.

## Policies

All agents inherit [policies/](../policies/) — do not redefine in agent folders.
