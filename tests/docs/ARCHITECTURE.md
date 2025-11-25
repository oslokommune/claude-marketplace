# Testing Framework Architecture

## System Overview

**Architecture**: Docker + tmux + Python Orchestrator with Autonomous Support Agent

Python orchestrator spawns isolated Docker containers, uses tmux to manage Claude Code sessions, monitors transcripts in real-time to auto-answer questions, and collects data for analysis.

## High-Level Architecture

```
┌───────────────────────────────────────────────────────────────┐
│                  Test Orchestrator (Python)                    │
│  - Load test prompts                                           │
│  - Spawn Docker containers (parallel)                          │
│  - Monitor transcripts (background threads)                    │
│  - Manage test execution & timeout handling                    │
│  - Collect and analyze results                                 │
└──────────────────┬───────────────────────────────────────────┘
                   │
      ┌────────────┴────────────────┐
      │                             │
┌─────▼──────┐               ┌─────▼──────┐    ... (parallel)
│  Docker 1  │               │  Docker 2  │
│            │               │            │
│  ┌──────┐  │               │  ┌──────┐  │
│  │ tmux │  │               │  │ tmux │  │
│  │      │  │               │  │      │  │
│  │Claude│◄─┼──Auto-answer  │  │Claude│  │
│  │ Code │  │   via tmux    │  │ Code │  │
│  └──┬───┘  │   send-keys   │  └──┬───┘  │
│     │      │               │     │      │
│  Transcript│               │  Transcript│
│     │      │               │     │      │
└─────┼──────┘               └─────┼──────┘
      │                            │
      │  (watched by monitor)      │
      │                            │
      └────────────┬───────────────┘
                   │
    ┌──────────────▼──────────────────┐
    │  Transcript Monitor & Support   │
    │                                  │
    │  ┌────────────────────────────┐ │
    │  │ Question Detector          │ │
    │  │ - Watch for AskUserQuestion│ │
    │  │ - Parse question type      │ │
    │  └────────┬───────────────────┘ │
    │           │                      │
    │  ┌────────▼───────────────────┐ │
    │  │ Support Agent              │ │
    │  │ - Generate names/paths     │ │
    │  │ - Select default options   │ │
    │  │ - Provide reasonable values│ │
    │  └────────┬───────────────────┘ │
    │           │                      │
    │  ┌────────▼───────────────────┐ │
    │  │ Answer Injector            │ │
    │  │ - tmux send-keys in Docker │ │
    │  └────────────────────────────┘ │
    └──────────────┬───────────────────┘
                   │
         ┌─────────▼──────────┐
         │  Transcript        │
         │  Analyzer (Python) │
         │  - Parse JSONL     │
         │  - Detect skills   │
         │  - Generate report │
         └────────────────────┘
```

## Why This Architecture?

**Complete Isolation**: Each test runs in a fresh Docker container
**Autonomous Execution**: Support agent prevents tests from hanging on questions
**Parallel Testing**: Multiple containers run simultaneously
**Production-Like**: Matches real Claude Code usage patterns
**Observable**: Full transcript capture and analysis

### Core Components

#### 1. Test Orchestrator (`scripts/orchestrator.py`)
```python
# Main responsibilities:
- Load test definitions from YAML
- Create Docker containers with proper configuration
- Start transcript monitoring threads
- Execute prompts via tmux automation
- Coordinate support agent for autonomous operation
- Handle timeouts and cleanup
- Collect transcripts and metadata
- Trigger analysis pipeline
```

#### 2. Transcript Monitor (`scripts/utils/transcript_monitor.py`)
```python
# Responsibilities:
- Watch transcript file in real-time (background thread)
- Detect new JSONL lines as they're written
- Parse for AskUserQuestion tool usage
- Trigger support agent when questions detected
- Log all question/answer interactions
```

#### 3. Support Agent (`scripts/utils/support_agent.py`)
```python
# Responsibilities:
- Classify question type (name, path, port, choice, boolean)
- Generate contextually appropriate answers:
  * Random names: "test-project-847"
  * Reasonable paths: "./workspace", "./src"
  * Port numbers: 8000-9000
  * Default choices: select first option
  * Boolean: default to "yes"
- Support configurable overrides per test
- Log decisions for debugging
```

