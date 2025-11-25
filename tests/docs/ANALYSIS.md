# Transcript Analysis & Validation

## Overview

This document describes how to parse Claude Code transcripts and validate that plugins/skills are being used correctly.

## Claude Code Transcript Format

Claude Code stores conversations in JSONL (JSON Lines) format at:
```
~/.claude/projects/<project-hash>/<session-id>.jsonl
```

Each line is a JSON object representing a message or event.

### Message Types

#### 1. User Messages
```json
{
  "role": "user",
  "content": "Create a Python script using UV",
  "timestamp": "2025-01-15T10:30:00Z"
}
```

#### 2. Assistant Messages
```json
{
  "role": "assistant",
  "content": "I'll create a Python script with PEP 723 headers...",
  "timestamp": "2025-01-15T10:30:05Z"
}
```

#### 3. Tool Use
```json
{
  "role": "assistant",
  "content": [
    {
      "type": "tool_use",
      "id": "toolu_123",
      "name": "Write",
      "input": {
        "file_path": "/path/to/script.py",
        "content": "#!/usr/bin/env python3\n..."
      }
    }
  ]
}
```

#### 4. Tool Results
```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_123",
      "content": "File created successfully..."
    }
  ]
}
```

#### 5. Command Messages (Skill Activation)
```json
{
  "role": "user",
  "content": "<command-message>The \"python-scripting\" skill is loading</command-message>"
}
```

## Detection Strategies

### 1. Skill Activation Detection

**Method 1: Command Message Parsing**
```python
def detect_skill_activation(transcript_lines):
    """Parse command-message tags for skill loading"""
    skills_activated = []

    for line in transcript_lines:
        msg = json.loads(line)
        if msg.get("role") == "user":
            content = msg.get("content", "")
            if "<command-message>" in content and "skill is loading" in content:
                # Extract skill name
                skill_name = extract_skill_name(content)
                skills_activated.append(skill_name)

    return skills_activated
```

**Method 2: Skill Tool Invocation**
```python
def detect_skill_usage(transcript_lines):
    """Detect Skill tool being called"""
    skills = []

    for line in transcript_lines:
        msg = json.loads(line)
        if msg.get("role") == "assistant":
            content = msg.get("content", [])
            for item in content:
                if item.get("type") == "tool_use" and item.get("name") == "Skill":
                    skill = item.get("input", {}).get("skill")
                    if skill:
                        skills.append(skill)

    return skills
```

### 2. Tool Usage Tracking

```python
def extract_tool_usage(transcript_lines):
    """Extract all tools used in conversation"""
    tools_used = {}

    for line in transcript_lines:
        msg = json.loads(line)
        if msg.get("role") == "assistant":
            content = msg.get("content", [])
            for item in content:
                if item.get("type") == "tool_use":
                    tool_name = item.get("name")
                    tools_used[tool_name] = tools_used.get(tool_name, 0) + 1

    return tools_used
```

### 3. File Operations Detection

```python
def detect_file_operations(transcript_lines):
    """Track files created, edited, or read"""
    operations = {
        "created": [],
        "edited": [],
        "read": []
    }

    for line in transcript_lines:
        msg = json.loads(line)
        if msg.get("role") == "assistant":
            content = msg.get("content", [])
            for item in content:
                if item.get("type") == "tool_use":
                    tool_name = item.get("name")
                    tool_input = item.get("input", {})

                    if tool_name == "Write":
                        operations["created"].append(tool_input.get("file_path"))
                    elif tool_name == "Edit":
                        operations["edited"].append(tool_input.get("file_path"))
                    elif tool_name == "Read":
                        operations["read"].append(tool_input.get("file_path"))

    return operations
```

### 4. Documentation Access Detection

```python
def detect_doc_access(transcript_lines, base_dir):
    """Check if skill documentation was accessed"""
    doc_files_read = []

    for line in transcript_lines:
        msg = json.loads(line)
        if msg.get("role") == "assistant":
            content = msg.get("content", [])
            for item in content:
                if item.get("type") == "tool_use" and item.get("name") == "Read":
                    file_path = item.get("input", {}).get("file_path", "")
                    if base_dir in file_path and "/skills/" in file_path:
                        doc_files_read.append(file_path)

    return doc_files_read
```

## Validation Logic

