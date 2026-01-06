# Hjelpeklasser

**Generated**: 2025-11-06T10:52:48.973989
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/grunnleggende/ressurser/hjelpeklasser.mdx`

---


# Hjelpeklasser

<Lead contributeBox={false}>
  Hjelpeklasser er CSS-klasser som er laget for gjenbruk på tvers av prosjektet
  ditt og kan brukes til å raskt og enkelt legge til stil eller funksjonalitet
  som du har behov for.
</Lead>

Oversikt over våre hjelpeklasser:

| Type              | Klassenavn                                    | Modifier / Helper                                     | Beskrivelse                                                 |
| ----------------- | --------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------- |
| Container         | .pkt-container                                | `--full`,<br />`{--breakpoint}`,<br />`{--alignment}` |
| Synlighet         | .pkt-show, .pkt-hide                          | `-{synlighet}-{breakpoint}-up`                        |                                                             |
| Tekstjustering    | .pkt-txt-start, .pkt-txt-center, .pkt-txt-end |                                                       |                                                             |
| Screenreader only | .pkt-sr-only                                  |                                                       | Innholdet blir skjult visuelt, men kan leses av skjermleser |
| Avkortning        | .pkt-truncate-text                            |                                                       | Krever `display: inline-block` eller `display: block`       |

## Container

Vår `pkt-container` er en CSS-klasse som brukes til å definere en innkapslet boks eller beholder for innholdet på nettsider. Den er spesielt nyttig for responsivt design, da den hjelper til med å justere og begrense innholdet til bestemte skjermstørrelser og gi riktig luft rundt innholdet. Dette bidrar til å opprettholde et ryddig layout og kan begrense innholdet til en bestemt bredde.

For å bruke `container` klassen, legger du til klassenavnet `pkt-container` på HTML-elementet du vil ha som container for innholdet.

For eksempel:

```html
<div class="pkt-container">
  <!-- Innholdet ditt her -->
</div>
```

En container med full bredde:

```html
<div class="pkt-container pkt-container--full">
  <!-- Innholdet ditt her -->
</div>
```

En container med justering til venstre, høyre eller sentrert:

```html
<div class="pkt-container pkt-container--left">
  <!-- Innholdet ditt her -->
</div>

<div class="pkt-container pkt-container--center">
  <!-- Innholdet ditt her -->
</div>

<div class="pkt-container pkt-container--right">
  <!-- Innholdet ditt her -->
</div>
```

En responsiv container med forskjellige bredder basert på skjermstørrelser:

```html
<div class="pkt-container pkt-container--phablet">
  <!-- Innholdet ditt her -->
</div>

<div class="pkt-container pkt-container--tablet">
  <!-- Innholdet ditt her -->
</div>

<div class="pkt-container pkt-container--laptop">
  <!-- Innholdet ditt her -->
</div>
```

Se våre [breakpoints her](/ressurser/breakpoints).

## Synlighet

Bruk `pkt-hide` for å skjule eller `pkt-show`for å gjøre elementer synlig. Disse kan brukes i kombinasjon med breakpoints.
`-{synlighet}-{breakpoint}-up` indikerer at synligheten av elementet vil endre seg basert på skjermstørrelsen. For eksempel, `.pkt-hide-md-up` betyr at elementet vil være skjult på medium skjermer og større.

```html
<!-- Skjul innholdet fra tablet og opp -->
<p class="pkt-hide-tablet-up">...</p>

<!-- Vis innholdet fra phablet og opp -->
<p class="pkt-hide pkt-show-phablet-up">...</p>
```

## Tekstjustering

Juster teksten, eksempel:

```html
<p class="pkt-txt-start">Venstrejustert tekst.</p>
<p class="pkt-txt-center">Senterjustert tekst.</p>
<p class="pkt-txt-end">Høyrejustert tekst.</p>
```

## Vis kun for skjermlesere

`pkt-sr-only` skjuler innholdet visuelt, men gjør det tilgjengelig for skjermlesere. Dette er nyttig for å gi tilgjengelighet til innhold som ikke skal vises på skjermen, men som er viktig for personer med nedsatt syn eller som bruker skjermlesere.

```html
<h2 class="pkt-sr-only">Tittel for skjermlesere</div>
```

## Farger

Vi har hjelpeklasser for bakgrunn, tekstfarge og border for alle våre farger. Les mer om [fargenes hjelpeklasser her](/ressurser/colors/kode#css-hjelpeklasser).

## Avkorting

Avkorter teksten som overskrider breddeområdet til elementet.
Krever `display: inline-block` eller `display: block` for å fungere som forventet.

```html
<div class="pkt-row">
  <div class="pkt-col-4 pkt-truncate-text">
    Oslo Origo er en kommunal etat i Oslo kommune, opprettet 1. januar 2020.
  </div>
</div>
```