---
name: punkt-docs
description: >
  Complete documentation for the Punkt Design System by Oslo Kommune. 
  Provides comprehensive information about UI components (buttons, inputs, modals, 
  forms, navigation), React and web component packages, design resources (colors, 
  typography, spacing), CSS framework, accessibility guidelines, and implementation 
  patterns. IMPORTANT: punkt-elements (web components) is the complete library with 
  all 31 components. punkt-react is a partial wrapper - when working in React, prefer 
  using punkt-elements web components directly for full component access. Use when 
  answering questions about Punkt, Oslo Kommune design system, implementing Punkt 
  components, styling with Punkt CSS, using punkt-react or punkt-elements packages, 
  design tokens, or Oslo municipal design standards.
allowed-tools: Read
---

# Punkt Design System Documentation

This skill provides comprehensive documentation for the Punkt Design System, 
Oslo Kommune's official design system for building accessible digital solutions.

## Overview


**Punkt** is Oslo Municipality's open-source design system for building accessible digital solutions for Norwegian citizens.


## Important: Library Architecture

**punkt-elements** (web components) is the **complete, primary library** with all 31 components.

**punkt-react** is a **partial wrapper** around punkt-elements - not all components have React wrappers.

**Recommendation**: When working in React projects, prefer using punkt-elements web components 
directly to ensure access to the full component set. React wrappers are provided for convenience 
but web components work seamlessly in React and provide complete functionality.

## Quick Reference

### Most Common Components

- [Button](components/button.md)
- [Textinput](components/textinput.md)
- [Select](components/select.md)
- [Modal](components/modal.md)
- [Checkbox](components/checkbox.md)
- [Textarea](components/textarea.md)
- [Card](components/card.md)
- [Alert](components/alert.md)
- [Accordion](components/accordion.md)
- [Tabs](components/tabs.md)

### Main Packages

- [punkt-react](packages/react.md) - React 18 component library
- [punkt-elements](packages/elements.md) - Web components (Lit)
- [punkt-css](packages/css.md) - SASS-based CSS framework
- [punkt-assets](packages/assets.md) - Icons, logos, and fonts

## How to Use This Documentation

This skill uses progressive disclosure - Claude reads only the files needed to answer your question.

### Finding Components

Browse all 31 components: [components/README.md](components/README.md)

Each component document includes:
- Usage guidelines and examples
- Complete prop specifications
- TypeScript interfaces
- Accessibility notes

### Package Information

View all 7 packages: [packages/README.md](packages/README.md)

Package docs include:
- Installation instructions
- API documentation
- Version information
- Peer dependencies

### Design Resources

Colors, typography, spacing: [resources/README.md](resources/README.md)

Includes:
- Design tokens
- Color palettes
- Typography scale
- Spacing system
- Grid system
- Breakpoints

### Best Practices

Accessibility and guidelines: [best-practices/README.md](best-practices/README.md)

Covers:
- Form design patterns
- Accessibility (UU) guidelines
- WCAG compliance
- Testing approaches

## Getting Started

For installation and setup instructions, see [getting-started.md](getting-started.md).

## Project Structure

For a complete overview of the project architecture, packages, and conventions, 
see [overview.md](overview.md).

## Contributing

See [contributing.md](contributing.md) for contribution guidelines, code of conduct, 
and security policy.

## Complete Component Reference

- [Accordion](components/accordion.md)
- [Alert](components/alert.md)
- [Backlink](components/backlink.md)
- [Breadcrumbs](components/breadcrumbs.md)
- [Button](components/button.md)
- [Card](components/card.md)
- [Checkbox](components/checkbox.md)
- [Combobox](components/combobox.md)
- [Consent](components/consent.md)
- [Datepicker](components/datepicker.md)
- [Footer](components/footer.md)
- [Header](components/header.md)
- [Headermeny](components/headermeny.md)
- [Icon](components/icon.md)
- [Inputwrapper](components/inputwrapper.md)
- [Link](components/link.md)
- [Linkcard](components/linkcard.md)
- [Loader](components/loader.md)
- [Messagebox](components/messagebox.md)
- [Modal](components/modal.md)
- [Progressbar](components/progressbar.md)
- [Radiobuttons](components/radiobuttons.md)
- [Searchinput](components/searchinput.md)
- [Select](components/select.md)
- [Stepper](components/stepper.md)
- [Switch](components/switch.md)
- [Table](components/table.md)
- [Tabs](components/tabs.md)
- [Tag](components/tag.md)
- [Textarea](components/textarea.md)
- [Textinput](components/textinput.md)

## Language Note

Documentation content is primarily in Norwegian (Bokmål) as Punkt serves 
Oslo Kommune (Oslo Municipality). Code examples, prop names, and technical 
documentation use English conventions.
