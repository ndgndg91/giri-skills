# Infrastructure & Messaging Guide

## 1. Storage Selection Criteria
- **RDB (MySQL/PostgreSQL)**: Complex relationships, strict ACID, normalized data.
- **NoSQL (MongoDB/DynamoDB)**: Flexible schemas, high throughput, denormalized documents.
- **NewSQL**: Strong consistency + Horizontal scalability.
- **Redis**: Caching, Distributed Locks (Redisson), Session, Rate Limiting.

## 2. Advanced Scalability Strategies

### 2.1. RDB Table Partitioning
- **When to use**: When a table grows too large (e.g., hundreds of millions of rows) causing performance degradation in indexing and vacuuming.
- **Range Partitioning**: Best for time-series data (e.g., `orders_2024_05`). Enables **partition pruning** for queries and easy archival (dropping old partitions).
- **Hash/List Partitioning**: Use when data doesn't have a clear range but needs to be distributed across physical files for I/O performance.

### 2.2. NoSQL Sharding (MongoDB Focus)
- **Shard Key Selection**: The most critical decision for horizontal scaling.
  - **High Cardinality**: Choose a key with many unique values to allow fine-grained distribution.
  - **Even Distribution**: Avoid monotonically increasing keys (like plain timestamps) for high-write workloads to prevent **Hot Shards**.
  - **Query Pattern Alignment**: Include the shard key in frequent queries to avoid "broadcast" (scatter-gather) queries across all shards.
- **Hashed Sharding**: Use when you need perfectly even distribution and don't require range queries on the shard key.

## 3. JVM & Container Runtime (EKS/cgroup v2)
### 3.1. Container Support & Memory Tuning
- **Heap vs. Native Memory**: Use `-XX:MaxRAMPercentage=70.0` to leave space for Direct Memory (Kafka Zero-copy) and OS cache.
- **OOM Handling**: Use `-XX:+ExitOnOutOfMemoryError`.

### 3.2. Garbage Collection (GC) Strategy
- **Generational ZGC (Java 21+)**: Standard for modern low-latency LTS services.

## 4. Apache Kafka Guide (Producer & Consumer)
- **Producer**: `enable.idempotence=true`, `acks=all`.
- **Consumer**: Manual commit (`enable.auto.commit=false`), Idempotent processing.

## 5. Consistency & Reliability Patterns
- **Transactional Outbox Pattern**: Guarantee atomicity between DB and Kafka.
- **Idempotency**: Design for At-Least-Once delivery.
- **Circuit Breaker**: Use Resilience4j for external calls.

## 6. Storage-Specific Tuning
- **MongoDB**: Set `serverSelectionTimeout`, tune connection pools.
- **RDB**: Tune HikariCP (`maximum-pool-size`, `max-lifetime`).

## 7. Connectivity & Security
- **Timeouts**: Mandatory `Connect` and `Read` timeouts.
- **IAM**: Use IRSA in EKS; avoid hardcoding credentials.
