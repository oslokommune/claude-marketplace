# Support Agent for Autonomous Testing

## Problem Statement

During test execution, Claude Code may ask clarifying questions:
- "What should I name this project?"
- "Which port should the server run on?"
- "What's the folder path?"

Without answers, tests hang and fail. We need an automated "support agent" to provide reasonable defaults.

## Solution: Real-Time Question Detection & Auto-Response

### Architecture Enhancement

```
┌─────────────────────────────────────────┐
│     Test Orchestrator                    │
│                                          │
│  ┌────────────────────────────────────┐ │
│  │  Transcript Monitor (Thread)       │ │
│  │  - Watch for AskUserQuestion       │ │
│  │  - Detect questions in real-time   │ │
│  └──────────┬─────────────────────────┘ │
│             │                            │
│             ▼                            │
│  ┌────────────────────────────────────┐ │
│  │  Support Agent                     │ │
│  │  - Parse question type             │ │
│  │  - Generate appropriate answer     │ │
│  │  - Return via callback             │ │
│  └──────────┬─────────────────────────┘ │
│             │                            │
└─────────────┼────────────────────────────┘
              │
              ▼
      ┌─────────────────┐
      │  Docker + tmux  │
      │                 │
      │  Claude Code    │
      │  (waiting for   │
      │   answer)       │
      └─────────────────┘
              ▲
              │
      Answer sent via
      tmux send-keys
```

## Implementation Approach

### 1. Real-Time Transcript Monitoring

Monitor the transcript file as it's being written:

```python
import time
import json
from pathlib import Path

class TranscriptMonitor:
    def __init__(self, transcript_path, callback):
        self.transcript_path = Path(transcript_path)
        self.callback = callback
        self.last_position = 0
        self.running = True

    def start(self):
        """Monitor transcript in background thread"""
        while self.running:
            if self.transcript_path.exists():
                self.check_for_questions()
            time.sleep(0.5)  # Poll every 500ms

    def check_for_questions(self):
        """Read new lines from transcript"""
        with open(self.transcript_path, 'r') as f:
            f.seek(self.last_position)
            new_lines = f.readlines()
            self.last_position = f.tell()

            for line in new_lines:
                self.process_line(line)

    def process_line(self, line):
        """Check if line contains a question"""
        try:
            msg = json.loads(line)

            # Detect AskUserQuestion tool
            if msg.get("role") == "assistant":
                content = msg.get("content", [])
                for item in content:
                    if isinstance(item, dict) and item.get("type") == "tool_use":
                        if item.get("name") == "AskUserQuestion":
                            # Found a question!
                            questions = item.get("input", {}).get("questions", [])
                            self.callback(questions, item.get("id"))

        except json.JSONDecodeError:
            pass  # Incomplete line, will retry
```

### 2. Support Agent - Answer Generator

Generate contextually appropriate answers:

