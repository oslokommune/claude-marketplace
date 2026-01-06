# Footer

**Generated**: 2025-11-06T10:52:48.946942
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/footer/index.mdx`
- `component-specs/footer.json`
- `component-specs/footer-simple.json`

---

## Documentation



# Footer

<Lead releaseDate="08.05.2023" lastUpdated="05.05.2025">
  Footer er en del av standardsidemalen og plasseres nederst på siden. Den gir
  brukeren tilgang til viktige lenker som kontaktinformasjon, personvern og
  tilgjengelighet. Footeren (sammen med header) bidrar til å synliggjøre Oslo
  kommune som avsender.
</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ footer: footerSpec }}
  previewJson={footerPreviewJson}
/>

## Kodebygger Footer Simple

<PktPreviewWithJson
  client:only="react"
  specs={{ "footer-simple": footerSimpleSpec }}
  previewJson={footerSimplePreview}
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Header"
    skin="blue"
    href={getComponentHref("header")}
    iconName="chevron-right"
    client:only="react"
  >
    Gir tilgang til hovednavigasjon øverst på siden
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

| Variant        | Bruk                                                                                                                                |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Normal         | Standard footer med tre kolonner, passer for alle løsninger som er tett koblet til oslo.kommune.no eller har behov for flere lenker |
| Simple (enkel) | Enkel footer med færre lenker, passer til mindre, selvstendige løsninger med begrenset behov for navigasjon                         |

<ImageWrapper>
  <img
    src="/assets/komponenter/footer/footer-1.svg"
    alt="Eksampel på normal footer."
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/footer/footer-2.svg"
    alt="Eksampel på simple bufooter."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk footer når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "du lager løsninger der Oslo kommune er avsender (i praksis skal footer alltid brukes i løsninger der Oslo kommune er avsender)",
    "du trenger et fast område for lenker til personvern, tilgjengelighet og kontaktinformasjon",
    "du vil gjøre det tydelig at løsningen tilhører Oslo kommune",
  ]}
/>
I noen få tilfeller, som interne verktøy uten publikum, kan det være mindre
behov for footer. Husk likevel at krav til tilgjengelighet gjelder flere
løsninger, og det kan derfor være lurt å ha footer uansett.

### Plassering av footer

Bruk et ikon som matcher alvorlighetsgraden og budskapetFooteren skal alltid plasseres nederst på siden. Den brukes i alle tjenester der Oslo kommune er avsender.

### Innhold i footer

Footeren bygger på oslo.kommune.no sin standard, men du kan tilpasse tekst og lenker etter behov.

Husk:

- Footeren må alltid inneholde lenker til personvern og tilgjengelighet.
- Andre lenker i footeren skal også være tilgjengelige andre steder på nettstedet.
- Unngå å bruke bilder eller ikoner i footeren.
- Ikke fyll footeren med for mange lenker.
- Fjern språklenker hvis det kun finnes én språkversjon.
- Lenker til sosiale medier bør kun brukes hvis de er relevante for løsningen.

### Når skal du bruke den vanlige footeren og når skal man bruke den enkle varianten?

Du bør bruke den standard varianten (normal) hvis løsningen din er en del av oslo.kommune.no, eller hvis du har behov for å vise flere lenker. Den enkle varianten (simple) passer kun for løsninger som er mer selvstendige, og som ikke trenger like mye navigasjon.

</ContentSection>
## Responsivitet

Footeren tilpasser seg automatisk skjermstørrelsen og bygger i høyden på mindre skjermer. På mobil og nettbrett vises innholdet i én kolonne for å sikre god lesbarhet.

Test alltid footeren i løsningen din på ulike skjermstørrelser. Sjekk at alle lenker har god nok plass, og at tekst og navigasjon fortsatt fungerer godt, både i stående og liggende visning.

Hvis du bruker normal footer med mange lenker, bør du vurdere rekkefølgen på lenkene, slik at de viktigste vises først.

<ImageWrapper>
  <img
    src="/assets/komponenter/footer/footer-3.svg"
    alt="Footer på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

## Universell utforming

Footeren må fungere for alle brukere, uansett hvordan de navigerer. Sørg for at alle lenker i footeren kan nås med tastatur og skjermleser.

Lenketekstene skal være tydelige og beskrive hva brukeren kan forvente når de klikker. Bruk eksternlenke-styling på lenker som tar brukeren ut av løsningen, slik at det er tydelig at de åpner en ny side.

Husk at footeren alltid inneholder viktige lenker, som personvern og tilgjengelighet. Disse må være lette å finne og bruke for alle.

Sjekk spesielt:

- At alle lenker kan fokuseres med tastatur.
- At lenketekstene gir mening også uten kontekst.
- At det er tilstrekkelig kontrast mellom tekst og bakgrunn (dette er ivaretatt av fargene i Punkt).

Les mer om universell utforming av lenker (i footer i dette tilfellet):

<div class="cards-container">
  <PktLinkCard
    title="Universell utforming av lenker (UU-tilsynet)"
    skin="beige"
    href="https://www.uutilsynet.no/veiledning/lenker/214"
    iconName="chevron-right"
    client:only="react"
  >
    Semantikk, lesbarhet og teknisk tilrettelegging i lenker og knapper.
  </PktLinkCard>
</div>

</ContentSection>

## Anatomi

### Normal versjon (standard footer med tre kolonner)

| Element                   | Beskrivelse                                                |
| ------------------------- | ---------------------------------------------------------- |
| 1. Bakgrunn               | Hovedområde med $brand-blue bakgrunn og hvit tekst         |
| 2. Kolonnetittel 1        | Tittel for første kolonne (valgfritt)                      |
| 3. Tekst (valgfritt)      | Beskrivende tekst eller forklaring i kolonnen (valgfritt)  |
| 4. Lenker, kolonne 1      | Klikkbare lenker i første kolonne                          |
| 5. Kolonnetittel 2        | Tittel for andre kolonne (valgfritt)                       |
| 6. Lenker, kolonne 2      | Klikkbare lenker i andre kolonne                           |
| 7. Kolonnetittel 3        | Tittel for tredje kolonne (valgfritt, men anbefalt)        |
| 8. Lenker, kolonne 3      | Klikkbare lenker i tredje kolonne                          |
| 9. Språklenke             | Lenke til annen språklig versjon av nettstedet (valgfritt) |
| 10. Sosiale medier-lenker | Lenker til Oslo kommunes kontoer (valgfritt)               |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/footer/footer-4.svg"
    alt="Anatomi av normal footer"
    aria-hidden="true"
  />
</ImageWrapper>

### Simple versjon (enkel footer)

| Element     | Beskrivelse                                        |
| ----------- | -------------------------------------------------- |
| 1. Bakgrunn | Hovedområde med $brand-blue bakgrunn og hvit tekst |
| 2. Lenker   | Inntil fem lenker til relevante sider              |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/footer/footer-5.svg"
    alt="Anatomi av normal footer"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="footer" />
<TechDetails specName="footer-simple" />

### Innstillinger for informasjonskapsler / Consent

Footer kan brukes til å legge inn Consent-komponenten i bunnen av siden. Dette kan gjøres ved å sende inn `includeConsent`-prop'en til PktFooter og PktFooterSimple. Da vil det bli lagt til en lenke i footer som åpner innstillingene for informasjonskapsler.

Se <a href={getComponentHref("consent")}>Consent</a> for mer informasjon om hvordan du bruker denne komponenten.

Footer og FooterSimple støtter alle Content-komponentens attributter.

</ContentSection>

## Props

### Footer

<SpecList specName="footer" />

### Footer Simple

<SpecList specName="footer-simple" />


---


### Component Specification

**Element name**: `pkt-footer`

**React component**: `PktFooter`

**CSS class**: `.pkt-footer`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `personvernOgInfoLink` | `personvernOgInfoLink` | string | `-` | Link to personvern og info page |
| `tilgjengelighetLink` | `tilgjengelighetLink` | string | `-` | Link to tilgjengelighet page |
| `openLinksInNewTab` | `openLinksInNewTab` | boolean | `-` | Whether to open links in new tab |
| `includeConsent` | `includeConsent` | boolean | `-` | Whether to include Consent component in the footer |
| `googleAnalyticsId` | `googleAnalyticsId` | string | `-` | Google Analytics ID for tracking when using Consent component |
| `hotjarId` | `hotjarId` | string | `-` | Hotjar ID for tracking when using Consent component |
| `columnOne` | `columnOne` | object | `-` | Content for the first column of the footer |
| `columnTwo` | `columnTwo` | object | `-` | Content for the second column of the footer |
| `socialLinks` | `socialLinks` | array | `-` | Array of social links for the footer |



### Component Specification

**Element name**: `pkt-footer-simple`

**React component**: `PktFooterSimple`

**CSS class**: `.pkt-footer-simple`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `personvernOgInfoLink` | `personvernOgInfoLink` | string | `-` | Link to personvern og info page |
| `tilgjengelighetLink` | `tilgjengelighetLink` | string | `-` | Link to tilgjengelighet page |
| `includeConsent` | `includeConsent` | boolean | `-` | Whether to include Consent component in the footer |
| `googleAnalyticsId` | `googleAnalyticsId` | string | `-` | Google Analytics ID for tracking when using Consent component |
| `hotjarId` | `hotjarId` | string | `-` | Hotjar ID for tracking when using Consent component |
| `links` | `links` | array | `-` | Array of links for the footer |


