# Spring Boot Style Guide (Kotlin 2 & Spring Boot 4 & JDK 25 LTS)

## 1. Modern Runtime & Framework Versioning
- **JDK Version**: **JDK 25 (LTS)** is the mandatory runtime.
- **Kotlin Version**: **Kotlin 2.x** with the **K2 compiler**.
- **Spring Boot**: Use **Spring Boot 4.x (LTS)**. 
  - Leverages deep integration with JDK 25 features (Structured Concurrency, Scoped Values).
  - Enhanced native image support and improved GraalVM compatibility.

## 2. Advanced Concurrency (JDK 25 + Spring 4)
- **Virtual Threads**: Enabled by default (`spring.threads.virtual.enabled=true`).
- **Structured Concurrency**: Preferred for complex parallel processing within Application Services.
- **Scoped Values**: Use for sharing request-scoped context (e.g., Auth info, TraceId) across virtual threads instead of `ThreadLocal`.

## 3. 4-Layered Architecture
- **Interfaces**, **Application**, **Domain**, **Infrastructure** layers must maintain strict boundaries.

## 4. Infrastructure Tuning (JDK 25 Optimized)
- **GC**: **Generational ZGC** is the default for low-latency heap management.
- **Memory**: `-XX:MaxRAMPercentage=75.0` for EKS/Container environments.
- **Observability**: Spring Boot 4 Actuator integrated with **Micrometer Tracing** and **W3C TraceContext**.

## 5. Implementation Standards (Kotlin 2)
- **K2 Compiler**: Utilize improved smart casting and ultra-fast compilation.
- **Functional & Concise**: Primary constructors, data classes, and idiomatic scope functions.
- **Serialization**: Prefer `kotlinx-serialization` for high-performance JSON processing.

## 6. Distributed Patterns
- **Locking**: Redisson-based distributed locks handled in the Application layer (AOP/Programmatic).
- **Caching**: Multi-level caching (Caffeine L1 + Redis L2) with Cache-Aside pattern.

## 7. Testing & Quality
- **JUnit 5 & MockK**.
- **Testcontainers**: Use for all integration tests (SQL, NoSQL, Messaging).
- **ArchUnit**: Mandatory to enforce 4-layer architectural constraints.
