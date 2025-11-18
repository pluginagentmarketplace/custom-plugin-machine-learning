#!/usr/bin/env python3
"""Expand plugin with additional skills from developer-roadmap roles."""

import os

# New skills to add based on roadmap.sh
new_skills = {
    "programming-languages": {
        "python-comprehensive": {
            "name": "python-comprehensive",
            "title": "Python Programming",
            "description": "Master Python from fundamentals to advanced OOP, async programming, and web frameworks.",
            "category": "Backend"
        },
        "java-ecosystem": {
            "name": "java-ecosystem",
            "title": "Java Programming & Ecosystem",
            "description": "Learn Java fundamentals, object-oriented programming, and the extensive Java ecosystem.",
            "category": "Backend"
        },
        "go-programming": {
            "name": "go-programming",
            "title": "Go Programming Language",
            "description": "Master Go for concurrent systems, microservices, and cloud-native applications.",
            "category": "Backend"
        },
        "rust-programming": {
            "name": "rust-programming",
            "title": "Rust Programming",
            "description": "Learn Rust for systems programming, memory safety, and high-performance applications.",
            "category": "Backend"
        },
        "cpp-programming": {
            "name": "cpp-programming",
            "title": "C++ Programming",
            "description": "Master C++ for systems programming, game development, and performance-critical applications.",
            "category": "Specialized"
        }
    },
    "web-frameworks": {
        "express-nodejs": {
            "name": "express-nodejs",
            "title": "Express.js Deep Dive",
            "description": "Advanced Express.js patterns, middleware, routing, and production deployment.",
            "category": "Backend"
        },
        "django-framework": {
            "name": "django-framework",
            "title": "Django Web Framework",
            "description": "Django ORM, admin panel, authentication, and building production Django applications.",
            "category": "Backend"
        },
        "fastapi-modern": {
            "name": "fastapi-modern",
            "title": "FastAPI Modern Web Framework",
            "description": "Building high-performance APIs with FastAPI, async/await, and automatic documentation.",
            "category": "Backend"
        },
        "spring-boot-java": {
            "name": "spring-boot-java",
            "title": "Spring Boot Framework",
            "description": "Spring Boot for enterprise Java applications, microservices, and cloud deployment.",
            "category": "Backend"
        },
        "laravel-php": {
            "name": "laravel-php",
            "title": "Laravel PHP Framework",
            "description": "Laravel for full-stack web development, eloquent ORM, and modern PHP.",
            "category": "Backend"
        }
    },
    "databases-advanced": {
        "postgresql-advanced": {
            "name": "postgresql-advanced",
            "title": "PostgreSQL Advanced Topics",
            "description": "Advanced PostgreSQL: JSON, full-text search, window functions, and optimization.",
            "category": "Database"
        },
        "mongodb-advanced": {
            "name": "mongodb-advanced",
            "title": "MongoDB Advanced Patterns",
            "description": "Advanced MongoDB: aggregation pipeline, sharding, replication, transactions.",
            "category": "Database"
        },
        "redis-advanced": {
            "name": "redis-advanced",
            "title": "Redis Caching & Pub/Sub",
            "description": "Redis for caching, sessions, real-time features, and message queues.",
            "category": "Database"
        }
    },
    "api-architectures": {
        "rest-best-practices": {
            "name": "rest-best-practices",
            "title": "REST API Best Practices",
            "description": "RESTful principles, versioning, security, rate limiting, and documentation.",
            "category": "Backend"
        },
        "grpc-protobuf": {
            "name": "grpc-protobuf",
            "title": "gRPC & Protocol Buffers",
            "description": "gRPC for efficient microservices communication with Protocol Buffers.",
            "category": "Backend"
        },
        "websocket-realtime": {
            "name": "websocket-realtime",
            "title": "WebSockets & Real-Time Communication",
            "description": "WebSocket protocols, Socket.io, and real-time bidirectional communication.",
            "category": "Full Stack"
        }
    },
    "frontend-advanced": {
        "web-performance": {
            "name": "web-performance",
            "title": "Web Performance Optimization",
            "description": "Core Web Vitals, lazy loading, code splitting, image optimization, and metrics.",
            "category": "Frontend"
        },
        "web-accessibility": {
            "name": "web-accessibility",
            "title": "Web Accessibility (a11y)",
            "description": "WCAG standards, ARIA, semantic HTML, and building inclusive web experiences.",
            "category": "Frontend"
        },
        "progressive-web-apps": {
            "name": "progressive-web-apps",
            "title": "Progressive Web Apps (PWA)",
            "description": "Service workers, offline-first, app manifest, and native-like web experiences.",
            "category": "Frontend"
        },
        "svelte-framework": {
            "name": "svelte-framework",
            "title": "Svelte Framework",
            "description": "Svelte reactive programming, stores, transitions, and building efficient SPAs.",
            "category": "Frontend"
        }
    },
    "devops-advanced": {
        "ci-cd-pipelines": {
            "name": "ci-cd-pipelines",
            "title": "CI/CD Pipelines & Automation",
            "description": "GitHub Actions, GitLab CI, Jenkins, and automated deployment workflows.",
            "category": "DevOps"
        },
        "monitoring-observability": {
            "name": "monitoring-observability",
            "title": "Monitoring & Observability",
            "description": "Prometheus, Grafana, ELK stack, distributed tracing, and alerting.",
            "category": "DevOps"
        },
        "security-devops": {
            "name": "security-devops",
            "title": "DevOps Security & Compliance",
            "description": "Container security, secret management, compliance, and secure infrastructure.",
            "category": "DevOps"
        },
        "gcp-cloud": {
            "name": "gcp-cloud",
            "title": "Google Cloud Platform",
            "description": "GCP services, Cloud Run, App Engine, and multi-cloud deployment strategies.",
            "category": "DevOps"
        },
        "azure-cloud": {
            "name": "azure-cloud",
            "title": "Azure Cloud Services",
            "description": "Azure services, App Service, Functions, and enterprise cloud deployment.",
            "category": "DevOps"
        }
    },
    "ai-ml-extended": {
        "nlp-transformers": {
            "name": "nlp-transformers",
            "title": "NLP & Transformer Models",
            "description": "Natural language processing, BERT, GPT, fine-tuning, and text generation.",
            "category": "AI/ML"
        },
        "computer-vision": {
            "name": "computer-vision",
            "title": "Computer Vision & Image Processing",
            "description": "CNN architectures, object detection, image segmentation, and video processing.",
            "category": "AI/ML"
        },
        "reinforcement-learning": {
            "name": "reinforcement-learning",
            "title": "Reinforcement Learning",
            "description": "Q-learning, policy gradient, actor-critic, and multi-agent reinforcement learning.",
            "category": "AI/ML"
        },
        "time-series-forecasting": {
            "name": "time-series-forecasting",
            "title": "Time Series & Forecasting",
            "description": "ARIMA, LSTM, Prophet, and forecasting techniques for temporal data.",
            "category": "AI/ML"
        }
    },
    "specialized-topics": {
        "system-architecture": {
            "name": "system-architecture",
            "title": "Large-Scale System Architecture",
            "description": "CAP theorem, eventual consistency, distributed consensus, and scaling patterns.",
            "category": "Specialized"
        },
        "game-development": {
            "name": "game-development",
            "title": "Game Development Fundamentals",
            "description": "Game engines, physics, graphics, networking, and game design patterns.",
            "category": "Specialized"
        },
        "blockchain-web3": {
            "name": "blockchain-web3",
            "title": "Blockchain & Web3 Development",
            "description": "Smart contracts, Ethereum, consensus mechanisms, and decentralized applications.",
            "category": "Specialized"
        },
        "cybersecurity-fundamentals": {
            "name": "cybersecurity-fundamentals",
            "title": "Cybersecurity Fundamentals",
            "description": "Network security, cryptography, vulnerability assessment, and ethical hacking.",
            "category": "Specialized"
        },
        "devrel-developer-advocacy": {
            "name": "devrel-developer-advocacy",
            "title": "Developer Relations & Advocacy",
            "description": "Community building, technical content creation, and developer experience.",
            "category": "Specialized"
        },
        "technical-writing": {
            "name": "technical-writing",
            "title": "Technical Writing & Documentation",
            "description": "API documentation, tutorials, guide writing, and developer content strategy.",
            "category": "Specialized"
        }
    }
}

