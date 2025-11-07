# Template: eventbridge-notifications

## Metadata

- **Version**: `0.0.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/eventbridge-notifications`
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
- `__gp_eventbridge_rules.tf`
- `__gp_lambda.tf`
- `__gp_lambda_iam.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Other Files

- `boilerplate.yml`
- `terragrunt.hcl`
- `terragrunt_custom.hcl`

## Conditional File Generation

- Always skip: `package-config*.yml`
- Skip `.terraform.lock.hcl*` if: `{{ not .IncludeLockFile }}`
- Skip `config_override.tf` if: `{{ list outputFolder "config_override.tf" | join "/" | pathExists }}`
- Skip `terragrunt_custom.hcl` if: `{{ list outputFolder "terragrunt_custom.hcl" | join "/" | pathExists }}`
