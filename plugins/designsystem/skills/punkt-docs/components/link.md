# Link

**Generated**: 2025-11-06T10:52:48.952268
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/link/index.mdx`
- `component-specs/link.json`
- `packages/elements/src/components/link/index.ts`
- `packages/elements/src/components/link/link.ts`

---

## Documentation



# Link

<Lead releaseDate="24.04.2023" lastUpdated="14.05.2025">
  Link (lenke) brukes for å sende brukeren til en annen nettside eller et annet
  sted i løsningen. Link skal være lett å kjenne igjen og forstå, og må derfor
  være tydelig både visuelt og språklig.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ link: linkSpec }}
  previewJson={linkPreviewJson}
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
    href={getComponentHref("Accordion")}
    iconName="chevron-right"
    client:only="react"
  >
    Når brukeren kan åpne og lukke innhold for å få mer informasjon.
  </PktLinkCard>
</div>

## Varianter

### Type og bruk

| Type         | Bruk                                                                 |
| ------------ | -------------------------------------------------------------------- |
| Intern link  | Link som leder til en side i samme løsning eller nettside            |
| Ekstern link | Link som leder til en ekstern nettside, skal merkes tydelig i linken |

<ImageWrapper>
  <img
    src="/assets/komponenter/link/link-1.svg"
    alt="Eksempel på intern link"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/link/link-2.svg"
    alt="Eksempel på ekstern link"
    aria-hidden="true"
  />
</ImageWrapper>
Viktig: Vi bruker ikke ekstern link-ikon. Les mer under retningslinjer for bruk.

<ContentSection backgroundColor="subtle-pale-blue">
  ## Retningslinjer for bruk

### Bruk link når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "du vil hjelpe brukeren å navigere til en annen side eller seksjon",
    "du trenger å lenke til tilleggsinformasjon",
    "du leder brukeren til en ekstern nettside eller fil",
  ]}
/>

### Unngå link når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "du skal utføre en handling som lagring eller innsending (bruk button)",
  ]}
/>

### Skriv tydelig og konkret linktekst

Linkteksten skal si hva som skjer når brukeren klikker på den, den skal gi mening også når den leses isolert (for eksempel i en linkliste på skjermleser).

Unngå utydelige tekster som "Klikk her", "Les mer" eller "Gå til".

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/link/link-3.svg",
    imgAlt:
      "Eksempel på klare og direkte tekster som gir brukeren indikasjon på hva som skjer etter klikk",
    caption:
      "Skriv klare og direkte tekster som gir brukeren indikasjon på hva som skjer etter klikk",
  }}
  badExample={{
    image: "/assets/komponenter/link/link-4.svg",
    imgAlt: "Eksempel på utydelige og generiske tekster",
    caption: "Unngå utydelige og generiske tekster",
  }}
/>
### Marker link med mer enn bare farge

Alle links må kunne oppdages uansett syn, situasjon eller utstyr. Bruk understrek eller et beskrivende ikon. Dersom du bruker ikon er det viktig at du har en klar og tydelig linktekst.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/link/link-5.svg",
    imgAlt: "Eksempel på Link somm markeres med ikon.",
    caption: "Link kan markeres med ikon",
  }}
  badExample={{
    image: "/assets/komponenter/link/link-6.svg",
    imgAlt: "Eksempel på link som kun markeres med farge.",
    caption: "Unngå at link kun markeres med farge",
  }}
/>
### Gå for én styling av lenker

Hold visuell stil konsekvent. Ikke bland farger, størrelser, ikoner eller varianter av linker.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/link/link-7.svg",
    imgAlt: "Eksempel på liste med linker",
    caption: "I en liste med linker burde alle ha samme styling",
  }}
  badExample={{
    image: "/assets/komponenter/link/link-8.svg",
    imgAlt: "Eksempel på ulike stil i liste med lenker",
    caption: "Unngå å variere mellom ulike linkstiler i samme kontekst",
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
    image: "/assets/komponenter/link/link-9.svg",
    imgAlt: "Eksempel på hvordan å markere lenker som åpner ny fane",
    caption:
      "Skriv alltid i linken hvis lenken åpner i ny fane og hvor den fører hen",
  }}
  badExample={{
    image: "/assets/komponenter/link/link-10.svg",
    imgAlt:
      "Eksempel på dårlig bruk av ekstern link-ikon og unnlate å skrive hvor linken fører",
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

Link fungerer automatisk på alle skjermstørrelser.

Du må selv teste at

- linken er tydelige og enkle å bruke, også på mobil
- tastaturnavigasjon er ivaretatt

<ImageWrapper>
  <img
    src="/assets/komponenter/link/link-11.svg"
    alt="Eksempel på link på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

### Link må være lette å oppdage og bruke

- Bruk understrek for å markere en link, ikke bare farge.
- Links må kunne brukes med tastatur og skjermleser.
- Fokusstil må være synlig.

### Linken må gi mening alene

Unngå flere linker med samme tekst på én side, med mindre de leder til samme sted. Skriv så konkret og presist som mulig.

Mer om universell utforming av links:

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

| Element         | Beskrivelse                                                   |
| --------------- | ------------------------------------------------------------- |
| 1. Linktekst    | Klikkbar tekst som forteller brukeren hva linken fører til    |
| 2. Ikon venstre | Ikon til venstre som viser at teksten er klikkbar (valgfritt) |
| 2. Ikon høyre   | Ikon til høyre som viser at teksten er klikkbar (valgfritt)   |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/link/link-12.svg"
    alt="Link anatomi"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="link" />

</ContentSection>

## Props

<SpecList specName="link" />


---


### Component Specification

**Element name**: `pkt-link`

**React component**: `PktLink`

**CSS class**: `.pkt-link`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `href` | `href` | string | `#` | URL til lenken |
| `target` | `target` | `_blank`, `_self`, `_parent`, `_top` | `_self` | Mål for lenken |
| `iconName` | `iconName` | icon | `-` | Ikon som skal vises ved siden av lenketeksten |
| `iconPosition` | `iconPosition` | `left`, `right` | `-` | Posisjonen til ikonet i forhold til lenketeksten |


