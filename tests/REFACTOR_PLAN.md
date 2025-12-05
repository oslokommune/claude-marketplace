# Orchestrator Refactoring Plan

## Objective
Split `orchestrator.py` into two components:
1. **`test_runner.py`** - Handles individual test execution in Docker containers
2. **`orchestrator.py`** - Coordinates multiple test runs, aggregation, and reporting

## Current Architecture Analysis

### Current orchestrator.py responsibilities:
- Load test prompt configurations from YAML files
- Build Docker image
- Execute individual test runs (create container, run claude -p, collect transcripts)
- Analyze transcripts using TranscriptAnalyzer
- Aggregate results across multiple runs
- Generate reports (console, JSON, markdown)
- Parallel execution coordination using ThreadPoolExecutor

### Key classes/functions:
- `TestRun` dataclass - represents a single test run configuration
- `SimplifiedOrchestrator` class:
  - `load_test_prompts()` - load YAML configs
  - `setup_docker()` - build Docker image
  - `execute_single_run()` - run ONE test in a container
  - `execute_prompt_tests()` - run ALL runs for ONE prompt
  - `run_tests()` - coordinate everything with parallel execution

## Proposed Split

### 1. test_runner.py (NEW FILE)
**Purpose:** Execute a single test run and return a structured result artifact

**Responsibilities:**
- Execute one test run in a Docker container
- Run `claude -p <prompt>` in non-interactive mode
- Collect transcript files
- Collect artifact files created during execution
- Return a structured TestExecutionArtifact
- Handle container lifecycle for single run
- Error handling for single run

**Public API:**
```python
@dataclass
class TestExecutionArtifact:
    """Complete artifact from a single test execution"""
    # Execution metadata
    run_number: int
    prompt_name: str
    container_name: str
    exit_code: int
    execution_time: float
    success: bool

    # Paths to collected files
    transcript_path: Optional[Path]
    transcript_size: int
    artifacts_dir: Path

    # Output from execution
    stdout: str
    stderr: str

    # Errors during execution (not test validation errors)
    execution_errors: List[str]

class TestRunner:
    """Execute individual test runs in Docker containers"""

    def __init__(
        self,
        docker_manager: DockerManager,
        plugins_dir: Path,
        verbose: bool = False
    ):
        pass

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
            prompt_config: Test configuration from YAML
            run_number: Which run number this is
            transcript_dir: Where to mount transcript directory
            artifacts_dir: Where to collect artifact files

        Returns:
            TestExecutionArtifact with all execution results
        """
        pass
```

**Key features:**
- Focused on EXECUTION only, not analysis
- Returns raw execution artifacts
- Container lifecycle management (create, start, execute, cleanup)
- Collects all output (stdout, stderr, transcript, artifacts)
- Handles timeouts from prompt config
- Proper error handling with detailed execution errors

**Dependencies:**
- docker_manager.py (ContainerConfig, DockerManager)
- Rich Console (for optional verbose output)
- Standard library (Path, dataclasses, time, typing)

---

### 2. orchestrator.py (REFACTORED)
**Purpose:** Coordinate multiple test runs, aggregate results, and generate reports

**Responsibilities:**
- Load test prompt configurations
- Setup Docker (build image)
- Coordinate parallel test execution using TestRunner
- Analyze execution artifacts using TranscriptAnalyzer
- Aggregate results across multiple runs
- Generate reports
- Handle CLI arguments and main entry point

**Refactored API:**
```python
class Orchestrator:
    """Coordinate test execution, analysis, and reporting"""

    def __init__(
        self,
        project_root: Path,
        verbose: bool = False,
        override_runs: Optional[int] = None
    ):
        self.test_runner: Optional[TestRunner] = None
        # ... other fields

    def load_test_prompts(self) -> List[Dict[str, Any]]:
        """Load all test prompt YAML files (unchanged)"""
        pass

    def setup_docker(self) -> bool:
        """Build Docker image and initialize TestRunner"""
        # Build image (same as before)
        # Create TestRunner instance
        self.test_runner = TestRunner(
            docker_manager=self.docker_manager,
            plugins_dir=self.plugins_dir,
            verbose=self.verbose
        )
        pass

    def execute_single_run(
        self,
        prompt_config: Dict[str, Any],
        run_number: int,
        transcript_dir: Path,
        artifacts_dir: Path
    ) -> TestResult:
        """
        Execute and analyze a single test run

        This now delegates execution to TestRunner,
        then analyzes the artifact
        """
        # 1. Execute using TestRunner
        artifact = self.test_runner.execute_test_run(
            prompt_config=prompt_config,
            run_number=run_number,
            transcript_dir=transcript_dir,
            artifacts_dir=artifacts_dir
        )

        # 2. Analyze transcript if available
        if artifact.transcript_path and artifact.transcript_path.exists():
            result = self.analyzer.analyze_transcript(
                artifact.transcript_path,
                prompt_config,
                run_number
            )
        else:
            # Create failed result
            result = TestResult(...)

        return result

    def execute_prompt_tests(...) -> List[TestResult]:
        """Execute all runs for a single prompt (mostly unchanged)"""
        pass

    def run_tests(self, max_workers: int = 6) -> Dict[str, Any]:
        """Run all tests with parallel execution (mostly unchanged)"""
        pass
```

