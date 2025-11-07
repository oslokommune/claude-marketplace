# Disabled states

**Generated**: 2025-11-06T10:52:48.981983
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/god-praksis/disabled-states/index.mdx`

---

**Category**: god-praksis

**Description**: Bruk av deaktivert innhold kan være utfordrende for brukere når det gjelder forståelse og tilgjengelighet. Av denne grunn anbefaler vi å unngå det så mye som mulig.



Designere benytter seg oftest av deaktivert innhold når de skal…

- Indikere at et valg ikke er relevant for øyeblikket, men kan bli viktig senere.
- Signalisere at et skjema ennå ikke er fullført eller at man må fylle ut noe annet først.
- Markere at et element ikke kan endres («read only»).

<ImageWrapper
  backgroundColor="white"
  caption="Eksempel på deaktivert innhold i form av inputfelter og knapper fra Punkt"
>
  <img
    src="/assets/god-praksis/disabled-states/disabled-1.svg"
    alt="Deaktivert innhold"
    aria-hidden="true"
  />
</ImageWrapper>

## Hvorfor er deaktivert innhold problematisk?

Deaktiverte tilstander kan medføre utfordringer for brukere av ulike grunner. Vanligvis har de lav kontrast og bruker fargeendringer som den eneste visuelle indikasjonen for å kommunisere at elementet er deaktivert. Dette kan skape problemer ikke bare for personer med nedsatt synsevne, men også for de som bruker enheter i omgivelser med sterkt lys eller som har dårlige skjermer.

Dersom vi designer en deaktivert tilstand som faktisk oppfyller kontrastkravene, er det en stor risiko for at brukerne fremdeles oppfatter elementet som aktivt. Dette kan føre til forvirring når de prøver å interagere med elementet og ikke forstår hvorfor det ikke fungerer som forventet.

En annen utfordring er at grunnen til at et element er deaktivert vanligvis ikke blir eksplisitt forklart - vi gir sjelden en forklaring på hvorfor nettopp dette elementet er deaktivert. Dette krever at brukeren gjør gjetninger, som kan føre til feilaktige antagelser.

Det er også verdt å merke seg at deaktiverte tilstander ikke mottar tastaturfokus, noe som kan føre til at brukere som er avhengige av tastatur eller skjermleser går glipp av dem.

<ContentSection backgroundColor="beige">
## Mulige løsninger og alternativer

Det er flere mulige alternative løsninger til deaktivert innhold, blant annet:

### Skjemavalidering

Tenker du på å bruke en deaktivert sende-knapp som en form for skjemavalidering? Det er bedre å validere skjemaet inline som vanlig, la knappen være aktiv, og vise en feilmelding når brukeren prøver å sende inn skjemaet.

<ImageWrapper>
  <img
    src="/assets/god-praksis/disabled-states/disabled-2.svg"
    alt="Validering i skjema."
    aria-hidden="true"
  />
</ImageWrapper>

### Ikke-aktuelle valg

Hvis et valg ikke er relevant, er det bedre å fjerne valget helt i stedet for å deaktivere det. Gi gjerne brukeren informasjon om hvorfor valget ikke er tilgjengelig.

### Skrivebeskyttet innhold

I stedet for å deaktivere skrivebeskyttede inndatafelt, bør du bruke vanlig tekst. Du kan også legge til ekstra informasjon som forklarer hvorfor informasjonen ikke kan endres.

<ExampleComparison
  goodExample={{
    image: "/assets/god-praksis/disabled-states/disabled-3.svg",
    imgAlt: "Gjør slik – Skriv vanlig tekst for skrivebeskyttet innhold",
    caption: "Skriv vanlig tekst for skrivebeskyttet innhold",
  }}
  badExample={{
    image: "/assets/god-praksis/disabled-states/disabled-4.svg",
    imgAlt: "Unngå – deaktiverte inputfelt for skrivebeskyttet innhold",
    caption: "Unngå deaktiverte inputfelt for skrivebeskyttet innhold",
  }}
/>

</ContentSection>

## Dersom du likevel må benytte deaktivert innhold

Hvis du likevel må benytte deg av deaktivert innhold, er det viktig å ta hensyn til følgende:

### Sikre universell oppfatning og forståelse

Sørg for at komponenten fremdeles kan oppfattes og forstås av alle brukere. Dette inkluderer personer med nedsatt synsevne, de som bruker enheter med dårlig skjermkvalitet, de som befinner seg i sterkt lys, samt personer med ulike nivåer av datakunnskap og kognitiv funksjonsnedsettelse.

<ImageWrapper caption="I Punkt har teksten høy nok kontrast til å møte AA-kravet - 5.45:1">
  <img
    src="/assets/god-praksis/disabled-states/disabled-5.svg"
    alt="Kontrastkrav i Punkt."
    aria-hidden="true"
  />
</ImageWrapper>

### Gi tilleggsinformasjon for skjermlesere

Gi tilleggsinformasjon for skjermlesere ved å legge til en span med klassen `pkt-sr-only` , eller bruke `wai-aria` attributter:

```html
<span class="pkt-sr-only">
  Denne funksjonaliteten er deaktivert på grunn av...
</span>

<button
  aria-disabled="true"
  aria-label="Denne funksjonaliteten er deaktivert på grunn av..."
>
  Klikk her
</button>
```

### Unngå gjettearbeid

Forsikre deg om at brukeren ikke trenger å gjette for å forstå hvorfor et element er deaktivert. Gi klare og forståelige opplysninger om hvorfor valget er deaktivert. Dette bør være tilgjengelig uten at brukeren må sveve musen over elementet (hover).

### Ta i bruk flere visuelle metoder

I tillegg til farge, bør du bruke andre grafiske elementer for å tydelig skille mellom aktive og inaktive valg. Dette vil bidra til bedre forståelse for alle brukere, uavhengig av deres visuelle evner eller enhetene de bruker.

<ImageWrapper caption="Eksempel fra Team Booking sin admin-løsning, der man tydelig ser hva man kan gjøre for å aktivere de deaktiverte feltene.">
  <img
    src="/assets/god-praksis/disabled-states/disabled-6.svg"
    alt="Kontrastkrav i Punkt."
    aria-hidden="true"
  />
  <img
    src="/assets/god-praksis/disabled-states/disabled-7.svg"
    alt="Kontrastkrav i Punkt."
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="beige">
## Les mer

- [NAV: Deaktiverte tilstander](https://aksel.nav.no/god-praksis/artikler/deaktiverte-tilstander)
- [UX Planet: Disabled buttons in a user interface](https://uxplanet.org/disabled-buttons-in-user-interface-4dafda3e6fe7)
- [Smashing Magazine: Frustrating design patterns - disabled buttons](https://www.smashingmagazine.com/2021/08/frustrating-design-patterns-disabled-buttons/)
- [Carbon Designsystem: Disabled states](https://carbondesignsystem.com/patterns/disabled-states/)
- [UX Knowledge Base: The disabled state in UI design](https://uxknowledgebase.com/the-disabled-state-in-ui-design-8c091d72868)

</ContentSection>