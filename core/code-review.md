# Code Review Standards

## 1. Multi-Perspective Review
When reviewing code, the agent must analyze the changes from five distinct perspectives and synthesize the findings.

- **Functional Accuracy**: Does the code fulfill the requirements? Are there any logical flaws or unhandled edge cases?
- **Maintainability**: Is the code readable and idiomatic? Does it follow the 4-layer architecture? Is there any redundant logic?
- **DBA & Data**: Are schema changes backward compatible? Are queries optimized (indexes)? Is the transaction scope appropriate?
- **Security**: Any PII leaks? Injection vulnerabilities? Proper authorization (RBAC/ABAC)?
- **Performance**: Any N+1 problems? Memory leaks? Are locks/caches used efficiently?

## 2. Synthesis & Severity Levels
The main agent should synthesize reviews to remove duplicates and categorize findings:

- **[CRITICAL]**: Must be fixed before merging. High risk of system failure, data loss, or security breach.
- **[MAJOR]**: Significant architectural or logical issues. Should be addressed unless there is a strong justification.
- **[MINOR/SUGGESTION]**: Improvements for better quality or future-proofing. Not strictly blocking.
- **[NIT]**: Small stylistic points or trivial suggestions.

## 3. Communication Tone
- Focus on the code, not the person.
- Ask "Why" instead of just saying "Change this".
- Provide concrete examples or documentation links for suggestions.
