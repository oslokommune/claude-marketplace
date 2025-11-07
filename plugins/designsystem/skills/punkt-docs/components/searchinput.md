# Search input

**Generated**: 2025-11-06T10:52:48.961030
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/searchinput/index.mdx`
- `component-specs/searchinput.json`

---

**Description**: 


## Documentation



# Search input

<Lead releaseDate="29.11.2023" lastUpdated="23.04.2025">
  Search input (søkefelt) lar brukeren navigere ved å skrive inn nøkkelord eller
  setninger og få opp relevante resultater. Komponentens formål er å hjelpe
  brukeren å finne fram til riktig innhold, enten i hele løsningen eller
  innenfor et avgrenset område.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ searchinput: searchInputSpec }}
  previewJson={searchInputPreviewJson}
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Text input"
    skin="blue"
    href={getComponentHref("textinput")}
    iconName="chevron-right"
    client:only="react"
  >
    For enkel fritekstskriving uten søkefunksjonalitet.
  </PktLinkCard>
  <PktLinkCard
    title="Combobox"
    skin="blue"
    href={getComponentHref("combobox")}
    iconName="chevron-right"
    client:only="react"
  >
    Kombinerer søkefelt med en nedtrekksliste.
  </PktLinkCard>
  <PktLinkCard
    title="Select"
    skin="blue"
    href={getComponentHref("select")}
    iconName="chevron-right"
    client:only="react"
  >
    Select gir brukeren faste valgmuligheter i en liste.
  </PktLinkCard>
</div>

## Varianter

### Varianter

| Variant         | Bruk                                                               |
| --------------- | ------------------------------------------------------------------ |
| Kun tekst       | Standard variant                                                   |
| Med ikon        | Når ikonet skal understøtte eller forsterke teksten                |
| Med “lukk”-ikon | Når tag brukes til filtrering og brukeren skal kunne fjerne valget |

<ImageWrapper>
  <img
    src="/assets/komponenter/searchinput/searchinput-1.svg"
    alt="Varianter: kun tekst"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/searchinput/searchinput-2.svg"
    alt="Varianter: med ikon"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/searchinput/searchinput-3.svg"
    alt="Varianter: med lukk-ikon"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk search input når

<ListWhenToUseOrNot
  icon="success"
  items={[
    `du ønsker at brukeren skal kunne søke i hele løsningen (globalt søk)`,
    `brukeren skal filtrere eller søke i et avgrenset område (lokalt søk)`,
  ]}
/>

### Unngå search input når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `det er få valg eller resultater (bruk <a href=${getComponentHref("select")}>select</a>, <a href=${getComponentHref("checkbox")}>checkbox</a> eller <a href=${getComponentHref("radiobuttons")}>radio button</a> i stedet)`,
    `du trenger kombinasjon av søk og valgliste (bruk <a href=${getComponentHref("combobox")}>combobox</a> i stedet)`,
  ]}
/>

### Globalt (overordnet) søk

Globalt søk skal brukes når søkefeltet søker gjennom hele løsningen eller nettstedet og skal kun
brukes i Oslo kommunes felles header.

<ImageWrapper>
  <img
    src="/assets/komponenter/searchinput/searchinput-4.svg"
    alt="Globalt overordnet søk"
    aria-hidden="true"
  />
</ImageWrapper>

### Lokalt søk

Lokalt søk brukes når brukeren skal filtrere eller søke i et mindre element på en side eller i en
løsning, for eksempel oppramsning av tilgjengelige pasienter eller en liste med elementer.

<ImageWrapper>
  <img
    src="/assets/komponenter/searchinput/searchinput-5.svg"
    alt="Lokalt søk"
    aria-hidden="true"
  />
</ImageWrapper>

### Plassholdertekst og label

Om du ønsker kan søkefeltet brukes sammen med ledetekst (label), men det er ikke påkrevd. I de fleste tilfeller er det
unødvendig med en synlig ledetekst over søkefeltet. Utformingen av søkefeltet, knappen og søkeikonet gjør funksjonen
tydelig for brukeren.

Søk er det eneste inputfeltet i designsystemet som kan brukes med kun plassholdertekst, fordi feltets funksjon er
tydelig selv når teksten forsvinner ved klikk.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/searchinput/searchinput-6.svg",
    imgAlt: "Gjør slik – logisk og tydelig label/placeholder som beskriver innholdet",
    caption: "Skriv logisk og tydelig label og plassholdertekst som hjelper brukeren med hva slags innhold de skal fylle inn",
  }}
  badExample={{
    image: "/assets/komponenter/searchinput/searchinput-7.svg",
    imgAlt: "Unngå – for generell plassholdertekst",
    caption: "Unngå for generell plassholdertekst som ikke gir brukeren indikasjon på hva de kan søke etter",
  }}
/>
</ContentSection>

## Responsivitet

På mobil legger det overordnede søket seg som et forstørrelsesglassikon. Ved klikk åpnes søkefeltet
under headeren. Lokale søk skal ligge over innholdet de filtrerer eller søker i.

<ImageWrapper>
  <img
    src="/assets/komponenter/searchinput/searchinput-8.svg"
    alt="Responsiv oppførsel for globalt søk"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/searchinput/searchinput-9.svg"
    alt="Responsiv oppførsel for lokalt søk"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

- Label må alltid finnes i koden, selv når den ikke er synlig
- “ESC” sletter teksten i feltet
- “Enter” utfører søket
- Søkeforslag må være navigerbare med piltaster og ha riktige ARIA-attributter

</ContentSection>

## Anatomi

| Element          | Beskrivelse                                                 |
| ---------------- | ----------------------------------------------------------- |
| Inputfelt        | Feltet der brukeren skriver søket                           |
| Plassholdertekst | Viser brukeren hva de kan søke etter                        |
| Knapp/ikon       | Brukes for å sende inn søket                                |
| Label            | Ledetekst (kan være skjult visuelt men skal finnes i koden) |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/searchinput/searchinput-10.svg"
    alt="Anatomi for globalt søk"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/searchinput/searchinput-11.svg"
    alt="Anatomi for lokalt søk"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="searchinput" />
</ContentSection>

## Props

<SpecList specName="searchinput" />


---


### Component Specification

**Element name**: `pkt-searchinput`

**React component**: `PktSearchInput`

**CSS class**: `.pkt-searchinput`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `name` | `name` | string | `-` | Navn som sendes brukes i skjema ved innsending |
| `id` | `id` | string | `-` | ID-en til søkefeltet |
| `appearance` | `appearance` | `local`, `local-with-button`, `global` | `local` | Utseende av søkefeltet |
| `placeholder` | `placeholder` | string | `-` | Tekst som vises i søkefeltet når det er tomt |
| `value` | `value` | string | `-` | Verdien som er skrevet inn i søkefeltet |
| `disabled` | `disabled` | boolean | `False` | Er søkefeltet deaktivert? |
| `fullwidth` | `fullwidth` | boolean | `False` | Skal søkefeltet ta opp hele bredden? |
| `label` | `label` | string | `-` | Label for søkefeltet |
| `action` | `action` | string | `-` | Handling som utføres når søkefeltet endres |
| `suggestions` | `suggestions` | array | `[{'title': 'Oslo', 'text': 'Hovedstaden i Norge'}, {'title': 'Bergen', 'text': 'Vestlandets hovedstad'}, {'title': 'Trondheim', 'text': 'Teknologihovedstaden'}]` | Liste over forslag til søkefeltet |


#### Events

- **`change`**: Hendelse som utløses når verdien i søkefeltet endres
- **`search`**: Hendelse som utløses når søkefeltet blir søkt
- **`suggestionClick`**: Hendelse som utløses når et forslag blir klikket


