# Infrastructure & Messaging Guide

## 1. Storage Selection Criteria
- **RDB (MySQL/PostgreSQL)**: Complex relationships, strict ACID, normalized data.
- **NoSQL (MongoDB/DynamoDB)**: Flexible schemas, high throughput, denormalized documents.
- **NewSQL**: Strong consistency + Horizontal scalability.
- **Redis**: Caching, Distributed Locks (Redisson), Session, Rate Limiting.

## 2. JVM & Container Runtime (EKS/cgroup v2)
### 2.1. Container Support & Memory Tuning
- **cgroup v2 Compatibility**: Use Java 17+ for proper resource detection.
- **Heap vs. Native Memory**:
  - Use **`-XX:MaxRAMPercentage=70.0`** (instead of 75.0) for heavy Kafka/NIO workloads to leave enough space for **Direct Memory** and **OS Page Cache**.
  - **Zero-copy Optimization**: Kafka leverages zero-copy via Java NIO. Explicitly monitor and tune **`-XX:MaxDirectMemorySize`** if OOM occurs despite sufficient Heap.
- **OOM Handling**: Use `-XX:+ExitOnOutOfMemoryError` to ensure fast recovery via Kubernetes restarts.

### 2.2. Garbage Collection (GC) Strategy
- **Generational ZGC (Java 21+)**: Best for low-latency and high-throughput balance on modern LTS versions.

## 3. Apache Kafka Guide (Producer & Consumer)
### 3.1. Producer Configuration
- **Idempotent Producer**: `enable.idempotence=true`, `acks=all`.
- **Ordering**: `max.in.flight.requests.per.connection <= 5`.

### 3.2. Consumer Configuration
- **Auto Commit**: Disable (`enable.auto.commit=false`). Use manual `AckMode.MANUAL_IMMEDIATE`.
- **Memory Awareness**: Be aware that consumers use **Direct Memory** for buffer management during high-throughput message consumption.
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
