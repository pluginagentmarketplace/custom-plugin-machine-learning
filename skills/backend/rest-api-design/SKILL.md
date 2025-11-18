---
name: rest-api-design
description: Master RESTful API design principles, HTTP methods, status codes, request/response patterns, versioning, and API best practices for production applications.
---

# 🔌 REST API Design

**Production-Ready RESTful API Architecture and Best Practices**

## Quick Start

### RESTful Endpoint Design
```javascript
// ✅ GOOD: Proper RESTful design
const express = require('express');
const router = express.Router();

// Collection endpoints
router.get('/api/v1/posts', (req, res) => {
  // List all posts with filtering, pagination
  const { page = 1, limit = 20, category } = req.query;
  // Implementation...
  res.json({ data: posts, pagination: { page, limit, total } });
});

router.post('/api/v1/posts', (req, res) => {
  // Create new post
  const { title, content, category } = req.body;
  // Validate input
  if (!title || !content) {
    return res.status(400).json({
      error: 'VALIDATION_ERROR',
      details: { title: 'Required', content: 'Required' }
    });
  }
  // Create and return 201
  res.status(201).json(newPost);
});

// Resource endpoints
router.get('/api/v1/posts/:id', (req, res) => {
  // Get specific post
  const post = findPostById(req.params.id);
  if (!post) {
    return res.status(404).json({
      error: 'NOT_FOUND',
      message: 'Post not found'
    });
  }
  res.json(post);
});

router.put('/api/v1/posts/:id', (req, res) => {
  // Replace entire post
  const post = updatePost(req.params.id, req.body);
  res.json(post);
});

router.patch('/api/v1/posts/:id', (req, res) => {
  // Partial update
  const post = patchPost(req.params.id, req.body);
  res.json(post);
});

router.delete('/api/v1/posts/:id', (req, res) => {
  deletePost(req.params.id);
  res.status(204).send(); // No content
});

// Sub-resource endpoints
router.get('/api/v1/posts/:postId/comments', (req, res) => {
  const comments = getCommentsByPostId(req.params.postId);
  res.json({ data: comments });
});

router.post('/api/v1/posts/:postId/comments', (req, res) => {
  const comment = createComment(req.params.postId, req.body);
  res.status(201).json(comment);
});
```

### HTTP Status Codes
```javascript
// ✅ GOOD: Proper status code usage
const responses = {
  // 2xx Success
  200: 'OK - Request successful',
  201: 'Created - Resource created',
  204: 'No Content - Delete successful',

  // 4xx Client Error
  400: 'Bad Request - Invalid input',
  401: 'Unauthorized - Auth required',
  403: 'Forbidden - No permission',
  404: 'Not Found - Resource not found',
  409: 'Conflict - Resource conflict',
  422: 'Unprocessable Entity - Validation failed',
  429: 'Too Many Requests - Rate limited',

  // 5xx Server Error
  500: 'Internal Server Error',
  503: 'Service Unavailable',
};
```

### Error Response Format
```javascript
// ✅ GOOD: Consistent error responses
const errorResponse = {
  error: 'VALIDATION_ERROR',
  message: 'The provided input is invalid',
  details: {
    email: 'Invalid email format',
    password: 'Must be at least 8 characters'
  },
  timestamp: '2024-01-15T10:30:00Z',
  path: '/api/v1/users',
  requestId: 'req-12345'
};
```


## Production Code Examples

```bash
# Command line examples for quick start
# Replace with language-specific code
echo "Production code examples will be customized per skill"
```
        


### Advanced Patterns
- Pattern 1: Industry best practices
- Pattern 2: Error handling strategies
- Pattern 3: Performance optimization
- Pattern 4: Testing approaches
- Pattern 5: Deployment strategies
        


### Real-World Projects
1. **Beginner Project** (Level: Beginner)
   - Core concepts application
   - Basic requirements
   - Expected duration: 1-2 weeks

2. **Intermediate Project** (Level: Intermediate)
   - Multiple integrations
   - Advanced concepts
   - Expected duration: 3-4 weeks

3. **Advanced Project** (Level: Advanced)
   - Production-grade application
   - Complex architecture
   - Expected duration: 6-8 weeks
        

