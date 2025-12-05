# Testing Framework - Usage Guide

## Quick Start

```bash
# From the project root directory
cd tests

# Run all tests (will build Docker image on first run)
uv run scripts/orchestrator.py
```

That's it! The orchestrator will:
1. Build the Docker test image (first run only)
2. Run all 6 test prompts in parallel
3. Execute 3 runs per prompt (18 total tests)
4. Auto-answer questions via support agent
5. Generate console, JSON, and Markdown reports

## Prerequisites

- **UV** - Python package manager (installed via .devcontainer)
- **Docker** - For isolated test environments
- **AWS Credentials** - For Bedrock API access (if testing Bedrock skill)

## Running Tests

### Run All Tests

```bash
# Run with defaults (3 runs per prompt)
uv run scripts/orchestrator.py

# Run with 1 run per prompt (for testing)
uv run scripts/orchestrator.py --runs 1

# Run with verbose debug output
uv run scripts/orchestrator.py --verbose

# Combine options
uv run scripts/orchestrator.py -v -r 1 -w 2
```

### Command Line Options

- `-v, --verbose` - Enable verbose debug output (shows container logs, detailed status)
- `-r, --runs N` - Override number of runs per prompt (default: from YAML files)
- `-w, --workers N` - Max parallel workers (default: 6)

### Force Rebuild Docker Image

```bash
# Delete the existing image first
docker rmi claude-plugin-test:latest

# Then run tests (will rebuild)
uv run scripts/orchestrator.py
```

### Test Individual Components

```bash
# Test transcript parser
uv run scripts/utils/transcript_parser.py <transcript.jsonl>

# Test support agent
uv run scripts/utils/support_agent.py

# Test analyzer
uv run scripts/analyzer.py <transcript.jsonl> <config.yml>

# Test reporter
uv run scripts/reporter.py
```

## Understanding Results

### Console Output

The orchestrator displays:
- Real-time progress bars for each test prompt
- Overall progress and ETA
- Detailed results table with:
  - Success rates per prompt
  - Skill activation rates
  - Pass/fail status
- Summary statistics

### Saved Reports

Reports are saved to `tests/results/reports/`:

- **JSON** (`results-<timestamp>.json`) - Machine-readable, for CI/CD
- **Markdown** (`results-<timestamp>.md`) - Human-readable, for GitHub
- **Transcripts** (`results/transcripts/`) - Full JSONL transcripts from each run
- **Artifacts** (`results/artifacts/`) - Files created during tests

### Success Criteria

A test prompt **passes** if:
- Skill activation rate ≥ 95% (configurable per prompt)
- All expected skills are activated
- No errors detected in transcript
- Validation criteria met (response contains expected text)

Overall framework **passes** if:
- 95%+ of test prompts pass

## Test Configuration

### Prompt YAML Format

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
  skill_activation_rate: 0.95  # Require 95% activation rate
  file_created: "*.py"
  file_contains: ["#!/usr/bin/env python3", "# /// script"]
timeout_seconds: 120
runs: 3
support_agent:
  enabled: true
  strategy: "permissive"
  custom_answers:  # Optional overrides
    "project name": "my-custom-name"
```

### Support Agent Configuration

The support agent automatically answers questions:

- **Names** - Generates random test names (e.g., "test-project-847")
- **Paths** - Provides reasonable paths ("./workspace", "./src")
- **Ports** - Random high ports (8000-9000)
- **Choices** - Selects first option
- **Booleans** - Defaults to "yes"

Override with `custom_answers` in prompt config.

## Troubleshooting

### Docker Build Fails

```bash
# Check Dockerfile syntax
docker build -f tests/config/docker/Dockerfile tests/config/docker/

# Ensure .devcontainer works first
# The test Dockerfile is based on it
```

### Tests Timeout

- Increase `timeout_seconds` in prompt YAML
- Check Docker resource limits (CPU/memory)
- Verify AWS credentials for Bedrock tests

### Skill Not Activating

- Check that plugins are properly mounted
- Verify `.claude-settings.json` enables the plugin
- Check transcript for errors: `cat tests/results/transcripts/<file>.jsonl`

### Support Agent Not Answering

- Check transcript monitor is detecting questions
- Verify tmux session is created properly
- Look for errors in console output

## Development

### Adding New Test Prompts

1. Create YAML file in appropriate category:
   ```bash
   vim tests/prompts/python/my-new-test.yml
   ```

2. Follow the format above

3. Run tests:
   ```bash
   uv run scripts/orchestrator.py
   ```

### Modifying Docker Environment

1. Edit `tests/config/docker/Dockerfile`

2. Rebuild:
   ```bash
   docker rmi claude-plugin-test:latest
   uv run scripts/orchestrator.py
   ```

### Debugging Individual Runs

```bash
# Keep container running for inspection
docker run -it --rm \
  -v $(pwd)/plugins:/home/node/.claude/plugins/marketplaces/origo:ro \
  -v $(pwd)/tests/results/transcripts:/transcripts:rw \
  claude-plugin-test:latest \
  /bin/bash

# Inside container, test Claude manually
tmux new -s test
claude
```

## Performance

**Expected Performance (MVP):**
- 6 prompts × 3 runs = 18 total tests
- Parallel execution (6 concurrent containers)
- Target: < 5 minutes total time
- Memory: ~8GB (6 containers × ~1.3GB each)

**Optimization:**
- Reduce `max_workers` if memory constrained
- Use faster storage for Docker volumes
- Pre-build image before running tests

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Test Plugins

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up UV
        run: curl -LsSf https://astral.sh/uv/install.sh | sh

      - name: Run tests
        run: |
          cd tests
          uv run scripts/orchestrator.py

      - name: Upload results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: test-results
          path: tests/results/reports/
```

## Architecture

```
Orchestrator
  ├── Load test prompts (YAML)
  ├── Build Docker image
  ├── Spawn containers (parallel)
  │   ├── Create tmux session
  │   ├── Start Claude Code
  │   ├── Monitor transcript
  │   │   └── Auto-answer questions
  │   └── Collect transcript
  ├── Analyze transcripts
  └── Generate reports
```

## Support

For issues or questions:
1. Check the documentation in `tests/docs/`
2. Review transcript files for errors
3. Open an issue on GitHub

## MVP Status

✅ All core components implemented:
- [x] 6 test prompts (1 per skill)
- [x] Docker environment with tmux
- [x] Parallel test execution
- [x] Real-time transcript monitoring
- [x] Autonomous support agent
- [x] Transcript analysis
- [x] Console, JSON, and Markdown reports

Next steps:
- Run end-to-end tests
- Fix any bugs discovered
- Optimize performance
- Add more test prompts (expand to 3-5 per skill)
