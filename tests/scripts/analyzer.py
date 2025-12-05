#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pyyaml",
# ]
# ///

"""
Transcript Analyzer - Analyze test results

Analyzes transcript files against test criteria and generates analysis results.
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import yaml

# Import our utilities
sys.path.insert(0, str(Path(__file__).parent / "utils"))
from transcript_parser import TranscriptParser


@dataclass
class TestResult:
    """Result of a single test run"""
    prompt_name: str
    run_number: int
    success: bool
    skills_activated: List[str]
    expected_skills: List[str]
    skill_activation_met: bool
    tool_usage: Dict[str, int]
    questions_asked: int
    errors: List[str]
    transcript_path: str
    execution_time: Optional[float] = None


@dataclass
class AggregatedResult:
    """Aggregated results across multiple runs"""
    prompt_name: str
    total_runs: int
    successful_runs: int
    success_rate: float
    skill_activation_rate: float
    expected_skill_activation_rate: float
    passed: bool
    runs: List[TestResult]
    common_errors: List[str]


class TranscriptAnalyzer:
    """Analyze transcripts and validate against test criteria"""

    def __init__(self):
        pass

    def analyze_transcript(
        self,
        transcript_path: Path,
        test_config: Dict[str, Any],
        run_number: int
    ) -> TestResult:
        """
        Analyze a single transcript file

        Args:
            transcript_path: Path to the transcript JSONL file
            test_config: Test configuration from YAML
            run_number: Run number for this test

        Returns:
            TestResult object
        """
        parser = TranscriptParser(transcript_path)
        parser.parse()

        # Extract expected criteria
        expected_skills = test_config.get("expected_skills", [])
        success_criteria = test_config.get("success_criteria", {})
        validation = test_config.get("validation", {})

        # Get actual results
        skills_activated = parser.get_skill_activations()
        tool_usage = parser.get_tool_usage()
        questions = parser.get_questions_asked()

        # Check skill activation
        skill_activation_met = self._check_skill_activation(
            skills_activated,
            expected_skills
        )

        # Check for errors
        errors = self._find_errors(parser)

        # Check validation criteria
        validation_met = self._check_validation(
            parser,
            validation
        )

        # Determine overall success
        success = skill_activation_met and validation_met and len(errors) == 0

        # Generate human-readable markdown transcript
        self._generate_markdown_transcript(
            transcript_path,
            parser,
            test_config,
            run_number,
            success
        )

        return TestResult(
            prompt_name=test_config.get("name", "unknown"),
            run_number=run_number,
            success=success,
            skills_activated=skills_activated,
            expected_skills=expected_skills,
            skill_activation_met=skill_activation_met,
            tool_usage=tool_usage,
            questions_asked=len(questions),
            errors=errors,
            transcript_path=str(transcript_path)
        )

    def aggregate_results(
        self,
        results: List[TestResult],
        test_config: Dict[str, Any]
    ) -> AggregatedResult:
        """
        Aggregate results from multiple runs

        Args:
            results: List of TestResult objects
            test_config: Test configuration from YAML

        Returns:
            AggregatedResult object
        """
        total_runs = len(results)
        successful_runs = sum(1 for r in results if r.success)
        success_rate = successful_runs / total_runs if total_runs > 0 else 0

        # Calculate skill activation rate
        skill_activations = sum(
            1 for r in results if r.skill_activation_met
        )
        skill_activation_rate = skill_activations / total_runs if total_runs > 0 else 0

        # Get expected rate from config
        expected_rate = test_config.get("success_criteria", {}).get(
            "skill_activation_rate",
            0.95
        )

        # Check if passed
        passed = skill_activation_rate >= expected_rate

        # Find common errors
        all_errors = []
        for r in results:
            all_errors.extend(r.errors)

        common_errors = list(set(all_errors))

        return AggregatedResult(
            prompt_name=test_config.get("name", "unknown"),
            total_runs=total_runs,
            successful_runs=successful_runs,
            success_rate=success_rate,
            skill_activation_rate=skill_activation_rate,
            expected_skill_activation_rate=expected_rate,
            passed=passed,
            runs=results,
            common_errors=common_errors
        )

    def _check_skill_activation(
        self,
        activated: List[str],
        expected: List[str]
    ) -> bool:
        """Check if all expected skills were activated"""
        for skill in expected:
            if skill not in activated:
                return False
        return True

    def _check_validation(
        self,
        parser: TranscriptParser,
        validation: Dict[str, Any]
    ) -> bool:
        """Check validation criteria"""
        if not validation:
            return True

        # Check if response contains required text
        response_contains = validation.get("response_contains", [])
        if response_contains:
            all_text = " ".join(
                msg.text_content for msg in parser.get_assistant_messages()
            )

            for required_text in response_contains:
                if required_text.lower() not in all_text.lower():
                    return False

        return True

    def _find_errors(self, parser: TranscriptParser) -> List[str]:
        """Find errors in the transcript"""
        errors = []

        # Look for error messages in assistant responses
        for msg in parser.get_assistant_messages():
            text = msg.text_content.lower()

            # Common error patterns
            error_patterns = [
                "error:",
                "exception:",
                "failed to",
                "could not",
                "unable to",
            ]

            for pattern in error_patterns:
                if pattern in text:
                    # Extract the error context (50 chars)
                    idx = text.index(pattern)
                    error_snippet = text[idx:idx+100]
                    errors.append(error_snippet)
                    break

        return errors

    def _generate_markdown_transcript(
        self,
        transcript_path: Path,
        parser: TranscriptParser,
        test_config: Dict[str, Any],
        run_number: int,
        success: bool
    ) -> None:
        """
        Generate a human-readable markdown version of the transcript

        Args:
            transcript_path: Path to the JSONL transcript
            parser: Parsed transcript
            test_config: Test configuration
            run_number: Run number
            success: Whether the test passed
        """
        # Create markdown file in the same directory
        md_path = transcript_path.with_suffix('.md')

        with open(md_path, 'w', encoding='utf-8') as f:
            # Header
            f.write(f"# Test Transcript: {test_config.get('name', 'unknown')}\n\n")
            f.write(f"**Run:** {run_number}\n")
            f.write(f"**Status:** {'✅ PASS' if success else '❌ FAIL'}\n")
            f.write(f"**Transcript:** `{transcript_path.name}`\n\n")

            # Test configuration
            f.write("## Test Configuration\n\n")
            f.write(f"**Prompt:**\n```\n{test_config.get('prompt', 'N/A')}\n```\n\n")
            f.write(f"**Expected Skills:** {', '.join(test_config.get('expected_skills', []))}\n")
            f.write(f"**Timeout:** {test_config.get('timeout_seconds', 120)}s\n\n")

            # Summary
            f.write("## Summary\n\n")
            skills = parser.get_skill_activations()
            tool_usage = parser.get_tool_usage()
            questions = parser.get_questions_asked()

            f.write(f"- **Skills Activated:** {', '.join(skills) if skills else 'None'}\n")
            f.write(f"- **Tools Used:** {len(tool_usage)}\n")
            f.write(f"- **Questions Asked:** {len(questions)}\n")
            f.write(f"- **Total Messages:** {len(parser.messages)}\n\n")

            # Tool usage breakdown
            if tool_usage:
                f.write("### Tool Usage\n\n")
                for tool, count in sorted(tool_usage.items(), key=lambda x: x[1], reverse=True):
                    f.write(f"- `{tool}`: {count} time(s)\n")
                f.write("\n")

            # Conversation
            f.write("## Conversation\n\n")

            for idx, msg in enumerate(parser.messages, 1):
                role = msg.role.upper()

                # Message header
                f.write(f"### {idx}. {role}\n\n")

                # Text content
                text = msg.text_content.strip()
                if text:
                    f.write(f"{text}\n\n")

                # Tool uses
                tools = msg.tool_uses
                if tools:
                    f.write("**Tools Used:**\n\n")
                    for tool in tools:
                        tool_name = tool.get('name', 'unknown')
                        tool_input = tool.get('input', {})

                        f.write(f"- **{tool_name}**\n")

                        # Show input in a compact way
                        if tool_input:
                            # Truncate large inputs
                            input_str = json.dumps(tool_input, indent=2)
                            if len(input_str) > 500:
                                input_str = input_str[:500] + "\n  ...(truncated)..."
                            f.write(f"  ```json\n  {input_str}\n  ```\n")
                        f.write("\n")

                # Questions
                questions_in_msg = msg.questions
                if questions_in_msg:
                    f.write("**Questions:**\n\n")
                    for q in questions_in_msg:
                        f.write(f"- {q.get('question', 'N/A')}\n")
                    f.write("\n")

                # Skill activations
                skill_acts = msg.skill_activations
                if skill_acts:
                    f.write(f"**✨ Skills Activated:** {', '.join(skill_acts)}\n\n")

                f.write("---\n\n")


if __name__ == "__main__":
    # Simple test
    if len(sys.argv) < 3:
        print("Usage: analyzer.py <transcript.jsonl> <test_config.yml>")
        sys.exit(1)

    transcript_path = Path(sys.argv[1])
    config_path = Path(sys.argv[2])

    if not transcript_path.exists():
        print(f"Transcript not found: {transcript_path}")
        sys.exit(1)

    if not config_path.exists():
        print(f"Config not found: {config_path}")
        sys.exit(1)

    # Load test config
    with open(config_path) as f:
        test_config = yaml.safe_load(f)

    # Analyze
    analyzer = TranscriptAnalyzer()
    result = analyzer.analyze_transcript(transcript_path, test_config, run_number=1)

    # Print results
    print("\nTest Analysis Results")
    print("=" * 60)
    print(f"Prompt: {result.prompt_name}")
    print(f"Success: {'✓' if result.success else '✗'}")
    print(f"Skills activated: {', '.join(result.skills_activated)}")
    print(f"Skill activation met: {'✓' if result.skill_activation_met else '✗'}")
    print(f"Questions asked: {result.questions_asked}")
    print(f"Errors: {len(result.errors)}")

    if result.errors:
        print("\nErrors found:")
        for error in result.errors:
            print(f"  - {error[:80]}...")
