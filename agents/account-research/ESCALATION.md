# Escalation

Role-specific escalation rules. Mandatory triggers from [shared/escalation-framework.md](../../shared/escalation-framework.md) always apply.

## Mandatory Escalation

| Condition | Route To |
|-----------|----------|
| Confidence < 0.60 after 3 retrieve attempts | Account executive or sales manager |
| Strategic/tier-1 account with confidence < 0.70 after retrieval | Account team lead |
| Legal, compliance, or hostile communication keyword | Legal contact + manager (Layer 4) |
| User says "speak to a human" | Next available account team member |
| Write blocked by data-spec (account update request) | Human with CRM write access |
| Customer executive complaint on active strategic account | Manager + CS liaison |

## Conditional Escalation

| Condition | Route To |
|-----------|----------|
| Multiple P1 cases + active renewal/expansion opp | CS manager + account executive |
| Conflicting CRM data (opp owner vs. account team mismatch) | Sales ops |
| Request for external market/competitive intel beyond KB | Research analyst (human) |
| Account ownership dispute | Sales ops |

## Escalation Payload

Include per escalation-framework:

- Original user request
- account_id and account_name if resolved
- Partial account_brief if constructed
- Confidence score and blocking reason
- source_records gathered
- missing_data list
- Suggested assignee role (from Layer 4 contacts)

## Output

`decision_action: escalate` with routing suggestion in `recommended_action` or summary narrative.

## Layer 4 Configuration

Customer-specific escalation contacts, strategic account lists, and ServiceNow assignment groups — not in this repo.
