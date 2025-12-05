# Claude Code First-Run Wizard Solution

## Problem
Claude Code runs an interactive first-run wizard on initial startup that requires user interaction (theme selection, authentication). This blocked automated testing in Docker containers.

## Solution
Pre-populate the Claude Code configuration in the Docker image to skip the wizard entirely.

## Implementation

### Required Files

1. **`settings.json`** - Claude configuration with:
   - Environment variables (Bedrock settings, AWS region, etc.)
   - Plugin configuration
   - Permissions
   - Copied from `.claude/settings.json` into the Docker image

2. **`statsig/statsig.stable_id.*`** - Telemetry tracking file
   - Contains a UUID in JSON format: `"00000000-0000-0000-0000-000000000000"`
   - Suffix can be any numeric value (e.g., `statsig.stable_id.1234567890`)
   - Signals to Claude Code that initialization has completed

3. **Directory Structure** - The following directories must exist:
   - `.claude/debug/`
   - `.claude/plugins/marketplaces/origo/`
   - `.claude/projects/`
   - `.claude/shell-snapshots/`
   - `.claude/statsig/`
   - `.claude/todos/`

### Dockerfile Changes

```dockerfile
# Create Claude Code directory structure to skip first-run wizard
RUN mkdir -p /home/node/.claude/plugins/marketplaces/origo \
  /home/node/.claude/debug \
  /home/node/.claude/projects \
  /home/node/.claude/shell-snapshots \
  /home/node/.claude/statsig \
  /home/node/.claude/todos

# Copy Claude settings.json into the image
COPY --chown=node:node settings.json /home/node/.claude/settings.json

# Create statsig stable_id file to skip first-run wizard
RUN echo '"00000000-0000-0000-0000-000000000000"' > /home/node/.claude/statsig/statsig.stable_id.1234567890 && \
  chown -R node:node /home/node/.claude
```

### Orchestrator Changes

1. **Removed first-run wizard handling code** (`orchestrator.py:188-202`)
   - Removed `tmux.send_enter()` calls that tried to navigate the wizard
   - Simplified to just wait 5 seconds for Claude to be ready

2. **Removed settings.json volume mount**
   - Removed `claude_settings_path` from `ContainerConfig`
   - Removed settings.json from volume mounts in `docker_manager.py`
   - Settings are now baked into the Docker image

## Testing

Verify the solution works:

```bash
# Test non-interactive mode
docker run --rm \
  -v $(pwd)/plugins:/home/node/.claude/plugins/marketplaces/origo:ro \
  --env-file .devcontainer/devcontainer.env \
  claude-plugin-test:latest \
  claude -p "What is 2+2?"

# Expected: Direct response without wizard
# Output: "2 + 2 = 4"
```

## Benefits

1. **No Manual Intervention** - Tests run fully autonomously
2. **Faster Startup** - No wizard navigation delays
3. **Reliability** - No timing-dependent tmux key sending
4. **Simplicity** - Fewer moving parts in the test orchestrator

## Notes

- The `settings.json` file must be kept in sync with the project's `.claude/settings.json`
- If Claude Code's initialization logic changes, this solution may need updates
- The statsig file suffix doesn't need to match any specific pattern, just needs to exist
