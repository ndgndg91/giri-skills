# Spring Boot Style Guide (Kotlin & Pragmatic DDD)

## 1. Project Structure & Layers
- **Interfaces (Web)**: `@RestController`, DTOs, and Request Mapping. No business logic.
- **Application**: `@Service`, `@Transactional`. Coordination and task orchestration.
- **Domain**: Pure business logic (Entities, VOs, Services). Minimal external dependencies.
- **Infrastructure**: Implementation of Repository interfaces, Persistence (`@Entity`), and External APIs.

## 2. JPA Entity vs Domain Entity Strategy
### Basic Principle: Pragmatic Unified Model
- By default, use **JPA Entity as Domain Entity** to maximize productivity and leverage JPA features (Lazy Loading, etc.).
- Use Kotlin's `open` classes or `all-open` plugin to support JPA proxying.

### When to Separate (Infrastructure Separation)
Consider separating JPA Entity from Domain Entity if:
- **Schema Mismatch**: Database table structure significantly differs from the object-oriented domain model.
- **Domain Pollution**: Persistence-specific concerns overwhelm the business logic.
- **Multiple Data Sources**: A single Domain Entity is composed of data from multiple sources.

## 3. Implementation Standards (Kotlin)
- **No Lombok**: Use Kotlin native features (data classes, primary constructors, named arguments).
- **Constructor Injection**: Use Kotlin's concise primary constructor syntax.
- **Global Exception Handling**: Use `@RestControllerAdvice` with consistent error response formats.
- **Validation**: Use Bean Validation (`@field:NotBlank`, etc.) with Kotlin's field target.

## 4. Testing Strategy
- **JUnit 5 & MockK**: Use MockK instead of Mockito for Kotlin-idiomatic mocking.
- **Testcontainers**: Use **Testcontainers** for integration tests to ensure compatibility with real database environments.
- **Slice Testing**: Use `@WebMvcTest` for Controllers and `@DataJpaTest` with Testcontainers for Repositories.
- **Integration Testing**: Use `@SpringBootTest` with Testcontainers for end-to-end verification.
