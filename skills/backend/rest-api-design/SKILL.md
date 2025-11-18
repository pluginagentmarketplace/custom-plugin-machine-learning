---
name: rest-api-design
description: Master RESTful API design principles, HTTP methods, status codes, and best practices.
---

# REST API Design

## Quick Start

### RESTful Endpoint Design
```
GET    /api/v1/users              # List all users
POST   /api/v1/users              # Create new user
GET    /api/v1/users/:id          # Get user by ID
PUT    /api/v1/users/:id          # Update user
DELETE /api/v1/users/:id          # Delete user
```

### HTTP Status Codes
```
2xx: Success
  200: OK
  201: Created
  204: No Content

4xx: Client Error
  400: Bad Request
  401: Unauthorized
  403: Forbidden
  404: Not Found

5xx: Server Error
  500: Internal Server Error
  503: Service Unavailable
```

## Key Topics

- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE semantics
- **Status Codes**: Proper use of HTTP status codes
- **Request/Response Format**: JSON standards, content negotiation
- **Pagination**: Cursor vs offset, limit/skip
- **Filtering & Sorting**: Query parameters best practices
- **Error Handling**: Consistent error format and messages
- **Versioning**: API versioning strategies
- **Authentication**: Basic, Bearer tokens, OAuth
- **Rate Limiting**: Preventing abuse
- **Documentation**: OpenAPI/Swagger

## Best Practices

✅ Use standard HTTP methods correctly
✅ Return appropriate status codes
✅ Use consistent naming conventions
✅ Implement pagination for large results
✅ Version your API
✅ Document with OpenAPI
✅ Use HATEOAS for discoverability
✅ Implement rate limiting

