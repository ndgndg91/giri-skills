# REST API Design Guide

## 1. Naming Conventions
- **URI Case**: Always use **kebab-case** for URIs (e.g., `/user-profiles`).
- **Resource Naming**: Use plural nouns for resources (e.g., `/users`). Avoid verbs in URIs.
- **Hierarchy**: Represent relationships through path nesting (e.g., `/users/{id}/orders`).

## 2. API Versioning
- **Strategy**: Use **Path-based versioning** (e.g., `/v1/users`).

## 3. Pagination Strategy
- **Default**: Use **Cursor-based Pagination** (e.g., `?cursor=abc&size=20`).
- **Performance**: Avoid Offset-based pagination for large datasets.

## 4. Response & Error Formats (Envelope Pattern)
All API responses must follow a consistent envelope structure containing a **traceId** for distributed tracing and observability.

### 4.1 Distributed Tracing (`meta.traceId`)
- **`traceId`**: A unique identifier for the entire transaction across services.
  - **Header Priority**:
    1. `traceparent` (W3C Trace Context standard)
    2. `X-Trace-Id` or `X-Request-Id` (legacy headers)
  - **Fallback**: If no header is provided, the entry-point service must generate a random UUID as the `traceId`.
  - **Propagation**: This ID must be propagated to all downstream internal calls and messaging headers (Kafka, etc.).
- **`timestamp`**: Server-side processing completion time in milliseconds (Unix timestamp).

### 4.2 Success Response Format
```json
{
  "meta": {
    "traceId": "uuid-or-traceparent",
    "timestamp": 1715827200000
  },
  "data": { ... }
}
```

### 4.3 Error Response Format
```json
{
  "meta": {
    "traceId": "uuid-or-traceparent",
    "timestamp": 1715827200000
  },
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {}
  }
}
```

## 5. HTTP Methods & Status Codes
- **GET**: 200 OK.
- **POST**: 201 Created.
- **PUT/PATCH/DELETE**: 200 OK or 204 No Content.

## 6. General Rules
- **Idempotency**: Ensure side-effecting operations are idempotent.
- **Filtering & Sorting**: Use query parameters.
