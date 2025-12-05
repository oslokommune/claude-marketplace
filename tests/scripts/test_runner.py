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
Test Runner - Execute individual Claude Code tests in Docker containers

This module handles the execution of single test runs:
- Creates and manages Docker containers
- Executes claude -p with the test prompt
- Collects transcripts and artifacts
- Returns structured execution results for analysis

Design for debuggability:
- Verbose logging at every step
- Detailed error messages with context
- Preserves all output (stdout, stderr, logs)
- Clear status reporting
"""

import sys
import time
import json
import threading
from pathlib import Path
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, asdict
from enum import Enum

from rich.console import Console
from rich.panel import Panel

# Import Docker manager
sys.path.insert(0, str(Path(__file__).parent / "utils"))
from docker_manager import DockerManager, ContainerConfig


class ExecutionStatus(Enum):
    """Status of test execution"""
    SUCCESS = "success"
    FAILED = "failed"
    ERROR = "error"
    TIMEOUT = "timeout"


@dataclass
class TestExecutionArtifact:
    """
    Complete artifact from a single test execution

    This contains all raw data from the execution, without any analysis.
    The orchestrator will pass this to the analyzer for validation.
    """
    # Execution metadata
    run_number: int
    prompt_name: str
    prompt_text: str
    container_name: str
    status: ExecutionStatus
    execution_time: float

    # Container execution results
    exit_code: int
    stdout: str
    stderr: str

    # Collected files
    transcript_path: Optional[Path]
    transcript_size: int
    artifacts_dir: Path
    artifact_files: List[str]  # List of files found in artifacts_dir

    # Execution errors (not test validation errors)
    execution_errors: List[str]

    # Debug information
    container_logs: str
    claude_command: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        data = asdict(self)
        # Convert Path objects to strings
        data['transcript_path'] = str(self.transcript_path) if self.transcript_path else None
        data['artifacts_dir'] = str(self.artifacts_dir)
        data['status'] = self.status.value
        return data

    def save_to_file(self, output_path: Path) -> None:
        """Save artifact as JSON for debugging"""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)


class TestRunner:
    """
    Execute individual test runs in Docker containers

    This class is responsible for:
    1. Creating isolated Docker containers
    2. Running claude -p with test prompts
    3. Collecting all output and artifacts
    4. Cleaning up containers

    It does NOT perform any test validation - that's the analyzer's job.
    """

    def __init__(
        self,
        docker_manager: DockerManager,
        plugins_dir: Path,
        verbose: bool = False
    ):
        """
        Initialize test runner

        Args:
            docker_manager: Configured DockerManager instance
            plugins_dir: Path to plugins directory to mount
            verbose: Enable detailed debug output
        """
        self.docker_manager = docker_manager
        self.plugins_dir = Path(plugins_dir)
        self.verbose = verbose
        self.console = Console()

    def debug(self, message: str, style: str = "dim"):
        """Print debug message if verbose mode is enabled"""
        if self.verbose:
            self.console.print(f"[{style}][DEBUG] {message}[/{style}]")

    def info(self, message: str):
        """Print info message"""
        self.console.print(f"[cyan]{message}[/cyan]")

    def error(self, message: str):
        """Print error message"""
        self.console.print(f"[red]ERROR: {message}[/red]")

    def execute_test_run(
        self,
        prompt_config: Dict[str, Any],
        run_number: int,
        transcript_dir: Path,
        artifacts_dir: Path
    ) -> TestExecutionArtifact:
        """
        Execute a single test run

        Args:
            prompt_config: Test configuration from YAML (name, prompt, timeout, etc.)
            run_number: Which run number this is (for multi-run tests)
            transcript_dir: Where to mount Claude's transcript directory
            artifacts_dir: Where to collect artifact files

        Returns:
            TestExecutionArtifact with all execution results
        """
        prompt_name = prompt_config.get("name", "unknown")
        prompt_text = prompt_config.get("prompt", "")
        timeout = prompt_config.get("timeout_seconds", 120)

        start_time = time.time()
        container = None
        execution_errors = []
        container_logs = ""

        # Generate container name with timestamp for uniqueness
        timestamp = int(time.time() * 1000)
        container_name = f"test-{prompt_name}-{run_number}-{timestamp}"

        self.debug(f"Starting execution: {prompt_name} (run {run_number})")
        self.debug(f"Container name: {container_name}")
        self.debug(f"Transcript dir: {transcript_dir}")
        self.debug(f"Artifacts dir: {artifacts_dir}")

        try:
            # Step 1: Create directories
            self.debug("Creating directories...")
            transcript_dir.mkdir(parents=True, exist_ok=True)
            artifacts_dir.mkdir(parents=True, exist_ok=True)

            # Step 2: Create container config
            self.debug("Creating container configuration...")

            # Look for .devcontainer/devcontainer.env file
            import os
            env_file = None
            project_root = self.plugins_dir.parent
            devcontainer_env = project_root / ".devcontainer" / "devcontainer.env"

            if devcontainer_env.exists():
                env_file = devcontainer_env
                self.debug(f"Using env file: {env_file}")
            else:
                self.debug(f"No env file found at: {devcontainer_env}")

            config = ContainerConfig(
                name=container_name,
                plugins_dir=self.plugins_dir,
                transcript_dir=transcript_dir,
                artifacts_dir=artifacts_dir,
                env_vars={},  # env_file will provide the vars
                env_file=env_file
            )

            # Step 3: Create container
            self.debug("Creating Docker container...")
            container = self.docker_manager.create_container(config)

            if not container:
                raise Exception("Failed to create container - docker_manager returned None")

            self.debug(f"Container created: {container.id[:12]}")

            # Step 4: Start container
            self.debug("Starting container...")
            if not self.docker_manager.start_container(container):
                raise Exception("Failed to start container")

            self.debug("Container started successfully")

            # Step 5: Execute claude -p command with timeout
            # Note: To avoid shell escaping issues, we pass the prompt directly as argv
            # instead of going through bash -c with a string
            self.debug(f"Executing claude -p with prompt: {prompt_text[:100]}...")
            self.info(f"[{prompt_name}] Running Claude Code (timeout: {timeout}s)...")

            # Execute with timeout using threading
            exec_start = time.time()
            exit_code = -1
            output = b""
            exec_error = None
            timed_out = False

            def run_exec():
                nonlocal exit_code, output, exec_error
                try:
                    # Pass prompt directly as argument to avoid escaping issues
                    # Use stdin=/dev/null to prevent hanging on input prompts
                    exit_code, output = container.exec_run(
                        cmd=["bash", "-c", "claude -p \"$@\" < /dev/null", "bash", prompt_text],
                        user="node",
                        workdir="/workspace",
                        demux=False,
                        stream=False,
                        tty=False,
                        stdin=False
                    )
                except Exception as e:
                    exec_error = e

            exec_thread = threading.Thread(target=run_exec, daemon=True)
            exec_thread.start()
            exec_thread.join(timeout=timeout)

            exec_time = time.time() - exec_start

            # Check if execution timed out
            if exec_thread.is_alive():
                timed_out = True
                self.error(f"[{prompt_name}] Execution timed out after {timeout}s")
                execution_errors.append(f"Execution timed out after {timeout}s")

                # Try to stop the container to kill the process
                try:
                    self.debug("Stopping container due to timeout...")
                    self.docker_manager.stop_container(container, timeout=5)
                except Exception as e:
                    self.debug(f"Error stopping container: {e}")
            elif exec_error:
                self.error(f"[{prompt_name}] Execution error: {exec_error}")
                execution_errors.append(f"Execution error: {exec_error}")
            else:
                self.debug(f"Execution completed in {exec_time:.1f}s with exit code: {exit_code}")

            # Decode output
            stdout = output.decode('utf-8', errors='ignore') if output else ""
            stderr = ""  # exec_run doesn't separate stderr when demux=False

            if self.verbose:
                self.debug("=== Command Output ===")
                self.console.print(f"[dim]{stdout[:500]}{'...' if len(stdout) > 500 else ''}[/dim]")

            # Step 6: Collect container logs
            self.debug("Collecting container logs...")
            try:
                container_logs = container.logs().decode('utf-8', errors='ignore')
                if self.verbose and container_logs:
                    self.debug("=== Container Logs ===")
                    self.console.print(f"[dim]{container_logs[:500]}{'...' if len(container_logs) > 500 else ''}[/dim]")
            except Exception as e:
                self.debug(f"Failed to collect container logs: {e}")
                container_logs = f"Error collecting logs: {e}"

            # Step 7: Find transcript file
            self.debug("Looking for transcript file...")
            transcript_path = None
            transcript_size = 0

            # Claude writes to ~/.claude/projects/<project-name>/
            # Since we're in /workspace, it creates -workspace directory
            workspace_transcript_dir = transcript_dir / "-workspace"

            self.debug(f"Checking for transcripts in: {workspace_transcript_dir}")

            if workspace_transcript_dir.exists():
                jsonl_files = list(workspace_transcript_dir.glob("*.jsonl"))
                self.debug(f"Found {len(jsonl_files)} JSONL files")

                if jsonl_files:
                    # Get the most recent one
                    transcript_path = max(jsonl_files, key=lambda p: p.stat().st_mtime)
                    transcript_size = transcript_path.stat().st_size
                    self.debug(f"Transcript found: {transcript_path.name} ({transcript_size} bytes)")
                else:
                    self.debug("No JSONL files found in workspace directory")
                    execution_errors.append("No transcript file created")
            else:
                self.debug(f"Workspace transcript directory doesn't exist: {workspace_transcript_dir}")
                execution_errors.append(f"Transcript directory not created: {workspace_transcript_dir}")

            # Step 8: Collect artifact files
            self.debug("Collecting artifact files...")
            artifact_files = []

            if artifacts_dir.exists():
                for file_path in artifacts_dir.rglob("*"):
                    if file_path.is_file():
                        rel_path = file_path.relative_to(artifacts_dir)
                        artifact_files.append(str(rel_path))

                self.debug(f"Found {len(artifact_files)} artifact files")
                if self.verbose and artifact_files:
                    for af in artifact_files[:10]:  # Show first 10
                        self.debug(f"  - {af}")

            # Step 9: Determine execution status
            execution_time = time.time() - start_time

            if timed_out:
                status = ExecutionStatus.TIMEOUT
                self.console.print(f"[red]⏱ [{prompt_name}] Timed out after {timeout}s[/red]")
            elif exit_code == 0 and transcript_path:
                status = ExecutionStatus.SUCCESS
                self.console.print(f"[green]✓ [{prompt_name}] Completed successfully ({execution_time:.1f}s)[/green]")
            elif exit_code != 0:
                status = ExecutionStatus.FAILED
                if exit_code != -1:  # Only add if we got a real exit code
                    execution_errors.append(f"Non-zero exit code: {exit_code}")
                self.console.print(f"[yellow]⚠ [{prompt_name}] Completed with exit code {exit_code} ({execution_time:.1f}s)[/yellow]")
            else:
                status = ExecutionStatus.ERROR
                self.console.print(f"[red]✗ [{prompt_name}] Completed with errors ({execution_time:.1f}s)[/red]")

            # Create artifact
            artifact = TestExecutionArtifact(
                run_number=run_number,
                prompt_name=prompt_name,
                prompt_text=prompt_text,
                container_name=container_name,
                status=status,
                execution_time=execution_time,
                exit_code=exit_code,
                stdout=stdout,
                stderr=stderr,
                transcript_path=transcript_path,
                transcript_size=transcript_size,
                artifacts_dir=artifacts_dir,
                artifact_files=artifact_files,
                execution_errors=execution_errors,
                container_logs=container_logs,
                claude_command=f"claude -p <prompt:{len(prompt_text)} chars>"
            )

            return artifact

        except Exception as e:
            # Handle any execution errors
            execution_time = time.time() - start_time
            self.error(f"[{prompt_name}] Execution failed: {e}")

            if self.verbose:
                import traceback
                self.console.print(f"[red]{traceback.format_exc()}[/red]")

            execution_errors.append(str(e))

            # Try to collect container logs even on failure
            if container:
                try:
                    container_logs = container.logs().decode('utf-8', errors='ignore')
                except:
                    container_logs = "Failed to collect logs"

            # Return error artifact
            return TestExecutionArtifact(
                run_number=run_number,
                prompt_name=prompt_name,
                prompt_text=prompt_text,
                container_name=container_name,
                status=ExecutionStatus.ERROR,
                execution_time=execution_time,
                exit_code=-1,
                stdout="",
                stderr="",
                transcript_path=None,
                transcript_size=0,
                artifacts_dir=artifacts_dir,
                artifact_files=[],
                execution_errors=execution_errors,
                container_logs=container_logs,
                claude_command=f"claude -p <prompt:{len(prompt_text)} chars>"
            )

        finally:
            # Always cleanup container
            if container:
                self.debug("Cleaning up container...")
                try:
                    self.docker_manager.stop_container(container, timeout=5)
                    self.docker_manager.remove_container(container, force=True)
                    self.debug("Container cleaned up successfully")
                except Exception as e:
                    self.error(f"Failed to cleanup container: {e}")


def main():
    """
    Standalone CLI for testing single test runs

    This is useful for debugging test execution without running the full orchestrator.

    Usage:
        python test_runner.py <prompt_yaml> [--run-number N] [--verbose]
    """
    import argparse
    import yaml

    parser = argparse.ArgumentParser(
        description="Execute a single Claude Code test run",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run a test with verbose output
  python test_runner.py prompts/basic/hello.yml --verbose

  # Run a specific run number
  python test_runner.py prompts/basic/hello.yml --run-number 2

  # Save artifact for debugging
  python test_runner.py prompts/basic/hello.yml --save-artifact artifact.json
        """
    )

    parser.add_argument("prompt_file", type=Path, help="Path to prompt YAML file")
    parser.add_argument("-n", "--run-number", type=int, default=1, help="Run number (default: 1)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose debug output")
    parser.add_argument("--save-artifact", type=Path, help="Save execution artifact to JSON file")
    parser.add_argument("--transcript-dir", type=Path, help="Custom transcript directory (default: tests/results/transcripts)")
    parser.add_argument("--artifacts-dir", type=Path, help="Custom artifacts directory (default: tests/results/artifacts)")

    args = parser.parse_args()

    console = Console()

    # Validate prompt file
    if not args.prompt_file.exists():
        console.print(f"[red]Error: Prompt file not found: {args.prompt_file}[/red]")
        sys.exit(1)

    # Load prompt config
    console.print(f"\n[bold]Loading prompt configuration...[/bold]")
    with open(args.prompt_file) as f:
        prompt_config = yaml.safe_load(f)

    console.print(f"  Prompt: [cyan]{prompt_config.get('name', 'unknown')}[/cyan]")
    console.print(f"  Timeout: {prompt_config.get('timeout_seconds', 120)}s")
    console.print()

    # Setup paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    tests_dir = project_root / "tests"

    transcript_dir = args.transcript_dir or (tests_dir / "results" / "transcripts" / f"debug-{int(time.time())}")
    artifacts_dir = args.artifacts_dir or (tests_dir / "results" / "artifacts" / f"debug-{int(time.time())}")

    # Setup Docker
    console.print("[bold]Setting up Docker...[/bold]")
    dockerfile = tests_dir / "config" / "docker" / "Dockerfile"

    if not dockerfile.exists():
        console.print(f"[red]Error: Dockerfile not found: {dockerfile}[/red]")
        sys.exit(1)

    docker_manager = DockerManager(dockerfile)

    console.print("Building Docker image...")
    if not docker_manager.build_image():
        console.print("[red]Failed to build Docker image[/red]")
        sys.exit(1)

    console.print("[green]✓ Docker image ready[/green]\n")

    # Create test runner
    plugins_dir = project_root / "plugins"
    test_runner = TestRunner(
        docker_manager=docker_manager,
        plugins_dir=plugins_dir,
        verbose=args.verbose
    )

    # Execute test
    console.print(Panel.fit(
        f"[bold]Executing Test Run {args.run_number}[/bold]",
        border_style="blue"
    ))
    console.print()

    artifact = test_runner.execute_test_run(
        prompt_config=prompt_config,
        run_number=args.run_number,
        transcript_dir=transcript_dir,
        artifacts_dir=artifacts_dir
    )

    # Print results
    console.print()
    console.print(Panel.fit("[bold]Execution Results[/bold]", border_style="blue"))
    console.print()

    console.print(f"[bold]Status:[/bold] {artifact.status.value}")
    console.print(f"[bold]Exit Code:[/bold] {artifact.exit_code}")
    console.print(f"[bold]Execution Time:[/bold] {artifact.execution_time:.2f}s")
    console.print(f"[bold]Transcript:[/bold] {artifact.transcript_path or 'Not found'}")
    console.print(f"[bold]Transcript Size:[/bold] {artifact.transcript_size} bytes")
    console.print(f"[bold]Artifacts:[/bold] {len(artifact.artifact_files)} files")

    if artifact.execution_errors:
        console.print(f"\n[bold red]Execution Errors:[/bold red]")
        for error in artifact.execution_errors:
            console.print(f"  • {error}")

    # Save artifact if requested
    if args.save_artifact:
        artifact.save_to_file(args.save_artifact)
        console.print(f"\n[green]✓ Artifact saved to: {args.save_artifact}[/green]")

    # Exit code
    sys.exit(0 if artifact.status == ExecutionStatus.SUCCESS else 1)


if __name__ == "__main__":
    main()
