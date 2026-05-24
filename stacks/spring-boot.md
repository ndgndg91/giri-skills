# Spring Boot Style Guide (Kotlin 2 & Spring Boot 4 & JDK 25 LTS)

## 1. Modern Runtime & Framework Versioning
- **JDK Version**: **JDK 25 (LTS)**.
- **Kotlin Version**: **Kotlin 2.x** (K2 compiler).
- **Spring Boot**: **Spring Boot 4.x (LTS)**.

## 2. API Gateway Strategy
- **Standard**: **Spring Cloud Gateway MVC** with **Virtual Threads**.

## 3. Web Server (WAS) Selection
- **Standard**: **Tomcat**. Full support for Virtual Threads.
- **Performance**: **Undertow** (Require `RequestLimitingHandler` for safety).

## 4. Advanced Concurrency (Virtual Threads)
- **Standard**: `spring.threads.virtual.enabled=true`.
- **Pinning Fix (JEP 491)**: From JDK 24+, the `synchronized` keyword no longer pins virtual threads to carrier threads during blocking I/O. **Feel free to use existing libraries and synchronized blocks.**
- **Remaining Pinning Risks**: Be cautious when calling **Native Methods (JNI)** or **Foreign Function & Memory (FFM)** APIs within virtual threads, as these can still cause pinning.
- **Focus**: Focus on actual resource limits (DB pools, memory) rather than thread-per-request overhead.

## 5. 4-Layered Architecture & DDD
- Strict boundaries: **Interfaces, Application, Domain, Infrastructure**.

## 6. Infrastructure & Tuning (JDK 25 Optimized)
- **GC**: **Generational ZGC**.
- **Memory**: `-XX:MaxRAMPercentage=70.0` (Accounting for Direct Memory).
- **Storage**: MongoDB selection timeout, HikariCP pool tuning.
- **Clients**: Mandatory timeouts & pooling for HTTP clients.

## 7. Implementation Standards (Kotlin 2)
- **One Class, One File**: Every top-level class, interface, or enum must reside in its own file to ensure clarity and traceability.
- **K2 Compiler**, **kotlinx-serialization**, idiomatic scope functions.

## 8. Testing & Quality
- **JUnit 5 & Mockito & AssertJ (BDD Style)**, **Testcontainers**, **ArchUnit**.
- **Test Naming Convention**:
  - Do **NOT** use Korean in test function names (Avoid backtick names in Korean to prevent CI/CD and static analysis compatibility issues).
  - Test function names must be written in English (e.g., `camelCase` or `snake_case`).
  - Use **`@DisplayName("한글 설명")`** to express test scenarios in Korean for executable specifications.
