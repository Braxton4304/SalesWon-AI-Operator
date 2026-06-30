# Security Policy

Implements: [specifications/governance-spec.md](../specifications/governance-spec.md), [runtime/SECURITY.md](../runtime/SECURITY.md)

- No secrets in source control — Azure Key Vault
- Managed Identity preferred
- Tenant isolation on every data path
- Frontend never passes trusted tenant_id
- ServiceNow ACL respected for all CRM reads

```yaml
policy_id: security
secrets_in_source: forbidden
tenant_isolation: required
credential_store: azure_key_vault
```
