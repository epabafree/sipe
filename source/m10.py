# -*- coding: utf-8 -*-
# Simp Mock 10: VARC (24 of 24). DILR and QA: m10_dilr.py, m10_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(10, "sm10.json")
P.passage("V1", "Passage 1 — Portugal’s azulejos", "Arts_and_Culture")
P.passage("V2", "Passage 2 — Why cities need history", "Social_Sciences")
P.passage("V3", "Passage 3 — The happiness revolution", "Philosophy_and_Psychology")
P.passage("V4", "Passage 4 — Treatment and selection", "Economics_and_Management")

V = P.Q["VARC"]
V[17]["q"] = V[17]["q"].replace("4. Industrialization would postpone the crisis, but not forever.",
                                "4. Industrialization would postpone the crisis Malthus foresaw, but not forever.")
V[20]["q"] = V[20]["q"].replace("Sentence: Many people believe that the best way to learn a new language is through immersion.",
                                "Sentence: Using the language all day, every day, builds fluency far faster than occasional lessons.")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Except", "1", "Easy",
 "Which claim does paragraph 3 deny?",
 steps(("The line", ev(3, "In other countries, you can remove the tiles and move them from one wall or building to another without losing anything")),
       ("Choosing", p("In Portugal the tiles are made for their setting, so moving them loses something: option 1 is not a feature."))) +
 final("Option 1"),
 "except",
 [("2", "Paragraphs 4–5."), ("3", "Early Islamic motifs."), ("4", "Scenography and figurative scenes.")],
 opts=["Tiles that can be moved from one building to another without losing anything.", V[1]["opts"][1], V[1]["opts"][2],
       "A sense of scenography, with figurative scenes tied to their setting."])

P.rc(2, "V1", "Inference", "4", "Easy",
 "Why does the setting matter?",
 steps(("The line", ev(3, "the mosaics are created specifically for the architecture, so, the work’s setting is as critical as the design elements")),
       ("Choosing", p("Option 4."))) +
 final("Option 4"),
 "inference",
 [("1", "About materials."), ("2", "About durability."), ("3", "What the untrained eye wrongly sees.")])

P.rc(3, "V1", "Main_Idea", "4", "Medium",
 "Why does the author include paragraph 3?",
 steps(("Its role", p("It shows that in Portugal tiles are made for their buildings on a monumental scale, unlike elsewhere. That backs the opening claim that azulejos are a key to Portugal.")),
       ("Choosing", p("Option 4 states the purpose; options 1 and 3 restate content."))) +
 final("Option 4"),
 "inference",
 [("1", "Content, not purpose."), ("2", "Not a comparison of designs."), ("3", "Content, not purpose.")])

