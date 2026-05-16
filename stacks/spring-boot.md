# Spring Boot Style Guide (Kotlin 2 & JDK 25 LTS)

## 1. Modern Runtime & Versioning
- **JDK Version**: Use **JDK 25 (LTS)** as the standard.
- **Kotlin Version**: Use **Kotlin 2.x** with the **K2 compiler** for improved performance and smart cast logic.
- **Spring Boot**: Use the latest 3.x or 4.x (compatible with JDK 25).

## 2. Advanced Concurrency (JDK 25+)
- **Virtual Threads**: Enabled by default (`spring.threads.virtual.enabled=true`).
- **Structured Concurrency**: Use for managing multiple sub-tasks as a single unit of work to improve error handling and observability.
- **Scoped Values**: Prefer over `ThreadLocal` for sharing immutable data between threads efficiently, especially with virtual threads.

## 3. 4-Layered Architecture
- **Interfaces (Web)**, **Application**, **Domain**, **Infrastructure** as defined in the core patterns.

## 4. Infrastructure Tuning (Optimized for Java 25)
- **Generational ZGC**: Recommended GC for high-throughput and low-latency requirements on JDK 25.
- **Memory Management**: Use `-XX:MaxRAMPercentage=75.0` to respect container limits in EKS.

## 5. Implementation Standards (Kotlin 2)
- **K2 Compiler Features**: Leverage improved smart casts and faster compilation.
- **No Lombok**: Native Kotlin primary constructors and data classes.
- **Functional Style**: Use scope functions (`let`, `run`, `apply`, `also`) and immutable collections.

## 6. Distributed Lock & Cache
- **Distributed Lock**: AOP-First with Redisson.
- **Cache**: Look-aside pattern with Spring Cache or `RedisTemplate`.

## 7. Testing Strategy
- **JUnit 5 & MockK**.
- **Testcontainers**: Mandatory for integration tests (DB, Redis, Mongo, Kafka).
- **Virtual Thread Testing**: Ensure tests are executed in a virtual thread environment to catch pinning issues.
