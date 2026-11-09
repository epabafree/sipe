# -*- coding: utf-8 -*-
# Simp Mock 8 (2025): VARC (24 of 24). DILR and QA: m25_08_dilr.py, m25_08_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(8, "sm25_08.json", series=2025)
P.passage("V1", "Passage 1 — The gravitational-wave hum", "Science_and_Technology")
P.passage("V2", "Passage 2 — Earthworks of the Llanos de Moxos", "Social_Science_and_History")
P.passage("V3", "Passage 3 — A history of scarcity", "Economics_and_Management")
P.passage("V4", "Passage 4 — The world as one big Weimar", "Politics")

P.va(1, P.summary_html(1, "Tribalism certainly functioned"), P.Q["VARC"][1]["opts"], "MCQ", "4", "Summary", "Medium",
 "Past: tribalism helped survival. Now: democracy lets us keep in-group loyalty and still cooperate, so is it still needed?",
 steps(("Choosing", p("Option 4 has the historical benefit and the question democracy raises about its necessity, by allowing loyalty and cooperation together."))) + final("Option 4"),
 "summary", [("1", "Says bias ‘persists’; the passage asks whether it still helps."), ("2", "Doubts the past benefit, which the passage accepts."), ("3", "‘Render it obsolete’ answers what the passage only asks.")])

# ---------------- Passage 1 (Q2–5) ----------------
P.rc(2, "V1", "Inference", "3", "Medium",
 "What does the whole discussion take for granted from its first lines?",
 steps(("The frame", ev(1, "The discovery confirmed Albert Einstein’s prediction of such waves") +
          p("Everything after (sources, detection, wavelengths) works inside Einstein’s account of gravity as distortions of space-time. That framework is assumed throughout.")),
       ("Why not 1", p("That accelerating masses make waves is stated as a fact within the passage, a consequence of the framework rather than the underlying assumption."))) + final("Option 3"),
 "inference", [("1", "Stated, and itself part of Einstein’s theory."), ("2", "Reverses cause and effect."), ("4", "Not ‘sole’: the passage describes two kinds of source.")])
P.rc(3, "V1", "Detail_Not_True", "1", "Easy",
 "Which waves were short and which long?",
 steps(("The facts", ev(1, "Physicists describe these as high-frequency, short-wavelength waves") +
          p("The 2015 signals were short-wavelength; the hum is long-wavelength and faint. Option 1 swaps them."))) + final("Option 1"),
 "notrue", [("2", "Correct: different frequencies and black-hole sizes."), ("3", "Correct: LIGO versus pulsar timing arrays."), ("4", "Broadly correct: detector arms versus stretching of the universe.")])
P.rc(4, "V1", "Inference_Except", "2", "Hard",
 "How firm is the southern asymmetry?",
 steps(("The line", ev(2, "This surprising asymmetry is one of several new puzzles for astronomers to investigate, hinting at uneven distributions") +
          p("A slightly stronger hum from the southern sky is a puzzle and a hint. The discovery doesn’t establish that black-hole pairs are more common there.")),
       ("The others", p("The hum comes from orbiting pairs scattered across the cosmos, continuously (1), and it confirms gravity’s wave nature as distortions of space-time (3, 4)."))) +
 trap("Option 2 sounds like the passage, but ‘hinting’ and ‘puzzles to investigate’ stop short of a finding.") + final("Option 2"),
 "except", [("1", "Indicated: many orbiting pairs, emitting for thousands of years."), ("3", "Indicated: waves are ripples in space-time."), ("4", "Indicated: a second kind of gravitational wave.")])
P.rc(5, "V1", "Inference", "1", "Medium",
 "Why do distant pulsars make a ‘vast detector’?",
 steps(("The method", ev(3, "As low-frequency gravitational waves drift by, the pulsars are nudged, altering their radio emissions by a tiny amount") +
          p("Waves with wavelengths of a light-year need a detector spanning light-years. The great distances let tiny distortions show up in pulse timing."))) + final("Option 1"),
 "inference", [("2", "Numbers help sensitivity, but the sentence is about size."), ("3", "The opposite: the sources are cosmic."), ("4", "The opposite: the signals work.")])

