# Icon

**Generated**: 2025-11-06T10:52:48.950180
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/icon/index.mdx`
- `component-specs/icon.json`
- `packages/elements/src/components/icon/index.ts`
- `packages/elements/src/components/icon/icon.ts`

---

## Documentation



# Icon

<Lead releaseDate="25.10.2024" lastUpdated="–">
 Du bruker icon for å vise visuelle symboler (ikoner). Ikonene er SVG-baserte og kan brukes i alle applikasjoner for å støtte tekst eller tydeliggjøre handlinger. For å se alle ikoner som kan brukes i Punkt, se [oversikten over ikoner](/ikoner/).

Det er også mulig å bruke egne ikoner ved å inkludere en `path`-attributt som peker til lokasjonen til en egen SVG-fil. Du kan da legge inn stien i `path` og navnet på filen (uten filendelsen .svg) i `name`.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ icon: iconSpec }}
  previewJson={iconPreview}
/>

<div class="cards-container">
  <PktLinkCard
    title="Button"
    skin="blue"
    href={getComponentHref("button")}
    iconName="chevron-right"
    client:only="react"
  >
   Ikoner brukes ofte i knapper for å understøtte handlinger.
  </PktLinkCard>

<PktLinkCard
  title="Logged-in menu"
  skin="blue"
  href={getComponentHref("headermeny")}
  iconName="chevron-right"
  client:only="react"
>
  Ikoner kan benyttes for å understreke menyelementer.
</PktLinkCard>

  <PktLinkCard
    title="Alert"
    skin="blue"
    href={getComponentHref("alert")}
    iconName="chevron-right"
    client:only="react"
  >
    Ikoner hjelper brukeren å raskt tolke budskapet visuelt.
  </PktLinkCard>
</div>

## Varianter

### Størrelser

Du kan velge mellom tre størrelser når du bruker icon:

| Variant | Beskrivelse                                          |
| ------- | ---------------------------------------------------- |
| Small   | Når det er lite plass tilgjengelig                   |
| Medium  | Passer godt i knapper og andre interaktive elementer |
| Large   | Bruk når ikonet skal få mer oppmerksomhet            |

<ImageWrapper>
  <img
    src="/assets/komponenter/icon/icon-1.svg"
    alt="Eksempler på small varianten av icon"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/icon/icon-2.svg"
    alt="Eksempler på medium varianten av icon"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/icon/icon-3.svg"
    alt="Eksempler på large varianten av icon"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk icon når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "du vil støtte tekstlig informasjon med et visuelt symbol",
    "du vil tydeliggjøre handlinger eller navigasjon",
    `du ønsker å gi ekstra kontekst til <a href="${getComponentHref("button")}">button</a> eller <a href="${getComponentHref("link")}">link</a>`,
  ]}
/>

### Unngå icon når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "ikonet alene skal bære all informasjon",
    `symbolet er uklart eller kan misforstås uten tekst`,
    "du vurderer å bruke ikonet kun for dekorasjon",
  ]}
/>

### Ikoner skal ikke erstatte tekst

Ikoner skal alltid brukes for å støtte tekst, ikke erstatte den. Hvis ikonet ikke er åpenbart for alle brukere, må du kombinere det med en tilhørende tekst som forklarer hva ikonet representerer. Bruk ikoner som er tydelige og gjenkjennelige for målgruppen.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/icon/icon-4.svg",
    imgAlt: "Eksempel på ikon kombinert med tekst",
    caption: "Dersom ikonet er uklart burde du kombinere det med en beskrivende tekst",
  }}
  badExample={{
    image: "/assets/komponenter/icon/icon-5.svg",
    imgAlt: "Eksempel ikkon uten teks.",
    caption: "Unngå ikoner uten kontekst som kan være forvirrende for brukeren",
  }}
/>
</ContentSection>

## Universell utforming

Alle ikoner må ha tilgjengelig navn eller tekst, enten via `aria-label`, `aria-hidden` eller ved at de kombineres med tekst i brukergrensesnittet.

Hvis ikonet kun er dekorativt, bruk `aria-hidden="true"` for å skjule det for skjermlesere.

Ikonene skal ha en tydelig kontrast mot bakgrunnen for å være godt synlige.

For bruk i lenker eller knapper skal ikonet ha en tydelig sammenheng med handlingen som utføres og teksten som hører med.

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="icon" />

### Stilsetting og farger

For ferdige klasser for størrelse på ikonene, kan man legge til klassene `pkt-icon--small`, `pkt-icon--medium` og `pkt-icon--large` på `pkt-icon`-elementet.

<CodeExample>
  <PktIcon
    name="user"
    client:only="react"
    className="pkt-icon--small"
  ></PktIcon>
  <PktIcon
    name="user"
    client:only="react"
    className="pkt-icon--medium"
  ></PktIcon>
  <PktIcon
    name="user"
    client:only="react"
    className="pkt-icon--large"
  ></PktIcon>
</CodeExample>

Det er også mulig å sette sine egne farger på ikonene ved å overstyre CSS-variabel `--fg-color` på SVGen i `pkt-icon`-elementet.

```html
<style>
  .green-layout pkt-icon {
    --fg-color: var(--pkt-color-brand-green-1000);
  }
</style>
<div class="green-layout">
  <pkt-icon name="user"></pkt-icon>
</div>
```

<CodeExample>
  <PktIcon
    name="user"
    client:only="react"
    className="pkt-icon--large"
    style={{ "--fg-color": "var(--pkt-color-brand-green-1000)" }}
  ></PktIcon>
</CodeExample>

### Avansert bruk

Som nevnt over kan man overstyre `path`-attributtet for å bruke egne ikoner.

{/* prettier-ignore */}
```html
<pkt-icon
  name="bees"
  path="/assets/"
></pkt-icon>
```

<CodeExample>
  <PktIcon
    name="bees"
    path="../../assets/frontpage/"
    client:only="react"
    className="pkt-icon--large"
  ></PktIcon>
</CodeExample>

Dersom man har behov for å overstyre absolutt alle `path`-attributter kan man sette dette globalt ved å overstyre `window.pktIconPath`.

{/* prettier-ignore */}
```html
<script>
  window.pktIconPath = "/assets/egne-ikoner/"
</script>
<pkt-icon
  name="eget-ikon"
></pkt-icon>
```

Dersom man har _enda_ mer avanserte behov, eller trenger å overstyre `fetch`-funksjonen i enhetstester eller liknende, kan man også overstyre med `window.pktFetch`. Her er det viktig at man følger JavaScripts `fetch` sitt API, og returnerer en `Promise`.

{/* prettier-ignore */}
```js
window.pktFetch = () =>  
  Promise.resolve({  
    ok: true,  
    text: () => Promise.resolve('<div>FakeIcon</div>'),  
  });
```

</ContentSection>

## Props

<SpecList specName="icon" />


---


### Component Specification

**Element name**: `pkt-icon`

**React component**: `PktIcon`

**CSS class**: `.pkt-icon`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `name` | `name` | icon | `-` | Ikonet som skal vises |
| `path` | `path` | string | `https://punkt-cdn.oslo.kommune.no/latest/icons/` | Overstyr stien til ikonet som skal vises |
| `className` | `className` | `pkt-icon--small`, `pkt-icon--medium`, `pkt-icon--large` | `-` | (className for React, class for elementer) |