**Key changes:**
- Delegates execution to TestRunner
- Focuses on coordination, not execution details
- Still handles analysis, aggregation, reporting
- Still manages parallel execution with ThreadPoolExecutor
- CLI entry point remains here

---

## Data Flow

### Before (Current):
```
Orchestrator
  ├─ Load YAML configs
  ├─ Build Docker
  ├─ For each prompt (parallel):
  │   └─ For each run (sequential):
  │       ├─ Create container
  │       ├─ Execute claude -p
  │       ├─ Collect transcript
  │       ├─ Analyze transcript
  │       ├─ Cleanup container
  │       └─ Return TestResult
  ├─ Aggregate results
  └─ Generate reports
```

### After (Proposed):
```
Orchestrator
  ├─ Load YAML configs
  ├─ Build Docker
  ├─ Create TestRunner
  ├─ For each prompt (parallel):
  │   └─ For each run (sequential):
  │       ├─ TestRunner.execute_test_run()
  │       │   ├─ Create container
  │       │   ├─ Execute claude -p
  │       │   ├─ Collect transcript & artifacts
  │       │   ├─ Cleanup container
  │       │   └─ Return TestExecutionArtifact
  │       ├─ Analyze artifact -> TestResult
  │       └─ Return TestResult
  ├─ Aggregate results
  └─ Generate reports
```

---

## Implementation Steps

### Step 1: Create test_runner.py
- Define `TestExecutionArtifact` dataclass
- Define `TestRunner` class with `execute_test_run()` method
- Move container execution logic from orchestrator
- Add proper error handling and timeout support
- Add artifact collection logic
- Write docstrings

### Step 2: Refactor orchestrator.py
- Add import for test_runner
- Remove container execution logic (move to TestRunner)
- Update `setup_docker()` to create TestRunner instance
- Update `execute_single_run()` to:
  1. Call TestRunner.execute_test_run()
  2. Analyze the returned artifact
  3. Return TestResult
- Keep all other functionality unchanged

### Step 3: Testing
- Verify single test run works
- Verify parallel execution works
- Verify error handling works
- Verify reports are generated correctly

### Step 4: Documentation
- Update USAGE.md with architecture diagram
- Document TestRunner API
- Document TestExecutionArtifact structure

---

## Benefits of This Split

1. **Separation of Concerns**
   - TestRunner: Execution only
   - Orchestrator: Coordination, analysis, reporting

2. **Reusability**
   - TestRunner can be used standalone for single test execution
   - Can create alternative orchestrators (e.g., sequential, different reporting)

3. **Testability**
   - TestRunner can be unit tested independently
   - Mock TestRunner for orchestrator tests

4. **Maintainability**
   - Smaller, focused files
   - Clear boundaries between components
   - Easier to modify execution logic without affecting coordination

5. **Extensibility**
   - Easy to add new artifact collection (logs, screenshots, etc.)
   - Easy to add different execution strategies
   - Can add pre/post execution hooks

---

## Files Modified

- **NEW:** `tests/scripts/test_runner.py`
- **MODIFIED:** `tests/scripts/orchestrator.py`
- **MODIFIED:** `tests/USAGE.md` (documentation)

---

## Backward Compatibility

- CLI interface remains unchanged (orchestrator.py main())
- YAML configuration format unchanged
- Report formats unchanged
- TestResult and AggregatedResult dataclasses unchanged
- Only internal implementation changes

---

## Migration Path

1. Create test_runner.py with new functionality
2. Refactor orchestrator.py to use test_runner
3. Run existing tests to verify behavior unchanged
4. Update documentation
5. (Optional) Add new features leveraging the split architecture
