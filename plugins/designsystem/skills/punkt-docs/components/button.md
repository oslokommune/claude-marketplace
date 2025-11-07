# Button

**Generated**: 2025-11-06T10:52:48.938575
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/button/index.mdx`
- `component-specs/button.json`
- `packages/elements/src/components/button/button.ts`
- `packages/elements/src/components/button/index.ts`

---

**Description**: Knapper er et viktig element i ethvert design. De har en viktig funksjon og er direkte knyttet til en handling (action).


## Documentation


# Button

<Lead releaseDate="13.03.2023" lastUpdated="07.07.2025">
  Button lar brukeren utføre en handling, for eksempel å sende inn et skjema,
  starte en prosess eller navigere videre. Den skal være tydelig, gi god
  tilbakemelding og plasseres der handlingen hører hjemme.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ button: buttonSpec }}
  previewJson={buttonPreviewJson}
  fullWidth
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Link"
    skin="blue"
    href={getComponentHref("link")}
    iconName="chevron-right"
    client:only="react"
  >
    Når brukeren skal navigere til en ny side.
  </PktLinkCard>
  <PktLinkCard
    title="Tag"
    skin="blue"
    href={getComponentHref("tag")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du bare skal vise en status eller kategori.
  </PktLinkCard>
  <PktLinkCard
    title="Backlink"
    skin="blue"
    href={getComponentHref("backlink")}
    iconName="chevron-right"
    client:only="react"
  >
    Når brukeren skal tilbake til et tidligere steg.
  </PktLinkCard>
</div>

## Varianter

### Skins

Buttons i Punkt har 3 ulike varianter (skins) og 3 ulike størrelser.

| Skin      | Bruk                                                   |
| --------- | ------------------------------------------------------ |
| Primary   | Hovedhandling på siden. Brukes én gang per flate       |
| Secondary | For alternative eller mindre viktige handlinger        |
| Tertiary  | Når button ikke skal ta oppmerksomhet, f.eks. «Avbryt» |

<ImageWrapper>
  <img
    src="/assets/komponenter/button/button-1.svg"
    alt="Eksampel på primary button."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/button/button-2.svg"
    alt="Eksampel på secundary button."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/button/button-3.svg"
    alt="Eksampel på tertiary button."
    aria-hidden="true"
  />
</ImageWrapper>

### Størrelser

Button kan også brukes i tre ulike størrelser:

| Størrelse        | Bruk                                    |
| ---------------- | --------------------------------------- |
| Small            | For trange flater, som tabeller         |
| Medium (default) | Standard, og skal brukes som hovedregel |
| Large            | For ekstra oppmerksomhet                |

<ImageWrapper>
  <img
    src="/assets/komponenter/button/button-4.svg"
    alt="Eksampel på small button accordion."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/button/button-5.svg"
    alt="Eksampel medium button."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/button/button-6.svg"
    alt="Eksampel large button."
    aria-hidden="true"
  />
</ImageWrapper>

### Farger

Button har også flere mulige farger. Vi anbefaler å bruke standardfargen Osloblå, men du kan spe på med andre farger i spesielle tilfeller.

| Farge              | Bruk                                        |
| ------------------ | ------------------------------------------- |
| Blue               | Standardfarge. Bruk denne så ofte som mulig |
| Blue outline       | For spesielle tilfeller, bruk med måte      |
| Green              | For å bekrefte suksess, f.eks. «Fullfør»    |
| Green outline      | For spesielle tilfeller, bruk med måte      |
| Dark green         | For spesielle tilfeller, bruk med måte      |
| Darg green outline | For spesielle tilfeller, bruk med måte      |
| Light beige        | For spesielle tilfeller, bruk med måte      |
| Dark beige outline | For spesielle tilfeller, bruk med måte      |
| Yellow             | For spesielle tilfeller, bruk med måte      |
| Yellow outline     | For spesielle tilfeller, bruk med måte      |
| Red                | For destruktive handlinger, som «Slett»     |
| Red outline        | For spesielle tilfeller, bruk med måte      |

<ImageWrapper>
  <img
    src="/assets/komponenter/button/button-7.svg"
    alt="Eksampel på button med ulike farger."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/button/button-8.svg"
    alt="Eksampel på  button med ulike farger."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/button/button-9.svg"
    alt="Eksampel på  button med ulike farger."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/button/button-10.svg"
    alt="Eksampel på  button med ulike farger."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/button/button-11.svg"
    alt="Eksampel på  button med ulike farger."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/button/button-12.svg"
    alt="Eksampel på  button med ulike farger."
    aria-hidden="true"
  />
</ImageWrapper>

| Variant             | Bruk                                               |
| ------------------- | -------------------------------------------------- |
| Label only          | Kun tekst                                          |
| Icon right          | Tekst + ikon til høyre                             |
| Icon left           | Tekst + ikon til venstre                           |
| Icon right and left | Tekst + ikon til høyre og til venstre              |
| Icon only           | Kun ikon, unngå bruk med mindre noe annet er mulig |

<ImageWrapper>
  <img
    src="/assets/komponenter/button/button-19.svg"
    alt="Eksampel på small button accordion."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/button/button-20.svg"
    alt="Eksampel medium button."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/button/button-21.svg"
    alt="Eksampel large button."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

## Retningslinjer for bruk

### Bruk button når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "brukeren skal utføre en konkret handling på siden",
    "handlingen ikke innebærer å gå til en ny side",
  ]}
/>

### Unngå button når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `handlingen er navigasjon til en ny side (bruk da heller en <a href="${getComponentHref("link")}">lenke</a>)`,
    `du vil vise status eller informasjon (bruk <a href="${getComponentHref("tag")}">tag</a> eller <a href="${getComponentHref("tabs")}">tabs</a>)`,
  ]}
/>

### Forskjellen mellom button og link

En tommelfingerregel er å skille mellom funksjonen til link og button:

- Bruk link når brukeren skal komme til en ny side
- Bruk button når brukerne skal utføre en konkret handling: logg inn, send, last opp osv.

Med det sagt, så er ikke dette noe som er satt i stein. Det vil være tilfeller der en button fungerer bedre enn en lenke selvom brukeren navigerer til en ny side, f.eks dersom det kun er én primærhandling brukeren kan gjøre på den aktuelle siden.

### Skriv tydelige tekster

Teksten i button skal være så enkel og tydelig som mulig. Bruk aktivt språk, gjerne verb i imperativ, og maks to – tre ord. Husk at teksten skal forklare hva som skjer.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/button/button-22.svg",
    imgAlt: "Eksempel klart og tydelig innhold",
    caption: "Skriv tydelig og klart innhold",
  }}
  badExample={{
    image: "/assets/komponenter/button/button-23.svg",
    imgAlt: "Eksempel ufullstendig og uklart innhold",
    caption: "Unngå ufullstendig og uklart innhold, tenk skjermleser",
  }}
/>

### Button er merkevarebærende

Buttons er noe av det brukeren legger mest merke til i en løsning. De signaliserer ikke bare handling, men også stil og tone. Derfor er det viktig å bruke farger og former som støtter Oslos visuelle identitet og gir en gjenkjennelig opplevelse.

Bruk primærfargen (mørkeblå) som hovedregel. Unngå å bruke sterke farger som grønn, rød og gul hvis det ikke er nødvendig. Disse fargene skal kun brukes for å understøtte et tydelig budskap, ikke for variasjon.

I Oslo kommunes løsninger bruker vi ikke buttons med avrundede hjørner. Formen skal være tydelig, enkel og i tråd med Oslo-profilen.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/button/button-24.svg",
    imgAlt: "Eksempel klart og tydelig innhold",
    caption: "Følg Oslo kommunes retningslinjer",
  }}
  badExample={{
    image: "/assets/komponenter/button/button-25.svg",
    imgAlt: "Eksempel ufullstendig og uklart innhold",
    caption: "Unngå egen styling og varianter av button",
  }}
/>

</ContentSection>

## Responsivitet

Button tilpasser seg tilgjengelig plass og innhold. På små skjermer anbefaler vi å bruke fullbredde for å sikre god trykkflate. For kode har vi egne props/attributter for dette: `fullWidth` og `fullWidthOnMobile`.

Unngå mange buttons på én rad. Da bør de stables vertikalt.

<ImageWrapper>
  <img
    src="/assets/komponenter/button/button-26.svg"
    alt="Accordion på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

## Universell utforming

Button skal fungere for alle brukere, derfor er det viktig at button

- er tilgjengelig med med tastaturnavigering og aktiveres med "Enter" eller "Space"
- viser tydelig fokusmarkering når den er aktiv

### Unngå deaktiverte buttons

Brukere forstår ofte ikke hvorfor en button er deaktivert. Derfor anbefaler vi å heller vise en feilmelding eller en hjelpetekst, enn å bruke disabled button.

Hvis du må deaktivere en button, må det være tydelig for brukeren hvorfor den er deaktivert og hva som må til for å aktivere den igjen.

Mer om universell utforming av buttons:

<div class="cards-container">
  <PktLinkCard
    title="Klart språk på knapper (KS.no)"
    skin="beige"
    href="https://www.ks.no/fagomrader/digitalisering/klart-sprak-i-digitale-selvbetjeningslosninger/"
    iconName="chevron-right"
    client:only="react"
  >
    Tips og råd for hvordan du skriver tydelige og forståelige knappetekster i
    digitale løsninger.
  </PktLinkCard>
  <PktLinkCard
    title="WCAG 2.5.8 Target Size  (wcag.com)"
    skin="beige"
    href="https://www.wcag.com/developers/2-5-8-target-size-minimum-level-aa/"
    iconName="chevron-right"
    client:only="react"
  >
    En praktisk gjennomgang av kravene til minimumsstørrelse for trykkbare
    elementer.
  </PktLinkCard>
</div>

</ContentSection>

## Anatomi

| Element              | Beskrivelse                           |
| -------------------- | ------------------------------------- |
| 1. Bakgrunn          | Bakgrunnsfarge (evt. outline)         |
| 2. Tekst (valgfritt) | Forklarer handlingen                  |
| 3. Ikon (valgfritt)  | Kan stå uten, foran eller etter tekst |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/button/button-27.svg"
    alt="Button anatomi."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="button" />

### Overstyring av sti til loading-animasjon

I likhet med <a href={getComponentHref("icon")}>Icon</a>-komponentens overstyring av sti til ikoner kan man overstyre stien til loading-animasjonen globalt ved å sette sti i `window.pktAnimationPath`.

</ContentSection>

## Props

<SpecList specName="button" />


---


### Component Specification

**Element name**: `pkt-button`

**React component**: `PktButton`

**CSS class**: `.pkt-btn`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `size` | `size` | `small`, `medium`, `large` | `medium` | Knappens størrelse |
| `fullWidth` | `full-width` | boolean | `False` | Knappen tar full bredde av containeren |
| `fullWidthOnMobile` | `full-width-on-mobile` | boolean | `False` | Knappen tar full bredde av containeren på små skjermer |
| `skin` | `skin` | `primary`, `secondary`, `tertiary` | `primary` | Er knappen primær, sekundær eller tertiær? |
| `type` | `type` | `button`, `submit`, `reset` | `button` | Hvilken type knapp er dette? |
| `color` | `color` | `blue`, `blue-outline`, `green`, `green-outline`, `green-dark`, `green-dark-outline`, `beige-light`, `beige-dark-outline`, `yellow`, `yellow-outline`, `red`, `red-outline` | `-` | Denne verdien overstyrer ‘skin’/utseende |
| `state` | `state` | `normal`, `focus`, `hover`, `active` | `-` | Her kan vi forhåndsvise knappens tilstander |
| `variant` | `variant` | `label-only`, `icon-left`, `icon-right`, `icon-only`, `icons-right-and-left` | `label-only` | Med eller uten ikon eller tekst |
| `iconName` | `iconName` | icon | `-` | Navn på ikonet som skal vises |
| `secondIconName` | `secondIconName` | icon | `-` | Navn på det andre ikonet som skal vises |
| `isLoading` | `isLoading` | boolean | `False` | Spinner for å vise at knappen er opptatt |
| `disabled` | `disabled` | boolean | `False` | Deaktiverer knappen |


#### Events

- **`onClick`**: Klikk-event for knappen



### TypeScript Interface

```typescript
export interface IPktButton {
  iconName?: PktIconName
  secondIconName?: PktIconName
  mode?: TPktButtonMode
  size?: TPktButtonSize
  fullWidth?: Booleanish
  fullWidthOnMobile?: Booleanish
  color?: TPktButtonColor
  skin?: TPktButtonSkin
  variant?: TPktButtonVariant
  state?: TPktButtonState
  type?: TPktButtonType
  isLoading?: Booleanish
  disabled?: Booleanish
  loadingAnimationPath?: string
}
```
