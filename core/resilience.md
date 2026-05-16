# Resilience & Stability Guide

## 1. Fault Tolerance Patterns
- **Circuit Breaker**: Prevent cascading failures using Resilience4j.
- **Bulkhead**: Isolate resources to prevent system-wide exhaustion.
- **Retry**: Use exponential backoff for transient failures.

## 2. Cache Stability (Anti-Cache Stampede)
To prevent the **Cache Stampede** effect (where multiple requests hit the DB simultaneously after cache expiry), apply the following strategies:
- **Distributed Lock**: Use a lock (e.g., Redisson) to ensure only one thread/instance updates the cache from the DB at a time.
- **Jitter (Random TTL)**: Add a small random variation to cache TTLs to prevent multiple keys from expiring at the exact same time.
- **Probabilistic Early Recomputation (PER)**: Recompute the cache slightly before it expires based on a probability function.
- **Soft Expiry**: Return stale data for a short period while the cache is being refreshed in the background.

## 3. Timeout & Resource Tuning
- **Explicit Timeouts**: Mandatory `connect-timeout` and `read-timeout` for all external calls.
- **Connection Pool Tuning**: Optimize HikariCP (`maximum-pool-size`, `max-lifetime`).

## 4. Lifecycle Management
- **Graceful Shutdown**: Allow in-flight requests to complete before termination.
- **Warm-up Strategy**: Pre-load classes and connection pools for EKS Pods.

## 5. Scaling & Performance
- **Auto-scaling (KEDA/HPA)**: Use accurate metrics for scaling.
- **Throttling**: Protect systems from traffic surges.
