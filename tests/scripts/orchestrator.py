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
import threading
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

from rich.console import Console

# Import our modules
sys.path.insert(0, str(Path(__file__).parent / "utils"))
from docker_manager import DockerManager, ContainerConfig

sys.path.insert(0, str(Path(__file__).parent))
from analyzer import TranscriptAnalyzer, TestResult
from reporter import Reporter
from test_runner import TestRunner, ExecutionStatus


class SimpleProgressTracker:
    """Thread-safe progress tracker for stdout output"""

    def __init__(self, verbose: bool = False):
        self.lock = threading.Lock()
        self.verbose = verbose
        self.prompt_status: Dict[str, Dict[int, str]] = {}  # {prompt_name: {run_num: status}}
        self.prompt_totals: Dict[str, int] = {}  # {prompt_name: total_runs}

    def init_prompt(self, prompt_name: str, total_runs: int):
        """Initialize tracking for a prompt"""
        with self.lock:
            self.prompt_status[prompt_name] = {}
            self.prompt_totals[prompt_name] = total_runs

    def mark_running(self, prompt_name: str, run_num: int, container_id: Optional[str] = None):
        """Mark a trial as running"""
        with self.lock:
            self.prompt_status[prompt_name][run_num] = "running"
            msg = f"[{prompt_name}] Trial {run_num}/{self.prompt_totals[prompt_name]}: Running..."
            if self.verbose and container_id:
                msg += f" (container: {container_id[:12]})"
            print(msg)
            sys.stdout.flush()

    def mark_complete(self, prompt_name: str, run_num: int, success: bool, exec_time: float,
                     errors: Optional[List[str]] = None):
        """Mark a trial as complete"""
        with self.lock:
            status = "✓ PASS" if success else "✗ FAIL"
            self.prompt_status[prompt_name][run_num] = status
            msg = f"[{prompt_name}] Trial {run_num}/{self.prompt_totals[prompt_name]}: {status} ({exec_time:.1f}s)"

            if self.verbose and errors:
                msg += f"\n  Errors: {', '.join(errors[:3])}"
                if len(errors) > 3:
                    msg += f" (+{len(errors)-3} more)"

            print(msg)
            sys.stdout.flush()

    def print_verbose(self, prompt_name: str, run_num: int, message: str):
        """Print verbose debug message"""
        if self.verbose:
            with self.lock:
                print(f"  [{prompt_name}] Trial {run_num}: {message}")
                sys.stdout.flush()

    def print_summary(self):
        """Print overall progress summary"""
        with self.lock:
            summaries = []
            for prompt_name in sorted(self.prompt_status.keys()):
                statuses = self.prompt_status[prompt_name]
                total = self.prompt_totals[prompt_name]
                passed = sum(1 for s in statuses.values() if s == "✓ PASS")
                pct = (passed / total * 100) if total > 0 else 0
                summaries.append(f"[{prompt_name}] {passed}/{total} passed ({pct:.0f}%)")

            print(f"\nProgress: {' | '.join(summaries)}\n")
            sys.stdout.flush()


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
        self.verbose = verbose
        self.override_runs = override_runs

        # Create single timestamp for this orchestrator run
        self.orchestrator_timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

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

    def cleanup_orphaned_containers(self) -> None:
        """Clean up orphaned containers from previous test runs"""
        self.console.print("[bold]Checking for orphaned containers...[/bold]")

        # Create a temporary DockerManager to check for orphans
        temp_manager = DockerManager(self.config_dir / "Dockerfile")

        # First, find orphaned containers
        orphaned = temp_manager.find_orphaned_containers()

        if not orphaned:
            self.console.print("[green]✓ No orphaned containers found[/green]")
            return

        # List what will be cleaned up
        self.console.print(f"[yellow]Found {len(orphaned)} orphaned container(s):[/yellow]")
        for container in orphaned:
            status = container.status
            self.console.print(f"  [dim]- {container.name} (status: {status})[/dim]")

        self.console.print("\n[bold]Cleaning up containers...[/bold]")

        # Define callback for verbose output
        def status_callback(message: str):
            if self.verbose:
                self.console.print(f"  [dim]{message}[/dim]")

        # Clean them up with progress feedback
        count, cleaned_names = temp_manager.cleanup_orphaned_containers(
            verbose_callback=status_callback
        )

        if count > 0:
            self.console.print(f"[green]✓ Successfully removed {count} container(s)[/green]")
        else:
            self.console.print("[yellow]⚠ No containers were removed[/yellow]")

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
            project_root=self.project_root,
            verbose=self.verbose
        )

        return True

    def execute_single_run(self, test_run: TestRun, tracker: SimpleProgressTracker) -> TestResult:
        """
        Execute and analyze a single test run

        This delegates execution to TestRunner, then analyzes the artifact.

        Args:
            test_run: TestRun configuration
            tracker: Progress tracker for stdout output

        Returns:
            TestResult object from analysis
        """
        prompt_name = test_run.prompt_config.get("name", "unknown")

        # Mark as running
        tracker.mark_running(prompt_name, test_run.run_number)

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

                # Mark as complete via tracker
                tracker.mark_complete(
                    prompt_name,
                    test_run.run_number,
                    result.success,
                    artifact.execution_time,
                    result.errors if not result.success else None
                )

                return result
            else:
                # No transcript - create failed result
                result = TestResult(
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

                # Mark as complete (failed) via tracker
                tracker.mark_complete(
                    prompt_name,
                    test_run.run_number,
                    False,
                    artifact.execution_time,
                    result.errors
                )

                return result

        except Exception as e:
            if self.verbose:
                import traceback
                self.console.print(f"[red]Traceback:\n{traceback.format_exc()}[/red]")

            result = TestResult(
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

            # Mark as complete (error) via tracker
            tracker.mark_complete(
                prompt_name,
                test_run.run_number,
                False,
                0.0,  # No execution time available
                result.errors
            )

            return result

    def create_test_run(
        self,
        prompt_config: Dict[str, Any],
        run_num: int
    ) -> TestRun:
        """Create a TestRun configuration"""
        prompt_name = prompt_config.get("name", "unknown")
        # Still need unique timestamp for container name to avoid conflicts
        container_timestamp = int(time.time() * 1000)

        # New hierarchical structure: {prompt-name}/{orchestrator-timestamp}/trial-{N}/
        base_dir = self.results_dir / prompt_name / self.orchestrator_timestamp
        trial_dir = base_dir / f"trial-{run_num}"

        return TestRun(
            prompt_config=prompt_config,
            run_number=run_num,
            container_name=f"test-{prompt_name}-{run_num}-{container_timestamp}",
            transcript_dir=trial_dir / "transcript",
            artifacts_path=trial_dir / "artifact"
        )

    def run_tests(self, max_workers: int = 6) -> Dict[str, Any]:
        """Run all tests with parallel execution at the individual run level"""
        start_time = time.time()

        # Clean up orphaned containers first
        self.cleanup_orphaned_containers()
        self.console.print()

        # Load prompts
        self.console.print("[bold]Loading test prompts...[/bold]")
        prompts = self.load_test_prompts()
        self.console.print(f"Found {len(prompts)} test prompt(s)")

        if not prompts:
            self.console.print("[red]No test prompts found![/red]")
            return {}

        # Setup Docker
        if not self.setup_docker():
            return {}

        # Calculate total runs across all prompts
        total_runs = sum(prompt.get("runs", 3) for prompt in prompts)
        self.console.print(f"\n[bold]Running {total_runs} test runs across {len(prompts)} prompt(s) (max {max_workers} parallel)...[/bold]\n")

        # Create all test runs upfront
        all_test_runs = []
        prompt_run_map = {}  # Map test_run to prompt_config

        for prompt_config in prompts:
            num_runs = prompt_config.get("runs", 3)
            for run_num in range(1, num_runs + 1):
                test_run = self.create_test_run(prompt_config, run_num)
                all_test_runs.append(test_run)
                prompt_run_map[id(test_run)] = prompt_config
                # Small delay to ensure unique timestamps
                time.sleep(0.001)

        # Execute all runs in parallel
        results_by_prompt = {prompt["name"]: [] for prompt in prompts}

        # Create simple progress tracker
        tracker = SimpleProgressTracker(verbose=self.verbose)
        for prompt_config in prompts:
            tracker.init_prompt(prompt_config["name"], prompt_config.get("runs", 3))

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all individual test runs
            futures = {
                executor.submit(self.execute_single_run, test_run, tracker): test_run
                for test_run in all_test_runs
            }

            # Process results as they complete
            for future in as_completed(futures):
                test_run = futures[future]
                prompt_config = prompt_run_map[id(test_run)]
                prompt_name = prompt_config["name"]

                try:
                    result = future.result()
                    results_by_prompt[prompt_name].append(result)

                except Exception as e:
                    print(f"[{prompt_name}] Trial {test_run.run_number}: ERROR - {e}")
                    sys.stdout.flush()

        # Print progress summary
        tracker.print_summary()

        # Organize results by prompt
        all_results = [
            {
                "config": prompt_config,
                "results": results_by_prompt[prompt_config["name"]]
            }
            for prompt_config in prompts
        ]

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

        # Use orchestrator timestamp for reports (consistent with test run directories)
        json_path = self.results_dir / "reports" / f"results-{self.orchestrator_timestamp}.json"
        md_path = self.results_dir / "reports" / f"results-{self.orchestrator_timestamp}.md"

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
