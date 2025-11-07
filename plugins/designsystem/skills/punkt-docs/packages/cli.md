# punkt-cli

**Generated**: 2025-11-06T10:52:48.929685
**Git Commit**: 05685b33
**Source Files**:
- `packages/cli/README.md`
- `packages/cli/package.json`

---

**Package**: @oslokommune/punkt-cli


## Bruk av punkt-cli

<a href="https://www.npmjs.com/package/@oslokommune/punkt-cli" target="_blank"><img src="https://img.shields.io/npm/v/@oslokommune/punkt-cli?logo=node.js&label=cli&style=for-the-badge&color=339933" alt="CLI verktøy" /></a>

OBS! Denne pakken er veldig utdatert og det er ingen situasjoner hvor du skulle trenge å bruke den.

Punkt har fått et kommandolinjeverktøy; `punkt` 🥳 for bruk i
terminalen eller scripts.

OBS: Denne pakken er utdatert og vi anbefaler å heller bruke manuelle prosesser og CDN som beskrevet på våre nettsider.

## 📝 Forutsetninger

Node >= 20.19.1 installert

## Installasjon

```sh
npm install -g @oslokommune/punkt-cli
```

## Tilgjengelige kommandoer

- `punkt` gir deg en oversikt over kommandoene og options.
- `punkt init` initierer designsystemet for bruk i din applikasjon.
  Lager også en `pkt.config.json` fil basert på valg som tas i oppsettet.
- `punkt svg sprite` generer svg sprites basert på `punkt.config.json`.

### punkt init

Denne kommandoen initierer designsystemet.

**Fordeler**

- Oppretter konfig-filen for deg.
- Gir deg muligheten til å installere andre pakker i designsystemet.
- Legger til grunnleggende SVG-ikoner i appen din, om du ønsker.
- Gir deg personaliserte tips basert på dine svar og `package.json` i applikasjonen
  din.

**punkt.config.json** kan eksempelvis se slik ut:

```json
{
  "svgsprite": {
    "files": [
      /* SVG-filer i svgsprite */ "../assets/src/icons/check.svg",
      "../assets/src/icons/24h.svg",
      "../assets/src/icons/share.svg"
    ],
    "output": {
      "fileType": "html" /* html|svg */,
      "filePath": "./index.html" /* sti til destinasjonsfilen */
    }
  }
}
```

### Punkt svg sprite

Komponentbibliotekene i Punkt designsystem forutsetter at en såkalt SVG Sprite eller
SVG Symbols er tilgjengelig på siden. Det kan du lese mer om her:
[Multi-Colored SVG Symbol Icons with CSS Variables](https://frontstuff.io/multi-colored-svg-symbol-icons-with-css-variables).

Denne kommandoen genererer en slik svgsprite for deg. Den trenger at
designsystemet er initiert.

Kommandoen er avhengig av følgende verdier i konfig:

- `svgsprite.files` --> Array med stier til SVG ikoner.
- `svgsprite.output.fileType` --> Streng bestående av en av disse verdiene:
  - `html` - svgsprite inlines i et element i en html-fil (se under).
  - `svg` - svgsprite skrives i en SVG-fil.
- `svgsprite.output.filePath` --> Streng bestående av sti til output-filen.

**MERK!** Om du velger å inline i en HTML-fil skal du legge til dette elementet«:

```html
<div id="pkt-icons-sprite"></div>
```

**Når brukes denne kommandoen?** Hver gang du legger til eller tar bort en SVG.

### Eksempel bruk

Hvis du har importert inn alert-information kan du nå ta den i bruk slik:

```html
<div class="pkt-alert">
  <span class="pkt-icon pkt-alert__icon">
    <svg viewBox="0 0 32 32" aria-hidden="true">
      <use href="#alert-information"></use>
    </svg>
  </span>
  <div class="pkt-alert__text">Bruk dette tekstfeltet til å skrive en kort varsling.</div>
</div>
```

## 🔢 Versjonering

Punkt bruker [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) for versjonering av pakkene.

## 👮 Lisens

`Punkt` er distribuert under [MIT-lisens](https://github.com/oslokommune/punkt/blob/main/packages/cli/LICENSE) for åpen kildekode.

![NPM License](https://img.shields.io/npm/l/@oslokommune/punkt-cli?style=for-the-badge)



## Package Metadata


- **Version**: 13.7.0

- **Name**: @oslokommune/punkt-cli

- **Description**: CLI-verkøyet til Punkt, et designsystem laget av Oslo Origo
