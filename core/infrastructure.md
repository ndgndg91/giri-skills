# Infrastructure & Messaging Guide

## 1. Storage Selection Criteria
- **RDB (MySQL/PostgreSQL)**: Use for complex relationships, strict ACID transactions, and normalized data.
- **NoSQL (MongoDB/DynamoDB)**: Use for flexible schemas, high write/read throughput, and denormalized document/Key-Value structures.
- **NewSQL**: Use when both RDB-like strong consistency and NoSQL-like horizontal scalability are required.
- **Redis**: Use for ultra-fast caching, distributed locks, session stores, and rate limiting.

## 2. Messaging & Streaming (Kafka vs Others)
### Apache Kafka: Realities & Trade-offs
- **Partition-Level Ordering**: Kafka guarantees order **ONLY within a partition**, not globally.
- **The Ordering Trade-off**: 
  - To guarantee order, messages must share the same `Partition Key`.
  - **Risk**: This can lead to **Hot Partitions**, where one partition is overwhelmed while others are idle, limiting throughput.
- **Producer Constraints**: For strict ordering, retries must be handled carefully (e.g., using idempotent producers or `max.in.flight.requests.per.connection=1`).
- **Consumer Parallelism**: Parallelism is limited by the number of partitions. One partition can only be consumed by one consumer thread in a group.

## 3. Consistency & Reliability Patterns
- **Transactional Outbox Pattern**: When saving to a DB and publishing a message (e.g., Kafka) simultaneously, use an Outbox table to guarantee atomicity and prevent data loss.
- **Idempotency**: Always design consumers to be idempotent. Messages can be delivered multiple times (At-Least-Once delivery).
- **Circuit Breaker**: Implement circuit breakers for external API or infrastructure calls to prevent cascading failures.

## 4. Operational Considerations
- **Connection Pooling**: Always configure and monitor connection pools (HikariCP, Lettuce) appropriately.
- **Security**: Avoid hardcoded credentials. Use IAM roles or secret managers.
