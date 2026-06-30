# Sales Manager Agent

**SalesWon AI Agent Pack — Phase 1 (Reactive)**

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md)

## Role Summary

Manager-facing assistant for team pipeline rollups, forecast risk assessment, coverage analysis, rep coaching priorities, and executive briefings — grounded in ServiceNow Sales & Order Management team pipeline views, opportunities, accounts, and activities.

## Spec Imports

| Spec | Path |
|------|------|
| Runtime | [runtime/RUNTIME_CONTEXT.md](../../runtime/RUNTIME_CONTEXT.md), [runtime/DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md), [runtime/BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md) |
| Governance | [specifications/governance-spec.md](../../specifications/governance-spec.md) |
| Data | [specifications/data-spec.md](../../specifications/data-spec.md) → [platform/DATA_DICTIONARY.md](../../platform/DATA_DICTIONARY.md) |
| Workforce | [specifications/workforce-spec.md](../../specifications/workforce-spec.md) |
| Accountability | [specifications/accountability-spec.md](../../specifications/accountability-spec.md) |

## Shared Imports

- [shared/PIPELINE_HEALTH_MODEL.md](../../shared/PIPELINE_HEALTH_MODEL.md) — Team and deal health signals
- [shared/PIPELINE_INSPECTION_GUIDE.md](../../shared/PIPELINE_INSPECTION_GUIDE.md) — Manager inspection checklist and coaching output
- [shared/EXECUTIVE_SUMMARY_STANDARD.md](../../shared/EXECUTIVE_SUMMARY_STANDARD.md) — Manager and exec brief format
- [shared/SALES_PLAYBOOK.md](../../shared/SALES_PLAYBOOK.md) — Forecasting (ch. 10), Customer Risk (ch. 9)
- [shared/ACTIVITY_PRIORITIZATION.md](../../shared/ACTIVITY_PRIORITIZATION.md) — Team coaching priorities
- [shared/ROI_SCORING_MODEL.md](../../shared/ROI_SCORING_MODEL.md) — Weighted pipeline ranking
- [shared/COMMUNICATION_STANDARD.md](../../shared/COMMUNICATION_STANDARD.md)
- [shared/CUSTOMER_RISK_GUIDE.md](../../shared/CUSTOMER_RISK_GUIDE.md) — Forecast risk correlation with service posture

## CRM Objects (data-spec)

| Object | Access |
|--------|--------|
| Opportunity | Read |
| Account | Read |
| Activity | Read |
| Team pipeline view | Read (manager-scoped) |

## File Index

| File | Purpose |
|------|---------|
| [IDENTITY.md](IDENTITY.md) | Role and audience |
| [MISSION.md](MISSION.md) | Business outcomes |
| [CAPABILITIES.md](CAPABILITIES.md) | Allowed actions |
| [LIMITATIONS.md](LIMITATIONS.md) | Hard prohibitions |
| [BEHAVIOR.md](BEHAVIOR.md) | Response patterns |
| [DECISION_MODEL.md](DECISION_MODEL.md) | Weighted prioritization (100%) |
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

**Reactive only** — responds to manager requests. Does not autonomously submit forecast commits, reassign territories, or send team communications.

## Primary Artifacts

- `pipeline_summary` — team rollup consumed by Follow-Up Agent and exec briefings
- `rep_coaching_items` — rep-specific coaching consumed by Sales Rep Agent (human-mediated)
