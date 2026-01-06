# Datepicker

**Generated**: 2025-11-06T10:52:48.945629
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/komponenter-og-maler/komponenter/datepicker/index.mdx`
- `component-specs/datepicker.json`
- `packages/elements/src/components/datepicker/datepicker-popup.ts`
- `packages/elements/src/components/datepicker/datepicker-range.ts`
- `packages/elements/src/components/datepicker/date-tags.ts`
- `packages/elements/src/components/datepicker/datepicker.ts`
- `packages/elements/src/components/datepicker/datepicker-multiple.ts`
- `packages/elements/src/components/datepicker/index.ts`
- `packages/elements/src/components/datepicker/datepicker-single.ts`
- `packages/elements/src/components/datepicker/datepicker-utils.ts`

---

## Documentation



# Datepicker

<Lead releaseDate="03.10.2024" lastUpdated="19.06.2025">
  Datepicker (datovelger) lar brukeren velge en dato, flere datoer eller et datointervall. Brukeren kan enten skrive dato direkte i feltet, eller velge fra en kalender.

Datepicker passer godt i skjemaer der datoen har betydning for videre steg, og når du vil tilby både fritekst og visuell kalender.

</Lead>

<div class="pkt-sr-only">

## Test komponenten

</div>

<PktPreviewWithJson
  client:only="react"
  specs={{ datepicker: datepickerSpec }}
  previewJson={datepickerPreview}
  fullWidth
/>

## Relaterte komponenter

<div class="cards-container">
  <PktLinkCard
    title="Text input"
    skin="blue"
    href={getComponentHref("textinput")}
    iconName="chevron-right"
    client:only="react"
  >
    Enkelt tekstfelt uten datovelger eller visuell støtte.
  </PktLinkCard>

<PktLinkCard
  title="Combobox"
  skin="blue"
  href={getComponentHref("combobox")}
  iconName="chevron-right"
  client:only="react"
>
  Inputfelt med søk- og/eller filtreringsmuligheter.
</PktLinkCard>

  <PktLinkCard
    title="Radiobutton"
    skin="blue"
    href={getComponentHref("radiobuttons")}
    iconName="chevron-right"
    client:only="react"
  >
    Egner seg til valg mellom få, faste datoer
  </PktLinkCard>
</div>
## Varianter

Card finnes i to hovedvarianter. Du kan kombinere disse med ulike skins og farger.

| Variant           | Bruk                                             |
| ----------------- | ------------------------------------------------ |
| Enkel dato        | Lar deg velge én spesifikk dato                  |
| Flere datoer      | Lar deg velge flere datoer samtidig              |
| Periode/intervall | Lar deg velge en periode med start- og sluttdato |

<ImageWrapper>
  <img
    src="/assets/komponenter/datepicker/datepicker-1.svg"
    alt="Eksempler på layout-variantene av datepicker"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/datepicker/datepicker-2.svg"
    alt="Eksempler på layout-variantene av datepicker"
    aria-hidden="true"
  />
  <img
    src="/assets/komponenter/datepicker/datepicker-3.svg"
    alt="Eksempler på layout-variantene av datepicker"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">
## Retningslinjer for bruk

### Bruk datepicker når

<ListWhenToUseOrNot
  icon="success"
  items={[
    "du vil la brukeren velge en dato eller et datointervall",
    "det er behov for både fritekst og kalender",
    "datoen er av betydning for videre steg i skjema eller prosess",
  ]}
/>

### Unngå datepicker når

<ListWhenToUseOrNot
  icon="avoid"
  items={[
    "datoen ikke har betydning for oppgaven",
    `brukeren kun trenger å velge mellom få, spesifikke datoer (da kan <a href="${getComponentHref("select")}">select</a> eller <a href="${getComponentHref("radiobuttons")}">radiobutton</a> være bedre)`,
  ]}
/>

### Forklar hva brukeren kan gjøre

Bruk hjelpetekst og label for å forklare format eller regler, f.eks. maks antall datoer eller begrensede valg. Beskriv hva som skal velges.

<ExampleComparison
  goodExample={{
    image: "/assets/komponenter/datepicker/datepicker-4.svg",
    imgAlt: "Eksempel forklarende label og hjelpetekst",
    caption: "Skriv forklarende label og hjelpetekst som hjelper brukeren å fylle inn riktig og forventet innhold",
  }}
  badExample={{
    image: "/assets/komponenter/datepicker/datepicker-5.svg",
    imgAlt: "Eksempel på datepicker med uklare etiketter.",
    caption: "Unngå uklare etiketter som kan forvirre",
  }}
/>
</ContentSection>

## Responsivitet

Datepicker tilpasser seg automatisk skjermstørrelsen. Kalenderen skalerer ned på små skjermer, slik at det fortsatt er lett å velge dato.

Vi anbefaler at du tester datepicker i løsningen din på ulike skjermstørrelser, både i stående og liggende visning, for å sikre at kalender, valgte datoer og eventuelle feilmeldinger vises tydelig.

<ImageWrapper>
  <img
    src="/assets/komponenter/datepicker/datepicker-6.svg"
    alt="Datepicker på mobil"
    aria-hidden="true"
  />
</ImageWrapper>
<ContentSection backgroundColor="subtle-pale-blue">

## Universell utforming

### Label skal alltid være synlig

Alle skjemaelementer må ha en synlig label (etikett). Den skal beskrive hva brukeren skal gjøre, for eksempel «Velg dato for avreise».

Dersom etiketten skjules visuelt, skal den likevel være tilgjengelig for skjermlesere ved å bruke skjulte klasser (for eksempel `pkt-sr-only`). Dette sikrer at brukere med skjermleser forstår hva feltet handler om.

### Dato må kunne velges med tastatur

Datepicker må fungere uten mus. Brukeren skal kunne:

- Åpne kalenderen med tastatur
- Navigere mellom datoer med piltaster
- Velge en dato med Enter
- Lukke kalenderen med Esc

Dette er særlig viktig for personer som bruker tastaturnavigasjon eller spesialutstyr. Sørg også for at det er tydelig hvilken dato som har fokus i kalenderen.

### Skjermlesere må kunne lese valgt dato

Når brukeren velger en dato, må denne informasjonen leses opp av skjermleser. Kalenderen må ha riktige ARIA-roller og -attributter, som `aria-label`og `aria-selected`. Bruk også ARIA Live-regioner forsiktig, slik at skjermleseren varsler valgte datoer på en kontrollert måte.

Hvis komponenten har feil, må feilmeldingen knyttes til inputfeltet med `aria-describedby`.

### Vis hjelpetekster for datoformat og regler

Datoformatet må forklares tydelig i komponenten. Bruk hjelpetekst som forklarer:

- Hvilket datoformat som skal brukes (f.eks. dd.mm.yyyy)
- Om det er begrensninger i valg av datoer
- Om brukeren kan velge flere datoer eller en periode

Unngå å kun vise denne informasjonen i placeholder, bruk alltid synlig tekst.

Les mer om universell utforming av cards:

<div class="cards-container">
  <PktLinkCard
    title="Datepickers(w3.org)"
    skin="beige"
    href="https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/datepicker-dialog/"
    iconName="chevron-right"
    client:only="react"
  >
    Tips og anbefalinger for hvordan du bør håndtere datovelgere.
  </PktLinkCard>
  <PktLinkCard
    title="Skjema (UU-tilsynet)"
    skin="beige"
    href="https://www.uutilsynet.no/veiledning/skjema/38"
    iconName="chevron-right"
    client:only="react"
  >
    Grunnleggende prinsipper for tilgjengelige skjemafelt.
  </PktLinkCard>
</div>
</ContentSection>

# Anatomi

| Element                                | Beskrivelse                                                                          |
| -------------------------------------- | ------------------------------------------------------------------------------------ |
| 1. Etikett (label)                     | Tekst som forteller hva brukeren skal gjøre                                          |
| 2. Hjelpetekst                         | Tilleggsinformasjon som forklarer datoformat, regler eller begrensninger (valgfritt) |
| 3. Inputfelt                           | Feltet der brukeren kan skrive inn dato manuelt, eller hvor valgt dato vises         |
| 4. Kalenderikon                        | Åpner kalenderen ved klikk                                                           |
| 5. Kalender (med navigasjon og datoer) | Viser valgt måned                                                                    |
| 6. Dagens dato                         | Datoen som er dagens dato, markert i kalenderen                                      |
| 7. Valgt dato/valgt periode            | Datoen eller perioden brukeren har valgt, markert i kalenderen og vist i inputfeltet |

<ImageWrapper backgroundColor="white">
  <img
    src="/assets/komponenter/datepicker/datepicker-7.svg"
    alt="Accordion anatomi."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="gray">
## Implementasjon i kode

<TechDetails specName="datepicker">
<div slot="usage">

### Bruk i skjema

For skjemaer fungerer Datepicker nær identisk med `<select>`. For én dato sendes én verdi ut i skjemaet (som vanlig `select`), og for flere datoer sendes flere datoer ut (som `select multiple`).

### Hendelseshåndtering

Datepicker for én enkel dato har en `change`-hendelse som sendes ut når ny dato velges (`onChange` i React). Denne er en “standard” hendelse som sendes ut fra alle input-elementer, som returnerer en Event med `target.value` som inneholder datoen.

For Datepicker med flere datoer, enten som periode eller frittstående datoer, bør man bruke hendelsen `value-change` (`onValueChange` i React). Denne hendelsen sender ut en CustomEvent med `detail` som inneholder en array av datostrenger.

</div>
<div slot="testing">

Om du bruker `data-testid` for å hente ut elementer i testene, vil attributten videresendes til selve skjemaelementet. Dersom du heller ønsker å bruke `data-testid` på elementet `<pkt-datepicker>`, må du sette attributten `skipForwardTestid` på elementet.

</div>
</TechDetails>

</ContentSection>

## Props

<SpecList specName="datepicker" />

OBS! `dateformat` er [standard formatteringsstreng](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table) for visning av datoer. Denne brukes for å sette “menneskeleselig” format på datoene i tags ved flervalgsmodus.


---


### Component Specification

**Element name**: `pkt-datepicker`

**React component**: `PktDatepicker`

**CSS class**: `.pkt-datepicker`


#### Properties

| Prop (React) | Attribute (Custom Element) | Type | Default | Description |
|--------------|----------------------------|------|---------|-------------|
| `name` | `name` | string | `-` | - |
| `label` | `label` | string | `-` | - |
| `helptext` | `helptext` | string | `-` | - |
| `helptextDropdown` | `helptextDropdown` | string | `-` | Hjelpetekst som vises i en lukket boks man kan åpne |
| `helptextDropdownButton` | `helptextDropdownButton` | string | `Les mer` | - |
| `dateformat` | `dateformat` | string | `dd.MM.yyyy` | - |
| `currentmonth` | `currentmonth` | ISOdatestring | `-` | - |
| `value` | `value` | ISOdatestring | `-` | - |
| `excludeweekdays` | `excludeweekdays` | string | `-` | Kommaseparert liste over ukedager (1-7) som skal ekskluderes |
| `excludedates` | `excludedates` | ISOdatestring | `-` | - |
| `min` | `min` | ISOdatestring | `None` | - |
| `max` | `max` | ISOdatestring | `None` | - |
| `weeknumbers` | `weeknumbers` | boolean | `False` | - |
| `withcontrols` | `withcontrols` | boolean | `False` | - |
| `multiple` | `multiple` | boolean | `False` | - |
| `maxlength` | `maxlength` | number | `-` | - |
| `range` | `range` | boolean | `False` | - |
| `hasError` | `hasError` | boolean | `False` | - |
| `errorMessage` | `errorMessage` | string | `-` | - |
| `disabled` | `disabled` | boolean | `False` | - |
| `fullwidth` | `fullwidth` | boolean | `False` | - |
| `required` | `required` | boolean | `False` | - |
| `requiredTag` | `requiredTag` | boolean | `False` | - |
| `requiredText` | `requiredText` | string | `Må fylles ut` | - |
| `optionalTag` | `optionalTag` | boolean | `False` | - |
| `optionalText` | `optionalText` | string | `Valgfritt` | - |
| `tagText` | `tagText` | string | `-` | Tekst som vises i en tag ved siden av label |
| `useWrapper` | `useWrapper` | boolean | `True` | Indikerer at feltet skal ha synlig label og hjelpetekst |
| `id` | `id` | string | `-` | Unik identifikasjon for datovelgeren |


#### Events

- **`change`**: Returnerer valgt dato som streng i ISO-format
- **`value-change`**: Returnerer en <code>array</code> med valgte datoer i ISO-format
- **`toggleHelpText`**: Returnerer <code>event.detail { isOpen: true }</code> eller <code>event.detail { isOpen: false }</code> når hjelpeteksten åpnes eller lukkes


