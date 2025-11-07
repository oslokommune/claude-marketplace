# Checkbox

**Generated**: 2025-11-06T10:52:48.941455
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/checkbox/index.mdx`
- `component-specs/checkbox.json`
- `packages/elements/src/components/checkbox/checkbox.ts`
- `packages/elements/src/components/checkbox/index.ts`

---

## Documentation

  PktLinkCard,
  PktInputWrapper,
  PktMessagebox,
} from "@oslokommune/punkt-react";



# Checkbox

<Lead releaseDate="04.10.2023" lastUpdated="07.07.2025">
  Checkbox brukes for å gi brukeren mulighet til å krysse av ett eller flere
  alternativer i en gruppe med valg. Du kan også bruke en enkeltstående checkbox
  for å be om bekreftelse, for eksempel "Jeg godtar vilkårene" før innsending av
  et skjema.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ checkbox: checkboxSpec }}
  previewJson={checkboxPreviewJson}
/>
## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Radiobutton"
    skin="blue"
    href={getComponentHref("radiobuttons")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du må velge kun ett alternativ blant flere.
  </PktLinkCard>
  <PktLinkCard
    title="Switch"
    skin="blue"
    href={getComponentHref("switch")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du skal skru noe av eller på, som en innstilling.
  </PktLinkCard>
  <PktLinkCard
    title="Select"
    skin="blue"
    href={getComponentHref("select")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du skal velge fra en lengre liste med mange alternativer.
  </PktLinkCard>
</div>

## Varianter

| Variant          | Bruk                                                                              |
| ---------------- | --------------------------------------------------------------------------------- |
| Standard         | Når checkbox står alene eller i en enkel liste                                    |
| Tile (med ramme) | Når du vil gruppere flere checkboxer visuelt. Gir tydelig avgrensning og mer luft |

<ImageWrapper>
  <img
    src="/assets/komponenter/checkbox/checkbox-1.svg"
    alt="Enkeltstående avmerkingsboks med og uten ramme"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/checkbox/checkbox-2.svg"
    alt="Enkeltstående checkbox"
    aria-hidden="true"
  />
</ImageWrapper>

| Variant       | Bruk                                                                              |
| ------------- | --------------------------------------------------------------------------------- |
| Enkeltstående | Når checkbox står alene eller i en enkel liste                                    |
| Gruppe        | Gruppér checkboxene når du tilbyr flere valg innenfor samme gruppe eller kategori |

<ImageWrapper caption="Enkeltstående checkbox">
  <img
    src="/assets/komponenter/checkbox/checkbox-2-1.svg"
    alt="Enkeltstående checkbox"
    aria-hidden="true"
  />
</ImageWrapper>
<ImageWrapper caption="En gruppe med checkboxer">
  <img
    src="/assets/komponenter/checkbox/checkbox-3.svg"
    alt="En gruppe med checkboxer"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk checkbox når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "man har en gruppe med valg innenfor samme kontekst",
    "valgene ikke utelukker hverandre",
    "brukeren skal kunne velge ett eller flere alternativer",
    "en bruker skal ha muligheten til å skru et alternativ på/av (for eksempel “akseptere vilkår” for en tjeneste, eller lignende funksjonalitet)",
  ]}
/>

### Unngå checkbox når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `brukeren kun kan velge ett alternativ (bruk <a href="${getComponentHref("radiobuttons")}">radiobutton</a> i stedet)`,
    `det er få alternativer (vurder heller <a href="${getComponentHref("switch")}">switch</a> eller <a href="${getComponentHref("radiobuttons")}">radiobutton</a>)`,
    `det er mer enn 10 alternativer å velge mellom (vurder å bruke <a href="${getComponentHref("select")}">select</a>)`,
    `det er en binær innstilling som kan beskrives som på/av (bruk <a href="${getComponentHref("switch")}">switch</a>)`,
  ]}
/>

### Skriv tydelige etiketter

Sørg for at hver checkbox har en klar og konkret etikett. Etiketten skal beskrive hva valget innebærer, ikke bare “Ja” eller “Nei”.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/checkbox/checkbox-4.svg",
    imgAlt: "Eksempel på klar og konkret etikett",
    caption: "Skriv klar og konkret etikett",
  }}
  badExample={{
    image: "/assets/komponenter/checkbox/checkbox-5.svg",
    imgAlt: "Eksempel på ufullstendig og uklart innhold..",
    caption: "Unngå ufullstendig og uklart innhold",
  }}
/>
### Forskjellen på radiobutton og checkbox

Ikke bruk checkboxer dersom brukeren kun kan velge ett valg (gå heller for <a href={getComponentHref('radiobuttons')}>radiobuttons</a>)

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/checkbox/checkbox-6.svg",
    imgAlt: "Eksempel på riktig bruk av radiobuttons",
    caption: "Bruk radiobuttons dersom det ene valget utelukker det andre",
  }}
  badExample={{
    image: "/assets/komponenter/checkbox/checkbox-7.svg",
    imgAlt: "Eksempel på riktig bruk av radiobuttons",
    caption:
      "Unngå checkboxer når brukeren ikke skal ha muligheten til å velge flere valg",
  }}
/>

### Opt in, ikke opt out

Checkbox skal alltid brukes som opt-in. Brukeren må selv aktivt krysse av for å gi samtykke (opt in), ikke måtte melde seg av (opt out).

Du skal aldri forhåndsvelge en checkbox for samtykke, for eksempel til å motta nyhetsbrev eller godta vilkår. Dette er et krav i GDPR.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/checkbox/checkbox-8.svg",
    imgAlt: "Eksempel på checkbox som brukes som opt-in",
    caption: "Checkbox skal alltid brukes som opt-in",
  }}
  badExample={{
    image: "/assets/komponenter/checkbox/checkbox-9.svg",
    imgAlt: "Eksempel på checkbox hvor brukeren selv må melde seg av.",
    caption: "Unngå at brukeren selv må melde seg av",
  }}
/>

### Plassering av checkbox

Plasser checkboxene vertikalt når det er mulig. Det gjør det enklere for brukeren å se hvilket valg som hører til hvilken tekst.

Horisontal plassering bør bare brukes hvis det er to til tre valg, og hvis det gir en mer kompakt løsning.

Har du lange etiketter som kan gå over flere linjer, skal checkboxene alltid plasseres vertikalt for best lesbarhet.

Hvis du har mange valg, bør du liste dem i én kolonne. Da blir det lettere for brukeren å skanne valgene.

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/checkbox/checkbox-10.svg"
    alt="Plassering av checkboxer"
    aria-hidden="true"
  />
</ImageWrapper>
</ContentSection>

## Responsivitet

På mobil skal alltid checkboxer ligge vertikalt for optimal lesbarhet.

Husk å teste:

- at teksten brytes riktig på små skjermer
- at grupperte checkboxer (tile) fortsatt er oversiktlige
- at fokusring og klikkeflater fungerer godt på touch

<ImageWrapper>
  <img
    src="/assets/komponenter/checkbox/checkbox-11.svg"
    alt="Checkbox på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

### Skriv en klar, kortfattet og unik label

Alle checkboxer krever en klar, kortfattet og unik label (etikett). For checkboxer uten label, for eksempel de som brukes i en tabell, kreves det fortsatt en skjult etikett for skjermlesere og andre hjelpeteknologier. WCAG 2.1: 1.3.1 [Info and Relationships](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships), 2.4.6 [Headings and Labels](https://www.w3.org/WAI/WCAG21/Understanding/headings-and-labels.html).

### Unngå standardvalg

Forhåndsvalgte valg anses som en villedende praksis for alle brukere. Implementer en standard uvalgt tilstand.

### Unngå deaktiverte (disabled) checkboxer

Vi anbefaler å unngå disabled på skjemaelementer som radio, checkbox og tekstfelt, fordi det kan skape problemer for tilgjengelighet.

Brukere forstår ofte ikke hvorfor et element er deaktivert. Derfor anbefaler vi å heller vise en feilmelding eller en hjelpetekst, enn å bruke disabled. Hvis du må deaktivere en checkbox, må det være tydelig hvorfor, og hva som må til for å aktivere den igjen.

### Tastaturinteraksjoner

Alle tastaturinteraksjoner og ARIA-etiketter må oppfylle tilgjengelighetskriterier.

### Bruk fieldset og legend

Bruk `fieldset` og `legend` (som inputwrapper tilbyr) ved grupper av avmerkingsbokser.

Les mer om universell utforming av checkbox:

<div class="cards-container">
  <PktLinkCard
    title="WAI-ARIA Checkbox Authoring Practices"
    skin="beige"
    href="https://www.w3.org/WAI/ARIA/apg/#checkbox"
    iconName="chevron-right"
    client:only="react"
  >
    Hvordan du lager universelt utformede webkomponenter og widgeter med
    ARIA-roller.
  </PktLinkCard>
</div>

</ContentSection>

## Anatomi

| Element        | Beskrivelse                       |
| -------------- | --------------------------------- |
| 1. Checkbox    | Selve checkboxen                  |
| 2. Label       | Tekst som beskriver valget        |
| 3. Hjelpetekst | Forklaring til valget (valgfritt) |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/checkbox/checkbox-12.svg"
    alt="Accordion anatomi."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="checkbox">
  <div slot="testing">
      Om dere bruker `data-testid` for å hente ut elementer i
      testene, vil attributten videresendes til selve skjemaelementet. Dersom
      dere heller ønsker å bruke `data-testid` på elementet
      `<pkt-checkbox>`, må dere sette attributten
      `skipForwardTestid` på elementet.

      Dersom dere skal teste tilstanden på `checked` bør dere teste
      på den visuelle tilstanden med en query mot `:checked`
      istedenfor å teste property `.checked`. Grunnen til dette har
      vi ikke helt klart å komme til bunns i, da det fungerer helt fint med
      riktig property i nettleseren. Det kan tenkes at dette kan løses ved å
      vente et øyeblikk, om det er helt nødvendig å teste property istedenfor
      synlig tilstand.

      I
      [punkt-testing-utils](https://www.npmjs.com/package/@oslokommune/punkt-testing-utils)
      har vi skrevet testen slik: `element.querySelectorAll(':checked').length`.

  </div>
</TechDetails>

</ContentSection>

## Props

<SpecList specName="checkbox" />


---


### Component Specification

**Element name**: `pkt-checkbox`

**React component**: `PktCheckbox`

**CSS class**: `.pkt-input-check`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `label` | `label` | string | `-` | - |
| `checkHelptext` | `checkHelptext` | string | `-` | - |
| `name` | `name` | string | `-` | - |
| `value` | `value` | string | `-` | - |
| `id` | `id` | string | `-` | - |
| `defaultChecked` | `defaultChecked` | boolean | `False` | - |
| `checked` | `checked` | boolean | `False` | - |
| `hasTile` | `hasTile` | boolean | `False` | - |
| `disabled` | `disabled` | boolean | `False` | - |
| `hasError` | `hasError` | boolean | `False` | - |
| `isSwitch` | `isSwitch` | boolean | `False` | - |
| `labelPosition` | `labelPosition` | `right`, `left` | `-` | - |
| `hideLabel` | `hideLabel` | boolean | `False` | - |
| `requiredTag` | `requiredTag` | Boolean | `False` | Viser en merking som indikerer at feltet er påkrevd |
| `requiredText` | `requiredText` | string | `-` | Tekst som vises i påkrevd-merkingen |
| `optionalTag` | `optionalTag` | boolean | `-` | Viser en merking som indikerer at feltet er valgfritt |
| `optionalText` | `optionalText` | string | `-` | Tekst som vises i valgfritt-merkingen |
| `tagText` | `tagText` | string | `-` | Tekst som vises i en tag ved siden av label |


#### Events

- **`change`**: Returnerer checkboxens verdi når den endres


