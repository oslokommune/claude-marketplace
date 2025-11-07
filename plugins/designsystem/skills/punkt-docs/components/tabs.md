# Tabs

**Generated**: 2025-11-06T10:52:48.965961
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/tabs/index.mdx`
- `component-specs/tabs.json`
- `component-specs/tab-item.json`
- `packages/elements/src/components/tabs/tabs-context.ts`
- `packages/elements/src/components/tabs/tabitem.ts`
- `packages/elements/src/components/tabs/tabs.ts`
- `packages/elements/src/components/tabs/index.ts`

---

**Description**: 


## Documentation



# Tabs

<Lead releaseDate="29.01.2024" lastUpdated="17.10.2025">
  Tabs (faner) er en type navigasjon på en side som lar brukeren bytte mellom
  relatert innhold uten å forlate siden. Valgt fane påvirker innholdet i et
  avgrenset område under fanerekken. Tabs gjør det enkelt å navigere mellom
  ulike deler av samme kontekst.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ tabs: tabsSpec, tabItem: tabItemSpec }}
  previewJson={tabsPreviewJson}
  fullWidth
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Tag"
    skin="blue"
    href={getComponentHref("tag")}
    iconName="chevron-right"
    client:only="react"
  >
    Bruk tag for å formidle ekstra informasjon i fanen
  </PktLinkCard>
  <PktLinkCard
    title="Accordion"
    skin="blue"
    href={getComponentHref("accordion")}
    iconName="chevron-right"
    client:only="react"
  >
    Når innhold kan vises/skjules seksjonsvis i samme side
  </PktLinkCard>
  <PktLinkCard
    title="Breadcrumbs"
    skin="blue"
    href={getComponentHref("breadcrumbs")}
    iconName="chevron-right"
    client:only="react"
  >
    Når brukeren skal navigere mellom sider i et hierarki
  </PktLinkCard>
</div>

## Varianter

Du kan kombinere flere elementer i fanene:

| Variant            | Beskrivelse                             |
| ------------------ | --------------------------------------- |
| Kun tekst          | Enkelt felt for lengre tekst            |
| Ikon og tekst      | Ikon sammen med tekst                   |
| Tekst og tag       | Tekst med en tag for ekstra informasjon |
| Ikon, tekst og tag | Kombinasjon av ikon, tekst og tag       |

<ImageWrapper>
  <img
    src="/assets/komponenter/tabs/tabs-1.svg"
    alt="Varianter av tabs: kun tekst"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/tabs/tabs-2.svg"
    alt="Varianter av tabs: ikon og tekst"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/tabs/tabs-3.svg"
    alt="Varianter av tabs: tekst og tag"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/tabs/tabs-4.svg"
    alt="Varianter av tabs: ikon-tekst-tag"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk tabs når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "innholdet hører til samme side, men bør deles opp i mindre seksjoner",
    "du vil gjøre det enkelt å navigere uten å forlate konteksten",
  ]}
/>

### Unngå tabs når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "innholdet ikke hører naturlig sammen",
    "det blir så mange faner at de skaper støy eller forvirring",
    "innholdet heller bør vises som en egen side eller seksjon",
  ]}
/>

### Skriv korte titler

Tittelen på en fane bør være kort, tydelig og beskrive panelet den åpner. Lange titler eller tekst som går over flere linjer gir dårlig lesbarhet.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/tabs/tabs-5.svg",
    imgAlt: "Gjør slik – korte og presise fanetitler",
    caption: "Bruk korte og presise titler i faner",
  }}
  badExample={{
    image: "/assets/komponenter/tabs/tabs-6.svg",
    imgAlt: "Unngå – lange fanetitler over flere linjer",
    caption: "Unngå lange og uklare fanetitler",
  }}
/>

### Antall faner

Gjør en vurdering av hvor mange faner løsningen trenger. For mange faner kan oppleves overveldende. På små skjermer vil overskytende faner få horisontal scroll.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/tabs/tabs-7.svg",
    imgAlt: "Gjør slik – begrenset antall faner for oversiktlighet",
    caption: "Bruk et begrenset antall faner for oversiktlighet",
  }}
  badExample={{
    image: "/assets/komponenter/tabs/tabs-8.svg",
    imgAlt: "Unngå – for mange faner på samme nivå",
    caption: "Unngå for mange faner på samme nivå",
  }}
/>

### Tags og ikoner

Unngå å bruke kun ikoner som titler på faner, og sørg for at eventuelle ikoner kommuniserer hvilken type innhold som er i fanen.

Dersom du bruker tags kan du selv velge hvilken farge du ønsker å ta i bruk basert på innholdet eller budskapet du ønsker å formidle. <a href={getComponentHref("tag")}>Les mer om god bruk av tags her</a>.

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/tabs/tabs-9.svg"
    alt="Varianter av tabs: kun tekst"
    aria-hidden="true"
  />
</ImageWrapper>

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/tabs/tabs-10.svg",
    imgAlt: "Gjør slik – bruk ikoner og tags for å tydeliggjøre innhold",
    caption: "Bruk ikoner og tags for å tydeliggjøre innhold",
  }}
  badExample={{
    image: "/assets/komponenter/tabs/tabs-11.svg",
    imgAlt: "Unngå – uklare ikoner og utydelige tags",
    caption: "Unngå faner med ikoner som ikke gir mening og uklare tags",
  }}
/>
</ContentSection>

## Responsivitet

- Tabs skal alltid ligge over innholdet de styrer
- På små skjermer vil fanerekken kunne scrolle horisontalt
- Test at titler, ikoner og tags skalerer godt på mobil og nettbrett

<ImageWrapper>
  <img
    src="/assets/komponenter/tabs/tabs-12.svg"
    alt="Tabs i mobilkontekst med horisontal scroll"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

- Én fane vil alltid være aktiv, slik at ett panel alltid er synlig
- Første fane skal være aktiv ved første besøk på en side
- Faner som brukes som inline navigasjon følger WAI-ARIA sine krav til tabs
- Dersom fanene brukes som lenker, oppfører de seg som en vanlig lenkemeny
- Tastaturnavigasjon må være støttet: bruk “pil høyre/venstre” for å navigere mellom faner og “enter” for å velge

<div class="cards-container">
  <PktLinkCard
    title="Tabs (WAI-ARIA)"
    skin="beige"
    href="https://www.w3.org/WAI/ARIA/apg/patterns/tabs/"
    iconName="chevron-right"
    client:only="react"
  >
    Beskriver hvordan du gjør tabs tilgjengelig
  </PktLinkCard>
</div>
</ContentSection>

## Anatomi

| Element            | Beskrivelse                                |
| ------------------ | ------------------------------------------ |
| Aktiv fane         | Fane som er valgt og styrer synlig innhold |
| Sidetittel på fane | Teksten som beskriver innholdet            |
| Tag (valgfritt)    | Tilleggsinformasjon                        |
| Ikon (valgfritt)   | Støtter fanens innhold visuelt             |
| Ikke aktiv fane    | Andre tilgjengelige valg                   |
| Aktiv linje        | Markering under aktiv fane                 |
| Skillelinje        | Skiller faner fra innholdet under          |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/tabs/tabs-13.svg"
    alt="Anatomi for tabs"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="tabs" extraSpecs={["tab-item"]} />
</ContentSection>

## Props

### PktTabs

<SpecList specName="tabs" />

### PktTabItem

<SpecList specName="tab-item" />


---


### Component Specification

**Element name**: `pkt-tabs`

**React component**: `PktTabs`

**CSS class**: `.pkt-tabs`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `tabs` | `tabs` | array | `-` | Liste med lenker eller funksjoner for hver tab (Gammel måte å sette opp tabs på, bruk heller PktTabItem inni PktTabs) |
| `arrowNav` | `arrow-nav` | boolean | `True` | Aktiverer piltastnavigasjon mellom tabs. Skrur også på role='tab' og aria-selected attributter. |
| `disableArrowNav` | `disable-arrow-nav` | boolean | `False` | Deaktivering av piltastnavigasjon (f.eks. for ren navigasjonsmeny). Overstyrer arrowNav-propsen. |


#### Events

- **`onTabSelected`**: Returnerer indeksen til den klikkede taben (React)
- **`tab-selected`**: Returnerer indeksen til den klikkede taben



### Component Specification

**Element name**: `pkt-tab-item`

**React component**: `PktTabItem`

**CSS class**: `.pkt-tabs__button`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `active` | `active` | boolean | `False` | Er dette den aktive taben? |
| `href` | `href` | string | `-` | URL for taben. Hvis satt, rendres taben som en lenke. |
| `icon` | `icon` | icon | `-` | Navnet på ikonet som skal vises |
| `tag` | `tag` | string | `-` | Tekst som vises i en tag på taben |
| `tagSkin` | `tag-skin` | `blue`, `green`, `red`, `beige`, `yellow`, `grey`, `gray`, `blue-light` | `blue` | Utseendet til tag-en |
| `index` | `index` | number | `0` | Tabens indeks i listen. Brukes for navigasjon og callbacks. Må settes eksplisitt når tabs mappes. |
| `controls` | `controls` | string | `-` | Setter aria-controls attributtet på taben |


#### Events

- **`click`**: Utløses når taben klikkes. Mottar event-objektet som parameter.


