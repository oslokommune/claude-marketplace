# Grid

**Generated**: 2025-11-06T10:52:48.973482
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/grunnleggende/ressurser/grid.mdx`

---


# Grid

<Lead contributeBox={false}>
  Grid brukes til å justere sideelementer basert på sekvenserte kolonner og
  rader. Vi bruker denne kolonnebaserte strukturen for å plassere tekst, bilder
  og funksjoner på en konsekvent måte gjennom hele designet.
</Lead>

Her er tre grunner til hvorfor du bør bruke grid:

**Konsekvens** – Grid bygger oppsettet til grensesnittet og bidrar til konsekvente løsninger ved hjelp av element plassering. Med grid sikrer vi bedre og enklere skanning av komponenter på skjermen, som bidrar til en positiv brukeropplevelse.

**Responsiv** – Ved hjelp av grid vil det være lettere å gjøre løsningen responsiv, samtidig som du beholder en konsekvent layout.

**Raskere designprosess** Grid gir designere retningslinjer for proporsjoner mellom elementer, som avstand og marginer. Det forenkler arbeidet og redusere muligheten for feil. Et felles utgangspunkt rundt grid letter samarbeidet til både designere og utviklere.

![grid-gif](/assets/grid-gif.gif)

## Hvordan bruke grid?

<CodeExample>
  <GridContainer client:load className="pkt-grid">
    <div class="pkt-cell pkt-cell--span3">.pkt-cell pkt-cell--span3</div>
    <div class="pkt-cell pkt-cell--span3">.pkt-cell pkt-cell--span3</div>
    <div class="pkt-cell pkt-cell--span3">.pkt-cell pkt-cell--span3</div>
    <div class="pkt-cell pkt-cell--span3">.pkt-cell pkt-cell--span3</div>
  </GridContainer>
</CodeExample>

```html
<section className="pkt-grid">
  <div class="pkt-cell pkt-cell--span3">.pkt-cell pkt-cell--span3</div>
  <div class="pkt-cell pkt-cell--span3">.pkt-cell pkt-cell--span3</div>
  <div class="pkt-cell pkt-cell--span3">.pkt-cell pkt-cell--span3</div>
  <div class="pkt-cell pkt-cell--span3">.pkt-cell pkt-cell--span3</div>
