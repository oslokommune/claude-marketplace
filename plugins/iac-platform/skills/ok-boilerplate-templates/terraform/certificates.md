# Template: certificates

## Metadata

- **Version**: `2.0.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/certificates`
- **Last Commit**: `1dece0cc` - fix: remove terragrunt after-hook that was not supposed to be there (#1636) (2025-11-05)
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

## Example Configuration

From `package-config-default.yml`:


```yaml

StackName: certificates

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`
- `__gp_dependencies.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_alb_certificate.tf`

### User Override Files

- `config_override.tf` (user-customizable)

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

## [2.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/certificates-v1.2.1...certificates-v2.0.0) (2024-06-06)


### ⚠ BREAKING CHANGES

* New directory structure ([#154](https://github.com/oslokommune/golden-path-boilerplate/issues/154))

### Features

* New directory structure ([#154](https://github.com/oslokommune/golden-path-boilerplate/issues/154)) ([3e34dd1](https://github.com/oslokommune/golden-path-boilerplate/commit/3e34dd1e3e5e0e3e1bc35359412809ca16dc199d))

## [1.2.1](https://github.com/oslokommune/golden-path-boilerplate/compare/certificates-v1.2.0...certificates-v1.2.1) (2024-05-31)


### Bug fixes

* Indentation and wording in templates ([#151](https://github.com/oslokommune/golden-path-boilerplate/issues/151)) ([678c37c](https://github.com/oslokommune/golden-path-boilerplate/commit/678c37c7b92f4d6d6794a6d4de8b5c007d30f7dc))

## [1.2.0](https://github.com/oslokommune/golden-path-boilerplate/compare/certificates-v1.1.0...certificates-v1.2.0) (2024-05-31)


### Features

* add name to version file ([#147](https://github.com/oslokommune/golden-path-boilerplate/issues/147)) ([0ceb454](https://github.com/oslokommune/golden-path-boilerplate/commit/0ceb454ede5dff40aa0acf8495d966dc93be219a))

## [1.1.0](https://github.com/oslokommune/golden-path-boilerplate/compare/certificates-v1.0.0...certificates-v1.1.0) (2024-05-30)


### Features

* Move certificate to new pattern ([#131](https://github.com/oslokommune/golden-path-boilerplate/issues/131)) ([355b385](https://github.com/oslokommune/golden-path-boilerplate/commit/355b3859d865e8570b73fbe188aa9a0b37793cc0))

## 1.0.0 (2024-05-21)


### Features

* Use release-please for all boilerplate templates ([#89](https://github.com/oslokommune/golden-path-boilerplate/issues/89)) ([e380d58](https://github.com/oslokommune/golden-path-boilerplate/commit/e380d58c9a0273bfb4667c6228555784a4e3c6ad))
