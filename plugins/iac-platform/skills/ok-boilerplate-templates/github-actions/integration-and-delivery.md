# Template: integration-and-delivery

## Metadata

- **Version**: `0.15.1`
- **Type**: `github-actions`
- **Template Path**: `boilerplate/github-actions/integration-and-delivery`
- **Last Commit**: `86415a23` - chore(deps): update dependency peter-evans/repository-dispatch to v4 (#1606) (2025-11-06)
- **Last Generated**: 2025-11-07

## Purpose

|         Name         |                                    Description                                     |  Type  |                                                                                                                                         Default                                                                                                                                         |Required|
|----------------------|------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
|`AppName`             |Application name                                                                    |`string`|``n/a``                                                                                                                                                                                                                                                                                  |yes     |
|`FileNameLabel`       |Optional label to include in the workflow filename for generating multiple workflows|`string`|````                                                                                                                                                                                                                                                                                     |no      |
|`Cache`               |Cache configuration.                                                                |`map`   |``{"Enable": false}``                                                                                                                                                                                                                                                                    |no      |

## Variables

### Required Variables

| Name | Type | Description |
|------|------|-------------|
| `AppName` | `string` | Application name |

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `FileNameLabel` | `string` | `` | Optional label to include in the workflow filename for generating multiple workflows |
| `Cache` | `map` | `{Enable: false}` | Cache configuration. |
| `GitHubEnvironment` | `string` | `{{ .Environment }}-app-{{ .AppName }}-ecr` | GitHub environment to run build and dispatch in |
| `Ecr` | `map` | `{Enable: true, Login: true, Push: true}` | ECR configuration. |
| `Ghcr` | `map` | `{Enable: true, Login: true, Push: true}` | GHCR configuration. |
| `PreBuildWorkflows` | `map` | `{}` |  |
| `IntegrationWorkflows` | `map` | `{}` |  |
| `OnPushPaths` | `list` | `[]` | On push paths. |
| `OnPushBranches` | `list` | `[main]` | On push branches. |
| `OnPullRequestPaths` | `list` | `[]` | On pull request paths. |
| `OnPullRequestTypes` | `list` | `[]` | On pull request types. |
| `DockerfilePath` | `string` | `Dockerfile` | Dockerfile path |
| `DockerContext` | `string` | `.` | Docker build context |
| `DockerTagRules` | `list` | `[]` | Docker tag rules |
| `DockerBuildArgs` | `list` | `[]` | Docker build arguments |
| `DockerPlatforms` | `list` | `[]` | Docker platforms |
| `ImageSecurityScan` | `map` | `{Enable: true, With: {}}` | Scan Docker image for vulnerabilities with Trivy |
| `Dispatch` | `map` | `{Enable: false, IacGitHubOrg: oslokommune, IacGitHubRepo: null}` | Dispatch event to another repository after build and push. |
| `Environments` | `list` | `[]` | Environment configuration. |
| `DockerSecrets` | `map` | `{}` | Docker secrets |
| `Runner` | `string` | `ubuntu-latest` | Github Action Runner |
| `DownloadArtifact` | `map` | `{}` |  |
| `PostBuildPushAction` | `map` | `{EcsDeploy: {Enable: false, IfCondition: github.ref_name == github.event.repository.default_branch},
  LocalCommit: {Enable: false, FilePath: _config.auto.tfvars.json}, RepositoryDispatch: {
    Enable: false, IacGitHubOrg: oslokommune, IacGitHubRepo: null}}` | Configuration for actions after Docker build and push |

## Feature Flags

These map-type variables control optional features:

### Cache

Cache configuration.


**Default configuration:**
```yaml

Cache:
  Enable: false

```


### Ecr

ECR configuration.


**Default configuration:**
```yaml

Ecr:
  Enable: true
  Login: true
  Push: true

```


### Ghcr

GHCR configuration.


**Default configuration:**
```yaml

Ghcr:
  Enable: true
  Login: true
  Push: true

```


### ImageSecurityScan

Scan Docker image for vulnerabilities with Trivy


**Default configuration:**
```yaml

ImageSecurityScan:
  Enable: true
  With: {}

```


### Dispatch

Dispatch event to another repository after build and push.


**Default configuration:**
```yaml

Dispatch:
  Enable: false
  IacGitHubOrg: oslokommune
  IacGitHubRepo: null

```


## Example Configuration

From `package-config-default.yml`:


```yaml

AppName: too-tikki
Environments:
- myenv-dev
- myenv-prod
IntegrationWorkflows:
  IntegrationTests:
    Name: integration-tests
    Description: Run integration tests
    Uses: ./.github/workflows/test_km_integration.yml
    Secrets:
      GHCR_TOKEN: '{{ `${{ secrets.GITHUB_TOKEN }}` }}'
    With:
      image: '{{ `ghcr.io/${{ github.repository }}/km:${{ needs.docker-build-push.outputs.image_version}}`
        }}'
    Needs:
    - docker-build-push
    NeededBy:
    - copy-to-ecr-and-dispatch
Cache:
  Enable: true
  PackageManager: pip
  DependencyManifestFilePattern: .github/mkdocs/requirements.txt
ImageSecurityScan:
  Enable: true
  With:
    exit-code: '0'
OnPushPaths:
- .github/mkdocs/requirements.txt
- too-tikki/too-tikki.Dockerfile
- too-tikki/docs/**.md
- too-tikki/docs/**.css
- too-tikki/mkdocs.yml
DockerContext: too-tikki
DockerfilePath: too-tikki/too-tikki.Dockerfile
PostBuildPushAction:
  EcsDeploy:
    Enable: true

```

## Generated Files

### Other Files

- `_gp_{{ .AppName }}{{ if .FileNameLabel }}_{{ .FileNameLabel }}{{ end }}_integration_and_delivery.yml`
- `boilerplate.yml`

## Conditional File Generation

- Always skip: `package-config*.yml`

## Recent Changes

## [0.15.1](https://github.com/oslokommune/golden-path-boilerplate/compare/integration-and-delivery-v0.15.0...integration-and-delivery-v0.15.1) (2025-08-18)


### Bug fixes

* Avoid including `package-config-default.yml` ([#1492](https://github.com/oslokommune/golden-path-boilerplate/issues/1492)) ([a3905c8](https://github.com/oslokommune/golden-path-boilerplate/commit/a3905c84c36695f7fdfa463bccf9022ae514dcb7))


### Dependency updates

* update dependency anchore/sbom-action to v0.20.4 ([#1376](https://github.com/oslokommune/golden-path-boilerplate/issues/1376)) ([28e449d](https://github.com/oslokommune/golden-path-boilerplate/commit/28e449d63895269966c62a1c25abba11677c604b))

## [0.15.0](https://github.com/oslokommune/golden-path-boilerplate/compare/integration-and-delivery-v0.14.0...integration-and-delivery-v0.15.0) (2025-08-07)


### Features

* add PreBuildWorkflows to integration-and-delivery template ([#1451](https://github.com/oslokommune/golden-path-boilerplate/issues/1451)) ([1df7b99](https://github.com/oslokommune/golden-path-boilerplate/commit/1df7b99952e3b4267f7963632715e5921f9e94c9))

## [0.14.0](https://github.com/oslokommune/golden-path-boilerplate/compare/integration-and-delivery-v0.13.0...integration-and-delivery-v0.14.0) (2025-07-31)


### Features

* add configurable condition for ECS deployment step ([#1406](https://github.com/oslokommune/golden-path-boilerplate/issues/1406)) ([ccd976f](https://github.com/oslokommune/golden-path-boilerplate/commit/ccd976f6d542f7deb29d8e42867a4a7efdbe36a8))

## [0.13.0](https://github.com/oslokommune/golden-path-boilerplate/compare/integration-and-delivery-v0.12.4...integration-and-delivery-v0.13.0) (2025-07-30)


### Features

* Add github action template var files ([#1394](https://github.com/oslokommune/golden-path-boilerplate/issues/1394)) ([abf49e3](https://github.com/oslokommune/golden-path-boilerplate/commit/abf49e37ee1ab4511315a020b9f4248b8bd15f56))

## [0.12.4](https://github.com/oslokommune/golden-path-boilerplate/compare/integration-and-delivery-v0.12.3...integration-and-delivery-v0.12.4) (2025-07-17)


### Bug fixes

* add aws_ecr_login false when ECR is disabled ([59edb2d](https://github.com/oslokommune/golden-path-boilerplate/commit/59edb2d809ea78acbf672b76eecd7cfaf3247ae1))
