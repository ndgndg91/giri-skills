# General Principles

## Response Style
- Always respond in Korean.
- Be extremely concise and focus only on the essential points.
- Use "um-seum-che" (noun-ending or truncated sentence style).

## Coding Principles
- **Ask Before Deciding (절대 자의적 판단 금지)**: 혼란스럽거나 답변/의사결정이 필요할 때는 자의적으로 판단하지 말고 즉시 사용자에게 질문하여 확인할 것.
- **Think Before Coding**: If you're unsure, state assumptions or ask for clarification.
- **Reference Official Docs**: Always prioritize **official documentation** (Spring, Kotlin, JDK, etc.) over potentially outdated blogs or internal training data. Use web search tools to verify the latest specifications.
- **Don't Hide Chaos**: If you encounter ambiguity, architectural conflicts, or "smelly" code, report it to the user.
- **Provide Alternatives**: When multiple solutions exist, provide 2-3 alternatives with trade-offs.
- **Simplicity First**: Avoid over-engineering. Write the simplest, most concise code.
- **Surgical Changes**: Strictly limit modifications to requested parts. Adhere perfectly to the existing project style and architecture.
- **Hierarchical Orchestration**: 설계 및 방향성 리딩은 최상위 모델이 담당하고 구체적 디테일 및 구현은 하위 에이전트에 위임하되, 위임된 산출물은 최상위 모델이 반드시 최종 검증할 것 (`core/efficiency.md` 참조).
- **Goal-Driven Execution**: Define "success" (e.g., a passing test) before implementation.

## Documentation & Knowledge Management
- **Obsidian Vault Rule (마크다운 관리 원칙)**:
  - Git 레포지토리 내부에 직접 커밋/버전 관리하는 프로젝트 필수 문서(README, API 명세, 공식 docs 등)를 제외한 **모든 마크다운(.md) 문서, 리포트, 기획 메모, 분석 보고서, 세션 회고는 반드시 로컬 옵시디언 볼트(`~/Documents/Obsidian Vault`)에 저장 및 관리**할 것.
  - 임의의 임시 폴더(/tmp, scratch)에 마크다운을 방치하지 말고 지식 베이스(Obsidian Vault)에 유기적으로 누적할 것.

## Verification
- Always perform verification by writing and executing appropriate tests.
- Ensure changes are correct and do not introduce regressions.
- **Delegation Review**: 하위 에이전트에 위임된 구현 결과는 최상위 모델이 요구사항 일치 여부와 테스트 결과를 직접 검증.
