# -*- coding: utf-8 -*-
# Simp Mock 7: VARC (24 of 24). DILR and QA: m07_dilr.py, m07_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(7, "sm07.json")
P.passage("V1", "Passage 1 — Hot spots and mantle plumes", "Science_and_Technology")
P.passage("V2", "Passage 2 — The amyloid hypothesis", "Science_and_Technology")
P.passage("V3", "Passage 3 — The upsurge in memory", "Social_Science_and_History")
P.passage("V4", "Passage 4 — Multinationals and the new imperialism", "Economics_and_Management")

# Small wording fixes so that each VA item has exactly one defensible answer.
V = P.Q["VARC"]
V[19]["q"] = V[19]["q"].replace("3. Efforts such as education and treatment programs have been made to address the issue of alcohol use disorder, yet its prevalence remains high.", "3. Though these factors are well known and efforts such as education and treatment programs have been made to address alcohol use disorder, its prevalence remains high.")
V[20]["q"] = V[20]["q"].replace("Despite these challenges, it is clear that the shift towards renewable energy is necessary for a sustainable future.",
                                "Despite these challenges, those targets show that the shift towards renewable energy is under way and is necessary for a sustainable future.")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Except", "3", "Easy",
 "Plumes came later, from Wilson and Morgan, to explain what plate tectonics could not.",
 steps(("The line", ev(1, "While the theory provided explanations for questions that had long puzzled scientists — where volcanoes appear, where land is born, where ocean basins are carved out, where ancient crust was annihilated")),
       ("Choosing", p("Options 1, 2 and 4 are what plate tectonics explains. Mantle plumes are a later idea that plate tectonics does not explain: option 3."))) +
 final("Option 3"),
 "except",
 [("1", "The heart of the theory."), ("2", "Volcanoes at plate boundaries."), ("4", "Listed: ‘where ocean basins are carved out’.")],
 opts=["how the Earth’s plates move and interact with each other.", "how volcanoes arise as plates move apart or collide.",
       "how mantle plumes form beneath the Earth’s rocky outer layer.", "where ocean basins are carved out."])

P.rc(2, "V1", "Main_Idea", "3", "Easy",
 "The passage starts with a puzzle and ends with its solution.",
 steps(("The thread", p("Intraplate volcanism (Hawai‘i) puzzled plate tectonics; hot spots and mantle plumes explain it, with evidence from hot spot tracks and helium.")),
       ("Choosing", p("Option 3 holds the puzzle and its explanation."))) +
 final("Option 3"),
 "inference",
 [("1", "Only the evidence half."), ("2", "The chains are away from boundaries."), ("4", "Two people only.")])

P.rc(3, "V1", "Inference", "2", "Medium",
 "Which statement does the passage support?",
 steps(("The line", ev(5, "The combined supply of hot magma neatly explains a great number of Earth’s intraplate volcanoes")),
       ("Choosing", p("Option 2. The others contradict the passage."))) +
 final("Option 2"),
 "inference",
 [("1", "The Ring of Fire is a place, not an explanation for all volcanoes."), ("3", "‘Difficult to explain without invoking plumes’."), ("4", "Morgan said plumes rise from the lower mantle.")],
 q="Which of the following statements is supported by the passage?")

