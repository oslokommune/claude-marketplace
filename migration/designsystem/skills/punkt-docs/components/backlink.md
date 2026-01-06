# Backlink

**Generated**: 2025-11-06T10:52:48.936680
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/backlink/index.mdx`
- `component-specs/backlink.json`
- `packages/elements/src/components/backlink/backlink.ts`
- `packages/elements/src/components/backlink/index.ts`

---

## Documentation



# Backlink

<Lead
  releaseDate="14.09.2023"
  lastUpdated="28.03.2025"
>
  Backlink (tilbake-lenke) hjelper brukeren med å forstå hvor de er, og gir en
  enkel måte å navigere tilbake til forrige steg i strukturen. Den bidrar til
  bedre oversikt og forutsigbarhet, særlig på undersider eller når man navigerer
  dypt i et hierarki.

Bruk backlink når du vil gi brukeren en ryddig og eksplisitt vei tilbake,
enten til en oversiktsside, et forrige steg eller en forside i en seksjon.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ backlink: backlinkSpec }}
  previewJson={backlinkPreviewJson}
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Breadcrumbs"
    skin="blue"
    href={getComponentHref("breadcrumbs")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du vil vise hele stien tilbake eller et høyere nivå i hierarkiet.
  </PktLinkCard>
  <PktLinkCard
    title="Button (med tilbake-ikon)"
    skin="blue"
    href={getComponentHref("button")}
    iconName="chevron-right"
    client:only="react"
  >
    Når “tilbake” er en aktiv handling brukeren må ta stilling til.
  </PktLinkCard>
  <PktLinkCard
    title="Header"
    skin="blue"
    href={getComponentHref("header")}
    iconName="chevron-right"
    client:only="react"
  >
    Header og header menu gir full tilgang til hovednavigasjonen.
  </PktLinkCard>
</div>

## Varianter

Punkt støtter både backlink og breadcrumbs som navigasjonsmønstre. Du må være konsekvent i løsningen din og kun bruke én av dem.

| Type        | Bruk                                                                                                      |
| ----------- | --------------------------------------------------------------------------------------------------------- |
| Backlink    | Brukes for å gå ett steg tilbake, for eksempel til en overordnet side eller oversikt                      |
| Breadcrumbs | Viser hvor brukeren er i en hierarkisk struktur og gir mulighet til å hoppe til et hvilket som helst nivå |

Viktig: Hvis løsningen din skal brukes sammen med Oslo kommune sine åpne
nettsider ([www.oslo.kommune.no](https://www.oslo.kommune.no)), skal du alltid
bruke backlink, aldri <a href={getComponentHref('breadcrumbs')}>breadcrumbs</a>.

<ImageWrapper>
  <img
    src="/assets/komponenter/backlink/backlink-1.svg"
    alt="Forskjellen mellom backlink og breadcrumb."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue" class="article-section" contentWidth="wide">

## Retningslinjer for bruk

### Bruk backlink når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "brukeren har navigert fra en liste eller oversikt",
    "du ikke bruker brødsmulesti, men trenger lokal tilbake-navigasjon",
    "du vil forsterke informasjonshierarkiet på siden",
  ]}
/>

### Unngå backlink når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "det allerede finnes annen navigasjon som dekker samme behov (for eksempel toppmenyen)",
    "brukerens vei tilbake ikke er entydig eller åpenbar",
    "du ikke vet hvilken vei tilbake som gir mening",
  ]}
/>

### Skriv tydelige lenketekster

Lenketeksten skal beskrive hvor brukeren kommer. Unngå vage tekster som bare «Tilbake».

Gode eksempler:

- «Tilbake til oversikten»
- «Tilbake til søkeresultatene»

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/backlink/backlink-2.svg",
    imgAlt: "Eksempel på riktig innhold på lenken",
    caption: "Gjør det tydelig for brukeren hvor de havner etter klikk",
  }}
  badExample={{
    image: "/assets/komponenter/backlink/backlink-3.svg",
    imgAlt: "Eksempel ikke egnet innhold på lenken",
    caption: "Unngå vage eller utydelige tekster, tilbake til hva?",
  }}
/>
</ContentSection>

## Responsivitet

### Backlink skal alltid plasseres øverst på siden

Backlink fungerer godt på både små og store skjermer. Backlink skaleres ikke
ned på små skjermer, men bryter linjer der det er nødvendig. Ikon og tekst
vises alltid sammen.

### Test plassering på mobil

På mobil vises backlink ofte øverst på siden. Pass på at den ikke konkurrerer med navigasjonsmeny eller tittel. Sørg for god luft over og under komponenten.

<ImageWrapper>
  <img
    src="/assets/komponenter/backlink/backlink-4.svg"
    alt="Backlink på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

## Universell utforming

### Lenketeksten må gi mening alene

Teksten i backlinken skal være tydelig og fortelle brukeren hvor lenken går.
Unngå vage ord som bare «Tilbake», skriv heller «Tilbake til oversikten» eller
noe annet passende.

### Fokus og tastaturnavigasjon

Brukeren skal kunne navigere til backlinken med Tab, og aktivere den med
Enter. Komponenten har synlig fokusindikator når den er aktiv.

### Ikke erstatt hovednavigasjonen

Ikke bruk backlink som eneste måte å navigere tilbake på. Den skal være et
hjelpetillegg, ikke erstatte hovedmenyen.

Les mer om universell utforming av backlink:

<div class="cards-container">
  <PktLinkCard
    title="WCAG 2.1 Link Purpose (W3C)"
    skin="beige"
    href="https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context.html"
    iconName="chevron-right"
    client:only="react"
  >
    Hvordan lenketekst skal gi mening uten å være avhengig av konteksten.
  </PktLinkCard>
  <PktLinkCard
    title="Universell utforming av lenker (UUtilsynet)"
    skin="beige"
    href="https://www.uutilsynet.no/veiledning/lenker/214"
    iconName="chevron-right"
    client:only="react"
  >
    Semantikk, lesbarhet og teknisk tilrettelegging i lenker og knapper.
  </PktLinkCard>
</div>

</ContentSection>

## Anatomi

| Element       | Beskrivelse                                                      |
| ------------- | ---------------------------------------------------------------- |
| 1. Ikon       | Et venstrevendt pilikon som signaliserer tilbake eller forrige   |
| 2. Lenketekst | Beskrivende tekst som forteller hvor brukeren kommer etter klikk |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/backlink/backlink-5.svg"
    alt="Backlinks anatomi."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="backlink" />
</ContentSection>

## Props

<SpecList specName="backlink" />


---


### Component Specification

**Element name**: `pkt-backlink`

**React component**: `PktBackLink`

**CSS class**: `.pkt-back-link`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `href` | `href` | String | `/` | URL til siden lenken skal peke til |
| `text` | `text` | String | `Forsiden` | Teksten til tilbake-lenken |
| `ariaLabel` | `ariaLabel` | String | `Gå tilbake til forrige side` | Teksten til navigasjonselementet som leses opp av skjermlesere |


#### Events

- **`onClick`**: React: Klikk-event for tilbake-lenken



### TypeScript Interface

```typescript
export interface IPktBackLink {
  href?: string
  text?: string
  ariaLabel?: string
}
```
