# Template: networking

## Metadata

- **Version**: `3.0.1`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/networking`
- **Last Commit**: `371eb5a4` - feat: add terragrunt setup for all stacks needed. add bin scripts to delete necessary resources (#1622) (2025-11-04)
- **Last Generated**: 2025-11-07

## Purpose

|      Name       |         Description          | Type |                                                                                                          Default                                                                                                          |Required|
|-----------------|------------------------------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
|`IncludeLockFile`|Include a Terraform lock file.|`bool`|``false``                                                                                                                                                                                                                  |no      |
|`VpcEndpoints`   |Enable VPC Endpoints          |`map` |``{"Enable": false, "Ecr": false, "Dkr": false, "Logs": false, "SsmMessages": false, "Prometheus": false, "Ssm": false, "S3": false, "Xray": false, "Sqs": false, "SecretsManager": false, "Sts": false, "Lambda": false}``|no      |
|`VpcFlowLogs`    |Enable VPC Flow Logs          |`map` |``{"Enable": false}``                                                                                                                                                                                                      |no      |

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)
- **networking-data** (version: `networking-data-v1.0.0`)
- **terragrunt** (version: `latest`)

## Variables

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `VpcEndpoints` | `map` | `{Dkr: false, Ecr: false, Enable: false, Lambda: false, Logs: false, Prometheus: false,
  S3: false, SecretsManager: false, Sqs: false, Ssm: false, SsmMessages: false, Sts: false,
  Xray: false}` | Enable VPC Endpoints |
| `VpcFlowLogs` | `map` | `{Enable: false}` | Enable VPC Flow Logs |

## Feature Flags

These map-type variables control optional features:

### VpcEndpoints

Enable VPC Endpoints


**Default configuration:**
```yaml

VpcEndpoints:
  Dkr: false
  Ecr: false
  Enable: false
  Lambda: false
  Logs: false
  Prometheus: false
  S3: false
  SecretsManager: false
  Sqs: false
  Ssm: false
  SsmMessages: false
  Sts: false
  Xray: false

```


### VpcFlowLogs

Enable VPC Flow Logs


**Default configuration:**
```yaml

VpcFlowLogs:
  Enable: false

```


## Example Configuration

From `package-config-default.yml`:


```yaml

StackName: networking
networking-data.StackName: networking-data
VpcFlowLogs:
  Enable: true

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`
- `__gp_dependencies.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_vpc.tf`
- `_gp_vpc_endpoints.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Helper Scripts

- `bin/_gp_networking-remove-all-vpce.sh`
- `bin/_gp_networking-remove-security-groups.sh`

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

## [3.0.1](https://github.com/oslokommune/golden-path-boilerplate/compare/networking-v3.0.0...networking-v3.0.1) (2025-08-06)


### Dependency updates

