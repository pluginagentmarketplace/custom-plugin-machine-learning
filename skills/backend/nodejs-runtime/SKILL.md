---
name: nodejs-runtime
description: Master Node.js runtime, event-driven architecture, and popular frameworks.
---

# Node.js Runtime & Frameworks

## Quick Start

### Express Server
```javascript
const express = require('express');
const app = express();

app.use(express.json());

app.get('/api/users', (req, res) => {
  res.json({ users: [] });
});

app.post('/api/users', (req, res) => {
  // Create user logic
  res.status(201).json({ id: 1, ...req.body });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

### Async Handling
```javascript
app.get('/api/data', async (req, res, next) => {
  try {
    const data = await fetchData();
    res.json(data);
  } catch (error) {
    next(error);
  }
});
```

## Key Topics

- **Node.js Event Loop**: Understanding asynchronous nature
- **Express.js**: Middleware, routing, error handling
- **Fastify**: High-performance framework
- **NestJS**: Full-featured framework with TypeScript support
- **Streams**: Working with streams for memory efficiency
- **Process Management**: PM2, clustering
- **Environment Variables**: dotenv, configuration
- **Debugging**: Chrome DevTools, logging

## Best Practices

✅ Use async/await for readability
✅ Implement proper error handling
✅ Use middleware for cross-cutting concerns
✅ Structure code with separation of concerns
✅ Use environment variables
✅ Implement logging and monitoring
✅ Secure with rate limiting and validation

