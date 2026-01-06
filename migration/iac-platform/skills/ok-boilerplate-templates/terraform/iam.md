# Template: iam

## Metadata

- **Version**: `3.0.1`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/iam`
- **Last Commit**: `6ed18a67` - docs: Update Boilerplate template docs (#1634) (2025-11-05)
- **Last Generated**: 2025-11-07

## Purpose

|          Name           |                                                     Description                                                     | Type |                  Default                   |Required|
|-------------------------|---------------------------------------------------------------------------------------------------------------------|------|--------------------------------------------|--------|
|`IncludeLockFile`        |Include a Terraform lock file.                                                                                       |`bool`|``false``                                   |no      |
|`MaskinportenKeyRotation`|Enable Maskinporten key rotation.                                                                                    |`map` |``{"Enable": false}``                       |no      |
|`GithubIdentityProvider` |Add GitHub as an identity provider (OIDC).                                                                           |`map` |``{"Enable": false}``                       |no      |

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)

## Variables

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `MaskinportenKeyRotation` | `map` | `{Enable: false}` | Enable Maskinporten key rotation. |
| `GithubIdentityProvider` | `map` | `{Enable: false}` | Add GitHub as an identity provider (OIDC). |
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `IamForEnvironmentCicd` | `map` | `{Enable: false, IacGitHubRepo: null}` | Enable IAM roles for CI/CD for the environment.  This is a experimental feature and should not be used in production. |

## Feature Flags

These map-type variables control optional features:

### MaskinportenKeyRotation

Enable Maskinporten key rotation.


**Default configuration:**
```yaml

MaskinportenKeyRotation:
  Enable: false

```


### GithubIdentityProvider

Add GitHub as an identity provider (OIDC).


**Default configuration:**
```yaml

GithubIdentityProvider:
  Enable: false

```


### IamForEnvironmentCicd

Enable IAM roles for CI/CD for the environment.

This is a experimental feature and should not be used in production.


**Default configuration:**
```yaml

IamForEnvironmentCicd:
  Enable: false
  IacGitHubRepo: null

```


## Example Configuration

From `package-config-default.yml`:


```yaml

StackName: iam
GithubIdentityProvider:
  Enable: true
MaskinportenKeyRotation:
  Enable: true

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_iam_cicd_policies.tf`
- `_gp_iam_cicd_roles.tf`
- `_gp_iam_github_identity_provider.tf`
- `_gp_iam_maskinporten_key_rotation.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Helper Scripts

- `bin/_gp_set_role_secret_in_iac_repo.sh`

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
- Skip `.terraform.lock.hcl*` if: `{{ not .IncludeLockFile }}`
- Skip `terragrunt_custom.hcl` if: `{{ list outputFolder "terragrunt_custom.hcl" | join "/" | pathExists }}`

## Recent Changes

## [3.0.1](https://github.com/oslokommune/golden-path-boilerplate/compare/iam-v3.0.0...iam-v3.0.1) (2025-10-03)


### Bug fixes

* ensure custom trust policy is created by default ([#1605](https://github.com/oslokommune/golden-path-boilerplate/issues/1605)) ([36f1403](https://github.com/oslokommune/golden-path-boilerplate/commit/36f1403436903a8108cf0edb4c5e491e44cc2b32))


### Dependency updates

* Update Terraform dependency lock files ([#1402](https://github.com/oslokommune/golden-path-boilerplate/issues/1402)) ([0ca8c1c](https://github.com/oslokommune/golden-path-boilerplate/commit/0ca8c1c8ee2b0e25a6fd7e19685d15e9524aeacc))

## [3.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/iam-v2.10.0...iam-v3.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))


### Dependency updates

* update dependency versions to v5 ([#1454](https://github.com/oslokommune/golden-path-boilerplate/issues/1454)) ([01fb21e](https://github.com/oslokommune/golden-path-boilerplate/commit/01fb21e7c1891dbf57451fbdd248bb59a79304e9))

## [2.10.0](https://github.com/oslokommune/golden-path-boilerplate/compare/iam-v2.9.2...iam-v2.10.0) (2025-07-26)


### Features

* Move var files for lock file generation to template dir ([#1346](https://github.com/oslokommune/golden-path-boilerplate/issues/1346)) ([d0a4b02](https://github.com/oslokommune/golden-path-boilerplate/commit/d0a4b02653613a92e8fcd582d14a2f3c911c17b0))


### Bug fixes

* Add IncludeLockFile to all Terraform boilerplate templates ([#1347](https://github.com/oslokommune/golden-path-boilerplate/issues/1347)) ([1a77fab](https://github.com/oslokommune/golden-path-boilerplate/commit/1a77fab696c5ad2523abbdc22a85b57f46399d3e))
* Remove error in case template lockfile is missing ([#1358](https://github.com/oslokommune/golden-path-boilerplate/issues/1358)) ([22debb6](https://github.com/oslokommune/golden-path-boilerplate/commit/22debb6595935feccca61e7afb1f72c51d102514))


### Dependency updates

* update dependency versions to v3.4.0 ([#1367](https://github.com/oslokommune/golden-path-boilerplate/issues/1367)) ([16f6283](https://github.com/oslokommune/golden-path-boilerplate/commit/16f628302d18f079b62f3c66d8adb6ae30b569c2))
* Update Terraform dependency lock files ([#1308](https://github.com/oslokommune/golden-path-boilerplate/issues/1308)) ([1f49902](https://github.com/oslokommune/golden-path-boilerplate/commit/1f49902150a5431d0d9815aaafad8b8858940e9c))

## [2.9.2](https://github.com/oslokommune/golden-path-boilerplate/compare/iam-v2.9.1...iam-v2.9.2) (2025-06-25)


### Dependency updates

* update dependency versions to v3.3.0 ([#1224](https://github.com/oslokommune/golden-path-boilerplate/issues/1224)) ([d2581ac](https://github.com/oslokommune/golden-path-boilerplate/commit/d2581ace71ccaf2ff7f677e22d0cac4cec3c2b34))
* Update Terraform dependency lock files ([#1206](https://github.com/oslokommune/golden-path-boilerplate/issues/1206)) ([b94e3c6](https://github.com/oslokommune/golden-path-boilerplate/commit/b94e3c601c31dcb7d37f2948631acbbb387ff32d))

## [2.9.1](https://github.com/oslokommune/golden-path-boilerplate/compare/iam-v2.9.0...iam-v2.9.1) (2025-06-19)


### Bug fixes

* Delete files from Golden path only ([#1162](https://github.com/oslokommune/golden-path-boilerplate/issues/1162)) ([bd43212](https://github.com/oslokommune/golden-path-boilerplate/commit/bd43212378defcb9437e54e2ccfb52b0502e1ff0))
* Remove sh files with delete-marker ([#1171](https://github.com/oslokommune/golden-path-boilerplate/issues/1171)) ([2ac3158](https://github.com/oslokommune/golden-path-boilerplate/commit/2ac31581acda734fec295a462d05e8b6f48f332b))


### Dependency updates

* Update Terraform dependency lock files ([#1149](https://github.com/oslokommune/golden-path-boilerplate/issues/1149)) ([7c500b3](https://github.com/oslokommune/golden-path-boilerplate/commit/7c500b3f870df325e5744ba29d3fb43798e1c882))
