# Template: receive-dispatch-event

## Metadata

- **Version**: `1.1.1`
- **Type**: `github-actions`
- **Template Path**: `boilerplate/github-actions/receive-dispatch-event`
- **Last Commit**: `e650d0d1` - deps: update dependency actions/checkout to v5 (#1504) (2025-08-19)
- **Last Generated**: 2025-11-07

## Purpose

|           Name           |          Description           |  Type  |                         Default                          |Required|
|--------------------------|--------------------------------|--------|----------------------------------------------------------|--------|
|`AppName`                 |Application name                |`string`|``n/a``                                                   |yes     |
|`Environment`             |Environment                     |`string`|``n/a``                                                   |yes     |
|`CreatePr`                |Environment                     |`bool`  |``false``                                                 |no      |

## Variables

### Required Variables

| Name | Type | Description |
|------|------|-------------|
| `AppName` | `string` | Application name |
| `Environment` | `string` | Environment |

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `CreatePr` | `bool` | false | Environment |
| `GpgSign` | `bool` | true | Sign commits with GnuPG |
| `WorkingDirectory` | `string` | `stacks/{{ .Environment }}/app-{{ .AppName }}` | Working directory |
| `ImageMetadataFile` | `string` | `__gp_config_app_image.auto.tfvars.json` | Image metadata file |
| `DispatchTypes` | `list` | `['{{ .Environment }}-{{ .AppName }}-image-tag-update']` | Dispatch types |
| `MachineUserPatSecretName` | `string` | `PAT_ON_MACHINE_USER_FOR_IMAGE_UPDATE` | Secret name for machine user PAT |

## Example Configuration

From `package-config-default.yml`:


```yaml

AppName: too-tikki
CreatePr: true
GpgSign: true
WorkingDirectory: environments/dev/app-{{ .AppName }}
ImageMetadataFile: __gp_config_app_image.auto.tfvars.json

```

## Generated Files

### Other Files

- `_gp_{{ .AppName }}_{{ .Environment }}_receive_dispatch_event.yml`
- `boilerplate.yml`

## Conditional File Generation

- Always skip: `package-config*.yml`

## Recent Changes

## [1.1.1](https://github.com/oslokommune/golden-path-boilerplate/compare/receive-dispatch-event-v1.1.0...receive-dispatch-event-v1.1.1) (2025-08-18)


### Bug fixes

* Avoid including `package-config-default.yml` ([#1492](https://github.com/oslokommune/golden-path-boilerplate/issues/1492)) ([a3905c8](https://github.com/oslokommune/golden-path-boilerplate/commit/a3905c84c36695f7fdfa463bccf9022ae514dcb7))

## [1.1.0](https://github.com/oslokommune/golden-path-boilerplate/compare/receive-dispatch-event-v1.0.3...receive-dispatch-event-v1.1.0) (2025-07-30)


### Features

* Add github action template var files ([#1394](https://github.com/oslokommune/golden-path-boilerplate/issues/1394)) ([abf49e3](https://github.com/oslokommune/golden-path-boilerplate/commit/abf49e37ee1ab4511315a020b9f4248b8bd15f56))

## [1.0.3](https://github.com/oslokommune/golden-path-boilerplate/compare/receive-dispatch-event-v1.0.2...receive-dispatch-event-v1.0.3) (2025-03-12)


### Dependency updates

* update peter-evans/create-pull-request action to v7.0.8 ([#1038](https://github.com/oslokommune/golden-path-boilerplate/issues/1038)) ([8311055](https://github.com/oslokommune/golden-path-boilerplate/commit/8311055f74597a47fa01549ee57a51f6332a17eb))

## [1.0.2](https://github.com/oslokommune/golden-path-boilerplate/compare/receive-dispatch-event-v1.0.1...receive-dispatch-event-v1.0.2) (2025-03-03)


### Dependency updates

* update peter-evans/create-pull-request action to v7.0.7 ([#1020](https://github.com/oslokommune/golden-path-boilerplate/issues/1020)) ([e8d0af5](https://github.com/oslokommune/golden-path-boilerplate/commit/e8d0af5bccb9834e838544df6708bfa4f238e2d2))

## [1.0.1](https://github.com/oslokommune/golden-path-boilerplate/compare/receive-dispatch-event-v1.0.0...receive-dispatch-event-v1.0.1) (2025-01-09)


### Dependency updates

* update peter-evans/create-pull-request action to v7.0.6 ([#860](https://github.com/oslokommune/golden-path-boilerplate/issues/860)) ([0576625](https://github.com/oslokommune/golden-path-boilerplate/commit/05766254b2afb7dff4d007b286c130c874c0cbc6))
