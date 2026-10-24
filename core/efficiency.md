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

## Hierarchical Model Orchestration (계층형 모델 오케스트레이션 및 역할 위임)
- **Top-Tier Model for Leading & Architecture (최상위 모델의 설계 및 방향성 리딩)**:
  - 시스템 전체 아키텍처 설계, 기술 방향성 수립, 도메인 모델링, 종합 의사결정 등 고차원적 리딩 작업은 항상 해당 환경의 최상위 추론/지능 모델(High-Tier / Reasoning Model)이 주도할 것.
- **Worker/Subagent Delegation for Implementation (하위 에이전트의 세부 구현 위임)**:
  - 구체적인 코드 작성/수정, 반복 작업, 단위 테스트 구현, 단순 탐색 등 세부 디테일 실행 작업은 하위/경량 작업 에이전트(Worker / Subagent / Fast Model)에게 적극적으로 위임할 것.
- **Model-Agnostic Tiering Principle (버전 무관 티어링 원칙)**:
  - 플랫폼별 구체적인 모델 명칭이나 버전(예: 플래그십 모델 vs 경량 모델)은 지속적으로 갱신되므로 특정 버전을 하드코딩하지 않고, "전체 방향성 리딩 = 최상위 추론 모델, 디테일 구현 및 실행 = 하위 에이전트"라는 계층적 역할 분담 원칙을 항상 견지할 것.

## Continuous Improvement (Self-Evolution)
- Detect and report inefficiencies or edge cases caused by these guidelines.
- Propose upgrades to `giri-skills` when better patterns are identified.
