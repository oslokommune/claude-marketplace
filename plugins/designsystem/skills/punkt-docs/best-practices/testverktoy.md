# Testverktøy

**Generated**: 2025-11-06T10:52:48.985035
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/universell-utforming/testverktoy/index.mdx`

---

**Category**: universell-utforming

**Description**: 



## Manuelle tester

Testing for universell utforming innebærer blant annet manuell testing, brukertesting og automatiserte verktøy. Det finnes mange ulike testverktøy og ingen fanger opp alt av utfordringer, så det er smart å bruke flere ulike testverktøy og også være klar over at de automatiserte løsningene må suppleres med manuell testing.

### Brukertesting

Kjør brukertester med folk! Finn brukere med ulike utgangspunkt for å bruke løsningen din. Spesielt viktig er det å teste med brukere av skjermleser og tastatur.

### Simulering

Det finnes flere verktøy som prøver å simulere ulike funksjonsnedsettelser. Det anbefales å teste noen av disse verktøyene, fordi det er en fin måte å få litt mer forståelse hvordan digitale løsinger oppleves av ulike brukere:

- [Web disability Simulator](https://chrome.google.com/webstore/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla)
- [Silktide Chrome-utvidelse](https://silktide.com/resources/tools/) (Vår favoritt)

### Skjermleser

Skjermlesere hjelper brukere med nedsatt syn å oppfatte innhold og navigere digitale løsninger. Det finnes ulike verktøy som er beregnet til bruk i ulike nettlesere og operativsystemer. Disse oppfører seg litt forskjellig, så det er lurt å teste med flere verktøy. De mest kjente skjermlesere er JAWS, VoiceOver og NVDA.

- [Liste over skjermlesere](https://en.wikipedia.org/wiki/List_of_screen_readers)
- [Silktide Chrome-utvidelse](https://silktide.com/resources/tools/) har også en funksjon for å simulere skjermleser.

Test om innholdet blir fremstilt på en logisk og tiltenkt måte. Pass på at ikke skjermleseren hopper over viktig informasjon eller funksjoner.

### Navigering

For å teste ut om løsningen er mulig å betjene ved hjelp av tastatur bør dette testes manuelt. Dette kan du gjøre slik:

- "Tab" er fremover
- "Tab" + "shift" er bakover
- "Space" for å ta et valg
- "Enter" for å aktivere funksjon
- Bruk piltaster for å navigere

## Automatiske tester

Mange tester er nettleserutvidelser som er enkle å kjøre både under utvikling og for andre når nettsiden er ute. Det er viktig å være klar over at automatiserte testverktøy bare finner [ca 30% av feilene i digitale løsninger.](https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage/) Det er derfor svært viktig med manuelle tester og brukertesting som en del av testprosessen.

### Nettleserutvidelser

Sjekk mange WCAG-krav med Wave. Denne er for alle som liker brukervennlige verktøy:

- [Wave](https://wave.webaim.org/)

Andre verktøy tester mer enn Wave og er mer tekniske, anbefales for utviklere:

- [Axe](https://www.deque.com/axe/devtools/) - Gratis, men betalt versjon for dypere tester.
- [Siteimprove](https://siteimprove.com/nb-no/core-platform/integrations/browser-extensions/) - Denne bruker UU-tilsynet. Gratis, men betalt versjon for dypere tester.
- [Google Lighthouse](https://developers.google.com/web/tools/lighthouse/) - Gratis. Tester også ytelse og søkemotoroptimalisering.
- [Silktide Chrome-utvidelse](https://silktide.com/resources/tools/) - Gratis. Mange forskjellige tester, også skjermleser.
- [ARC toolkit - Chrome-utvidelse](https://chrome.google.com/webstore/detail/arc-toolkit/chdkkkccnlfncngelccgbgfmjebmkmce/related)
- [Playwright](https://playwright.dev/)

Og sjekk fargekontraster med:

- [A11y fargekontrastsjekker](https://color.a11y.com/)
- [Contrast checker](https://webaim.org/resources/contrastchecker/) fra WebAIM
- [Stark](https://www.figma.com/community/plugin/732603254453395948/Stark) plugin i Figma
- Developer tools i nettlesere

### axe cli

Vi kan anbefale å installere [axe-cli](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/cli) for rask test av WCAG-kravene under utviklingsprosessen.

Du vil trenge Node og NPM.
Installer globalt eller i ditt prosjekt:

```sh
$ npm install @axe-core/cli -g
```

Kjør prosjektet ditt og test siden du ønsker å teste, man kan legge til flere paths for å teste flere sider:

```sh
$ axe http://localhost:3000 http://localhost:3000/komponenter/badge
```

Du vil få feilmeldinger i terminal med en link til en side som hjelper deg med å fikse feilen.

```sh

  Violation of "landmark-no-duplicate-banner" with 1 occurrences!
    Ensures the document has at most one banner landmark. Correct invalid elements at:
     - #pkt-header
    For details, see: https://dequeuniversity.com/rules/axe/4.4/landmark-no-duplicate-banner

```

### Jest axe

Du kan lage egne UU-tester med [jest-axe](https://www.npmjs.com/package/jest-axe)

Disse kan inkluderes som en GitHub action. Les mer om dette i denne artikkelen om [automatisering av uu-testing](https://www.adrianbolonio.com/en/blog/accessibility-github-actions).

### Cypress axe

Du kan lage cypress-tester med [cypress-axe](https://www.npmjs.com/package/cypress-axe).

Disse kan inkluderes som en GitHub action. Les mer om dette i denne artikkelen om [automatisering av uu-testing](https://www.adrianbolonio.com/en/blog/accessibility-github-actions).

### Robust løsning

En robust løsning er om koden er uten store syntaksfeil, at man bruker [HTML5-semantikk](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#inline_text_semantics), og [ARIA-roller](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles) om HTML5 ikke er tilstrekkelig.

Bruk verktøy for å analysere koden for syntaksfeil, for eksempel ESLint.
Eller kjør kode eller ferdig nettside med:

- [W3C Markup Validator](https://validator.w3.org/)

#### Les mer

<div class="cards-container">

  <PktLinkCard
    title="Testoppsett hos nav.no"
    skin="blue"
    href="https://github.com/navikt/uu-testing"
    iconName="document-code"
    client:only="react"
  >
    NAV sitt testoppsett for digitale løsninger
  </PktLinkCard>
  <PktLinkCard
    title="Sjekkliste (uutilsynet.no)"
    skin="blue"
    href="https://www.uutilsynet.no/tilgjengelighetserklaering/wcag-sjekkliste-utfylling-av-tilgjengelighetserklaering/1333"
    iconName="list"
    client:only="react"
  >
    Sjekklister for utfylling av tilgjengelighetserklæring
  </PktLinkCard>
</div>