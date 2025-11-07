# Template: renovate

## Metadata

- **Version**: `unknown`
- **Type**: `github-actions`
- **Template Path**: `boilerplate/github-actions/renovate`
- **Last Commit**: `a3905c84` - fix: Avoid including `package-config-default.yml` (#1492) (2025-08-13)
- **Last Generated**: 2025-11-07

## Purpose

This template contains a Renovate configuration file and GitHub Actions workflow to run Renovate.
Running Renovate in GitHub Actions provides self-hosted control, eliminating reliance on the Mend-hosted app and giving full ownership of the pipeline.

## Variables

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IgnorePaths` | `list` | `[stacks/dev/packages.yml, stacks/prod/packages.yml, stacks/autodeploy/**]` |  |
| `DependencyDashboard` | `bool` | true | Enable Renovate's dependency dashboard |
| `Repository` | `string` | `pirates-iac` |  |

## Generated Files

### Other Files

- `boilerplate.yml`
- `workflows/renovate.yml`

## Conditional File Generation

- Always skip: `package-config*.yml`
