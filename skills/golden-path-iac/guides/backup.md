# Backup and Restore

**Source files**: 5


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


## guides/enable-immutable-backup.md

# Enable immutable backups

## After 24 hours: Verify backups

You must wait 24 hours to ensure that at least one backup exists.

* Go to **AWS console** > **AWS Backup** > **Backup vaults**
* Verify that the vault lock status is **Locked – Governance mode**.
* Go to the backup vault with the same name as your environment
* Verify that there is at least one recovery point

!!! Info
    **Governance mode** locks can be modified by users with extended permissions.

    **Compliance mode locks** can only be modified for `changeable_for_days` days. After that, it cannot be modified by any user, including the root user. This ensures that the backup cannot be deleted by anyone.

## Step 1: Enable immutable backups

In the file `config_override.tf` create a new local `changeable_for_days` like this:

```tf
locals{
    ...
    changeable_for_days = 3
    ...
}
```

This sets a three day wait period until the lock becomes **immutable**.

## Step 2: Apply the configuration

- !!! Warning Once these changes are applied a three day countdown begins. When **Compliance mode** is in effect, backups can only be deleted by lifecycle rules. Not even AWS support can override this lock.

Initialize Terraform and apply the configuration:

```bash
terraform init
terraform apply
```

## Step 3: Verify vault lock

* Go to **AWS console** > **AWS Backup** > **Backup vaults**
* Verify that the vault lock status is **Locked – Compliance mode**.


---


## guides/restore-rds-backup.md

# Restore RDS backup

This guide shows you how to restore a database backup to a new database cluster.

## Before you begin

You need to:

* Complete [Configure AWS Backup](configure-aws-backup.md)
* Have at least one snapshot available (by default a database backup is completed nightly)
* Configure [RDS bastion](connect-to-a-database-from-your-computer.md) to be able to verify your restored database
* Have `psql` installed to connect to your database

## Step 1: Find a backup to restore

- You can perform a point-in-time or snapshot recovery. A point-in-time recovery is essentially a snapshot recovery with the database transaction log replayed on top afterwards. Such a recovery can take a bit longer, but will restore your cluster to a more recent state.

- Start by opening the AWS console, finding the Amazon RDS service, opening **Automated backups** and clicking on the RDS cluster you want to restore:

* For point-in-time recovery: Click the **Actions** dropdown and select **Restore to point in time**.
* For snapshot recovery: Click on the snapshot you want to restore from (optionally clicking on the _Creation time_ column header to sort them by date). Click the **Actions** dropdown and select **Restore snapshot**.

- !!! tip If you want to restore from a manually created snapshot, you can do that by opening **Snapshots** in the left hand menu, selecting the **Manual** pane and clicking on the snapshot you want to restore from. The remaining steps are the same as for automatic backups.

## Step 2: Configure your new database

If this is a point-in-time recovery, start by selecting the time to restore from.

- Under **Settings** provide a name for the new database cluster under **DB instance identifier**. The default from Golden Path is `${local.environment}-main` (e.g., `pirates-dev-main`).

- <figure markdown="span"> ![Activate incoming webhooks](../images/backup/restore-step2-name.png){ width="900" } </figure>

Under **Instance configuration** select "Serverless v2". Update "Maximum capacity (ACUs)" as needed.

- <figure markdown="span"> ![Activate incoming webhooks](../images/backup/restore-step2-configure-db.png){ width="900" } </figure>

- Under **Connectivity** ensure that the VPC, subnet group and security groups are the same as for your existing DB instance, and do not have `default` in their IDs or names.

- !!! tip You can find the details of your existing DB cluster and instance under **Amazon RDS** > **Databases** and by clicking on the cluster or the instance. Connectivity details can, as an example, be found by clicking at the instance and looking at the details under the **Connectivity & security** pane.

Under **Additional configuration**:

1. Ensure that the **DB cluster parameter group** is the same as the DB cluster you are restoring from.
1. Ensure that **Deletion protection** is enabled.

- Finally, click **Restore DB cluster** or **Restore to point in time**, depending on recovery type. Restoring a database takes some time (approx. 30min for an empty database). While restoring the database will be listed as creating. Before continuing the database status must be "Available".

## Step 3: Verify database backup

- !!! Assumption In order to do this step you must already have RDS bastion configured. If you do not have RDS bastion configure, see [Connect to a database from your computer](connect-to-a-database-from-your-computer.md)

