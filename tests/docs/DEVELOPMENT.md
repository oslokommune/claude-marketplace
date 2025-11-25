# Development Guide

## Implementation Roadmap

### Phase 2: Core Framework Implementation

#### Step 1: Docker Environment Setup

**Files to Create:**
- `tests/config/docker/Dockerfile`
- `tests/config/docker/.claude-settings.json`
- `tests/config/docker/docker-compose.yml`

**Dockerfile Considerations:**

```dockerfile
# Base image considerations:
# - Ubuntu 22.04 or 24.04
# - Pre-install Claude Code CLI
# - Install tmux, jq, git
# - Copy plugins from host

FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    tmux \
    jq \
    git \
    python3.12 \
    && rm -rf /var/lib/apt/lists/*

# Install Claude Code CLI
# (exact method TBD - may need official installer)

# Set up Claude Code environment
WORKDIR /workspace
COPY config/docker/.claude-settings.json /root/.claude/settings.json

# Copy plugins
COPY ../plugins /root/.claude/plugins/marketplaces/origo/plugins

# Entry point for test execution
ENTRYPOINT ["tmux"]
```

**Key Decisions:**
- Mount plugins as read-only volumes
- Use environment variables for AWS credentials (mock or test account)
- Configure Claude Code to use local plugins
- Set up logging/transcript collection

#### Step 2: Python Orchestrator

**File**: `tests/scripts/orchestrator.py`

**Core Functionality:**

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pyyaml",
#     "docker",
#     "click",
#     "rich",
# ]
# ///

import click
from rich.console import Console
from rich.table import Table
import docker
import yaml
from pathlib import Path
import json
from datetime import datetime

console = Console()

class TestOrchestrator:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.docker_client = docker.from_env()
        self.results = []

    def load_config(self, path):
        """Load test configuration"""
        with open(path) as f:
            return yaml.safe_load(f)

    def load_prompts(self, category=None):
        """Load test prompts, optionally filtered by category"""
        prompts = []
        prompt_dir = Path("tests/prompts")

        for yaml_file in prompt_dir.rglob("*.yml"):
            with open(yaml_file) as f:
                prompt = yaml.safe_load(f)
                if category is None or prompt.get("category") == category:
                    prompts.append(prompt)

        return prompts

    def run_test(self, prompt_config):
        """Execute a single test prompt multiple times"""
        console.print(f"\n[bold]Testing: {prompt_config['name']}[/bold]")

        runs = []
        for i in range(prompt_config.get("runs", 5)):
            run_result = self.execute_single_run(prompt_config, i + 1)
            runs.append(run_result)

            status = "✓ PASS" if run_result["pass"] else "✗ FAIL"
            duration = run_result["duration"]
            console.print(f"  Run {i+1}/{prompt_config['runs']} ... {status} ({duration:.1f}s)")

        return {
            "prompt": prompt_config["name"],
            "runs": runs,
            "pass_rate": sum(1 for r in runs if r["pass"]) / len(runs)
        }

    def execute_single_run(self, prompt_config, run_number):
        """Execute prompt in Docker container"""
        container = None
        try:
            # Create container
            container = self.create_container(prompt_config)

            # Start container
            container.start()

            # Execute prompt via tmux
            result = self.send_prompt_to_claude(container, prompt_config["prompt"])

            # Wait for completion or timeout
            transcript = self.wait_and_collect_transcript(
                container,
                timeout=prompt_config.get("timeout_seconds", 120)
            )

            # Analyze transcript
            validation = self.analyze_transcript(transcript, prompt_config)

            return {
                "run_number": run_number,
                "pass": validation["pass"],
                "duration": validation["duration"],
                "transcript_path": validation["transcript_path"],
                "details": validation
            }

        finally:
            if container:
                container.stop()
                container.remove()

    def create_container(self, prompt_config):
        """Create Docker container for test execution"""
        # Implementation details
        pass

    def send_prompt_to_claude(self, container, prompt):
        """Send prompt to Claude Code via tmux"""
        # Implementation details
        pass

    def wait_and_collect_transcript(self, container, timeout):
        """Wait for Claude to finish and collect transcript"""
        # Implementation details
        pass

    def analyze_transcript(self, transcript, expected):
        """Analyze transcript against expected criteria"""
        # Delegate to analyzer module
        pass

