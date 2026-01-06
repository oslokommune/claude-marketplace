---
name: hooks-reference
description: Comprehensive guide to Claude Code hooks - how to configure, write, and debug hooks that respond to tool calls, user prompts, sessions, and other events. Use when implementing automation, validation, or conditional logic triggered by Claude Code events.
---

# Claude Code Hooks Reference

Claude Code hooks are bash commands or LLM-based prompts that execute automatically in response to specific events, enabling you to automate workflows, validate actions, and integrate with external systems.

## Quick Start

Hooks are configured in your settings files:
- **User settings**: `~/.claude/settings.json`
- **Project settings**: `.claude/settings.json`
- **Local settings**: `.claude/settings.local.json`

### Basic Structure

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-bash-command"
          }
        ]
      }
    ]
  }
}
```

## Common Hook Events

| Event | Triggers | Use Case |
|-------|----------|----------|
| **PreToolUse** | Before a tool executes | Validate/approve tool calls |
| **PostToolUse** | After a tool completes | Process results, add context |
| **PermissionRequest** | When Claude asks permission | Auto-approve or deny tools |
| **UserPromptSubmit** | When user submits a prompt | Validate input, add context |
| **Stop** | When Claude finishes responding | Check if work is complete |
| **SessionStart** | When Claude Code starts | Load environment, context |
| **SessionEnd** | When Claude Code stops | Cleanup, logging |
| **Notification** | When Claude sends notifications | Handle alerts |

## Hook Types

### Bash Command Hooks (type: "command")

Execute bash scripts or commands automatically.

```json
{
  "type": "command",
  "command": "bash-command-or-script-path",
  "timeout": 60
}
```

**Exit codes:**
- **0**: Success (stdout shown in verbose mode, except UserPromptSubmit adds to context)
- **2**: Blocking error (stderr is error message, blocks action)
- **Other**: Non-blocking error (shown in verbose mode)

### Prompt-Based Hooks (type: "prompt")

Use an LLM to make intelligent context-aware decisions.

```json
{
  "type": "prompt",
  "prompt": "Your evaluation prompt with $ARGUMENTS placeholder",
  "timeout": 30
}
```

Response format:
```json
{
  "decision": "approve" | "block",
  "reason": "Explanation",
  "continue": false,
  "stopReason": "Optional message"
}
```

## Key Features

### Matchers

Pattern matching for tool-specific hooks:
- `Write` - Exact match
- `Edit|Write` - Regex match
- `*` or `""` - Match all tools

### Input/Output

**Hook input** (via stdin):
- `session_id` - Current session ID
- `cwd` - Working directory
- `tool_name` - Which tool triggered (for PreToolUse)
- `tool_input` - The tool's parameters
- Event-specific fields

**Hook output**:
- Exit code + stdout/stderr for bash hooks
- JSON response for prompt hooks
- Use `continue: false` to stop Claude execution

### Permission Decisions

For `PreToolUse` and `PermissionRequest`:
```json
{
  "hookSpecificOutput": {
    "permissionDecision": "allow" | "deny" | "ask",
    "permissionDecisionReason": "Explanation",
    "updatedInput": { "modified_field": "new_value" }
  }
}
```

### Environment Variables

- `CLAUDE_PROJECT_DIR` - Absolute path to project root
- `CLAUDE_CODE_REMOTE` - "true" if running in web environment
- `CLAUDE_ENV_FILE` - (SessionStart only) Path to persist environment variables

## For Detailed Reference

See [reference.md](reference.md) for:
- Complete hook event documentation
- Detailed input/output schemas
- All exit code behaviors
- Advanced JSON output formats
- Security considerations
- Hook execution details

See [examples.md](examples.md) for:
- Practical configuration examples
- Bash command hooks
- Prompt-based hooks
- Permission auto-approval patterns
- Error handling examples
- MCP tool hooks

## Common Patterns

### Auto-approve file reads
```json
{
  "matcher": "Read",
  "hooks": [
    {
      "type": "command",
      "command": "echo '{\"decision\": \"approve\"}'"
    }
  ]
}
```

### Validate user input
```json
{
  "hooks": [
    {
      "type": "command",
      "command": "/path/to/validation-script.py"
    }
  ]
}
```

### Intelligent stop decision
```json
{
  "hooks": [
    {
      "type": "prompt",
      "prompt": "Check if all requested tasks are complete. Return JSON with decision: approve or block"
    }
  ]
}
```

## Debugging

1. **Check configuration**: Run `/hooks` to see registered hooks
2. **Enable debug mode**: `claude --debug` for detailed execution logs
3. **Test commands**: Run hook commands manually first
4. **Verify syntax**: Ensure JSON is valid and scripts are executable
5. **Check matcher patterns**: Remember matchers are case-sensitive

Common issues:
- Quotes not escaped in JSON
- Wrong matcher names (case-sensitive)
- Commands not in PATH or missing execute permissions
- Hook timeouts (default 60 seconds)

## Security Considerations

⚠️ **Hooks execute arbitrary shell commands.** You are responsible for:
- Validating and sanitizing inputs
- Quoting all shell variables: `"$VAR"` not `$VAR`
- Using absolute paths
- Blocking path traversal (check for `..`)
- Avoiding sensitive files (`.env`, `.git/`, keys)

Always review and test hooks in a safe environment before production use.

## Next Steps

- Review complete [reference.md](reference.md) for all hook event types
- Study [examples.md](examples.md) for practical patterns
- Create hooks for your workflow
- Test with `claude --debug`
- Commit hooks to version control for team consistency
