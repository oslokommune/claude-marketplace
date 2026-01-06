#!/usr/bin/env python3
"""
Cleanup script to remove plugin references from ~/.claude configuration.
Preserves logs and session history.
"""

import argparse
import json
import shutil
from pathlib import Path


CLAUDE_DIR = Path.home() / ".claude"
PLUGINS_DIR = CLAUDE_DIR / "plugins"


def print_action(action: str, path: Path, dry_run: bool) -> None:
    prefix = "[DRY RUN] " if dry_run else ""
    print(f"{prefix}{action}: {path}")


def clean_settings_json(dry_run: bool) -> bool:
    """Remove enabledPlugins from settings.json."""
    settings_file = CLAUDE_DIR / "settings.json"
    if not settings_file.exists():
        return False

    with open(settings_file) as f:
        settings = json.load(f)

    if "enabledPlugins" not in settings:
        return False

    plugins = settings.get("enabledPlugins", {})
    if not plugins:
        return False

    print_action(f"MODIFY (remove {len(plugins)} plugin entries)", settings_file, dry_run)
    for plugin_id, enabled in plugins.items():
        status = "enabled" if enabled else "disabled"
        print(f"         - {plugin_id} ({status})")

    if not dry_run:
        del settings["enabledPlugins"]
        with open(settings_file, "w") as f:
            json.dump(settings, f, indent=2)
            f.write("\n")

    return True


def clean_installed_plugins(dry_run: bool) -> bool:
    """Clear installed_plugins.json."""
    installed_file = PLUGINS_DIR / "installed_plugins.json"
    if not installed_file.exists():
        return False

    with open(installed_file) as f:
        data = json.load(f)

    plugins = data.get("plugins", {})
    if not plugins:
        return False

    print_action(f"MODIFY (remove {len(plugins)} installed plugins)", installed_file, dry_run)
    for plugin_id, installations in plugins.items():
        # Each plugin has a list of installations
        if isinstance(installations, list) and installations:
            version = installations[0].get("version", "unknown")
        else:
            version = "unknown"
        print(f"         - {plugin_id} v{version}")

    if not dry_run:
        data["plugins"] = {}
        with open(installed_file, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")

    return True


def clean_known_marketplaces(dry_run: bool) -> bool:
    """Clear known_marketplaces.json if it has entries."""
    marketplaces_file = PLUGINS_DIR / "known_marketplaces.json"
    if not marketplaces_file.exists():
        return False

    with open(marketplaces_file) as f:
        data = json.load(f)

    if not data:
        return False

    print_action(f"MODIFY (remove {len(data)} marketplaces)", marketplaces_file, dry_run)
    for marketplace_id in data:
        print(f"         - {marketplace_id}")

    if not dry_run:
        with open(marketplaces_file, "w") as f:
            json.dump({}, f, indent=2)
            f.write("\n")

    return True


def clean_install_counts_cache(dry_run: bool) -> bool:
    """Delete install-counts-cache.json."""
    cache_file = PLUGINS_DIR / "install-counts-cache.json"
    if not cache_file.exists():
        return False

    with open(cache_file) as f:
        data = json.load(f)

    print_action(f"DELETE (cache with {len(data)} entries)", cache_file, dry_run)

    if not dry_run:
        cache_file.unlink()

    return True


def clean_plugin_cache(dry_run: bool) -> bool:
    """Remove plugin cache directory contents."""
    cache_dir = PLUGINS_DIR / "cache"
    if not cache_dir.exists():
        return False

    # Find all marketplace directories in cache
    marketplaces = [d for d in cache_dir.iterdir() if d.is_dir()]
    if not marketplaces:
        return False

    for marketplace_dir in marketplaces:
        plugin_count = sum(1 for _ in marketplace_dir.rglob("plugin.json"))
        print_action(f"DELETE (marketplace cache: {marketplace_dir.name}, ~{plugin_count} plugins)", marketplace_dir, dry_run)

        if not dry_run:
            shutil.rmtree(marketplace_dir)

    return True


def clean_marketplaces_dir(dry_run: bool) -> bool:
    """Remove marketplace directory contents."""
    marketplaces_dir = PLUGINS_DIR / "marketplaces"
    if not marketplaces_dir.exists():
        return False

    contents = list(marketplaces_dir.iterdir())
    if not contents:
        return False

    print_action(f"DELETE (marketplace repos: {len(contents)} items)", marketplaces_dir, dry_run)
    for item in contents:
        print(f"         - {item.name}")

    if not dry_run:
        for item in contents:
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove plugin references from ~/.claude configuration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s              # Dry run (preview changes)
  %(prog)s --execute    # Actually perform cleanup
        """,
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually perform the cleanup (default is dry run)",
    )
    args = parser.parse_args()

    dry_run = not args.execute

    print("=" * 60)
    if dry_run:
        print("DRY RUN MODE - No changes will be made")
    else:
        print("EXECUTE MODE - Changes will be applied")
    print("=" * 60)
    print()

    changes = []

    # Run all cleanup functions
    if clean_settings_json(dry_run):
        changes.append("settings.json")

    if clean_installed_plugins(dry_run):
        changes.append("installed_plugins.json")

    if clean_known_marketplaces(dry_run):
        changes.append("known_marketplaces.json")

    if clean_install_counts_cache(dry_run):
        changes.append("install-counts-cache.json")

    if clean_plugin_cache(dry_run):
        changes.append("cache/")

    if clean_marketplaces_dir(dry_run):
        changes.append("marketplaces/")

    print()
    print("=" * 60)
    if changes:
        action = "Would affect" if dry_run else "Affected"
        print(f"{action} {len(changes)} locations:")
        for change in changes:
            print(f"  - {change}")
        if dry_run:
            print()
            print("Run with --execute to apply changes")
    else:
        print("No plugin references found to clean up")
    print("=" * 60)


if __name__ == "__main__":
    main()
