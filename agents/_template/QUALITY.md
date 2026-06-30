# Quality

Correctness, completeness, and hallucination avoidance criteria for this agent.

## Correctness

- [ ] Every factual claim traceable to `sources`
- [ ] CRM field values match retrieved records
- [ ] Dates and amounts not hardcoded
- [ ] Tenant and visibility rules respected

## Completeness

- [ ] User question fully addressed or explicitly deferred with `ask`/`escalate`
- [ ] Required OUTPUT_SCHEMA fields present
- [ ] Recommended actions include target record and rationale

## Hallucination Avoidance

- [ ] No CRM fields invented when missing — use missing_data_behavior
- [ ] No policy citations without reference in shared/ or Layer 4
- [ ] No fabricated metrics or ROI numbers

## Evaluation Harness (Planned)

Automated validation against OUTPUT_SCHEMA + golden datasets. See [architecture/domains/testing-deployment](../../architecture/domains/testing-deployment/README.md).
