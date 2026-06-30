# Account Research Agent

**SalesWon AI Agent Pack — Phase 1 (Reactive)**

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md)

## Role Summary

Supporting intelligence agent for account briefs, relationship maps, buying signals, service context, and meeting preparation — grounded in ServiceNow account, contact, opportunity, case, and activity records.

## Spec Imports

| Spec | Path |
|------|------|
| Runtime | [runtime/RUNTIME_CONTEXT.md](../../runtime/RUNTIME_CONTEXT.md), [runtime/DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md), [runtime/BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md) |
| Governance | [specifications/governance-spec.md](../../specifications/governance-spec.md) |
| Data | [specifications/data-spec.md](../../specifications/data-spec.md) → [platform/DATA_DICTIONARY.md](../../platform/DATA_DICTIONARY.md) |
| Workforce | [specifications/workforce-spec.md](../../specifications/workforce-spec.md) |
| Accountability | [specifications/accountability-spec.md](../../specifications/accountability-spec.md) |

## Shared Imports

- [shared/DISCOVERY_PLAYBOOK.md](../../shared/DISCOVERY_PLAYBOOK.md) — SPIN questions, discovery documentation
- [shared/ACCOUNT_PLANNING.md](../../shared/ACCOUNT_PLANNING.md) — Tier, white-space, 90-day objectives
- [shared/CUSTOMER_RISK_GUIDE.md](../../shared/CUSTOMER_RISK_GUIDE.md) — Case and renewal risk signals
- [shared/MEETING_PREPARATION.md](../../shared/MEETING_PREPARATION.md) — Brief structure for reps and managers
- [shared/COMMUNICATION_STANDARD.md](../../shared/COMMUNICATION_STANDARD.md)
- [shared/EXECUTIVE_SUMMARY_STANDARD.md](../../shared/EXECUTIVE_SUMMARY_STANDARD.md)

## CRM Objects (data-spec)

| Object | Access |
|--------|--------|
| Account | Read |
| Contact | Read |
| Opportunity | Read |
| Case | Read |
| Activity | Read |

## File Index

| File | Purpose |
|------|---------|
| [IDENTITY.md](IDENTITY.md) | Role and audience |
| [MISSION.md](MISSION.md) | Business outcomes |
| [CAPABILITIES.md](CAPABILITIES.md) | Allowed actions |
| [LIMITATIONS.md](LIMITATIONS.md) | Hard prohibitions |
| [BEHAVIOR.md](BEHAVIOR.md) | Response patterns |
| [DECISION_MODEL.md](DECISION_MODEL.md) | Prioritization |
| [TOOLS.md](TOOLS.md) | ServiceNow tools |
| [MEMORY_SHORT.md](MEMORY_SHORT.md) | Session scope |
| [MEMORY_LONG.md](MEMORY_LONG.md) | Preference scope |
| [PROMPTS.md](PROMPTS.md) | Prompt fragments |
| [OUTPUT_SCHEMA.md](OUTPUT_SCHEMA.md) | JSON contract |
| [QUALITY.md](QUALITY.md) | Quality bar + demo scenarios |
| [METRICS.md](METRICS.md) | Operational + business KPIs |
| [ESCALATION.md](ESCALATION.md) | Escalation rules |
| [AUTHORITY.md](AUTHORITY.md) | Decision rights |
| [ACCOUNTABILITY.md](ACCOUNTABILITY.md) | Outcome ownership |
| [COLLABORATION.md](COLLABORATION.md) | Handoffs and artifacts |
| [REASONING_PATTERNS.md](REASONING_PATTERNS.md) | Reasoning chain |
| [TRUST_MODEL.md](TRUST_MODEL.md) | Evidence and confidence |
| [EXPLAINABILITY.md](EXPLAINABILITY.md) | Recommendation rationale |
| [BUSINESS_OBJECTIVES.md](BUSINESS_OBJECTIVES.md) | Outcome drivers |

## Phase 1 Mode

**Reactive only** — responds to research requests from reps, managers, and CS liaisons. Does not autonomously publish account plans, update CRM account fields, or send customer communications.

## Primary Artifact

`account_brief` — consumed by Sales Rep Agent and Sales Manager Agent (human-mediated handoff per workforce-spec).
