# Building from source

Needs Python 3.10+ and `genanki`.

```
pip install genanki
cd source
python build.py
```

Output goes to `source/out/`: `sipe.apkg`, the CSVs and media.

| Path | |
| --- | --- |
| `extract/` | Question text, options and passages |
| `paperlib.py` | Helpers used by the per-paper modules |
| `b2_*.py` … `b5_*.py`, `data_*.py` | Solutions, hints, tags and difficulty for each paper |
| `data_ref.py` | Formula and technique cards |
| `tpl/` | Card templates, CSS and the shared script |
| `media/` | Diagrams (SVG) |

## Releases

The workflow in `.github/workflows/build.yml` runs on every push to `main`. It reads the newest version heading in `CHANGELOG.md`; if no release exists for that version yet, it builds the deck and publishes a release with `sipe.apkg` and the CSV bundle attached, using that version's changelog section as the notes. So publishing a release only takes a new changelog entry.
