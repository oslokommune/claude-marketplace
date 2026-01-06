# IAC Platform Plugin Migration Instructions

## Target Repository
`oslokommune/golden-path-boilerplate`

## Objective
Convert this repository into a Claude Code plugin by adding the plugin structure and migrating skill content from the DIG marketplace.

## Steps

### 1. Create Plugin Manifest

Create `.claude-plugin/plugin.json` at the repository root:

```json
{
  "name": "dig-iac-platform",
  "description": "Infrastructure as code with Terraform and Boilerplate templates using the OK tool",
  "version": "2.0.0",
  "author": {
    "name": "Kjøremiljø"
  },
  "keywords": [
    "iac",
    "infrastructure as code",
    "terraform",
    "boilerplate",
    "dig",
    "ok-tool",
    "aws",
    "ecs",
    "rds"
  ]
}
```

### 2. Create Plugin Directory Structure

The plugin requires these directories at the repository ROOT (not inside `.claude/`):

```
golden-path-boilerplate/
├── .claude-plugin/
│   └── plugin.json              # Created in step 1
├── skills/                      # NEW - plugin skills (copy from this package)
│   ├── golden-path-iac/         # IaC getting started, guides, reference
│   └── ok-boilerplate-templates/ # Template documentation
├── .claude/                     # KEEP - existing project config
│   ├── commands/
│   └── skills/                  # Existing project-specific skills
└── boilerplate/                 # Existing template source code
```

### 3. Copy Content

Copy the following from this migration package to the target repository root:

1. `skills/` → `<repo-root>/skills/`

### 4. Handle Existing `.claude/skills/`

The repository has `.claude/skills/boilerplate-cli/`. This is a project-specific skill for working within this repository. You have options:

**Option A:** Keep both - project skills in `.claude/skills/`, plugin skills in root `skills/`

**Option B:** Move `boilerplate-cli` to root `skills/` if it should be part of the plugin

**Option C:** Merge `boilerplate-cli` content into `ok-boilerplate-templates` if they overlap

### 5. Verify Plugin Structure

After migration, the repository should be installable as a plugin:

```bash
# Test locally
claude plugin install ./

# Verify skills are available
claude --print-skills
```

## Content Included

This package contains:

- `skills/` - 2 skills:
  - `golden-path-iac/` - Comprehensive IaC documentation:
    - `overview.md` - Architecture overview
    - `getting-started.md` - Quick start guide
    - `setup/` - Prerequisites, infrastructure, application, CI/CD setup
    - `guides/` - AWS access, backup, cleanup, CloudFront, database, observability
    - `reference/` - ADRs, Renovate, security, technologies
    - `cli/` - OK tool commands reference

  - `ok-boilerplate-templates/` - Template documentation:
    - `SKILL.md` - Main skill with template index
    - `terraform/` - 24 Terraform template docs
    - `github-actions/` - 6 GitHub Actions template docs

- `plugin.json` - Reference for the manifest (adapt as needed)

## Notes

- The templates documented in `ok-boilerplate-templates/` correspond to the actual templates in `boilerplate/terraform/` and `boilerplate/github-actions/`
- Skills at root level (`skills/`) are plugin skills, exposed when the plugin is installed
- Skills in `.claude/skills/` are project skills, only active when working in this repository
- Consider whether `boilerplate-cli` should be a plugin skill or remain project-specific
