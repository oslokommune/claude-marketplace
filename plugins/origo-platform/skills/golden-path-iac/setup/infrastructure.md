# Infrastructure Setup

**Source files**: 14


## setup/ci-cd/bump-image/add-pat-as-a-secret-to-the-infrastructure-repository.md

- This section shows you how to add the PAT as a secret to the infrastructure repository. It's [the same PAT you created earlier](../dispatch-image-tag/create-pat-for-sending-dispatch-events.md).

## Step 1: Add the secret

- Change `IAC_REPO` to the name of your infrastructure repository and paste the PAT when asked to paste your secret.

=== "CLI"

Run these commands and paste the PAT from the previous section of the guide when prompted.

    ```sh
    IAC_REPO="oslokommune/pirates-iac"
    gh secret set --repo "$IAC_REPO" PAT_ON_MACHINE_USER_FOR_IMAGE_UPDATE
    ```

    ```txt title="Example output"
    ? Paste your secret ***
    ✓ Set Actions secret PAT_ON_MACHINE_USER_FOR_IMAGE_UPDATE for oslokommune/pirates-iac
    ```

=== "GUI"

- Go to your infrastructure repository and navigate to **Settings** > **Secrets and variables** > **Actions** > **Repository secrets**. Click on **New repository secret**.


    **Name**

:   `PAT_ON_MACHINE_USER_FOR_IMAGE_UPDATE`

    **Value**

- :   The value of the PAT that you previously added to your team's 1Password vault (for example `github_pat_R2eH8G6iO3qV7jK1bW0zN4pL`).

Click on **Add secret**.

- !!! question "Why is this a repository secret?" You don't need to use an environment for this secret because it's the same value for all environments.

## Next step

[Create a GPG key](create-gpg-key.md) for the GitHub machine user.


---


## setup/ci-cd/deploy-image/add-an-environment-to-the-infrastructure-repository.md

- This section guides you through setting up the GitHub environment used to deploy the container image to AWS.

- This must be done to be aligned with the IAM permissions created after enabling `IamForCicd` during [setup of IAM roles](../push-image/create-iam-roles-for-pushing-the-image-to-ecr.md)

- !!! tip "What is a GitHub environment?" [GitHub environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment) store secrets unique to the environment. It also allows you to define deployment protection rules, such as requiring a manual approval before deployment.

## Step 1: Create environment

- Go to your GitHub infrastructure repository and navigate to **Settings** > **Environments** and click on **New environment**.

<!-- markdownlint-disable-next-line MD036 -->
**Name**

:   `<Environment>-<AppName>-cicd` (for example `pirates-dev-app-too-tikki-cicd`)

## Next step

- [Add a GitHub workflow](add-a-workflow-for-running-terraform.md) file to the infrastructure repository.


---


## setup/ci-cd/deploy-image/add-iam-secrets-to-the-infrastructure-repository.md

- This section shows you how to set up the IAM role ARN as a secret in the GitHub environment you created earlier.

## Step 1: Add the secret

```bash title="repo-iac/environments/dev/app-too-tikki"
cd bin
./set_role_secret_in_iac_repo.sh
```

## Step 2: Verify that the workflow can run Terraform

- Make a change to the Terraform code for your application in the infrastructure repository, and push it to the `main` branch. The workflow should now run and apply the changes to your infrastructure.

For example, change a override by editing the file `app-too-tikki/config_override.tf`.


---


## setup/ci-cd/dispatch-image-tag/notifying-the-infrastructure-repository-of-updated-images.md

- This section describes how to notify your infrastructure repository about an updated container image from the application repository.

- Given this configuration, you should achieve the following outcome in the workflow file after completing this page:

- | Configuration                        |                                                        | |--------------------------------------|--------------------------------------------------------| | Environment                          | `pirates-dev`                                          | | IacGitHubRepo                        | `pirates-iac`                                          | | IacGitHubOrg                         | `oslokommune`                                          | | **Outcome** in jobs.dispatch.steps   |                                                        | | with.repository                      | `oslokommune/pirates-iac`                              | | with.event_type                      | `pirates-dev-too-tikki-image-tag-update`               | | env.RECEIVER_WORKFLOW                | `_gp_too-tikki_pirates-dev_receive_dispatch_event.yml` |

## Step 1: Enable dispatch

