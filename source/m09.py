# -*- coding: utf-8 -*-
# Simp Mock 9: VARC (24 of 24). DILR and QA: m09_dilr.py, m09_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(9, "sm09.json")
P.passage("V1", "Passage 1 — The virtuous circle", "Economics_and_Management")
P.passage("V2", "Passage 2 — How corals feed", "Science_and_Technology")
P.passage("V3", "Passage 3 — Costly signals", "Economics_and_Management")
P.passage("V4", "Passage 4 — What addicts crave", "Science_and_Technology")

V = P.Q["VARC"]
V[20]["q"] = V[20]["q"].replace("Sentence: Happiness is not something ready-made; it comes from your own actions.",
                                "Sentence: Happiness is not only something we feel; it also comes from what we do.")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Except", "1", "Medium",
 "Separate what a pluralistic society is from how it comes about.",
 steps(("What the passage lists", p("Pluralism makes usurping power hard (checks on power), brings the rule of law, and widens equal participation in politics.")),
       ("The odd one", p("Conflict between elites and their opponents is how inclusive institutions emerge, not a feature of the society once it exists: option 1."))) +
 final("Option 1"),
 "except",
 [("2", "‘Equal … in the political system’."), ("3", "Paragraphs 2 and 3."), ("4", "The virtuous circle.")],
 q="According to the passage, all of the following are features of a pluralistic society EXCEPT:",
 opts=[V[1]["opts"][0], V[1]["opts"][1], V[1]["opts"][2], "A tendency for inclusive institutions to persist and expand."])

P.rc(2, "V1", "Main_Idea", "3", "Easy",
 "Paragraph 1 defines the circle as positive feedback.",
 steps(("The line", ev(1, "inclusive economic and political institutions tend to create a virtuous circle, a process of positive feedback")),
       ("Choosing", p("Option 3: the mechanisms keep the institutions going through feedback."))) +
 final("Option 3"),
 "inference",
 [("1", "How the institutions arise, not the circle."), ("2", "Monopolies are what inclusive institutions reduce."), ("4", "The reverse of the passage.")])

P.rc(3, "V1", "Inference", "2", "Easy",
 "Paragraph 2 makes one point.",
 steps(("The line", ev(2, "as Franklin Roosevelt discovered when he tried to remove the checks on his power imposed by the Supreme Court")),
       ("Choosing", p("Option 2 says exactly this."))) +
 final("Option 2"),
 "inference",
 [("1", "‘Unreasonably’ is not in the text."), ("3", "Nothing about populist policies."), ("4", "Nothing about popularity.")],
 opts=[V[3]["opts"][0], "Pluralistic institutions stopped Franklin Roosevelt when he tried to remove the checks the Supreme Court placed on his power.", V[3]["opts"][2], V[3]["opts"][3]])

