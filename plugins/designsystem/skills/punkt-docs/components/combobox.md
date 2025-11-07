# Combobox

**Generated**: 2025-11-06T10:52:48.942576
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/combobox/index.mdx`
- `component-specs/combobox.json`
- `packages/elements/src/components/combobox/index.ts`
- `packages/elements/src/components/combobox/combobox.ts`

---

**Description**: 


## Documentation


# Combobox

<Lead
  releaseDate="09.04.2024"
  lastUpdated="19.06.2025"
>
En combobox (multiselect, flervalg) kombinerer et tekstfelt med en nedtrekksliste. Den lar brukeren:

- Søke ved å skrive inn tekst (for å filtrere alternativer)
- Velge ett eller flere alternativer fra en forhåndsdefinert liste
- Legge til egne verdier dersom det er tillatt (valgfritt)

Formålet med en combobox er å gjøre det enklere for brukeren å finne eller legge inn riktig verdi, spesielt når det er mange alternativer.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ combobox: comboboxSpec }}
  previewJson={comboboxPreview}
  fullWidth
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Select"
    skin="blue"
    href={getComponentHref("select")}
    iconName="chevron-right"
    client:only="react"
  >
    For gruppering av tekst og innhold uten statushensikt.
  </PktLinkCard>
  <PktLinkCard
    title="Text input"
    skin="blue"
    href={getComponentHref("textinput")}
    iconName="chevron-right"
    client:only="react"
  >
    Alert kan brukes i en modal ved behov for kritisk informasjon.
  </PktLinkCard>
  <PktLinkCard
    title="Search input"
    skin="blue"
    href={getComponentHref("searchinput")}
    iconName="chevron-right"
    client:only="react"
  >
    Kan brukes for å vise status i tillegg til alert.
  </PktLinkCard>
</div>

## Varianter

Comboboxen kan brukes i to forskjellige typer:

| Type       | Bruk                                  |
| ---------- | ------------------------------------- |
| Enkeltvalg | Brukeren kan velge kun ett alternativ |
| Flervalg   | Brukeren kan velge flere alternativer |

<ImageWrapper>
  <img
    src="/assets/komponenter/combobox/combobox-1.svg"
    alt="Eksampel på enkeltvalg combobox"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/combobox/combobox-2.svg"
    alt="Eksampe flervalg combobox"
    aria-hidden="true"
  />
</ImageWrapper>

Når du bruker flervalg, blir valgene registrert som tags. Tagsene kan plasseres inne i, eller utenfor, feltet.

<ImageWrapper>
  <img
    src="/assets/komponenter/combobox/combobox-3.svg"
    alt="Eksampel på combobox."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/combobox/combobox-4.svg"
    alt="Eksampel combobox med valg som tags utenfor feltet"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

## Retningslinjer for bruk

### Bruk combobox når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "brukeren har mange valg og kan velge flere enn én",
    "du ønsker at brukeren skal kunne søke eller filtrere ",
    "brukeren skal kunne skrive inn fritekst",
  ]}
/>

### Unngå combobox når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `det er færre enn 3 alternativer å velge mellom (bruk heller <a href="${getComponentHref("checkbox")}">checkbox</a> eller <a href="${getComponentHref("radiobuttons")}">radiobutton</a>)`,
    `det er viktig at brukeren bare velger fra en fast liste`,
    `kun søk er nødvendig (bruk heller <a href="${getComponentHref("searchinput")}">search input</a>)`,
  ]}
/>

### Skriv tydelig label og hjelpetekst

Sørg for at label (etiketten) til comboboxen er beskrivende og gir brukeren en tydelig forståelse om hva som trengs av input. Bruk både label og hjelpetekst for å forklare regler som for eksempel maks antall valg eller fritekst.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/combobox/combobox-5.svg",
    imgAlt: "Eksempe på tydelige og klare etiketter og hjelpetekster",
    caption: "Skriv tydelige og klare etiketter og hjelpetekster.",
  }}
  badExample={{
    image: "/assets/komponenter/combobox/combobox-6.svg",
    imgAlt: "Eksempel på ufullstendig og uklar etikett og hjelpetekst",
    caption: "Unngå ufullstendig og uklar etikett og hjelpetekst.",
  }}
/>
### Beskriv mulighetene til brukeren Dersom du gir brukeren mulighet for å legge
til nye alternativer, forklar tydelig hvordan brukeren skal benytte comboboxen i
hjelpeteksten.

<ImageWrapper  backgroundColor="white">
  <img
    src="/assets/komponenter/combobox/combobox-7.svg"
    alt="Eksampel på combobox."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/combobox/combobox-8.svg"
    alt="Eksampel combobox med valg som tags utenfor feltet"
    aria-hidden="true"
  />
</ImageWrapper>
</ContentSection>

## Responsivitet

Combobox fungere godt på alle skjermstørrelser, inkludert mobil og nettbrett. Den tilpasser seg tilgjengelig plass, og både inputfelt og liste over alternativer bryter linjer der det er nødvendig.

Det er noen ting vi anbefaler at dere tester og vurderer når dere bruker combobox:

- Pass på at tags (i flervalg) ikke bygger for mange linjer eller blir visuelt overveldende. På smale skjermer bør lange verdier trunkeres, brytes eller skjules på en ryddig måte.
- Unngå at valgoversikten dekker for mye av skjermen. Du kan vurdere å bruke fullskjermsvisning av listen på små skjermer dersom det er mange valg.
- Comboboxen fungerer like godt i både stående og liggende visning. Likevel anbefaler vi at dere tester både på mobil og nettbrett.

<ImageWrapper>
  <img
    src="/assets/komponenter/combobox/combobox-9.svg"
    alt="Combobox på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

## Universell utforming

### Skjemaelementer skal ha en-kolonnes layout og synlig struktur

Skjemaelementer burde ha en en-kolonnes layout, og hvert element skal ha sin egen label for å beskrive bruk. Om label av en eller annen grunn ikke skal vises skal den fortsatt finnes, men bruke klassen pkt-sr-only slik at skjemaet fortsatt er brukervennlig.

### Alle felt må ha logisk label

Alle tekstfelt skal ha et tilknyttet label (ledetekst/etikett). Label bør være koblet til tekstfeltet i koden slik at skjermlesere kan lese opp riktig informasjon. Komplekse skjema kan kreve mer hjelp enn bare labels.

### Feilmeldinger skal være synlige og tydelige

Feilmeldinger bør være kodet som tekst og identifisere det spesifikke skjemaelementet hvor feilen oppstod. Feilmeldingen må beskrive feilen og være synlig uten at brukeren gjør noen ekstra handlinger.

Les mer om universell utforming av combobox:

<div class="cards-container">
  <PktLinkCard
    title="Ledetekster i skjema (UUtilsynet)"
    skin="beige"
    href="https://www.uutilsynet.no/veiledning/skjema/38#ledetekster_og_instruksjoner"
    iconName="chevron-right"
    client:only="react"
  >
    Skriv gode ledetekster og instruksjoner i skjema
  </PktLinkCard>
  <PktLinkCard
    title="Ledetekst i digitale løsninger (KS.no)"
    skin="beige"
    href="https://www.ks.no/fagomrader/digitalisering/digital-kompetanse/klart-sprak-i-digitale-selvbetjeningslosninger/"
    iconName="chevron-right"
    client:only="react"
  >
    Tips til hvordan du skriver gode, tydelige ledetekster
  </PktLinkCard>
</div>

</ContentSection>

## Anatomi

| Element            | Beskrivelse                                          |
| ------------------ | ---------------------------------------------------- |
| 1. Label           | Tittel/etikett over feltet (valgfritt)               |
| 2. Hjelpetekst     | Forklaring under feltet (valgfritt)                  |
| 3. Inputfelt       | Skrivefelt med autocomplete og visning av valg       |
| 4. Tags            | Valgte alternativer i flervalg                       |
| 5. Alternativer    | Liste over valg som kan søkes og velges fra          |
| 6. Valg alternativ | Valgt alternativ får aktiv checkbox og vises som tag |
| 7. Hover           | Visuell tilbakemelding ved hover og valgt tilstand   |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/combobox/combobox-10.svg"
    alt="Accordion anatomi."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="combobox" />
</ContentSection>

## Props

<SpecList specName="combobox" />


---


### Component Specification

**Element name**: `pkt-combobox`

**React component**: `PktCombobox`

**CSS class**: `.pkt-combobox`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `name` | `name` | string | `-` | Navn som brukes i skjema ved innsending |
| `id` | `id` | string | `-` | Unik ID for feltet |
| `label` | `label` | string | `-` | Tekst som vises over feltet |
| `placeholder` | `placeholder` | string | `-` | Spesifiserer en kort hint som beskriver forventet verdi av feltet. |
| `multiple` | `multiple` | boolean | `True` | Mulighet for å velge flere valg |
| `tagPlacement` | `tagPlacement` | `inside`, `outside` | `top` | Plassering av valgte verdier i feltet ved flervalg |
| `maxlength` | `maxlength` | number | `-` | Maks antall valg dersom flervalg er aktivert |
| `typeahead` | `typeahead` | boolean | `True` | Mulighet for automatisk utfylling av feltet fra listen over valg |
| `includeSearch` | `includeSearch` | boolean | `-` | Mulighet for å søke etter valg inni dropdown |
| `allowUserInput` | `allowUserInput` | boolean | `-` | Mulighet for å skrive inn egne verdier |
| `displayValueAs` | `displayValueAs` | `label`, `value`, `prefixAndValue` | `label` | Hvordan valgt verdi vises i feltet |
| `value` | `value` | string | `-` | Valgt verdi. Streng ved enkelt valg, array av strenger ved flervalg. |
| `helptext` | `helptext` | string | `-` | Hjelpetekst som vises over feltet |
| `helptextDropdown` | `helptextDropdown` | string | `-` | Hjelpetekst som vises over feltet |
| `helptextDropdownButton` | `helptextDropdownButton` | string | `Les mer` | Tekst som vises på knappen for å åpne/lukke utvidet hjelpetekst |
| `disabled` | `disabled` | boolean | `-` | Feltet er deaktivert |
| `hasError` | `hasError` | boolean | `-` | Feltet har en feil |
| `errorMessage` | `errorMessage` | string | `-` | Tekst som vises under feltet ved feil |
| `required` | `required` | boolean | `-` | Feltet må fylles ut |
| `requiredTag` | `requiredTag` | boolean | `-` | Viser en merking som indikerer at feltet er påkrevd |
| `requiredText` | `requiredText` | string | `-` | Tekst som vises i påkrevd-merkingen |
| `optionalTag` | `optionalTag` | boolean | `-` | Viser en merking som indikerer at feltet er valgfritt |
| `optionalText` | `optionalText` | string | `-` | Tekst som vises i valgfritt-merkingen |
| `tagText` | `tagText` | string | `-` | Tekst som vises i en tag ved siden av label |
| `fullwidth` | `fullwidth` | boolean | `-` | Skal feltet ta opp hele bredden? |
| `defaultOptions` | `defaultOptions` | array | `[]` | Liste over valg som kan velges, om options sendes inn som array med objekter (denne vil ikke modifiseres ved endring innad i komponenten) |
| `options` | `options` | array | `[]` | Liste over valg som kan velges, om options sendes inn som array med objekter |


