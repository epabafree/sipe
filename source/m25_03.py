# -*- coding: utf-8 -*-
# Simp Mock 3 (2025): VARC (24 of 24). DILR and QA: m25_03_dilr.py, m25_03_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(3, "sm25_03.json", series=2025)
P.passage("V1", "Passage 1 — The Theory-Theory of concepts", "Philosophy_and_Psychology")
P.passage("V2", "Passage 2 — Are factory jobs better?", "Economics_and_Management")
P.passage("V3", "Passage 3 — Tortoises as ecological architects", "Environment_and_Life_Science")
P.passage("V4", "Passage 4 — Voices brought back by AI", "Science_and_Technology")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Inference", "2", "Medium",
 "The theory borrows from Kuhn’s philosophy of science. What happens to theories in Kuhn’s picture?",
 steps(("The view", p("Concepts sit inside theories that we acquire and use in explaining; the view draws on Kuhn to explain how cognition <i>develops</i>. Theories in this sense are revised as we learn.")),
       ("The odd one", p("Option 2 says the theories are logically sound and never change. Development and revision are the whole point, so this is inconsistent."))) + final("Option 2"),
 "inference", [("1", "Fits: everyday mini-theories of how things work."), ("3", "Fits: theories are used to explain and categorise."), ("4", "Fits: development through revision, as in Kuhn.")])
P.rc(2, "V1", "Detail", "3", "Medium",
 "The question quotes the passage’s ‘domain-specific explanatory expectations’. What do they replace?",
 steps(("The line", ev(3, "the Theory-Theory has been responsible for largely displacing the notion that cognitive development starts from a simple base of perceptual primitives grouped together by similarity") +
          p("Development is guided by expectations specific to each domain rather than by bare perception. Option 3 states the evidence for that."))) + final("Option 3"),
 "detail", [("1", "Kuhn is a source of the idea, not evidence for domain-specific expectations."), ("2", "The critique of prototype theory is a separate origin."), ("4", "Theory of mind is one domain; it doesn’t show expectations differ across domains.")])
P.rc(3, "V1", "Inference", "2", "Easy",
 "Morton’s idea: we explain behaviour through beliefs, intentions, emotions.",
 steps(("What it shows", p("We read others’ actions through an internal framework, a ‘theory’ of how minds work. Option 2 says this."))) + final("Option 2"),
 "inference", [("1", "‘Untested assumptions’ isn’t the point."), ("3", "Perception isn’t discussed in the quote."), ("4", "Nothing about scientific methods.")])
