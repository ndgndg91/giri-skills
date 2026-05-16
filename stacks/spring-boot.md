# Spring Boot Style Guide (Kotlin 2 & Spring Boot 4 & JDK 25 LTS)

## 1. Modern Runtime & Framework Versioning
- **JDK Version**: **JDK 25 (LTS)**.
- **Kotlin Version**: **Kotlin 2.x** (K2 compiler).
- **Spring Boot**: **Spring Boot 4.x (LTS)**.

## 2. API Gateway Strategy
- **Standard**: **Spring Cloud Gateway MVC** with **Virtual Threads**.
- **Alternative**: **Spring Cloud Gateway (Reactive)** for extreme high-concurrency streaming.

## 3. Web Server (WAS) Selection
- **Standard**: **Tomcat**. Best stability and integration with Virtual Threads.
- **High Performance**: **Undertow**. 
  - **Caution**: The default worker task queue is **unbounded**, which can lead to **OOM** under high load.
  - **Best Practice**: Must apply **`RequestLimitingHandler`** via `WebServerFactoryCustomizer` to explicitly limit concurrent requests and queue size.
- **Modular**: **Jetty**. High flexibility for custom HTTP needs.

## 4. Advanced Concurrency (Virtual Threads)
- **Standard**: `spring.threads.virtual.enabled=true`.
- **Precaution**: Avoid `synchronized` for long I/O. Use `ReentrantLock`.

## 5. 4-Layered Architecture & DDD
- Strict boundaries: **Interfaces, Application, Domain, Infrastructure**.

## 6. Infrastructure & Tuning
- **GC**: **Generational ZGC**.
- **Memory**: `-XX:MaxRAMPercentage=70.0` (Accounting for Direct Memory).
- **Storage**: MongoDB selection timeout, HikariCP pool tuning.
- **Clients**: Mandatory timeouts & pooling for HTTP clients.

## 7. Implementation Standards (Kotlin 2)
- **K2 Compiler**, **kotlinx-serialization**, idiomatic scope functions.

## 8. Testing & Quality
- **JUnit 5 & MockK**, **Testcontainers**, **ArchUnit**.
