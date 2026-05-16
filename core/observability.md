# Observability Guide

## 1. APM & Monitoring (Datadog)
- **Standard**: Use **Datadog** as the primary platform for APM, Distributed Tracing, and Unified Logging.
- **Tracing**: Propagate `traceId` (W3C traceparent) across all service boundaries.

## 2. Metrics & Health Checks (Spring Boot Actuator)
- **Actuator**: Enable `Spring Boot Actuator` for all services.
- **Kubernetes Probes**:
  - **Liveness**: `/actuator/health/liveness` - Indicates if the app is alive. Kubernetes restarts the Pod if this fails.
  - **Readiness**: `/actuator/health/readiness` - Indicates if the app is ready to accept traffic. Kubernetes removes the Pod from Service load balancers if this fails.
- **Configuration**: Ensure `management.endpoint.health.probes.enabled=true` is set (automatically enabled in Kubernetes environments).
- **Custom Metrics**: Expose business-critical metrics via Micrometer and monitor via Datadog.

## 3. Logging Strategy
- **Format**: Use **JSON format** for structured logging.
- **Correlation**: Every log entry must include the **`traceId`**.
- **Log Levels**: Standardize on ERROR, WARN, INFO, and DEBUG. Ensure sensitive data is never logged.

## 4. Alerting & Dashboards
- Monitor Error Rate, Latency (p99), and Infrastructure saturation.
- Set up alerts for failed Liveness/Readiness probes and high circuit breaker open rates.
