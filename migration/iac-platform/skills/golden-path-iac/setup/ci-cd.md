# CI/CD Setup

**Source files**: 21


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


## setup/ci-cd/bump-image/add-a-workflow-for-bumping-the-image-tag.md

- Set up a workflow that listens for events from your application repository. When it receives an event, it commits the new image tag to the infrastructure repository.

## Step 1: Update configuration

- Set `ExampleImage` to `false` in the configuration file to deploy a custom Docker image instead of the example image.

```diff title="repo-iac/environments/dev/app-too-tikki/package-config.yml"
ExampleImage:
- Enable: true
+ Enable: false
```

Update code:

```bash title="repo-iac/environments/dev/app-too-tikki/"
ok pkg install
```

## Step 2: Create metadata file

- Create a metadata file to store the image tag and digest. Add it to the `app-too-tikki` directory of your IaC repository.

The initial values aren't important—we'll update them automatically.

```json title="repo-iac/environments/dev/app-too-tikki/__gp_config_app_image.auto.tfvars.json"
{
  "main_container_image_digest": "sha256:2eb61545144b6c60eae0a7ae6d622cdd3bb205124f0054cbc3ad799516b67c1a",
  "main_container_image_tag": "sha-cbd6a43f973802a3dc60ed55ecf43f8a817bdd54"
}
```

## Step 3: Create configuration file

- Create a configuration file for the receive-dispatch workflow in the `repo-iac/.github/workflows/_config/dev/` folder:

```bash title="repo-iac/.github/workflows/_config/dev/"
ok pkg add receive-dispatch-event too-tikki_receive-dispatch-event
```

## Step 4: Update configuration file

Update the receive-dispatch-event workflow configuration:

```yaml title="repo-iac/.github/workflows/_config/dev/too-tikki_receive-dispatch-event.yml"
AppName: "too-tikki"
CreatePr: true
GpgSign: true
WorkingDirectory: "environments/dev/app-{{ .AppName }}"
ImageMetadataFile: "__gp_config_app_image.auto.tfvars.json"
```

## Step 5: Install package

```bash title="repo-iac/.github/workflows/_config/dev"
ok pkg install ../..
```

## Step 6: Verify

- Check that the IaC repository contains the new workflow file at `repo-iac/.github/workflows/_gp_too-tikki_pirates-dev_receive_dispatch_event.yml`.

- The outcome values from [configure the workflow](../dispatch-image-tag/notifying-the-infrastructure-repository-of-updated-images.md) should appear in the new workflow file.

--8<-- "includes/commit.md"

## Step 7: Test the workflow

- Build a new image to run the workflow chain. The receiving workflow will fail because you haven't configured a PAT and GPG key yet. The next section covers this.

## Next step

- [Add PAT as a secret](add-pat-as-a-secret-to-the-infrastructure-repository.md) to the infrastructure repository.


---


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


## setup/ci-cd/bump-image/create-gpg-key.md

- This section guides you through creating a GPG key for the GitHub machine user that it will use to sign commits in the GitHub Actions workflows.

## Step 1: Create a passphrase

Create a strong passphrase for the GPG key and add it to your team's 1Password vault.

## Step 2: Install

Install GnuPG:

```sh
brew install gnupg
```

## Step 3: Generate the GPG key

- Run the following commands and replace the values with your own. The `GITHUB_USERNAME` and `GITHUB_EMAIL` values should match the machine user's GitHub profile.

```sh
export GNUPGHOME=$(mktemp -d -t gnupg_$(date +%Y%m%d%H%M)_XXX)
export GITHUB_USERNAME="ok-pirates-bot"
export GITHUB_EMAIL="ok-pirates-bot@oslo.kommune.no"
export IAC_REPO="oslokommune/pirates-iac"
```

Run GnuPG to Generate the key. When prompted, paste in the passphrase you created earlier:

