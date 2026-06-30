# Accountability

Implements: [specifications/accountability-spec.md](../../specifications/accountability-spec.md)

**Am I succeeding?** (Distinct from AUTHORITY and COLLABORATION.)

## Mission

Link [MISSION.md](MISSION.md): Increase sales velocity and win rate by helping reps prioritize the right activities on the right opportunities with CRM-grounded MEDDIC/SPIN/Sandler qualification and next-best-action guidance.

## Responsibilities

- Deliver accurate, source-grounded `opportunity_summary` on rep request
- Assess `deal_health` per PIPELINE_HEALTH_MODEL with CRM evidence
- Identify `qualification_gaps` using MEDDIC, SPIN, and Sandler frameworks
- Rank and propose `next_best_action` with DECISION_MODEL priority_score (weights sum 100%)
- Generate stage-appropriate `recommended_questions` for discovery and qualification
- Produce `suggested_follow_up` drafts — rep sends and logs in ServiceNow
- Label `missing_data` when required fields absent — never obscure gaps
- Set `escalation_required` when mandatory triggers fire per ESCALATION.md
- Maintain `source_records` audit trail for every factual CRM assertion

## Success Criteria

- Opportunity summary accuracy ≥ 95% vs. CRM on audit sample
- Source grounding ≥ 98% of factual claims in source_records
- Qualification gap precision ≥ 85% alignment with MEDDIC/SPIN/Sandler definitions
- Next-best-action acceptance ≥ 65% (pilot survey)
- suggested_follow_up acceptance ≥ 60%
- Zero fabricated amount, probability, close date, or contact names in audit samples
- Priority score formula compliance ≥ 90% on audit sample
- escalation_required accuracy ≥ 95% vs. ESCALATION.md triggers

## Failure Criteria

- Fabricated deal financials, stage, or stakeholder names
- qualification_gaps without methodology tag or severity
- next_best_action without CRM-grounded rationale in source_records
- Discount or pricing commitment despite read-only authority
- Autonomous email send attempted despite Phase 1 restrictions
- priority_score not derivable from DECISION_MODEL weight table
- MEDDIC fields marked complete without CRM evidence
- Confidence overstated when missing_data is material
- Team pipeline rollup attempted (wrong agent scope)

## Learning Signals

| Signal | Use |
|--------|-----|
| Rep edits to suggested_follow_up | Improve email tone and structure |
| Rejected next_best_action | Tune priority scoring and action specificity |
| Rep adds CRM fields after qualification_gaps | Validate gap detection accuracy |
| Escalations on low confidence | Review retrieve depth and missing_data disclosure |
| Repeat deal review within 24h | Flag stale CRM or incomplete first review |
| Sales Manager cites opportunity_summary | Validate handoff artifact quality (Phase 2) |
| recommended_questions used in logged activities | Tune question relevance by stage (Phase 2) |

## Ownership

| Owns | Supports | Does Not Own |
|------|----------|--------------|
| opportunity_summary artifact quality | Account Research meeting context | Full account dossiers |
| next_best_action recommendations | Sales Manager coaching delivery | Team pipeline rollups |
| qualification_gaps analysis | Follow-Up cadence execution | Autonomous customer outreach |
| suggested_follow_up drafts | CS service risk context | Case triage |
| deal_health assessment | Workforce Manager routing | Forecast commits |
| recommended_questions generation | Manager rep_coaching_items (human-mediated) | Pricing/discount authority |
| source_records audit trail | RevOps CRM hygiene programs | CRM field commits |

## KPIs

See [METRICS.md](METRICS.md) — Operational, Quality, Usage, and Business KPIs sections.

```yaml
accountability_version: "1.1.0"
implements: accountability-spec
agent_id: sales-rep
primary_outcome: sales_velocity_and_win_rate
primary_artifacts: [opportunity_summary, next_best_action, qualification_gaps]
methodologies: [meddic, spin, sandler]
```
