# AWS Access

**Source files**: 3


## guides/access-to-aws.md

# Access to AWS

- We use AWS IAM Identity Center (formerly AWS Single Sign-On) to manage access to our AWS accounts. This guide helps you set up browser-based and command-line access to AWS.

## Things to consider

- !!! tip "Recommended practice" Use the role with the least privileges needed for your task. If you're just browsing the AWS Console, a read-only role is likely sufficient. This prevents accidental changes and follows the principle of least privilege.

## Before you begin

- Make sure you have [ok](../setup/before-you-start/tools/ok.md) and the [AWS CLI](../setup/before-you-start/tools/aws-cli.md) installed, and that your Microsoft account has been granted access to one or more AWS accounts. Contact Team Kjøremiljø if you need help with any of this.

## Step 1: Verify browser-based access

Access the AWS web interface ("AWS Console") by following these steps:

1. Visit [https://osloorigo.awsapps.com/start](https://osloorigo.awsapps.com/start)
1. Sign in using your Microsoft account
1. Verify that you have access to one more AWS accounts

## Step 2: Configure command-line access

- The AWS CLI reads settings from _profiles_ in an `$HOME/.aws/config` file. Each profile tells the CLI which AWS account and role to use, and includes settings like your default region and how to authenticate.

- !!! tip "AWS CLI Profile" A profile is a named set of settings that tells the AWS CLI how to access AWS resources. You can have multiple profiles on your computer, each representing access to a different AWS account or role. For example, you might have one profile for admin access to your development account, and another for read-only access to production.

- You can manually define these profiles, but it becomes tedious and error-prone when you have access to multiple AWS accounts and roles. To help with this, we provide a command in [ok](../setup/before-you-start/tools/ok.md) that automatically generates properly formatted profiles with consistent naming for all accounts and roles you have access to:

1. Install the [AWS CLI](../setup/before-you-start/tools/aws-cli.md) if you haven't already.
1. Generate AWS CLI configuration by running the following command - your default web browser will automatically open and ask for access as part of the process:

   ```sh
   ok aws generate \
     --sso-start-url "https://osloorigo.awsapps.com/start" \
     --sso-region "eu-west-1" \
     --template 'ok-{{.AccountName}}-{{if eq .RoleName "AWSAdministratorAccess"}}admin{{else if eq .RoleName "OrigoReadOnlyAccess"}}read{{else}}{{.RoleName}}{{end}}'
   ```

1. Copy the content between the two `---` markers in the command output into your `$HOME/.aws/config` file. Create the file if it doesn't already exist.
1. Run `aws --profile "<profile-name>" sts get-caller-identity` to check if it everything works as expected, replacing `<profile-name>` with one of the profiles in your AWS CLI configuration file.

- After this setup, you'll have a profile for each combination of AWS account and role you have access to. You can then use these profiles with the AWS CLI by setting the `AWS_PROFILE` environment variable or using the `--profile` flag. We share some shell snippets below to make it easier to work with AWS CLI profiles.

## Step 3: Improve the command-line experience (optional)

We recommend adding these small functions to your `$HOME/.bashrc` or `$HOME/.zshrc`:

1. Add a shell function to your shell configuration file that makes it easy to switch between AWS CLI profiles:

    ```sh
    function sso() {
      local profile="$(aws configure list-profiles | fzf)"
      export AWS_PROFILE="$profile"
      aws sso login
    }
    ```

1. Add a snippet to your shell configuration file that gives you a nice-looking prompt that displays the active AWS profile (if any) in your prompt:

    ```sh
    if [ "$ZSH_NAME" != "" ]; then
      setopt PROMPT_SUBST
      PROMPT='🚀 %B%F{%(?.blue.red)}%1~%f%b${AWS_PROFILE:+" (🔓 $AWS_PROFILE)"}%F{default} '
    elif [ "$BASH" != "" ]; then
      PS1='\[\033[01;34m\]🚀 \W\[\033[00m\]${AWS_PROFILE:+\[\033[33m\] (🔓 $AWS_PROFILE)\[\033[00m\]} '
    fi
    ```

- If you have questions about or issues with any of this, please reach out in the [#origo-kjøremiljø-support](https://oslokommune.slack.com/archives/CV9EGL9UG) Slack channel and we'll help you out!


---


## guides/configure-aws-backup.md

# Configure AWS Backup

- This guide shows you how to configure AWS Backup to schedule daily backups of AWS resources including databases and S3 buckets.

- !!! Warning As part of this series of guides you will create a AWS Backup vault and enable [**Compliance mode**](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html#backup-vault-lock-modes). When **Compliance mode** is enabled, any backups created cannot be deleted by any user including the root user.

## Step 1: Add and configure the `backup` package

- !!! info "Assumption" This step assumes you are already using Boilerplate and have a `common-config.yml`. If you do not, have a look here for an [example](https://github.com/oslokommune/pirates-iac/blob/main/stacks/dev/common-config.yml)

```sh title="repo-iac/environments/dev/"
ok pkg add backup
cd backup
```

Edit `package-config.yml` to disable the slack notifications (you will set this up later):

```yaml title="repo-iac/environments/dev/backup/package-config.yml"
StackName: "backup"

NotifySlack:
  Enable: false
```

!!! Warning In `config_override.tf`, it's possible to set the variable `changeable_for_days`.

- If or when you set `changeable_for_days`, you will **NOT be able to delete the backup** after `changeable_for_days` days. This ensures that intruders cannot delete your backups.

## Step 2: Install the package

```bash title="repo-iac/environments/dev/backup/"
ok pkg install
```

## Step 3: Initialize and apply the `backup` stack

Initialize Terraform and apply the configuration:

```bash title="repo-iac/environments/dev/backup/"
terraform init
terraform apply
```

## Step 4: Verify

* Go to **AWS console** > **AWS Backup** > **Backup plans**
* Verify that you have a backup plan with the name of your environment
* Go to the backup plan
* Verify that it contains two scheduled backup rules: Daily and monthly

## Next steps

- Follow the [Slack notification guide](slack-backup-notifications.md) to set up Slack notifications for backups.


---


## guides/find-aws-account-id.md

# How do I find my AWS Account ID

Use the AWS CLI to find your AWS Account ID:

```bash
aws sts get-caller-identity --query "Account" --output text
```


---
