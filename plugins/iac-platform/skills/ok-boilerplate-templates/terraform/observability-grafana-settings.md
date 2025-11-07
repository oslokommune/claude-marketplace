# Template: observability-grafana-settings

## Metadata

- **Version**: `3.0.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/observability-grafana-settings`
- **Last Commit**: `8dd6645e` - docs: Update Boilerplate template docs (#1455) (2025-08-06)
- **Last Generated**: 2025-11-07

## Purpose

|      Name       |                                      Description                                      | Type |       Default       |Required|
|-----------------|---------------------------------------------------------------------------------------|------|---------------------|--------|
|`IncludeLockFile`|Include a Terraform lock file.                                                         |`bool`|``false``            |no      |
|`Terragrunt`     |Enable Terragrunt. This is a experimental feature and should not be used in production.|`map` |``{"Enable": false}``|no      |
<!-- BOILERPLATE END -->

## Dependencies

This template depends on:

- **terragrunt** (version: `latest`)

## Variables

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `Terragrunt` | `map` | `{Enable: false}` | Enable Terragrunt. This is a experimental feature and should not be used in production. |

## Feature Flags

These map-type variables control optional features:

### Terragrunt

Enable Terragrunt.
This is a experimental feature and should not be used in production.


**Default configuration:**
```yaml

Terragrunt:
  Enable: false

```


## Example Configuration

From `package-config-default.yml`:


```yaml

StackName: observability-grafana-settings

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`
- `__gp_dependencies.tf`
- `__gp_versions.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_grafana_settings.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Other Files

- `.terraform.lock.hcl`
- `_gp_rm_gp_file.sh`
- `boilerplate.yml`
- `templates/replace.sh`
- `terragrunt.hcl`
- `terragrunt_custom.hcl`

## Conditional File Generation

- Always skip: `package-config*.yml`
- Skip `.terraform.lock.hcl*` if: `{{ not .IncludeLockFile }}`
- Skip `terragrunt_custom.hcl` if: `{{ list outputFolder "terragrunt_custom.hcl" | join "/" | pathExists }}`
- Skip `config_override.tf` if: `{{ list outputFolder "config_override.tf" | join "/" | pathExists }}`

## Recent Changes

## [3.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/observability-grafana-settings-v2.4.0...observability-grafana-settings-v3.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))

## [2.4.0](https://github.com/oslokommune/golden-path-boilerplate/compare/observability-grafana-settings-v2.3.3...observability-grafana-settings-v2.4.0) (2025-07-25)


### Features

* Move var files for lock file generation to template dir ([#1346](https://github.com/oslokommune/golden-path-boilerplate/issues/1346)) ([d0a4b02](https://github.com/oslokommune/golden-path-boilerplate/commit/d0a4b02653613a92e8fcd582d14a2f3c911c17b0))


### Bug fixes

* Add IncludeLockFile to all Terraform boilerplate templates ([#1347](https://github.com/oslokommune/golden-path-boilerplate/issues/1347)) ([1a77fab](https://github.com/oslokommune/golden-path-boilerplate/commit/1a77fab696c5ad2523abbdc22a85b57f46399d3e))
* Remove error in case template lockfile is missing ([#1358](https://github.com/oslokommune/golden-path-boilerplate/issues/1358)) ([22debb6](https://github.com/oslokommune/golden-path-boilerplate/commit/22debb6595935feccca61e7afb1f72c51d102514))

## [2.3.3](https://github.com/oslokommune/golden-path-boilerplate/compare/observability-grafana-settings-v2.3.2...observability-grafana-settings-v2.3.3) (2025-06-19)


### Bug fixes

* Delete files from Golden path only ([#1162](https://github.com/oslokommune/golden-path-boilerplate/issues/1162)) ([bd43212](https://github.com/oslokommune/golden-path-boilerplate/commit/bd43212378defcb9437e54e2ccfb52b0502e1ff0))
* Remove sh files with delete-marker ([#1171](https://github.com/oslokommune/golden-path-boilerplate/issues/1171)) ([2ac3158](https://github.com/oslokommune/golden-path-boilerplate/commit/2ac31581acda734fec295a462d05e8b6f48f332b))

## [2.3.2](https://github.com/oslokommune/golden-path-boilerplate/compare/observability-grafana-settings-v2.3.1...observability-grafana-settings-v2.3.2) (2025-02-18)


### Bug fixes

* Use terragrunt dependency ([0cda36e](https://github.com/oslokommune/golden-path-boilerplate/commit/0cda36ed558983b084a02a0f2201513b38a3462b))

## [2.3.1](https://github.com/oslokommune/golden-path-boilerplate/compare/observability-grafana-settings-v2.3.0...observability-grafana-settings-v2.3.1) (2024-12-23)


### Bug fixes

* set less restrictive terraform version ([#846](https://github.com/oslokommune/golden-path-boilerplate/issues/846)) ([a29539d](https://github.com/oslokommune/golden-path-boilerplate/commit/a29539d453ca7482e3fb017b9e3b4f32e5187260))
