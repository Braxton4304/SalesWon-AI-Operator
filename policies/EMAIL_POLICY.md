# Email Policy

Implements: [specifications/governance-spec.md](../specifications/governance-spec.md)

## Phase 1 Rules

- All agent-generated email is **draft_only**
- Human must review and send from ServiceNow or approved client
- No autonomous send under any Digital Employee authority level

## Draft Requirements

- Subject + body required
- No internal CRM jargon in customer-facing drafts
- Follow [shared/EMAIL_STYLE_GUIDE.md](../shared/EMAIL_STYLE_GUIDE.md)
- Link related case/opportunity in internal metadata only

## Retention

- Drafts logged in audit per governance-spec
- Sent emails: ServiceNow is source of truth
- Agent short memory: do not persist full draft bodies beyond session

## Approval

Per [APPROVAL_POLICY.md](APPROVAL_POLICY.md): rep or CS agent drafts → human sends.

```yaml
policy_id: email
phase_1_send: human_only
draft_authority: agents with AUTHORITY.draft including customer_email
retention_audit: required
```
