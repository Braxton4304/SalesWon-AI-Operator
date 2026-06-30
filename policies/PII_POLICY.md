# PII Policy

## Classification

| Class | Logging | Outputs |
|-------|---------|---------|
| Public | Allowed | Allowed |
| Internal | Redact in user logs | Allowed |
| Confidential | Minimal | Mask if not required |
| PII | Mask by default | Only when necessary for task |

## Rules

- No PII in aggregate organizational memory
- User long memory scoped to single user — never cross-user
- Audit logs: mask email/phone unless compliance requires full record

```yaml
policy_id: pii
cross_user_memory: forbidden
audit_pii_default: masked
```
