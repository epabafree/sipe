# -*- coding: utf-8 -*-
# Simp Mock 11 (2025): VARC (24 of 24). DILR and QA: m25_11_dilr.py, m25_11_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(11, "sm25_11.json", series=2025)
P.passage("V1", "Passage 1 — Who owns the data?", "Economics_and_Management")
P.passage("V2", "Passage 2 — Two myths about poverty", "Social_Science_and_History")
P.passage("V3", "Passage 3 — The cunning of uncertainty", "Philosophy_and_Psychology")
P.passage("V4", "Passage 4 — Are viruses alive?", "Environment_and_Life_Science")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Inference_Except", "1", "Medium",
 "List the two concerns the passage names.",
 steps(("The concerns", ev(1, "First, politically, the business models of tech platforms thrive on engagement and advertising") +
          ev(1, "Second, economically, their data advantage stifles competition") +
          p("Extreme content (2), blocked competition through data (3), and users unable to reclaim their data (4: ‘users lack bargaining power’).")),
       ("The odd one", p("The passage never says they directly manipulate markets through interventions."))) + final("Option 1"),
 "except", [("2", "Political concern."), ("3", "Economic concern."), ("4", "Paragraph 3.")])
P.rc(2, "V1", "Inference", "4", "Easy",
 "What is ‘the real issue’?",
 steps(("The line", ev(2, "The real issue is data access—without it, rivals cannot grow") +
          p("Breaking up firms doesn’t fix the data advantage."))) + final("Option 4"),
 "inference", [("1", "Infrastructure isn’t discussed."), ("2", "Not compared that way."), ("3", "Not the stated reason.")])
P.rc(3, "V1", "Application", "3", "Medium",
 "Scale and network effects come from data; what does the author want for data?",
 steps(("The fix", ev(2, "Ensuring fair data distribution is crucial") +
          p("Fairer, wider access to data addresses the scale advantage."))) + final("Option 3"),
 "inference", [("1", "‘dismantling them may not solve the problem’."), ("2", "Not discussed."), ("4", "Not the author’s remedy.")])
P.rc(4, "V1", "Purpose", "1", "Medium",
 "What is a serf’s relation to the land he works?",
 steps(("The image", ev(4, "Just as feudalism gave way to property rights, data serfdom may eventually be replaced by a fairer system") +
          p("Users produce the data but don’t control it, like serfs on a lord’s land.")),
       ("Why not 4", p("The author says ‘may eventually’, and the whole passage is about action; nothing happens ‘naturally’."))) + final("Option 1"),
 "purpose", [("2", "Close, but the point is the user’s position."), ("3", "The tide ‘is turning’."), ("4", "‘Naturally’ isn’t the claim.")])

P.va(5, P.summary_html(5, "Something is intrinsically"), P.Q["VARC"][5]["opts"], "MCQ", "3", "Summary", "Medium",
 "Intrinsic goods are good in themselves; instrumental goods lead to intrinsic goods or avoid intrinsic bads.",
 steps(("Choosing", p("Option 3 has both definitions, including ‘prevent intrinsic harms’, without relying on the examples."))) + final("Option 3"),
 "summary", [("1", "Leaves out the avoidance of harm."), ("2", "Leaves out the avoidance of harm."), ("4", "Leaves out the avoidance of harm.")])
P.va(6, P.missing_html(6), P.Q["VARC"][6]["opts"], "MCQ", "2", "Missing_Sentence", "Easy",
 "‘Their impact’ today follows the lasting legacy.",
 steps(("Find the spot", p("Blank 4 follows ‘the Silk Roads left a lasting legacy’; the sentence gives present-day evidence.")),
       ("Match the label", p("Blank 4 is choice 2, labelled ‘Option 4’."))) + final("Choice 2 (“Option 4”)"),
 "missing", [("1", "“Option 1”: the history hasn’t been told yet."), ("3", "“Option 3”: in the middle of trade goods."), ("4", "“Option 2”: among the empires.")])

# ---------------- Passage 2 (Q7–10) ----------------
P.rc(7, "V2", "Inference_Except", "3", "Medium",
 "Does the author think poverty can be ended?",
 steps(("The view", ev(6, "Poverty is not natural; it results from deliberate systems and policies") +
          p("Dispossession and policy (1), the flawed race for wealth (2) and dependence on money (4) all fit.")),
       ("The odd one", p("If poverty comes from how property and resources are arranged, changing that arrangement could end it. Option 3 contradicts the author."))) + final("Option 3"),
 "except", [("1", "The first myth’s rebuttal."), ("2", "‘a highway to nowhere’."), ("4", "Money dependence creates poverty.")])
