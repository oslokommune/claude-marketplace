# Template: backup

## Metadata

- **Version**: `4.1.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/backup`
- **Last Commit**: `a729a1ca` - chore(main): release backup 4.1.0 (#1526) (2025-11-05)
- **Last Generated**: 2025-11-07

## Purpose

|         Name         |                 Description                  | Type |       Default       |Required|
|----------------------|----------------------------------------------|------|---------------------|--------|
|`NotifySlack`         |Notify slack channel when a backup is created.|`map` |``{"Enable": false}``|no      |
|`IncludeLockFile`     |Include a Terraform lock file.                |`bool`|``false``            |no      |
|`UseTagSelection`     |Use tag selection for backup.                 |`bool`|``true``             |no      |

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)

## Variables

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `NotifySlack` | `map` | `{Enable: false}` | Notify slack channel when a backup is created. |
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `UseTagSelection` | `bool` | true | Use tag selection for backup. |
| `UseResourceSelection` | `bool` | false | Use resources selection for backup. |

## Feature Flags

These map-type variables control optional features:

### NotifySlack

Notify slack channel when a backup is created.


**Default configuration:**
```yaml

NotifySlack:
  Enable: false

```


## Example Configuration

From `package-config-default.yml`:


```yaml

StackName: backup
NotifySlack:
  Enable: false

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_backup.tf`
- `_gp_backup_iam.tf`
- `_gp_backup_slack.tf`
- `_gp_backup_sns.tf`
- `_gp_module_migration.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Helper Scripts

- `bin/_gp_backup-remove-recovery-points.sh`

### Other Files

- `.terraform.lock.hcl`
- `_gp_rm_gp_file.sh`
- `boilerplate.yml`
- `terragrunt.hcl`
- `terragrunt_custom.hcl`

## Conditional File Generation

- Always skip: `package-config*.yml`
- Skip `config_override.tf` if: `{{ list outputFolder "config_override.tf" | join "/" | pathExists }}`
- Skip `.terraform.lock.hcl*` if: `{{ not .IncludeLockFile }}`
- Skip `terragrunt_custom.hcl` if: `{{ list outputFolder "terragrunt_custom.hcl" | join "/" | pathExists }}`

## Recent Changes

## [4.1.0](https://github.com/oslokommune/golden-path-boilerplate/compare/backup-v4.0.0...backup-v4.1.0) (2025-11-05)


### Features

* add terragrunt setup for all stacks needed. add bin scripts to delete necessary resources ([#1622](https://github.com/oslokommune/golden-path-boilerplate/issues/1622)) ([371eb5a](https://github.com/oslokommune/golden-path-boilerplate/commit/371eb5a432977d23662c945b6e5f40e1806350c7))
* Use sane default setup in var files ([#1482](https://github.com/oslokommune/golden-path-boilerplate/issues/1482)) ([730a63b](https://github.com/oslokommune/golden-path-boilerplate/commit/730a63b9ca8c31ea1e4580d2585f2ecb358b9fa2))


### Bug fixes

* exclude datadog forwarder from AWS Backup ([#1625](https://github.com/oslokommune/golden-path-boilerplate/issues/1625)) ([d6c1d61](https://github.com/oslokommune/golden-path-boilerplate/commit/d6c1d61bd1509e2502cc407309b31c7e32c9a277))


### Dependency updates

* Update Terraform dependency lock files ([#1402](https://github.com/oslokommune/golden-path-boilerplate/issues/1402)) ([0ca8c1c](https://github.com/oslokommune/golden-path-boilerplate/commit/0ca8c1c8ee2b0e25a6fd7e19685d15e9524aeacc))

## [4.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/backup-v3.8.0...backup-v4.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))


### Dependency updates

* update dependency versions to v5 ([#1454](https://github.com/oslokommune/golden-path-boilerplate/issues/1454)) ([01fb21e](https://github.com/oslokommune/golden-path-boilerplate/commit/01fb21e7c1891dbf57451fbdd248bb59a79304e9))

## [3.8.0](https://github.com/oslokommune/golden-path-boilerplate/compare/backup-v3.7.1...backup-v3.8.0) (2025-07-26)


### Features

* Move var files for lock file generation to template dir ([#1346](https://github.com/oslokommune/golden-path-boilerplate/issues/1346)) ([d0a4b02](https://github.com/oslokommune/golden-path-boilerplate/commit/d0a4b02653613a92e8fcd582d14a2f3c911c17b0))


### Bug fixes

* Remove error in case template lockfile is missing ([#1358](https://github.com/oslokommune/golden-path-boilerplate/issues/1358)) ([22debb6](https://github.com/oslokommune/golden-path-boilerplate/commit/22debb6595935feccca61e7afb1f72c51d102514))


### Dependency updates

* update dependency versions to v3.4.0 ([#1367](https://github.com/oslokommune/golden-path-boilerplate/issues/1367)) ([16f6283](https://github.com/oslokommune/golden-path-boilerplate/commit/16f628302d18f079b62f3c66d8adb6ae30b569c2))
* Update Terraform dependency lock files ([#1308](https://github.com/oslokommune/golden-path-boilerplate/issues/1308)) ([1f49902](https://github.com/oslokommune/golden-path-boilerplate/commit/1f49902150a5431d0d9815aaafad8b8858940e9c))

## [3.7.1](https://github.com/oslokommune/golden-path-boilerplate/compare/backup-v3.7.0...backup-v3.7.1) (2025-06-25)


### Dependency updates

* update dependency versions to v3.3.0 ([#1224](https://github.com/oslokommune/golden-path-boilerplate/issues/1224)) ([d2581ac](https://github.com/oslokommune/golden-path-boilerplate/commit/d2581ace71ccaf2ff7f677e22d0cac4cec3c2b34))
* Update Terraform dependency lock files ([#1206](https://github.com/oslokommune/golden-path-boilerplate/issues/1206)) ([b94e3c6](https://github.com/oslokommune/golden-path-boilerplate/commit/b94e3c601c31dcb7d37f2948631acbbb387ff32d))

## [3.7.0](https://github.com/oslokommune/golden-path-boilerplate/compare/backup-v3.6.4...backup-v3.7.0) (2025-06-19)


### Features

* Support directories as dependencies in template ([c388500](https://github.com/oslokommune/golden-path-boilerplate/commit/c388500ed611e3a11490de8be33177081e9208d5))


### Bug fixes

* Delete files from Golden path only ([#1162](https://github.com/oslokommune/golden-path-boilerplate/issues/1162)) ([bd43212](https://github.com/oslokommune/golden-path-boilerplate/commit/bd43212378defcb9437e54e2ccfb52b0502e1ff0))
* Remove sh files with delete-marker ([#1171](https://github.com/oslokommune/golden-path-boilerplate/issues/1171)) ([2ac3158](https://github.com/oslokommune/golden-path-boilerplate/commit/2ac31581acda734fec295a462d05e8b6f48f332b))


### Dependency updates

* Update Terraform dependency lock files ([#1149](https://github.com/oslokommune/golden-path-boilerplate/issues/1149)) ([7c500b3](https://github.com/oslokommune/golden-path-boilerplate/commit/7c500b3f870df325e5744ba29d3fb43798e1c882))
