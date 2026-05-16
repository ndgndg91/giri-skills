# Code Review Standards

## 1. Multi-Perspective Review
When reviewing code, the agent must analyze the changes from eight distinct perspectives and synthesize the findings.

1. **Functional Accuracy**: Does the code fulfill the requirements? Any logical flaws or unhandled edge cases?
2. **Maintainability**: Is the code readable, idiomatic, and consistent with the 4-layer architecture?
3. **DBA & Data**: Are schema changes backward compatible? Are queries optimized (indexes)? Transaction scope?
4. **Security**: Any PII leaks? Injection vulnerabilities? Proper auth (RBAC/ABAC)? Replay attack defense?
5. **Performance**: N+1 problems? Memory leaks? Efficient use of locks/caches? Zero-copy awareness?
6. **Observability & Operability**: Proper logging with `traceId`? Metrics/Actuator exposed? Error handling visibility?
7. **API Contract & Backward Compatibility**: Breaking changes in API/Messaging? Support for older App versions? Expand-Contract followed?
8. **Test Quality**: Meaningful assertions? Edge cases covered? Flaky tests? Proper use of Testcontainers?

## 2. Synthesis & Severity Levels
The main agent should synthesize reviews from all perspectives, removing duplicates and categorizing findings:

- **[CRITICAL]**: Must be fixed before merging. High risk of system failure, data loss, security breach, or breaking production.
- **[MAJOR]**: Significant architectural, logical, or stability issues.
- **[MINOR/SUGGESTION]**: Improvements for code quality, future-proofing, or better readability.
- **[NIT]**: Small stylistic points or trivial suggestions.

## 3. Communication Tone
- Focus on the code, not the person.
- Ask "Why" to understand the rationale.
- Provide concrete examples or documentation links for suggestions.
