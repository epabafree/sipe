# Study Planner: practise anything, no search syntax

![Study Planner](img/study-planner.png)

## How it works (in plain words)
1. Every card carries labels (tags): section, year, slot, topic, MCQ/TITA, difficulty.
2. A **filtered deck** is a temporary practice deck that Anki fills with every card matching a search, from any paper.
3. When you delete the filtered deck, the cards go back to their papers with your progress kept.

The planner builds the search for you.

## Steps
1. Open **sipe ▸ 00 Start Here ▸ Study Planner**.
2. Tap a **recipe**, or tick what you want: section, topics, years, slots, MCQ/TITA, difficulty, your history (new / due / got wrong recently / forgotten 2+ times), flags, and which card types to include.
3. Press **Copy**.
4. Follow the instructions shown for your device:
   - **Desktop:** Tools ▸ Create Filtered Deck… (or press F) → paste into Search → Limit 9999 → Build.
   - **Android:** deck list ⋮ ▸ Create filtered deck → paste → Build.
   - **iPad/iPhone (AnkiMobile):** deck list ▸ Add (+) ▸ Filtered Deck → paste → Build.
5. Study it. Delete it when you're done.

## Recipes
| Recipe | What you get |
| --- | --- |
| Revisit a paper | Every card of a paper, done or not, in exam order, without changing your schedule |
| Practise one topic | Every question on a topic, across all years |
| Topic + its formulas | Those questions plus the topic's formula cards |
| Redo my mistakes | Everything you got wrong in the last 7 / 14 / 30 days |
| Fix concept gaps | Red-flagged cards |
| Silly-mistake drill | Orange-flagged cards, shuffled |
| Speed work | Blue-flagged cards |
| Tricks to revise | Green-flagged cards |
| Keep forgetting | Cards forgotten 2+ times |
| TITA practice | Typed-answer questions only |
| Whole passages & sets | Set cards only |

## Examples of what the planner produces
- All algebra questions: `deck:sipe tag:sipe::Card::Question tag:sipe::Topic::QA::Algebra`
- DILR questions I got wrong in the last 14 days: `deck:sipe tag:sipe::Card::Question tag:sipe::Section::DILR rated:14:1`
- Red or orange flags in QA: `deck:sipe tag:sipe::Section::QA (flag:1 OR flag:2)`

The match count shows how many cards fit your topics and filters; history and flags are applied by Anki when you build the deck.