P.rc(4, "V1", "Detail", "4", "Medium",
 "The passage mentions one weakness of the view in the same paragraph as the objections.",
 steps(("The line", ev(3, "While the theory has often been vaguely formulated, due in large part to the open-endedness inherent in the central notion of a theory") +
          p("The only difficulty the passage names is vagueness about what counts as a theory. Option 4."))) + final("Option 4"),
 "detail", [("1", "Rigidity isn’t mentioned."), ("2", "The passage says it explains categorisation."), ("3", "It stresses causal reasoning.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Detail_Not_True", "4", "Medium",
 "What does the author say about cyclicality, and on whose behalf?",
 steps(("What politicians claim", p("Tariffs to reduce reliance on foreign goods, subsidies and reversing decline to make workers better off, which covers rebuilding the middle class and community prosperity.")),
       ("The odd one", ev(3, "manufacturing roles can be more cyclical than those in services") +
          p("Cyclicality is the author’s point <i>against</i> manufacturing, not a reason politicians give for it."))) + final("Option 4"),
 "except", [("1", "Tariffs on foreign goods."), ("2", "Making workers better off: the politicians’ case."), ("3", "The same promise for communities.")])
P.rc(6, "V2", "Purpose", "2", "Easy",
 "‘A long pedigree’, then Smith.",
 steps(("The line", ev(2, "The argument that manufacturing jobs are better than other sorts has a long pedigree. Adam Smith deemed manufacturing “productive,” unlike services") +
          p("Smith shows how old the belief is: it goes back to classical economics."))) + final("Option 2"),
 "purpose", [("1", "The author doesn’t endorse the link."), ("3", "Smith wrote before the industrial era the passage describes."), ("4", "Nostalgia comes up at the end, about politicians, not Smith.")])
P.rc(7, "V2", "Main_Idea", "3", "Easy",
 "Paragraph 3 opens with the enthusiasts’ case and then ‘But compare…’.",
 steps(("The point", ev(3, "But compare workers of similar education levels and there is little evidence they would gain by moving from services to manufacturing") +
          p("Pay, security and conditions no longer favour manufacturing; the wage premium has ‘disappeared’."))) + final("Option 3"),
 "inference", [("1", "No ‘temporary’ superiority."), ("2", "The paragraph says conditions have improved."), ("4", "The author argues against such investment.")])
P.rc(8, "V2", "Application", "2", "Easy",
 "The BLS paper compares services and manufacturing directly.",
 steps(("The line", ev(3, "“many industries within services equal or exceed manufacturing.”") +
          p("For similarly educated workers. Option 2."))) + final("Option 2"),
 "inference", [("1", "Creativity isn’t compared."), ("3", "Better conditions don’t make manufacturing better than services."), ("4", "Manufacturing is said to be more cyclical.")])

P.va(9, P.missing_html(9), P.Q["VARC"][9]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "‘This shortsighted approach’ looks back at the whole policy. ‘In the long run’ looks ahead.",
 steps(("Find the spot", p("The paragraph builds from the policy (slashing aid, withdrawing) to its consequences and ends with ‘risk permanently weakening U.S. influence’. The sentence is the final warning, at blank 4.")),
       ("Match the label", p("Blank 4 is choice 1, labelled ‘Option 4’."))) + final("Choice 1 (“Option 4”)"),
 "missing", [("2", "“Option 1”: the consequences haven’t been described yet."), ("3", "“Option 3”: the China comparison still needs its conclusion."), ("4", "“Option 2”: the credibility point follows and continues the argument.")])
P.va(10, P.missing_html(10), P.Q["VARC"][10]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "The sentence leads straight into ‘Consequently, central banks may continue to see them as a viable… option.’",
 steps(("Find the hook", p("‘Consequently’ needs a reason just before it. ‘Negative rates offer one of the few remaining ways’ is that reason, so the sentence goes at blank 3.")),
       ("Match the label", p("Blank 3 is choice 1, labelled ‘Option 3’."))) + final("Choice 1 (“Option 3”)"),
 "missing", [("2", "“Option 1”: the paragraph has to open with negative rates themselves."), ("3", "“Option 4”: after the conclusion."), ("4", "“Option 2”: between how they work and the critics.")])
P.va(11, P.summary_html(11, "When did the"), P.Q["VARC"][11]["opts"], "MCQ", "2", "Summary", "Hard",
 "Two kinds of divide: first intellectual and political, then a new kind of society ‘in human history’.",
 steps(("What the passage says", "<ol><li>Europeans first dated modernity from Rome’s fall or the late-15th-century revival, by intellectual, political and religious criteria.</li><li>From the late 18th century, observers saw a new type of society, new in human history: commerce, industry, abundance.</li></ol>"),
       ("Choosing", p("Option 2 keeps the shift in criteria and its global reach."))) + final("Option 2"),
 "summary", [("1", "Leaves out the change in criteria."), ("3", "Close, but keeps it to European perceptions and drops the political-intellectual first framing."), ("4", "Misstates when the modern era was first dated.")])

# ---------------- Passage 3 (Q12–15) ----------------
P.rc(12, "V3", "Inference_Except", "4", "Medium",
 "Were the landscape changes natural?",
 steps(("What can be inferred", p("With goats gone and tortoises caged, the island overgrew, so overgrowth persists without large herbivores (1), removing goats wasn’t enough (2), and tortoises shape vegetation (3).")),
       ("The odd one", p("Each change came from human action: introducing goats, removing them, caging tortoises. Nothing suggests a natural swing between barren and wooded."))) + final("Option 4"),
 "except", [("1", "Overgrowth came when no herbivores were left."), ("2", "Goats gone, yet no savanna."), ("3", "Recovery waited for them.")])
P.rc(13, "V3", "Detail_Not_True", "3", "Medium",
 "Which option is a result, not an action?",
 steps(("Human actions", p("Introducing goats and rats; moving tortoises in to clear albatross runways; the recovery driven by reintroducing tortoises.")),
       ("The odd one", p("Woody plants growing after the goats were removed is the ecosystem’s response, not something people did directly."))) + final("Option 3"),
 "notrue", [("1", "Whalers, settlers and pirates introduced them."), ("2", "People move tortoises to clear runways."), ("4", "Brought about by reintroducing tortoises.")])
P.rc(14, "V3", "Purpose", "4", "Easy",
 "Read the last sentence.",
 steps(("The line", ev(3, "The results bode well for other rewilding projects that include giant tortoise restoration as a keystone of their efforts") +
          p("The Mascarenes are an example of where the approach could work too."))) + final("Option 4"),
 "purpose", [("1", "The projects are ‘underway’, not yet successes."), ("2", "Unique challenges aren’t discussed."), ("3", "Native ranges aren’t discussed.")])
P.rc(15, "V3", "Weaken", "1", "Hard",
 "The argument: tortoises are restoring Española to its natural savanna-like state.",
 steps(("Undermining", p("If Española was mostly dense forest through its history, the savanna isn’t its natural state, and the ‘restoration’ story collapses.")),
       ("The others", p("Option 2 weakens the role of tortoises but not the idea of restoration; options 3 and 4 support the argument."))) + final("Option 1"),
 "weaken", [("2", "Contradicts one detail, but the passage reports the opposite happened."), ("3", "Supports the tortoises’ role."), ("4", "Supports it.")])

P.va(16, P.sent_html(16), [], "TITA", "5", "Odd_One_Out", "Easy",
 "Four sentences describe what the Super Bowl is today. One is history.",
 steps(("The chain", p("4 → 1 → 2 → 3: one of the most watched events (4); for players, the culmination of a season (1); the halftime show (2); the adverts (3).")),
       ("The odd one", p("Sentence 5, on the 1966 merger, is the event’s origin, which the paragraph doesn’t discuss."))) + final("5"),
 "oddone", [("4", "Introduces the event."), ("1", "“However”: for players it is more than entertainment."), ("2", "“Beyond the game itself”."), ("3", "“Equally legendary”: adverts.")], why_title="How the other sentences fit")
P.va(17, P.summary_html(17, "Laughing and crying"), P.Q["VARC"][17]["opts"], "MCQ", "3", "Summary", "Medium",
 "Familiar, universal, not symbolic, ambiguous: and so we don’t know what they are.",
 steps(("Choosing", p("Option 3 keeps familiar, universal, non-symbolic, ambiguous, and the open question of what they are."))) + final("Option 3"),
 "summary", [("1", "‘Across cultures’ moves the question; the passage asks what they are."), ("2", "Says they are studied across fields; the passage asks which field is responsible."), ("4", "Leaves out that they aren’t symbolic.")])

# ---------------- Passage 4 (Q18–21) ----------------
P.rc(18, "V4", "Inference_Except", "3", "Easy",
 "Is anything said about what audiences prefer?",
 steps(("The odd one", p("The sentence is about what the film contains. Nothing in it, or the passage, reports audience preferences between the real and AI voices."))) + final("Option 3"),
 "except", [("1", "Featuring her real performances keeps her work intact."), ("2", "‘No announcement that the AI tech will develop new music’."), ("4", "Existing performances are used as they are.")])
P.rc(19, "V4", "Purpose", "2", "Medium",
 "Piaf, Warhol, Herrmann, Bourdain: films, documentaries, audiobooks.",
 steps(("The role", p("The examples show the range of creative uses of voice recreation. The ethical worries come with Bourdain and the music section, but the examples as a group illustrate the variety.")),
       ("Choosing", p("Option 2."))) + final("Option 2"),
 "purpose", [("1", "Only Bourdain is about ethics."), ("3", "Warhol’s and Bourdain’s cases aren’t about heritage."), ("4", "Only one example was controversial.")])
P.rc(20, "V4", "Vocabulary", "1", "Easy",
 "‘Uncanny’: strangely real, and unsettling for it.",
 steps(("Reading it", p("The replicas are realistic enough to disturb, which is why artists object."))) + final("Option 1"),
 "detail", [("2", "Uncanny means too real, not unconvincing."), ("3", "‘Indistinguishable’ drops the unsettling sense."), ("4", "‘Admirably’ is the opposite tone.")])
P.rc(21, "V4", "Tone", "1", "Medium",
 "The estate is moved; critics object; the author reports both.",
 steps(("Signals", p("Positive: the estate’s pleasure, the Beatles’ careful use. Negative: Bourdain controversy, Drake, ethical and legal debates. The author takes no side.")),
       ("Choosing", p("Balanced: option 1."))) + final("Option 1"),
 "inference", [("2", "Ignores the controversies."), ("3", "Ignores the positive cases."), ("4", "The author treats it as significant.")])

P.va(22, P.missing_html(22), P.Q["VARC"][22]["opts"], "MCQ", "3", "Missing_Sentence", "Medium",
 "The sentence sums up why China succeeded. Where has the paragraph just listed China’s moves?",
 steps(("Find the spot", p("Before blank 3: restrictions spurred domestic investment, and firms used the large home market. The sentence names the overall strategy; the next sentence turns to ‘Meanwhile, Western companies…’.")),
       ("Check the others", p("Blanks 1 and 2 come before China’s strategy is described; blank 4 is after the conclusion."))) + final("Option 3"),
 "missing", [("1", "Before the strategy is described."), ("2", "The paragraph is still on the Western failure."), ("4", "After the conclusion.")])
P.va(23, P.summary_html(23, "Instead of being organized"), P.Q["VARC"][23]["opts"], "MCQ", "2", "Summary", "Hard",
 "Content is ‘flat’: no hierarchy of truth. The result is cacophony or the loudest voice.",
 steps(("Choosing", p("Option 2 keeps the cause (content over information), the flatness (no hierarchy of truth) and the result (the loudest voice wins)."))) + final("Option 2"),
 "summary", [("1", "‘Manipulation’ goes beyond the passage."), ("3", "‘Authoritative voices’ misreads ‘loudest’."), ("4", "Critical thinking isn’t mentioned; leaves out the single victor.")])
P.va(24, P.sent_html(24), [], "TITA", "5", "Odd_One_Out", "Medium",
 "The paragraph follows her Oscar Sunday. One sentence is about her education.",
 steps(("The chain", p("4 → 1 → 2 → 3: on Oscar Sunday she is in a star’s bedroom (4); the stylist arrives and finalises gowns (1); she loves the last-minute fittings (2); she has long fielded last-minute gown requests (3).")),
       ("The odd one", p("Sentence 5, on her Oxford studies and persuasive skills, leaves the day and the last-minute theme behind."))) + final("5"),
 "oddone", [("4", "Sets the scene."), ("1", "Her morning."), ("2", "Last-minute fittings."), ("3", "Last-minute requests, earlier in her career.")], why_title="How the other sentences fit")
