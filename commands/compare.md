---
name: compare
description: /compare
allowed-tools: Read
---

# /compare

Compare different technologies, frameworks, languages, and approaches side-by-side.

## Description

The `/compare` command helps you evaluate and choose between competing technologies by comparing features, performance, learning curve, and use cases.

## Usage

```
/compare <tech1> vs <tech2>
/compare frameworks <category>
/compare languages <use-case>
/compare databases
```

## Popular Comparisons

### Frontend Frameworks
- React vs Vue vs Angular vs Svelte
- Next.js vs Remix vs SvelteKit
- JavaScript vs TypeScript

### Backend Frameworks
- Express vs Fastify vs NestJS
- Django vs FastAPI vs Flask
- Spring Boot vs Quarkus
- Node.js vs Go vs Rust

### Databases
- PostgreSQL vs MySQL
- MongoDB vs Firebase
- Redis vs Memcached
- SQL vs NoSQL

### Cloud Platforms
- AWS vs Google Cloud vs Azure
- Vercel vs Netlify vs Heroku

## Usage Examples

### Framework comparison
```
> /compare React vs Vue vs Angular

📊 FRONTEND FRAMEWORK COMPARISON

┌─────────────┬──────────┬──────────┬──────────┐
│ Criteria    │ React    │ Vue      │ Angular  │
├─────────────┼──────────┼──────────┼──────────┤
│ Learning    │ Moderate │ Gentle   │ Steep    │
│ Performance │ Excellent│ Good     │ Good     │
│ Community   │ Largest  │ Growing  │ Large    │
│ Job Market  │ 5/5 ⭐   │ 3/5 ⭐   │ 4/5 ⭐   │
│ Bundle Size │ 40KB     │ 33KB     │ 130KB    │
└─────────────┴──────────┴──────────┴──────────┘

REACT
✅ Pros:
  • Largest ecosystem
  • Most job opportunities
  • Flexible and unopinionated
  • Great tooling (Next.js)

❌ Cons:
  • Steeper learning curve
  • More boilerplate
  • Requires additional libraries

📚 Best For:
  • Large enterprise apps
  • Progressive enhancement
  • Startups with React-experienced teams

💰 Average Salary: $120k-180k

VUE
✅ Pros:
  • Gentle learning curve
  • Great documentation
  • Progressive enhancement
  • Balanced features

❌ Cons:
  • Smaller job market
  • Smaller ecosystem
  • Less mature tooling

📚 Best For:
  • Learning web development
  • Project prototypes
  • Smaller teams

💰 Average Salary: $100k-150k

ANGULAR
✅ Pros:
  • Full-featured framework
  • Great for large teams
  • Excellent tooling
  • Strong typing (TypeScript)

❌ Cons:
  • Steep learning curve
  • More boilerplate
  • Heavier bundle size
  • Slower development

📚 Best For:
  • Enterprise applications
  • Large teams
  • Complex applications

💰 Average Salary: $110k-160k

RECOMMENDATION
───────────────
→ React: If you want maximum job opportunities
→ Vue: If you're learning or want simplicity
→ Angular: If building large enterprise apps
```

### Language comparison
```
> /compare languages backend

🔧 BACKEND PROGRAMMING LANGUAGES

┌───────────┬──────────┬──────────┬──────────┐
│ Language  │ Speed    │ Learning │ Ecosystem│
├───────────┼──────────┼──────────┼──────────┤
│ Python    │ Medium   │ Gentle   │ Excellent│
│ Node.js   │ Medium   │ Moderate │ Excellent│
│ Go        │ Fast     │ Moderate │ Growing  │
│ Java      │ Fast     │ Moderate │ Excellent│
│ Rust      │ Fastest  │ Steep    │ Growing  │
└───────────┴──────────┴──────────┴──────────┘

By Use Case:

APIs & Web Services:
→ Python (FastAPI, Django)
→ Node.js (Express, NestJS)
→ Go (Gin, Echo)

Microservices:
→ Go
→ Java (Spring Boot)
→ Rust

Data Processing:
→ Python
→ Java

System Programming:
→ Rust
→ C++
→ Go

Machine Learning:
→ Python (TensorFlow, PyTorch)

Real-time Systems:
→ Go
→ Rust
→ Node.js
```

### Database comparison
```
> /compare databases

💾 DATABASE COMPARISON

RELATIONAL (SQL)
──────────────
PostgreSQL (Best overall)
✅ Advanced features, JSON support, full-text search
✅ Excellent for complex queries
💰 Free, open-source

MySQL (Popular)
✅ Simple, reliable, good performance
✅ Widely supported
💰 Free, open-source

SQL Server (Enterprise)
✅ Enterprise features, great for Windows
💰 Expensive licensing

NOSQL
─────
MongoDB (Document)
✅ Flexible schema, good for startups
✅ Horizontal scaling
💰 Free with MongoDB Atlas

Redis (Cache/Store)
✅ Ultra-fast, perfect for caching
✅ Real-time features
💰 Free, easy to self-host

DynamoDB (Serverless)
✅ Fully managed, pay per request
✅ Scales automatically
💰 AWS pricing model

NewSQL (Best of Both)
──────────
CockroachDB
✅ SQL + horizontal scaling
✅ ACID compliance + distributed
💰 Commercial + open-source options

When to Use What:
─────────────────
PostgreSQL → Default choice for most projects
MongoDB → Rapid prototyping, flexible schema
Redis → Caching, sessions, real-time
DynamoDB → Serverless apps, unpredictable load

👉 80% of projects should start with PostgreSQL
```

### Performance comparison
```
> /compare performance

⚡ PERFORMANCE METRICS

Language/Framework Speed:
1. Rust - 1x (baseline)
2. Go - 1.5x slower than Rust
3. C++ - 1.2x slower than Rust
4. Java - 2x slower than Rust
5. Node.js - 3-5x slower than Rust
6. Python - 50-100x slower than Rust

Startup Speed:
1. Go - Instant binary execution
2. Rust - Instant compiled binary
3. Node.js - ~500ms startup
4. Python - ~100ms startup (cached)
5. Java - ~1-2s startup (JVM warmup)

Memory Usage:
1. Rust - Minimal (~10MB)
2. C++ - Minimal (~10-20MB)
3. Go - Low (~20-30MB)
4. Java - Medium (~100MB+ JVM)
5. Node.js - Medium (~50-100MB)
6. Python - Medium (~50-100MB)

For Most Web Applications:
───────────────────────────
✅ Any modern language is "fast enough"
✅ Choose based on ecosystem & job market
✅ Optimize specific bottlenecks later
✅ Premature optimization is the root of all evil
```

## Comparison Criteria

- **Performance**: Speed and efficiency
- **Learning Curve**: Time to learn
- **Community**: Support and ecosystem
- **Job Market**: Employment demand
- **Scalability**: Growth potential
- **Ecosystem**: Libraries and tools
- **Documentation**: Learning resources
- **Maturity**: Stability and reliability

## Use Cases

- Choosing first technology to learn
- Technology migration decisions
- Framework selection
- Database choice
- Tool evaluation
- Language comparison

## Tips

💡 No single best technology - context matters
💡 Compare based on YOUR use case
💡 Community size ≠ Best technology
💡 Job market = Learning investment
💡 Learn fundamentals > Chase trends

## See Also

- `/learn` - Structured learning
- `/trending` - Hot technologies
- `/skills` - Detailed skill guides
- `/roadmap` - Industry roadmaps
