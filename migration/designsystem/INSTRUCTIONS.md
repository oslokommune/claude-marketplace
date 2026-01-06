# Design System Plugin Migration Instructions

## Target Repository
`oslokommune/punkt` (or appropriate Punkt design system repository - TO BE CONFIRMED)

## Objective
Convert the target repository into a Claude Code plugin by adding the plugin structure and migrating skill content from the DIG marketplace.

## Steps

### 1. Create Plugin Manifest

Create `.claude-plugin/plugin.json` at the repository root:

```json
{
  "name": "dig-designsystem",
  "description": "Punkt Design System - Oslo Kommune's design system for accessible frontend applications",
  "version": "2.0.0",
  "author": {
    "name": "Designsystem"
  },
  "keywords": [
    "design system",
    "frontend",
    "punkt",
    "dig",
    "components",
    "react",
    "webcomponents",
    "ui",
    "styles",
    "css",
    "icons"
  ]
}
```

### 2. Create Plugin Directory Structure

The plugin requires these directories at the repository ROOT:

```
punkt/
├── .claude-plugin/
│   └── plugin.json          # Created in step 1
├── skills/                  # NEW - plugin skills (copy from this package)
│   └── punkt-docs/
│       ├── SKILL.md
│       ├── components/      # 31 component docs
│       ├── packages/        # 7 package docs
│       ├── resources/       # Design tokens, colors, typography
│       └── best-practices/  # Accessibility, forms, testing
└── ...                      # Existing Punkt source code
```

### 3. Copy Content

Copy the following from this migration package to the target repository root:

1. `skills/` → `<repo-root>/skills/`

### 4. Verify Plugin Structure

After migration, the repository should be installable as a plugin:

```bash
# Test locally
claude plugin install ./

# Verify skills are available
claude --print-skills
```

## Content Included

This package contains:

- `skills/punkt-docs/` - Comprehensive Punkt documentation:
  - `SKILL.md` - Main skill definition with component index
  - `getting-started.md` - Installation and setup
  - `overview.md` - Project architecture
  - `contributing.md` - Contribution guidelines

  - `components/` - 31 component docs:
    - accordion, alert, backlink, breadcrumbs, button, card, checkbox, combobox
    - consent, datepicker, footer, header, headermeny, icon, inputwrapper
    - link, linkcard, loader, messagebox, modal, progressbar, radiobuttons
    - searchinput, select, stepper, switch, table, tabs, tag, textarea, textinput

  - `packages/` - 7 package docs:
    - react.md - punkt-react (React 18 components)
    - elements.md - punkt-elements (Web components/Lit)
    - css.md - punkt-css (SASS framework)
    - assets.md - punkt-assets (Icons, logos, fonts)
    - cli.md - punkt-cli
    - testing-utils.md - Testing utilities
    - vue.md - Vue components

  - `resources/` - Design tokens:
    - colors.md, typografi.md, spacing.md, font.md
    - grid.md, breakpoints.md
    - ikoner.md, illustrasjoner.md, oslologo.md
    - hjelpeklasser.md

  - `best-practices/` - Guidelines:
    - punkt-og-uu.md - Accessibility (UU)
    - skjemadesign.md - Form design
    - kontrastsjekker.md - Contrast checking
    - testverktoy.md - Testing tools
    - disabled-states.md - Disabled state patterns
    - innsiktsprinsipper.md - Design principles

- `plugin.json` - Reference for the manifest (adapt as needed)

## Notes

- Documentation is primarily in Norwegian (Bokmål) as Punkt serves Oslo Kommune
- Code examples and technical terms use English conventions
- The skill uses progressive disclosure - Claude reads files on-demand
- punkt-elements (web components) is the complete library; punkt-react is a partial wrapper