P.rc(8, "V2", "Weaken", "2", "Medium",
 "The main claim: poverty isn’t inevitable.",
 steps(("The claim", ev(1, "The first myth about poverty is that it has always existed and always will")),
       ("The challenge", p("If poverty existed in every society regardless of system, the author’s core argument falls.")),
       ("Why not 1", p("Wealth gaps among hunter-gatherers weaken one example but don’t show poverty in the author’s sense everywhere."))) + final("Option 2"),
 "weaken", [("1", "Narrower than option 2."), ("3", "About efficiency, not inevitability."), ("4", "Supports the author.")])
P.rc(9, "V2", "Inference", "1", "Easy",
 "The ‘highway’ is the economic race; the ‘Wild West’ part lacks protections.",
 steps(("The images", ev(8, "Others resemble the 19th-century ‘Wild West,’ where barefoot travellers are pushed aside") +
          p("Metaphors for an economic system that is unregulated in places and runs on one logic everywhere."))) + final("Option 1"),
 "inference", [("2", "Not a reference to expansion."), ("3", "Not irony about success."), ("4", "Not literal.")])
P.rc(10, "V2", "Inference", "4", "Medium",
 "A few see the danger; what are most people doing?",
 steps(("The line", ev(7, "Most, however, remain busy keeping up, eager to pass those in their way") +
          p("They know about the disparities but are absorbed in their own race."))) + final("Option 4"),
 "inference", [("1", "Not quite: the author says people pity or ignore the poor."), ("2", "Partly true, but not the focus of that line."), ("3", "Governments aren’t described that way.")])

P.va(11, P.missing_html(11), P.Q["VARC"][11]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "Climbing and nesting go with where it lives.",
 steps(("Find the spot", p("Blank 2 follows ‘This nocturnal animal is found in dry grasslands and scrublands’ and comes before what it eats: habits and habitat sit together.")),
       ("Match the label", p("Blank 2 is choice 1, labelled ‘Option 2’."))) + final("Choice 1 (“Option 2”)"),
 "missing", [("2", "“Option 1”: still on its name."), ("3", "“Option 4”: conservation."), ("4", "“Option 3”: habitat loss.")])
P.va(12, P.sent_html(12), [], "TITA", "1", "Odd_One_Out", "Medium",
 "Four sentences are about ageing advanced economies. One turns to other economies.",
 steps(("The chain", p("5 → 4 → 3 → 2: birth rates reshape advanced economies (5); labour shortages and elder care (4); schools closing (3); South Korea’s strollers (2).")),
       ("The odd one", p("Sentence 1 opens a new topic: ageing beyond advanced economies."))) + final("1"),
 "oddone", [("2", "An example."), ("3", "An effect."), ("4", "Examples."), ("5", "The opening.")], why_title="How the other sentences fit")

# ---------------- Passage 3 (Q13–16) ----------------
P.rc(13, "V3", "Detail", "2", "Easy",
 "Why are these elements dismissed?",
 steps(("The line", ev(1, "in part because they flout core beliefs about meritocracy and in part because they seem to contradict the rational commitments of the scientific enterprise") +
          p("They clash with rewards for ability and with scientific rationality."))) + final("Option 2"),
 "detail", [("1", "Not stated."), ("3", "Not stated."), ("4", "Related, but not the reason given.")])
P.rc(14, "V3", "Inference_Except", "4", "Medium",
 "The author treats uncertainty as part of being human, not a defect.",
 steps(("The view", ev(3, "Uncertainty, perhaps even more than self-control, goes hand in hand with being human") +
          p("Uncertainty is part of existence, not a flaw in our systems. The author would disagree with option 4.")),
       ("The others", p("It reasserts itself against control (1), social infrastructure matters (2), and science displaces rather than captures it (3)."))) + final("Option 4"),
 "except", [("1", "Whack-a-mole."), ("2", "Social infrastructures as luck."), ("3", "‘displaced rather than captured’.")])
P.rc(15, "V3", "Inference_Except", "3", "Medium",
 "Does the author say neoliberalism makes people feel secure?",
 steps(("The critique", ev(2, "exposes the poverty of neoliberal policies, which offload the management of uncertainty onto individuals") +
          p("Shifting management onto individuals (1); the need for institutional help (2); social infrastructure as a buffer (4).")),
       ("The odd one", p("A sense of security from individual responsibility is the opposite of the critique."))) + final("Option 3"),
 "except", [("1", "Stated."), ("2", "Implied."), ("4", "Implied.")])