### 1. Success Criteria Evaluation

```python
class TestValidator:
    def __init__(self, prompt_config, transcripts):
        self.config = prompt_config
        self.transcripts = transcripts

    def validate(self):
        """Run all validation checks"""
        results = {
            "skill_activation": self.check_skill_activation(),
            "tool_usage": self.check_tool_usage(),
            "files_created": self.check_file_creation(),
            "content_validation": self.check_content(),
            "pass": False
        }

        results["pass"] = self.compute_pass_fail(results)
        return results

    def check_skill_activation(self):
        """Validate expected skills were activated"""
        expected = set(self.config["expected_skills"])

        activation_count = 0
        for transcript in self.transcripts:
            activated = set(detect_skill_activation(transcript))
            if expected.issubset(activated):
                activation_count += 1

        rate = activation_count / len(self.transcripts)
        required_rate = self.config["success_criteria"]["skill_activation_rate"]

        return {
            "rate": rate,
            "required": required_rate,
            "pass": rate >= required_rate,
            "runs": len(self.transcripts),
            "successes": activation_count
        }
```

### 2. Statistical Analysis

```python
def compute_statistics(runs):
    """Compute statistical metrics across runs"""
    import statistics

    success_rates = [r["skill_activation"]["rate"] for r in runs]

    return {
        "mean": statistics.mean(success_rates),
        "median": statistics.median(success_rates),
        "stdev": statistics.stdev(success_rates) if len(success_rates) > 1 else 0,
        "min": min(success_rates),
        "max": max(success_rates),
        "variance": statistics.variance(success_rates) if len(success_rates) > 1 else 0
    }
```

### 3. Flakiness Detection

```python
def detect_flakiness(test_results):
    """Identify tests with inconsistent results"""

    total_runs = len(test_results)
    passes = sum(1 for r in test_results if r["pass"])
    failures = total_runs - passes

    flakiness_score = min(passes, failures) / total_runs

    if flakiness_score > 0.2:  # More than 20% inconsistent
        return {
            "is_flaky": True,
            "score": flakiness_score,
            "recommendation": "Review prompt or increase tolerance"
        }

    return {"is_flaky": False, "score": flakiness_score}
```

## Validation Rules

### Rule 1: Skill Activation Rate

```python
# Pass if ≥95% of runs activate expected skills
if skill_activation_rate >= 0.95:
    status = "PASS"
```

**Reasoning**: Allow for occasional AI variability, but expect high consistency.

### Rule 2: Tool Usage

```python
# Pass if all required tools were used at least once
required_tools = {"Write", "Bash"}
used_tools = set(extract_tool_usage(transcript).keys())

if required_tools.issubset(used_tools):
    status = "PASS"
```

**Reasoning**: Validate expected behavior without being overly prescriptive.

### Rule 3: File Creation

```python
# Pass if files matching pattern were created
import glob

pattern = "*.py"
created_files = detect_file_operations(transcript)["created"]
matches = [f for f in created_files if glob.fnmatch(f, pattern)]

if len(matches) > 0:
    status = "PASS"
```

**Reasoning**: Verify artifacts were produced.

### Rule 4: Content Validation

```python
# Pass if created files contain expected strings
required_strings = ["#!/usr/bin/env python3", "# /// script"]
file_content = read_created_file(file_path)

if all(s in file_content for s in required_strings):
    status = "PASS"
```

**Reasoning**: Validate quality of generated content.

## Analysis Output Format

### Per-Run Analysis

```json
{
  "run_id": "run_001",
  "timestamp": "2025-01-15T10:30:00Z",
  "duration_seconds": 45.2,
  "transcript_path": "/path/to/transcript.jsonl",
  "skills_activated": [
    "origo-ai-platform:python",
    "origo-ai-platform:bedrock"
  ],
  "tools_used": {
    "Write": 2,
    "Bash": 1,
    "Read": 1
  },
  "files_created": ["script.py"],
  "validation": {
    "skill_activation": {"pass": true, "rate": 1.0},
    "tool_usage": {"pass": true},
    "file_creation": {"pass": true},
    "content": {"pass": true}
  },
  "overall_pass": true
}
```

### Aggregate Analysis

