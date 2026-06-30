# Enterprise Policies

Implements: [specifications/governance-spec.md](../specifications/governance-spec.md)

Agents and runtime **inherit** these policies — never redefine. Authority levels in `AUTHORITY.md` reference relevant policies.

## Policy Index

| Policy | Scope |
|--------|-------|
| [EMAIL_POLICY.md](EMAIL_POLICY.md) | Email draft, review, send, retention |
| [COMMUNICATION_POLICY.md](COMMUNICATION_POLICY.md) | Channels, tone, AI disclosure |
| [SECURITY_POLICY.md](SECURITY_POLICY.md) | Auth, secrets, tenant isolation |
| [DATA_RETENTION.md](DATA_RETENTION.md) | Memory, audit, CRM cache retention |
| [PII_POLICY.md](PII_POLICY.md) | PII in logs, memory, outputs |
| [CUSTOMER_PROMISES.md](CUSTOMER_PROMISES.md) | Prohibited customer commitments |
| [APPROVAL_POLICY.md](APPROVAL_POLICY.md) | Draft → approve → commit workflow |

## Inheritance

```text
policies/ → runtime/GOVERNANCE.md → agents/*/AUTHORITY.md → agents/*/LIMITATIONS.md
```

## Machine-Readable Contract

```yaml
policy_layer_version: "1.0.0"
implements: governance-spec
inheritance: mandatory
override_by_agent: forbidden
```
