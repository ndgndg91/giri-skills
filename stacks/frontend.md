# Frontend & Mobile Strategy

## 1. Web Development
- **Standard**: **React + TypeScript + Tailwind CSS**.
- **Principle**: Strong typing for API responses and component props.

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
