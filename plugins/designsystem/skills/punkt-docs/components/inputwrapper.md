# Input wrapper

**Generated**: 2025-11-06T10:52:48.951394
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/inputwrapper/index.mdx`
- `component-specs/input-wrapper.json`

---

**Description**: 


## Documentation


# Input wrapper

<Lead releaseDate="15.08.2023" lastUpdated="07.07.2025">
  Input wrapper legger til en standardpakke med elementer rundt et inputfelt.
  Den brukes i alle inputfeltene i Punkt, og sikrer at etikett, hjelpetekst og
  feilmeldinger alltid vises på en konsekvent måte.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ "input-wrapper": inputWrapperSpec }}
  previewJson={inputWrapperPreview}
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
    Bruker input wrapper for label og feilmelding
  </PktLinkCard>
  <PktLinkCard
    title="Textarea"
    skin="blue"
    href={getComponentHref("textarea")}
    iconName="chevron-right"
    client:only="react"
  >
    Får samme struktur og hjelpetekst via input wrapper
  </PktLinkCard>
  <PktLinkCard
    title="Combobox"
    skin="blue"
    href={getComponentHref("combobox")}
    iconName="chevron-right"
    client:only="react"
  >
    Omsluttes av input wrapper for konsistent visning
  </PktLinkCard>
</div>

## Varianter

### States

Input wrapper støtter de samme states som feltene den omslutter:

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
    src="/assets/komponenter/inputwrapper/inputwrapper-1.svg"
    alt="States for Input wrapper - Default"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/inputwrapper/inputwrapper-2.svg"
    alt="States for Input wrapper - Hover"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/inputwrapper/inputwrapper-3.svg"
    alt="States for Input wrapper - Focus"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/inputwrapper/inputwrapper-4.svg"
    alt="States for Input wrapper - Active"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/inputwrapper/inputwrapper-5.svg"
    alt="States for Input wrapper - Error"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/inputwrapper/inputwrapper-6.svg"
    alt="States for Input wrapper - Disabled"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Labels/etikett

Labels bør være korte, tydelige og plassert slik at de er enkle å oppfatte. Brukeren skal umiddelbart forstå hva som skal fylles ut. Vi anbefaler at du holder deg til 1 til 3 ord i label, unngå kolon og bruk labels konsekvent på tvers av løsningen.

Dersom du må skjule en label visuelt, for eksempel i tabeller, må den fremdeles være programmert inn slik at skjermlesere kan lese den. Det er også viktig å teste at brukeren forstår hva de skal fylle inn i et slikt tilfelle.

Ikke bruk plassholder som eneste instruksjon. Den forsvinner når brukeren skriver, og er ikke alltid tilgjengelig for skjermlesere. Gi heller nødvendig veiledning med en label og/eller hjelpetekst.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/inputwrapper/inputwrapper-7.svg",
    imgAlt: "Gjør slik – Skriv tydelig og konsise labels",
    caption: "Skriv tydelig og konsise labels",
  }}
  badExample={{
    image: "/assets/komponenter/inputwrapper/inputwrapper-8.svg",
    imgAlt: "Unngå – Unødvendig innhold og kolon på slutten av label",
    caption: "Unngå unødvendig innhold og kolon på slutten av label",
  }}
/>

### Merking av valgfrie eller obligatoriske felt

I Punkt bruker vi kun merkingen “Valgfritt” og “Må fylles ut”. Vi anbefaler alltid å unngå stjerne (\*) som markering, fordi den kan være uklar for brukerne og vanskelig å oppfatte med hjelpemidler.

Som hovedregel bør du unngå valgfrie felter og bare be om informasjon du faktisk trenger. Når du likevel må ha en kombinasjon, bør feltene merkes konsekvent:

- Hvis alle felter på en side er obligatoriske, kan du utelate merkingen og heller skrive det i hjelpeteksten eller over skjemaet
- Hvis alle felter er valgfrie, markerer du feltene med “Valgfritt”
- Hvis du har en blanding av obligatoriske og valgfrie felter, markerer du hvert felt individuelt med “Må fylles ut” eller “Valgfritt”.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/inputwrapper/inputwrapper-9.svg",
    imgAlt: "Gjør slik – Bredde som indikerer forventet innhold",
    caption:
      "Bredden til inputfeltet bør gi brukeren en indikasjon på hva som forventes at de fyller inn",
  }}
  badExample={{
    image: "/assets/komponenter/inputwrapper/inputwrapper-10.svg",
    imgAlt: "Unngå – For brede eller for smale felt",
    caption: "Unngå for brede eller for smale felt for forventet innhold",
  }}
/>

### Hjelpetekst

Hjelpetekst skal alltid bidra til å avklare, ikke gjenta. Den skal forklare hvordan brukeren skal fylle ut feltet, for eksempel hvilket format som gjelder, eller hvor de finner informasjonen. Hjelpetekst bør plasseres tett ved feltet og være lett å oppdage, ellers blir den oversett. Skriv alltid i setningsstil, og bruk hele setninger når det er mulig. Hjelpeteksten bør plasseres over feltet slik at den ikke kolliderer med feilmeldinger.

<ImageWrapper>
  <img
    src="/assets/komponenter/inputwrapper/inputwrapper-11.svg"
    alt="Eksempel på hjelpetekst"
    aria-hidden="true"
  />
</ImageWrapper>

### Ekspanderende hjelpetekst

Dersom du trenger mer plass, kan du bruke ekspanderende hjelpetekst. Dette gjør det mulig å gi utfyllende forklaringer eller legge inn lenker uten å skape for mye støy for brukeren. Husk at utvidet hjelpetekst skal være et supplement, det viktigste må alltid stå tilgjengelig uten ekstra klikk.

<ImageWrapper>
  <img
    src="/assets/komponenter/inputwrapper/inputwrapper-12.svg"
    alt="Ekspanderende hjelpetekst"
    aria-hidden="true"
  />
</ImageWrapper>

### Feilmeldinger og validering

Feilmeldinger skal være konkrete og hjelpe brukeren videre. De bør forklare hva som er galt, og så langt som mulig foreslå hvordan det kan rettes opp.

Feilmeldinger i Punkt kombinerer rød ramme, ikon og tekst. Teksten skal inneholde essensen av hjelpeteksten, slik at brukeren får all nødvendig informasjon samlet.

For å fungere godt må feilmeldinger oppfylle følgende prinsipper:

#### 1. Spesifikk og hjelpsom

Gi klar informasjon om problemet, og foreslå løsning dersom det er mulig, for eksempel riktig format eller korrigering ved feilstavinger.

#### 2. Ikke for tidlig

Unngå å vise feilmeldinger før brukeren har begynt å fylle ut feltet, eller mens hen fortsatt skriver. Vent til brukeren har forlatt feltet eller prøvd å sende inn skjemaet.

#### 3. Feiloppsummering

I skjemaer med flere felter bør feil presenteres både i nærheten av hvert enkelt felt og samlet i en feiloppsummering øverst på siden. Bruk gjerne messagebox i rød variant til dette.

#### 4. Behold gyldig data

All informasjon som er skrevet inn riktig må bli stående. Det er svært frustrerende å måtte fylle ut hele skjemaet på nytt etter en feil.

<ImageWrapper>
  <img
    src="/assets/komponenter/inputwrapper/inputwrapper-13.svg"
    alt="Feilmeldinger og validering"
    aria-hidden="true"
  />
</ImageWrapper>
</ContentSection>

## Responsivitet

Input wrapper tilpasser seg tilgjengelig plass og bryter linjer ved behov.

Test at:

- hjelpetekst og feilmeldinger holder seg nær feltet
- prefiks/suffiks ikke skyver ut viktig innhold
- klikkbare ikoner er store nok på mobil

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

### Alle felt skal ha label

Alle skjemaelementer må ha en label. Den kan være synlig, eller skjult med `pkt-sr-only` dersom layouten krever det. Selv når label skjules visuelt, må den være til stede i koden slik at skjermlesere kan lese den opp.

### Korrekt kobling i koden

Labels må alltid være koblet til det riktige inputfeltet i koden. Dette gjør at skjermlesere kan presentere informasjonen på en forståelig måte, og gir brukeren riktig kontekst når de fyller ut skjemaet.

### Feilmeldinger skal være tilgjengelige

Feilmeldinger må være kodet som tekst, plassert tett på feltet der feilen har oppstått. Bruk en ARIA live region (`aria-live="assertive"` eller `role="alert"`) for å informere når feil oppstår. Denne må være en del av DOM-en fra starten for å fungere. Punkt sine skjemakomponenter har dette innebygget.

### Unngå unødvendige deaktiverte felt

Ikke bruk deaktivert tilstand (`disabled`) hvis det ikke er helt nødvendig. Felt som ikke kan fylles ut skaper ofte forvirring. Bruk heller ren tekst eller `readonly` for å informere brukeren uten å hindre interaksjon.

### Unngå kun plassholder

Plassholdertekst er ofte utilgjengelig for skjermlesere og forsvinner ved innskriving.

### Inndata

For å sikre en god brukeropplevelse er det viktig å velge riktig input-type og bruke `autocomplete` der det er relevant. Dette gjør skjemaet enklere å fylle ut og mer tilgjengelig.

- **Tillat variasjoner**: Brukerne skriver inn informasjon på ulike måter. Tillat variasjoner så lenge innholdet er forståelig (telefonnummer med mellomrom, personnumre med punktum, e-post med mellomrom til slutt)
- **Velg riktig input-type**: Bruk inputtyper som passer til informasjonen du ber om, for eksempel `tel`, `search` eller `email`. Dette gir mobilbrukere et tilpasset tastatur (merk at noen typer kan aktivere klientsidevalidering)
- **Bruk av autocomplete**: `autocomplete` skal brukes i felter som mottar personlig informasjon. Hvis feltet ber om opplysninger om en annen person enn brukeren, sett `autocomplete="off"`
- **Automatisk formatering**: Dersom du formaterer data automatisk mens brukeren skriver, må formateringen være synlig uten å forstyrre

<div class="cards-container">
  <PktLinkCard
    title="Ledetekster og instruksjoner (UUtilsynet)"
    skin="beige"
    href="https://www.uutilsynet.no/veiledning/332-ledetekster-eller-instruksjoner/1263"
    iconName="chevron-right"
    client:only="react"
  >
    Beskriver hvordan du gjør text input tilgjengelige.
  </PktLinkCard>
  <PktLinkCard
    title="Placeholders in Form Fields Are Harmful (NNg)"
    skin="beige"
    href="https://www.nngroup.com/articles/form-design-placeholders/"
    iconName="chevron-right"
    client:only="react"
  >
    Forklarer hvorfor bruk av kun placeholder tekst er ugunstig.
  </PktLinkCard>
</div>

</ContentSection>

## Anatomi

| Element                   | Beskrivelse                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| Label (etikett)           | Kort og tydelig ledetekst som beskriver hva brukeren skal velge                                 |
| Valgfritt-/obligatorisk   | Merker feltet som valgfritt eller obligatorisk                                                  |
| Hjelpetekst               | Kort forklaring under label som hjelper brukeren å forstå hvordan de skal fylle ut feltet       |
| Ekspanderende hjelpetekst | “Les mer”-knapp som viser mer utfyllende informasjon når brukeren trenger ekstra forklaring     |
| Inputfelt                 | Selve inputfeltet der brukeren skriver inn                                                      |
| Plassholdertekst          | Midlertidig tekst i feltet som indikerer at brukeren må gjøre et valg, skal ikke erstatte label |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/inputwrapper/inputwrapper-14.svg"
    alt="Input wrapper anatomi"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="input-wrapper" />
</ContentSection>

## Props

<SpecList specName="input-wrapper" />


---


### Component Specification

**Element name**: `pkt-input-wrapper`

**React component**: `PktInputWrapper`

**CSS class**: `.pkt-inputwrapper`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `forId` | `forId` | string | `-` | Id-en til skjemaelementet som dette wrapper rundt |
| `label` | `label` | string | `-` | Merkelapp for skjemaelementet |
| `helptext` | `helptext` | string | `-` | Hjelpetekst for skjemaelementet |
| `helptextDropdown` | `helptextDropdown` | string | `-` | Hjelpetekst som vises i ekspanderende felt |
| `helptextDropdownButton` | `helptextDropdownButton` | string | `Les mer <span class='pkt-sr-only'>om feltet</span>` | Tekst som vises i knappen for å vise hjelpetekst i dropdown |
| `ariaDescribedby` | `ariaDescribedby` | string | `-` | Id-en til elementet som beskriver skjemaelementet |
| `counter` | `counter` | boolean | `False` | Teller for antall tegn i skjemaelementet |
| `counterCurrent` | `counterCurrent` | number | `-` | Tellerens nåværende verdi |
| `counterMaxLength` | `counterMaxLength` | number | `-` | Maks antall tegn som kan skrives i skjemaelementet |
| `counterPosition` | `counterPosition` | `top`, `bottom` | `bottom` | Telleren sin plassering i forhold til elementet |
| `optionalTag` | `optionalTag` | boolean | `False` | Viser en merking som indikerer at feltet er valgfritt |
| `optionalText` | `optionalText` | string | `Valgfritt` | Tekst som vises i valgfritt-merkingen |
| `requiredTag` | `requiredTag` | boolean | `False` | Viser en merking som indikerer at feltet er påkrevd |
| `requiredText` | `requiredText` | string | `Må fylles ut` | Tekst som vises i påkrevd-merkingen |
| `tagText` | `tagText` | string | `-` | Tekst som vises i en tag ved siden av label |
| `hasError` | `hasError` | boolean | `False` | Indikerer at skjemaelementet har en feil |
| `errorMessage` | `errorMessage` | string | `-` | Feilmelding som vises når skjemaelementet har en feil |
| `disabled` | `disabled` | boolean | `False` | Indikerer at skjemaelementet er deaktivert |
| `inline` | `inline` | boolean | `False` | Indikerer at skjemaelementet skal flyte sammen med sidens innhold |
| `hasFieldset` | `hasFieldset` | boolean | `False` | Indikerer at innholdet er et fieldset |
| `useWrapper` | `useWrapper` | boolean | `True` | Indikerer om skjemaelementet skal bruke en wrapper |
| `role` | `role` | string | `group` | Rollen til elementet |


#### Events

- **`toggleHelpText`**: Event for å vise eller skjule hjelpetekst i dropdown


