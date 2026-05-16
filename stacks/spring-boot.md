# Spring Boot Style Guide (Kotlin 2 & Spring Boot 4 & JDK 25 LTS)

## 1. Modern Runtime & Framework Versioning
- **JDK Version**: **JDK 25 (LTS)**.
- **Kotlin Version**: **Kotlin 2.x** (K2 compiler).
- **Spring Boot**: **Spring Boot 4.x (LTS)**.

## 2. API Gateway Strategy
- **Standard**: **Spring Cloud Gateway MVC** with **Virtual Threads**.
  - **Why**: Higher developer productivity, easier debugging, and native compatibility with blocking libraries while maintaining high scalability via Virtual Threads.
- **Alternative**: **Spring Cloud Gateway (Reactive)**. 
  - **Why**: Use only for extreme high-concurrency streaming cases or when the entire stack is already reactive.

## 3. Web Server (WAS) Selection
- **Standard**: **Tomcat**. Best integration with Spring Boot 4 and Virtual Threads.
- **Performance**: **Undertow**. Low memory footprint.
- **Modular**: **Jetty**. High flexibility for embedded/custom HTTP needs.

## 4. Advanced Concurrency (Virtual Threads)
- **Standard**: `spring.threads.virtual.enabled=true`.
- **Precaution**: Avoid `synchronized` for long I/O to prevent thread pinning. Use `ReentrantLock`.

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