- To enable dispatch, add the following lines to the `too-tikki_docker-build-push.yml` configuration file in the application repository.

```diff title="repo-apps/.github/workflows/_config/dev/too-tikki_docker-build-push.yml"
AppName: too-tikki
+ PostBuildPushAction:
+  RepositoryDispatch:
+    Enable: true
+    IacGitHubOrg: "oslokommune"
+    IacGitHubRepo: "pirates-iac"
```

The `Enable` flag is used to enable the dispatch event.

- The `IacGitHubRepo` is the name of the repository where the dispatch event will be sent, this must be within the organization configured by `IacGitHubOrg`.

## Step 2: Update the `docker-build-push` package

Run the following command to update the package:

```bash title="repo-apps/.github/workflows/_config/dev"
ok pkg install
```

## Step 3: Verify the outcome

- The workflow file `.github/workflows/_gp_too-tikki_pirates-dev_build_and_push_image.yml` should now have a `jobs.dispatch` job that sends an event to the infrastructure repository.

- The outcomes as listed in the above table should be present in the `jobs.dispatch.steps` section of the workflow file.

- The values of `event_type` and `RECEIVER_WORKFLOW` will be used in the receiving infrastructure repository to target the correct workflow.

--8<-- "includes/commit.md"

## Step 4: Try to run the workflow

- Try running the workflow. It will fail because the workflow tries to send a "dispatch event" to your infrastructure repository without the proper authentication. To resolve this, you need to set up a Personal Access Token (PAT).

## Next step

[Create a Personal Access Token](create-pat-for-sending-dispatch-events.md).


---


## setup/infrastructure/github-repository.md

# Create a new GitHub repository

GitHub is used to host the Terraform code for your infrastructure.

- !!! tip "Naming convention" A good naming convention is to use the name of your team along with `-iac`, for example `barnehageplass-iac`.

