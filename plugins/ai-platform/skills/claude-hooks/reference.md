# Hooks Reference Documentation

## Hook Events - Complete Reference

### PreToolUse

Runs after Claude creates tool parameters and before the tool executes.

**Matcher Values:**
- `Task` - Subagent tasks
- `Bash` - Shell commands
- `Glob` - File pattern matching
- `Grep` - Content search
- `Read` - File reading
- `Edit` - File editing
- `Write` - File writing
- `WebFetch`, `WebSearch` - Web operations
- `mcp__*` - MCP server tools (e.g., `mcp__memory__create_entities`)

**Input Schema:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "default|plan|acceptEdits|bypassPermissions",
  "hook_event_name": "PreToolUse",
  "tool_name": "string",
  "tool_input": { /* tool-specific */ },
  "tool_use_id": "string"
}
```

**Decision Control:**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow" | "deny" | "ask",
    "permissionDecisionReason": "string",
    "updatedInput": { /* modified parameters */ }
  }
}
```

- `allow` - Bypass permission system, approve automatically
- `deny` - Block the tool call, show reason to Claude
- `ask` - Ask user for confirmation in UI

### PostToolUse

Runs immediately after a tool completes successfully.

**Input Schema:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "string",
  "hook_event_name": "PostToolUse",
  "tool_name": "string",
  "tool_input": { /* tool-specific */ },
  "tool_response": { /* tool-specific */ },
  "tool_use_id": "string"
}
```

**Decision Control:**
```json
{
  "decision": "block" | undefined,
  "reason": "Explanation for decision",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "Additional information for Claude"
  }
}
```

- `block` - Prompts Claude with reason
- `undefined` - No feedback to Claude

### PermissionRequest

Runs when Claude asks permission to use a tool.

**Matcher Values:** Same as PreToolUse

**Input Schema:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "string",
  "hook_event_name": "PermissionRequest",
  "tool_name": "string"
}
```

**Decision Control:**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow" | "deny",
      "updatedInput": { /* optional */ },
      "message": "Optional reason for deny"
    }
  }
}
```

### UserPromptSubmit

Runs when user submits a prompt, before Claude processes it.

**Input Schema:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "string",
  "hook_event_name": "UserPromptSubmit",
  "prompt": "string"
}
```

**Exit Code 0 (Success):**
- Plain text stdout → Added as context to conversation
- JSON with `additionalContext` → Structured context addition

**Decision Control:**
```json
{
  "decision": "block" | undefined,
  "reason": "Explanation shown to user",
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "string"
  }
}
```

- `block` - Prevent prompt processing, erase from context
- `undefined` - Allow prompt to proceed

**Exit Code 2:**
- Blocks prompt processing
- stderr message shown to user only (not Claude)
- Prompt erased from context

### Stop

Runs when Claude finishes responding. Does not run on user interrupt.

**Input Schema:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "permission_mode": "string",
  "hook_event_name": "Stop",
  "stop_hook_active": boolean
}
```

**Decision Control (Bash):**
```json
{
  "decision": "block" | undefined,
  "reason": "Required when blocking - tells Claude how to proceed"
}
```

**Decision Control (Prompt):**
```json
{
  "decision": "approve" | "block",
  "reason": "Explanation",
  "continue": false,
  "stopReason": "Message shown to user"
}
```

**Note:** Check `stop_hook_active: true` to prevent infinite loops when Stop hooks trigger other work.

### SubagentStop

Runs when a subagent (Task tool call) finishes.

**Input Schema:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "permission_mode": "string",
  "hook_event_name": "SubagentStop",
  "stop_hook_active": boolean
}
```

**Decision Control:** Same as Stop event

### Notification

Runs when Claude Code sends notifications.

**Matcher Values:**
- `permission_prompt` - Permission requests
- `idle_prompt` - Idle timeout (60+ seconds)
- `auth_success` - Authentication success
- `elicitation_dialog` - MCP tool input needed

