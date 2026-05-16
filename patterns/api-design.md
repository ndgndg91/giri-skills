# REST API Design Guide

## 1. Naming Conventions
- **URI Case**: Always use **kebab-case** for URIs (e.g., `/user-profiles`, `/order-items`).
- **Resource Naming**: Use plural nouns for resources (e.g., `/users`, `/orders`). Avoid verbs in URIs.
- **Hierarchy**: Represent relationships through path nesting (e.g., `/users/{id}/orders`).

## 2. API Versioning
- **Strategy**: Use **Path-based versioning** (e.g., `/v1/users`, `/v2/orders`).
- **Reason**: Provides clear visibility and simplifies caching and routing.

## 3. Pagination Strategy
- **Default**: Use **Cursor-based Pagination** (e.g., `?cursor=abc&size=20`).
- **Performance**: Avoid Offset-based pagination for large datasets due to `OFFSET` performance degradation in RDBMS (Full scan issues).
- **Consistency**: Cursor-based pagination provides more stable results when data is frequently added/deleted.

## 4. HTTP Methods & Status Codes
- **GET**: Retrieve resources (200 OK).
- **POST**: Create a new resource (201 Created).
- **PUT**: Replace an existing resource (200 OK or 204 No Content).
- **PATCH**: Partially update a resource (200 OK).
- **DELETE**: Remove a resource (200 OK or 204 No Content).
- **Error Status**:
  - 400 Bad Request (Invalid input)
  - 401 Unauthorized (Missing/Invalid Auth)
  - 403 Forbidden (Insufficient permissions)
  - 404 Not Found (Resource doesn't exist)
  - 500 Internal Server Error (Server-side failure)

## 5. Error Response Format
- Always return a consistent error object:
  ```json
  {
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "details": {}
  }
  ```

## 6. General Rules
- **Idempotency**: Ensure PUT, PATCH, and DELETE operations are idempotent where possible.
- **Filtering & Sorting**: Use query parameters (e.g., `?status=active&sort=createdAt,desc`).
