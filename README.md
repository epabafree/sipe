# sipe

An Anki deck of CAT previous-year questions. Each question is an interactive card: pick an option (or type the answer for TITA questions), then flip it for a worked solution.

<p align="center"><img src="docs/img/qa-solution.png" width="440" alt="A QA card after answering"></p>

## What's in it

| Paper | VARC | DILR | QA | Total |
| --- | ---: | ---: | ---: | ---: |
| CAT 2023 Slot 1 | 24 | 20 | 22 | 66 |
| CAT 2023 Slot 2 | 24 | 20 | 22 | 66 |
| CAT 2023 Slot 3 | 24 | 20 | 22 | 66 |
| CAT 2022 Slot 1 | 24 | 20 | 22 | 66 |
| CAT 2022 Slot 2 | 24 | 20 | 22 | 66 |
| CAT 2022 Slot 3 | 24 | 20 | 22 | 66 |
| CAT 2021 Slot 1 | 24 | 20 | 22 | 66 |
| | | | | **462** |

Alongside the question cards there are set cards (a whole RC passage or DILR set on one card), formula and technique cards, a practice card for each topic area, and a card for each paper with a practice mode and a timed mock.

## Installing

1. Install Anki: [desktop](docs/install-desktop.md), [Android](docs/install-android.md) or [iPad/iPhone](docs/install-ipad.md).
2. Download `sipe.apkg` from the [latest release](https://github.com/epabafree/sipe/releases/latest).
3. Import it. No add-ons are needed.

If you're upgrading from v0.4 or earlier, read [updating](docs/updating.md) first; the deck layout changed in v0.5.

## Layout

```
sipe
├── 00 Start Here                              guide and Study Planner
├── 01 Verbal Ability & Reading Comprehension  by year and slot, then whole passages
├── 02 Data Interpretation & Logical Reasoning by year and slot, then whole sets
├── 03 Quantitative Aptitude                   by year and slot
├── 04 Practice by Topic
├── 05 Formulas & Concepts
└── 06 Papers & Mocks
```

Every card is tagged (`sipe::Topic::QA::Algebra::Quadratic_Equations`, `sipe::Paper::2023_S1`, `sipe::Format::TITA` and so on), which is what the Study Planner and the topic cards use.

<p>
<img src="docs/img/varc-dark.png" width="32%" alt="A VARC card in dark mode">
<img src="docs/img/topic-practice.png" width="32%" alt="Topic practice card">
<img src="docs/img/set-card.png" width="32%" alt="A DILR set card">
</p>

## Notes on the content

Questions, options, passages and data are kept as printed. Clear misprints are fixed, and each fix is listed in the [changelog](CHANGELOG.md). Answers are checked against the official keys. Solutions are written for this deck rather than copied from the source.

The source groups the 2021 and 2022 questions by topic rather than by paper, so they have been put back into exam order using the official response sheets. Where a question's position couldn't be confirmed, the changelog says so. Options are listed in the order the source prints them, which for a few of these questions differs from the exam.

Difficulty labels are estimates, not official data.

## Documentation

- [Solving a card](docs/using-the-cards.md) · [Toolbar](docs/toolbar-and-tools.md) · [Set cards](docs/set-cards.md)
- [Papers and mocks](docs/papers-practice-and-mock.md) · [Practice by topic](docs/practice-by-topic.md) · [Study Planner](docs/study-planner.md)
- [Formula cards](docs/formula-cards.md) · [Flags](docs/flags.md)
- [Updating](docs/updating.md) · [CSV import](docs/csv-import.md) · [FAQ](docs/faq.md) · [Building from source](docs/building.md)

## Roadmap

- CAT 2021 Slots 2 and 3
- CAT 2017–2020
- CAT 1991–2008 (mostly DILR and QA)
- More mocks and longer explanations after that

Found a mistake? Open an issue with the ID printed at the bottom of the answer side, e.g. `2023-S1-QA-07`.
