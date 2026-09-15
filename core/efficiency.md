# Operational Efficiency & Accuracy Balance

## Core Principle: Accuracy Over Efficiency
- **Never compromise accuracy for token savings.**
- **Verify with Docs**: Before implementing complex framework features or using new versions, use search/fetch tools to verify the latest official specifications.
- If the context is ambiguous, read the full file (`read_file`).

## Balanced Tool Usage
### 1. Smart Reading Strategy
- Exploration: Full `read_file`.
- Maintenance: Targeted `start/end_line` once location is confirmed.

### 2. Safe Surgical Edits
- Provide 3-5 lines of context in `replace`.
- Verify changes immediately after editing.

### 3. Latency Reduction
- **Maximize Parallelism (독립적 작업 최대 병렬화)**: 빌드, 테스트, 배포, 조회 등 상호 의존성이 없는 독립적인 작업은 서브에이전트나 백그라운드 프로세스를 활용해 최대한 병렬로 동시 실행할 것.
- Use parallel tool execution for independent tasks.
- Provide clear "if-then" instructions to reduce turns.

## Continuous Improvement (Self-Evolution)
- Detect and report inefficiencies or edge cases caused by these guidelines.
- Propose upgrades to `giri-skills` when better patterns are identified.
