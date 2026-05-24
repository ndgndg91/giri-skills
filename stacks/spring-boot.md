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
  - Test function names must be written in English using `should_snake_case` (e.g., `should_do_something_when_condition`).
  - Use **`@DisplayName("한글 설명")`** to express test scenarios in Korean for executable specifications.
  - Write BDD scenario comments in lowercase: `// given`, `// when`, `// then`.

## 9. Financial Precision & Money Types (BigDecimal & Scale Factor)
- **Anti-Pattern**: Do **NOT** use `Double` or `Float` for monetary amounts, interest rates, or margins due to IEEE 754 floating-point rounding errors.
- **Standard**: Use **`BigDecimal`** and specify an explicit **`RoundingMode`** (e.g., `RoundingMode.HALF_UP` for rounding) to guarantee perfect precision in trade and financial operations.
- **High-Performance Optimization (Scale Factor Pattern)**: Under extreme high-throughput, low-latency transaction processing where the object allocation overhead of `BigDecimal` becomes a bottleneck:
  - Apply the **Scale Factor** pattern using primitive **`Long`** types.
  - Scale all values by a fixed factor (e.g., multiplying by `10,000` to support up to 4 decimal places) for fast integer-based arithmetic.
  - Convert back to the target precision only at the presentation or external API boundary.


