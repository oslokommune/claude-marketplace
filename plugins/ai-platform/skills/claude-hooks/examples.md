# Hooks Examples

Practical examples of configurable hooks for common use cases.

## Example 1: Auto-Approve File Reads

Auto-approve reading documentation and configuration files without permission prompts.

**Configuration (.claude/settings.json):**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Read",
        "hooks": [
          {
            "type": "command",
            "command": "python3 '$CLAUDE_PROJECT_DIR'/.claude/hooks/auto-approve-docs.py"
          }
        ]
      }
    ]
  }
}
```

**Script (.claude/hooks/auto-approve-docs.py):**
```python
#!/usr/bin/env python3
import json
import sys

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(1)

file_path = input_data.get("tool_input", {}).get("file_path", "")

# Auto-approve documentation files
doc_extensions = (".md", ".mdx", ".txt", ".json", ".yaml", ".yml", ".toml")
config_patterns = (".env.example", "README", "package.json", "pyproject.toml")

should_auto_approve = (
    file_path.endswith(doc_extensions) or
    any(pattern in file_path for pattern in config_patterns)
)

if should_auto_approve:
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "permissionDecisionReason": "Documentation/config file auto-approved"
        },
        "suppressOutput": True
    }
    print(json.dumps(output))
    sys.exit(0)

# For other files, use normal permission flow
sys.exit(0)
```

## Example 2: Validate User Input

Prevent users from accidentally including secrets in prompts.

**Configuration (.claude/settings.json):**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 '$CLAUDE_PROJECT_DIR'/.claude/hooks/validate-prompt.py"
          }
        ]
      }
    ]
  }
}
```

**Script (.claude/hooks/validate-prompt.py):**
```python
#!/usr/bin/env python3
import json
import re
import sys
import datetime

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)

prompt = input_data.get("prompt", "")

# Check for sensitive patterns
sensitive_patterns = [
    (r"(?i)\b(password|secret|key|token|api_key|auth|credential)\s*[:=]",
     "appears to contain credentials"),
    (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
     "may contain email addresses"),
    (r"(?i)(database|db)_url\s*[:=]",
     "may contain database connection strings"),
]

issues = []
for pattern, message in sensitive_patterns:
    if re.search(pattern, prompt):
        issues.append(message)

if issues:
    # Block prompt with warning
    output = {
        "decision": "block",
        "reason": f"Security check: Prompt {', '.join(issues)}. Please remove sensitive information and try again."
    }
    print(json.dumps(output))
    sys.exit(0)

# Add context with current timestamp
context = f"Current time: {datetime.datetime.now().isoformat()}"
output = {
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": context
    }
}
print(json.dumps(output))
sys.exit(0)
```

## Example 3: Auto-Format Code After Writing

Run code formatter immediately after writing files.

**Configuration (.claude/settings.json):**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 '$CLAUDE_PROJECT_DIR'/.claude/hooks/format-code.py",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

**Script (.claude/hooks/format-code.py):**
```python
#!/usr/bin/env python3
import json
import sys
import subprocess

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(1)

file_path = input_data.get("tool_input", {}).get("file_path", "")

# Only format Python files
if not file_path.endswith(".py"):
    sys.exit(0)

# Run black formatter
try:
    result = subprocess.run(
        ["black", "--quiet", file_path],
        timeout=10,
        capture_output=True
    )
    if result.returncode == 0:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": f"Code formatted with black"
            }
        }
        print(json.dumps(output))
    sys.exit(0)
except (subprocess.TimeoutExpired, FileNotFoundError):
    # black not installed or timed out, continue anyway
    sys.exit(0)
```

## Example 4: Intelligent Stop Hook

Use LLM to decide if Claude should continue or stop.

**Configuration (.claude/settings.json):**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Evaluate whether Claude should stop working based on the session context: $ARGUMENTS\n\nConsider:\n1. Are all user-requested tasks complete?\n2. Are there any errors that need fixing?\n3. Is follow-up work needed?\n\nRespond with JSON:\n{\"decision\": \"approve\" to stop | \"block\" to continue, \"reason\": \"explanation\"}",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Example 5: Conditional Bash Command Validation

Prevent execution of potentially dangerous bash commands.

**Configuration (.claude/settings.json):**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 '$CLAUDE_PROJECT_DIR'/.claude/hooks/validate-bash.py"
          }
        ]
      }
    ]
  }
}
```

**Script (.claude/hooks/validate-bash.py):**
```python
#!/usr/bin/env python3
import json
import re
import sys

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(1)

