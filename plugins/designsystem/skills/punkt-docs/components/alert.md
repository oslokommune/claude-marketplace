# Alert

**Generated**: 2025-11-06T10:52:48.935100
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/alert/index.mdx`
- `component-specs/alert.json`
- `packages/elements/src/components/alert/alert.ts`
- `packages/elements/src/components/alert/index.ts`

---

## Documentation



# Alert

<Lead
  releaseDate="13.03.2023"
  lastUpdated="07.07.2025"
>
Alert (varsel, statusbeskjed) gir en beskjed til brukeren – for eksempel for å informere om en viktig hendelse, bekrefte en handling eller varsle om en feil.

Formålet med en alert er å hjelpe brukeren med å forstå hva som har skjedd og eventuelt hva de bør gjøre videre.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ alert: alertSpec }}
  previewJson={alertPreviewJson}
  fullWidth
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Messagebox"
    skin="blue"
    href={getComponentHref("messagebox")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du vil vise informasjon som ikke er kritisk eller tidsavhengig.
  </PktLinkCard>
  <PktLinkCard
    title="Modal"
    skin="blue"
    href={getComponentHref("modal")}
    iconName="chevron-right"
    client:only="react"
  >
    Når du vil vise detaljert innhold uten å ta brukeren ut av kontekst.
  </PktLinkCard>
  <PktLinkCard
    title="Accordion"
    skin="blue"
    href={getComponentHref("accordion")}
    iconName="chevron-right"
    client:only="react"
  >
    Når brukeren kan åpne og lukke innhold for å få mer informasjon.
  </PktLinkCard>
</div>

## Varianter

### Statuser

Alert har fire ulike statuser med tilhørende farge og ikon:

| Type            | Bruk                                                                                            |
| --------------- | ----------------------------------------------------------------------------------------------- |
| Info (blå)      | Gir tilleggsinformasjon som ikke krever umiddelbar handling                                     |
| Success (grønn) | Bekrefter at en handling har vært vellykket                                                     |
| Warning (gul)   | Advarer brukeren om systemfeil og konsekvenser av valg                                          |
| Error (rød)     | Gir brukeren beskjed om at noe er feil. Hvis mulig, si noe om hvordan hen kan løse oppgaven sin |

<ImageWrapper>
  <img
    src="/assets/komponenter/alert/alert-1.svg"
    alt="Alle fargevarianter av alert"
    aria-hidden="true"
  />
</ImageWrapper>

### Størrelse

Alert har to ulike størrelser:

| Størrelse | Bruk                                                    |
| --------- | ------------------------------------------------------- |
| Standard  | Default                                                 |
| Kompakt   | For korte, tettere meldinger (f.eks. inline i skjemaer) |

<ImageWrapper>
  <img
    src="/assets/komponenter/alert/alert-2.svg"
    alt="To varianter av alert, default og compact"
    aria-hidden="true"
  />
</ImageWrapper>

### Bruksområder

Alert har tre ulike bruksområder:

| Bruksområde  | Plassering                                             |
| ------------ | ------------------------------------------------------ |
| Inline alert | Brukes tett på innhold (f.eks. under felt)             |
| Banner alert | Plassert over innhold, med tittel og dato              |
| Toast alert  | Kort status som vises midlertidig (f.eks. autolagring) |

<ContentSection backgroundColor="subtle-pale-blue">

## Retningslinjer for bruk

### Bruk alert når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "du vil informere brukeren om en viktig status, endring eller feil",
    "du vil bekrefte at en handling har blitt utført, for eksempel at noe har blitt sendt inn, lagret, eller slettet",
  ]}
/>

### Unngå alert når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "informasjonen ikke er kritisk for brukerens oppgave",
    `det bare handler om visuell gruppering – bruk <a href="${getComponentHref("messagebox")}">messagebox</a> i stedet`,
    "det allerede finnes for mange alerts ",
  ]}
/>

### Alerten skal være lett å forstå

Bruk et ikon som matcher alvorlighetsgraden og budskapet.

Alerten bør formidle budskapet raskt og effektivt, særlig når du bruker inline alert. Ved bruk av banner alert, kan du vurdere å legge til en tittel hvis meldingen trenger en oppsummering.

Hvis alerten ikke er knyttet til en bestemt handling, bør brukeren kunne lukke den manuelt. Dette gir brukeren kontroll og reduserer visuell støy.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/alert/alert-3.svg",
    imgAlt: "Eksempel på klare og direkte meldinger",
    caption: "Skriv klare og direkte meldinger",
  }}
  badExample={{
    image: "/assets/komponenter/alert/alert-4.svg",
    imgAlt: "Eksempel på unødvendig detaljert informasjon",
    caption: "Unngå lange avsnitt eller unødvendig detaljert informasjon",
  }}
/>
### Vis én alert om gangen

For mange alerts kan overvelde og forvirre. Vis én alert om gangen hvis mulig, og sørg for at den viktigste meldingen vises øverst.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/alert/alert-5.svg",
    imgAlt: "Eksempel tydelig og klart, i kun én alert.",
    caption: "Skriv tydelig og klart, i kun én alert",
  }}
  badExample={{
    image: "/assets/komponenter/alert/alert-6.svg",
    imgAlt: "Eksempel på flere statuser i flere ulike alerts.",
    caption: "Unngå å dele opp flere statuser i flere ulike alerts",
  }}
/>

### Plasser alerten i nærheten av innholdet

Plasser alerten så nært det innholdet eller feltet den handler om som mulig. Det gjør det enklere å forstå konteksten.

Hvis alerten er en feilmelding, skal brukeren alltid få vite hva hen kan gjøre for å fikse feilen. Du finner tips om hvordan skrive gode feilmeldinger i artikkelen om beste praksis for skjemadesign.

</ContentSection>

## Responsivitet

Alert-komponenten tilpasser seg automatisk tilgjengelig plass og bryter linjer der det er nødvendig. Dette gjelder både inline alerts, banner alerts og toast alerts.

Det er likevel viktig å teste hvordan alerten fungerer i din løsning, da
kontekst og plassering har betydning for opplevelsen:

- Toast alerts bør testes på mobil (både i stående og liggende visning) for å sikre at meldingen er tydelig og ikke blir oversett.
- Plassering påvirker tilgjengelighet og synlighet. På små skjermer kan det være nødvendig å justere marginer, padding eller z-index for å unngå at alerten dekker viktig innhold.
- Lange meldinger bør vurderes nøye. Selv om komponenten bryter linjer, kan for mye tekst gjøre det vanskelig å oppfatte innholdet raskt.

Kort oppsummert: Alerten håndterer layout og linjebryting automatisk, men du
må selv sikre god plassering, visuell prioritering og tydelighet i den
konteksten alerten brukes.

<ImageWrapper>
  <img
    src="/assets/komponenter/alert/alert-7.svg"
    alt="Alert på mobil"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Universell utforming

### Innhold må gi mening med skjermleser

Alert må kunne oppfattes av alle brukere, uavhengig av hvordan de navigerer
eller hvilke hjelpemidler de bruker. Du må sørge for at innholdet kan leses
med skjermleser og være tilgjengelig med kun tastatur.

Det er viktig at budskapet i alerten ikke kun blir formidlet visuelt – både
tekst og ikon må bidra til å forklare innholdet.

### Sørg for at meldingen kan oppfattes i tide

Ved bruk av toast alerts som forsvinner automatisk må du være sikker på at
alle brukere får med seg meldingen, også de med skjermleser. Er du er i
tvil, anbefaler vi å la meldingen bli værende med mulighet for å lukke den
manuelt.

### Lukkeknappen må være tilgjengelig med tastatur

Alerts som kan lukkes må ha en tydelig og tilgjengelig lukkeknapp som kan
fokuseres og aktiveres med tastatur.

### Test komponenten på ulike skjermstørrelser

Du må sørge for å teste at komponenten fungerer som den skal på ulike
skjermer. Vi anbefaler også at du tester på ulike zoom-nivå.{" "}

Mer om universell utforming av alerts:

<div class="cards-container">
  <PktLinkCard
    title="Statusbeskjed (UUtilsynet)"
    skin="beige"
    href="https://www.uutilsynet.no/wcag-standarden/413-statusbeskjeder-niva-aa/152"
    iconName="chevron-right"
    client:only="react"
  >
    Hvordan oppfylle WCAG krav til statusbeskjeder forklart av UUtilsynet
  </PktLinkCard>
  <PktLinkCard
    title="ARIA Live Regions (MDM webdocs)"
    skin="beige"
    href="https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Live_Regions"
    iconName="chevron-right"
    client:only="react"
  >
    Mer om bruk av aria-live i alerts
  </PktLinkCard>
</div>

</ContentSection>

## Anatomi

| Element                   | Beskrivelse                        |
| ------------------------- | ---------------------------------- |
| 1. Ikon                   | Angir type alert (valgfritt)       |
| 2. Tittel (valgfritt)     | Beskrivende overskrift (valgfritt) |
| 3. Melding                | Hovedinnhold                       |
| 4. Dato (valgfritt)       | Dato eller tidsperiode (valgfritt) |
| 5. Lukkeknapp (valgfritt) | Lukker alert permanent (valgfritt) |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/alert/alert-8.svg"
    alt="Anatomi av alert"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

### Om options

Alert kan enten ta en JSON-liste som attributt/prop i options, eller en rekke `<option>`-elementer. Dersom du forventer at options vil endre seg dynamisk, eller ta i bruk `tagSkinColor`, `description` eller `prefix`, anbefaler vi at du bruker JSON-liste. Uansett vil `options` alltid bli konvertert til en array av objekter i komponenten.

<TechDetails specName="alert"></TechDetails>

</ContentSection>

## Props

<SpecList specName="alert" />


---


### Component Specification

**Element name**: `pkt-alert`

**React component**: `PktAlert`

**CSS class**: `.pkt-alert`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `title` | `title` | string | `-` | Tittelen som vises øverst i på meldingen |
| `skin` | `skin` | `info`, `success`, `warning`, `error` | `info` | Hvordan type melding er dette? |
| `date` | `date` | string | `-` | Dato som vises nederst i på meldingen |
| `ariaLive` | `ariaLive` | `off`, `polite`, `assertive` | `polite` | Hvordan skal skjermleseren lese opp meldingen? |
| `compact` | `compact` | boolean | `False` | Gjør meldingen mindre |
| `closeAlert` | `closeAlert` | boolean | `False` | Viser 'Lukk'-knappen |


#### Events

- **`onClose`**: React: Klikk-event for 'Lukk'-knappen
- **`close`**: Vue: Klikk-event for 'Lukk'-knappen



### TypeScript Interface

```typescript
export interface IPktAlert {
  skin?: TAlertSkin
  closeAlert?: boolean
  title?: string
  date?: string | null
  ariaLive?: TAriaLive | null
  'aria-live'?: TAriaLive | null
  compact?: boolean
  role?: string
}
```