def create_skill(category, skill_id, skill_info):
    """Create a SKILL.md file for the given skill."""
    skill_dir = f"skills/{category.lower()}/{skill_id}"
    os.makedirs(skill_dir, exist_ok=True)

    # Basic skill template
    skill_content = f"""---
name: {skill_info['name']}
description: {skill_info['description']}
---

# {skill_info['title']}

Expert-level guide for {skill_info['title']}.

## Quick Start

[Quick start examples and code snippets]

## Key Topics

- Core concepts and fundamentals
- Advanced patterns and techniques
- Real-world applications
- Best practices and optimization
- Common pitfalls and solutions

## Learning Path

1. **Foundations** → Core concepts
2. **Intermediate** → Practical application
3. **Advanced** → Optimization and patterns
4. **Expert** → Production systems

## Projects

- Real-world project ideas
- Hands-on examples
- Portfolio pieces

## Resources

- Official documentation
- Recommended courses
- Community forums
- Code examples

## Best Practices

✅ Best practice 1
✅ Best practice 2
✅ Best practice 3

## Next Steps

Continue learning with related skills and build practical projects.
"""

    with open(f"{skill_dir}/SKILL.md", 'w') as f:
        f.write(skill_content)

    return skill_dir

# Create all new skills
count = 0
for category, skills in new_skills.items():
    for skill_id, skill_info in skills.items():
        # Map category to skill type
        category_map = {
            "programming-languages": "backend",
            "web-frameworks": "backend",
            "databases-advanced": "database",
            "api-architectures": "backend",
            "frontend-advanced": "frontend",
            "devops-advanced": "cloud-devops",
            "ai-ml-extended": "ai-ml",
            "specialized-topics": "specialized"
        }

        skill_type = category_map.get(category, "specialized")
        created_dir = create_skill(skill_type, skill_id, skill_info)
        print(f"✅ Created {created_dir}/SKILL.md")
        count += 1

print(f"\n✨ Created {count} additional skills!")
print(f"📊 New skill total: 29 + {count} = {29 + count} skills")
