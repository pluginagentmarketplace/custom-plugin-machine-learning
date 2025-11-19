---
name: fullstack-patterns
description: Master patterns for building cohesive full-stack applications.
---

# Full Stack Architecture Patterns

## Client-Server Communication

### REST Pattern
```
Client → HTTP Request → Server
Server → JSON Response → Client
```

### GraphQL Pattern
```
Client → GraphQL Query → Server
Server → Typed Response → Client
```

### Real-time Pattern (WebSockets)
```
Client ↔ WebSocket ↔ Server
Bidirectional communication
```

## State Management Patterns

- **Server State**: Database, cache, external APIs
- **Client State**: UI state, user preferences
- **Sync Strategy**: Automatic sync, manual sync, optimistic updates

## Data Flow Patterns

1. **Traditional MVC**: Routes → Controllers → Models → Views
2. **Component-Driven**: Components → State → Data Fetching
3. **Event-Driven**: Events → Handlers → State Updates
4. **Query-Based**: Queries → Resolvers → Data

## Common Patterns

- **Repository Pattern**: Data access abstraction
- **Middleware Pattern**: Cross-cutting concerns
- **Observer Pattern**: Real-time updates
- **Factory Pattern**: Object creation
- **Decorator Pattern**: Adding functionality

## Best Practices

✅ Separate concerns clearly
✅ Keep components focused
✅ Use consistent patterns
✅ Document architecture decisions
✅ Plan for scalability
✅ Implement proper testing