P.va(6, P.missing_html(6), P.Q["VARC"][6]["opts"], "MCQ", "3", "Missing_Sentence", "Medium",
 "‘Moreover … dangerous’ adds a second risk right after ‘inherently risky’.",
 steps(("Find the spot", p("Blank 4 follows ‘an endeavor both exorbitantly costly and inherently risky’. The sentence expands on the risk; the last sentence adds a further complication.")),
       ("Match the label", p("Blank 4 is choice 3, labelled ‘Option 4’."))) + final("Choice 3 (“Option 4”)"),
 "missing", [("1", "“Option 1”: about the two camps being separate."), ("2", "“Option 2”: between the camps’ dispute and ‘the divide … narrowing’."), ("4", "“Option 3”: before the costs and risks are explained.")])

# ---------------- Passage 2 (Q7–10) ----------------
P.rc(7, "V2", "Inference", "2", "Hard",
 "Which item only shows the land was altered, not that people lived there over time?",
 steps(("The evidence", p("Once-populated sites and transplanted trees (1), maize pollen (3) and canals and ponds for farming (4) each point to people living and working there.")),
       ("The odd one", p("A modified landscape on its own could come from short-term or occasional use. It overturns the ‘pristine’ idea but doesn’t prove sustained habitation by itself."))) + final("Option 2"),
 "inference", [("1", "Direct evidence of settlement."), ("3", "Long-term farming."), ("4", "Year-round water management.")])
P.rc(8, "V2", "Detail", "3", "Easy",
 "Which detail shows people being treated unequally?",
 steps(("The line", ev(3, "Diverse ways of burying the dead—some more opulent than others—imply a social hierarchy") +
          p("The passage draws the inference itself."))) + final("Option 3"),
 "detail", [("1", "Shows organisation, not rank."), ("2", "Coordination isn’t hierarchy."), ("4", "Says nothing about rank.")])
P.rc(9, "V2", "Inference", "3", "Hard",
 "A catastrophic decline should leave a break. Which option shows the culture vanished?",
 steps(("The hypothesis", ev(3, "As for the fate of the Casarabe people, many suspect they were ravaged by Old World diseases") +
          p("If disease wiped them out, there should be no cultural line to people living there now. The Sirionós today have ‘no connection to the Casarabe culture’: a clean break.")),
       ("Why not 1", p("Abandonment around 1400, a century before Columbus, can’t be caused by Old World diseases; and the passage adds that others stayed until at least 1550. It cuts against the disease explanation."))) +
 trap("Option 1 mentions decline, but its date predates European contact.") + final("Option 3"),
 "inference", [("1", "Predates contact; weakens the disease theory."), ("2", "About trade, not decline."), ("4", "Speculative; nothing in the passage links hierarchy to disease.")])
P.rc(10, "V2", "Inference", "1", "Medium",
 "Mounds over 20 m high, canals and ponds, trade, burial differences.",
 steps(("The evidence", ev(2, "Lombardo’s group has identified a system of canals and ponds near the mounds") +
          p("Monumental earthworks and water systems need large, organised labour; a hierarchy implies different roles."))) + final("Option 1"),
 "inference", [("2", "They built permanent mounds."), ("3", "Burials imply hierarchy."), ("4", "Maize ‘to the exclusion of almost anything else’.")])

P.va(11, P.summary_html(11, "There are several"), P.Q["VARC"][11]["opts"], "MCQ", "3", "Summary", "Hard",
 "Speakers use characters like authors do; theory has no room for it.",
 steps(("Choosing", p("Option 3 has both halves: characters in everyday speech, and theories that don’t account for them."))) + final("Option 3"),
 "summary", [("1", "‘Overlooked phenomenon’ and ‘lack precise criteria’ is a detail."), ("2", "Makes the proposal the main point."), ("4", "Leaves out the comparison with literary authors.")])
