# Contributing to Punkt

**Generated**: 2025-11-06T10:52:48.986246
**Git Commit**: 05685b33
**Source Files**:
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`

---

## Contributing Guidelines


## Hvordan bidra - Repoet ⭐

Takk for at du vil bidra til å gjøre designsystemet bedre. Her definerer vi hvordan.

Dette repoet inneholder subrepoer som har ulike fremgangsmåter for å bidra. Så hvor ønsker du å hjelpe?

- [assets](/bidra/som-utvikler/assets) - Ressurser
- [css](/bidra/som-utvikler/css) - CSS-rammeverket
- [vue](/bidra/som-utvikler/vue) - Vue 3 komponenter
- [react](/bidra/som-utvikler/react) - React komponenter

## Forutsetninger

Aller først må du konfigurere git-hooks slik at scripts kjøres ved commits, som for eksempel et script som kopierer innhold fra readme og contributing til dokumentasjonsnettsiden.

Sett opp git hooks:

```sh
git config core.hooksPath scripts/git-hooks
```

### Lerna

Vi bruker Lerna for å gjøre utvikling i et monorepo smidigere.
Les mer om [Lerna](https://lerna.js.org/).

Kjør kommandoer fra rot.
Kommandoer:

```sh
npx nx graph                    # Oversikt over avhengighetene
npx lerna add-caching           # Konfigurer caching
npm run build                   # Bygger alle pakkene og docs
npm run build-assets            # Bygger bare punkt-assets
npm run build-css               # Bygger bare punkt-css
npm run build-css-app           # Bygger bare punkt-css devapp
npm run build-react             # Bygger bare punkt-react
npm run build-react-app         # Bygger bare punkt-react devapp
npm run build-vue               # Bygger bare punkt-vue
npm run build-vue-app           # Bygger bare punkt-vue devapp
npm run build-docs              # Bygger bare punkt-docs
npm run dev-cli                 # Kjører punkt-cli dev-serveren
npm run dev-css                 # Kjører punkt-css dev-serveren
npm run dev-docs                # Kjører docs dev-serveren
npm run dev-react               # Kjører punkt-react dev-serveren
npm run dev-vue                 # Kjører punkt-vue dev-serveren
npm run publish                 # Versjonering og publisering til npm - ikke private pakker
npm run svgo                    # Optimaliserer svg-filer i gitte foldere i assets
npm run test                    # Kjører alle testene til pakkene og docs
npm run update-changelog        # Oppdaterer changelogs
npm run watch                   # npx lerna run --parallel watch
npm run watch-css               # npx lerna run watch --scope=@oslokommune/punkt-css
```

## 🤝 Lag PR

Når du er klar for en PR skriv din GitHub-message som sier hva som er gjort, og evt issue nummer.

Vi bruker [Conventional Commits](https://www.conventionalcommits.org/) for å beskrive commits gjennom
noen regler. Ingen fare om du ikke følger den, vi tar en gjennomgang og evt justerer 😎.

<type>(<omfang>): #<oppgavenummer> <beskrivelse>

[valgfri ytterligere beskrivelse av endringen]

### Type

- feat: En ny funksjon
- fix: En feilretting
- docs: Kun endringer i dokumentasjon - vår nettside
- chore: Endringer i byggeprosessen eller hjelpeverktøy og biblioteker
- style: Endringer som ikke påvirker betydningen av koden (mellomrom, formatering, osv)

### Omfang

- assets (@oslokommune/punkt-assets på NPM)
- cli (@oslokommune/punkt-cli på NPM)
- css (@oslokommune/punkt-css på NPM)
- react (@oslokommune/punkt-react på NPM)
- vue (@oslokommune/punkt-vue på NPM)
- all (alle ovennevnte)

### Oppgavenummer

GitHub oppgavenummer som denne commit er relatert til.

### Beskrivelse

En kort beskrivelse av endringen.

### Ytterligere beskrivelse (valgfri)

En lengre beskrivelse av endringen, kan være flere avsnitt.

### Eksempler

```sh
fix(vue): #NR Rett feil på alert-komponenten               # med issuenummer
fix(vue): Rett feil på alert-komponenten                   # patcher en bug i koden (patch i Semantic Versioning)
feat(vue): Legg til funksjonalitet                         # ny funksjonalitet i koden (minor i Semantic Versioning)
feat(vue)!: Legg til funksjonalitet og endre eksisterende  # breaking change i koden (major i Semantic Versioning)
docs: Endre dokumentasjon                                  # Endring i dokumentasjon
```

## Bugs

Hvis du finner en bug sjekk om den allerede diskuteres på [Github discussion](https://github.com/oslokommune/punkt/discussions). Hvis ikke kan du [opprette et issue her](https://github.com/oslokommune/punkt/issues). Bruk labels `bug` og hvilken del av repoet det gjelder, for eksempel `assets` eller `docs`.

## Nye ideer?

Hvis du vil diskutere nye features eller muligheten for å endre på eksisterende funksjonalitet++, [dra hit](https://github.com/oslokommune/punkt/discussions). Tag gjerne diskusjonen du lager med en av de eksisterende kategoriene.

Hvis diskusjonen ender med at arbeid på designsystemet skal utføres, så lager **vi (Origo)** et issue, som lenker til diskusjonen. Hvis deler av arbeidet skal utføres på noe som eksisterer i dette repoet, så skal det også opprettes en PR i det **oppgaven påbegynnes** - ikke i det den er ferdig!

## Ta kontakt

Vi kan også nåes på Slack hos oslokommune.slack.com på [#origo-punkt](https://oslokommune.slack.com/archives/C01EWV9U07R) for en hyggelig prat. 👋🏼



---


## Code of Conduct


# Code of Conduct (english only)

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, caste, color, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
[INSERT CONTACT METHOD].
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**:
Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**:
A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder][Mozilla CoC].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][FAQ]. Translations are available
at [https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
[Mozilla CoC]: https://github.com/mozilla/diversity
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations



---


## Security Policy


# Security Policy

## Supported Versions

All versions

## Reporting a Vulnerability

If you have knowledge of a vulnerability in Punkt, please create an issue with a severity label attached.
