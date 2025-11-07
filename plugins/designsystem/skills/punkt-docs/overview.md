# Punkt Design System - Overview

**Generated**: 2025-11-06T10:52:48.921248
**Git Commit**: 05685b33
**Source Files**:
- `AGENTS.md`
- `README.md`

---

# Punkt Design System

**Punkt** is Oslo Municipality's open-source design system for building accessible digital solutions for Norwegian citizens.

## Project Type

A comprehensive design system monorepo providing UI components, styling framework, assets, and documentation. Currently at v13.12.0.

## Tech Stack

- **Monorepo**: Lerna v9 + npm workspaces + Nx for caching
- **Components**: Lit 3.x (web components), React 18, Vue 3 (deprecated)
- **Build**: Vite, TypeScript, esbuild
- **Testing**: Vitest (elements/react), Jest, Testing Library, jest-axe
- **Docs**: Astro v5 with React + MDX
- **Styling**: SASS/SCSS with 7-1 architecture pattern
- **CI/CD**: GitHub Actions

## Architecture & Structure

### Published Packages (`/packages/`)

All packages published to NPM under `@oslokommune` scope:

#### `punkt-elements` (v13.11.0)
- **Path**: `/packages/punkt-elements/`
- **Purpose**: Core web components built with Lit
- **Components**: 29 components (accordion, button, card, calendar, checkbox, combobox, datepicker, input, modal, select, tabs, textarea, etc.)
- **Framework**: Lit 3.x (Shadow DOM, Custom Elements)
- **Tests**: Vitest + Testing Library
- **Key Files**:
  - `/src/components/` - Component implementations
  - `/src/utils/` - Shared utilities
  - `/src/styles/` - Component styles
  - `vite.config.ts` - Build configuration

#### `punkt-react` (v13.12.0)
- **Path**: `/packages/punkt-react/`
- **Purpose**: React wrapper library for Punkt components
- **Components**: 35+ components (wraps punkt-elements + pure React components)
- **Framework**: React 18 with TypeScript
- **Pattern**: Uses `@lit/react` for wrapping web components, pure React where appropriate
- **Features**: React Hook Form integration, forwardRef support
- **Tests**: Vitest + React Testing Library
- **Key Files**:
  - `/lib/` - Component implementations
  - `/lib/utils/` - Shared utilities and context
  - `vite.config.ts` - Build configuration

#### `punkt-vue` (v13.11.0)
- **Path**: `/packages/punkt-vue/`
- **Purpose**: Vue 3 component library (LEGACY - being phased out)
- **Status**: Deprecated, maintained but not actively developed
- **Framework**: Vue 3 with Composition API
- **Key Files**:
  - `/src/lib/` - Component implementations

#### `punkt-css` (v13.11.0)
- **Path**: `/packages/punkt-css/`
- **Purpose**: SASS-based CSS framework
- **Architecture**: SASS 7-1 pattern:
  - `/abstracts` - Functions, mixins, placeholders, variables
  - `/base` - Base styles, typography
  - `/components` - Component-specific styles
  - `/elements` - HTML element styles
  - `/normalise` - CSS normalization
- **Output**: Compiled CSS for various use cases
- **Key Files**:
  - `/scss/` - Source SASS files
  - `/css/` - Compiled outputs

#### `punkt-assets` (v13.11.0)
- **Path**: `/packages/punkt-assets/`
- **Purpose**: Design assets (SVG icons, logos, fonts)
- **Contents**: 100+ optimized SVG icons
- **Tools**: SVGO for optimization
- **Key Files**:
  - `/src/icons/` - SVG icon library
  - `/src/logos/` - Oslo Kommune logos
  - `/src/fonts/` - Web fonts

#### `punkt-cli` (v13.7.0)
- **Path**: `/packages/punkt-cli/`
- **Purpose**: Command-line tools for Punkt workflows
- **Framework**: Commander.js
- **Features**: SVG sprite generation, project setup utilities
- **Key Files**:
  - `/src/commands/` - CLI command implementations

#### `punkt-testing-utils` (v13.12.0)
- **Path**: `/packages/punkt-testing-utils/`
- **Purpose**: Shared testing utilities across packages
- **Contents**: Testing Library wrappers, jest-axe setup, custom matchers
- **Used by**: punkt-elements, punkt-react test suites

### Applications (`/apps/`)

Private applications, not published to NPM:

