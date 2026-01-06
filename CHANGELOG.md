# Changelog

## [2.0.0](https://github.com/oslokommune/claude-marketplace/compare/v1.0.0...v2.0.0) (2025-01-06)

### ⚠ BREAKING CHANGES

* Marketplace is now a thin index pointing to external plugin repositories

### Features

* Convert to thin index architecture ([#TBD](https://github.com/oslokommune/claude-marketplace/issues/TBD))
  * Plugins now live in their source repositories
  * Marketplace only contains the index (marketplace.json)
  * Migration packages provided for transitioning plugins

### Plugin Distribution

| Plugin | Source Repository |
|--------|-------------------|
| ai-platform | oslokommune/kunstig-intelligens |
| iac-platform | oslokommune/golden-path-boilerplate |
| km-internal | oslokommune/golden-path-iac |
| designsystem | oslokommune/punkt |
