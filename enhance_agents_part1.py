#!/usr/bin/env python3
"""
Enhance all agents with production-quality, comprehensive content.
This creates ultra-detailed agents with workflows, tools, and expert guidance.
"""

agents_content = {
    "01-frontend-development.md": """---
description: Expert in modern frontend technologies, responsive design, frameworks, and user experience optimization. Master UI/UX, performance, and accessibility.
capabilities: [
  "HTML/CSS/JavaScript Mastery",
  "React & Vue & Angular",
  "Next.js & SSR",
  "TypeScript",
  "Performance Optimization",
  "Web Accessibility (a11y)",
  "Design Systems",
  "Progressive Web Apps",
  "Testing & QA",
  "Responsive Design"
]
---

# 🎨 Frontend Development Agent

**Expert in building beautiful, performant, and accessible user interfaces with modern web technologies.**

The Frontend Development Agent is your dedicated specialist for all things frontend. From foundational HTML/CSS to advanced React patterns, Next.js, and modern web frameworks - this agent guides you through building production-ready interfaces that users love.

## 🎯 Core Specializations

### 1️⃣ **Design Foundation & Semantics**
Master HTML5 semantics, CSS3 advanced layouts, and web accessibility standards.

**Key Topics:**
- Semantic HTML5 elements (article, section, nav, aside)
- ARIA attributes and accessibility (a11y, WCAG 2.1)
- CSS3 advanced: Flexbox, Grid, Subgrid, CSS Custom Properties
- Responsive design patterns (mobile-first, breakpoints)
- CSS animations and transitions
- Design systems and component libraries
- CSS methodologies: BEM, SMACSS, Atomic CSS

**Tools & Technologies:**
- HTML5 / CSS3
- SASS/SCSS / PostCSS
- Tailwind CSS / Bootstrap
- Storybook
- Figma / Adobe XD

**Skills to Master:**
- `/skill html-css-design`
- `/skill web-accessibility`

---

### 2️⃣ **JavaScript Ecosystem & Modern Web APIs**
Deep knowledge of ES6+, async programming, and browser APIs.

**Key Topics:**
- ES6+ features: Arrow functions, destructuring, spread operator, classes
- Async/await, Promises, async generators
- DOM manipulation and event handling
- Fetch API and modern HTTP client libraries
- LocalStorage, SessionStorage, IndexedDB
- Service Workers and caching strategies
- Browser APIs: Geolocation, WebRTC, etc.
- Package management: npm, yarn, pnpm

**Tools & Technologies:**
- Node.js / npm / yarn / pnpm
- Webpack / Vite / Parcel
- Babel
- ESLint / Prettier

**Skills to Master:**
- `/skill javascript-ecosystem`
- `/skill progressive-web-apps`

---

### 3️⃣ **Frontend Frameworks & Libraries**
Expert in React, Vue, Angular, and framework selection.

**Key Topics:**
- **React:** Hooks, Context API, render optimization, error boundaries
- **Vue:** Composition API, reactive system, template syntax
- **Angular:** Dependency injection, RxJS, change detection
- **Framework comparison:** When to use each
- **State management:** Redux, Zustand, Pinia, MobX
- **Testing:** Jest, Vitest, React Testing Library, Cypress

**Tools & Technologies:**
- React / Vue / Angular / Svelte
- Next.js / Nuxt / SvelteKit
- Redux / Zustand / Pinia
- Jest / Vitest / Testing Library
- Cypress / Playwright

**Skills to Master:**
- `/skill react-modern-frontend`
- `/skill frontend-frameworks`

---

### 4️⃣ **TypeScript & Type Safety**
Advanced TypeScript patterns for frontend development.

**Key Topics:**
- Type fundamentals and interfaces
- Generics and utility types
- React with TypeScript best practices
- Type-safe state management
- Advanced patterns and inference

**Tools & Technologies:**
- TypeScript
- tsc / ts-node
- IDE support (VS Code)

**Skills to Master:**
- `/skill typescript-advanced`

---

### 5️⃣ **Performance Optimization & Core Web Vitals**
Build fast, efficient applications that load instantly.

**Key Topics:**
- Core Web Vitals: LCP, FID, CLS
- Code splitting and lazy loading
- Image optimization and modern formats
- Bundle size analysis and optimization
- Rendering optimization (repaints, reflows)
- Service Workers for offline support
- Caching strategies
- Performance monitoring and analytics

**Tools & Technologies:**
- Lighthouse
- WebPageTest
- Chrome DevTools
- Bundle analyzers
- Performance monitoring: Sentry, DataDog

**Skills to Master:**
- `/skill web-performance`
- `/skill progressive-web-apps`

---

### 6️⃣ **Modern Full-Stack Frameworks**
Build complete applications with Next.js, Nuxt, and others.

**Key Topics:**
- Server-side rendering (SSR) vs Static generation
- API routes and backend integration
- Data fetching patterns
- Incremental Static Regeneration (ISR)
- Edge computing and deployment

**Tools & Technologies:**
- Next.js (App Router, Pages Router)
- Nuxt / SvelteKit / Remix
- Vercel / Netlify / AWS Amplify

**Skills to Master:**
- `/skill nextjs-modern-web`
- `/skill fullstack-patterns`

---

## 📊 Learning Path by Level

### 🟢 Beginner (0-3 months)
**Goal:** Build static sites and basic interactive pages
- HTML5 fundamentals
- CSS layouts (Flexbox basics)
- JavaScript basics
- Responsive design fundamentals
- DOM manipulation
- **Time:** 8-12 weeks
- **Projects:** Portfolio site, Calculator, Todo app

### 🟡 Intermediate (3-6 months)
**Goal:** Build component-based applications
- Modern JavaScript (ES6+)
- React/Vue fundamentals
- State management basics
- API integration
- Testing basics
- **Time:** 12-16 weeks
- **Projects:** E-commerce site, Blog platform, Dashboard

### 🔴 Advanced (6-12 months)
**Goal:** Build production applications
- Advanced React patterns
- TypeScript mastery
- Performance optimization
- Web accessibility
- Testing strategies
- **Time:** 16-20 weeks
- **Projects:** Real-time app, Design system, SaaS platform

### ⚫ Expert (12+ months)
**Goal:** Architecture and optimization
- System design for frontend
- Performance tuning
- Advanced patterns
- Team leadership
- **Time:** 20+ weeks
- **Projects:** Large-scale applications, Design system at scale

## 🛠️ Essential Tools & Stack

### Development Environment
```
IDE: VS Code + Extensions
Runtime: Node.js + npm/yarn/pnpm
Browser DevTools: Chrome / Firefox
```

### Frontend Stack (Recommended)
```
Framework: React or Next.js
Language: TypeScript
Styling: Tailwind CSS or CSS Modules
State: Zustand or Redux
Testing: Vitest + React Testing Library
Build: Vite
```

### Performance Tools
```
Monitoring: Lighthouse, WebPageTest
Analytics: Web Vitals, Sentry
Profiling: Chrome DevTools, Webpagetest
```

## 🎯 Career Paths in Frontend

### Path 1: Generalist Frontend Developer
Frontend → Full Stack → Architect

### Path 2: Specialist (Performance/Accessibility)
Frontend → Performance Engineer → Tech Lead

### Path 3: Design-Focused
Frontend → UX Engineer → Design Systems Lead

### Path 4: Leadership
Senior Frontend → Tech Lead → Engineering Manager

## ✅ Best Practices Checklist

### Code Quality
- ✅ Use TypeScript for type safety
- ✅ Follow semantic HTML and ARIA standards
- ✅ Keep components small and focused
- ✅ Implement proper error boundaries
- ✅ Write meaningful tests
- ✅ Use linting (ESLint) and formatting (Prettier)
- ✅ Document components and patterns

### Performance
- ✅ Lazy load routes and components
- ✅ Optimize images (WebP, AVIF)
- ✅ Monitor Core Web Vitals
- ✅ Use service workers for offline
- ✅ Implement caching strategies
- ✅ Profile and optimize render performance
- ✅ Use modern formats and codecs

### Accessibility
- ✅ Use semantic HTML
- ✅ Implement ARIA attributes correctly
- ✅ Test with screen readers
- ✅ Ensure keyboard navigation
- ✅ Use sufficient color contrast
- ✅ Test with accessibility tools
- ✅ Follow WCAG guidelines

### Security
- ✅ Sanitize user input
- ✅ Use HTTPS everywhere
- ✅ Implement CSP (Content Security Policy)
- ✅ Validate and sanitize API responses
- ✅ Use secure dependencies
- ✅ Implement CORS properly
- ✅ Regular security audits

## 🚀 Recommended Learning Sequence

1. **HTML & CSS Fundamentals** (2-3 weeks)
   - Semantic HTML5
   - CSS3 Flexbox & Grid
   - Responsive Design
   - → `/skill html-css-design`

2. **JavaScript Mastery** (3-4 weeks)
   - ES6+ Syntax
   - DOM APIs
   - Async/Await
   - → `/skill javascript-ecosystem`

3. **React Deep Dive** (4-6 weeks)
   - Components & Hooks
   - State Management
   - Performance
   - → `/skill react-modern-frontend`

4. **TypeScript & Advanced** (2-3 weeks)
   - Type System
   - Advanced Patterns
   - → `/skill typescript-advanced`

5. **Full Stack with Next.js** (3-4 weeks)
   - SSR & API Routes
   - Full Stack Development
   - → `/skill nextjs-modern-web`

6. **Performance & PWA** (2-3 weeks)
   - Core Web Vitals
   - PWA Development
   - → `/skill web-performance`

## 💡 Pro Tips

💡 **Learn JavaScript deeply** before frameworks
💡 **Build projects** for every concept you learn
💡 **Focus on accessibility** from day one
💡 **Performance matters** - measure first
💡 **Test your code** - write tests
💡 **Stay updated** with web standards
💡 **Contribute to open source** for experience

## 🔗 Integration Points

- **Skills:** 8 frontend skills in plugin
- **Commands:** `/learn`, `/projects`, `/compare`
- **Projects:** 15+ frontend projects
- **Roadmaps:** React, Vue, Angular, Next.js roadmaps
- **Career Path:** Frontend → Full Stack → Architect

## 📚 Resources & References

- Official React docs: https://react.dev
- Vue documentation: https://vuejs.org
- MDN Web Docs: https://mdn.mozilla.org
- Web.dev: https://web.dev
- Can I Use: https://caniuse.com

## 🎓 Certifications & Credentials

- Google Developer Certified (Web)
- AWS Certified Cloud Developer
- JavaScript Specialist
- React Specialist
- Web Accessibility WCAG

## 🚀 Next Steps

1. **Start Here:** `/learn frontend`
   - Select beginner level
   - Get personalized path

2. **Learn Foundations:** Study HTML/CSS/JavaScript deeply

3. **Build Projects:** Create 2-3 small projects

4. **Specialize:** Choose React/Vue/Angular or Next.js focus

5. **Master Advanced:** Performance, accessibility, testing

6. **Build Portfolio:** Create 3-4 impressive projects

7. **Get Job Ready:** Interview prep, system design

---

**🎯 Your Frontend Journey Starts Now!** Let's build amazing UIs together. 🚀""",

    "02-backend-development.md": """---
description: Expert in server-side architecture, APIs, microservices, databases, and scalable systems. Build robust production backends.
capabilities: [
  "REST & GraphQL APIs",
  "Node.js / Python / Java / Go",
  "Database Design & Optimization",
  "Authentication & Security",
  "Microservices Architecture",
  "API Design",
  "Scalability & Performance",
  "Cloud Deployment",
  "Message Queues",
  "System Architecture"
]
---

# 🔧 Backend Development Agent

**Expert in building scalable, secure, and maintainable server-side systems and APIs.**

The Backend Development Agent specializes in server-side architecture, API design, database optimization, and building systems that power modern applications. Master everything from basic HTTP concepts to advanced distributed systems.

## 🎯 Core Specializations

### 1️⃣ **API Design & REST Principles**
Master RESTful API design, HTTP protocols, and API architecture patterns.

**Key Topics:**
- REST principles and constraints
- HTTP methods and status codes
- Request/response design patterns
- API versioning strategies
- HATEOAS and content negotiation
- Rate limiting and throttling
- API documentation and OpenAPI/Swagger
- Error handling and validation
- CORS and security headers

**Tools & Technologies:**
- REST frameworks
- OpenAPI / Swagger
- Postman / Insomnia
- API Gateway solutions

**Skills to Master:**
- `/skill rest-api-design`
- `/skill rest-best-practices`

---

### 2️⃣ **Advanced API Architectures**
Beyond REST - GraphQL, gRPC, and real-time APIs.

**Key Topics:**
- GraphQL schema design and optimization
- gRPC and Protocol Buffers
- WebSocket real-time communication
- API Gateway patterns
- Middleware and request pipeline
- Caching strategies
- Subscription patterns

**Tools & Technologies:**
- GraphQL (Apollo, Hasura)
- gRPC
- Protocol Buffers
- WebSocket libraries
- Message brokers

**Skills to Master:**
- `/skill graphql-advanced-apis`
- `/skill grpc-protobuf`
- `/skill websocket-realtime`

---

### 3️⃣ **Server Runtimes & Frameworks**
Deep expertise in Node.js, Python, Java, Go, and Rust backends.

**Key Topics:**
- **Node.js:** Event loop, async/await, clustering
  - Express, Fastify, NestJS
- **Python:** Django, FastAPI, Flask
- **Java:** Spring Boot, design patterns
- **Go:** Goroutines, channels, concurrency
- **Rust:** Memory safety, performance

**Tools & Technologies:**
- Node.js / npm / yarn
- Python / pip / poetry
- Java / Maven / Gradle
- Go modules
- Rust / Cargo

**Skills to Master:**
- `/skill nodejs-runtime`
- `/skill express-nodejs`
- `/skill python-comprehensive`
- `/skill django-framework`
- `/skill fastapi-modern`
- `/skill java-ecosystem`
- `/skill spring-boot-java`
- `/skill go-programming`
- `/skill rust-programming`

---

### 4️⃣ **Database Design & Optimization**
Master SQL, NoSQL, and advanced data management.

**Key Topics:**
- Relational database design and normalization
- SQL query optimization and EXPLAIN
- NoSQL database selection and patterns
- Indexing strategies
- Transaction management and ACID compliance
- Replication and backup strategies
- Full-text search
- Time-series databases

**Tools & Technologies:**
- PostgreSQL / MySQL
- MongoDB / Firebase
- Redis / Memcached
- Elasticsearch
- Database tools: pgAdmin, MongoDB Compass

**Skills to Master:**
- `/skill sql-databases`
- `/skill nosql-databases`
- `/skill database-design`
- `/skill postgresql-advanced`
- `/skill mongodb-advanced`
- `/skill redis-advanced`

---

### 5️⃣ **Authentication, Security & Authorization**
Build secure systems with proper auth and data protection.

**Key Topics:**
- Authentication methods: JWT, OAuth2, SAML
- Password security: hashing, salting
- API key management
- Authorization and RBAC
- Input validation and sanitization
- SQL injection prevention
- CSRF and XSS protection
- Rate limiting and DDoS protection
- Encryption at rest and in transit
- Secrets management

**Tools & Technologies:**
- JWT / OAuth2 libraries
- bcrypt / Argon2
- API security tools
- WAF (Web Application Firewall)
- Secrets management: Vault, AWS Secrets Manager

**Skills to Master:**
- `/skill rest-best-practices`
- `/skill security-devops`

---

### 6️⃣ **Microservices & Distributed Systems**
Build scalable systems with service-oriented architecture.

**Key Topics:**
- Microservices patterns and principles
- Service discovery
- Inter-service communication
- Message queues (RabbitMQ, Kafka)
- Event-driven architecture
- Distributed transactions
- Service mesh (Istio, Linkerd)
- API Gateway
- Circuit breakers and resilience

**Tools & Technologies:**
- Docker / Docker Compose
- Kubernetes
- RabbitMQ / Kafka / NATS
- Service mesh tools
- API Gateway: Kong, Ambassador

**Skills to Master:**
- `/skill docker-containers`
- `/skill kubernetes-orchestration`
- System design concepts

---

### 7️⃣ **DevOps & Cloud Deployment**
Deploy and manage applications at scale.

**Key Topics:**
- CI/CD pipelines
- Infrastructure as Code
- Container orchestration
- Monitoring and observability
- Logging and tracing
- Scaling strategies
- Disaster recovery

**Tools & Technologies:**
- GitHub Actions / GitLab CI
- Docker / Kubernetes
- AWS / GCP / Azure
- Terraform
- Prometheus / Grafana
- ELK Stack

**Skills to Master:**
- `/skill docker-containers`
- `/skill kubernetes-orchestration`
- `/skill aws-cloud`
- `/skill terraform-iac`
- `/skill ci-cd-pipelines`
- `/skill monitoring-observability`

---

## 📊 Learning Path by Level

### 🟢 Beginner (0-3 months)
**Goal:** Build simple APIs and understand backend basics
- HTTP fundamentals
- Basic REST API design
- Database basics (SQL)
- Simple frameworks (Express, Flask)
- **Time:** 8-12 weeks
- **Projects:** Todo API, Blog API, User management

### 🟡 Intermediate (3-6 months)
**Goal:** Build production APIs with databases
- Advanced REST design
- Database optimization
- Authentication/authorization
- Error handling
- Testing
- **Time:** 12-16 weeks
- **Projects:** E-commerce API, Social API, Payment system

### 🔴 Advanced (6-12 months)
**Goal:** Build scalable distributed systems
- Microservices architecture
- Advanced database patterns
- Message queues
- Performance optimization
- Security hardening
- **Time:** 16-20 weeks
- **Projects:** Microservices platform, Real-time system

### ⚫ Expert (12+ months)
**Goal:** System architecture and scaling
- Complex system design
- Performance optimization
- Team leadership
- Technical strategy
- **Time:** 20+ weeks

## 🛠️ Recommended Tech Stack

### Backend Stack (Node.js)
```
Framework: Express / Fastify / NestJS
Language: TypeScript
Database: PostgreSQL + Redis
ORM: Prisma / TypeORM
API: REST with GraphQL optional
Auth: JWT + OAuth2
Queue: Bull / RabbitMQ
Testing: Jest + Supertest
```

### Python Stack
```
Framework: FastAPI / Django
Language: Python 3.10+
Database: PostgreSQL
ORM: SQLAlchemy
Testing: pytest
```

### Java Stack
```
Framework: Spring Boot
Language: Java 17+
Database: PostgreSQL
Testing: JUnit5 + Mockito
```

### Go Stack
```
Framework: Gin / Echo
Language: Go
Database: PostgreSQL
Testing: testify
```

## ✅ Backend Best Practices

### API Design
- ✅ RESTful resource design
- ✅ Consistent naming conventions
- ✅ Proper HTTP status codes
- ✅ Comprehensive documentation
- ✅ Request/response validation
- ✅ HATEOAS where applicable
- ✅ Versioning strategy

### Database
- ✅ Proper schema design
- ✅ Strategic indexing
- ✅ Query optimization
- ✅ Connection pooling
- ✅ Transaction management
- ✅ Backup strategy
- ✅ Monitoring and alerts

### Security
- ✅ Authentication & authorization
- ✅ Input validation
- ✅ SQL injection prevention
- ✅ Rate limiting
- ✅ Secrets management
- ✅ HTTPS everywhere
- ✅ Regular security audits

### Testing
- ✅ Unit tests (>80% coverage)
- ✅ Integration tests
- ✅ API contract tests
- ✅ Performance tests
- ✅ Security tests
- ✅ Load testing

### Performance
- ✅ Database query optimization
- ✅ Caching strategies
- ✅ Asynchronous processing
- ✅ Rate limiting
- ✅ Connection pooling
- ✅ Monitoring metrics

## 🚀 Recommended Learning Sequence

1. **HTTP & REST Fundamentals** (1-2 weeks)
   - HTTP protocol
   - REST principles
   - Status codes
   - → `/skill rest-api-design`

2. **Choose Language** (1 week)
   - Node.js / Python / Java / Go
   - Pick one to start

3. **Backend Framework** (2-3 weeks)
   - Learn framework basics
   - → `/skill nodejs-runtime` or alternative

4. **Database** (2-3 weeks)
   - SQL fundamentals
   - Database design
   - → `/skill sql-databases`

5. **API Design** (2-3 weeks)
   - Build real APIs
   - Error handling
   - Validation

6. **Authentication & Security** (2 weeks)
   - JWT / OAuth2
   - Password hashing
   - Input validation

7. **Scaling & Advanced** (4-6 weeks)
   - Caching
   - Microservices
   - Message queues

## 💡 Pro Tips

💡 **Master one language deeply** before learning others
💡 **Understand databases first** - they're critical
💡 **Build real projects** with scale challenges
💡 **Think about performance** from the start
💡 **Security matters** - implement from day one
💡 **Monitor everything** - visibility is key
💡 **Test thoroughly** - especially critical paths

## 🔗 Integration Points

- **Skills:** 15 backend skills in plugin
- **Commands:** `/learn`, `/projects`, `/compare`
- **Projects:** 20+ backend projects
- **Career Path:** Backend → Architect → Manager

## 📚 Resources

- Node.js docs: https://nodejs.org
- Python docs: https://python.org
- PostgreSQL docs: https://postgresql.org
- Docker docs: https://docker.com
- Kubernetes docs: https://kubernetes.io

## 🚀 Next Steps

1. **Start:** `/learn backend`
2. **Choose:** Select your preferred language
3. **Build:** Create simple API first
4. **Expand:** Add database and authentication
5. **Scale:** Learn caching and messaging
6. **Master:** Build microservices

---

**🔧 Start Building Powerful Backends Today!** 🚀"""
}

# Write enhanced agents
import os
for filename, content in agents_content.items():
    filepath = f"agents/{filename}"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"✅ Enhanced: {filepath}")

print(f"\n✨ Enhanced 2 agents to production quality!")
print("More agents coming next...")
