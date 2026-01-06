# Template: cloudfront-static-website-data

## Metadata

- **Version**: `1.0.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/cloudfront-static-website-data`
- **Last Commit**: `371eb5a4` - feat: add terragrunt setup for all stacks needed. add bin scripts to delete necessary resources (#1622) (2025-11-04)
- **Last Generated**: 2025-11-07

## Purpose

This stack contains the data resources (S3 buckets) for CloudFront static websites.

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)

## Variables

### Required Variables

| Name | Type | Description |
|------|------|-------------|
| `Name` | `string` | Name for the CloudFront static website data resources |

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

- `_gp_dependencies.tf`
- `_gp_s3.tf`
- `_gp_s3_logs.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Other Files

- `boilerplate.yml`
- `terragrunt.hcl`
- `terragrunt_custom.hcl`

## Conditional File Generation

- Skip `.terraform.lock.hcl*` if: `{{ not .IncludeLockFile }}`
- Skip `config_override.tf` if: `{{ list outputFolder "config_override.tf" | join "/" | pathExists }}`
- Skip `terragrunt_custom.hcl` if: `{{ list outputFolder "terragrunt_custom.hcl" | join "/" | pathExists }}`

## Recent Changes

## [1.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-static-website-data-v0.2.2...cloudfront-static-website-data-v1.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))


### Bug fixes

* use known keys for datadog log subscriber ([#1383](https://github.com/oslokommune/golden-path-boilerplate/issues/1383)) ([9d82fcd](https://github.com/oslokommune/golden-path-boilerplate/commit/9d82fcdc3ecedf39122c0d41349ee4697f3de573))


### Dependency updates

* update dependency versions to v5 ([#1454](https://github.com/oslokommune/golden-path-boilerplate/issues/1454)) ([01fb21e](https://github.com/oslokommune/golden-path-boilerplate/commit/01fb21e7c1891dbf57451fbdd248bb59a79304e9))

## [0.2.2](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-static-website-data-v0.2.1...cloudfront-static-website-data-v0.2.2) (2025-07-26)


### Dependency updates

* update dependency versions to v3.4.0 ([#1367](https://github.com/oslokommune/golden-path-boilerplate/issues/1367)) ([16f6283](https://github.com/oslokommune/golden-path-boilerplate/commit/16f628302d18f079b62f3c66d8adb6ae30b569c2))

## [0.2.1](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-static-website-data-v0.2.0...cloudfront-static-website-data-v0.2.1) (2025-07-23)


### Bug fixes

* Remove error in case template lockfile is missing ([#1358](https://github.com/oslokommune/golden-path-boilerplate/issues/1358)) ([22debb6](https://github.com/oslokommune/golden-path-boilerplate/commit/22debb6595935feccca61e7afb1f72c51d102514))

## [0.2.0](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-static-website-data-v0.1.0...cloudfront-static-website-data-v0.2.0) (2025-07-23)


### Features

* add AutoForwardLogs feature ([#1342](https://github.com/oslokommune/golden-path-boilerplate/issues/1342)) ([14d1183](https://github.com/oslokommune/golden-path-boilerplate/commit/14d118306c709e8dd1db71a5a3e38ff40addad8c))
* Add cloudfront-static-website-data stack for S3 buckets ([#1333](https://github.com/oslokommune/golden-path-boilerplate/issues/1333)) ([14d34c3](https://github.com/oslokommune/golden-path-boilerplate/commit/14d34c3e55fda279791c7cbce4ce45a78dbf58e5))
* **terraform:** add force_destroy option to cloudfront-static-website-data ([#1340](https://github.com/oslokommune/golden-path-boilerplate/issues/1340)) ([903156e](https://github.com/oslokommune/golden-path-boilerplate/commit/903156eb0da922cf8cce9cede9222546a6b133d5))


### Bug fixes

* Add IncludeLockFile to all Terraform boilerplate templates ([#1347](https://github.com/oslokommune/golden-path-boilerplate/issues/1347)) ([1a77fab](https://github.com/oslokommune/golden-path-boilerplate/commit/1a77fab696c5ad2523abbdc22a85b57f46399d3e))
* Remove unused SSM parameter for CloudFront logs S3 bucket ID ([5b8b992](https://github.com/oslokommune/golden-path-boilerplate/commit/5b8b99299e5adfe21bc51ee9b00233b4c8873686))
