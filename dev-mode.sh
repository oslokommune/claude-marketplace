#!/bin/bash
# Enable local plugin development mode for Claude Marketplace

set -e

echo "Enabling local plugin development mode..."

# Remove any existing marketplace mount
echo "Removing existing marketplace mount..."
claude plugin marketplace remove dig 2>/dev/null || true

# Add local directory as marketplace
echo "Adding local directory as marketplace..."
claude plugin marketplace add ./

# Install plugins
echo "Installing plugins..."
for plugin in plugins/*/; do
    plugin_name=$(basename "$plugin")
    echo "Installing $plugin_name..."
    claude plugin install "$plugin_name@dig"
done

echo "Local development mode enabled!"