## Key Topics

### 📋 RESTful Principles
- Client-Server architecture
- Stateless communication
- Cacheability
- Uniform interface (CRUD)
- Layered system
- Code on demand (optional)

### 🎯 Resource Design
- Noun-based URLs (not verbs)
- Hierarchical relationships
- Collection vs singular resources
- Query parameters for filtering
- Pagination and sorting
- Expansion/sparse fieldsets

### 🔐 Security
- Authentication (OAuth2, JWT)
- Authorization (roles, permissions)
- HTTPS only
- Rate limiting
- CORS configuration
- Input validation
- SQL injection prevention

### 📊 Pagination & Filtering
```javascript
// ✅ Pagination patterns
GET /api/v1/posts?page=1&limit=20
GET /api/v1/posts?offset=0&limit=20
GET /api/v1/posts?cursor=abc123&limit=20

// ✅ Filtering
GET /api/v1/posts?category=tech&status=published
GET /api/v1/posts?author=john&created_after=2024-01-01
GET /api/v1/posts?search=query

// ✅ Sorting
GET /api/v1/posts?sort=-created_at,title
GET /api/v1/posts?orderBy=created_at&order=desc
```

### 📤 Request/Response Format
```javascript
// ✅ Consistent request/response
// Request
POST /api/v1/posts
Content-Type: application/json
Authorization: Bearer token

{
  "title": "New Post",
  "content": "...",
  "category": "tech"
}

// Response
{
  "data": {
    "id": "post-123",
    "title": "New Post",
    "content": "...",
    "category": "tech",
    "created_at": "2024-01-15T10:30:00Z",
    "author": {
      "id": "user-456",
      "name": "John Doe"
    }
  },
  "meta": {
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```

## Advanced Concepts

### API Versioning
```javascript
// ✅ Versioning strategies

// 1. URL path versioning (most common)
GET /api/v1/posts
GET /api/v2/posts

// 2. Header versioning
GET /api/posts
Accept: application/vnd.myapi.v1+json

// 3. Query parameter versioning
GET /api/posts?version=1

// Implementation with Express
const v1Router = require('./routes/v1');
const v2Router = require('./routes/v2');

app.use('/api/v1', v1Router);
app.use('/api/v2', v2Router);
```

### API Documentation
```javascript
/**
 * @swagger
 * /api/v1/posts:
 *   get:
 *     summary: List all posts
 *     parameters:
 *       - in: query
 *         name: page
 *         schema:
 *           type: integer
 *         description: Page number
 *       - in: query
 *         name: limit
 *         schema:
 *           type: integer
 *         description: Items per page
 *     responses:
 *       200:
 *         description: List of posts
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 data:
 *                   type: array
 *                   items:
 *                     $ref: '#/components/schemas/Post'
 *       400:
 *         description: Invalid parameters
 */
```

## Best Practices ✅

✅ Use nouns for URLs, not verbs
✅ Use proper HTTP methods (GET, POST, PUT, PATCH, DELETE)
✅ Return appropriate status codes
✅ Consistent response format
✅ Proper pagination (offset/limit or cursor)
✅ Filtering via query parameters
✅ Sorting via query parameters
✅ API versioning strategy
✅ Comprehensive documentation (OpenAPI/Swagger)
✅ Rate limiting
✅ CORS properly configured
✅ HTTPS only
✅ Input validation & sanitization
✅ Error handling with details
✅ Request IDs for tracing

## Real-World Projects

### 1. E-Commerce API
- Products, orders, users, reviews
- Full CRUD operations
- Advanced filtering & pagination
- Authentication & authorization
- Webhook support

### 2. Blog Platform API
- Posts, comments, categories
- User management
- Search functionality
- Rate limiting
- API keys

### 3. Social Media API
- Users, posts, likes, comments
- Following system
- Notifications
- Real-time updates
- Feed algorithms

## Tools & Technologies

- **Design:** OpenAPI/Swagger, Postman, Insomnia
- **Testing:** Jest, Supertest, Rest Assured
- **Documentation:** Swagger UI, API Blueprint
- **Monitoring:** Sentry, DataDog, Elastic

---

**Master RESTful API design today!** 🚀
