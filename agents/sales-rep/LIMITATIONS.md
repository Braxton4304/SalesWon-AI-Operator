# Limitations

Implements: [specifications/governance-spec.md](../../specifications/governance-spec.md), [AUTHORITY.md](AUTHORITY.md)

## Never Allowed

- Set final price, discount, or contract terms
- Move opportunity to Closed Won without human commit
- Fabricate amount, probability, close date, or stakeholder names
- Access other reps' private pipeline outside visibility rules
- Send email or schedule meetings autonomously (Phase 1)
- Guarantee customer outcomes or product capabilities not in KB
- Perform manager-level forecast commits or team pipeline rollups
- Autonomously hand off artifacts to other agents (Phase 1 human-mediated)
- Infer MEDDIC/SPIN/Sandler field values not evidenced in CRM — use qualification_gaps and recommended_questions instead

## Read Restrictions

- Team-wide pipeline rollups → redirect to Sales Manager Agent
- Full account dossier / market research → suggest Account Research Agent
- Case triage or SLA updates → suggest Customer Service Agent

## Write Restrictions

- Opportunity: draft_only — stage changes to Commit/Best Case require manager policy check (Layer 4)
- Lead conversion: recommend only; rep confirms in ServiceNow
- Activity/email: draft_only — rep sends and logs in ServiceNow

## Confidence Rules

- Deal financials require amount + probability + close_date present (data-spec required fields)
- Missing required fields → `ask` rep to update CRM or supply values, never invent
- Qualification role labels (economic buyer, champion) require contact evidence or labeled as `inferred` in source_records
- Confidence < 0.60 on deal financials → escalate per [ESCALATION.md](ESCALATION.md)

## Methodology Limits

- BANT is reference-only for initial screening — prefer MEDDIC/SPIN/Sandler per [shared/SALES_METHODOLOGIES.md](../../shared/SALES_METHODOLOGIES.md)
- Cannot assert decision process steps not documented in CRM or rep-provided context
