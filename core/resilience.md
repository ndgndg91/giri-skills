# Resilience & Stability Guide

## 1. Fault Tolerance Patterns
- **Circuit Breaker**: Use libraries like **Resilience4j** to prevent cascading failures when external services are down.
- **Bulkhead**: Isolate resources (e.g., separate connection pools for different services) to ensure that a failure in one area doesn't exhaust system-wide resources.
- **Retry**: Implement retries with **exponential backoff** for transient failures, but avoid retrying on 4xx errors.

## 2. Timeout & Resource Tuning
- **Explicit Timeouts**: **Never use default timeouts.** Always specify `connect-timeout` and `read-timeout` for all external calls (HTTP, DB, Redis).
- **Connection Pool Tuning (HikariCP)**: 
  - Tune `maximum-pool-size` based on DB capacity and concurrency.
  - Set `connection-timeout` and `max-lifetime` appropriately to prevent "connection leaked" or stale connection issues.

## 3. Lifecycle Management
- **Graceful Shutdown**: Enable graceful shutdown to allow in-flight requests to complete before the application process terminates.
- **Warm-up Strategy**: For cloud environments (EKS), implement a warm-up process (e.g., pre-loading classes, pre-establishing connection pools) to prevent latency spikes on the first few requests to a new Pod.

## 4. Scaling & Performance
- **Auto-scaling (KEDA/HPA)**: Ensure the application metrics (CPU, Memory, or Custom Metrics) accurately reflect load for effective auto-scaling.
- **Throttling**: Apply server-side throttling to protect the system from unexpected traffic surges.
