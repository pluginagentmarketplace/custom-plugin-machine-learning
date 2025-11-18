#!/usr/bin/env python3
"""Generate SKILL.md files for all skills in the plugin."""

import os
import json
from pathlib import Path

# Define all skills with their metadata
skills_data = {
    "frontend": {
        "html-css-design": {
            "name": "html-css-design",
            "title": "HTML, CSS & Modern Design",
            "description": "Master semantic HTML5, advanced CSS layouts, responsive design, and modern styling techniques including Flexbox, Grid, and animations.",
            "content": """# HTML, CSS & Modern Design

## Quick Start

### Semantic HTML5
```html
<article>
  <header>
    <h1>Article Title</h1>
    <time datetime="2024-01-15">January 15, 2024</time>
  </header>
  <section>Main content here</section>
  <footer>Article metadata</footer>
</article>
```

### CSS Grid Layout
```css
.container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}
```

### Responsive Design
```css
@media (max-width: 768px) {
  .container {
    grid-template-columns: 1fr;
  }
}
```

## Key Topics

- **Semantic HTML**: Use proper tags (article, section, nav, aside)
- **CSS Layouts**: Flexbox and Grid for modern layouts
- **Responsive Design**: Mobile-first approach with media queries
- **Accessibility**: ARIA attributes, semantic structure
- **Performance**: Critical CSS, lazy loading images
- **Design Systems**: Creating reusable component systems
- **CSS Preprocessors**: SASS/SCSS for organized styling

## Best Practices

✅ Use semantic HTML elements
✅ Mobile-first responsive design
✅ Optimize images and assets
✅ Implement CSS best practices
✅ Test accessibility (WCAG)
✅ Use CSS Grid and Flexbox
✅ Avoid CSS specificity issues
"""
        },
        "javascript-ecosystem": {
            "name": "javascript-ecosystem",
            "title": "JavaScript Ecosystem & ES6+",
            "description": "Deep dive into modern JavaScript, ES6+ features, async programming, and the rich JavaScript ecosystem.",
            "content": """# JavaScript Ecosystem & ES6+

## Quick Start

### Modern JavaScript Syntax
```javascript
// Arrow functions
const greet = (name) => `Hello, ${name}!`;

// Destructuring
const { name, age } = person;

// Spread operator
const newArray = [...array, 4, 5];

// Template literals
const message = `${name} is ${age} years old`;
```

### Async Programming
```javascript
// async/await
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    return response.json();
  } catch (error) {
    console.error(error);
  }
}

// Promise chains
fetch('/api/data')
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

## Key Topics

- **ES6+ Features**: Arrow functions, classes, modules, template literals
- **Async Programming**: Promises, async/await, error handling
- **Functional Programming**: Array methods, map/filter/reduce
- **Module System**: CommonJS vs ES Modules
- **npm Ecosystem**: Package management, scripts
- **Testing**: Jest, Vitest, testing strategies
- **Tooling**: Webpack, Vite, Parcel, build optimization

## Best Practices

✅ Use const by default, let when needed
✅ Prefer arrow functions for callbacks
✅ Use async/await over .then()
✅ Handle errors properly
✅ Use destructuring for cleaner code
✅ Understand hoisting and scope
✅ Optimize bundle size
"""
        },
        "react-modern-frontend": {
            "name": "react-modern-frontend",
            "title": "React & Modern Frontend",
            "description": "Master React with hooks, functional components, state management, and modern best practices.",
            "content": """# React & Modern Frontend

## Quick Start

### Functional Components with Hooks
```jsx
import { useState, useEffect } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Count: ${count}`;
  }, [count]);

  return (
    <button onClick={() => setCount(count + 1)}>
      Clicked {count} times
    </button>
  );
}
```

### Custom Hooks
```javascript
function useWindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handleResize = () => setWidth(window.innerWidth);
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return width;
}
```

## Key Topics

- **React Hooks**: useState, useEffect, useContext, useReducer
- **Component Patterns**: Composition, render props, compound components
- **State Management**: Context API, Redux, Zustand
- **Performance**: React.memo, useMemo, useCallback
- **Server Components**: RSC, Next.js, streaming
- **Testing**: React Testing Library, Jest
- **Best Practices**: Key props, avoiding prop drilling, composition

## Best Practices

✅ Use functional components and hooks
✅ Memoize expensive computations
✅ Avoid prop drilling with Context
✅ Use proper key props in lists
✅ Handle loading and error states
✅ Test user interactions, not implementation
✅ Optimize bundle size
"""
        },
        "frontend-frameworks": {
            "name": "frontend-frameworks",
            "title": "Frontend Frameworks Comparison",
            "description": "Understand and compare modern frontend frameworks: React, Vue, Angular, and others.",
            "content": """# Frontend Frameworks Comparison

## Framework Overview

### React
- **Size**: ~40KB minified
- **Learning Curve**: Moderate
- **Ecosystem**: Largest third-party ecosystem
- **Use Case**: SPAs, complex UIs

### Vue.js
- **Size**: ~33KB minified
- **Learning Curve**: Gentle
- **Ecosystem**: Growing, good official plugins
- **Use Case**: SPAs, progressive enhancement

### Angular
- **Size**: ~130KB minified
- **Learning Curve**: Steep
- **Ecosystem**: Complete framework with batteries
- **Use Case**: Large enterprise applications

### Svelte
- **Size**: ~3.6KB minified
- **Learning Curve**: Moderate
- **Ecosystem**: Smaller but growing
- **Use Case**: Performance-critical apps

## Choosing a Framework

1. **Project Size**: Small → Svelte, Medium/Large → React/Vue, Enterprise → Angular
2. **Team Experience**: Use what team knows
3. **Performance Requirements**: Svelte for maximum performance
4. **Time to Market**: Vue or React for faster development
5. **Long-term Maintenance**: Consider community size

## Key Topics

- Framework comparison criteria
- Virtual DOM vs Reactivity systems
- Component models
- Routing and state management
- Server-side rendering
- Build tooling and performance
- Learning resources and community
"""
        }
    },
    "backend": {
        "rest-api-design": {
            "name": "rest-api-design",
            "title": "REST API Design",
            "description": "Master RESTful API design principles, HTTP methods, status codes, and best practices.",
            "content": """# REST API Design

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
"""
        },
        "nodejs-runtime": {
            "name": "nodejs-runtime",
            "title": "Node.js Runtime & Frameworks",
            "description": "Master Node.js runtime, event-driven architecture, and popular frameworks.",
            "content": """# Node.js Runtime & Frameworks

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
"""
        },
        "backend-frameworks": {
            "name": "backend-frameworks",
            "title": "Backend Frameworks (Spring Boot, ASP.NET, Go, etc)",
            "description": "Overview of popular backend frameworks across different languages.",
            "content": """# Backend Frameworks

## Java - Spring Boot

```java
@SpringBootApplication
public class Application {
  public static void main(String[] args) {
    SpringApplication.run(Application.class, args);
  }
}

@RestController
@RequestMapping("/api/users")
public class UserController {
  @GetMapping
  public List<User> getUsers() {
    return new ArrayList<>();
  }
}
```

## Python - Django

```python
from django.urls import path
from django.http import JsonResponse

def get_users(request):
    return JsonResponse({'users': []})

urlpatterns = [
    path('api/users/', get_users),
]
```

## Go - Gin

```go
package main

func main() {
  router := gin.Default()
  router.GET("/api/users", getUsers)
  router.Run(":3000")
}

func getUsers(c *gin.Context) {
  c.JSON(200, gin.H{"users": []})
}
```

## Framework Comparison

- **Spring Boot**: Enterprise-grade, rich ecosystem, steep learning curve
- **Django**: Full-featured, batteries included, great documentation
- **Go (Gin)**: High performance, simple, great for microservices
- **Rust (Actix)**: Type-safe, fast, modern language

## Key Topics

- Framework patterns and architectures
- Dependency injection
- Request validation
- Error handling
- Testing frameworks
- Deployment strategies
"""
        },
        "graphql-advanced-apis": {
            "name": "graphql-advanced-apis",
            "title": "GraphQL & Advanced API Design",
            "description": "Master GraphQL for flexible, powerful API development.",
            "content": """# GraphQL & Advanced API Design

## Quick Start

### Basic GraphQL Schema
```graphql
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
}

type Query {
  user(id: ID!): User
  users: [User!]!
  post(id: ID!): Post
}

type Mutation {
  createUser(name: String!, email: String!): User!
  createPost(title: String!, content: String!): Post!
}
```

### Query Examples
```graphql
query {
  user(id: "1") {
    name
    email
    posts {
      title
    }
  }
}
```

## Key Topics

- **Schema Design**: Types, queries, mutations, subscriptions
- **Resolvers**: Writing efficient resolvers
- **DataLoader**: Preventing N+1 queries
- **Authentication**: Securing GraphQL endpoints
- **Subscriptions**: Real-time data with WebSockets
- **Performance**: Query cost analysis, rate limiting
- **Federation**: Apollo Federation for microservices
- **Best Practices**: Schema conventions, error handling

## Best Practices

✅ Design schemas carefully
✅ Use DataLoader for batch queries
✅ Implement proper error handling
✅ Version APIs with fields, not breaking changes
✅ Document with SDL
✅ Implement authentication and authorization
✅ Monitor query performance
"""
        }
    },
    "fullstack": {
        "typescript-advanced": {
            "name": "typescript-advanced",
            "title": "Advanced TypeScript",
            "description": "Master advanced TypeScript patterns, generics, and type system features.",
            "content": """# Advanced TypeScript

## Quick Start

### Generics
```typescript
function identity<T>(arg: T): T {
  return arg;
}

const result = identity<string>("hello");
```

### Generic Constraints
```typescript
interface WithId {
  id: number;
}

function getId<T extends WithId>(obj: T): number {
  return obj.id;
}
```

### Utility Types
```typescript
type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};

type Partial<T> = {
  [K in keyof T]?: T[K];
};

type Pick<T, K extends keyof T> = {
  [P in K]: T[P];
};
```

## Advanced Concepts

- **Generics**: Writing reusable, type-safe code
- **Utility Types**: Readonly, Partial, Pick, Record, etc.
- **Conditional Types**: Type inference and branching
- **Template Literal Types**: Type manipulation
- **Decorators**: Metadata and aspect-oriented programming
- **Module Resolution**: Path mapping, imports
- **Type Guards**: Narrowing types effectively

## Best Practices

✅ Use generics for reusable components
✅ Leverage utility types
✅ Write strict TypeScript configuration
✅ Avoid `any` type
✅ Use discriminated unions
✅ Proper error handling
"""
        },
        "nextjs-modern-web": {
            "name": "nextjs-modern-web",
            "title": "Next.js & Modern Web Development",
            "description": "Master Next.js for production-ready full-stack applications.",
            "content": """# Next.js & Modern Web Development

## Quick Start

### App Router (Next.js 13+)
```typescript
// app/page.tsx
export default function Home() {
  return <h1>Welcome</h1>;
}

// app/api/users/route.ts
export async function GET() {
  return Response.json({ users: [] });
}
```

### Server Components
```typescript
// Server component by default
export default async function Posts() {
  const posts = await fetchPosts();
  return (
    <ul>
      {posts.map(post => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

## Key Features

- **App Router**: File-based routing, server components
- **SSR/SSG**: Server-side rendering and static generation
- **API Routes**: Backend endpoints in the same project
- **Image Optimization**: Automatic image optimization
- **Dynamic Routes**: [id], [...slug] patterns
- **Middleware**: Request interception
- **Database Integration**: Prisma, ORMs
- **Deployment**: Vercel, Docker

## Best Practices

✅ Use Server Components by default
✅ Implement proper error boundaries
✅ Optimize images and assets
✅ Use dynamic imports for large components
✅ Implement proper caching
✅ Secure API endpoints
✅ Use TypeScript for type safety
"""
        },
        "fullstack-patterns": {
            "name": "fullstack-patterns",
            "title": "Full Stack Architecture Patterns",
            "description": "Master patterns for building cohesive full-stack applications.",
            "content": """# Full Stack Architecture Patterns

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
"""
        }
    },
    "mobile": {
        "react-native-mobile": {
            "name": "react-native-mobile",
            "title": "React Native Mobile Development",
            "description": "Build cross-platform mobile apps with React Native.",
            "content": """# React Native Mobile Development

## Quick Start

### React Native Component
```javascript
import { View, Text, StyleSheet } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Hello Mobile!</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    fontSize: 24,
  },
});
```

## Key Topics

- **Core Components**: View, Text, ScrollView, FlatList
- **Navigation**: React Navigation stack, tab, drawer
- **State Management**: Redux, Context API, Zustand
- **Networking**: Fetch, axios, real-time APIs
- **Platform-Specific Code**: .ios.js, .android.js, Platform.select
- **Native Modules**: Bridging to native code
- **Performance**: FlatList optimization, Hermes engine
- **Testing**: Testing Library, Detox

## Best Practices

✅ Use FlatList for long lists
✅ Optimize images and assets
✅ Handle platform differences
✅ Test on real devices
✅ Use native modules wisely
✅ Monitor performance
✅ Implement proper error handling
"""
        },
        "flutter-development": {
            "name": "flutter-development",
            "title": "Flutter & Dart Development",
            "description": "Master Flutter for beautiful, high-performance mobile apps.",
            "content": """# Flutter & Dart Development

## Quick Start

### Flutter Widget
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Flutter')),
        body: const Center(child: Text('Hello Flutter!')),
      ),
    );
  }
}
```

## Key Topics

- **Widgets**: StatelessWidget, StatefulWidget, CustomPaint
- **Flutter Architecture**: Widget tree, rendering pipeline
- **State Management**: Provider, Riverpod, GetX, BLoC
- **Navigation**: Navigator, GoRouter, deep linking
- **Networking**: HTTP, WebSockets, API integration
- **Performance**: Profiling, optimization, frame rates
- **Testing**: Unit tests, widget tests, integration tests
- **Deployment**: iOS and Android release process

## Best Practices

✅ Use const constructors
✅ Separate business logic from UI
✅ Use proper state management
✅ Optimize rebuilds
✅ Test thoroughly
✅ Use design patterns
✅ Handle errors gracefully
"""
        },
        "native-ios-swift": {
            "name": "native-ios-swift",
            "title": "Native iOS Development with Swift",
            "description": "Develop native iOS apps using Swift and SwiftUI.",
            "content": """# Native iOS Development with Swift

## Quick Start

### SwiftUI View
```swift
import SwiftUI

struct ContentView: View {
    @State private var count = 0

    var body: some View {
        VStack {
            Text("Count: \\(count)")
                .font(.headline)

            Button(action: { count += 1 }) {
                Text("Increment")
            }
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
```

## Key Topics

- **SwiftUI**: Declarative UI framework
- **State Management**: @State, @Binding, @ObservedObject
- **Navigation**: NavigationStack, NavigationSplitView
- **Networking**: URLSession, Combine, async/await
- **Core Data**: Local data persistence
- **AsyncAwait**: Modern concurrency model
- **Performance**: View optimization, memory management
- **Testing**: XCTest, UI testing

## Best Practices

✅ Use SwiftUI for new projects
✅ Leverage Swift's type safety
✅ Use @State and @Binding properly
✅ Handle optionals carefully
✅ Test UI thoroughly
✅ Monitor memory usage
✅ Use async/await for concurrency
"""
        }
    },
    "database": {
        "sql-databases": {
            "name": "sql-databases",
            "title": "SQL Databases & Queries",
            "description": "Master SQL, relational databases, and query optimization.",
            "content": """# SQL Databases & Queries

## Quick Start

### Basic Queries
```sql
-- SELECT
SELECT id, name, email FROM users WHERE age > 18;

-- JOIN
SELECT u.name, p.title
FROM users u
JOIN posts p ON u.id = p.user_id;

-- Aggregation
SELECT category, COUNT(*)
FROM posts
GROUP BY category;

-- Subqueries
SELECT name FROM users
WHERE id IN (SELECT user_id FROM posts);
```

## Advanced Queries

- **Window Functions**: OVER, PARTITION BY, ROW_NUMBER
- **CTEs**: WITH clauses, recursive queries
- **Transactions**: ACID compliance, isolation levels
- **Indexes**: B-tree, hash indexes, composite indexes
- **Query Optimization**: EXPLAIN ANALYZE, cost estimation

## Database Systems

- **PostgreSQL**: Advanced features, JSON support
- **MySQL**: Popular, reliable, good performance
- **SQL Server**: Enterprise features, T-SQL
- **SQLite**: Embedded, lightweight

## Best Practices

✅ Use parameterized queries
✅ Create appropriate indexes
✅ Normalize schemas
✅ Use transactions for consistency
✅ Monitor slow queries
✅ Plan for backups
✅ Use constraints
"""
        },
        "nosql-databases": {
            "name": "nosql-databases",
            "title": "NoSQL Databases",
            "description": "Master NoSQL databases: MongoDB, Redis, DynamoDB, and more.",
            "content": """# NoSQL Databases

## MongoDB

```javascript
// Insert
db.users.insertOne({ name: 'John', age: 30 });

// Query
db.users.find({ age: { $gt: 25 } });

// Update
db.users.updateOne({ name: 'John' }, { $set: { age: 31 } });

// Aggregation
db.users.aggregate([
  { $match: { age: { $gt: 25 } } },
  { $group: { _id: null, avgAge: { $avg: '$age' } } }
]);
```

## Redis

```
SET key value
GET key
DEL key
INCR counter
LPUSH list value
HSET hash field value
```

## Database Comparison

- **MongoDB**: Document model, flexible schema
- **Redis**: In-memory, caching, pub/sub
- **DynamoDB**: Serverless, managed, pay-per-request
- **Cassandra**: Distributed, high throughput
- **CouchDB**: Document database, replication

## Use Cases

- **MongoDB**: User profiles, content management
- **Redis**: Caching, sessions, leaderboards
- **DynamoDB**: High-traffic applications, real-time data

## Best Practices

✅ Choose right database for use case
✅ Index frequently queried fields
✅ Plan for scaling
✅ Monitor performance
✅ Implement caching strategies
✅ Use appropriate data structures
"""
        },
        "database-design": {
            "name": "database-design",
            "title": "Database Design & Modeling",
            "description": "Master database design, normalization, and data modeling.",
            "content": """# Database Design & Modeling

## Normalization Levels

### First Normal Form (1NF)
- Atomic values only
- No repeated groups

### Second Normal Form (2NF)
- Meets 1NF
- No partial dependencies

### Third Normal Form (3NF)
- Meets 2NF
- No transitive dependencies

## Entity-Relationship (ER) Modeling

```
[User] 1 ─── M [Post]
       |
       └─── M [Comment]

User: id, name, email, created_at
Post: id, title, content, user_id, created_at
Comment: id, content, post_id, user_id, created_at
```

## Relationships

- **One-to-One**: User → Profile
- **One-to-Many**: User → Posts
- **Many-to-Many**: Student → Courses

## Design Principles

- **DRY**: Don't repeat data
- **Consistency**: Same types, formats
- **Integrity**: Constraints, foreign keys
- **Performance**: Indexes, query optimization

## Scaling Strategies

- **Vertical Scaling**: Bigger server
- **Horizontal Scaling**: Sharding, replication
- **Caching**: Redis, Memcached
- **Read Replicas**: Distribute reads

## Best Practices

✅ Normalize appropriately
✅ Use proper data types
✅ Add constraints
✅ Plan for growth
✅ Use indexes wisely
✅ Monitor performance
"""
        }
    },
    "cloud-devops": {
        "docker-containers": {
            "name": "docker-containers",
            "title": "Docker & Container Technology",
            "description": "Master Docker for containerization and application deployment.",
            "content": """# Docker & Container Technology

## Quick Start

### Dockerfile
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]
```

### Docker Commands
```bash
docker build -t myapp:1.0 .
docker run -p 3000:3000 myapp:1.0
docker push myapp:1.0
docker-compose up
```

### Docker Compose
```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
```

## Key Concepts

- **Images**: Blueprints for containers
- **Containers**: Runtime instances
- **Registries**: Docker Hub, ECR, private registries
- **Volumes**: Persistent storage
- **Networks**: Container communication
- **Multi-stage Builds**: Optimized production images

## Best Practices

✅ Use alpine images for size
✅ Multi-stage builds
✅ Use .dockerignore
✅ Don't run as root
✅ Pin base image versions
✅ Use health checks
✅ Optimize layer caching
"""
        },
        "kubernetes-orchestration": {
            "name": "kubernetes-orchestration",
            "title": "Kubernetes & Container Orchestration",
            "description": "Master Kubernetes for managing containerized applications at scale.",
            "content": """# Kubernetes & Container Orchestration

## Quick Start

### Deployment Manifest
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:1.0
        ports:
        - containerPort: 3000
        env:
        - name: PORT
          value: "3000"
```

### Service Manifest
```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
  type: LoadBalancer
```

## Key Concepts

- **Pods**: Smallest deployable unit
- **Deployments**: Manage pod replicas
- **Services**: Load balancing and discovery
- **ConfigMaps**: Configuration management
- **Secrets**: Sensitive data management
- **Persistent Volumes**: Storage
- **Namespaces**: Logical isolation
- **Ingress**: HTTP routing

## Best Practices

✅ Use resource limits
✅ Implement health checks
✅ Use rolling updates
✅ Separate config from code
✅ Use namespaces
✅ Monitor and log
✅ Security best practices
"""
        },
        "aws-cloud": {
            "name": "aws-cloud",
            "title": "AWS Cloud Services",
            "description": "Master AWS services for building scalable cloud applications.",
            "content": """# AWS Cloud Services

## Core Services

### Compute
- **EC2**: Virtual machines, autoscaling
- **Lambda**: Serverless functions
- **ECS**: Docker container orchestration
- **EKS**: Kubernetes on AWS

### Database
- **RDS**: Relational databases
- **DynamoDB**: NoSQL database
- **Aurora**: High-performance relational

### Storage
- **S3**: Object storage
- **EBS**: Block storage
- **EFS**: File storage

### Networking
- **VPC**: Virtual private cloud
- **CloudFront**: CDN
- **ALB**: Load balancing

## Getting Started

```bash
# Configure AWS CLI
aws configure

# Launch EC2 instance
aws ec2 run-instances --image-id ami-xxx

# Upload to S3
aws s3 cp file.txt s3://bucket/
```

## Key Concepts

- **Regions**: Geographic locations
- **Availability Zones**: Independent datacenters
- **IAM**: Identity and access management
- **Security Groups**: Firewall rules
- **Auto Scaling**: Automatic scaling

## Best Practices

✅ Use least privilege IAM
✅ Enable encryption
✅ Use managed services
✅ Monitor costs
✅ Implement disaster recovery
✅ Use infrastructure as code
"""
        },
        "terraform-iac": {
            "name": "terraform-iac",
            "title": "Terraform & Infrastructure as Code",
            "description": "Master Terraform for managing cloud infrastructure as code.",
            "content": """# Terraform & Infrastructure as Code

## Quick Start

### Main Configuration
```hcl
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "example"
  }
}

resource "aws_s3_bucket" "example" {
  bucket = "my-bucket"
}

output "instance_ip" {
  value = aws_instance.example.public_ip
}
```

## Key Concepts

- **Resources**: Infrastructure components
- **Variables**: Input values
- **Outputs**: Return values
- **State**: Track infrastructure
- **Modules**: Reusable components
- **Providers**: Infrastructure platforms

## Commands

```bash
terraform init          # Initialize
terraform plan          # Preview changes
terraform apply         # Apply changes
terraform destroy       # Destroy infrastructure
terraform state list    # View state
```

## Best Practices

✅ Version control everything
✅ Use modules
✅ Use variables
✅ Implement remote state
✅ Use workspaces
✅ Follow naming conventions
✅ Document infrastructure
"""
        },
        "linux-sysadmin": {
            "name": "linux-sysadmin",
            "title": "Linux System Administration",
            "description": "Master Linux for server management and system administration.",
            "content": """# Linux System Administration

## Essential Commands

### File Management
```bash
ls -la              # List files with details
cp source dest      # Copy files
mv source dest      # Move files
rm file            # Remove file
mkdir dirname      # Create directory
find . -name "*.log"  # Find files
```

### User Management
```bash
useradd username   # Create user
passwd username    # Set password
usermod -aG sudo username  # Add to group
userdel username   # Delete user
```

### Permissions
```bash
chmod 755 file     # Set permissions (rwxr-xr-x)
chown user:group file  # Change owner
chmod +x script.sh # Make executable
```

### System Information
```bash
uname -a          # System info
df -h             # Disk usage
ps aux            # Running processes
top               # Process monitor
```

## Package Management

```bash
apt update && apt upgrade    # Debian/Ubuntu
yum update && yum upgrade    # RedHat/CentOS
apt install package          # Install package
```

## Networking

```bash
ifconfig          # Network interfaces
netstat -tuln     # Listening ports
ss -tuln          # Modern netstat
ping host         # Test connectivity
ssh user@host     # Remote login
scp file user@host:/path  # Copy over SSH
```

## Best Practices

✅ Use sudo instead of root
✅ Regular backups
✅ Monitor logs
✅ Keep system updated
✅ Configure firewall
✅ Manage SSH keys
✅ Document changes
"""
        }
    },
    "ai-ml": {
        "machine-learning-fundamentals": {
            "name": "machine-learning-fundamentals",
            "title": "Machine Learning Fundamentals",
            "description": "Master ML fundamentals, algorithms, and best practices.",
            "content": """# Machine Learning Fundamentals

## Quick Start

### Linear Regression
```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 5, 4])

model = LinearRegression()
model.fit(X, y)
predictions = model.predict([[5]])
```

### Classification
```python
from sklearn.tree import DecisionTreeClassifier

X = [[0, 0], [1, 1]]
y = [0, 1]

clf = DecisionTreeClassifier()
clf.fit(X, y)
clf.predict([[2, 2]])
```

## ML Workflow

1. **Data Collection**: Gather training data
2. **Preprocessing**: Clean, normalize, split
3. **Feature Engineering**: Select/create features
4. **Model Selection**: Choose algorithm
5. **Training**: Fit model to data
6. **Evaluation**: Assess performance
7. **Hyperparameter Tuning**: Optimize
8. **Deployment**: Put model in production

## Key Algorithms

- **Regression**: Linear, polynomial, ridge
- **Classification**: Logistic, SVM, Random Forest
- **Clustering**: K-means, hierarchical
- **Ensemble**: Gradient Boosting, Random Forest

## Evaluation Metrics

- **Regression**: MSE, RMSE, R²
- **Classification**: Accuracy, Precision, Recall, F1
- **Clustering**: Silhouette score, Davies-Bouldin

## Best Practices

✅ Always split train/test data
✅ Scale/normalize features
✅ Handle missing values
✅ Avoid overfitting
✅ Cross-validate
✅ Use appropriate metrics
✅ Document experiments
"""
        },
        "deep-learning-neural-networks": {
            "name": "deep-learning-neural-networks",
            "title": "Deep Learning & Neural Networks",
            "description": "Master deep learning architectures and neural networks.",
            "content": """# Deep Learning & Neural Networks

## Quick Start

### TensorFlow/Keras
```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=10)
```

### PyTorch
```python
import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = Net()
```

## Neural Network Architectures

- **CNNs**: Convolutional, for images
- **RNNs**: Recurrent, for sequences
- **LSTMs**: Long short-term memory
- **Transformers**: Attention-based models
- **GANs**: Generative models
- **Autoencoders**: Unsupervised learning

## Training Process

1. **Forward Pass**: Compute predictions
2. **Loss Calculation**: Measure error
3. **Backpropagation**: Compute gradients
4. **Weight Update**: Adjust parameters

## Best Practices

✅ Use GPU when available
✅ Implement data augmentation
✅ Use batch normalization
✅ Monitor with TensorBoard
✅ Prevent overfitting
✅ Use pretrained models
✅ Save checkpoints
"""
        },
        "data-science-analytics": {
            "name": "data-science-analytics",
            "title": "Data Science & Analytics",
            "description": "Master data analysis, visualization, and insights extraction.",
            "content": """# Data Science & Analytics

## Quick Start

### Pandas Data Analysis
```python
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Explore
df.head()
df.info()
df.describe()

# Filter
df[df['age'] > 30]

# Group
df.groupby('category')['value'].sum()

# Aggregate
df.agg({'value': 'sum', 'count': 'mean'})
```

### Data Visualization
```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='age', y='income')
plt.title('Age vs Income')
plt.show()
```

## Analytics Process

1. **Question Definition**: What to analyze?
2. **Data Collection**: Gather relevant data
3. **Data Cleaning**: Remove outliers, handle missing
4. **Exploration**: Understand patterns
5. **Analysis**: Statistical tests
6. **Visualization**: Create insights
7. **Communication**: Present findings

## Statistical Analysis

- **Descriptive Stats**: Mean, median, std dev
- **Hypothesis Testing**: T-tests, chi-square
- **Correlation**: Pearson, Spearman
- **Regression Analysis**: Linear, logistic

## Tools

- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Matplotlib**: Visualization
- **Seaborn**: Statistical visualization
- **Plotly**: Interactive dashboards

## Best Practices

✅ Ask clear questions
✅ Validate assumptions
✅ Use appropriate visualizations
✅ Test hypotheses
✅ Document methodology
✅ Avoid misleading charts
✅ Cite data sources
"""
        },
        "mlops-deployment": {
            "name": "mlops-deployment",
            "title": "MLOps & Model Deployment",
            "description": "Master model deployment, versioning, and production ML systems.",
            "content": """# MLOps & Model Deployment

## Model Serving

### Flask REST API
```python
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction[0]})
```

### Docker Deployment
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY model.pkl .
COPY app.py .
CMD ["python", "app.py"]
```

## MLOps Frameworks

- **MLflow**: Experiment tracking, model registry
- **Kubeflow**: ML on Kubernetes
- **DVC**: Data and model versioning
- **Weights & Biases**: Experiment tracking
- **Seldon**: Model serving platform

## ML Pipeline

```
Data → Training → Validation → Deployment → Monitoring
```

## Key Concepts

- **Model Versioning**: Track model changes
- **A/B Testing**: Compare model versions
- **Monitoring**: Performance, drift detection
- **Retraining**: Update models regularly
- **Data Pipeline**: Automated data processing
- **CI/CD for ML**: Automated model deployment

## Best Practices

✅ Version everything
✅ Automate pipelines
✅ Monitor in production
✅ Handle data drift
✅ Plan retraining
✅ Test models thoroughly
✅ Document decisions
"""
        }
    },
    "specialized": {
        "system-design": {
            "name": "system-design",
            "title": "System Design & Architecture",
            "description": "Master system design for scalable, reliable applications.",
            "content": """# System Design & Architecture

## Core Principles

### Scalability
- **Horizontal**: Add more servers
- **Vertical**: More powerful servers
- **Database Sharding**: Partition data

### Reliability
- **Redundancy**: Backup systems
- **Replication**: Data copies
- **Load Balancing**: Distribute traffic

### Consistency
- **ACID**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Choose 2 of 3 (Consistency, Availability, Partition tolerance)
- **Eventual Consistency**: Accept temporary inconsistency

## Design Patterns

### Caching
```
Client → Cache → Database
```

### Load Balancing
```
Clients → Load Balancer → Servers
```

### Database Replication
```
Primary → Replicas (read-only)
```

## Common Architectures

- **Monolith**: Single application
- **Microservices**: Independent services
- **Serverless**: Function-based
- **Event-Driven**: Message-based

## Estimation

- **Traffic**: QPS, concurrent users
- **Storage**: Data volume, growth
- **Bandwidth**: Data transfer rates
- **Latency**: Response time targets

## Design Examples

- **Twitter**: Distributed, high throughput
- **YouTube**: Video streaming, CDN
- **Uber**: Real-time location, matching
- **Instagram**: Photo storage, feed generation

## Best Practices

✅ Plan for scale
✅ Use proven patterns
✅ Monitor everything
✅ Plan for failure
✅ Use caching wisely
✅ Document decisions
"""
        },
        "software-architecture": {
            "name": "software-architecture",
            "title": "Software Architecture & Design Patterns",
            "description": "Master software architecture principles and design patterns.",
            "content": """# Software Architecture & Design Patterns

## Architectural Patterns

### MVC (Model-View-Controller)
```
User → Controller → Model → View → User
```

### MVVM (Model-View-ViewModel)
```
View ↔ ViewModel ↔ Model
```

### Layered Architecture
```
UI Layer → Business Logic → Data Access → Database
```

### Microservices
```
API Gateway → [Service1, Service2, Service3]
```

## Design Patterns

### Creational
- **Singleton**: Single instance
- **Factory**: Object creation
- **Builder**: Complex object construction

### Structural
- **Adapter**: Interface compatibility
- **Decorator**: Add functionality
- **Facade**: Simplified interface

### Behavioral
- **Observer**: Event handling
- **Strategy**: Algorithm selection
- **State**: Object state management

## SOLID Principles

- **S**ingle Responsibility
- **O**pen/Closed Principle
- **L**iskov Substitution
- **I**nterface Segregation
- **D**ependency Inversion

## Clean Code

```python
# Good
def calculate_total_price(items):
    return sum(item.price * item.quantity for item in items)

# Bad
def calc(i):
    t = 0
    for x in i:
        t += x.p * x.q
    return t
```

## Best Practices

✅ Keep it simple
✅ DRY principle
✅ SOLID principles
✅ Proper naming
✅ Document decisions
✅ Code reviews
✅ Refactor regularly
"""
        },
        "testing-qa": {
            "name": "testing-qa",
            "title": "Testing & Quality Assurance",
            "description": "Master testing strategies and quality assurance practices.",
            "content": """# Testing & Quality Assurance

## Testing Pyramid

```
    △ E2E
   ▲▲▲ Integration
  ▲▲▲▲▲ Unit
```

Most tests at bottom, fewer at top.

## Test Types

### Unit Testing
```javascript
test('adds two numbers', () => {
  expect(add(2, 3)).toBe(5);
});
```

### Integration Testing
```javascript
test('user signup flow', async () => {
  const response = await signupUser(userData);
  expect(response.status).toBe(201);
});
```

### End-to-End Testing
```javascript
test('user can login and view dashboard', async () => {
  await page.goto('/login');
  await page.fill('[name=email]', 'user@test.com');
  // ... more steps
});
```

## Testing Frameworks

- **JavaScript**: Jest, Vitest, Testing Library
- **Python**: pytest, unittest
- **Java**: JUnit, Mockito
- **Go**: testing, testify

## QA Practices

- **Test-Driven Development**: Write tests first
- **Continuous Testing**: Automated test runs
- **Code Coverage**: Measure test coverage
- **Performance Testing**: Load, stress tests
- **Security Testing**: Vulnerability scanning

## Best Practices

✅ Test behavior, not implementation
✅ Aim for high coverage
✅ Automate repetitive tests
✅ Test edge cases
✅ Keep tests maintainable
✅ Run tests frequently
✅ Document test strategy
"""
        }
    }
}

# Create skills
for category, skills in skills_data.items():
    for skill_id, skill_info in skills.items():
        # Create directory
        skill_dir = f"skills/{category}/{skill_id}"
        os.makedirs(skill_dir, exist_ok=True)

        # Create SKILL.md
        skill_content = f"""---
name: {skill_info['name']}
description: {skill_info['description']}
---

{skill_info['content']}
"""

        skill_file = f"{skill_dir}/SKILL.md"
        with open(skill_file, 'w') as f:
            f.write(skill_content)

        print(f"✅ Created {skill_file}")

print(f"\n✨ Created {len([s for c in skills_data.values() for s in c])} skill files!")