#### `docs-astro`
- **Path**: `/apps/docs-astro/`
- **Purpose**: Documentation website (punkt.oslo.kommune.no)
- **Framework**: Astro v5 with React integration
- **Features**:
  - Component documentation with live examples
  - Design guidelines
  - Usage guides
  - MDX for content authoring
  - Syntax highlighting with Prism
- **Key Files**:
  - `/src/pages/` - Documentation pages (MDX)
  - `/src/components/` - Doc site components
  - `/src/content/` - Content collections
  - `astro.config.mjs` - Astro configuration

#### `cdn`
- **Path**: `/apps/cdn/`
- **Purpose**: CDN hosting application (punkt-cdn.oslo.kommune.no)
- **Function**: Serves compiled assets via CDN
- **Tech**: Mustache templates for version management
- **Key Files**:
  - `/templates/` - Mustache templates
  - Static file hosting configuration

## Component Patterns

### Web Components (punkt-elements)
```typescript
// Lit-based web component with Shadow DOM
@customElement('pkt-button')
export class PktButton extends LitElement {
  @property({ type: String }) variant = 'primary'
  @property({ type: Boolean }) disabled = false

  render() {
    return html`<button>${this.slot}</button>`
  }
}
```

### React Wrappers (punkt-react)
```typescript
// React wrapper using forwardRef
export const PktButton = forwardRef<HTMLButtonElement, IPktButton>(
  ({ variant, disabled, children, ...props }, ref) => {
    return <button ref={ref} className={`pkt-btn pkt-btn--${variant}`} />
  }
)
```

### CSS Naming (BEM-inspired)
```scss
.pkt-button                  // Block
.pkt-button--primary         // Modifier
.pkt-button__icon            // Element
```

## Development Workflow

### Key Scripts
- `npm run build` - Build all packages
- `npm run dev-docs` - Run documentation site locally
- `npm run dev-react` - Develop React components with HMR
- `npm run dev-elements` - Develop web components with HMR
- `npm run test-elements` - Run element tests
- `npm run test-react` - Run React tests
- `npm run lerna:publish` - Publish packages to NPM

### Build System
- **Vite** for fast builds and HMR
- **TypeScript** for type safety (declaration files generated)
- **Nx** for build caching and task orchestration
- **Lerna** for versioning and publishing

### Testing Strategy
- **Unit tests**: Vitest for components
- **Integration tests**: Testing Library (DOM/React)
- **Accessibility tests**: jest-axe for a11y validation
- **Coverage**: Tracked per package

### Versioning
- **Semantic versioning** (major.minor.patch)
- **Conventional Commits** for changelogs
- **Automated**: Lerna handles versioning and publishing
- **Current**: v13.12.0 (most packages at v13.11.0 or v13.12.0)

## Key Conventions

### File Organization
- TypeScript source in `/src/` or `/lib/`
- Tests colocated with components (`.test.ts`, `.test.tsx`)
- Styles in component directories or separate `/styles/` folder
- Build outputs in `/dist/`

### Naming Conventions
- Components: PascalCase (PktButton, PktAccordion)
- Custom elements: kebab-case with `pkt-` prefix (pkt-button, pkt-accordion)
- CSS classes: BEM-inspired with `pkt-` prefix
- Files: kebab-case for components, camelCase for utilities

### Accessibility Requirements
- ARIA attributes required on interactive components
- Keyboard navigation support mandatory
- Screen reader testing with jest-axe
- WCAG 2.1 AA compliance target

### Language
- **UI text**: Norwegian (Bokmål)
- **Documentation**: Norwegian
- **Code**: English (variable names, comments)

## Important Notes for LLMs

1. **Primary component library**: `punkt-elements` (Lit web components) is the core. `punkt-react` wraps these for React users.

2. **Deprecation**: `punkt-vue` is legacy and being phased out. New development should use `punkt-elements`.

3. **Inter-package dependencies**: React components depend on elements, CSS, and assets. Changes to elements may require React wrapper updates.

4. **Testing required**: All components must have unit tests and accessibility tests before publishing.

5. **Norwegian context**: User-facing text is in Norwegian. Keep this when adding new UI strings.

6. **Monorepo commands**: Use Lerna for cross-package operations. Nx handles caching.

7. **Version sync**: Packages are versioned together but may have different version numbers if not changed in a release.

8. **Build before test**: Some tests require built artifacts. Run `npm run build` if tests fail unexpectedly.

## Common File Locations

