# CSV import (alternative)

Each release also ships CSV files plus a `media/` folder.

1. Import the `.apkg` once, so the note types (“sipe · Question”, “sipe · Set”, …) exist.
2. Copy everything from `media/` into your Anki profile's `collection.media` folder.
3. File ▸ Import each CSV. Deck, note type, tags and a permanent ID are read from the file headers, so nothing needs mapping. Re-importing updates cards instead of duplicating them.

| File | Contents |
| --- | --- |
| `sipe_questions_VARC/DILR/QA.csv` | Question cards |
| `sipe_sets.csv` | Set cards |
| `sipe_formulas_techniques.csv` | Formula and technique cards |
| `sipe_mock.csv` | Paper cards (practice + mock) |
| `sipe_start_here_*.csv` | Welcome guide and Study Planner |
