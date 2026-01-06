# Template: terraform-on-changed-dirs

## Metadata

- **Version**: `2.5.0`
- **Type**: `github-actions`
- **Template Path**: `boilerplate/github-actions/terraform-on-changed-dirs`
- **Last Commit**: `e650d0d1` - deps: update dependency actions/checkout to v5 (#1504) (2025-08-19)
- **Last Generated**: 2025-11-07

## Purpose

|      Name      |                                                 Description                                                 |  Type  |                Default                |Required|
|----------------|-------------------------------------------------------------------------------------------------------------|--------|---------------------------------------|--------|
|`FileTypes`     |File types to watch for changes                                                                              |`list`  |``["**.tf", "**.lock.hcl", "**.json"]``|no      |
|`StacksRootDir` |Root directory for the stacks                                                                                |`string`|``n/a``                                |yes     |
|`Stacks`        |List of stacks to run the action for                                                                         |`list`  |``n/a``                                |yes     |

## Variables

### Required Variables

| Name | Type | Description |
|------|------|-------------|
| `StacksRootDir` | `string` | Root directory for the stacks |
| `Stacks` | `list` | List of stacks to run the action for |

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `FileTypes` | `list` | `['**.tf', '**.lock.hcl', '**.json']` | File types to watch for changes |
| `OnPushBranches` | `list` | `[main]` | On push branches. |
| `ApplyBranch` | `string` | `main` | If changes are detected on this branch, the workflow runs "terraform apply". If not, "terraform plan" is run. |
| `PostWorkflows` | `map` | `{}` |  |

## Example Configuration

From `package-config-default.yml`:


```yaml

FileTypes:
- '**.tf'
- '**.json'
StacksRootDir: environments/dev
Stacks:
- name: app-too-tikki
  githubEnvironment: pirates-dev-app-too-tikki-cicd

```

## Generated Files

### Other Files

- `_gp_{{ .Environment }}_terraform_on_changed_dirs.yml`
- `boilerplate.yml`

## Conditional File Generation

- Always skip: `package-config*.yml`

## Recent Changes

## [2.5.0](https://github.com/oslokommune/golden-path-boilerplate/compare/terraform-on-changed-dirs-v2.4.5...terraform-on-changed-dirs-v2.5.0) (2025-08-19)


### Features

* Use YAML anchors for stack paths ([#1509](https://github.com/oslokommune/golden-path-boilerplate/issues/1509)) ([45d51d0](https://github.com/oslokommune/golden-path-boilerplate/commit/45d51d0068258c375281a429c77be90d274bce06))

## [2.4.5](https://github.com/oslokommune/golden-path-boilerplate/compare/terraform-on-changed-dirs-v2.4.4...terraform-on-changed-dirs-v2.4.5) (2025-08-13)


### Bug fixes

* Avoid including `package-config-default.yml` ([#1492](https://github.com/oslokommune/golden-path-boilerplate/issues/1492)) ([a3905c8](https://github.com/oslokommune/golden-path-boilerplate/commit/a3905c84c36695f7fdfa463bccf9022ae514dcb7))

## [2.4.4](https://github.com/oslokommune/golden-path-boilerplate/compare/terraform-on-changed-dirs-v2.4.3...terraform-on-changed-dirs-v2.4.4) (2025-08-08)


### Dependency updates

* update dependency oslokommune/reusable-terraform-plan-apply to v2.3.7 ([#1480](https://github.com/oslokommune/golden-path-boilerplate/issues/1480)) ([a3e15e0](https://github.com/oslokommune/golden-path-boilerplate/commit/a3e15e0a55b433c5553f7c30769f2d246ec6d8ce))

## [2.4.3](https://github.com/oslokommune/golden-path-boilerplate/compare/terraform-on-changed-dirs-v2.4.2...terraform-on-changed-dirs-v2.4.3) (2025-08-08)


### Bug fixes

* run all workflows to completion instead of failing fast ([e7ccc55](https://github.com/oslokommune/golden-path-boilerplate/commit/e7ccc55c95168998944c81905ff1e1b14397dfe0))

## [2.4.2](https://github.com/oslokommune/golden-path-boilerplate/compare/terraform-on-changed-dirs-v2.4.1...terraform-on-changed-dirs-v2.4.2) (2025-08-07)


### Dependency updates

* update dependency oslokommune/reusable-terraform-plan-apply to v2.3.5 ([#1470](https://github.com/oslokommune/golden-path-boilerplate/issues/1470)) ([8c83694](https://github.com/oslokommune/golden-path-boilerplate/commit/8c836943dfe4cacb62486bb3463163f0d7550f7a))
