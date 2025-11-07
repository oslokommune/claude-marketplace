# Prerequisites and Tools

**Source files**: 12


## setup/before-you-start/aws-account.md

# AWS account

- You will need an AWS account to be able to deploy the infrastructure. If you need a new AWS account, contact Kjøremiljø to set it up for you. You will need to be added to the AWS IAM Identity Center user group by Team Kjøremiljø for the AWS account you need access to.

- Once you have an account, check out the [Access to AWS](../../guides/access-to-aws.md) guide for instructions on how to configure browser-based and command-line access to AWS.


---


## setup/before-you-start/index.md



# Before you start

The Setup section will have all you  need to set up your infrastructure.

- We recommend starting by installing all the required [tools](tools/index.md), checking that you have access to an [AWS account](./aws-account.md), and configuring [CLI access to the account](../../guides/access-to-aws.md).

- !!! note "AWS Usage in Origo" It is important that you have read and understood the [RFC-0005 _Bruk av AWS i Origo_](https://github.com/oslokommune/rfc/tree/main/0005-bruk-av-aws) (AWS usage in Origo) document before you start setting up your infrastructure. This RFC describes the regulations for protecting user data to avoid the transfer of personal data to 3rd party countries in accordance with GDPR.

Thereafter we will guide you through building your infrastructure and application.

## Meet `too-tikki` and `pirates-iac`

- The reference implementation of the Golden Path is [`pirates-iac`](https://github.com/oslokommune/pirates-iac/tree/main){:target=\"_blank\"}.

- The Java application `too-tikki` is used as an example throughout the documentation. The [`too-tikki`](https://github.com/oslokommune/pirates-iac/tree/main/stacks/prod/app-too-tikki){:target=\"_blank\"} is also the reference application.

- <figure markdown> <img src="../../images/general/too-tikki-stacks.png" width="300" alt="A screen capture from GitHub showing the folder structure of app-too-tikki" /> </figure>

- The infrastructure is set up by using Boilerplate templates. All the templates are prefixed with `__gp` (Golden Path).

## If you need to diverge from the path

- Sometimes you might have special requirements for your infrastructure and need to diverge from the path we have created. This is done by using [Terraform overrides](overrides.md).


---


## setup/before-you-start/overrides.md

# Terraform overrides

![This guide is optional](../../images/tags/optional-tag.svg){ align=left width=150}

<br> <br>

- The Golden Path uses Boilerplate templating to set up your infrastructure. To get all the benefits from being on the Golden Path, use Terraform overrides when you need to diverge from the path.

- !!! tip "Learn more about overrides" See the [HashiCorp documentation for override files](https://developer.hashicorp.com/terraform/language/files/override){:target="_blank"}.

- !!! example "Reference implementation" See [how Terraform overrides are used in `pirates-iac`](https://github.com/oslokommune/pirates-iac/blob/main/stacks/dev/app-too-tikki/_gp_alb_tg_host_routing_override.tf#L11){:target="_blank"}.

## Why use overrides?

- Overrides let you make changes based on your needs while still getting infrastructure updates. We collect data about which overrides teams create and add them to the Golden Path when possible.

## Frequently asked questions

### What if I don't need a resource created by Boilerplate?

- !!! Warning "Considerations" Before you remove resources from Boilerplate you should consider if the change you need could be done as a feature toggle in Boilerplate. You should also consider that other parts of the Golden Path may depend on the resource you are trying to remove. Removing resources in this way should be a last resort.

- You can remove a resource added by Boilerplate by adding a `count` to the resource. Given the following Terraform code:

```hcl
resource "aws_s3_bucket" "example" {
  bucket = "my-tf-test-bucket"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}
```

- Adding a `count` override to the resource in a file with the ending `_override.tf` removes the resource:

```hcl
resource "aws_s3_bucket" "example" {
    count = 0
}
```


---


## setup/before-you-start/tools/aws-cli.md



# AWS Command Line Interface

- [![Homebrew version](https://img.shields.io/homebrew/v/awscli){:target=\"_blank\"}](https://formulae.brew.sh/formula/awscli)

- The [AWS Command Line Interface](https://aws.amazon.com/cli/){:target=\"_blank\"} is mainly required for its [SSO authentication command](https://docs.aws.amazon.com/cli/latest/reference/sso/index.html){:target=\"_blank\"}.

```sh
brew install awscli
```

- Alternatively you can refer to [AWS' guide for installing AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html){:target=\"_blank\"}

- You will also need to install `session-manager` either through [Homebrew session-manager](https://aws.amazon.com/cli/){:target=\"_blank\"} for Mac or the general [AWS installation instruction](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html) for other platforms. `session-manager` is used by `ok forward` to connect to your database remotely.


---


## setup/before-you-start/tools/boilerplate.md



# `boilerplate`

`boilerplate` is used for generating all Terraform stacks from Golden Path.

- There are no brew packages available, save the following script and run it to install or update `boilerplate`:

```sh
MY_BIN_DIR="$HOME/bin"
PLATFORM=$(uname | tr '[:upper:]' '[:lower:]')

gh release download \
  --repo "gruntwork-io/boilerplate" \
  --clobber \
  --pattern "boilerplate_${PLATFORM}_amd64" \
  --output "$MY_BIN_DIR/boilerplate"

chmod +x "$MY_BIN_DIR/boilerplate"
```

Add the location of the Boilerplate binary to your PATH:

```bash
export PATH=$PATH:$HOME/bin
```

Verify that the correct version of Boilerplate is installed:

```bash
boilerplate -v
```

Persist the location of Boilerplate:

=== "macOS"

    ```bash
    echo 'export PATH=$PATH:$HOME/bin' >> ~/.zshrc
    ```

=== "Linux"

    ```bash
    echo 'export PATH=$PATH:$HOME/bin' >> ~/.bash_profile
    ```

- Alternatively you can refer to [`boilerplate` install documentation on GitHub](https://github.com/gruntwork-io/boilerplate?tab=readme-ov-file#install){:target=\"_blank\"}


---


## setup/before-you-start/tools/fzf.md



# `fzf`

- [![Homebrew version](https://img.shields.io/homebrew/v/fzf){:target=\"_blank\"}](https://formulae.brew.sh/formula/fzf)

- The `fzf` tool is a command-line fuzzy finder used by `ok` to interactively select items from a list.

```sh
brew install fzf
```

- Alternatively you can refer to [`fzf` on GitHub](https://github.com/junegunn/fzf#installation){:target=\"_blank\"}


---


## setup/before-you-start/tools/gh.md



# `gh`

- [![Homebrew version](https://img.shields.io/homebrew/v/gh){:target=\"_blank\"}](https://formulae.brew.sh/formula/gh)

- The `gh` tool is the official GitHub CLI and is used by `ok` to download reusable GitHub Actions workflows.

```sh
brew install gh
```

Then authenticate and follow the on-screen instructions:

```sh
gh auth login
```

Alternatively you can refer to [`gh` on GitHub](https://github.com/cli/cli){:target=\"_blank\"}


---


## setup/before-you-start/tools/index.md



# Tools

- We recommend using the [`brew`](https://brew.sh/){:target=\"_blank\"} package manager for installing software. In addition to MacOs, Homebrew also works on [Linux and Windows Subsystem for Linux (WSL)](https://docs.brew.sh/Homebrew-on-Linux){:target=\"_blank\"}.

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Required tools

- | Our guide                                         | External source                                                                                                                                   | |---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------| | [yq with brew](yq.md)                             | [yq on GitHub](https://github.com/mikefarah/yq/#install){:target=\"_blank\"}                                                                      | | [gh with brew](gh.md)                             | [gh on GitHub](https://github.com/cli/cli){:target=\"_blank\"}                                                                                    | | [jq with brew](jq.md)                             | [jq on GitHub](https://jqlang.github.io/jq/download/){:target=\"_blank\"}                                                                         | | [fzf with brew](fzf.md)                           | [fzf on GitHub](https://github.com/junegunn/fzf#installation){:target=\"_blank\"}                                                                 | | [Terraform (and TFSwitch) with brew](terraform.md)    | [HashiCorp's guide for installing Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli){:target=\"_blank\"} | | [AWS CLI with brew](aws-cli.md)                   | [AWS' guide for installing AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html){:target=\"_blank\"}            | | [Boilerplate](boilerplate.md)                     | [Gruntwork's guide for installing Boilerplate](https://github.com/gruntwork-io/boilerplate?tab=readme-ov-file#install){:target=\"_blank\"}        | | [ok](ok.md)                                       | -                                                                                                                                                 |


---


## setup/before-you-start/tools/jq.md



# `jq`

- [![Homebrew version](https://img.shields.io/homebrew/v/yq){:target=\"_blank\"}](https://formulae.brew.sh/formula/yq)

The `jq` tool is used by `ok`.

```sh
brew install jq
```

Or you can refer to [`jq`](https://jqlang.github.io/jq/){:target=\"_blank\"}


---


## setup/before-you-start/tools/ok.md

# `ok`

- [The `ok` tool](https://github.com/oslokommune/ok){:target=\"_blank\"} helps you get started with writing Terraform code and manage different environments.

## Installation

- We recommend using `brew` for installing `ok`. Homebrew is supported on [MacOS](https://brew.sh/){:target=\"_blank\"}, [Linux and WSL](https://docs.brew.sh/Homebrew-on-Linux){:target=\"_blank\"}.

=== "With `brew`"

Run the following command:

    ```bash
    brew tap oslokommune/ok https://github.com/oslokommune/ok
    brew install ok
    ```

=== "Manual install"

Run the following commands:

    ```
    BIN_DIR="$HOME/bin"
    PLATFORM=$(uname | tr '[:upper:]' '[:lower:]')
    ARCH=$(uname -m)

    case $ARCH in
         x86_64)
             ARCH="amd64"
            ;;
        aarch64|arm64)
            ARCH="arm64"
            ;;
         *)
            echo "Unsupported architecture: $ARCH"
            exit 1
            ;;
    esac

    gh release download \
        --repo "oslokommune/ok" \
        --pattern "ok_*_${PLATFORM}_${ARCH}.tar.gz" \
        --output - | tar -xzOf - ok > "$BIN_DIR/ok"
  
    chmod +x "$BIN_DIR/ok"
    "$BIN_DIR/ok" version

    ```

---

Verify that the `ok` command is available by running the following command:

```bash
ok
```

## Updating

To update the `ok` tool, run the following command:

```bash
brew update
brew upgrade ok
```

To check which version you have, you can run `ok version`.

## Delete `ok`

To delete the `ok` tool, run the follow the following command

```bash
cd $HOME/bin
rm ok
rm port-forward
```

If you can't find `ok` in the location above, check out

```bash
$HOME/git/golden-path-iac/bin
```


---


## setup/before-you-start/tools/terraform.md



# Terraform

- We recommend using [`tfswitch`](https://warrensbox.github.io/terraform-switcher/){:target=\"_blank\"} to manage your Terraform versions.

Install `tfswitch`:

```sh
brew install warrensbox/tap/tfswitch
```

Install Terraform:

```sh
tfswitch --latest
```

Add the location of the `tfswitch` binary to your `PATH`:

```bash
export PATH=$PATH:$HOME/bin
```

Verify that the correct version of Terraform is installed:

```bash
terraform version
```

Persist the location of Terraform versions managed by `tfswitch`:

=== "macOS"

    ```bash
    echo 'export PATH=$PATH:$HOME/bin' >> ~/.zshrc
    ```

=== "Linux"

    ```bash
    echo 'export PATH=$PATH:$HOME/bin' >> ~/.bash_profile
    ```

- !!! tip "Executable PATH" Once you open a new terminal window the path to the Terraform binary managed by `tfswitch` will not be set.

- To persist the path you must add the same command we ran manually in step 3 to your `~/.bash_profile` or `~/.zshrc` file. Below is an example of how to do this.

- !!! tip "Caching Terraform plugins" Terraform can cache plugins. This saves you time when downloading the same plugin multiple times. More information can be found in [HashiCorp's configuration reference](https://developer.hashicorp.com/terraform/cli/config/config-file#configuration-file-syntax)

- Alternatively you can refer to [HashiCorp's guide for installing Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli){:target=\"_blank\"}

## Add shell aliases (highly recommended)

- Add the following aliases to your shell configuration file (for example `~/.bashrc` or `~/.zshrc`[^1]):

```sh
alias tf='terraform'
alias tfa='tfswitch && terraform apply'
alias tfc='tfswitch && terraform console'
alias tfd='tfswitch && terraform destroy'
alias tff='tfswitch && terraform fmt'
alias tfi='tfswitch && terraform init'
alias tfo='tfswitch && terraform output'
alias tfp='tfswitch && terraform plan'
alias tfv='tfswitch && terraform validate'
alias tfl='tfswitch && terraform providers lock -platform=darwin_amd64 -platform=darwin_arm64 -platform=linux_amd64 -platform=windows_amd64'
```

- [^1]: See [What should/shouldn't go in `.zshenv`, `.zshrc`, `.zlogin`, `.zprofile`, `.zlogout`?](https://unix.stackexchange.com/questions/71253/what-should-shouldnt-go-in-zshenv-zshrc-zlogin-zprofile-zlogout){:target=\"_blank\"}.


---


## setup/before-you-start/tools/yq.md



# `yq`

- [![Homebrew version](https://img.shields.io/homebrew/v/yq){:target=\"_blank\"}](https://formulae.brew.sh/formula/yq)

The `yq` tool is used by `ok`.

```sh
brew install yq
```

- Alternatively you can refer to [`yq` on GitHub](https://github.com/mikefarah/yq/#install){:target=\"_blank\"}


---
