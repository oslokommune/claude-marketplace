# punkt-vue

**Generated**: 2025-11-06T10:52:48.926925
**Git Commit**: 05685b33
**Source Files**:
- `packages/vue/README.md`
- `packages/vue/package.json`

---

**Package**: @oslokommune/punkt-vue


## Bruk av punkt-vue

<a href="https://www.npmjs.com/package/@oslokommune/punkt-vue" target="_blank"><img src="https://img.shields.io/npm/v/@oslokommune/punkt-vue?logo=vue.js&label=vue&style=for-the-badge&color=42b883" alt="Vue komponenter" /></a>

Dette repoet inneholder Punkt sine UI-komponenter for Vue 3. Komponentene er laget for å fungere sammen med `@oslokommune/punkt-assets` og `@oslokommune/punkt-css`. Dersom vi har komponenter som ikke eksisterer i Vue, kan man ta i bruk komponenter fra `@oslokommune/punkt-elements` i Vue.

## 📝 Forutsetninger

Peer dependencies:

- nodejs `20.19.1`
- vue `>= 3.0.0`
- @oslokommune/punkt-assets `>= 1.0`
- @oslokommune/punkt-css `>= 1.0`

## 🚀 Kom i gang - npm

### 1. Installer komponentbiblioteket

```sh
npm add @oslokommune/punkt-vue
```

### 2. Importer komponentene

```js
/* src/main.js

Velg å installere hele bundlen */
import { createApp } from 'vue'
import PktVue from '@oslokommune/punkt-vue'

const app = createApp({})

app.use(PktVue)

/* eller kun individuelle komponenter (med ikoner)*/
import { createApp } from 'vue'
import { PktHeader, PktFooter, PktIcon } from '@oslokommune/punkt-vue'

const app = createApp({})

app.component('pkt-header', PktHeader)
app.component('pkt-footer', PktFooter)
app.component('pkt-icon', PktIcon)
```

## 🟪 Ikoner

Alle våre komponenter bruker PktIcon-komponenten for å importere ikonene via vår [CDN](https://punkt-cdn.oslo.kommune.no/).

Om du har en content security policy(CSP) satt opp må du åpne for https://punkt-cdn.oslo.kommune.no/ i din CSP.

Les mer om ikoner [her.](/ressurser/ikoner/kode)

## 🔵 Bruk av `punkt-elements`

En del komponenter i punkt-vue-pakken tar i bruk elementer fra punkt-elements-pakken. Det skal i all hovedsak fungere veldig bra, men dersom dere skulle oppleve utfordringer med reaktive objekter eller verdier i slots, så kan det hjelpe å pakke innholdet i slots i en `div` eller annet wrapper-element. OG dersom dette skulle oppstå, ta gjerne kontakt med Punkt-teamet så vi kan feilsøke og forbedre koden vår!

Vi utvikler i dag ikke nye komponenter i Vue, så om dere ser komponenter dere ønsker å bruke i Vue som ikke eksisterer i punkt-vue-pakken, så kan dere bruke elementene fra punkt-elements-pakken som om de skulle vært Vue-komponenter.

## 🧩 Komponentbiblioteket

For beskrivelse av hvordan ta i bruk hver enkelt komponent se [om komponenter](/komponenter/).

## 🔢 Versjonering

Punkt bruker [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) for versjonering av pakkene.

## 👮 Lisens

`Punkt` er distribuert under [MIT-lisens](https://github.com/oslokommune/punkt/blob/main/packages/vue/LICENSE) for åpen kildekode.

![NPM License](https://img.shields.io/npm/l/@oslokommune/punkt-vue?style=for-the-badge)



## Package Metadata


- **Version**: 13.13.2

- **Name**: @oslokommune/punkt-vue

- **Description**: Vue komponentbibliotek til Punkt, et designsystem laget av Oslo Origo
