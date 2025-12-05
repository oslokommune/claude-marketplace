# Instructions for Claude Code

## Default Behavior

**ALWAYS enter plan mode before implementing any non-trivial changes.** For any task that involves:
- Code modifications spanning multiple files
- Architectural decisions or design choices
- Refactoring or restructuring code
- Adding new features or functionality
- Making changes that could have multiple implementation approaches

You MUST:
1. Use `EnterPlanMode` tool first
2. Explore the codebase thoroughly
3. Design an implementation approach
4. Present the plan for approval before executing

**Exceptions** (when you can skip plan mode):
- Trivial changes (typo fixes, single-line edits)
- User explicitly says "no need to plan" or "just do it"
- Simple, obvious fixes with no design decisions needed

## Skills

Always review the available skills to see if any of them are relevant for the task at hand.