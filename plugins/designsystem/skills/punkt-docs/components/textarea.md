# Textarea

**Generated**: 2025-11-06T10:52:48.968503
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/textarea/index.mdx`
- `component-specs/textarea.json`
- `packages/elements/src/components/textarea/index.ts`
- `packages/elements/src/components/textarea/textarea.ts`

---

**Description**: 


## Documentation



# Textarea

<Lead releaseDate="11.09.2023" lastUpdated="07.07.2025">
  Textarea (fritekstfelt) er et skjemaelement som lar brukeren skrive tekst over flere linjer. Bruk det når du forventer at brukeren skal skrive inn lengre tekst, som fritekstsvar eller beskrivelser.

For korte svar anbefaler vi <a href={getComponentHref("textinput")}>text input</a>.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ textarea: textareaSpec }}
  previewJson={textareaPreviewJson}
  fullWidth
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Text input"
    skin="blue"
    href={getComponentHref("textinput")}
    iconName="chevron-right"
    client:only="react"
  >
    Bruk når du forventer korte svar (én linje)
  </PktLinkCard>
  <PktLinkCard
    title="Combobox"
    skin="blue"
    href={getComponentHref("combobox")}
    iconName="chevron-right"
    client:only="react"
  >
    Bruk når brukeren skal kunne velge fra en liste med alternativer
  </PktLinkCard>
  <PktLinkCard
    title="Search input"
    skin="blue"
    href={getComponentHref("searchinput")}
    iconName="chevron-right"
    client:only="react"
  >
    Bruk når formålet er å søke, ikke å skrive inn en lengre tekst
  </PktLinkCard>
</div>

## Varianter

| Variant    | Beskrivelse                             |
| ---------- | --------------------------------------- |
| Default    | Enkelt felt for lengre tekst            |
| Med teller | Når du har en maksgrense på antall tegn |

<ImageWrapper>
  <img
    src="/assets/komponenter/textarea/textarea-1.svg"
    alt="Varianter av textarea: Default"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/textarea/textarea-2.svg"
    alt="Varianter av textarea: Med teller"
    aria-hidden="true"
  />
</ImageWrapper>

### States

| State    | Beskrivelse                                                 |
| -------- | ----------------------------------------------------------- |
| Default  | Feltet vises i normal tilstand, klar til bruk               |
| Hover    | Når brukeren beveger musepekeren over feltet                |
| Focus    | Når brukeren har markert feltet og er klar til å skrive     |
| Active   | Når brukeren skriver i feltet                               |
| Error    | Når feltet har en feil, og en forklarende feilmelding vises |
| Disabled | Når feltet ikke er tilgjengelig for interaksjon             |

<ImageWrapper>
  <img
    src="/assets/komponenter/textarea/textarea-3.svg"
    alt="States for textarea - Default"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/textarea/textarea-4.svg"
    alt="States for textarea - Hover"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/textarea/textarea-5.svg"
    alt="States for textarea - Focus"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/textarea/textarea-6.svg"
    alt="States for textarea - Active"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/textarea/textarea-7.svg"
    alt="States for textarea - Error"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/textarea/textarea-8.svg"
    alt="States for textarea - Disabled"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk textarea når

<ListWhenToUseOrNot
  icon="success"
  items={[
    `brukeren skal skrive lengre fritekstsvar`,
    `svaret ikke har en fast struktur`,
  ]}
/>

### Unngå textarea når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `du forventer korte svar (bruk <a href="${getComponentHref("textinput")}">text input</a>)`,
    `du bare trenger valg eller avkryssing (bruk <a href="${getComponentHref("checkbox")}">checkbox</a>, <a href="${getComponentHref("radiobuttons")}">radio button</a> eller <a href="${getComponentHref("select")}">select</a>)`,
  ]}
/>

### Plassholder

Du kan legge til plassholdertekst, men ikke bruk den som eneste instruksjon. Plassholderen forsvinner når brukeren skriver, og er ikke alltid tilgjengelig for skjermlesere.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/textarea/textarea-9.svg",
    imgAlt: "Gjør slik – eksempel med tydelig etikett og hjelpetekst",
    caption:
      "Bruk label for å forklare feltet, og bruk plassholder kun som støtte",
  }}
  badExample={{
    image: "/assets/komponenter/textarea/textarea-10.svg",
    imgAlt: "Unngå – eksempel hvor plassholder brukes som eneste instruksjon",
    caption: "Unngå bruk av plassholder som eneste instruksjon",
  }}
/>

### Størrelse

Textarea skal ha en høyde som står i forhold til hvor mye tekst du forventer at brukeren skriver. For små felt gjør det vanskelig å lese og redigere lengre svar.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/textarea/textarea-11.svg",
    imgAlt: "Gjør slik – hensiktsmessig høyde for lengre svar",
    caption: "Tilpass høyden på textarea etter mengden tekst du forventer",
  }}
  badExample={{
    image: "/assets/komponenter/textarea/textarea-12.svg",
    imgAlt: "Unngå – for liten høyde som gjør lesing/redigering vanskelig",
    caption:
      "Unngå å gjøre feltet for lite, da blir det vanskelig å lese og redigere tekst",
  }}
/>

### Teller (counter)

Hvis du har en tegnbegrensning, kan du legge til en teller. Den hjelper brukeren med å holde seg innenfor grensen uten å stoppe skrivingen.

Brukeren må få lov til å fullføre tanken sin selv om grensen overskrides. Derfor skal feltet kunne inneholde mer tekst enn maksgrensen, men samtidig vise at grensen er passert (content overflow).

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/textarea/textarea-13.svg"
    alt="Teller viser antall tegn og maksgrense"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/textarea/textarea-14.svg"
    alt="Antall tegn over maksgrense"
    aria-hidden="true"
  />
</ImageWrapper>

</ContentSection>

## Responsivitet

Textarea tilpasser seg bredden på skjermen og bryter linjer automatisk. Test på mobil, nettbrett og desktop for å sikre at feltet er lett å bruke og lese overalt.

<ImageWrapper>
  <img
    src="/assets/komponenter/textarea/textarea-15.svg"
    alt="Textarea i mobilkontekst"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

## Universell utforming

### Ledetekst og instruksjon

Alle skjemaelementer må ha en label eller instruksjon som forklarer hvordan feltet skal fylles ut, inkludert om det er obligatorisk eller valgfritt. Labelen må være koblet til feltet i koden slik at skjermlesere kan lese opp riktig informasjon. I mer komplekse skjemaer kan du trenge ekstra forklaring gjennom hjelpetekst eller ekspanderende hjelpetekst.

### Feilmeldinger

Feilmeldinger må være tilgjengelige både for skjermlesere og for de som navigerer med tastatur. Det skal være enkelt å identifisere hvilket felt feilen gjelder, og meldingen bør beskrive både hva som er galt og hvordan brukeren kan rette opp.

### Spesielt for textarea

- Feltet må kunne ekspanderes slik at lange svar blir håndterbar
- Telleren må ikke blokkere innskriving, men tydelig vise når maksgrensen er passert (content overflow)
- Test at feltet fungerer godt med zoom og på små skjermer

</ContentSection>

## Anatomi

| Element                   | Beskrivelse                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| Label (etikett)           | Kort og tydelig ledetekst som beskriver hva brukeren skal velge                                 |
| Valgfritt-/obligatorisk   | Merker feltet som valgfritt eller obligatorisk                                                  |
| Hjelpetekst               | Kort forklaring under label som hjelper brukeren å forstå hvordan de skal fylle ut feltet       |
| Ekspanderende hjelpetekst | “Les mer”-knapp som viser mer utfyllende informasjon når brukeren trenger ekstra forklaring     |
| Inputfelt                 | Selve tekstfeltet der brukeren skriver inn                                                      |
| Plassholdertekst          | Midlertidig tekst i feltet som indikerer at brukeren må gjøre et valg, skal ikke erstatte label |
| Teller                    | Viser hvor mange tegn brukeren har skrevet, og maksgrensen (valgfritt)                          |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/textarea/textarea-16.svg"
    alt="Anatomi for textarea"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="textarea" />
</ContentSection>

## Props

<SpecList specName="textarea" />


---


### Component Specification

**Element name**: `pkt-textarea`

**React component**: `PktTextarea`

**CSS class**: `.pkt-textarea`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `label` | `label` | string | `-` | Tekst som vises over feltet |
| `name` | `name` | string | `-` | Navn som sendes brukes i skjema ved innsending |
| `placeholder` | `placeholder` | string | `-` | Spesifiserer en kort hint som beskriver forventet verdi av feltet. |
| `helptext` | `helptext` | string | `-` | Hjelpetekst som vises over feltet |
| `helptextDropdown` | `helptextDropdown` | string | `-` | Hjelpetekst som vises i en lukket boks man kan åpne |
| `helptextDropdownButton` | `helptextDropdownButton` | string | `Les mer` | Tekst som vises på knappen for å åpne/lukke utvidet hjelpetekst |
| `rows` | `rows` | number | `-` | Spesifiserer antall synlige rader i feltet. |
| `value` | `value` | string | `-` | Spesifiserer den nåværende verdien av feltet. |
| `autocomplete` | `autocomplete` | string | `off` | Spesifiserer hvordan type `autocomplete` feltet har. Standard er 'off'. |
| `ariaLabelledby` | `ariaLabelledby` | string | `-` | Spesifiserer ID-en til elementet som beskriver feltet. |
| `required` | `required` | boolean | `False` | Er feltet påkrevd? |
| `requiredTag` | `requiredTag` | boolean | `-` | Indikerer om feltet er påkrevd. |
| `requiredText` | `requiredText` | string | `Må fylles ut` | Tekst som vises i påkrevd-merkingen |
| `optionalTag` | `optionalTag` | boolean | `-` | Indikerer om feltet er valgfritt. |
| `optionalText` | `optionalText` | string | `Valgfritt` | Tekst som vises i valgfritt-merkingen |
| `tagText` | `tagText` | string | `-` | Tekst som vises i en tag ved siden av label |
| `hasError` | `hasError` | boolean | `-` | Indikerer om feltet har en feil. |
| `errorMessage` | `errorMessage` | string | `-` | Tekst som vises under datovelgeren ved feiltilstand |
| `disabled` | `disabled` | boolean | `False` | Indikerer om feltet er deaktivert. |
| `inline` | `inline` | boolean | `False` | Indikerer om feltet skal vises inline. |
| `fullwidth` | `fullwidth` | boolean | `False` | Indikerer om feltet skal ta opp full bredde. |
| `useWrapper` | `useWrapper` | boolean | `True` | Indikerer at feltet skal ha synlig label og hjelpetekst |
| `id` | `id` | string | `-` | Spesifiserer den unike identifikatoren for feltet. |
| `counter` | `counter` | boolean | `False` | Indikerer om en teller skal vises. |
| `counterMaxLength` | `counterMaxLength` | number | `-` | Spesifiserer maksimal lengde for telleren. |


