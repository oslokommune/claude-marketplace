#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

"""
Transcript Monitor - Real-time transcript watching

Monitors a Claude Code transcript file as it's being written and triggers
callbacks when events of interest occur (like questions being asked).
"""

import json
import time
import threading
from pathlib import Path
from typing import Callable, Optional, Any, Dict, List
from dataclasses import dataclass


@dataclass
class QuestionEvent:
    """Represents a question detected in the transcript"""
    tool_use_id: str
    questions: List[Dict[str, Any]]
    timestamp: float


class TranscriptMonitor:
    """Monitor a transcript file in real-time for events"""

    def __init__(
        self,
        transcript_path: Path,
        on_question: Optional[Callable[[QuestionEvent], None]] = None,
        on_skill_activation: Optional[Callable[[str], None]] = None,
        poll_interval: float = 0.5
    ):
        """
        Initialize the transcript monitor

        Args:
            transcript_path: Path to the transcript file to monitor
            on_question: Callback when a question is detected
            on_skill_activation: Callback when a skill activation is detected
            poll_interval: How often to check the file (seconds)
        """
        self.transcript_path = Path(transcript_path)
        self.on_question = on_question
        self.on_skill_activation = on_skill_activation
        self.poll_interval = poll_interval

        self.last_position = 0
        self.running = False
        self.thread: Optional[threading.Thread] = None

        # Track what we've already seen to avoid duplicates
        self.seen_tool_use_ids = set()
        self.seen_skills = set()

    def start(self) -> None:
        """Start monitoring in a background thread"""
        if self.running:
            return

        self.running = True
        self.thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.thread.start()

    def stop(self) -> None:
        """Stop monitoring"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)

    def _monitor_loop(self) -> None:
        """Main monitoring loop (runs in background thread)"""
        # Wait for file to be created
        while self.running and not self.transcript_path.exists():
            time.sleep(self.poll_interval)

        # Monitor for new lines
        while self.running:
            try:
                self._check_for_new_lines()
            except Exception as e:
                # Don't crash the monitor on errors
                print(f"Error in monitor loop: {e}")

            time.sleep(self.poll_interval)

    def _check_for_new_lines(self) -> None:
        """Check for new lines in the transcript file"""
        if not self.transcript_path.exists():
            return

        with open(self.transcript_path, 'r') as f:
            f.seek(self.last_position)
            new_lines = f.readlines()
            self.last_position = f.tell()

            for line in new_lines:
                self._process_line(line)

    def _process_line(self, line: str) -> None:
        """Process a single line from the transcript"""
        line = line.strip()
        if not line:
            return

        try:
            data = json.loads(line)

            # Check for assistant messages with tool uses
            if data.get("role") == "assistant":
                content = data.get("content", [])
                if not isinstance(content, list):
                    return

                for item in content:
                    if not isinstance(item, dict):
                        continue

                    # Check for questions
                    if item.get("type") == "tool_use":
                        self._handle_tool_use(item)

                    # Check for skill activations in text
                    if item.get("type") == "text":
                        self._check_for_skills(item.get("text", ""))

            # Also check for command-message tags in system messages
            if data.get("role") == "system":
                content = data.get("content", "")
                if isinstance(content, str):
                    self._check_for_skills(content)

        except json.JSONDecodeError:
            # Skip malformed lines (might be incomplete)
            pass

    def _handle_tool_use(self, tool_item: Dict[str, Any]) -> None:
        """Handle a tool use item"""
        tool_name = tool_item.get("name")
        tool_use_id = tool_item.get("id")

        # Avoid processing the same tool use twice
        if tool_use_id in self.seen_tool_use_ids:
            return

        self.seen_tool_use_ids.add(tool_use_id)

        # Check for questions
        if tool_name == "AskUserQuestion" and self.on_question:
            questions = tool_item.get("input", {}).get("questions", [])
            if questions:
                event = QuestionEvent(
                    tool_use_id=tool_use_id,
                    questions=questions,
                    timestamp=time.time()
                )
                self.on_question(event)

        # Check for skill activations
        if tool_name == "Skill" and self.on_skill_activation:
            skill_name = tool_item.get("input", {}).get("skill", "")
            if skill_name and skill_name not in self.seen_skills:
                self.seen_skills.add(skill_name)
                self.on_skill_activation(skill_name)

    def _check_for_skills(self, text: str) -> None:
        """Check text content for skill activation patterns"""
        if not self.on_skill_activation:
            return

        text_lower = text.lower()

        # Common patterns that indicate skill activation
        if "skill is loading" not in text_lower and "command-message" not in text_lower:
            return

        # List of skills to check for
        skills = [
            "origo-ai-platform:python",
            "origo-ai-platform:bedrock",
            "origo-ai-platform:subagent",
            "origo-ai-platform:claude-hooks",
            "origo-iac-platform:ok-boilerplate-templates",
            "origo-designsystem:punkt-docs",
        ]

        for skill in skills:
            if skill in text and skill not in self.seen_skills:
                self.seen_skills.add(skill)
                self.on_skill_activation(skill)


if __name__ == "__main__":
    # Simple test
    import sys

    if len(sys.argv) < 2:
        print("Usage: transcript_monitor.py <transcript.jsonl>")
        sys.exit(1)

    def on_question(event: QuestionEvent):
        print(f"\n[QUESTION DETECTED] {len(event.questions)} question(s)")
        for q in event.questions:
            print(f"  - {q.get('question', 'Unknown')}")

    def on_skill(skill_name: str):
        print(f"\n[SKILL ACTIVATED] {skill_name}")

    monitor = TranscriptMonitor(
        Path(sys.argv[1]),
        on_question=on_question,
        on_skill_activation=on_skill
    )

    print(f"Monitoring {sys.argv[1]}...")
    print("Press Ctrl+C to stop")

    monitor.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping monitor...")
        monitor.stop()
