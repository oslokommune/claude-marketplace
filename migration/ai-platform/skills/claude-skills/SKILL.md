---
name: claude-skills
description: Guide for creating and managing Agent Skills in Claude Code. Use when the user asks about Skills, how to create Skills, Skill configuration, or troubleshooting Skills.
---

# Claude Skills Guide

A Skill is a markdown file that teaches Claude how to do something specific. Skills are **model-invoked** - Claude automatically applies them when requests match their description. You don't need to explicitly call a Skill.

## How Skills Work

1. **Discovery**: At startup, Claude loads the name and description of each available Skill
2. **Activation**: When a request matches a Skill's description, Claude asks to use it
3. **Execution**: Claude follows the Skill's instructions, loading referenced files as needed

Claude uses semantic similarity to match requests against descriptions, so write descriptions with keywords users would naturally say.

## Where Skills Live

| Location   | Path                              | Applies to                        |
|:-----------|:----------------------------------|:----------------------------------|
| Enterprise | Managed settings                  | All users in your organization    |
| Personal   | `~/.claude/skills/`              | You, across all projects          |
| Project    | `.claude/skills/`                | Anyone working in this repository |
| Plugin     | Bundled with plugins              | Anyone with the plugin installed  |

If two Skills have the same name, enterprise > personal > project > plugin.

## Creating a Skill

### Minimal Structure

A Skill needs only a `SKILL.md` file:

```
my-skill/
└── SKILL.md
```

### SKILL.md Format

```yaml
---
name: your-skill-name
description: What this Skill does and when to use it (max 1024 chars)
---

# Your Skill Name

## Instructions
Clear, step-by-step guidance for Claude.

## Examples
Concrete examples of using this Skill.
```

### Required Metadata Fields

- `name`: Lowercase letters, numbers, hyphens only (max 64 chars). Must match directory name.
- `description`: What the Skill does and when to use it. **This is how Claude decides when to apply the Skill.**

### Optional Metadata Fields

- `allowed-tools`: List of tools Claude can use without permission when this Skill is active
- `model`: Specific model to use (e.g., `claude-sonnet-4-20250514`)

## Progressive Disclosure for Large Skills

Keep `SKILL.md` under 500 lines. For larger Skills, split content into multiple files:

```
my-skill/
├── SKILL.md         # Overview and navigation
├── reference.md     # Detailed docs (loaded when needed)
├── examples.md      # Usage examples (loaded when needed)
└── scripts/
    └── helper.py    # Utility script (executed, not loaded)
```

In `SKILL.md`, reference supporting files:

```markdown
For complete API details, see [reference.md](reference.md)

To validate input:
\```bash
python scripts/helper.py input.txt
\```
```

**Key principles:**
- Keep references one level deep (don't nest file references)
- Scripts can be executed without loading into context
- Only files explicitly referenced by Claude are loaded

## Restricting Tool Access

Use `allowed-tools` to limit which tools Claude can use:

```yaml
---
name: reading-files-safely
description: Read files without making changes
allowed-tools: Read, Grep, Glob
---
```

When active, Claude can only use specified tools without asking permission. Useful for:
- Read-only Skills
- Security-sensitive workflows
- Limited-scope operations

## Skills vs. Other Options

| Feature          | When it runs                  | Use for                                      |
|:-----------------|:------------------------------|:---------------------------------------------|
| **Skills**       | Claude chooses when relevant  | Specialized knowledge and standards          |
| Slash commands   | You type `/command`           | Reusable prompts you invoke explicitly       |
| CLAUDE.md        | Every conversation            | Project-wide instructions                    |
| Subagents        | Claude delegates or you invoke| Tasks needing separate context/tools         |
| Hooks            | On specific tool events       | Automated workflows on events                |
| MCP servers      | Claude calls tools as needed  | Connect to external tools/data               |

**Skills vs. subagents**: Skills add knowledge to current conversation. Subagents run in separate context with own tools.

**Skills vs. MCP**: Skills tell Claude *how* to use tools. MCP *provides* the tools.

## Using Skills with Subagents

Built-in agents (Explore, Plan, Verify) and the Task tool do NOT have access to Skills.

Only custom subagents in `.claude/agents/` can use Skills, via the `skills` field:

```yaml
# .claude/agents/my-agent/AGENT.md
---
name: my-agent
description: My custom agent
skills: skill-one, skill-two
---
```

## Troubleshooting

### Skill Not Triggering

**Problem**: Claude doesn't use your Skill when expected.

**Solution**: Improve the description. Good descriptions answer:
1. What does this Skill do? (List specific capabilities)
2. When should Claude use it? (Include trigger terms users would say)

```yaml
# Vague - won't trigger reliably
description: Helps with documents

# Clear - triggers when appropriate
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

### Skill Doesn't Load

**Check file path**: Must be `SKILL.md` (case-sensitive) in correct location:
- Personal: `~/.claude/skills/my-skill/SKILL.md`
- Project: `.claude/skills/my-skill/SKILL.md`

**Check YAML syntax**:
- `---` must start on line 1 (no blank lines before)
- Use spaces for indentation, not tabs
- Must end with `---` before Markdown content

**Run debug mode**: `claude --debug` to see loading errors

### Multiple Skills Conflict

**Problem**: Claude uses wrong Skill or seems confused.

**Solution**: Make descriptions distinct with specific trigger terms.

Instead of two Skills both mentioning "data analysis", differentiate:
- "sales data in Excel files and CRM exports"
- "log files and system metrics"

### Plugin Skills Not Appearing

1. Clear plugin cache: `rm -rf ~/.claude/plugins/cache`
2. Restart Claude Code
3. Reinstall plugin: `/plugin install plugin-name@marketplace-name`

Plugin Skills must be in `skills/` directory at plugin root:
```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── my-skill/
        └── SKILL.md
```

## Best Practices

1. **Write clear descriptions** with keywords users would naturally say
2. **Keep SKILL.md under 500 lines** - use progressive disclosure for larger Skills
3. **Use allowed-tools** to restrict capabilities when appropriate
4. **Test your Skill** by asking Claude questions that match the description
5. **List dependencies** in the description if Skill requires external packages
6. **Use present tense** and clear, actionable instructions
7. **Include examples** to show concrete usage patterns

## Viewing Available Skills

To see which Skills Claude has access to, ask: "What Skills are available?"

Claude loads all Skill names and descriptions at startup, so it can list currently available Skills.

## Distribution

- **Project Skills**: Commit `.claude/skills/` to version control
- **Plugins**: Create `skills/` directory in plugin with Skill folders
- **Enterprise**: Deploy through managed settings organization-wide
