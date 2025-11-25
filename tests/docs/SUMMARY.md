# Testing Framework - Architecture Summary

## Chosen Architecture

**Docker + tmux + Python Orchestrator + Autonomous Support Agent**

This is the only architecture we're implementing. Alternative approaches have been removed from documentation.

## Core Innovation: Support Agent

The support agent is a **critical component** that enables fully autonomous testing by automatically answering questions that Claude Code asks during test execution.

### How It Works

```
1. Test starts → Claude Code runs in Docker + tmux
2. Transcript Monitor watches for AskUserQuestion events (real-time)
3. Support Agent generates appropriate answers:
   - Names: "test-project-847"
   - Paths: "./workspace", "./src"
   - Ports: 8000-9000
   - Choices: select first option
   - Boolean: default to "yes"
4. Answer Injector sends response via tmux send-keys
5. Claude continues without hanging
```

### Why This Matters

Without the support agent, tests would **hang indefinitely** when Claude asks clarifying questions like:
- "What should I name this project?"
- "Which port should the server run on?"
- "What directory should I create this in?"

With the support agent, tests run **completely unattended** at any time, including in CI/CD.

## System Components

### 1. Test Orchestrator (`scripts/orchestrator.py`)
- Loads YAML test definitions
- Spawns isolated Docker containers (parallel)
- Starts transcript monitoring threads
- Coordinates support agent
- Collects results

### 2. Transcript Monitor (`scripts/utils/transcript_monitor.py`)
- Watches transcript JSONL file in real-time (500ms polling)
- Detects AskUserQuestion tool usage
- Triggers support agent

### 3. Support Agent (`scripts/utils/support_agent.py`)
- Rule-based question classification
- Generates contextually appropriate answers
- Supports custom overrides per test
- Logs all decisions

### 4. Answer Injector (`scripts/utils/tmux_controller.py`)
- Executes tmux send-keys in Docker containers
- Handles special characters and escaping
- Confirms answer acceptance

### 5. Docker Environment (`config/docker/`)
- Ubuntu 24.04 + Claude Code CLI
- Pre-loaded plugins
- Volume mounts for transcript access
- Clean state per test

### 6. Transcript Analyzer (`scripts/analyzer.py`)
- Parses JSONL transcripts
- Detects skill activations
- Tracks tool usage
- Records support agent interactions
- Statistical analysis

### 7. Reporter (`scripts/reporter.py`)
- Console output (Rich formatted)
- JSON results (CI/CD)
- Markdown reports (GitHub PRs)
- Support agent logs

## Test Prompt Structure

```yaml
name: create-bedrock-script
category: python
description: Test Bedrock skill activation
prompt: |
  Create a Python script using AWS Bedrock...
expected_skills:
  - origo-ai-platform:python
  - origo-ai-platform:bedrock
success_criteria:
  skill_activation_rate: 0.95
timeout_seconds: 120
runs: 5
support_agent:
  enabled: true
  strategy: "permissive"
  custom_answers:
    "project name": "test-script"
```

## Data Flow

1. **Setup**: Load prompts, validate Docker
2. **Execution**:
   - Spawn container
   - Start monitoring
   - Send prompt
   - Auto-answer questions (loop)
   - Collect transcript
3. **Analysis**: Parse, detect skills, compare to expectations
4. **Report**: Generate results

## Success Metrics

- **Support Agent**: 90%+ question handling rate
- **Skill Activation**: 95%+ across 5 runs
- **Coverage**: 18-42 test prompts
- **Autonomy**: Zero human intervention required

## MVP Scope

**6 prompts** (1 per skill) × **3 runs** = **18 test executions**
**Parallel execution** with **real-time progress tracking**
**Target**: < 5 minutes total execution time

### Implementation Status

**Phase 1: Foundation** ✅ (Complete)
- [x] Define architecture
- [x] Design support agent
- [x] Define MVP scope
- [x] Document approach

**Phase 2: MVP Implementation** (Next - 2-3 days)
- [ ] Docker environment (based on .devcontainer)
- [ ] Orchestrator with parallel execution
- [ ] Progress tracking UI (Rich library)
- [ ] Transcript monitor (real-time)
- [ ] Support agent (rule-based)
- [ ] tmux controller + answer injection
- [ ] Write 6 test prompts
- [ ] Transcript analyzer
- [ ] Reporter (console + JSON)
- [ ] End-to-end testing

**Phase 3: Expansion** (Future)
- [ ] Expand to 3-5 prompts per skill (18-30 total)
- [ ] Increase to 5 runs per prompt
- [ ] Advanced statistical analysis

**Phase 4: Production** (Future)
- [ ] CI/CD pipeline
- [ ] Historical trending
- [ ] Performance optimization

## Key Files

### Start Here
- `MVP_QUICK_REFERENCE.md` - **Quick start** - At-a-glance MVP summary
- `MVP_SCOPE.md` - **Detailed MVP requirements** and 6 test prompts

### Architecture
- `ARCHITECTURE.md` - Detailed system design
- `SUPPORT_AGENT.md` - Support agent implementation
- `SUMMARY.md` - This file - architecture overview

### Reference
- `PROMPTS.md` - Test prompt patterns and best practices
- `ANALYSIS.md` - Transcript parsing details
- `DEVELOPMENT.md` - Implementation guide
- `PROJECT_PLAN.md` - Goals and roadmap

## Documentation Status

✅ All documentation reflects the chosen architecture (Docker + tmux + Support Agent)
✅ MVP scope defined: 6 prompts, 3 runs each, parallel execution
✅ Based on existing .devcontainer/Dockerfile
✅ Target: < 5 minutes total, 2-3 days implementation
