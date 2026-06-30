# Capabilities

## Read (ServiceNow / data-spec)

| Object | Use Cases |
|--------|-----------|
| **Case** | Status, priority, impact, urgency, assignment, work notes, resolution history, SLA timers |
| **Account** | Customer tier, industry, open case count, strategic/VIP flag |
| **Contact** | Requester identity, role, communication history |
| **Activity** | Scheduled follow-ups, callbacks, related tasks |

## Draft-Only Writes (recommend action)

| Object | Draft Types |
|--------|-------------|
| **Case** | Customer email draft, internal work note, proposed state change (e.g. Awaiting Customer) |
| **Activity** | Follow-up call task, callback reminder |

All drafts emit `decision_action: recommend` with `recommended_action.draft_payload` in OUTPUT_SCHEMA. Rep commits in ServiceNow per [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md).

## Response Types

- Structured `case_summary` (open + recent context)
- ITIL `impact` and `urgency` assessment with `severity` derivation
- SLA status and time-to-breach estimate
- `customer_sentiment` assessment (from case text + history)
- `suggested_customer_response` per EMAIL_STYLE_GUIDE
- Triage recommendation (priority, assignment group suggestion)
- Related case / duplicate detection summary
- Escalation handoff with `escalation_required` and `escalation_reason`

## Shared Knowledge Applied

- [shared/CUSTOMER_SERVICE_FRAMEWORK.md](../../shared/CUSTOMER_SERVICE_FRAMEWORK.md) — tier handling, sentiment rules, resolve-at-lowest-tier
- [shared/COMMUNICATION_STANDARD.md](../../shared/COMMUNICATION_STANDARD.md) — channel policies (email draft_only)
- [shared/escalation-framework.md](../../shared/escalation-framework.md) — mandatory triggers
- [shared/confidence-scoring.md](../../shared/confidence-scoring.md) — confidence bands

## Tools

See [TOOLS.md](TOOLS.md).

```yaml
capabilities_version: "1.0.0"
agent_id: customer-service
write_mode: draft_only
phase: 1
```
