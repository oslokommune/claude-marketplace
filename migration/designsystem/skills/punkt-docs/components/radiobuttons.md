# Radio button

**Generated**: 2025-11-06T10:52:48.960086
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/radiobuttons/index.mdx`
- `component-specs/radiobutton.json`

---

## Documentation


# Radio button

<Lead
  releaseDate="04.10.2023"
  lastUpdated="07.07.2025"
>
  Du bruker radio button når brukeren skal velge én av flere forhåndsdefinerte alternativer. Radio button fungerer best når det er fem eller færre valg, og når du ønsker at alle alternativene skal være synlige samtidig slik at brukeren enkelt kan sammenligne dem.

Radio buttons brukes ofte i skjemaer og spørreskjemaer der valget er gjensidig utelukkende.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ radiobutton: radiobuttonSpec }}
  previewJson={radiobuttonPreviewJson}
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Checkbox"
    skin="blue"
    href={getComponentHref("checkbox")}
    iconName="chevron-right"
    client:only="react"
  >
    Når brukeren kan velge flere alternativer.
  </PktLinkCard>
  <PktLinkCard
    title="Select"
    skin="blue"
    href={getComponentHref("select")}
    iconName="chevron-right"
    client:only="react"
  >
    Når det er mange valg (flere enn fem).
  </PktLinkCard>
  <PktLinkCard
    title="Switch"
    skin="blue"
    href={getComponentHref("switch")}
    iconName="chevron-right"
    client:only="react"
  >
    Når valget er binært og kan endres med ett klikk.
  </PktLinkCard>
</div>

## Varianter

| Varianter | Beskrivelse                                                  |
| --------- | ------------------------------------------------------------ |
| Standard  | Viser ett eller flere valg som radio buttons                 |
| Med ramme | Radio button plassert i "tile"-layout for tydelig gruppering |

<ImageWrapper>
  <img
    src="/assets/komponenter/radiobuttons/radiobutton-1.svg"
    alt="Standard radio button"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/radiobuttons/radiobutton-2.svg"
    alt="Radio button med ramme"
    aria-hidden="true"
  />
</ImageWrapper>

Radio button skal alltid brukes sammen i grupper, og helst med inputwrapper (kalt "radio button group" i Figma). Gruppen kan inneholde:

- Label (etikett)
- Valgfritt-/obligatorisk-tag
- Hjelpetekst eller ekspanderende hjelpetekst
- Feilmelding

<ContentSection backgroundColor="subtle-pale-blue" >
## Retningslinjer for bruk

### Bruk radio button når

<ListWhenToUseOrNot
  icon="success"
  items={[
    `brukeren skal velge én av flere alternativer`,
    `valgene utelukker hverandre`,
    `det er viktig at alle alternativene vises samtidig`,
  ]}
/>

### Unngå radio button når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `brukeren kan velge flere alternativer (bruk da <a href="${getComponentHref("checkbox")}">checkbox</a>)`,
    `det er få alternativer og kun én innstilling skal slås av/på (bruk  <a href="${getComponentHref("switch")}">switch</a>)`,
    `du har mange valg (bruk da <a href="${getComponentHref("select")}">select</a>)`,
  ]}
/>

### Skriv tydelige etiketter og hjelpetekst

Skriv klare og konkrete etiketter som beskriver hva valget innebærer, ikke bare "Ja" eller "Nei". Unngå kolon etter label og store bokstaver i hele ordet, skriv slik at brukeren forstår hva du spør etter.

Hjelpetekster skal være hele setninger. Du kan legge hjelpetekst over gruppen eller under hvert valg. Bruk ekspanderende hjelpetekst ved behov for mer informasjon eller lenker.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/radiobuttons/radiobutton-3.svg",
    imgAlt: "Eksempel på en kort og tydelig tekst i etikett og alternativer",
    caption: "Skriv kort og tydelig tekst i etikett og alternativer",
  }}
  badExample={{
    image: "/assets/komponenter/radiobuttons/radiobutton-4.svg",
    imgAlt:
      "Eksempel på  radio buttons med lange eller uklare tekster i etikett og alternativer",
    caption: "Unngå lange eller uklare tekster i etikett og alternativer",
  }}
/>

### Ikke bruk radio button om brukeren skal kunne velge flere valg

Radio buttons skal kun brukes dersom det ene valget utelater det andre.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/radiobuttons/radiobutton-5.svg",
    imgAlt:
      "Eksempel riktig bruk av komponeneter ved valg av flere alternativer",
    caption: `Bruk checkbox dersom brukeren skal ha mulighet til å krysse av flere alternativer`,
  }}
  badExample={{
    image: "/assets/komponenter/radiobuttons/radiobutton-6.svg",
    imgAlt:
      "Eksempel på  radio buttons som brukes for å la brukeren velge flere alternativer",
    caption:
      "Unngå å bruke radio button for å la brukeren velge flere alternativer",
  }}
/>

### Antall valg

Radio button skal ha minst to alternativer. Har du mer enn fem valg, bør du vurdere å bruke select for bedre oversikt og brukervennlighet.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/radiobuttons/radiobutton-7.svg",
    imgAlt: "Eksempel riktig bruk av komponeneter ved mange alternativer",
    caption: `Bruk select dersom du har mange alternativer`,
  }}
  badExample={{
    image: "/assets/komponenter/radiobuttons/radiobutton-8.svg",
    imgAlt: "Eksempel på radio buttons som brukes ved mange alternativer",
    caption: "Unngå radio button ved mange alternativer",
  }}
/>

### Plassering

Plasser radio button vertikalt for best lesbarhet. Horisontal plassering kan brukes hvis det kun er to til tre korte valg. Hvis etikettene er lange eller bryter linjer, bruk vertikal plassering.

På mobil skal radio buttons alltid ligge vertikalt.

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/radiobuttons/radiobutton-9.svg"
    alt="Eksempel på plassering av radio button."
    aria-hidden="true"
  />
</ImageWrapper>

</ContentSection>

## Responsivitet

Radio button tilpasser seg skjermstørrelse automatisk, men

- bruk vertikal plassering på små skjermer
- test linjebryting, lesbarhet og fokushåndtering

<ImageWrapper>
  <img
    src="/assets/komponenter/radiobuttons/radiobutton-10.svg"
    alt="Eksempel på radio button på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

Radio buttons skal kunne brukes med tastatur og skjermleser:

- Bruk `fieldset` og `legend` for å gruppere radio buttons, eller `aria-labelledby`
- Naviger mellom valg med “pil opp” og “pil ned”
- Velg med “mellomrom”
- Sørg for tydelig fokusring ved tabbing
- Unngå disabled-tilstand. Hvis du må deaktivere noe, forklar hvorfor og hva som kreves for å aktivere det

<div class="cards-container">
  <PktLinkCard
    title="UU-tilsynet om skjema og radioknapper"
    skin="beige"
    href="https://www.uutilsynet.no/veiledning/skjema/38#introduksjon"
    iconName="chevron-right"
    client:only="react"
  >
    Beskriver hvordan du gjør radio buttons tilgjengelige
  </PktLinkCard>
</div>

</ContentSection>

## Anatomi

| Element                      | Beskrivelse                              |
| ---------------------------- | ---------------------------------------- |
| 1. Etikett                   | Overskrift for gruppen                   |
| 2. Valgfritt-/obligatorisk   | Tilleggsinfo om feltets krav             |
| 3. Hjelpetekst               | Utfyllende forklaring                    |
| 4. Ekspanderende hjelpetekst | For mye info eller lenker                |
| 5. Radio buttons             | Alternativene brukeren kan velge mellom  |
| 6. Radio button hjelpetekst  | Hjelpetekst under en enkelt radio button |

<ImageWrapper caption="Gruppe med radioknapper">
  <img
    src="/assets/komponenter/radiobuttons/radiobutton-11.svg"
    alt="Anatomi gruppe med radioknapper."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
  ## Implementasjon i kode

  <TechDetails specName="radiobutton" />
</ContentSection>

## Props

<SpecList specName="radiobutton" />


---


### Component Specification

**Element name**: `pkt-radiobutton`

**React component**: `PktRadioButton`

**CSS class**: `.pkt-input-check`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `id` | `id` | string | `-` | Unik ID for radiobutton |
| `name` | `name` | string | `-` | Navn for radiobutton |
| `label` | `label` | string | `-` | Tekst i label for radiobutton |
| `checked` | `checked` | boolean | `False` | Er radiobutton valgt? |
| `defaultChecked` | `defaultChecked` | boolean | `False` | Skal radiobutton være valgt som standard? |
| `hasTile` | `hasTile` | boolean | `False` | - |
| `disabled` | `disabled` | boolean | `False` | Er radiobutton deaktivert? |
| `checkHelptext` | `checkHelptext` | string | `-` | Hjelpetekst som vises under radiobutton |
| `value` | `value` | string | `-` | Verdien som sendes når radiobutton er valgt |
| `hasError` | `hasError` | boolean | `False` | Indikerer om radiobutton har en feil |
| `requiredTag` | `requiredTag` | Boolean | `False` | Viser en merking som indikerer at feltet er påkrevd |
| `requiredText` | `requiredText` | string | `-` | Tekst som vises i påkrevd-merkingen |
| `optionalTag` | `optionalTag` | boolean | `-` | Viser en merking som indikerer at feltet er valgfritt |
| `optionalText` | `optionalText` | string | `-` | Tekst som vises i valgfritt-merkingen |
| `tagText` | `tagText` | string | `-` | Tekst som vises i en tag ved siden av label |


#### Events

- **`change`**: Hendelse som utløses når radiobutton endres


