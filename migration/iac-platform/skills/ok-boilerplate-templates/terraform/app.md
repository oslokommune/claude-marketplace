# Template: app

## Metadata

- **Version**: `10.1.5`
- **Type**: `terraform`
- **Template Path**: `boilerplate/terraform/app`
- **Last Commit**: `22a5599f` - fix: correct default path to load balancing folder on disk (#1633) (2025-11-05)
- **Last Generated**: 2025-11-07

## Purpose

Boilerplate for an application running on ECS.

## Dependencies

This template depends on:

- **versions** (version: `versions-v5.0.0`)
- **app-data** (version: `app-data-v5.0.1`)

## Variables

### Required Variables

| Name | Type | Description |
|------|------|-------------|
| `AppName` | `string` | Application name |

### Optional Variables

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `IncludeLockFile` | `bool` | false | Include a Terraform lock file. |
| `AppReadOnlyRootFileSystem` | `bool` | false | Enable read-only root filesystem. |
| `AppEcsExec` | `bool` | false | Enable ECS Exec. |
| `ExampleImage` | `map` | `{Enable: false}` | Use Nginx example image. |
| `AlbHostRouting` | `map` | `{ApexDomain: {Enable: false, TargetGroupTargetStickiness: false}, Enable: false, Internal: true,
  Subdomain: {Enable: false, TargetGroupTargetStickiness: false}}` | Add ALB host routing. See: - https://github.com/oslokommune/golden-path-iac/tree/main/terraform/modules/alb-tg-host-routing - https://github.com/oslokommune/golden-path-iac/tree/main/terraform/modules/alb-tg-host-routing-apex |
| `DatabaseConnectivity` | `map` | `{Enable: false}` | Add database. |
| `OpenTelemetrySidecar` | `map` | `{Enable: false}` | Add OpenTelemetry sidecar to collect Prometheus metrics. |
| `TelemetryCollection` | `map` | `{AutoInstrumentation: {Enable: false, Runtime: java}, DatadogAgent: {Enable: false},
  Enable: false}` | Configure telemetry collection including OpenTelemetry collector for logs/traces/metrics, Java auto-instrumentation, and Datadog agent for container monitoring. |
| `Xray` | `map` | `{Enable: false}` | Enable AWS X-Ray tracing. |
| `VpcEndpoints` | `map` | `{Enable: false}` | Enable VPC endpoints. |
| `ServiceConnect` | `map` | `{Enable: false}` | Enable Amazon ECS Service Connect for service discovery. Enable this if you want to easily discover and connect to other services in your ECS cluster. |
| `DailyShutdown` | `map` | `{Enable: false}` | Enable daily shutdown of the ECS service. |
| `IamForCicd` | `map` | `{AppGitHubRepo: null, AssumableCdRole: false, EcsDeployFromAppRepo: false, Enable: false,
  IacGitHubRepo: null}` | Enable IAM roles for CI/CD. |
| `DeploymentCircuitBreaker` | `map` | `{Enable: false}` | Enable deployment circuit breaker for ECS service. |
| `Ecr` | `map` | `{Enable: true}` | Enable ECR |

## Feature Flags

These map-type variables control optional features:

### ExampleImage

Use Nginx example image.


**Default configuration:**
```yaml

ExampleImage:
  Enable: false

```


### AlbHostRouting

Add ALB host routing. See:
- https://github.com/oslokommune/golden-path-iac/tree/main/terraform/modules/alb-tg-host-routing
- https://github.com/oslokommune/golden-path-iac/tree/main/terraform/modules/alb-tg-host-routing-apex


**Default configuration:**
```yaml

AlbHostRouting:
  ApexDomain:
    Enable: false
    TargetGroupTargetStickiness: false
  Enable: false
  Internal: true
  Subdomain:
    Enable: false
    TargetGroupTargetStickiness: false

```


### DatabaseConnectivity

Add database.


**Default configuration:**
```yaml

DatabaseConnectivity:
  Enable: false

```


### OpenTelemetrySidecar

Add OpenTelemetry sidecar to collect Prometheus metrics.


**Default configuration:**
```yaml

OpenTelemetrySidecar:
  Enable: false

```


### TelemetryCollection

Configure telemetry collection including OpenTelemetry collector for logs/traces/metrics, Java auto-instrumentation, and Datadog agent for container monitoring.


**Default configuration:**
```yaml

TelemetryCollection:
  AutoInstrumentation:
    Enable: false
    Runtime: java
  DatadogAgent:
    Enable: false
  Enable: false

```


### Xray

Enable AWS X-Ray tracing.


**Default configuration:**
```yaml

Xray:
  Enable: false

```


### VpcEndpoints

Enable VPC endpoints.


**Default configuration:**
```yaml

VpcEndpoints:
  Enable: false

```


### ServiceConnect

Enable Amazon ECS Service Connect for service discovery. Enable this if you want to easily discover and connect to other services in your ECS cluster.


**Default configuration:**
```yaml

ServiceConnect:
  Enable: false

```


### DailyShutdown

Enable daily shutdown of the ECS service.


**Default configuration:**
```yaml

DailyShutdown:
  Enable: false

```


### IamForCicd

Enable IAM roles for CI/CD.


**Default configuration:**
```yaml

IamForCicd:
  AppGitHubRepo: null
  AssumableCdRole: false
  EcsDeployFromAppRepo: false
  Enable: false
  IacGitHubRepo: null

```


### DeploymentCircuitBreaker

Enable deployment circuit breaker for ECS service.


**Default configuration:**
```yaml

DeploymentCircuitBreaker:
  Enable: false

```


### Ecr

Enable ECR


**Default configuration:**
```yaml

Ecr:
  Enable: true

```


## Example Configuration

From `package-config-default.yml`:


```yaml

StackName: app-hello-world
app-data.StackName: app-hello-world-data
AppName: hello-world
AppEcsExec: true
AppReadOnlyRootFileSystem: false
ExampleImage:
  Enable: true
Ecr:
  Enable: false
ServiceConnect:
  Enable: true
AlbHostRouting:
  Enable: true
  Internal: false
  Subdomain:
    Enable: true
    TargetGroupTargetStickiness: false
DatabaseConnectivity:
  Enable: true
DailyShutdown:
  Enable: true
IamForCicd:
  Enable: false
  AppGitHubRepo: some-app-repo
  IacGitHubRepo: some-iac-repo
TelemetryCollection:
  Enable: false
  AutoInstrumentation:
    Enable: false
    Runtime: java

```

## Generated Files

### Configuration Layer (`__gp_*.tf`)

- `__gp_config.tf`
- `__gp_dependencies.tf`
- `__gp_variables.tf`

### Resource Layer (`_gp_*.tf`)

- `_gp_alb_tg_host_routing_apex_domain.tf`
- `_gp_alb_tg_host_routing_subdomain.tf`
- `_gp_ecs_container_definition_main.tf`
- `_gp_ecs_otel_collector_sidecar.tf`
- `_gp_ecs_service.tf`
- `_gp_iam_cd_assumable_role.tf`
- `_gp_iam_cicd_policies.tf`
- `_gp_iam_cicd_roles.tf`
- `_gp_security_groups.tf`
- `_gp_telemetry_collection.tf`

### User Override Files

- `config_override.tf` (user-customizable)

### Helper Scripts

- `bin/_gp_app-verify-url-available.sh`
- `bin/set_role_secret_in_app_repo.sh`
- `bin/set_role_secret_in_iac_repo.sh`

### Other Files

- `.terraform.lock.hcl`
- `boilerplate.yml`
- `terragrunt.hcl`
- `terragrunt_custom.hcl`

## Conditional File Generation

- Always skip: `package-config*.yml`
- Skip `.terraform.lock.hcl*` if: `{{ not .IncludeLockFile }}`
- Skip `__gp_config_app_image.auto.tfvars.json` if: `{{ list outputFolder "__gp_config_app_image.auto.tfvars.json" | join "/" | pathExists }}`
- Skip `config_override.tf` if: `{{ list outputFolder "config_override.tf" | join "/" | pathExists }}`
- Skip `terragrunt_custom.hcl` if: `{{ list outputFolder "terragrunt_custom.hcl" | join "/" | pathExists }}`

## Recent Changes

## [10.1.5](https://github.com/oslokommune/golden-path-boilerplate/compare/app-v10.1.4...app-v10.1.5) (2025-10-15)


### Bug fixes

* customizable name of OTel environment ([#1604](https://github.com/oslokommune/golden-path-boilerplate/issues/1604)) ([ddb350c](https://github.com/oslokommune/golden-path-boilerplate/commit/ddb350c94c085ca5cdad68cb4e28884b5a576d2c))
* customizable name of OTel environment for Datadog-specific tag ([#1610](https://github.com/oslokommune/golden-path-boilerplate/issues/1610)) ([aac0916](https://github.com/oslokommune/golden-path-boilerplate/commit/aac09160a3fb045c2ec5d9f839e169504589faf7))

## [10.1.4](https://github.com/oslokommune/golden-path-boilerplate/compare/app-v10.1.3...app-v10.1.4) (2025-09-29)


### Dependency updates

* update dependency otel-config-generator to v0.7.0 ([#1601](https://github.com/oslokommune/golden-path-boilerplate/issues/1601)) ([5862ecf](https://github.com/oslokommune/golden-path-boilerplate/commit/5862ecfe2a611990b4659b7e39b775f899c69638))

## [10.1.3](https://github.com/oslokommune/golden-path-boilerplate/compare/app-v10.1.2...app-v10.1.3) (2025-09-16)


### Bug fixes

* no repositoryCredentials must be null ([#1577](https://github.com/oslokommune/golden-path-boilerplate/issues/1577)) ([30d53a9](https://github.com/oslokommune/golden-path-boilerplate/commit/30d53a9231a3997a19a17f4c010cbf79e5126719))
* Use camelCase for repositoryCredentials ([#1574](https://github.com/oslokommune/golden-path-boilerplate/issues/1574)) ([93e13c9](https://github.com/oslokommune/golden-path-boilerplate/commit/93e13c9b6fa3ea417108405b608e4104ee3c056d))

## [10.1.2](https://github.com/oslokommune/golden-path-boilerplate/compare/app-v10.1.1...app-v10.1.2) (2025-09-04)


### Dependency updates

* update dependency app-data to v5.0.1 ([#1564](https://github.com/oslokommune/golden-path-boilerplate/issues/1564)) ([516f080](https://github.com/oslokommune/golden-path-boilerplate/commit/516f080f9138b5f1f9e899f856a748ffe66896e2))
* Update Terraform dependency lock files ([#1402](https://github.com/oslokommune/golden-path-boilerplate/issues/1402)) ([0ca8c1c](https://github.com/oslokommune/golden-path-boilerplate/commit/0ca8c1c8ee2b0e25a6fd7e19685d15e9524aeacc))

## [10.1.1](https://github.com/oslokommune/golden-path-boilerplate/compare/app-v10.1.0...app-v10.1.1) (2025-08-26)


### Bug fixes

* Use container definition compatible with module v6 ([8a6b03d](https://github.com/oslokommune/golden-path-boilerplate/commit/8a6b03dcb49b9ac258181cd216a96c1599debbbe))
