# Renovate Dependency Management

**Source files**: 1


## reference/renovate/index.md

# Renovate

- [Renovate](https://github.com/renovatebot/renovate) is a tool for automatically updating dependencies in a codebase. It is very powerful and flexible, and you can think of it as Dependabot on steroids. While it supports every ecosystem under the sun, our default configuration only uses it to automatically update templates from the Golden Path through Pull Requests. We run Renovate as a scheduled GitHub Actions workflow in [golden-path-renovate](https://github.com/oslokommune/golden-path-renovate/actions/workflows/renovate.yml).

## How do I use it?

- Renovate regularly opens Pull Requests in enrolled repositories, and by default only updates Golden Path templates.

### Handling an update to a Terraform template

1. **Read the release notes to understand the changes.**<br/>
- These can be especially useful when updating major versions as that typically implies some kind of breaking change that requires manual intervention.
1. **Apply the changes in a PR as you normally would any Terraform change.**<br/>
- If it's a minor or patch update, you should typically be able to apply the changes as-is. If you don't have a CI/CD pipeline for your infrastructure, pull down the branch locally, navigate to the affected directory, run Terraform manually (i.e., `terraform init`, `terraform plan`, `terraform apply`, etc.), and finally merge the PR.

### Familiarize yourself with the `Dependency Dashboard`

- Renovate will create an issue named `Dependency Dashboard` the first time it runs against a repository. This issue will show you all the available updates, and can also be used to manually select which updates Renovate should create Pull Requests for on its next run.

- !!! tip Pin the Dependency Dashboard issue to keep it at the top of your issues list for easy access. You can pin it by opening the issue and clicking the pin icon in the right sidebar, or by using the three-dot menu and selecting "Pin issue".

## Details

<!-- vale off -->
- The `renovate.json5` file in your repository defines Renovate's behavior when running against your repository. Feel free to customize this if you'd like - there are [many](https://docs.renovatebot.com/configuration-options/) options.
- At most 4 PRs from Renovate are open at once unless temporarily overridden (through the `Dependency Dashboard`) or on a more permanent basis (through the `renovate.json5` configuration file).
- For updates to Golden Path templates, Renovate prioritizes major versions (`X.0.0`) over minor versions (`0.X.0`) over patch versions (`0.0.X`).
- By default PRs for new major versions of Golden Path templates are created immediately, minor versions bi-weekly, and patch versions once a month.
- Renovate runs every weekday on an hourly schedule. You can also manually trigger [this GitHub Actions workflow](https://github.com/oslokommune/golden-path-renovate/actions/workflows/renovate.yml) to have Renovate run immediately against your repository instead of waiting for the next scheduled run (e.g., if you've made changes through the `Dependency Dashboard` that you want to take effect ASAP).
<!-- vale on-->

- Any questions or input? Let us know in [#origo-kjøremiljø-support](https://oslokommune.slack.com/archives/CV9EGL9UG) 🙋


---
