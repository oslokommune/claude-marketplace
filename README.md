# DIG Claude Marketplace

Official Claude Code plugin marketplace for Digitaliseringsetaten (DIG) Oslo kommune.

## Getting Started

Use [claude-setup](https://github.com/oslokommune/claude-setup) to set up your Claude Code workspace.

## Manual Installation

Add the marketplace:

```bash
claude plugin marketplace add oslokommune/claude-marketplace
```

Install plugins:

```bash
claude plugin install <plugin-name>@dig
```

## Available Plugins

| Plugin | Description |
|--------|-------------|
| `ai-platform` | Best practices and tools for Claude Code usage in DIG Oslo kommune |
| `iac-platform` | Infrastructure as code with Terraform and Boilerplate templates using the OK tool |
| `km-internal` | Internal workflows and tools for Team Kjremilj (KM) |
| `designsystem` | Punkt Design System - Oslo Kommune's design system for accessible frontend applications |
| `betterbeads` | GitHub-native task management CLI for AI agents using GitHub Issues and Projects |
| `claude-ping` | Sound notification plugin that plays themed audio cues in response to Claude Code events |

## Plugin Sources

This marketplace is an index that points to plugins hosted in their source repositories:

| Plugin | Repository |
|--------|------------|
| ai-platform | [oslokommune/kunstig-intelligens](https://github.com/oslokommune/kunstig-intelligens) |
| iac-platform | [oslokommune/golden-path-boilerplate](https://github.com/oslokommune/golden-path-boilerplate) |
| km-internal | [oslokommune/golden-path-iac](https://github.com/oslokommune/golden-path-iac) |
| designsystem | [oslokommune/punkt-ki](https://github.com/oslokommune/punkt-ki) |
| betterbeads | [falense/betterbeads](https://github.com/falense/betterbeads) |
| claude-ping | [oslokommune/claude-ping](https://github.com/oslokommune/claude-ping) |

## Updating Plugins

```bash
claude plugin update <plugin-name>@dig
```

## For Plugin Developers

Work directly in the source repository. See [CLAUDE.md](CLAUDE.md) for contribution guidelines.