- !!! tip "Give Team Kjøremiljø read access to your repository" To better help out your team in case of need, Team Kjøremiljø would like read access to your infrastructure repository. This can be achieved two ways: By setting the privacy of the repository to "Internal", or by granting read access for the repository to [the `kjoremiljo` team in GitHub](https://github.com/orgs/oslokommune/teams/kjoremiljo){:target=\"_blank\"}.

- Create a new empty repository for your team (see [how to create a new repository](https://docs.github.com/en/get-started/quickstart/create-a-repo){:target=\"_blank\"}).

- Checkout the repository locally on your machine (see [how to clone a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository){:target=\"_blank\"}).

Initialize with a `.gitignore` file to avoid checking in Terraform cache files etc:

```gitignore title=".gitignore"
.DS_Store

**/.terraform/*
**.tfstate
*.tfstate.*
```

## Next step

- [Initialize environment](initialize-environment.md) to create configuration files for your first environment.


---


## setup/infrastructure/initialize-environment.md

## Step 1: Create environment directory

Navigate to the directory where you checked out the repository:

   ```bash
   # Replace <~/projects/repo-iac> with your repository location
   cd ~/projects/repo-iac
   ```

Create a directory for environments (it will contain `dev`, `qa`, `prod`, etc.):

   ```bash title="repo-iac/"
   mkdir environments
   cd environments/
   ```

Create a directory for your first environment (using `dev` as example):

   ```bash title="repo-iac/environments"
   mkdir dev
   cd dev/
   ```

## Step 2: Create configuration file

Create `common-config.yml` in the `dev/` directory:

```yaml title="repo-iac/environments/dev/common-config.yml"
AccountId: "1234567890"
Region: "eu-west-1"
Team: "pirates"
Environment: "pirates-dev"
```

- | Parameter       | Description                                                                                                                                                                                                                                                       | Validation               | |-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------------------ | | `AccountId`     | AWS account ID where the environment will be created. [How do I find my account ID?](../../guides/find-aws-account-id.md).                                                                                                                                    |                          | | `Region`        | AWS region where the environment will be created. Typically: `eu-west-1`.                                                                                                                                                                                     |                          | | `Team`          | Team name. Used as part of AWS resource names.                                                                                                                                                                                           | Alpha-numeric and dashes | | `Environment`   | Environment name. Used as part of AWS resource names, for example the S3 bucket created to store the `remote_state`. **Note**: Recommended to contain the environment (dev/prod/staging). | Alpha-numeric and dashes |

This file will be used for all templates in the **dev** stack.

## Next step

- Set up [remote state](setup-remote-state.md) to create the S3 bucket and DynamoDB table for storing Terraform state remotely.


---


## setup/infrastructure/setup-application-common.md

# Application Common

All applications share a common set of infrastructure components that are set up in this guide.

- The stack will set up an ECS cluster for the current `Environment` and a rule for fetching public images through the ECR repository.

## Step 1: Add and configure the `app-common` package

```bash title="repo-iac/environments/dev/"
ok pkg add app-common
cd app-common
```

Update `package-config.yml` with your preferences.

## Step 2: Install the package

```bash title="repo-iac/environments/dev/app-common/"
ok pkg install
```

## Step 3: Initialize and apply the `app-common` stack

```bash title="repo-iac/environments/dev/app-common/"
terraform init
terraform apply
```

## Step 4: Perform initial pull for ECR

!!! info "What's this?" If you previously pulled the following image:

    ```hcl
    public.ecr.aws/nginx/nginx:latest
    ```

You can now pull the image via the ECR pull through cache address:

    ```hcl
    ${var.account_id}.dkr.ecr.${var.region}.amazonaws.com/${var.environment}-ecr-public/nginx/nginx:latest
    ```

In other words, the original upstream registry URL:

    ```
    public.ecr.aws/
    ```

Is replaced with:

    ```
    ${var.account_id}.dkr.ecr.${var.region}.amazonaws.com/${var.environment}-ecr-public/
    ```

ECR pull through cache is enabled by default, but can be configured with the following:

```yaml title="repo-iac/environments/dev/app-common/package-config.yml"
EcrPullThroughCache:
  Enable: true
```

- Each image will get a separate ECR repository and needs a unique lifecycle policy, specify the upstream images you need:

```hcl title="repo-iac/environments/dev/app-common/config_override.tf"
pull_through_cache_repositories = [
  "aws-observability/aws-otel-collector",
  "nginx/nginx-prometheus-exporter",
  "nginx/nginx"
]
pull_through_cache_ecr_max_image_count = 15
```

Then run the following to populate ECR with the latest version of `nginx/nginx`:

```bash title="repo-iac/environments/dev/app-common/bin"
bash _gp_ecr_pull_through_cache_init.sh -i nginx/nginx
```

If a specific tag is required, use the `-t` flag:

```bash title="repo-iac/environments/dev/app-common/bin"
bash _gp_ecr_pull_through_cache_init.sh -i nginx/nginx -t alpine-slim
```

Repeat for each image in the list defined previously in `config_override.tf`.

Subsequent pulls will not require access to the internet

## Step 5: Verify

=== "AWS CLI"

To verify that a new ECS cluster has been created, run the following command:

    ```bash
    aws ecs list-clusters | jq '.clusterArns'
    ```

The output list should contain the name of the ECS cluster you just created.

=== "AWS console"

Login to the AWS console and navigate to **ECS**.

The list should contain the name of the ECS cluster you just created.

---

--8<-- "includes/commit.md"

## Next step

Set up an [application](../application/create-a-new-stack-for-your-application.md).


---


## setup/infrastructure/setup-certificates.md

![This guide is optional](../../images/tags/optional-tag.svg){ align=left width=150} <br> <br>

Certificates for each application are created within its corresponding application stack.

- If you need additional certifications you can create them by setting up a separate certificates stack.

## Step 1: Add and configure the `scaffold` package

```bash title="repo-iac/environments/dev/"
ok pkg add scaffold certificates
cd certificates
```

Update `package-config.yml` with your preferences.

## Step 2: Install the package

```bash title="repo-iac/environments/dev/certificates/"
ok pkg install
```

## Step 3: Initialize and apply the `certificates` stack

```bash title="repo-iac/environments/dev/certificates/"
terraform init
terraform apply
```

This will not create any resources since we are scaffolding a empty stack.

## Step 4: Add custom certificate

- Depending on your needs you can create one or more certificates. The following example creates a certificate for `km-dev.oslo.systems`.

```bash title="repo-iac/environments/dev/certificates/km-dev-certificate.tf"
module "acm_certificate_km" {
  # https://github.com/terraform-aws-modules/terraform-aws-acm
  source  = "terraform-aws-modules/acm/aws"
  version = "5.0.1"

  create_certificate = true

  domain_name = "km-dev.oslo.systems"
  zone_id     = data.aws_route53_zone.km.zone_id

  validation_method   = "DNS"
  wait_for_validation = true
}

data "aws_route53_zone" "km" {
  name = "km-dev.oslo.systems"
}
```

## Step 5: Verify

=== "AWS CLI"

Run the following command:

    ```bash
    aws acm list-certificates | jq '.CertificateSummaryList[].DomainName'
    ```

The output list should contain `km-dev.oslo.systems`.

=== "AWS console"

- Login to the AWS console and navigate to **Certficate Manager**. Select **List certificates** in the left-hand menu.

The list should contain `km-dev.oslo.systems`

---

--8<-- "includes/commit.md"

## Next step

Set up [load balancing](setup-load-balancing.md).


---


## setup/infrastructure/setup-databases.md

All applications in an environment share a common database cluster.

- The database cluster set up for your environment is `{Environment}-main`, and the default database is `{Environment}-main-one`.

## Step 1: Add and configure the `databases` package

```bash title="repo-iac/environments/dev/"
ok pkg add databases
cd databases
```

- Update `package-config.yml` with your preferences. Enabling `Serverless` creates a Serverless database cluster. To create a traditional database cluster, set `Enable` to `false`.

## Step 2: Install the package

```bash title="repo-iac/environments/dev/databases/"
ok pkg install
```

## Step 3: Initialize and apply the `databases` stack

```bash title="repo-iac/environments/dev/databases/"
terraform init
terraform apply
```

## Step 4: Verify

=== "AWS CLI"

Run the following command:

    ```bash
    aws rds describe-db-instances | jq '.DBInstances[].DBInstanceIdentifier'
    ```

The output list should contain the name of the VPC you just created.

=== "AWS console"

Login to the AWS console and navigate to **RDS**. Select **Databases** in the left-hand menu.

The list should contain the name of the database cluster you just created.

---

--8<-- "includes/commit.md"

## Next step

Set up [certificates](setup-certificates.md).


---


## setup/infrastructure/setup-dns.md

All applications in a environment will be deployed to a subdomain of `oslo.systems`.

- The default domain for your environment is `{Environment}.oslo.systems`. Each new application will use a subdomain of this domain.

## Step 1: Add and configure the `dns` package

```bash title="repo-iac/environments/dev/"
ok pkg add dns
cd dns
```

## Step 2: Install and apply the package

```bash title="dns/"
ok pkg install
terraform init
terraform apply
```

Once `terraform apply` completes, name servers will be printed to the console.

```hcl title="Output from terraform apply"
name_servers = tolist([
  "ns-123.awsdns-44.org",
  "ns-321.awsdns-29.co.uk",
  "ns-213.awsdns-35.com",
  "ns-231.awsdns-18.net",
])
```

## Step 3: Verify

=== "AWS CLI"

    ```bash
    aws route53 list-hosted-zones | jq '.HostedZones[].Name'
    ```

Output should contain the domain you created.

=== "AWS console"

Login to **AWS console** and navigate to **Route 53**. Select **Hosted zones**.

List should contain the domain you created.

---

## Step 4: Add DNS Name Servers

- The output from Step 2 are the name servers for the root domain specified in `_gp_dns.tf`. Because `oslo.systems` was specified as the root domain, follow the guide [Adding a subdomain to `oslo.systems`](https://github.com/oslokommune/origo-aws-infrastructure/tree/master/infrastructure/production/dns/oslo.systems/auto_applied_subdomains#readme){:target=\"_blank\"} to complete the setup.

To override default configuration, set the `root_domain` variable in `dns/config_override.tf`.

The domain `pirates-dev.oslo.systems` should now resolve to applications you deploy.

## Step 5: Verify

To verify the subdomain is properly registered with a name server (after completing step 4):

```bash
dig NS +short {Environment}.oslo.systems
```

This should return name servers corresponding to the list printed after `terraform apply` in step 2.

- If you don't have `dig` installed, use [this DNS lookup tool](https://dns-lookup.jvns.ca/#|NS){:target=\"_blank\"} to check `{your-subdomain}.oslo.systems`.

## Next step

Set up [networking](setup-networking.md).


---


## setup/infrastructure/setup-iam.md

![This guide is optional](../../images/tags/optional-tag.svg){ align=left width=150} <br> <br>

- IAM setup is only applicable for environments that require either OIDC authentication for CI/CD or for applications that have Maskinporten integration.

## Step 1: Add and configure the `iam` package

```bash title="repo-iac/environments/dev/"
ok pkg add iam
cd iam
```

Update `package-config.yml` and enable the components you need:

```yaml title="iam/package-config.yml"
StackName: "iam"
MaskinportenKeyRotation:
  Enable: false
GithubIdentityProvider:
  Enable: false
```

- !!! Warning "Only one per account" You can only have one **GithubIdentityProvider** or **MaskinportenKeyRotation** enabled per account. If already enabled in a different environment, you cannot enable it here.

Enabling it will cause an error when applying the stack.

## Step 2: Install and apply the package

```bash title="iam/"
ok pkg install
terraform init
terraform apply
```

## Step 3: Verify

=== "AWS CLI"

### OIDC

To verify **OIDC** is correctly set up:

    ```bash
    aws iam list-open-id-connect-providers | jq '.OpenIDConnectProviderList[].Arn'
    ```

Output should contain a provider with `token.actions.githubusercontent.com` in the ARN.

### Maskinporten

To verify **Maskinporten** role is set up:

    ```bash
    aws iam list-roles | jq '.Roles[].RoleName' | grep dataplatform-maskinporten
    ```
Output should contain role `dataplatform-maskinporten`.

=== "AWS console"

### OIDC

Login to **AWS console** and navigate to **IAM**. Select **Identity Providers**.

List should contain provider `token.actions.githubusercontent.com`.

### Maskinporten

In **IAM**, select **Roles** and search for `dataplatform-maskinporten`.

List should contain role `dataplatform-maskinporten`.

---

## Next step

Set up [application common](setup-application-common.md).


---


## setup/infrastructure/setup-load-balancing.md

- To have an application accessible from the internet you need a load balancer that can route traffic to the application.

The load balancer set up for your environment is `{Environment}-public`.

## Step 1: Add and configure the `load-balancing` package

```bash title="repo-iac/environments/dev/"
ok pkg add load-balancing-alb load-balancing-alb-main
cd load-balancing-alb-main
```

- We chose `main` here because we have just one load balancer. If you have multiple load balancers, you can replace `main` with something more descriptive (for instance "payments", "catalog", "orders").

- Update `package-config.yml` with your preferences. The `Name` field should be `main` (or whatever you chose above) to avoid confusion:

```yaml title="repo-iac/environments/dev/load-balancing-alb-main/package-config.yml"
# ...
Name: "main"
# ...
```

## Step 2: Install the package

```bash title="repo-iac/environments/dev/load-balancing-alb-main/"
ok pkg install
```

## Step 3: Initialize and apply the `load-balancing` stacks

ALB are separated into two stacks when creating them.

- The first stack is the data stack, which contains data-related resources, this must be applied first.

The second stack is the alb stack, which contains the load balancing set up, route53, etc.

```bash title="repo-iac/environments/dev/load-balancing-alb-main-data/"
terraform init
terraform apply
```

```bash title="repo-iac/environments/dev/load-balancing-alb-main/"
terraform init
terraform apply
```

## Step 4: Verify

=== "AWS CLI"

Run the following command:

    ```bash
    aws elbv2 describe-load-balancers | jq '.LoadBalancers[].LoadBalancerName'
    ```

The output list should contain the name of the load balancer you just created.

=== "AWS console"

Login to the AWS console and navigate to **EC2**. Select **Load Balancers** in the left-hand menu.

The list should contain the name of the load balancer you just created.

---

## Next step

Set up [IAM](setup-iam.md).


---


## setup/infrastructure/setup-networking.md

All applications in an environment share a common network (VPC).

The default VPC for your environment set up by this guide is: `{Environment}`

## Step 1: Add and configure the `networking` package

```bash title="repo-iac/environments/dev/"
ok pkg add networking
cd networking
```

Update `package-config.yml` with your preferences.

## Step 2: Install the package

```bash title="repo-iac/environments/dev/networking/"
ok pkg install
```

## Step 3: Configure CIDR range

- Each VPC must have a unique CIDR range within the Origo AWS organization. You must claim a range and document this in the [Google doc](https://docs.google.com/spreadsheets/d/1Ly-gVkakvZ2ZtcS3aDb0E2ZYOMEFUb6fE3Ma7mVsVKI/edit?gid=0#gid=0) created for this purpose.

Once a range have been claimed: edit `config_override.tf` and set the CIDR range chosen:

```hcl title="repo-iac/environments/dev/networking/config_override.tf"
vpc_cidr_block = "{value-chosen}"
```

- !!! note "Release CIDR block" The CIDR block must be released (removed from the Google doc) once the VPC is no longer in use.

## Step 4: Initialize and apply the `networking` stack

```bash title="repo-iac/environments/dev/networking/"
terraform init
terraform apply
```

## Step 4: Verify

=== "AWS CLI"

Run the following command:

    ```bash
    aws ec2 describe-vpcs | jq '.Vpcs[].Tags[] | select(.Key == "Name") | .Value'
    ```

The output list should contain the name of the VPC you just created.

=== "AWS console"

Login to the AWS console and navigate to **VPC**. Select **Your VPCs** in the left-hand menu.

The list should contain the name of the VPC you just created.

---

--8<-- "includes/commit.md"

## Next step

Set up [databases](setup-databases.md).


---


## setup/infrastructure/setup-remote-state.md

# Remote state

Now that we have created the environment definition file, we can bootstrap the environment.

- Terraform state is a file that contains information about the resources that Terraform has created. By default, this file is stored locally on the machine it is run from. The bootstrap command will create the necessary S3 bucket and DynamoDB table that will instead be used to store Terraform state remotely.

- After these steps, you will have a foundation for all the other stacks you create inside this environment.

## Step 1: Add and configure the `remote-state` package

```bash title="repo-iac/environments/dev/"
ok pkg add remote-state
cd remote-state
```

In `package-config.yml`, set `S3Backend` to `false`:

```yaml title="repo-iac/environments/dev/remote-state/package-config.yml"
StackName: "remote-state"

S3Backend: false
```

## Step 2: Install the package

```bash title="repo-iac/environments/dev/remote-state/"
ok pkg install
```

## Step 3: Initialize and apply the `remote-state` stack

- Now you need to tell Terraform to initialize this stack and apply it, to create the S3 bucket and DynamoDB table:

- !!! note "SSH Key" If you haven't already added a SSH key to your GitHub account (or have `gh`(GitHub CLI) configured). See [GitHub SSH key guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account){:target=\"_blank\"} for more information. This is required for Terraform to be able to fetch the modules from the `golden-path-iac` repository.

```bash title="repo-iac/environments/dev/remote-state/"
terraform init
terraform apply
```

## Step 4: Verify

Verify that the S3 bucket for storing remote Terraform state was created.

You are looking for a bucket with the following name:

``` bash
ok-iac-config-${local.account_id}-${local.region}-${local.environment}
```

For example:

```bash
2021-09-01 10:00:00 ok-iac-config-12345678910-eu-west-1-my-team-dev
```

=== "AWS CLI"

Run the following command:

      ```bash
      aws s3 ls
      ```

The list should contain the name of the S3 bucket you just created.

=== "AWS console"

Login to the AWS console and navigate to S3.

The list should contain the name of the S3 bucket you just created.

---

## Step 5: Move your current local Terraform state to the S3 backend

- You now have a place to store Terraform state for all your future stacks. However, the stack you're currently working on is already using a local state file (`terraform.tfstate`).

- The next step is to transfer this local state file to the S3 bucket you just set up. This is done by reconfiguring Terraform to use the S3 bucket as the backend.

Edit `package-config.yml` and set `S3Backend` to `true`:

```yaml title="repo-iac/environments/dev/remote-state/package-config.yml"
StackName: "remote-state"

S3Backend: true
```

Reinstall the package:

```bash title="repo-iac/environments/dev/remote-state/"
ok pkg install
```

Initialize the new configuration:

```bash title="repo-iac/environments/dev/remote-state/"
terraform init -migrate-state -force-copy
```

- Verify that everything is working by running `terraform plan`. There should not be any changes to apply at this point:

```bash title="repo-iac/environments/dev/remote-state"
terraform plan
```

- You can now delete `terraform.tfstate` since it's stored in the S3 bucket instead. This is done so that the next time Terraform is run, it's updating the correct file instead of adding a new local file.

```bash title="repo-iac/environments/dev/remote_state"
rm "terraform.tfstate" && \
rm "terraform.tfstate.backup"
```

--8<-- "includes/commit.md"

## Next step

Set up [DNS](setup-dns.md).


---
