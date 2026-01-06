# Stepper

**Generated**: 2025-11-06T10:52:48.963139
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/stepper/index.mdx`
- `component-specs/steps.json`
- `component-specs/step-item.json`

---

**Description**: En komponent for å visualisere brukere gjennom en flerstegsprosess.


## Documentation



# Stepper

<Lead releaseDate="12.07.2024" lastUpdated="–">
  Stepper brukes til å vise hvor langt brukeren har kommet i en stegvis prosess
  og hva som gjenstår. Den gir en visuell representasjon av fremdriften ved å
  dele opp prosessen i logiske trinn. Stepper brukes ofte i skjemaer,
  spørreundersøkelser eller navigasjon som krever flere steg.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ steps: stepperSpec, stepItem: stepItemSpec }}
  previewJson={stepperPreviewJson}
  fullWidth
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Progressbar"
    skin="blue"
    href={getComponentHref("progressbar")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du ikke trenger klikkbar navigasjon mellom steg
  </PktLinkCard>
  <PktLinkCard
    title="Tabs"
    skin="blue"
    href={getComponentHref("tabs")}
    iconName="chevron-right"
    client:only="react"
  >
    Bytt mellom innhold der rekkefølgen ikke er lineær
  </PktLinkCard>
  <PktLinkCard
    title="Breadcrumbs"
    skin="blue"
    href={getComponentHref("breadcrumbs")}
    iconName="chevron-right"
    client:only="react"
  >
    Viser brukeren en hierarkisk struktur på tvers av sider
  </PktLinkCard>
</div>

## Varianter

| Variant    | Bruk                                                               |
| ---------- | ------------------------------------------------------------------ |
| Vertikal   | Passer best på smale skjermer eller når siden er bygd opp i høyden |
| Horisontal | Brukes når innholdet i ett trinn avhenger av et tidligere trinn    |

<ImageWrapper>
  <img
    src="/assets/komponenter/stepper/stepper-1.svg"
    alt="Varianter av stepper: vertikal"
    aria-hidden="true"
  />
</ImageWrapper>

<ImageWrapper>
  <img
    src="/assets/komponenter/stepper/stepper-2.svg"
    alt="Varianter av stepper: horisontal"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk stepper når

<ListWhenToUseOrNot
  icon="success"
  items={[
    `du vil hjelpe brukeren å forstå hvor langt de er kommet i en prosess`,
    `prosessen har flere logiske steg (3–8 steg anbefales)`,
    `det er behov for en visuell representasjon av fremdriften`,
  ]}
/>

### Unngå stepper når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `prosessen er kort og enkel (bruk heller <a href="${getComponentHref("progressbar")}">progressbar</a>)`,
    `du bare trenger å vise fremdrift uten klikkbar navigasjon`,
  ]}
/>

### Navigasjon

Stepper kan brukes som navigasjon, men skal aldri være eneste måte å navigere på. Brukeren må alltid ha flere måter å bevege seg frem og tilbake.

### Tekst og innhold

Stegene bør ha korte og beskrivende titler. Lange titler blir vanskelige å lese, spesielt i horisontale stepper.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/stepper/stepper-3.svg",
    imgAlt: "Gjør slik – korte og beskrivende titler",
    caption: "Skriv korte og beskrivende titler",
  }}
  badExample={{
    image: "/assets/komponenter/stepper/stepper-4.svg",
    imgAlt: "Unngå – lange overskrifter i horisontal stepper",
    caption: "Unngå lange overskrifter i horisontal stepper",
  }}
  direction="column"
/>

</ContentSection>

## Responsivitet

Stepper tilpasser seg tilgjengelig plass.

- Vertikal stepper fungerer godt på smale skjermer
- Horisontal stepper passer best på større flater

Husk å test at alle trinn vises tydelig på ulike skjermstørrelser og zoom-nivåer.

<ImageWrapper>
  <img
    src="/assets/komponenter/stepper/stepper-5.svg"
    alt="Stepper i ulike skjermstørrelser"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

### Ikke bruk stepper som hovednavigasjon

En stepper kan brukes for å indikere hvor brukeren er i en prosess. Den kan brukes som en visuell guide eller for å vise fremdrift og navigere. Selve komponenten bør derimot ikke være hovednavigasjonsmåten for brukeren.

### Husk å teste stepperen med tastatur og skjermleser

Dersom brukeren har mulighet til å bruke stepperen til å navigere, sørg for at det er mulig ved hjelp av tastatur og skjermleser.

</ContentSection>

## Anatomi

| Element                 | Beskrivelse                                       |
| ----------------------- | ------------------------------------------------- |
| Tittel                  | Kort og tydelig overskrift for steget             |
| Ikon for steg           | Viser status: fullført, aktivt eller ufullstendig |
| Hjelpetekst (valgfritt) | Innholdet som hører til steget                    |
| Aktiv linje             | Kobler sammen fullførte steg                      |
| Ikke aktiv linje        | Viser fremtidige steg                             |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/stepper/stepper-6.svg"
    alt="Anatomi for Stepper"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="steps" />
</ContentSection>

## Props

### Stepper

<SpecList specName="steps" />

### Step Item

<SpecList specName="step-item" />


---


### Component Specification

**Element name**: `pkt-stepper`

**React component**: `PktStepper`

**CSS class**: `.pkt-stepper`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `activeStep` | `activeStep` | number | `-` | Indeks for det aktive trinnet i stepperen |
| `hideNonActiveStepsContent` | `hideNonActiveStepsContent` | boolean | `True` | Skal innholdet for inaktive trinn skjules? |
| `orientation` | `orientation` | `horizontal`, `vertical` | `horizontal` | Orienteringen av stepperen, enten 'horizontal' eller 'vertical' |



### Component Specification

**Element name**: `pkt-step-item`

**React component**: `PktStep`

**CSS class**: `.pkt-step`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `status` | `status` | `completed`, `current`, `incomplete` | `-` | - |
| `title` | `title` | string | `-` | - |