command = input_data.get("tool_input", {}).get("command", "")

# Define dangerous patterns to warn about
dangerous_patterns = [
    (r"\brm\s+-rf\s+/", "Attempted recursive delete of root directory"),
    (r"\b:(){:\|:&};:", "Potential fork bomb detected"),
    (r">\s*/dev/sda", "Attempted raw disk overwrite"),
]

warnings = []
for pattern, message in dangerous_patterns:
    if re.search(pattern, command):
        warnings.append(message)

if warnings:
    # Block with clear error message
    error_msg = "Security blocked: " + ", ".join(warnings)
    print(error_msg, file=sys.stderr)
    sys.exit(2)

# Also warn about common mistakes (non-blocking)
if "grep" in command and "|" not in command:
    print("Tip: Consider using 'rg' (ripgrep) instead of 'grep' for better performance", file=sys.stderr)

sys.exit(0)
```

## Example 6: Load Project Context on Startup

Add relevant project information when session starts.

**Configuration (.claude/settings.json):**
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "bash '$CLAUDE_PROJECT_DIR'/.claude/hooks/load-context.sh"
          }
        ]
      }
    ]
  }
}
```

**Script (.claude/hooks/load-context.sh):**
```bash
#!/bin/bash

# Load project context and persist environment variables if available
if [ -n "$CLAUDE_ENV_FILE" ]; then
  # Export relevant environment variables
  echo 'export PROJECT_ROOT="'"$CLAUDE_PROJECT_DIR"'"' >> "$CLAUDE_ENV_FILE"
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi

# Output context information
echo "# Project Context"
echo ""
echo "## Recent Changes"
git log --oneline -5 2>/dev/null || echo "Not a git repository"
echo ""
echo "## Current Branch"
git branch --show-current 2>/dev/null || echo "N/A"
echo ""
echo "## Open Issues"
if [ -d ".beads" ]; then
  bd ready 2>/dev/null | head -5 || echo "No issues tracked"
else
  echo "No issue tracking configured"
fi

exit 0
```

## Example 7: Permission-Based Bash Command Approval

Auto-approve safe commands, ask for confirmation on others.

**Configuration (.claude/settings.json):**
```json
{
  "hooks": {
    "PermissionRequest": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 '$CLAUDE_PROJECT_DIR'/.claude/hooks/bash-permissions.py"
          }
        ]
      }
    ]
  }
}
```

**Script (.claude/hooks/bash-permissions.py):**
```python
#!/usr/bin/env python3
import json
import sys

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(1)

tool_input = input_data.get("tool_input", {})
command = tool_input.get("command", "")

# Safe commands that can be auto-approved
safe_patterns = [
    "git status",
    "git log",
    "ls ",
    "pwd",
    "echo ",
    "cat ",
    "head ",
    "tail ",
]

# Check if command starts with a safe pattern
is_safe = any(command.startswith(pattern) for pattern in safe_patterns)

if is_safe:
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PermissionRequest",
            "decision": {
                "behavior": "allow"
            }
        }
    }
    print(json.dumps(output))
else:
    # For other commands, ask user
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PermissionRequest",
            "decision": {
                "behavior": "ask"
            }
        }
    }
    print(json.dumps(output))

sys.exit(0)
```

## Example 8: Post-Edit Validation

Validate files after they're edited.

**Configuration (.claude/settings.json):**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 '$CLAUDE_PROJECT_DIR'/.claude/hooks/validate-edit.py"
          }
        ]
      }
    ]
  }
}
```

**Script (.claude/hooks/validate-edit.py):**
```python
#!/usr/bin/env python3
import json
import sys
import subprocess

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(1)

file_path = input_data.get("tool_input", {}).get("file_path", "")

# Validate JSON files
if file_path.endswith(".json"):
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": "JSON file syntax validated successfully"
            }
        }
        print(json.dumps(output))
    except json.JSONDecodeError as e:
        output = {
            "decision": "block",
            "reason": f"Invalid JSON in {file_path}: {e}"
        }
        print(json.dumps(output))
    sys.exit(0)

