# Font

**Generated**: 2025-11-06T10:52:48.972901
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/grunnleggende/ressurser/font.mdx`

---


# Font

<Lead contributeBox={false}>
  Oslo kommune har utviklet en egen skrifttype - Oslo Sans. Oslo Sans skal
  benyttes i all kommunikasjon fra Oslo kommune. Punkt bruker Oslo Sans.
</Lead>

Oslo sans kommer i fire ulike vekter: Light (300), Regular (400), Medium (500) og Bold (700).

Oslo Sans er tilgjengelig i filformatene woff og woff2. Vi anbefaler at du bruker Oslo Sans gjennom Punkts stilsett, men om du ønsker å laste ned fontene direkte kan du gjøre det via CDN.

| Skrifttype              | Lenke til CDN                                                                                               |
| :---------------------- | :---------------------------------------------------------------------------------------------------------- |
| OsloSans Bold           | [OsloSans-Bold.woff](https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Bold.woff)                     |
|                         | [OsloSans-Bold.woff2](https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Bold.woff2)                   |
| OsloSans Light          | [OsloSans-Light.woff](https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Light.woff)                   |
|                         | [OsloSans-Light.woff2](https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Light.woff2)                 |
| OsloSans Medium         | [OsloSans-Medium.woff](https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Medium.woff)                 |
|                         | [OsloSans-Medium.woff2](https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Medium.woff2)               |
| OsloSans Regular        | [OsloSans-Regular.woff](https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Regular.woff)               |
|                         | [OsloSans-Regular.woff2](https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Regular.woff2)             |
| OsloSans Regular Italic | [OsloSans-RegularItalic.woff](https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-RegularItalic.woff)   |
|                         | [OsloSans-RegularItalic.woff2](https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-RegularItalic.woff2) |

**NB!** Om du ønsker å låse til versjon bytter du ut `latest` med ønsket versjon.

## Eksempel på bruk i kode

Om du ønsker å ta i bruk fontene via NPM anbefaler vi å lese mer om [Installasjon](/kom-i-gang/for-utviklere) for å få en grundigere innføring av de ulike delene.

```css
@font-face {
  font-display: swap;
  font-family: Oslo Sans;
  font-style: normal;
  font-weight: 400;
  src:
    url(https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Regular.woff2)
      format("woff2"),
    url(https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Regular.woff)
      format("woff");
}

@font-face {
  font-display: swap;
  font-family: Oslo Sans;
  font-style: italic;
  font-weight: 400;
  src:
    url(https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-RegularItalic.woff2)
      format("woff2"),
    url(https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-RegularItalic.woff)
      format("woff");
}

@font-face {
  font-display: swap;
  font-family: Oslo Sans;
  font-style: normal;
  font-weight: 300;
  src:
    url(https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Light.woff2)
      format("woff2"),
    url(https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Light.woff)
      format("woff");
}

@font-face {
  font-display: swap;
  font-family: Oslo Sans;
  font-style: normal;
  font-weight: 500;
  src:
    url(https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Medium.woff2)
      format("woff2"),
    url(https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Medium.woff)
      format("woff");
}

@font-face {
  font-display: swap;
  font-family: Oslo Sans;
  font-style: normal;
  font-weight: 700;
  src:
    url(https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Bold.woff2)
      format("woff2"),
    url(https://punkt-cdn.oslo.kommune.no/latest/fonts/OsloSans-Bold.woff)
      format("woff");
}

body {
  color: #2a2859;
  font-family: "Oslo Sans", arial, sans-serif;
  font-size: 1rem;
  font-weight: 300;
  letter-spacing: normal;
  line-height: 1.5em;
}
```