#### 4. Answer Injector (`scripts/utils/tmux_controller.py`)
```python
# Responsibilities:
- Execute tmux commands in Docker containers
- Send answers via tmux send-keys
- Handle special characters and escaping
- Wait for prompts to appear
- Confirm answer acceptance
```

#### 5. Docker Environment (`config/docker/`)
```dockerfile
# Key features:
- Base: Ubuntu 24.04 + Claude Code CLI
- Pre-installed plugins from ./plugins
- Configured AWS credentials (test account)
- Pre-configured .claude/settings.json
- tmux for session management
- Volume mounts for transcript access
```

#### 6. Prompt Library (`prompts/`)
```
prompts/
├── python/
│   ├── create-bedrock-script.yml
│   ├── use-uv-tool.yml
│   └── metadata.json
├── iac/
│   ├── deploy-cloudfront.yml
│   ├── setup-app-template.yml
│   └── metadata.json
└── design/
    ├── use-punkt-button.yml
    ├── implement-form.yml
    └── metadata.json
```

**Prompt Definition Format:**
```yaml
name: create-bedrock-script
category: python
description: Test that Claude creates a Python script using Bedrock API
prompt: |
  Create a Python script that uses AWS Bedrock to summarize text.
  Use the Bedrock skill and follow best practices.
expected_skills:
  - origo-ai-platform:python
  - origo-ai-platform:bedrock
expected_tools:
  - Write
  - Bash
success_criteria:
  skill_activation_rate: 0.95
  tool_usage: ["Write"]
  file_created: "*.py"
  file_contains: ["#!/usr/bin/env python3", "bedrock"]
timeout_seconds: 120
runs: 5
support_agent:
  enabled: true  # Auto-answer questions
  strategy: "permissive"  # Always provide reasonable defaults
  custom_answers:  # Optional overrides
    "project name": "test-bedrock-script"
    "port": "8080"
```

#### 7. Transcript Analyzer (`scripts/analyzer.py`)
```python
# Capabilities:
- Parse Claude Code JSONL transcripts
- Detect skill activations
- Track tool usage patterns
- Measure response times
- Extract file operations
- Statistical analysis across runs
```

#### 8. Reporter (`scripts/reporter.py`)
```python
# Output formats:
- Console summary (pass/fail, Rich formatted)
- JSON results (for CI/CD integration)
- Markdown report (GitHub PR comments)
- Detailed failure analysis
- Support agent interaction logs
```

### Data Flow

1. **Setup Phase**
   - Orchestrator reads prompt definitions
   - Validates Docker environment
   - Prepares test matrix
   - Initializes support agent configuration

2. **Execution Phase**
   - For each prompt (can run in parallel):
     - Spawn Docker container with volume mounts
     - Launch tmux session with Claude Code
     - Start transcript monitor thread
     - Send prompt to Claude Code
     - **Monitor Loop** (concurrent):
       - Watch transcript for new lines
       - Detect AskUserQuestion events
       - Generate appropriate answers via support agent
       - Inject answers via tmux send-keys
       - Continue until completion or timeout
     - Collect final transcript
     - Tear down container
   - Repeat N times per prompt for statistical validation

3. **Analysis Phase**
   - Parse all transcripts
   - Extract metrics:
     - Skill activation count
     - Tool usage frequency
     - Support agent interactions
     - Success/failure detection
     - Response time statistics
   - Compare against expected criteria
   - Calculate statistical measures

4. **Reporting Phase**
   - Generate pass/fail summary
   - Identify flaky tests
   - Report support agent activity
   - Create detailed reports
   - Store results for trending

### File Structure

