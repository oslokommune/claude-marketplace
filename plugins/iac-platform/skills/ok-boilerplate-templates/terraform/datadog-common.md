# Template: datadog-common

## Metadata

- **Version**: `2.0.1`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/datadog-common`
- **Last Commit**: `371eb5a4` - feat: add terragrunt setup for all stacks needed. add bin scripts to delete necessary resources (#1622) (2025-11-04)
- **Last Generated**: 2025-11-07

## Purpose

|      Name       |         Description          | Type |      Default       |Required|
|-----------------|------------------------------|------|--------------------|--------|
|`IncludeLockFile`|Include a Terraform lock file.|`bool`|``false``           |no      |
|`IntegrationRole`|IAM role for Datadog          |`map` |``{"Enable": true}``|no      |
|`LambdaForwarder`|Lambda forwarder for Datadog  |`map` |``{"Enable": true}``|no      |

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)

## Variables

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `IntegrationRole` | `map` | `{Enable: true}` | IAM role for Datadog |
| `LambdaForwarder` | `map` | `{Enable: true}` | Lambda forwarder for Datadog |

## Feature Flags

These map-type variables control optional features:

### IntegrationRole

IAM role for Datadog


**Default configuration:**
```yaml

IntegrationRole:
  Enable: true

```


### LambdaForwarder

Lambda forwarder for Datadog


**Default configuration:**
```yaml

LambdaForwarder:
  Enable: true

```


## Example Configuration

From `package-config-default.yml`:


```yaml

StackName: datadog-common

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`
- `__gp_dependencies.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_lambda_forwarder.tf`
- `_gp_role.tf`
- `_gp_secrets.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Other Files

- `.terraform.lock.hcl`
- `boilerplate.yml`
- `terragrunt.hcl`
- `terragrunt_custom.hcl`

## Conditional File Generation

- Always skip: `package-config*.yml`
- Skip `.terraform.lock.hcl*` if: `{{ not .IncludeLockFile }}`
- Skip `config_override.tf` if: `{{ list outputFolder "config_override.tf" | join "/" | pathExists }}`
- Skip `terragrunt_custom.hcl` if: `{{ list outputFolder "terragrunt_custom.hcl" | join "/" | pathExists }}`

## Recent Changes

## [2.0.1](https://github.com/oslokommune/golden-path-boilerplate/compare/datadog-common-v2.0.0...datadog-common-v2.0.1) (2025-10-15)


### Bug fixes

* customizable name of OTel environment ([#1604](https://github.com/oslokommune/golden-path-boilerplate/issues/1604)) ([ddb350c](https://github.com/oslokommune/golden-path-boilerplate/commit/ddb350c94c085ca5cdad68cb4e28884b5a576d2c))


### Dependency updates

* Update Terraform dependency lock files ([#1402](https://github.com/oslokommune/golden-path-boilerplate/issues/1402)) ([0ca8c1c](https://github.com/oslokommune/golden-path-boilerplate/commit/0ca8c1c8ee2b0e25a6fd7e19685d15e9524aeacc))

## [2.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/datadog-common-v1.1.1...datadog-common-v2.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))


### Dependency updates

* update dependency versions to v5 ([#1454](https://github.com/oslokommune/golden-path-boilerplate/issues/1454)) ([01fb21e](https://github.com/oslokommune/golden-path-boilerplate/commit/01fb21e7c1891dbf57451fbdd248bb59a79304e9))

## [1.1.1](https://github.com/oslokommune/golden-path-boilerplate/compare/datadog-common-v1.1.0...datadog-common-v1.1.1) (2025-07-30)


### Bug fixes

* store datadog api key in secrets manager ([#1399](https://github.com/oslokommune/golden-path-boilerplate/issues/1399)) ([d4a30db](https://github.com/oslokommune/golden-path-boilerplate/commit/d4a30db59bf25b20c33fe4e9e6ef7e793ecc7963))

## [1.1.0](https://github.com/oslokommune/golden-path-boilerplate/compare/datadog-common-v1.0.2...datadog-common-v1.1.0) (2025-07-26)


### Features

* Move var files for lock file generation to template dir ([#1346](https://github.com/oslokommune/golden-path-boilerplate/issues/1346)) ([d0a4b02](https://github.com/oslokommune/golden-path-boilerplate/commit/d0a4b02653613a92e8fcd582d14a2f3c911c17b0))


### Bug fixes

* Add IncludeLockFile to all Terraform boilerplate templates ([#1347](https://github.com/oslokommune/golden-path-boilerplate/issues/1347)) ([1a77fab](https://github.com/oslokommune/golden-path-boilerplate/commit/1a77fab696c5ad2523abbdc22a85b57f46399d3e))
* Remove error in case template lockfile is missing ([#1358](https://github.com/oslokommune/golden-path-boilerplate/issues/1358)) ([22debb6](https://github.com/oslokommune/golden-path-boilerplate/commit/22debb6595935feccca61e7afb1f72c51d102514))


### Dependency updates

* update dependency versions to v3.4.0 ([#1367](https://github.com/oslokommune/golden-path-boilerplate/issues/1367)) ([16f6283](https://github.com/oslokommune/golden-path-boilerplate/commit/16f628302d18f079b62f3c66d8adb6ae30b569c2))
* Update Terraform dependency lock files ([#1308](https://github.com/oslokommune/golden-path-boilerplate/issues/1308)) ([1f49902](https://github.com/oslokommune/golden-path-boilerplate/commit/1f49902150a5431d0d9815aaafad8b8858940e9c))

## [1.0.2](https://github.com/oslokommune/golden-path-boilerplate/compare/datadog-common-v1.0.1...datadog-common-v1.0.2) (2025-06-27)


### Dependency updates

* Update Terraform dependency lock files ([#1270](https://github.com/oslokommune/golden-path-boilerplate/issues/1270)) ([1fa683f](https://github.com/oslokommune/golden-path-boilerplate/commit/1fa683f31cb857ed3bc8123162df8ef22c44dfad))
