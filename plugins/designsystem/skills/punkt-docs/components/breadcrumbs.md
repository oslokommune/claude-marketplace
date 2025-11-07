# Breadcrumbs

**Generated**: 2025-11-06T10:52:48.937709
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/breadcrumbs/index.mdx`
- `component-specs/breadcrumbs.json`

---

## Documentation



# Breadcrumbs

<Lead releaseDate="14.09.2023" lastUpdated="16.05.2025">
  Breadcrumbs (brødsmulesti) viser brukeren hvor de er i strukturen, og gjør det
  mulig å navigere tilbake til høyere nivå. Den hjelper brukeren med å forstå
  hierarkiet og finne veien tilbake.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ breadcrumbs: breadcrumbsSpec }}
  previewJson={breadcrumbsPreviewJson}
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Backlink"
    skin="blue"
    href={getComponentHref("backlink")}
    iconName="chevron-right"
    client:only="react"
  >
    En enkel lenke for å gå tilbake til forrige side eller et høyere nivå.
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

Punkt støtter både <a href={getComponentHref('backlink')}>backlink</a> og
breadcrumbs som navigasjonsmønstre. Du må være konsekvent i løsningen din og
kun bruke én av dem.

    | Type        | Bruk                                                                                   |
    |-------------|----------------------------------------------------------------------------------------|
    | Backlink    | Brukes for å gå ett steg tilbake, for eksempel til en overordnet side eller oversikt   |
    | Breadcrumbs | Viser hvor brukeren er i en hierarkisk struktur og gir mulighet til å hoppe til et hvilket som helst nivå |

Viktig: Hvis løsningen din skal brukes sammen med Oslo kommune sine åpne nettsider ([www.oslo.kommune.no](https://www.oslo.kommune.no)), skal du alltid bruke <a href={getComponentHref('backlink')}>backlink</a>, aldri breadcrumbs.

<ImageWrapper>
  <img
    src="/assets/komponenter/breadcrumbs/breadcrumbs-1.svg"
    alt="Backlink vs breadcrumbs."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue" class="article-section" contentWidth="wide">
## Retningslinjer for bruk

### Bruk breadcrumbs når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "løsningen har et tydelig hierarki",
    "du vil gi oversikt over hvor brukeren er i strukturen",
    "brukeren skal kunne hoppe tilbake til et overordnet nivå",
  ]}
/>

### Unngå breadcrumbs når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "hierarkiet er grunt (bruk heller backlink)",
    "brukerens vei tilbake ikke er entydig",
    "det finnes annen navigasjon som dekker behovet",
  ]}
/>

### Skriv korte og tydelige lenketekster

Hvert nivå bør ha et enkelt og beskrivende navn. Unngå tekniske eller interne
navn (f.eks. “/nav/root/sub/area”).

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/breadcrumbs/breadcrumbs-2.svg",
    imgAlt: "Eksempel på riktig innhold på breadcrumbs",
    caption: "Fortell brukeren tydelig hva de tidligere sidene omhandler",
  }}
  badExample={{
    image: "/assets/komponenter/breadcrumbs/breadcrumbs-3.svg",
    imgAlt: "Eksempel på ikke egnet innhold på breadcrumbs",
    caption: "Unngå lange titler og uklare sidetitler",
  }}
/>

</ContentSection>

## Responsivitet

Breadcrumbs bryter automatisk linje dersom det ikke er nok plass på én linje.

<ul>
  <li>Lenketekstene skaleres ikke ned</li>
  <li>Det er ingen automatisk forkorting eller komprimering (f.eks. «…»)</li>
  <li>Separatoren (>) vises mellom hvert nivå, uavhengig av skjermstørrelse</li>
</ul>

Sørg for at breadcrumbs fungerer visuelt i din løsning, spesielt hvis den vises sammen med tittel, filter eller toppnavigasjon.

Det vanligste er å gå for [backlink](https://punkt.oslo.kommune.no/latest/komponenter-og-maler/komponenter/backlink/) på mobil på grunn av mindre plass, du må selv vurdere hva som fungerer best i din løsning.

<ImageWrapper >
  <img
    src="/assets/komponenter/breadcrumbs/breadcrumbs-5.svg"
    alt="Breadcrumbs på mobil"
    aria-hidden="true"
  />

  <img
    src="/assets/komponenter/breadcrumbs/breadcrumbs-4.svg"
    alt="Breadcrumbs på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

### Lenketeksten må gi mening alene

Teksten i breadcrumbs skal være tydelig og fortelle brukeren hvor lenken går.
Unngå vage ord som bare «Tilbake», skriv heller «Tilbake til oversikten» eller
noe annet passende.

### Fokus og tastaturnavigasjon

Brukeren skal kunne navigere til breadcrumbs med Tab, og aktivere den med
Enter. Komponenten har synlig fokusindikator når den er aktiv.

### Ikke erstatt hovednavigasjonen

Ikke bruk breadcrumbs som eneste måte å navigere tilbake på. Den skal være et
hjelpetillegg, ikke erstatte hovedmenyen.

Les mer om universell utforming av breadcrumbs:

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

| Element        | Beskrivelse                                                                      |
| -------------- | -------------------------------------------------------------------------------- |
| 1. Lenke       | Viser hvert nivå i hierarkiet. Hver lenke tar brukeren til det tilhørende nivået |
| 2. Ikon        | Ikon mellom hvert nivå. Brukes for å skille nivåene                              |
| 3. Aktivt nivå | Viser gjeldende side. Den siste lenken i breadcrumbs-stien er ikke klikkbar      |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/breadcrumbs/breadcrumbs-6.svg"
    alt="Backlinks anatomi."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

Breadcrumbs er default en anchor-link komponent. Ønsker du å bruke React router(Link) kan du spesifisere dette i props navigationType med verdien router. Komponenten bør bare brukes med maks 4 lenker.

<TechDetails specName="breadcrumbs" />
</ContentSection>

## Props

<SpecList specName="breadcrumbs" />


---


### Component Specification

**Element name**: `pkt-breadcrumbs`

**React component**: `PktBreadcrumbs`

**CSS class**: `.pkt-breadcrumbs`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `breadcrumbs` | `breadcrumbs` | array | `[]` | Liste over brødsmuler |
| `navigationType` | `navigationType` | `router`, `anchor` | `anchor` | Hvordan skal brødsmulene navigeres? |


