# Legacy Modernization & Refactoring

## 1. Core Strategies
- **Strangler Fig Pattern**: Gradually replace legacy functionality with new services/modules. The old system is slowly "strangled" until it can be decommissioned.
- **Boy Scout Rule**: Always leave the code a little cleaner than you found it. Perform small refactors (renaming, extracting methods) during regular task execution.
- **Feathers' Strategy**: Before refactoring legacy code, wrap it in tests (Characterization Tests) to ensure existing behavior is preserved.

## 2. Refactoring Principles
- **Small Steps**: Make incremental changes with frequent commits and tests.
- **Feature Toggles**: Use toggles to safely roll out refactored logic in production and roll back instantly if needed.
- **Don't Over-Refactor**: Focus on areas with high change frequency or high bug density.

## 3. Technical Debt Management
- Identify and document technical debt in **ADRs**.
- Dedicate a portion of every sprint/cycle to debt reduction.
