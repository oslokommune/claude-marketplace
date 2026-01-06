# Template: app-common

## Metadata

- **Version**: `4.0.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/app-common`
- **Last Commit**: `371eb5a4` - feat: add terragrunt setup for all stacks needed. add bin scripts to delete necessary resources (#1622) (2025-11-04)
- **Last Generated**: 2025-11-07

## Purpose

|        Name         |                                                       Description                                                       | Type |          Default          |Required|
|---------------------|-------------------------------------------------------------------------------------------------------------------------|------|---------------------------|--------|
|`IncludeLockFile`    |Include a Terraform lock file.                                                                                           |`bool`|``false``                  |no      |
|`EcrPullThroughCache`|Enable ECR pull through cache                                                                                            |`map` |``{"Enable": true}``       |no      |
|`Logs`               |Whether to enable various logs (e.g., store events emitted from the ECS cluster in CloudWatch for easier troubleshooting)|`map` |``{"ClusterEvents": true}``|no      |

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)

## Variables

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `EcrPullThroughCache` | `map` | `{Enable: true}` | Enable ECR pull through cache |
| `Logs` | `map` | `{ClusterEvents: true}` | Whether to enable various logs (e.g., store events emitted from the ECS cluster in CloudWatch for easier troubleshooting) |

## Feature Flags

These map-type variables control optional features:

### EcrPullThroughCache

Enable ECR pull through cache


**Default configuration:**
```yaml

EcrPullThroughCache:
  Enable: true

```


## Example Configuration

From `package-config-default.yml`:


```yaml

StackName: app-common

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_common.tf`
- `__gp_config.tf`
- `__gp_ecr_pull_through_cache.tf`
- `__gp_ecs_cluster.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Helper Scripts

- `bin/_gp_ecr_pull_through_cache_init.sh`

### Other Files

- `.terraform.lock.hcl`
- `_gp_rm_gp_file.sh`
- `boilerplate.yml`
- `terragrunt.hcl`
- `terragrunt_custom.hcl`

## Conditional File Generation

- Always skip: `package-config*.yml`
- Skip `.terraform.lock.hcl*` if: `{{ not .IncludeLockFile }}`
- Skip `config_override.tf` if: `{{ list outputFolder "config_override.tf" | join "/" | pathExists }}`
- Skip `terragrunt_custom.hcl` if: `{{ list outputFolder "terragrunt_custom.hcl" | join "/" | pathExists }}`

## Recent Changes

## [4.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/app-common-v3.9.0...app-common-v4.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))


### Dependency updates

* update dependency versions to v5 ([#1454](https://github.com/oslokommune/golden-path-boilerplate/issues/1454)) ([01fb21e](https://github.com/oslokommune/golden-path-boilerplate/commit/01fb21e7c1891dbf57451fbdd248bb59a79304e9))

## [3.9.0](https://github.com/oslokommune/golden-path-boilerplate/compare/app-common-v3.8.2...app-common-v3.9.0) (2025-07-25)


### Features

* Move var files for lock file generation to template dir ([#1346](https://github.com/oslokommune/golden-path-boilerplate/issues/1346)) ([d0a4b02](https://github.com/oslokommune/golden-path-boilerplate/commit/d0a4b02653613a92e8fcd582d14a2f3c911c17b0))


### Bug fixes

* Add IncludeLockFile to all Terraform boilerplate templates ([#1347](https://github.com/oslokommune/golden-path-boilerplate/issues/1347)) ([1a77fab](https://github.com/oslokommune/golden-path-boilerplate/commit/1a77fab696c5ad2523abbdc22a85b57f46399d3e))
* Remove error in case template lockfile is missing ([#1358](https://github.com/oslokommune/golden-path-boilerplate/issues/1358)) ([22debb6](https://github.com/oslokommune/golden-path-boilerplate/commit/22debb6595935feccca61e7afb1f72c51d102514))


### Dependency updates

* update dependency versions to v3.4.0 ([#1367](https://github.com/oslokommune/golden-path-boilerplate/issues/1367)) ([16f6283](https://github.com/oslokommune/golden-path-boilerplate/commit/16f628302d18f079b62f3c66d8adb6ae30b569c2))
* Update Terraform dependency lock files ([#1308](https://github.com/oslokommune/golden-path-boilerplate/issues/1308)) ([1f49902](https://github.com/oslokommune/golden-path-boilerplate/commit/1f49902150a5431d0d9815aaafad8b8858940e9c))

## [3.8.2](https://github.com/oslokommune/golden-path-boilerplate/compare/app-common-v3.8.1...app-common-v3.8.2) (2025-06-25)


### Dependency updates

* update dependency versions to v3.3.0 ([#1224](https://github.com/oslokommune/golden-path-boilerplate/issues/1224)) ([d2581ac](https://github.com/oslokommune/golden-path-boilerplate/commit/d2581ace71ccaf2ff7f677e22d0cac4cec3c2b34))
* Update Terraform dependency lock files ([#1206](https://github.com/oslokommune/golden-path-boilerplate/issues/1206)) ([b94e3c6](https://github.com/oslokommune/golden-path-boilerplate/commit/b94e3c601c31dcb7d37f2948631acbbb387ff32d))

## [3.8.1](https://github.com/oslokommune/golden-path-boilerplate/compare/app-common-v3.8.0...app-common-v3.8.1) (2025-06-19)


### Bug fixes

* Delete files from Golden path only ([#1162](https://github.com/oslokommune/golden-path-boilerplate/issues/1162)) ([bd43212](https://github.com/oslokommune/golden-path-boilerplate/commit/bd43212378defcb9437e54e2ccfb52b0502e1ff0))
* remove redundant tags ([#1140](https://github.com/oslokommune/golden-path-boilerplate/issues/1140)) ([11096c1](https://github.com/oslokommune/golden-path-boilerplate/commit/11096c1019530de6df3f47ecb4110881f638afaa))
* Remove sh files with delete-marker ([#1171](https://github.com/oslokommune/golden-path-boilerplate/issues/1171)) ([2ac3158](https://github.com/oslokommune/golden-path-boilerplate/commit/2ac31581acda734fec295a462d05e8b6f48f332b))

## [3.8.0](https://github.com/oslokommune/golden-path-boilerplate/compare/app-common-v3.7.0...app-common-v3.8.0) (2025-04-03)


### Features

* log ecs cluster events to cloudwatch by default ([#1116](https://github.com/oslokommune/golden-path-boilerplate/issues/1116)) ([50384a1](https://github.com/oslokommune/golden-path-boilerplate/commit/50384a10c943cc41cca5e1ed541d08589867055b))
* Support directories as dependencies in template ([c388500](https://github.com/oslokommune/golden-path-boilerplate/commit/c388500ed611e3a11490de8be33177081e9208d5))
