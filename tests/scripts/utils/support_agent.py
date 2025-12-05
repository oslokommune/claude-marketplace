#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

"""
Support Agent - Autonomous question answering

Generates reasonable default answers to common questions that Claude Code
might ask during testing, enabling fully autonomous test execution.
"""

import random
import string
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class Answer:
    """Represents an answer to a question"""
    header: str
    value: str
    reasoning: str


class SupportAgent:
    """Generates reasonable default answers to questions"""

    def __init__(self, custom_answers: Optional[Dict[str, str]] = None):
        """
        Initialize the support agent

        Args:
            custom_answers: Optional dict of custom answers to override defaults
                           Format: {"question_header": "answer_value"}
        """
        self.custom_answers = custom_answers or {}

        self.question_handlers = {
            "name": self._generate_name,
            "path": self._generate_path,
            "port": self._generate_port,
            "number": self._generate_number,
            "boolean": self._generate_boolean,
            "choice": self._select_choice,
        }

    def answer_questions(self, questions: List[Dict[str, Any]]) -> List[Answer]:
        """
        Generate answers for multiple questions

        Args:
            questions: List of question dicts from AskUserQuestion

        Returns:
            List of Answer objects with generated values
        """
        answers = []

        for q in questions:
            question_text = q.get("question", "").lower()
            options = q.get("options", [])
            header = q.get("header", "")
            multi_select = q.get("multiSelect", False)

            # Check for custom override
            if header in self.custom_answers:
                answer = Answer(
                    header=header,
                    value=self.custom_answers[header],
                    reasoning="Custom override provided"
                )
                answers.append(answer)
                continue

            # Classify question type
            q_type = self._classify_question(question_text, header, options)

            # Generate answer
            value, reasoning = self.question_handlers[q_type](
                question_text, options, header, multi_select
            )

            answer = Answer(
                header=header,
                value=value,
                reasoning=reasoning
            )
            answers.append(answer)

        return answers

    def _classify_question(
        self,
        text: str,
        header: str,
        options: List[Dict[str, Any]]
    ) -> str:
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

        if any(word in text for word in ["should", "enable", "disable", "want", "yes", "no"]):
            return "boolean"

        # Default to name for free-form text
        return "name"

    def _generate_name(
        self,
        question: str,
        options: List[Dict[str, Any]],
        header: str,
        multi_select: bool
    ) -> tuple[str, str]:
        """Generate a random project/file name"""
        adjectives = ["test", "demo", "sample", "example", "quick"]
        nouns = ["project", "app", "service", "tool", "script"]

        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        num = random.randint(100, 999)

        name = f"{adj}-{noun}-{num}"
        return name, f"Generated random name: {name}"

    def _generate_path(
        self,
        question: str,
        options: List[Dict[str, Any]],
        header: str,
        multi_select: bool
    ) -> tuple[str, str]:
        """Generate a reasonable path"""
        if "output" in question or "result" in question:
            return "./output", "Output directory path"
        elif "source" in question or "src" in question:
            return "./src", "Source directory path"
        elif "workspace" in question:
            return "./workspace", "Workspace directory path"
        else:
            return "./workspace", "Default workspace path"

    def _generate_port(
        self,
        question: str,
        options: List[Dict[str, Any]],
        header: str,
        multi_select: bool
    ) -> tuple[str, str]:
        """Generate a random high port number"""
        port = random.randint(8000, 9000)
        return str(port), f"Random high port: {port}"

    def _generate_number(
        self,
        question: str,
        options: List[Dict[str, Any]],
        header: str,
        multi_select: bool
    ) -> tuple[str, str]:
        """Generate a reasonable number based on context"""
        if "timeout" in question:
            return "60", "Reasonable timeout value"
        elif "retry" in question or "attempt" in question:
            return "3", "Standard retry count"
        elif "size" in question or "limit" in question:
            return "100", "Reasonable size limit"
        else:
            num = random.randint(1, 10)
            return str(num), f"Random number: {num}"

    def _generate_boolean(
        self,
        question: str,
        options: List[Dict[str, Any]],
        header: str,
        multi_select: bool
    ) -> tuple[str, str]:
        """Default to 'yes' for boolean questions"""
        # Use permissive strategy - default to yes
        return "yes", "Permissive strategy: defaulting to yes"

    def _select_choice(
        self,
        question: str,
        options: List[Dict[str, Any]],
        header: str,
        multi_select: bool
    ) -> tuple[str, str]:
        """Select from provided options"""
        if not options:
            return "default", "No options provided, using default"

        if multi_select:
            # For multi-select, choose the first option
            selected = [options[0].get("label", "default")]
            return ",".join(selected), f"Multi-select: chose first option"

        # Single select - prefer first option (usually default/recommended)
        first_option = options[0].get("label", "default")
        return first_option, f"Selected first option: {first_option}"


if __name__ == "__main__":
    # Simple test
    agent = SupportAgent()

    # Test various question types
    test_questions = [
        {
            "question": "What should we name this project?",
            "header": "Project Name",
            "options": []
        },
        {
            "question": "Which port should the server run on?",
            "header": "Port",
            "options": []
        },
        {
            "question": "Select a framework",
            "header": "Framework",
            "options": [
                {"label": "React", "description": "React framework"},
                {"label": "Vue", "description": "Vue framework"},
                {"label": "Angular", "description": "Angular framework"}
            ]
        },
        {
            "question": "Do you want to enable TypeScript?",
            "header": "TypeScript",
            "options": []
        }
    ]

    answers = agent.answer_questions(test_questions)

    print("Support Agent Test Results:")
    print("=" * 60)
    for answer in answers:
        print(f"\nQuestion: {answer.header}")
        print(f"Answer: {answer.value}")
        print(f"Reasoning: {answer.reasoning}")
