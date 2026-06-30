# Data Retention Policy

## Retention Periods (Defaults)

| Data | Retention | Storage |
|------|-----------|---------|
| Audit logs | 7 years | Azure SQL audit schema |
| Long memory (user prefs) | 365 days | Azure SQL memory schema |
| Short memory | Session TTL 120 min | Ephemeral |
| CRM cache in runtime | No persistent cache of CRM as SoR | ServiceNow authoritative |

## GDPR

- User deletion requests purge long memory by user_id + tenant_id
- Audit logs: legal hold exceptions per Layer 4

```yaml
policy_id: data_retention
audit_retention_days: 2555
long_memory_retention_days: 365
crm_source_of_truth: servicenow
```
