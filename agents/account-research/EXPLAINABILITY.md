# Explainability

When user asks **"Why did you recommend this?"** respond with:

## Response Structure

1. **Recommendation restated** — e.g., "I flagged Acme as at-risk due to service posture and flagged executive engagement gap."
2. **Priority score breakdown** — factors from [DECISION_MODEL.md](DECISION_MODEL.md): risk signals, pipeline value, meeting urgency, relationship gaps
3. **Evidence** — cite `source_records` (account, opp, case, contact IDs and fields)
4. **Authority check** — confirm action is within [AUTHORITY.md](AUTHORITY.md) (read/analyze/recommend only)
5. **What would change the recommendation** — e.g., "CIO engagement logged in CRM would reduce risk severity and raise confidence."

## Explainability by Output Field

| Field | Explain With |
|-------|--------------|
| account_brief.headline | Top risk + top opportunity from snapshot |
| relationship_map.role_label | Contact title + activity evidence or assumption basis |
| buying_signals | CRM event type, date, source_record_id |
| risks.severity | CUSTOMER_RISK_GUIDE signal mapping |
| recommended_research_questions | missing_data field each question targets |
| confidence | TRUST_MODEL factor table |
| assumptions | Why inference was necessary vs. retrieve |

## Example (Demo)

**User:** "Why is Acme expansion at-risk?"

**Agent explainability response:**

1. **Restated:** Expansion FY26 is at-risk because of correlated P2 cases and missing economic buyer engagement.
2. **Priority:** Service risk weight 0.9 (2 P2 cases open 12+ days) + late-stage opp without CIO activity in 45 days.
3. **Evidence:** opp789 (Proposal, $250K, close 2026-07-15); cs2001 (P2, In Progress); con101 last activity 2026-05-15.
4. **Authority:** Assessment only — no opp stage change; recommend exec alignment activity via recommend.
5. **Would change if:** P2 cases resolved (service_context → green); CIO activity logged within 14 days of close date.

## Anti-Patterns

- "Because the AI determined..." without CRM citation
- Confidence number without factor breakdown
- Risk claims without CUSTOMER_RISK_GUIDE reference

```yaml
explainability_version: "1.0.0"
agent_id: account-research
```
