---
name: golden-path-iac
description: >
  Complete documentation for The Golden Path - Oslo Kommune's Infrastructure
  as Code toolkit for AWS. Provides comprehensive guidance on setting up
  production-ready AWS infrastructure with Terraform, including VPC networking,
  ECS application deployment, RDS databases, GitHub Actions CI/CD, Datadog
  observability, and AWS Backup. Includes the "ok" CLI tool, security best
  practices, and operational guides. Use when working with Golden Path,
  Oslo Kommune infrastructure, AWS setup with Terraform, pirates-iac repository,
  too-tikki example app, or implementing infrastructure for Oslo municipal services.
allowed-tools: Read
---

# The Golden Path Documentation

This skill provides comprehensive documentation for The Golden Path,
Oslo Kommune's toolkit for setting up production-ready infrastructure on AWS.

## Overview

**The Golden Path** is an Infrastructure as Code toolkit that provides:

- Terraform modules and templates for AWS infrastructure
- Complete setup guides from prerequisites to production
- Operational guides for common tasks
- The "ok" CLI tool for simplified operations
- Security best practices and architectural decisions
- Integration with Datadog for observability

**Target audience**: Oslo Kommune teams setting up AWS infrastructure for municipal services.

## Quick Reference

### Most Common Tasks

- [Setting up new infrastructure](setup/infrastructure.md)
- [Deploying an application](setup/application.md)
- [Configuring CI/CD](setup/ci-cd.md)
- [Connecting to databases](guides/database.md)
- [Setting up monitoring](guides/observability.md)
- [Configuring backups](guides/backup.md)

### Essential Commands

```bash
# ok CLI commands
ok aws             # AWS operations
ok forward         # Port forwarding
ok package         # Package management

# Terraform operations
terraform init
terraform plan
terraform apply
```

## How to Use This Documentation

This skill uses progressive disclosure - Claude reads only the files needed to answer your question.

### Getting Started

New to the Golden Path? Start here:
- [Getting Started Guide](getting-started.md) - First steps and overview
- [Project Overview](overview.md) - Architecture and technology stack
- [Prerequisites](setup/prerequisites.md) - Tools and requirements

### Setup Guides

Complete infrastructure setup documentation: [setup/](setup/)

- [Prerequisites](setup/prerequisites.md) - Required tools and accounts
- [Infrastructure Setup](setup/infrastructure.md) - VPC, DNS, databases, load balancers
- [Application Setup](setup/application.md) - ECS, services, task definitions
- [CI/CD Setup](setup/ci-cd.md) - GitHub Actions workflows

### Operational Guides

Task-specific how-to guides: [guides/](guides/)

- [AWS Access](guides/aws-access.md) - SSO and credential management
- [Database Operations](guides/database.md) - Connections, migrations, upgrades
- [Backup & Restore](guides/backup.md) - AWS Backup, restore procedures
- [Observability](guides/observability.md) - Datadog integration and monitoring
- [CloudFront](guides/cloudfront.md) - CDN deployment
- [Cleanup](guides/cleanup.md) - Environment deletion

### CLI Reference

Documentation for the "ok" CLI tool: [cli/](cli/)

- [CLI Overview](cli/README.md) - Installation and usage
- [Command Reference](cli/commands.md) - All available commands

### Reference Materials

Technical references and best practices: [reference/](reference/)

- [Security Best Practices](reference/security.md) - Terraform, GitHub Actions, secrets
- [Architectural Decisions](reference/adrs.md) - ADRs from pirates-iac
- [Technology Learning](reference/technologies.md) - AWS, Terraform, terminal guides
- [Renovate](reference/renovate.md) - Dependency management

## Technology Stack

- **Cloud**: AWS (VPC, ECS, RDS, Route53, ACM, ALB/NLB, IAM, Backup)
- **IaC**: Terraform, Boilerplate templates
- **CI/CD**: GitHub Actions with OIDC
- **Observability**: Datadog (APM, logs, metrics)
- **Languages**: Java (example: too-tikki app)
- **Tools**: ok CLI, AWS CLI, gh, jq, yq

## Example Repository

The [pirates-iac](https://github.com/oslokommune/pirates-iac) repository serves as a reference
implementation showing all concepts in practice with the too-tikki Java application.

## Contributing

See [contributing.md](contributing.md) for guidelines on contributing to The Golden Path.

---

**Generated**: 2025-11-07T09:22:51.791857
**Git Commit**: 2f7bf83
**Branch**: main
**Source**: 122 markdown files from /workspace/docs