```sh
gpg --batch --gen-key <<EOF
%echo Generating a GPG key
Key-Type: RSA
Key-Length: 4096
Subkey-Type: RSA
Subkey-Length: 4096
Name-Real: $GITHUB_USERNAME
Name-Email: $GITHUB_EMAIL
Expire-Date: 0
%ask-passphrase
%commit
%echo done
EOF
```

## Step 4: Add the key and passphrase as a secret

Add the private key to the infrastructure repository as a secret:

```sh
gpg --armor --export-secret-key "$GITHUB_EMAIL" \
    | gh secret set --repo "$IAC_REPO" GPG_PRIVATE_KEY_FOR_MACHINE_USER
```

```txt title="Example output"
✓ Set Actions secret GPG_PRIVATE_KEY_FOR_MACHINE_USER for oslokommune/pirates-iac
```

Add the passphrase to the infrastructure repository as a secret:

```sh
gh secret set --repo "$IAC_REPO" GPG_PASSPHRASE_FOR_MACHINE_USER
```

```txt title="Example output"
? Paste your secret ***
✓ Set Actions secret GPG_PASSPHRASE_FOR_MACHINE_USER for oslokommune/pirates-iac
```

## Step 5: Add the public key to the GitHub account

Copy the GPG public key to the clipboard:

```sh
gpg --armor --export "$GITHUB_EMAIL" | pbcopy
```

- Follow [the official GitHub guide to add the GPG key to the machine user](https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-gpg-key-to-your-github-account).

## Step 6: Save in 1Password

Add the GPG public and private key to your team's 1Password vault:

```sh
gpg --armor --export "$GITHUB_EMAIL" | pbcopy
gpg --armor --export-secret-key "$GITHUB_EMAIL" | pbcopy
```

## Step 7: Verify

- Now that you've added both a PAT and a GPG key to the repository, you can try to trigger the chain of workflows again. It should now run without any errors and the metadata file `__gp_config_app_image.auto.tfvars.json` should be updated with the latest values from the application repository.

You can now move on to the next section to set up the Terraform workflow.

## Next step

[Deploy the image](../deploy-image/index.md) to AWS.


---


## setup/ci-cd/bump-image/index.md

# Bump the image tag

- This guide shows you how to use the metadata from the dispatch event to update the image tag in Terraform code.

- ![Bump the image tag in the infrastructure repository](ci_cd_bump_the_image_tag.png "Bump the image tag in the infrastructure repository")

## Next step

- [Add a GitHub workflow](add-a-workflow-for-bumping-the-image-tag.md) to the infrastructure repository.


---


## setup/ci-cd/deploy-image/add-a-workflow-for-running-terraform.md

- The `terraform-on-changed-dirs` workflow is a GitHub Action that triggers when changes are made within configured stacks. This workflow is used to deploy the infrastructure changes to the environment in AWS.

## Step 1: Create a new configuration file

- In the `repo-iac/.github/workflows/_config/dev/` folder, create a new configuration file for the `terraform-on-changed-dirs` workflow:

```bash
ok pkg add terraform-on-changed-dirs
```

## Step 1: Update the configuration file

Update the configuration file for the Terraform-on-changed-dirs workflow:

```bash title="repo-iac/.github/workflows/_config/dev/terraform-on-changed-dirs.yml"
FileTypes:
  - "**.tf"
  - "**.json"
StacksRootDir: "environments/dev"
Stacks:
  - name: "app-too-tikki"
    githubEnvironment: "pirates-dev-app-too-tikki-cicd"
```

* `FileTypes` defines which files you want the workflow to trigger on
* `StacksRootDir` is the root directory for your stacks in the environment
* `Stacks` is a list of stacks that you want to trigger on. Each stack has a `name` (matching the stack directory name) and a `githubEnvironment` that corresponds to the outcome when you [added a GitHub environment](./add-an-environment-to-the-infrastructure-repository.md) .

## Step 2: Install the `terraform-on-changed-dirs` package

```sh title="repo-iac/.github/workflows/_config/dev/"
ok pkg install ../..
```

## Step 3: Verify

- Verify that the workflow file `repo-iac/.github/workflows/_gp_pirates-dev_terraform_on_changed_dirs.yml` has been created.