* update dependency networking-data to v1 ([#1460](https://github.com/oslokommune/golden-path-boilerplate/issues/1460)) ([345744d](https://github.com/oslokommune/golden-path-boilerplate/commit/345744d48ea2fc7fcdac6d54cfeaa828775c1989))

## [3.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/networking-v2.11.0...networking-v3.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))


### Bug fixes

* create role for vpc flow logs outside of module ([#1436](https://github.com/oslokommune/golden-path-boilerplate/issues/1436)) ([930de7e](https://github.com/oslokommune/golden-path-boilerplate/commit/930de7e4c77fcd2cd25499497759bd3f03da8514))


### Dependency updates

* update dependency networking-data to v1 ([#1459](https://github.com/oslokommune/golden-path-boilerplate/issues/1459)) ([e024789](https://github.com/oslokommune/golden-path-boilerplate/commit/e0247896f11267b3f33b149fb5223a99f941ac20))
* update dependency versions to v5 ([#1454](https://github.com/oslokommune/golden-path-boilerplate/issues/1454)) ([01fb21e](https://github.com/oslokommune/golden-path-boilerplate/commit/01fb21e7c1891dbf57451fbdd248bb59a79304e9))

## [2.11.0](https://github.com/oslokommune/golden-path-boilerplate/compare/networking-v2.10.1...networking-v2.11.0) (2025-07-26)


### Features

* Move var files for lock file generation to template dir ([#1346](https://github.com/oslokommune/golden-path-boilerplate/issues/1346)) ([d0a4b02](https://github.com/oslokommune/golden-path-boilerplate/commit/d0a4b02653613a92e8fcd582d14a2f3c911c17b0))


### Bug fixes

* Add IncludeLockFile to all Terraform boilerplate templates ([#1347](https://github.com/oslokommune/golden-path-boilerplate/issues/1347)) ([1a77fab](https://github.com/oslokommune/golden-path-boilerplate/commit/1a77fab696c5ad2523abbdc22a85b57f46399d3e))
* Remove error in case template lockfile is missing ([#1358](https://github.com/oslokommune/golden-path-boilerplate/issues/1358)) ([22debb6](https://github.com/oslokommune/golden-path-boilerplate/commit/22debb6595935feccca61e7afb1f72c51d102514))


### Dependency updates

* update dependency networking-data to v0.5.2 ([#1374](https://github.com/oslokommune/golden-path-boilerplate/issues/1374)) ([39a0e00](https://github.com/oslokommune/golden-path-boilerplate/commit/39a0e005e71172dcca476dd2af3e6b8d54d340da))
* update dependency versions to v3.4.0 ([#1367](https://github.com/oslokommune/golden-path-boilerplate/issues/1367)) ([16f6283](https://github.com/oslokommune/golden-path-boilerplate/commit/16f628302d18f079b62f3c66d8adb6ae30b569c2))
* Update Terraform dependency lock files ([#1308](https://github.com/oslokommune/golden-path-boilerplate/issues/1308)) ([1f49902](https://github.com/oslokommune/golden-path-boilerplate/commit/1f49902150a5431d0d9815aaafad8b8858940e9c))

## [2.10.1](https://github.com/oslokommune/golden-path-boilerplate/compare/networking-v2.10.0...networking-v2.10.1) (2025-06-25)


### Bug fixes

* Downgrade VPC module to avoid flow logs issue ([#1247](https://github.com/oslokommune/golden-path-boilerplate/issues/1247)) ([1689136](https://github.com/oslokommune/golden-path-boilerplate/commit/16891363caebe9f67793f375408d18d2d192db99))


### Dependency updates

* update dependency networking-data to v0.5.0 ([#1218](https://github.com/oslokommune/golden-path-boilerplate/issues/1218)) ([59ae1dc](https://github.com/oslokommune/golden-path-boilerplate/commit/59ae1dcc31b63e2f82e5863fd26613a6c813ed2c))
* update dependency networking-data to v0.5.1 ([#1250](https://github.com/oslokommune/golden-path-boilerplate/issues/1250)) ([a6f4db9](https://github.com/oslokommune/golden-path-boilerplate/commit/a6f4db9965e2c2ba38dc55033cf553439c4ac4db))
* update dependency versions to v3.3.0 ([#1224](https://github.com/oslokommune/golden-path-boilerplate/issues/1224)) ([d2581ac](https://github.com/oslokommune/golden-path-boilerplate/commit/d2581ace71ccaf2ff7f677e22d0cac4cec3c2b34))
* Update Terraform dependency lock files ([#1206](https://github.com/oslokommune/golden-path-boilerplate/issues/1206)) ([b94e3c6](https://github.com/oslokommune/golden-path-boilerplate/commit/b94e3c601c31dcb7d37f2948631acbbb387ff32d))

## [2.10.0](https://github.com/oslokommune/golden-path-boilerplate/compare/networking-v2.9.0...networking-v2.10.0) (2025-06-19)


### Features

* Support directories as dependencies in template ([c388500](https://github.com/oslokommune/golden-path-boilerplate/commit/c388500ed611e3a11490de8be33177081e9208d5))


### Bug fixes

* Delete files from Golden path only ([#1162](https://github.com/oslokommune/golden-path-boilerplate/issues/1162)) ([bd43212](https://github.com/oslokommune/golden-path-boilerplate/commit/bd43212378defcb9437e54e2ccfb52b0502e1ff0))
* Remove sh files with delete-marker ([#1171](https://github.com/oslokommune/golden-path-boilerplate/issues/1171)) ([2ac3158](https://github.com/oslokommune/golden-path-boilerplate/commit/2ac31581acda734fec295a462d05e8b6f48f332b))
* require a CIDR range to be chose for VPC setup ([#1012](https://github.com/oslokommune/golden-path-boilerplate/issues/1012)) ([bd72599](https://github.com/oslokommune/golden-path-boilerplate/commit/bd72599d3e5c2d263e3e955f4e4f748be54ad86b))


### Dependency updates

* Update Terraform dependency lock files ([#1149](https://github.com/oslokommune/golden-path-boilerplate/issues/1149)) ([7c500b3](https://github.com/oslokommune/golden-path-boilerplate/commit/7c500b3f870df325e5744ba29d3fb43798e1c882))
