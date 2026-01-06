---
name: agent-sdk
description: How to create Claude Code Python agents using the Claude Code SDK
---

# Claude Agent SDK Skill

## Overview

The Claude Agent SDK allows building autonomous agents that interact with Claude Code programmatically. This skill covers building agents in Python using the `claude-agent-sdk` package.

## Installation

```bash
pip install claude-agent-sdk
```

## Core Concepts

### Two Interaction Patterns

**1. `query()` - One-off interactions**
- Creates new session each time
- No conversation memory
- Best for: Independent tasks, automation scripts

**2. `ClaudeSDKClient` - Continuous conversations**
- Maintains session across multiple exchanges
- Claude remembers context
- Supports interrupts, custom tools, hooks
- Best for: Interactive apps, follow-up questions, complex workflows

## Basic Usage

### Simple Query Pattern

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "Bash"],
        permission_mode='acceptEdits',
        cwd="/path/to/project"
    )

    async for message in query(
        prompt="Analyze this codebase",
        options=options
    ):
        print(message)

asyncio.run(main())
```

### Continuous Conversation Pattern

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

async def main():
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write"],
        permission_mode='acceptEdits'
    )

    async with ClaudeSDKClient(options=options) as client:
        # First question
        await client.query("Create a Python file")
        async for message in client.receive_response():
            print(message)

        # Follow-up - Claude remembers previous context
        await client.query("Add a main function to that file")
        async for message in client.receive_response():
            print(message)

asyncio.run(main())
```

## Key Configuration Options

### ClaudeAgentOptions

```python
ClaudeAgentOptions(
    # Tool permissions
    allowed_tools=["Read", "Write", "Bash", "Grep", "Glob"],
    disallowed_tools=[],
    permission_mode='default',  # 'default', 'acceptEdits', 'plan', 'bypassPermissions'

    # Working directory
    cwd="/path/to/project",
    add_dirs=["/additional/path"],

    # Model selection
    model="claude-sonnet-4-5-20250929",

    # System prompt
    system_prompt="You are an expert...",
    # OR use preset with extensions:
    system_prompt={
        "type": "preset",
        "preset": "claude_code",
        "append": "Additional instructions..."
    },

    # MCP servers for custom tools
    mcp_servers={
        "myserver": create_sdk_mcp_server(...)
    },

    # Session management
    continue_conversation=False,
    resume="session-id",
    fork_session=False,
    max_turns=50,

    # Advanced
    can_use_tool=custom_permission_handler,
    hooks={...},
    env={"KEY": "value"},
    setting_sources=["project"]  # Load .claude/settings.json
)
```

## Creating Custom Tools

### Define Tools with @tool Decorator

```python
from claude_agent_sdk import tool, create_sdk_mcp_server
from typing import Any

@tool("fetch_price", "Fetch price from URL", {
    "url": str,
    "selector": str
})
async def fetch_price(args: dict[str, Any]) -> dict[str, Any]:
    url = args["url"]
    selector = args["selector"]

    # Your implementation
    price = await scrape_price(url, selector)

    return {
        "content": [{
            "type": "text",
            "text": f"Price: ${price}"
        }]
    }

@tool("validate_pattern", "Validate extraction pattern", {
    "html": str,
    "selector": str
})
async def validate_pattern(args: dict[str, Any]) -> dict[str, Any]:
    # Validation logic
    is_valid = check_selector(args["html"], args["selector"])

    return {
        "content": [{
            "type": "text",
            "text": f"Valid: {is_valid}"
        }]
    }

# Create MCP server with tools
extractor_server = create_sdk_mcp_server(
    name="extractor",
    version="1.0.0",
    tools=[fetch_price, validate_pattern]
)

# Use in agent
options = ClaudeAgentOptions(
    mcp_servers={"extractor": extractor_server},
    allowed_tools=[
        "mcp__extractor__fetch_price",
        "mcp__extractor__validate_pattern",
        "Read", "Write"
    ]
)
```

## Message Handling

### Processing Different Message Types

```python
from claude_agent_sdk import (
    AssistantMessage,
    TextBlock,
    ToolUseBlock,
    ToolResultBlock,
    ResultMessage
)

async with ClaudeSDKClient(options) as client:
    await client.query("Analyze this file")

    async for message in client.receive_response():
        # Assistant text responses
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(f"Text: {block.text}")
                elif isinstance(block, ToolUseBlock):
                    print(f"Using tool: {block.name}")
                    print(f"Input: {block.input}")
                elif isinstance(block, ToolResultBlock):
                    print(f"Tool result: {block.content}")

        # Final result with costs
        elif isinstance(message, ResultMessage):
            print(f"Cost: ${message.total_cost_usd}")
            print(f"Turns: {message.num_turns}")
            print(f"Duration: {message.duration_ms}ms")
```

## Advanced Features

