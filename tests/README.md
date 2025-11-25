# Plugin Testing Framework

Autonomous testing framework for validating Claude Code plugin consistency and reliability.

## Overview

This testing framework validates that Claude Code plugins activate correctly and consistently when given specific prompts. It uses Docker for isolation, tmux for session management, an autonomous support agent to handle questions, and Python for orchestration and analysis.

**Key Innovation**: Built-in support agent automatically answers questions during test execution, enabling fully autonomous testing.

## Project Status

**Current Phase**: Architecture & Planning ✅
**Next Phase**: MVP Implementation
**MVP Scope**: 6 prompts (1 per skill), 3 runs each, parallel execution

## Quick Links

### Planning Documents
- [MVP Scope](docs/MVP_SCOPE.md) - **START HERE** - Refined requirements and deliverables
- [Project Plan](docs/PROJECT_PLAN.md) - Overall goals and roadmap
- [Architecture](docs/ARCHITECTURE.md) - System design and components

### Technical Details
- [Support Agent](docs/SUPPORT_AGENT.md) - Autonomous question handling
- [Prompts](docs/PROMPTS.md) - Test prompt structure and examples
- [Analysis](docs/ANALYSIS.md) - Transcript parsing and validation
- [Development](docs/DEVELOPMENT.md) - Implementation guide

## Directory Structure

```
tests/
├── docs/                          # Architecture and planning documents
│   ├── PROJECT_PLAN.md
│   ├── ARCHITECTURE.md
│   ├── SUPPORT_AGENT.md
│   ├── PROMPTS.md
│   ├── ANALYSIS.md
│   └── DEVELOPMENT.md
├── prompts/                       # Test prompt definitions (TODO)
│   ├── python/
│   ├── iac/
│   ├── design/
│   └── subagent/
├── scripts/                       # Implementation (TODO)
│   ├── orchestrator.py
│   ├── analyzer.py
│   ├── reporter.py
│   └── utils/
│       ├── transcript_monitor.py
│       ├── support_agent.py
│       ├── tmux_controller.py
│       └── docker_manager.py
├── config/                        # Configuration files (TODO)
│   └── docker/
│       ├── Dockerfile
│       └── .claude-settings.json
├── results/                       # Test outputs (TODO)
│   ├── transcripts/
│   ├── reports/
│   └── artifacts/
└── README.md                      # This file
```

## Goals

1. **Autonomous Testing**: Run tests without human intervention using support agent
2. **Consistency Validation**: Verify plugins activate reliably (95%+ rate)
3. **Regression Detection**: Catch breaking changes early
4. **Documentation**: Generate usage examples
5. **CI/CD Integration**: Automate in development workflow

## Architecture Summary

**Docker + tmux + Python Orchestrator + Support Agent**

```
Python Orchestrator
    ↓
Docker Containers (parallel) + Transcript Monitors
    ↓
tmux Sessions → Claude Code ← Auto-answered questions
    ↓
Transcript Collection + Support Agent Logs
    ↓
Analysis & Reporting
```

**Key Innovation**: Support agent monitors transcripts in real-time and automatically answers questions (names, paths, choices) so tests run fully autonomously.

## Test Coverage (MVP)

### 6 Skills, 1 Prompt Each

1. **Python Skill** (`origo-ai-platform:python`)
   - UV script creation with PEP 723

2. **Bedrock Skill** (`origo-ai-platform:bedrock`)
   - AWS Bedrock API integration

3. **Sub-Agent Skill** (`origo-ai-platform:subagent`)
   - Custom agent creation

4. **Hooks Skill** (`origo-ai-platform:claude-hooks`)
   - PreToolUse hook configuration

5. **Infrastructure Skill** (`origo-iac-platform:ok-boilerplate-templates`)
   - CloudFront template information

6. **Design System Skill** (`origo-designsystem:punkt-docs`)
   - Punkt Button component usage

**MVP Target**: 6 prompts × 3 runs = 18 test executions per full run
**Future**: Expand to 3-5 prompts per skill (18-30 total prompts)

## Key Components

### 1. Test Orchestrator
- Spawns Docker containers
- Manages parallel test execution
- Coordinates support agent
- Collects transcripts

