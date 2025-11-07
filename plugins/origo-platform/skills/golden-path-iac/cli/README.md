# ok CLI Documentation

The "ok" CLI tool simplifies common Golden Path operations.

## Installation

The ok CLI is part of the Golden Path toolkit. Installation instructions are in [setup/prerequisites.md](../setup/prerequisites.md).

## Usage

```bash
# Get help
ok --help

# Common commands
ok aws             # AWS operations
ok forward         # Port forwarding
ok package         # Package management
ok completion      # Shell completion
ok version         # Version information
```

## Command Reference

See [commands.md](commands.md) for detailed documentation of all available commands.

## Configuration

The ok CLI reads configuration from:
- Environment variables
- Configuration files in your project
- Command-line flags

## Examples

```bash
# Port forward to a service
ok forward my-service 8080

# List available packages
ok package list

# Install shell completion
ok completion bash > /etc/bash_completion.d/ok
```
