---
name: system-design
description: Master system design for scalable, reliable applications.
---

# System Design & Architecture

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

