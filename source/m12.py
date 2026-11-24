# -*- coding: utf-8 -*-
# Simp Mock 12: VARC (24 of 24). DILR and QA: m12_dilr.py, m12_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(12, "sm12.json")
P.passage("V1", "Passage 1 — Bureaucracy and political systems", "Social_Sciences")
P.passage("V2", "Passage 2 — Death as resistance", "Philosophy_and_Psychology")
P.passage("V3", "Passage 3 — Hawking’s information paradox", "Science_and_Technology")
P.passage("V4", "Passage 4 — Material literacy", "Arts_and_Culture")

V = P.Q["VARC"]
V[17]["q"] = V[17]["q"].replace('1. A "competitive" market typically features', '1. Such a "competitive" market typically features')

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Main_Idea", "2", "Easy",
 "Centralized, fragmented, decentralized: what is compared?",
 steps(("The thread", p("The passage shows how the bureaucracy’s role changes with the political system: centralized (UK, France), fragmented (US) and decentralized new democracies.")),
       ("Choosing", p("Option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "Origins and growth are not traced."), ("3", "Developed versus nascent is only part."), ("4", "Hierarchies are not discussed.")])

P.rc(2, "V1", "Except", "4", "Medium",
 "Where is bureaucracy a competitor?",
 steps(("The line", ev(4, "In this situation, bureaucracy is seen as a competitor for political power")),
       ("Choosing", p("That holds in fragmented systems like the US, not in government systems generally: option 4."))) +
 final("Option 4"),
 "except",
 [("1", "Paragraph 3."), ("2", "Paragraph 4."), ("3", "Paragraph 5.")])

P.rc(3, "V1", "Inference", "3", "Medium",
 "Read the sentences after ‘The irony’.",
 steps(("The line", ev(4, "Rather than increasing political control over the bureaucracy, the process lessens it because the bureaucracy supplies its own political legitimacy")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "The cause, not the irony."), ("2", "Popularity is not discussed."), ("4", "A consequence, not the irony.")],
 opts=[V[3]["opts"][0], "Politicians who attack the bureaucracy ironically make it more popular with voters.", V[3]["opts"][2], V[3]["opts"][3]])

P.rc(4, "V1", "Main_Idea", "1", "Easy",
 "Which list covers the whole passage?",
 steps(("Choosing", p("Bureaucracy, political systems, institutions, decentralization and the politicization of bureaucracy in fragmented systems: option 1."))) +
 final("Option 1"),
 "inference",
 [("2", "Misses decentralization and politicization."), ("3", "Direct democracy and instability are not discussed."), ("4", "Details only.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Inference", "3", "Medium",
 "Who lives in ‘death-worlds’?",
 steps(("The line", ev(1, "This power, has led to the creation of ‘death-worlds’ inhabited by ‘living dead’")),
       ("Choosing", p("The ‘living dead’ are those living under necropolitical power: option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "They are living."), ("2", "Too narrow."), ("4", "Resisters are a separate idea.")])

P.rc(6, "V2", "Inference", "4", "Medium",
 "Non-nihilistic = meaningful; subject-formation = identity.",
 steps(("The line", ev(2, "Confronting death, whether as an individual or collective, inevitably transforms the subjective experience of the living")),
       ("Choosing", p("Option 4."))) +
 final("Option 4"),
 "inference",
 [("1", "Hegel says it does serve an end."), ("2", "Not acceptance."), ("3", "Resistance is Eagleton’s and Bargu’s angle.")])

P.rc(7, "V2", "Main_Idea", "2", "Medium",
 "Theology even among the nonreligious.",
 steps(("The line", ev(3, "death, and its attendant rituals and discourses, can assume a theological character even among the nonreligious")),
       ("Choosing", p("Option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "She offers it as an alternative."), ("3", "She calls theologisation a precondition, not separation."), ("4", "She describes, not criticises.")])

P.rc(8, "V2", "Except", "4", "Medium",
 "Bargu ties necroresistance to martyrdom.",
 steps(("The line", ev(3, "this form of resistance overlaps with Abrahamic martyrdom")),
       ("Choosing", p("Saying necroresistance has no place in religious contexts contradicts this: option 4."))) +
 final("Option 4"),
 "except",
 [("1", "Fits Mbembe and the resisters."), ("2", "Bargu’s point."), ("3", "Fanon’s point.")],
 q="Which one of the following statements contradicts the passage?",
 opts=["Death can be used both by those in power and by those resisting it.", V[8]["opts"][1], V[8]["opts"][2], V[8]["opts"][3]])

# ---------------- Passage 3 (Q9–12) ----------------
P.rc(9, "V3", "Inference", "3", "Medium",
 "‘Its lack of features’.",
 steps(("The line", ev(1, "But this did not seem to be the case for radiation from black holes")),
       ("Choosing", p("The radiation seemed to carry no information about the system: option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "That pleased, not puzzled."), ("2", "The reverse."), ("4", "That is quantum mechanics’ rule, not the puzzle.")])

P.rc(10, "V3", "Inference", "4", "Easy",
 "‘The amount of information in a system doesn’t change’.",
 steps(("The line", ev(3, "The amount of information in a system doesn’t change, though it may be hard to access")),
       ("Choosing", p("Option 4."))) +
 final("Option 4"),
 "inference",
 [("1", "Not in the passage."), ("2", "That is Hawking’s challenge."), ("3", "Contradicts the line.")])

P.rc(11, "V3", "Except", "4", "Medium",
 "How far did string theory go?",
 steps(("The line", ev(5, "That concept has provided at least a partial resolution of the puzzle")),
       ("Choosing", p("String theory explained only certain idealised black holes, so option 4 is not part of the paradox."))) +
 final("Option 4"),
 "except",
 [("1", "Paragraph 1."), ("2", "Paragraph 3."), ("3", "Paragraph 1.")],
 q="Based on the passage, all of the following are part of Hawking’s paradox EXCEPT:",
 opts=["Hawking radiation brought general relativity and quantum theory together.", "Information about a collapsing star seemed to be reduced to the temperature of a warm body.",
       "Black holes seemed to break the rule that the probabilities of all outcomes add up to one.", "String theory has fully explained the radiation of all black holes."])

P.rc(12, "V3", "Inference", "2", "Medium",
 "What do the sceptics claim about the burning log?",
 steps(("The line", ev(4, "the outgoing radiation is not exactly that of a black body because subtle connections between the outgoing photons remain intact")),
       ("Choosing", p("In both cases information only looks lost: option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "Not the reason for the comparison."), ("3", "Not the point of comparison."), ("4", "Energy is not discussed.")],
 opts=[V[12]["opts"][0], "In both, information about the starting state looks lost but may survive in subtle correlations in what is given off.", V[12]["opts"][2], V[12]["opts"][3]])

# ---------------- Passage 4 (Q13–16) ----------------
P.rc(13, "V4", "Except", "1", "Easy",
 "Who does formal visual analysis favour?",
 steps(("The line", ev(2, "This approach also draws attention to makers who have marked their products or appeared in written records")),
       ("Choosing", p("That bias belongs to the approach the author criticises: option 1."))) +
 final("Option 1"),
 "except",
 [("2", "Paragraph 3."), ("3", "Last paragraph."), ("4", "Last paragraph.")])

P.rc(14, "V4", "Main_Idea", "2", "Medium",
 "‘True sense of the conditions of its creation’.",
 steps(("The line", ev(2, "It is often the evidence of the unconscious act of the maker—the substrate, interior, or back rather than the surface, exterior, or front—that provide a true sense of the conditions of its creation")),
       ("Choosing", p("Option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "A supporting point."), ("3", "They used raffia, not the same materials."), ("4", "The point is adaptation, not exchange.")])

P.rc(15, "V4", "Weaken", "3", "Medium",
 "The progressive model: today’s work is the most advanced.",
 steps(("The line", ev(3, "we can divest ourselves of the notion that technology has continually improved")),
       ("Choosing", p("A 2000-year-old pot made with techniques still in use shows old work can match today’s: option 3."))) +
 final("Option 3"),
 "weaken",
 [("1", "Supports it."), ("2", "Supports it."), ("4", "Supports it.")],
 opts=[V[15]["opts"][0], V[15]["opts"][1], V[15]["opts"][2], "Roman aqueducts were later replaced by modern pipelines that carry far more water."])

P.rc(16, "V4", "Inference", "1", "Medium",
 "‘More comfortable with approximations’.",
 steps(("The line", ev(1, "when we have become distant from making and are more comfortable with approximations")),
       ("Choosing", p("Digitized images stand in for real objects: option 1."))) +
 final("Option 1"),
 "inference",
 [("2", "No such ranking."), ("3", "The author rejects this."), ("4", "Objects arise from specific contexts.")],
 q="Which of the following is supported by the passage?")

# ---------------- Verbal ability (Q17–24) ----------------
P.va(17, P.sent_html(17), [], "TITA", "4132", "Para_Jumble", "Medium",
 "Competition, such a market, despite this, deviations.",
 steps(("Order", p("4 says how competition arises. 1 ‘Such a competitive market’ defines it. 3 ‘Despite this’ notes pockets of power. 2 says deviations must be weighed."))) +
 final("4132"),
 "pj",
 [("4", "Opens."), ("1", "“Such”."), ("3", "“Despite this”."), ("2", "Conclusion.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.sent_html(18), [], "TITA", "3142", "Para_Jumble", "Easy",
 "Contrast, problem, response, hybrid.",
 steps(("Order", p("3 contrasts the theories and flags a problem. 1 names it. 4 ‘In response’ some mix them. 2 ‘This hybrid theory’."))) +
 final("3142"),
 "pj",
 [("3", "Opens."), ("1", "The problem."), ("4", "Response."), ("2", "“This hybrid”.")],
 why_title="Why each sentence goes where it does")

P.va(19, P.sent_html(19), [], "TITA", "2143", "Para_Jumble", "Easy",
 "Charge, additionally, more harm, conclusion.",
 steps(("Order", p("2 states the neglect. 1 ‘Additionally’ legal challenges. 4 disinformation. 3 ‘Given this history’ governments respond."))) +
 final("2143"),
 "pj",
 [("2", "Opens."), ("1", "“Additionally”."), ("4", "Further harm."), ("3", "Conclusion.")],
 why_title="Why each sentence goes where it does")

P.va(20, P.missing_html(20), P.strict_opts(20), "MCQ", "4", "Missing_Sentence", "Easy",
 "‘They pose certain challenges’ needs one named.",
 steps(("Find the spot", p("Blank 4 follows ‘they pose certain challenges’; the sentence names one."))) +
 final("Option 4"),
 "missing",
 [("1", "Censorship not yet raised."), ("2", "Before censorship is proposed."), ("3", "Before ‘Nevertheless’.")])

P.va(21, P.missing_html(21), P.strict_opts(21), "MCQ", "2", "Missing_Sentence", "Medium",
 "‘These features’ needs features just before it.",
 steps(("Find the spot", p("After blank 2 comes ‘These features can potentially reshape the financial system, promoting more secure and private transactions’. Security and privacy must be named just before.")),
       ("Check", p("At blank 1 the sentence would be followed by decentralized networks, not ‘these features’."))) +
 final("Option 2"),
 "missing",
 [("1", "‘These features’ would then refer to decentralized networks."), ("3", "Benefits already given."), ("4", "Among the problems.")])

P.va(22, P.summary_html(22, "Like great works, deep feelings"), V[22]["opts"], "MCQ", "4", "Summary", "Medium",
 "Hidden meaning, habits, universes, beauty and absurdity.",
 steps(("What the passage says", "<ol><li>Deep feelings mean more than they say and shape habits unconsciously.</li><li>Great feelings create their own universes.</li><li>This is even truer of emotions from beauty or absurdity.</li></ol>"),
       ("Choosing", p("Option 4."))) +
 final("Option 4"),
 "summary",
 [("1", "Drops the universes."), ("2", "Drops the unconscious shaping."), ("3", "Mixes up which feelings light which worlds.")])

P.va(23, P.summary_html(23, "All of Dostoevsky’s heroes"), V[23]["opts"], "MCQ", "1", "Summary", "Medium",
 "Modern questioning, extremes, artist.",
 steps(("What the passage says", "<ol><li>His heroes ask about the meaning of life: a modern, metaphysical concern.</li><li>The intensity invites extreme answers.</li><li>He shows the consequences in a life: an artist.</li></ol>"),
       ("Choosing", p("Option 1."))) +
 final("Option 1"),
 "summary",
 [("2", "Drops why he is an artist."), ("3", "Calls him a philosopher artist."), ("4", "Reverses the shift.")])

P.va(24, P.summary_html(24, "Idleness, it is usually said"), [V[24]["opts"][0],
     "The common view that idleness breeds evil is dismissed as low-born: idleness without boredom is a divine good, boredom is the real evil, and not valuing idleness shows one has not risen to full humanity.",
     V[24]["opts"][2], V[24]["opts"][3]], "MCQ", "2", "Summary", "Medium",
 "Rejection, the true evil, the last line.",
 steps(("What the passage says", "<ol><li>The view that idleness is evil is plebeian.</li><li>Idleness without boredom is divine; boredom is the evil.</li><li>Not valuing idleness shows one has not risen to humanity.</li></ol>"),
       ("Choosing", p("Option 2."))) +
 final("Option 2"),
 "summary",
 [("1", "Drops the last point."), ("3", "‘Understanding of humanity’ misreads."), ("4", "‘Ridiculous’ and ‘understanding’ misread.")])