P.rc(4, "V1", "Inference", "4", "Easy",
 "Read the last paragraph’s first sentence.",
 steps(("The line", ev(5, "a free media often provides information about and mobilizes opposition to threats against inclusive institutions")),
       ("Choosing", p("Option 4 restates it."))) +
 final("Option 4"),
 "inference",
 [("1", "Opposition to criticism of the government: reversed."), ("2", "Not in the passage."), ("3", "Threats to the government, not to institutions.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Main_Idea", "3", "Medium",
 "Every paragraph comes back to how corals get energy.",
 steps(("The thread", p("Paragraphs 1–2: two ways corals feed. Paragraph 3: development blocks the light the algae need. Paragraph 4: heat makes corals expel the algae and starve.")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "Beauty and conservation are not the theme."), ("2", "Leaves out the feeding."), ("4", "Extinction is not discussed.")],
 opts=["The beauty of coral reefs and the conservation work needed to protect them.", V[5]["opts"][1], V[5]["opts"][2], V[5]["opts"][3]])

P.rc(6, "V2", "Except", "4", "Easy",
 "Corals need clear water.",
 steps(("The line", ev(2, "clear water, transparent to sunlight, is of paramount importance for the flourishing of a classic coral reef")),
       ("Choosing", p("Clear, low-nutrient water helps corals: option 4."))) +
 final("Option 4"),
 "except",
 [("1", "Feeds rival algae."), ("2", "Corals starve."), ("3", "Algae make harmful reactive oxygen.")])

P.rc(7, "V2", "Except", "2", "Easy",
 "What does a seawall do compared with mangroves?",
 steps(("The line", ev(3, "a concrete seawall will filter rainwater flowing into the ocean much less efficiently than an intact mangrove forest")),
       ("Choosing", p("A seawall filters less, so more nutrients reach the sea. Option 2 says the opposite."))) +
 final("Option 2"),
 "except",
 [("1", "Mangroves filter better."), ("3", "Reclamation destroys reefs."), ("4", "Poor waste treatment harms them.")])

P.rc(8, "V2", "Inference", "3", "Easy",
 "What do corals do when the algae make too much reactive oxygen?",
 steps(("The line", ev(4, "Responding to that emergency, corals repulse the algae from their bodies")),
       ("Choosing", p("Bleaching is the loss of colour that follows expelling the algae: option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "Corals do not react with oxygen."), ("2", "Death may follow later."), ("4", "A cause, not the meaning.")])

# ---------------- Passage 3 (Q9–12) ----------------
P.rc(9, "V3", "Weaken", "4", "Medium",
 "The argument rests on the link between ability and cost.",
 steps(("The line", ev(3, "In general, having the qualities that employers value makes it easier to get a degree")),
       ("Choosing", p("If those qualities did not make a degree easier, the degree would signal nothing: option 4."))) +
 final("Option 4"),
 "weaken",
 [("1", "Concerns how peahens perceive, not whether the cost is honest."), ("2", "Which qualities are valued does not matter."), ("3", "Other signals can coexist.")])

P.rc(10, "V3", "Inference", "3", "Easy",
 "‘Honest because … costly’.",
 steps(("The line", ev(5, "Costly signals – signals that are honest because of the fact that they are costly – are ubiquitous")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "Opposite: they are honest."), ("2", "Not about admiration."), ("4", "Self-selection, not elimination.")])

P.rc(11, "V3", "Inference", "2", "Easy",
 "Why do employers not simply ask?",
 steps(("The line", ev(2, "Communication is difficult because individuals have incentives to lie")),
       ("Choosing", p("Option 2 follows directly."))) +
 final("Option 2"),
 "inference",
 [("1", "The passage says talk is unreliable."), ("3", "Communication is unreliable."), ("4", "The passage stresses even an unrelated degree.")],
 q="Which of the following is supported by the passage?")

P.rc(12, "V3", "Except", "1", "Easy",
 "Which trait is not expensive display?",
 steps(("The idea", ev(5, "only the peacocks in good enough condition can afford to grow an elaborate tail")),
       ("Choosing", p("Manes, displays and elaborate songs are costly displays only the fit can afford. A chameleon’s colour change is camouflage or warning: option 1."))) +
 final("Option 1"),
 "except",
 [("2", "A costly ornament."), ("3", "Wasting energy to show fitness."), ("4", "Elaborate song.")])

# ---------------- Passage 4 (Q13–16) ----------------
P.rc(13, "V4", "Main_Idea", "2", "Easy",
 "‘In truth …’.",
 steps(("The line", ev(1, "In truth, addictive cravings seek out vital emotional experiences")),
       ("Choosing", p("Option 2 names the real object of craving, the paragraph’s claim."))) +
 final("Option 2"),
 "inference",
 [("1", "The view it criticises; does not give the claim."), ("3", "A method, not the claim."), ("4", "A detail.")])

P.rc(14, "V4", "Except", "1", "Medium",
 "Which is not about dopamine and reward?",
 steps(("Choosing", p("Options 2–4 come from paragraphs 2–4 on dopamine. Elusive emotional experiences are the author’s own alternative, not part of the reward system: option 1."))) +
 final("Option 1"),
 "except",
 [("2", "Paragraph 2."), ("3", "Paragraph 3."), ("4", "Paragraph 4.")])

P.rc(15, "V4", "Inference", "2", "Medium",
 "Paragraph 3: two bursts of dopamine.",
 steps(("The line", ev(3, "these boosts in dopamine trigger cravings that overestimate the amount of reward that is expected")),
       ("Choosing", p("Option 2: the drug adds a second burst, so the reward seems bigger."))) +
 final("Option 2"),
 "inference",
 [("1", "Dependence is not mentioned."), ("3", "The author’s alternative, not paragraph 3."), ("4", "A decrease is the reverse.")],
 opts=[V[15]["opts"][0], "The drug adds a chemical burst of dopamine on top of the anticipatory one, so cravings overestimate the reward.", V[15]["opts"][2], V[15]["opts"][3]])

P.rc(16, "V4", "Except", "4", "Easy",
 "Implications of ‘not automatic, not chronic’.",
 steps(("Choosing", p("Options 1–3 follow from addiction being avoidable and treatable. Option 4 is about neuroscience, not the quoted claim."))) +
 final("Option 4"),
 "except",
 [("1", "‘Not automatic’."), ("2", "If not automatic, vulnerability differs."), ("3", "‘Not chronic’.")])

# ---------------- Verbal ability (Q17–24) ----------------
P.va(17, P.sent_html(17), [], "TITA", "3124", "Para_Jumble", "Easy",
 "Topic, statistic, however, remedy.",
 steps(("Order", p("3 introduces mobile devices. 1 adds how much we use them. 2 ‘However’ turns to harm. 4 gives the remedy."))) +
 final("3124"),
 "pj",
 [("3", "Opens."), ("1", "Usage."), ("2", "“However”."), ("4", "Remedy.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.sent_html(18), [], "TITA", "3421", "Para_Jumble", "Easy",
 "Poem, its context, one line, its relevance now.",
 steps(("Order", p("3 names the poem. 4 ‘it’ was written during the Russian Civil War. 2 picks one line. 1 applies it to the attack on free speech."))) +
 final("3421"),
 "pj",
 [("3", "Opens."), ("4", "“It”."), ("2", "One line."), ("1", "Present day.")],
 why_title="Why each sentence goes where it does")

P.va(19, P.sent_html(19), [], "TITA", "4321", "Para_Jumble", "Easy",
 "Population, the need, the problem, the fix.",
 steps(("Order", p("4 gives the 2050 population. 3 ‘this growing population’. 2 names a harm of current farming. 1 ‘these challenges’ and solutions."))) +
 final("4321"),
 "pj",
 [("4", "Opens."), ("3", "“This growing population”."), ("2", "The harm."), ("1", "“These challenges”.")],
 why_title="Why each sentence goes where it does")

P.va(20, P.missing_html(20), P.strict_opts(20), "MCQ", "4", "Missing_Sentence", "Easy",
 "The sentence moves from feelings to doing.",
 steps(("Find the spot", p("Before blank 4 the paragraph is on emotions we cultivate; after it come activities we take up. The sentence bridges the two.")),
       ("Check the others", p("Blanks 1–3 come before the emotions point."))) +
 final("Option 4"),
 "missing",
 [("1", "Too early."), ("2", "Breaks ‘external … However’."), ("3", "Before the emotions, not after.")])

P.va(21, P.missing_html(21), P.strict_opts(21), "MCQ", "2", "Missing_Sentence", "Medium",
 "Playfulness goes with risk-taking and experiment.",
 steps(("Find the spot", p("After blank 2 come taking risks, experimenting and embracing ambiguity: play. ‘Intelligence having fun’ introduces that.")),
       ("Check", p("Blank 1 is about exposure, 3 about collaboration, 4 the close."))) +
 final("Option 2"),
 "missing",
 [("1", "Exposure to experiences is not play."), ("3", "Collaboration."), ("4", "The close is about fulfilment.")])

P.va(22, P.summary_html(22, "We may never know"), [V[22]["opts"][0], V[22]["opts"][1],
     "Humans may have ridden horses as early as 3000 B.C.E., though evidence on when horses were tamed and fully domesticated remains patchy and conflicting.", V[22]["opts"][3]],
 "MCQ", "3", "Summary", "Easy",
 "New evidence plus a patchy timeline.",
 steps(("What the passage says", "<ol><li>Riding may date to 3000 B.C.E.</li><li>The timeline is patchy.</li><li>Milking and genetic evidence point to different dates.</li></ol>"),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "summary",
 [("1", "Wrong date for the riding evidence."), ("2", "Milking is not art or riding."), ("4", "Drops the new finding.")])

P.va(23, P.summary_html(23, "The intellectual ethic of a technology"), V[23]["opts"], "MCQ", "2", "Summary", "Medium",
 "What the ethic is, and who misses it.",
 steps(("What the passage says", "<ol><li>Inventors and users overlook a technology’s intellectual ethic.</li><li>Its effects are by-products.</li><li>It is the message a tool transmits, and its effect is the most profound.</li></ol>"),
       ("Choosing", p("Option 2."))) +
 final("Option 2"),
 "summary",
 [("1", "Turns the examples into the claim."), ("3", "Drops what the ethic is."), ("4", "‘Effect … on the intellectual ethic’ misreads.")])

P.va(24, P.summary_html(24, "Insurance is what economists call"), ["Insurance is a selection market; if prices rise, the riskier customers leave, leaving the cheaper ones and making insurance unprofitable.",
     V[24]["opts"][1], V[24]["opts"][2], V[24]["opts"][3]], "MCQ", "3", "Summary", "Medium",
 "Selection market and the spiral.",
 steps(("What the passage says", "<ol><li>Insurance is a selection market needing a mix of customers.</li><li>Higher prices drive out the low-risk ones.</li><li>Costs and prices spiral until cover is too dear or the insurer fails.</li></ol>"),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "summary",
 [("1", "Reverses who leaves."), ("2", "Leaves out the spiral."), ("4", "Drops ‘selection market’.")])
