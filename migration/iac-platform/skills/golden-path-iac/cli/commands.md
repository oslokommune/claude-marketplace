# CLI Commands

**Source files**: 17


## cli/ok.md

# ok

The `ok` infrastructure toolbox.

## Synopsis

- The `ok` tool is a comprehensive infrastructure management toolbox designed to streamline the setup and maintenance of Terraform environments. It provides a variety of commands to bootstrap infrastructure, manage environment configurations, handle AWS operations, and more.

Key functionalities include:

- Executing AWS-specific commands.
- Managing and updating Boilerplate templates.

- Whether you're setting up a new environment or maintaining an existing one, `ok` simplifies and automates many of the repetitive tasks involved in infrastructure management.

## Options

```sh
      --config string   config file (default is /home/runner/.config/ok/config.yml)
  -h, --help            help for ok
```

## See also

- [ok aws](ok_aws.md) - Group of AWS related commands.
- [ok completion](ok_completion.md) - Generate the autocompletion script for the
specified shell
- [ok forward](ok_forward.md) - Starts a port forwarding session to a database.
- [ok pkg](ok_pkg.md) - Group of package related commands for managing
Boilerplate packages.
- [ok version](ok_version.md) - Prints the version of the `ok` tool and the
current latest version available.


---


## cli/ok_aws.md

# ok aws

Group of AWS related commands.

## Options

```sh
  -h, --help   help for aws
```

## See also

- [ok](ok.md) - The `ok` infrastructure toolbox.
- [ok aws admin-session](ok_aws_admin-session.md) - Start an admin session to an
AWS account
- [ok aws ecs-exec](ok_aws_ecs-exec.md) - Get a shell to a running ECS task
- [ok aws generate](ok_aws_generate.md) - Generate AWS CLI configuration for AWS
IAM Identity Center roles


---


## cli/ok_aws_admin-session.md

# ok aws admin-session

Start an admin session to an AWS account

```sh
ok aws admin-session [flags]
```

## Options

```sh
  -h, --help          help for admin-session
  -s, --start-shell   Start a working shell to execute AWS commands
```

## See also

- [ok aws](ok_aws.md) - Group of AWS related commands.


---


## cli/ok_aws_ecs-exec.md

# ok aws ecs-exec

Get a shell to a running ECS task

```sh
ok aws ecs-exec [flags]
```

## Options

```sh
  -h, --help   help for ecs-exec
```

## See also

- [ok aws](ok_aws.md) - Group of AWS related commands.


---


## cli/ok_aws_generate.md

# ok aws generate

Generate AWS CLI configuration for AWS IAM Identity Center roles

## Synopsis

Generate AWS CLI configuration for AWS IAM Identity Center roles.

Profile name template supports the following variables:

- `{{.SessionName}}`: The name of the SSO session
- `{{.AccountName}}`: The name of the AWS account
- `{{.AccountID}}`: The ID of the AWS account
- `{{.RoleName}}`: The name of the IAM role

Example:

```sh
ok aws generate \
  --sso-start-url "https://my-sso.awsapps.com/start" \
  --sso-region "eu-west-1" \
  --template "ok-{{.AccountName}}-{{.RoleName}}"
```

```sh
ok aws generate [flags]
```

## Options

```sh
  -h, --help                   help for generate
      --region string          The default region for generated profiles (defaults to sso-region if not set)
      --session-name string    An optional name of the SSO session (defaults to the AWS IAM Identity Center instance identifier if not set)
      --sso-region string      The region of the AWS IAM Identity Center instance
      --sso-start-url string   The start URL of the AWS IAM Identity Center instance
      --template string        Go string template for generating profile names
```

## See also

- [ok aws](ok_aws.md) - Group of AWS related commands.


---


## cli/ok_completion.md

# ok completion

Generate the autocompletion script for the specified shell

## Synopsis

- Generate the autocompletion script for ok for the specified shell. See each sub-command's help for details on how to use the generated script.

## Options

```sh
  -h, --help   help for completion
```

## See also

