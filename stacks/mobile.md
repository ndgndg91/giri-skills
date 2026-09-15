# Mobile & Flutter Engineering Standards

## 1. 실기기(iPhone/iOS Device) 테스트 원칙 (CRITICAL)
- **무조건 `--release` 모드로 빌드/실행**:
  - 실기기(특히 iOS 무선 환경)에서 `debug` 모드로 실행 시 Dart VM 로컬 네트워크 mDNS 소켓 연결 오류(`SocketException: Send failed / No route to host`)로 앱이 비정상 종료됨.
  - **실기기 배포/테스트 명령은 무조건 `--release` 플래그 필수 적용**:
    ```bash
    flutter run -d <DEVICE_ID> --release
    ```
- **시뮬레이터(Simulator)와 실기기 분리**:
  - `debug` 모드는 오직 iOS 시뮬레이터(`open -a Simulator`)에서만 사용.
  - 실기기에서는 항상 `--release` 모드로 설치 및 단독 구동.