P.rc(16, "V3", "Inference_Except", "3", "Hard",
 "The claim is about where luck comes from, not about how individuals cope.",
 steps(("The claim", ev(2, "one’s access to nurturing social infrastructures is itself a significant source of luck") +
          p("Support matters (1); luck depends on social conditions (2); unequal structures mean unequal luck (4).")),
       ("The odd one", p("Option 3 is about individuals’ own ability to manage uncertainty, a claim about capacity the statement doesn’t make; it speaks only of who has access."))) +
 trap("Option 3 sounds like a natural consequence, but the statement says nothing about individual ability.") + final("Option 3"),
 "except", [("1", "Follows."), ("2", "Follows: access is a matter of fortune."), ("4", "Follows.")])

# ---------------- Passage 4 (Q17–20) ----------------
P.rc(17, "V4", "Tone", "1", "Easy",
 "Explanation (cells, LUCA, virions) plus musing on what being alive means.",
 steps(("The tone", ev(4, "The virus is not the virion. The virus is a process, not a thing") +
          p("Expository and reflective."))) + final("Option 1"),
 "inference", [("2", "There are interpretive insights."), ("3", "It is grounded in science, not abstract."), ("4", "Not alarmist.")])
P.rc(18, "V4", "Inference_Except", "4", "Medium",
 "Does the passage say the boundary is arbitrary?",
 steps(("Supported", p("Viruses resist neat categories (1); all cellular life shares one template (2); viruses shape the balance of species (3).")),
       ("The odd one", p("The passage says viruses alternate between living and nonliving phases; it doesn’t call the boundary arbitrary or a matter of perception."))) + final("Option 4"),
 "except", [("1", "Wimmer’s yes-and-no."), ("2", "LUCA’s template."), ("3", "‘They fundamentally shape the balance of species’.")])
P.rc(19, "V4", "Inference", "2", "Hard",
 "Which statement, if false, gives a true description of viruses?",
 steps(("Negate each", p("Option 2 negated: viral genes do decide their ability to infect, consistent with a virus being its genome’s process. Negating 1, 3 or 4 contradicts the passage (they need cells, lack metabolism, shape species)."))) + final("Option 2"),
 "inference", [("1", "Negation contradicts ‘borrowed hardware’."), ("3", "Negation contradicts ‘no metabolism of their own’."), ("4", "Negation contradicts their impact on species.")])
P.rc(20, "V4", "Purpose", "3", "Medium",
 "What does Wimmer answer?",
 steps(("The line", ev(5, "Viruses, he says, “alternate between nonliving and living phases”") +
          p("His work backs a yes-and-no answer: classification is ambiguous."))) + final("Option 3"),
 "purpose", [("1", "No ethics."), ("2", "Not his point."), ("4", "A detail of his work, not why he’s cited.")])

P.va(21, P.summary_html(21, "To flourish is"), P.Q["VARC"][21]["opts"], "MCQ", "3", "Summary", "Medium",
 "Growth despite failure, with mindfulness, self-compassion and courage.",
 steps(("Choosing", p("Option 3 keeps growth despite failure and all three supports, including courage to embrace imperfection."))) + final("Option 3"),
 "summary", [("1", "‘Learning from it’ shifts the focus."), ("2", "Leaves out courage."), ("4", "Leaves out courage.")])
P.va(22, P.summary_html(22, "Ecuador, once a"), P.Q["VARC"][22]["opts"], "MCQ", "3", "Summary", "Hard",
 "Location → drug hub → violence → crackdown.",
 steps(("Choosing", p("Option 3 follows the causal chain from location to crackdown. Migration is a side effect."))) + final("Option 3"),
 "summary", [("1", "Leaves out the location."), ("2", "Leaves out the location."), ("4", "Puts migration on a level with the crackdown.")])
P.va(23, P.missing_html(23), P.Q["VARC"][23]["opts"], "MCQ", "1", "Missing_Sentence", "Easy",
 "A topic sentence for a list of eras.",
 steps(("Find the spot", p("Blank 1 opens the paragraph; the eras then follow in order.")),
       ("Match the label", p("Blank 1 is choice 1, labelled ‘Option 1’."))) + final("Choice 1 (“Option 1”)"),
 "missing", [("2", "“Option 2”: mid-list."), ("3", "“Option 3”: mid-list."), ("4", "“Option 4”: after the conclusion.")])
P.va(24, P.sent_html(24), [], "TITA", "3", "Odd_One_Out", "Hard",
 "Four sentences trace allies scrambling as US protection fades. One contradicts that.",
 steps(("The chain", p("4 → 2 → 5 → 1: Pax Americana ending (4); the far right unsettles allies (2); allies seek new protectors (5); Japan may rethink nuclear restraint (1).")),
       ("The odd one", p("Sentence 3 puts the defence of freedom on Germany and Japan, which clashes with sentence 5 (Germany seeking ties with Russia)."))) + final("3"),
 "oddone", [("1", "Japan’s response."), ("2", "The cause."), ("4", "The opening."), ("5", "The allies’ responses.")], why_title="How the other sentences fit")