- [ok](ok.md) - The `ok` infrastructure toolbox.
- [ok completion bash](ok_completion_bash.md) - Generate the autocompletion
script for bash
- [ok completion fish](ok_completion_fish.md) - Generate the autocompletion
script for fish
- [ok completion powershell](ok_completion_powershell.md) - Generate the
autocompletion script for powershell
- [ok completion zsh](ok_completion_zsh.md) - Generate the autocompletion script
for zsh


---


## cli/ok_completion_bash.md

# ok completion bash

Generate the autocompletion script for bash

## Synopsis

Generate the autocompletion script for the bash shell.

- This script depends on the 'bash-completion' package. If it is not installed already, you can install it via your OS's package manager.

To load completions in your current shell session:

```sh
source <(ok completion bash)
```

To load completions for every new session, execute once:

### Linux

```sh
ok completion bash > /etc/bash_completion.d/ok
```

### macOS

```sh
ok completion bash > $(brew --prefix)/etc/bash_completion.d/ok
```

You will need to start a new shell for this setup to take effect.

```sh
ok completion bash
```

## Options

```sh
  -h, --help              help for bash
      --no-descriptions   disable completion descriptions
```

## See also

- [ok completion](ok_completion.md) - Generate the autocompletion script for the
specified shell


---


## cli/ok_completion_fish.md

# ok completion fish

Generate the autocompletion script for fish

## Synopsis

Generate the autocompletion script for the fish shell.

To load completions in your current shell session:

```sh
ok completion fish | source
```

To load completions for every new session, execute once:

```sh
ok completion fish > ~/.config/fish/completions/ok.fish
```

You will need to start a new shell for this setup to take effect.

```sh
ok completion fish [flags]
```

## Options

```sh
  -h, --help              help for fish
      --no-descriptions   disable completion descriptions
```

## See also

- [ok completion](ok_completion.md) - Generate the autocompletion script for the
specified shell


---


## cli/ok_completion_powershell.md

# ok completion powershell

Generate the autocompletion script for powershell

## Synopsis

Generate the autocompletion script for powershell.

To load completions in your current shell session:

```sh
ok completion powershell | Out-String | Invoke-Expression
```

- To load completions for every new session, add the output of the above command to your powershell profile.

```sh
ok completion powershell [flags]
```

## Options

```sh
  -h, --help              help for powershell
      --no-descriptions   disable completion descriptions
```

## See also

- [ok completion](ok_completion.md) - Generate the autocompletion script for the
specified shell


---


## cli/ok_completion_zsh.md

# ok completion zsh

Generate the autocompletion script for zsh

## Synopsis

Generate the autocompletion script for the zsh shell.

- If shell completion is not already enabled in your environment you will need to enable it. You can execute the following once:

```sh
echo "autoload -U compinit; compinit" >> ~/.zshrc
```

To load completions in your current shell session:

```sh
source <(ok completion zsh)
```

To load completions for every new session, execute once:

### Linux

```sh
ok completion zsh > "${fpath[1]}/_ok"
```

### macOS

```sh
ok completion zsh > $(brew --prefix)/share/zsh/site-functions/_ok
```

You will need to start a new shell for this setup to take effect.

```sh
ok completion zsh [flags]
```

## Options

```sh
  -h, --help              help for zsh
      --no-descriptions   disable completion descriptions
```

## See also

- [ok completion](ok_completion.md) - Generate the autocompletion script for the
specified shell


---


## cli/ok_forward.md

# ok forward

Starts a port forwarding session to a database.

```sh
ok forward [flags]
```

## Options

```sh
  -h, --help   help for forward
```

## See also

- [ok](ok.md) - The `ok` infrastructure toolbox.


---


## cli/ok_pkg.md

# ok pkg

Group of package related commands for managing Boilerplate packages.

## Options

```sh
  -h, --help   help for pkg
```

## See also