- Root config: `/lerna.json`, `/nx.json`, `/package.json`
- TypeScript config: `/tsconfig.json`, `/tsconfig.*.json`
- Package configs: `/packages/*/package.json`
- Component source: `/packages/punkt-elements/src/components/`
- React source: `/packages/punkt-react/lib/`
- SASS source: `/packages/punkt-css/scss/`
- Icons: `/packages/punkt-assets/src/icons/`
- Docs pages: `/apps/docs-astro/src/pages/`
- Test utilities: `/packages/punkt-testing-utils/src/`

## CI/CD

- **GitHub Actions** workflows in `/.github/workflows/`
- Automated builds on PR
- Automated publishing on main branch
- PR preview deployments for docs
- NPM publishing with provenance



---


# Project README


<h1 align="center">
  <img alt="Punkt logo" src="https://cdn-nocors.punkt.oslo.systems/latest/icons/punkt-circle-blue.svg" width="224"/><br/>
  Punkt designsystem
</h1>

<p align="center">Utvikles av <a href="https://labs.oslo.kommune.no/" 
  target="_blank">Oslo Origo</a> for å gjøre det enklere og mer inspirerende for 
  designere og utviklere i Origo å lage gjenkjennbare og UU-vennlige digitale
  løsninger for innbyggere i Oslo.
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@oslokommune/punkt-assets" target="_blank"><img src="https://img.shields.io/npm/v/@oslokommune/punkt-assets?logo=svg&label=ressurser&style=for-the-badge&color=FFB13B" alt="Ressurser" /></a>
  <a href="https://www.npmjs.com/package/@oslokommune/punkt-css" target="_blank"><img src="https://img.shields.io/npm/v/@oslokommune/punkt-css?logo=sass&label=css&style=for-the-badge&color=bf4080" alt="CSS-rammeverk" /></a>
  <a href="https://www.npmjs.com/package/@oslokommune/punkt-cli" target="_blank"><img src="https://img.shields.io/npm/v/@oslokommune/punkt-cli?logo=node.js&label=cli&style=for-the-badge&color=339933" alt="CLI verktøy" /></a>
  <a href="https://www.npmjs.com/package/@oslokommune/punkt-react" target="_blank"><img src="https://img.shields.io/npm/v/@oslokommune/punkt-react?logo=react&label=react&style=for-the-badge&color=61dafb" alt="React komponenter" /></a>
  <a href="https://www.npmjs.com/package/@oslokommune/punkt-vue" target="_blank"><img src="https://img.shields.io/npm/v/@oslokommune/punkt-vue?logo=vue.js&label=vue&style=for-the-badge&color=42b883" alt="Vue komponenter" /></a>
  <a href="https://www.npmjs.com/package/@oslokommune/punkt-elements" target="_blank"><img src="https://img.shields.io/npm/v/@oslokommune/punkt-elements?logo=webcomponentsdotorg&label=customelements&style=for-the-badge&color=bf4080" alt="Custom elements" /></a>
</p>

<br>

## 🧩 Bestanddeler

