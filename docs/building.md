# Building the deck from source

Requirements: Python 3.10+ and `pip install genanki`.

```
cd source
python build.py
```

The `.apkg`, CSVs and media are written to `source/out/`.

| Path | What it holds |
| --- | --- |
| `extract/` | Question text, options and passages taken from the source papers |
| `data_*.py`, `b2_*.py` | Solutions, hints, tags and difficulty, per batch |
| `data_ref.py` | Formula and technique cards |
| `tpl/` | Card templates, styles and the shared card script |
| `media/` | Diagrams (SVG) |

Pushing a tag such as `v0.2.0` runs the GitHub Action, which builds the deck and attaches it to a release.
