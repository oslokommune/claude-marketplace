# Accordion

**Generated**: 2025-11-06T10:52:48.933018
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/accordion/index.mdx`
- `component-specs/accordion.json`
- `component-specs/accordionItem.json`
- `packages/elements/src/components/accordion/accordionitem.ts`
- `packages/elements/src/components/accordion/accordion.ts`
- `packages/elements/src/components/accordion/index.ts`

---

## Documentation



# Accordion

<Lead releaseDate="25.04.2024" lastUpdated="26.05.2025">
  Accordion (også kalt expandable, trekkspill eller uttrekkspanel) brukes til å
  gruppere innhold som kan åpnes og lukkes. Det hjelper brukeren å få oversikt
  og gjør det enklere å fokusere på én ting om gangen. Accordion egner seg godt
  når du har mye informasjon, men ikke ønsker å overvelde brukeren.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{
    accordion: accordionSpec,
    accordionItem: accordionItemSpec,
  }}
  previewJson={accordionPreview}
  fullWidth
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Tabs"
    skin="blue"
    href={getComponentHref("tabs")}
    iconName="chevron-right"
    client:only="react"
  >
    Lar brukeren bytte mellom ulike visninger eller seksjoner.
  </PktLinkCard>
  <PktLinkCard
    title="Modal"
    skin="blue"
    href={getComponentHref("modal")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du vil vise detaljert innhold uten å ta brukeren ut av kontekst.
  </PktLinkCard>
  <PktLinkCard
    title="Messagebox"
    skin="blue"
    href={getComponentHref("messagebox")}
    iconName="chevron-right"
    client:only="react"
  >
    Grupperer informasjon uten funksjonalitet for å åpne og lukke.
  </PktLinkCard>
</div>

## Varianter

### Typer

Accordion har to ulike typer med ulike bruksområder:

| Type             | Beskrivelse                                                                                                 |
| ---------------- | ----------------------------------------------------------------------------------------------------------- |
| Standard         | Flere rader kan åpnes samtidig                                                                              |
| Single (en åpen) | Brukes når bare ett panel bør være åpent, for eksempel ved trinnvis guiding eller steg-for-steg-informasjon |

<ImageWrapper>
  <img
    src="/assets/komponenter/accordion/accordion-1.svg"
    alt="Eksampel på standard accordion."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/accordion/accordion-2.svg"
    alt="Eksampel på accordion."
    aria-hidden="true"
  />
</ImageWrapper>

### Størrelser

Accordion kommer i to ulike størrelser:

| Størrelse | Beskrivelse                                                                                                                                                                       |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Default   | Standard størrelse. Brukes når du har vanlig mengde innhold og vil at komponenten skal ta litt mer plass for bedre lesbarhet.                                                     |
| Compact   | Kompakt størrelse. Brukes når du vil spare plass eller når accordion skal stå i et område med mange andre elementer. Passer godt der du vil ha en mer kompakt og diskret løsning. |

<ImageWrapper>
  <img
    src="/assets/komponenter/accordion/accordion-3.svg"
    alt="Eksampel på standard accordion."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/accordion/accordion-4.svg"
    alt="Eksampel på accordion."
    aria-hidden="true"
  />
</ImageWrapper>

### Skins

Accordion kommer i fire ulike skins (farger og styling):

| Skin       | Beskrivelse                  |
| ---------- | ---------------------------- |
| Borderless | Enkel bakgrunnsfarge og stil |
| Border     | Kantlinje på radene          |
| Beige      | Annenhver rad er beige       |
| Blue       | Annenhver rad er blå         |

<ImageWrapper>
  <img
    src="/assets/komponenter/accordion/accordion-5.svg"
    alt="Eksampel på borderless accordion."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/accordion/accordion-6.svg"
    alt="Eksampel på blue accordion ."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/accordion/accordion-7.svg"
    alt="Eksampel på border accordion ."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue" >
## Retningslinjer for bruk

### Bruk accordion når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "du vil presentere mye informasjon uten å overvelde brukeren",
    "brukeren ikke trenger å lese alt for å forstå helheten",
    "du har relaterte temaer som kan grupperes sammen",
  ]}
/>

### Unngå accordion når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "alt innhold må leses i én sammenheng for å forstå helheten",
    `du trenger mer kompleks interaktivitet, bruk heller <a href="${getComponentHref("modal")}">modal</a> eller  <a href="${getComponentHref("tabs")}">tabs</a>`,
  ]}
/>

### Radene må ha tydelige overskrifter

Tittelen i hvert rad må være beskrivende og kort. Brukeren må forstå hva de
finner bak hver rad uten å måtte åpne den. De bør også kun inneholde ett
enkelt tema.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/accordion/accordion-8.svg",
    imgAlt: "Eksempel på tydelig overskrift",
    caption: "Skriv tydelige og beskrivende overskrifter",
  }}
  badExample={{
    image: "/assets/komponenter/accordion/accordion-9.svg",
    imgAlt: "Eksempel ulogiske overskrifter",
    caption: "Unngå lange og ulogiske titler med flere temaer",
  }}
/>

### Hold innholdet kort og konsist

Innholdet i hvert rad bør være maks én til to korte setninger. Hvis det blir
for langt, vurder å dele det opp eller flytte det til en egen side.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/accordion/accordion-10.svg",
    imgAlt: "Eksempel på kort og tydelig tekst på radene",
    caption: "Skriv tydelig og så kort som mulig",
  }}
  badExample={{
    image: "/assets/komponenter/accordion/accordion-11.svg",
    imgAlt: "Eksempel på lang innhold på radene",
    caption:
      "Unngå å bruke accordion til veldig langt innhold, led heller brukeren til en annen side om du har mye innhold",
  }}
/>

### Bruk accordion til innhold som logisk hører sammen

Accordion skal hjelpe brukeren å orientere seg. Derfor må innholdet høre
sammen. Tenk på det som en liste med elementer som tilhører samme kategori.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/accordion/accordion-12.svg",
    imgAlt: "Eksempel på accordion med relaterte innhold",
    caption: "Hold innholdet i accordion relatert til hverandre",
  }}
  badExample={{
    image: "/assets/komponenter/accordion/accordion-13.svg",
    imgAlt: "Eksempel på innhold som ikke hører sammen",
    caption: "Unngå å bruke accordion til å samle informasjon som ikke hører sammen",
  }}
/>
</ContentSection>

## Responsivitet

Accordion fungerer godt på alle skjermstørrelser. Den kollapser eller ekspanderer innhold uten å endre layout.

Du bør likevel teste og forsikre deg om at

    - overskrifter ikke avkortes
    - det er lett å se hva som er åpent/lukket, også på mobil
    - marginer og spacing mellom radene er riktig

<ImageWrapper>
  <img
    src="/assets/komponenter/accordion/accordion-14.svg"
    alt="Accordion på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

## Universell utforming

### Innholdet må gi mening med skjermleser

Accordion må være tilgjengelig for alle, også for brukere som navigerer med
tastatur eller bruker skjermleser. Bruker du komponenten som den er vil du få
funksjonaliteten, men du burde forsikre deg om at innholdet gjør det lett for
brukeren å navigere i komponenten.

### Komponenten støtter

- navigasjon mellom accordion-rader med "Tab" og "Shift" + "Tab"
- åpning og lukking av rader med Enter eller Space
- tydelig visuell fokusindikator når en rad er i fokus
- tydelig markering av hvilken rad som er åpen

### Er Punkt sin accordion tilgjengelig nok?

Punkt sin accordion-komponent bruker HTML-elementene `details` og
`summary`. Dette er fordi disse elementene er semantiske og
tilgjengelige i seg selv. Når man først leser om accordion på internett
refereres det ofte til en [test gjort av Haskall i
2019](https://www.hassellinclusion.com/blog/accessible-accordions-part-2-using-details-summary/)
som argumentasjon for å bruke andre alternativer (ofte buttons wrappet
i headings som f.eks. [WAI-ARIA sin accordion
Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/examples/accordion/#sc1_label).
Dette er fordi `details` og `summary`-elementene har hatt dårlig
støtte i enkelte skjermlesere tidligere. Dette er noe som har blitt, og blir
bedre med tiden. I dag er støtten god nok til at vi kan bruke disse
elementene.

Mer om universell utforming av accordion:

<div class="cards-container">
  <PktLinkCard
    title="Accordion Pattern (WAI-ARIA)"
    skin="beige"
    href="https://www.w3.org/WAI/ARIA/apg/patterns/accordion/"
    iconName="chevron-right"
    client:only="react"
  >
    Retningslinjer for universelt utformede accordions
  </PktLinkCard>
</div>

</ContentSection>

## Anatomi

| Element                | Beskrivelse                                          |
| ---------------------- | ---------------------------------------------------- |
| 1. Tittel (valgfritt)  | Brukes som en forklaring over hele accordion-gruppen |
| 2. Åpne- og lukke-ikon | Viser status og gir visuell ledetråd (pil-ikon)      |
| 3. Overskrift          | Tittel på hver rad, vises som summary                |
| 4. Innhold             | Teksten eller innholdet som vises når raden åpnes    |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/accordion/accordion-15.svg"
    alt="Accordion anatomi."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode
Accordion lar brukeren åpne og lukke innhold. I Punkt er komponenten bygget på de semantiske HTML-elementene `<details>` og `<summary>`. Dette gir innebygd støtte for tastaturnavigasjon og gjør komponenten både enkel og tilgjengelig.

For React og Elements tilbyr Punkt både wrapper-komponenten `<PktAccordion>` og enkeltstående `<PktAccordionItem>`.

Som standard kan flere accordion-rader være åpne samtidig. Ønsker du at kun én rad skal være åpen, må du styre tilstanden selv. Les mer under "Begrens antall åpne rader".

<TechDetails specName="accordion" extraSpecs={["accordionItem"]}></TechDetails>

### Begrens antall åpne rader

Som standard støtter `Accordion` åpning av flere rader samtidig. For å styre at kun én rad kan være åpen om gangen, må man styre alle radene sin toggle tilstand lokalt - det vil si at man må overstyre den automatiske tilstandshåndteringen til komponenten. Dette gjøres ved å sette en boolean `isOpen` og en `onClick/click` funksjon på `<AccordionItem>/<pkt-accordion-item>` som styrer åpne-lukke tilstanden til komponenten.

I React trenger man å sende inn `event` for å forhindre inkonsekvent oppførsel. Dette er fordi `<details>`-elementet har sin egen innebygde `toggle`-funksjon som kan føre til inkonsekvens når vi prøver å sette `isOpen`-propen i React. I `<AccordionItem>` kjører vi `e.preventDefault()` for å forhindre at `<details>`-elementet sin innebygde `toggle`-funksjon kjører. Sjekk eksemplene under!

<CodeTabs hideWebTab showElementsTab hideVueTab client:only="react">
<div class="elements tabcontent">

```js
<script>
  @state() private openedItem: string = ''
  function toggleCurrentOpenItem(e: MouseEvent, id: string) {
    e.preventDefault() // Prevent default behavior to ensure controlled state
    if (this.openedItem === id) {
      this.openedItem = ''
    } else {
      this.openedItem = id
    }
  }
