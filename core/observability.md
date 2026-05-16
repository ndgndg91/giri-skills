# Observability Guide

## 1. APM & Monitoring (Datadog)
- **Standard**: Use **Datadog** as the primary platform for APM, Distributed Tracing, and Unified Logging.
- **Tracing**: Propagate `traceId` (W3C traceparent) across all service boundaries.

## 2. Metrics & Health Checks (Spring Boot Actuator)
- **Port Separation**: **Always separate the management port** (e.g., 8081) from the application serving port (e.g., 8080) using `management.server.port`.
  - **Security**: Prevent sensitive endpoints (env, configprops, heapdump) from being exposed to the public internet via the main load balancer.
  - **Stability**: Ensure health checks and metrics remain accessible even if the main application thread pool is exhausted.
- **Kubernetes Probes**:
  - **Liveness**: `/actuator/health/liveness`
  - **Readiness**: `/actuator/health/readiness`
- **Configuration**: Ensure `management.endpoint.health.probes.enabled=true` is set.

## 3. Logging Strategy
- **Format**: Use **JSON format** for structured logging.
- **Correlation**: Every log entry must include the **`traceId`**.
- **Log Levels**: ERROR, WARN, INFO, DEBUG.

## 4. Alerting & Dashboards
- Monitor Error Rate, Latency (p99), and Infrastructure saturation.
- Set up alerts for failed Liveness/Readiness probes.
