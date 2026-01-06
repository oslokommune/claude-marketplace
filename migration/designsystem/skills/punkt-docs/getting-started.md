# Getting Started with Punkt

**Generated**: 2025-11-06T10:52:48.922985
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/grunnleggende/ta-i-bruk-punkt.mdx`
- `apps/docs-astro/src/pages/grunnleggende/for-utviklere/kom-i-gang.mdx`

---

## Grunnleggende

*Alt du trenger å vite for å ta i bruk Punkt i kode og design.*


## Hvorfor ta i bruk Punkt?

Oslo kommune tilbyr over 500 digitale tjenester. Disse har tidligere vært utviklet og designet separat, noe som har ført til store forskjeller i brukeropplevelse og uttrykk.

Punkt skal gjøre det enklere å

- bygge gjenkjennelige og tilgjengelige løsninger for innbyggere, ansatte og næringsliv
- skape mer bærekraftige tjenester gjennom gjenbruk og standardisering
- jobbe sammen i tverrfaglige team

### Samarbeid på tvers

Vi mener at utviklere og designere jobber best når de samarbeider tett. Punkt legger til rette for dette – både i verktøy og prosess. Punkt har både et kodebibliotek og designbibliotek. TIl sammen gir det deg alt du trenger for å jobbe effektivt og helhetlig med digitale løsninger.

<div class="cards-container">
  <PktLinkCard
    title="Kom i gang som designer"
    skin="beige"
    href={import.meta.env.BASE_URL + "grunnleggende/for-designere/kom-i-gang/"}
    iconName="palette"
    client:only="react"
  >
    Hvordan ta i bruk designsystemet i Figma
  </PktLinkCard>
  <PktLinkCard
    title="Kom i gang som utvikler"
    skin="beige"
    href={import.meta.env.BASE_URL + "grunnleggende/for-utviklere/kom-i-gang/"}
    iconName="document-code"
    client:only="react"
  >
    Pakker, Github og samarbeid med designere
  </PktLinkCard>
</div>

## Hva består Punkt av?

<div class="single-column-container single-column-container--medium-padding">
<PktLinkCard
  title="Komponentbibliotek"
  href={import.meta.env.BASE_URL + "komponenter-og-maler/"}
  skin="no-padding"
  iconName="chevron-right"
  client:only="react"
>
  UI-komponenter som følger WCAG-krav og Oslo kommunes visuelle profil.
</PktLinkCard>

<PktLinkCard
  title="Designfiler i Figma"
  href={
    import.meta.env.BASE_URL +
    "grunnleggende/for-designere/kom-i-gang/#trenger-du-figma-tilgang"
  }
  skin="no-padding"
  iconName="chevron-right"
  client:only="react"
>
  Figma-biblioteker med ferdige komponenter, ikoner, illustrasjoner og maler.
</PktLinkCard>
<PktLinkCard
  title="Kodepakker"
  href={import.meta.env.BASE_URL + "grunnleggende/for-utviklere/kom-i-gang/"}
  skin="no-padding"
  iconName="chevron-right"
  client:only="react"
>
  Fungerer med alle frontend-rammeverk, med fleksibel tilpasning.
</PktLinkCard>

<PktLinkCard
  title="Tokens og designmønstre"
  href={import.meta.env.BASE_URL + "grunnleggende/ressurser/om-ressurser/"}
  skin="no-padding"
  iconName="chevron-right"
  client:only="react"
>
  Felles grunnprinsipper for typografi, farger, spacing, layout med mer.
</PktLinkCard>

<PktLinkCard
  title="Artikler, god praksis og guider"
  href={import.meta.env.BASE_URL + "god-praksis/"}
  skin="no-padding"
  iconName="chevron-right"
  client:only="react"
>
  Alt du trenger å vite om hvordan du kan lage gode løsninger i Oslo kommune.
</PktLinkCard>
</div>

<ContentSection backgroundColor="beige" >
## Universell utforming som standard

Universell utforming handler om mer enn å tilfredsstille tekniske krav, det er en grunnleggende del av hvordan vi utvikler komponenter og digitale løsninger i Punkt. Vi jobber for at alle innbyggere, uavhengig av funksjonsevne, alder eller digital kompetanse, skal kunne bruke Oslo kommunes digitale tjenester på en likeverdig og inkluderende måte.

Når du bruker Punkt, er du allerede godt i gang med å lage løsninger som oppfyller kravene til universell utforming.

<PktLink
  href={import.meta.env.BASE_URL + "universell-utforming/punkt-og-uu/"}
  target="_self"
  iconName="chevron-right"
  client:only="react"
  iconPosition="left">
  Se hvordan vi jobber med universell utforming i Punkt
</PktLink>
</ContentSection>


---


## Kom i gang

**


# Kom i gang som utvikler

<Lead contributeBox={false}>
  Designsystemet Punkt skal hjelpe deg som utvikler i Origo å komme raskt i gang
  med å bygge digitale løsninger som følger Oslo kommunes visuelle identitet og
  som er universelt utformet.
</Lead>

Koden til Punkt er delt opp i ulike pakker:

- [punkt-assets](https://www.npmjs.com/package/@oslokommune/punkt-assets) - Ikoner, fonter og logoer
- [punkt-css](https://www.npmjs.com/package/@oslokommune/punkt-css) - Stilsett og -hjelpere for Punkts ressurser og komponenter
- [punkt-elements](https://www.npmjs.com/package/@oslokommune/punkt-elements) - Punkts Web Components-komponenter
- [punkt-react](https://www.npmjs.com/package/@oslokommune/punkt-react) - Punkts React-komponenter
- [punkt-testing-utils](https://www.npmjs.com/package/@oslokommune/punkt-testing-utils) - Verktøy for å forenkle enhetstesting

Minstekravet for å komme igang med Punkt er å installere `assets` og `css`. Deretter kan du velge om du trenger `elements` eller `react`.

`assets`, `css` og `elements` kan brukes fra vår CDN uten noen byggesteg, og det ønskes. Men de fleste velger å installere pakkene inn i sitt prosjekt. Se egne [CDN-instrukser](#cdn) dersom du ønsker å bruke Punkt fra CDN. Alle andre instrukser forutsetter at du laster ned våre pakker fra NPM.

<PktMessagebox title="Utviklere og Figma" skin="blue" client:only="react">
  <p>
    Designsystemet Punkt leveres også som et bibliotek i designverktøyet Figma.
    I tverfaglige team er det naturlig at utviklere og designere jobber tett
    sammen også i designprosessen. Vi anbefaler at alle utviklere har tilgang
    til Punkt i Figma.
  </p>

  <p>[Informasjon om Figma og tilganger](/grunnleggende/for-designere/kom-i-gang/)</p>
</PktMessagebox>

## CSS og assets

Punkt CSS er basert på `Sass`, og for å få mest mulig utbytte av våre stilsett anbefaler vi at dere bruker `SCSS`-filene våre fremfor de genererte CSS-filene.

Start med å legge til de nødvendige pakker i prosjektet ditt:

```sh
npm add -D sass
npm add @oslokommune/punkt-assets
npm add @oslokommune/punkt-css
```

Deretter kan du inkludere Punkt i hoved-stilsettet ditt:

```scss
/* Overstyr stien til fontene. */
@use "@oslokommune/punkt-css/dist/scss/abstracts/variables" with (
  $font-path: "@oslokommune/punkt-assets/dist"
);

