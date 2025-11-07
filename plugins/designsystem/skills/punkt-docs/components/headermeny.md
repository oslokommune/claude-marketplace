# Logged-in menu

**Generated**: 2025-11-06T10:52:48.949253
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/headermeny/index.mdx`

---

## Documentation


# Logged-in menu

<Lead
  releaseDate="25.08.2023"
  lastUpdated="-"
>
 Logged-in menu gir brukeren tilgang til navigasjon i løsningen. Den brukes som regel sammen med header, men kan også brukes andre steder ved behov.

Logged-in menu er del av <a href={getComponentHref("header")}>header-komponenten</a> og følger automatisk med ved bruk av Punkt sin header. Se header for demo og kode.

</Lead>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Header"
    skin="blue"
    href={getComponentHref("header")}
    iconName="chevron-right"
    client:only="react"
  >
    Overliggende navigasjon
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
  <PktLinkCard
    title="Footer"
    skin="blue"
    href={getComponentHref("footer")}
    iconName="chevron-right"
    client:only="react"
  >
    Innhold nederst på siden eller løsningen din.
  </PktLinkCard>
</div>

## Varianter

Logged-in menu har én variant, men du kan tilpasse innhold og struktur etter behov. Det er støtte for flere seksjoner og valgfritt antall lenker.

<ImageWrapper>
  <img
    src="/assets/komponenter/header/loggedinmenu-1.svg"
    alt="Logged-in menu med ulike type innhold"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk logged-in menu når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "løsningen har behov for navigasjon til flere områder eller seksjoner",
    "du vil gi brukeren en tydelig og samlet meny i headeren",
  ]}
/>

### Unngå logged-in menu når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "løsningen har få, faste lenker, da er det ofte bedre å bruke vanlige lenker direkte i headeren",
  ]}
/>

### Logged-in menu skal være enkel å bruke

Hold menyen ryddig og oversiktlig. Bruk korte og tydelige lenketekster. Unngå for mange valg, vi anbefaler maks to nivåer (hovedlenke + eventuelle underlenker).

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/header/loggedinmenu-2.svg",
    imgAlt: "Eksempel på god bruk av logged-in menu",
    caption: "Bruk korte lenker og organiser innholdet i logiske seksjoner",
  }}
  badExample={{
    image: "/assets/komponenter/header/loggedinmenu-3.svg",
    imgAlt:
      "Eksempel på bruk av lange eller utydelige lenketekster i loggen-in menu",
    caption: "Unngå lange eller utydelige lenketekster",
  }}
/>

### Tenk igjennom innhold og navigasjon

Før du tar i bruk logged-in menu, bør du vurdere:

- Hva brukeren trenger tilgang til under innlogging
- Om noen lenker heller bør plasseres i hovedmeny, footer eller på selve siden

Du kan tilpasse menyen med egne lenker, ikoner og seksjoner. Se også <a href={getComponentHref("link")}>retningslinjer for lenketekster</a>.

### Oppbygning

Logged-in menu kan bestå av inntil fem seksjoner:

**1. Pålogget bruker:** Viser brukerens fulle navn. På mobil kan du velge mellom å vise et ikon eller initialer. Du kan også legge til tilleggsinformasjon, for eksempel sist innlogget eller rolle.

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/header/loggedinmenu-4.svg"
    alt="Eksempel på  Pålogget bruker"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/header/loggedinmenu-5.svg"
    alt="Eksempel på  Pålogget bruker"
    aria-hidden="true"
  />
</ImageWrapper>

**2. Brukermeny:** Inneholder lenker til relevante sider i tjenesten. Vi anbefaler maks fire lenker, men antallet kan justeres etter behov. Velg ikoner og lenketekster som er logiske for brukeren.

<ImageWrapper>
  <img
    src="/assets/komponenter/header/loggedinmenu-6.svg"
    alt="Eksempel på ulike lenker"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/header/loggedinmenu-7.svg"
    alt="Eksempel på ulike lenker"
    aria-hidden="true"
  />
</ImageWrapper>

**3. Representert organisasjon:** Viser hvilken organisasjon brukeren representerer. Brukeren skal kunne klikke på «Endre organisasjon» for å velge en annen.

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/header/loggedinmenu-8.svg"
    alt="Eksempel på representert organisasjon"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/header/loggedinmenu-9.svg"
    alt="Eksempel på representert organisasjon"
    aria-hidden="true"
  />
</ImageWrapper>

**4. Brukervalg:** Omfatter logg ut-knappen, som skal føre til en side som bekrefter at brukeren er logget ut. Du kan også inkludere andre valg, som en lenke til innstillinger.

<ImageWrapper>
  <img
    src="/assets/komponenter/header/loggedinmenu-10.svg"
    alt="Eksempel på ulike brukervalg"
    aria-hidden="true"
  />
</ImageWrapper>

**5. Horisontal lenkeliste:** Brukes til lenker som personvern og kontakt. Denne seksjonen anbefales kun hvis løsningen ikke har en footer med denne typen informasjon.

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/header/loggedinmenu-11.svg"
    alt="Eksempel på horisontal lenkeliste"
    aria-hidden="true"
  />

</ImageWrapper>
</ContentSection>

## Responsivitet

Logged-in menu tilpasser seg automatisk skjermstørrelsen og fyller bredden av skjermen. På mobil vises menyen som en hamburgermeny.

Test menyen på mobil, nettbrett og desktop for å sikre at alt fungerer som forventet.

<ImageWrapper >
  <img
    src="/assets/komponenter/header/loggedinmenu-12.svg"
    alt="Header med logged-in menu på mobil"
    aria-hidden="true"
  />
</ImageWrapper>
<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

Logged-in menu skal være tilgjengelig for alle brukere:

- Alle lenker og menyer skal fungere med tastatur og skjermleser
- Sørg for tydelige fokusmarkeringer
- Bruk riktige ARIA-roller og attributter (f.eks. `aria-expanded`, `aria-controls`)
- Kontrastkrav er ivaretatt av Punkt-fargene

<PktMessagebox skin="blue" client:only="react" title="">
  <ul>
    <li>Hvis du bruker React eller Elements: Alt av ARIA-støtte er innebygd</li>
    <li>
      Hvis du kun bruker CSS: Du må selv legge til tastaturnavigasjon og ARIA
      manuelt
    </li>
  </ul>
</PktMessagebox>

</ContentSection>

## Anatomi

| Element                      | Beskrivelse                                        |
| ---------------------------- | -------------------------------------------------- |
| 1. Bakgrunn                  | Bakgrunnsfarge                                     |
| 2. Pålogget bruker           | Viser brukerens navn, evt. rolle og sist innlogget |
| 2.1 Ledetekst                | Teksten “Pålogget som”                             |
| 2.2 Navn                     | Fullt navn eller brukernavn på innlogget bruker    |
| 2.3 Sist innlogget           | Tidspunkt for siste innlogging (valgfritt)         |
| 3. Brukermeny                | Lenker til relevante sider i løsningen             |
| 3.1-3.4 Lenker               | Tilpassede lenker som kan inneholde ikon og tekst  |
| 4. Representert organisasjon | Tilpassede lenker som kan inneholde ikon og tekst  |
| 4.1 Ledetekst                | Teksten “Representerer”                            |
| 4.2 Organisasjonsnavn        | Navn på organisasjonen                             |
| 4.3 Organisasjonsnummer      | Org.nr. tilknyttet organisasjonen                  |
| 4.4 Endre organisasjon       | Lenke for å bytte organisasjon                     |
| 5. Brukervalg                | Handlinger knyttet til brukerens sesjon            |
| 5.1 Innstillinger            | Lenke til innstillinger                            |
| 5.2 Logg ut                  | Lenke for å logge ut av løsningen                  |
| 6. Horisontal lenkeliste     | Eventuelle tillegg som kontakt og personvern       |
| 6.1. Kontakt                 | Lenke til kontaktinformasjon                       |
| 6.2 Personvern               | Lenke til kontaktinformasjon                       |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/header/loggedinmenu-13.svg"
    alt="logged-in menu anatomi"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

Se <a href={getComponentHref("header")}>dokumentasjonen for header</a>. Logged-in menu er en integrert del av header-komponenten.

</ContentSection>

## Props

For props se <a href={getComponentHref("header")}>dokumentasjonen for header</a>. Logged-in menu er en integrert del av header-komponenten.


---

