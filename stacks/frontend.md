# Frontend & Mobile Strategy

## 1. Web Development
- **Standard**: **React + TypeScript + Tailwind CSS**.
- **Principles**:
  - **Type Safety**: Strong typing for API responses and component props.
  - **Design Taste & Anti-Slop**: Strictly follow `patterns/frontend-taste.md`. Ban generic AI slop (violet gradients, 3 identical cards, eyebrow badges, cream+terracotta tropes) and enforce substance-driven design with distinct typography, real UI fragments, and argument-based layouts.
  - **View Separation**: Clearly distinguish public narrative pages from high-density, utility-focused app screens.
  - **Verification**: Verify visual hierarchy and responsive behavior across viewports (Mobile 375px, Tablet 768px, Desktop 1280px+).

## 2. Mobile Development Options
- **Compose Multiplatform (Recommended)**: 
  - Best for Kotlin developers. Share UI and business logic between Android, iOS, and Desktop.
  - Higher performance and tighter integration with the Kotlin ecosystem.
- **React Native**: 
  - Best for leveraging existing React (Web) knowledge. 
  - Large ecosystem and fast iteration for UI-heavy apps.
- **Flutter**: 
  - Best for high-performance, consistent UI across all platforms with a single codebase.

## 3. Shared Logic Strategy
- Maintain a **Common Module** (or KMP module) for shared business logic, validation rules, and DTOs when building Multi-platform applications.
