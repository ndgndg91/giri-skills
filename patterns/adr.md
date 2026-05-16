# Architecture Decision Records (ADR)

## 1. Why ADR?
- To record the context and rationale behind significant architectural decisions.
- To follow the "Don't Hide Chaos" principle by documenting the trade-offs and conflicts encountered.

## 2. ADR Template
Each ADR should follow this structure:
- **Title**: Short and descriptive (e.g., ADR-001: Use Redis for Distributed Locking).
- **Status**: Proposed, Accepted, Superceded.
- **Context**: What is the problem? What are the constraints?
- **Decision**: What is the chosen solution?
- **Consequences**: What are the trade-offs? What is better now? What is worse?

## 3. Storage
- Store ADRs in the project repository under `/docs/adr/` to keep them close to the code.
