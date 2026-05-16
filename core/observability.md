# Observability Guide

## 1. APM & Monitoring (Datadog)
- **Standard**: Use **Datadog** as the primary platform for APM (Application Performance Monitoring), Distributed Tracing, and Unified Logging.
- **Tracing**: Ensure all services are instrumented to propagate `traceId` for end-to-end visibility.
- **Dashboards**: Monitor key metrics: Latency (p95, p99), Throughput (RPS), Error Rate, and Resource Usage (CPU/Mem).

## 2. Metrics & Health Checks (Spring Boot Actuator)
- **Actuator**: Enable `Spring Boot Actuator` for all services.
- **Endpoints**:
  - `/actuator/health`: Use for L7 health checks and Kubernetes Readiness/Liveness probes.
  - `/actuator/metrics`: Expose JVM, Connection Pool, and Custom business metrics for Prometheus/Datadog scraping.
- **Custom Metrics**: Register critical business events (e.g., "Order Processed") as Micrometer counters/timers.

## 3. Logging Strategy
- **Format**: Use **JSON format** for logs to ensure compatibility with log aggregators (Datadog, ELK).
- **Correlation**: Every log entry must include the **`traceId`**.
- **Log Levels**:
  - **ERROR**: Immediate action required. Includes stack traces.
  - **WARN**: Unexpected but recoverable situation.
  - **INFO**: Significant business milestones or lifecycle events.
  - **DEBUG/TRACE**: Detailed info for troubleshooting (Disabled in production).

## 4. Alerting
- Set up alerts for:
  - Error rate spikes.
  - P99 latency exceeding SLAs.
  - Infrastructure saturation (e.g., high CPU/Memory/Disk usage).
  - Failed health checks.