```python
import random
import string

class SupportAgent:
    """Generates reasonable default answers to common questions"""

    def __init__(self):
        self.question_handlers = {
            "name": self._generate_name,
            "path": self._generate_path,
            "port": self._generate_port,
            "number": self._generate_number,
            "boolean": self._generate_boolean,
            "choice": self._select_choice,
        }

    def answer_questions(self, questions):
        """Generate answers for multiple questions"""
        answers = {}

        for q in questions:
            question_text = q.get("question", "").lower()
            options = q.get("options", [])
            header = q.get("header", "")

            # Classify question type
            q_type = self._classify_question(question_text, header, options)

            # Generate answer
            answer = self.question_handlers[q_type](question_text, options, header)
            answers[header] = answer

        return answers

    def _classify_question(self, text, header, options):
        """Determine question type from context"""

        # If options provided, it's a choice question
        if options:
            return "choice"

        # Pattern matching for common question types
        if any(word in text for word in ["name", "called", "title"]):
            return "name"

        if any(word in text for word in ["path", "directory", "folder", "location"]):
            return "path"

        if any(word in text for word in ["port", "address"]):
            return "port"

        if any(word in text for word in ["number", "count", "size", "limit"]):
            return "number"

        if any(word in text for word in ["should", "enable", "disable", "want"]):
            return "boolean"

        # Default to choice if we have options, otherwise name
        return "choice" if options else "name"

    def _generate_name(self, question, options, header):
        """Generate a random project/file name"""
        adjectives = ["test", "demo", "sample", "example", "quick"]
        nouns = ["project", "app", "service", "tool", "script"]

        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        num = random.randint(100, 999)

        return f"{adj}-{noun}-{num}"

    def _generate_path(self, question, options, header):
        """Generate a reasonable path"""
        if "output" in question or "result" in question:
            return "./output"
        elif "source" in question or "src" in question:
            return "./src"
        else:
            return "./workspace"

    def _generate_port(self, question, options, header):
        """Generate a random high port number"""
        return str(random.randint(8000, 9000))

    def _generate_number(self, question, options, header):
        """Generate a reasonable number based on context"""
        if "timeout" in question:
            return "60"
        elif "retry" in question or "attempt" in question:
            return "3"
        elif "size" in question or "limit" in question:
            return "100"
        else:
            return str(random.randint(1, 10))

    def _generate_boolean(self, question, options, header):
        """Default to 'yes' for boolean questions"""
        return "yes"

    def _select_choice(self, question, options, header):
        """Select first option from choices"""
        if not options:
            return "default"

        # Prefer first option (usually the default/recommended)
        return options[0].get("label", "default")
```

### 3. Answer Injection via tmux

Send the answer back to Claude Code:

```python
class TMuxController:
    def __init__(self, container, session_name):
        self.container = container
        self.session_name = session_name

    def send_answer(self, answers, tool_use_id):
        """Send answers back to Claude Code"""

        # Claude Code expects answers in specific format
        # For AskUserQuestion, we need to select the option

        for header, answer in answers.items():
            # Simulate user selecting answer
            # This depends on Claude Code's interface
            # May need to send arrow keys + Enter or type selection

            self.send_keys(answer)
            self.send_keys("Enter")

    def send_keys(self, text):
        """Send keys to tmux session"""
        # Escape special characters
        escaped = text.replace('"', '\\"')

        # Execute in container
        cmd = f'tmux send-keys -t {self.session_name} "{escaped}"'
        self.container.exec_run(cmd)
```

### 4. Integration with Orchestrator

```python
class TestOrchestrator:
    def execute_single_run(self, prompt_config, run_number):
        """Execute prompt with support agent"""
        container = None
        monitor = None

        try:
            # Create container
            container = self.create_container(prompt_config)
            container.start()

            # Get transcript path (will be created by Claude)
            transcript_path = self.get_transcript_path(container)

            # Start support agent monitoring
            support_agent = SupportAgent()
            tmux_controller = TMuxController(container, "claude-session")

            def on_question_detected(questions, tool_use_id):
                """Callback when question is detected"""
                console.print(f"[yellow]Question detected, auto-answering...[/yellow]")

                # Generate answers
                answers = support_agent.answer_questions(questions)
                console.print(f"[dim]Answers: {answers}[/dim]")

                # Send to Claude
                tmux_controller.send_answer(answers, tool_use_id)

            # Start monitoring in background thread
            monitor = TranscriptMonitor(transcript_path, on_question_detected)
            monitor_thread = threading.Thread(target=monitor.start, daemon=True)
            monitor_thread.start()

            # Execute prompt
            self.send_prompt_to_claude(container, prompt_config["prompt"])

            # Wait for completion
            transcript = self.wait_and_collect_transcript(
                container,
                timeout=prompt_config.get("timeout_seconds", 120)
            )

            return self.analyze_transcript(transcript, prompt_config)

        finally:
            if monitor:
                monitor.running = False
            if container:
                container.stop()
                container.remove()
```

