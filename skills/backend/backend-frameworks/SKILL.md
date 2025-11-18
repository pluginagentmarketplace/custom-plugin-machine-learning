---
name: backend-frameworks
description: Overview of popular backend frameworks across different languages.
---

# Backend Frameworks

## Java - Spring Boot

```java
@SpringBootApplication
public class Application {
  public static void main(String[] args) {
    SpringApplication.run(Application.class, args);
  }
}

@RestController
@RequestMapping("/api/users")
public class UserController {
  @GetMapping
  public List<User> getUsers() {
    return new ArrayList<>();
  }
}
```

## Python - Django

```python
from django.urls import path
from django.http import JsonResponse

def get_users(request):
    return JsonResponse({'users': []})

urlpatterns = [
    path('api/users/', get_users),
]
```

## Go - Gin

```go
package main

func main() {
  router := gin.Default()
  router.GET("/api/users", getUsers)
  router.Run(":3000")
}

func getUsers(c *gin.Context) {
  c.JSON(200, gin.H{"users": []})
}
```

## Framework Comparison

- **Spring Boot**: Enterprise-grade, rich ecosystem, steep learning curve
- **Django**: Full-featured, batteries included, great documentation
- **Go (Gin)**: High performance, simple, great for microservices
- **Rust (Actix)**: Type-safe, fast, modern language

## Key Topics

- Framework patterns and architectures
- Dependency injection
- Request validation
- Error handling
- Testing frameworks
- Deployment strategies

