# Messagebox

**Generated**: 2025-11-06T10:52:48.956035
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/messagebox/index.mdx`
- `component-specs/messagebox.json`
- `packages/elements/src/components/messagebox/index.ts`
- `packages/elements/src/components/messagebox/messagebox.ts`

---

## Documentation



# Messagebox

<Lead
  releaseDate="21.03.2023"
  lastUpdated="31.10.2024"
>
  Messagebox brukes for å gruppere informasjon og hjelpe brukeren med å forstå innholdet på en side, uten at det krever handling. Den gjør det lettere å skille ut tips, veiledning eller annen støtteinformasjon fra det øvrige innholdet.

Messagebox skal ikke brukes til status eller varslinger – da skal du bruke <a href={getComponentHref("alert")}>alert</a>.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ messagebox: messageboxSpec }}
  previewJson={messageboxPreviewJson}
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
    Når du skal vise status, feil eller bekreftelser
  </PktLinkCard>
  <PktLinkCard
    title="Card"
    skin="blue"
    href={getComponentHref("card")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du bare vil gruppere innhold visuelt
  </PktLinkCard>
  <PktLinkCard
    title="Accordion"
    skin="blue"
    href={getComponentHref("accordion")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du vil gi ekstra informasjon, men bare ved behov
  </PktLinkCard>
</div>

## Varianter

### Varianter

I Punkt finnes messagebox i fire ulike fargevarianter

| Skin  | Beskrivelse                                                           |
| ----- | --------------------------------------------------------------------- |
| Beige | Nøytral info, generell støtte                                         |
| Blue  | Hjelp og forklaring                                                   |
| Red   | For å gjøre brukeren oppmerksom på noe viktig som kan ha konsekvenser |
| Green | Positiv bekreftelse eller fremheving                                  |

<ImageWrapper>
  <img
    src="/assets/komponenter/messagebox/messagebox-1.svg"
    alt="Varianter av messagebox"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/messagebox/messagebox-2.svg"
    alt="Varianter av messagebox"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/messagebox/messagebox-3.svg"
    alt="Varianter av messagebox"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/messagebox/messagebox-4.svg"
    alt="Varianter av messagebox"
    aria-hidden="true"
  />
</ImageWrapper>

### Størrelser

Alle variantene kommer i to størrelser

| Variant | Beskrivelse                     |
| ------- | ------------------------------- |
| Default | Standardstørrelse               |
| Small   | Brukes der plassen er begrenset |

<ImageWrapper>
  <img
    src="/assets/komponenter/messagebox/messagebox-5.svg"
    alt="Ulike størrelser på messagebox"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/messagebox/messagebox-6.svg"
    alt="Ulike størrelser på messagebox"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk messagebox når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "du vil gi brukeren kontekst, støtte eller forklaring",
    "informasjonen ikke krever at brukeren gjør noe",
    "du trenger å fremheve tekst visuelt, men uten varslingseffekt",
  ]}
/>

### Unngå messagebox når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `du gir status, feil eller bekreftelser (bruk <a href="${getComponentHref("alert")}">alert</a>)`,
    `du bare trenger visuell inndeling (bruk <a href="${getComponentHref("card")}">card</a>)`,
    `meldingen vises midlertidig og skal fanges opp raskt (vurder  <a href="${getComponentHref("alert")}">toast alert</a> eller <a href="${getComponentHref("alert")}">inline alert</a>)`,
  ]}
/>

### Messagebox er en fleksibel komponent

Komponenten har ingen bestemte retningslinjer for bruk, den kan fritt brukes til innhold du ønsker å gruppere eller fremheve. Ved å bruke komponenten kan du hjelpe brukerne med å visuelt skille mellom det som er relatert og det som ikke er det.

</ContentSection>

## Responsivitet

### Automatisk skalering

Messagebox tilpasser seg automatisk bredden på skjermen, og innholdet bryter linjer der det er nødvendig. Den fungerer godt både i stående og liggende visning på mobil.

Du trenger ikke å gjøre manuell tilpasning, men

- pass på at teksten ikke blir for tett eller lang
- unngå å bruke mange messageboxes rett etter hverandre (det skaper støy)

<ImageWrapper>
  <img
    src="/assets/komponenter/messagebox/messagebox-7.svg"
    alt="Messagebox på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

Messagebox er en visuell komponent. Den skal ikke brukes til statiske meldinger som må oppfattes via skjermleser (bruk da <a href={getComponentHref("alert")}>alert</a>).

Det er viktig at du husker at messagebox ikke skal ha `ARIA`-roller. Ikke bruk `role="status"` eller `aria-live` og at tekst og tittel må være selvforklarende, også uten annen kontekst.

</ContentSection>

## Anatomi

| Element                  | Beskrivelse                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| 1. Bakgrunn og kantlinje | Bakgrunnsfarge med tilhørende kantlinje                               |
| 2. Tittel (valgfritt)    | Oppsummerer innholdet, gjør det lettere å skumlese                    |
| 3. Innhold               | Forklarende tekst, kan inneholde lister, lenker, knapper eller ikoner |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/messagebox/messagebox-8.svg"
    alt="Anatomi av messagebox komponenten."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="messagebox" />
</ContentSection>

## Props

<SpecList specName="messagebox" />


---


### Component Specification

**Element name**: `pkt-messagebox`

**React component**: `PktMessagebox`

**CSS class**: `.pkt-messagebox`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `title` | `title` | string | `-` | Tittelen på meldingsboksen |
| `skin` | `skin` | `beige`, `blue`, `red`, `green` | `beige` | Velg farge på meldingsboksen |
| `compact` | `compact` | boolean | `False` | Gjør meldingsboksen mindre |
| `closable` | `closable` | boolean | `False` | Viser lukkeknapp |


#### Events

- **`onClose`**: React: Event som trigges når meldingsboksen lukkes
- **`on-close`**: Vue: Event som trigges når meldingsboksen lukkes


