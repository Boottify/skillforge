# ⚒ Skillforge

> **Forge skills. Ship faster.**

[![Website](https://img.shields.io/badge/website-skillforge.boottify.com-%23f59e0b?style=flat-square)](https://skillforge.boottify.com)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square)](https://www.python.org/)

Skillforge is a **lightweight skill manager for AI coding assistants**. It lets you browse, install, publish, and manage skills across Claude Code, Hermes, Cursor, Windsurf, and any tool that uses SKILL.md format.

---

## What Are Skills?

Skills are reusable procedural knowledge packs for AI coding assistants. Instead of repeating instructions, you install a skill once and the assistant loads it on demand. Skills cover workflows like:

- **Deployment pipelines** — `npm run build && restart`
- **Code review** — PR checklist, security scan, quality gates
- **Database migrations** — Prisma push, generate, verify
- **Design system** — Color tokens, typography scale, component patterns
- **Debugging** — Systematic root-cause analysis, log inspection

Each skill is a `SKILL.md` file with YAML frontmatter — portable across tools.

---

## Quick Start

```bash
# Install
curl -fsSL https://skillforge.boottify.com/install.sh | bash

# Or clone and install manually
git clone https://github.com/Boottify/skillforge.git
cd skillforge && ./install.sh
```

```bash
# Browse available skills
skillforge search "deployment"

# Install a skill
skillforge install deploy-pipeline

# List installed skills
skillforge list

# Create a new skill from template
skillforge create my-workflow

# Publish to registry
skillforge publish my-workflow
```

---

## Commands

| Command | Description |
|---------|-------------|
| `skillforge search <query>` | Search the skill registry |
| `skillforge install <name>` | Install a skill from registry |
| `skillforge list` | List installed skills |
| `skillforge create <name>` | Create a new skill from template |
| `skillforge validate <name>` | Validate SKILL.md format |
| `skillforge publish <name>` | Publish to registry |
| `skillforge update` | Update all installed skills |
| `skillforge remove <name>` | Uninstall a skill |

---

## Skill Format

Every skill is a `SKILL.md` file:

```markdown
---
name: my-skill
description: What this skill does
version: 1.0.0
---

# My Skill

## When to Use
- Use this skill when...

## Steps
1. First step
2. Second step

## Pitfalls
- Watch out for...
```

---

## Registry

The public registry lives at [skillforge.boottify.com/registry](https://skillforge.boottify.com/registry). Skills are versioned, tagged, and searchable.

Popular skills:
- `deploy-pipeline` — Build, test, deploy workflow
- `code-review` — PR checklist with security scan
- `database-migrate` — Prisma migration safety net
- `design-system` — Color and typography tokens
- `debug-workflow` — 4-phase systematic debugging

---

## Architecture

```
~/.skillforge/
├── skills/           # Installed skills
│   ├── deploy-pipeline/
│   │   └── SKILL.md
│   └── code-review/
│       └── SKILL.md
├── registry.json     # Local registry cache
└── config.yaml       # User config
```

Skillforge is a single Python script (~1,500 lines) with zero dependencies beyond Python 3.10+. It works on Linux, macOS, and WSL.

---

## Comparison

| Tool | Focus | Skillforge |
|------|-------|------------|
| **Glyph** | Codebase indexing | Complementary — index your code |
| **Skillforge** | Skill management | This tool — manage your skills |
| **Custom scripts** | One-off automation | Portable, shareable, versioned |

---

## Contributing

Skills are open. Submit yours via PR to the [registry](https://github.com/Boottify/skillforge-registry).

---

Built with ☕ in Lithuania. Part of the [Boottify](https://boottify.com) tools ecosystem.