### 2. Support Agent System
- **Transcript Monitor**: Watches for questions in real-time
- **Answer Generator**: Creates reasonable defaults (names, paths, ports)
- **Answer Injector**: Sends responses via tmux

### 3. Prompt Library
- YAML-based test definitions
- Expected behaviors and success criteria
- Support agent configuration per test

### 4. Transcript Analyzer
- Parses JSONL transcripts
- Detects skill activations and tool usage
- Tracks support agent interactions
- Statistical analysis across runs

### 5. Reporter
- Console summary (Rich formatted)
- JSON for CI/CD
- Markdown reports
- Failure analysis with support agent logs

## Technology Stack

- **Docker**: Isolated test environments
- **tmux**: Session management
- **Python 3.12+**: Orchestration (UV managed)
- **YAML**: Test definitions
- **JSONL**: Transcript format
- **GitHub Actions**: CI/CD

## Development Phases

### Phase 1: Foundation ✅ (Complete)
- [x] Define architecture
- [x] Design support agent approach
- [x] Design test prompt structure
- [x] Plan transcript analysis
- [x] Define MVP scope

### Phase 2: MVP Implementation (Next - 2-3 days)
**Goal**: 6 prompts, 3 runs each, parallel execution, < 5 min total

- [ ] Docker environment (based on .devcontainer)
- [ ] Orchestrator + parallel execution
- [ ] Progress tracking UI (Rich library)
- [ ] Transcript monitor (real-time)
- [ ] Support agent (rule-based)
- [ ] tmux controller + answer injection
- [ ] Write 6 test prompts (1 per skill)
- [ ] Transcript analyzer
- [ ] Reporter (console + JSON)
- [ ] End-to-end testing

### Phase 3: Expansion (Future)
- [ ] Expand to 3-5 prompts per skill
- [ ] Increase to 5 runs per prompt
- [ ] Advanced analysis

### Phase 4: Production (Future)
- [ ] CI/CD pipeline
- [ ] Historical trending
- [ ] Performance optimization

## Getting Started (Future)

Once implemented, running tests will be:

```bash
# Run all tests
uv run tests/orchestrator.py

# Run specific category
uv run tests/orchestrator.py --category python

# Run single test
uv run tests/orchestrator.py --test create-uv-python-script

# Generate report
uv run tests/reporter.py --results results/latest.json
```

## Success Criteria

- ✅ Documented architecture with support agent
- ⏳ Working Docker environment
- ⏳ Functional orchestrator with monitoring
- ⏳ Autonomous support agent (90%+ success rate)
- ⏳ 18+ test prompts
- ⏳ 95%+ skill activation rate
- ⏳ CI/CD pipeline active
- ⏳ Automated reporting with support agent logs

## Contributing

When adding new test prompts:

1. Follow YAML schema in [docs/PROMPTS.md](docs/PROMPTS.md)
2. Place in appropriate category directory
3. Test locally before committing
4. Update documentation

## Design Decisions

### Why Docker?
- Complete isolation per test
- Reproducible environments
- Parallel execution enabled
- CI/CD standard

### Why Support Agent?
- **Critical for autonomy**: Tests hang without it
- Enables realistic testing of question flows
- Reduces test brittleness
- 90%+ automation rate expected

### Why tmux?
- Session automation
- Easy answer injection via send-keys
- Well-tested for CLI apps
- Container-compatible

### Why Python + UV?
- Fast dependency management
- Self-contained scripts
- Rich ecosystem (Rich, Docker SDK)
- Easy CI/CD integration

### Why Multiple Runs?
- AI is non-deterministic
- Statistical validation (95% threshold)
- Catch flaky tests
- Build confidence in consistency

## Known Limitations

1. **AI Variability**: Responses may differ run-to-run
2. **Timing Sensitive**: Network/API delays affect results
3. **Docker Overhead**: Slower than native execution
4. **Resource Intensive**: Multiple containers need resources

## Mitigation Strategies

- Focus on skill activation, not exact output
- Use statistical thresholds (95% not 100%)
- Implement retry logic
- Configurable parallelism
- Timeout handling

## Future Enhancements

- Performance benchmarking
- Cost tracking
- Web dashboard
- Historical trending
- ML-based failure prediction
- Auto-prompt generation

## Questions?

See [docs/](docs/) for detailed documentation or open an issue.
