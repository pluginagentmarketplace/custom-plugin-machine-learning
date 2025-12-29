---
name: skills
description: /skills
allowed-tools: Read
---

# /skills

Browse and discover available skills organized by agent and category.

## Description

The `/skills` command lets you explore the comprehensive skill library organized by the 8 agent specializations. Each skill is a deep dive into a specific topic with examples and best practices.

## Usage

```
/skills
/skills list <agent>
/skills search <query>
/skills detail <skill-id>
```

## Available Skills (29 Total)

### 🎨 **Frontend Development (4 skills)**
- `html-css-design` - Semantic HTML5 and advanced CSS techniques
- `javascript-ecosystem` - Modern JavaScript and ES6+ features
- `react-modern-frontend` - React hooks and best practices
- `frontend-frameworks` - Vue, Angular, framework comparison

### 🔧 **Backend Development (4 skills)**
- `rest-api-design` - RESTful API principles and design
- `nodejs-runtime` - Node.js and popular frameworks
- `backend-frameworks` - Spring Boot, Django, Go, PHP
- `graphql-advanced-apis` - GraphQL design and optimization

### 🌐 **Full Stack Development (3 skills)**
- `typescript-advanced` - Advanced TypeScript patterns
- `nextjs-modern-web` - Next.js and modern web framework
- `fullstack-patterns` - Full-stack architecture patterns

### 📱 **Mobile Development (3 skills)**
- `react-native-mobile` - Cross-platform React Native
- `flutter-development` - Flutter and Dart programming
- `native-ios-swift` - Swift and SwiftUI development

### 🗄️ **Database & Data (3 skills)**
- `sql-databases` - SQL and relational databases
- `nosql-databases` - MongoDB, Redis, DynamoDB
- `database-design` - Data modeling and architecture

### ☁️ **Cloud & DevOps (5 skills)**
- `docker-containers` - Docker and containerization
- `kubernetes-orchestration` - Kubernetes management
- `aws-cloud` - AWS services and architecture
- `terraform-iac` - Infrastructure as code
- `linux-sysadmin` - Linux administration

### 🤖 **AI/ML & Data Science (4 skills)**
- `machine-learning-fundamentals` - ML algorithms and practices
- `deep-learning-neural-networks` - Neural networks and DL
- `data-science-analytics` - Data analysis and insights
- `mlops-deployment` - Model deployment and MLOps

### 👨‍💼 **Specialized Roles (3 skills)**
- `system-design` - Scalable system architecture
- `software-architecture` - Architecture patterns
- `testing-qa` - Testing strategies and QA

## Usage Examples

### List skills by agent
```
> /skills list backend

📚 Backend Development Skills:

1. rest-api-design
   Learn RESTful API design principles, HTTP methods,
   status codes, and best practices.
   Level: Intermediate
   Duration: 4-6 hours

2. nodejs-runtime
   Master Node.js runtime, event-driven architecture,
   and popular frameworks like Express.
   Level: Intermediate
   Duration: 6-8 hours

3. backend-frameworks
   Overview of Spring Boot, Django, Go, and other
   backend frameworks.
   Level: Intermediate
   Duration: 8-10 hours

4. graphql-advanced-apis
   Learn GraphQL for flexible, powerful API development.
   Level: Advanced
   Duration: 6-8 hours
```

### Search for skills
```
> /skills search "typescript"

🔍 Search results for "typescript":

1. typescript-advanced
   Advanced TypeScript patterns, generics, utility types
   Agent: Full Stack & Web
   Level: Advanced

2. react-modern-frontend
   Includes TypeScript usage in React components
   Agent: Frontend Development
   Level: Intermediate
```

### View skill details
```
> /skills detail typescript-advanced

📖 SKILL: typescript-advanced
Agent: Full Stack & Web Agent
Level: Advanced
Duration: 6-8 hours

OVERVIEW
────────
Master advanced TypeScript patterns, generics, and type
system features for building robust, type-safe applications.

QUICK START
───────────
[Code examples and quick introduction]

KEY TOPICS
──────────
✓ Generics - Writing reusable, type-safe code
✓ Utility Types - Readonly, Partial, Pick, Record
✓ Conditional Types - Type inference and branching
✓ Template Literal Types - Type manipulation
✓ Decorators - Metadata and aspect-oriented programming
✓ Module Resolution - Path mapping and imports
✓ Type Guards - Narrowing types effectively

BEST PRACTICES
──────────────
✅ Use generics for reusable components
✅ Leverage utility types
✅ Write strict TypeScript configuration
✅ Avoid `any` type
✅ Use discriminated unions

PROJECTS
────────
1. Type-safe API client library
2. Generic data structures (Stack, Queue, Tree)
3. Advanced React component patterns

RESOURCES
─────────
[Links to relevant documentation and tutorials]

NEXT STEPS
──────────
- Practice with the projects listed above
- Apply patterns to your own code
- Explore related skills
```

### List by category
```
> /skills list ai-ml

📚 AI/ML & Data Science Skills (4):

🤖 machine-learning-fundamentals
   ML algorithms, training process, evaluation metrics
   Duration: 8-10 hours

🧠 deep-learning-neural-networks
   Neural networks, CNNs, RNNs, Transformers
   Duration: 10-12 hours

📊 data-science-analytics
   Data analysis, visualization, insights extraction
   Duration: 8-10 hours

🚀 mlops-deployment
   Model serving, pipelines, monitoring
   Duration: 6-8 hours

Total Learning Time: 32-40 hours
Recommended Learning Path: (Detailed path shown)
```

## Quick Reference

### By Level
- **Beginner**: html-css-design, javascript-ecosystem, rest-api-design
- **Intermediate**: react-modern-frontend, nodejs-runtime, database-design
- **Advanced**: typescript-advanced, graphql-advanced-apis, system-design
- **Expert**: mlops-deployment, kubernetes-orchestration, software-architecture

### By Technology
- **JavaScript/TypeScript**: javascript-ecosystem, typescript-advanced, nextjs-modern-web
- **Databases**: sql-databases, nosql-databases, database-design
- **Cloud/DevOps**: docker-containers, kubernetes-orchestration, aws-cloud
- **AI/ML**: machine-learning-fundamentals, deep-learning-neural-networks, mlops-deployment

## Tips

✨ **For Beginners**: Start with frontend/backend fundamentals
✨ **For Career Change**: Pick specialization, follow /learn path
✨ **For Specialization**: Deep dive into 3-4 related skills
✨ **For Mastery**: Complete all skills in an agent area

## See Also

- `/learn` - Guided learning paths
- `/explore` - Explore specializations
- `/roadmap` - Industry roadmaps

## Contribution

Want to add new skills? The plugin is open source and welcomes contributions!
