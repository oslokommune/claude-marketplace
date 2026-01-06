# Template: cloudfront-static-website

## Metadata

- **Version**: `1.3.0`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/cloudfront-static-website`
- **Last Commit**: `29841ff4` - chore(deps): update dependency terraform-aws-modules/cloudfront/aws to v5.0.1 (#1619) (2025-11-05)
- **Last Generated**: 2025-11-07

## Purpose

Creates a static website hosted on S3 with CloudFront distribution, SSL certificate, and custom domain.
> [!NOTE]
> This stack might take a **long time** to both **apply** and **destroy** due to the CloudFront distribution. Deployment typically takes around 5 minutes, while destruction can take 5-6 minutes.
> [!NOTE]
> This template has a dependency on the [CloudFront data template](../cloudfront-static-website-data/) which creates the S3 buckets used for content and logging.

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)
- **cloudfront-static-website-data** (version: `main`)

## Variables

### Required Variables

| Name | Type | Description |
|------|------|-------------|
| `Name` | `string` | Name for the CloudFront static website resources |

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `RedirectAllToIndex` | `bool` | false | Make the Cloudfront distribution compatible with client-side routing (e.g., React Router), forwarding all requests to index.html |
| `RootObject` | `string` | `index.html` | Default object to serve for directory requests |
| `ErrorObject` | `string` | `404.html` | Default error page object |
| `AppendIndexToDirectories` | `bool` | false | Append index.html to directory URLs |
| `IamForCicd` | `map` | `{Enable: false, GitHubRepo: null}` | Enable IAM roles for CI/CD. |

## Feature Flags

These map-type variables control optional features:

### IamForCicd

Enable IAM roles for CI/CD.


**Default configuration:**
```yaml

IamForCicd:
  Enable: false
  GitHubRepo: null

```


## Example Configuration

From `package-config-default.yml`:


```yaml

StackName: some-site
cloudfront-static-website-data.StackName: some-site-data
Name: some-site
RedirectAllToIndex: false
RootObject: index.html
ErrorObject: 404.html
AppendIndexToDirectories: false
IamForCicd:
  Enable: true
  GitHubRepo: some-site

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`
- `__gp_dependencies.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_cloudfront.tf`
- `_gp_dns.tf`
- `_gp_iam.tf`
- `_gp_providers.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Helper Scripts

- `bin/set_github_secrets.sh`

### Other Files

- `boilerplate.yml`
- `terragrunt.hcl`
- `terragrunt_custom.hcl`

## Conditional File Generation

- Always skip: `package-config*.yml`
- Skip `.terraform.lock.hcl*` if: `{{ not .IncludeLockFile }}`
- Skip `config_override.tf` if: `{{ list outputFolder "config_override.tf" | join "/" | pathExists }}`
- Skip `terragrunt_custom.hcl` if: `{{ list outputFolder "terragrunt_custom.hcl" | join "/" | pathExists }}`

## Recent Changes

## [1.3.0](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-static-website-v1.2.0...cloudfront-static-website-v1.3.0) (2025-08-25)


### Features

* Add flexible domain configuration ([85726a0](https://github.com/oslokommune/golden-path-boilerplate/commit/85726a0f560b5b998841a474b2aea593493f3a28))

## [1.2.0](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-static-website-v1.1.0...cloudfront-static-website-v1.2.0) (2025-08-19)


### Features

* Move object locals out of user facing config ([#1519](https://github.com/oslokommune/golden-path-boilerplate/issues/1519)) ([0360a3b](https://github.com/oslokommune/golden-path-boilerplate/commit/0360a3b2ed6dbffa58514e4bb898eda94bdf0363))
* simplify CloudFront static website variables ([11f7324](https://github.com/oslokommune/golden-path-boilerplate/commit/11f7324e29ee319f9c55b237a7600f0531b8073c))

## [1.1.0](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-static-website-v1.0.1...cloudfront-static-website-v1.1.0) (2025-08-15)


### Features

* Make secrets script display colors correctly on all platforms ([#1507](https://github.com/oslokommune/golden-path-boilerplate/issues/1507)) ([0acec71](https://github.com/oslokommune/golden-path-boilerplate/commit/0acec71e06ef68ffd3f4ea12d7de0db2950e7689))

## [1.0.1](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-static-website-v1.0.0...cloudfront-static-website-v1.0.1) (2025-08-13)


### Bug fixes

* improvements to cloudfront-static-website ([236593a](https://github.com/oslokommune/golden-path-boilerplate/commit/236593af66851d979d264c3649e2587eeb2c8db0))

## [1.0.0](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-static-website-v0.4.1...cloudfront-static-website-v1.0.0) (2025-08-06)


### ⚠ BREAKING CHANGES

* update templates for aws provider v6

### Features

* update templates for aws provider v6 ([ce3e28d](https://github.com/oslokommune/golden-path-boilerplate/commit/ce3e28d394e885a1a24e6cf915683e41732f52a1))


### Dependency updates

* update dependency versions to v5 ([#1454](https://github.com/oslokommune/golden-path-boilerplate/issues/1454)) ([01fb21e](https://github.com/oslokommune/golden-path-boilerplate/commit/01fb21e7c1891dbf57451fbdd248bb59a79304e9))
