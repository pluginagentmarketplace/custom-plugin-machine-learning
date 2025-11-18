---
name: kubernetes-orchestration
description: Master Kubernetes for managing containerized applications at scale.
---

# Kubernetes & Container Orchestration

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