/* Hent inn Punkts stiler */
@use "@oslokommune/punkt-css/dist/scss/pkt";
```

Og vips er du i gang! Det er mulig du må fjerne noen av dine lokale stiler (f.eks. font-family) dersom de krasjer med Punkt.

Les mer om verktøyene og hjelpeklassene våre under de forskjellige **Ressurser**-sidene.

## React

Vær oppmerksom på at Punkt React er avhengig av Punkt CSS. En del av våre React-komponenter tar internt i bruk komponenter fra Punkt Elements. Mer om dette lenger ned.

For å installere Punkt React:

```sh
npm add @oslokommune/punkt-react
```

Det er alt du strengt tatt trenger å gjøre. For instrukser om hvordan du tar i bruk komponentene og hva du kan gjøre med dem kan du lese på de enkelte komponenters dokumentasjonssider.

Eksempel:

```jsx
...
<PktTextInput label="First name" id="firstName" />
<PktButton skin="primary" variant="icon-left" iconName="user">
	Testbutton
</PktButton>
```

OBS: Våre React-komponenter bruker ikoner og ressurser fra vår CDN. Dersom du bruker en Content Security Policy (CSP) må du åpne for å hente ressurser fra `https://punkt-cdn.oslo.kommune.no/`.

Dersom du har enhetstester i løsningen din kan det være at du må tilrettelegge litt spesielt for de React-komponenter som internt tar i bruk Punkt Elements. Sjekk komponentens dokumentasjon under avsnittene for “Implementasjon i kode” om du er usikker.

