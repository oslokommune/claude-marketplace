# AI Platform Plugin Migration Instructions

## Target Repository
`oslokommune/kunstig-intelligens`

## Objective
Convert this repository into a Claude Code plugin by adding the plugin structure and migrating skill content from the DIG marketplace.

## Steps

### 1. Create Plugin Manifest

Create `.claude-plugin/plugin.json` at the repository root:

```json
{
  "name": "dig-ai-platform",
  "description": "Best practices and tools for Claude Code usage in DIG Oslo kommune",
  "version": "2.0.0",
  "author": {
    "name": "KITT"
  },
  "hooks": {
    "Notification": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PLUGIN_ROOT}/scripts/log-hook-event.py Notification"
          }
        ]
      }
    ],
    "PreCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PLUGIN_ROOT}/scripts/log-hook-event.py PreCompact"
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "uv run ${CLAUDE_PLUGIN_ROOT}/scripts/organize_permissions.py --merge-local"
          }
        ]
      }
    ]
  }
}
```

### 2. Create Plugin Directory Structure

The plugin requires these directories at the repository ROOT (not inside `.claude/`):

```
kunstig-intelligens/
├── .claude-plugin/
│   └── plugin.json          # Created in step 1
├── skills/                  # NEW - plugin skills (copy from this package)
│   ├── bedrock/
│   ├── claude-agent-sdk/
│   ├── claude-hooks/
│   ├── claude-skills/
│   ├── claude-subagent/
│   └── python/
├── scripts/                 # NEW - hook scripts (copy from this package)
│   ├── log-hook-event.py
│   ├── organize_permissions.py
│   └── generate-memory-from-transcript.py
├── .claude/                 # KEEP - existing project config (separate from plugin)
│   ├── settings.json
│   ├── commands/           # Project-specific commands
│   └── skills/             # Can be removed after migration or kept for project-specific skills
└── ...
```

### 3. Copy Content

Copy the following from this migration package to the target repository root:

1. `skills/` → `<repo-root>/skills/`
2. `scripts/` → `<repo-root>/scripts/`

### 4. Handle Existing `.claude/skills/`

The repository may already have `.claude/skills/`. You have two options:

**Option A (Recommended):** Remove `.claude/skills/` after verifying all content is in root `skills/`

**Option B:** Keep both if there are project-specific skills that shouldn't be part of the plugin

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

- `skills/` - 6 skills:
  - `bedrock/` - AWS Bedrock API usage
  - `claude-agent-sdk/` - Building custom agents
  - `claude-hooks/` - Claude Code hooks
  - `claude-skills/` - Creating skills
  - `claude-subagent/` - Subagent patterns
  - `python/` - Python with UV package manager

- `scripts/` - Hook scripts:
  - `log-hook-event.py` - Event logging
  - `organize_permissions.py` - Permission management
  - `generate-memory-from-transcript.py` - Memory generation

- `plugin.json` - Reference for the manifest (adapt as needed)

## Notes

- The `${CLAUDE_PLUGIN_ROOT}` variable in hooks expands to the plugin's installed location
- Skills at root level (`skills/`) are plugin skills, exposed when the plugin is installed
- Skills in `.claude/skills/` are project skills, only active when working in this repository
- Keep `.claude/settings.json` for project-specific configuration (env vars, permissions)