@click.command()
@click.option("--category", help="Filter by category")
@click.option("--test", help="Run specific test by name")
@click.option("--runs", type=int, help="Override number of runs")
@click.option("--parallel", type=int, default=1, help="Parallel workers")
def main(category, test, runs, parallel):
    """Run plugin tests"""

    orchestrator = TestOrchestrator("tests/config/test_config.yml")

    # Load prompts
    prompts = orchestrator.load_prompts(category=category)

    if test:
        prompts = [p for p in prompts if p["name"] == test]

    if not prompts:
        console.print("[red]No tests found matching criteria[/red]")
        return

    console.print(f"[bold]Running {len(prompts)} test(s)[/bold]\n")

    # Execute tests
    results = []
    for prompt in prompts:
        if runs:
            prompt["runs"] = runs

        result = orchestrator.run_test(prompt)
        results.append(result)

    # Summary
    console.print("\n[bold]Summary:[/bold]")
    total_pass = sum(1 for r in results if r["pass_rate"] >= 0.95)
    console.print(f"Passed: {total_pass}/{len(results)}")
    console.print(f"Failed: {len(results) - total_pass}/{len(results)}")

    # Save results
    output_path = f"tests/results/results_{datetime.now().isoformat()}.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    console.print(f"\nResults saved to: {output_path}")

if __name__ == "__main__":
    main()
```

#### Step 3: Transcript Analyzer

**File**: `tests/scripts/analyzer.py`

**Key Functions:**

```python
class TranscriptAnalyzer:
    def analyze(self, transcript_path, expected_config):
        """Main analysis entry point"""
        lines = self.load_transcript(transcript_path)

        return {
            "skills_activated": self.detect_skills(lines),
            "tools_used": self.extract_tools(lines),
            "files_created": self.detect_files(lines),
            "duration": self.calculate_duration(lines),
            "validation": self.validate_criteria(lines, expected_config)
        }

    def detect_skills(self, lines):
        """Detect skill activations"""
        skills = []
        for line in lines:
            msg = json.loads(line)
            content = str(msg.get("content", ""))

            if "<command-message>" in content and "skill is loading" in content:
                # Extract skill name from message
                # Example: 'The "python-scripting" skill is loading'
                skill = self.extract_skill_name(content)
                if skill:
                    skills.append(skill)

        return skills

    def extract_skill_name(self, content):
        """Extract skill name from command message"""
        import re
        match = re.search(r'The "(.+?)" skill is loading', content)
        return match.group(1) if match else None

    def validate_criteria(self, lines, expected):
        """Validate against success criteria"""
        validation = {}

        # Check skill activation
        activated = set(self.detect_skills(lines))
        expected_skills = set(expected.get("expected_skills", []))
        validation["skills"] = expected_skills.issubset(activated)

        # Check tool usage
        tools_used = set(self.extract_tools(lines).keys())
        expected_tools = set(expected.get("expected_tools", []))
        validation["tools"] = expected_tools.issubset(tools_used)

        # Check file creation
        files = self.detect_files(lines)
        pattern = expected.get("success_criteria", {}).get("file_created")
        if pattern:
            import fnmatch
            matches = [f for f in files["created"] if fnmatch.fnmatch(f, pattern)]
            validation["files"] = len(matches) > 0

        # Overall pass
        validation["pass"] = all(validation.values())

        return validation
```

#### Step 4: Reporter

**File**: `tests/scripts/reporter.py`

**Output Formats:**

1. **Console Summary** (Rich tables)
2. **JSON** (CI/CD consumption)
3. **Markdown** (GitHub PR comments)

### Phase 3: Analysis & Validation

#### Implementation Priorities

1. **Basic Skill Detection** (MVP)
   - Parse command-message tags
   - Count activations
   - Calculate pass/fail

2. **Tool Usage Tracking** (V1)
   - Extract tool_use events
   - Count frequencies
   - Validate expectations

3. **Statistical Analysis** (V1.5)
   - Mean, median, std dev
   - Flakiness detection
   - Confidence intervals

4. **Advanced Analysis** (V2)
   - Timing analysis
   - Pattern detection
   - Failure correlation

### Phase 4: Integration & Automation

#### CI/CD Pipeline

**File**: `.github/workflows/test-plugins.yml`

```yaml
name: Test Plugins

on:
  push:
    branches: [main]
    paths:
      - 'plugins/**'
      - 'tests/**'
  pull_request:
    paths:
      - 'plugins/**'
      - 'tests/**'

