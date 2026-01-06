# GitHub CLI Command Reference

Complete reference for gh CLI commands used in the GitHub Projects workflow.

## Project Commands

### List Project Items

```bash
gh project item-list PROJECT_NUMBER --owner OWNER --format json --limit 500
```

**Output fields:**
- `items[].id` - Project item ID (needed for updates)
- `items[].content.number` - Issue/PR number
- `items[].content.repository` - Full repo path (e.g., "oslokommune/golden-path-iac")
- `items[].title` - Item title
- `items[].status` - Current status value
- `items[].assignees` - Array of assignee logins
- `items[].["linked pull requests"]` - Array of linked PRs

### View Project Metadata

```bash
gh project view PROJECT_NUMBER --owner OWNER --format json
```

**Output:** Project ID, title, description, URL.

### List Project Fields

```bash
gh project field-list PROJECT_NUMBER --owner OWNER --format json
```

**Output:** Field definitions including IDs and options for single-select fields.

### Update Project Item Status

```bash
gh project item-edit \
  --id "ITEM_ID" \
  --project-id "PROJECT_ID" \
  --field-id "FIELD_ID" \
  --single-select-option-id "OPTION_ID"
```

**Parameters:**
- `--id` - The project item ID (from `item-list`)
- `--project-id` - The project's global ID (from `project view`)
- `--field-id` - The status field ID (from `field-list`)
- `--single-select-option-id` - The target status option ID

---

## Issue Commands

### View Issue Details

```bash
gh issue view ISSUE_NUMBER --repo OWNER/REPO --json number,title,body,labels,assignees,url,state
```

**Common JSON fields:**
- `number`, `title`, `body`, `url`, `state`
- `labels[].name` - Label names
- `assignees[].login` - Assignee usernames

### Create Development Branch

```bash
gh issue develop ISSUE_NUMBER --checkout --repo OWNER/REPO
```

**Behavior:**
- Creates a branch named after the issue
- Checks out the branch
- Links the branch to the issue

**Fallback** (if `gh issue develop` unavailable):
```bash
git checkout -b "ISSUE_NUMBER-slug"
```

### List Issues

```bash
gh issue list --repo OWNER/REPO --state open --json number,title,labels
```

---

## Pull Request Commands

### Create Draft PR

```bash
gh pr create --draft \
  --title "PR Title" \
  --body "PR body with Closes #ISSUE_NUMBER" \
  --repo OWNER/REPO
```

**Using HEREDOC for body:**
```bash
gh pr create --draft --title "Title" --body "$(cat <<'EOF'
## Summary
Closes #123

## Changes
- Change 1
- Change 2
EOF
)"
```

### View PR Status

```bash
gh pr view --json number,state,isDraft,title,url,reviews,statusCheckRollup,mergeable
```

**Key fields:**
- `isDraft` - Boolean, true if still draft
- `state` - OPEN, CLOSED, MERGED
- `reviews` - Array of review objects
- `statusCheckRollup` - CI check results
- `mergeable` - MERGEABLE, CONFLICTING, UNKNOWN

### Mark PR Ready for Review

```bash
gh pr ready
```

### Add Reviewers

```bash
gh pr edit --add-reviewer USERNAME1,USERNAME2
```

### Merge PR

```bash
gh pr merge --squash --delete-branch
```

**Options:**
- `--squash` - Squash commits
- `--merge` - Create merge commit
- `--rebase` - Rebase and merge
- `--delete-branch` - Delete branch after merge

---

## Parsing Project Data with jq

### Get Item ID by Issue Number

```bash
cat .tmp/project.json | jq -r '.items[] | select(.content.number == 123) | .id'
```

### Get Item ID by Issue Number and Repo

```bash
cat .tmp/project.json | jq -r '.items[] | select(.content.number == 123 and (.content.repository // "" | contains("repo-name"))) | .id'
```

### Filter Items by Status

```bash
cat .tmp/project.json | jq -r '.items[] | select(.status == "Now 🏗") | .title'
```

### Count Items by Status

```bash
cat .tmp/project.json | jq '[.items[] | .status] | group_by(.) | map({status: .[0], count: length})'
```

### Format Item for Display

```bash
cat .tmp/project.json | jq -r '.items[] | select(.status == "Now 🏗") | "- #\(.content.number) **\(.title)** [\(.content.repository // "" | split("/") | .[-1])]"'
```

---

## Error Handling

### Check if Command Succeeded

```bash
if gh issue view 123 --repo owner/repo &>/dev/null; then
  echo "Issue exists"
else
  echo "Issue not found"
fi
```

### Handle Missing Project Data

```bash
if [ ! -f .tmp/project.json ]; then
  echo "Run Phase 1 (Review) first to fetch project data"
  exit 1
fi
```

### Validate Item ID Before Update

```bash
ITEM_ID=$(cat .tmp/project.json | jq -r '.items[] | select(.content.number == 123) | .id')
if [ -z "$ITEM_ID" ] || [ "$ITEM_ID" = "null" ]; then
  echo "Issue #123 not found in project"
  exit 1
fi
```

---

## Project Configuration

### oslokommune Project #27

| Setting | Value |
|---------|-------|
| Project ID | `PVT_kwDOARnAEM4AFVWG` |
| Status Field ID | `PVTSSF_lADOARnAEM4AFVWGzgDEtlA` |

### Status Options

| Status | ID | Use Case |
|--------|-----|----------|
| New Tasks 🫧 | `58ff5a13` | Newly created, needs triage |
| Next 🦦 | `47fc9ee4` | Ready to start |
| Now 🏗 | `72bc076b` | Currently in progress |
| Blocked ✋ | `3422c687` | Waiting on something |
| Completed 🎉 | `98236657` | Done |

### Backlog/Category Statuses (not workflow)

These are category labels, not workflow states:
- OK tool 🧰, Security 🔐, Tech/Improve 🕹️, Admin/Misc 💼
- Docs 🪜, AWS Org 🏢, GitHub 🐙, Tech/Misc 👾
- DB 📀, VPC ☁️, ECS/Containers/App 📦, Observability 🔭
- CICD for Golden Path ⚡️, CICD for App ⚡️, CICD for IaC ⚡️

---

## Getting IDs for Other Projects

### Get Project ID

```bash
gh project view PROJECT_NUMBER --owner OWNER --format json | jq '.id'
```

### Get Status Field ID and Options

```bash
gh project field-list PROJECT_NUMBER --owner OWNER --format json | jq '.fields[] | select(.name == "Status")'
```
