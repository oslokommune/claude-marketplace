# The Golden Path - Overview

**Generated**: 2025-11-07T09:22:51.791857
**Git Commit**: 2f7bf83
**Branch**: main
**Source Files**: 122 markdown files

---

## Project Type

An Infrastructure as Code toolkit for setting up production-ready AWS infrastructure
for Oslo Kommune (Oslo Municipality) services.

## Purpose

The Golden Path provides:
- Pre-configured Terraform modules for AWS services
- Step-by-step setup guides
- Operational runbooks for common tasks
- Security best practices
- Example implementations

## Documentation Structure

The source documentation contains 122 markdown files organized into:

- **Setup**: 47 files - Infrastructure and application setup
- **Guides**: 23 files - Operational how-to guides
- **CLI**: 17 files - "ok" CLI documentation
- **Reference**: 13 files - Technical references
- **Updates**: 15 files - Update guides
- **Help**: 2 files - Troubleshooting
- **Community**: 4 files - Community resources

## Technology Stack

### Infrastructure
- **AWS Services**: VPC, ECS (Fargate), RDS (PostgreSQL), Route53, ACM, ALB, NLB, IAM, Backup
- **Terraform**: Infrastructure as Code with Boilerplate templating
- **State Management**: S3 backend with DynamoDB locking

### CI/CD
- **GitHub Actions**: Automated workflows
- **OIDC**: Keyless AWS authentication
- **Workflows**: Image build, tag dispatch, bump, deploy

### Observability
- **Datadog**: APM, logs, metrics, tracing
- **OpenTelemetry**: Instrumentation framework
- **CloudWatch**: AWS-native monitoring

### Tools
- **ok CLI**: Simplified operations tool
- **AWS CLI**: AWS operations
- **gh**: GitHub CLI
- **jq/yq**: JSON/YAML processing

## Example Application

**too-tikki**: Java application serving as reference implementation in the pirates-iac repository.

## Target Audience

Oslo Kommune development teams setting up and operating AWS infrastructure for municipal services.

## Documentation Format

Built with MkDocs using Material theme, published to km.oslo.systems.