</section>
```

<strong>Container</strong>

Grid containeren er brukt til å holde på, gi luft til og plassere innholdet i en layout på siden. Denne har klassen `pkt-grid`. Default bredde på containeren er 100%.

Dersom du ønsker spacing på venstre og høyre side av containeren kan du enten bruke modifier `pkt-grid--padding` (16px på små skjermer og 32px på store) eller bruke [spacing-hjelpeklassene](/ressurser/spacing).

<strong>Celler</strong>

Med gridsystemet angir man ikke kolonner og rader, men celler.
En grid-celle er et rom du plasserer ditt innhold inni. Cellen fungerer som en celle i en tabell eller et regneark. Cellen fyller plassen på raden såfremt det er plass, hvis ikke faller de automatisk ned til neste rad. Cellene i vårt gridsystem skal ha klassen `pkt-cell`.

Hver celle tar opp 1/12 plass av GridContaineren, bruk modifiers om du ønsker andre bredder.

Vi bruker en 12 kolonnes gridsystem basert på CSS Grid Layout. Det anbefales sterkt å studere lenkene i bunnen av siden for å lære mer om CSS Grid Layout

<CodeExample noHorizontalPadding>
  <GridContainer client:load className="pkt-grid" show-guide>
    <div class="pkt-cell pkt-cell--span11">11</div>
    <div class="pkt-cell">1</div>
    <div class="pkt-cell pkt-cell--span10">10</div>
    <div class="pkt-cell pkt-cell--span2">2</div>
    <div class="pkt-cell pkt-cell--span9">9</div>
    <div class="pkt-cell pkt-cell--span3">3</div>
    <div class="pkt-cell pkt-cell--span8">8</div>
    <div class="pkt-cell pkt-cell--span4">4</div>
    <div class="pkt-cell pkt-cell--span7">7</div>
    <div class="pkt-cell pkt-cell--span5">5</div>
    <div class="pkt-cell pkt-cell--span6">6</div>
    <div class="pkt-cell pkt-cell--span6">6</div>
  </GridContainer>
</CodeExample>

## Modifiers og helpers

### pkt-grid

| Type          | Modifier / Helper                                                                                                                                                            | Default            | Beskrivelse                                                               |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------- |
| Bredde        | `--phablet`, `--tablet`, `--tablet-big`, `--laptop`, `--desktop`, `--full`                                                                                                   | `pkt-grid--full`   | Maksbredde på containeren                                                 |
| Justering     | `--left`, `--right`, `--center`                                                                                                                                              | `pkt-grid--center` | Justér container med margins                                              |
| Gutters / Gap | `--gap-{spacing}`, `--colgap-{spacing}`, `--rowgap-{spacing}`, `--gap-{spacing}-{breakpoint}-up`, `--colgap-{spacing}-{breakpoint}-up`, `--rowgap-{spacing}-{breakpoint}-up` | 16px / 32px        | Les mer om gap under.                                                     |
| Padding       | `--padding`                                                                                                                                                                  | ingen              | Legger til 16px / 32px padding på venstre og høyre side av grid-container |
| Margins       | `mx-size-16`, `mx-size-32-tablet-up`                                                                                                                                         | auto               | Bruk våre hjelpeklasser for spacing                                       |

## pkt-cell

| Type      | Modifier / Helper                                                          | Default              | Beskrivelse                                                |
| --------- | -------------------------------------------------------------------------- | -------------------- | ---------------------------------------------------------- |
| Bredde    | `--span{n}`, `--span{n}-{breakpoint}-up`                                   | `pkt-cell--span1`    | Antall kolonner cellen skal gå over. Span går fra 1 til 12 |
| Justering | `--left`, `--right`, `--center` , `--top`, `--center-vertical`, `--bottom` | `justify-self: auto` | Justér innholdet i celle                                   |

## pkt-gap

Gap er rommet mellom to kolonner, også kalt gutters. Default er disse:

- 16px for visningsområde 767px og smalere.
- 32px for visningsområde 768px og bredere.

| Modifier / Helper                    | Beskrivelse                                                               |
| ------------------------------------ | ------------------------------------------------------------------------- |
| `--gap-{spacing}`                    | Gap mellom kolonner og rader. Alle verdier definert i spacing er tillatt. |
| `--colgap-{spacing}`                 | Gap mellom kolonner. Alle verdier definert i spacing er tillatt.          |
| `--rowgap-{spacing}`                 | Gap mellom rader. Alle verdier definert i spacing er tillatt.             |
| `--gap-{spacing}-{breakpoint}-up`    | Gap mellom kolonner og rader fra et breakpoint og oppover.                |
| `--colgap-{spacing}-{breakpoint}-up` | Gap mellom kolonner fra et breakpoint og oppover.                         |
| `--rowgap-{spacing}-{breakpoint}-up` | Gap mellom rader fra et breakpoint og oppover.                            |

## Eksempler

### Responsiv grid

Tabellen under illustrerer hvordan `pkt-grid` oppfører seg ved ulike breakpoints.
Dersom vi ønsker at innholdet skal skalere med skjermbredden jobber vi med et `fluid grid system`. Responsivt design benytter seg av denne måten å designe på for å utnytte den tilgjengelige skjermplassen på en hvilken som helst enhet. Fluid betyr at kolonnebredden hele tiden vil øke/minke i størrelse i det visningsområdet endrer seg. Gap og marginer forblir samme størrelse.

|                        | Mobile | Phablet | tablet | tablet-big | laptop | desktop |
| :--------------------- | :----- | :------ | :----- | :--------- | :----- | :------ |
| `pkt-grid--phablet`    | 100%   | 36rem   | 36rem  | 36rem      | 36rem  | 36rem   |
| `pkt-grid--tablet`     | 100%   | 100%    | 48rem  | 48rem      | 48rem  | 48rem   |
| `pkt-grid--tablet-big` | 100%   | 100%    | 100%   | 64rem      | 64rem  | 64rem   |
| `pkt-grid--laptop`     | 100%   | 100%    | 100%   | 100%       | 80 rem | 80rem   |
| `pkt-grid--desktop`    | 100%   | 100%    | 100%   | 100%       | 100%   | 100rem  |
| `pkt-grid--full`       | 100%   | 100%    | 100%   | 100%       | 100%   | 100%    |

“A fluid container will stretch to the outer boundaries of its outermost parent. Often, this is the browser, but in cases where a fluid grid is inside of a container between the browser and itself, it can still be fluid and 100% the width of its parent, but maybe not the browser.”

<CodeExample noHorizontalPadding>
  <GridContainer client:load className="pkt-grid pkt-grid--phablet" show-guide>
    <div class="pkt-cell pkt-cell--span12">.pkt-grid--phablet</div>
  </GridContainer>
  <GridContainer client:load className="pkt-grid pkt-grid--tablet" show-guide>
    <div class="pkt-cell pkt-cell--span12">.pkt-grid--tablet</div>
  </GridContainer>
  <GridContainer
    client:load
    className="pkt-grid pkt-grid--tablet-big"
    show-guide
  >
    <div class="pkt-cell pkt-cell--span12">.pkt-grid--tablet-big</div>
  </GridContainer>
  <GridContainer client:load className="pkt-grid pkt-grid--laptop" show-guide>
    <div class="pkt-cell pkt-cell--span12">.pkt-grid--laptop</div>
  </GridContainer>
  <GridContainer client:load className="pkt-grid pkt-grid--desktop" show-guide>
    <div class="pkt-cell pkt-cell--span12">.pkt-grid--desktop</div>
  </GridContainer>
  <GridContainer client:load className="pkt-grid pkt-grid--full" show-guide>
    <div class="pkt-cell pkt-cell--span12">.pkt-grid--full</div>
  </GridContainer>
</CodeExample>

```html
<section className="pkt-grid pkt-grid--phablet">
  <div class="pkt-cell pkt-cell--span12">.pkt-grid--phablet</div>
