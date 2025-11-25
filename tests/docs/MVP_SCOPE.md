# MVP Scope - Testing Framework

## MVP Requirements (Refined)

### Test Coverage
- **6 test prompts** - One per skill
- **3 runs per prompt** - For consistency validation
- **Total: 18 test executions** per full run

### Skills to Test

1. `origo-ai-platform:python` - Python scripting with UV
2. `origo-ai-platform:bedrock` - AWS Bedrock API usage
3. `origo-ai-platform:subagent` - Sub-agent creation
4. `origo-ai-platform:claude-hooks` - Hook configuration
5. `origo-iac-platform:ok-boilerplate-templates` - Infrastructure templates
6. `origo-designsystem:punkt-docs` - Design system documentation

### Execution Model

**Parallel with Progress Tracking**

```
Prompt 1: [=====>    ] Run 1/3 (45s)
Prompt 2: [====>     ] Run 1/3 (38s)
Prompt 3: [===>      ] Run 1/3 (31s)
Prompt 4: [======>   ] Run 2/3 (67s)
Prompt 5: [=>        ] Run 1/3 (12s)
Prompt 6: [=========>] Run 3/3 (102s) ✓

Overall Progress: 12/18 complete (66%)
```

Features:
- All 6 prompts run in parallel
- Real-time progress bars (Rich library)
- Live status updates per prompt
- ETA calculations
- Success/failure indicators

### Docker Strategy

**Base Image**: Use existing `.devcontainer/Dockerfile`

Advantages:
- ✅ Claude Code already installed
- ✅ UV (Python) already installed
- ✅ AWS CLI already installed
- ✅ jq, git, and essential tools included
- ✅ User 'node' with proper permissions
- ✅ .claude config directory ready

Modifications needed:
- ✅ Add tmux (not currently installed)
- ✅ Copy plugins directory
- ✅ Configure .claude/settings.json
- ✅ Mount transcript directory

### Success Criteria (MVP)

- [ ] 6 test prompts (one per skill) defined
- [ ] All 6 prompts run in parallel
- [ ] Real-time progress tracking visible
- [ ] Support agent handles 90%+ of questions
- [ ] 95%+ skill activation rate (at least 3/3 runs)
- [ ] Complete test run in < 5 minutes
- [ ] Detailed results report generated

### Out of Scope (MVP)

- ❌ Multiple prompts per skill (future: expand to 3-5 per skill)
- ❌ 5 runs per prompt (starting with 3)
- ❌ CI/CD integration (Phase 4)
- ❌ Historical trending
- ❌ LLM-powered support agent
- ❌ Web dashboard

## Prompt Definitions (MVP)

### 1. Python Skill
```yaml
name: python-uv-script
category: python
description: Validate Python skill with UV script creation
prompt: |
  Create a Python script that reads a JSON file and prints its contents.
  Use UV with PEP 723 headers. Name it "reader.py".
expected_skills:
  - origo-ai-platform:python
success_criteria:
  skill_activation_rate: 0.95
  file_created: "*.py"
  file_contains: ["#!/usr/bin/env python3", "# /// script"]
timeout_seconds: 120
runs: 3
support_agent:
  enabled: true
  strategy: "permissive"
```

### 2. Bedrock Skill
```yaml
name: bedrock-api-call
category: python
description: Validate Bedrock skill activation
prompt: |
  Create a Python script that uses AWS Bedrock to generate text.
  Use the Claude Sonnet 4.5 model in eu-central-1 region.
  Name it "bedrock-test.py".
expected_skills:
  - origo-ai-platform:bedrock
  - origo-ai-platform:python
success_criteria:
  skill_activation_rate: 0.95
  file_created: "*.py"
  file_contains: ["bedrock", "eu-central-1"]
timeout_seconds: 180
runs: 3
support_agent:
  enabled: true
```

### 3. Sub-Agent Skill
```yaml
name: create-subagent
category: subagent
description: Validate sub-agent creation skill
prompt: |
  Create a sub-agent specialized in code review.
  Name it "code-reviewer".
expected_skills:
  - origo-ai-platform:subagent
success_criteria:
  skill_activation_rate: 0.95
  file_created: ".claude/agents/*.md"
  file_contains: ["name: code-reviewer", "tools:"]
timeout_seconds: 120
runs: 3
support_agent:
  enabled: true
```

### 4. Claude Hooks Skill
```yaml
name: setup-bash-hook
category: hooks
description: Validate Claude hooks skill
prompt: |
  Set up a PreToolUse hook that logs all Bash commands to a file.
expected_skills:
  - origo-ai-platform:claude-hooks
success_criteria:
  skill_activation_rate: 0.95
  file_contains: ["PreToolUse", "Bash", "hooks"]
timeout_seconds: 120
runs: 3
support_agent:
  enabled: true
```