P.rc(4, "V1", "Except", "2", "Easy",
 "Did the motifs stay the same?",
 steps(("The line", ev(4, "we are always changing and adjusting to new concepts, new ideas")),
       ("Choosing", p("The tiles moved from Islamic knotwork to scenography and contemporary work, so option 2 is false."))) +
 final("Option 2"),
 "except",
 [("1", "The opening claim."), ("3", "Paragraph 1."), ("4", "Paragraphs 4–5.")],
 opts=[V[4]["opts"][0], "Portuguese azulejos have kept the same Islamic motifs since they first appeared.", V[4]["opts"][2], V[4]["opts"][3]])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Strengthen", "2", "Medium",
 "The author’s alternative is timing.",
 steps(("The line", ev(3, "The city came to the immigrants, not the immigrants to the city")),
       ("Choosing", p("If no Italian clusters formed where migration came before the city grew, timing, not cultural distance, explains clusters: option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "About dispersal later, not formation."), ("3", "Economic reasons, not timing."), ("4", "Supports clustering by the late arrivals but not against cultural distance as clearly.")])

P.rc(6, "V2", "Inference", "1", "Medium",
 "Spanish immigrants were even closer culturally, yet clustered more.",
 steps(("The line", ev(3, "Spanish immigrants in Buenos Aires, who shared even more socio-cultural traits with Argentine society than Italians did, nonetheless clustered much more")),
       ("Choosing", p("The comparison shows the hypothesis fails: option 1."))) +
 final("Option 1"),
 "inference",
 [("2", "Discrimination is not discussed."), ("3", "The author rejects culture as the cause."), ("4", "‘Solely’ jobs; not in the text.")],
 q="What point does the author make by comparing Italian and Spanish immigrants in Buenos Aires?")

P.rc(7, "V2", "Inference", "3", "Easy",
 "When did each group arrive?",
 steps(("The line", ev(3, "Italian immigrants arrived earlier and they often settled on small rural plots in the then pampas")),
       ("Choosing", p("The Spanish came later, into a city already formed: option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "They were closer culturally."), ("2", "Not stated."), ("4", "Similarity is not the author’s cause.")])

P.rc(8, "V2", "Except", "4", "Medium",
 "Which flaw is never raised?",
 steps(("The flaws", p("Present-mindedness (ignoring history), relying on cultural difference, and assuming the city has a fixed shape are all raised.")),
       ("Choosing", p("Nothing is said about studying too few cities: option 4."))) +
 final("Option 4"),
 "except",
 [("1", "Paragraph 2."), ("2", "The social-distance hypothesis."), ("3", "‘Flawed assumption that the city had a definite shape’.")],
 q="Which of the following is NOT presented in the passage as a flaw of current urban studies?",
 opts=[V[8]["opts"][0], V[8]["opts"][1], "Treating a city as if it had a fixed shape into which people simply spread.", V[8]["opts"][3]])

# ---------------- Passage 3 (Q9–12) ----------------
P.rc(9, "V3", "Main_Idea", "2", "Medium",
 "Break with tradition and money-likeness.",
 steps(("The thread", p("The packaged happiness sold today has little continuity with older ideas of happiness as an objective condition, and measuring it makes it money-like.")),
       ("Choosing", p("Option 2 holds both."))) +
 final("Option 2"),
 "inference",
 [("1", "States one old view as the author’s thesis."), ("3", "Not about owning money."), ("4", "Leaves out the break with tradition.")],
 opts=[V[9]["opts"][0], "Treating happiness as a measurable, saleable product breaks with the older view of it as an objective condition and turns it into something money-like.",
       V[9]["opts"][2], V[9]["opts"][3]])

P.rc(10, "V3", "Inference", "2", "Medium",
 "Read the sentence after ‘happiness revolution’.",
 steps(("The line", ev(1, "The scientific study, laboratory refinement, and industrial production of happiness are all big business")),
       ("Choosing", p("Option 2 restates it."))) +
 final("Option 2"),
 "inference",
 [("1", "Not about people getting happier."), ("3", "‘Digital measurement’ is not stated."), ("4", "Ancient inquiry is the contrast.")],
 opts=["The rise in people’s happiness brought about by industrial and digital technology.",
       "The modern scientific study, refinement and large-scale selling of happiness as a product.", V[10]["opts"][2], V[10]["opts"][3]])

P.rc(11, "V3", "Inference", "3", "Easy",
 "‘Its imperfect ancestor’.",
 steps(("The line", ev(5, "it is often to economics that this field looks as its imperfect ancestor")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "Economics does not measure happiness in the text."), ("2", "Not replacement."), ("4", "Reverses the relation.")])

P.rc(12, "V3", "Inference", "4", "Medium",
 "Which one does the author imply?",
 steps(("Choosing", p("The author is critical of measuring happiness. Option 4, that measurement misses individual experience, fits; options 1–3 praise the approach."))) +
 final("Option 4"),
 "inference",
 [("1", "Praises the approach."), ("2", "Praises the approach."), ("3", "Praises the approach.")])

# ---------------- Passage 4 (Q13–16) ----------------
P.rc(13, "V4", "Except", "1", "Easy",
 "Selection = picking by traits.",
 steps(("The line", ev(1, "You get signed up by an agency because you’re beautiful")),
       ("Choosing", p("Options 2–4 pick people by traits. Option 1 picks a policy by its effect: option 1."))) +
 final("Option 1"),
 "except",
 [("2", "Picks by traits."), ("3", "Picks by traits."), ("4", "Picks by traits.")])

P.rc(14, "V4", "Inference", "3", "Medium",
 "What did the study show?",
 steps(("The line", ev(3, "when you compare apples and apples the income bonus from selective schools disappears")),
       ("Choosing", p("The higher earnings do not show that the same student would earn less elsewhere: option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "Not the point."), ("2", "Not the point."), ("4", "This is what the study suggests.")])

P.rc(15, "V4", "Inference", "4", "Medium",
 "Among students admitted to both, the choice did not matter.",
 steps(("The line", ev(4, "Within that set it doesn’t seem to matter whether you go to the more selective school")),
       ("Choosing", p("So Penn’s higher average comes from whom it admits: option 4."))) +
 final("Option 4"),
 "inference",
 [("1", "Too absolute."), ("2", "All Penn State students: too broad."), ("3", "That would be a selection result.")])

P.rc(16, "V4", "Inference", "2", "Medium",
 "What explains Harvard students’ success?",
 steps(("The line", ev(3, "It’s quite possible that the student who goes to Harvard is more ambitious and energetic")),
       ("Choosing", p("Option 2 fits the passage’s explanation."))) +
 final("Option 2"),
 "inference",
 [("1", "The passage says the opposite."), ("3", "The bonus disappeared."), ("4", "Not discussed.")],
 q="Which of the following is most consistent with the passage?",
 opts=["Higher earnings of Ivy League graduates are mainly a treatment effect.", V[16]["opts"][1], V[16]["opts"][2], V[16]["opts"][3]])

# ---------------- Verbal ability (Q17–24) ----------------
P.va(17, P.sent_html(17), [], "TITA", "2431", "Para_Jumble", "Medium",
 "Malthus, his crisis, the Ehrlichs, their fears.",
 steps(("Order", p("2 Malthus’s warning. 4 ‘the crisis Malthus foresaw’ was postponed. 3 the Ehrlichs add fuel in the 1960s. 1 ‘their fears’ were reasonable."))) +
 final("2431"),
 "pj",
 [("2", "Opens."), ("4", "Malthus’s crisis."), ("3", "1960s."), ("1", "“Their fears”.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.sent_html(18), [], "TITA", "1432", "Para_Jumble", "Medium",
 "Claim, definition, ancient drivers, also others.",
 steps(("Order", p("1 globalization is old. 4 what it is. 3 migration and climate since ancient times. 2 ‘also’ military and cultural."))) +
 final("1432"),
 "pj",
 [("1", "Opens."), ("4", "Definition."), ("3", "First examples."), ("2", "“Also”.")],
 why_title="Why each sentence goes where it does")

P.va(19, P.sent_html(19), [], "TITA", "2143", "Para_Jumble", "Medium",
 "Crisis, neglect, moreover, but the fact is.",
 steps(("Order", p("2 introduces the twin crises. 1 informal workers are overlooked. 4 ‘Moreover’ austerity is ignored. 3 ‘But the fact is’ economies depend on them."))) +
 final("2143"),
 "pj",
 [("2", "Opens."), ("1", "Neglect."), ("4", "“Moreover”."), ("3", "Rebuttal.")],
 why_title="Why each sentence goes where it does")

P.va(20, P.missing_html(20), P.strict_opts(20), "MCQ", "3", "Missing_Sentence", "Easy",
 "‘Additionally’ needs a first benefit before it.",
 steps(("Find the spot", p("After blank 3 comes ‘Additionally, immersion allows learners to …’, a second benefit. The sentence is the first.")),
       ("Check the others", p("Blank 2 is followed by where programs are found, not a benefit; blank 4 leads into the challenges."))) +
 final("Option 3"),
 "missing",
 [("1", "Before immersion is introduced."), ("2", "Not followed by ‘Additionally’."), ("4", "Before ‘However’ challenges.")])

P.va(21, P.missing_html(21), P.strict_opts(21), "MCQ", "2", "Missing_Sentence", "Easy",
 "The turn from problem to response.",
 steps(("Find the spot", p("Blank 2 comes after the waste of fast fashion and before ‘This includes using environmentally-friendly materials’. ‘This’ needs the trend."))) +
 final("Option 2"),
 "missing",
 [("1", "Before the problem."), ("3", "Trend already explained."), ("4", "After the close.")])

P.va(22, P.summary_html(22, "If an alien race"), V[22]["opts"][:3] + ["Why and when humans swapped thick fur for fine vellus hair is uncertain, but the dominant theory links it to early humans’ need to keep cool."],
 "MCQ", "4", "Summary", "Easy",
 "Uncertainty plus the leading theory.",
 steps(("What the passage says", "<ol><li>Humans look furless but have fine hair.</li><li>Why and when this changed is unknown.</li><li>The leading theory is body cooling.</li></ol>"),
       ("Choosing", p("Option 4."))) +
 final("Option 4"),
 "summary",
 [("1", "‘Only primate’ overstated."), ("2", "States the theory as fact."), ("3", "Drops the uncertainty.")])

P.va(23, P.summary_html(23, "Today, we tend to look back"), [V[23]["opts"][0],
     "Honour in pre-democratic societies went only to those who risked their lives; this belief in a superior class upheld social order and still echoes in our respect for soldiers.",
     V[23]["opts"][2], V[23]["opts"][3]], "MCQ", "2", "Summary", "Medium",
 "Honour for risk-takers, hierarchy, the echo today.",
 steps(("What the passage says", "<ol><li>Honour went only to those who risked their lives.</li><li>That belief in superiority held hierarchy in place.</li><li>An echo survives in respect for soldiers and firemen.</li></ol>"),
       ("Choosing", p("Option 2."))) +
 final("Option 2"),
 "summary",
 [("1", "Drops the risk of life."), ("3", "Aristocrats are not still respected."), ("4", "Megalothymia is a detail.")])

P.va(24, P.summary_html(24, "For centuries, historians"), V[24]["opts"], "MCQ", "3", "Summary", "Medium",
 "The extreme view and its end point.",
 steps(("What the passage says", "<ol><li>Determinists see technology as autonomous.</li><li>In the extreme view, humans just build tools.</li><li>Once technology reproduces itself, humans are dispensable.</li></ol>"),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "summary",
 [("1", "‘Indispensable’ reverses it."), ("2", "‘Civilization beyond control’ distorts."), ("4", "Credits the extreme view to Veblen.")])
