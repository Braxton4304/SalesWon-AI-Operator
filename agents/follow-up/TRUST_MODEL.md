# Trust Model

**Why trust this follow-up recommendation?**

## Evidence Sources

| Source | Used For | Trust Level |
|--------|----------|-------------|
| ServiceNow activity | due_date, state, days_overdue | High (source_of_truth) |
| ServiceNow opportunity | Revenue weight, close_date urgency | High when required fields present |
| ServiceNow contact | Recipient, role | High |
| Activity work notes | Objection detection | Medium — interpret, don't quote without citation |
| EMAIL_LIBRARY / KB | Template structure, objection responses | High for format; medium for personalization |
| CUSTOMER_OBJECTION_LIBRARY | Message framing | High for approach; no pricing numbers |
| Layer 4 cadence config | Stage windows | High when configured |

## Confidence Calculation

Per [shared/confidence-scoring.md](../../shared/confidence-scoring.md):

| Factor | Impact |
|--------|--------|
| activity.due_date + state present | +0.15 |
| Linked opp amount + close_date present | +0.10 |
| Contact email present for draft | +0.10 |
| Last activity date within 90 days | +0.05 |
| Missing due_date | −0.25 → ask |
| Missing opp amount on revenue-weighted item | −0.15 → missing_data |
| Stale last_activity (>180d) | −0.10 |
| Objection inferred without note citation | −0.20 |

**Bands:** ≥ 0.85 recommend/answer; 0.60–0.84 recommend with caveats; < 0.60 ask or escalate.

## Missing Data / Assumptions

- **CRM facts** — due dates, states, amounts: never assumed; populate missing_data
- **Assumptions** — Label separately: "Assuming standard 7-day discovery cadence (Layer 4 default)"
- **Inferences** — Objection category from notes must cite activity id in reason

## Audit Trail

Every response includes source_records mirroring sources for workforce audit. Human sender remains accountable for final email per COMMUNICATION_STANDARD.

```yaml
trust_model_version: "1.0.0"
agent_id: follow-up
confidence_policy: shared/confidence-scoring.md
```
