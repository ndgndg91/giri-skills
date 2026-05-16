# Security Guide

## 1. Authentication & Authorization
- **JWT**: Store in **HttpOnly, Secure cookies**. Use short-lived AT + RTR.
- **RBAC & ABAC**: Default RBAC, context-sensitive ABAC.

## 2. Replay Attack Defense
- **Timestamp & Nonce**: For sensitive Open APIs, validate a `Timestamp` and a unique `Nonce` in each request.
- **Window Validation**: Reject requests with timestamps older than a specific window (e.g., 5 minutes) to prevent delayed re-execution.
- **Nonce Uniqueness**: Store and check the `Nonce` within the timestamp window to ensure a request is never processed twice.

## 3. Data Protection
- **PII Masking**: Mask sensitive info in logs/UI.
- **Encryption**: AES-256 for data-at-rest, TLS for transit.
- **Injection Defense**: Parameterized queries and CSP headers.

## 4. Rate Limiting
- Mandatory for Public APIs. Use Redis-based Leaky Bucket/Token Bucket.

## 5. Security Headers
- Set HSTS, X-Content-Type-Options, X-Frame-Options, CSP.
