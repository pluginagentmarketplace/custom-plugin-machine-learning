#!/usr/bin/env python3
"""Update plugin.json with new skills and commands."""

import json
import os

# Read current plugin.json
with open('.claude-plugin/plugin.json', 'r') as f:
    plugin = json.load(f)

# Update version and description
plugin['version'] = '1.1.0'
plugin['description'] = 'Ultra-comprehensive developer learning platform with 64 skills, 8 specialized agents, and integration with 65+ developer roadmaps. Master frontend, backend, mobile, database, cloud/DevOps, AI/ML, and specialized roles.'

# Expand keywords
plugin['keywords'] = [
    "learning",
    "development",
    "roadmap",
    "developer-training",
    "ai",
    "machine-learning",
    "web-development",
    "cloud-computing",
    "devops",
    "mobile-development",
    "frontend",
    "backend",
    "fullstack",
    "typescript",
    "javascript",
    "python",
    "java",
    "golang",
    "rust",
    "kubernetes",
    "docker",
    "aws",
    "system-design",
    "architecture",
    "microservices",
    "agent-skills",
    "skill-development",
    "career-growth"
]

# Add new commands
plugin['commands'].extend([
    {
        "name": "trending",
        "file": "commands/trending.md",
        "description": "Discover trending technologies and skills to learn next"
    },
    {
        "name": "projects",
        "file": "commands/projects.md",
        "description": "Browse real-world projects organized by difficulty and topic"
    },
    {
        "name": "compare",
        "file": "commands/compare.md",
        "description": "Compare different technologies, frameworks, and approaches"
    },
    {
        "name": "career-path",
        "file": "commands/career-path.md",
        "description": "Get personalized career path recommendations"
    }
])

