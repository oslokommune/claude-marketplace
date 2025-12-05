#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rich",
# ]
# ///

"""
Reporter - Generate test reports

Creates formatted reports from test results in multiple formats:
- Console (Rich formatted)
- JSON (for CI/CD)
- Markdown (for GitHub)
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

# Import analyzer types
sys.path.insert(0, str(Path(__file__).parent))
from analyzer import AggregatedResult


class Reporter:
    """Generate test reports in various formats"""

    def __init__(self):
        self.console = Console()

    def print_console_report(
        self,
        results: List[AggregatedResult],
        total_time: float
    ) -> None:
        """
        Print a formatted console report

        Args:
            results: List of aggregated results
            total_time: Total execution time in seconds
        """
        # Header
        self.console.print()
        self.console.print(
            Panel.fit(
                "[bold]Plugin Testing Framework - Results[/bold]",
                border_style="blue"
            )
        )
        self.console.print()

        # Summary table
        table = Table(
            title="Test Summary",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold cyan"
        )

        table.add_column("Prompt", style="white", no_wrap=True)
        table.add_column("Runs", justify="center")
        table.add_column("Success Rate", justify="center")
        table.add_column("Skill Activation", justify="center")
        table.add_column("Result", justify="center")

        total_tests = 0
        passed_tests = 0

        for result in results:
            total_tests += 1
            if result.passed:
                passed_tests += 1

            # Format success rate
            success_rate = f"{result.success_rate * 100:.0f}%"

            # Format skill activation
            skill_rate = f"{result.skill_activation_rate * 100:.0f}%"
            expected_rate = f"{result.expected_skill_activation_rate * 100:.0f}%"
            skill_activation = f"{skill_rate} / {expected_rate}"

            # Status emoji
            status = "✓" if result.passed else "✗"
            status_style = "green" if result.passed else "red"

            table.add_row(
                result.prompt_name,
                f"{result.successful_runs}/{result.total_runs}",
                success_rate,
                skill_activation,
                f"[{status_style}]{status}[/{status_style}]"
            )

        self.console.print(table)
        self.console.print()

        # Overall summary
        overall_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        overall_status = "PASSED" if overall_rate >= 95 else "FAILED"
        overall_color = "green" if overall_rate >= 95 else "red"

        summary_text = f"""
[bold]Overall Results:[/bold]
  Total Prompts: {total_tests}
  Passed: {passed_tests}
  Failed: {total_tests - passed_tests}
  Success Rate: {overall_rate:.1f}%
  Total Time: {total_time:.1f}s

[bold {overall_color}]Status: {overall_status}[/bold {overall_color}]
        """

        self.console.print(Panel(summary_text.strip(), border_style=overall_color))
        self.console.print()

        # Detailed failures
        failed_results = [r for r in results if not r.passed]
        if failed_results:
            self.console.print("[bold red]Failed Tests:[/bold red]")
            for result in failed_results:
                self.console.print(f"\n[red]✗ {result.prompt_name}[/red]")
                self.console.print(f"  Skill activation: {result.skill_activation_rate * 100:.0f}% (expected: {result.expected_skill_activation_rate * 100:.0f}%)")

                if result.common_errors:
                    self.console.print("  [dim]Common errors:[/dim]")
                    for error in result.common_errors[:3]:
                        self.console.print(f"    - {error[:80]}...")

    def generate_json_report(
        self,
        results: List[AggregatedResult],
        output_path: Path,
        total_time: float
    ) -> None:
        """
        Generate JSON report for CI/CD

        Args:
            results: List of aggregated results
            output_path: Where to save the JSON
            total_time: Total execution time
        """
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_time_seconds": total_time,
            "summary": {
                "total_prompts": len(results),
                "passed": sum(1 for r in results if r.passed),
                "failed": sum(1 for r in results if not r.passed),
                "success_rate": sum(1 for r in results if r.passed) / len(results) if results else 0
            },
            "results": []
        }

        for result in results:
            report["results"].append({
                "prompt_name": result.prompt_name,
                "passed": result.passed,
                "total_runs": result.total_runs,
                "successful_runs": result.successful_runs,
                "success_rate": result.success_rate,
                "skill_activation_rate": result.skill_activation_rate,
                "expected_skill_activation_rate": result.expected_skill_activation_rate,
                "common_errors": result.common_errors,
                "runs": [
                    {
                        "run_number": run.run_number,
                        "success": run.success,
                        "skills_activated": run.skills_activated,
                        "skill_activation_met": run.skill_activation_met,
                        "questions_asked": run.questions_asked,
                        "errors": run.errors,
                        "transcript_path": run.transcript_path
                    }
                    for run in result.runs
                ]
            })

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)

        self.console.print(f"[dim]JSON report saved to: {output_path}[/dim]")

    def generate_markdown_report(
        self,
        results: List[AggregatedResult],
        output_path: Path,
        total_time: float
    ) -> None:
        """
        Generate Markdown report for GitHub

        Args:
            results: List of aggregated results
            output_path: Where to save the Markdown
            total_time: Total execution time
        """
        passed = sum(1 for r in results if r.passed)
        total = len(results)
        success_rate = (passed / total * 100) if total > 0 else 0

        md_content = f"""# Plugin Testing Framework - Results

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Total Time:** {total_time:.1f}s
**Status:** {"✅ PASSED" if success_rate >= 95 else "❌ FAILED"}

## Summary

- **Total Prompts:** {total}
- **Passed:** {passed}
- **Failed:** {total - passed}
- **Success Rate:** {success_rate:.1f}%

## Test Results

| Prompt | Runs | Success Rate | Skill Activation | Status |
|--------|------|--------------|------------------|--------|
"""

        for result in results:
            status = "✅" if result.passed else "❌"
            success = f"{result.success_rate * 100:.0f}%"
            skill = f"{result.skill_activation_rate * 100:.0f}% / {result.expected_skill_activation_rate * 100:.0f}%"

            md_content += f"| {result.prompt_name} | {result.successful_runs}/{result.total_runs} | {success} | {skill} | {status} |\n"

        # Failed tests section
        failed_results = [r for r in results if not r.passed]
        if failed_results:
            md_content += "\n## Failed Tests\n\n"

            for result in failed_results:
                md_content += f"### ❌ {result.prompt_name}\n\n"
                md_content += f"- **Skill Activation:** {result.skill_activation_rate * 100:.0f}% (expected: {result.expected_skill_activation_rate * 100:.0f}%)\n"
                md_content += f"- **Successful Runs:** {result.successful_runs}/{result.total_runs}\n"

                if result.common_errors:
                    md_content += "\n**Errors:**\n"
                    for error in result.common_errors[:3]:
                        md_content += f"- `{error[:80]}...`\n"

                md_content += "\n"

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(md_content)

        self.console.print(f"[dim]Markdown report saved to: {output_path}[/dim]")


if __name__ == "__main__":
    # Simple test with mock data
    from analyzer import AggregatedResult, TestResult

    mock_result = AggregatedResult(
        prompt_name="test-prompt",
        total_runs=3,
        successful_runs=3,
        success_rate=1.0,
        skill_activation_rate=1.0,
        expected_skill_activation_rate=0.95,
        passed=True,
        runs=[],
        common_errors=[]
    )

    reporter = Reporter()
    reporter.print_console_report([mock_result], total_time=120.5)