## Configuration

Allow tests to configure support agent behavior:

```yaml
# In prompt definition
name: create-app-with-questions
category: python
prompt: |
  Create a new web application project
support_agent:
  enabled: true
  strategy: "permissive"  # always answer yes/default
  custom_answers:
    "project name": "test-webapp"
    "port": "8080"
  # Or disable for tests that shouldn't have questions
  # enabled: false
```

## Advanced: LLM-Powered Support Agent (Optional)

For more complex questions, use a lightweight LLM:

```python
class LLMSupportAgent(SupportAgent):
    """Use small LLM to generate contextual answers"""

    def __init__(self):
        super().__init__()
        # Use AWS Bedrock with small model (Haiku)
        self.bedrock = boto3.client('bedrock-runtime', region='eu-central-1')
        self.model_id = "eu.anthropic.claude-haiku-4-5-20251001-v1:0"

    def answer_questions(self, questions):
        """Generate answers using LLM"""
        answers = {}

        for q in questions:
            question_text = q.get("question")
            options = q.get("options", [])

            # Use LLM for complex questions
            if self._is_complex_question(question_text):
                answer = self._llm_answer(question_text, options)
            else:
                # Fall back to rule-based for simple questions
                answer = super().answer_questions([q])

            answers[q.get("header")] = answer

        return answers

    def _llm_answer(self, question, options):
        """Ask LLM to select best option or generate answer"""
        prompt = f"""You are helping run automated tests. Answer this question concisely:

Question: {question}

{f"Options: {', '.join([o['label'] for o in options])}" if options else ""}

Provide a simple, reasonable default answer suitable for testing. Just the answer, no explanation."""

        # Call Bedrock (simplified)
        response = self.bedrock.invoke_model(
            modelId=self.model_id,
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 50
            })
        )

        return json.loads(response['body'].read())['content'][0]['text']
```

## Benefits of This Approach

1. **Autonomous Testing**: Tests don't hang on questions
2. **Realistic Testing**: Tests actual user flows with questions
3. **Configurable**: Can customize answers per test
4. **Scalable**: Works across all Docker containers
5. **Observable**: See what questions are asked and how answered

## Limitations & Considerations

### 1. Timing Sensitivity
- Need to detect questions quickly (< 1s)
- File-based monitoring has slight delay
- Alternative: Hook into Claude's output stream directly

### 2. Answer Format
- Must match Claude Code's expected input format
- May need to reverse-engineer AskUserQuestion response format
- Test with simple prompts first

### 3. Question Complexity
- Rule-based works for simple questions
- Complex questions may need LLM support
- Or skip tests that require complex human judgment

### 4. False Positives
- Monitor might trigger on non-questions
- Need robust detection logic
- Add safeguards (timeout, max answers)

## Alternative: Pre-Answered Prompts

Simpler approach - craft prompts to avoid questions:

```yaml
# Instead of:
prompt: "Create a web application"

# Be explicit:
prompt: |
  Create a web application named "test-app" on port 8080
  in the ./src directory. Use default configuration.
```

**Pros**: No complex monitoring needed
**Cons**: Less realistic, doesn't test question flows

## Recommendation

**Phase 1 (MVP)**:
- Use explicit prompts (avoid questions)
- Add basic rule-based support agent

**Phase 2 (V1)**:
- Implement transcript monitoring
- Full support agent with auto-answers

**Phase 3 (V2)**:
- LLM-powered support agent for complex questions
- Configurable answer strategies per test

## Implementation Priority

1. ✅ Document approach (this file)
2. ⏳ Implement TranscriptMonitor
3. ⏳ Build rule-based SupportAgent
4. ⏳ Integrate with TMuxController
5. ⏳ Test with simple questions
6. ⏳ Add configuration options
7. ⏳ Consider LLM support for complex cases

This makes the Docker + tmux architecture even more powerful for autonomous testing!