- [ok](ok.md) - The `ok` infrastructure toolbox.
- [ok pkg add](ok_pkg_add.md) - Add the Boilerplate template to the package
manifest with an optional output folder
- [ok pkg fmt](ok_pkg_fmt.md) - Format the package manifest file.
- [ok pkg install](ok_pkg_install.md) - Install or update Boilerplate packages.
- [ok pkg update](ok_pkg_update.md) - Update Boilerplate package manifest and
package configuration files


---


## cli/ok_pkg_add.md

# ok pkg add

Add the Boilerplate template to the package manifest with an optional output folder

## Synopsis

- Add the Boilerplate template to the package manifest with an optional output folder. The template version is fetched from the latest GitHub release in the template repository. The output folder is useful when you need multiple instances of the same template with different configurations, for example having multiple instances of the application template.

```sh
ok pkg add <template> [outputFolder] [flags]
```

## Examples

```sh
ok pkg add databases my-postgres-database
ok pkg add app ecommerce-website
ok pkg add app ecommerce-api
BASE_URL=../boilerplate/terraform ok pkg add networking

```

## Options

```sh
  -h, --help              help for add
      --no-schema         Do not add the JSON schema for the package
  -s, --no-var-file       Do not download a var file for the package
  -v, --var-file string   Download a var file for the package with the specified name (default "default")
```

## See also

- [ok pkg](ok_pkg.md) - Group of package related commands for managing
Boilerplate packages.


---


## cli/ok_pkg_fmt.md

# ok pkg fmt

Format the package manifest file.

```sh
ok pkg fmt [flags]
```

## Examples

```sh
ok pkg fmt
```

## Options

```sh
  -h, --help   help for fmt
```

## See also

- [ok pkg](ok_pkg.md) - Group of package related commands for managing
Boilerplate packages.


---


## cli/ok_pkg_install.md

# ok pkg install

Install or update Boilerplate packages.

## Synopsis

Install or update Boilerplate packages.

- If no arguments are used, the command installs all the packages specified in the package manifest file.

- If one or more output folders are specified, the command installs only the packages whose OutputFolder matches the specified folders. (OutputFolder is a field in the package manifest file.)

Set the environment variable BASE_URL to specify where package templates are downloaded from.

```sh
ok pkg install [outputFolder ...] [flags]
```

## Examples

```sh
ok pkg install networking
ok pkg install networking my-app
BASE_URL=../boilerplate/terraform ok pkg install networking my-app

```

## Options

```sh
  -h, --help          help for install
  -i, --interactive   Select package(s) to install interactively
  -r, --recursive     Install packages from manifests found in all subdirectories, but excluding the current directory.
```

## See also

- [ok pkg](ok_pkg.md) - Group of package related commands for managing
Boilerplate packages.


---


## cli/ok_pkg_update.md

# ok pkg update

Update Boilerplate package manifest and package configuration files

## Synopsis

Update Boilerplate package manifest and package configuration files.

- If no arguments are used, the command installs all the packages specified in the package manifest file.

- If one or more output folders are specified, the command installs only the packages whose OutputFolder matches the specified folders. (OutputFolder is a field in the package manifest file.)

Set the environment variable BASE_URL to specify where package templates are downloaded from.

```sh
ok pkg update [outputFolder ...] [flags]
```

## Examples

```sh
ok pkg update
ok pkg update my-package

```

## Options

```sh
      --disable-manifest-update   Disable package manifest version updates (useful when using an external dependency manager like Renovate)
  -h, --help                      help for update
  -i, --interactive               Select package(s) to install interactively
      --migrate-config            Automatically migrate package configuration files to the latest version, if possible (default true)
  -r, --recursive                 Update packages from manifests found in all subdirectories, but excluding the current directory.
      --update-schema             Update the JSON schema for affected packages (default true)
```

## See also

- [ok pkg](ok_pkg.md) - Group of package related commands for managing
Boilerplate packages.


---


## cli/ok_version.md

# ok version

Prints the version of the `ok` tool and the current latest version available.

```sh
ok version [flags]
```

## Options

```sh
  -h, --help   help for version
```

## See also

- [ok](ok.md) - The `ok` infrastructure toolbox.


---