</section>
```

#### Justering av grid

Dersom containeren ikke tar full bredde, er det mulighet til å justere containeren til venstre, midt eller høyre. Default er venstre.

<CodeExample noHorizontalPadding>
  <GridContainer
    client:load
    className="pkt-grid pkt-grid--phablet pkt-grid--left"
    show-guide
  >
    <div class="pkt-cell pkt-cell--span12">.pkt-grid--left</div>
  </GridContainer>
  <GridContainer client:load className="pkt-grid pkt-grid--phablet" show-guide>
    <div class="pkt-cell pkt-cell--span12">Default center</div>
  </GridContainer>
  <GridContainer
    client:load
    className="pkt-grid pkt-grid--phablet pkt-grid--right"
    show-guide
  >
    <div class="pkt-cell pkt-cell--span12">pkt-grid--right</div>
  </GridContainer>
</CodeExample>

```html
<section className="pkt-grid pkt-grid--phablet pkt-grid--left">
  <div class="pkt-cell pkt-cell--span12">.pkt-grid--left</div>
</section>
```

### Responsive celler

Lag en responsive layout ved å angi hvor stor andel av siden innholdet skal ha på ulike skjermstørrelser.

- Full bredde på mobil.
- 4 celler fordelt på to rader fra tablet og opp

Resize nettleservinduet for å se hvordan det oppfører seg.

<CodeExample noHorizontalPadding>
  <GridContainer client:load className="pkt-grid" show-guide>
    <div class="pkt-cell pkt-cell--span12 pkt-cell--span6-tablet-up">1</div>
    <div class="pkt-cell pkt-cell--span12 pkt-cell--span6-tablet-up">2</div>
    <div class="pkt-cell pkt-cell--span12 pkt-cell--span6-tablet-up">3</div>
    <div class="pkt-cell pkt-cell--span12 pkt-cell--span6-tablet-up">4</div>
  </GridContainer>
</CodeExample>

```html
<section className="pkt-grid">
  <div class="pkt-cell pkt-cell--span12 pkt-cell--span6-tablet-up">1</div>
  <div class="pkt-cell pkt-cell--span12 pkt-cell--span6-tablet-up">2</div>
  <div class="pkt-cell pkt-cell--span12 pkt-cell--span6-tablet-up">3</div>
  <div class="pkt-cell pkt-cell--span12 pkt-cell--span6-tablet-up">4</div>
