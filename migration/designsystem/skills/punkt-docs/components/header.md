# Header

**Generated**: 2025-11-06T10:52:48.948143
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/header/index.mdx`
- `component-specs/header.json`

---

## Documentation



# Header

<Lead
  releaseDate="25.08.2023"
  lastUpdated="-"
  contributeBox={false}
>
  Headeren er den globale navigasjonen for tjenester og nettsider i Oslo kommune. Den gir tydelig avsender og gjenkjennelighet på tvers av løsninger, og skal være lik på alle sider i en applikasjon.

I headeren kan brukeren få tilgang til meny, <a href={getComponentHref("headermeny")}>innlogget meny</a> og logg ut-funksjon. Ved å klikke på brukernavnet åpnes en ekspandert meny.

</Lead>

<PktAlert
  title=""
  skin="warning"
  date="18.07.2025"
  client:only="react"
  class="mb-size-32"
>
  <span>
    Denne komponenten er under forbedring. Har du innspill, forslag eller
    tilbakemeldinger? Ta kontakt på{" "}
    <a href="https://oslokommune.slack.com/archives/C01EWV9U07R">#punkt</a> på
    Slack eller send en e-post til punkt@origo.oslo.kommune.no.
  </span>
</PktAlert>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ header: headerSpec }}
  previewJson={headerPreviewJson}
  fullWidth
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Footer"
    skin="blue"
    href={getComponentHref("footer")}
    iconName="chevron-right"
    client:only="react"
  >
    Innhold nederst på siden eller løsningen din.
  </PktLinkCard>
  <PktLinkCard
    title="Logged-in menu"
    skin="blue"
    href={getComponentHref("headermeny")}
    iconName="chevron-right"
    client:only="react"
  >
    Samler navigasjonslenker i en meny i toppen
  </PktLinkCard>
  <PktLinkCard
    title="Breadcrumbs"
    skin="blue"
    href={getComponentHref("breadcrumbs")}
    iconName="chevron-right"
    client:only="react"
  >
    Viser hvor brukeren befinner seg i sidens struktur
  </PktLinkCard>
</div>

## Varianter

| Type             | Bruk                                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------------------------- |
| Innlogget header | Brukes i de fleste innloggede løsninger, viser logo, tjenestenavn, innlogget meny og/eller logg ut-knapp |
| Utlogget header  | Brukes på åpne sider som oslo.kommune.no, viser logo, søkefelt, megameny og kontaktlenker                |

**Merk:** Denne dokumentasjonen beskriver kun innlogget header. Utlogget header utvikles som del av oslo.kommune.no og webforvaltningen og kommer snart i Punkt.

<ImageWrapper caption="Innlogget header">
  <img
    src="/assets/komponenter/header/header-1.svg"
    alt="Innloget header"
    aria-hidden="true"
  />
</ImageWrapper>
<ImageWrapper caption="Utlogget header">
  <img
    src="/assets/komponenter/header/header-2.svg"
    alt="Utlogget header"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk header når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "løsningen har Oslo kommune som avsender",
    "du vil gi brukeren tilgang til navigasjon eller innlogget funksjonalitet",
    "du vil tydeliggjøre at løsningen tilhører Oslo kommune",
  ]}
/>

Dersom løsningen er et internt verktøy eller en side uten offentlig tilgang, kan en egen header være mer hensiktsmessig. Dette må vurderes grundig og som hovedregel bør du _alltid_ bruke header-komponenten.

### Headeren skal være enkel å bruke

Oslo-logoen skal alltid vises til venstre, i sin helhet. Tjenestenavn er valgfritt, men anbefales for tydelighet. Bruk kun nødvendige navigasjonselementer, og sørg for at strukturen er lik på alle sider i tjenesten.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/header/header-3.svg",
    imgAlt: "Eksempel på anbefalt bruk av header",
    caption: "Bruk tydelig Oslo-logo og eventuelt tjenestenavn til venstre",
  }}
  badExample={{
    image: "/assets/komponenter/header/header-4.svg",
    imgAlt: "Eksempel på ikke anbefalt bruk av header",
    caption: "Unngå å ende plassering eller størrelse på logo eller meny",
  }}
  direction="column"
/>

### Innhold i header

Logo og avsender skal alltid stå til venstre. Navigasjonselementer som meny, innlogget meny og logg ut-knapp plasseres til høyre. Ikke bruk alle elementer samtidig, velg det som passer brukerens behov.

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/header/header-5.svg"
    alt="Forklaring av posisjoner og dimensjoner tilgjengelig til hver element i headeren"
    aria-hidden="true"
  />
</ImageWrapper>

### Behold struktur og utseende

Du kan tilpasse bakgrunnsfargen i headeren, men må sørge for god kontrast og at det fortsatt matcher Oslo kommunes visuelle profil.

Oslo-logoen skal ikke kombineres med andre logoer og må alltid vises i sin helhet. [Les mer om riktig bruk av Oslo-logoen](https://designmanual.oslo.kommune.no/oslologo)

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/header/header-6.svg",
    imgAlt: "Eksempel på anbefalt bruk av Oslo kommunes visuelle profil",
    caption:
      "Forhold deg til Oslo kommunes visuelle profil og prioriter standard og gjenkjennelig headerstyling slik at brukeren lett kan navigere mellom åpne og innloggede sider",
  }}
  badExample={{
    image: "/assets/komponenter/header/header-7.svg",
    imgAlt:
      "Eksempel på ikke anbfelat bruk av Oslo kommunes visuelle identitet ",
    caption:
      "Unngå å bryte Oslo kommunes visuelle identitet og overlesse headeren med mange elementer",
  }}
/>

### Søk i header

Søkefelt er ikke inkludert i innlogget header for å unngå forvirring med søket på oslo.kommune.no, som er globalt. Hvis du trenger søk i en innlogget løsning, bør det plasseres som en egen komponent, for eksempel rett under header eller i hovedinnholdet.

</ContentSection>

## Responsivitet

Headeren tilpasser seg automatisk til skjermstørrelsen. På mobil samles navigasjonen i menyen. Du kan velge om brukeren skal vises med initialer eller ikon.

Test alltid headeren på mobil, nettbrett og desktop.

<ImageWrapper>
  <img
    src="/assets/komponenter/header/header-8.svg"
    alt="Header på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

Headeren skal være tilgjengelig for alle – uansett hvilke hjelpemidler eller navigasjonsmetoder brukeren benytter. Det betyr at den må fungere med både tastatur, skjermleser og andre assistive teknologier.

### Gjør headeren forståelig og navigerbar

- Alle interaktive elementer skal kunne brukes med tastatur alene (for eksempel med “Tab”, “Enter” og “Esc”).
- Bruk beskrivende og tydelige tekster på knapper og lenker, unngå generiske lenketekster som “Klikk her”.
- Sørg for tilstrekkelig kontrast mellom tekst og bakgrunn.

Bruk landemerker og ARIA-roller riktig:

- `<header>` eller `role="banner"` for header
- `role="navigation"` og `aria-label` på meny hvis det finnes flere navigasjoner på siden
- `aria-expanded` og `aria-controls` for å indikere tilstand på nedtrekksmenyer

### Tilpasset ulike brukere og kontekster

[Forskning fra GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/#research-on-this-pattern) viser at brukere forventer:

- Konsistent plassering av navigasjon på tvers av sider
- Enkle og intuitive etiketter på menyvalg
- At det er lett å skille mellom innhold og navigasjon
- Mulighet for å forstå hvor man er i løsningen (for eksempel via aktiv tilstand eller <a href={getComponentHref("breadcrumbs")}>breadcrumbs</a>)

### Viktig om implementasjon

Hvis du bruker React- eller Elements-versjonen av header, er riktig ARIA-støtte innebygd. Bruker du bare CSS, må du selv sørge for:

- ARIA-attributter for meny og nedtrekk
- Fokus-støtte og tastaturnavigasjon
- At `aria-expanded` oppdateres riktig når menyen åpnes og lukkes

<div class="cards-container">
  <PktLinkCard
    title="Navigate a service (GOV.UK)"
    skin="beige"
    href="https://design-system.service.gov.uk/patterns/navigate-a-service/"
    iconName="chevron-right"
    client:only="react"
  >
   Forskning og anbefalinger for hvordan brukere forstår og beveger seg i digitale tjenester
  </PktLinkCard>
  <PktLinkCard
    title="Navigasjonsmetoder (UUtilsynet)"
    skin="beige"
    href="https://www.uutilsynet.no/veiledning/navigasjonsmetoder/217"
    iconName="chevron-right"
    client:only="react"
  >
   Hvordan navigasjon og meny skal fungere med tastatur og skjermleser
  </PktLinkCard>
</div>
</ContentSection>

## Anatomi

| Element                       | Beskrivelse                               |
| ----------------------------- | ----------------------------------------- |
| 1. Bakgrunn                   | Hvit bakgrunn i hele headeren             |
| 2. Oslo-logo                  | Plassert til venstre, lenker til forsiden |
| 3. Tjenestenavn (valgfritt)   | Navn på tjeneste ved siden av logoen      |
| 4. Meny (valgfritt)           | Meny for navigasjon                       |
| 5. Innlogget meny (valgfritt) | Meny for innloggede brukere               |
| 6. Logg ut-knapp (valgfritt)  | Knapp for utlogging                       |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/header/header-9.svg"
    alt="Header anatomi."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="header" />

</ContentSection>
## Props

<SpecList specName="header" />


---


### Component Specification

**Element name**: `pkt-header`

**React component**: `PktHeader`

**CSS class**: `.pkt-header`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `logoLink` | `logoLink` | string | `https://www.oslo.kommune.no/` | Hva skjer når brukeren klikker på logoen? |
| `serviceName` | `serviceName` | string | `-` | Navnet på tjenesten som vises i headeren |
| `fixed` | `fixed` | boolean | `True` | Skal headeren være fast i toppen av siden? |
| `scrollToHide` | `scrollToHide` | boolean | `True` | Skal headeren skjules når brukeren skroller ned? |
| `user` | `user` | object | `-` | Brukerobjektet som inneholder informasjon om den innloggede brukeren |
| `userMenu` | `userMenu` | array | `-` | Menyen som vises når brukeren klikker på brukerknapp |
| `userMenuFooter` | `userMenuFooter` | array | `-` | Innholdet som vises i bunnen av brukermenyen |
| `userOptions` | `userOptions` | array | `-` | Alternativer for brukeren som kan endres |
| `representing` | `representing` | object | `-` | Objekt som inneholder informasjon om representasjon, hvis aktuelt |
| `canChangeRepresentation` | `canChangeRepresentation` | boolean | `False` | Skal brukeren kunne endre representasjon? |
| `showLogOutButton` | `showLogOutButton` | boolean | `True` | Skal logg ut-knappen vises i headeren? |
| `showMenuButton` | `showMenuButton` | boolean | `False` | Skal menyknappen vises i headeren? |


#### Events

- **`changeRepresentation`**: Bruker endrer representasjon
- **`logIn`**: Bruker klikker på logg inn-knappen
- **`logOut`**: Bruker klikker på logg ut-knappen


