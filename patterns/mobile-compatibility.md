# Mobile App Version Compatibility & Server Management

## 1. App Version Awareness
- **Mandatory Headers**: Every request from a mobile app must include versioning headers for the server to identify the client's state.
  - `X-App-Version`: Semantic version (e.g., 1.2.3).
  - `X-App-Platform`: iOS or Android.
  - `X-App-Build`: Build number (e.g., 104).
- **Server Logic**: Use these headers to handle version-specific logic or workarounds for bugs present in older app versions.

## 2. Versioning & Backward Compatibility
- **Permanent Support**: Old API paths (e.g., `/v1`) must remain functional as long as the corresponding app version is supported.
- **Non-Breaking Changes**:
  - Never remove or rename fields in existing API responses used by older apps.
  - Make new fields optional or provide default values to prevent older apps (with older DTOs) from crashing during deserialization.
- **BFF (Backend for Frontend)**: Consider using a BFF layer to transform data specifically for different app versions if they diverge significantly.

## 3. Force Update & Maintenance Strategy
- **Version Check API**: Implement a lightweight endpoint (e.g., `/v1/app/check-version`) called during app startup.
- **Response Structure**:
  ```json
  {
    "latestVersion": "1.5.0",
    "minRequiredVersion": "1.2.0",
    "forceUpdate": true,
    "updateUrl": "https://...",
    "message": "A critical update is required."
  }
  ```
- **Graceful Degradation**: Inform users when a specific feature is no longer supported on their current version.

## 4. Feature Toggles & Remote Config
- **Remote Config**: Use a central configuration system (e.g., Firebase Remote Config or custom DB) to enable/disable features per app version without requiring a store update.
- **Kill Switch**: Maintain a "kill switch" for specific features in case of critical bugs discovered in the wild.

## 5. Testing for Compatibility
- **Regression Testing**: Maintain automated tests that use old DTOs/Clients to verify that new server changes don't break older app versions.
- **Side-by-side Testing**: Run tests for both the latest and the minimum supported versions during CI.
