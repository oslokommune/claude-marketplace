---
name: github-projects
description: Manage GitHub Projects workflow with three phases - review project board to pick tasks, setup work on an issue (create branch, draft PR, update status), and complete work (finalize PR, update status). Use when working with GitHub Projects, starting work, or phrases like "show project", "what should I work on", "start issue", "pick a task", "I'm done", or "finish work".
---

# GitHub Projects Workflow

Three-phase workflow for GitHub Projects. Default: **oslokommune project #27** (Team kjøremiljø).

## Quick Reference

| Phase | Trigger Phrases | Actions |
|-------|-----------------|---------|
| **Review** | "show project", "what should I work on" | Display board, help pick task |
| **Setup** | "start issue #X", "work on #X" | Create branch, draft PR, move to Now |
| **Complete** | "I'm done", "finish work" | Update status, mark PR ready |

---

## Phase 1: Review

Display the current project state to help identify work items.

### Instructions

1. **Fetch project data**:
   ```bash
   mkdir -p .tmp
   gh project item-list 27 --owner oslokommune --format json --limit 500 > .tmp/project.json
   ```

2. **Get status counts**:
   ```bash
   cat .tmp/project.json | jq '[.items[] | .status] | group_by(.) | map({status: .[0], count: length})'
   ```

3. **Display items by workflow status**:
   ```bash
   # Now 🏗 items
   cat .tmp/project.json | jq -r '.items[] | select(.status == "Now 🏗") | "- #\(.content.number) **\(.title)** [\(.content.repository // "" | split("/") | .[-1])] \(if (.assignees // []) | length > 0 then "@" + ((.assignees // []) | join(", @")) else "" end)\(if ((.["linked pull requests"] // []) | length > 0) then " 🔗" else "" end)"' | sort -t'[' -k2

   # Blocked ✋ items
   cat .tmp/project.json | jq -r '.items[] | select(.status == "Blocked ✋") | "- #\(.content.number) **\(.title)** [\(.content.repository // "" | split("/") | .[-1])] \(if (.assignees // []) | length > 0 then "@" + ((.assignees // []) | join(", @")) else "" end)"' | sort -t'[' -k2

   # Next 🦦 items
   cat .tmp/project.json | jq -r '.items[] | select(.status == "Next 🦦") | "- #\(.content.number) **\(.title)** [\(.content.repository // "" | split("/") | .[-1])]"' | sort -t'[' -k2

   # New Tasks 🫧 items
   cat .tmp/project.json | jq -r '.items[] | select(.status == "New Tasks 🫧") | "- #\(.content.number) **\(.title)** [\(.content.repository // "" | split("/") | .[-1])]"' | sort -t'[' -k2
   ```

4. **Present overview** in this format:
   ```
   ## Project: Team kjøremiljø

   ### Summary
   | Status | Count |
   |--------|-------|
   | Now 🏗 | X |
   | Blocked ✋ | X |
   | Next 🦦 | X |
   | New Tasks 🫧 | X |

   ### Now 🏗 (In Progress)
   - #123 **Issue title** [repo-name] @assignee 🔗

   ### Blocked ✋ (Needs Attention)
   ...

   ### Next 🦦 (Up Next)
   ...

   ### New Tasks 🫧 (Triage Needed)
   ...
   ```

5. **Ask user** which issue they want to work on.

---

## Phase 2: Setup

After user selects an issue, prepare the workspace for development.

### Prerequisites
- Issue number (required)
- Repository name (from project data or current directory)

### Instructions

1. **Get issue details**:
   ```bash
   gh issue view ISSUE_NUMBER --repo OWNER/REPO --json number,title,body,labels,assignees,url
   ```

2. **Create branch from issue** (automatically names and links branch):
   ```bash
   gh issue develop ISSUE_NUMBER --checkout --repo OWNER/REPO
   ```

   If `gh issue develop` is unavailable, create manually:
   ```bash
   BRANCH_NAME="ISSUE_NUMBER-$(echo 'issue-title' | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd '[:alnum:]-')"
   git checkout -b "$BRANCH_NAME"
   ```

