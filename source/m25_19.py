# -*- coding: utf-8 -*-
# Simp Mock 19 (2025): VARC (24 of 24). DILR and QA: m25_19_dilr.py, m25_19_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(19, "sm25_19.json", series=2025)
P.passage("V1", "Passage 1 — Was settling down a mistake?", "Social_Science_and_History")
P.passage("V2", "Passage 2 — City-killer asteroids", "Science_and_Technology")
P.passage("V3", "Passage 3 — The dirty secret of climate finance", "Economics_and_Management")
P.passage("V4", "Passage 4 — Is the novel dead?", "Arts_and_Literature")


def listed(n, direc):
    parts = [x.strip() for x in P.Q["VARC"][n]["q"].split("\n\n") if x.strip()]
    return f"<p>{direc}</p><ol class=\"sent\">" + "".join(f"<li>{x}</li>" for x in parts[1:]) + "</ol>"


# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Inference", "4", "Easy",
 "Harari sees a fall; what do Graeber and Wengrow see?",
 steps(("The line", ev(3, "Humans moved fluidly between nomadic and sedentary lifestyles, experimenting with many forms of “civilization.”") +
          p("History as experiment and change, not a one-way slide."))) + final("Option 4"),
 "inference", [("1", "That is closer to Harari."), ("2", "They don’t weigh benefits."), ("3", "Not their claim.")])
P.rc(2, "V1", "Inference", "3", "Medium",
 "Whose ideological weight?",
 steps(("The line", ev(4, "These debates on human origins often serve as mirrors for our current anxieties") +
          p("‘Their descendants’ are us: we load our own debates onto them.")),
       ("Why not 1", p("The point is about our interpretations, not their capacity for thought."))) + final("Option 3"),
 "inference", [("1", "Not about their minds."), ("2", "Overstates."), ("4", "Not the point.")])
P.rc(3, "V1", "Purpose", "2", "Easy",
 "‘archaeology became poetry’.",
 steps(("The line", ev(7, "In that moment, archaeology became poetry—a fleeting human gesture preserved across millennia") +
          p("A tiny object brings a felt link with an ancient person."))) + final("Option 2"),
 "purpose", [("1", "Not about limits."), ("3", "Not about groundwork."), ("4", "Dating isn’t the point.")])