**Input Schema:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "string",
  "hook_event_name": "Notification",
  "message": "string",
  "notification_type": "string"
}
```

### SessionStart

Runs when Claude Code starts or resumes a session.

**Matcher Values:**
- `startup` - Normal startup
- `resume` - Resume with --resume/--continue
- `clear` - After /clear command
- `compact` - After auto/manual compact

**Input Schema:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "permission_mode": "string",
  "hook_event_name": "SessionStart",
  "source": "startup" | "resume" | "clear" | "compact"
}
```

**Environment Variable:**
- `CLAUDE_ENV_FILE` - Path to file for persisting environment variables

**Decision Control:**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "string"
  }
}
```

**Example: Persisting environment variables**
```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=production' >> "$CLAUDE_ENV_FILE"
  echo 'export API_KEY=your-api-key' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

### SessionEnd

Runs when Claude Code session ends.

**Input Schema:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "string",
  "hook_event_name": "SessionEnd",
  "reason": "clear" | "logout" | "prompt_input_exit" | "other"
}
```

Cannot block session termination, but can perform cleanup tasks.

### PreCompact

Runs before Claude Code performs a compact operation.

**Matcher Values:**
- `manual` - From `/compact` command
- `auto` - From auto-compact (full context window)

**Input Schema:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "permission_mode": "string",
  "hook_event_name": "PreCompact",
  "trigger": "manual" | "auto",
  "custom_instructions": "string"
}
```

## Exit Codes and Behavior

### Exit Code 0 (Success)

| Hook Event | Behavior |
|-----------|----------|
| `PreToolUse` | Allow tool call, stdout in verbose mode |
| `PermissionRequest` | Auto-approve, stdout in verbose mode |
| `PostToolUse` | Tool already ran, stdout in verbose mode |
| `Notification` | stdout in verbose mode only |
| `UserPromptSubmit` | **stdout added as context**, allow prompt |
| `Stop` | stdout in verbose mode, process JSON output |
| `SubagentStop` | stdout in verbose mode, process JSON output |
| `SessionStart` | **stdout added as context** |
| `SessionEnd` | stdout in verbose mode |
| `PreCompact` | stdout in verbose mode |

### Exit Code 2 (Blocking Error)

| Hook Event | Behavior |
|-----------|----------|
| `PreToolUse` | Block tool call, stderr to Claude |
| `PermissionRequest` | Deny permission, stderr to Claude |
| `PostToolUse` | stderr to Claude (tool already ran) |
| `Notification` | stderr to user only |
| `UserPromptSubmit` | Block prompt, stderr to user only, erase prompt |
| `Stop` | Block stoppage, stderr to Claude |
| `SubagentStop` | Block stoppage, stderr to Claude subagent |
| `SessionStart` | stderr to user only |
| `SessionEnd` | stderr to user only |
| `PreCompact` | stderr to user only |

### Other Exit Codes

Non-blocking error. stderr shown to user in verbose mode with format: `Failed with non-blocking status code: {stderr}`

## JSON Output Format

### Common Fields (All Hooks)

```json
{
  "continue": true,
  "stopReason": "string",
  "suppressOutput": true,
  "systemMessage": "string"
}
```

- `continue: false` - Stop Claude execution
- `stopReason` - Message shown when continue is false
- `suppressOutput: true` - Hide stdout from transcript
- `systemMessage` - Warning message to user

### PreToolUse JSON Output

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow" | "deny" | "ask",
    "permissionDecisionReason": "string",
    "updatedInput": { /* modified tool input */ }
  }
}
```

### PermissionRequest JSON Output

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow" | "deny",
      "updatedInput": { /* optional */ },
      "message": "Optional reason for deny",
      "interrupt": false
    }
  }
}
```

### PostToolUse JSON Output

```json
{
  "decision": "block" | undefined,
  "reason": "string",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "string"
  }
}
```

### UserPromptSubmit JSON Output

```json
{
  "decision": "block" | undefined,
  "reason": "string",
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "string"
  }
}
```

### Stop/SubagentStop JSON Output

```json
{
  "decision": "approve" | "block",
  "reason": "string",
  "continue": false,
  "stopReason": "string"
}
```

## Configuration Files

### Settings Hierarchy

1. **Enterprise** (highest priority) - Managed policy settings
2. **User** - `~/.claude/settings.json`
3. **Project** - `.claude/settings.json`
4. **Local** - `.claude/settings.local.json` (not committed)

