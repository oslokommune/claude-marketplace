# Plugin Marketplace Architecture

This document describes the architecture for Claude Code plugins and marketplaces at DIG Oslo kommune.

## Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         End User                                │
│                                                                 │
│  claude plugin marketplace add oslokommune/claude-marketplace   │
│  claude plugin install ai-platform@dig                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Marketplace (this repo)                    │
│                                                                 │
│  A thin index that points to plugins in their source repos      │
│                                                                 │
│  .claude-plugin/marketplace.json                                │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ {                                                         │  │
│  │   "plugins": [                                            │  │
│  │     { "name": "ai-platform",                              │  │
│  │       "source": { "repo": "oslokommune/kunstig-..." }}    │  │
│  │   ]                                                       │  │
│  │ }                                                         │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Source Repositories                         │
│                                                                 │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐  │
│  │kunstig-intelligens│  │golden-path-      │  │punkt         │  │
│  │                  │  │boilerplate       │  │              │  │
│  │ ai-platform      │  │ iac-platform     │  │ designsystem │  │
│  │ plugin           │  │ plugin           │  │ plugin       │  │
│  └──────────────────┘  └──────────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Core Concepts

### Plugin

A **plugin** is an addon to Claude Code that extends its capabilities. A plugin can contain:

| Component | Purpose | Location |
|-----------|---------|----------|
| **Skills** | Knowledge and workflows Claude can invoke | `skills/<name>/SKILL.md` |
| **Commands** | User-invocable slash commands | `commands/<name>.md` |
| **Hooks** | Event-driven automation | `plugin.json` or `hooks/hooks.json` |
| **MCP Servers** | External tool integrations | `plugin.json` or `.mcp.json` |
| **LSP Servers** | Language intelligence for codebase navigation | `plugin.json` or `.lsp.json` |

### Marketplace

A **marketplace** is a distribution index that catalogs plugins and their locations. It does not contain plugin code—it only points to where plugins are hosted.

### Skill

A **skill** is knowledge or a workflow that Claude can autonomously invoke based on context. Skills are triggered by:
- Matching the `description` field against user intent
- Direct invocation via `/skill-name`

### Command

A **command** is a user-invocable action triggered with a slash prefix (e.g., `/explore`). Unlike skills, commands are explicitly invoked by the user.

### Hook

A **hook** is an event handler that runs shell commands in response to Claude Code events (e.g., `SessionStart`, `SessionEnd`, `Notification`).

## Directory Structures

### Plugin Structure

A repository becomes a plugin by having `.claude-plugin/plugin.json` at its root:

```
repository/
├── .claude-plugin/
│   └── plugin.json           # Required: plugin manifest
├── skills/                   # Plugin skills (exposed when installed)
│   └── <skill-name>/
│       ├── SKILL.md          # Required: skill definition
│       └── *.md              # Supporting documentation
├── commands/                 # Slash commands
│   └── <command-name>.md
├── scripts/                  # Hook scripts
│   └── *.py
├── .mcp.json                 # MCP server definitions (optional)
├── .lsp.json                 # LSP server definitions (optional)
└── .claude/                  # Project config (separate from plugin)
    ├── settings.json         # Project-specific settings
    └── skills/               # Project-specific skills (not in plugin)
```

**Important distinctions:**
- `skills/` at root → Plugin skills, available when plugin is installed anywhere
- `.claude/skills/` → Project skills, only available when working in this repo

### Marketplace Structure

```
marketplace-repo/
├── .claude-plugin/
│   └── marketplace.json      # Required: marketplace index
└── README.md
```

### Skill Structure

```
skills/<skill-name>/
├── SKILL.md                  # Required: main skill file
├── reference/                # Optional: additional docs
│   └── *.md
└── templates/                # Optional: code templates
    └── *
```

## Configuration Files

### plugin.json

