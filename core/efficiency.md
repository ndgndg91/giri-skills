# Operational Efficiency & Accuracy Balance

## Core Principle: Accuracy Over Efficiency
- **Never compromise accuracy for token savings.**
- If the context is ambiguous or the logic is complex, read the full file (`read_file`).
- Only use optimized tools (like range-based reading) when the target area is clearly identified.

## Balanced Tool Usage

### 1. Smart Reading Strategy
- **Exploration Phase**: Use full `read_file` or wide `grep_search` to understand the architecture and context.
- **Maintenance Phase**: Use `start_line` and `end_line` for targeted reads once the location is confirmed.

### 2. Safe Surgical Edits
- **Contextual `replace`**: Provide enough surrounding lines (3-5 lines) in `old_string` to ensure the match is unique and the edit is safe.
- **Verification Loop**: After a `replace` or `write_file`, verify the change by reading the modified part or running tests immediately.

### 3. Latency Reduction
- **Parallel Execution**: Execute independent tool calls in a single turn to minimize waiting time.
- **Conditional Directives**: Provide clear "if-then" instructions to reduce conversational turns.

## Continuous Improvement (Self-Evolution)
- **Detect Inefficiency**: If existing skills or principles cause edge cases, errors, or significant overhead in a specific context, **immediately alert the user**.
- **Propose Upgrades**: When a better pattern or more efficient workflow is identified, suggest updating the relevant guideline in `giri-skills` to improve future performance.
