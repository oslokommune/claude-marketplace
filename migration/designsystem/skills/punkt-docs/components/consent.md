# Consent

**Generated**: 2025-11-06T10:52:48.943987
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/consent/index.mdx`
- `component-specs/consent.json`
- `packages/elements/src/components/consent/strings.ts`
- `packages/elements/src/components/consent/consent.ts`
- `packages/elements/src/components/consent/index.ts`

---

## Documentation



# Consent

<Lead releaseDate="05.05.2025" lastUpdated="19.06.2025" >

Consent (cookie banner) lar brukeren gi samtykke til
informasjonskapsler og annen datainnsamling. Den brukes for å informere
brukeren om hvordan dataene deres blir brukt og for å gi dem muligheten til å
godta eller avslå bruken av informasjonskapsler.

Du kan også bruke Oslo kommunes cookie banner direkte uten denne komponenten. Se [Oslo kommunes cookie banner](https://github.com/oslokommune/ukeweb_cookie_banner) på Github.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ consent: consentSpec }}
  previewJson={consentPreview}
/>

## Varianter

Selve modalvinduet er alltid likt, men metodene for å åpne den kan varieres. På første innlasting av siden vil den alltid åpne dersom brukeren ikke tidligere har gitt samtykker.

| Triggertype | Beskrivelse             |
| ----------- | ----------------------- |
| Knapp       | Åpner consent via knapp |
| Lenke       | Åpner consent via lenke |
| Ikon        | Åpner consent via ikon  |

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk consent når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "du skal innhente eller oppdatere samtykker til bruk av cookies og sporing",
    "du må gi brukeren tydelig informasjon om hvordan data brukes",
  ]}
/>

### Unngå consent når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    `du ikke håndterer data eller sporing som krever samtykke`,
    `du ønsker å informere om noe annet enn cookies og personvern (bruk da <a href="${getComponentHref("modal")}">modal</a>)`,
  ]}
/>

### Consent skal være enkel å forstå

Bruk tydelig språk som forklarer hva brukeren samtykker til, og gi alltid mulighet til å avslå eller endre senere.

### Gjør consent og innstillinger lett tilgjengelig

Funksjonen for å åpne innstillinger senere kan gjøres gjennom en knapp, en lenke eller et ikon.

</ContentSection>

## Responsivitet

Consent fungerer på alle skjermstørrelser og tilpasser seg automatisk tilgjengelig plass. På mobil åpner den som et helskjerms modalvindu. Vi anbefaler å teste hvordan teksten fremstår på små skjermer for å sikre at informasjonen er lett å lese.

<ImageWrapper>
  <img
    src="/assets/komponenter/consent/consent-1.svg"
    alt="Consent på små skjermer"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

- Knappen for å endre eller avslå samtykker skal være tydelig og tilgjengelig
- Bruk klarspråk slik at innholdet er lett å forstå

<div class="cards-container">
  <PktLinkCard
    title="Cookie Permissions 101 (NN/g)"
    skin="beige"
    href="https://www.nngroup.com/articles/cookie-permissions/"
    iconName="chevron-right"
    client:only="react"
  >
    Forskning på hvordan brukere forstår og håndterer samtykker
  </PktLinkCard>
</div>
</ContentSection>

## Anatomi

| Element                                  | Beskrivelse                                                         |
| ---------------------------------------- | ------------------------------------------------------------------- |
| 1. Tittel                                | Overskrift som forklarer at Oslo kommune bruker informasjonskapsler |
| 2. Brødtekst                             | Forklarer hva cookies brukes til og hva samtykke innebærer          |
| 3. Primærhandling                        | Godta alle                                                          |
| 4. Sekundærhandling                      | Kun nødvendige                                                      |
| 5. Innstillinger for informasjonskapsler | Åpner innstillinger for å endre samtykker                           |
| 6. Illustrasjon                          | Illustrasjon av en kjeks                                            |
| 7. Logo                                  | Oslo-logo som viser Oslo kommune som avsender                       |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/consent/consent-2.svg"
    alt="Anatomi for Consent"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="consent" />

### Håndtering av samtykker

Når brukeren bekrefter eller endrer samtykker, vil komponenten sende ut et custom event med navnet `toggle-consent`. Dette eventet kan brukes til å oppdatere applikasjonen din med de nye samtykkene. Du kan lytte til dette eventet ved å bruke `addEventListener` eller ved å bruke `onToggleConsent`-prop'en i React.

Custom event-hendelsen inneholder en `detail`-egenskap som er et objekt med de samtykkene brukeren har gitt. Dette objektet vil se slik ut:

```json
{
  "statistics": true,
  "survey": true,
  "functional": true
}
```

I tillegg til at man kan sjekke hvilke samtykker brukeren har gitt og agere deretter, kan man også sende inn attributtene `googleAnalyticsId` og `hotjarId` for å aktivere Google Tag Manager/Google Analytics og Hotjar uten å måtte sette opp noe selv.

<CodeTabs showElementsTab hideWebTab client:only="react">
<div class="elements tabcontent">

```html
<pkt-consent id="osloConsent" googleAnalyticsId="GTM-00000"></pkt-consent>
<script>
  const consent = document.querySelector("#osloConsent");
  consent.addEventListener("toggle-consent", (event) => {
    console.log(event.detail);
  });