# Validate Python files
if file_path.endswith(".py"):
    result = subprocess.run(
        ["python3", "-m", "py_compile", file_path],
        capture_output=True
    )
    if result.returncode != 0:
        output = {
            "decision": "block",
            "reason": f"Python syntax error in {file_path}: {result.stderr.decode()}"
        }
        print(json.dumps(output))
    sys.exit(0)

sys.exit(0)
```

## Example 9: MCP Tool Logging

Log all MCP tool operations.

**Configuration (.claude/settings.json):**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "mcp__.*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 '$CLAUDE_PROJECT_DIR'/.claude/hooks/log-mcp-calls.py"
          }
        ]
      }
    ]
  }
}
```

**Script (.claude/hooks/log-mcp-calls.py):**
```python
#!/usr/bin/env python3
import json
import sys
from datetime import datetime

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(1)

tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})
tool_response = input_data.get("tool_response", {})

log_entry = {
    "timestamp": datetime.now().isoformat(),
    "tool": tool_name,
    "input_keys": list(tool_input.keys()),
    "response_keys": list(tool_response.keys()),
}

# Log to file
log_file = "/tmp/mcp_operations.log"
try:
    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
except Exception:
    pass

sys.exit(0)
```

## Example 10: Block Sensitive File Writes

Prevent writing to sensitive files.

**Configuration (.claude/settings.json):**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 '$CLAUDE_PROJECT_DIR'/.claude/hooks/protect-sensitive-files.py"
          }
        ]
      }
    ]
  }
}
```

**Script (.claude/hooks/protect-sensitive-files.py):**
```python
#!/usr/bin/env python3
import json
import sys

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(1)

file_path = input_data.get("tool_input", {}).get("file_path", "")

# Protect sensitive files
protected_patterns = [
    ".env",
    ".secrets",
    "credentials",
    "private.key",
    ".aws/credentials",
    ".ssh/id_rsa",
]

is_protected = any(pattern in file_path for pattern in protected_patterns)

if is_protected:
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": f"Cannot write to sensitive file: {file_path}"
        }
    }
    print(json.dumps(output))
    sys.exit(0)

sys.exit(0)
```

## Example 11: Simple Context Injection

Add custom context to every prompt submission.

**Configuration (.claude/settings.json):**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Working in project: MyProject. Always follow the style guide in STYLE.md'"
          }
        ]
      }
    ]
  }
}
```

When user submits a prompt, this context is automatically added to the conversation.

## Example 12: Cleanup on Session End

Perform cleanup tasks when session ends.

**Configuration (.claude/settings.json):**
```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash '$CLAUDE_PROJECT_DIR'/.claude/hooks/cleanup.sh"
          }
        ]
      }
    ]
  }
}
```

**Script (.claude/hooks/cleanup.sh):**
```bash
#!/bin/bash

# Clean up temporary files
find "$CLAUDE_PROJECT_DIR" -name "*.tmp" -delete 2>/dev/null

# Log session end
echo "[$(date)] Session ended" >> "$CLAUDE_PROJECT_DIR/.claude/session.log"

# Optional: sync git changes
# cd "$CLAUDE_PROJECT_DIR" && git add -A && git commit -m "Session cleanup" 2>/dev/null

exit 0
```

## Testing Hooks

Always test hooks before deploying:

```bash
# 1. Test the script manually
bash .claude/hooks/your-script.sh

# 2. Test with sample JSON input
echo '{"tool_name":"Read","tool_input":{"file_path":"test.md"}}' | \
  python3 .claude/hooks/your-script.py

# 3. Enable debug mode in Claude Code
claude --debug

# 4. Check registered hooks
# Run /hooks command in Claude Code
```

## Troubleshooting Tips

- Use `$CLAUDE_PROJECT_DIR` for reliable paths
- Always quote shell variables: `"$VAR"`
- Test scripts standalone before using in hooks
- Check exit codes: 0=success, 2=block, other=warning
- Use `json.loads()` to parse stdin safely
- Add logging to temporary files for debugging
- Run `claude --debug` to see hook execution details