</script>

<pkt-accordion skin="blue" aria-labelledby="accordion-standard">
  <pkt-accordion-item
    id=${item.id}
    title=${item.title}
    .isOpen=${this.openedItem == item.id}
    @click=${(e: MouseEvent) => this.toggleCurrentOpenItem(e, item.id)}
  >
    ${item.content}
    <p>Element innhold</p>
  </pkt-accordion-item>
</pkt-accordion>
```

</div>

<div class="react tabcontent">

```js
const [openedItem, setOpenedItem] = useState<string>('')

const toggleCurrentOpenItem = (e: React.MouseEvent, id: string) => {
  if (openedItem.includes(id)) {
    setOpenedItem('')
  } else {
    setOpenedItem(id)
  }
}

return (
  <PktAccordion compact skin={"borderless"}>
    {accordionItems.map((item, index) => {
      return (
        <PktAccordionItem
          id={item.id}
          key={item.id}
          title={item.title}
          defaultOpen={index === 0}
          isOpen={openedItem === item.id}
          onClick={(e) => toggleCurrentOpenItem(e, item.id)}
        >
          {item.content}
        </PktAccordionItem>
      );
    })}
  </PktAccordion>
)

```

</div>
</CodeTabs>

</ContentSection>

## Props

### PktAccordion

<SpecList specName="accordion" />

### PktAccordionItem

<SpecList specName="accordionItem" />


---


### Component Specification

**Element name**: `pkt-accordion`

**React component**: `PktAccordion`

**CSS class**: `.pkt-accordion`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `skin` | `skin` | `borderless`, `outlined`, `beige`, `blue` | `borderless` | Hvordan skal accordion se ut? |
| `ariaLabelledBy` | `ariaLabelledBy` | string | `-` | ID'en til elementet som beskriver accordionen. Brukes for tilgjengelighet. |
| `compact` | `compact` | boolean | `False` | En kompakt accordion har mindre padding og margin |
| `name` | `name` | string | `-` | Navn på accordion-gruppen, som brukes for å gruppere flere accordion-items sammen. |



### Component Specification

**Element name**: `pkt-accordion-item`

**React component**: `PktAccordionItem`

**CSS class**: `.pkt-accordion-item`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `title` | `title` | string | `-` | Tittelen som vises i sammendraget av elementet |
| `id` | `id` | string | `-` | ID-en til accordion-elementet |
| `defaultOpen` | `defaultOpen` | boolean | `-` | Et accordion-element kan settes til å være åpent som standard når siden lastes |
| `isOpen` | `isOpen` | boolean | `-` | En prop som kan brukes til å overstyre lokal isOpen-tilstand, og beskriver om accordion-elementet er åpent eller ikke |
| `name` | `name` | string | `-` | Navn på accordion-element, som brukes for å gruppere flere accordion-elementer sammen. |



### TypeScript Interface

```typescript
export interface IPktAccordionItem {
  defaultOpen?: boolean
  id: string
  title: string
  skin?: TPktAccordionSkin
  compact?: boolean
  isOpen?: boolean
  name?: string | undefined
}
```
