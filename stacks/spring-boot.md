# Spring Boot Style Guide (Kotlin 2 & Spring Boot 4 & JDK 25 LTS)

## 1. Modern Runtime & Framework Versioning
- **JDK Version**: **JDK 25 (LTS)**.
- **Kotlin Version**: **Kotlin 2.x** (K2 compiler).
- **Spring Boot**: **Spring Boot 4.x (LTS)**.

## 2. Web Server (WAS) Selection
- **Standard**: **Tomcat**. Most mature and has excellent integration with Virtual Threads in Spring Boot 4.
- **High Performance**: **Undertow**. Recommended for scenarios requiring minimal memory footprint and maximum raw throughput.
- **Reactive**: **Netty**. Use only when adopting the Spring WebFlux (Reactive) paradigm.

## 3. Advanced Concurrency (Virtual Threads)
- **Standard**: `spring.threads.virtual.enabled=true`.
- **Thread Pinning Caution**: Avoid using `synchronized` blocks for long-running I/O or blocking operations. Use `ReentrantLock` to prevent virtual threads from pinning to carrier threads.
- **Thread Pool Tuning**: With Virtual Threads, traditional worker thread pool (`max-threads`) tuning is secondary. Focus on resource constraints (DB connections, memory) instead.

## 4. 4-Layered Architecture & DDD
- Maintain strict boundaries between **Interfaces, Application, Domain, and Infrastructure**.

## 5. Infrastructure Tuning (JDK 25 Optimized)
- **GC**: **Generational ZGC** for low-latency.
- **Memory**: `-XX:MaxRAMPercentage=70.0` to accommodate Direct Memory (Kafka/NIO).
- **MongoDB**: `serverSelectionTimeout` tuning.
- **HTTP Clients**: Mandatory Connect/Read timeout and connection pooling.

## 6. Implementation Standards (Kotlin 2)
- **K2 Compiler**: Improved smart casts and compilation speed.
- **Serialization**: `kotlinx-serialization` for high performance.
- **Validation**: Bean Validation with Kotlin field targets.

## 7. Testing & Quality
- **JUnit 5 & MockK**.
- **Testcontainers**: Mandatory for all infrastructure-related integration tests.
- **ArchUnit**: Enforce architectural constraints through code.
