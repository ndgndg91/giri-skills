# Security Guide

## 1. Authentication (JWT Strategy)
- **Storage**: Prefer storing JWT in **HttpOnly, Secure, and SameSite=Strict/Lax cookies** instead of LocalStorage to mitigate XSS risks.
- **Self-Contained vs. Revocation**: 
  - Leverage JWT's stateless nature for performance.
  - For immediate revocation, implement a **Blacklist** (via Redis) or use short-lived Access Tokens with **Refresh Token Rotation (RTR)**.
- **CSRF Protection**: When using cookies, ensure CSRF protection (e.g., SameSite cookies or CSRF tokens) is active.

## 2. Access Control (RBAC & ABAC)
- **RBAC (Role-Based)**: Default for most scenarios. Assign permissions to roles (e.g., ADMIN, USER).
- **ABAC (Attribute-Based)**: Use for fine-grained or context-sensitive authorization (e.g., "Allow access if user is in Dept A AND time is between 9-5").
- **Principle of Least Privilege**: Grant only the minimum permissions required for a task.

## 3. Data Protection
- **PII Masking**: Always mask sensitive Personal Identifiable Information (PII) in logs and UI (e.g., phone numbers, emails).
- **Encryption**: Encrypt sensitive data at rest (AES-256) and always use TLS (HTTPS) in transit.
- **Injection Defense**: 
  - Use Prepared Statements/Parameterized Queries to prevent SQL Injection.
  - Sanitize inputs and use CSP headers to prevent XSS.

## 4. Rate Limiting
- **Requirement**: Mandatory for Public/Open APIs to prevent abuse and DoS attacks.
- **Implementation**: Use API Gateways or Redis-based algorithms (Leaky Bucket, Token Bucket) for distributed rate limiting.

## 5. Security Headers
- Ensure appropriate security headers are set: `Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options`, `Content-Security-Policy`.
