# Spring Boot Style Guide (Kotlin & Pragmatic DDD)

## 1. 4-Layered Architecture
- **Interfaces (Web)**: Entry point for external systems. Handles DTO mapping and request/response.
- **Application**: Orchestrates business use cases. Manages transactions, distributed locks, and cache coordination.
- **Domain**: Pure business logic (Entities, VOs, Domain Services). No dependency on frameworks or infrastructure.
- **Infrastructure**: Technical implementations (JPA, Redis, External Clients).

## 2. JPA Entity vs Domain Entity Strategy
### Basic Principle: Pragmatic Unified Model
- By default, use **JPA Entity as Domain Entity** for productivity.
- Use Kotlin's `all-open` plugin to support JPA proxying.

### When to Separate
- **Schema Mismatch**: DB structure differs significantly from the domain model.
- **Domain Pollution**: Persistence concerns overwhelm business logic.
- **Multiple Data Sources**: Data combined from multiple sources (DB, APIs).

## 3. Distributed Lock Strategy (Redis/Redisson)
- **AOP-First**: Use custom annotations (e.g., `@DistributedLock`) for standard cases to maintain clean business logic.
- **Programmatic Fallback**: Use `RedissonClient` or a `LockTemplate` when keys are dynamic/complex or when multiple locks require fine-grained orchestration.
- **Transaction Rule**: Acquire the lock **before** starting a transaction and release it **after** the transaction commits to ensure data consistency across threads.

## 4. Caching Strategy (Redis & Caffeine)
- **Abstraction-First**: Use Spring Cache (`@Cacheable`, `@CacheEvict`) for simple Look-aside patterns.
- **Manual Control**: Use `RedisTemplate` or specialized `CacheRepository` for complex TTL management, bulk operations, or data-specific serialization needs.
- **Pattern**: Prefer **Cache-Aside** for reads. Evict or update cache on writes.

## 5. Implementation Standards (Kotlin)
- **No Lombok**: Use native Kotlin features (data classes, named arguments).
- **Constructor Injection**: Preferred over field injection.
- **Validation**: Use Bean Validation with Kotlin field targets (`@field:NotBlank`).

## 6. Testing Strategy
- **JUnit 5 & MockK**: Standard for unit testing.
- **Testcontainers**: Use for integration tests to ensure compatibility with real DB/Redis environments.
- **Slice Testing**: `@WebMvcTest`, `@DataJpaTest` with Testcontainers for focused verification.
