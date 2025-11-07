# Farger

**Generated**: 2025-11-06T10:52:48.972247
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/grunnleggende/ressurser/colors.mdx`

---


# Farger

<Lead contributeBox={false}>
  Oslo kommune har en fargepalett som er inspirert av Oslos bybilde; blått fra
  trikken og fjorden, grønt fra våre grønne lunger og marka. De varme fargene er
  inspirert av fasader på byens bygninger.
</Lead>

Samlet sammensetning av fargene bør stemme overens med merkevarefargen som er valgt som hovedfarge til applikasjonen/domenet. Nyansefarger bør brukes på en måte som komplimenterer brandfargene.

## Navngiving og fargeoppsett

Vi har to nivåer av farger i Punkt: brand farger og semantiske farger:

<ImageWrapper>
  <img
    src="/assets/ressurser/colors/farger-1.svg"
    alt="Farger"
    aria-hidden="true"
  />
</ImageWrapper>

Fargesystemet består av globale farger som refererer til hva fargen er (eks. brand-dark-blue-100) og et semantisk nivå som beskriver hva fargen skal brukes til (eks. text-body-default).

Fargene har semantiske fargenavn som er bygget opp av tre ledd: UI-element - Situasjon - Variant/Tilstand. Første ledd refererer til elementet som fargelegges: background, Surface

- Background: Som regel bakgrunnen på hele siden (HTML body).
- Surface: Bakgrunnsfargen til en element, som for eksempel et panel, en knapp, en seksjon, etc.
- Border: Fargen til en ramme (stroke).
- Text/Icon: Fargen på tekst og ikoner.

## Brand farger

<Colors category="brand" client:only="react" />

## Semantiske farger

<Colors category="semantic" client:only="react" showToolbar />

## Sass-variabler

Alle fargene er tilgjengelige som et Sass map i `scss/abstracts/varaiables/_colors.scss`.

```scss
$pkt-colors: (
  // Blue
  brand-blue-100: #f1fdff,
  brand-blue-200: #e5fcff,
  brand-blue-300: #d1f9ff,
  brand-blue-500: #b3f5ff,
  brand-blue-1000: #6fe9ff,
  brand-dark-blue-700: #6a698b,
  brand-dark-blue-1000: #2a2859,
  brand-warm-blue-1000: #1f42aa,
  // Green
  brand-green-400: #c7fde9,
  brand-green-1000: #43f8b6,
  brand-light-green-400: #e5ffe6,
  brand-light-green-1000: #c7f6c9,
  brand-dark-green-1000: #034b45,
  // Yellow
  brand-yellow-1000: #f9c66b,
  brand-yellow-500: #ffe7bc,
  // Red
  brand-red-100: #fff2f1,
  brand-red-400: #ffdfdc,
  brand-red-600: #ffb4ac,
  brand-red-1000: #ff8274,
  // Beige
  brand-light-beige-1000: #f8f0dd,
  brand-dark-beige-1000: #d0bfae,
  // Neutrals
  brand-neutrals-white: #ffffff,
  brand-neutrals-100: #f9f9f9,
  brand-neutrals-200: #f2f2f2,
  brand-neutrals-1000: #2c2c2c,
  brand-neutrals-black: #000000,
  brand-neutrals-transparent: transparent,
  // Purple
  brand-purple-1000: #e0adff,
  // Grays
  grays-gray-100: #e6e6e6,
  grays-gray-200: #cccccc,
  grays-gray-300: #b3b3b3,
  grays-gray-400: #9a9a9a,
  grays-gray-500: #808080,
  grays-gray-600: #666666,
  grays-gray-700: #4d4d4d,
  grays-gray-800: #333333,
  grays-gray-900: #1a1a1a,
  grays-gray-1000: #2c2c2c
) !default;
```

## Semantiske variabler

De semantiske fargene beskriver hva variablene er ment å brukes til.
Fargenavnet er bygget opp av tre ledd: UI-element, situasjon, variant/tilstand.

Første ledd refererer til elementet som fargelegges: background, Surface.

- Background: Som regel bakgrunnen på hele siden (HTML body).
- Surface: Bakgrunnsfargen til en element, som for eksempel et panel, en knapp, en seksjon, etc.
- Border: Fargen til en ramme (stroke).
- Text/Icon: Fargen på tekst og ikoner.

Dette er våre semantiske variabler:

```scss
$pkt-semantic-colors: (
  // Background
  background-card: map.get($pkt-colors, brand-neutrals-white),
  background-default: map.get($pkt-colors, brand-neutrals-white),
  background-subtle: map.get($pkt-colors, brand-neutrals-100),
  background-transparent: map.get($pkt-colors, brand-neutrals-transparent),
  // Borders
  border-default: map.get($pkt-colors, brand-dark-blue-1000),
  border-beige: map.get($pkt-colors, brand-dark-beige-1000),
  border-blue: map.get($pkt-colors, brand-blue-1000),
  border-gray: map.get($pkt-colors, grays-gray-200),
  border-green: map.get($pkt-colors, brand-green-1000),
  border-light-beige: map.get($pkt-colors, brand-light-beige-1000),
  border-red: map.get($pkt-colors, brand-red-1000),
  border-subtle: map.get($pkt-colors, brand-neutrals-200),
  border-yellow: map.get($pkt-colors, brand-yellow-1000),
  border-states-active: map.get($pkt-colors, brand-warm-blue-1000),
  border-states-disabled: map.get($pkt-colors, grays-gray-300),
  border-states-focus: map.get($pkt-colors, brand-purple-1000),
  border-states-hover: map.get($pkt-colors, brand-warm-blue-1000),
  // Surface
  surface-default-faded-green: map.get($pkt-colors, brand-light-green-400),
  surface-default-faded-red: map.get($pkt-colors, brand-red-400),
  surface-default-gray: map.get($pkt-colors, brand-neutrals-100),
  surface-default-light-beige: map.get($pkt-colors, brand-light-beige-1000),
  surface-default-light-blue: map.get($pkt-colors, brand-blue-300),
  surface-default-light-green: map.get($pkt-colors, brand-green-400),
  surface-default-red: map.get($pkt-colors, brand-red-600),
  surface-default-yellow: map.get($pkt-colors, brand-yellow-500),
  surface-strong-beige: map.get($pkt-colors, brand-dark-beige-1000),
  surface-strong-blue: map.get($pkt-colors, brand-blue-1000),
  surface-strong-dark-blue: map.get($pkt-colors, brand-dark-blue-1000),
  surface-strong-dark-green: map.get($pkt-colors, brand-dark-green-1000),
  surface-strong-gray: map.get($pkt-colors, brand-neutrals-200),
  surface-strong-green: map.get($pkt-colors, brand-green-1000),
  surface-strong-light-green: map.get($pkt-colors, brand-light-green-1000),
  surface-strong-red: map.get($pkt-colors, brand-red-1000),
  surface-strong-yellow: map.get($pkt-colors, brand-yellow-1000),
  surface-subtle-light-blue: map.get($pkt-colors, brand-blue-200),
  surface-subtle-light-red: map.get($pkt-colors, brand-red-100),
  surface-subtle-pale-blue: map.get($pkt-colors, brand-blue-100),
  surface-subtle-white: map.get($pkt-colors, brand-neutrals-white),
  // Text
  text-body-dark: map.get($pkt-colors, brand-dark-blue-1000),
  text-body-default: map.get($pkt-colors, brand-dark-blue-1000),
  text-body-light: map.get($pkt-colors, brand-neutrals-white),
  text-placeholder: map.get($pkt-colors, grays-gray-600),
  text-action-disabled: map.get($pkt-colors, grays-gray-600),
  text-action-active: map.get($pkt-colors, brand-warm-blue-1000),
  text-action-hover: map.get($pkt-colors, brand-warm-blue-1000),
  text-action-normal: map.get($pkt-colors, brand-dark-blue-1000)
) !default;
```

## CSS-variabler

Disse fargene gjøres tilgjengelig i frontend med et prefix `--pkt-color`, som [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties).

```css
:root {
  --pkt-color-brand-dark-beige-1000: #d0bfae;
  --pkt-color-brand-light-beige-1000: #f8f0dd;
  --pkt-color-brand-blue-1000: #6fe9ff;
}

