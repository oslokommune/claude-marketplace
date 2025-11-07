# Switch

**Generated**: 2025-11-06T10:52:48.964026
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/switch/index.mdx`

---

## Documentation



# Switch

<Lead
  releaseDate="31.01.2024"
  lastUpdated="13.03.2025"
>
  En switch (også kalt toggle eller bryter) lar brukeren veksle mellom to 
  mulige tilstander – av eller på. Den brukes for handlinger som får 
  umiddelbar effekt, uten at brukeren må bekrefte eller lagre.

Typiske bruksområder er å skru på varsler, aktivere en funksjon eller slå av
en innstilling.

For demo og implementasjonsdetaljer kan du se <a href={getComponentHref("checkbox")}>checkbox</a>.

</Lead>

## Eksempler

<CodeExample toggleMode>

<PktCheckbox isSwitch id="checboxSingle" label="Switch" client:only="react" />
<p>
  Med <code>labelPosition</code> kan man legge label til venstre:
</p>
<PktCheckbox
  isSwitch
  id="checboxSingle2"
  label="Switch"
  labelPosition="left"
  client:only="react"
/>
<p>Switch kan også presenteres med en skjult label:</p>
<PktCheckbox
  isSwitch
  id="checboxSingle3"
  label="Switch"
  hideLabel
  client:only="react"
/>

</CodeExample>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Checkbox"
    skin="blue"
    href={getComponentHref("checkbox")}
    iconName="chevron-right"
    client:only="react"
  >
    For valg i skjema eller når lagring kreves
  </PktLinkCard>
  <PktLinkCard
    title="Radio button"
    skin="blue"
    href={getComponentHref("radiobuttons")}
    iconName="chevron-right"
    client:only="react"
  >
    Når brukeren skal velge kun ett alternativ i en liste
  </PktLinkCard>
  <PktLinkCard
    title="Button"
    skin="blue"
    href={getComponentHref("button")}
    iconName="chevron-right"
    client:only="react"
  >
    For enkeltstående handlinger som krever bekreftelse
  </PktLinkCard>
</div>

## Varianter

### Variant

| Variant          | Beskrivelse                                  |
| ---------------- | -------------------------------------------- |
| Standard         | Når switch står alene eller i en enkel liste |
| Med ramme (tile) | Når du vil ramme inn en switch visuelt       |

<ImageWrapper>
  <img
    src="/assets/komponenter/switch/switch-1.svg"
    alt="Varianter: Standard og med ramme (tile)"
    aria-hidden="true"
  />

    <img
    src="/assets/komponenter/switch/switch-2.svg"
    alt="Varianter: Standard og med ramme (tile)"
    aria-hidden="true"

/>

</ImageWrapper>

### Type

| Type         | Beskrivelse                                                                         |
| ------------ | ----------------------------------------------------------------------------------- |
| Frittstående | Brukes når konteksten er tydelig, for eksempel i tabeller eller lister              |
| Med tekst    | Brukes når det er nødvendig å forklare hva som skrus av/på, kan også ha hjelpetekst |

<ImageWrapper>
  <img
    src="/assets/komponenter/switch/switch-3.svg"
    alt="Typer: Frittstående og med tekst"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

## Retningslinjer for bruk

### Bruk switch når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "handlingen får umiddelbar effekt når den slås av eller på",
    "brukeren forventer en visuell bekreftelse på tilstanden",
    "valget gjelder én funksjon eller innstilling",
  ]}
/>

### Unngå switch når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `du trenger bekreftelse eller lagring før endringen trer i kraft (bruk <a href="${getComponentHref("checkbox")}">checkbox</a> eller <a href="${getComponentHref("button")}">button</a>)`,
    `brukeren skal kunne velge flere alternativer samtidig (bruk <a href="${getComponentHref("checkbox")}">checkbox</a>)`,
    `brukeren skal velge ett av flere alternativer (bruk <a href="${getComponentHref("radiobuttons")}">radio button</a>)`,
  ]}
/>

### Bruk switch når endring i tilstanden ikke skal kreve bekreftelse

Bruk switch for binære handlinger som slår en funksjon av eller på umiddelbart. Endringen skal tre i kraft med én gang,
uten at brukeren må bekrefte eller lagre. Gi alltid switchen en tydelig ledetekst som forteller hva som blir aktivert eller deaktivert.

<ImageWrapper>
  <img
    src="/assets/komponenter/switch/switch-4.svg"
    alt="Typer: Frittstående og med tekst"
    aria-hidden="true"
  />
</ImageWrapper>

### Switch skal ikke erstatte knapp

En switch skal ikke brukes til å starte en enkeltstående handling som normalt gjøres med en knapp. For eksempel: "Lagre endringer" bør være en button, ikke en switch.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/switch/switch-5.svg",
    imgAlt: "Gjør slik – bruk knapp for enkeltstående handlinger",
    caption: "Bruk knapp for handlinger som krever bekreftelse",
  }}
  badExample={{
    image: "/assets/komponenter/switch/switch-6.svg",
    imgAlt: "Unngå – switch som erstatning for knapp",
    caption: "Unngå switch som erstatning for knapp",
  }}
/>

### Ledeteksten skal beskrive handlingen

Ledeteksten skal fortelle hva som skrus av eller på, switchen viser statusen. Unngå å legge status direkte inn i teksten.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/switch/switch-7.svg",
    imgAlt: "Gjør slik – ledetekst beskriver handlingen",
    caption: "Skriv ledetekst som beskriver hva som skrus av eller på",
  }}
  badExample={{
    image: "/assets/komponenter/switch/switch-8.svg",
    imgAlt: "Unngå – ledetekst uttrykker status i stedet for handling",
    caption: "Unngå ledetekst som uttrykker status i stedet for handling",
  }}
/>

### Endringen skal ha umiddelbar effekt

En switch skal ikke kreve et ekstra steg for å bekrefte. Effekten skal tre i kraft idet brukeren aktiverer eller deaktiverer bryteren.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/switch/switch-9.svg",
    imgAlt: "Gjør slik – la endringen tre i kraft umiddelbart",
    caption: "La endringen tre i kraft umiddelbart når switchen aktiveres",
  }}
  badExample={{
    image: "/assets/komponenter/switch/switch-10.svg",
    imgAlt: "Unngå – ekstra lagringstrinn etter at switch er brukt",
    caption: "Unngå ekstra lagringstrinn etter at switchen er brukt",
  }}
/>
</ContentSection>

## Responsivitet

Switch fungerer på alle skjermstørrelser. Den tilpasser seg tilgjengelig plass, og bryteren og eventuell tekst bryter linjer ved behov.

- at ledetekst og bryter har god avstand og er lett å treffe på mobil
- at interaksjonen fungerer like godt i stående og liggende visning
- at skjulte etiketter fungerer på alle skjermlesere

<ImageWrapper>
  <img
    src="/assets/komponenter/switch/switch-11.svg"
    alt="Switch i ulike skjermstørrelser"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

### Switch er egentlig bare en checkbox

Switch er teknisk implementert som en checkbox med `role="switch"`, og følger samme tastaturinteraksjon: “space” aktiverer/deaktiverer.

### Bruk alltid ledetekst/etikett

Bruk alltid en etikett (synlig eller skjult) som beskriver hva bryteren gjør (WCAG 2.1: 1.3.1 Info and Relationships, 2.4.6 Headings and Labels). Ved grupper av switcher, bruk `fieldset` og `legend` for å gi kontekst.

### Switch og skjermleser

Endringen skal annonseres for skjermlesere umiddelbart ved aktivering (WAI-ARIA Switch Pattern).

<div class="cards-container">
  <PktLinkCard
    title="WAI-ARIA Switch Pattern"
    skin="beige"
    href="https://www.w3.org/WAI/ARIA/apg/patterns/switch/"
    iconName="chevron-right"
    client:only="react"
  >
    Hvordan gjøre en switch tilgjengelig og universelt utformet
  </PktLinkCard>
</div>
</ContentSection>

## Anatomi

| Element                       | Beskrivelse                             |
| ----------------------------- | --------------------------------------- |
| Ledetekst venstre (valgfritt) | Kort tekst som beskriver handlingen     |
| Switch                        | Selve bryteren som endrer tilstand      |
| Ledetekst høyre (valgfritt)   | Kort tekst som beskriver handlingen     |
| Hjelpetekst (valgfritt)       | Utfyllende forklaring under ledeteksten |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/switch/switch-12.svg"
    alt="Anatomi for Switch"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

Se <a href={getComponentHref("checkbox")}>checkbox</a> for implementasjon i kode.

</ContentSection>

## Props

Se <a href={getComponentHref("checkbox")}>checkbox</a> for egenskaper.


---

