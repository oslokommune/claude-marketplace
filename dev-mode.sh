#!/bin/bash
# Enable local marketplace development mode
#
# This script registers the local marketplace index with Claude Code.
# The marketplace is a thin index pointing to plugins in external repos:
#   - ai-platform     → oslokommune/kunstig-intelligens
#   - iac-platform    → oslokommune/golden-path-boilerplate
#   - km-internal     → oslokommune/golden-path-iac
#   - designsystem    → oslokommune/punkt
#
# For plugin development, work directly in the source repo and use:
#   claude plugin install ./
#
# This script is for testing the marketplace index itself.

set -e

echo "Enabling local marketplace development mode..."

# Remove any existing marketplace mount
echo "Removing existing marketplace mount..."
claude plugin marketplace remove dig 2>/dev/null || true

# Add local directory as marketplace
echo "Adding local directory as marketplace..."
claude plugin marketplace add ./

echo ""
echo "Marketplace registered. Available plugins:"
echo "  - ai-platform@dig     (from oslokommune/kunstig-intelligens)"
echo "  - iac-platform@dig    (from oslokommune/golden-path-boilerplate)"
echo "  - km-internal@dig     (from oslokommune/golden-path-iac)"
echo "  - designsystem@dig    (from oslokommune/punkt)"
echo ""
echo "Install a plugin with: claude plugin install <plugin-name>@dig"
echo ""
echo "NOTE: Plugins are fetched from their source repos, not from this directory."
echo "      The plugins/ folder contains legacy content pending migration."