/* Brukes enkelt der du ønsker */
.eksempel {
  background: var(--pkt-color-brand-dark-beige-1000);
}
```

## CSS-hjelpeklasser

Fargene er også tilgjengelige som hjelpeklasser i CSS. Disse kan brukes direkte i HTML. De forskjellige fargene er tilgjengelige som klasser med prefikset `pkt-color-bg-`, `pkt-color-txt-` og `pkt-color-border-` etterfulgt av fargenavnet. Disse klassene kan brukes for både brandfarger og semantiske farger. For de semantiske fargene ser muligens klassene litt rare ut, men dette er et resultat av at alt er automatisk generert ut fra alle tilgjengelige farger.

```html
<div class="pkt-color-bg-surface-default-faded-green">
  <p class="pkt-color-txt-text-body-dark">Dette er en tekst</p>
  <aside class="pkt-color-border-border-green">Sidetekst</aside>
</div>
```

## SCSS funksjon

Du kan også ta i bruk farge-stilene slik:

```scss
@use "sass:map";
@use "@oslokommune/punkt-css/scss/abstracts/variables";

.wrapper {
  background-color: map.get(variables.$pkt-colors, "brand-red-1000");
}
```

## Kontrast

Alle farger bør testes for kontrast ved å bruke en online kontrastkontroll for å sikre at den oppfyller WCAG AA-krav for tilgjengelighet. Dette kan du gjøre via plugins i Figma, på nett eller du kan ta i bruk kontrastsjekkeren under.

<ContrastChecker client:only="react" />

## Tilgjengelighet for fargeblinde

Det er en god idé å teste fargene du planlegger å bruke med en fargeblindesimuleringsapp, for eksempel Color Oracle. Du kan bruke simuleringen til å justere fargekombinasjonene for å være tilgjengelige.