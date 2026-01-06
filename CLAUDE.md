# Claude Marketplace

This is a thin marketplace index for DIG (Digitaliseringsetaten) Oslo kommune plugins.

## Architecture

The marketplace is an **index only** - it points to plugins hosted in their source repositories:

| Plugin | Source Repository |
|--------|-------------------|
| ai-platform | [oslokommune/kunstig-intelligens](https://github.com/oslokommune/kunstig-intelligens) |
| iac-platform | [oslokommune/golden-path-boilerplate](https://github.com/oslokommune/golden-path-boilerplate) |
| km-internal | [oslokommune/golden-path-iac](https://github.com/oslokommune/golden-path-iac) |
| designsystem | [oslokommune/punkt](https://github.com/oslokommune/punkt) |

## For End Users

```bash
# Add the DIG marketplace
claude plugin marketplace add oslokommune/claude-marketplace

# Install plugins
claude plugin install ai-platform@dig
claude plugin install iac-platform@dig
```

## For Plugin Developers

Work directly in the source repository:

```bash
# Clone the plugin source repo
git clone git@github.com:oslokommune/kunstig-intelligens.git
cd kunstig-intelligens

# Install plugin locally for testing
claude plugin install ./

# Make changes, test, commit, push
```

## For Marketplace Maintainers

```bash
# Register local marketplace for testing
./dev-mode.sh

# Edit .claude-plugin/marketplace.json to update plugin references
```

## Migration

The `migration/` folder contains packages for migrating plugin content to source repos.
The `plugins/` folder contains legacy content pending migration.
