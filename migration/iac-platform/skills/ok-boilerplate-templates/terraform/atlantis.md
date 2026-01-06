# Template: atlantis

## Metadata

- **Version**: `1.17.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/atlantis`
- **Last Commit**: `40a4ea97` - chore(main): release atlantis 1.17.0 (#1523) (2025-11-05)
- **Last Generated**: 2025-11-07

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)

## Variables

### Required Variables

| Name | Type | Description |
|------|------|-------------|
| `Environment` | `string` | Environment name (e.g., dev, test, prod) |
| `GitHubOrg` | `string` | GitHub organization name |
| `GitHubRepo` | `string` | GitHub repository name |

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `AwsProviderVersion` | `string` | `>= 5.70.0, < 6.0.0` | The version of the AWS provider to use |
| `FirstTimeSetup` | `map` | `{Enable: true}` | Enable first-time setup for Atlantis |
| `SlackAlerts` | `map` | `{ChannelName: cats, Enable: true}` | Configure Slack alerts for Atlantis |
| `BasicAuth` | `map` | `{Enable: true}` | Configure basic authentication on the Atlantis web server. Consider setting up Cognito authentication on the ALB instead. |
| `AlbHostRouting` | `map` | `{CognitoAuthentication: false, Enable: false}` | Add ALB host routing. See: - https://github.com/oslokommune/golden-path-iac/tree/main/terraform/modules/alb-tg-host-routing |
| `TerragruntAtlantisConfig` | `map` | `{Enable: true}` | Options for the Terragrunt Atlantis Config integration. Use this to automatically generate repo level config for Atlantis, based on Terragrunt dependencies. If this is disabled, you must create the Atlantis repo level config some other way. - See: https://github.com/transcend-io/terragrunt-atlantis-config |

## Feature Flags

These map-type variables control optional features:

### FirstTimeSetup

Enable first-time setup for Atlantis


**Default configuration:**
```yaml

FirstTimeSetup:
  Enable: true

```


### SlackAlerts

Configure Slack alerts for Atlantis


**Default configuration:**
```yaml

SlackAlerts:
  ChannelName: cats
  Enable: true

```


### BasicAuth

Configure basic authentication on the Atlantis web server. Consider setting up Cognito authentication on the ALB instead.


**Default configuration:**
```yaml

BasicAuth:
  Enable: true

```


### AlbHostRouting

Add ALB host routing. See:
- https://github.com/oslokommune/golden-path-iac/tree/main/terraform/modules/alb-tg-host-routing


**Default configuration:**
```yaml

AlbHostRouting:
  CognitoAuthentication: false
  Enable: false

```


### TerragruntAtlantisConfig

Options for the Terragrunt Atlantis Config integration. Use this to automatically generate repo level config for
Atlantis, based on Terragrunt dependencies.
If this is disabled, you must create the Atlantis repo level config some other way.
-
See: https://github.com/transcend-io/terragrunt-atlantis-config


**Default configuration:**
```yaml

TerragruntAtlantisConfig:
  Enable: true

```


## Example Configuration

From `package-config-default.yml`:


