---
name: sql-databases
description: Master SQL, relational databases, and query optimization.
---

# SQL Databases & Queries

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

