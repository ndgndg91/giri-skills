# CI/CD & Deployment Guide (EKS Focus)

## 1. Infrastructure as Code (Terraform)
- **Standard**: Use **Terraform** to manage EKS clusters, VPCs, IAM roles, and all cloud resources.
- **State Management**: Use **Remote State** (e.g., S3 + DynamoDB for locking) to enable team collaboration and prevent state corruption.
- **Modularization**: Create reusable Terraform modules for consistent infrastructure patterns across different environments.
- **Security**: Apply the **Principle of Least Privilege** in IAM roles using Terraform. Use **TFLint** and **Checkov** for static analysis.

## 2. Containerization Strategy
- **Build Tool**: Use **Cloud Native Buildpacks (CNB)** or **Multi-stage Dockerfiles**.
- **Base Image**: Use **Distroless** (e.g., `gcr.io/distroless/java25`) for security and minimal footprint.

## 3. CI Pipeline (GitHub Actions)
- **Workflow**: Automated testing, linting, and security scanning on every PR.
- **Image Push**: Build and push immutable images to **Amazon ECR** with Git SHA tags.

## 4. CD & GitOps (ArgoCD & Helm)
- **Packaging**: Use **Helm** for application packaging.
  - Maintain a base Helm chart and use `values.yaml` for environment-specific configurations.
- **GitOps**: Use **ArgoCD** to synchronize the EKS cluster state with the Helm charts stored in the "git-ops" repository.
- **Secrets Management**: Integrate **AWS Secrets Manager** with Kubernetes via **External Secrets Operator (ESO)**.

## 5. Deployment & Stability
- **Strategies**: Implement **Canary** or **Blue-Green** deployments for high-risk changes.
- **EKS Optimization**: 
  - Use **IRSA** for fine-grained IAM permissions for Pods.
  - Configure **HPA/KEDA** based on metrics from Datadog or Prometheus.
  - Implement **Graceful Shutdown** and **Warm-up** logic (as defined in the Resilience guide).