### Custom Permission Handler

```python
async def permission_handler(tool_name: str, input_data: dict, context: dict):
    # Block dangerous operations
    if tool_name == "Bash" and "rm -rf /" in input_data.get("command", ""):
        return {
            "behavior": "deny",
            "message": "Dangerous command blocked",
            "interrupt": True
        }

    # Redirect file writes
    if tool_name == "Write":
        safe_path = f"./sandbox/{input_data['file_path']}"
        return {
            "behavior": "allow",
            "updatedInput": {**input_data, "file_path": safe_path}
        }

    # Allow everything else
    return {"behavior": "allow", "updatedInput": input_data}

options = ClaudeAgentOptions(
    can_use_tool=permission_handler,
    permission_mode="default"
)
```

### Using Hooks

```python
from claude_agent_sdk import HookMatcher, HookContext
from typing import Any

async def log_tool_use(
    input_data: dict[str, Any],
    tool_use_id: str | None,
    context: HookContext
) -> dict[str, Any]:
    print(f"Tool: {input_data.get('tool_name')}")
    return {}

async def validate_bash(
    input_data: dict[str, Any],
    tool_use_id: str | None,
    context: HookContext
) -> dict[str, Any]:
    if input_data['tool_name'] == 'Bash':
        command = input_data['tool_input'].get('command', '')
        if is_dangerous(command):
            return {
                'hookSpecificOutput': {
                    'hookEventName': 'PreToolUse',
                    'permissionDecision': 'deny',
                    'permissionDecisionReason': 'Dangerous command'
                }
            }
    return {}

options = ClaudeAgentOptions(
    hooks={
        'PreToolUse': [
            HookMatcher(matcher='Bash', hooks=[validate_bash], timeout=120),
            HookMatcher(hooks=[log_tool_use])
        ],
        'PostToolUse': [
            HookMatcher(hooks=[log_tool_use])
        ]
    }
)
```

## Error Handling

```python
from claude_agent_sdk import (
    CLINotFoundError,
    ProcessError,
    CLIJSONDecodeError,
    CLIConnectionError
)

try:
    async for message in query(prompt="Hello"):
        print(message)
except CLINotFoundError:
    print("Install Claude Code: npm install -g @anthropic-ai/claude-code")
except ProcessError as e:
    print(f"Process failed: {e.exit_code}")
    print(f"Stderr: {e.stderr}")
except CLIJSONDecodeError as e:
    print(f"JSON parse error: {e.line}")
except CLIConnectionError as e:
    print(f"Connection failed: {e}")
```

## Agent Architecture Best Practices

### 1. Single Responsibility Agents

Create focused agents for specific tasks:

```python
# Specialized scraper agent
scraper_options = ClaudeAgentOptions(
    system_prompt="You are a web scraping specialist",
    allowed_tools=["mcp__browser__navigate", "mcp__browser__extract"],
    mcp_servers={"browser": browser_server}
)

# Specialized validator agent
validator_options = ClaudeAgentOptions(
    system_prompt="You validate extraction patterns",
    allowed_tools=["mcp__validator__check", "Read"],
    mcp_servers={"validator": validator_server}
)
```

### 2. Orchestrator Pattern

Use a main agent to coordinate sub-agents:

```python
async def orchestrator():
    async with ClaudeSDKClient(orchestrator_options) as coordinator:
        # Get URLs to scrape
        await coordinator.query("Find product URLs")
        urls = extract_urls(await coordinator.receive_response())

        # Delegate to scraper agents
        for url in urls:
            async with ClaudeSDKClient(scraper_options) as scraper:
                await scraper.query(f"Extract price from {url}")
                result = await scraper.receive_response()
                # Process result
```

### 3. Feedback Loops

Implement validation and retry logic:

```python
async def extract_with_validation(url: str):
    async with ClaudeSDKClient(extractor_options) as agent:
        await agent.query(f"Generate extraction pattern for {url}")

        async for message in agent.receive_response():
            if isinstance(message, ResultMessage):
                pattern = parse_pattern(message)

                # Validate pattern
                if not validate_pattern(pattern):
                    # Retry with feedback
                    await agent.query(
                        f"Pattern failed validation. Error: {error}. Try again."
                    )
                    async for msg in agent.receive_response():
                        # Process retry
                        pass
```

### 4. State Management

Use ClaudeSDKClient for stateful interactions:

```python
class PatternGeneratorAgent:
    def __init__(self):
        self.client = None
        self.attempts = 0

    async def __aenter__(self):
        self.client = ClaudeSDKClient(options)
        await self.client.connect()
        return self

    async def generate_pattern(self, url: str):
        self.attempts += 1
        await self.client.query(f"Generate pattern for {url}")

        async for message in self.client.receive_response():
            # Client maintains conversation context
            # Next query remembers previous attempts
            pass

    async def refine_pattern(self, feedback: str):
        # Claude remembers the pattern from generate_pattern()
        await self.client.query(f"Refine based on: {feedback}")
        async for message in self.client.receive_response():
            pass

    async def __aexit__(self, *args):
        await self.client.disconnect()

# Usage
async with PatternGeneratorAgent() as agent:
    await agent.generate_pattern(url)
    await agent.refine_pattern("Price selector failed")
    # All in same conversation context
```

