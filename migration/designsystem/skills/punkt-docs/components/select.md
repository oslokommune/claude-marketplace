# Select

**Generated**: 2025-11-06T10:52:48.962119
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/select/index.mdx`
- `component-specs/select.json`
- `packages/elements/src/components/select/select.ts`
- `packages/elements/src/components/select/index.ts`

---

## Documentation



# Select

<Lead
  releaseDate="19.09.2023"
  lastUpdated="07.07.2025"
>
  Select (nedtrekksliste) lar brukeren velge ett enkelt alternativ fra en liste. Den brukes når du har mange valg, men ikke plass eller behov for å vise alle samtidig.

Formålet med komponenten er å gjøre det enkelt å velge riktig alternativ uten at det tar unødvendig plass i et skjema eller løsning.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ select: selectSpec }}
  previewJson={selectPreviewJson}
  fullWidth
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
    Når brukeren kan velge flere alternativer
  </PktLinkCard>
  <PktLinkCard
    title="Radio button"
    skin="blue"
    href={getComponentHref("radiobuttons")}
    iconName="chevron-right"
    client:only="react"
  >
    Når det er få valg og man kun skal velge ett
  </PktLinkCard>
  <PktLinkCard
    title="Combobox"
    skin="blue"
    href={getComponentHref("combobox")}
    iconName="chevron-right"
    client:only="react"
  >
    Når brukeren kan skrive for å søke etter alternativer
  </PktLinkCard>
</div>

## Varianter

### Innhold

| Type                           | Beskrivelse                                                     |
| ------------------------------ | --------------------------------------------------------------- |
| Standard                       | Label, placeholder og valgliste                                 |
| Med hjelpetekst                | Kort hjelpetekst under feltet                                   |
| Med ekspanderende hjelpetekst  | Hjelpetekst bak “Les mer”-knapp                                 |
| Valgfritt-tag/obligatorisk tag | Viser enten “Valgfritt” eller “Må fylles ut” ved siden av label |

<ImageWrapper>
  <img
    src="/assets/komponenter/select/select-1.svg"
    alt="Varianter av select"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/select/select-2.svg"
    alt="Varianter av select"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/select/select-3.svg"
    alt="Varianter av select"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/select/select-4.svg"
    alt="Varianter av select"
    aria-hidden="true"
  />
</ImageWrapper>

Select brukes vanligvis sammen med <a href={getComponentHref("inputwrapper")}>input wrapper</a>, under dokumentasjonen til denne finner du mer
om hvordan du skriver gode labels og hjelpetekster, og om funksjonene i input wrapper.

### States

Text input har seks ulike states som gir brukeren visuell tilbakemelding i ulike situasjoner:

| Type     | Beskrivelse                                                 |
| -------- | ----------------------------------------------------------- |
| Default  | Feltet vises i normal tilstand, klar til bruk               |
| Hover    | Når brukeren beveger musepekeren over feltet                |
| Focus    | Når brukeren har markert feltet og er klar til å skrive     |
| Active   | Når brukeren skriver i feltet                               |
| Error    | Når feltet har en feil, og en forklarende feilmelding vises |
| Disabled | Når feltet ikke er tilgjengelig for interaksjon             |

<ImageWrapper>
  <img
    src="/assets/komponenter/select/select-5.svg"
    alt="States av select - Default"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/select/select-6.svg"
    alt="States av select - Hover"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/select/select-7.svg"
    alt="States av select - Focus"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/select/select-8.svg"
    alt="States av select - Active"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/select/select-9.svg"
    alt="States av select - Error"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/select/select-10.svg"
    alt="States av select - Disabled"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk select når

<ListWhenToUseOrNot
  icon="success"
  items={[
    `du skal presentere mange alternativ der bare ett kan velges`,
    `du ønsker å unngå at lange lister med alternativer blir overveldende`,
    `du trenger å få plass til flere alternativer på liten plass`,
  ]}
/>

### Unngå select når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `du har få valg og god plass (bruk heller <a href="${getComponentHref("radiobuttons")}">radio button</a>)`,
    `brukeren kan velge mer enn ett alternativ (bruk heller <a href="${getComponentHref("checkbox")}">checkbox</a>)`,
    `du har strukturerte alternativer med nok plass er det bedre å liste ut alle valgene`,
  ]}
/>

### Antall og tilgjengelighet

Select fungerer best når du har mange alternativer, men bare ett skal velges. Har du færre enn fem valg, er radioknapper ofte bedre fordi valgene blir mer synlige og enklere å sammenligne.

Lange lister kan være utfordrende for brukere med skjermleser, og det finnes kjente tilgjengelighetsproblemer med select-komponenten (les mer under [“Research about this component” på gov.uk](https://design-system.service.gov.uk/components/select/)).

Vurder om du kan forenkle spørsmålet slik at det blir færre alternativer. Hvis det gir mening, bruk <a href={getComponentHref("radiobuttons")}>radio button</a> for å gi en bedre opplevelse.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/select/select-11.svg",
    imgAlt: "Gjør slik – bruk select når du har mange alternativer",
    caption: "Bruk select når du har mange alternativer",
  }}
  badExample={{
    image: "/assets/komponenter/select/select-12.svg",
    imgAlt: "Unngå – select ved få alternativer",
    caption: "Unngå select ved få alternativer",
  }}
/>

### Sortering av alternativer

Det er viktig å liste ut elementene dine på en oversiktlig måte, om det så er alfabetisk, tidsbasert eller en annen logisk rekkefølge.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/select/select-13.svg",
    imgAlt: "Gjør slik – sorter i logisk rekkefølge",
    caption: "Sorter alternativene i en logisk rekkefølge",
  }}
  badExample={{
    image: "/assets/komponenter/select/select-14.svg",
    imgAlt: "Unngå – ulogisk rekkefølge og inkonsekvente navn",
    caption:
      "Unngå å liste alternativer i ulogisk rekkefølge og å bruke forskjellige måter å skrive alternativene",
  }}
/>

### Bruk select til riktig formål

Select passer best til ryddige, relaterte lister. Ikke bruk den til å velge innhold som egentlig krever et annet format, som adresse eller telefonnummer.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/select/select-15.svg",
    imgAlt: "Gjør slik – relaterte lister",
    caption: "Bruk select til lister med relatert innhold",
  }}
  badExample={{
    image: "/assets/komponenter/select/select-16.svg",
    imgAlt: "Unngå – postnummer og tall som krever annet format",
    caption: "Unngå select for innhold som bør velges på en annen måte",
  }}
/>

### Label, hjelpetekst og plassholder

En label skal være kort og presis, helst mellom ett og tre ord. Unngå kolon på slutten og bruk verken kun store eller kun små bokstaver.

Plassholder skal aldri være eneste instruksjon. Den forsvinner når brukeren gjør et valg, og er ikke alltid tilgjengelig for skjermlesere. Bruk heller label og/eller hjelpetekst for å gi nødvendig veiledning.

Les mer om innhold i skjemaelementer i <a href={getComponentHref("inputwrapper")}>input wrapper-dokumentasjonen</a> og om [god praksis for skjemaer](/god-praksis/skjemadesign/).

</ContentSection>

## Responsivitet

Select tilpasser seg automatisk tilgjengelig plass og bryter linjer der det er nødvendig. Test alltid på ulike skjermstørrelser og zoom-nivåer at det fortsatt er enkelt å navigere med tastatur og skjermleser.

<ImageWrapper>
  <img
    src="/assets/komponenter/select/select-17.svg"
    alt="Select i mobilkontekst"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

## Universell utforming

- Alle felt skal ha en tilknyttet label, også hvis den skjules visuelt (`pkt-sr-only`).
- Feilmeldinger skal være kodet som tekst og knyttet til det spesifikke feltet.
- Select kan være utfordrende for skjermlesere ved veldig lange lister, vurder alternativer som <a href={getComponentHref("radiobuttons")}>radio button</a> eller <a href={getComponentHref("combobox")}>combobox</a> om det gir bedre opplevelse.

</ContentSection>

## Anatomi

| Element                   | Beskrivelse                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| Label (etikett)           | Kort og tydelig ledetekst som beskriver hva brukeren skal velge                                 |
| Valgfritt-/obligatorisk   | Merker feltet som valgfritt eller obligatorisk                                                  |
| Hjelpetekst               | Kort forklaring under label som hjelper brukeren å forstå hvordan de skal fylle ut feltet       |
| Ekspanderende hjelpetekst | “Les mer”-knapp som viser mer utfyllende informasjon når brukeren trenger ekstra forklaring     |
| Inputfelt                 | Selve nedtrekkslisten der brukeren velger et alternativ                                         |
| Plassholdertekst          | Midlertidig tekst i feltet som indikerer at brukeren må gjøre et valg, skal ikke erstatte label |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/select/select-18.svg"
    alt="Anatomi for Select"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="select" />
</ContentSection>

## Props and tokens

<SpecList specName="select" />


---


### Component Specification

**Element name**: `pkt-select`

**React component**: `PktSelect`

**CSS class**: `.pkt-select`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `label` | `label` | string | `-` | Tekst som vises over feltet |
| `requiredTag` | `requiredTag` | boolean | `False` | Viser en merking som indikerer at feltet er påkrevd |
| `requiredText` | `requiredText` | string | `-` | Tekst som vises i påkrevd-merkingen |
| `optionalTag` | `optionalTag` | boolean | `-` | Viser en merking som indikerer at feltet er valgfritt |
| `optionalText` | `optionalText` | string | `-` | Tekst som vises i valgfritt-merkingen |
| `tagText` | `tagText` | string | `-` | Tekst som vises i en tag ved siden av label |
| `hasError` | `hasError` | boolean | `-` | Angir om feltet har feil |
| `errorMessage` | `errorMessage` | string | `-` | Feilmelding som vises under feltet |
| `helptext` | `helptext` | string | `-` | Hjelpetekst som vises over feltet |
| `helptextDropdown` | `helptextDropdown` | string | `-` | Hjelpetekst som vises i en lukket boks man kan åpne |
| `helptextDropdownButton` | `helptextDropdownButton` | string | `-` | Tekst som vises på knappen for å åpne/lukke utvidet hjelpetekst |
| `name` | `name` | string | `-` | Navn på feltet |
| `id` | `id` | string | `-` | Id på feltet |
| `value` | `value` | string | `-` | Verdi på feltet |
| `disabled` | `disabled` | boolean | `False` | Angir om feltet er disabled |
| `inline` | `inline` | boolean | `False` | Angir om feltet skal vises i en linje |
| `fullwidth` | `fullwidth` | boolean | `False` | Angir om feltet skal ta full bredde |
| `ariaDescribedBy` | `ariaDescribedBy` | string | `-` | Spesifiserer ID-en til elementet som beskriver feltet |
| `ariaLabelledby` | `ariaLabelledby` | string | `-` | Spesifiserer ID-en til elementet som navigerer til feltet |



### TypeScript Interface

```typescript
export interface IPktSelect {
  options: TSelectOption[]
  value: string
}
```
