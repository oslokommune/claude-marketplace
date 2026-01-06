# 17 tips for å lage et godt skjema

**Generated**: 2025-11-06T10:52:48.983673
**Git Commit**: 05685b33
**Source Files**:
- `apps/docs-astro/src/pages/god-praksis/skjemadesign/index.mdx`

---

**Category**: god-praksis

**Description**: Vi har samlet 17 retningslinjer du bør ta stilling til når du ønsker å designe eller bygge et godt skjema. Vi anbefaler også å ta en titt på lenkene nederst på siden.





Skjemaer brukes mye hos Origo og i Oslo kommunes løsninger, og bør derfor være konsekvente, 
ryddige og enkle å forstå. Det er mye godt innhold om det å lage bra skjemaer og det er ikke helt 
enkelt.

<PktMessagebox skin="blue" client:only="react" title="">
  <span>
Først og fremst bør du vurdere om du trenger et skjema i det hele tatt. Bruk tid med teamet og 
gjøre innsikt i hva dere trenger å vite, og hva dere skal gjøre med det dere samler inn i skjemaet.
  </span>
</PktMessagebox>

### Innhold:
1. [Skriv en forklarende intro](#1-skriv-en-forklarende-intro)<br/>
2. [Ha alle felter under hverandre på én linje](#2-ha-alle-felter-under-hverandre-på-én-linje)<br/>
3. [Alltid bruk label og plasser den over tekstfeltet](#3-alltid-bruk-label-og-plasser-den-over-tekstfeltet)<br/>
4. [Ikke bruk plassholdertekst som hjelpetekst eller label](#4-ikke-bruk-plassholdertekst-som-hjelpetekst-eller-label)<br/>
5. [Hjelp brukeren på vei med gode hjelpetekster](#5-hjelp-brukeren-på-vei-med-gode-hjelpetekster)<br/>
6. [Lag grupper - plasser det som hører sammen, sammen](#6-lag-grupper---plasser-det-som-hører-sammen-sammen)<br/>
7. [Merk det som er valgfritt (eller det som er obligatorisk)](#7-merk-det-som-er-valgfritt-eller-det-som-er-obligatorisk)<br/>
8. [... Men trenger du egentlig å spørre om det?](#8-men-trenger-du-egentlig-å-spørre-om-det)<br/>
9. [Tekstfeltet skal være like bredt som innholdet](#9-tekstfeltet-skal-være-like-bredt-som-innholdet)<br/>
10. [Dropdown/select er ikke alltid det beste valget: prøv heller å liste ut elementene](#10-dropdownselect-er-ikke-alltid-det-beste-valget-prøv-heller-å-liste-ut-elementene)<br/>
11. [Keep it short and sweet!](#11-keep-it-short-and-sweet)<br/>
12. [Er det noe vi kan få gratis? Ja, da burde vi det](#12-er-det-noe-vi-kan-få-gratis-ja-da-burde-vi-det)<br/>
13. [Opt-in, ikke opt-out](#13-opt-in-ikke-opt-out)<br/>
14. [Merk feil tydelig og i sammenheng med der feilen har oppstått](#14-merk-feil-tydelig-og-i-sammenheng-med-der-feilen-har-opptått)<br/>
15. [Ha en tydelig call-to-action](#15-ha-en-tydelig-call-to-action)<br/>
16. [Utviklerne må på banen](#16-utviklerne-må-på-banen)<br/>
17. [Design skjemaet som en samtale!](#17-design-skjemaet-som-en-samtale)<br/>


<ContentSection backgroundColor="subtle-pale-blue">

### 1. Skriv en forklarende intro
Før du i det hele tatt begynner med input-felter og filopplastning kan det være lurt å skrive en kort, 
forklarende intro til skjemaet ditt. Her kan du gjerne beskrive:

- <strong>Hvor langt skjemaet er</strong>, for eksempel hvor mange steg eller hvor lang
  tid det forventes å ta å fylle det ut. På denne måten kan brukeren gjøre en
  vurdering på om de skal fylle ut med en gang, eller vente til de har bedre
  tid.
- <strong>Om de trenger noe for å fylle ut skjemaet</strong>, for eksempel dokumenter,
  filer, bilder, datoer, fødselsnummere eller lignende. På denne måten sikrer du
  at brukeren fyller ut skjemaet ferdig, og ikke må avslutte midt i for å finne
  ytterligere dokumentasjon eller lignende.


<PktMessagebox skin="blue" client:only="react" title="">
  <span>
Obs: Dersom brukeren trenger dokumentasjon for å fylle ut skjemaet, bør du gi brukeren mulighet til å lagre skjemaet underveis 
for å komme tilbake til det senere.
  </span>
</PktMessagebox>

<ImageWrapper caption="Eksempel på introtekst.">
  <img
    src="/assets/god-praksis/skjemadesign/skjemadesign-2.svg"
    alt="Skjema for søknad om redusert barnehagebetaling"
    aria-hidden="true"
  />
</ImageWrapper>

</ContentSection>

### 2. Ha alle felter under hverandre på én linje

Plasser skjemafeltene under hverandre med venstrestilt tekst, med noen unntak (f.eks. postnummer og poststed 
og landskode og telefonnummer).

Prøv å holde skjemaområdet til maks 500 px bredt. Dette gir bedre lesbarhet og gjør det enklere å skanne over 
skjemaet.

<ImageWrapper>
  <img
    src="/assets/god-praksis/skjemadesign/skjemadesign-3.svg"
    alt="Skjema med bredde 500px"
    aria-hidden="true"
  />
</ImageWrapper>

På mobil burde skjemaelementene fylle bredden på siden, men fortsatt holde seg til satt størrelse der vi vet 
lengden på inputteksten.

<ExampleComparison
  goodExample={{
    image: "/assets/god-praksis/skjemadesign/skjemadesign-4.svg",
    imgAlt: "To skjemaer, ett med riktig mengde luft rundt og ett med feil mengde luft rundt",
    caption: "Bruk hele bredden på siden når du har et skjema på mobil",
  }}
  badExample={{
    image: "/assets/god-praksis/skjemadesign/skjemadesign-4-2.svg",
    imgAlt: "To skjemaer, ett med riktig mengde luft rundt og ett med feil mengde luft rundt",
    caption: "Unngå å gjøre skjemaet for smalt eller for bredt for siden på mobil",
  }}
/>


<ContentSection backgroundColor="subtle-pale-blue">

### 3. Alltid bruk label og plasser den over tekstfeltet

Plasser alltid label over tekstfeltet, sammen med eventuell hjelpetekst. Å plassere teksten på venstre side 
gjør det vanskeligere å scanne over skjemaet.

Husk på at en god label:

- Er konsis og konsekvent slik at brukeren skjønner hva som forventes av hen
- Om mulig: kun er 1-3 ord og under 20 bokstaver, inkludert mellomrom
- Ikke har bare store eller bare små bokstaver
- Ikke inneholder kolon

<ExampleComparison
  goodExample={{
    image: "/assets/god-praksis/skjemadesign/skjemadesign-5.svg",
    imgAlt: "Viser riktig bruk av label over tekstfelt",
    caption: "Plasser label og hjelpetekst over tekstfeltet",
  }}
  badExample={{
    image: "/assets/god-praksis/skjemadesign/skjemadesign-5-2.svg",
    imgAlt: "Viser feil bruk av label ved siden av tekstfelt",
    caption: "Unngå å plassere label og hjelpetekst ved siden av eller under tekstfelt",
  }}
/>

</ContentSection>

### 4. Ikke bruk plassholdertekst som hjelpetekst eller label

Tekstfeltet har mulighet for plassholdertekst, men unngå å bruke plassholdertekst med meningsbærende 
eller viktig innhold. Den er nemlig ikke tilgjengelig for skjermlesere og kan skape forvirring for brukeren. 
Gå heller for ledetekst og/eller hjelpetekst.

Prøv generelt å unngå plassholdertekst, vi vet også at folk kan oppleve det som at det allerede er utfylt og 
dermed hopper de over det.

<ExampleComparison
  goodExample={{
    image: "/assets/god-praksis/skjemadesign/skjemadesign-6.svg",
    imgAlt: "Viser label og hjelpetekst over tekstfeltet",
    caption: "Plasser label og hjelpetekst over tekstfeltet",
  }}
  badExample={{
    image: "/assets/god-praksis/skjemadesign/skjemadesign-6-2.svg",
    imgAlt: "o skjemaer, ett med riktig mengde luft rundt og ett med feil mengde luft rundt",
    caption: "Unngå å bruke plassholdertekst som label eller hjelpetekst",
  }}
/>

<ContentSection backgroundColor="subtle-pale-blue">

### 5. Hjelp brukeren på vei med gode hjelpetekster

Hjelpetekstene skal brukes for å gi ytterligere informasjon om hva som forventes av brukeren. Hjelpeteksten 
skal supplere label (ledetekst) og aldri erstatte den.

Teksten skal være kort og konkret, og forklare brukeren hva hen skal gjøre. Det er viktig å vurdere om hjelpetekst 
virkelig er nødvendig, eller kan label forbedres til å være lettere å forstå og dermed fjerne behovet for ekstra forklaring?

I Punkt har vi to typer hjelpetekster: den som skrives rett under label og ekspanderende hjelpetekst, der brukeren 
aktivt må klikke for å få mer informasjon. Ekspanderende hjelpetekst brukes når det er behov for en lengre forklaring 
som går mer i dybden. Ofte holder det med vanlig hjelpetekst over én linje.

Når du skriver hjelpetekster er det greit å...

- Holde teksten kort
- Bruke enkle ord som alle brukere kan forstå
- Unngå faguttrykk og vanskelige ord så langt det er mulig (hvis du må bruke spesialiserte temaer, bør det alltid være 
tilgjengelig hjelpetekst).

Noen ganger kan det også være hjelp i å legge til <i>format og forventet antall direkte i label-teksten</i>.

<ImageWrapper caption="Tre varianter av hjelpetekst.">
  <img
    src="/assets/god-praksis/skjemadesign/skjemadesign-7.svg"
    alt="Skjema med forskjellige typer hjelpetekster"
    aria-hidden="true"
  />
</ImageWrapper>

</ContentSection>

### 6. Lag grupper - plasser det som hører sammen, sammen

Ofte har vi forskjellige temaer (eller kategorier) i et skjema. Derfor er det lurt å gruppére de feltene som hører 
sammen i en gruppe for å gjøre det enklere for brukeren å navigere seg gjennom skjemaet.

En eller flere skjemakomponenter sammen utgjør en skjemaseksjon, og et skjema kan bestå av en eller flere seksjoner.

Du kan enten gruppere gjennom overskrifter og visuell kategorisering, eller dele opp skjemaet i flere steg.


<ImageWrapper caption="To muligheter for gruppering, enten med titler eller med stegviser.">
  <img
    src="/assets/god-praksis/skjemadesign/skjemadesign-8.svg"
    alt="Skjemaer med ulike typer gruppering"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

### 7. Merk det som er valgfritt (eller det som er obligatorisk)

Å markere obligatoriske felter i skjema med en asterisk\* har blitt vanlig, men det kan føre til visuell støy. Det er 
bedre å merke valgfrie felt med "(valgfri/valgfritt)", slik at det er tydeligere for brukerne hvilke felter som må fylles ut. 
Å bruke en asterisk kan være forvirrende for noen. Å plassere den med liten tekst over skjemaet er heller ikke alltid 
tilstrekkelig for forståelse. Likevel sier UUtilsynet at det er obligatoriske felter som skal merkes på grunn av skjermlesere. 
Her må ditt team ta en vurdering av hva som vil fungere best i deres løsning.

I Punkt har du mulighet til å velge enten valgfritt-tag eller obligatorisk-tag. Bruk kun én av variantene i din tjeneste eller 
løsning for å unngå å forvirre brukeren. Selv om du har mulighet for begge, anbefales det å markere de valgfrie feltene.

<ImageWrapper caption="Skjema med valgfrie felter markert, og skjema med obligatoriske felter markert.">
  <img
    src="/assets/god-praksis/skjemadesign/skjemadesign-9.svg"
    alt="Ett skjema med felter merket som valgfritt, og ett skjema med felter merket som påkrevd"
    aria-hidden="true"
  />
</ImageWrapper>

</ContentSection>

### 8. … Men trenger du egentlig å spørre om det?

Spør deg selv: om dette feltet er valgfritt, trenger vi egentlig å spørre om det i det hele tatt? Ikke putt inn "standard"-felter 
bare fordi det er nice to have. Det er ofte ikke nødvendig å spørre om informasjon som må lagres og behandles på en god måte, med 
mindre vi trenger informasjonen til vårt formål. Du kan lese mer om 
[dataminimeringsprinsippet hos Datatilsynet](https://www.datatilsynet.no/rettigheter-og-plikter/personvernprinsippene/grunnleggende-personvernprinsipper/dataminimering/) 
som skriver mer om dette.

<PktMessagebox skin="blue" client:only="react" title="">
  <span>
Og du, husk at du bør ha god grunn til å spørre om kjønn i et skjema, er det egentlig nødvendig? Generelt er det greit å tenke over 
om man bruker inkluderende og nøytralt språk, 
[KS har en fin oversikt over gode prinsipper for inkluderende språk](https://www.ks.no/fagomrader/digitalisering/klart-sprak-i-digitale-selvbetjeningslosninger/sprak/prinsipper-for-inkluderende-sprak/) 
som kan være verdt en titt.
  </span>
</PktMessagebox>

<ContentSection backgroundColor="subtle-pale-blue">

### 9. Tekstfeltet skal være like bredt som innholdet

For å gi brukeren en indikasjon på riktig utfylling og for å hjelpe dem på veien er det viktig at selve tekstfeltet kun er like 
stort som innholdet som skal tastes inn. For eksempel ved telefonnummer (som vi vet er 8 tegn), CVC-kode (som vi vet er tre tegn) 
eller postnummer (som er fire tegn).

<ExampleComparison
  goodExample={{
    image: "/assets/god-praksis/skjemadesign/skjemadesign-10.svg",
    imgAlt: "Skjema med feltbreddet tilpasset forventet innhold",
    caption: "Tilpass bredden på tekstfeltet til forventet innhold",
  }}
  badExample={{
    image: "/assets/god-praksis/skjemadesign/skjemadesign-10-2.svg",
    imgAlt: "Skjema med feltbredder i full bredde",
    caption: "Unngå for brede eller for smale innhold til forventet innhold",
  }}
/>

</ContentSection>

### 10. Dropdown/select er ikke alltid det beste valget: prøv heller å liste ut elementene

Det er ikke alltid at dropdown er det beste valget. Har du veldig mange alternativer kan det være en god løsning, men har du 
mellom 2-6 kan det være en idé å liste dem ut i stedet.

Her har Team Booking løst det helt perfekt:

<ImageWrapper caption="Eksempel hentet fra Booking sin digitale løsning.">
  <img
    src="/assets/god-praksis/skjemadesign/skjemadesign-11.svg"
    alt="Radioknapper plassert horisontalt i bokser"
    aria-hidden="true"
  />
</ImageWrapper>

<ContentSection backgroundColor="subtle-pale-blue">

### 11. Keep it short and sweet!

Hold skjemaet ditt så kort som mulig! Det øker sjansene betydelig for at folk fyller ut.

</ContentSection>

### 12. Er det noe vi kan få gratis? Ja, da burde vi det

F.eks fødselsnummer sier noe om folkeregistrert kjønn, postnummer sier noe om poststed. Ikke be folk fylle ut om de kan slippe.

I tillegg kan det hende vi allerede har informasjon om brukerne våre, spesielt om de har registrert seg eller brukt tjenestene 
våre tidligere, dette gjør det mulig for oss å hjelpe brukerne med å fylle ut skjemaene våre mer effektivt. Tenk også over om 
det er mulig å koble seg til noen offentlige registre, f.eks fra Folkeregisteret i en søknad eller informasjon om inntekt fra Altinn.

<ContentSection backgroundColor="subtle-pale-blue">

### 13. Opt-in, ikke opt-out

Ifølge GDPR kan vi ikke lenger forhåndsvelge at brukerne skal motta nyhetsbrev, reklame eller annen relevant informasjon. De må 
aktivt gi samtykke ("opt-in") for å motta slike ting, og det er ikke lenger tillatt å ha "opt-out" som standardvalg.

<ExampleComparison
  goodExample={{
    image: "/assets/god-praksis/skjemadesign/skjemadesign-12.svg",
    imgAlt: "Et skjema der samtykke ikke er avkrysset ennå",
    caption: "La brukeren selv velge hva de ønsker å krysse av på",
  }}
  badExample={{
    image: "/assets/god-praksis/skjemadesign/skjemadesign-12-2.svg",
    imgAlt: "Et skjema der samtykke er forhåndsutfylt",
    caption: "Unngå forhåndsutfylte samtykker og skjemaelementer",
  }}
/>

</ContentSection>

### 14. Merk feil tydelig og i sammenheng med der feilen har oppstått

Det er viktig å gi brukeren god hjelp dersom de har fylt ut feil. Feltet skal markeres tydelig og feilmeldingen må være 
lett å forstå. Gi brukeren en vei videre for hvordan de skal fikse feilene, gi dem god hjelp.

Husk at:

- Skjemaet valideres når brukeren prøver å sende inn skjemaet eller det gjeldende steget
- Hvert skjemafelt som er feil eller mangelfullt skal merkes med en statusfarge for feil og få en beskrivende feilmelding. Styling på dette ligger inne i designsystemet Punkt.
- Når brukeren retter feilen, skjules feilmeldingen med én gang både på feltet, og går tilbake til standard farge

Det er viktig å skrive gode og beskrivende feilmeldinger. Under ser du et eksempel på en god oppbygning av feilmeldinger:

<ImageWrapper>
  <img
    src="/assets/god-praksis/skjemadesign/skjemadesign-13.svg"
    alt="Eksempel på en god feilmelding med beskrivelser og hjelp på veien"
    aria-hidden="true"
  />
</ImageWrapper>

Du kan lese enda mer om hvordan du kan skrive gode meldinger i Drive-mappen kalt 
[Retningslinjer og prinsipper for meldinger ](https://drive.google.com/drive/u/1/folders/1Dqu-onqdvpmgSsLfgj3bgH_vefA_leQs).

<ContentSection backgroundColor="subtle-pale-blue">

### 15. Ha en tydelig call-to-action

Fortell brukeren hva som skjer etter at de er ferdig med skjemaet og trykker seg videre. Dersom det er 
flere steg i skjemaet, bruker du knapp med “forrige” og “neste”. I siste steg må det komme tydelig frem hva 
som kommer til å skje når brukeren trykker på knappen, for eksempel med “Send inn skjema” eller “Send til godkjenning”.

Knappen skal inneholde det som faktisk kommer til å skje, et verb og den faktiske handlingen så konkret som mulig. 
F.eks: send inn skjemaet, avbryt bestillingen, se oppsummering og betal eller slett kontoen, unngå "OK", “Klikk her” eller “Ferdig”.

<ExampleComparison
  goodExample={{
    image: "/assets/god-praksis/skjemadesign/skjemadesign-14.svg",
    imgAlt: "Skjema med 'Send inn skjema'-knapp",
    caption: "Ha en tydelig call-to-action som beskriver hva som skjer videre",
  }}
  badExample={{
    image: "/assets/god-praksis/skjemadesign/skjemadesign-14-2.svg",
    imgAlt: "Skjema med 'Ferdig'-knapp",
    caption: "Unngå uklar knappetekst som kan forvirre brukeren",
  }}
/>

</ContentSection>

### 16. Utviklerne må på banen

Hvis man for eksempel koder skjemaet slik at hvert felt vet hva det er, altså hvilken type input man ber om, kan 
man for eksempel få egne tastaturer for hvert felt på mobile enheter. Det vil si at når vi for eksempel ber om et 
nummer, så får brukeren opp nummertastaturet på mobilen. Dette gjør utfyllingen uendelig mye enklere for folk som 
fyller ut skjema på mobil. Les mer om dette på [UUtilsynet sine sider](https://www.uutilsynet.no/veiledning/135-identifiser-formal-med-inndata/1238).

Det er generelt viktig å sette opp skjemaet semantisk og [kode det optimalt for skjermlesere](https://www.w3.org/WAI/tutorials/forms/).

<ContentSection backgroundColor="subtle-pale-blue">

### 17. Design skjemaet som en samtale!

Daniel i Netlife har skrevet en [fantastisk artikkel](https://www.netlife.com/blogg/lag-skjema-som-en-samtale) 
om hvordan du burde sette opp skjemaet som en samtale.

</ContentSection>

### Det kan også være lurt å lese seg opp på skjemadesign!

Her er noen gode ressurser for å lære enda mer om det å sette opp et godt skjema:

- [Elmer3-retningslinjene fra Brønnøysundsregistrene: Retningslinjene er ment for å sikre at offentlige elektroniske skjemaer blir utviklet på en enhetlig og brukervennlig måte](https://brukskvalitet.brreg.no/elmer3/)
- [Design bedre skjema så folk kan gjøre det de kom for (Netlife)](https://medium.com/netlife/design-bedre-skjema-s%C3%A5-folk-kan-gj%C3%B8re-det-de-kom-for-aaddc706684c)
- [Skjema (UUTilsynet)](https://www.uutilsynet.no/veiledning/skjema/38)
- [10 tips for å lage gode skjemaer (Universitetet i Oslo)](https://www.uio.no/tjenester/it/adm-app/nettskjema/hjelp/beste-praksis-for-nettskjema.html)
- [Hvordan gjøre skjemaer universelt utformet? (Bouvet)](https://www.bouvet.no/bouvet-deler/skjema--hvordan-gjore-dem-universelt-utformet)
- [Use these top 10 tips when you design forms](https://blog.prototypr.io/use-these-top-10-tips-when-you-design-forms-d095d6e3ab8a)

<ContentSection backgroundColor="beige">

export const checklistElements = [
  "Vi har skrevet en kort og forklarende intro til skjemaet",
  "Alle feltene er under hverandre på én linje (med noen unntak)",
  "Vi har tatt i bruk label og plassert dem over inputfeltet",
  "Vi har ikke tatt i bruk plassholdertekst i stedet for label",
  "Vi har gruppert elementene i skjemaet på en logisk måte (enten i steg eller visuelle grupper)",
  "Vi har skrevet gode og forklarende hjelpetekster der det trengs (og droppet det der det ikke er nødvendig)",
  "Vi har markert det som er valgfritt (eller det som er obligatorisk)",
  "… Og vi har tatt en vurdering og fjernet det som ikke er nødvendig å spørre om",
  "Tekstfeltene er like brede som forventet innhold",
  "Vi har brukt select der det er mest hensiktsmessig (flere alternativer) eller listet ut elementene dersom det er mulig",
  "Vi har holdt skjemaet så kort som mulig",
  "Vi har tatt i bruk mulighetene for å hente inn informasjon “gratis”",
  "Vi har bare tatt i bruk opt-in",
  "Vi har markert feilene tydelig og skrevet gode og logiske feilmeldinger",
  "Skjemaet har en tydelig call-to-action",
  "Vi har koblet på utviklerne og de har bidratt med semantisk oppsett av skjemaet",
  "Vi har, etter beste evne, designet skjemaet som en samtale",
  "Vi har lest litt ekstra om skjemadesign",
  "Vi har testet skjemaet både på desktop og mobil (og det fungerer like godt begge steder)",
  "Vi har kontaktet designsystem-teamet dersom vi har trengt hjelp eller råd",

];

<Checklist
  title="Sjekkliste"
  checklistElements={checklistElements}
  color="transparent"
/>

</ContentSection>