## Tool Input/Output Schemas

### Built-in Tools

**Read**
```python
input = {"file_path": str, "offset": int | None, "limit": int | None}
output = {"content": str, "total_lines": int, "lines_returned": int}
```

**Write**
```python
input = {"file_path": str, "content": str}
output = {"message": str, "bytes_written": int, "file_path": str}
```

**Bash**
```python
input = {
    "command": str,
    "timeout": int | None,
    "description": str | None,
    "run_in_background": bool | None
}
output = {"output": str, "exitCode": int, "killed": bool | None}
```

**Grep**
```python
input = {
    "pattern": str,
    "path": str | None,
    "output_mode": "content" | "files_with_matches" | "count",
    "-i": bool | None,  # case insensitive
    "glob": str | None
}
output = {"matches": [...], "total_matches": int}
```

**Glob**
```python
input = {"pattern": str, "path": str | None}
output = {"matches": list[str], "count": int}
```

## Common Patterns for ExtractorPatternAgent

### Pattern Generation Flow

```python
async def generate_extraction_patterns(url: str):
    options = ClaudeAgentOptions(
        system_prompt="""You are a web scraping pattern generator.
        Analyze HTML and generate CSS/XPath selectors for product data.""",
        allowed_tools=[
            "mcp__browser__fetch",
            "mcp__parser__analyze",
            "Write"
        ],
        mcp_servers={
            "browser": browser_server,
            "parser": parser_server
        },
        permission_mode='acceptEdits'
    )

    async with ClaudeSDKClient(options) as agent:
        # Step 1: Fetch page
        await agent.query(f"Fetch HTML from {url}")
        async for msg in agent.receive_response():
            pass

        # Step 2: Analyze and generate patterns
        await agent.query("Generate extraction patterns for price, title, availability")
        async for msg in agent.receive_response():
            if isinstance(msg, ResultMessage):
                # Parse generated patterns
                patterns = extract_patterns(msg)

        # Step 3: Validate
        await agent.query(f"Validate patterns: {patterns}")
        async for msg in agent.receive_response():
            pass

        return patterns
```

### Structured Output with JSON Schema

```python
from claude_agent_sdk import OutputFormat

schema = {
    "type": "object",
    "properties": {
        "patterns": {
            "type": "object",
            "properties": {
                "price": {
                    "type": "object",
                    "properties": {
                        "selector": {"type": "string"},
                        "type": {"enum": ["css", "xpath"]},
                        "confidence": {"type": "number"}
                    },
                    "required": ["selector", "type", "confidence"]
                },
                "title": {"type": "object", "properties": {...}},
                "availability": {"type": "object", "properties": {...}}
            }
        }
    },
    "required": ["patterns"]
}

options = ClaudeAgentOptions(
    output_format={"type": "json_schema", "schema": schema},
    allowed_tools=["Read", "Write"]
)

async for message in query(
    prompt="Generate extraction patterns",
    options=options
):
    if isinstance(message, ResultMessage):
        # Result is guaranteed to match schema
        patterns = json.loads(message.result)
```

## Best Practices

1. **Use ClaudeSDKClient for multi-step workflows** - Maintains context
2. **Use query() for simple one-off tasks** - Simpler API
3. **Always use async context managers** - Proper cleanup
4. **Validate tool inputs/outputs** - Add error handling
5. **Set appropriate timeouts** - Prevent hanging
6. **Use structured outputs** - Enforce schema compliance
7. **Implement retry logic** - Handle transient failures
8. **Log tool usage** - Use hooks for observability
9. **Sandbox dangerous operations** - Use can_use_tool for safety
10. **Load project settings when needed** - Use setting_sources=["project"]

## Debugging

### Enable stderr logging

```python
def stderr_logger(line: str):
    print(f"[STDERR] {line}")

options = ClaudeAgentOptions(
    stderr=stderr_logger,
    allowed_tools=["Bash"]
)
```

### Track message flow

```python
async for message in client.receive_response():
    print(f"Message type: {type(message).__name__}")
    if hasattr(message, 'content'):
        print(f"Content blocks: {len(message.content)}")
```

## Resources

- Installation: `pip install claude-agent-sdk`
- Python SDK Guide: https://code.claude.com/docs/en/agent-sdk/python
- TypeScript SDK: https://code.claude.com/docs/en/agent-sdk/typescript
- CLI Reference: https://code.claude.com/docs/en/cli-reference
