# Template: versions

## Metadata

- **Version**: `5.0.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/versions`
- **Last Commit**: `6ed18a67` - docs: Update Boilerplate template docs (#1634) (2025-11-05)
- **Last Generated**: 2025-11-07

## Purpose

|        Name        |                                      Description                                      |  Type  |           Default            |Required|
|--------------------|---------------------------------------------------------------------------------------|--------|------------------------------|--------|
|`IncludeLockFile`   |Include a Terraform lock file.                                                         |`bool`  |``false``                     |no      |
|`StackName`         |Name of Terraform stack.                                                               |``      |``n/a``                       |yes     |
|`AccountId`         |AWS account ID.                                                                        |``      |``n/a``                       |yes     |

## Variables

### Required Variables

| Name | Type | Description |
|------|------|-------------|
| `StackName` | `string` | Name of Terraform stack. |
| `AccountId` | `string` | AWS account ID. |
| `Team` | `string` | Team name. |
| `Environment` | `string` | Environment name. |

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `Region` | `string` | `eu-west-1` | AWS region. |
| `TerraformVersion` | `string` | `>= 1.10.0` | The version of Terraform to use. |
| `AwsProviderVersion` | `string` | `>= 6.0.0, < 7.0.0` | The version of the AWS provider to use |
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `S3Backend` | `bool` | true | Use S3 as a backend. |
| `IamForCicd` | `map` | `{AssumableCdRole: false}` | Enable IAM roles for CI/CD. |
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

StackName: versions
S3Backend: false

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_versions.tf`

### Other Files

- `.terraform.lock.hcl`
- `_gp_rm_gp_file.sh`
- `boilerplate.yml`

## Conditional File Generation

- Always skip: `package-config*.yml`
- Skip `.terraform.lock.hcl` if: `{{ not .IncludeLockFile }}`

## Recent Changes

## [5.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/versions-v4.0.0...versions-v5.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))

## [4.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/versions-v3.4.0...versions-v4.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* require aws provider v6 ([#1421](https://github.com/oslokommune/golden-path-boilerplate/issues/1421))

### Features

* require aws provider v6 ([#1421](https://github.com/oslokommune/golden-path-boilerplate/issues/1421)) ([1d5e35f](https://github.com/oslokommune/golden-path-boilerplate/commit/1d5e35fe5deb77868c0233f12c95bfd69152e32a))

## [3.4.0](https://github.com/oslokommune/golden-path-boilerplate/compare/versions-v3.3.0...versions-v3.4.0) (2025-07-25)


### Features

* Move var files for lock file generation to template dir ([#1346](https://github.com/oslokommune/golden-path-boilerplate/issues/1346)) ([d0a4b02](https://github.com/oslokommune/golden-path-boilerplate/commit/d0a4b02653613a92e8fcd582d14a2f3c911c17b0))


### Bug fixes

* Add IncludeLockFile to all Terraform boilerplate templates ([#1347](https://github.com/oslokommune/golden-path-boilerplate/issues/1347)) ([1a77fab](https://github.com/oslokommune/golden-path-boilerplate/commit/1a77fab696c5ad2523abbdc22a85b57f46399d3e))
* Skip README in versions template ([651bf4b](https://github.com/oslokommune/golden-path-boilerplate/commit/651bf4ba96aa587a35f821e9441ba9148a047475))


### Dependency updates

* Update Terraform dependency lock files ([#1308](https://github.com/oslokommune/golden-path-boilerplate/issues/1308)) ([1f49902](https://github.com/oslokommune/golden-path-boilerplate/commit/1f49902150a5431d0d9815aaafad8b8858940e9c))

## [3.3.0](https://github.com/oslokommune/golden-path-boilerplate/compare/versions-v3.2.4...versions-v3.3.0) (2025-06-24)


### Features

* Trigger release of [#1203](https://github.com/oslokommune/golden-path-boilerplate/issues/1203) ([12a7fb8](https://github.com/oslokommune/golden-path-boilerplate/commit/12a7fb84437430557fdfa802f76dacc86cac00d3))

## [3.2.4](https://github.com/oslokommune/golden-path-boilerplate/compare/versions-v3.2.3...versions-v3.2.4) (2025-06-23)


### Bug fixes

* Set aws provider to v5 ([#1203](https://github.com/oslokommune/golden-path-boilerplate/issues/1203)) ([31496cf](https://github.com/oslokommune/golden-path-boilerplate/commit/31496cfabe1d4e0b54246e33f9de75ac4790a6f5))