```
tests/
├── docs/
│   ├── PROJECT_PLAN.md           # Goals, scope, roadmap
│   ├── ARCHITECTURE.md            # This file - system design
│   ├── PROMPTS.md                 # Prompt design patterns
│   ├── ANALYSIS.md                # Transcript analysis details
│   ├── SUPPORT_AGENT.md           # Support agent implementation
│   └── DEVELOPMENT.md             # Implementation guide
├── prompts/
│   ├── python/                    # Python skill tests
│   ├── iac/                       # Infrastructure tests
│   ├── design/                    # Design system tests
│   ├── subagent/                  # Sub-agent tests
│   └── schemas/
│       └── prompt.schema.json
├── scripts/
│   ├── orchestrator.py            # Main test runner
│   ├── analyzer.py                # Transcript analyzer
│   ├── reporter.py                # Results formatter
│   └── utils/
│       ├── docker_manager.py      # Docker container management
│       ├── tmux_controller.py     # tmux automation & answer injection
│       ├── transcript_monitor.py  # Real-time transcript watching
│       ├── support_agent.py       # Question answering logic
│       └── transcript_parser.py   # JSONL parsing
├── config/
│   ├── test_config.yml            # Test execution settings
│   └── docker/
│       ├── Dockerfile             # Test environment image
│       └── .claude-settings.json  # Claude Code configuration
├── results/
│   ├── transcripts/               # Collected JSONL files
│   ├── reports/                   # Generated reports
│   └── artifacts/                 # Created files from tests
├── .github/
│   └── workflows/
│       └── test-plugins.yml       # CI/CD pipeline
└── README.md                      # Main documentation
```

## Key Design Decisions

### 1. Docker Container Strategy
- **One-shot containers**: Each test run gets fresh container for clean state
- **Volume mounts**: Plugin directory (read-only), transcript directory (read-write)
- **Network isolation**: Prevents external dependencies
- **Resource limits**: CPU/memory constraints for consistency

### 2. Autonomous Support Agent
- **Real-time monitoring**: Watch transcripts as they're written (500ms polling)
- **Rule-based answering**: Pattern matching for common question types
- **Reasonable defaults**: Generate names, paths, ports that make sense
- **Configurable**: Override answers per test when needed
- **Observable**: Log all questions and generated answers

### 3. Concurrency Model
- **Parallel prompts**: Multiple Docker containers run simultaneously
- **Sequential runs**: Multiple runs of same prompt in series (for statistics)
- **Background monitoring**: Each container has dedicated monitor thread
- **Configurable workers**: Adjust parallelism based on resources

### 4. Transcript Analysis
- **JSONL parsing**: Native Claude Code transcript format
- **Event detection**: Skill activations, tool usage, questions asked
- **Fuzzy matching**: Account for slight variations
- **Statistical validation**: Require N/M runs to pass (typically 95%)

### 5. Error Handling
- **Timeout detection**: Kill runaway sessions
- **Question detection timeout**: Max 5 minutes waiting for answer
- **Retry logic**: Re-run failed tests once
- **Graceful degradation**: Partial results still useful
- **Detailed logging**: Debug failures and support agent decisions

## Technology Choices

### Python + UV
- Fast dependency management
- Self-contained scripts
- Easy CI/CD integration

### tmux
- Session automation
- Screen scraping (if needed)
- Log capture
- Well-tested for CLI apps

### Docker
- Reproducible environments
- Parallel execution
- Resource isolation
- CI/CD standard

### YAML for Prompts
- Human-readable
- Easy to version control
- Schema validation
- Extensible

## Implementation Roadmap

### Phase 1: Foundation ✅
- [x] Document architecture
- [x] Design support agent approach
- [x] Define prompt structure
- [x] Plan transcript analysis
- [x] Define MVP scope

### Phase 2: MVP Implementation (Next)
**Scope**: 6 prompts (1 per skill), 3 runs each, parallel execution

- [ ] Build Docker environment (based on .devcontainer)
- [ ] Implement orchestrator with parallel execution
- [ ] Add progress tracking UI (Rich library)
- [ ] Create transcript monitor
- [ ] Build support agent (rule-based)
- [ ] Implement tmux controller
- [ ] Write 6 test prompts
- [ ] Create basic analyzer
- [ ] Build reporter (console + JSON)

**Target**: < 5 minutes total execution, < 3 days implementation

### Phase 3: Expansion (Future)
- [ ] Expand to 3-5 prompts per skill (18-30 total)
- [ ] Increase runs to 5 per prompt
- [ ] Add statistical analysis
- [ ] Performance optimization

### Phase 4: Production (Future)
- [ ] Add CI/CD pipeline
- [ ] Historical trending
- [ ] Advanced reporting
- [ ] Documentation and examples

## Critical Success Factors

1. **Support Agent Reliability**: Must handle 90%+ of questions autonomously
2. **Skill Activation Detection**: Accurate parsing of transcript events
3. **Docker Performance**: Container startup/cleanup must be efficient
4. **Statistical Validation**: Multiple runs must provide meaningful confidence
5. **Maintainability**: Easy to add new test prompts and categories