jobs:
  test-plugins:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Docker
        uses: docker/setup-docker-action@v2

      - name: Install UV
        run: curl -LsSf https://astral.sh/uv/install.sh | sh

      - name: Run tests
        run: |
          uv run tests/orchestrator.py

      - name: Generate report
        if: always()
        run: |
          uv run tests/reporter.py --format markdown > report.md

      - name: Comment PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('report.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: report
            });

      - name: Upload artifacts
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: test-results
          path: tests/results/
```

## Technical Challenges & Solutions

### Challenge 1: tmux Automation

**Problem**: Sending prompts to Claude Code in tmux

**Solutions:**
```bash
# Option 1: tmux send-keys
tmux send-keys -t session_name "claude" Enter
sleep 2
tmux send-keys -t session_name "Create a Python script" Enter

# Option 2: Expect scripts
expect << 'EOF'
spawn claude
expect ">"
send "Create a Python script\r"
expect eof
EOF

# Option 3: Direct stdin
echo "Create a Python script" | claude --non-interactive
```

**Recommendation**: tmux send-keys for compatibility

### Challenge 2: Transcript Location

**Problem**: Finding transcripts in Docker containers

**Solution:**
```python
# Mount transcript directory as volume
volumes = {
    "/home/user/.claude/projects": {
        "bind": "/transcripts",
        "mode": "rw"
    }
}

# Or copy after execution
container.exec_run("cp /root/.claude/projects/*.jsonl /output/")
```

### Challenge 3: AWS Credentials

**Problem**: Tests need AWS credentials for Bedrock

**Solutions:**
- Use test AWS account with limited permissions
- Mock Bedrock responses (localstack)
- Skip actual API calls, validate intent only

**Recommendation**: Test account with rate limits

### Challenge 4: Non-Determinism

**Problem**: AI responses vary

**Solutions:**
- Multiple runs (statistical validation)
- Focus on observable behavior (skills/tools)
- Looser validation criteria
- Flakiness detection and retry

### Challenge 5: Performance

**Problem**: Docker + multiple runs = slow

**Solutions:**
- Parallel execution (docker-compose)
- Container pooling (keep warm)
- Incremental testing (changed prompts only)
- Fast-fail for obvious failures

## Testing the Tests

**Meta-testing strategy:**

1. **Unit tests** for analyzer/parser
2. **Mock transcripts** for validation logic
3. **Integration tests** with known-good prompts
4. **Canary tests** in CI/CD

## Development Workflow

1. **Create prompt definition**
   ```bash
   cp tests/prompts/template.yml tests/prompts/python/new-test.yml
   # Edit new-test.yml
   ```

2. **Test locally**
   ```bash
   uv run tests/orchestrator.py --test new-test --runs 1
   ```

3. **Refine criteria**
   - Adjust success_criteria
   - Update expected behaviors
   - Test again

4. **Full validation**
   ```bash
   uv run tests/orchestrator.py --test new-test --runs 5
   ```

5. **Commit and push**
   - CI/CD runs automatically
   - Review results in PR

## Debugging Tips

**View Docker logs:**
```bash
docker logs -f <container_id>
```

**Access running container:**
```bash
docker exec -it <container_id> bash
```

**Inspect transcript:**
```bash
cat ~/.claude/projects/<hash>/<session>.jsonl | jq .
```

**Test analyzer standalone:**
```bash
uv run tests/analyzer.py --transcript path/to/transcript.jsonl --config path/to/prompt.yml
```

## Performance Optimization

1. **Docker image caching**
   - Pre-build base image
   - Layer dependencies efficiently

2. **Parallel execution**
   - Use docker-compose scale
   - Python multiprocessing

3. **Selective testing**
   - Test changed categories only
   - Skip stable tests in dev

4. **Result caching**
   - Cache passing tests
   - Only re-run on changes

## Monitoring & Observability

**Metrics to track:**
- Test execution time
- Pass/fail rates over time
- Skill activation reliability
- Flaky test frequency
- Resource usage (CPU, memory)

**Dashboards:**
- Historical trends
- Category performance
- Recent failures
- Flakiness scores

## Next Steps

1. Implement Docker environment
2. Build basic orchestrator
3. Create transcript analyzer
4. Write first 3 test prompts
5. Validate end-to-end
6. Iterate and expand
