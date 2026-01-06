# Tag

**Generated**: 2025-11-06T10:52:48.967362
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/tag/index.mdx`
- `component-specs/tag.json`
- `packages/elements/src/components/tag/tag.ts`
- `packages/elements/src/components/tag/index.ts`

---

**Description**: Tag brukes for øke «information scent» for en lenke/knapp eller å legge en merkelapp på tekst eller tittel.


## Documentation


# Tag

<Lead releaseDate="12.06.2023" lastUpdated="31.10.2024">
  En tag (også kalt badge eller chip) brukes for å merke, kategorisere eller
  organisere innhold med korte nøkkelord. Den kan hjelpe brukeren å raskt skanne
  informasjon, skille mellom kategorier eller filtrere innhold.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ tag: tagSpec }}
  previewJson={tagPreviewJson}
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

### Varianter

| Variant         | Bruk                                                               |
| --------------- | ------------------------------------------------------------------ |
| Kun tekst       | Standard variant                                                   |
| Med ikon        | Når ikonet skal understøtte eller forsterke teksten                |
| Med “lukk”-ikon | Når tag brukes til filtrering og brukeren skal kunne fjerne valget |

<ImageWrapper>
  <img
    src="/assets/komponenter/tag/tag-1.svg"
    alt="Varianter: kun tekst"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/tag/tag-2.svg"
    alt="Varianter: med ikon"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/tag/tag-3.svg"
    alt="Varianter: med lukk-ikon"
    aria-hidden="true"
  />
</ImageWrapper>

### Størrelser

Tag finnes i flere størrelser og farger, og kan brukes med eller uten ikon. Når en tag brukes til
filtrering, kan den ha et “lukk”-ikon slik at brukeren kan fjerne valget.

| Størrelse        | Bruk                                                             |
| ---------------- | ---------------------------------------------------------------- |
| Small            | Når tagen brukes tett på annet innhold og trenger å være diskret |
| Medium (default) | Standardstørrelse som passer i de fleste tilfeller               |
| Large            | Når teksten er lengre eller tagen skal være mer fremtredende     |

<ImageWrapper>
  <img
    src="/assets/komponenter/tag/tag-4.svg"
    alt="Størrelser: Small"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/tag/tag-5.svg"
    alt="Størrelser: Medium"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/tag/tag-6.svg"
    alt="Størrelser: Large"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk tag når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "du skal merke eller gruppere informasjon etter nøkkelord",
    "du vil la brukeren filtrere på kategorier",
    "du trenger en kort og lettlest markør i grensesnittet",
  ]}
/>

### Unngå tag når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "informasjonen krever lengre forklaringer",
    "farge alene er brukt for å formidle mening",
    "du ønsker et interaktivt element som tar brukeren til en ny side eller løsning (bruk heller button)",
  ]}
/>

### Skriv korte og konsise tags

Sørg for at teksten i tagen er klar og konsis, det er viktig å bruke korte tekster for enkel skanning.
Bruk to ord kun om det er nødvendig for å beskrive statusen eller skille den fra en annen tag. Dersom
den skal bli lest av skjermleser må den også inkludere kontekst.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/tag/tag-3.svg",
    imgAlt:
      "Gjør slik – Skriv tydelige og korte tekster som gir mening i kontekst",
    caption: "Skriv tydelige og korte tekster som gir mening i kontekst",
  }}
  badExample={{
    image: "/assets/komponenter/tag/tag-4.svg",
    imgAlt: "Unngå – for korte og uklare tekster uten kontekst",
    caption: "Unngå for korte og uklare tekster uten kontekst",
  }}
/>

### Ikke bruk kun farge for å skille tags fra hverandre

Farge bør ikke brukes som det eneste middelet for å skille tags fra hverandre. Sørg for at
informasjonen som tillegges fargen også kommer tydelig frem i innholdet, via tekst og ikon. Dersom
du bruker egendefinerte farger, må kravene til minimum kontrast overholdes.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/tag/tag-5.svg",
    imgAlt: "Gjør slik – Bruk tekst og farge sammen for å tydeliggjøre status",
    caption: "Bruk tekst og farge sammen for å tydeliggjøre status",
  }}
  badExample={{
    image: "/assets/komponenter/tag/tag-6.svg",
    imgAlt: "Unngå – å bruke kun farge for å skille tags fra hverandre",
    caption: "Unngå å bruke kun farge for å skille tags fra hverandre",
  }}
/>

### Bruk av ikon i tags

Dersom du bruker ikon skal dette alltid vises på venstre side av teksten. Ikonet skal underbygge
teksten i tagen. Ikke bruk tag med kun ikon, dette gjør det vanskelig for brukeren å skjønne
betydningen.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/tag/tag-7.svg",
    imgAlt: "Gjør slik – Bruk ikon sammen med tekst for å underbygge innholdet",
    caption: "Bruk ikon sammen med tekst for å underbygge innholdet",
  }}
  badExample={{
    image: "/assets/komponenter/tag/tag-8.svg",
    imgAlt: "Unngå – tag med kun ikon eller ulogisk ikon",
    caption: "Unngå tag med kun ikon eller tag med ulogisk ikon",
  }}
/>
</ContentSection>

## Responsivitet

Tag skalerer godt på alle skjermstørrelser og bryter linjer der det er nødvendig.

På små skjermer bør du vurdere om mange tags kan gjøre grensesnittet uoversiktlig eller dytter ned
viktig innhold. Trunker eller avkort lange tekster for å unngå at de bygger for mange linjer.

<ImageWrapper>
  <img
    src="/assets/komponenter/tag/tag-9.svg"
    alt="Tag i bruk på små og store skjermer"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

### Teksten må gi mening i kontekst

En tag bør alltid ha en kort og tydelig tekst som gir mening når den leses opp av skjermlesere. Ikke
bruk generiske ord som “Ny” alene, men skriv for eksempel “Ny søknad” slik at sammenhengen blir
forståelig.

### Bruk aria-label for lukkbare tags

For lukkbare tags kan du sende inn en valgfri ariaLabel som gir skjermlesere mer informasjon. Denne
vil da leses opp i stedet for selve teksten i tagen. Uten ariaLabel vil skjermleseren lese opp
tekstinnholdet i tagen, etterfulgt av en standardbeskrivelse: “Klikk for å fjerne [tagtekst]”.

### Ikke bruk farge alene

Fargen på en tag blir ikke opplest av skjermlesere og er ikke nok som meningsbærer for brukere med
svakt eller dårlig syn. Sørg derfor for at informasjonen fargen skal formidle også kommer tydelig
frem i tekst eller ikon. Du kan også legge til skjult hjelpetekst som kun blir lest opp av skjermlesere.

### Tags som knapper

Når en tag kan lukkes eller klikkes, får den rollen som en knapp og skal kunne fokuseres og aktiveres
med tastatur. Sørg for at dette fungerer konsekvent.

</ContentSection>

## Anatomi

| Element          | Beskrivelse                                                 |
| ---------------- | ----------------------------------------------------------- |
| Ikon (valgfritt) | Understøtter teksten                                        |
| Tekst            | Kort og tydelig innhold som beskriver status eller kategori |
| Bakgrunn         | Bakgrunnsfarge for tag                                      |
| “Lukk”-ikon      | Brukes til filtrering slik at brukeren kan fjerne valget    |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/tag/tag-10.svg"
    alt="Anatomi for Tag"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="tag" />
</ContentSection>

## Props

<SpecList specName="tag" />


---


### Component Specification

**Element name**: `pkt-tag`

**React component**: `PktTag`

**CSS class**: `.pkt-tag`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `size` | `size` | `small`, `medium`, `large` | `medium` | Størrelsen på taggen |
| `iconName` | `iconName` | icon | `-` | Navnet på ikonet som skal vises i taggen |
| `skin` | `skin` | `blue`, `blue-light`, `blue-dark`, `green`, `red`, `beige`, `yellow`, `gray` | `blue` | Utseendet til taggen |
| `closeTag` | `closeTag` | boolean | `False` | Skal taggen ha en lukkeknapp? |
| `textStyle` | `textStyle` | `thin-text`, `normal-text` | `normal-text` | Stilen på teksten i taggen |
| `type` | `type` | `button`, `submit`, `reset` | `button` | Type tag, brukes for å spesifisere om det er en knapp, submit eller reset |
| `ariaLabel` | `ariaLabel` | string | `-` | aria-label for taggen, brukes for tilgjengelighet |



### TypeScript Interface

```typescript
export interface IPktTag {
  closeTag?: boolean
  size?: TPktSize
  skin?: TTagSkin
  textStyle?: string | null
  iconName?: PktIconName
  type?: TTagType
  ariaLabel?: IAriaAttributes['aria-label'] | null
}
```
