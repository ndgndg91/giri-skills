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
All API responses must follow a consistent envelope structure containing metadata for traceability.

### 4.1 Common Metadata (`meta`)
- **`requestId`**: A unique identifier for the request.
  - Priority: Value of the `X-Request-Id` HTTP header (if provided by the client).
  - Fallback: Generate a random UUID on the server.
- **`timestamp`**: Server-side processing completion time in milliseconds (Unix timestamp).

### 4.2 Success Response Format
```json
{
  "meta": {
    "requestId": "uuid-string",
    "timestamp": 1715827200000
  },
  "data": {
    "id": 1,
    "name": "Example"
  }
}
```

### 4.3 Error Response Format
```json
{
  "meta": {
    "requestId": "uuid-string",
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
- Standardize on appropriate 4xx and 5xx codes for errors.

## 6. General Rules
- **Idempotency**: Ensure side-effecting operations (PUT, PATCH, DELETE) are idempotent.
- **Filtering & Sorting**: Use query parameters.
