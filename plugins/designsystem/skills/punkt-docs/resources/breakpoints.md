# Breakpoints

**Generated**: 2025-11-06T10:52:48.971587
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/grunnleggende/ressurser/breakpoints.mdx`

---


# Breakpoints

<Lead contributeBox={false}>
  Breakpoints er størrelser som avgjør hvordan den responsive layouten oppfører
  seg på tvers av enheter og skjermstørrelser.
</Lead>

- **Breakpoints** er kjernen i responsiv design.
- Lag **mobil først design** ved hjelp av media queries.
- Gjør det **enkelt** å skrive media queries med navngitte breakpoints eller tilpassede verdier i rem.

Det er 6 standard breakpoints tilgjengelig.

| Breakpoint | Dimensjon     | Pixler      |
| :--------- | :------------ | :---------- |
| mobile     | opp til 36rem | ~576px      |
| phablet    | fra 36rem     | fra ~576px  |
| tablet     | fra 48rem     | fra ~768px  |
| tablet-big | fra 64rem     | fra ~1024px |
| laptop     | fra 80rem     | fra ~1280px |
| desktop    | fra 100rem    | fra ~1600px |

## Figma

I Figma vil du ha tilgang på 7 ulike grids for størrelser fra mobil til desktop.
I desktop varianten finner vi to versjoner, i Origo har vi ulike behov derfor finner du en variant for admin-panel og nettsidene. Når siden går over 1600px anbefaler vi at sidene av griden får hvit luft/spacing. I

Disse størrelsene finnes i Figma:

| Type               | Dimensjon | Kolonner |
| :----------------- | :-------- | :------- |
| Adminpanel Desktop | 1600px    | 12       |
| Desktop            | 1600px    | 12       |
| Laptop             | 1280px    | 12       |
| Tablet-big         | 1024px    | 8        |
| Tablet             | 768px     | 8        |
| Phablet            | 576px     | 8        |
| Mobile             | 360px     | 4        |

## Variabler

Breakpointsene er tilgjengelige som et Sass map i `abstracts/variables/_breakpoints.scss`.

```scss
$breakpoints: (
  "mobile": 0,
  "phablet": 36rem /* ~576px */,
  "tablet": 48rem /* ~768px */,
  "tablet-big": 64rem /* ~1024px */,
  "laptop": 80rem /* ~1280px */,
  "desktop": 100rem /* ~1600px */,
) !default;
```

## SCSS mixin

Det finnes ulike media queries tilgjengelig for bruk ved bruk av SCSS mixin.

### Min-width

Dette er den vanligste måten å bruke media queries på i Punkt sine Sass-filer.

```scss
@use '@oslokommune/punkt-css/scss/abstracts/mixins/breakpoints' as *;

@include bp('mobile-up') {
  // Unødvendig, tar alle skjermstørrelser
  ...;
}
@include bp('phablet-up') { /* 576 og opp */
  ...;
}
@include bp('tablet-up') { /* 768px og opp */
  ...;
}
@include bp('tablet-big-up') { /* 1024px og opp */
  ...;
}
@include bp('laptop-up') { /* 1280px og opp */
  ...;
}
@include bp('desktop-up') { /* 1600px og opp */
  ...;
}

// Eksempel
.eksempel {
  width: 100%;

  @include bp('tablet-up') {
    width: $pageWidth;
  }
}
```

### Enkeltbreakpoints

Det er også mulighet for å angi et enkelt område av skjermstørrelse.

```scss
@use "@oslokommune/punkt-css/scss/abstracts/mixins/breakpoints" as *;

@include bp('mobile') { /* opp til 575px */
  ...;
}
@include bp('phablet') { /* 576 til 767px */
  ...;
}
@include bp('tablet') { /* 768px til 1023px */
  ...;
}
@include bp('tablet-big') { /* 1024px til 1279px */
  ...;
}
@include bp('laptop') { /* 1280px til 1599px */
  ...;
}
@include bp('desktop') { /* 1600px og opp */
  ...;
}

// Eksempel
.eksempel {
  width: 100%;

  @include bp('tablet') {
    width: $pageWidth;
  }
}
```