<table width="100%" cellpadding="25" class="table-centered">
<tbody>
  <tr valign="top">
    <td align="center" width="50%">
      <img alt="Figma logo" src="https://cdn-nocors.punkt.oslo.systems/latest/icons/figma.svg" height="100"/><br/>
      <h3>Figma</h3>
      <p>I Figma finnes visuell profil, design tokens, og spesifikasjoner til bl.a komponenter.</p>
      <p><a href="https://www.figma.com/file/Eej5jm3jIUjeMfzLE0aOTB/Punkt---Origo-designsystem?node-id=0%3A1&t=VDbEaltk80wYiYn3-0" target="_blank">Kom i gang (krever innlogging)</a></p>
    </td>
    <td align="center">
      <img alt="Sass logo" src="https://cdn-nocors.punkt.oslo.systems/latest/icons/sass.svg" height="100"/><br/>
      <h3>CSS</h3>
      <p>CSS-rammeverk med ressurser som SCSS og CSS.</p>
      <p><a href="https://www.npmjs.com/package/@oslokommune/punkt-css" target="_blank">punkt-css på NPM</a></p>
      <p><a href="https://github.com/oslokommune/punkt/blob/main/packages/css/README.md" target="_blank">Kom i gang</a></p>
    </td>
  </tr>
  <tr valign="top">
    <td align="center">
      <img alt="SVG logo" src="https://cdn-nocors.punkt.oslo.systems/latest/icons/svg.svg" height="100"/><br/>
      <h3>Ressurser</h3>
      <p>Fonter, logoer og ikoner.</p>
      <p><a href="https://www.npmjs.com/package/@oslokommune/punkt-assets" target="_blank">punkt-assets på NPM</a></p>
      <p><a href="https://github.com/oslokommune/punkt/blob/main/packages/assets/README.md" target="_blank">Kom i gang</a></p>
    </td>
    <td align="center">
      <img alt="React logo" src="https://cdn-nocors.punkt.oslo.systems/latest/icons/code.svg" height="100"/><br/>
      <h3>Punkt Elements</h3>
      <p>Vårt hovedkomponentbibliotek med custom elements (web components)</p>
      <p><a href="https://www.npmjs.com/package/@oslokommune/punkt-elements" target="_blank">punkt-elements på NPM</a></p>
      <p><a href="https://github.com/oslokommune/punkt/blob/main/packages/elements/README.md" target="_blank">Kom i gang</a></p>
    </td>
  </tr> 
  <tr valign="top">
    <td align="center">
      <img alt="React logo" src="https://cdn-nocors.punkt.oslo.systems/latest/icons/react.svg" height="100"/><br/>
      <h3>React komponenter</h3>
      <p>React komponentbibliotek.</p>
      <p><a href="https://www.npmjs.com/package/@oslokommune/punkt-react" target="_blank">punkt-react på NPM</a></p>
      <p><a href="https://github.com/oslokommune/punkt/blob/main/packages/react/README.md" target="_blank">Kom i gang</a></p>
    </td>
    <td align="center">
      <img alt="Vuejs logo" src="https://cdn-nocors.punkt.oslo.systems/latest/icons/vue.svg" height="100"/><br/>
      <h3>Vue komponenter</h3>
      <p>Vue komponentbibliotek. Ikke lenger oppdatert. Bruk Punkt Elements for å supplere manglende komponenter. Vil etterhvert erstattes helt med Punkt Elements.</p>
      <p><a href="https://www.npmjs.com/package/@oslokommune/punkt-vue" target="_blank">punkt-vue på NPM</a></p>
      <p><a href="https://github.com/oslokommune/punkt/blob/main/packages/vue/README.md" target="_blank">Kom i gang</a></p>
    </td>
  </tr>
  <tr valign="top">
    <td align="center" colspan="2">
      <img alt="Punkt logo" src="https://cdn-nocors.punkt.oslo.systems/latest/icons/punkt-circle-blue.svg" height="100"/><br/>
      <h3>Dokumentasjon</h3>
      <p>Nettstedet til designsystemet som inneholder all nødvendig info.</p>
      <p><a href="https://punkt.oslo.kommune.no" target="_blank">punkt.oslo.kommune.no</a></p>
    </td> 
  </tr>
</tbody>
</table>

## ⭐ Bidra

I tillegg til at `Punkt` skal gjøre det enklere og raskere å lage mer robuste løsninger i Oslo
Origo, skal det være enkelt og fint å vedlikeholde. Utviklingen skjer åpent på GitHub, og alle som ønsker
kan følge utviklingen, gjøre det enkelt å bidra og påvirke videreutviklingen.

Om du ønsker å bidra i utviklingen, enten med å foreslå forbedringer, kode ny funksjonalitet, rapportere
feil, rette feil, eller bare diskutere veien videre så foregår alt her i dette repoet på github.

- [Se oppgaver vi jobber med](https://github.com/orgs/oslokommune/projects/24/views/23)
- [Se åpne bugs](https://github.com/oslokommune/punkt/issues?q=is%3Aissue+is%3Aopen+label%3A%22🐞%20bug%22)
- [Foreslå forbedringer eller rapporter feil selv](https://github.com/oslokommune/punkt/issues/new)
- [Delta i diskusjonen](https://github.com/oslokommune/punkt/discussions)

Vi kommer til å lage en guide på nettsiden for hvordan du som utvikler kan bidra. Samme informasjon vil
ligge i `CONTRIBUTING.md` på github. Gjør deg også kjent med [våre regler for bidragsytere](https://github.com/oslokommune/punkt/blob/main/CODE_OF_CONDUCT.md) før du
starter, slik at vi får et positivt og fint fellesskap.

## 👮 Lisens

`Punkt` er distribuert under [MIT-lisens](https://github.com/oslokommune/punkt/blob/LICENSE)
for åpen kildekode.

![NPM License](https://img.shields.io/npm/l/@oslokommune/punkt-css?style=for-the-badge)
