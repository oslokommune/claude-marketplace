# Table

**Generated**: 2025-11-06T10:52:48.964974
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/table/index.mdx`
- `component-specs/table.json`
- `component-specs/table-data-cell.json`

---

**Description**: Dokumentasjon og eksempler for opt-in styling av tabeller.


## Documentation


# Table

<Lead releaseDate="16.05.2024" lastUpdated="–">
  Tabeller brukes for å presentere strukturert data i rader og kolonner. De gjør
  det enklere å skanne, sammenligne og utføre handlinger på data. Tabellen kan
  inneholde interaktive elementer som lenker, knapper, inputfelt og
  avkrysningsbokser.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{
    table: tableSpec,
    "table-data-cell": tableDataCellSpec,
    "table-header-cell": tableHeaderCellSpec,
    "table-header": tableHeaderSpec,
    "table-row": tableRowSpec,
    "table-body": tableBodySpec,
  }}
  previewJson={tablePreviewJson}
  fullWidth
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Search input"
    skin="blue"
    href={getComponentHref("searchinput")}
    iconName="chevron-right"
    client:only="react"
  >
    For å gi brukeren mulighet til å filtrere og søke i tabellen
  </PktLinkCard>
  <PktLinkCard
    title="Checkbox"
    skin="blue"
    href={getComponentHref("checkbox")}
    iconName="chevron-right"
    client:only="react"
  >
    For å velge én eller flere rader for massehandlinger
  </PktLinkCard>
  <PktLinkCard
    title="Text input"
    skin="blue"
    href={getComponentHref("textinput")}
    iconName="chevron-right"
    client:only="react"
  >
    Når tabellen inneholder redigerbare felt
  </PktLinkCard>
</div>

## Varianter

### Størrelser

| Størrelse | Beskrivelse                                        |
| --------- | -------------------------------------------------- |
| Default   | For lesbarhet på desktop                           |
| Compact   | Når mange rader må få plass uten horisontal scroll |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/table/table-1.svg"
    alt="Størrelser: Default"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/table/table-2.svg"
    alt="Størrelser: Compact"
    aria-hidden="true"
  />
</ImageWrapper>

### Utseende/skin

| Skin  | Beskrivelse                                                 |
| ----- | ----------------------------------------------------------- |
| Basic | Hvit bakgrunn, grå skillelinjer                             |
| Zebra | Annenhver rad med lyseblå/grå bakgrunn for enklere skanning |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/table/table-3.svg"
    alt="Utseende: Basic"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/table/table-4.svg"
    alt="Utseende: Zebra"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk table når

<ListWhenToUseOrNot
  icon="success"
  items={[
    `du skal vise strukturert data i rader og kolonner`,
    `brukeren må kunne sammenligne flere poster side om side`,
    `det er behov for sortering, filtrering eller paginering`,
  ]}
/>

### Unngå table når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `du bare skal vise én post i detalj (bruk for eksempel <a href="${getComponentHref("card")}">card</a> i stedet)`,
    `dataene blir vanskelig å lese på små skjermer, og en annen visning fungerer bedre`,
    `du egentlig bare trenger en enkel liste`,
  ]}
/>

### Skriv tydelige og beskrivende kolonneoverskrifter

Bruk korte og konsise overskrifter som gjør det enkelt å forstå hva kolonnen inneholder.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/table/table-5.svg",
    imgAlt: "Gjør slik – klare og presise kolonneoverskrifter",
    caption:
      "Skriv klare og presise kolonneoverskrifter som gjør innholdet lett å forstå",
  }}
  badExample={{
    image: "/assets/komponenter/table/table-6.svg",
    imgAlt: "Unngå – uklare og ufullstendige kolonneoverskrifter",
    caption:
      "Unngå uklare og ufullstendige kolonneoverskrifter som gjør innholdet vanskelig å tolke",
  }}
/>

### Juster innhold riktig

Tekst skal venstrejusteres, mens tall og summeringer bør høyrejusteres for enklere skanning.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/table/table-7.svg",
    imgAlt: "Gjør slik – venstrejustert tekst og høyrejusterte tall",
    caption: "Tabell med venstrejustert tekst og høyrejusterte tall for enkel sammenligning",
  }}
  badExample={{
    image: "/assets/komponenter/table/table-8.svg",
    imgAlt: "Unngå – ulogisk og ulik justering",
    caption: "Unngå ulogisk og ulik justering som gjør det vanskelig å skanne innholdet",
  }}
/>
</ContentSection>

## Responsivitet

Table tilpasser seg tilgjengelig plass og vises ulikt avhengig av skjermstørrelse.

På mobil og små skjermer bygges radene i høyden. Vi anbefaler å unngå horisontal scrolling fordi
det kan være forvirrende for brukeren. Dersom du likevel velger å bruke horisontal scroll, bør du
alltid teste det nøye på målgruppen.

<ImageWrapper>
  <img
    src="/assets/komponenter/table/table-9.svg"
    alt="Table på små skjermer"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

### Innholdet må gi mening med skjermleser

Alle tabeller skal kodes semantisk med `<table>`, `<thead>`, `<tbody>`, `<th>` og `<td>`. Bruk `scope` for
å knytte kolonne- og radoverskrifter til cellene.

### Alle handlinger må være tilgjengelige med tastatur

Brukeren skal kunne navigere med “Tab” og “Shift+Tab”, og aktivere elementer med “Enter” eller “Mellomrom”.

### Sørg for tydelig kontrast og fokusmarkering

Tekst, linjer og bakgrunn skal ha tilstrekkelig kontrast, og fokus på interaktive elementer skal være synlig.

### Bruk caption ved behov

Hvis tabellen trenger en forklarende tittel, bruk `<caption>` slik at skjermlesere fanger det opp.

<div class="cards-container">
  <PktLinkCard
    title="Tilgjengelige tabeller (W3C)"
    skin="beige"
    href="https://www.w3.org/WAI/tutorials/tables/"
    iconName="chevron-right"
    client:only="react"
  >
    Teknikker for tilgjengelige tabeller hos W3C
  </PktLinkCard>
</div>
</ContentSection>

## Anatomi

| Element            | Beskrivelse                                             |
| ------------------ | ------------------------------------------------------- |
| Tittel (valgfritt) | Gir en overskrift som beskriver hva tabellen inneholder |
| Kolonneoverskrift  | Viser hva hver kolonne representerer                    |
| Celleinnhold       | Viser data eller handlinger i tabellen                  |
| Rad                | Grupperer innhold på tvers av kolonner                  |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/table/table-10.svg"
    alt="Anatomi for Table"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="table" />
</ContentSection>

## Props

### Table

<SpecList specName="table" />

### TableDataCell

<SpecList specName="table-data-cell" />


---


### Component Specification

**Element name**: `pkt-table`

**React component**: `PktTable`

**CSS class**: `.pkt-table`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `compact` | `compact` | boolean | `False` | Skal tabellen vises i kompakt modus? |
| `skin` | `skin` | `basic`, `zebra-blue` | `basic` | Utseendet til tabellen |
| `responsiveView` | `responsiveView` | boolean | `True` | Skal tabellen vises responsivt? |



### Component Specification

**Element name**: `pkt-table-data-cell`

**React component**: `PktTableDataCell`

**CSS class**: `.pkt-table__data-cell`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `dataLabel` | `dataLabel` | string | `-` | Etikett som brukes for responsiv visning av tabellen, typisk samme som kolonneoverskriften |