P.va(12, P.missing_html(12), P.Q["VARC"][12]["opts"], "MCQ", "4", "Missing_Sentence", "Easy",
 "‘The temple’ needs the temple to have been named.",
 steps(("Find the spot", p("Blank 2 follows the introduction of the Kailashnath Temple; the next sentence begins describing its structure.")),
       ("Match the label", p("Blank 2 is choice 4, labelled ‘Option 2’."))) + final("Choice 4 (“Option 2”)"),
 "missing", [("1", "“Option 1”: no temple yet."), ("2", "“Option 4”: after the closing praise."), ("3", "“Option 3”: inside the account of how it was carved.")])

# ---------------- Passage 3 (Q13–16) ----------------
P.rc(13, "V3", "Inference_Except", "2", "Hard",
 "Who says nature is inexhaustible: the neoclassical model, or the Cornucopians it came from?",
 steps(("Neoclassical Scarcity", ev(1, "scarcity of goods leads to high prices, which spurs innovation to find new resources, substitutes, or production methods") +
          p("It is a cultural creation (1), it assumes insatiable desire (3), and scarcity drives innovation (4).")),
       ("The odd one", p("‘Nature is inexhaustible’ is the Cornucopian belief, its ancestor. The neoclassical model still starts from scarcity."))) + final("Option 2"),
 "except", [("1", "The authors ‘denaturalize’ it."), ("3", "Insatiable desire for consumption."), ("4", "Scarcity spurs innovation.")])
P.rc(14, "V3", "Detail_Not_True", "3", "Medium",
 "Which item belongs to the older view the modern one replaced?",
 steps(("The factors", ev(2, "the explosion of consumer culture, bourgeois anxieties about labor unrest, and a view of the world as “stock” to be exploited") +
          p("Plus the drive for ever-increasing riches, 2 percent growth.")),
       ("The odd one", p("Distaste for greed belongs to Neo-Aristotelian Scarcity, the view that was displaced."))) + final("Option 3"),
 "notrue", [("1", "Named."), ("2", "Named."), ("4", "Named as the vision unleashed.")])
P.rc(15, "V3", "Purpose", "1", "Easy",
 "Bacon speaks of the scientist who must ‘conquer and subdue’ nature.",
 steps(("The line", ev(3, "Some of these thinkers applied a violently patriarchal model to the task of discovery") +
          p("Bacon illustrates the belief that nature’s treasure could be forced open."))) + final("Option 1"),
 "purpose", [("2", "No moral controls are discussed."), ("3", "Not ‘universally criticized’."), ("4", "Others ‘emphasized harmony’, but that isn’t why Bacon is cited.")])
P.rc(16, "V3", "Application", "2", "Easy",
 "Scarcity → high price → innovation → lower price.",
 steps(("Match", p("A mineral shortage leads firms to cheaper synthetics: the full neoclassical loop."))) + final("Option 2"),
 "inference", [("1", "Restriction, not innovation."), ("3", "Restraint, not innovation."), ("4", "Limiting production is the older, restraint view.")])

# ---------------- Passage 4 (Q17–20) ----------------
P.rc(17, "V4", "Inference", "3", "Medium",
 "What does the author want us to learn from Weimar?",
 steps(("Context", ev(1, "we find ourselves globally in an exceedingly fragile phase of technological and political transition") +
          p("Then: ‘don’t assume the next phase of history will provide any relief’. Weimar is useful as a warning of how fragile structures fail under pressure: ‘the new arrangement was just too weak to withstand the pressures of what was to come.’"))) + final("Option 3"),
 "inference", [("1", "True of Weimar, but not its lesson."), ("2", "The author sees ‘no Hitler in our midst’."), ("4", "Not suggested.")])
