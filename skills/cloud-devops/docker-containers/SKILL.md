---
name: docker-containers
description: Master Docker for containerization and application deployment.
---

# Docker & Container Technology

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

