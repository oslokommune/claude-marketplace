# Template: load-balancing-alb-data

## Metadata

- **Version**: `3.1.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/load-balancing-alb-data`
- **Last Commit**: `9102e8c9` - fix: correct naming of load balancer for terragrunt scripts (#1637) (2025-11-06)
- **Last Generated**: 2025-11-07

## Purpose

|      Name       |                                                                   Description                                                                   | Type |      Default       |Required|
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------|--------------------|--------|
|`IncludeLockFile`|Include a Terraform lock file.                                                                                                                   |`bool`|``false``           |no      |
|`AutoForwardLogs`|Automatically forward any CloudWatch log groups or S3 logs created by this template to Datadog if the current account is integrated with Datadog.|`map` |``{"Enable": true}``|no      |
<!-- BOILERPLATE END -->

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)

## Variables

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `AutoForwardLogs` | `map` | `{Enable: true}` | Automatically forward any CloudWatch log groups or S3 logs created by this template to Datadog if the current account is integrated with Datadog. |

## Feature Flags

These map-type variables control optional features:

### AutoForwardLogs

Automatically forward any CloudWatch log groups or S3 logs created by this template to Datadog if the current account is integrated with Datadog.


**Default configuration:**
```yaml

AutoForwardLogs:
  Enable: true

```


## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_alb_s3.tf`
- `_gp_dependencies.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Helper Scripts

- `bin/_gp_load-balancing-alb-empty-bucket.sh`

### Other Files

- `.terraform.lock.hcl`
- `boilerplate.yml`
- `terragrunt.hcl`
- `terragrunt_custom.hcl`

## Conditional File Generation

- Skip `.terraform.lock.hcl*` if: `{{ not .IncludeLockFile }}`
- Skip `config_override.tf` if: `{{ list outputFolder "config_override.tf" | join "/" | pathExists }}`
- Skip `terragrunt_custom.hcl` if: `{{ list outputFolder "terragrunt_custom.hcl" | join "/" | pathExists }}`

## Recent Changes

## [3.1.0](https://github.com/oslokommune/golden-path-boilerplate/compare/load-balancing-alb-data-v3.0.0...load-balancing-alb-data-v3.1.0) (2025-08-13)


### Features

* require SSL transport to ALB log bucket ([#1464](https://github.com/oslokommune/golden-path-boilerplate/issues/1464)) ([4a029be](https://github.com/oslokommune/golden-path-boilerplate/commit/4a029bee0b9f9d22819cac75e96500d6a7be97f7))

## [3.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/load-balancing-alb-data-v2.6.3...load-balancing-alb-data-v3.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))


### Dependency updates

* update dependency versions to v5 ([#1454](https://github.com/oslokommune/golden-path-boilerplate/issues/1454)) ([01fb21e](https://github.com/oslokommune/golden-path-boilerplate/commit/01fb21e7c1891dbf57451fbdd248bb59a79304e9))

## [2.6.3](https://github.com/oslokommune/golden-path-boilerplate/compare/load-balancing-alb-data-v2.6.2...load-balancing-alb-data-v2.6.3) (2025-07-29)


### Bug fixes

* use known keys for datadog log subscriber ([#1383](https://github.com/oslokommune/golden-path-boilerplate/issues/1383)) ([9d82fcd](https://github.com/oslokommune/golden-path-boilerplate/commit/9d82fcdc3ecedf39122c0d41349ee4697f3de573))

## [2.6.2](https://github.com/oslokommune/golden-path-boilerplate/compare/load-balancing-alb-data-v2.6.1...load-balancing-alb-data-v2.6.2) (2025-07-26)


### Bug fixes

* Add IncludeLockFile to all Terraform boilerplate templates ([#1347](https://github.com/oslokommune/golden-path-boilerplate/issues/1347)) ([1a77fab](https://github.com/oslokommune/golden-path-boilerplate/commit/1a77fab696c5ad2523abbdc22a85b57f46399d3e))
* Remove error in case template lockfile is missing ([#1358](https://github.com/oslokommune/golden-path-boilerplate/issues/1358)) ([22debb6](https://github.com/oslokommune/golden-path-boilerplate/commit/22debb6595935feccca61e7afb1f72c51d102514))


### Dependency updates

* update dependency versions to v3.4.0 ([#1367](https://github.com/oslokommune/golden-path-boilerplate/issues/1367)) ([16f6283](https://github.com/oslokommune/golden-path-boilerplate/commit/16f628302d18f079b62f3c66d8adb6ae30b569c2))
* Update Terraform dependency lock files ([#1308](https://github.com/oslokommune/golden-path-boilerplate/issues/1308)) ([1f49902](https://github.com/oslokommune/golden-path-boilerplate/commit/1f49902150a5431d0d9815aaafad8b8858940e9c))

## [2.6.1](https://github.com/oslokommune/golden-path-boilerplate/compare/load-balancing-alb-data-v2.6.0...load-balancing-alb-data-v2.6.1) (2025-06-26)


### Dependency updates

* update dependency datadog-log-subscription to v0.1.1 ([#1256](https://github.com/oslokommune/golden-path-boilerplate/issues/1256)) ([ca52cd8](https://github.com/oslokommune/golden-path-boilerplate/commit/ca52cd8a0a31b4b8038af94c73b84d00155d533a))
