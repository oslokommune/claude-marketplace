# Application Setup

**Source files**: 5


## setup/application/ci-cd/ci-cd-slack.md

# Slack notifications

- The [official Slack integration supports workflow notifications](https://github.com/integrations/slack#actions-workflow-notifications){:target=\"_blank\"}.

Subscribe to a workflow with the `subscribe` command:

```sh
/github subscribe oslokommune/pirates-iac workflows:{name:"Run Terraform on changed directories"}
```

Quiet the spam by unsubscribing to some events by using the `unsubscribe` command:

```sh
/github unsubscribe oslokommune/pirates-iac issues pulls commits releases deployments
```


---


## setup/application/create-a-new-stack-for-your-application.md

# Application

Given this configuration, you should achieve the following outcome after completing this page:

- | Configuration |                                               | |---------------|-----------------------------------------------| | Environment   | `pirates-dev`                                 | | AppName       | `too-tikki`                                   | | **Outcome**   |                                               | | ECR           | `pirates-dev-too-tikki`                       | | URL           | `https://too-tikki.pirates-dev.oslo.systems/` |

## Step 1: Add and configure the `app` package

```bash title="repo-iac/environments/dev/"
ok pkg add app app-too-tikki
cd app-too-tikki
```

- Update `package-config.yml` to enable the components you need. You can use the following configuration to set up a minimal application running on **nginx** with an internet-facing address:

```yaml title="repo-iac/environments/dev/app-too-tikki/package-config.yml"
# Attribute reference:
# https://github.com/oslokommune/golden-path-boilerplate/blob/main/boilerplate/terraform/app/boilerplate.yml
StackName: "app-too-tikki"
app-data.StackName: "app-too-tikki-data"

AppName: "too-tikki"
AppEcsExec: false
AppReadOnlyRootFileSystem: false

ExampleImage:
  Enable: true
Ecr:
  Enable: false
ServiceConnect:
  Enable: false
AlbHostRouting:
  Enable: true
  Internal: false
  Subdomain:
    Enable: true
    TargetGroupTargetStickiness: false
DatabaseConnectivity:
  Enable: false
DailyShutdown:
  Enable: false
IamForCicd:
  Enable: false
TelemetryCollection:
  Enable: false
```

## Step 2: Install the package

```bash title="repo-iac/environments/dev/app-too-tikki/"
ok pkg install
```

## Step 3: Initialize and apply the `app` stacks

Applications are separated into two stacks when creating them.

- The first stack is the data stack, which contains ECR and data-related resources, this must be applied first.

- The second stack is the application stack, which contains the load balancing set up, ECS service, security groups and more for your application.

```bash title="repo-iac/environments/dev/app-too-tikki-data/"
terraform init
terraform apply
```

```bash title="repo-iac/environments/dev/app-too-tikki/"
terraform init
terraform apply
```

## Step 4: Verify

### Verify in the AWS CLI

To verify that ECR is correctly set up, run the following command:

```bash
aws ecr describe-repositories | jq '.repositories[].repositoryName'
```

The output list should contain the name of the ECR repository.

### Verify in the AWS console

Login to the AWS console and navigate to **ECR**. Select **Repositories** in the left-hand menu.

The list should contain the name of the ECR repository.

### Verify in the browser

- Go to [`https://too-tikki.pirates-dev.oslo.systems/`](https://too-tikki.pirates-dev.oslo.systems/) and you should see the default Nginx page. Change URL according to your environment and application name.

--8<-- "includes/commit.md"

- <figure markdown> <img src="../../../docs/images/otter/party-otter.svg" width="450" alt="Otter celebrating with balloons" /> </figure>


---


## setup/ci-cd/dispatch-image-tag/add-pat-as-a-secret-to-the-application-repository.md

- This section shows you how to set up the PAT you just created as a secret in the application repository.

## Step 1: Add the secret

- Change `APP_REPO` to the name of your application repository and paste the PAT when asked to paste your secret.

=== "CLI"

    ```sh
    export APP_REPO="oslokommune/pirates-apps"
    gh secret set --repo "$APP_REPO" PAT_ON_MACHINE_USER_FOR_IAC_DISPATCH
    ```

    ```txt title="Example output"
    ? Paste your secret ***
    ✓ Set Actions secret PAT_ON_MACHINE_USER_FOR_IAC_DISPATCH for oslokommune/pirates-apps
    ```

=== "GUI"

- Go to your application repository and navigate to **Settings** > **Secrets and variables** > **Actions** > **Repository secrets**. Click on **New repository secret**.

    **Name**

:   `PAT_ON_MACHINE_USER_FOR_IAC_DISPATCH`

    **Value**

- :   The value of the personal access token you created previously (for example `github_pat_R2eH8G6iO3qV7jK1bW0zN4pL`)

Click on **Add secret**.

- !!! question "Why is this a repository secret?" You don't need to use an environment for this secret because it's the same value for all environments.

## Step 2: Verify

- Try to run the `_gp_too-tikki_pirates-dev_build_and_push_image.yml` workflow. It should now run without any errors. This means the workflow has successfully sent an event to your infrastructure repository.

## Next step

Bump the [image tag](../bump-image/index.md) in Terraform.


---


## setup/ci-cd/push-image/add-an-environment-to-the-application-repository.md

- This must be done to be aligned with the IAM permissions created after enabling `IamForCicd` during [setup of IAM roles](create-iam-roles-for-pushing-the-image-to-ecr.md)

- !!! tip "What is a GitHub environment?" [GitHub environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment) store secrets unique to the environment. It also allows you to define deployment protection rules, such as requiring a manual approval before deployment.

## Step 1: Create environment

- Go to your GitHub application repository and navigate to **Settings** > **Environments** and click on **New environment**.

<!-- markdownlint-disable-next-line MD036 -->
**Name**

:   `<Environment>-<AppName>-ecr` (for example `pirates-dev-app-too-tikki-ecr`)

## Next step

- Add a [GitHub workflow](building-container-images-with-docker.md) file to the application repository.


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
