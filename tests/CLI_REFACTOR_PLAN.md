# CLI GUI Refactoring Plan

## Overview
Refactor the test orchestrator CLI to provide a clean, live-updating interface focused on key metrics: **success rate**, **skill activation**, and **test progression**. The new design must scale for high parallelization (20+ concurrent tests).

## Current State Analysis

### Current Problems
1. **Output Pollution**: Test runners, docker managers, and analyzers all write directly to console via `self.console.print()`
2. **Progress Tracking**: Uses simple Rich Progress bars that don't show enough detail
3. **No Central State**: Each component manages its own output independently
4. **Poor Scalability**: Current UI doesn't handle many parallel tests well
5. **Limited Metrics**: Doesn't show real-time skill activation or success rates during execution

### Current Components
- **orchestrator.py**: Main coordinator, uses ThreadPoolExecutor and Rich Progress
- **test_runner.py**: Executes tests in Docker, prints verbose output
- **analyzer.py**: Analyzes transcripts, generates markdown reports
- **reporter.py**: Generates final reports (console, JSON, markdown)

## Proposed Architecture

### 1. Central State Management
Create a `TestState` class that maintains all test execution state:
- Test queue and status (pending/running/completed)
- Real-time metrics per test (execution time, success, skills activated)
- Aggregate statistics (overall success rate, skill activation rate)
- Error tracking
- Thread-safe updates from parallel workers

### 2. UI Components (Rich Layout)

#### Main Layout Structure
```
┌─────────────────────────────────────────────────────────┐
│  Plugin Testing Framework - Live Dashboard              │
│  Progress: 15/30 tests (50%) | Time: 2m 34s             │
└─────────────────────────────────────────────────────────┘

┌─────────────────────── Metrics ─────────────────────────┐
│  Success Rate:    87% (13/15)    Target: ≥95%           │
│  Skill Activation: 93% (14/15)   Target: ≥95%           │
│  Avg Time/Test:   8.2s                                   │
└─────────────────────────────────────────────────────────┘

┌───────────────────── Test Status ───────────────────────┐
│ ✓ python-uv-script           3/3  100%  [python]   8.1s │
│ ✓ bedrock-api-call          3/3  100%  [bedrock]  12.3s │
│ ↻ punkt-button-usage         2/3   67%  [punkt]    9.8s │
│ ⏳ terraform-module-lookup    1/3   --   [--]      4.2s │
│ ⋯ aws-cloudfront-deploy      0/3   --   [--]       --   │
│ ⋯ pytest-runner              0/3   --   [--]       --   │
└─────────────────────────────────────────────────────────┘

┌─────────────────────── Workers ─────────────────────────┐
│ Worker 1: ✓ python-uv-script-3                          │
│ Worker 2: ↻ terraform-module-lookup-1                    │
│ Worker 3: ⏳ bedrock-api-call-3                          │
│ Worker 4: [idle]                                         │
│ Worker 5: [idle]                                         │
│ Worker 6: [idle]                                         │
└─────────────────────────────────────────────────────────┘

[ERROR] punkt-button-usage-2: Skill 'punkt-docs' not activated
```

#### Status Icons
- `⋯` - Pending (not started)
- `⏳` - Running (actively executing)
- `↻` - Running with some failures (mixed results)
- `✓` - Completed successfully
- `✗` - Completed with failures

### 3. Silent Worker Mode
Modify worker components to emit structured events instead of printing:
- **test_runner.py**: Return events via callback instead of `self.console.print()`
- **docker_manager.py**: Silent mode flag to suppress output
- **analyzer.py**: Silent analysis, no console output

### 4. Event System
Create an event-based architecture:

```python
class TestEvent:
    """Base class for test events"""
    timestamp: float
    test_name: str
    run_number: int

class TestStartedEvent(TestEvent):
    worker_id: int
    container_name: str

class TestCompletedEvent(TestEvent):
    success: bool
    execution_time: float
    skills_activated: List[str]
    exit_code: int

class TestFailedEvent(TestEvent):
    error: str

class SkillActivatedEvent(TestEvent):
    skill_name: str
```

### 5. Live Dashboard
Use Rich's `Live` context manager for real-time updates:
- Single render loop that updates entire UI
- No spurious print statements
- Thread-safe state updates
- Smooth refresh rate (2-5 Hz)

## Implementation Plan

