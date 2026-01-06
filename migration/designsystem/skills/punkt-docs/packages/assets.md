# punkt-assets

**Generated**: 2025-11-06T10:52:48.928952
**Git Commit**: 05685b33
**Source Files**:
- `packages/assets/README.md`
- `packages/assets/package.json`

---

**Package**: @oslokommune/punkt-assets


## Bruk av punkt-assets

<a href="https://www.npmjs.com/package/@oslokommune/punkt-assets" target="_blank"><img src="https://img.shields.io/npm/v/@oslokommune/punkt-assets?logo=svg&label=ressurser&style=for-the-badge&color=FFB13B" alt="Ressurser" /></a>

Denne pakken inneholder Punkts ressurser, og består i all hovedsak av svg-elementer.

## 📖 Innhold

```sh
@oslokommune/punkt-assets
 ├── fonts/                     # oslosans font
 ├── icons/                     # alle svg-ikoner
 ├── logos/                     # oslologo og diverse favicons
```

## 🚀 Kom i gang - npm

```sh
npm add @oslokommune/punkt-assets
```

Se eksempler på hvordan ta i bruk assets her:

- [Font](/kom-i-gang/for-utviklere/css#-kom-i-gang---npm)
- [Ikoner](/ressurser/ikoner/kode)
- [Logo](/ressurser/oslologo)

## 🏎️ Kom i gang - cdn

Ved å inkludere Punkts ressurser via vår CDN på
[punkt-cdn.oslo.kommune.no](https://punkt-cdn.oslo.kommune.no/),
er du kjapt igang uten noe byggesteg.

Du kan peke til SVG-ikoner, fonter og logoer.

Se tilgjengelige filer på [cdn](https://punkt-cdn.oslo.kommune.no/).

```html
<!doctype html>
<html lang="no">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Punkt</title>
    <link href="https://punkt-cdn.oslo.kommune.no/latest/css/pkt.min.css" rel="stylesheet" />
  </head>
  <body>
    <h1>Velkommen til Oslo Origo</h1>
    <img
      src="https://punkt-cdn.oslo.kommune.no/latest/logos/oslologo.svg"
      alt="Oslo kommune logo"
      height="64"
    />
  </body>
</html>
```

## 🔢 Versjonering

Punkt bruker [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) for versjonering av pakkene.

## 👮 Lisens

`@oslokommune/punkt-assets` er distribuert under [MIT-lisens](https://github.com/oslokommune/punkt/blob/main/packages/assets/LICENSE) for åpen kildekode.

![NPM License](https://img.shields.io/npm/l/@oslokommune/punkt-assets?style=for-the-badge)



## Package Metadata


- **Version**: 13.11.0

- **Name**: @oslokommune/punkt-assets

- **Description**: Punkt - designsystem av Oslo Origo - Assets
