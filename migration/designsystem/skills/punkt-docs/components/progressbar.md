# Progressbar

**Generated**: 2025-11-06T10:52:48.958744
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/progressbar/index.mdx`
- `component-specs/progressbar.json`
- `packages/elements/src/components/progressbar/progressbar.ts`
- `packages/elements/src/components/progressbar/index.ts`

---

**Description**: 


## Documentation



# Progressbar

<Lead releaseDate="26.06.2024" lastUpdated="17.01.2025">
  En progressbar (fremdriftsindikator) gir brukeren visuell tilbakemelding på
  hvor langt en prosess har kommet. Den brukes til å vise fremgang i en oppgave
  eller handling, for eksempel under lasting, opplasting eller i en stegvis
  prosess.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ progressbar: progressbarSpec }}
  previewJson={progressbarPreviewJson}
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Loader"
    skin="blue"
    href={getComponentHref("loader")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du vil vise at en prosess pågår, men ikke har en tydelig fremdrift
  </PktLinkCard>
  <PktLinkCard
    title="Stepper"
    skin="blue"
    href={getComponentHref("stepper")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du vil vise en serie steg og hvor langt brukeren har kommet
  </PktLinkCard>
  <PktLinkCard
    title="Alert"
    skin="blue"
    href={getComponentHref("alert")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du vil gi en status, f.eks. om fremdriften er fullført eller feiler
  </PktLinkCard>
</div>

## Varianter

### Farger (skins)

Progressbar kommer i fire ulike skins:

| Skin      | Beskrivelse                                      |
| --------- | ------------------------------------------------ |
| Dark blue | Standard                                         |
| Blue      | Informativ fremdrift eller nøytral verdi         |
| Green     | Fremdrift mot et positivt mål                    |
| Red       | Fremdrift mot kritisk grense eller negativ verdi |

<ImageWrapper>
  <img
    src="/assets/komponenter/progressbar/progressbar-1.svg"
    alt="Skins for progressbar: dark blue"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/progressbar/progressbar-2.svg"
    alt="Skins for progressbar: blue"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/progressbar/progressbar-3.svg"
    alt="Skins for progressbar: green"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/progressbar/progressbar-4.svg"
    alt="Skins for progressbar: red"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk progressbar når

<ListWhenToUseOrNot
  icon="success"
  items={[
    `du har to eller flere steg i en prosess`,
    `brukeren må vite hvor langt de har kommet, og hva som gjenstår`,
    `du ønsker å redusere usikkerhet eller frafall underveis`,
  ]}
/>

### Unngå progressbar når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `prosessen er ett steg, da er den overflødig`,
    `rekkefølgen i en prosess ikke er relevant`,
    `du allerede bruker en annen fremdriftsindikator`,
  ]}
/>

### Progressbar skal være tydelig

Det er ikke påkrevd å ha etikett eller tekst, men det bør være klart hva progressbaren representerer. Dersom prosessen består av flere steg, bør teksten forklare hvor i prosessen brukeren er.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/progressbar/progressbar-5.svg",
    imgAlt: "Gjør slik – korte og konsise tekster",
    caption: "Bruk korte og konsise tekster",
  }}
  badExample={{
    image: "/assets/komponenter/progressbar/progressbar-6.svg",
    imgAlt: "Unngå – lange eller uklare tekster",
    caption: "Unngå lange eller uklare tekster",
  }}
/>
</ContentSection>

## Responsivitet

Progressbar tilpasser seg tilgjengelig plass og fungerer på både store og små skjermer. Den skalerer automatisk i bredde, men du bør teste at etiketter og tekster forblir lesbare på alle skjermstørrelser.

<ImageWrapper>
  <img
    src="/assets/komponenter/progressbar/progressbar-7.svg"
    alt="Responsiv oppførsel for progressbar"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

### Gi skjermleseren riktig informasjon

Skjermlesere må få vite hva progressbaren viser. Bruk riktig kombinasjon av `aria-label`, `aria-labelledby` eller `aria-valuetext`.

- Bruk `aria-label` hvis baren ikke har en synlig etikett
- Bruk `aria-labelledby` hvis etiketten står utenfor komponenten
- Bruk `aria-valuetext` hvis prosenttall alene ikke gir mening, for eksempel i stegvis fremdrift (“5 av 10”)

Hvis du bruker `statusType="fraction"`, kan skjermleser lese “50 %”. Bruk `aria-valuetext` for å si “Spørsmål 5 av 10” hvis det gir mer mening.

### Bruk riktig rolle

Progressbar har to ARIA-roller:

- `progressbar`: viser fremdrift i en prosess (standard)
- `meter`: viser en verdi innenfor et spenn (for eksempel temperatur eller poengsum)

### Etiketten må være tydelig

En progressbar skal alltid ha en forklarende etikett, enten som tittel i komponenten, eller med `aria-labelledby`. Gjør det klart: Hva måles? Hva gjenstår?

### Eksempler

| Visuell tekst     | Hva skjermleser bør få vite                           |
| ----------------- | ----------------------------------------------------- |
| 50 %              | “50 prosent fullført” (ok hvis konteksten er tydelig) |
| 5 av 10 spørsmål  | “Spørsmål 5 av 10” via `aria-valuetext`               |
| Ikke synlig tekst | aria-label="Du har fullført 3 av 7 steg"              |

<div class="cards-container">
  <PktLinkCard
    title="ARIA progressbar"
    skin="beige"
    href="https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/progressbar_role"
    iconName="chevron-right"
    client:only="react"
  >
    Beskriver hvordan du gjør fremdriftsindikatorer tilgjengelige
  </PktLinkCard>
  <PktLinkCard
    title="Accessible Progress Indicators (NN/g)"
    skin="beige"
    href="https://www.nngroup.com/articles/progress-indicators/"
    iconName="chevron-right"
    client:only="react"
  >
    Beste praksis for fremdriftsindikatorer
  </PktLinkCard>
</div>
</ContentSection>

## Anatomi

| Element       | Beskrivelse                        |
| ------------- | ---------------------------------- |
| Fylt område   | Viser faktisk fremgang             |
| Tomt område   | Viser gjenværende del av prosessen |
| Tekst         | Valgfri beskrivelse av fremdrift   |
| Etikett/label | Valgfri tittel som gir kontekst    |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/progressbar/progressbar-8.svg"
    alt="Anatomi for progressbar"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="progressbar" />
</ContentSection>

## Props

<SpecList specName="progressbar" />


---


### Component Specification

**Element name**: `pkt-progressbar`

**React component**: `PktProgressbar`

**CSS class**: `.pkt-progressbar`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `skin` | `skin` | `dark-blue`, `light-blue`, `green`, `red` | `dark-blue` | Velg farge på fremdriftslinjen |
| `title` | `title` | string | `-` | Tittelen på fremdriftslinjen |
| `valueMin` | `valueMin` | number | `0` | Minimumsverdien for fremdriftslinjen |
| `valueMax` | `valueMax` | number | `100` | Maksimumsverdien for fremdriftslinjen |
| `ariaLabel` | `ariaLabel` | string | `-` | aria-label for fremdriftslinjen |
| `ariaLabelledby` | `ariaLabelledby` | string | `-` | aria-labelledby for fremdriftslinjen |
| `ariaValueText` | `ariaValueText` | string | `-` | aria-valuetext for fremdriftslinjen |
| `valueCurrent` | `valueCurrent` | number | `0` | Nåværende verdi for fremdriftslinjen |
| `statusType` | `statusType` | `none`, `percentage`, `fraction` | `percentage` | Type statusindikator |
| `statusPlacement` | `statusPlacement` | `left`, `following`, `center` | `following` | Plassering av statusindikator |
| `id` | `id` | string | `-` | id for fremdriftslinjen |
| `titlePosition` | `titlePosition` | `left`, `center` | `left` | Plassering av tittelen |
| `role` | `role` | `progressbar`, `meter` | `progressbar` | Velg hva fremdriftslinjen skal brukes til |
| `ariaLive` | `ariaLive` | `off`, `polite`, `assertive` | `polite` | Velg ønsket nivå av aria-live |



### TypeScript Interface

```typescript
export interface IPktProgressbar {
  ariaLabel?: string | null
  ariaLabelledby?: string | null
  ariaLive?: TAriaLive | null
  ariaValueText?: string | null
  id?: string | null
  role?: TProgressbarRole
  skin?: TProgressbarSkin
  statusPlacement?: TProgressbarStatusPlacement
  statusType?: TProgressbarStatusType
  title?: string | null
  titlePosition?: TProgressbarTitlePosition
  valueCurrent: number
  valueMax?: number
  valueMin?: number
}
```
