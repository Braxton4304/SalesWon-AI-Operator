# Security

Implements: [specifications/governance-spec.md](../specifications/governance-spec.md)

## Principles

- **No secrets in source control** — Azure Key Vault only
- **Managed Identity** preferred over connection strings
- **Least-privilege RBAC** on every Azure resource
- **Tenant isolation** — mandatory on every data path

## Tenant Isolation

- Every SQL table with tenant data includes `tenant_id`
- Every query filters by resolved tenant from authenticated principal
- Frontend **never** passes `tenant_id` as a trusted value
- Vector indexes, blob keys, and queue messages scoped by tenant

## Authentication

- Entra ID / SSO for user-facing apps (TBD — ADR)
- Service-to-service via Managed Identity
- ServiceNow OAuth for CRM connector

## Data Classification

| Class | Handling |
|-------|----------|
| Public | May appear in logs |
| Internal | Redact in user-visible logs |
| Confidential | Encrypt at rest; minimal logging |
| PII | Mask in audit unless compliance requires |

Customer-specific classification rules are Layer 4 configuration.

## ServiceNow ACL Alignment

CRM visibility MUST respect ServiceNow ACLs and data-spec `ownership_rule` / `visibility_rule`.

## Machine-Readable Contract

```yaml
implements: governance-spec
secrets_in_source: forbidden
credential_store: azure_key_vault
identity: managed_identity_preferred
tenant_isolation: required
frontend_trusted_tenant_id: forbidden
```
