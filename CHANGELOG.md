# Changelog

## v0.10.0

Added CAT 2021 Slot 3 (66 questions, 8 set cards), in the original exam order. The project schedule in DILR Set 2 is redrawn from the source.

VARC Q3 (the clock passage, "all of the following arguments, EXCEPT") follows the official key, option 2. Option 3 is close to a line in the passage, and the card explains the difference.

The timed mock's section table now wraps on narrow screens.

Fixes to the source text:
- Hyphens restored in "half-century", "time-saving", "Nano-Sentinels" and "industry-wide".

## v0.9.0

Added CAT 2021 Slot 2 (66 questions, 8 set cards), in the original exam order. The order-processing chart in DILR Set 1 is redrawn from the source.

Fixes to the source text:
- DILR Set 2: fact 1 read "value for an object is o10"; it should be 10.
- Knowledge passage: "things-in-themselves" and "things-as-they-are-in-themselves" restored.
- Summary on preprints: "peer-reviewed" and "conservative" restored.

## v0.8.0

Added CAT 2021 Slot 1 (66 questions, 8 set cards), in the original exam order. The sales chart in DILR Set 4 is redrawn from the source. The source doesn't show the 2019 mark for Storage, so it is drawn at the end of the 2020 bar (about 5.1). Q17 uses it, but its answer is the same for any value from about 3.8 to 5.8.

Two new formula cards: the inradius of a right triangle, and the sign of a rational expression.

Fixes to the source text:
- DILR Set 2: "a profit of I 4 per unit" → "₹4 per unit".
- DILR Set 3: "acquintance" → "acquaintance", "Bhratan" → "Bharatan", "Ezhill" → "Ezhil".
- Cuttlefish passage: "marshmalow" → "marshmallow", and the quotation marks around "delayed" and "never".
- Utopia passage: "institutions and more." → "institutions and mores,".
- McGurk summary: "ga-gaga" → "ga-ga-ga", "in congruent" → "incongruent", "many limes" → "many times".
- QA Q17: "work alone" → "works alone".

## v0.7.0

Added CAT 2022 Slot 3 (66 questions, 8 set cards), in the original exam order. The four bar charts in DILR Set 1 are given as tables.

DILR Q5 (females aged 20–30 in 1980 who died between 50 and 60) can be read two ways. The card uses the official answer, 30, and explains the other reading.

Three new formula cards: medians and the centroid, which side lengths make a polygon, and the same remainder for several divisors.

Fixes to the source text:
- QA Q3: the right-hand side of the second equation was missing. It reads (4a/b)^(6x − y) = (2a/b)^(y − 6x).
- QA Q14: "less then" → "less than".
- Software passage: "aimlessly click around", "for", "data collected", "screen-driven".
- Other passages: "so-called", "industrialisation", "Farmers", "modern genetic", "nation’s".

## v0.6.0

Added CAT 2022 Slot 2 (66 questions, 8 set cards), in the original exam order.

DILR Q6 (widget routes, "If the last location visited is Ahmednagar…") was dropped from scoring in the actual exam: under the tie-breaking rule Ahmednagar can't be the last stop. The card keeps the question and explains this; the intended answer is 35.

Two new formula cards: when a power equals 1, and the standard sums of n and n².

Fixes to the source text:
- QA Q19: the exponent was printed as a second factor. The equation is (x² − 10)^(x² − 3x − 10) = 1, not a product.
- RC passage on octopuses: the source leaves out the paragraph on chromatophores that three questions rely on. A short summary of it has been added in brackets.
- RC Q2: option 4 read "capable of being a music king"; corrected to "capable of musicking".
- DILR Set 3: the revenue axis label "8" should be 80. Both plots are redrawn.
- Engineering passage: "roles can", "FDA-approved", "self-reflection", "primes students" restored.

## v0.5.0

Added CAT 2022 Slot 1 (66 questions, 8 set cards).

VARC and DILR follow the original exam order. Seven QA questions (2, 3, 12, 13, 14, 19 and 21) couldn't be matched to their original positions because their text isn't in the response sheet, so their numbering is approximate.

The deck layout has changed. Top-level decks are numbered and use full section names, set cards now sit under their section, and each paper card has its own deck under `06 Papers & Mocks`. Existing installs need a fresh import; see [docs/updating.md](docs/updating.md).

Added topic-wise practice (`04 Practice by Topic`). Questions from all papers are grouped by topic area, with filters for subtopic and paper.

Other changes:
- Removed the flag reminder from the answer side.
- Paper and topic cards show the same content on both sides.
- Four new formula cards: three-set overlaps, absolute values as distances, the greatest integer function, distributing identical objects.

Fixes to the source text:
- Tokens set: "Rashida" → "Rasheeda", "How among" → "Who among".
- Restored hyphens in "work-from-home", "non-tangibles" and "get-together".

## v0.4.0

Added CAT 2023 Slots 2 and 3 (132 questions, 16 set cards). The release is now a single `sipe.apkg` containing everything so far.

- 21 new formula and technique cards (58 in total). VARC technique cards list every question of their type.
- One paper card per slot.
- Long inline maths in formula examples now wraps on phones.

Fixes to the source text:
- Slot 2 VARC Q22: answer key corrected from 4321 to 4312.
- Slot 3 DILR Set 2: the street map was missing the A–E street.
- Slot 3 QA Q3: the second equation had "=" where it should have "+".

## v0.2.0 — CAT 2023 Slot 1 (full paper)
- All 66 questions of CAT 2023 Slot 1 (24 VARC, 20 DILR, 22 QA) in original order.
- 8 set cards (4 RC passages, 4 DILR sets).
- 37 formula and technique cards.
- Papers: new **Practice** mode (free navigation, instant checking, solutions, progress per device) alongside the timed mock.
- Study Planner: new **Revisit a paper** recipe.
- Cards can accept more than one correct option.
- Source corrections: DILR Set 3 data table (Range row, “Modal”); DILR Set 1 Q2 accepts both B1 and D2; the printed workings for QA Q7 and Q22 rewritten; one VARC passage typo; minor hyphenation.

## v0.1.0 — Pilot
- 26 questions from CAT 2023 Slot 1, toolbar, theme switch, timer, flags, formula cards, Study Planner, mock.
