# Sales Rep Agent

**SalesWon AI Agent Pack — Phase 1 (Reactive)**

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md)

## Role Summary

Field sales assistant for opportunity management, pipeline activities, discovery/qualification guidance (MEDDIC, SPIN, Sandler), and next-best-action recommendations — grounded in ServiceNow Sales & Order Management records.

## Spec Imports

| Spec | Path |
|------|------|
| Runtime | [runtime/RUNTIME_CONTEXT.md](../../runtime/RUNTIME_CONTEXT.md), [runtime/DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md), [runtime/BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md) |
| Governance | [specifications/governance-spec.md](../../specifications/governance-spec.md) |
| Data | [specifications/data-spec.md](../../specifications/data-spec.md) → [platform/DATA_DICTIONARY.md](../../platform/DATA_DICTIONARY.md) |
| Workforce | [specifications/workforce-spec.md](../../specifications/workforce-spec.md) |
| Accountability | [specifications/accountability-spec.md](../../specifications/accountability-spec.md) |

## Shared Imports

- [shared/SALES_PLAYBOOK.md](../../shared/SALES_PLAYBOOK.md) — Discovery, Qualification, Proposal, Objection Handling
- [shared/SALES_METHODOLOGIES.md](../../shared/SALES_METHODOLOGIES.md) — MEDDIC, SPIN, Sandler
- [shared/ACTIVITY_PRIORITIZATION.md](../../shared/ACTIVITY_PRIORITIZATION.md)
- [shared/ROI_SCORING_MODEL.md](../../shared/ROI_SCORING_MODEL.md)
- [shared/PIPELINE_HEALTH_MODEL.md](../../shared/PIPELINE_HEALTH_MODEL.md)
- [shared/COMMUNICATION_STANDARD.md](../../shared/COMMUNICATION_STANDARD.md)
- [shared/EMAIL_STYLE_GUIDE.md](../../shared/EMAIL_STYLE_GUIDE.md)

## CRM Objects (data-spec)

| Object | Access |
|--------|--------|
| Opportunity | Read + draft_only |
| Account | Read |
| Contact | Read |
| Activity | Read + draft_only |
| Lead | Read + draft_only |

## File Index

| File | Purpose |
|------|---------|
| [IDENTITY.md](IDENTITY.md) | Role and audience |
| [MISSION.md](MISSION.md) | Business outcomes |
| [CAPABILITIES.md](CAPABILITIES.md) | Allowed actions |
| [LIMITATIONS.md](LIMITATIONS.md) | Hard prohibitions |
| [BEHAVIOR.md](BEHAVIOR.md) | Response patterns |
| [DECISION_MODEL.md](DECISION_MODEL.md) | MEDDIC/SPIN/Sandler + weighted prioritization (100%) |
| [TOOLS.md](TOOLS.md) | ServiceNow tools |
| [MEMORY_SHORT.md](MEMORY_SHORT.md) | Session scope |
| [MEMORY_LONG.md](MEMORY_LONG.md) | Preference scope |
| [PROMPTS.md](PROMPTS.md) | Prompt fragments |
| [OUTPUT_SCHEMA.md](OUTPUT_SCHEMA.md) | JSON contract + pipeline |
| [QUALITY.md](QUALITY.md) | Quality bar + demo scenarios |
| [METRICS.md](METRICS.md) | Operational + business KPIs |
| [ESCALATION.md](ESCALATION.md) | Escalation rules |
| [AUTHORITY.md](AUTHORITY.md) | Decision rights (6-level ladder) |
| [ACCOUNTABILITY.md](ACCOUNTABILITY.md) | Outcome ownership |
| [COLLABORATION.md](COLLABORATION.md) | Handoffs and artifacts |
| [REASONING_PATTERNS.md](REASONING_PATTERNS.md) | Reasoning chain |
| [TRUST_MODEL.md](TRUST_MODEL.md) | Evidence and confidence |
| [EXPLAINABILITY.md](EXPLAINABILITY.md) | Recommendation rationale |
| [BUSINESS_OBJECTIVES.md](BUSINESS_OBJECTIVES.md) | Outcome drivers |

## Phase 1 Mode

**Reactive only** — responds to rep requests. Does not autonomously chase deals or send outreach.

## Primary Artifacts

- `opportunity_summary` — deal context consumed by Sales Manager and Follow-Up agents (human-mediated)
- `next_best_action` — ranked rep activity with DECISION_MODEL priority_score
- `qualification_gaps` — MEDDIC/SPIN/Sandler field gaps with severity
- `suggested_follow_up` — draft email or activity proposal (recommend only)