### 5. Infrastructure Templates Skill
```yaml
name: ok-template-info
category: iac
description: Validate ok-boilerplate-templates skill
prompt: |
  What templates are available for deploying a CloudFront static website?
  Show me the configuration steps.
expected_skills:
  - origo-iac-platform:ok-boilerplate-templates
success_criteria:
  skill_activation_rate: 0.95
  skill_docs_accessed: true
timeout_seconds: 90
runs: 3
support_agent:
  enabled: true
validation:
  response_contains:
    - "cloudfront-static-website"
    - "ok pkg add"
```

### 6. Punkt Design System Skill
```yaml
name: punkt-button-usage
category: design
description: Validate Punkt documentation skill
prompt: |
  Show me how to use the Punkt Button component.
  Include examples of different variants.
expected_skills:
  - origo-designsystem:punkt-docs
success_criteria:
  skill_activation_rate: 0.95
  skill_docs_accessed: true
timeout_seconds: 90
runs: 3
support_agent:
  enabled: true
validation:
  response_contains:
    - "Button"
    - "variant"
```

## Docker Configuration (MVP)

### Test Dockerfile
```dockerfile
# Use existing devcontainer as base
FROM .devcontainer:latest

# Add tmux (only missing dependency)
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
  tmux \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy plugins
COPY --chown=node:node plugins /home/node/.claude/plugins/marketplaces/origo/plugins

# Copy test Claude settings
COPY --chown=node:node tests/config/docker/.claude-settings.json /home/node/.claude/settings.json

USER node
WORKDIR /workspace
```

### Volume Mounts
```yaml
volumes:
  - ./plugins:/home/node/.claude/plugins/marketplaces/origo/plugins:ro
  - ./transcripts:/transcripts:rw
  - ./artifacts:/artifacts:rw
```

## Progress Tracking (MVP)

### Console Output
```
Plugin Testing Framework - MVP Run
===========================================

Running 6 prompts in parallel (3 runs each)...

┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━┓
┃ Prompt             ┃ Progress    ┃ Status ┃ Time   ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━┩
│ python-uv-script   │ ████████▌   │ 3/3 ✓  │ 2m 15s │
│ bedrock-api-call   │ ████████▌   │ 3/3 ✓  │ 2m 48s │
│ create-subagent    │ █████░░░░   │ 2/3 ⏳ │ 1m 42s │
│ setup-bash-hook    │ ████████▌   │ 3/3 ✓  │ 1m 58s │
│ ok-template-info   │ ████████░   │ 2/3 ⏳ │ 1m 23s │
│ punkt-button-usage │ ████░░░░░   │ 1/3 ⏳ │ 0m 51s │
└────────────────────┴─────────────┴────────┴────────┘

Overall: 14/18 runs complete (77.8%)
ETA: 1m 24s remaining
```

### Implementation Notes
- Use Rich library for progress bars
- Update every 2 seconds
- Show per-prompt and overall progress
- Live ETA calculation based on average times
- Color coding (green=pass, red=fail, yellow=running)

## Performance Targets (MVP)

- **Total execution time**: < 5 minutes for full run (6 prompts × 3 runs)
- **Container startup**: < 10 seconds per container
- **Support agent response**: < 1 second to detect and answer
- **Parallel execution**: 6 containers running simultaneously
- **Memory usage**: < 8GB total (6 containers × ~1.3GB each)

## Deliverables (MVP)

1. ✅ 6 prompt YAML files
2. ✅ Test Dockerfile based on .devcontainer
3. ✅ Orchestrator with parallel execution
4. ✅ Progress tracking UI (Rich)
5. ✅ Support agent (rule-based)
6. ✅ Transcript analyzer
7. ✅ Results reporter (console + JSON)

## Timeline Estimate (MVP)

**Total: 2-3 days focused work**

- Day 1 (6-8 hours):
  - Set up Docker environment
  - Implement orchestrator skeleton
  - Transcript monitor
  - Support agent (basic)

- Day 2 (6-8 hours):
  - tmux controller
  - Progress tracking UI
  - Transcript analyzer
  - Write 6 test prompts

- Day 3 (4-6 hours):
  - End-to-end testing
  - Bug fixes
  - Reporter
  - Documentation

## Next Steps

1. Review and approve this MVP scope
2. Begin implementation:
   - Start with Dockerfile
   - Then orchestrator + progress tracking
   - Then support agent
   - Finally integration and testing