</section>
```

#### Automatisk wrapping

I dette eksempelet går ikke breddene opp i 12, og de wrappes derfor automatisk ned på linjen under. De to siste cellene faller dog fint på plass.

<CodeExample noHorizontalPadding>
  <GridContainer client:load className="pkt-grid" show-guide>
    <div class="pkt-cell pkt-cell--span6">6 kolonner</div>
    <div class="pkt-cell pkt-cell--span7">7 kolonner</div>
    <div class="pkt-cell pkt-cell--span8">8 kolonner</div>
    <div class="pkt-cell pkt-cell--span4">4 kolonner</div>
  </GridContainer>
</CodeExample>

```html
<section className="pkt-grid">
  <div class="pkt-cell pkt-cell--span6">6 kolonner</div>
  <div class="pkt-cell pkt-cell--span7">7 kolonner</div>
  <div class="pkt-cell pkt-cell--span8">8 kolonner</div>
  <div class="pkt-cell pkt-cell--span4">4 kolonner</div>
</section>
```

### Responsiv gap/gutter

En gap/ gutter på 32px på tablet og oppover. 16px under.

<CodeExample>
  <GridContainer
    client:load
    className="pkt-grid pkt-grid--gap-size-16 pkt-grid--gap-size-32-tablet-up"
  >
    <div class="pkt-cell pkt-cell--span3">
      .pkt-grid--gap-size-16 pkt-grid--gap-size-32-tablet-up
    </div>
    <div class="pkt-cell pkt-cell--span3">
      .pkt-grid--gap-size-16 pkt-grid--gap-size-32-tablet-up
    </div>
    <div class="pkt-cell pkt-cell--span3">
      .pkt-grid--gap-size-16 pkt-grid--gap-size-32-tablet-up
    </div>
    <div class="pkt-cell pkt-cell--span3">
      .pkt-grid--gap-size-16 pkt-grid--gap-size-32-tablet-up
    </div>
  </GridContainer>
</CodeExample>

```html
<section
  className="pkt-grid pkt-grid--gap-size-16 pkt-grid--gap-size-32-tablet-up"
>
  <div class="pkt-cell pkt-cell--span3">
    .pkt-grid--gap-size-16 pkt-grid--gap-size-32-tablet-up
  </div>
  <div class="pkt-cell pkt-cell--span3">
    .pkt-grid--gap-size-16 pkt-grid--gap-size-32-tablet-up
  </div>
  <div class="pkt-cell pkt-cell--span3">
    .pkt-grid--gap-size-16 pkt-grid--gap-size-32-tablet-up
  </div>
  <div class="pkt-cell pkt-cell--span3">
    .pkt-grid--gap-size-16 pkt-grid--gap-size-32-tablet-up
  </div>
</section>
```

#### Les mer

- [MDN - CSS Grid Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
- [Css-tricks - A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [CSS - In Real Life - Debugging CSS Grid Part 2: What the Fr(action)?](https://css-irl.info/debugging-css-grid-part-2-what-the-fraction/)
- [CSS - In Real Life - Is it Time to Ditch the Design Grid?](https://css-irl.info/is-it-time-to-ditch-the-design-grid/)

### Universell utforming

- [Utforming og presentasjon](https://www.uutilsynet.no/veiledning/utforming-og-presentasjon/227)
- [Visningsretning](https://www.uutilsynet.no/veiledning/134-visningsretning/1237)