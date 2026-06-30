# Mission

**Primary outcome:** Increase sales velocity and win rate by helping reps prioritize the right activities on the right opportunities at the right time — with CRM-grounded qualification and next-best-action guidance.

## Success Criteria

| Metric | Target (Phase 1 pilot) |
|--------|------------------------|
| Next-best-action acceptance | ≥ 65% |
| Opportunity field accuracy in summaries | ≥ 95% |
| Qualification gap identification | ≥ 80% useful per rep survey |
| Activity draft acceptance | ≥ 60% |
| Schema compliance | ≥ 99% |
| Source grounding in source_records | ≥ 98% |

## Business Reasoning Alignment

Per [runtime/BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md):

- **Revenue** — Primary. Pipeline progression and deal hygiene.
- **Sales Velocity** — Primary. Activity prioritization and stale deal recovery prompts.
- **Activity Effectiveness** — Secondary. ROI-weighted recommendations via DECISION_MODEL.
- **Customer Retention** — Tertiary. Flags risk signals for CS handoff on active deals.

## ServiceNow Context

Opportunities on `sn_opportunity` (mapped as **opportunity**), linked **account**, **contact**, **task**/**activity**, and **lead** for early-stage work.

## Accountability Link

See [ACCOUNTABILITY.md](ACCOUNTABILITY.md) for owned artifacts (`opportunity_summary`, `next_best_action`, `qualification_gaps`) and failure criteria.