P.rc(4, "V1", "Weaken", "1", "Easy",
 "The argument: lots of helium-3 means deep mantle material, so a plume.",
 steps(("The argument", ev(7, "suggests that these volcanoes are mining mantle matter from considerable depth — and a plume is a reasonable explanation")),
       ("Choosing", p("If boundary volcanoes, which need no plume, also have plenty of helium-3, then helium-3 no longer points to a plume: option 1."))) +
 final("Option 1"),
 "weaken",
 [("2", "Strengthens."), ("3", "Strengthens."), ("4", "Strengthens.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Inference", "3", "Easy",
 "‘Not necessarily.’",
 steps(("The line", ev(6, "Do these results mean the amyloid cascade hypothesis was right? Not necessarily. It does suggest to some researchers that with more coaxing, targeting amyloid could still lead to effective therapeutics")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "‘Not necessarily’ rules out ‘definitively proven’."), ("2", "Too strong."), ("4", "Too strong.")])

P.rc(6, "V2", "Except", "2", "Easy",
 "Which reason is never mentioned?",
 steps(("The reasons", ev(6, "the small to non-existent effect sizes in these trials and earlier ones suggest that amyloid plaques are not the cause of the disease")),
       ("Choosing", p("Plaques appearing before onset is not in the passage: option 2."))) +
 final("Option 2"),
 "except",
 [("1", "Paragraph 2."), ("3", "Larson’s point in paragraph 4."), ("4", "Small’s ‘smoke, not the fire’.")])

P.rc(7, "V2", "Weaken", "3", "Medium",
 "Larson grants statistical significance; he doubts clinical significance.",
 steps(("The argument", ev(4, "statistical significance, which means the results were likely not due to chance, does not always equate to clinical significance")),
       ("Choosing", p("Clear differences noticed by caregivers would show clinical significance: option 3."))) +
 final("Option 3"),
 "weaken",
 [("1", "Not about the drug’s effect."), ("2", "Approval does not show a noticeable difference."), ("4", "About safety, not size of effect.")],
 opts=["A combination of genetic, environmental and lifestyle factors contribute to the onset of AD.",
       "On 6 January 2023, America’s Food and Drug Administration approved lecanemab.",
       "Caregivers of patients on lecanemab reported clearly noticeable improvements in memory and daily functioning.",
       "Patients taking lecanemab experienced no adverse side effects during the clinical trial."])

P.rc(8, "V2", "Inference", "4", "Easy",
 "Two camps appear in the last paragraph.",
 steps(("The line", ev(6, "Many researchers, however, aren’t convinced")),
       ("Choosing", p("Tanzi is thrilled; Small and others are not. The role of amyloid is debated: option 4."))) +
 final("Option 4"),
 "inference",
 [("1", "Its link is not in doubt; its causal role is."), ("2", "One camp’s view."), ("3", "One possibility Tanzi mentions.")])

# ---------------- Passage 3 (Q9–12) ----------------
P.rc(9, "V3", "Except", "2", "Easy",
 "The upsurge criticises official history.",
 steps(("The line", ev(1, "criticism of official versions of history and recovery of areas of history previously repressed")),
       ("Choosing", p("Option 2 reverses this."))) +
 final("Option 2"),
 "except",
 [("1", "The acceleration of history."), ("3", "The democratisation of history."), ("4", "Roots and heritage.")])

P.rc(10, "V3", "Main_Idea", "3", "Medium",
 "What causes the upsurge, and what has it done to memory’s standing?",
 steps(("The thread", p("A world-wide upsurge in memory, driven by the acceleration of history and its democratisation, has given memory new prestige against history.")),
       ("Choosing", p("Option 3 has both causes and the result."))) +
 final("Option 3"),
 "inference",
 [("1", "One cause only."), ("2", "One cause only."), ("4", "A form of the upsurge, not its cause.")],
 opts=["The world is experiencing an acceleration of history that has left people feeling cut off from the past.",
       "The democratisation of history has given rise to diverse memories that affirm the identities of minority groups.",
       "A world-wide upsurge in memory, driven by the acceleration and the democratisation of history, has given memory a prestige that rivals history.",
       "The upsurge in memory is driven by a growing interest in genealogical research and ‘roots’ across countries and social groups."])

P.rc(11, "V3", "Inference", "3", "Medium",
 "Who holds each?",
 steps(("The line", ev(6, "Unlike history, which has always been in the hands of the public authorities, of scholars and specialised peer groups, memory has acquired all the new privileges and prestige of a popular protest movement")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "‘Weaponised’ and ‘repression’ go too far."), ("2", "The three forms are ways of seeing the future."), ("4", "Distancing is a cause of memory, not memory itself.")])

P.rc(12, "V3", "Except", "1", "Easy",
 "Does the sentence say history no longer matters?",
 steps(("The line", p("Memory gains prestige beside history; nothing says history has lost its value.")),
       ("Choosing", p("Option 1 goes too far."))) +
 final("Option 1"),
 "except",
 [("2", "Popular and inclusive."), ("3", "Challenges the experts’ control."), ("4", "Minority memories.")])

# ---------------- Passage 4 (Q13–16) ----------------
P.rc(13, "V4", "Except", "1", "Medium",
 "The irony: a movement meant to ease pressure on capital has increased it.",
 steps(("The line", ev(4, "It is an ironic ending to our consideration of the problem of imperialism that the movement whose origins were connected with alleviating the pressures on capital has ended up by making them worse")),
       ("Choosing", p("Options 2–4 follow from the irony. Undermining national boundaries (option 1) goes further than ‘coexist uneasily’ and is not what the irony is about."))) +
 final("Option 1"),
 "except",
 [("2", "The expansion turned into home-market pressure."), ("3", "The original aim."), ("4", "The paradox itself.")],
 opts=["As MNCs operate across borders, they end up undermining national boundaries and prerogatives.",
       "The very expansion meant to relieve capital has intensified competition at home.",
       "The initial objective of imperialism was to expand capital by gaining access to resources and markets in other countries.",
       "The effects of imperialism and globalisation on the world economy have been paradoxical for economic actors."])

P.rc(14, "V4", "Except", "3", "Easy",
 "Where does the bulk of investment go?",
 steps(("The line", ev(1, "three-quarters of the flow of international investment goes to Europe and Canada and other developed capitalist lands")),
       ("Choosing", p("Option 3 contradicts this."))) +
 final("Option 3"),
 "except",
 [("1", "The first change."), ("2", "Paragraph 2."), ("4", "Paragraphs 2 and 3.")])

P.rc(15, "V4", "Inference", "2", "Medium",
 "‘New imperialism’ is imperialism run by multinationals.",
 steps(("The line", ev(3, "the new imperialism has greatly intensified the competitiveness of the system in its developed homelands")),
       ("Choosing", p("The passage’s new imperialism is multinationals investing abroad for profit and influence: option 2. Option 4 is one of its effects."))) +
 final("Option 2"),
 "inference",
 [("1", "The old, classic imperialism."), ("3", "The overseas capital moved to other developed lands, not from colonies in general."), ("4", "One effect.")])

P.rc(16, "V4", "Main_Idea", "3", "Easy",
 "‘Too soon to foretell’.",
 steps(("The line", ev(4, "It is too soon to foretell the consequences of this internationalization and intensification of competition")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "Not the point."), ("2", "One detail."), ("4", "One detail.")])

# ---------------- Verbal ability (Q17–24) ----------------
P.va(17, P.sent_html(17), [], "TITA", "4312", "Para_Jumble", "Easy",
 "Follow the show in time.",
 steps(("Order", p("4: he takes the stage. 3: he centres himself. 1: lights dim, music starts. 2: he launches into his first song."))) +
 final("4312"),
 "pj",
 [("4", "Takes the stage."), ("3", "Prepares."), ("1", "Music starts."), ("2", "First song.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.sent_html(18), [], "TITA", "3241", "Para_Jumble", "Medium",
 "Context, continuing problems, further complications, the risk.",
 steps(("Order", p("3 sets the scene. 2: differences ‘continue to divide’. 4 ‘further complicated’ things. 1: the result, growing fear of war."))) +
 final("3241"),
 "pj",
 [("3", "Context."), ("2", "Continuing divisions."), ("4", "“Further complicated”."), ("1", "The consequence.")],
 why_title="Why each sentence goes where it does")

P.va(19, P.sent_html(19), [], "TITA", "4123", "Para_Jumble", "Medium",
 "‘These factors’ in sentence 3 points back to sentence 2.",
 steps(("Order", p("4 introduces the problem and its harm. 1 details the harms. 2 gives the contributing factors. 3: though ‘these factors’ are known and efforts made, prevalence stays high."))) +
 final("4123"),
 "pj",
 [("4", "Topic."), ("1", "Harms."), ("2", "Factors."), ("3", "“These factors”: closes.")],
 why_title="Why each sentence goes where it does")

P.va(20, P.missing_html(20), P.strict_opts(20), "MCQ", "1", "Missing_Sentence", "Easy",
 "‘Those targets’ near the end needs the targets mentioned earlier.",
 steps(("Find the spot", p("The last sentence speaks of ‘those targets’, so the sentence must come earlier. Blank 2 would break ‘They’ (renewable sources) from its antecedent; blank 3 would separate ‘these challenges’ from the challenges. Blank 1 is left.")),
       ("Check", p("After ‘reducing our carbon emissions is more important than ever’, countries’ targets follow naturally."))) +
 final("Option 1"),
 "missing",
 [("2", "Breaks ‘They’."), ("3", "Breaks ‘these challenges’."), ("4", "After ‘those targets’.")])

P.va(21, P.missing_html(21), P.strict_opts(21), "MCQ", "2", "Missing_Sentence", "Easy",
 "‘This has been particularly important during the pandemic’: what is ‘this’?",
 steps(("Find the spot", p("At blank 2, the growing popularity and access of online education is ‘this’ that mattered during COVID-19.")),
       ("Check the others", p("At blank 1 it would come before online education is defined; blanks 3 and 4 are after the challenges and the conclusion."))) +
 final("Option 2"),
 "missing",
 [("1", "Before the definition."), ("3", "Among the challenges."), ("4", "After the conclusion.")])

P.va(22, P.summary_html(22, "The discovery"), P.Q["VARC"][22]["opts"], "MCQ", "4", "Summary", "Medium",
 "The new use: partial reprogramming.",
 steps(("What the passage says", "<ol><li>Yamanaka factors can make mature cells embryonic-like, which won a Nobel prize.</li><li>They are now being used for partial reprogramming, to repair tissues and set back ageing.</li><li>Partial reprogramming stops short of pluripotency.</li></ol>"),
       ("Choosing", p("Option 4 has the new use and its key condition."))) +
 final("Option 4"),
 "summary",
 [("1", "Only the prize."), ("2", "Only the stem cell part."), ("3", "Credits the revolution to the ageing potential.")])

P.va(23, P.summary_html(23, "The current assessment tests"), P.Q["VARC"][23]["opts"], "MCQ", "4", "Summary", "Medium",
 "Bias, DSM-5 and subtypes.",
 steps(("What the passage says", "<ol><li>Autism tests show gender (and racial) bias.</li><li>DSM-5 criteria are restrictive, outdated and fit the white male experience.</li><li>They do not separate subtypes.</li></ol>"),
       ("Choosing", p("Option 4."))) +
 final("Option 4"),
 "summary",
 [("1", "Leaves out DSM-5."), ("2", "Leaves out the bias."), ("3", "Says the criteria exclude girls and non-white people: too strong.")])

P.va(24, P.summary_html(24, "Few things"), P.Q["VARC"][24]["opts"], "MCQ", "1", "Summary", "Medium",
 "Steam therapy: history and proof.",
 steps(("What the passage says", "<ol><li>Heat has long been used to soothe the body, as in the Aztec temazcal.</li><li>Science shows steam helps breathing and other ailments.</li><li>Saunas carry the practice on.</li></ol>"),
       ("Choosing", p("Option 1."))) +
 final("Option 1"),
 "summary",
 [("2", "Makes the temazcal about sweating."), ("3", "Too much detail; loses the science."), ("4", "Credits the rocks and herbs as the origin.")])
