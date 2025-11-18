---
name: nosql-databases
description: Master NoSQL databases: MongoDB, Redis, DynamoDB, and more.
---

# NoSQL Databases

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