# Build new skills list with all 64 skills
new_skills_data = [
    # Original 29 skills
    ("frontend-dev-agent", "html-css-design", "skills/frontend/html-css-design/SKILL.md"),
    ("frontend-dev-agent", "javascript-ecosystem", "skills/frontend/javascript-ecosystem/SKILL.md"),
    ("frontend-dev-agent", "react-modern-frontend", "skills/frontend/react-modern-frontend/SKILL.md"),
    ("frontend-dev-agent", "frontend-frameworks", "skills/frontend/frontend-frameworks/SKILL.md"),
    ("backend-dev-agent", "rest-api-design", "skills/backend/rest-api-design/SKILL.md"),
    ("backend-dev-agent", "nodejs-runtime", "skills/backend/nodejs-runtime/SKILL.md"),
    ("backend-dev-agent", "backend-frameworks", "skills/backend/backend-frameworks/SKILL.md"),
    ("backend-dev-agent", "graphql-advanced-apis", "skills/backend/graphql-advanced-apis/SKILL.md"),
    ("fullstack-web-agent", "typescript-advanced", "skills/fullstack/typescript-advanced/SKILL.md"),
    ("fullstack-web-agent", "nextjs-modern-web", "skills/fullstack/nextjs-modern-web/SKILL.md"),
    ("fullstack-web-agent", "fullstack-patterns", "skills/fullstack/fullstack-patterns/SKILL.md"),
    ("mobile-crossplatform-agent", "react-native-mobile", "skills/mobile/react-native-mobile/SKILL.md"),
    ("mobile-crossplatform-agent", "flutter-development", "skills/mobile/flutter-development/SKILL.md"),
    ("mobile-crossplatform-agent", "native-ios-swift", "skills/mobile/native-ios-swift/SKILL.md"),
    ("database-data-agent", "sql-databases", "skills/database/sql-databases/SKILL.md"),
    ("database-data-agent", "nosql-databases", "skills/database/nosql-databases/SKILL.md"),
    ("database-data-agent", "database-design", "skills/database/database-design/SKILL.md"),
    ("cloud-devops-agent", "docker-containers", "skills/cloud-devops/docker-containers/SKILL.md"),
    ("cloud-devops-agent", "kubernetes-orchestration", "skills/cloud-devops/kubernetes-orchestration/SKILL.md"),
    ("cloud-devops-agent", "aws-cloud", "skills/cloud-devops/aws-cloud/SKILL.md"),
    ("cloud-devops-agent", "terraform-iac", "skills/cloud-devops/terraform-iac/SKILL.md"),
    ("cloud-devops-agent", "linux-sysadmin", "skills/cloud-devops/linux-sysadmin/SKILL.md"),
    ("ai-ml-data-agent", "machine-learning-fundamentals", "skills/ai-ml/machine-learning-fundamentals/SKILL.md"),
    ("ai-ml-data-agent", "deep-learning-neural-networks", "skills/ai-ml/deep-learning-neural-networks/SKILL.md"),
    ("ai-ml-data-agent", "data-science-analytics", "skills/ai-ml/data-science-analytics/SKILL.md"),
    ("ai-ml-data-agent", "mlops-deployment", "skills/ai-ml/mlops-deployment/SKILL.md"),
    ("specialized-architect-agent", "system-design", "skills/specialized/system-design/SKILL.md"),
    ("specialized-architect-agent", "software-architecture", "skills/specialized/software-architecture/SKILL.md"),
    ("specialized-architect-agent", "testing-qa", "skills/specialized/testing-qa/SKILL.md"),

    # New 35 skills
    ("backend-dev-agent", "python-comprehensive", "skills/backend/python-comprehensive/SKILL.md"),
    ("backend-dev-agent", "java-ecosystem", "skills/backend/java-ecosystem/SKILL.md"),
    ("backend-dev-agent", "go-programming", "skills/backend/go-programming/SKILL.md"),
    ("backend-dev-agent", "rust-programming", "skills/backend/rust-programming/SKILL.md"),
    ("specialized-architect-agent", "cpp-programming", "skills/backend/cpp-programming/SKILL.md"),
    ("backend-dev-agent", "express-nodejs", "skills/backend/express-nodejs/SKILL.md"),
    ("backend-dev-agent", "django-framework", "skills/backend/django-framework/SKILL.md"),
    ("backend-dev-agent", "fastapi-modern", "skills/backend/fastapi-modern/SKILL.md"),
    ("backend-dev-agent", "spring-boot-java", "skills/backend/spring-boot-java/SKILL.md"),
    ("backend-dev-agent", "laravel-php", "skills/backend/laravel-php/SKILL.md"),
    ("database-data-agent", "postgresql-advanced", "skills/database/postgresql-advanced/SKILL.md"),
    ("database-data-agent", "mongodb-advanced", "skills/database/mongodb-advanced/SKILL.md"),
    ("database-data-agent", "redis-advanced", "skills/database/redis-advanced/SKILL.md"),
    ("backend-dev-agent", "rest-best-practices", "skills/backend/rest-best-practices/SKILL.md"),
    ("backend-dev-agent", "grpc-protobuf", "skills/backend/grpc-protobuf/SKILL.md"),
    ("fullstack-web-agent", "websocket-realtime", "skills/fullstack/websocket-realtime/SKILL.md"),
    ("frontend-dev-agent", "web-performance", "skills/frontend/web-performance/SKILL.md"),
    ("frontend-dev-agent", "web-accessibility", "skills/frontend/web-accessibility/SKILL.md"),
    ("frontend-dev-agent", "progressive-web-apps", "skills/frontend/progressive-web-apps/SKILL.md"),
    ("frontend-dev-agent", "svelte-framework", "skills/frontend/svelte-framework/SKILL.md"),
    ("cloud-devops-agent", "ci-cd-pipelines", "skills/cloud-devops/ci-cd-pipelines/SKILL.md"),
    ("cloud-devops-agent", "monitoring-observability", "skills/cloud-devops/monitoring-observability/SKILL.md"),
    ("cloud-devops-agent", "security-devops", "skills/cloud-devops/security-devops/SKILL.md"),
    ("cloud-devops-agent", "gcp-cloud", "skills/cloud-devops/gcp-cloud/SKILL.md"),
    ("cloud-devops-agent", "azure-cloud", "skills/cloud-devops/azure-cloud/SKILL.md"),
    ("ai-ml-data-agent", "nlp-transformers", "skills/ai-ml/nlp-transformers/SKILL.md"),
    ("ai-ml-data-agent", "computer-vision", "skills/ai-ml/computer-vision/SKILL.md"),
    ("ai-ml-data-agent", "reinforcement-learning", "skills/ai-ml/reinforcement-learning/SKILL.md"),
    ("ai-ml-data-agent", "time-series-forecasting", "skills/ai-ml/time-series-forecasting/SKILL.md"),
    ("specialized-architect-agent", "system-architecture", "skills/specialized/system-architecture/SKILL.md"),
    ("specialized-architect-agent", "game-development", "skills/specialized/game-development/SKILL.md"),
    ("specialized-architect-agent", "blockchain-web3", "skills/specialized/blockchain-web3/SKILL.md"),
    ("specialized-architect-agent", "cybersecurity-fundamentals", "skills/specialized/cybersecurity-fundamentals/SKILL.md"),
    ("specialized-architect-agent", "devrel-developer-advocacy", "skills/specialized/devrel-developer-advocacy/SKILL.md"),
    ("specialized-architect-agent", "technical-writing", "skills/specialized/technical-writing/SKILL.md"),
]

# Clear existing skills and add all
plugin['skills'] = []
for agent, skill_id, skill_file in new_skills_data:
    plugin['skills'].append({
        "id": skill_id,
        "agent": agent,
        "file": skill_file
    })

# Write updated plugin.json
with open('.claude-plugin/plugin.json', 'w') as f:
    json.dump(plugin, f, indent=2)

print(f"✅ Updated plugin.json")
print(f"✅ Version: {plugin['version']}")
print(f"✅ Total skills: {len(plugin['skills'])}")
print(f"✅ Total commands: {len(plugin['commands'])}")
print(f"✅ Keywords expanded: {len(plugin['keywords'])}")
