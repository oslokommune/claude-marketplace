# Modal

**Generated**: 2025-11-06T10:52:48.957528
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/modal/index.mdx`
- `component-specs/modal.json`
- `packages/elements/src/components/modal/modal.ts`
- `packages/elements/src/components/modal/index.ts`

---

## Documentation




# Modal

<Lead
  releaseDate="26.11.2024"
  lastUpdated="19.06.2025"
>
  Modal (også kalt dialog eller popup) er et midlertidig vindu som vises over annet innhold. Du bruker modal når du vil be brukeren ta stilling til noe viktig, vise informasjon eller gi mulighet for interaksjon, uten at de forlater den siden de er på.

Modaler bør brukes med måte. De kan oppleves forstyrrende, og må derfor ha en tydelig hensikt og være enkle å lukke.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<CodeExample>
  <ModalExamples client:only="react" />
</CodeExample>

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
    title="Messagebox"
    skin="blue"
    href={getComponentHref("messagebox")}
    iconName="chevron-right"
    client:only="react"
  >
    Brukes for å vise informasjon eller beskjed på en roligere måte
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

Modal kommer i to ulike visuelle varianter. Du velger selv hvilken variant som passer best i din løsning.

| Style  | Beskrivelse                                                                   |
| ------ | ----------------------------------------------------------------------------- |
| Simple | For enkle og nøytrale flater som admin-grensesnitt                            |
| Symbol | Luftigere stil med lukknapp, passer for løsninger som matcher oslo.kommune.no |

<ImageWrapper>
  <img
    src="/assets/komponenter/modal/modal-1.svg"
    alt="Varianter av modal"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/modal/modal-2.svg"
    alt="Varianter av modal"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk modal når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "du trenger en bekreftelse på en kritisk handling (for eksempel ved sletting eller endringer som ikke kan angres)",
    "du vil vise ekstra informasjon uten å forlate siden",
    "du vil vise et skjema brukeren må fylle ut umiddelbart",

]}
/>

### Unngå modal når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "innholdet er langt eller komplekst, bruk heller en ny side",
    "det er flere steg i prosessen",
    `informasjonen ikke er kritisk, bruk heller <a href="${getComponentHref("accordion")}">accordion</a> eller lignende`,

]}
/>

### Bruk modaler med omhu

Modaler er ofte forstyrrende, og regnes sjelden som god brukeropplevelse. De bryter brukerens flyt, tar over skjermen og gir inntrykk av at noe haster, selv når det ikke gjør det.

En modal kan få brukeren til å miste tråden i oppgaven de jobber med. De vet kanskje ikke hvorfor den dukker opp, hvordan den lukkes eller om de må gjøre noe. Dette gjelder særlig for brukere med konsentrasjonsvansker, nedsatt syn eller skjermleser.

I følge [Nielsen Norman Group](https://www.nngroup.com/articles/modal-nonmodal-dialog/) kan modaler skape usikkerhet eller frustrasjon hvis de ikke er forventet eller blokkerer viktig innhold.

<ContentItem width="narrow" removeBottomMargin>
  <PktMessagebox skin="blue" client:only="react" title="">
    <span>
      Er innholdet faktisk viktig nok til å avbryte brukeren? Og er det tydelig
      hva brukeren skal gjøre? Modal er en forstyrrelse. Bruk den bare når det
      er helt nødvendig, og gjør det tydelig hva brukeren skal gjøre.
    </span>
  </PktMessagebox>
</ContentItem>

Vi anbefaler at du tester modalen i bruk – helst med faktiske brukere – før du setter den i produksjon. Det er den beste måten å sikre at modalen hjelper, ikke hindrer.

### Ikke åpne modal automatisk

En modal skal aldri vises uten at brukeren har gjort noe som tilsier det. Det må alltid være en tydelig trigger som gjør at brukeren forventer et avbrudd.

### Gi brukeren en tydelig handling å utføre

En modal uten knapp eller neste steg skaper frustrasjon. Sørg for at det er tydelig hva brukeren skal gjøre, for eksempel lagre, sende inn, slette eller avbryte.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/modal/modal-3.svg",
    imgAlt: "Eksempel på riktig bruk av modal",
    caption:
      "Bruk modal når du vil gi mer informasjon, uten at det forstyrrer resten av oppgaven brukeren jobber med",
  }}
  badExample={{
    image: "/assets/komponenter/modal/modal-4.svg",
    imgAlt: "eksempel på dårlig bruk av modal",
    caption:
      "Unngå utydelige modaler der brukeren blir usikker på hva som skjer etter trykk eller interaksjon",
  }}
/>

### Ikke bruk modaler til lange skjemaer eller mye interaksjon

Hvis modalen inneholder mange felt eller seksjoner, velg heller en egen side. Det gir bedre oversikt og navigasjon, særlig på små skjermer.

### Ikke bruk modal til ukritisk informasjon

Modal passer ikke for små oppdateringer eller informasjon som kan vises på en roligere måte. Bruk inline-elementer eller infoseksjoner (for eksempel <a href={getComponentHref("messagebox")}>messagebox</a>) i stedet.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/modal/modal-5.svg",
    imgAlt: "Eksempel på riktig bruk av modal",
    caption: "Bruk modal til kritiske handlinger og beskjeder",
  }}
  badExample={{
    image: "/assets/komponenter/modal/modal-6.svg",
    imgAlt: "eksempel på dårlig bruk av modal",
    caption:
      "Unngå modal ikke haster eller krever brukerens umiddelbare oppmerksomhet",
  }}
/>

### Når du viser feilmeldinger i modal

Bruk komponenten <a href={getComponentHref("alert")}>alert</a> for å vise feil, advarsler eller suksessmeldinger inne i modalen. Ikke endre bakgrunn eller tekstfarge på modalen for å signalisere alvor.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/modal/modal-7.svg",
    imgAlt: "Eksempel på riktig bruk av modal",
    caption: "Gå for å endre elementer i innholdet for å fremheve alvorlighetsgraden av en handling",
  }}
  badExample={{
    image: "/assets/komponenter/modal/modal-8.svg",
    imgAlt: "eksempel på dårlig bruk av modal",
    caption: "Unngå å endre fargen til modalen",
  }}
/>
</ContentSection>

## Responsivitet

Når brukeren har mindre skjermplass, for eksempel på mobil, tar modaler ofte over hele visningen. Det kan føre til at brukeren mister oversikten, eller blir usikker på hva som skjer.

På mobil er det derfor ekstra viktig at modalen

- oppleves som naturlig del av brukerflyten
- har én tydelig handling og ikke flere valg som krever vurdering
- er enkel å lukke med tydelig lukknapp og støtte for å bruke “Esc”/tilbake

Unngå å vise modaler med mye innhold, flere valg eller lange skjemaer på mobil. Det kan være krevende å navigere, spesielt med skjermtastatur oppe, og gir ofte en dårlig opplevelse.

Test alltid modal på mobilskjerm, i både stående og liggende visning. Pass på at innholdet ikke kuttes, at brukeren enkelt forstår hva som skjer, og at det er lett å gå tilbake.

<PktMessagebox skin="blue" client:only="react" title="">
  <span>
    Modaler på mobil fungerer best når de er korte, enkle og har én klar
    beskjed. Alt annet bør vurderes løst på en annen måte.
  </span>
</PktMessagebox>

<ImageWrapper>
  <img
    src="/assets/komponenter/modal/modal-9.svg"
    alt="modal på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

### Modal må være tilgjengelig for alle

Modal er en dialogboks som vises over innholdet på siden. Den bruker HTML-elementet `<dialog>`, som automatisk setter fokus på det første fokuserbare elementet når modalen åpnes. I Punkt sin løsning er dette ofte lukknappen, og den får derfor autofocus. Vi anbefaler alltid å vise lukknappen, det gir forutsigbarhet og kontroll for brukeren.

### Fokus skal styres riktig

Når modalen åpnes, skal fokus flyttes inn i modalen automatisk, helst til første interaktive element. Fokus må holdes inne i modalen så lenge den er åpen. Brukeren skal ikke kunne tabbe seg «bak» eller ut av den. Når modalen lukkes, skal fokus returneres til det elementet som åpnet den.

### Gi brukeren en tydelig vei ut

Alle modaler må kunne lukkes med både "Esc" og en synlig lukknapp. Det gjør det enkelt å forstå hvordan man kommer seg videre, og er spesielt viktig for brukere med motoriske utfordringer.

Merk: "Esc" fungerer bare dersom du åpner modalen med den innebygde funksjonen `showModal()`. Dette vises i kodeeksemplene lenger ned.

### Tastaturnavigasjon må fungere

Alle knapper og felt inne i modalen må kunne nås og brukes med tastatur. Hvis modalen inneholder et skjema, må submit-knappen være wrappet i `<form method="dialog">`. Da lukkes modalen automatisk når skjemaet sendes inn, uten at du trenger ekstra logikk.

### Tittelen må være tydelig

Modalen skal alltid ha en tittel i en` <h1>`-tag. Dette hjelper skjermlesere med å tolke innholdet, og gir god kontekst for alle brukere.

### Tilpass visning på små skjermer

På mobil og små skjermer skal modalen utvide seg og ta hele bredden. Modalen justerer seg automatisk når skjermen er smalere enn 576 px (36 rem). Vi anbefaler å teste dette i praksis, særlig hvis du har mye innhold i modalen.

<div class="cards-container">
  <PktLinkCard
    title="<dialog> element (MDN)"
    skin="beige"
    href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog"
    iconName="chevron-right"
    client:only="react"
  >
    Teknisk dokumentasjon og forklaring av dialog-elementet i HTML. Attributter,
    metoder og bruksmønstre.
  </PktLinkCard>
  <PktLinkCard
    title="WAI-ARIA Authoring Practices: Dialog (W3C)"
    skin="beige"
    href="https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/"
    iconName="chevron-right"
    client:only="react"
  >
    Hvordan bygge en universelt utformet modal
  </PktLinkCard>
</div>

</ContentSection>

## Anatomi

| Element                     | Beskrivelser                                              |
| --------------------------- | --------------------------------------------------------- |
| 1. Tittel                   | Overskriften i modalen, gir brukeren kontekst             |
| 2. Lukke-ikon               | Knapp med ikon oppe til høyre, skal alltid være synlig    |
| 3. Innhold                  | Tekst, skjemaelementer, instruksjoner eller annet innhold |
| 4. Valgfritt innhold (slot) | Område for egendefinert innhold                           |
| 5. Handlinger               | En eller flere knapper nederst i modalen                  |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/modal/modal-10.svg"
    alt="Anatomi på Modal."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="modal" />
</ContentSection>

## Props

<SpecList specName="modal" />


---


### Component Specification

**Element name**: `pkt-modal`

**React component**: `PktModal`

**CSS class**: `.pkt-modal`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `headingText` | `headingText` | string | `-` | Heading tekst på modalen |
| `hideCloseButton` | `hideCloseButton` | boolean | `False` | Gjemmer lukkeknappen. Dersom denne er satt til true, vil ikke lukkeknappen vises, og dermed er det viktig at man tilbyr en annen måte som f.eks. en knapp for å lukke modalen på. |
| `closeOnBackdropClick` | `closeOnBackdropClick` | boolean | `False` | Lukk modalen når bakgrunnen trykkes på |
| `closeButtonSkin` | `closeButtonSkin` | `blue`, `yellow-filled` | `blue` | Stil på lukkeknappen |
| `size` | `size` | `small`, `medium`, `large` | `medium` | Størrelsen på modalen |
| `variant` | `variant` | `dialog`, `drawer` | `dialog` | Standard dialog eller skuff |
| `drawerPosition` | `drawerPosition` | `left`, `right` | `right` | Posisjonen til skuffen |
| `transparentBackdrop` | `transparentBackdrop` | boolean | `False` | Bakgrunnen er gjennomsiktig |


#### Events

- **`background-click`**: Event som trigges når bakgrunnen trykkes på
- **`close`**: Event som trigges når meldingsboksen lukkes



### TypeScript Interface

```typescript
export interface IPktModal {
  headingText?: string
  removePadding?: boolean
  hideCloseButton?: boolean
  closeOnBackdropClick?: boolean
  closeButtonSkin?: 'blue' | 'yellow-filled'
  size?: TPktSize
  variant?: 'dialog' | 'drawer'
  drawerPosition?: 'left' | 'right'
  transparentBackdrop?: boolean
}
```
