# Spacing

**Generated**: 2025-11-06T10:52:48.976229
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/grunnleggende/ressurser/spacing.mdx`

---


# Spacing

<Lead contributeBox={false}>
  Spacing er en bestemt mengde luft i komponenten og mellom elementer. Ved bruk
  av spacing vil man bidra til et mer konsekvent design.
</Lead>

Spacing skalaene til Punkt går fra 2px til 104px og brukes i alle komponentene vi lager i designsystemet. Bruk spacing når du bygger individuelle komponenter til dine skisser.

Alle våre elementer er utformet etter en 8-punkts skala med en grunnlinje på 8px.
8-punkts skalaen er ment å sikre visuell konsekvens og balanse på tvers av alle elementer. Elementhøyder, bredder, padding og margin skal følge en skala på 8.

## Variabler

Alle spacing-verdiene er tilgjengelige som et Sass map i `_settings.scss`.

```scss
$spacing: (
  "size-0": 0rem,
  "size-2": 0.125rem,
  "size-4": 0.25rem,
  "size-8": 0.5rem,
  "size-12": 0.75rem,
  "size-16": 1rem,
  "size-24": 1.5rem,
  "size-32": 2rem,
  "size-40": 2.5rem,
  "size-64": 4rem,
  "size-104": 6.5rem,
) !default;
```

## CSS-klasser

Punkt inkluderer hjelpeklasser for enkelt å sette responsiv margin og padding for å tilpassse et elements utseende.

Hjelpeklassene er bygget opp slik:

`{type}{retning}-{størrelse}`

I tillegg kan du legge på fra hvilket breakpoint det gjelder fra (frivillig):

`{type}{retning}-{størrelse}--{breakpoint}-up`

Lær mer om verdier for breakpoints [på siden som omhandler breakpoints](/ressurser/breakpoints).

| Navn      | Mulige verdier         |
| :-------- | :--------------------- |
| Type      | **m** for margin       |
|           | **p** for padding      |
| Retning   | **t** for topp         |
|           | **r** for høyre        |
|           | **b** for bunn         |
|           | **l** for venstre      |
|           | **x** for horisontalt  |
|           | **y** for vertikalt    |
| Størrelse | **size-0** for 0px     |
|           | **size-2** for 2px     |
|           | **size-4** for 4px     |
|           | **size-8** for 8px     |
|           | **size-12** for 12px   |
|           | **size-16** for 16px   |
|           | **size-24** for 24px   |
|           | **size-32** for 32px   |
|           | **size-40** for 40px   |
|           | **size-64** for 64px   |
|           | **size-104** for 104px |

### Eksempel

```html
<!-- Margin bunn settes til 24px (1.5rem) -->
<p class="mb-size-24">Margin bunn</p>

<!--
margin til høyre settes til 0
padding top settes til 24px (1.5rem)
-->
<p class="mr-size-0 pt-size-24">margin høyre og padding topp</p>

<!--
padding settes til 12px (0.75rem) til venstre og høyre
Ved breakpoint laptop og større endres dette til 24px (1.5rem)
-->
<p class="px-size-12 px-size-24--laptop-up">Horisontal padding</p>
```

## SCSS funksjon

Du kan også ta i bruk spacing-stilene med mixin `get-text`:

```scss
@use "sass:map";
@use "@oslokommune/punkt-css/scss/abstracts/variables";

.wrapper {
  padding: map.get(variables.$spacing, "size-24");
}
```