Using the `ok` tool enable access to the database from your local machine with:

```bash
ok forward #Follow the prompts and select your newly restored database.
```

In another terminal type:

```bash
psql --host=localhost --port=4812 --username=root --password --dbname=postgres
```

- The master password will be the same as for the old database. If you do not know the old password, you can update it to a known value from the console **Amazon RDS** > **Databases** > (Select restored DB) > (Modify). Set a new master password and apply the configuration.

- You should now be able to verify that the content of your database is as expected and can proceed to connect your application to the new database.

## Step 4: Connect app to new database

- This step assumes that you are following the Golden Path and details may vary depending on your setup.

In your application stack, create a new SSM parameter as follows:

```hcl
resource "aws_ssm_parameter" "db_endpoint" {
  name  = "/${local.environment}/database/${local.db_name}/restored_db_endpoint"
  type  = "String"
  value = "To be set in console"
  tags  = local.common_tags

  lifecycle {
    ignore_changes = [
      value
    ]
  }
}
```

Create the new resource by running `terraform apply`.

- Locate the database endpoint in the console under **Amazon RDS** > **Databases** > (Select your restored DB instance). Copy the database endpoint.

- Update the value of the newly created parameter under **AWS Systems Manager** > **Parameter Store** > (Search for `restored_db_endpoint`).

## Step 5: Update the App DB endpoint

Create a new file called `__gp_dependencies_override.tf` with the following:

```hcl
data "aws_ssm_parameter" "db_endpoint" {
  name            = "/${local.environment}/database/${local.db_name}/restored_db_endpoint"
  with_decryption = false
}
```

Run `terraform apply` again to update your application.

## Next step

- !!! Warning The above approach assumes that the username and password for the database will remain the same. If you rotate the password on the old database you will experience connectivity issues with the restored database.

- Once you have restored your application to a working state you should import the new database into your Terraform configuration for easier management.


---


## guides/restore-s3-backup.md

# Restore S3 backup

- This guide shows you how to restore a S3 backup to the source S3 bucket, a new S3 bucket or an existing S3 bucket.

- You could also look at the [AWS S3 Restore documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-s3.html)

## Things to consider

You will need to make some decisions before you start the restore:

* Where do you want to restore the backup to (source, new or existing S3 bucket)?
* Do you want to restore the entire backup or just specific folders? Do you have the URI of the folders you want to restore?
* If you have point-in-time-restore: from when do you want to restore the backup?

## Before you begin

You need to:

* Complete [Configure AWS Backup](configure-aws-backup.md)
* Have at least one snapshot available (by default a S3 backup is completed nightly)
* Have enough time - a restore can take up to hours

## Step 1: Have the right permissions

If you want to restore to an existing bucket, you need to temporarily enable ACL on that bucket:

* Go to the AWS S3 service
* Select the bucket you want to restore to
* Select **Permissions** > **Object Ownership** > **Edit**
* Select **ACLs enabled** and **Save changes**

- <figure markdown="span"> ![Enable ](../images/backup/restore-s3-enable-acls.png){ width="900" } </figure>

- !!! info If you are using Golden Path boilerplate:backup v3.2.0 or later, you have the necessary permissions. If you are _NOT_ using Golden Path boilerplate:backup v3.2.0 or later, you need to either:

* Upgrade to the latest version of the boilerplate

Or add extra permissions to the role used for the restore (for example: `aws-backup-<timestamp>`):

* Go to the AWS IAM service
* Select **Roles** > **aws-backup-<timestamp>**
* In **Permissions policies** > **Add permissions** > **Attach policies**
* Select **AWSBackupServiceRolePolicyForS3Restore** and **Add permissions**

## Step 2: Find a snapshot to restore

- In the AWS console find the AWS Backup. Under **Protected resources** you will find the backup resources.

- Select the resource you want to restore. Under **Recovery points** you will find the snapshots available.

Select the recovery point you want to restore and click **Restore**.

## Step 3: Configure restore

1. Under **Settings** > **Restore type** you can choose between **Restore entire bucket** or **Item level restore**.

- 2. Under **Settings** > **Restore destination** you can choose between **Restore to source bucket**, **Use existing bucket** or **Create new bucket**.