### Phase 1: State Management
**Files to Create:**
- `tests/scripts/ui/test_state.py` - Central state manager
- `tests/scripts/ui/events.py` - Event definitions

**Key Classes:**
- `TestState`: Thread-safe state container
- `TestStatus`: Enum for test states
- `TestMetrics`: Data class for test metrics
- Event hierarchy for different test lifecycle events

### Phase 2: Event System
**Files to Modify:**
- `test_runner.py` - Add event callbacks, remove console output
- `docker_manager.py` - Add silent mode flag
- `analyzer.py` - Add event emission for skill activation

**Changes:**
- Add `event_callback` parameter to TestRunner
- Emit events at key lifecycle points
- Remove all `self.console.print()` calls from workers

### Phase 3: UI Components
**Files to Create:**
- `tests/scripts/ui/dashboard.py` - Main dashboard using Rich Live
- `tests/scripts/ui/components.py` - Reusable UI components (metrics panel, test table, workers panel)

**Key Components:**
- `Dashboard`: Main UI coordinator
- `MetricsPanel`: Real-time metrics display
- `TestTable`: Scrollable test status table
- `WorkersPanel`: Worker status display
- `ErrorLog`: Recent errors display

### Phase 4: Integration
**Files to Modify:**
- `orchestrator.py` - Replace Progress UI with new Dashboard

**Changes:**
- Initialize `TestState` and `Dashboard`
- Pass event callback to workers
- Use `Live` context instead of `Progress`
- Handle keyboard interrupts gracefully

### Phase 5: Scalability Features
**Enhancements for High Parallelization:**
- Collapsible test groups (group by category)
- Auto-scroll to active tests
- Worker utilization metrics
- Queue depth indicator
- Estimated time remaining

## Technical Details

### Thread Safety
- Use `threading.Lock` for state updates
- Immutable data structures where possible
- Event queue for UI updates

### Performance
- Limit UI refresh rate (2-5 Hz max)
- Batch state updates
- Lazy rendering for large test lists
- Terminal size detection for responsive layout

### Error Handling
- Graceful degradation if terminal doesn't support features
- Fallback to simple progress bar for non-interactive terminals
- Proper cleanup on Ctrl+C

## Migration Strategy

### Backwards Compatibility
- Keep old reporter for final summary
- Support `--verbose` flag for debug mode
- Maintain JSON/Markdown report generation
- Keep existing CLI arguments

### Verbose Mode
In verbose mode, print detailed logs to file:
- `tests/results/debug/execution-{timestamp}.log`
- Worker output
- Docker logs
- Event stream

## Testing Strategy
1. Test with single worker (sequential execution)
2. Test with 6 workers (current default)
3. Test with 20+ workers (future scaling)
4. Test error scenarios (failures, timeouts)
5. Test terminal resize handling
6. Test Ctrl+C interruption

## Success Criteria
✓ No spurious output during test execution
✓ Real-time success rate visible
✓ Real-time skill activation visible
✓ Per-test progress clearly shown
✓ Worker utilization visible
✓ Scales to 20+ parallel tests
✓ Clean, professional appearance
✓ Handles errors gracefully
✓ Responsive to terminal size changes

## Implementation Order
1. Create state management (`TestState`, events)
2. Create UI components (panels, tables, dashboard)
3. Make workers silent (event-based)
4. Integrate dashboard into orchestrator
5. Add scalability features
6. Testing and refinement

## Estimated Effort
- Phase 1: 1-2 hours (state + events)
- Phase 2: 2-3 hours (worker modifications)
- Phase 3: 3-4 hours (UI components)
- Phase 4: 1-2 hours (integration)
- Phase 5: 2-3 hours (scalability)
- Testing: 1-2 hours

**Total: 10-16 hours of development**

## Files to Create
```
tests/scripts/ui/
├── __init__.py
├── test_state.py      # Central state management
├── events.py          # Event definitions
├── dashboard.py       # Main dashboard with Rich Live
└── components.py      # Reusable UI components
```

## Files to Modify
```
tests/scripts/
├── orchestrator.py    # Replace Progress with Dashboard
├── test_runner.py     # Add event callbacks, silent mode
├── analyzer.py        # Silent analysis
└── utils/
    └── docker_manager.py  # Add silent mode flag
```

## Future Enhancements (Post-MVP)
- Real-time transcript streaming
- Test filtering/search
- Interactive mode (pause/resume)
- Historical comparison
- Performance graphs
- Export live state to JSON
- Web dashboard (optional)
