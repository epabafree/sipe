# Updating to a new release

Every card has a permanent ID. Importing a newer `.apkg` **updates** existing cards (fixes, better solutions) and **adds** new ones. Your review history, intervals and flags stay.

1. Download the new `.apkg` from **Releases**.
2. Import it (File ▸ Import). If Anki asks how to handle updates, choose to update existing notes.
3. Sync, if you use more than one device.

## Moving to v0.5 (new deck layout)

v0.5 reorganised the decks: full section names, numbered so they stay in order, plus **Practice by Topic** and **Papers & Mocks**. Anki keeps existing cards in whichever deck they are already in when you import, so the new layout only appears on a fresh import:

1. In Anki, delete the old **sipe** deck (gear icon ▸ Delete). If you still have a **Mock Tests** deck from the pilot, delete that too.
2. Import `sipe.apkg` from the latest release.

This resets your review history for sipe. Future releases keep the same layout, so later updates won’t need this step.

**Note for pilot users:** the early pilot used a different deck name (“CAT PYQ”). Delete that old deck before importing.
