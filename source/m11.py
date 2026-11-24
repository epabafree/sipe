# -*- coding: utf-8 -*-
# Simp Mock 11: VARC (24 of 24). DILR and QA: m11_dilr.py, m11_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(11, "sm11.json")
P.passage("V1", "Passage 1 — Birds that lose their way", "Science_and_Technology")
P.passage("V2", "Passage 2 — The myth of learning styles", "Philosophy_and_Psychology")
P.passage("V3", "Passage 3 — Feelings as numbers", "Economics_and_Management")
P.passage("V4", "Passage 4 — Colouring the brain", "Science_and_Technology")

V = P.Q["VARC"]

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Main_Idea", "3", "Easy",
 "What does the new paper explore?",
 steps(("The line", ev(1, "disturbances to Earth's magnetic field can lead birds astray")),
       ("Choosing", p("The passage is built around the link between geomagnetic disturbance and vagrancy: option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "Too broad; weather is set aside."), ("2", "Vague about the cause."), ("4", "Weather is not studied.")])

P.rc(2, "V1", "Inference", "4", "Easy",
 "Paragraph 2’s first sentence.",
 steps(("The line", ev(2, "assessing the causes of vagrancy could help scientists better understand the threats birds face and the ways they adapt to those threats")),
       ("Choosing", p("Option 4 restates it."))) +
 final("Option 4"),
 "inference",
 [("1", "Conservation strategies are not mentioned."), ("2", "Not said to cause the decline."), ("3", "Not said that they cannot return.")])

P.rc(3, "V1", "Inference", "3", "Medium",
 "Disturbed fields should matter only if birds use them.",
 steps(("The line", ev(5, "a strong correlation between birds that were captured far outside of their expected range and the geomagnetic disturbances")),
       ("Choosing", p("If birds stray just when the field is disturbed, they must have been relying on it: option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "In familiar areas they use geography."), ("2", "Success under disturbance suggests other cues."), ("4", "Weather, not magnetism.")],
 q="Which observation would most strongly suggest that birds rely on magnetoreceptors to navigate?")

P.rc(4, "V1", "Inference", "2", "Medium",
 "The last paragraph has a surprise and an exception.",
 steps(("The lines", ev(6, "To their surprise, solar activity actually reduced the incidence of vagrancy") + ev(6, "birds that migrate during the day were generally exceptions to this rule—they were more affected by solar activity")),
       ("Choosing", p("Option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "Invented reasoning; vagrancy not eliminated."), ("3", "Vagrancy fell."), ("4", "Day migrants were affected.")],
 opts=[V[4]["opts"][0], "Solar activity generally reduced vagrancy, but birds that migrate by day were more affected by it.", V[4]["opts"][2], V[4]["opts"][3]])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Except", "3", "Easy",
 "What decides how well a method works?",
 steps(("The line", ev(6, "The effectiveness of learning methods is determined more by the nature of the material being learned than by subjective preferences")),
       ("Choosing", p("Option 3 reverses the author’s point, so it is not one of the problems raised."))) +
 final("Option 3"),
 "except",
 [("1", "Paragraphs 3 and 5."), ("2", "Paragraph 6."), ("4", "Paragraph 5.")])

P.rc(6, "V2", "Except", "4", "Easy",
 "Learning styles stress differences.",
 steps(("The line", ev(2, "a progressive movement that stressed individual differences in children")),
       ("Choosing", p("A single method for all learners is the opposite idea: option 4."))) +
 final("Option 4"),
 "except",
 [("1", "Stated."), ("2", "‘More empirical methods’."), ("3", "Stated.")])

P.rc(7, "V2", "Main_Idea", "3", "Medium",
 "Which list covers the whole passage, including the end?",
 steps(("The arc", p("What learning styles are, how they emerged, whether they are valid and measurable, that they are preferences, and that the material decides the method.")),
       ("Choosing", p("Option 3 is the only list with the closing point."))) +
 final("Option 3"),
 "inference",
 [("1", "Ends with empirical methods, not the material."), ("2", "Leaves out the closing point."), ("4", "Leaves out validity and the closing point.")],
 opts=[V[7]["opts"][0], V[7]["opts"][1], V[7]["opts"][2], "VARK Model, Emergence and history, Learning Styles industry, Personality types, Learning preferences."])

P.rc(8, "V2", "Inference", "1", "Medium",
 "Paragraph 3 on Coffield’s review.",
 steps(("The line", ev(3, "few of which were peer-reviewed or conducted in well-designed studies")),
       ("Choosing", p("Option 1. The others are claims of learning styles theory that the passage rejects."))) +
 final("Option 1"),
 "inference",
 [("2", "The passage says the material decides."), ("3", "The 2016 study found no gain."), ("4", "Not in the passage.")],
 q="Which of the following is supported by the passage?",
 opts=["Much of the published material on learning styles was not peer-reviewed or based on well-designed studies.", V[8]["opts"][1], V[8]["opts"][2], V[8]["opts"][3]])

# ---------------- Passage 3 (Q9–12) ----------------
P.rc(9, "V3", "Main_Idea", "4", "Easy",
 "The first sentence states the finding.",
 steps(("The line", ev(1, "human feelings can accurately be expressed numerically and have more predictive power for how we behave than formal studies of socioeconomic factors")),
       ("Choosing", p("Option 4."))) +
 final("Option 4"),
 "inference",
 [("1", "Feelings are not said to indicate circumstances."), ("2", "They can be quantified."), ("3", "Not combined with socioeconomic factors.")])

P.rc(10, "V3", "Except", "2", "Medium",
 "A 10% chance of quitting is not zero.",
 steps(("The argument", p("Lower ratings come with higher chances of quitting, divorce or hospital stays.")),
       ("Choosing", p("Some contented workers quitting fits a 10% probability, so option 2 does not undermine it."))) +
 final("Option 2"),
 "except",
 [("1", "Low ratings without quitting cut against it."), ("3", "Low-rated marriages not ending."), ("4", "Health ratings fail to predict.")])

P.rc(11, "V3", "Inference", "3", "Easy",
 "Why does economics care?",
 steps(("The line", ev(4, "socioeconomic factors had a lesser probability of predicting human behaviour than data on feelings")),
       ("Choosing", p("Feelings help predict economic behaviour such as quitting a job: option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "No ranking of fields."), ("2", "No comparison of the two kinds of measure."), ("4", "Reverses it.")])

P.rc(12, "V3", "Except", "3", "Easy",
 "What do the researchers admit they do not know?",
 steps(("The lines", ev(4, "researchers are still a bit perplexed as to why estimates of seemingly subjective feelings can be such good predictors") + ev(7, "we still don’t know for sure how it’s done")),
       ("Choosing", p("They say feelings can be put in numbers, so a lack of numerical units is not a limitation they acknowledge: option 3."))) +
 final("Option 3"),
 "except",
 [("1", "Paragraph 4."), ("2", "Lower-income countries."), ("4", "Paragraph 7.")],
 opts=["Not knowing why feelings predict future actions so well.", V[12]["opts"][1], V[12]["opts"][2], V[12]["opts"][3]])

# ---------------- Passage 4 (Q13–16) ----------------
P.rc(13, "V4", "Inference", "3", "Easy",
 "‘Anatomical independence of nerve cells’.",
 steps(("The line", ev(1, "demonstrated the anatomical independence of nerve cells")),
       ("Choosing", p("Neurons are separate cells: option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "The reverse."), ("2", "True of Cajal but about neuroscience, not his histology."), ("4", "Brainbow is modern.")])

P.rc(14, "V4", "Inference", "2", "Medium",
 "Same desire, new technology.",
 steps(("The line", ev(2, "Imaging technology in the 21st century is beyond what Cajal and his contemporaries could have imagined, but our desire remains the same")),
       ("Choosing", p("The goal is unchanged while tools change: option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "Goes beyond the lines."), ("3", "About progress, not the unchanged goal."), ("4", "Methods have changed.")])

P.rc(15, "V4", "Except", "4", "Medium",
 "What does the stimulating: light or electricity?",
 steps(("The line", ev(4, "they shine a certain kind of light at those neurons to open their ion channels and fire the electrical signal")),
       ("Choosing", p("Light triggers the neuron, which then fires its own signal. The technique does not stimulate electrically: option 4."))) +
 final("Option 4"),
 "except",
 [("1", "‘Add new code’."), ("2", "Light."), ("3", "‘Carefully and selectively’.")])

P.rc(16, "V4", "Inference", "1", "Easy",
 "What do the colours do?",
 steps(("The line", ev(5, "Brainbow technique can trace many neurons at once")),
       ("Choosing", p("Coloured proteins label neurons so they can be traced: option 1."))) +
 final("Option 1"),
 "inference",
 [("2", "That is optogenetics."), ("3", "That is immunofluorescence."), ("4", "That is CLARITY.")])

# ---------------- Verbal ability (Q17–24) ----------------
P.va(17, P.sent_html(17), [], "TITA", "2431", "Para_Jumble", "Medium",
 "Myth, example, so it survived, then mutual influence.",
 steps(("Order", p("2 says printing did not end manuscripts. 4 gives works still handwritten. 3 ‘Thus’ they survived. 1 adds how the two influenced each other."))) +
 final("2431"),
 "pj",
 [("2", "Opens."), ("4", "Examples."), ("3", "“Thus”."), ("1", "Further point.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.sent_html(18), [], "TITA", "3214", "Para_Jumble", "Easy",
 "Claim, figures, more figures, conclusion.",
 steps(("Order", p("3 says rivers hold a tiny fraction. 2 gives rivers’ share. 1 adds lakes and soil. 4 draws the lesson."))) +
 final("3214"),
 "pj",
 [("3", "Opens."), ("2", "Rivers."), ("1", "Lakes, soil."), ("4", "Conclusion.")],
 why_title="Why each sentence goes where it does")

P.va(19, P.sent_html(19), [], "TITA", "2413", "Para_Jumble", "Medium",
 "Short-term risk, endurance, long-term damage, effects.",
 steps(("Order", p("2 introduces burnout risk. 4 ‘some may endure it’. 1 prolonged exposure damages the relationship with work. 3 ‘This’ has longer-term effects."))) +
 final("2413"),
 "pj",
 [("2", "Opens."), ("4", "“It”."), ("1", "Prolonged."), ("3", "“This”.")],
 why_title="Why each sentence goes where it does")

P.va(20, P.missing_html(20), P.strict_opts(20), "MCQ", "3", "Missing_Sentence", "Easy",
 "‘The converse’ starts from L being false.",
 steps(("Find the spot", p("After ‘the converse also can be established, as follows’, the proof must begin by assuming L is false."))) +
 final("Option 3"),
 "missing",
 [("1", "Before the argument."), ("2", "Before the sketch."), ("4", "After L is shown true.")])

P.va(21, P.missing_html(21), P.strict_opts(21), "MCQ", "2", "Missing_Sentence", "Easy",
 "‘This paradox’ needs a paradox just before.",
 steps(("Find the spot", p("Blank 2 follows ‘an imposing edifice on sinking ground’ and precedes the region’s wealth and decline."))) +
 final("Option 2"),
 "missing",
 [("1", "No paradox yet."), ("3", "Paradox already explained."), ("4", "Too late.")])

P.va(22, P.summary_html(22, "In recent years, genetic-sequencing"), V[22]["opts"], "MCQ", "1", "Summary", "Easy",
 "Finding, limitation, wider risk.",
 steps(("What the passage says", "<ol><li>Gene variants explain bad drug reactions.</li><li>The studies covered only people of European ancestry.</li><li>This ‘genomic gap’ may worsen inequality.</li></ol>"),
       ("Choosing", p("Option 1."))) +
 final("Option 1"),
 "summary",
 [("2", "Drops what the variants do."), ("3", "Drops the finding."), ("4", "Drops whom the studies covered.")])

P.va(23, P.summary_html(23, "The foundations of identity"), [V[23]["opts"][0], V[23]["opts"][1],
     "Believing that their true inner self is at odds with their social role, people search for it anxiously, and relief comes only when that self is accepted and publicly recognised.",
     "Modern identity is a product of social validation, through which society assigns people the roles that relieve their alienation and anxiety."],
 "MCQ", "3", "Summary", "Medium",
 "Inner versus outer, search, relief.",
 steps(("What the passage says", "<ol><li>Identity rests on a gap between inner and outer self.</li><li>The search for the inner self brings alienation and anxiety.</li><li>Relief needs acceptance and public recognition.</li></ol>"),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "summary",
 [("1", "Blames the concept for alienation."), ("2", "Muddles what modern identity values."), ("4", "Society does not assign the relief.")])

P.va(24, P.summary_html(24, "The conflict between the determinists"), V[24]["opts"], "MCQ", "4", "Summary", "Easy",
 "Disagreement, then common ground.",
 steps(("What the passage says", "<ol><li>The two camps will never agree on humanity’s nature.</li><li>Both accept that technology marks turning points.</li><li>Civilization owes its form to technology.</li></ol>"),
       ("Choosing", p("Option 4."))) +
 final("Option 4"),
 "summary",
 [("1", "Agreement is about technology, not faith."), ("2", "Technology is not a product of faith."), ("3", "Invents who holds which view.")])
