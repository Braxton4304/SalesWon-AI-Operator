# Trust Model

**Why trust this recommendation?**

## Evidence Sources

| Source | Used For | Precedence |
|--------|----------|------------|
| ServiceNow case | State, priority, impact, urgency, assignment, SLA, work notes | Authoritative |
| ServiceNow account | Tier, strategic flag, open case count | Authoritative |
| ServiceNow contact | Requester identity, role | Authoritative |
| ServiceNow activity | Follow-up tasks, callback history | Authoritative |
| CUSTOMER_SERVICE_FRAMEWORK | Sentiment handling, tier rules, SLA awareness | Policy |
| escalation-framework | Mandatory escalation triggers | Policy |
| EMAIL_STYLE_GUIDE | Customer draft format | Methodology |
| COMMUNICATION_STANDARD | Channel policies | Policy |
| CUSTOMER_PROMISES | Commitment boundaries | Policy |
| Knowledge base (RAG) | Resolution procedures | Supplementary |

Precedence per [data-spec](../../specifications/data-spec.md): CRM > Layer 4 config > policy/methodology > RAG > agent inference (never for CRM field values).

## Confidence Calculation

Per [shared/confidence-scoring.md](../../shared/confidence-scoring.md) adapted for case scope:

| Factor | Impact |
|--------|--------|
| Case retrieved with all required fields (short_description, state, assigned_to) | +0.15 |
| SLA data retrieved when SLA question asked | +0.10 |
| impact/urgency from CRM fields (not inferred) | +0.10 |
| Account tier retrieved for strategic assessment | +0.05 |
| Work notes retrieved for sentiment assessment | +0.08 |
| KB article supports recommended resolution step | +0.05 |
| Missing required case field after retrieve | −0.25 → escalate per data-spec |
| impact/urgency inferred (fields absent) | −0.10 |
| SLA policy not applicable or absent when asked | −0.08 |
| Case data stale (>24h since last query in session) | −0.05 |
| CRM priority conflicts with computed severity by >1 band | −0.12 |
| Sentiment insufficient text (unknown) | −0.05 |

## Confidence Bands

| Band | Range | Behavior |
|------|-------|----------|
| High | ≥ 0.85 | Full answer; draft ready for rep send |
| Medium | 0.60–0.84 | Answer with missing_data prominent; note inferred ITIL |
| Low | < 0.60 | Retrieve (up to 3x) then escalate |

## Missing Data / Assumptions

- **missing_data:** Required case fields absent, SLA unavailable, impact/urgency inferred — always list with impact on severity and escalation
- **No assumptions array:** CS agent does not invent CRM field values — use missing_data and reduce confidence instead
- **source_records:** Field-level audit trail for every case fact, ITIL score, SLA claim, and draft evidence

## Trust Signals for Users

1. Every case fact traceable to case source_record with fields_used
2. impact/urgency.source indicates crm_field vs. inferred
3. priority_score explainable via DECISION_MODEL weight table (sums 100%)
4. escalation_reason cites ESCALATION.md trigger ID
5. suggested_customer_response requires_human_send always true
6. SLA times from platform fields — never estimated without missing_data flag

```yaml
trust_model_version: "1.0.0"
agent_id: customer-service
confidence_framework: shared/confidence-scoring.md
decision_model_weights_sum: 100
```
