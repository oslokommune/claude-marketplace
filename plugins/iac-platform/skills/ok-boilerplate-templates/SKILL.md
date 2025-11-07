---
name: ok-boilerplate-templates
description: Guide for using the ok tool to manage and deploy Boilerplate infrastructure templates
---

# Boilerplate Templates with `ok` Tool

This skill provides guidance on using the `ok` tool to manage Boilerplate templates for infrastructure deployment.

## Overview

The `ok` tool is a comprehensive infrastructure management toolbox that streamlines Terraform environment setup and maintenance.
This repository contains **30 templates** (24 Terraform, 6 GitHub Actions).

## Core `ok pkg` Commands

### Adding a Template

```bash
# Add a template to your package manifest
ok pkg add <template-url> [--output-folder <path>]
```

**Template URL format:**
```
github.com/oslokommune/golden-path-boilerplate//boilerplate/<type>/<template-name>?ref=<version>
```

### Installing/Updating Templates

```bash
# Install or update all templates in package manifest
ok pkg install

# Update package manifest and configurations
ok pkg update
```

## Available Templates


### Github-Actions Templates

- [cloudfront-deploy](github-actions/cloudfront-deploy.md) (v0.4.2)
- [docker-build-push](github-actions/docker-build-push.md) (v2.4.1)
- [integration-and-delivery](github-actions/integration-and-delivery.md) (v0.15.1)
- [receive-dispatch-event](github-actions/receive-dispatch-event.md) (v1.1.1)
- [renovate](github-actions/renovate.md) (vunknown)
- [terraform-on-changed-dirs](github-actions/terraform-on-changed-dirs.md) (v2.5.0)



### Terraform Templates

- [app](terraform/app.md) (v10.1.5)
- [app-common](terraform/app-common.md) (v4.0.0)
- [app-data](terraform/app-data.md) (v5.0.1)
- [atlantis](terraform/atlantis.md) (v1.17.0)
- [backup](terraform/backup.md) (v4.1.0)
- [certificates](terraform/certificates.md) (v2.0.0)
- [cloudfront-static-website](terraform/cloudfront-static-website.md) (v1.3.0)
- [cloudfront-static-website-data](terraform/cloudfront-static-website-data.md) (v1.0.0)
- [databases](terraform/databases.md) (v5.0.0)
- [datadog-common](terraform/datadog-common.md) (v2.0.1)
- [dns](terraform/dns.md) (v4.0.0)
- [eventbridge-notifications](terraform/eventbridge-notifications.md) (v0.0.0)
- [iam](terraform/iam.md) (v3.0.1)
- [load-balancing-alb](terraform/load-balancing-alb.md) (v4.0.0)
- [load-balancing-alb-data](terraform/load-balancing-alb-data.md) (v3.1.0)
- [networking](terraform/networking.md) (v3.0.1)
- [networking-data](terraform/networking-data.md) (v1.0.0)
- [observability](terraform/observability.md) (v3.0.0)
- [observability-grafana-settings](terraform/observability-grafana-settings.md) (v3.0.0)
- [rds-bastion](terraform/rds-bastion.md) (v4.1.1)
- [remote-state](terraform/remote-state.md) (v3.0.0)
- [scaffold](terraform/scaffold.md) (v3.0.0)
- [terragrunt](terraform/terragrunt.md) (v3.2.1)
- [versions](terraform/versions.md) (v5.0.0)




## Template Documentation

Each template in the Available Templates section above links to detailed documentation that includes:
- Required and optional variables
- Feature flags and configuration
- Dependencies
- Example configurations
- Recent changelog entries

## Working with Templates

### Step 1: Choose a Template

1. Review available templates in the list above
2. Click on a template name to read its detailed documentation
3. Check required variables and dependencies

### Step 2: Add Template to Project

```bash
# Example: Add the app template
ok pkg add \\
  github.com/oslokommune/golden-path-boilerplate//boilerplate/terraform/app?ref=app-v10.1.5 \\
  --output-folder infrastructure/app
```

### Step 3: Configure Variables

After adding a template, configure it by editing:
- `package-config.yml` - Your custom variable values
- Review `package-config-default.yml` for available options

### Step 4: Install/Generate

```bash
# Generate Terraform code from templates
ok pkg install
```

## Best Practices

1. **Version Pinning**: Always use specific version tags (e.g., `?ref=app-v10.1.5`) rather than `latest`
2. **Read Documentation**: Review the template documentation linked in the Available Templates section before using a template
3. **Check Dependencies**: Some templates depend on others (e.g., `app` requires `app-data`)
4. **Review Changelogs**: Check recent changes section in template docs for breaking updates
5. **Validate Configuration**: Use `ok pkg fmt` to format package manifests

## Common Workflows

### Setting up a new application

```bash
# 1. Add networking template
ok pkg add github.com/oslokommune/golden-path-boilerplate//boilerplate/terraform/networking?ref=networking-v3.0.1

# 2. Add load balancer
ok pkg add github.com/oslokommune/golden-path-boilerplate//boilerplate/terraform/load-balancing-alb?ref=load-balancing-alb-v4.0.0

# 3. Add application
ok pkg add github.com/oslokommune/golden-path-boilerplate//boilerplate/terraform/app?ref=app-v10.1.5

# 4. Configure variables in package-config.yml
# 5. Generate infrastructure code
ok pkg install
```

### Adding a database

```bash
# Add databases template
ok pkg add github.com/oslokommune/golden-path-boilerplate//boilerplate/terraform/databases?ref=databases-v5.0.0

# Configure in package-config.yml and install
ok pkg install
```

## Troubleshooting

- **Missing variables**: Check template documentation for required variables
- **Dependency errors**: Ensure dependent templates are added first
- **Version conflicts**: Use `ok pkg update` to sync configurations
- **Template not found**: Verify template name and version in the Available Templates section above

## Reference

- **Total templates**: 30
- **Last updated**: 2025-11-07
- **Repository**: github.com/oslokommune/golden-path-boilerplate