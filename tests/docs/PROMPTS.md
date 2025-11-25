# Test Prompt Design & Structure

## Overview

Test prompts are designed to trigger specific skills and validate plugin activation consistency.

## Prompt Categories

### Category 1: Python Development (`prompts/python/`)

**Target Skills:**
- `origo-ai-platform:python`
- `origo-ai-platform:bedrock`

**Test Scenarios:**

1. **Basic UV Script Creation**
   - Prompt: "Create a Python script with PEP 723 headers using UV"
   - Expected: Skill activation, Write tool, proper headers
   - Validates: Python skill recognition, template usage

2. **Bedrock Integration**
   - Prompt: "Write a Python script that calls AWS Bedrock to analyze sentiment"
   - Expected: Both python + bedrock skills, boto3 dependency
   - Validates: Multi-skill coordination

3. **CLI Tool Creation**
   - Prompt: "Create a CLI tool using Click that processes JSON files"
   - Expected: Python skill, proper dependencies, Rich output
   - Validates: Dependency selection, best practices

### Category 2: Infrastructure (`prompts/iac/`)

**Target Skills:**
- `origo-iac-platform:ok-boilerplate-templates`

**Test Scenarios:**

1. **Template Discovery**
   - Prompt: "What Terraform templates are available for deploying a web app?"
   - Expected: Skill activation, template listing
   - Validates: Documentation lookup

2. **CloudFront Setup**
   - Prompt: "Help me set up a CloudFront static website using the ok tool"
   - Expected: ok-boilerplate skill, template guidance
   - Validates: Specific template knowledge

3. **App Deployment**
   - Prompt: "I need to deploy an application with load balancing. What templates should I use?"
   - Expected: Skill activation, app + load-balancing-alb recommendation
   - Validates: Template dependency understanding

### Category 3: Design System (`prompts/design/`)

**Target Skills:**
- `origo-designsystem:punkt-docs`

**Test Scenarios:**

1. **Component Documentation**
   - Prompt: "How do I use the Punkt Button component in React?"
   - Expected: Skill activation, accurate component docs
   - Validates: Documentation retrieval

2. **Form Implementation**
   - Prompt: "Create a form using Punkt components with TextInput and Button"
   - Expected: Skill activation, proper component usage
   - Validates: Multi-component knowledge

3. **Design Tokens**
   - Prompt: "What are the available color tokens in Punkt design system?"
   - Expected: Skill activation, color resource lookup
   - Validates: Resource documentation access

### Category 4: Sub-Agent Creation (`prompts/subagent/`)

**Target Skills:**
- `origo-ai-platform:subagent`
- `origo-ai-platform:claude-hooks`

**Test Scenarios:**

1. **Create Custom Agent**
   - Prompt: "Create a sub-agent specialized in code review"
   - Expected: Subagent skill, proper file creation
   - Validates: Agent template knowledge

2. **Hook Configuration**
   - Prompt: "Set up a hook to log all bash commands"
   - Expected: Claude-hooks skill, proper JSON structure
   - Validates: Hook system understanding

## Prompt Definition Schema

```yaml
# Schema version
schema_version: "1.0"

# Test metadata
name: string                    # Unique identifier (kebab-case)
category: string                # python | iac | design | subagent
description: string             # Human-readable description
tags: array<string>             # Optional tags for filtering

# Test configuration
prompt: string                  # The actual prompt to send
timeout_seconds: integer        # Max execution time (default: 120)
runs: integer                   # Number of times to run (default: 5)

# Expected behavior
expected_skills: array<string>  # Skills that should activate
expected_tools: array<string>   # Tools that should be used
success_criteria:
  skill_activation_rate: float  # Min rate (0.0-1.0) for pass
  tool_usage: array<string>     # Required tools
  file_created: string          # Glob pattern for files
  file_contains: array<string>  # Strings that should appear
  skill_docs_accessed: boolean  # Verify doc access

# Optional validation
validation:
  custom_script: string         # Path to custom validator
  artifacts_check: object       # Check specific artifacts
```

## Example Prompt Definitions

### Example 1: Python Script Creation

