# Database Operations

**Source files**: 4


## guides/connect-to-a-database-from-your-computer.md

# Connect to a database from your computer

This guide shows you how to connect to a database via localhost on a specific port.

- <figure markdown> ![Otters doing telecommunication](https://user-images.githubusercontent.com/1691190/229385245-5f484665-cb90-4f2a-aa13-54fddbfc511e.svg){ width="390" } </figure>

- !!! example "Reference implementation" See how [RDS bastion is configured in `pirates-iac`](https://github.com/oslokommune/pirates-iac/blob/main/stacks/dev/rds-bastion/_gp_rds_bastion.tf).

## Things to consider

The database will be accessible by anyone who can log in to the AWS account.

- If you choose to omit the optional step involving the setup of VPC endpoints, it's important to understand the implications. When you run the `ok forward` command, as outlined in this guide, it initiates an ECS task running Nginx. This setup allows the container to access your database. However, it also grants Nginx access to the entire internet, [denoted by the CIDR block `0.0.0.0/0`](https://github.com/oslokommune/golden-path-iac/blob/main/terraform/modules/rds_bastion/security_groups.tf#L32). **You should consider the security implications of this**, but as a general guideline, you should not run this in production.

## Before you begin

* You have followed the setup guide and have a working environment
* You have a database in a private subnet
* You have an ECS cluster in a private subnet

## Step 1: Configure

1. Add and configure the RDS bastion package

    ```bash title="repo-iac/environments/dev"
    ok pkg add rds-bastion
    cd rds-bastion
    ```

Update `package-config.yml` with your preferences.

2. Install and apply the package

    ```bash title="repo-iac/environments/dev/rds-bastion/"
    ok pkg install
    terraform init
    terraform apply
    ```

## Step 2: Enhance container security with VPC endpoints (optional)

- To enhance the security of your container and prevent it from accessing the internet directly, you can utilize VPC endpoints.

!!! warning "Before you begin"
    - Ensure you have set up VPC endpoints. For guidance, refer to [setting up networking](../setup/infrastructure/setup-networking.md).
    - Make sure you have a suitable container image in your private ECR registry. For details on setting this up, see [Create and use ECR pull through cache rules](../setup/infrastructure/setup-application-common.md/#step-4-perform-initial-pull-for-ecr).

- Once you have the VPC endpoints set up and your container image in place, the next step is to enable VPC endpoint support in your Terraform configuration.

1. Open `rds-bastion/package-config.yml`.
2. Modify the file by setting the `UseVPCEndpoints` variable to `true`. 3. Apply the configuration

```bash title="repo-iac/environments/dev/rds-bastion/"
ok pkg install
terraform init
terraform apply
```

## Step 3: Connect to database

1. Run the `ok forward` command to start the port forwarding session.

    ```bash
    ok forward
    ```

- 2. You will be presented a list of Task Definitions which is applicable for port forwarding. Select the one you want to use using the arrow keys and press enter.

    ```bash
    > ssm-pf-my-bastion-task-definition
    > ssm-pf-another-bastion-task-definition
    ```

Now a new ECS task will be started. This usually takes 20 to 30 seconds.

- 3. Next you will be presented a list of all the RDS instances in your environment. Select the one you want to port forward to using the arrow keys and press enter.

    ```bash
    > my-team-db.c7d1xxxi7fm.eu-west-1.rds.amazonaws.com
    > some-other-db.c7d1xxxi7fm.eu-west-1.rds.amazonaws.com
    ```

- 4. Last step is to enter the ports you want to forward to and expose locally for the forwarded database. 5. Now the database is port forwarded and you can connect to it using the forwarded ports.

    ```bash
    LOCAL_PORT=4812 # or replace this with the port you entered in step 4
    psql --host=localhost --port=$LOCAL_PORT --username=db_username --password --dbname=postgres
    ```

6. When you are done, press `Ctrl+C` to stop the port forwarding session.

- If you don't stop the port forwarding session manually, it will be stopped automatically by the Lambda function after some time of inactivity.

## builds/ directory

- !!! info "What is the `builds` directory?" `terraform apply` will create a directory called `builds`. This should be committed to your IaC repository. If not, future runs of `terraform apply` will always detect a change. Sometimes `terraform plan/apply` will report a change even though the code has not changed. This is due to the hash changing and it is normal expected behavior.


---


## guides/database.md

# IAM access to PostgreSQL databases

- For background information on the database choices, please read [the RFC for RDBMS in the Golden Path](https://github.com/oslokommune/golden-path-iac/blob/main/rfc/0001-Database/0001-Database.md){:target=\"_blank\"}.

## IAM access to PostgreSQL

- The [`iam_database_authentication_enabled`](https://github.com/terraform-aws-modules/terraform-aws-rds-aurora/blob/master/variables.tf#L199){:target=\"_blank\"} flag is set to `true` in both the `postgres_aurora` and `postgres_aurora_serverless` module supplied as part of Golden Path. [The AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html){:target=\"_blank\"} explains more about the benefits and limitations when using IAM access to your database, please review this before continuing.

- !!! info "Future" This first version of the documentation will set up the database user and connect from a dedicated EC2 instance to show the step-by-step required to connect to your database. Connecting from localhost with IAM access will be covered later once [#65](https://github.com/oslokommune/golden-path-iac/issues/65){:target=\"_blank\"} is done.

### Prerequisites

* A PostgreSQL database and a user capable of adding new users (as the one supplied by Golden Path setup)
* EC2 instance - for demonstrating the IAM functionality only. This will be void once `Connection to PostgreSQL from localhost` is done
  * Create a EC2 instance in the correct VPC where your DB cluster is set up
    * Ubuntu is fine
    * Choose the VPC where your infrastructure is set up
    * Choose a public subnet to get a public IP address
  * Remember to create a keypair and download it
  * Go to the VPC where you created your EC2 instance and update the security group for the instance
    * Allow inbound SSH from your IP address
    * Allow outbound rules to all outbound
  * Update PostgreSQL cluster to allow connection from EC2: **Actions > Set up EC2 connection**
    * This will set up a security group that connects the EC2 instance with your RDS instance
    * Choose the EC2 instance you just created
  * SSH to the box:
    * `ssh -i "YOUR-KEY-FILE.pem" ubuntu@X.Y.Z.A`. Keep this connection open for the step by step below
    * Install PostgreSQL client: `sudo apt-get install postgresql-client-14`

## Step by step

### Enable IAM authentication

* If the `IAM DB authentication` flag under cluster `Configuration` is set to `Enabled`: no action is needed
* Otherwise: run `terraform get -update` and `tf apply` to enable IAM authentication

### Connect to PostgreSQL

- From the EC2 instance: Connect with the user set up by Golden Path, this user have rights to add another user and grant access

```sh
psql --host=YOUR-DATABASE-HTTP-ENDPOINT \
  --port=5432 \
  --username=db_username \
  --password \
  --dbname=postgres
```

* Values for `db_username` and `db_password` are located in [AWS Parameter Store](https://eu-west-1.console.aws.amazon.com/systems-manager/parameters/){:target=\"_blank\"}
* The default database name is `postgres` if nothing else is configured. Do not confuse with DB instance ID

### Create IAM user

- Create a new user for your database. In this case `mydbuser` will be used as an example, but the username should reflect the usage you intend for this user to have.

```sql
CREATE USER mydbuser WITH LOGIN;
```

Grant the special `rds_iam` role to the new user:

```sql
GRANT rds_iam TO mydbuser;
```

### Grant access to database

- You can grant different levels of access to the user, execute one of the following statements (or any other grants based on your requirement):

#### Full access to schema

```sql
GRANT USAGE ON SCHEMA schema_name TO mydbuser;
```

#### Only access to one table

```sql
GRANT SELECT ON table_name TO mydbuser;
```

#### Access to all tables

```sql
GRANT SELECT ON ALL TABLES IN SCHEMA schema_name TO mydbuser;
```

### Policy document

- Given the following policy document in `rds-connect-mypostgres-cluster-policy.json` (update with the correct ARN for your user):

```json
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Effect": "Allow",
         "Action": [
             "rds-db:connect"
         ],
         "Resource": [
             "arn:aws:rds-db:eu-west-1:[account-id]:dbuser:[DbiResourceId]/mydbuser"
         ]
      }
   ]
}
```

To find the `DbiResourceId` for your Resource:

```sh
aws rds describe-db-instances \
  --query "DBInstances[*].[DBInstanceIdentifier,DbiResourceId]"
```

Create the policy:

```sh
aws iam create-policy \
  --policy-name rds-connect-mypostgres-cluster-policy \
  --policy-document file://rds-connect-mypostgres-cluster-policy.json
```

### Create role

Create a role and attach the following policy stored in `assume-role-policy.json`:

```sh
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AssumeRolePolicy",
      "Effect": "Allow",
      "Principal": {"AWS": "[account-id]"},
      "Action": "sts:AssumeRole"
    }]
}
```

```sh
aws iam create-role \
  --role-name rds-assume-mydbuser-mypostgres-cluster \
  --assume-role-policy-document file://assume-role-policy.json
```

Attach the `rds-connect-mypostgres-cluster-policy` created to that role:

```sh
aws iam attach-role-policy \
  --policy-arn arn:aws:iam::[account-id]:policy/rds-connect-mypostgres-cluster-policy \
  --role-name rds-assume-mydbuser-mypostgres-cluster
```

- Now there is a role that can be assumed at a later point. You can check that everything is in order by running:

```sh
aws sts assume-role \
  --role-arn "arn:aws:iam::[account-id]:role/rds-assume-mydbuser-mypostgres-cluster" \
  --role-session-name assume-mydbuser-mypostgres-cluster
```

### Connect with IAM to PostgreSQL

Switch to your local machine where you have `awscli` set up and run the following:

```sh
export RDSHOST="YOUR-DATABASE-HTTP-ENDPOINT"

export PGPASSWORD="$(aws rds generate-db-auth-token \
--hostname $RDSHOST \
--port 5432 \
--region eu-west-1 \
--username mydbuser)"

echo $PGPASSWORD
```

Copy the `PGPASSWORD` for later usage.

### Download the certificate for RDS

On the EC2 instance where you will connect to PostgreSQL, download the certificate:

```sh
curl -XGET https://s3.amazonaws.com/rds-downloads/rds-ca-2019-root.pem > rds-ca-2019-root.pem
```

### Connect to RDS

Export `PGPASSWORD` from your local machine to the EC2 instance:

```sh
export PGPASSWORD='Password-copied-from-earlier-command'
```

and connect to PostgreSQL:

```sh
psql -h YOUR-DATABASE-HTTP-ENDPOINT \
  -p 5432 \
  "sslmode=verify-full sslrootcert=rds-ca-2019-root.pem dbname=postgres user=mydbuser"
```


---


## guides/database_migration.md

# How to migrate PostgreSQL data from RDS to Aurora

## Introduction

- This document describes two methods on how to migrate data from Relational Database Service (RDS) to Aurora Serverless. Both processes will require a maintenance window in which downtime is expected.

- Use method 1 if you are migrating from an AWS RDS database to Aurora PostgreSQL (non-Serverless). Use method 2 if you are migrating from any other database to Aurora Serverless or Aurora PostgreSQL. Check each method for any limitations or special considerations.

## Prerequisites

* You must be [logged in to your AWS account](../guides/access-to-aws.md) with a role that have administrator rights.

## Migrate using RDS snapshot

- By using a snapshot of the RDS instance, you will be able to create a new Aurora cluster based on the data that exists in the database at the moment the snapshot was taken.

- Any data written to the database after the snapshot was taken will not be migrated. Consider turning off any services that might write to the database during the migration process.

### Limitations

* Major version upgrades are not supported for example PostgreSQL 9.6 to 10.7

### Step-by-step using snapshot

1. Get the RDS instance identifier and engine version of the database you want to migrate data from:

      ```bash
      aws rds describe-db-instances --query 'DBInstances[*].DBInstanceIdentifier'
      ```

2. Get the engine version of the database you want to migrate data from:

      ```bash
      # Replace <db-instance-identifier> with the RDS instance identifier from step 1
      aws rds describe-db-instances --db-instance-identifier <db-instance-identifier> --query 'DBInstances[*].EngineVersion'
      ```

3. Create a snapshot of the RDS instance:

      ```bash
      # Replace <rds-instance-id> with the RDS instance identifier from step 1
      # Replace <snapshot-name> with the name of the snapshot
      aws rds create-db-snapshot --db-instance-identifier <rds-instance-id> --db-snapshot-identifier <snapshot-name>
      ```

4. Wait for the snapshot to be created:

- You can check the progress in [RDS console](https://console.aws.amazon.com/rds/home){:target=\"_blank\"} or by waiting for the `aws-cli` command below to complete.

      ```bash
      # Replace <snapshot-name> with the name of the snapshot used in step 3.
      aws rds wait db-snapshot-completed --db-snapshot-identifier <snapshot-name>
      # This command will return when the snapshot is created, but you won't see anything in the process
      ```

5. Get the ARN of the snapshot for use in the next step:

      ```bash
      # Replace <snapshot-name> with the name of the snapshot used in step 3
      aws rds describe-db-snapshots --db-snapshot-identifier <snapshot-name> --query 'DBSnapshots[*].DBSnapshotArn'
      ```

6. Update the Terraform file which represents the new database

- This file usually exists in the `infra/` directory in your IaC repository and is usually one of either `postgres-aurora` or `postgres-aurora-severless`.

      ```hcl
         module "args_rds" {
            source = "git@github.com:oslokommune/golden-path-iac//terraform/modules/args-rds-aurora?ref=args-rds-aurora-v0.1.0"
         }

         locals {
            args_rds = module.args_rds.data.serverless.small
         }

         module "rds_aurora_serverless" {
            source  = "terraform-aws-modules/rds-aurora/aws"

            name        = local.db_name
            engine      = local.args_rds.engine
            engine_mode = local.args_rds.engine_mode
            # Replace <engine-version> with the engine version from step 2, or upgrade to another valid version
            engine_version = "<engine-version>"
            ..

            # Replace <snapshot-arn> with the ARN of the snapshot from step 5
            snapshot_identifier = "<snapshot-arn>"

            tags = local.common_tags
         }

      ```

- 7. The migration starts when the Terraform plan is applied. The migration will take some time depending on the size of the database. You can check the progress of the migration in the [AWS RDS console](https://console.aws.amazon.com/rds/home){:target=\"_blank\"} and look at the `Status` column.

8. You can now update endpoints and other services to point to the new database.

- 9. Once the migration is done you can remove the snapshot identifier from the Terraform file and apply again. This will remove the snapshot identifier from the Terraform state.

10. Verify that the migration was successful and remove the old database.

## Migrate using `pg_dump` and `pg_restore`

- By using `pg_dump` and `pg_restore` you can create a dump of the database and then restore it to the new database. Similar to the snapshot method, any data written to the database after the dump was taken will not be migrated. Consider turning off any services that might write to the database during the migration process.

### Step-by-step using `pg_dump` and `pg_restore`

- You need to have access to the database you want to migrate data from. This can be done by locally connecting to the database using a bastion host and then dumping the database to your machine, or by running the commands from within a EC2 instance that has access to the database and a storage medium where the dump can be stored to and subsequently restored from to new the new database.

- !!! info "EC2" Team Kjøremiljo recommends dumping and restoring from an EC2 instance, as it will be faster, secure and more reliable than doing it from a local machine.

#### Dump the database

1. Have a shell open to the EC2 instance or bastion host that has access to the database you want
to migrate data from.

2. Create a dump of the database:

    ```bash
    # Replace <hostname> with the hostname of the database you want to migrate data from
    # Replace <username> with the master username
    # Replace <database> with the name of the database
    # Replace <output-file> with the name of the dump file
    pg_dump --host <hostname> --format=directory --create --jobs 5 --dbname <database> --username <username> --file <output-file>.dump
    ```

- 3. Copy the dump file to a storage medium that can be accessed from the new database. This can be done by copying the file to an S3 bucket or to a shared drive.

#### Restore the database

1. Create a new database using the Terraform file from the first method. You can use the same
- Terraform file as the one used in the first method, but you need to remove the snapshot identifier from the file.

- 2. Have a shell open to the EC2 instance or bastion host that has access to the database you want to migrate data to.

3. Restore the dump file to the new database:

    ```bash
    # Replace <hostname> with the hostname of the new database
    # Replace <username> with the master username
    # Replace <database> with the name of the database
    # Replace <input-file> with the name of the dump file
    pg_restore --host <hostname> --jobs 5 --dbname <database> --username <username> --file <input-file>.dump
    ```

- 4. You can now update endpoints and other services to point to the new database. 5. Verify that the data has been migrated correctly and delete the dump file from the storage medium.

## See also

- [Best practices for migrating PostgreSQL databases to Amazon RDS and Amazon Aurora](https://aws.amazon.com/blogs/database/best-practices-for-migrating-postgresql-databases-to-amazon-rds-and-amazon-aurora){:target=\"_blank\"}


---


## guides/postgresql-upgrade-version.md

# Upgrade PostgreSQL version

This guide explains how to upgrade PostgreSQL between minor or major versions.

## Before you begin

* **Enable backups** for your database first. See [Restore RDS backup](restore-rds-backup.md) to find existing backups-
* Upgrade development databases before production.
* **Choose your target version** from the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.PostgreSQL.UpgradeVersion.html). Consider upgrading to PostgreSQL 16 first if going from 15 to 17.
* Review database customizations outside Golden Path (such as read replicas).
* **Plan for downtime** - major version upgrades cause service interruption.

- !!! info "What's new in PostgreSQL?" Check [Amazon RDS for PostgreSQL updates](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.html)

## Step 1: Set target version

Create `_gp_postgres_aurora_serverless_override.tf` and set the engine version:

```hcl title="repo-iac/environments/dev/databases/_gp_postgres_aurora_serverless_override.tf"
module "rds_aurora_serverless_main" {
  allow_major_version_upgrade = true   # Only needed for major version changes
  engine_version = "17.5"              # Replace with your target version
}
```

- !!! info "What happens if you set major version only?" AWS uses the default minor version, not necessarily the latest

## Step 2: Set parameter group family

- If you are changing the major version, update the parameter group family parameter in `config_override.tf`.

- Find available values in the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.setting-capacity.html#aurora-serverless-v2.parameter-groups-defaults):

```hcl title="repo-iac/environments/dev/databases/config_override.tf"
  db_cluster_parameter_group_family = "aurora-postgresql17"
```

## Step 3: Apply changes

Plan, review, then apply the updated configuration

```shell
terraform plan
terraform apply
```

- !!! tip "Track upgrade time" Time the upgrade to plan your production deployment. Production databases are larger and take longer to upgrade

## Step 4: Verify upgrade

Test that your application works and that you can connect via `ok forward`.

## Step 5: Reset variables

If in step 1 you created `_gp_postgres_aurora_serverless_override.tf` from scratch, delete the file.

If you updated it, remove the variables you added:

* `engine_version`
* `allow_major_version_upgrade`

Apply the changes:

```shell
terraform apply
```

## Step 6: Commit changes

Commit and push all changes to your IaC repository.


---
