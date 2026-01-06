# punkt-testing-utils

**Generated**: 2025-11-06T10:52:48.930425
**Git Commit**: 05685b33
**Source Files**:
- `packages/testing-utils/README.md`
- `packages/testing-utils/package.json`

---

**Package**: @oslokommune/punkt-testing-utils


# punkt-testing-utils

<a href="https://www.npmjs.com/package/@oslokommune/punkt-testing-utils" target="_blank"><img src="https://img.shields.io/npm/v/@oslokommune/punkt-testing-utils?logo=testinglibrary&label=testinglibrary&style=for-the-badge&color=E33332" alt="React komponenter" /></a>

Dette biblioteket oppstod for å gjøre det enklere å skrive frontend-tester i applikasjoner som bruker Punkt og testing-library.

testing-library ikke har veldig god støtte for custom elements (web components). Når du oppgraderer til ny Punkt-versjon, og Punkt-teamet har migrert komponenter fra React/Vue til Web components, risikerer du at testene dine begynner å feile på ikke-opplagt vis.

punkt-testing-utils er ment å gjøre oppgradering til nye Punkt-versjoner mindre smertefullt, ved å abstrahere funksjoner fra testing-library og la meg som webapp-utvikler forholde meg til funksjoner som vedlikeholdes av Punkt.

## Eksempel:

I Team Booking har vi en haug med tester på frontend-koden vår. Disse er skrevet i react-testing-library, og er dermed typisk noe sånt:

### Uten punkt-testing-library

```
render()
const input = screen.getByRole("textbox", "Skriv her")
fireEvent.change(input, "Noe tekst")
const submitButton = screen.getByLabelText("button", "Send inn")
fireEvent.click(button);
// Assert at noe er sendt inn
```

Dette funker fint så lenge `getByRole` finner en `<input/>` og en `<button/>`, sånn at verdien blir satt og knappen trykket på, og det har fungert så lenge Punkt-komponentene har vært enkle React-komponenter.

Men etterhvert som Punkt skrives om til custom elements, holder ikke lenger den forutsetningen. En `getByRole` kan nå ende opp med å finne punkt-textinput sin interne, skjulte `<input>`, som ikke er ment å herjes med.
react-testing-library gir ikke noe gratis mtp custom elements.

Så hver gang vi har oppdatert webappen vår til ny Punkt-versjon, har en haug av testene våre brukket, og det har vært mye jobb med å fikse dem, **hver gang**.

### Med punkt-testing-library

```
const input = ptl.getPktElementByLabelText("Skriv her"); // ptl = punkt-testing-library
await ptl.setPktElementValue(input, "Noe tekst");
const submitButton = screen.getByLabelText("button", "Send inn")
await ptl.pktClickButton(submitButton);
// Assert at noe er sendt inn

```

Dette er mindre sårbart fordi vi ikke trenger å vite om input-feltet er et `PktTextinput` eller et `HTMLInput`-element - så lenge vi holder oss til funksjoner fra punkt-testing-library, vil testene våre fungere uavhengig av hvilken versjon av Punkt vi bruker.

Funksjonene i punkt-testing-library støtter både gamle (ikke-custom-elements) og nye (custom elements) versjoner av Punkt-komponentene, sånn at testene ikke brekker når Punkt bytter implementasjon av komponentene sine. punkt-testing-library er i seg selv dekket av tester, og bor i kodebasen til Punkt, så Team Designsystem vil tidlig oppdage tidlig om de har endret noe som gjør at noe brekker.

Etter å ha skrevet om testene våre en siste (🤞) gang, denne gang til å bruke punkt-testing-library, har det vært (så godt som) smertefritt å bytte Punkt-versjon i webappen vår.

Funksjoner i punkt-testing-library som tar et element som parameter, kan også kalles med label, så eksempelet kan forkortes til

```
await setPktElementValue('Skriv her', 'Noe tekst');
await pktClickButton('Send inn');
```

Merk at funksjoner i punkt-testing-library som endrer verdier eller trigger events er asynkrone (returnerer et promise), så de bør alltid brukes med `await`.

## Installasjon og oppsett

```
npm install --save-dev @oslokommune/punkt-testing-utils
```

Du må initialisere punkt-testing-library med din testing-library-implementasjon, med react-testing-library blir det sånn:

```
import * as ReactTestingLibrary from '@testing-library/react';
import { setupPktTestingLibrary } from '@oslokommune/punkt-testing-utils';

const {
  getPktElementByLabelText,
  setPktElementChecked,
  setPktElementValue,
  getAllPktElementsByLabelText,
  waitForPktElementsToBeDefined,
  getPktSelectOptions,
} = setupPktTestingLibrary(ReactTestingLibrary)
```

Dette kan du gjerne gjøre i en felles-fil som du importerer i testene dine.

## API

```
type PktElementType = PktDatepicker | PktProgressbar | PktTextarea | PktInputWrapper | PktSelect | PktRadioButton;
export declare const waitForPktElementsToBeDefined: () => Promise<(CustomElementConstructor | undefined)[]>;
export declare const getPktElementByLabelText: (label: string, container?: HTMLElement) => PktElementType;
export declare function setPktElementValue(element: PktElementType, valueOrValues: string | Array<string>): Promise<boolean>;
export declare const setPktElementChecked: (element: PktElementType, checked: boolean) => Promise<boolean>;
type PktOption = [string, string | null, boolean];
export declare const getPktSelectOptions: (selectElement: PktSelect) => Array<PktOption>;
export declare const setPktSelectedOptionsByLabel: (selectElement: PktElementType | HTMLSelectElement, ...optionLabels: Array<string>) => Promise<boolean>;
export declare const checkPktElement: (element: PktRadioButton) => Promise<boolean>;
export declare const getAllPktElementsByLabelText: (label: string, container?: HTMLElement) => Element[];
```

## Men vent! Er dette bare for React? Hva med Vue? Svelte? Cypress? Playwright?

Foreløpig har vi ikke gjort noe for å støtte Vue, men det er en liten, teoretisk sjanse for at det funker ut av boksen. punkt-testing-library har en dependency til dom-testing-library, men ikke til react-testing-library. Du kan plugge inn ditt favoritt (testing-library-kompatible) test-bibliotek, for eksempel vue-testing-library og håpe at det funker - men det har vi som sagt ikke testa, ennå. Men prøv gjerne, og se hvor det tryner, så kan vi fikse det i fellesskap.
Hvis du bruker et testbibliotek som ikke er basert på testing-library, må du implementere en del funksjoner selv. I så fall kan det være best å kopiere koden lage et nytt testbibliotek.

Det kan også være mulig å bruke punkt-testing-library med helt andre testrammeverk. Du må i så fall implementere `PktTestingLibraryOptions`-interfacet selv, og initialisere punkt-testing-library med din implementasjon:

```
const MyTestingLibrary = {
  fireEvent: /* implementasjon */ ,
  findAllByLabelText: /* implementasjon */
  // osv
}

const { getPktElementByLabelText, setPktElementChecked, ...} = setupPktTestingLibrary(MyTestingLibrary)
```

## Kjente problemer

Biblioteket er p.t. kompilert som en commonjs-modul. Vite støtter ikke dette, så i din `vite.config.ts` må du ha:

```js
server: {
  deps: {
    inline: ['@oslokommune/punkt-testing-utils']
  }
}
```



## Package Metadata


- **Version**: 13.15.1

- **Name**: @oslokommune/punkt-testing-utils

- **Description**: Test-utilities for Punkt
