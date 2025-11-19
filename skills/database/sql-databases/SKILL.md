---
name: sql-databases
description: Master sql databases & query optimization. Production-ready code examples, best practices, and real-world applications.
---

# SQL Databases & Query Optimization

**Production-Quality Guide with Real Code Examples**

## Quick Start

```sql
-- Basic CRUD operations
SELECT * FROM users WHERE active = true;
SELECT id, name, email FROM users WHERE created_at > '2024-01-01';

-- Insert data
INSERT INTO users (name, email) VALUES ('John', 'john@example.com');

-- Update with WHERE clause
UPDATE users SET last_login = NOW() WHERE id = 1;

-- Delete with safety
DELETE FROM users WHERE id = 1 AND archived = true;

-- Joins
SELECT u.name, p.title FROM users u
  JOIN posts p ON u.id = p.user_id
  WHERE u.active = true;

-- Aggregation with GROUP BY
SELECT category, COUNT(*) as count
FROM posts
GROUP BY category
HAVING count > 5
ORDER BY count DESC;

-- Window functions (PostgreSQL)
SELECT name, salary,
  ROW_NUMBER() OVER (ORDER BY salary DESC) as rank
FROM employees;

-- Optimization with indexes
CREATE INDEX idx_users_email ON users(email);
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';
```


## Production Code Examples

```bash
# Command line examples for quick start
# Replace with language-specific code
echo "Production code examples will be customized per skill"
```
        


### Advanced Patterns
- Pattern 1: Industry best practices
- Pattern 2: Error handling strategies
- Pattern 3: Performance optimization
- Pattern 4: Testing approaches
- Pattern 5: Deployment strategies
        


### Real-World Projects
1. **Beginner Project** (Level: Beginner)
   - Core concepts application
   - Basic requirements
   - Expected duration: 1-2 weeks

2. **Intermediate Project** (Level: Intermediate)
   - Multiple integrations
   - Advanced concepts
   - Expected duration: 3-4 weeks

3. **Advanced Project** (Level: Advanced)
   - Production-grade application
   - Complex architecture
   - Expected duration: 6-8 weeks
        

## Key Topics

- ACID properties and transactions
- Data modeling and normalization
- Joins (INNER, LEFT, RIGHT, FULL)
- Aggregation and grouping
- Subqueries and CTEs
- Indexing strategies
- Query optimization and EXPLAIN
- Stored procedures and triggers

## Advanced Concepts

### Best Practices
- ✅ Production-ready code patterns
- ✅ Performance optimization
- ✅ Testing strategies
- ✅ Error handling
- ✅ Security considerations
- ✅ Scalability patterns
- ✅ Maintainability and documentation

### Common Pitfalls
- ❌ Avoid inefficient patterns
- ❌ Don't skip testing
- ❌ Don't ignore error handling
- ❌ Don't optimize prematurely
- ❌ Don't hardcode values
- ❌ Don't skip documentation

## Real-World Projects

- Design e-commerce database
- Create analytics queries
- Build data warehouse schema

## Resources

- Official documentation
- Recommended tutorials
- Best practices guides
- Community forums

## Career Integration

This skill connects to:
- Related technologies
- Career paths
- Interview preparation
- Portfolio building

---

**Master SQL Databases & Query Optimization today!** 🚀