3. **Create draft PR**:
   ```bash
   gh pr create --draft \
     --title "ISSUE_TITLE" \
     --body "$(cat <<'EOF'
   ## Summary
   Closes #ISSUE_NUMBER

   ## Changes
   -

   ## Test Plan
   -
   EOF
   )" \
     --repo OWNER/REPO
   ```

4. **Move issue to "Now 🏗" status**:
   ```bash
   # Get item ID from project data
   ITEM_ID=$(cat .tmp/project.json | jq -r '.items[] | select(.content.number == ISSUE_NUMBER and (.content.repository // "" | contains("REPO"))) | .id')

   # Update status
   gh project item-edit \
     --id "$ITEM_ID" \
     --project-id "PVT_kwDOARnAEM4AFVWG" \
     --field-id "PVTSSF_lADOARnAEM4AFVWGzgDEtlA" \
     --single-select-option-id "72bc076b"
   ```

5. **Save work context** for later:
   ```bash
   cat > .tmp/current-work.json << EOF
   {
     "issue_number": ISSUE_NUMBER,
     "repository": "OWNER/REPO",
     "branch": "BRANCH_NAME",
     "pr_number": PR_NUMBER,
     "item_id": "ITEM_ID",
     "started_at": "$(date -Iseconds)"
   }
   EOF
   ```

6. **Display issue context**:
   - Show issue body/description
   - List labels and assignees
   - Provide links to issue and draft PR
   - Summarize what needs to be done

---

## Phase 3: Completion

When work is done on the issue.

### Instructions

1. **Read work context** (if available):
   ```bash
   cat .tmp/current-work.json
   ```

   If no context file, infer from current branch:
   ```bash
   BRANCH=$(git branch --show-current)
   ISSUE_NUMBER=$(echo "$BRANCH" | grep -oE '^[0-9]+')
   ```

2. **Verify PR status**:
   ```bash
   gh pr view --json number,state,isDraft,title,url,reviews,statusCheckRollup
   ```

3. **Mark PR ready for review** (if still draft):
   ```bash
   gh pr ready
   ```

4. **Update project status to "Completed 🎉"**:
   ```bash
   gh project item-edit \
     --id "$ITEM_ID" \
     --project-id "PVT_kwDOARnAEM4AFVWG" \
     --field-id "PVTSSF_lADOARnAEM4AFVWGzgDEtlA" \
     --single-select-option-id "98236657"
   ```

5. **Optional - Request reviewer**:
   ```bash
   gh pr edit --add-reviewer USERNAME
   ```

6. **Clean up** work context:
   ```bash
   rm -f .tmp/current-work.json
   ```

7. **Show summary**:
   - PR URL and status
   - Issue status change confirmation
   - Suggest next steps (e.g., "Run Phase 1 to pick another task")

---

## Configuration

### Project Details
| Setting | Value |
|---------|-------|
| Owner | oslokommune |
| Project Number | 27 |
| Project ID | `PVT_kwDOARnAEM4AFVWG` |
| Status Field ID | `PVTSSF_lADOARnAEM4AFVWGzgDEtlA` |

### Status Option IDs

| Status | Option ID |
|--------|-----------|
| New Tasks 🫧 | `58ff5a13` |
| Next 🦦 | `47fc9ee4` |
| Now 🏗 | `72bc076b` |
| Blocked ✋ | `3422c687` |
| Completed 🎉 | `98236657` |

---

## State Management

Work context is stored in `.tmp/current-work.json`:
- **Created** during Phase 2 (Setup)
- **Read** during Phase 3 (Completion)
- **Deleted** after Phase 3 completes

This allows resuming work across sessions. If the context file is missing, fall back to inferring issue number from the current git branch name.

---

## Detailed Reference

For complete gh CLI command documentation and examples, see [reference/gh-commands.md](reference/gh-commands.md).
