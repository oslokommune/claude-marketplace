# Universell utforming i Punkt

**Generated**: 2025-11-06T10:52:48.985629
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/universell-utforming/punkt-og-uu/index.mdx`

---

**Category**: universell-utforming

**Description**: Alle digitale tjenester i Oslo kommune skal være tilgjengelige for alle, uavhengig av alder, funksjonsevne og digital kompetanse.



## Vår tilnærming til universell utforming

For Punkt er målet at alle skal kunne bruke Oslo kommunes digitale tjenester på en likeverdig og inkluderende måte, uavhenging av funksjonsevne, alder eller digital kompetanse.
Universell utforming er derfor høyt prioritert hos oss og handler om langt mer enn å tilfredsstille tekniske minimumskrav.

### Slik utvikler vi tilgjengelige komponenter

Universell utforming er en integrert del av hele livssyklusen til en komponent. Ved å prioritere tilgjengelighet fra idé til lansering, blir det aldri en ettertanke. Vi dokumenterer tilgjengelighet for hver komponent i vårt [komponentbibliotek](/komponenter-og-maler/). Komponentene er i seg selv universelt utformet, men her finner du i tillegg tips til hvordan komponentene brukes på en tilgjengelig måte i en større kontekst.

### Semantisk HTML

Vi bruker semantisk riktige HTML-elementer som reflekterer innholdets betydning. Det gir en tydelig struktur og bedre støtte for hjelpemidler som skjermlesere.

### ARIA

Når semantisk HTML alene ikke gir nok informasjon, supplerer vi med relevante ARIA-roller og ARIA-attributter.

### Tastaturnavigasjon og skjermlesere

Alle interaktive elementer kan betjenes med tastatur alene og har tydelig fokusmarkering. Innholdet leses også opp på en måte som gir mening for skjermleserbrukere.

### Responsivitet

Komponentene skalerer sømløst fra mobil til store skjermer. Layouten tilpasses ulike skjermbredder, og innhold kan forstørres opptil 400 % uten tap av funksjonalitet eller lesbarhet.

### Visuell tilgjengelighet

Vi følger WCAGs kontrastkrav for tekst, bakgrunner og interaksjonselementer, i tillegg til Oslo kommunes designmanual. Punkt har også egen kontrastsjekker som hjelper deg med å bekrefte at designet oppfyller kravene.

### Kontinuerlig testing

Tilgjengelighet testes løpende gjennom:

- **Automatiserte verktøy** som axe DevTools, Silktide Inspector og Lighthouse
- **Manuelle hjelpemiddeltester** som VoiceOver
- **Tastaturnavigasjon** med systematisk manuell gjennomgang av alle interaktive elementer

<div class="cards-container">
  <PktLinkCard
    title="Testverktøy"
    skin="blue"
    href={import.meta.env.BASE_URL + "universell-utforming/testverktoy/"}
    iconName="document-text"
    client:only="react"
  >
    Oversikt over ulike testverktøy for UU og hvordan de fungerer.
  </PktLinkCard>
  <PktLinkCard
    title="Kontrastsjekker"
    skin="blue"
    href={import.meta.env.BASE_URL + "universell-utforming/testverktoy/"}
    iconName="palette"
    client:only="react"
  >
    Kontrollér at designet ditt møter kravene til kontrast.
  </PktLinkCard>
</div>

### Krav om tilgjengelighetserklæring for alle løsninger

Som en del av Oslo kommune er vi forpliktet til å følge kravene i Webdirektivet (WAD). Det innebærer at alle digitale løsninger og komponenter vi utvikler skal ha en tilgjengelighetserklæring. Dette er både et juridisk krav og et viktig virkemiddel for å dokumentere tilgjengeligheten i praksis.

I Punkt bidrar vi til at dere kan oppfylle kravet:

- Vi dokumenterer hvordan hver komponent møter kravene i WCAG 2.1.
- Vi registrerer og synliggjør eventuelle kjente avvik, og planlegger forbedringer.
- Vi sørger for at utviklingsteam som bruker Punkt-komponenter har nødvendig informasjon for å fylle ut erklæringen for sine egne løsninger.
- Vi oppdaterer informasjonen når komponenter endres.

<PktMessagebox skin="beige" client:only="react" title="">

Det enkelte team er selv ansvarlig for å fylle ut og publisere
tilgjengelighetserklæring for løsningene sine.

Ved å bruke våre komponenter får teamet et godt utgangspunkt for å sikre
tilgjengelighet, forutsatt at komponentene brukes slik de er
utviklet.

</PktMessagebox>

<div class="cards-container">
  <PktLinkCard
    title="Tilgjengelighetserklæring"
    skin="blue"
    href="https://www.uutilsynet.no/tilgjengelighetserklaering/korleis-lage-og-publisere-tilgjengelegheitserklaering/1131"
    iconName="shield-law-paragraph"
    client:only="react"
  >
    Alt om tilgjengelighetserklæringen hos uutilsynet.no
  </PktLinkCard>
  <PktLinkCard
    title="WCAG-standarden"
    skin="blue"
    href="https://www.uutilsynet.no/wcag-standarden/wcag-standarden/86"
    iconName="face-happy"
    client:only="react"
  >
    Alle WCAG-kravene som inngår i regelverket hos uutilsynet.no
  </PktLinkCard>
</div>

### Vi forplikter oss til kontinuerlig forbedring

Universell utforming er ikke en aktivitet vi gjør én gang, men er en pågående prosess.

Vi i Punkt forplikter oss til å

- brukerteste og innhente innsikt for å forstå faktiske behov
- samle inn tilbakemeldinger fra innbyggere, utviklere og designere i Oslo kommune
- iterere og forbedre komponenter basert på reelle utfordringer og brukeropplevelser
- holde oss oppdatert på endringer i WCAG og andre regelverk som påvirker oss

Vi ønsker alltid å lære mer og bli bedre over tid. Vi inviterer til en åpen dialog for å forbedre løsningene våre og du kan når som helst høre fra deg på #punkt på Slack.

<div class="cards-container">
  <PktLinkCard
    title="Bidra"
    skin="blue"
    href={import.meta.env.BASE_URL + "grunnleggende/bidra/"}
    iconName="heart"
    client:only="react"
  >
    Hvordan bidra til designsystemet
  </PktLinkCard>
</div>