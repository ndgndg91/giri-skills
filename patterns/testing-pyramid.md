# Testing Pyramid & QA Strategy

## 1. The Testing Pyramid
- **Unit Tests (High Volume)**: Test individual functions and domain logic in isolation. Fast and reliable. Aim for high coverage in the `Domain` layer.
- **Integration Tests (Moderate Volume)**: Verify interaction between layers and external systems using **Testcontainers** (DB, Kafka, Redis).
- **E2E Tests (Low Volume)**: Test critical user journeys from the API gateway to the database.

## 2. Specialized Testing
- **Property-Based Testing**: Use for complex logic to automatically test a wide range of input values and edge cases.
- **Contract Testing (Pact)**: Essential for maintaining compatibility between microservices.
- **ArchUnit**: Automated tests to enforce architectural boundaries and rules.

## 3. Quality Assurance
- Tests must be part of the CI pipeline.
- Failed tests must block the deployment.
- Aim for **"Flaky-free"** tests by ensuring isolation and proper resource cleanup.