P.rc(4, "V1", "Inference", "1", "Easy",
 "What does the author recommend instead of grand narratives?",
 steps(("The line", ev(6, "studying what little remains without imposing grand theories") +
          p("Grand theories flatten a messy process."))) + final("Option 1"),
 "inference", [("2", "Harari’s view."), ("3", "Not said."), ("4", "Not said.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Detail_Not_True", "2", "Easy",
 "Is origin given as a reason for headlines?",
 steps(("The headlines", ev(2, "made headlines due to its size—40-90m wide—and a 1.2% chance of hitting Earth") +
          p("Size and city-scale damage (3), the threshold (1) and the shifting risk (4).")),
       ("The odd one", p("Its probable origin is mentioned later, not as why it made news."))) + final("Option 2"),
 "except", [("1", "Crossed the threshold."), ("3", "‘city killer’."), ("4", "3.1% then 0.001%.")])
P.rc(6, "V2", "Inference_Except", "3", "Medium",
 "What did missions actually do?",
 steps(("Supported", ev(6, "Dart, in 2022, was the first mission to alter an asteroid’s orbit intentionally") +
          p("Insights for defence (1), dual aims (2), changing an orbit (4).")),
       ("The odd one", p("Structure and risk come up in paragraph 5, but no mission is said to have assessed an asteroid’s risk from its structure."))) + final("Option 3"),
 "except", [("1", "‘expanded our knowledge’."), ("2", "Fast’s quote."), ("4", "Dart.")])
P.rc(7, "V2", "Detail_Not_True", "3", "Easy",
 "What sends asteroids inward?",
 steps(("The line", ev(3, "Jupiter’s gravity can occasionally nudge them toward the inner Solar System") +
          p("Gravity, not composition, does the nudging.")),
       ("The others", p("Air bursts (1), damage (2) and crater versus blast (4) depend on composition and structure."))) + final("Option 3"),
 "except", [("1", "Rubble piles."), ("2", "Iron-rich."), ("4", "YR4.")])
P.rc(8, "V2", "Purpose", "3", "Medium",
 "Has early deflection been shown to work?",
 steps(("Shown", p("Chelyabinsk shows real harm (1); Psyche 16 shows composition matters for science and value (2); missions grew knowledge (4).")),
       ("The odd one", ev(6, "proving we might deflect a dangerous one in the future") +
          p("Dart shows deflection might work; nothing says effective measures can be put in place once a risk is spotted."))) + final("Option 3"),
 "except", [("1", "Chelyabinsk."), ("2", "Psyche 16."), ("4", "Galileo to Dart.")])

P.va(9, P.ms(9), P.Q["VARC"][9]["opts"], "MCQ", "4", "Missing_Sentence", "Easy",
 "An example of Hollywood’s villain AI.",
 steps(("Find the spot", p("Blank 1 follows ‘Artificial Intelligence has often played the villain in Hollywood’; ‘But in real life’ then contrasts.")),
       ("Match the label", p("Blank 1 is choice 4, labelled ‘Option 1’."))) + final("Choice 4 (“Option 1”)"),
 "missing", [("1", "“Option 2”: real-life critics already in view."), ("2", "“Option 3”: about studios."), ("3", "“Option 4”: the ending.")])
P.va(10, P.summary_html(10, "This realization began"), P.Q["VARC"][10]["opts"], "MCQ", "1", "Summary", "Medium",
 "The contrast, and where it led.",
 steps(("The core", p("Seeing empty lives amid plenty and rich lives amid poverty sent the author to theology and its universal questions.")),
       ("Choosing", p("Option 1 keeps the contrast and the turn to theology."))) + final("Option 1"),
 "summary", [("2", "Drops theology."), ("3", "‘rejection of theology’ inverts it."), ("4", "‘futility of the human experience’ distorts.")])
P.va(11, listed(11, P.ODD_DIR), [], "TITA", "3", "Odd_One_Out", "Medium",
 "Dependence, uses, finite supply, precarious future.",
 steps(("The chain", p("2 → 4 → 1 → 5: we depend on helium; its uses; it is finite; growing risk.")),
       ("The odd one", p("Sentence 3 is a statistic about hospitals that breaks the general chain."))) + final("3"),
 "oddone", [("1", "Finite."), ("2", "Opening."), ("4", "Uses."), ("5", "Conclusion.")], why_title="How the other sentences fit")

# ---------------- Passage 3 (Q12–15) ----------------
P.rc(12, "V3", "Main_Idea", "4", "Medium",
 "Diversion, stretched definitions, and unmet needs.",
 steps(("The scope", ev(3, "But this vision ignores what poor countries actually need") +
          p("The passage covers rebranded aid, opaque definitions and a mismatch with real needs.")),
       ("Choosing", p("Options 1–3 each take one part."))) + final("Option 4"),
 "summary", [("1", "One part."), ("2", "One part."), ("3", "One part.")])
P.rc(13, "V3", "Inference_Except", "2", "Medium",
 "Rebranding is calling old or unrelated spending ‘climate finance’.",
 steps(("Rebranding", ev(1, "Britain, for instance, classifies climate finance as part of its 0.5 percent aid target") +
          p("Counting aid (1), tagging loans with co-benefits (3), cutting aid to fund climate goals (4).")),
       ("The odd one", p("Money channelled through foreign consultants is a different problem: who gets the funds."))) + final("Option 2"),
 "except", [("1", "Britain."), ("3", "World Bank."), ("4", "Diverted aid.")])
P.rc(14, "V3", "Purpose", "3", "Easy",
 "Read the sentence after the examples.",
 steps(("The line", ev(2, "There are no uniform rules on what qualifies as climate finance, and no obligation for transparency") +
          p("The odd projects show there is no rulebook."))) + final("Option 3"),
 "purpose", [("1", "Not the point made."), ("2", "The opposite."), ("4", "A later paragraph.")])
P.rc(15, "V3", "Tone", "2", "Easy",
 "‘The dirty secret’.",
 steps(("Tone", p("The author exposes flaws in how climate finance works: critical."))) + final("Option 2"),
 "inference", [("1", "Takes a stance."), ("3", "More than informing."), ("4", "Concern is part, but critique dominates.")])

P.va(16, P.summary_html(16, "The word civility"), P.Q["VARC"][16]["opts"], "MCQ", "1", "Summary", "Medium",
 "Two concepts and the leaders’ role.",
 steps(("The core", p("Civility is the baseline; respect takes deliberate habits; leaders shape culture most.")),
       ("Choosing", p("Option 1 covers all three."))) + final("Option 1"),
 "summary", [("2", "‘later add-on’ is not said."), ("3", "Leaves out civility."), ("4", "Dismisses respect.")])

# ---------------- Passage 4 (Q17–20) ----------------
P.rc(17, "V4", "Tone", "1", "Medium",
 "Why might TV viewers find the complaint ‘comforting’?",
 steps(("The line", ev(1, "can feel they are engaging with culture's dominant narrative form rather than just relaxing") +
          p("A wry dig at viewers justifying the remote: ironic."))) + final("Option 1"),
 "inference", [("2", "Not dismissive."), ("3", "No nostalgia."), ("4", "Not attacking television.")])
P.rc(18, "V4", "Inference", "3", "Easy",
 "Not dead, but not central.",
 steps(("The line", ev(1, "But neither are they as culturally central as they were in the 1900s") +
          p("Still produced in quantity, less central."))) + final("Option 3"),
 "inference", [("1", "‘Novels are not, in fact, dying’."), ("2", "Not strong now."), ("4", "Not said.")])
P.rc(19, "V4", "Purpose", "4", "Medium",
 "Old beliefs meeting a broken world.",
 steps(("The line", ev(4, "Reconciling beliefs nurtured in a stable world with an unstable one produced towering works") +
          p("Ways of handling a chaotic world and inner conflict."))) + final("Option 4"),
 "purpose", [("1", "Not about national preferences."), ("2", "That is Dostoyevsky’s narrator."), ("3", "Not abstraction.")])
P.rc(20, "V4", "Detail", "3", "Easy",
 "Social mores and inner lives; then form.",
 steps(("The line", ev(2, "writers responded to a rapidly changing world by experimenting with form, structure and subject") +
          p("Society and character, then experiments in form."))) + final("Option 3"),
 "detail", [("1", "‘completely abandoned’ overstates."), ("2", "Not said."), ("4", "Not said.")])

P.va(21, P.summary_html(21, "Sustainability is a strategic"), P.Q["VARC"][21]["opts"], "MCQ", "4", "Summary", "Medium",
 "Strategy, not trade-off; business plus government.",
 steps(("The core", p("Sustainability is strategic: firms show it pays, and governments must steady expectations through public-private initiatives.")),
       ("Choosing", p("Option 4 keeps both parts."))) + final("Option 4"),
 "summary", [("1", "Vague about who acts."), ("2", "Misses the profitability point."), ("3", "Too general.")])
P.va(22, P.ms(22), P.Q["VARC"][22]["opts"], "MCQ", "4", "Missing_Sentence", "Medium",
 "‘This is where to begin’ asks for a where.",
 steps(("Find the spot", p("Blank 4 comes after ‘this is where to begin’ and names the place: the agri-food sector.")),
       ("Match the label", p("Blank 4 is choice 4."))) + final("Option 4"),
 "missing", [("1", "Before agriculture is raised."), ("2", "Repeats the next point too early."), ("3", "Mid-argument.")])
P.va(23, P.ms(23), P.Q["VARC"][23]["opts"], "MCQ", "3", "Missing_Sentence", "Medium",
 "From use to meaning.",
 steps(("Find the spot", p("Blank 3 follows ‘its presence is cultural too’; the sweat, dust and pride are that cultural weight.")),
       ("Match the label", p("Blank 3 is choice 3."))) + final("Option 3"),
 "missing", [("1", "Before the uses."), ("2", "Before the list of uses."), ("4", "After the closing line.")])
P.va(24, listed(24, P.ODD_DIR), [], "TITA", "2", "Odd_One_Out", "Medium",
 "A history of street-style photography.",
 steps(("The chain", p("4 → 3 → 5 → 1: Edwardian posing; candid moments; social media; fashion rewritten from the street.")),
       ("The odd one", p("Sentence 2 is about brands copying street style, outside the photography thread."))) + final("2"),
 "oddone", [("1", "Conclusion."), ("3", "The shift."), ("4", "Opening."), ("5", "Today.")], why_title="How the other sentences fit")
