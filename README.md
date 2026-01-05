<div align="center">

<!-- Animated Typing Banner -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=2E9EF7&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=100&lines=Machine+Learning+Assistant;7+Agents+%7C+7+Skills;Production-Grade+Claude+Plugin" alt="Machine Learning Assistant" />

<br/>

<!-- Badge Row 1: Status Badges -->
[![Version](https://img.shields.io/badge/Version-1.4.0-blue?style=for-the-badge)](https://github.com/pluginagentmarketplace/custom-plugin-machine-learning/releases)
[![License](https://img.shields.io/badge/License-Custom-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)](#)
[![SASMP](https://img.shields.io/badge/SASMP-v1.4.0-blueviolet?style=for-the-badge)](#)

<!-- Badge Row 2: Content Badges -->
[![Agents](https://img.shields.io/badge/Agents-7-orange?style=flat-square&logo=robot)](#-agents)
[![Skills](https://img.shields.io/badge/Skills-7-purple?style=flat-square&logo=lightning)](#-skills)
[![Commands](https://img.shields.io/badge/Commands-8-green?style=flat-square&logo=terminal)](#-commands)

<br/>

<!-- Quick CTA Row -->
[**Install Now**](#-quick-start) | [**Explore Agents**](#-agents) | [**Browse Skills**](#-skills) | [**Documentation**](#-documentation)

---

### What is this?

> **Machine Learning Assistant** is a production-grade Claude Code plugin with **7 specialized agents** and **7 bonded skills** for complete ML development lifecycle.

</div>

---

## Table of Contents

- [Quick Start](#-quick-start)
- [Architecture](#-architecture)
- [Agents](#-agents)
- [Skills](#-skills)
- [Commands](#-commands)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)

---

## Quick Start

### Prerequisites

- Claude Code CLI v2.0.27+
- Active Claude subscription

### Installation

```bash
# From Marketplace
/plugin marketplace add pluginagentmarketplace/custom-plugin-machine-learning
/plugin install machine-learning-assistant@pluginagentmarketplace-machine-learning

# Or Local Installation
git clone https://github.com/pluginagentmarketplace/custom-plugin-machine-learning.git
cd custom-plugin-machine-learning
/plugin load .
```

### Verify Installation

```
machine-learning-assistant:01-ml-fundamentals
machine-learning-assistant:02-supervised-learning
machine-learning-assistant:03-unsupervised-learning
machine-learning-assistant:04-deep-learning
machine-learning-assistant:05-nlp
machine-learning-assistant:06-computer-vision
machine-learning-assistant:07-model-deployment
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    ML ASSISTANT ARCHITECTURE                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐        │
│  │ 01-ML        │   │ 02-Supervised│   │ 03-Unsupervised│       │
│  │ Fundamentals │──▶│ Learning     │──▶│ Learning     │        │
│  └──────┬───────┘   └──────────────┘   └──────────────┘        │
│         │                                                        │
│         ▼                                                        │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐        │
│  │ 04-Deep      │──▶│ 05-NLP       │   │ 06-Computer  │        │
│  │ Learning     │   │              │   │ Vision       │        │
│  └──────┬───────┘   └──────────────┘   └──────────────┘        │
│         │                                                        │
│         ▼                                                        │
│  ┌──────────────┐                                               │
│  │ 07-Model     │  ◀── All agents feed into deployment         │
│  │ Deployment   │                                               │
│  └──────────────┘                                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Agents

### 7 Specialized ML Agents

| # | Agent | Description | Primary Skill |
|---|-------|-------------|---------------|
| 1 | **01-ml-fundamentals** | ML foundations: algorithms, preprocessing, feature engineering, evaluation | `ml-fundamentals` |
| 2 | **02-supervised-learning** | Classification, regression, ensemble methods, hyperparameter tuning | `supervised-learning` |
| 3 | **03-unsupervised-learning** | Clustering, dimensionality reduction, anomaly detection | `clustering` |
| 4 | **04-deep-learning** | Neural networks, PyTorch/TensorFlow, training strategies | `deep-learning` |
| 5 | **05-nlp** | Text processing, transformers, LLMs, embeddings | `nlp-basics` |
| 6 | **06-computer-vision** | Image classification, object detection, segmentation | `computer-vision` |
| 7 | **07-model-deployment** | APIs, Docker, monitoring, MLOps, A/B testing | `ml-deployment` |

### Agent Features

Each agent includes:
- **Role & Responsibility Boundaries** - Clear scope definition
- **Input/Output Schemas** - Type-safe interfaces
- **Error Handling** - Exponential backoff retry logic
- **Token Optimization** - Context management
- **Troubleshooting Guide** - Common issues & solutions
- **Integration Points** - Cross-references to related agents/skills

---

## Skills

### 7 Production-Ready Skills

| Skill | Description | Bonded Agent |
|-------|-------------|--------------|
| `ml-fundamentals` | Preprocessing, pipelines, cross-validation | 01-ml-fundamentals |
| `supervised-learning` | Classifiers, regressors, tuning | 02-supervised-learning |
| `clustering` | K-Means, DBSCAN, PCA, anomaly detection | 03-unsupervised-learning |
| `deep-learning` | PyTorch training, architectures, optimization | 04-deep-learning |
| `nlp-basics` | Text processing, embeddings, transformers | 05-nlp |
| `computer-vision` | Image augmentation, transfer learning, detection | 06-computer-vision |
| `ml-deployment` | FastAPI, Docker, monitoring, versioning | 07-model-deployment |

### Skill Features

Each skill includes:
- **Parameter Validation** - Required/optional with types
- **Retry Logic** - Exponential backoff
- **Observability** - Logging and metrics
- **Quick Start** - Working code examples
- **Best Practices** - DO/DON'T guidelines
- **Unit Test Templates** - pytest examples
- **Troubleshooting** - Problem/cause/solution tables

---

## Commands

| Command | Description |
|---------|-------------|
| `/learn` | Start an ML learning path |
| `/explore` | Explore available agents |
| `/roadmap` | ML learning roadmaps |
| `/skills` | Browse available skills |
| `/trending` | Trending ML technologies |
| `/projects` | ML project ideas |
| `/compare` | Compare ML algorithms |
| `/career-path` | ML career recommendations |

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Agent not found | Restart Claude Code after installation |
| Skill not loading | Check SKILL.md frontmatter syntax |
| Command error | Verify command file exists in `/commands` |

### Debug Checklist

1. Verify plugin.json paths are correct
2. Check agent/skill YAML frontmatter
3. Ensure all referenced files exist
4. Validate JSON syntax in plugin.json

---

## Integrity Matrix

| Agent | Primary Skill | Status |
|-------|--------------|--------|
| 01-ml-fundamentals | ml-fundamentals | Bonded |
| 02-supervised-learning | supervised-learning | Bonded |
| 03-unsupervised-learning | clustering | Bonded |
| 04-deep-learning | deep-learning | Bonded |
| 05-nlp | nlp-basics | Bonded |
| 06-computer-vision | computer-vision | Bonded |
| 07-model-deployment | ml-deployment | Bonded |

**Validation:**
- Zero broken links
- Zero orphan skills
- Zero ghost triggers
- Zero circular dependencies

---

## Metadata

| Field | Value |
|-------|-------|
| **Version** | 1.4.0 |
| **Last Updated** | 2025-01-01 |
| **Status** | Production Ready |
| **SASMP** | v1.4.0 |
| **Agents** | 7 |
| **Skills** | 7 |
| **Commands** | 8 |

---

## Contributing

1. Fork the repository
2. Create your feature branch
3. Follow the production-grade format for agents/skills
4. Submit a pull request

---

## License

Copyright 2025 **Dr. Umit Kacar** & **Muhsin Elcicek**

See [LICENSE](LICENSE) for details.

---

<div align="center">

**Made with precision for the Claude Code Community**

[![GitHub](https://img.shields.io/badge/GitHub-pluginagentmarketplace-black?style=for-the-badge&logo=github)](https://github.com/pluginagentmarketplace)

</div>
