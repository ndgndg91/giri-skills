# CI/CD & Deployment Guide (EKS Focus)

## 1. Containerization Strategy
- **Build Tool**: Use **Cloud Native Buildpacks (CNB)** via Spring Boot's `bootBuildImage` or a **Multi-stage Dockerfile**.
- **Base Image**: Use **Distroless** (e.g., `gcr.io/distroless/java25`) or **Alpine** for the final runtime image to minimize attack surface and image size.
- **Layer Optimization**: Order Dockerfile commands from least to most frequently changed to maximize layer caching.

## 2. CI Pipeline (GitHub Actions)
- **Quality Gates**: Every PR must pass:
  - Unit & Integration tests (including Testcontainers).
  - Static analysis (e.g., SonarQube, ArchUnit).
  - Vulnerability scanning (e.g., Trivy, Snyk) for dependencies and images.
- **Registry**: Push images to **Amazon ECR** with immutable tags (e.g., `sha-{git-commit-hash}`).

## 3. CD & GitOps (ArgoCD)
- **Deployment Pattern**: Use **GitOps** with **ArgoCD**. The infrastructure state (Helm charts or K8s manifests) should be managed in a separate "git-ops" repository.
- **Configuration Management**: Use **Helm** to manage environment-specific configurations (Dev, Staging, Prod).
- **Secrets**: Never store secrets in Git. Use **AWS Secrets Manager** or **HashiCorp Vault** integrated via **External Secrets Operator**.

## 4. Deployment Strategies
- **Zero-Downtime**: Always use **Rolling Updates** at a minimum.
- **Advanced Strategies**:
  - **Canary**: Shift a small percentage of traffic to the new version and monitor metrics (via Datadog) before full rollout.
  - **Blue-Green**: Switch traffic between two identical environments for instant rollback capability.
- **Rollback**: Automate rollbacks based on error rate or latency spikes detected during Canary/Rolling updates.

## 5. EKS Integration
- **IRSA (IAM Roles for Service Accounts)**: Use IRSA to grant the Pods only the necessary AWS permissions.
- **Resource Limits**: Define precise CPU/Memory requests and limits based on performance testing to enable effective HPA (Horizontal Pod Autoscaler) and KEDA.
