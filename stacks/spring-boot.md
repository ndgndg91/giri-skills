# Spring Boot Style Guide (Kotlin 2 & Spring Boot 4 & JDK 25 LTS)

## 1. Modern Runtime & Framework Versioning
- **JDK Version**: **JDK 25 (LTS)**.
- **Kotlin Version**: **Kotlin 2.x** (K2 compiler).
- **Spring Boot**: **Spring Boot 4.x (LTS)**.

## 2. Web Server (WAS) Selection
- **Standard**: **Tomcat**. Highest maturity and standard for Enterprise. Excellent integration with Virtual Threads.
- **High Performance / Low Footprint**: **Undertow**. Best for high throughput with minimal memory usage.
- **Modular & Flexible**: **Jetty**. 
  - **Why**: Lightweight and highly customizable. Ideal for embedded environments or when specific HTTP/2, HTTP/3 features and flexible connector configurations are needed. Used extensively by Google and Eclipse ecosystem.
- **Reactive**: **Netty**. Strictly for Spring WebFlux scenarios.

## 3. Advanced Concurrency (Virtual Threads)
- **Standard**: `spring.threads.virtual.enabled=true`.
- **Thread Pinning Caution**: Avoid `synchronized` for long I/O. Use `ReentrantLock` to prevent pinning virtual threads to carrier threads.
- **Resource Focus**: Move away from thread pool size tuning; focus on DB pool and Memory constraints.

## 4. 4-Layered Architecture & DDD
- **Interfaces, Application, Domain, Infrastructure** boundaries must be enforced.

## 5. Infrastructure Tuning (JDK 25 Optimized)
- **GC**: **Generational ZGC**.
- **Memory**: `-XX:MaxRAMPercentage=70.0` (Accounting for Direct Memory).
- **MongoDB**: `serverSelectionTimeout` tuning.
- **HTTP Clients**: Mandatory Connect/Read timeout & Connection Pooling.

## 6. Implementation Standards (Kotlin 2)
- **K2 Compiler** features, **kotlinx-serialization**, and idiomatic Kotlin scope functions.

## 7. Testing & Quality
- **JUnit 5 & MockK**, **Testcontainers**, **ArchUnit**.
