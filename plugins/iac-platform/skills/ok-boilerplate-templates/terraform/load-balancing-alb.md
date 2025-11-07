# Template: load-balancing-alb

## Metadata

- **Version**: `4.0.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/load-balancing-alb`
- **Last Commit**: `9102e8c9` - fix: correct naming of load balancer for terragrunt scripts (#1637) (2025-11-06)
- **Last Generated**: 2025-11-07

## Purpose

|      Name       |                                                                                                           Description                                                                                                            |  Type  |                 Default                 |Required|
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------|--------|
|`IncludeLockFile`|Include a Terraform lock file.                                                                                                                                                                                                    |`bool`  |``false``                                |no      |
|`Name`           |Application Load Balancer name                                                                                                                                                                                                    |`string`|``main``                                 |no      |
|`Internal`       |If true, the Application Load Balancer will be internal. If false, it will be internet-facing.                                                                                                                                    |`bool`  |``true``                                 |no      |

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)
- **load-balancing-alb-data** (version: `load-balancing-alb-data-v3.0.0`)

## Variables

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `Name` | `string` | `main` | Application Load Balancer name |
| `Internal` | `bool` | true | If true, the Application Load Balancer will be internal. If false, it will be internet-facing. |
| `Dns` | `map` | `{Enable: true, EnableHttps: true}` | If Enable is true, a Route 53 record will be created for the ALB. If EnableHttps is true, a certificate will be configured for the domain and the ALB will be configured to use it. All HTTP requests will be redirected to HTTPS. |

## Feature Flags

These map-type variables control optional features:

### Dns

If Enable is true, a Route 53 record will be created for the ALB. If EnableHttps is true, a certificate will be configured for the domain and the ALB will be configured to use it. All HTTP requests will be redirected to HTTPS.


**Default configuration:**
```yaml

Dns:
  Enable: true
  EnableHttps: true

```


## Example Configuration

From `package-config-default.yml`:


```yaml

StackName: load-balancing-alb
load-balancing-alb-data.StackName: load-balancing-alb-data
Internal: true
Name: main
Dns:
  Enable: true
  EnableHttps: true

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`
- `__gp_dependencies.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_alb.tf`
- `_gp_alb_certificate.tf`
- `_gp_alb_route53_dns_record.tf`
- `_gp_alb_security_group.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Helper Scripts

- `bin/_gp_load-balancing-alb-remove-deletion-protection.sh`

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

## [4.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/load-balancing-alb-v3.7.1...load-balancing-alb-v4.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))


### Dependency updates

* update dependency load-balancing-alb-data to v3 ([#1458](https://github.com/oslokommune/golden-path-boilerplate/issues/1458)) ([280fffb](https://github.com/oslokommune/golden-path-boilerplate/commit/280fffbc2a9eaf75d16f1342523acd3be6470108))
* update dependency versions to v5 ([#1454](https://github.com/oslokommune/golden-path-boilerplate/issues/1454)) ([01fb21e](https://github.com/oslokommune/golden-path-boilerplate/commit/01fb21e7c1891dbf57451fbdd248bb59a79304e9))

## [3.7.1](https://github.com/oslokommune/golden-path-boilerplate/compare/load-balancing-alb-v3.7.0...load-balancing-alb-v3.7.1) (2025-07-29)


### Dependency updates

* update dependency load-balancing-alb-data to v2.6.3 ([#1386](https://github.com/oslokommune/golden-path-boilerplate/issues/1386)) ([87abe27](https://github.com/oslokommune/golden-path-boilerplate/commit/87abe27627d6c883c911e0b23571c717e33fd9f9))

## [3.7.0](https://github.com/oslokommune/golden-path-boilerplate/compare/load-balancing-alb-v3.6.2...load-balancing-alb-v3.7.0) (2025-07-26)


### Features

* Move var files for lock file generation to template dir ([#1346](https://github.com/oslokommune/golden-path-boilerplate/issues/1346)) ([d0a4b02](https://github.com/oslokommune/golden-path-boilerplate/commit/d0a4b02653613a92e8fcd582d14a2f3c911c17b0))


### Bug fixes

* Add IncludeLockFile to all Terraform boilerplate templates ([#1347](https://github.com/oslokommune/golden-path-boilerplate/issues/1347)) ([1a77fab](https://github.com/oslokommune/golden-path-boilerplate/commit/1a77fab696c5ad2523abbdc22a85b57f46399d3e))
* Remove error in case template lockfile is missing ([#1358](https://github.com/oslokommune/golden-path-boilerplate/issues/1358)) ([22debb6](https://github.com/oslokommune/golden-path-boilerplate/commit/22debb6595935feccca61e7afb1f72c51d102514))


### Dependency updates

* update dependency load-balancing-alb-data to v2.6.2 ([#1373](https://github.com/oslokommune/golden-path-boilerplate/issues/1373)) ([d03fb68](https://github.com/oslokommune/golden-path-boilerplate/commit/d03fb6820695be2056bb8595fcf8d66f542a76d9))
* update dependency versions to v3.4.0 ([#1367](https://github.com/oslokommune/golden-path-boilerplate/issues/1367)) ([16f6283](https://github.com/oslokommune/golden-path-boilerplate/commit/16f628302d18f079b62f3c66d8adb6ae30b569c2))
* Update Terraform dependency lock files ([#1308](https://github.com/oslokommune/golden-path-boilerplate/issues/1308)) ([1f49902](https://github.com/oslokommune/golden-path-boilerplate/commit/1f49902150a5431d0d9815aaafad8b8858940e9c))

## [3.6.2](https://github.com/oslokommune/golden-path-boilerplate/compare/load-balancing-alb-v3.6.1...load-balancing-alb-v3.6.2) (2025-06-26)


### Dependency updates

* update dependency load-balancing-alb-data to v2.6.1 ([#1259](https://github.com/oslokommune/golden-path-boilerplate/issues/1259)) ([aa2de35](https://github.com/oslokommune/golden-path-boilerplate/commit/aa2de352db5dd0b000eb01083e4fcf0e2c5a6bac))

## [3.6.1](https://github.com/oslokommune/golden-path-boilerplate/compare/load-balancing-alb-v3.6.0...load-balancing-alb-v3.6.1) (2025-06-25)


### Dependency updates

* update dependency load-balancing-alb-data to v2.5.0 ([#1216](https://github.com/oslokommune/golden-path-boilerplate/issues/1216)) ([f356bde](https://github.com/oslokommune/golden-path-boilerplate/commit/f356bde2128ab629578d2d97a86ab15b59e43d25))
* update dependency load-balancing-alb-data to v2.5.1 ([#1249](https://github.com/oslokommune/golden-path-boilerplate/issues/1249)) ([417bbee](https://github.com/oslokommune/golden-path-boilerplate/commit/417bbee76be8bef34a9e62b0e2bd02d7e6085d54))
* update dependency versions to v3.3.0 ([#1224](https://github.com/oslokommune/golden-path-boilerplate/issues/1224)) ([d2581ac](https://github.com/oslokommune/golden-path-boilerplate/commit/d2581ace71ccaf2ff7f677e22d0cac4cec3c2b34))
* Update Terraform dependency lock files ([#1206](https://github.com/oslokommune/golden-path-boilerplate/issues/1206)) ([b94e3c6](https://github.com/oslokommune/golden-path-boilerplate/commit/b94e3c601c31dcb7d37f2948631acbbb387ff32d))
