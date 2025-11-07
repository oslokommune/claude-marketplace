# Text input

**Generated**: 2025-11-06T10:52:48.969873
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/textinput/index.mdx`
- `component-specs/textinput.json`
- `packages/elements/src/components/textinput/textinput.ts`
- `packages/elements/src/components/textinput/index.ts`

---

## Documentation



# Text input

<Lead
  releaseDate="14.08.2023"
  lastUpdated="07.07.2025"
>

Et text input (tekstfelt, inputfelt) lar brukeren skrive fritekst, oftest i skjemaer, men også i andre deler av en tjeneste. Bruk tekstfelt til korte verdier som får plass på én linje, for eksempel navn, e-post, telefonnummer, fødselsnummer eller beløp.

Målet er at brukeren raskt forstår hva som skal fylles inn, og får tydelig tilbakemelding hvis noe er feil.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ textinput: textInputSpec }}
  previewJson={textInputPreviewJson}
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
    Når brukeren skal velge ett av få alternativer
  </PktLinkCard>
  <PktLinkCard
    title="Combobox"
    skin="blue"
    href={getComponentHref("combobox")}
    iconName="chevron-right"
    client:only="react"
  >
    Når brukeren skal skrive for å søke etter alternativer
  </PktLinkCard>
</div>

## Varianter

Text input brukes vanligvis sammen med input wrapper. Under dokumentasjonen til denne finner du mer om hvordan du skriver gode labels og hjelpetekster, og om funksjonene i input wrapper.

| Type                           | Beskrivelse                                                     |
| ------------------------------ | --------------------------------------------------------------- |
| Standard                       | Label, placeholder og tekstfelt                                 |
| Med hjelpetekst                | Kort hjelpetekst under label                                    |
| Med ekspanderende hjelpetekst  | Hjelpetekst bak “Les mer”-knapp                                 |
| Valgfritt-tag/obligatorisk tag | Viser enten “Valgfritt” eller “Må fylles ut” ved siden av label |

Text input brukes vanligvis sammen med <a href={getComponentHref("inputwrapper")}>input wrapper</a>, under dokumentasjonen til denne finner du mer om hvordan du skriver gode labels og hjelpetekster, og om funksjonene i input wrapper.

<ImageWrapper>
  <img
    src="/assets/komponenter/input/textinput-1.svg"
    alt="Varianter av text input"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/input/textinput-2.svg"
    alt="Varianter av text input"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/input/textinput-3.svg"
    alt="Varianter av text input"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/input/textinput-4.svg"
    alt="Varianter av text input"
    aria-hidden="true"
  />
</ImageWrapper>

### States

Text input har seks ulike states som gir brukeren visuell tilbakemelding i ulike situasjoner:

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
    src="/assets/komponenter/input/textinput-5.svg"
    alt="States for text input"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/input/textinput-6.svg"
    alt="States for text input"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/input/textinput-7.svg"
    alt="States for text input"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/input/textinput-8.svg"
    alt="States for text input"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/input/textinput-9.svg"
    alt="States for text input"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/input/textinput-10.svg"
    alt="States for text input"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk text input når

<ListWhenToUseOrNot
  icon="success"
  items={[
    `brukeren skal skrive kort fritekst på én linje, som navn, e-post, telefonnummer eller beløp`,
    `verdien er unik og ikke kan velges fra en liste`,
  ]}
/>

### Unngå text input når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `brukeren skal velge mellom forhåndsdefinerte alternativer (bruk heller <a href="${getComponentHref("select")}">select</a>, <a href="${getComponentHref("radiobuttons")}">radio button</a> eller <a href="${getComponentHref("checkbox")}">checkbox</a>)`,
    `innholdet er lengre fritekst, som avsnitt eller flere setninger (bruk heller <a href="${getComponentHref("textarea")}">textarea</a>)`,
  ]}
/>

### Labels/etikett

En label skal være kort og presis, helst mellom ett og tre ord. Unngå kolon på slutten og bruk verken kun store eller små bokstaver.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/input/textinput-11.svg",
    imgAlt: "Gjør slik – tydelige og konsise labels",
    caption: "Skriv tydelig og konsise labels",
  }}
  badExample={{
    image: "/assets/komponenter/input/textinput-12.svg",
    imgAlt: "Unngå – unødvendig innhold og kolon på slutten av label",
    caption: "Unngå unødvendig innhold og kolon på slutten av label",
  }}
/>

### Plassholder

Plassholder skal aldri være eneste instruksjon. Den forsvinner når brukeren gjør et valg, og er ikke alltid tilgjengelig for skjermlesere. Bruk heller label og/eller hjelpetekst for å gi nødvendig veiledning.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/input/textinput-13.svg",
    imgAlt: "Gjør slik – bruk label over text input",
    caption: "Bruk label over text input",
  }}
  badExample={{
    image: "/assets/komponenter/input/textinput-14.svg",
    imgAlt: "Unngå – placeholdertekst som eneste ledetekst",
    caption: "Unngå å bruke plassholdertekst som eneste ledetekst",
  }}
/>

### Bredde

Bredden på feltet bør passe til innholdet du forventer at brukeren fyller inn. Et telefonnummerfelt bør for eksempel ikke være bredere enn antallet tegn som skal skrives inn. Ulik bredde på feltene gjør det lettere å navigere i skjemaer med mange felt.

Text input er egnet til korte tekster og svar. <a href={getComponentHref("textarea")}>Textarea</a> er egnet til mer utfyllende og lengre svar.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/input/textinput-15.svg",
    imgAlt: "Gjør slik – bredde som indikerer forventet innhold",
    caption:
      "Bredden til inputfeltet bør gi brukeren en indikasjon på hva som forventes at de fyller inn",
  }}
  badExample={{
    image: "/assets/komponenter/input/textinput-16.svg",
    imgAlt: "Unngå – for brede eller smale felt",
    caption: "Unngå for brede eller for smale felt for forventet innhold",
  }}
/>

### Valgfritt eller påkrevd

Velg én metode for å markere felter: enten viser du «Valgfritt» på de åpne feltene, eller «Må fylles ut» på de obligatoriske. Bland aldri begge i samme løsning.

<ImageWrapper>
  <img
    src="/assets/komponenter/input/textinput-17.svg"
    alt="Merking av valgfritt"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/input/textinput-18.svg"
    alt="Merking av obligatorisk"
    aria-hidden="true"
  />
</ImageWrapper>

### Prefiks og suffiks

Bruk prefiks når faste tegn skal vises foran verdien, for eksempel landskode på telefonnummer. Bruk suffiks når du skal vise en enhet, et ikon eller tilby en handling som å tømme feltet eller vise/skjule passord.

<ImageWrapper>
  <img
    src="/assets/komponenter/input/textinput-19.svg"
    alt="Eksempel på prefiks og suffiks"
    aria-hidden="true"
  />
</ImageWrapper>

### Hjelpetekst og feilmeldinger

Hjelpetekst skal alltid bidra til å avklare, ikke gjenta. Den skal forklare hvordan brukeren skal fylle ut feltet, for eksempel hvilket format som gjelder, eller hvor de finner informasjonen.

Feilmeldinger skal være konkrete og hjelpe brukeren videre. De bør forklare hva som er galt, og så langt som mulig foreslå hvordan det kan rettes opp.

Les mer om innhold i skjemaelementer i <a href={getComponentHref("inputwrapper")}>input wrapper-dokumentasjonen</a> og om [god praksis for skjemaer](/god-praksis/skjemadesign/).

</ContentSection>

## Responsivitet

Text input tilpasser seg tilgjengelig plass og bryter linjer ved behov.

Test at:

- hjelpetekst og feilmeldinger holder seg nær feltet
- prefiks/suffiks ikke skyver ut viktig innhold
- klikkbare ikoner er store nok på mobil

<ImageWrapper>
  <img
    src="/assets/komponenter/input/textinput-20.svg"
    alt="Text input i mobilkontekst"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

### Synlig eller skjult label

Alle felt skal ha en label. Den kan være synlig, eller skjult med `pkt-sr-only` når den ikke skal vises visuelt. Labelen må være koblet til feltet i koden, slik at skjermlesere leser opp riktig informasjon.

### Hjelpetekst og feilmelding

Hjelpetekst og feilmeldinger skal knyttes til feltet med `aria-describedby`. På den måten får skjermlesere lest opp riktig kontekst. Feilmeldinger må være tekst, plassert rett under feltet, og forklare både hva som er galt og hvordan det kan rettes. Ikke vis feilmeldinger før brukeren faktisk har forsøkt å fylle ut feltet.

### Riktig type og autofyll

Bruk riktige type-verdier for å gi bedre tilgjengelighet og riktig tastatur på mobil, for eksempel `email`, `tel` eller `password`. Angi autocomplete der det er nyttig, som `name` eller `one-time-code`.

### Klikkbare prefiks og suffiks

Ikoner eller tekst som fungerer som handlinger (for eksempel “vis/skjul passord”) må kunne fokuseres med tastatur og ha en tydelig beskrivelse for skjermlesere.

### Unngå plassholder som instruksjon

Plassholdertekst forsvinner når brukeren skriver, og er ofte utilgjengelig for skjermlesere. Viktig veiledning må derfor alltid ligge i label eller hjelpetekst.

### Inndata

For å sikre en god brukeropplevelse er det viktig å bruke en kombinasjon av riktig input-type og autocomplete-attributter. [Les mer om autocomplete på MDN Webdocs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete).

- Tillat variasjoner i hvordan data skrives inn, så lenge informasjonen er forståelig. For eksempel bør telefonnumre kunne inneholde mellomrom, personnumre punktum, og e-postadresser aksepteres selv om de har et mellomrom til slutt
- Velg inputtyper som samsvarer med informasjonen du ber om, for eksempel tel, search eller email. Dette gir mobilbrukere et tilpasset tastatur, men vær oppmerksom på at enkelte inputtyper kan aktivere klientsidevalidering
- `autocomplete` brukes i felter som mottar personlig informasjon. Hvis feltet skal be om personopplysninger om en annen person enn brukeren, må du sette `autocomplete="off"`
- Pass på at brukerne ser inndata som formateres automatisk, men uten at det forstyrrer dem mens de fyller ut.

Mer om universell utforming av text input:

<div class="cards-container">
  <PktLinkCard
    title="Ledetekster og instruksjoner (UUtilsynet)"
    skin="beige"
    href="https://www.uutilsynet.no/veiledning/332-ledetekster-eller-instruksjoner/1263"
    iconName="chevron-right"
    client:only="react"
  >
    Beskriver hvordan du gjør text input tilgjengelige
  </PktLinkCard>
  <PktLinkCard
    title="Placeholders in Form Fields Are Harmful (NNg)"
    skin="beige"
    href="https://www.nngroup.com/articles/form-design-placeholders/"
    iconName="chevron-right"
    client:only="react"
  >
    Forklarer hvorfor bruk av kun placeholder tekst bør unngås
  </PktLinkCard>
</div>
</ContentSection>

## Anatomi

| Element                   | Beskrivelse                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| Label (etikett)           | Kort og tydelig ledetekst som beskriver hva brukeren skal skrive                                |
| Valgfritt-/obligatorisk   | Merker feltet som valgfritt eller obligatorisk                                                  |
| Hjelpetekst               | Kort forklaring under label som hjelper brukeren å forstå hvordan de skal fylle ut feltet       |
| Ekspanderende hjelpetekst | “Les mer”-knapp som viser mer utfyllende informasjon når brukeren trenger ekstra forklaring     |
| Inputfelt                 | Selve inputfeltet der brukeren skriver inn                                                      |
| Plassholdertekst          | Midlertidig tekst i feltet som indikerer at brukeren må gjøre et valg, skal ikke erstatte label |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/input/textinput-21.svg"
    alt="Anatomi for Text input"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="textinput" />
</ContentSection>

## Props

<SpecList specName="textinput" />


---


### Component Specification

**Element name**: `pkt-textinput`

**React component**: `PktTextinput`

**CSS class**: `.pkt-textinput`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `label` | `label` | string | `-` | Tekst som vises over feltet |
| `name` | `name` | string | `-` | Navn som sendes brukes i skjema ved innsending |
| `placeholder` | `placeholder` | string | `-` | Spesifiserer en kort hint som beskriver forventet verdi av feltet. |
| `helptext` | `helptext` | string | `-` | Hjelpetekst som vises over feltet |
| `helptextDropdown` | `helptextDropdown` | string | `-` | Hjelpetekst som vises i en lukket boks man kan åpne |
| `helptextDropdownButton` | `helptextDropdownButton` | string | `Les mer` | Tekst som vises på knappen for å åpne/lukke utvidet hjelpetekst |
| `size` | `size` | number | `-` | Spesifiserer bredde på feltet i antall tegn. |
| `type` | `type` | `color`, `date`, `datetime-local`, `email`, `file`, `month`, `number`, `password`, `search`, `tel`, `text`, `time`, `url`, `week` | `text` | Spesifiserer typen av feltet. Standard er 'text'. |
| `omitSearchIcon` | `omitSearchIcon` | boolean | `False` | Indikerer om søkeikonet skal utelates. |
| `value` | `value` | string | `-` | Spesifiserer den nåværende verdien av feltet. |
| `autocomplete` | `autocomplete` | string | `off` | Spesifiserer hvordan type `autocomplete` feltet har. Standard er 'off'. |
| `suffix` | `suffix` | string | `-` | Spesifiserer et suffiks som vises etter feltet. |
| `prefix` | `prefix` | string | `-` | Spesifiserer et prefiks som vises før feltet. |
| `iconNameRight` | `iconNameRight` | icon | `-` | Spesifiserer navnet på ikonet som vises til høyre for feltet. |
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


#### Events

- **`change`**: Returnerer verdi som streng
- **`toggleHelpText`**: Returnerer <code>event.detail { isOpen: true }</code> eller <code>event.detail { isOpen: false }</code> når hjelpeteksten åpnes eller lukkes


