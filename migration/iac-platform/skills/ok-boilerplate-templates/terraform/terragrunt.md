# Template: terragrunt

## Metadata

- **Version**: `3.2.1`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/terragrunt`
- **Last Commit**: `8dd6645e` - docs: Update Boilerplate template docs (#1455) (2025-08-06)
- **Last Generated**: 2025-11-07

## Purpose

|           Name           |                                                 Description                                                  | Type |                   Default                    |Required|
|--------------------------|--------------------------------------------------------------------------------------------------------------|------|----------------------------------------------|--------|
|`Terragrunt`              |Enable Terragrunt. This is a experimental feature and should not be used in production.                       |`map` |``{"Enable": false, "DependenciesPaths": []}``|no      |
|`DefaultDependenciesPaths`|Default dependecies paths for terragrunt. This is a experimental feature and should not be used in production.|`list`|``[]``                                        |no      |
<!-- BOILERPLATE END -->

## Variables

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `Terragrunt` | `map` | `{DependenciesPaths: [], Enable: false}` | Enable Terragrunt. This is a experimental feature and should not be used in production. |
| `DefaultDependenciesPaths` | `list` | `[]` | Default dependecies paths for terragrunt. This is a experimental feature and should not be used in production. |

## Feature Flags

These map-type variables control optional features:

### Terragrunt

Enable Terragrunt.
This is a experimental feature and should not be used in production.


**Default configuration:**
```yaml

Terragrunt:
  DependenciesPaths: []
  Enable: false

```


## Generated Files

### Other Files

- `boilerplate.yml`
- `terragrunt.hcl`
- `terragrunt_custom.hcl`

## Conditional File Generation

- Skip `terragrunt_custom.hcl` if: `{{ list outputFolder "terragrunt_custom.hcl" | join "/" | pathExists }}`