```yaml
schema_version: "1.0"
name: create-uv-python-script
category: python
description: Test UV-based Python script creation with dependencies
tags: [python, uv, pep723]

prompt: |
  Create a Python script that fetches data from a REST API and saves it to a JSON file.
  Use UV package manager with PEP 723 headers.

timeout_seconds: 120
runs: 5

expected_skills:
  - origo-ai-platform:python
expected_tools:
  - Write
  - Bash
success_criteria:
  skill_activation_rate: 0.95
  tool_usage: ["Write"]
  file_created: "*.py"
  file_contains:
    - "#!/usr/bin/env python3"
    - "# /// script"
    - "requires-python"
    - "dependencies"
    - "requests"
```

### Example 2: Bedrock Integration

```yaml
schema_version: "1.0"
name: bedrock-sentiment-analysis
category: python
description: Test Bedrock skill activation for AI integration
tags: [python, bedrock, aws]

prompt: |
  Write a Python script that uses AWS Bedrock to analyze the sentiment of text input.
  Use the eu-central-1 region and Claude Sonnet 4.5 model.

timeout_seconds: 180
runs: 5

expected_skills:
  - origo-ai-platform:python
  - origo-ai-platform:bedrock
expected_tools:
  - Write
  - Bash
success_criteria:
  skill_activation_rate: 0.90
  tool_usage: ["Write"]
  file_created: "*.py"
  file_contains:
    - "boto3"
    - "eu-central-1"
    - "bedrock"
    - "claude-sonnet"
```

### Example 3: Infrastructure Template

```yaml
schema_version: "1.0"
name: cloudfront-template-guidance
category: iac
description: Test ok-boilerplate skill for CloudFront setup
tags: [iac, terraform, cloudfront]

prompt: |
  I want to deploy a static website to CloudFront using the ok tool.
  What templates do I need and how do I configure them?

timeout_seconds: 90
runs: 5

expected_skills:
  - origo-iac-platform:ok-boilerplate-templates
expected_tools:
  - Read
success_criteria:
  skill_activation_rate: 0.95
  skill_docs_accessed: true
validation:
  response_contains:
    - "cloudfront-static-website"
    - "ok pkg add"
    - "package-config.yml"
```

### Example 4: Design System Component

```yaml
schema_version: "1.0"
name: punkt-button-usage
category: design
description: Test Punkt documentation access for Button component
tags: [design, punkt, react]

prompt: |
  Show me how to use the Punkt Button component in a React application.
  Include different variants and props.

timeout_seconds: 90
runs: 5

expected_skills:
  - origo-designsystem:punkt-docs
expected_tools:
  - Read
success_criteria:
  skill_activation_rate: 0.95
  skill_docs_accessed: true
validation:
  response_contains:
    - "punkt-react"
    - "Button"
    - "variant"
```

## Prompt Best Practices

### 1. Clear Intent
- State exactly what you want Claude to do
- Avoid ambiguous language
- Be specific about technologies

### 2. Natural Language
- Write as a developer would naturally ask
- Don't over-engineer the prompt
- Test with real-world phrasing

### 3. Appropriate Scope
- Each prompt should test 1-3 skills
- Not too simple (trivial activation)
- Not too complex (multiple failure points)

### 4. Validation Balance
- Strict enough to catch issues
- Flexible enough for AI variability
- Focus on skill activation, not exact output

### 5. Timeout Tuning
- Simple queries: 60-90s
- Code generation: 120-180s
- Complex tasks: 180-300s

## Anti-Patterns to Avoid

❌ **Too Vague**: "Help me with infrastructure"
✅ **Specific**: "Set up CloudFront static website using ok tool"

❌ **Multi-Goal**: "Create app, deploy it, and set up monitoring"
✅ **Focused**: "What templates do I need to deploy an app?"

❌ **Overly Prescriptive**: "Use skill X, then tool Y, then..."
✅ **Natural**: "Create a Python script that uses Bedrock"

❌ **Unrealistic**: "Build entire application with tests"
✅ **Realistic**: "Create a CLI tool with proper structure"

## Test Coverage Goals

### Minimum Coverage (MVP)
- 3 prompts per skill (18 total)
- Core functionality of each skill
- Basic activation detection

### Comprehensive Coverage (V1)
- 5-7 prompts per skill (30-42 total)
- Edge cases and variations
- Multi-skill coordination
- Error handling scenarios

### Full Coverage (V2+)
- 10+ prompts per skill (60+ total)
- All documented features
- Performance variations
- Integration scenarios
- Negative test cases

## Prompt Maintenance

- **Version Control**: All prompts in git
- **Review Process**: PR review for new prompts
- **Success Tracking**: Monitor pass rates over time
- **Deprecation**: Mark outdated prompts
- **Evolution**: Update as skills improve
