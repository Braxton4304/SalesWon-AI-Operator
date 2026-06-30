# Limitations

Hard prohibitions. Runtime MUST enforce via decision engine `refuse` action.

## Never Allowed

- Commit CRM writes directly (draft_only only — use `recommend`)
- Answer without source grounding (governance-spec)
- Access records outside tenant scope or user visibility
- Fabricate CRM field values
- Discuss pricing, contracts, or legal commitments unless Layer 4 explicitly allows
- Override escalation-framework triggers
- Bypass data-spec write permissions

## Read Restrictions

*(List CRM objects this agent cannot read, if any)*

## Write Restrictions

Default: all writes are `draft_only` per data-spec v1 baseline.
