---
name: database-design
description: Master database design, normalization, and data modeling.
---

# Database Design & Modeling

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