</script>
```

</div>

<div class="react tabcontent">
  ```jsx
  <PktConsent
    googleAnalyticsId="GTM-00000"
    onToggleConsent={(event) => {
      console.log(event.detail);
    }}
  />
  ```
</div>

<div class="vue tabcontent">
```html
<pkt-consent
  googleAnalyticsId="GTM-00000"
  @toggle-consent="(event) => {
    console.log(event.detail);
  }}"
></pkt-consent>
```
</div>
</CodeTabs>

### Bruk på andre domener enn \*.oslo.kommune.no

Ut av boksen vil Consent-komponenten kun fungere på domener som ender på `.oslo.kommune.no`. Dersom du ønsker å bruke den på et annet domene, f.eks. `localhost` eller `*.oslo.systems`, kan du sette attributten `cookieDomain` til det domenet du ønsker å bruke. Dette må gjøres både i HTML og i React/Vue.

Om du skal bruke Consent både i testmiljøer og i produksjon anbefaler vi at du sjekker `window.location.hostname` og setter `cookieDomain` deretter. Dette kan gjøres slik:

<CodeTabs showElementsTab hideWebTab hideVueTab client:only="react">
<div class="elements tabcontent">

```html
<script>
  function getCookieDomain(host) {
    if (host.includes("oslo.systems")) return ".oslo.systems";
    if (host.includes("oslo.kommune.no")) return ".oslo.kommune.no";
    return host;
  }

  window.cookieBanner_cookieDomain = getCookieDomain(window.location.hostname);
</script>

<pkt-consent id="osloConsent"></pkt-consent>
```

</div>
<div class="react tabcontent">

```jsx
function getCookieDomain(host) {
  if (host.includes("oslo.systems")) return ".oslo.systems";
  if (host.includes("oslo.kommune.no")) return ".oslo.kommune.no";
  return host;
}

const cookieDomain = getCookieDomain(window.location.hostname);

return <PktConsent cookieDomain={cookieDomain} />;
```

</div>
</CodeTabs>

### Content Security Policy / CSP

For å bruke Consent i din applikasjon må du tillate `https://cdn.web.oslo.kommune.no` (eller `https://*.oslo.kommune.no`) i din Content Security Policy. Spesifikt må `script-src` og `style-src` tillates og dette kommer av at Consent laster inn innhold fra Oslo kommunes CDN.

Spør oss gjerne om du trenger hjelp til å sette opp CSP!

</ContentSection>

## Props

<SpecList specName="consent" />


---


### Component Specification

**Element name**: `pkt-consent`

**React component**: `PktConsent`

**CSS class**: `.pkt-consent`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `triggerType` | `triggerType` | `button`, `link`, `icon` | `-` | Type element som brukes for å trigge visning av innstillinger for samtykke |
| `triggerText` | `triggerText` | string | `-` | Tekst som vises på trigger-elementet |
| `googleAnalyticsId` | `googleAnalyticsId` | string | `-` | ID for Google Analytics eller Google Tag Manager |
| `hotjarId` | `hotjarId` | string | `-` | ID for Hotjar |
| `devMode` | `devMode` | boolean | `-` | Aktiverer utviklermodus for testing av samtykkeinnstillinger |
| `cookieDomain` | `cookieDomain` | string | `-` | Domene for cookies, brukes for å sette cookies på riktig domene |
| `cookieSecure` | `cookieSecure` | boolean | `-` | Angir om cookies skal settes som sikre (kun over HTTPS) |
| `cookieExpiryDays` | `cookieExpiryDays` | string | `-` | Antall dager før cookies utløper |


#### Events

- **`toggle-consent`**: Event som trigges når brukeren lagrer eller oppdaterer samtykke
- **`onToggleConsent`**: React-Event som trigges når brukeren lagrer eller oppdaterer samtykke