## Elements

Punkt Elements er våre komponenter som er bygger på web components-teknologi. Det betyr at de kan tas i bruk i alle frontendrammeverk og til og med rett i HTML.

For å installere komponentene:

```sh
npm add @oslokommune/punkt-elements
```

Og deretter kan du finne instrukser for hver komponent under “Implementasjon i kode” på komponentens dokumentasjonsside.

Eksempel:

```js
```

```html
<pkt-textinput label="Fornavn" name="fornavn"></pkt-textinput>
<pkt-button type="submit"><span>Dette er en knapp</span></pkt-button>
```

Vær oppmerksom på at dersom du skal ha reaktivt innhold (innhold som kan forandre seg programmatisk) i komponentene anbefaler vi at det pakkes inn i en `span` eller `div` eller liknende.

## CDN

Dersom du ønsker å ta i bruk CSS, ressurser og Elements-komponenter fra CDN kan det enkelt gjøres ved å inkludere disse rett inn i prosjektet ditt. Vær dog oppmerksom på at dersom du bruker CSP kan du støte på utfordringer. Legg inn `https://punkt-cdn.oslo.kommune.no/` i CSP-reglene dine om så.

Vi anbefaler å enkelt og greit inkludere hele CSS-rammeverket vårt, men om du heller vil velge ut hva du ønsker å inkludere kan du finne rett fil ved å [lete i vår CDN](https://punkt-cdn.oslo.kommune.no/).

Her er et eksempel på hvordan du kan ta i bruk Punkt i en ren HTML-side:

```html
<!doctype html>
<html lang="no">
  <head>
    <meta charset="utf-8" />
    <title>Punkt</title>
    <link
      href="https://punkt-cdn.oslo.kommune.no/latest/css/pkt.min.css"
      rel="stylesheet"
    />
    <script
      src="https://punkt-cdn.oslo.kommune.no/latest/elements/pkt-consent.js"
      type="module"
    ></script>
  </head>
  <body>
    <pkt-consent
      id="osloConsent"
      triggerType="link"
      triggerText="Åpne samtykkemodal"
      devMode
    ></pkt-consent>
    <script>
      const consent = document.querySelector("#osloConsent");
      consent.addEventListener("toggle-consent", (event) => {
        console.log(event.detail);
      });
    </script>
  </body>
</html>
```

_Akkurat nå_ har vi en liten bug i Punkt Elements som gjør at for å få komponentene til å oppføre seg riktig fra CDN må du legge inn denne kodesnutten før du laster inn komponentene:

```html
<script>
  // Workaround for "process is not defined" i nettlesermiljøer
  window.process = window.process || {};
  window.process.env = window.process.env || {};
  window.process.env.NODE_ENV = window.process.env.NODE_ENV || "production";
</script>
```

## Trenger du hjelp?

Dersom du støter på noen problemer eller utfordringer må du ikke nøle med å ta kontakt med oss! Den enkleste måten å få kontakt med oss er på [Slack-kanalen vår](https://oslokommune.slack.com/archives/C01EWV9U07R), men vi har også en epost-adresse du kan nå oss på: [punkt@origo.oslo.kommune.no](mailto:punkt@origo.oslo.kommune.no).


---

