# Release Process

This repository uses [release-please](https://github.com/googleapis/release-please) to automate releases for the three Claude Code plugins:

- `dig-ai-platform`
- `dig-designsystem`
- `dig-iac-platform`

## How It Works

### 1. Conventional Commits

Release Please tracks releases based on [Conventional Commits](https://www.conventionalcommits.org/). When you commit changes, use these prefixes:

- `feat:` - New feature (triggers minor version bump)
- `fix:` - Bug fix (triggers patch version bump)
- `feat!:` or `fix!:` - Breaking change (triggers major version bump)
- `chore:`, `docs:`, `style:`, etc. - No version bump

**Examples:**
```bash
git commit -m "feat(ai-platform): add new bedrock skill"
git commit -m "fix(designsystem): correct punkt docs navigation"
git commit -m "feat(iac-platform)!: breaking change to boilerplate templates"
```

### 2. Automatic Release PRs

When you push commits to `main`, release-please will:

1. Analyze commits since the last release for each plugin
2. Calculate the next version number based on conventional commits
3. Create or update a Release PR for each plugin that has changes
4. The Release PR includes:
   - Updated version in `.claude-plugin/plugin.json`
   - Generated `CHANGELOG.md`
   - Release notes
5. **Automatically merge the Release PR** (no manual approval needed)

### 3. Creating a Release

Releases happen automatically:

1. **Push conventional commits** to `main`
2. **release-please creates Release PR** with version bumps and changelog
3. **PR is automatically merged** via GitHub Actions
4. release-please then automatically:
   - Creates a GitHub release
   - Creates a git tag (e.g., `dig-ai-platform-v1.1.0`)
   - Uploads a tarball archive (e.g., `ai-platform-1.1.0.tar.gz`)

No manual intervention needed!

## Manual Release (if needed)

If you need to trigger a release manually or debug the workflow:

1. Go to **Actions** → **Release Please** in GitHub
2. Click **Run workflow**
3. Select the `main` branch
4. Click **Run workflow**

## Prerequisites

### Required GitHub Settings

**1. Create a Personal Access Token (Required for Organization Repos)**

For organization repositories (like `oslokommune/claude-marketplace`), you need a Personal Access Token (PAT) with `repo` scope:

1. Go to **GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)**
2. Click **Generate new token (classic)**
3. Give it a descriptive name: `release-please-claude-marketplace`
4. Set expiration (recommend: 90 days or 1 year)
5. Check **repo** scope (full control of private repositories)
6. Click **Generate token** and copy the token

Then add it to your repository:

1. Go to **Repository Settings → Secrets and variables → Actions**
2. Click **New repository secret**
3. Name: `RELEASE_PLEASE_TOKEN`
4. Value: Paste your PAT
5. Click **Add secret**

**2. Enable Workflow Permissions (If not using PAT)**

If using a personal repository (not organization), go to **Settings → Actions → General → Workflow permissions**:

- Select "Read and write permissions"
- Check "Allow GitHub Actions to create and approve pull requests"

**3. Enable Auto-Merge (Optional)**

For fully automated releases:

- **Settings → General → Pull Requests** → Enable "Allow auto-merge"

**3. Branch Protection Rules (If Configured)**

If you have branch protection on `main`:
- Either disable required reviews for release PRs
- Or configure GitHub Actions bot to bypass protection rules

## Configuration Files

### `release-please-config.json`
Defines the release configuration for each plugin:
- Release type: `simple` (no package.json)
- Package names
- Version update strategy for `plugin.json`

### `.release-please-manifest.json`
Tracks current versions of each plugin. This file is automatically updated by release-please.

## Version Numbering

This project follows [Semantic Versioning](https://semver.org/):

- **Major** (1.0.0): Breaking changes
- **Minor** (0.1.0): New features (backwards compatible)
- **Patch** (0.0.1): Bug fixes

## Tips

### Releasing Multiple Plugins

Each plugin is released independently. If you make changes to multiple plugins in a single commit, release-please will create separate Release PRs for each.

### Skipping Releases

Commits without conventional prefixes (e.g., regular commit messages) won't trigger releases.

### Force a Specific Version

Add this to your commit message:
```
Release-As: 2.0.0
```

### Reviewing Releases

Release PRs are automatically merged, but you can review them before they merge by checking the GitHub Actions tab. If you need to prevent auto-merge, disable the workflow or close the PR before it merges.

## Troubleshooting

### "author_id does not have push access" error

**For Organization Repos:** This means you need to create and add a Personal Access Token (PAT). The default `GITHUB_TOKEN` doesn't have permission to create releases in organization repositories.

**Solution:**
1. Create a PAT with `repo` scope (see Prerequisites section above)
2. Add it as a repository secret named `RELEASE_PLEASE_TOKEN`
3. Push an empty commit to trigger the workflow:
   ```bash
   git commit --allow-empty -m "chore: trigger release" && git push
   ```

**For Personal Repos:** This means GitHub Actions doesn't have write permissions.
1. Go to **Settings → Actions → General → Workflow permissions**
2. Select "Read and write permissions"
3. Check "Allow GitHub Actions to create and approve pull requests"
4. Retry the workflow

### Release PR not created?
- Check that your commits use conventional commit format
- Ensure commits are in the plugin's directory (`plugins/<name>/`)
- Check GitHub Actions logs for errors

### Wrong version number?
- Review your commit messages
- Use `!` for breaking changes: `feat!: breaking change`
- Close the auto-generated PR and push a corrected commit with the right conventional commit prefix

### Need to release without commits?
You can manually create and merge a Release PR, or add an empty commit:
```bash
git commit --allow-empty -m "chore(ai-platform): trigger release"
```