--8<-- "includes/commit.md"

## Next step

[Create encryption keys](create-encryption-keys-with-age.md).


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


## setup/ci-cd/deploy-image/create-encryption-keys-with-age.md

<!-- markdownlint-disable MD041 -->

- The GitHub workflow uses [Age](https://age-encryption.org){:target=\"_blank\"} for encrypting the Terraform plan along with the entire Terraform working directory. It stores it as a GitHub Actions artifact and passes it between the plan and apply jobs in the workflow.

- !!! question "Why is this necessary?" Using an artifact makes it possible to have [deployment protection rules](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment#deployment-protection-rules){:target=\"_blank\"} (approvals) invoked between the plan and apply stages. Since anyone with read access to the repository can download the artifact, it's important to encrypt it.

## Step 1: Install

Install `age`:

```sh
brew install age
```

## Step 2: Generate keys

Generate an encryption key:

```sh
AGE_KEY_FILE=$(mktemp)
age-keygen > "$AGE_KEY_FILE"
```

## Step 3: Set repository secrets

Use `age` together with `gh` to set these as repository secrets:

```sh
IAC_REPO="oslokommune/pirates-iac"
```

```sh
cat "$AGE_KEY_FILE" | gh secret set --repo "$IAC_REPO" AGE_SECRET_KEY
age-keygen -y "$AGE_KEY_FILE" | gh secret set --repo "$IAC_REPO" AGE_PUBLIC_KEY
```

## Step 4: Save in 1Password

Add the keys to your team's 1Password vault:

=== "Mac"

    ```sh
    cat "$AGE_KEY_FILE" | pbcopy
    age-keygen -y "$AGE_KEY_FILE" | pbcopy
    ```

=== "Linux (X11)"

    ```sh
    cat "$AGE_KEY_FILE" | xclip -selection clipboard
    age-keygen -y "$AGE_KEY_FILE" | xclip -selection clipboard
    ```

=== "Linux (Wayland)"

    ```sh
    cat "$AGE_KEY_FILE" | wl-copy
    age-keygen -y "$AGE_KEY_FILE" | wl-copy
    ```

## Step 5: Delete the key file

Delete the key file when you're done:

```sh
rm "$AGE_KEY_FILE"
```

## Next step

[Add IAM role ARN as a secret](add-iam-secrets-to-the-infrastructure-repository.md).


---


## setup/ci-cd/deploy-image/index.md

# Deploy the image

- This guide shows you how to set up a GitHub Actions workflow that runs Terraform on changed infrastructure code.

- ![Deploy the image in the infrastructure repository](ci_cd_deploy_the_image.png "Deploy the image in the infrastructure repository")

- !!! question "Want to know more?" Go to [`oslokommune/reusable-terraform-plan-apply`](https://github.com/oslokommune/reusable-terraform-plan-apply) if you want to know how everything works under the hood.

## Next step

Begin by [setting up a GitHub environment](add-an-environment-to-the-infrastructure-repository.md).


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


## setup/ci-cd/dispatch-image-tag/create-pat-for-sending-dispatch-events.md

This section shows you how to create a Personal Access Token (PAT) in GitHub that allows it to:

- Read and write files in your infrastructure repository.
- Send a dispatch event to your infrastructure repository.

## Before you begin

You should have:

- A GitHub **machine user** ("bot account").
    - [To **create a machine user**, follow GitHub's instructions](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).

## Step 1: Create a PAT

- To create the PAT, go to the GitHub **machine user** and select **Settings** > **Developer settings** > **Personal access tokens** > **Fine-grained tokens**.

Enter these values:

<!-- markdownlint-capture --> <!-- markdownlint-disable MD036 -->
**Token name**

:   `pirates-iac-cicd` (replace `pirates-iac` with your own repository)

**Expiration**

:   Today's date plus one year.

**Description**

- :   `Used in GitHub Actions workflows to send dispatch events and update image tags in the infrastructure repository.`

**Resource owner**

:   `oslokommune`

**Repository access - only select repositories**

:   `pirates-iac` (replace with your infrastructure repository)

**Repository permissions**

:   **Contents** > **Read and write** <!-- markdownlint-restore -->

Click **Generate token**.

## Step 2: Save in 1Password

- Add the token to your team's 1Password vault, note the machine user name that was used to generate it.

- !!! question "Why should I store the token in 1Password?" You will use this PAT as a secret in both the application and infrastructure repository. GitHub only displays the key once, so putting it in 1Password makes it more convenient to fetch later.

- <!-- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-fine-grained-personal-access-token -->

## Next step

- [Add PAT as a secret to the application repository](add-pat-as-a-secret-to-the-application-repository.md).


---


## setup/ci-cd/dispatch-image-tag/index.md

# Dispatch the image tag

This guide shows how to send metadata from the application to the infrastructure repository.

![Dispatch image tag](ci_cd_dispatch_the_image_tag.png "Dispatch image tag")

## Next step

[Configure the workflow](notifying-the-infrastructure-repository-of-updated-images.md).


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


## setup/ci-cd/enable-oidc.md

# Enable OIDC

- Before you can push a container image or dispatch a image tag, an OIDC provider must be created. This provider is used when creating the IAM roles for the GitHub Actions workflows.

- You can read more about the OIDC provider in the [AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) and [GitHub](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) documentation.

## Step 1: Enable OIDC provider

- The OIDC provider is configured in the `iam` stack that was [created in a previous section](../infrastructure/setup-iam.md).

Enable the `GithubIdentityProvider`:

```diff title="repo-iac/environments/dev/_config/iam.yml"
StackName: "iam"
MaskinportenKeyRotation:
  Enable: false
GithubIdentityProvider:
- Enable: false
+ Enable: true
```

- Then follow the steps in the [setup IAM guide](../infrastructure/setup-iam.md) to fetch the IAM template, apply the stack and verify the provider.

--8<-- "includes/commit.md"

## Next step

Push [container image](push-image/index.md) to ECR.


---


## setup/ci-cd/index.md

# Continuous delivery and deployment

## Before you begin

You should have:

- An Elastic Container Registry repository that you can push container images to.
- An IAM stack in your infrastructure repository.
- A GitHub repository for your application.
- A GitHub **machine user** ("bot account").
    - [To **create a machine user**, follow GitHub's instructions](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).

- !!! question "What's a machine user?" A [machine user is a GitHub account created to automate tasks](https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts#user-accounts), such as doing work in CI/CD workflows.

## After you finish

- This setup guide will walk you through a CI/CD pipeline for a `dev` environment, repeat the steps for a `prod` environment once you have set this up.

## Next step

Create [workflow directory](workflows-directory.md).


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


## setup/ci-cd/push-image/building-container-images-with-docker.md

## Step 1: Create a new configuration file

- In the `.github/workflows/_config/dev/` folder of the `repo-apps` repository, create a new configuration file for the build-push workflow:

```bash title="repo-apps/.github/workflows/_config/dev/"

ok pkg add docker-build-push too-tikki_docker-build-push
```

## Step 2: Update the configuration file

Update the configuration file for the `docker-build-push` workflow:

```bash title="repo-apps/.github/workflows/_config/dev/too-tikki_docker-build-push.yml"
AppName: too-tikki
Dispatch:
  Enable: false
OnPushPaths:
  - "main.go"
OnPushBranches:
  - "main"
Cache:
  Enable: false
Ecr:
  Enable: true
  Login: true
  Push: true
Ghcr:
  Enable: false
DockerfilePath: Dockerfile
```

This configuration triggers the workflow when:

- **`main.go`** is updated
- Changes are pushed to the **`main` branch**
- In the **`too-tikki`** application repository

The workflow will:

- **Build** the Docker image using the `Dockerfile` in the repository root
- **Push** the image to **ECR**

## Step 2: Add Docker build secrets (optional)

**Does your Dockerfile use secrets?** Add them to your workflow configuration if you have `RUN` instructions that require authentication, such as **GitHub Packages** access.

```diff title="repo-apps/.github/workflows/_config/dev/too-tikki_docker-build-push.yml"
DockerfilePath: Dockerfile
+DockerSecrets:
+  GPR_USERNAME: "secrets.GPR_USERNAME"
+  GPR_ACCESS_TOKEN: "secrets.GPR_ACCESS_TOKEN"
```

The example configuration will generate the following secret setup in the workflow:

```yaml title="Example secrets generated"
DOCKER_SECRETS: |
  GPR_ACCESS_TOKEN=${{ secrets.GPR_ACCESS_TOKEN }}
  GPR_USERNAME=${{ secrets.GPR_USERNAME }}
```

- !!! tip "Using secrets in `RUN` instructions" Secrets in `DOCKER_SECRETS` are available as volumes. Use the `--mount` option to mount them.

    ```dockerfile title="Example"
    RUN --mount=type=secret,id=GPR_USERNAME \
        --mount=type=secret,id=GPR_ACCESS_TOKEN \
        GPR_USERNAME=$(cat /run/secrets/GPR_USERNAME) \
        GPR_ACCESS_TOKEN=$(cat /run/secrets/GPR_ACCESS_TOKEN) \
        gradle buildFatJar --no-daemon
    ```

- Ask in [`#origo-kjøremiljø-support`](https://oslokommune.slack.com/archives/CV9EGL9UG) if you need help with this.

## Step 3: Install the `docker-build-push` package

```bash title="repo-apps/.github/workflows/_config/dev"
ok pkg install ../..
```

## Step 4: Verify

- The application repository should now contain a new workflow file located at `.github/workflows/_gp_too-tikki_pirates-dev_build_and_push_image.yml`.

--8<-- "includes/commit.md"

## Step 5: Try to run the workflow

- Try to run the workflow in the application repository under **Actions** . It will fail because the workflow is not able to authenticate with AWS yet. The next section will show you how to configure this.

## Next step

- Create the [IAM roles](create-iam-roles-for-pushing-the-image-to-ecr.md) that will allow the workflow to push the image to ECR.


---


## setup/ci-cd/push-image/create-iam-roles-for-pushing-the-image-to-ecr.md

- This section shows how to update the `too-tikki` application stack to create IAM roles for authenticating to ECR from your application repository in GitHUb.

- This guide builds on [the guide for creating a new stack for your application](../../application/create-a-new-stack-for-your-application.md).

## Before you begin

You should already have an application stack in your infrastructure repository.

```bash title="repo-iac/environments/dev"
cd app-too-tikki/
terraform output
```

- Observe the output of the `terraform output` command, since `IamForCicd` is not yet enabled it should look something like this:

```bash title="Output from running terraform output"
ecr_repository_url = "1234567890.dkr.ecr.eu-west-1.amazonaws.com/pirates-dev-too-tikki"
service_url = "https://too-tikki.pirates-dev.oslo.systems"
```

## Step 1: Update configuration

- Set `Enable: true` in the configuration file for the application stack to enable the `IamForCicd` component.

- Update `AppGithubRepo` and `IacGitHubRepo` to match your setup, these should be where your application and infrastructure repositories are located inside the `oslokommune` GitHub organization.

```diff title="repo-iac/environments/dev/app-too-tikki/package-config.yml"
IamForCicd:
+ Enable: true
  AppGitHubRepo: pirates-apps
  IacGitHubRepo: pirates-iac
```

## Step 2: Update the application stack

Re-configure the application stack to include the IAM roles:

```bash title="repo-iac/environments/dev/app-too-tikki/"
ok pkg install
```

## Step 3: Apply the stack

```bash title="repo-iac/environments/dev"
cd app-too-tikki/
terraform init
terraform apply
```

The output should now be updated with several more variables.

```bash
app_gh_env_name = "pirates-dev-app-too-tikki-ecr"
ecr_repository_url = "1234567890.dkr.ecr.eu-west-1.amazonaws.com/pirates-dev-too-tikki"
iac_gh_env_name = "pirates-dev-app-too-tikki-cicd"
iam_assumable_role_github_oidc_cicd_arn = "arn:aws:iam::1234567890:role/gh_for_repo_pirates-iac_in_env_pirates-dev-app-too-tikki-cicd"
iam_assumable_role_github_oidc_ecr_arn = "arn:aws:iam::1234567890:role/gh_for_repo_pirates-apps_in_env_pirates-dev-app-too-tikki-ecr"
service_url = "https://too-tikki.pirates-dev.oslo.systems"
```

For pushing the image to ECR there are two variables that are important:

### Environment

- The `app_gh_env_name` should match the environment created [earlier](add-an-environment-to-the-application-repository.md) and is where the GitHub Actions workflow will push the image from.

- The `iac_gh_env_name` is not relevant for pushing the image, but will be used later when [deploying the image](../deploy-image/index.md) via Terraform.

### Assumable role

- The `iam_assumable_role_github_oidc_ecr_arn` is the role that the GitHub Actions workflow will assume to push the image to ECR.

- The role will have enough rights to push to the ECR repository that was created for the application  common stack. To use the role in the GitHub Actions workflow you need to add it as a secret to the application repository.

- The `iam_assumable_role_github_oidc_cicd_arn` is not relevant for pushing the image, but will be used later when [deploying the image](../deploy-image/index.md) via Terraform.

## Step 4: Update the application repository

Set the IAM role in the application repository's environment:

```bash title="repo-iac/environments/dev/app-too-tikki"
cd bin
./set_role_secret_in_app_repo.sh
```

The environment should now be ready to push the image to ECR.

--8<-- "includes/commit.md"

## Step 5: Try to run the workflow

Try to run the workflow in the application repository under **Actions**.


---


## setup/ci-cd/push-image/index.md

# Push a container image

- This guide shows you how to build and push a container image to ECR from an application repository using GitHub Actions.

- ![Pushing a container image to ECR](ci_cd_push_a_container_image.png "Pushing a container image to ECR")

## Next step

Add a [GitHub environment](add-an-environment-to-the-application-repository.md).


---


## setup/ci-cd/workflows-directory.md

- All CI/CD workflows are stored in the `.github/workflows` directory in the root of your application and IaC repositories.

- The default Golden Path setup assumes a structure where an application is built and pushed to both `dev` and `prod` environments via a single IaC repository.

## Step 1: Create a configuration folder for dev environment

- To separate `dev` and `prod` workflow configuration, we recommend creating a subdirectory for each environment.

For both infrastructure and application repository, create a `_config/dev` directory:

```bash title="repo-iac/"
mkdir -p .github/workflows/_config/dev
```

```bash title="repo-app/"
mkdir -p .github/workflows/_config/dev
```

- Note: All workflow files from Boilerplate templates will be generated in the root of the `workflows` directory. The `_config/dev/` directory is used to store configuration files for the environment.

## Step 2: Create a common configuration file

- For both infrastructure and application repository, create a common configuration file, change values according to the environment

```bash title="repo-iac/.github/workflows/_config/dev/common-config.yml"
AccountId: "1234567890"
Region: "eu-west-1"
Team: "pirates"
Environment: "pirates-dev"
```

```bash title="repo-app/.github/workflows/_config/dev/common-config.yml"
AccountId: "1234567890"
Region: "eu-west-1"
Team: "pirates"
Environment: "pirates-dev"
```

## Step 3: Create a packages.yml file

- For both infrastructure and application repository, create a `packages.yml` file in the `_config/dev` directory.

```bash title="repo-iac/.github/workflows/_config/dev/packages.yml"
DefaultPackagePathPrefix: "boilerplate/github-actions"

```

```bash title="repo-app/.github/workflows/_config/dev/packages.yml"
DefaultPackagePathPrefix: "boilerplate/github-actions"

```

- `DefaultPackagePathPrefix`: this path is used by the `ok` tool to locate the GitHub Actions packages.

--8<-- "includes/commit.md"

## Next step

Enable [OIDC](enable-oidc.md).


---
