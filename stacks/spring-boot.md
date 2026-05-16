# Spring Boot Style Guide (Kotlin & Pragmatic DDD)

## 1. 4-Layered Architecture
- **Interfaces (Web)**: Entry point for external systems. Handles DTO mapping and request/response.
- **Application**: Orchestrates business use cases. Manages transactions, distributed locks, and cache coordination.
- **Domain**: Pure business logic (Entities, VOs, Domain Services). No dependency on frameworks or infrastructure.
- **Infrastructure**: Technical implementations (JPA, Redis, External Clients).

## 2. Modern Runtime (Virtual Threads)
- **Standard**: Enable **Virtual Threads** (`spring.threads.virtual.enabled=true`) for applications running on Java 21+.
- **Benefits**: Simplifies concurrency by allowing a blocking-style programming model while maintaining high scalability.
- **Precaution**: Avoid long-running synchronized blocks to prevent thread pinning. Use `ReentrantLock` if necessary.

## 3. Infrastructure Tuning

### 3.1. Connection Pools (HikariCP)
- Always tune `maximum-pool-size`, `connection-timeout`, and `max-lifetime` based on production load.

### 3.2. MongoDB (Spring Data Mongo)
- **Server Selection**: Explicitly configure `serverSelectionTimeout` to prevent long waits during cluster failover.
- **Connection Pool**: Monitor and tune `max-connection-pool-size` and `min-connection-pool-size`.

### 3.3. HTTP Clients (RestClient, WebClient, Feign)
- **Timeouts**: Mandatory configuration of `Connect Timeout` and `Read Timeout`.
- **Connection Pooling**: Use pooled connection managers (e.g., Apache HttpClient or Jetty Client) to reuse connections and avoid socket exhaustion.

## 4. JPA Entity vs Domain Entity Strategy
### Basic Principle: Pragmatic Unified Model
- By default, use **JPA Entity as Domain Entity**. Use Kotlin's `all-open` plugin.

### When to Separate
- **Schema Mismatch**, **Domain Pollution**, or **Multiple Data Sources**.

## 5. Distributed Lock & Cache
- **Distributed Lock**: AOP-First with Redisson. Ensure lock acquisition happens outside the transaction.
- **Cache**: Spring Cache for simple cases, `RedisTemplate` for complex logic. Use **Cache-Aside** pattern.

## 6. Testing Strategy
- **JUnit 5 & MockK** for unit tests.
- **Testcontainers** for integration tests (DB, Redis, Mongo, Kafka).
- **Slice Testing**: `@WebMvcTest`, `@DataJpaTest`, `@DataMongoTest`.
