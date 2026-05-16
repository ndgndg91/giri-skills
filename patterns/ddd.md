# Domain-Driven Design (DDD) Principles

## Ubiquitous Language
- Use a consistent vocabulary shared by both domain experts and developers.
- Ensure all code entities (classes, methods, variables) reflect this language.

## Layered Architecture
- **Interfaces (Infrastructure/Web)**: Handle requests, DTO mapping, and UI concerns.
- **Application**: Coordinate domain objects to perform tasks. Transaction management.
- **Domain**: Pure business logic. Entity, Value Object, Domain Service. No external dependencies.
- **Infrastructure**: Technical implementation (DB, External API, Messaging).

## Tactical Patterns
- **Aggregate Root**: Maintain consistency boundaries. All access to the aggregate must go through the root.
- **Entity vs Value Object**: Distinguish by identity. Use VOs for immutable attributes without identity.
- **Repository**: Define interfaces in the Domain layer, implement in the Infrastructure layer.
- **Domain Events**: Use events to decouple aggregates and handle side effects.

## Strategy
- Always prioritize the **Domain layer** when designing new features.
- Keep the Domain layer free from framework-specific annotations if possible.
- Focus on behavior rather than just data structures.
