# KM Internal Plugin Migration Instructions

## Target Repository
`oslokommune/golden-path-iac`

## Objective
Convert this repository into a Claude Code plugin by adding the plugin structure and migrating the github-projects skill from the DIG marketplace.

## Steps

### 1. Create Plugin Manifest

Create `.claude-plugin/plugin.json` at the repository root:

```json
{
  "name": "dig-km-internal",
  "description": "Internal workflows and tools for Team kjøremiljø (KM) at DIG Oslo kommune",
  "version": "2.0.0",
  "author": {
    "name": "Kjøremiljø"
  }
}
```

### 2. Create Plugin Directory Structure

The plugin requires these directories at the repository ROOT:

```
golden-path-iac/
├── .claude-plugin/
│   └── plugin.json          # Created in step 1
├── skills/                  # NEW - plugin skills (copy from this package)
│   └── github-projects/
│       ├── SKILL.md
│       └── reference/
└── ...                      # Existing repo content
```

### 3. Copy Content

Copy the following from this migration package to the target repository root:

1. `skills/` → `<repo-root>/skills/`

### 4. Verify Plugin Structure

After migration, the repository should be installable as a plugin:

```bash
# Test locally
claude plugin install ./

# Verify skills are available
claude --print-skills
```

## Content Included

This package contains:

- `skills/github-projects/` - GitHub Projects workflow skill:
  - `SKILL.md` - Three-phase workflow for GitHub Projects:
    - **Phase 1: Review** - Display project board, pick tasks
    - **Phase 2: Setup** - Create branch, draft PR, update status
    - **Phase 3: Complete** - Finalize PR, update status
  - `reference/` - Additional reference documentation

- `plugin.json` - Reference for the manifest (adapt as needed)

## Notes

- This skill is specific to Team kjøremiljø's GitHub Projects workflow
- Default project: oslokommune project #27 (Team kjøremiljø)
- Contains hardcoded project IDs and field IDs for the team's project board
- Trigger phrases: "show project", "what should I work on", "start issue", "I'm done"
