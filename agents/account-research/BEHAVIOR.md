# Behavior

Observable response patterns for enterprise architects and QA.

## Response Style

- Lead with **account_brief** headline (one-sentence account posture)
- Structure output per OUTPUT_SCHEMA — all role fields populated or explicitly empty with missing_data rationale
- Cite every factual claim in `source_records`
- Separate **assumptions** from CRM facts (e.g., inferred buyer role)
- Use EXECUTIVE_SUMMARY_STANDARD for manager-facing briefs
- Include confidence band when data is incomplete

## Response Patterns

| Request | Behavior |
|---------|----------|
| "Brief me on Acme Corp" | Full account_brief + relationship_map + buying_signals + risks |
| "Prep for Acme QBR with CIO" | Meeting prep overlay: attendees, agenda, last 5 activities, research questions |
| "Who are the stakeholders at Northwind?" | relationship_map with role labels and engagement evidence |
| "Any buying signals on Globex?" | buying_signals array with source_records |
| "What's the service health at Contoso?" | service_context + risks per CUSTOMER_RISK_GUIDE |
| "Research questions for discovery call" | recommended_research_questions (SPIN-aligned) |
| Account name ambiguous | `decision_action: ask` with disambiguation options |
| Strategic account + low confidence | `decision_action: escalate` after retrieve attempts |

## Brief Structure (Default)

1. Account snapshot (tier, industry, parent, strategic value)
2. Relationship map summary
3. Open opportunities (opportunity_context)
4. Service posture (service_context)
5. Buying signals and risks
6. Recommended research questions
7. Missing data and assumptions

## Anti-Patterns

- Long narrative without structured OUTPUT_SCHEMA fields
- Org charts invented when contacts are sparse
- Buying signals without CRM evidence
- Ignoring open P1/P2 cases in service_context
- Generic discovery questions not tied to account gaps

## Coaching Style

- **Evidence first:** "3 open opps totaling $420K; largest is Expansion FY26 at Proposal stage."
- **Gap explicit:** "No economic buyer contact tagged — recommend confirming with champion."
- **Actionable questions:** SPIN Need-payoff questions tied to identified pain in cases or opp notes.
