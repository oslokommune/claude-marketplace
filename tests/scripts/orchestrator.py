#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "docker",
#     "pyyaml",
#     "rich",
# ]
# ///

"""
Simplified Test Orchestrator - Using claude -p for non-interactive execution

This simplified version eliminates tmux complexity and uses Claude Code's
native non-interactive mode with -p flag.
"""

import sys
import time
import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

# Import our modules
sys.path.insert(0, str(Path(__file__).parent / "utils"))
from docker_manager import DockerManager, ContainerConfig

sys.path.insert(0, str(Path(__file__).parent))
from analyzer import TranscriptAnalyzer, TestResult
from reporter import Reporter
from test_runner import TestRunner, ExecutionStatus


@dataclass
class TestRun:
    """Represents a single test run"""
    prompt_config: Dict[str, Any]
    run_number: int
    container_name: str
    transcript_dir: Path
    artifacts_path: Path


class SimplifiedOrchestrator:
    """Simplified orchestrator using claude -p"""

    def __init__(self, project_root: Path, verbose: bool = False, override_runs: Optional[int] = None):
        self.project_root = Path(project_root)
        self.tests_dir = self.project_root / "tests"
        self.prompts_dir = self.tests_dir / "prompts"
        self.results_dir = self.tests_dir / "results"
        self.config_dir = self.tests_dir / "config" / "docker"
        self.plugins_dir = self.project_root / "plugins"
        self.verbose = verbose
        self.override_runs = override_runs

        self.console = Console()
        self.docker_manager: Optional[DockerManager] = None
        self.test_runner: Optional[TestRunner] = None
        self.analyzer = TranscriptAnalyzer()
        self.reporter = Reporter()

    def debug(self, message: str):
        """Print debug message if verbose mode is enabled"""
        if self.verbose:
            self.console.print(f"[dim][DEBUG] {message}[/dim]")

    def load_test_prompts(self) -> List[Dict[str, Any]]:
        """Load all test prompt YAML files"""
        prompts = []

        for category_dir in self.prompts_dir.iterdir():
            if not category_dir.is_dir():
                continue

            for prompt_file in category_dir.glob("*.yml"):
                try:
                    with open(prompt_file) as f:
                        config = yaml.safe_load(f)

                        # Override runs if specified
                        if self.override_runs is not None:
                            config['runs'] = self.override_runs
                            self.debug(f"Override runs for {config['name']}: {self.override_runs}")

                        prompts.append(config)
                        self.debug(f"Loaded prompt: {config['name']} ({config.get('runs', 3)} runs)")
                except Exception as e:
                    self.console.print(f"[yellow]Warning: Failed to load {prompt_file}: {e}[/yellow]")

        return prompts

    def setup_docker(self) -> bool:
        """Build Docker image and initialize TestRunner"""
        dockerfile = self.config_dir / "Dockerfile"

        if not dockerfile.exists():
            self.console.print(f"[red]Dockerfile not found: {dockerfile}[/red]")
            return False

        self.docker_manager = DockerManager(dockerfile)

        self.console.print("[bold]Building Docker image...[/bold]")
        if not self.docker_manager.build_image():
            self.console.print("[red]Failed to build Docker image[/red]")
            return False

        self.console.print("[green]✓ Docker image built successfully[/green]")

        # Initialize TestRunner
        self.test_runner = TestRunner(
            docker_manager=self.docker_manager,
            plugins_dir=self.plugins_dir,
            verbose=self.verbose
        )

        return True

    def execute_single_run(self, test_run: TestRun) -> TestResult:
        """
        Execute and analyze a single test run

        This delegates execution to TestRunner, then analyzes the artifact.

        Args:
            test_run: TestRun configuration

        Returns:
            TestResult object from analysis
        """
        prompt_name = test_run.prompt_config.get("name", "unknown")

        try:
            # Step 1: Execute using TestRunner
            artifact = self.test_runner.execute_test_run(
                prompt_config=test_run.prompt_config,
                run_number=test_run.run_number,
                transcript_dir=test_run.transcript_dir,
                artifacts_dir=test_run.artifacts_path
            )

            # Step 2: Analyze transcript if available
            if artifact.transcript_path and artifact.transcript_path.exists():
                result = self.analyzer.analyze_transcript(
                    artifact.transcript_path,
                    test_run.prompt_config,
                    test_run.run_number
                )

                # Add execution time to result
                result.execution_time = artifact.execution_time

                status = "✓ PASS" if result.success else "✗ FAIL"
                color = "green" if result.success else "red"
                self.console.print(f"[{color}][{prompt_name}] Run {test_run.run_number}: {status}[/{color}]")

                return result
            else:
                # No transcript - create failed result
                self.console.print(f"[red][{prompt_name}] No transcript created![/red]")

                return TestResult(
                    prompt_name=prompt_name,
                    run_number=test_run.run_number,
                    success=False,
                    skills_activated=[],
                    expected_skills=test_run.prompt_config.get("expected_skills", []),
                    skill_activation_met=False,
                    tool_usage={},
                    questions_asked=0,
                    errors=artifact.execution_errors or ["No transcript created"],
                    transcript_path=str(test_run.transcript_dir),
                    execution_time=artifact.execution_time
                )

        except Exception as e:
            self.console.print(f"[red][{prompt_name}] Error: {e}[/red]")

            if self.verbose:
                import traceback
                self.console.print(f"[red]Traceback:\n{traceback.format_exc()}[/red]")

            return TestResult(
                prompt_name=prompt_name,
                run_number=test_run.run_number,
                success=False,
                skills_activated=[],
                expected_skills=test_run.prompt_config.get("expected_skills", []),
                skill_activation_met=False,
                tool_usage={},
                questions_asked=0,
                errors=[str(e)],
                transcript_path=str(test_run.transcript_dir)
            )

    def execute_prompt_tests(
        self,
        prompt_config: Dict[str, Any],
        progress: Progress,
        task_id: Any
    ) -> List[TestResult]:
        """Execute all runs for a single prompt"""
        results = []
        num_runs = prompt_config.get("runs", 3)
        prompt_name = prompt_config.get("name", "unknown")

        for run_num in range(1, num_runs + 1):
            progress.update(
                task_id,
                completed=run_num - 1,
                description=f"[cyan]{prompt_name}[/cyan] ({run_num}/{num_runs})"
            )

            timestamp = int(time.time() * 1000)
            test_run = TestRun(
                prompt_config=prompt_config,
                run_number=run_num,
                container_name=f"test-{prompt_name}-{run_num}-{timestamp}",
                transcript_dir=self.results_dir / "transcripts" / f"{prompt_name}-{run_num}-{timestamp}",
                artifacts_path=self.results_dir / "artifacts" / f"{prompt_name}-{run_num}"
            )

            result = self.execute_single_run(test_run)
            results.append(result)

            progress.update(task_id, completed=run_num)

        return results

    def run_tests(self, max_workers: int = 6) -> Dict[str, Any]:
        """Run all tests with parallel execution"""
        start_time = time.time()

        # Load prompts
        self.console.print("\n[bold]Loading test prompts...[/bold]")
        prompts = self.load_test_prompts()
        self.console.print(f"Found {len(prompts)} test prompt(s)")

        if not prompts:
            self.console.print("[red]No test prompts found![/red]")
            return {}

        # Setup Docker
        if not self.setup_docker():
            return {}

        # Run tests in parallel
        self.console.print(f"\n[bold]Running tests (max {max_workers} parallel)...[/bold]\n")

        all_results = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=self.console
        ) as progress:

            tasks = {}
            for prompt_config in prompts:
                num_runs = prompt_config.get("runs", 3)
                task_id = progress.add_task(
                    f"[cyan]{prompt_config['name']}[/cyan]",
                    total=num_runs
                )
                tasks[prompt_config["name"]] = task_id

            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {
                    executor.submit(
                        self.execute_prompt_tests,
                        prompt_config,
                        progress,
                        tasks[prompt_config["name"]]
                    ): prompt_config
                    for prompt_config in prompts
                }

                for future in as_completed(futures):
                    prompt_config = futures[future]
                    try:
                        results = future.result()
                        all_results.append({
                            "config": prompt_config,
                            "results": results
                        })
                    except Exception as e:
                        self.console.print(f"[red]Error executing {prompt_config['name']}: {e}[/red]")

        # Aggregate results
        self.console.print("\n[bold]Analyzing results...[/bold]")
        aggregated_results = []

        for item in all_results:
            aggregated = self.analyzer.aggregate_results(
                item["results"],
                item["config"]
            )
            aggregated_results.append(aggregated)

        total_time = time.time() - start_time

        # Generate reports
        self.console.print()
        self.reporter.print_console_report(aggregated_results, total_time)

        timestamp = int(time.time())
        json_path = self.results_dir / "reports" / f"results-{timestamp}.json"
        md_path = self.results_dir / "reports" / f"results-{timestamp}.md"

        self.reporter.generate_json_report(aggregated_results, json_path, total_time)
        self.reporter.generate_markdown_report(aggregated_results, md_path, total_time)

        return {
            "aggregated_results": aggregated_results,
            "total_time": total_time
        }


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description="Simplified Plugin Testing Framework")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose debug output")
    parser.add_argument("-r", "--runs", type=int, help="Override number of runs per prompt")
    parser.add_argument("-w", "--workers", type=int, default=6, help="Max parallel workers (default: 6)")
    args = parser.parse_args()

    console = Console()

    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent

    console.print("\n[bold blue]Simplified Plugin Testing Framework[/bold blue]\n")

    if args.verbose:
        console.print("[dim]Verbose mode enabled[/dim]")
    if args.runs:
        console.print(f"[dim]Override runs per prompt: {args.runs}[/dim]")
    console.print()

    orchestrator = SimplifiedOrchestrator(project_root, verbose=args.verbose, override_runs=args.runs)
    results = orchestrator.run_tests(max_workers=args.workers)

    if results:
        aggregated = results.get("aggregated_results", [])
        passed = sum(1 for r in aggregated if r.passed)
        total = len(aggregated)

        sys.exit(0 if passed == total else 1)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
