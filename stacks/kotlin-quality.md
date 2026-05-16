# Kotlin Code Quality & Architecture Enforcement

## 1. ArchUnit
- **Mandatory**: Use **ArchUnit** to enforce 4-layer architectural constraints via unit tests.
- **Rules**:
  - `Domain` must not depend on `Application`, `Interfaces`, or `Infrastructure`.
  - `Application` must not depend on `Interfaces`.
  - Controllers must not access Repositories directly.

## 2. Detekt
- **Usage**: Use **Detekt** for static analysis.
- **Optimization**: Focus on "Highly Important" rules (Complexity, LongMethod, Naming) to avoid developer fatigue. Disable or relax stylistic rules that are too pedantic.

## 3. ktlint
- Use **ktlint** for consistent code formatting according to official Kotlin style guides.
