# Link card

**Generated**: 2025-11-06T10:52:48.953497
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/linkcard/index.mdx`
- `component-specs/linkcard.json`
- `packages/elements/src/components/linkcard/linkcard.ts`
- `packages/elements/src/components/linkcard/index.ts`

---

## Documentation



# Link card

<Lead releaseDate="24.04.2023" lastUpdated="20.12.2024">
  Link card (lenkekort) er en utvidet lenke med ikon, tittel og beskrivende
  tilleggstekst. Du bruker link card når du vil lede brukeren videre, for
  eksempel inn til en ny tjeneste eller underside, og samtidig gi litt mer
  informasjon om hva de finner der.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ linkcard: linkcardSpec }}
  previewJson={linkcardPreviewJson}
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Button"
    skin="blue"
    href={getComponentHref("button")}
    iconName="chevron-right"
    client:only="react"
  >
    Ikoner brukes ofte i knapper for å understøtte handlinger.
  </PktLinkCard>
  <PktLinkCard
    title="Logged-in menu"
    skin="blue"
    href={getComponentHref("headermeny")}
    iconName="chevron-right"
    client:only="react"
  >
    Ikoner kan benyttes for å understreke menyelementer.
  </PktLinkCard>
  <PktLinkCard
    title="Accordion"
    skin="blue"
    href={getComponentHref("accordion")}
    iconName="chevron-right"
    client:only="react"
  >
    Når brukeren kan åpne og lukke innhold for å få mer informasjon.
  </PktLinkCard>
</div>

## Varianter

### Skins

Link card kommer i flere ulike stiler, du kan selv vurdere hvilken som ser best ut i din løsning og til ditt formål:

| Skin          | Beskrivelse                           |
| ------------- | ------------------------------------- |
| Transparent   | Transparent bakgrunn og ingen padding |
| Grey outline  | Kantlinje i lys grå                   |
| Beige outline | Kantlinje i lys beige                 |
| Blue          | Blå helfarget bakgrunn                |
| Beige         | Beige helfarget bakgrunn              |
| Green         | Grønn helfarget bakgrunn              |
| Grey          | Grå helfarget bakgrunn                |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/linkcard/linkcard-1.svg"
    alt="Eksempel på de ulike varianter av linkcard"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
  ## Retningslinjer for bruk

### Bruk link card når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "du vil lede brukeren videre til en ny side",
    "du har behov for å gi mer informasjon enn en vanlig lenke gir",
    "du skal presentere flere likeverdige innganger (for eksempel på en forside eller oversiktsside)",
  ]}
/>

### Unngå link card når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `én lenke alene er nok (bruk da vanlig <a href="${getComponentHref("link")}">link</a>)`,
    `kortet inneholder mange visuelle elementer, f.eks. bilder, knapper (bruk  <a href="${getComponentHref("card")}">card</a>)`,
  ]}
/>

### Skriv tydelig og konkret tekst

Tittelen og brødteksten skal sammen forklare hva brukeren finner, og hvorfor det er relevant.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/linkcard/linkcard-2.svg",
    imgAlt:
      "Eksempel på klare og direkte tekster som gir brukeren indikasjon på hva som skjer etter klikk",
    caption:
      "Skriv klare og direkte tekster som gir brukeren indikasjon på hva som skjer etter klikk",
  }}
  badExample={{
    image: "/assets/komponenter/linkcard/linkcard-3.svg",
    imgAlt: "Eksempel på utydelige og generiske tekster",
    caption: "Unngå utydelige og generiske tekster",
  }}
/>

### Bruk ikon som gir mening

Ikoner skal understøtte innholdet. Ikke bruk dekorative ikoner uten funksjon.

[Chevron](/ikoner) (pil) brukes for å indikere transportlenke i lenkelister.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/linkcard/linkcard-4.svg",
    imgAlt: "Eksempel på ikon som representerer temaet",
    caption: "Velg et ikon som representerer temaet",
  }}
  badExample={{
    image: "/assets/komponenter/linkcard/linkcard-5.svg",
    imgAlt:
      "Eksempel på ikoner som ikke har noen tydelig tilknytning til innholde",
    caption: "Unngå ikoner som ikke har noen tydelig tilknytning til innholdet",
  }}
/>

### Ikke bruk ekstern link-ikon

Ikonet kan misforstås og gi dårlig brukeropplevelse. Mange tror det betyr «åpnes i ny fane», andre tror det betyr
«ekstern side». Vi anbefaler å alltid bruke tekst for å forklare hva linken
leder til.

Du kan dypdykke i begrunnelsen for denne avgjørelsen i [artikkelen
hos Designsystemet](https://www.designsystemet.no/no/patterns/external-links) som
vi har vært med som bidragsytere i.

### Åpne i ny fane _kun_ når det er nødvendig

Som hovedregel åpnes links i samme fane. Åpning i ny fane bør kun brukes:

- Hvis brukeren risikerer å bli logget ut
- Hvis brukeren er midt i en prosess der data kan gå tapt

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/linkcard/linkcard-6.svg",
    imgAlt:
      "Eksempel på card som viser at lenken åpner i ny fane og hvor den fører hen",
    caption:
      "Skriv alltid i linken hvis lenken åpner i ny fane og hvor den fører hen",
  }}
  badExample={{
    image: "/assets/komponenter/linkcard/linkcard-7.svg",
    imgAlt:
      "Eksempel på ikke anbefalt bruk av ekstern link-ikon og mangel på å skrive hvor linken fører",
    caption:
      "Unngå å bruke ekstern link-ikon og unnlate å skrive hvor linken fører",
  }}
/>

### Gi beskjed ved filer og nedlasting

Gjør det tydelig hvis linken fører til en fil. Oppgi:

- Filtype (for eksempel PDF, DOCX)
- Eventuelt filstørrelse, særlig for store filer
- Hvis filen skal lastes ned, bruk download-attributt og informer i teksten.

</ContentSection>

## Responsivitet

Link card tilpasser seg automatisk skjermbredden. På store skjermer plasseres kortene ved siden av hverandre, vanligvis i rader med opptil tre i bredden. På mobil og små skjermer brytes layouten slik at hvert kort vises i full bredde under hverandre.

Tekststørrelsen skaleres ned på mobil (fra 24px til 20px).

Husk å sjekke at [kontrastforholdet mellom tekst og bakgrunn](/universell-utforming/kontrastsjekker/) holder WCAG-nivå, særlig hvis du endrer skin-varianten eller kombinerer cards med mørkere bakgrunner. Det er også viktig å kontrollere at det er nok luft mellom kortene, slik at de ikke glir visuelt sammen.

<ImageWrapper>
  <img
    src="/assets/komponenter/linkcard/linkcard-8.svg"
    alt="Link card"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
  ## Universell utforming

### Hele link card må fungere som en lenke

Link card er satt opp slik at hele kortet er klikkbart, ikke bare teksten eller ikonet. Når du bruker tastatur eller skjermleser, skal det være enkelt å navigere til kortet og aktivere det.

### Teksten må forklare hvor brukeren havner

Bruk alltid en konkret og beskrivende tittel, og suppler gjerne med en forklarende tillegstekst. «Les mer» eller «Trykk her» sier ingenting om hva brukeren får. En god link card gir både retning og forventning, også når den leses isolert med skjermleser.

### Skjermleser må få med seg hele innholdet

En skjermleser skal kunne lese opp både tittel og tilleggstekst slik at brukeren får nok informasjon til å vurdere om de vil klikke. Sørg for at all tekst ligger riktig strukturert i koden, og at rekkefølgen gir mening. Dekorative ikoner må merkes med `aria-hidden="true"`, slik at de ikke forstyrrer opplesningen.

### Ikke bruk like linktekster med ulik funksjon

Linkteksten må være unik for hvert kort – med mindre de faktisk leder til det samme. Flere like tekster på samme side skaper forvirring, spesielt for skjermleserbrukere. Skriv så konkret og presist du kan.

Mer om universell utforming av link card:

  <div class="cards-container">
    <PktLinkCard
      title="Lenker (UUtilsynet)"
      skin="beige"
      href="https://www.uutilsynet.no/veiledning/lenker/214"
      iconName="chevron-right"
      client:only="react"
    >
      Hvordan oppfylle WCAG krav til lenker forklart av UUtilsynet
    </PktLinkCard>
    <PktLinkCard
      title="Writing Hyperlinks (NNGroup)"
      skin="beige"
      href="https://www.nngroup.com/articles/writing-links/"
      iconName="chevron-right"
      client:only="react"
    >
      Beste praksis for å skrive linktekst
    </PktLinkCard>
  </div>
</ContentSection>

## Anatomi

| Element                     | Beskrivelse                                                   |
| --------------------------- | ------------------------------------------------------------- |
| 1. Ikon                     | Klikkbar tekst som forteller brukeren hva linken fører til    |
| 2. Lenketekst               | Ikon til venstre som viser at teksten er klikkbar (valgfritt) |
| 3. Tilleggstekst            | Ikon til høyre som viser at teksten er klikkbar (valgfritt)   |
| 4. Bakgrunn eller kantlinje | Dato eller tidsperiode (valgfritt)                            |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/linkcard/linkcard-9.svg"
    alt="Anatomi av link card."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
  ## Implementasjon i kode

<TechDetails specName="linkcard" />

</ContentSection>

## Props

<SpecList specName="linkcard" />


---


### Component Specification

**Element name**: `pkt-linkcard`

**React component**: `PktLinkCard`

**CSS class**: `.pkt-linkcard`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `title` | `title` | string | `-` | Tittelen til lenkekortet |
| `href` | `href` | string | `-` | URL til siden lenken skal peke til |
| `skin` | `skin` | `normal`, `no-padding`, `blue`, `beige`, `green`, `gray`, `beige-outline`, `gray-outline` | `-` | Velg utseende på lenkekortet |
| `iconName` | `iconName` | icon | `-` | Navn på ikonet som skal vises |
| `openInNewTab` | `openInNewTab` | boolean | `False` | Åpne lenken i ny fane |
| `external` | `external` | boolean | `False` | Lenken går til en ekstern side |



### TypeScript Interface

```typescript
export interface IPktLinkCard {
  title?: string
  href?: string
  iconName?: string
  external?: boolean
  openInNewTab?: boolean
  skin?: TLinkCardSkin
}
```
