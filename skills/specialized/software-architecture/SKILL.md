---
name: software-architecture
description: Master software architecture principles and design patterns.
---

# Software Architecture & Design Patterns

## Architectural Patterns

### MVC (Model-View-Controller)
```
User → Controller → Model → View → User
```

### MVVM (Model-View-ViewModel)
```
View ↔ ViewModel ↔ Model
```

### Layered Architecture
```
UI Layer → Business Logic → Data Access → Database
```

### Microservices
```
API Gateway → [Service1, Service2, Service3]
```

## Design Patterns

### Creational
- **Singleton**: Single instance
- **Factory**: Object creation
- **Builder**: Complex object construction

### Structural
- **Adapter**: Interface compatibility
- **Decorator**: Add functionality
- **Facade**: Simplified interface

### Behavioral
- **Observer**: Event handling
- **Strategy**: Algorithm selection
- **State**: Object state management

## SOLID Principles

- **S**ingle Responsibility
- **O**pen/Closed Principle
- **L**iskov Substitution
- **I**nterface Segregation
- **D**ependency Inversion

## Clean Code

```python
# Good
def calculate_total_price(items):
    return sum(item.price * item.quantity for item in items)

# Bad
def calc(i):
    t = 0
    for x in i:
        t += x.p * x.q
    return t
```

## Best Practices

✅ Keep it simple
✅ DRY principle
✅ SOLID principles
✅ Proper naming
✅ Document decisions
✅ Code reviews
✅ Refactor regularly