- 3. Under **Restore role** you need to choose an IAM role with the necessary permissions. If you are using golden path boilerplate:backup v3.2.0 or later, the role aws-backup-<timestamp> contains the necessary permissions.

4. Select **Restore backup**

- <figure markdown="span"> ![Settings for restore backup](../images/backup/restore-s3-settings.png){ width="900" } </figure>

- <figure markdown="span"> ![Restore role](../images/backup/restore-s3-restore-role.png){ width="900" } </figure>

## Step 4: Verify

- You will be taken to a page where you could monitor the progress. The restore can take up to hours, but the restored files will be available as soon as they are restored.

- <figure markdown="span"> ![Enable ](../images/backup/restore-s3-monitoring.png){ width="900" } </figure>

- !!! question Troubleshooting - The restore went OK but the files are still missing If the restore went OK but the files are still missing, you should check the following:

     * Did you restore to the correct bucket?
     * Did you restore the correct folders?
     * Did you restore from the correct snapshot?
      * Did the files exist at the time of the snapshot?

## Step 5: Clean up

- If you have turned on the ACL on the existing bucket, you should turn it off again in one of two ways:

Either run Terraform to restore the settings of your S3 bucket.

Or turn it off manually:

* Go to the AWS S3 service
* Select the bucket you restored to
* Select **Permissions** > **Object Ownership** > **Edit**
* Select **ACLs disabled (recommended)** and **Save changes**


---


## guides/slack-backup-notifications.md

# Configure Slack notifications for backup events

## Step 1: Create a Slack app

- Go to [Slack API apps](https://api.slack.com/apps) and create a new Slack app connected to the Oslo kommune workspace. You can choose any name you prefer.

<figure markdown="span"> ![Create a Slack app](../images/backup/app-name.png) </figure>

## Step 2: Create an incoming Slack webhook

Under **Features** > **Incoming Webhooks** activate the toggle incoming webhooks.

- <figure markdown="span"> ![Activate incoming webhooks](../images/backup/inc-webhook.png){ width="900" } </figure>

- Create a new webhook attached to a channel of your choice. Select **Add New Webhook to Workspace** and select a channel to receive backup notifications in.

- <figure markdown="span"> ![Create an incoming webhook](../images/backup/inc-webhook-act.png){ width="900" } </figure>

Copy the webhook URL to the clipboard.

<!-- ![Chose a channel](../images/backup/create-webhook.png) -->

## Step 3: Set webhook URL in AWS console

- In the AWS console, **Systems manager** > **Parameter Store** find the SSM Parameter `/${local.environment}/slack/webhook/backup`. Add the webhook URL from the previous step to this parameter.

## Step 4: Configure Slack app name and channel

In your Terraform IaC configuration, locate the file `config_override.tf`.

Create two new locals like this:

```tf title="repo-iac/environments/dev/backup/config_override.tf"
locals{
    ...
    ################################################################################
    # Slack notifications
    ################################################################################
    slack_username = "reporter"
    slack_channel  = "temp-aws-root-alerts"
    ...
}
```

- Adjust Slack username and Slack channel to suit your needs. The Slack channel needs to be the same that you selected in Step #2.

## Step 5: Enable Slack notifications

Edit `package-config.yml` and enable `NotifySlack`:

```yaml title="repo-iac/environments/dev/backup/package-config.yml"
NotifySlack:
  Enable: true
```

## Step 6: Update the `backup` stack and apply

Update the `backup` stack using the new configuration:

```bash title="repo-iac/environments/dev/backup"
ok pkg install
```

Initialize Terraform and apply the configuration:

```bash title="repo-iac/environments/dev/backup"
terraform init
terraform apply
```

## Step 7: Verify Slack notifications

Next time a backup runs a message should be posted to your channel.

```markdown
✅ An AWS Backup job was completed successfully
Resource ARN
`arn:aws:rds:eu-west-1:1234567890:cluster:pirates-dev-main`
Recovery point ARN
`arn:aws:rds:eu-west-1:1234567890:cluster-snapshot:awsbackup:job-e09f3a12-9239-7e82-041b-db378838f32e`
```

- !!! Tip By default you are notified of successful and failed jobs. You can further filter notifications by overriding the `backup_vault_events` input for the `aws_backup` module.

## Next steps

- After 24 hours, follow the guide for [enabling immutable backups](enable-immutable-backup.md) to verify that the backup is working as expected, and enable immutable backups.


---
