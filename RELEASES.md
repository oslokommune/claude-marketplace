# Release Process

This repository uses [release-please](https://github.com/googleapis/release-please) to automate releases for the three Claude Code plugins:

- `origo-ai-platform`
- `origo-designsystem`
- `origo-iac-platform`

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

### 3. Creating a Release

To release a plugin:

1. **Review the Release PR** created by release-please
2. **Merge the Release PR** into `main`
3. release-please will automatically:
   - Create a GitHub release
   - Create a git tag (e.g., `origo-ai-platform-v1.1.0`)
   - Upload a tarball archive (e.g., `ai-platform-1.1.0.tar.gz`)

## Manual Release (if needed)

If you need to trigger a release manually or debug the workflow:

1. Go to **Actions** → **Release Please** in GitHub
2. Click **Run workflow**
3. Select the `main` branch
4. Click **Run workflow**

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

### Preview Changes

Release PRs show exactly what will be released. Review them carefully before merging!

## Troubleshooting

### Release PR not created?
- Check that your commits use conventional commit format
- Ensure commits are in the plugin's directory (`plugins/<name>/`)
- Check GitHub Actions logs for errors

### Wrong version number?
- Review your commit messages
- Use `!` for breaking changes: `feat!: breaking change`
- Edit the Release PR before merging to adjust version/changelog

### Need to release without commits?
You can manually create and merge a Release PR, or add an empty commit:
```bash
git commit --allow-empty -m "chore(ai-platform): trigger release"
```
