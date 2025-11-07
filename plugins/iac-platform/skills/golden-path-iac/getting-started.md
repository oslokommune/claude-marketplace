# Getting Started with The Golden Path

## Welcome

The Golden Path provides a complete toolkit for setting up production-ready
infrastructure on AWS. This guide will help you get started.

## What You'll Build

Following The Golden Path, you'll create:

- **VPC Networking**: Isolated network infrastructure with public/private subnets
- **ECS Application Platform**: Container orchestration with Fargate
- **RDS Databases**: Managed PostgreSQL databases
- **Load Balancing**: Application and network load balancers
- **CI/CD Pipelines**: Automated deployment workflows
- **Observability**: Datadog monitoring and alerting
- **Backup Strategy**: Automated AWS Backup

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] AWS account with appropriate permissions
- [ ] GitHub account and repository
- [ ] Required tools installed (see [setup/prerequisites.md](setup/prerequisites.md)):
  - Terraform
  - AWS CLI
  - GitHub CLI (gh)
  - jq and yq
  - ok CLI

## Getting Started Steps

### 1. Review Prerequisites

Read through [setup/prerequisites.md](setup/prerequisites.md) to understand all requirements.

### 2. Set Up Infrastructure

Follow the infrastructure guide: [setup/infrastructure.md](setup/infrastructure.md)

This covers:
- GitHub repository setup
- Remote state configuration
- DNS and networking
- Databases and certificates
- Load balancers and IAM

### 3. Deploy Your Application

Follow the application guide: [setup/application.md](setup/application.md)

This covers:
- ECS cluster setup
- Service definitions
- Task configurations

### 4. Configure CI/CD

Set up automated deployments: [setup/ci-cd.md](setup/ci-cd.md)

This covers:
- GitHub Actions workflows
- OIDC authentication
- Deployment pipelines

### 5. Set Up Monitoring

Configure observability: [guides/observability.md](guides/observability.md)

This covers:
- Datadog integration
- APM instrumentation
- Log forwarding

## Example Repository

The [pirates-iac](https://github.com/oslokommune/pirates-iac) repository demonstrates
all concepts with the too-tikki example application.

## Next Steps

- Review the [overview](overview.md) for architectural context
- Check the [setup guides](setup/) for detailed instructions
- Explore [operational guides](guides/) for common tasks

## Getting Help

- [Common Issues](help/) - Troubleshooting guide
- [Community Resources](community/) - Connect with others
- [Contact Information](help/) - How to get support
