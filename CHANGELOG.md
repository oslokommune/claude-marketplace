# Changelog

## [3.0.0](https://github.com/oslokommune/claude-marketplace/compare/dig-marketplace-v2.0.0...dig-marketplace-v3.0.0) (2026-01-07)


### ⚠ BREAKING CHANGES

* Marketplace now points to external plugin repositories instead of containing plugin content directly.

### Features

* Add global code rules and update settings for improved package management and permissions ([968adef](https://github.com/oslokommune/claude-marketplace/commit/968adefcd652ffb957c637421112a7471364142d))
* Add km-internal plugin for Team kjøremiljø workflows ([9a8eb21](https://github.com/oslokommune/claude-marketplace/commit/9a8eb21444a4c9072de72046f395f69e9585634a))
* Add organize_permissions script to manage and sort permissions in settings files ([dcfa4d5](https://github.com/oslokommune/claude-marketplace/commit/dcfa4d5c14e01fb6d76e19b8a6b89b4ad7b09cdc))
* Convert marketplace to thin index architecture ([12ffb3a](https://github.com/oslokommune/claude-marketplace/commit/12ffb3a3702f64424a03dff150b7f115ade2ae11))
* Draft plugins ([32012dd](https://github.com/oslokommune/claude-marketplace/commit/32012ddf62866832314973e45f498a856cb5cfe7))
* Fix permissions ([928e6b8](https://github.com/oslokommune/claude-marketplace/commit/928e6b808d8d8f15272619f2fccdf05fdcdf4fec))
* Initial release ([2943aff](https://github.com/oslokommune/claude-marketplace/commit/2943aff42decf735e4cf05283190f82c5c76baac))
* Migrate organization naming from Origo to DIG ([b8d8d8b](https://github.com/oslokommune/claude-marketplace/commit/b8d8d8be0d9805f08e4ced97d646e3e63e898f4d))
* Register km-internal plugin in marketplace ([d83284f](https://github.com/oslokommune/claude-marketplace/commit/d83284fe629caa15b506bb5fca5f5d634a273662))
* Remove readme ([ea753a5](https://github.com/oslokommune/claude-marketplace/commit/ea753a59323f7fd72f44f54f1748481cebdf2b5c))
* Update description ([f531bc6](https://github.com/oslokommune/claude-marketplace/commit/f531bc6b637a172ae5ba8382cb658be9236c4c38))
* Update explore.md promtp ([623ace8](https://github.com/oslokommune/claude-marketplace/commit/623ace8283be488549d7fdbd3be4fc38802771ea))


### Bug Fixes

* add support for PAT token in organization repos ([da812b7](https://github.com/oslokommune/claude-marketplace/commit/da812b7d18ee7abcd55c88ed0a797536e66e00c3))
* permission for GHA ([3fd7db4](https://github.com/oslokommune/claude-marketplace/commit/3fd7db432cb4ca9988a134b19cd57b5bc2ad46fe))
* Remove Origo references ([2e9c0c9](https://github.com/oslokommune/claude-marketplace/commit/2e9c0c94606607a0afb572507b10189964def4da))
* Update folder structure ([47af9cd](https://github.com/oslokommune/claude-marketplace/commit/47af9cd14c90e903e4a9f42468459e0574080608))
* Update version to 2.0.1 in marketplace.json ([db30470](https://github.com/oslokommune/claude-marketplace/commit/db30470710c7ba674d5ab663ef7baf4e4065c937))

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
