# punkt-react

**Generated**: 2025-11-06T10:52:48.925878
**Git Commit**: 05685b33
**Source Files**:
- `packages/react/README.md`
- `packages/react/package.json`

---

**Package**: @oslokommune/punkt-react


## Bruk av punkt-react

<a href="https://www.npmjs.com/package/@oslokommune/punkt-react" target="_blank"><img src="https://img.shields.io/npm/v/@oslokommune/punkt-react?logo=react&label=react&style=for-the-badge&color=61dafb" alt="React komponenter" /></a>

Dette repoet inneholder Punkt sine UI-komponenter for React. Komponentene er laget for å fungere sammen med `@oslokommune/punkt-assets` og `@oslokommune/punkt-css`. De fleste komponenter tar i bruk custom elements fra `@oslokommune/punkt-elements`. Enn så lenge støtter vi ikke full bruk i server-side-genererte apper.

## 📝 Forutsetninger

Peer dependencies:

- nodejs `20.19.1`
- react `>= 18`
- @oslokommune/punkt-assets `*`
- @oslokommune/punkt-css `*`

## 🚀 Kom i gang - npm

### 1. Installer komponentbiblioteket

```sh
npm add @oslokommune/punkt-react
```

### 2. Importer komponentene

```js
// src/App.tsx

import { PktButton, PktTextInput } from "@oslokommune/punkt-react";

...

  <PktTextInput label="First name" id="firstName" />
  <PktButton skin="primary" variant="icon-left" iconName="user">
    Testbutton
  </PktButton>

```

## 🟪 Ikoner

Alle våre komponenter bruker PktIcon-komponenten for å importere
ikonene via vår [CDN](https://punkt-cdn.oslo.kommune.no/).

Om du har en content security policy(CSP) satt opp må du åpne for https://punkt-cdn.oslo.kommune.no/ i din CSP.

Les mer om ikoner [her.](/ressurser/ikoner/kode)

## 🧩 Komponentbiblioteket

For beskrivelse av hvordan ta i bruk hver enkelt komponent se [om komponenter](/komponenter/).

## 🔢 Versjonering

Punkt bruker [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) for versjonering av pakkene.

## 👮 Lisens

`Punkt` er distribuert under [MIT-lisens](https://github.com/oslokommune/punkt/blob/main/packages/react/LICENSE) for åpen kildekode.

![NPM License](https://img.shields.io/npm/l/@oslokommune/punkt-react?style=for-the-badge)



## Package Metadata


- **Version**: 13.15.1

- **Name**: @oslokommune/punkt-react

- **Description**: React komponentbibliotek til Punkt, et designsystem laget av Oslo Origo
