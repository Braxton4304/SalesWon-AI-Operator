# Trust Model

**Why trust this recommendation?**

## Evidence Sources

| Source | Used For | Precedence |
|--------|----------|------------|
| ServiceNow account | Tier, industry, hierarchy | Authoritative |
| ServiceNow contact | Names, titles, linked opps | Authoritative |
| ServiceNow opportunity | Pipeline, stages, amounts, close dates | Authoritative |
| ServiceNow case | Service health, priority, state | Authoritative |
| ServiceNow activity | Engagement recency, meeting history | Authoritative |
| DISCOVERY_PLAYBOOK | Research question structure (SPIN) | Methodology |
| ACCOUNT_PLANNING | Brief structure, 90-day objectives | Methodology |
| CUSTOMER_RISK_GUIDE | Risk signal definitions | Policy |
| Knowledge base (RAG) | Product white-space, industry context | Supplementary |

Precedence per [data-spec](../../specifications/data-spec.md): CRM > Layer 4 config > RAG > agent inference (never for CRM field values).

## Confidence Calculation

Per [shared/confidence-scoring.md](../../shared/confidence-scoring.md):

| Factor | Impact |
|--------|--------|
| Account name resolved uniquely | +0.10 |
| Contact records with titles present | +0.10 |
| Activities within 30 days | +0.08 |
| Open opps with required fields complete | +0.10 |
| Case data retrieved for service_context | +0.05 |
| Relationship roles confirmed in CRM | +0.10 |
| Missing economic buyer on late-stage opp | −0.12 |
| Inferred roles > 50% of relationship_map | −0.10 |
| Stale activity (> 45 days) on strategic account | −0.08 |
| Conflicting opp/case signals | −0.15 → consider escalate |

## Confidence Bands

| Band | Range | Behavior |
|------|-------|----------|
| High | ≥ 0.85 | Full answer; brief ready for exec meeting |
| Medium | 0.60–0.84 | Answer with assumptions and missing_data prominent |
| Low | < 0.60 | Retrieve (up to 3x) then escalate |

## Missing Data / Assumptions

- **missing_data:** CRM fields absent that limit brief quality — always list with impact
- **assumptions:** Inferences (role labels, white-space, buyer identity) — never merge into snapshot as facts
- **source_records:** Field-level audit trail for every factual assertion

## Trust Signals for Users

1. Every pipeline number traceable to opportunity source_record
2. Risk severity cites CUSTOMER_RISK_GUIDE signal type
3. Research questions name the gap they close
4. role_confidence distinguishes confirmed vs. inferred contacts

```yaml
trust_model_version: "1.0.0"
agent_id: account-research
confidence_framework: shared/confidence-scoring.md
```