P.rc(18, "V4", "Inference", "3", "Medium",
 "Why is Weimar ‘permanent’ for us?",
 steps(("The line", ev(3, "we are connected enough by globalization to affect each other intimately without having the possibility of true global governance") +
          p("Problems travel across the world, but no global solution can form."))) + final("Option 3"),
 "inference", [("1", "The opposite: no true global governance."), ("2", "Not argued."), ("4", "The author rejects this.")])
P.rc(19, "V4", "Tone", "3", "Medium",
 "‘Truly, we are all trapped with each other.’ But: ‘that is not the worst outcome’.",
 steps(("The tone", ev(3, "And that is not the worst outcome") +
          p("Worried, but not apocalyptic: Weimar ‘might ultimately have righted itself’. Pessimistic yet reserved."))) + final("Option 3"),
 "inference", [("1", "No optimism about institutions."), ("2", "The author takes a view."), ("4", "Nowhere advocated.")])
P.rc(20, "V4", "Application", "2", "Medium",
 "What happened to Weimar under depression?",
 steps(("The parallel", ev(3, "But catastrophes like the Great Depression doomed the republic") +
          p("A connected world without real governance would likely fracture further under a severe downturn."))) + final("Option 2"),
 "inference", [("1", "Shared governance is said to be impossible."), ("3", "No such institutions are relied on."), ("4", "‘Immediately’ and ‘authoritarian’ go too far.")])

P.va(21, P.summary_html(21, "China's Chang'e"), P.Q["VARC"][21]["opts"], "MCQ", "1", "Summary", "Hard",
 "Samples from a young region; crater-counting had only been checked against old regions.",
 steps(("Choosing", p("Option 1 has the mission, the young region and the crater-counting models the samples test."))) +
 trap("Options 2 and 4 attribute the young age to the samples; the passage says orbital imagery suggested it.") + final("Option 1"),
 "summary", [("2", "The young age came from imagery, not the samples."), ("3", "Leaves out the young region, which is the point of the samples."), ("4", "Same problem as 2; thermal history is a side point.")])
P.va(22, P.missing_html(22), P.Q["VARC"][22]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "‘This phenomenon’ needs a described phenomenon; ‘ready youth’ fits after the conclusion about early learning.",
 steps(("Find the spot", p("Blank 3 follows ‘Such early auditory learning illustrates the powerful role of parental influence from the very start of life.’ The sentence sums up before the turn to human children.")),
       ("Match the label", p("Blank 3 is choice 1, labelled ‘Option 3’."))) + final("Choice 1 (“Option 3”)"),
 "missing", [("2", "“Option 1”: before the example."), ("3", "“Option 4”: the paragraph has moved to humans."), ("4", "“Option 2”: in the middle of the zebra-finch example.")])

P.va(23, P.sent_html(23), [], "TITA", "4", "Odd_One_Out", "Medium",
 "Four sentences: three champions of austerity, what they do, and what the evidence says. One offers another explanation.",
 steps(("The chain", p("2 → 1 → 5 → 3: three figures champion austerity (2); the UK case (1); Argentina and the US (5); evidence that austerity hurts (3).")),
       ("The odd one", p("Sentence 4 adds ‘another possible explanation’ about geopolitics, a thread the others don’t set up."))) + final("4"),
 "oddone", [("1", "The UK example."), ("2", "The opening."), ("3", "The verdict."), ("5", "The other two examples.")], why_title="How the other sentences fit")
P.va(24, P.sent_html(24), [], "TITA", "2", "Odd_One_Out", "Hard",
 "Four sentences are about the regime and authentic Russian spirituality. One is a general question about fundamentalists.",
 steps(("The chain", p("3 → 1 → 4 → 5: the regime doesn’t match genuine Russian spirituality (3); its ‘Eurasia’ is a facade (1); authentic versus perverted fundamentalists (4); revive authentic values against those in power (5).")),
       ("The odd one", p("Sentence 2 asks a general rhetorical question, not tied to Russia."))) + final("2"),
 "oddone", [("1", "The facade."), ("3", "The claim."), ("4", "The distinction."), ("5", "The remedy.")], why_title="How the other sentences fit")