```yaml

StackName: atlantis
GitHubOrg: oslokommune
GitHubRepo: pirates-iac
FirstTimeSetup:
  Enable: false
SlackAlerts:
  Enable: true
  ChannelName: cats
BasicAuth:
  Enable: true
AlbHostRouting:
  Enable: true
  CognitoAuthentication: true
TerragruntAtlantisConfig:
  Enable: true

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`
- `__gp_dependencies.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_alb.tf`
- `_gp_atlantis.tf`
- `_gp_atlantis_server_config.tf`
- `_gp_cd_policy.tf`
- `_gp_cloudwatch_query.tf`
- `_gp_cognito.tf`
- `_gp_security_groups.tf`
- `_gp_ssm.tf`
- `_gp_waf.tf`
- `_gp_waf_top_insights.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Helper Scripts

- `bin/_gp_set_secret.sh`

### Other Files

- `.terraform.lock.hcl`
- `boilerplate.yml`
- `files/_gp_atlantis.yaml`

## Conditional File Generation

- Always skip: `package-config*.yml`
- Skip `.terraform.lock.hcl*` if: `{{ not .IncludeLockFile }}`
- Skip `config_override.tf` if: `{{ list outputFolder "config_override.tf" | join "/" | pathExists }}`

## Recent Changes

## [1.17.0](https://github.com/oslokommune/golden-path-boilerplate/compare/atlantis-v1.16.2...atlantis-v1.17.0) (2025-11-05)


### Features

* Use sane default setup in var files ([#1482](https://github.com/oslokommune/golden-path-boilerplate/issues/1482)) ([730a63b](https://github.com/oslokommune/golden-path-boilerplate/commit/730a63b9ca8c31ea1e4580d2585f2ecb358b9fa2))


### Dependency updates

* Update Terraform dependency lock files ([#1402](https://github.com/oslokommune/golden-path-boilerplate/issues/1402)) ([0ca8c1c](https://github.com/oslokommune/golden-path-boilerplate/commit/0ca8c1c8ee2b0e25a6fd7e19685d15e9524aeacc))

## [1.16.2](https://github.com/oslokommune/golden-path-boilerplate/compare/atlantis-v1.16.1...atlantis-v1.16.2) (2025-08-06)


### Bug fixes

* Remove removed variable service_name ([#1449](https://github.com/oslokommune/golden-path-boilerplate/issues/1449)) ([e0af8db](https://github.com/oslokommune/golden-path-boilerplate/commit/e0af8dbfe088915687e78ff9b5dce2a53f5d8720))


### Dependency updates

* update dependency versions to v5 ([#1454](https://github.com/oslokommune/golden-path-boilerplate/issues/1454)) ([01fb21e](https://github.com/oslokommune/golden-path-boilerplate/commit/01fb21e7c1891dbf57451fbdd248bb59a79304e9))

## [1.16.1](https://github.com/oslokommune/golden-path-boilerplate/compare/atlantis-v1.16.0...atlantis-v1.16.1) (2025-07-26)


### Dependency updates

* update dependency versions to v3.4.0 ([#1367](https://github.com/oslokommune/golden-path-boilerplate/issues/1367)) ([16f6283](https://github.com/oslokommune/golden-path-boilerplate/commit/16f628302d18f079b62f3c66d8adb6ae30b569c2))

## [1.16.0](https://github.com/oslokommune/golden-path-boilerplate/compare/atlantis-v1.15.2...atlantis-v1.16.0) (2025-07-25)


### Features

* Move var files for lock file generation to template dir ([#1346](https://github.com/oslokommune/golden-path-boilerplate/issues/1346)) ([d0a4b02](https://github.com/oslokommune/golden-path-boilerplate/commit/d0a4b02653613a92e8fcd582d14a2f3c911c17b0))


### Bug fixes

* Add IncludeLockFile to all Terraform boilerplate templates ([#1347](https://github.com/oslokommune/golden-path-boilerplate/issues/1347)) ([1a77fab](https://github.com/oslokommune/golden-path-boilerplate/commit/1a77fab696c5ad2523abbdc22a85b57f46399d3e))
* Remove error in case template lockfile is missing ([#1358](https://github.com/oslokommune/golden-path-boilerplate/issues/1358)) ([22debb6](https://github.com/oslokommune/golden-path-boilerplate/commit/22debb6595935feccca61e7afb1f72c51d102514))


### Dependency updates

* Update Terraform dependency lock files ([#1308](https://github.com/oslokommune/golden-path-boilerplate/issues/1308)) ([1f49902](https://github.com/oslokommune/golden-path-boilerplate/commit/1f49902150a5431d0d9815aaafad8b8858940e9c))

## [1.15.2](https://github.com/oslokommune/golden-path-boilerplate/compare/atlantis-v1.15.1...atlantis-v1.15.2) (2025-06-25)


### Dependency updates

* Update Terraform dependency lock files ([#1206](https://github.com/oslokommune/golden-path-boilerplate/issues/1206)) ([b94e3c6](https://github.com/oslokommune/golden-path-boilerplate/commit/b94e3c601c31dcb7d37f2948631acbbb387ff32d))
