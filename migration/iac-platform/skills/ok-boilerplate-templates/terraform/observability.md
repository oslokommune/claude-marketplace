# Template: observability

## Metadata

- **Version**: `3.0.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/observability`
- **Last Commit**: `0ca8c1c8` - deps: Update Terraform dependency lock files (#1402) (2025-09-04)
- **Last Generated**: 2025-11-07

## Purpose

|       Name       |         Description          | Type | Default |Required|
|------------------|------------------------------|------|---------|--------|
|`EnablePrometheus`|Enable Prometheus.            |`bool`|``true`` |no      |
|`EnableGrafana`   |Enable Grafana.               |`bool`|``true`` |no      |
|`IncludeLockFile` |Include a Terraform lock file.|`bool`|``false``|no      |

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)
- **terragrunt** (version: `latest`)

## Variables

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `EnablePrometheus` | `bool` | true | Enable Prometheus. |
| `EnableGrafana` | `bool` | true | Enable Grafana. |
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |

## Example Configuration

From `package-config-default.yml`:


```yaml

StackName: observability
GrafanaAdminGroupNames: DS-OOO_AWS_MYTEAM_DEV
GrafanaEditorGroupNames: DS-OOO_AWS_MYTEAM_TEAM

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`
- `__gp_dependencies_grafana.tf`
- `__gp_variables_grafana.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_grafana.tf`
- `_gp_grafana_api_keys.tf`
- `_gp_prometheus.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Other Files

- `.terraform.lock.hcl`
- `_gp_rm_gp_file.sh`
- `boilerplate.yml`

## Conditional File Generation

- Always skip: `package-config*.yml`
- Skip `config_override.tf` if: `{{ list outputFolder "config_override.tf" | join "/" | pathExists }}`
- Skip `*grafana*` if: `{{ not .EnableGrafana }}`
- Skip `*prometheus*` if: `{{ not .EnablePrometheus }}`
- Skip `.terraform.lock.hcl*` if: `{{ not .IncludeLockFile }}`

## Recent Changes

## [3.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/observability-v2.8.0...observability-v3.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))


### Dependency updates

* update dependency versions to v5 ([#1454](https://github.com/oslokommune/golden-path-boilerplate/issues/1454)) ([01fb21e](https://github.com/oslokommune/golden-path-boilerplate/commit/01fb21e7c1891dbf57451fbdd248bb59a79304e9))

## [2.8.0](https://github.com/oslokommune/golden-path-boilerplate/compare/observability-v2.7.2...observability-v2.8.0) (2025-07-26)


### Features

* Move var files for lock file generation to template dir ([#1346](https://github.com/oslokommune/golden-path-boilerplate/issues/1346)) ([d0a4b02](https://github.com/oslokommune/golden-path-boilerplate/commit/d0a4b02653613a92e8fcd582d14a2f3c911c17b0))


### Bug fixes

* Remove error in case template lockfile is missing ([#1358](https://github.com/oslokommune/golden-path-boilerplate/issues/1358)) ([22debb6](https://github.com/oslokommune/golden-path-boilerplate/commit/22debb6595935feccca61e7afb1f72c51d102514))


### Dependency updates

* update dependency versions to v3.4.0 ([#1367](https://github.com/oslokommune/golden-path-boilerplate/issues/1367)) ([16f6283](https://github.com/oslokommune/golden-path-boilerplate/commit/16f628302d18f079b62f3c66d8adb6ae30b569c2))
* Update Terraform dependency lock files ([#1308](https://github.com/oslokommune/golden-path-boilerplate/issues/1308)) ([1f49902](https://github.com/oslokommune/golden-path-boilerplate/commit/1f49902150a5431d0d9815aaafad8b8858940e9c))

## [2.7.2](https://github.com/oslokommune/golden-path-boilerplate/compare/observability-v2.7.1...observability-v2.7.2) (2025-06-25)


### Dependency updates

* Update Terraform dependency lock files ([#1206](https://github.com/oslokommune/golden-path-boilerplate/issues/1206)) ([b94e3c6](https://github.com/oslokommune/golden-path-boilerplate/commit/b94e3c601c31dcb7d37f2948631acbbb387ff32d))

## [2.7.1](https://github.com/oslokommune/golden-path-boilerplate/compare/observability-v2.7.0...observability-v2.7.1) (2025-06-24)


### Dependency updates

* update dependency versions to v3.3.0 ([#1224](https://github.com/oslokommune/golden-path-boilerplate/issues/1224)) ([d2581ac](https://github.com/oslokommune/golden-path-boilerplate/commit/d2581ace71ccaf2ff7f677e22d0cac4cec3c2b34))

## [2.7.0](https://github.com/oslokommune/golden-path-boilerplate/compare/observability-v2.6.0...observability-v2.7.0) (2025-06-19)


### Features

* Support directories as dependencies in template ([c388500](https://github.com/oslokommune/golden-path-boilerplate/commit/c388500ed611e3a11490de8be33177081e9208d5))


### Bug fixes

* Delete files from Golden path only ([#1162](https://github.com/oslokommune/golden-path-boilerplate/issues/1162)) ([bd43212](https://github.com/oslokommune/golden-path-boilerplate/commit/bd43212378defcb9437e54e2ccfb52b0502e1ff0))
* Remove sh files with delete-marker ([#1171](https://github.com/oslokommune/golden-path-boilerplate/issues/1171)) ([2ac3158](https://github.com/oslokommune/golden-path-boilerplate/commit/2ac31581acda734fec295a462d05e8b6f48f332b))
