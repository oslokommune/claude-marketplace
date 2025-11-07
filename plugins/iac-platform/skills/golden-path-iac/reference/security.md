# Security Best Practices

**Source files**: 7


## reference/security/aws-production-environment-access.md

# AWS production environment access

- <!-- vale off --> To get access to your AWS production environment, please refer to the document ["Admin-tilgang til AWS produksjon"](https://docs.google.com/document/d/1ZfITl9UVg2aLqjuiTLvG331ikLPEho1Z361rbLwED4c/edit){:target=\"_blank\"} on Google Drive. <!-- vale on -->


---


## reference/security/commit-signature.md

# Commit signature

- [Commits should be signed](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification){:target=\"_blank\"} in order to ensure trust and verification of source.

- The repository flag `Require signed commits` (**Settings > Branches**) should be considered on relevant branches.


---


## reference/security/environment-secrets.md

# Environment secrets and variables

## Summary

- We recommend you separate your environment secrets from other typical environment variables. You can use AWS Secrets Manager and AWS Parameter Store to store environment secrets and variables. It is common to store values that belong together in the same place. For example storing both a `client_id` and `client_secret` in the same location to make it easier to manage.

## Environment secrets

- Environment secrets are sensitive information that should not be stored in plain text. Examples of environment secrets include:

* Database credentials
* API keys
* Environment specific secrets

- Environment secrets are stored in AWS Secrets Manager. You can refer to these in your Terraform configuration using the `aws_secretsmanager_secret_version` resource. This resource will automatically fetch the secret value from AWS Secrets Manager. The secret is stored in the `secret_string` attribute.

```hcl title="Example"
resource "aws_secretsmanager_secret" "my_secret" {
  name = "my_secret"
}
```

### Automatic rotation

- Secrets in AWS Secrets Manager can be configured to automatically rotate. This is done by setting the `rotation_enabled` attribute to `true`. `rotation_lambda_arn` specifies the ARN of the Lambda function that will be used to rotate the secret. The Lambda function must have the `secretsmanager:RotateSecret` permission.

## Environment variables

- Environment variables are non-sensitive information that is used to configure your application. Examples of environment variables include:

* Database connection strings
* API URLs
* Environment specific configuration
* Environment specific variables
* Environment specific settings
* Environment specific flags

- Environment variables are stored in AWS Parameter Store. They are referenced in your Terraform configuration using the `aws_ssm_parameter` resource. This resource will automatically fetch the parameter value from AWS Parameter Store. The variable is stored it in the `value` attribute.

```hcl title="Example"
resource "aws_ssm_parameter" "my_parameter" {
  name = "my_parameter"
  type = "String"
  value = "my_value"
  description = "My parameter"
}
```


---


## reference/security/risk-assessment.md



# Risk assessment (ROS)

- Before deploying any application to production, the team owning the application must conduct a risk assessment (ROS).

- Team Kjøremiljø plans to provide information to support the process in the future. At the moment teams need to assess all the components that divert from the Golden Path set up and document the risk for missing ROS on Golden Path. Team Veiviser has done a good job here and you can use them as a reference for how this can be done.


---


## reference/security/security-github-actions.md


# GitHub Actions

## Scorecards

- [Scorecards from the Open Source Security Foundation](https://github.com/ossf/scorecard/blob/main/docs/checks.md){:target=\"_blank\"} is a good starting point to learn about security best practices for GitHub Actions.

## Permissions and environments

- Use the `permissions` key in workflows to specify least privilege [permissions](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#modifying-the-permissions-for-the-github_token){:target=\"_blank\"} for `GITHUB_TOKEN`. [You can find a lot of examples at GitHub](https://github.com/step-security/secure-workflows/tree/main/knowledge-base/actions){:target=\"_blank\"}. For example:

```yaml
    permissions:
      contents: write
      pull-requests: write
```

- Continuous delivery _jobs_ (for example running Terraform) should run isolated in its own job with scoped permissions and environments to reduce the risk of [supply-chain attacks](https://en.wikipedia.org/wiki/Supply_chain_attack){:target=\"_blank\"} and adheres to the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege){:target=\"_blank\"}.

- 🔴 In the example below, both `hashicorp/setup-terraform` and `terraform-linters/setup-tflint` will be able to assume the same AWS IAM role because they originate from a job that has an environment named `production`. This trust condition is checked by the IAM policy.[^2]

```yaml
jobs:

  terraform:

    name: Lint and apply Terraform configuration

    permissions:
      id-token: write
      contents: read

    environment: production

    steps:
      - uses: aws-actions/configure-aws-credentials@sha-1
      - uses: terraform-linters/setup-tflint@sha-1
      - uses: hashicorp/setup-terraform@sha-1
```

🟢 Only `aws-actions/configure-aws-credentials` and `hashicorp/setup-terraform` can use the IAM role:

```yaml
jobs:

  tflint:

    name: Lint Terraform configuration

    permissions:
      contents: read

    environment: production

    steps:
      - uses: terraform-linters/setup-tflint@sha-1

  tflint:

    name: Lint and Terraform configuration

    permissions:
      id-token: write
      contents: read

    steps:
      - uses: aws-actions/configure-aws-credentials@sha-1
      - uses: hashicorp/setup-terraform@sha-1
```

## Pin actions

- GitHub Actions should be pinned to a commit hash. This is because Git tags are mutable in practice.[^1] There's no need to fork an action for security purposes as long as you follow this recommendation. Use [Dependabot](https://docs.github.com/en/code-security/dependabot){:target=\"_blank\"} to keep on top of security updates. When pinning to a SHA-1 hash it's good practice to comment with the corresponding version number:

```yaml
        uses: actions/checkout@e2f20e631ae6d7dd3b768f56a5d2af784dd54791 # v2.5.0
```

## Use fine-grained personal access tokens for cross-repository access

- 🟢 Set up fine-grained personal access tokens (PAT) on a [machine user](https://docs.github.com/en/developers/overview/managing-deploy-keys#machine-users){:target=\"_blank\"} (such as [`okctl-bot`](https://github.com/okctl-bot){:target=\"_blank\"}). Consider making the token available as a organization-level secret, which reduces the need to create duplicate secrets.

🔴 Avoid using PATs attached to private GitHub accounts.

## SSH deploy keys for cross-repository access

- 🔴 **Don't** use SSH deploy keys unless you have a special reason. Use [fine-grained personal access tokens](#use-fine-grained-personal-access-tokens-for-cross-repository-access) instead. This eliminates the need of using a third-party action.

- If there is no other option, use [`webfactory/ssh-agent`](https://github.com/webfactory/ssh-agent){:target=\"_blank\"} to load SSH deploy keys in a GitHub Actions workflow.

```yaml
      - name: Load golden-path-iac SSH deploy key
        uses: webfactory/ssh-agent@fc49353b67b2b7c1e0e6a600572d01a69f2672dd # v0.5.4
        with:
            ssh-private-key: ${{ secrets.GOLDEN_PATH_IAC_PRIVATE_DEPLOY_KEY }}
```

## Signing commits in workflows with GnuPG

- Use [`crazy-max/ghaction-import-gpg`](https://github.com/crazy-max/ghaction-import-gpg){:target=\"_blank\"} to sign commits in a GitHub Actions workflow.

```yaml
      - name: Import GPG key
        uses: crazy-max/ghaction-import-gpg@111c56156bcc6918c056dbef52164cfa583dc549 # v5.2.0
        with:
          gpg_private_key: ${{ secrets.GPG_PRIVATE_KEY }}
          passphrase: ${{ secrets.GPG_PASSPHRASE }}

          # Username and email is inferred from GPG key metadata
          git_user_signingkey: true
          git_commit_gpgsign: true
          git_config_global: true
```

## See also

- [`actions/starter-workflows`](https://github.com/actions/starter-workflows){:target=\"_blank\"}
- [GitHub Actions Security Best Practices](https://blog.gitguardian.com/github-actions-security-cheat-sheet){:target=\"_blank\"}
- [The ultimate guide to GitHub Actions authentication](https://michaelheap.com/ultimate-guide-github-actions-authentication){:target=\"_blank\"}
- [Implementing least privilege for secrets in GitHub Actions](https://github.blog/2021-04-13-implementing-least-privilege-for-secrets-in-github-actions/){:target=\"_blank\"}
- [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions){:target=\"_blank\"}

- [^2]: [Filtering for a specific environment](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#filtering-for-a-specific-environment){:target=\"_blank\"} [^3]: [Principle_of_least_privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege){:target=\"_blank\"}


---


## reference/security/security-report.md



# Security report

- The Golden Path has been evaluated by the security team from EY. The newest report is from December 2022. Contact Nina Høegh-Larsen on Slack if you wish to get access to the report.


---


## reference/security/security-terraform.md



# Terraform

- There are multiple tools for policy as code and linting. These can be used to scan for security issues in Terraform code. Some examples are [Checkov](https://www.checkov.io/){:target=\"_blank\"}, [`tfsec`](https://aquasecurity.github.io/tfsec){:target=\"_blank\"}, [Terrascan](https://runterrascan.io/){:target=\"_blank\"} or [`tflint`](https://github.com/terraform-linters/tflint){:target=\"_blank\"}.


---
