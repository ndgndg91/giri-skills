# Centralized Configuration & Secret Management

## 1. Centralized Configuration (Spring Cloud Config)
- **Standard**: Use **Spring Cloud Config** to manage application properties across different environments from a central repository (Git, HashiCorp Vault, or S3).
- **Dynamic Refresh**: Use `@RefreshScope` for beans that need to update their configuration at runtime without a full application restart.
- **Fail-fast**: Configure applications to fail fast if the config server is unavailable during startup to prevent misconfigured instances.

## 2. Secret Management (AWS Secrets Manager / Vault)
- **Standard**: Never store sensitive data (DB passwords, API keys, Private keys) in plaintext within Git or configuration files.
- **AWS Secrets Manager**: Recommended for applications running on AWS/EKS. Integrate using **Spring Cloud AWS Secrets Manager** or **External Secrets Operator (ESO)**.
- **HashiCorp Vault**: Use for advanced features like dynamic secrets, fine-grained access control, and multi-cloud environments.
- **Environment Separation**: Maintain separate secret stores/paths for each environment (Dev, Staging, Prod).

## 3. Kubernetes Integration (External Secrets Operator)
- **Standard**: Use the **External Secrets Operator (ESO)** to synchronize secrets from AWS Secrets Manager or Vault into Kubernetes native `Secret` objects.
- **Benefit**: Decouples the application from specific secret management APIs and allows using standard K8s environment variables or volume mounts.

## 4. Best Practices
- **Placeholders**: Use placeholders in `application.yml` (e.g., `password: ${DB_PASSWORD}`) and inject values via Environment Variables or Secret Stores.
- **Audit Logs**: Enable auditing for secret access to track who accessed which secret and when.
- **Rotation**: Implement automatic secret rotation for database passwords and API keys where supported.