```json
{
  "name": "plugin-name",
  "description": "What this plugin provides",
  "version": "1.0.0",
  "author": {
    "name": "Team Name"
  },
  "keywords": ["tag1", "tag2"],
  "hooks": {
    "SessionStart": [...],
    "SessionEnd": [...],
    "Notification": [...]
  },
  "mcpServers": {...},
  "lspServers": {...}
}
```

### marketplace.json

```json
{
  "name": "marketplace-name",
  "owner": {
    "name": "Organization",
    "email": "contact@example.com"
  },
  "metadata": {
    "description": "Marketplace description",
    "version": "1.0.0"
  },
  "plugins": [
    {
      "name": "plugin-name",
      "source": {
        "source": "github",
        "repo": "org/repo-name"
      },
      "description": "Plugin description",
      "author": { "name": "Team" }
    }
  ]
}
```

### SKILL.md

```markdown
---
name: skill-name
description: >
  Detailed description of when Claude should use this skill.
  Include trigger phrases and use cases.
---

# Skill Title

## Instructions

Step-by-step instructions for Claude to follow...

## Reference

Links to additional documentation...
```

## Plugin Sources

Marketplaces can reference plugins from multiple sources:

### Local Path
```json
{ "source": "./plugins/local-plugin" }
```

### GitHub Repository
```json
{
  "source": {
    "source": "github",
    "repo": "owner/repo-name"
  }
}
```

### Any Git URL
```json
{
  "source": {
    "source": "url",
    "url": "https://gitlab.com/org/repo.git"
  }
}
```

## Skill Types

### Instructional Skills

Teach Claude how to perform tasks following specific patterns:

```markdown
---
name: python-scripting
description: How to use UV package manager for Python development
---

# Python Scripting

## Instructions

When developing in Python, always use UV package manager...
```

### Workflow Skills

Guide Claude through multi-phase processes:

```markdown
---
name: github-projects
description: Manage GitHub Projects with three phases - review, setup, complete
---

# GitHub Projects Workflow

## Phase 1: Review
...

## Phase 2: Setup
...

## Phase 3: Complete
...
```

### Documentation Skills

Provide reference material Claude reads on-demand:

```markdown
---
name: punkt-docs
description: Punkt Design System component documentation
---

# Punkt Design System

## Components

- [Button](components/button.md)
- [Modal](components/modal.md)
...
```

## Installation Scopes

| Scope | Location | Use Case |
|-------|----------|----------|
| `user` | `~/.claude/settings.json` | Personal plugins across all projects |
| `project` | `.claude/settings.json` | Team plugins shared via version control |
| `local` | `.claude/settings.local.json` | Project-specific, gitignored |

## Development Workflow

### For Plugin Developers

```bash
# Work in the source repository
cd kunstig-intelligens

# Install plugin locally for testing
claude plugin install ./

# Verify skills are available
claude --print-skills

# Make changes, test, iterate
# Commit and push when ready
```

### For End Users

```bash
# Add marketplace once
claude plugin marketplace add oslokommune/claude-marketplace

# Install plugins
claude plugin install ai-platform@dig
claude plugin install iac-platform@dig
```

## DIG Plugin Distribution

| Plugin | Source Repository | Domain |
|--------|-------------------|--------|
| ai-platform | oslokommune/kunstig-intelligens | AI/Claude best practices |
| iac-platform | oslokommune/golden-path-boilerplate | Terraform, infrastructure |
| km-internal | oslokommune/golden-path-iac | Team workflows |
| designsystem | oslokommune/punkt | Frontend, Punkt components |

## Key Principles

1. **Plugins live with their domain** - Skills about Terraform live in the Terraform repo
2. **Marketplace is thin** - Only an index, no plugin content
3. **Self-contained plugins** - Each plugin works independently, no cross-plugin dependencies
4. **Skills over commands** - Prefer skills (Claude decides when to use) over commands (user must invoke)
5. **Progressive disclosure** - Skills can link to detailed docs that Claude reads on-demand
