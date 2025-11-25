# MVP Quick Reference

## At a Glance

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Plugin Testing Framework - MVP              ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ Prompts:      6 (1 per skill)               ┃
┃ Runs:         3 per prompt                  ┃
┃ Total Execs:  18 test runs                  ┃
┃ Execution:    Parallel with progress bars   ┃
┃ Time Target:  < 5 minutes                   ┃
┃ Docker Base:  .devcontainer/Dockerfile      ┃
┃ Key Feature:  Autonomous support agent      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## 6 Test Prompts

| # | Skill | Test Name | What It Tests |
|---|-------|-----------|---------------|
| 1 | `python` | python-uv-script | UV script with PEP 723 |
| 2 | `bedrock` | bedrock-api-call | AWS Bedrock integration |
| 3 | `subagent` | create-subagent | Custom agent creation |
| 4 | `claude-hooks` | setup-bash-hook | PreToolUse hook config |
| 5 | `ok-boilerplate` | ok-template-info | CloudFront template docs |
| 6 | `punkt-docs` | punkt-button-usage | Button component usage |

## System Architecture

```
Orchestrator (Python + UV)
    ↓
6 Docker Containers (parallel)
    ↓
Each Container:
  - tmux session with Claude Code
  - Transcript monitor (background thread)
  - Support agent (auto-answers questions)
    ↓
Collect 18 transcripts
    ↓
Analyze & Report
```

## Docker Setup

**Base**: Existing `.devcontainer/Dockerfile`

**Already includes**:
- ✅ Claude Code installed
- ✅ UV (Python package manager)
- ✅ AWS CLI
- ✅ jq, git, essential tools
- ✅ User 'node' configured
- ✅ .claude directory ready

**Need to add**:
- ➕ tmux (for session management)
- ➕ Copy plugins directory
- ➕ Configure .claude/settings.json

## Progress Tracking

Real-time console output with Rich library:

```
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

Overall: 14/18 complete (77.8%)
ETA: 1m 24s remaining
```

## Success Criteria

- [ ] All 6 prompts execute successfully
- [ ] Support agent handles 90%+ of questions
- [ ] 95%+ skill activation rate (3/3 runs pass)
- [ ] Total execution time < 5 minutes
- [ ] Parallel execution works smoothly
- [ ] Progress tracking is accurate and live
- [ ] Results report is clear and actionable

## Key Components (Implementation Order)

1. **Docker Environment** (4h)
   - Extend .devcontainer/Dockerfile
   - Add tmux
   - Configure settings

2. **Orchestrator** (6h)
   - Load YAML prompts
   - Spawn 6 containers in parallel
   - Coordinate execution

3. **Progress Tracking** (3h)
   - Rich library integration
   - Live updates
   - ETA calculations

4. **Transcript Monitor** (3h)
   - Watch JSONL files
   - Detect questions
   - Trigger support agent

5. **Support Agent** (4h)
   - Question classifier
   - Answer generator
   - Decision logging

6. **tmux Controller** (3h)
   - Execute tmux commands in Docker
   - Send answers via send-keys
   - Handle escaping

7. **Test Prompts** (2h)
   - Write 6 YAML files
   - Define success criteria
   - Configure support agent

8. **Analyzer** (4h)
   - Parse transcripts
   - Detect skills
   - Track support agent activity

9. **Reporter** (3h)
   - Console summary
   - JSON output
   - Pass/fail logic

10. **Integration** (4h)
    - End-to-end testing
    - Bug fixes
    - Performance tuning

**Total**: ~36 hours (2-3 days)

## Command Line Usage

```bash
# Run all tests (MVP - 6 prompts, 3 runs each)
uv run tests/orchestrator.py

# Run specific test
uv run tests/orchestrator.py --test python-uv-script

# Generate report from results
uv run tests/reporter.py --results results/latest.json

# Debug mode (verbose logging)
uv run tests/orchestrator.py --debug
```

## File Locations

```
tests/
├── prompts/
│   ├── python-uv-script.yml
│   ├── bedrock-api-call.yml
│   ├── create-subagent.yml
│   ├── setup-bash-hook.yml
│   ├── ok-template-info.yml
│   └── punkt-button-usage.yml
├── scripts/
│   ├── orchestrator.py          # Main entry point
│   ├── analyzer.py
│   ├── reporter.py
│   └── utils/
│       ├── transcript_monitor.py
│       ├── support_agent.py
│       ├── tmux_controller.py
│       └── docker_manager.py
├── config/
│   └── docker/
│       ├── Dockerfile
│       └── .claude-settings.json
└── results/
    ├── transcripts/
    ├── reports/
    └── artifacts/
```

## Next Steps

1. ✅ Review and approve this MVP scope
2. ⏳ Begin implementation (Day 1):
   - Docker environment
   - Orchestrator skeleton
   - Progress tracking
3. ⏳ Continue (Day 2):
   - Support agent
   - tmux controller
   - Test prompts
4. ⏳ Finalize (Day 3):
   - Analyzer
   - Reporter
   - End-to-end testing

## Expansion Plan (Post-MVP)

After MVP proves the concept:
- Add 2-4 more prompts per skill (total: 18-30)
- Increase runs from 3 to 5
- Add statistical analysis (variance, flakiness detection)
- Implement CI/CD pipeline
- Add historical trending
