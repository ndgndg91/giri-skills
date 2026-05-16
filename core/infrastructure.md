# Infrastructure & Messaging Guide

## 1. Storage Selection Criteria
- **RDB (MySQL/PostgreSQL)**: Complex relationships, strict ACID, normalized data.
- **NoSQL (MongoDB/DynamoDB)**: Flexible schemas, high throughput, denormalized documents.
- **NewSQL**: Strong consistency + Horizontal scalability.
- **Redis**: Caching, Distributed Locks (Redisson), Session, Rate Limiting.

## 2. JVM & Container Runtime (EKS/cgroup v2)
### 2.1. Container Support & Memory
- **cgroup v2 Compatibility**: Use Java 17+ (or 11.0.16+) for proper cgroup v2 resource detection. Ensure `-XX:+UseContainerSupport` is enabled (default in modern JVMs).
- **Memory Settings**: Avoid fixed `-Xmx`. Use percentage-based settings to adapt to container limits:
  - `-XX:MaxRAMPercentage=75.0` (Allow some overhead for metaspace, threads, and OS).
  - `-XX:InitialRAMPercentage=75.0` (To avoid heap resizing overhead).
- **OOM Handling**: Use `-XX:+ExitOnOutOfMemoryError` or `-XX:+CrashOnOutOfMemoryError` to let Kubernetes restart the Pod immediately on OOM.

### 2.2. Garbage Collection (GC) Strategy
- **G1GC**: Default for most applications. Good balance between throughput and latency.
- **ZGC (Java 17+)**: Use for low-latency requirements (sub-millisecond pauses).
- **Generational ZGC (Java 21+)**: Significantly improved throughput and memory efficiency over standard ZGC.

## 3. Apache Kafka Guide (Producer & Consumer)
### 3.1. Producer Configuration
- **Idempotent Producer**: `enable.idempotence=true`, `acks=all`.
- **Ordering**: `max.in.flight.requests.per.connection <= 5`.
### 3.2. Consumer Configuration
- **Auto Commit**: Disable (`enable.auto.commit=false`). Use manual `AckMode.MANUAL_IMMEDIATE`.
- **Idempotency**: Consumers MUST be idempotent using business keys.

## 4. Consistency & Reliability Patterns
- **Transactional Outbox Pattern**: Guarantee atomicity between DB and Kafka.
- **Idempotency**: Design for At-Least-Once delivery.
- **Circuit Breaker**: Use Resilience4j for external calls.

## 5. Storage-Specific Tuning
- **MongoDB**: Set `serverSelectionTimeout`, tune connection pools.
- **RDB**: Tune HikariCP (`maximum-pool-size`, `max-lifetime`).

## 6. Connectivity & Security
- **Timeouts**: Mandatory `Connect` and `Read` timeouts.
- **IAM**: Use IAM roles/Service Accounts (IRSA in EKS).
