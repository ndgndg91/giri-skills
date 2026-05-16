# Project Structure Guide (Single vs Multi-Module)

## 1. Single Module Structure
- **When to use**: 
  - Small-scale projects, MVPs, or simple CRUD applications.
  - When the domain boundaries are not yet clear.
- **Pros**: Simple configuration, fast build times, easy to manage.
- **Cons**: Difficult to enforce strict layering as the project grows; hard to share code between different deployment units (e.g., API and Batch).

## 2. Multi-Module Structure (Recommended for Enterprise)
- **When to use**: 
  - Complex domains with multiple Bounded Contexts.
  - When sharing code (Domain/Infrastructure) across different applications (API, Worker, Batch, Admin).
  - To enforce strict dependency rules between layers.
- **Standard Module Layout**:
  - **`app-api`**: REST API controllers, Web-specific configurations. Depends on `core`.
  - **`app-worker`**: Kafka consumers, scheduled tasks. Depends on `core`.
  - **`core` (or `domain`)**: Core business logic, Entities, Services, and Repository interfaces. Purest part of the system.
  - **`infrastructure` (optional)**: Specific implementations for DB, external clients, etc. Can be merged into `core` for smaller multi-module projects but keep packages separate.
  - **`client-xxx`**: Independent modules for external API integrations to keep the core clean.
  - **`common`**: Cross-cutting concerns like shared utilities, logging, and constants. (Keep this lean).

## 3. Modular Monolith Strategy
- Even in a single or multi-module monolith, maintain clear **Bounded Contexts** using package structures.
- Use tools like **ArchUnit** to enforce that the `Domain` layer does not depend on `Interfaces` or `Infrastructure`.

## 4. Decision Matrix
- If you have more than two deployment units (e.g., API + Batch): **Multi-module**.
- If multiple teams are working on different contexts: **Multi-module**.
- If it's a prototype or a very small internal tool: **Single module**.
