# Setup Documentation

Complete guides for setting up Golden Path infrastructure.

## Setup Phases

The Golden Path setup follows these phases:

1. **Prerequisites** ([prerequisites.md](prerequisites.md))
   - AWS account setup
   - Required tools installation
   - Boilerplate configuration

2. **Infrastructure** ([infrastructure.md](infrastructure.md))
   - GitHub repository
   - Remote state (S3/DynamoDB)
   - VPC networking
   - DNS (Route53)
   - Databases (RDS)
   - Certificates (ACM)
   - Load balancers (ALB/NLB)
   - IAM roles and policies

3. **Application** ([application.md](application.md))
   - ECS cluster
   - Service definitions
   - Task configurations
   - Application common resources

4. **CI/CD** ([ci-cd.md](ci-cd.md))
   - GitHub Actions setup
   - OIDC configuration
   - Deployment workflows

## Quick Start

1. Start with [prerequisites.md](prerequisites.md)
2. Follow [infrastructure.md](infrastructure.md) step by step
3. Deploy your app with [application.md](application.md)
4. Automate with [ci-cd.md](ci-cd.md)

## Example Repository

See [pirates-iac](https://github.com/oslokommune/pirates-iac) for a complete working example.
