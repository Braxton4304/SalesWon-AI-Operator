# Long Memory

Preference and organizational context scoped to individual rep. No customer PII export beyond session needs.

## Rep Preferences

- Preferred coaching detail level (concise vs. detailed qualification audits)
- Default meeting prep format (bullets vs. narrative)
- Frequently referenced opps (pinned by rep)
- Preferred methodology emphasis (MEDDIC-heavy vs. SPIN discovery style)
- Won/lost reason patterns rep cares about (aggregated, no customer PII export)
- Email draft tone preference (formal vs. conversational per EMAIL_STYLE_GUIDE)

## Org Memory (Layer 4)

- Stage definitions and exit criteria
- Product SKU list for qualification
- Discount approval matrix reference (read-only — escalate on discount requests)
- Forecast category definitions for rep's team
- MEDDIC field mapping to ServiceNow opportunity attributes (when configured)

## Learning Signals (Phase 2)

- Accepted vs. rejected next_best_action recommendations
- suggested_follow_up edit patterns
- recommended_questions usage in subsequent activities
- Qualification gap closure rate after coaching

## Boundaries

- Long memory does not override CRM — always re-query for opportunity_summary
- Manager rep_coaching_items stored only when rep explicitly references in session
- No autonomous sync with Sales Manager Agent artifacts

```yaml
memory_long_version: "1.1.0"
agent_id: sales-rep
scope: rep_preference
crm_authoritative: true
```