```json
{
  "test_name": "create-uv-python-script",
  "category": "python",
  "runs": 5,
  "passes": 5,
  "failures": 0,
  "pass_rate": 1.0,
  "statistics": {
    "skill_activation_rate": {
      "mean": 1.0,
      "median": 1.0,
      "stdev": 0.0,
      "min": 1.0,
      "max": 1.0
    },
    "duration": {
      "mean": 42.3,
      "median": 43.1,
      "stdev": 3.2,
      "min": 38.5,
      "max": 47.2
    }
  },
  "flakiness": {
    "is_flaky": false,
    "score": 0.0
  },
  "common_failures": [],
  "recommendation": "Stable test - ready for CI/CD"
}
```

## Error Classification

### 1. Skill Not Activated
- **Cause**: Prompt didn't trigger skill
- **Action**: Revise prompt to be more explicit
- **Severity**: High

### 2. Wrong Skill Activated
- **Cause**: Prompt ambiguous
- **Action**: Clarify prompt intent
- **Severity**: Medium

### 3. Tool Not Used
- **Cause**: AI chose alternative approach
- **Action**: Relax validation or adjust prompt
- **Severity**: Low

### 4. Timeout
- **Cause**: Task too complex or hung
- **Action**: Increase timeout or simplify
- **Severity**: High

### 5. Content Mismatch
- **Cause**: AI used different but valid approach
- **Action**: Relax content validation
- **Severity**: Low

## Advanced Analysis

### 1. Skill Activation Timing

```python
def analyze_activation_timing(transcript_lines):
    """Measure when skills activate relative to prompt"""
    prompt_time = None
    activation_times = []

    for line in transcript_lines:
        msg = json.loads(line)
        ts = msg.get("timestamp")

        if msg.get("role") == "user" and not prompt_time:
            prompt_time = parse_timestamp(ts)
        elif "<command-message>" in str(msg.get("content")):
            activation_time = parse_timestamp(ts)
            delay = (activation_time - prompt_time).total_seconds()
            activation_times.append(delay)

    return activation_times
```

### 2. Tool Usage Patterns

```python
def analyze_tool_patterns(transcripts):
    """Identify common tool usage patterns"""
    patterns = {}

    for transcript in transcripts:
        tools = extract_tool_usage(transcript)
        sequence = tuple(sorted(tools.keys()))
        patterns[sequence] = patterns.get(sequence, 0) + 1

    return patterns
```

### 3. Failure Correlation

```python
def correlate_failures(test_results):
    """Find common factors in failures"""
    failures = [r for r in test_results if not r["pass"]]

    # Look for patterns
    common_tools = set.intersection(*[set(f["tools_used"].keys()) for f in failures])
    common_skills = set.intersection(*[set(f["skills_activated"]) for f in failures])

    return {
        "common_tools": list(common_tools),
        "common_skills": list(common_skills),
        "failure_count": len(failures)
    }
```

## Reporting Requirements

### Console Output (Quick Feedback)
```
Testing: create-uv-python-script
  Run 1/5 ... ✓ PASS (42.3s)
  Run 2/5 ... ✓ PASS (43.1s)
  Run 3/5 ... ✓ PASS (38.5s)
  Run 4/5 ... ✓ PASS (47.2s)
  Run 5/5 ... ✓ PASS (41.8s)

Result: PASS (5/5) - 100% success rate
```

### JSON Output (CI/CD Integration)
```json
{
  "version": "1.0",
  "timestamp": "2025-01-15T10:30:00Z",
  "summary": {
    "total_tests": 18,
    "passed": 17,
    "failed": 1,
    "pass_rate": 0.944
  },
  "tests": [...]
}
```

### Markdown Report (Human Review)
```markdown
# Test Results - 2025-01-15

## Summary
- **Total Tests**: 18
- **Passed**: 17 (94.4%)
- **Failed**: 1 (5.6%)

## Failures
### bedrock-sentiment-analysis
- Skill activation: 3/5 runs (60%)
- Issue: Bedrock skill not consistently triggered
- Recommendation: Make prompt more explicit about AWS Bedrock
```

## Next Steps

1. ✅ Define analysis approach (this document)
2. ⏳ Implement transcript parser
3. ⏳ Build validation engine
4. ⏳ Create report generator
5. ⏳ Add statistical analysis
6. ⏳ Integrate with orchestrator
