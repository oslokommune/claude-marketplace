#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

"""
Transcript Parser - Parse Claude Code JSONL transcripts

Parses JSONL transcript files and extracts relevant events like:
- Skill activations
- Tool usage
- Questions asked
- Messages sent
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class TranscriptMessage:
    """Represents a single message in the transcript"""
    role: str
    content: List[Any]
    raw: Dict[str, Any]

    @property
    def text_content(self) -> str:
        """Extract text content from message"""
        texts = []
        for item in self.content:
            if isinstance(item, dict) and item.get("type") == "text":
                texts.append(item.get("text", ""))
            elif isinstance(item, str):
                texts.append(item)
        return " ".join(texts)

    @property
    def tool_uses(self) -> List[Dict[str, Any]]:
        """Extract tool use events"""
        tools = []
        for item in self.content:
            if isinstance(item, dict) and item.get("type") == "tool_use":
                tools.append(item)
        return tools

    @property
    def skill_activations(self) -> List[str]:
        """Detect skill activations in the message"""
        skills = []

        # Look for skill invocations in tool uses
        for tool in self.tool_uses:
            if tool.get("name") == "Skill":
                skill_name = tool.get("input", {}).get("skill", "")
                if skill_name:
                    skills.append(skill_name)

        # Also look for command-message tags in text
        text = self.text_content.lower()
        if "command-message" in text or "skill is loading" in text:
            # Try to extract skill name from common patterns
            if "origo-ai-platform:python" in text:
                skills.append("origo-ai-platform:python")
            if "origo-ai-platform:bedrock" in text:
                skills.append("origo-ai-platform:bedrock")
            if "origo-ai-platform:subagent" in text:
                skills.append("origo-ai-platform:subagent")
            if "origo-ai-platform:claude-hooks" in text:
                skills.append("origo-ai-platform:claude-hooks")
            if "origo-iac-platform:ok-boilerplate-templates" in text:
                skills.append("origo-iac-platform:ok-boilerplate-templates")
            if "origo-designsystem:punkt-docs" in text:
                skills.append("origo-designsystem:punkt-docs")

        return skills

    @property
    def asks_question(self) -> bool:
        """Check if this message asks a question"""
        for tool in self.tool_uses:
            if tool.get("name") == "AskUserQuestion":
                return True
        return False

    @property
    def questions(self) -> List[Dict[str, Any]]:
        """Extract questions asked"""
        questions = []
        for tool in self.tool_uses:
            if tool.get("name") == "AskUserQuestion":
                qs = tool.get("input", {}).get("questions", [])
                questions.extend(qs)
        return questions


class TranscriptParser:
    """Parse Claude Code JSONL transcripts"""

    def __init__(self, transcript_path: Path):
        self.transcript_path = Path(transcript_path)
        self.messages: List[TranscriptMessage] = []

    def parse(self) -> List[TranscriptMessage]:
        """Parse the transcript file"""
        self.messages = []

        if not self.transcript_path.exists():
            return self.messages

        with open(self.transcript_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                try:
                    data = json.loads(line)

                    # Check if message data is nested under "message" key
                    message_data = data.get("message", data)

                    # Only process messages with role and content
                    if "role" in message_data and "content" in message_data:
                        content = message_data["content"]
                        # Ensure content is a list
                        if isinstance(content, str):
                            content = [{"type": "text", "text": content}]
                        elif not isinstance(content, list):
                            content = [content]

                        msg = TranscriptMessage(
                            role=message_data["role"],
                            content=content,
                            raw=data
                        )
                        self.messages.append(msg)

                except json.JSONDecodeError:
                    # Skip malformed lines
                    continue

        return self.messages

    def get_skill_activations(self) -> List[str]:
        """Get all skill activations from the transcript"""
        skills = []
        for msg in self.messages:
            skills.extend(msg.skill_activations)
        return list(set(skills))  # Remove duplicates

    def get_tool_usage(self) -> Dict[str, int]:
        """Count tool usage across all messages"""
        tool_counts = {}
        for msg in self.messages:
            for tool in msg.tool_uses:
                tool_name = tool.get("name", "unknown")
                tool_counts[tool_name] = tool_counts.get(tool_name, 0) + 1
        return tool_counts

    def get_questions_asked(self) -> List[Dict[str, Any]]:
        """Get all questions asked in the transcript"""
        all_questions = []
        for msg in self.messages:
            all_questions.extend(msg.questions)
        return all_questions

    def get_assistant_messages(self) -> List[TranscriptMessage]:
        """Get all assistant messages"""
        return [msg for msg in self.messages if msg.role == "assistant"]

    def get_user_messages(self) -> List[TranscriptMessage]:
        """Get all user messages"""
        return [msg for msg in self.messages if msg.role == "user"]


if __name__ == "__main__":
    # Simple test
    import sys

    if len(sys.argv) < 2:
        print("Usage: transcript_parser.py <transcript.jsonl>")
        sys.exit(1)

    parser = TranscriptParser(sys.argv[1])
    messages = parser.parse()

    print(f"Parsed {len(messages)} messages")
    print(f"Skills activated: {parser.get_skill_activations()}")
    print(f"Tool usage: {parser.get_tool_usage()}")
    print(f"Questions asked: {len(parser.get_questions_asked())}")
