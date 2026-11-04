# Eppy's CAT PYQ — the **sipe** Anki deck

Every CAT previous-year question as an interactive Anki card, with a worked solution for each one.
You tap an option and see straight away whether you're right; the answer side then gives a step-by-step solution, a shortcut, the key formula, and why the other options are wrong.

![A QA card's solution](docs/img/qa-solution.png)

## What's included so far

| Release | Contents | Questions |
| --- | --- | --- |
| **CAT 2023 Slot 1** | Full paper: 24 VARC · 20 DILR · 22 QA, in the original order | 66 |
| Set cards | 4 RC passages and 4 DILR sets, each as one card with all its questions | 8 |
| Formula & technique cards | QA and DILR formulas, VARC question-type techniques | 37 |
| Papers | Practice navigator + optional timed mock for CAT 2023 Slot 1 | 1 |
| Start Here | Welcome guide and the Study Planner | 2 |

Coming next: CAT 2023 Slots 2 and 3, then 2022, 2021, 2020–2017 and 1991–2008. See the [roadmap](#roadmap).

## Quick start

1. Install Anki for your device: [Windows / Mac / Linux](docs/install-desktop.md) · [Android](docs/install-android.md) · [iPad & iPhone](docs/install-ipad.md).
2. Download the latest `.apkg` from **Releases** (right-hand side of this page).
3. Double-click it, or use **File ▸ Import** in Anki. No add-ons are needed.
4. Open **sipe ▸ 00 Start Here**, then choose a paper, for example **sipe ▸ QA ▸ 2023 ▸ Slot 1**.

## Features

| | |
| --- | --- |
| **Interactive questions** | Tap an option, press 1–4, or type the answer for TITA questions. You see right or wrong at once. → [Solving cards](docs/using-the-cards.md) |
| **Solutions you can follow** | Numbered steps, properly typeset maths, tables and redrawn diagrams for DILR, quoted passage evidence for VARC. |
| **Quiet toolbar** | Timer (show / hide / off), calculator, text size and font, step-by-step solutions, Light / Dark / Auto, all on the card. → [Toolbar and tools](docs/toolbar-and-tools.md) |
| **Handy extras** | Cross out options, highlight passages, “Need a nudge?” for a first-step hint. |
| **Set cards** | A whole RC passage or DILR set on one card, as in the exam. → [Set cards](docs/set-cards.md) |
| **Papers** | **Practice** mode lets you move freely through a paper and recheck anything; **Timed mock** gives exam conditions and a CAT-style score. → [Papers](docs/papers-practice-and-mock.md) |
| **Mistake flags** | Red = concept gap, Orange = silly mistake, Blue = too slow, Green = new trick. → [Flags](docs/flags.md) |
| **Study Planner** | Tick topics, years, flags or “got wrong recently” and copy a ready-made search. No Anki search syntax needed. → [Study Planner](docs/study-planner.md) |
| **Formula cards** | Formulas by topic, with what each symbol means, when to use it, a trap and a quick example. → [Formula cards](docs/formula-cards.md) |
| **Safe updates** | Importing a newer release updates cards and keeps your progress. → [Updating](docs/updating.md) |

<p>
<img src="docs/img/varc-dark.png" width="49%" alt="VARC card in dark mode">
<img src="docs/img/practice.png" width="49%" alt="Practice navigator">
</p>

## Deck layout

```
sipe
├── 00 Start Here        Welcome guide, Study Planner
├── VARC ▸ 2023 ▸ Slot 1
├── DILR ▸ 2023 ▸ Slot 1
├── QA   ▸ 2023 ▸ Slot 1
├── Sets ▸ VARC · DILR
├── Formulas ▸ QA ▸ Algebra · Arithmetic · Geometry · Modern Maths · Number System ; DILR ; VARC
└── Papers               Practice + timed mock, one card per paper
```

Tags follow the same tree (`sipe::Section::QA`, `sipe::Topic::QA::Algebra::Quadratic_Equations`, `sipe::Year::2023`, `sipe::Paper::2023_S1`, `sipe::Format::TITA`, …) so the [Study Planner](docs/study-planner.md) can pull any combination together.

## Roadmap

| # | Batch | Status |
| --- | --- | --- |
| 0 | Pilot | ✓ |
| 1 | This repository and docs | ✓ |
| 2 | CAT 2023 Slot 1 (full paper) | ✓ |
| 3–4 | CAT 2023 Slots 2 and 3 | next |
| 5–10 | CAT 2022 and 2021, one release per slot | |
| 11–14 | CAT 2020, 2019, 2018, 2017 | |
| 15–17 | CAT 1991–2008 | |
| 18 | v1.0: complete formula library, final review | |

## More

- [CSV import (alternative to the .apkg)](docs/csv-import.md)
- [FAQ and troubleshooting](docs/faq.md)
- [Building the deck from source](docs/building.md)
- [Changelog](CHANGELOG.md)
