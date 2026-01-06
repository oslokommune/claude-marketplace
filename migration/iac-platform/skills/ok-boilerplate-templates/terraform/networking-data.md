# Template: networking-data

## Metadata

- **Version**: `1.0.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/networking-data`
- **Last Commit**: `371eb5a4` - feat: add terragrunt setup for all stacks needed. add bin scripts to delete necessary resources (#1622) (2025-11-04)
- **Last Generated**: 2025-11-07

## Purpose

|      Name       |         Description          | Type | Default |Required|
|-----------------|------------------------------|------|---------|--------|
|`IncludeLockFile`|Include a Terraform lock file.|`bool`|``false``|no      |
<!-- BOILERPLATE END -->

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)
- **terragrunt** (version: `latest`)

## Variables

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_vpc_flow_logs.tf`

### User Override Files

- `config_override.tf` (user-customizable)

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

## [1.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/networking-data-v0.5.2...networking-data-v1.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))


### Dependency updates

* update dependency versions to v5 ([#1454](https://github.com/oslokommune/golden-path-boilerplate/issues/1454)) ([01fb21e](https://github.com/oslokommune/golden-path-boilerplate/commit/01fb21e7c1891dbf57451fbdd248bb59a79304e9))

## [0.5.2](https://github.com/oslokommune/golden-path-boilerplate/compare/networking-data-v0.5.1...networking-data-v0.5.2) (2025-07-26)


### Bug fixes

* Add IncludeLockFile to all Terraform boilerplate templates ([#1347](https://github.com/oslokommune/golden-path-boilerplate/issues/1347)) ([1a77fab](https://github.com/oslokommune/golden-path-boilerplate/commit/1a77fab696c5ad2523abbdc22a85b57f46399d3e))
* Remove error in case template lockfile is missing ([#1358](https://github.com/oslokommune/golden-path-boilerplate/issues/1358)) ([22debb6](https://github.com/oslokommune/golden-path-boilerplate/commit/22debb6595935feccca61e7afb1f72c51d102514))


### Dependency updates

* update dependency versions to v3.4.0 ([#1367](https://github.com/oslokommune/golden-path-boilerplate/issues/1367)) ([16f6283](https://github.com/oslokommune/golden-path-boilerplate/commit/16f628302d18f079b62f3c66d8adb6ae30b569c2))
* Update Terraform dependency lock files ([#1308](https://github.com/oslokommune/golden-path-boilerplate/issues/1308)) ([1f49902](https://github.com/oslokommune/golden-path-boilerplate/commit/1f49902150a5431d0d9815aaafad8b8858940e9c))

## [0.5.1](https://github.com/oslokommune/golden-path-boilerplate/compare/networking-data-v0.5.0...networking-data-v0.5.1) (2025-06-25)


### Dependency updates

* update dependency versions to v3.3.0 ([#1224](https://github.com/oslokommune/golden-path-boilerplate/issues/1224)) ([d2581ac](https://github.com/oslokommune/golden-path-boilerplate/commit/d2581ace71ccaf2ff7f677e22d0cac4cec3c2b34))
* Update Terraform dependency lock files ([#1206](https://github.com/oslokommune/golden-path-boilerplate/issues/1206)) ([b94e3c6](https://github.com/oslokommune/golden-path-boilerplate/commit/b94e3c601c31dcb7d37f2948631acbbb387ff32d))

## [0.5.0](https://github.com/oslokommune/golden-path-boilerplate/compare/networking-data-v0.4.2...networking-data-v0.5.0) (2025-06-19)


### Features

* Support directories as dependencies in template ([c388500](https://github.com/oslokommune/golden-path-boilerplate/commit/c388500ed611e3a11490de8be33177081e9208d5))


### Dependency updates

* Update Terraform dependency lock files ([#1149](https://github.com/oslokommune/golden-path-boilerplate/issues/1149)) ([7c500b3](https://github.com/oslokommune/golden-path-boilerplate/commit/7c500b3f870df325e5744ba29d3fb43798e1c882))

## [0.4.2](https://github.com/oslokommune/golden-path-boilerplate/compare/networking-data-v0.4.1...networking-data-v0.4.2) (2025-03-13)


### Dependency updates

* Update Terraform dependency lock files ([#1068](https://github.com/oslokommune/golden-path-boilerplate/issues/1068)) ([6c27e84](https://github.com/oslokommune/golden-path-boilerplate/commit/6c27e84023c4481e7f4335f518b1f04fd2a854a8))
