# Card

**Generated**: 2025-11-06T10:52:48.939823
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/card/index.mdx`
- `component-specs/card.json`
- `packages/elements/src/components/card/card.ts`
- `packages/elements/src/components/card/index.ts`

---

## Documentation


# Card

<Lead releaseDate="03.10.2024" lastUpdated="20.05.2025">
  Card (kort) brukes for å gruppere innhold som hører sammen, og kan inneholde
  tekst, bilde, ikon, knapp og lenker, eller en kombinasjon av disse. Card gjør
  det enklere å skanne, sammenligne og velge mellom flere elementer.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ card: cardSpec }}
  previewJson={cardPreview}
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Link card"
    skin="blue"
    href={getComponentHref("linkcard")}
    iconName="chevron-right"
    client:only="react"
  >
    Når hele cardet kun skal være en lenke uten fleksibelt innhold.
  </PktLinkCard>

<PktLinkCard
  title="Table"
  skin="blue"
  href={getComponentHref("table")}
  iconName="chevron-right"
  client:only="react"
>
  Når du skal vise strukturerte data i kolonner og rader.
</PktLinkCard>

  <PktLinkCard
    title="Alert"
    skin="blue"
    href={getComponentHref("alert")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du vil vise en fremhevet melding med ikon og tekst.
  </PktLinkCard>
</div>

## Varianter

Card finnes i to hovedvarianter. Du kan kombinere disse med ulike skins og farger.

| Layout    | Bruk                                                                                     |
| --------- | ---------------------------------------------------------------------------------------- |
| Portrait  | Innhold stables vertikalt, fungerer godt når du legger flere card ved siden av hverandre |
| Landscape | Når du vil bruke mer av bredden, f.eks. i desktop-visning                                |

<ImageWrapper>
  <img
    src="/assets/komponenter/card/card-1.svg"
    alt="Eksempler på layout-variantene av card"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/card/card-2.svg"
    alt="Eksempler på layout-variantene av card"
    aria-hidden="true"
  />
</ImageWrapper>

| Skin       | Bruk                               |
| ---------- | ---------------------------------- |
| Outlined   | Når du vil ramme inn uten bakgrunn |
| Filled     | Full bakgrunnsfarge                |
| No padding | Fjerner marger inne i cardet       |

<ImageWrapper>
  <img
    src="/assets/komponenter/card/card-3.svg"
    alt="Eksempler på skin-variantene av card"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/card/card-4.svg"
    alt="Eksempler på skin-variantene av card"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/card/card-5.svg"
    alt="Eksempler på skin-variantene av card"
    aria-hidden="true"
  />
</ImageWrapper>

| Bildestil | Bruk                                     |
| --------- | ---------------------------------------- |
| Square    | Gir et strammere uttrykk                 |
| Round     | Mer lekent, harmonerer med Oslo-profilen |

<ImageWrapper>
  <img
    src="/assets/komponenter/card/card-6.svg"
    alt="Eksempler på bildestil-variantene av card"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/card/card-7.svg"
    alt="Eksempler på bildestil-variantene av card"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk card når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "du vil gruppere informasjon",
    "du trenger oversiktlige valg i grid eller liste",
    "du ønsker fleksibel visning med eller uten bilde, innhold eller handling",
  ]}
/>

### Unngå card når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "du bare viser én ting og ikke trenger visuell gruppering",
    `informasjonen egner seg bedre i ren tekst eller tabell`,
  ]}
/>

### Tilpass cardet til ditt innholdsbehov

Komponenten er fleksibel, og du kan selv velge om du vil bruke:

- tekst
- tittel
- undertittel
- bilde
- tags over eller under innholdet
- lenker eller knapper

Du kan også velge om hele cardet skal være klikkbart.

Unngå å overlesse cardet. Bruk luft og visuell prioritering. Om du bruker flere card i samme løsning, kan det være lurt å designe alle like og bruke de samme elementene konsekvent.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/card/card-8.svg",
    imgAlt: "Eksempel på ryddig, tydelig og konkret innhold",
    caption: "Hold innholdet ryddig, tydelig og konkret",
  }}
  badExample={{
    image: "/assets/komponenter/card/card-9.svg",
    imgAlt: "Eksempel på cardet med mye innhold.",
    caption: "Unngå å overlesse cardet med innhold",
  }}
/>

### Skriv tydelig og konsist

Innholdet i et card skal være lett å skanne. Bruk korte titler og tydelig handling. Hvis cardet er klikkbart, må det være klart hvor det leder, følg [regler for god lenketekst](https://www.uutilsynet.no/veiledning/lenker/214).

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/card/card-10.svg",
    imgAlt: "Eksempel kort og tydelig tekst på radene",
    caption: "Skriv lettlest innhold og tydelig lenketekst",
  }}
  badExample={{
    image: "/assets/komponenter/card/card-11.svg",
    imgAlt: "Eksempel lang innhold på radene",
    caption:
      "Unngå uklart innhold og utydelig lenketekst",
  }}
/>
</ContentSection>

## Responsivitet

Card tilpasser seg automatisk til ulike skjermstørrelser. Innhold bryter linjer og grid flyter om ved behov.

Landscape-card skaleres automatisk ned til portrait på små skjermer. På mobil anbefaler vi å bruke portrait-layout som utgangspunkt, særlig dersom cardsene vises i listevisning.

Vi anbefaler at du uansett tester ulike visningsformer og antall cards i din løsning.

<ImageWrapper>
  <img
    src="/assets/komponenter/card/card-12.svg"
    alt="Card på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

## Universell utforming

Card skal kunne brukes og forstås av alle, også de som bruker tastatur eller skjermleser.
Her er noen viktige prinsipper for å sikre tilgjengelighet:

### Struktur og semantikk

Bruk riktig heading-nivå i konteksten der cardet vises, og sørg for at alle card på samme nivå i løsningen også benytter samme heading-nivå. Dette gir god struktur for skjermlesere og visuell lesing.

### Interaktive og ikke-interaktive card

Et card kan enten være:

- Interaktivt: hele cardet fungerer som en lenke eller knapp
- Ikke-interaktivt: cardet inneholder klikkbare elementer som knapper eller lenker

Unngå å blande disse. Ikke legg knapper inne i et kort som allerede er klikkbart - knappen vil være umulig å nå med musepeker. Kort sagt: én handling per område.

### Tastaturnavigasjon og fokus

Brukeren skal kunne bruke “Tab” for å navigere:

- I interaktive card: Hele cardet er et tab stop og aktiveres med “Enter” eller “Mellomrom”.
- I ikke-interaktive card: Bare knapper og lenker er fokuserbare

Alle fokuserbare elementer har tydelig visuell fokusindikator. Skriv tydelig lenketekst som skjermleseren forstår, les mer om [gode lenketekster her](https://www.uutilsynet.no/veiledning/lenker/214).

Les mer om universell utforming av cards:

<div class="cards-container">
  <PktLinkCard
    title="Inclusive Components – Cards (inclusive-components.design)"
    skin="beige"
    href="https://inclusive-components.design/cards/"
    iconName="chevron-right"
    client:only="react"
  >
    En praktisk og pedagogisk gjennomgang av hvordan cards kan være universelt
    utformet.
  </PktLinkCard>
</div>

</ContentSection>

## Anatomi

| Element      | Beskrivelse                                                                                                         |
| ------------ | ------------------------------------------------------------------------------------------------------------------- |
| 1. Label     | Overskrift for kortet. Bruk `<h3>` eller tilsvarende semantikk                                                      |
| 2. Brødtekst | Forklarende tekst som utdyper innholdet                                                                             |
| 3. Bilde     | Illustrasjon eller fotografi (valgfritt)                                                                            |
| 4. Handling  | Lenke eller knapp for navigasjon eller videre handling, brukes kun dersom ikke hele cardet er klikkbart (valgfritt) |
| 5. Container | Kortets ramme, med eller uten kantlinje og padding                                                                  |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/card/card-13.svg"
    alt="Accordion anatomi."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="card" />
</ContentSection>

## Props

<SpecList specName="card" />


---


### Component Specification

**Element name**: `pkt-card`

**React component**: `PktCard`

**CSS class**: `.pkt-card`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `heading` | `heading` | string | `-` | Tittel på card |
| `headingLevel` | `headingLevel` | `1`, `2`, `3`, `4`, `5`, `6` | `3` | Nivået på headingen. Brukes for tilgjengelighet. |
| `subheading` | `subheading` | string | `-` | Undertittel på card |
| `layout` | `layout` | `vertical`, `horizontal` | `vertical` | Stående/liggende. Portrett/landskap. Horisontal/vertikal. Kjært barn… |
| `skin` | `skin` | `outlined`, `outlined-beige`, `gray`, `blue`, `beige`, `green` | `outlined` | Fargen på card. Velg mellom outlined, outlined-beige, gray, blue, beige og green. |
| `padding` | `padding` | `none`, `default` | `default` | Skal det være padding på innsiden av card? |
| `metaLead` | `metaLead` | string | `False` | Undertekst med fet skriftvekt |
| `metaTrail` | `metaTrail` | string | `False` | Undertekst med normal skriftvekt |
| `tagPosition` | `tagPosition` | `top`, `bottom` | `top` | Plassering av tags i card |
| `clickCardlink` | `clickCardlink` | string | `-` | Href sendes inn som streng for å gjøre card klikkbart. Heading brukes som lenktetekst. |
| `openLinkInNewTab` | `openLinkInNewTab` | boolean | `False` | Velg denne dersom du ønsker at lenken i card skal åpnes i ny fane. |
| `borderOnHover` | `borderOnHover` | boolean | `True` | Vi anbefaler hoverborder på klikkbart card. Kan slås av ved behov. |
| `image` | `image` | object | `-` | Bildet på card. Tar inn et objekt av typen {src: string, alt: string}. |
| `imageShape` | `imageShape` | `square`, `round` | `square` | Her kan vi velge om bildet i card skal være firkantet eller rundt. |
| `tags` | `tags` | array | `-` | Liste av tags på card. Tar inn et array med objekter med følgende stringproperties: skin, iconName, ariaLabel, text |
| `ariaLabel` | `ariaLabel` | string | `-` | Tekst til skjermleser for aria-label på card. Settes automatisk til headingen, eller subheadingen der heading ikke eksisterer. |



### TypeScript Interface

```typescript
export interface IPktCard {
  ariaLabel?: IAriaAttributes['aria-label']
  metaLead?: string | null
  metaTrail?: string | null
  layout?: TLayout
  heading?: string
  headingLevel?: IPktHeading['level']
  image?: { src: string; alt: string }
```
