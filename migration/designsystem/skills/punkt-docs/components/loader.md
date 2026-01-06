# Loader

**Generated**: 2025-11-06T10:52:48.954855
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/loader/index.mdx`
- `component-specs/loader.json`
- `packages/elements/src/components/loader/loader.ts`
- `packages/elements/src/components/loader/index.ts`

---

## Documentation



# Loader

<Lead
  releaseDate="14.02.2024"
  lastUpdated="16.05.2025"
>
  Loader gir en visuell indikasjon på at noe lastes, og forteller brukeren at systemet jobber i bakgrunnen. Den bidrar til å redusere usikkerhet, og hjelper brukeren med å forstå at de må vente et øyeblikk før innholdet er klart.

Formålet med loader er å synliggjøre systemstatus og forbedre brukeropplevelsen i situasjoner med ventetid.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ loader: loaderSpec }}
  previewJson={loaderPreviewJson}
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Alert"
    skin="blue"
    href={getComponentHref("alert")}
    iconName="chevron-right"
    client:only="react"
  >
    For å forklare feil eller uventede lasteproblemer
  </PktLinkCard>
  <PktLinkCard
    title="Button"
    skin="blue"
    href={getComponentHref("button")}
    iconName="chevron-right"
    client:only="react"
  >
    Spinner kan brukes i Punkts button for å gi indikasjon på opplastning
  </PktLinkCard>
  <PktLinkCard
    title="Messagebox"
    skin="blue"
    href={getComponentHref("messagebox")}
    iconName="chevron-right"
    client:only="react"
  >
    Hvis du vil vise status eller forklaring i stedet for animasjon
  </PktLinkCard>
</div>

## Varianter

### Typer

I Punkt finnes det to ulike typer loader

| Type                 | Beskrivelse                                                                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Oslo-loader (shapes) | En animert bølge med Oslo-former som skifter mellom brandfargene. Egner seg godt til hele sider eller større seksjoner                                     |
| Spinner              | En klassisk roterende sirkel. Kommer i blå og regnbue, men du kan også bruke andre brandfarger. Egner seg godt i små elementer og komponenter, som knapper |

<ImageWrapper>
  <img
    src="/assets/komponenter/loader/loader-1.svg"
    alt="Oslo loader varianter"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/loader/loader-2.svg"
    alt="Oslo loader varianter"
    aria-hidden="true"
  />
</ImageWrapper>

### Farger

Spinner-varianten kan brukes i to ulike fargekombinasjoner

| Variant | Beskrivelse                                                 |
| ------- | ----------------------------------------------------------- |
| Blue    | Statisk Oslo-blå, brukes i formelle og nøytrale grensesnitt |
| Rainbow | Animeres med flere brandfarger, mer leken                   |

<ImageWrapper>
  <img
    src="/assets/komponenter/loader/loader-3.svg"
    alt="Oslo loader varianter"
    aria-hidden="true"
  />
</ImageWrapper>

### Størrelser

Begge variantene kommer i tre størrelser

| Variant          | Beskrivelse                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Small            | Brukes der plassen er begrenset, for eksempel inne i en knapp eller ved siden av et skjemafelt. Passer best med spinner-variant |
| Medium (default) | Standardstørrelse som passer godt til komponenter og seksjoner. Fungerer både med spinner og Oslo-loader                        |
| Large            | For større flater eller når loaderen skal være et sentralt blikkfang, som ved fullskjerm-visning                                |

<ImageWrapper>
  <img
    src="/assets/komponenter/loader/loader-4.svg"
    alt="Oslo loader størrelser"
    aria-hidden="true"
  />
  <br />
  <img
    src="/assets/komponenter/loader/loader-5.svg"
    alt="Oslo loader størrelser"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk loader når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "systemet henter data og brukeren må vente i mer enn 300 ms",
    "du laster inn hele sider, seksjoner eller komponenter",
    `du trenger å gi visuell tilbakemelding for handlinger (for eksempel i en <a href="${getComponentHref("button")}">button</a>)`,
  ]}
/>

### Unngå loader når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "innholdet laster raskere enn 300 ms (brukeren vil ikke bli påvirket)",
    "det er mer effektivt å vise skeleton eller tomtilstand mens man venter",
    `du allerede bruker en annen visuell indikator for status, som <a href="${getComponentHref("progressbar")}">progressbar</a> eller <a href="${getComponentHref("alert")}">alert</a>`,
  ]}
/>

### Velg riktig variant og plassering

Bruk Oslo-loader for større flater eller fullskjerm. Spinneren passer bedre i mindre områder, som knapper, skjemafelt eller under tabs.

### Legg til tekst ved lang ventetid

Dersom ventetiden overstiger 4 sekunder, bør du legge til en forklarende tekst som informerer brukeren om hva som skjer. Eksempel: «Laster inn oversikt over søknader...»

Dersom innholdet ikke lastes som forventet, vurder å bruke en alert for å informere om feilen eller hva brukeren bør gjøre videre.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/loader/loader-6.svg",
    imgAlt: "Eksempel på anbefalt bruk av loader",
    caption: "Gi brukeren en indikasjon på at noe skjer og hva hen venter på",
  }}
  badExample={{
    image: "/assets/komponenter/loader/loader-7.svg",
    imgAlt: "Eksempel på loader uten indikasjon  på hva som skjer",
    caption:
      "Unngå å la en loader stå lenge uten å gi brukeren en indikasjon på hva som skjer",
  }}
/>

</ContentSection>

## Responsivitet

### Automatisk skalering

Loader tilpasser seg tilgjengelig plass. På små skjermer legges loaderen midtstilt, med tekst under om nødvendig. Spinneren er godt egnet til kompakte flater, mens Oslo-loaderen gir bedre effekt på større skjermer eller flater.

### Tilgjengelighet på mobil

Når du bruker loader på mobil og nettbrett, må du teste at

- teksten under loaderen er synlig og lesbar
- animasjonen holder seg innenfor synsfeltet
- kontrasten er god nok, særlig ved bruk av egendefinerte farger
- trykkflater og knapper ikke havner bak en fullskjerm-loader

<ImageWrapper>
  <img
    src="/assets/komponenter/loader/loader-8.svg"
    alt="Loader mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
  ## Universell utforming

### Lesbarhet og skjermleser

Loader må kunne oppfattes av brukere som navigerer med skjermleser eller tastatur.

Du må

- legge til `aria-label="Laster inn"` eller bruke `role="status"` med en beskrivende tekst
- sørge for at loaderen fjernes fra DOM når lasting er fullført
- merke dekorative animasjoner med `aria-hidden="true"` slik at de ikke leses opp

I tillegg skal wrapper-elementet bruke `aria-live="polite"` for å gi skjermleseren beskjed om at innhold oppdateres.

Bruk `aria-busy="true"` på containeren mens innhold lastes inn, og sett det til false når oppdateringen er ferdig. Dette gir skjermleseren tydelig signal om at noe er i endring og at den bør vente før den leser opp nytt innhold.

Dersom det ikke sendes inn tekst til komponenten, brukes `aria-label="Loading"` som fallback for å gi nødvendig kontekst.

### Tastaturnavigasjon og fokus

En loader skal ikke blokkere interaksjon uten å forklare hvorfor. Hvis du bruker fullskjerm-loader, pass på at den ikke hindrer fokus eller skjuler viktige elementer. Det må være tydelig at brukeren må vente.

Mer om universell utforming av loader og statusbeskjeder:

<div class="cards-container">
  <PktLinkCard
    title="4.1.3 Statusbeskjeder (UUtilsynet)"
    skin="beige"
    href="https://www.uutilsynet.no/wcag-standarden/413-statusbeskjeder-niva-aa/152"
    iconName="chevron-right"
    client:only="react"
  >
    Hvordan du bør kode statusbeskjeder og hvordan de bør skrives
  </PktLinkCard>
  <PktLinkCard
    title="Status Messages – WCAG 2.2 (W3C)"
    skin="beige"
    href="https://www.w3.org/WAI/WCAG21/Understanding/status-messages.html"
    iconName="chevron-right"
    client:only="react"
  >
    Hvordan du implementerer statusmeldinger
  </PktLinkCard>
</div>

</ContentSection>

## Anatomi

| Element           | Beskrivelse                                                       |
| ----------------- | ----------------------------------------------------------------- |
| 1. Loader-element | Enten Oslo-logo (shapes) eller spinner                            |
| 2. Tekst          | Valgfri beskrivelse som vises visuelt og leses opp av skjermleser |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/loader/loader-9.svg"
    alt="Anatomi av loader."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="loader" />

### Overstyring av sti til loading-animasjon

I likhet med <a href={getComponentHref("icon")}>Icon</a>-komponentens overstyring av sti til ikoner kan man overstyre stien til loading-animasjonen globalt ved å sette sti i `window.pktAnimationPath`.

</ContentSection>

## Props

<SpecList specName="loader" />


---


### Component Specification

**Element name**: `pkt-loader`

**React component**: `PktLoader`

**CSS class**: `.pkt-loader`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `message` | `message` | string | `-` | Tekst som vises under loaderen |
| `size` | `size` | `small`, `medium`, `large` | `medium` | Størrelse på loaderen |
| `variant` | `variant` | `rainbow`, `blue`, `shapes` | `rainbow` | Fargevariant på loaderen |
| `delay` | `delay` | number | `0` | Tid i millisekunder før loaderen vises |
| `inline` | `inline` | boolean | `False` | Loader er en del av sidens floatelementer |
| `isLoading` | `isLoading` | boolean | `True` | Loader er aktiv |



### TypeScript Interface

```typescript
export interface IPktLoader {
  /**
   * The `delay` prop controls how much time the loading should be given before the loader is displayed.
   * This is handy for situations where the load time might be so short that loader is not necessary.
   * Delay time is in milliseconds.
   */
  delay?: number
  /**
   * The `inline` prop decides whether the loader should be displayed inline or not.
   */
  inline?: boolean
  /**
   * The boolean 'isLoading' decides whether the loader or the children will be displayed.
   * If set to false, the children will be displayed.
   */
  isLoading?: boolean
  /**
   * The message to display when the loader is loading.
   */
  message?: string | null
  /**
   * The size of the loader. Default is "medium".
   */
  size?: TPktSize
  /**
   * The variant of the loader. Default is "shapes" which is the OSLO wave loader.
   * Other variants are "blue" and "rainbow" which are spinner variants.
   */
  variant?: TPktLoaderVariant
  /**
   * Override path to loading animations.
   */
  loadingAnimationPath?: string
}
```
