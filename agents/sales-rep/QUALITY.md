# Quality

Implements: [OUTPUT_SCHEMA.md](OUTPUT_SCHEMA.md), [DECISION_MODEL.md](DECISION_MODEL.md), [TRUST_MODEL.md](TRUST_MODEL.md)

## Correctness

- [ ] Amount, probability, close date, stage match ServiceNow source_records
- [ ] Activity recency calculated from actual activity dates in source_records
- [ ] Contact roles not invented — confirmed or labeled inferred
- [ ] deal_health aligns with PIPELINE_HEALTH_MODEL signals
- [ ] priority_score aligns with DECISION_MODEL formula (weights sum 100%)
- [ ] qualification_gaps reference real MEDDIC/SPIN/Sandler/CRM fields

## Completeness

- [ ] All required OUTPUT_SCHEMA fields present (including empty arrays where applicable)
- [ ] next_best_action includes rationale tied to CRM field in source_records
- [ ] recommended_questions tagged with methodology and purpose
- [ ] suggested_follow_up populated or explicitly type none
- [ ] missing_data lists gaps impacting confidence or scoring
- [ ] escalation_required set correctly per ESCALATION.md
- [ ] Meeting prep includes account + opp + stakeholders when requested

## Hallucination Avoidance

- [ ] No competitor names unless in opp record or KB source_records
- [ ] priority_score derived from documented DECISION_MODEL inputs, not arbitrary
- [ ] No MEDDIC field marked complete without CRM evidence
- [ ] Financial figures traceable to opportunity source_record

## Methodology Quality

- [ ] Early-stage opps use SPIN/Sandler recommended_questions appropriately
- [ ] Late-stage opps prioritize MEDDIC blocking gaps
- [ ] Severity (blocking/important/nice_to_have) matches stage and gap type
- [ ] recommended_questions address specific qualification_gaps when present

## Explainability Quality

- [ ] priority_score_factors populated or explainable on request
- [ ] "Why" responses cite DECISION_MODEL weight table
- [ ] Authority scope confirmed for draft/recommend actions

## Demo Scenarios

1. **Healthy opp summary** — complete MEDDIC, recent activity, deal_health healthy, moderate priority_score
2. **At-risk opp with activity recommendation** — stale activity, blocking economic_buyer gap, next_best_action + suggested_follow_up
3. **Discovery coaching** — early stage, SPIN recommended_questions, Sandler pain gap
4. **Discount request** — refuse + escalation_required + escalation_payload to manager
5. **Pipeline prioritization for today** — pipeline_rankings ordered by DECISION_MODEL, top 3 with next_action_summary
6. **Missing required fields** — missing_data populated, confidence reduced, ask or retrieve
7. **Explainability request** — factor breakdown per EXPLAINABILITY.md on named opp

## Automated Validation

Automated validation against OUTPUT_SCHEMA + golden rep pipeline datasets. See [architecture/domains/testing-deployment](../../architecture/domains/testing-deployment/README.md).

```yaml
quality_version: "1.1.0"
agent_id: sales-rep
schema_ref: agents/sales-rep/OUTPUT_SCHEMA.md
decision_model_weights_sum: 100
```
