# Template: docker-build-push

## Metadata

- **Version**: `2.4.1`
- **Type**: `github-actions`
- **Template Path**: `boilerplate/github-actions/docker-build-push`
- **Last Commit**: `b5d6ebdb` - chore(main): release docker-build-push 2.4.1 (#1497) (2025-08-18)
- **Last Generated**: 2025-11-07

## Purpose

|        Name         |                     Description                     |  Type  |                                                                                                   Default                                                                                                   |Required|
|---------------------|-----------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
|`AppName`            |Application name                                     |`string`|``n/a``                                                                                                                                                                                                      |yes     |
|`Environment`        |Environment                                          |`string`|``n/a``                                                                                                                                                                                                      |yes     |
|`PostBuildPushAction`|Configuration for actions after Docker build and push|`map`   |``{"LocalCommit": {"Enable": false, "FilePath": "_config.auto.tfvars.json"}, "RepositoryDispatch": {"Enable": false, "IacGitHubRepo": null, "IacGitHubOrg": "oslokommune"}, "EcsDeploy": {"Enable": false}}``|no      |

## Variables

### Required Variables

| Name | Type | Description |
|------|------|-------------|
| `AppName` | `string` | Application name |
| `Environment` | `string` | Environment |

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `PostBuildPushAction` | `map` | `{EcsDeploy: {Enable: false}, LocalCommit: {Enable: false, FilePath: _config.auto.tfvars.json},
  RepositoryDispatch: {Enable: false, IacGitHubOrg: oslokommune, IacGitHubRepo: null}}` | Configuration for actions after Docker build and push |
| `OnPushPaths` | `list` | `[]` | On push paths. |
| `OnPushPathsIgnore` | `list` | `[]` | On push paths ignore. |
| `OnPushBranches` | `list` | `[main]` | On push branches. |
| `OnPrTypes` | `list` | `[]` | On PR types. |
| `OnPrPaths` | `list` | `[]` | On PR paths. |
| `OnWorkflowCall` | `map` | `{Enable: false, Inputs: {}, Secrets: {}}` | On workflow call. |
| `IfCondition` | `string` | `` | If condition for the build and push job |
| `Ecr` | `map` | `{Enable: true, Login: true, Push: true}` | ECR configuration. |
| `Ghcr` | `map` | `{Enable: true, Login: true, Push: true}` | GHCR configuration. |
| `Cache` | `map` | n/a | Cache configuration. |
| `GitHubEnvironment` | `string` | `{{ .Environment }}-app-{{ .AppName }}-ecr` | GitHub environment to run build and dispatch in |
| `DockerfilePath` | `string` | `Dockerfile` | Dockerfile path |
| `DockerSecrets` | `map` | `{}` | Docker secrets |
| `DockerContext` | `string` | `.` | Docker build context |
| `DockerTagRules` | `list` | `[]` | Docker tag rules |
| `DockerBuildArgs` | `list` | `[]` | Docker build arguments |
| `DockerPlatforms` | `list` | `[]` | Docker platforms |
| `PreWorkflows` | `map` | `{}` |  |
| `DownloadArtifact` | `map` | `{}` |  |

## Feature Flags

These map-type variables control optional features:

### OnWorkflowCall

On workflow call.


**Default configuration:**
```yaml

OnWorkflowCall:
  Enable: false
  Inputs: {}
  Secrets: {}

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


## Example Configuration

From `package-config-default.yml`:


```yaml

AppName: too-tikki
Dispatch:
  Enable: true
OnPushPaths:
- main.go
OnPushBranches:
- main
Cache:
  Enable: false
Ecr:
  Enable: true
  Login: true
  Push: true
Ghcr:
  Enable: false
DockerfilePath: Dockerfile
PostBuildPushAction:
  RepositoryDispatch:
    Enable: true
    IacGitHubOrg: oslokommune
    IacGitHubRepo: my-iac-repo

```

## Generated Files

### Other Files

- `_gp_{{ .AppName }}_{{ .Environment }}_build_and_push_image.yml`
- `boilerplate.yml`

## Conditional File Generation

- Always skip: `package-config*.yml`

## Recent Changes

## [2.4.1](https://github.com/oslokommune/golden-path-boilerplate/compare/docker-build-push-v2.4.0...docker-build-push-v2.4.1) (2025-08-18)


### Bug fixes

* Avoid including `package-config-default.yml` ([#1492](https://github.com/oslokommune/golden-path-boilerplate/issues/1492)) ([a3905c8](https://github.com/oslokommune/golden-path-boilerplate/commit/a3905c84c36695f7fdfa463bccf9022ae514dcb7))

## [2.4.0](https://github.com/oslokommune/golden-path-boilerplate/compare/docker-build-push-v2.3.2...docker-build-push-v2.4.0) (2025-07-30)


### Features

* Add github action template var files ([#1394](https://github.com/oslokommune/golden-path-boilerplate/issues/1394)) ([abf49e3](https://github.com/oslokommune/golden-path-boilerplate/commit/abf49e37ee1ab4511315a020b9f4248b8bd15f56))


### Bug fixes

* **template:** remove trailing comma in DockerPlatforms list ([#1329](https://github.com/oslokommune/golden-path-boilerplate/issues/1329)) ([6174c41](https://github.com/oslokommune/golden-path-boilerplate/commit/6174c41fec67da2cc86c2ac48c8b962cb3bed63e))

## [2.3.2](https://github.com/oslokommune/golden-path-boilerplate/compare/docker-build-push-v2.3.1...docker-build-push-v2.3.2) (2025-03-06)


### Bug fixes

* Add -ecr to environment name for ecs deploy job ([c02e956](https://github.com/oslokommune/golden-path-boilerplate/commit/c02e95673a26cd48bed4d951c4cc8d49c312cd68))

## [2.3.1](https://github.com/oslokommune/golden-path-boilerplate/compare/docker-build-push-v2.3.0...docker-build-push-v2.3.1) (2025-03-06)


### Bug fixes

* Add environment and id-token perm for ecs deploy job ([f2dcee1](https://github.com/oslokommune/golden-path-boilerplate/commit/f2dcee1c59ee5aba0cc8e53dbb061b58a54b0733))

## [2.3.0](https://github.com/oslokommune/golden-path-boilerplate/compare/docker-build-push-v2.2.1...docker-build-push-v2.3.0) (2025-03-05)


### Features

* Use action that removes invalid properties from task definition ([8f9086e](https://github.com/oslokommune/golden-path-boilerplate/commit/8f9086e23c261d3db2bdba94b617aa050a9f74d9))
