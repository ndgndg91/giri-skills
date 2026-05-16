# REST API Design Guide

## 1. Naming Conventions
- **URI Case**: Always use **kebab-case** for URIs (e.g., `/user-profiles`).
- **Resource Naming**: Use plural nouns for resources (e.g., `/users`). Avoid verbs in URIs.

## 2. API Versioning
- **Strategy**: Use **Path-based versioning** (e.g., `/v1/users`).

## 3. Pagination Strategy
- **Default**: Use **Cursor-based Pagination** (e.g., `?cursor=abc&size=20`).

## 4. Response & Error Formats (Envelope Pattern)
All API responses must follow a consistent envelope structure containing a **traceId**.

### 4.1 Distributed Tracing & Headers
- **Header Priority**: `traceparent`, `Trace-Id`, or `Request-Id`. **Avoid `X-` prefix.**
- **`timestamp`**: Server-side processing completion time in milliseconds.

## 5. Idempotency Strategy
- **Idempotency-Key**: For non-idempotent operations (primarily **POST**), clients must provide a unique **`Idempotency-Key`** in the header.
- **Server Handling**:
  - Use Redis or DB to store the `Idempotency-Key` with a TTL (e.g., 24 hours).
  - If the same key is received, return the cached successful response without re-executing business logic.
  - Return **409 Conflict** if a request with the same key is already in progress.

## 6. HTTP Methods & Status Codes
- **GET**: 200 OK.
- **POST**: 201 Created.
- **PUT/PATCH/DELETE**: 200 OK or 204 No Content.

## 7. General Rules
- **Idempotency**: Standard HTTP methods (GET, PUT, DELETE) should be idempotent by design. Use the `Idempotency-Key` strategy for POST.
- **Filtering & Sorting**: Use query parameters.
