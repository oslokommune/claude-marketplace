# Template: cloudfront-deploy

## Metadata

- **Version**: `0.4.2`
- **Type**: `github-actions`
- **Template Path**: `boilerplate/github-actions/cloudfront-deploy`
- **Last Commit**: `e650d0d1` - deps: update dependency actions/checkout to v5 (#1504) (2025-08-19)
- **Last Generated**: 2025-11-07

## Purpose

GitHub Actions workflow template for deploying static sites to S3 and CloudFront.

## Variables

### Required Variables

| Name | Type | Description |
|------|------|-------------|
| `Name` | `string` | Application/service name |
| `Environment` | `string` | Environment |

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `DockerfilePath` | `string` | `Dockerfile` | Path to Dockerfile |
| `DockerContext` | `string` | `.` | Docker build context |
| `ContainerSitePath` | `string` | `/app/site` | Path inside container where built site files are located |
| `LocalSitePath` | `string` | `./site` | Local path to extract site files to |

## Example Configuration

From `package-config-default.yml`:


```yaml

Name: my-app
DockerfilePath: ./my-app/Dockerfile
ContainerSitePath: /app/mkdocs/site/.
DockerContext: ./my-app

```

## Generated Files

### Other Files

- `_gp_{{ .Name }}_{{ .Environment }}_cloudfront_deploy.yml`
- `boilerplate.yml`

## Conditional File Generation

- Always skip: `package-config*.yml`

## Recent Changes

## [0.4.2](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-deploy-v0.4.1...cloudfront-deploy-v0.4.2) (2025-08-18)


### Bug fixes

* Avoid including `package-config-default.yml` ([#1492](https://github.com/oslokommune/golden-path-boilerplate/issues/1492)) ([a3905c8](https://github.com/oslokommune/golden-path-boilerplate/commit/a3905c84c36695f7fdfa463bccf9022ae514dcb7))

## [0.4.1](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-deploy-v0.4.0...cloudfront-deploy-v0.4.1) (2025-08-13)


### Bug fixes

* improvements to cloudfront-static-website ([236593a](https://github.com/oslokommune/golden-path-boilerplate/commit/236593af66851d979d264c3649e2587eeb2c8db0))

## [0.4.0](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-deploy-v0.3.0...cloudfront-deploy-v0.4.0) (2025-07-30)


### Features

* Add github action template var files ([#1394](https://github.com/oslokommune/golden-path-boilerplate/issues/1394)) ([abf49e3](https://github.com/oslokommune/golden-path-boilerplate/commit/abf49e37ee1ab4511315a020b9f4248b8bd15f56))

## [0.3.0](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-deploy-v0.2.0...cloudfront-deploy-v0.3.0) (2025-07-24)


### Features

* Add URL to environment ([d7e48e9](https://github.com/oslokommune/golden-path-boilerplate/commit/d7e48e9e2424d03a13d6e10773c829cc3b02f87b))


### Bug fixes

* Enclose variables in quotes ([18ea801](https://github.com/oslokommune/golden-path-boilerplate/commit/18ea80106719484a3054bf8843163c3f736b2617))

## [0.2.0](https://github.com/oslokommune/golden-path-boilerplate/compare/cloudfront-deploy-v0.1.0...cloudfront-deploy-v0.2.0) (2025-07-23)


### Features

* Add CloudFront deployment workflow ([1108226](https://github.com/oslokommune/golden-path-boilerplate/commit/1108226ddbe18bba3b1115379604c40785148401))