Enterprise can use `allowManagedHooksOnly` to block user/project/plugin hooks.

### Hook Configuration Structure

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "Pattern",
        "hooks": [
          {
            "type": "command",
            "command": "bash-command",
            "timeout": 60
          },
          {
            "type": "prompt",
            "prompt": "Your evaluation prompt",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Environment Variables

### Available in All Hooks

- `CLAUDE_PROJECT_DIR` - Absolute path to project root
- `CLAUDE_CODE_REMOTE` - "true" if running in web environment
- All standard environment variables

### Available Only in SessionStart

- `CLAUDE_ENV_FILE` - Path to file for persisting environment variables for subsequent bash commands

## Plugin Hooks

Plugin hooks are merged with user and project hooks automatically.

**Plugin hook file:** `hooks/hooks.json` or custom path in `hooks` field

**Environment variables for plugins:**
- `${CLAUDE_PLUGIN_ROOT}` - Absolute path to plugin directory
- `${CLAUDE_PROJECT_DIR}` - Project root directory

**Example plugin hook:**
```json
{
  "description": "Plugin hook description",
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Execution Details

- **Timeout**: 60 seconds default (configurable per command)
- **Parallelization**: All matching hooks run in parallel
- **Deduplication**: Identical hook commands deduplicated automatically
- **Working directory**: Current directory when Claude Code runs
- **Input**: JSON via stdin
- **Output**: stdout/stderr processed per exit code and hook type

## MCP Tool Hooks

MCP tools follow naming pattern: `mcp__<server>__<tool>`

Examples:
- `mcp__memory__create_entities`
- `mcp__filesystem__read_file`
- `mcp__github__search_repositories`

Target specific tools or servers with regex:
```json
{
  "matcher": "mcp__memory__.*",
  "hooks": [...]
}
```

Or target all write operations:
```json
{
  "matcher": "mcp__.*__write.*",
  "hooks": [...]
}
```

## Debugging

### Enable Debug Mode
```bash
claude --debug
```

Shows:
- Hook matching and execution
- Command execution details
- Exit codes and output
- Hook timing information

### Common Troubleshooting

| Problem | Solution |
|---------|----------|
| Hook not triggering | Check description matches user request keywords |
| JSON syntax error | Escape quotes: `\"`, validate with JSON linter |
| Matcher not matching | Remember case-sensitive exact matches, regex supported |
| Command not found | Use absolute paths, verify executable permissions |
| Timeout | Increase timeout value, check for hanging processes |
| Scripts not working | Test manually first, verify PATH, check exit codes |

### View Registered Hooks

Run `/hooks` command to see all loaded hooks and their configuration.

## Security Best Practices

1. **Validate inputs** - Never trust stdin data blindly
2. **Quote variables** - Always use `"$VAR"` not `$VAR`
3. **Block path traversal** - Check for `..` in paths
4. **Use absolute paths** - Specify full paths, use `$CLAUDE_PROJECT_DIR`
5. **Skip sensitive files** - Avoid `.env`, `.git/`, API keys, etc.
6. **Limit scope** - Use `allowed-tools` to restrict capabilities
7. **Test thoroughly** - Test in safe environment before production

### Security Warning

⚠️ **Hooks execute arbitrary shell commands.** You are solely responsible for:
- Commands you configure
- Files hooks can access/modify
- Data hooks can process
- System damage from malicious/broken hooks

Anthropic provides no warranty or liability for hook-related damages.

### Configuration Safety

- Settings snapshot taken at startup
- Changes to hook config require review in `/hooks` menu
- Prevents external hook modification from affecting current session

## Best Practices

1. **Keep hooks focused** - Do one thing well
2. **Use allowed-tools** - Restrict unnecessary tool access
3. **Add clear descriptions** - Help users understand when hooks run
4. **Log for debugging** - Write to files for troubleshooting
5. **Handle errors gracefully** - Proper exit codes and messages
6. **Test thoroughly** - Verify behavior in safe environment
7. **Version control** - Commit hooks for team consistency
8. **Document custom hooks** - Explain purpose and dependencies
