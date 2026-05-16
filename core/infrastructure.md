# Infrastructure & Messaging Guide

## 1. Storage Selection Criteria
- **RDB (MySQL/PostgreSQL)**: Complex relationships, strict ACID, normalized data.
- **NoSQL (MongoDB/DynamoDB)**: Flexible schemas, high throughput, denormalized documents.
- **NewSQL**: Strong consistency + Horizontal scalability.
- **Redis**: Caching, Distributed Locks (Redisson), Session, Rate Limiting.

## 2. Apache Kafka Guide (Producer & Consumer)

### 2.1. Producer Configuration (Idempotency & Ordering)
- **Idempotent Producer**: Always set `enable.idempotence=true` to prevent duplicate messages during retries.
- **Acks**: Set `acks=all` for maximum durability.
- **Ordering**: Ensure `max.in.flight.requests.per.connection <= 5` (with idempotence) to maintain partition-level order.
- **Batching**: Tune `linger.ms` and `batch.size` to balance latency and throughput.

### 2.2. Consumer Configuration (Reliability & Performance)
- **Auto Commit**: **Disable auto-commit** (`enable.auto.commit=false`). Use manual acknowledgment (e.g., `AckMode.MANUAL_IMMEDIATE` in Spring Kafka) to ensure "At-Least-Once" delivery.
- **Listener Types**:
  - **Record Listener**: Best for simple, independent message processing.
  - **Batch Listener**: Best for high-throughput scenarios where processing messages in chunks is more efficient.
- **Idempotent Consumer**: Since Kafka guarantees "At-Least-Once", consumers **MUST** be idempotent. Use a unique business key (e.g., `eventId`, `orderId`) to de-duplicate processed messages in the DB/Cache.

### 2.3. Error Handling & Resilience
- **Retries**: Implement exponential backoff for transient errors.
- **DLQ (Dead Letter Queue)**: Use a DLQ for non-recoverable errors to prevent the consumer from getting stuck (Poison Pill).
- **Outbox Pattern**: Use the **Transactional Outbox Pattern** to ensure atomicity between DB updates and Kafka publishing.

## 3. Storage-Specific Tuning
- **MongoDB**: Explicitly set `serverSelectionTimeout` and tune connection pool sizes.
- **RDB**: Optimize indexing for query performance and use connection pooling (HikariCP) with proper timeouts.

## 4. Connectivity & Security
- **Timeouts**: Mandatory `Connect` and `Read` timeouts for all infrastructure clients.
- **IAM**: Use IAM roles or secret managers; avoid hardcoding credentials.
