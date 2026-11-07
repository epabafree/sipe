# -*- coding: utf-8 -*-
# Batch 10 — CAT 2021 Slot 3: VARC (Q1–24). DILR and QA: b10_21s3_dilr.py, b10_21s3_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2021, 3, "ex10_21s3.json")
P.passage("P1", "Passage 1 — The price of keeping time", "Science_and_Technology")
P.passage("P2", "Passage 2 — Pinker’s The Language Instinct", "Philosophy_and_Psychology")
P.passage("P3", "Passage 3 — Soft robots", "Science_and_Technology")
P.passage("P4", "Passage 4 — How the unconscious took shape", "Philosophy_and_Psychology")

# ---------------- Verbal ability (Q1) ----------------
P.va(1, P.sent_html(1), [], "TITA", "2314", "Para_Jumble", "Hard",
 "Sentence 3 says a Foucauldian approach goes ‘beyond these conceptions’. Which conceptions?",
 steps(("The opener", p("Sentence 2 gives the standard view: relationships are made through communication and relational histories.")),
       ("Going further", p("Sentence 3 goes “beyond these conceptions” to regimes of truth. Sentence 1 explains what regimes of truth do, and sentence 4 draws the conclusion about power/knowledge."))) +
 final("2314"),
 "pj",
 [("2", "Communication and relational history."), ("3", "“Beyond these conceptions”: regimes of truth."), ("1", "What regimes of truth do."), ("4", "The conclusion: power/knowledge.")],
 why_title="Why each sentence goes where it does")

# ---------------- Passage 1: Clocks ----------------
P.rc(2, "P1", "Inference", "2", "Hard",
 "Only one option follows from the passage. Look at what it says about clocks in quantum computers.",
 steps(("The relevant lines", ev(1, "as they increased the clock’s accuracy, the heat produced in the system grew") + ev(4, "particularly those used in quantum computers and other devices where both accuracy and temperature are crucial") +
          p("Clocks that must be very accurate pay for it in heat and entropy, and quantum computers need very accurate clocks. Option 2 follows.")),
       ("The others", p("The arrow of time isn’t what is untested for atomic clocks; a less accurate clock doesn’t have to produce less heat, because the relationship is only a limit; and the membrane is vibrated by a current, it doesn’t produce one."))) +
 final("Option 2"),
 "inference",
 [("1", "It is the accuracy–entropy relationship that is untested for atomic clocks."), ("3", "The relationship is a limit, so it doesn’t run in reverse."), ("4", "The current drives the membrane; it isn’t produced by it.")])

P.rc(3, "P1", "Except", "2", "Hard",
 "What exactly does the passage say you ‘pay’ for accuracy with?",
 steps(("The relevant line", ev(1, "“If a clock is more accurate, you are paying for it somehow,” says Ares. In this case, you pay for it by pouring more ordered energy into the clock, which is then converted into entropy.") +
          p("The price is ordered energy turned into entropy. Heat is how the entropy spreads, but the passage never calls the heat itself the price, so option 2 isn’t an argument the author makes.")),
       ("Option 3", p("Option 3 is close to the passage’s “a large, inefficient grandfather clock isn’t more precise than an atomic clock”. The official key treats it as made, so option 2 is the answer."))) +
 final("Option 2 (official answer)"),
 "except",
 [("1", "¶4: the results may not be universal."), ("3", "Close to ¶3’s grandfather clock line; the key accepts it."), ("4", "¶4: accuracy and temperature both matter for quantum computers.")])

P.rc(4, "P1", "Purpose", "1", "Medium",
 "The example comes right after the point that the relationship is only a limit.",
 steps(("The point it illustrates", ev(3, "it doesn’t mean that a clock that creates the most possible entropy would be maximally accurate")),
       ("Choosing", p("Going faster uses more fuel, but using more fuel doesn’t make you faster. Likewise, more accuracy costs more entropy, but more entropy doesn’t give more accuracy."))) +
 final("Option 1"),
 "purpose",
 [("2", "Time saved by speed isn’t the point."), ("3", "Measuring a car’s speed has nothing to do with it."), ("4", "Turns the example into ‘more of everything’, which misses its point.")])

P.rc(5, "P1", "Main_Idea", "3", "Easy",
 "What is the passage about, in three words?",
 steps(("Choosing", p("The passage is about measuring time: accuracy has a price, paid in entropy. The other options list details."))) +
 final("Option 3"),
 "inference",
 [("1", "Details of the experiment."), ("2", "Details."), ("4", "The membrane and the arrow of time are side points.")])

# ---------------- Verbal ability (Q6–8) ----------------
P.va(6, P.sent_html(6), [], "TITA", "4", "Odd_One_Out", "Medium",
 "Four sentences explain why gender imbalance in tech matters for the technology itself. One talks about the workplace.",
 steps(("The chain", p("3 → 5 → 1 → 2: technology embodies its makers’ values (3), so a male-only perspective limits it (5), as with Wikipedia (1), leaving society with a distorted picture (2).")),
       ("The odd one", p("Sentence 4 turns to redressing workplace representation and broader social change. It moves away from what technology embodies."))) +
 final("4"),
 "oddone",
 [("3", "Technology embodies its makers’ values."), ("5", "So male perspectives limit it."), ("1", "An example."), ("2", "The consequence for society.")],
 why_title="How the other sentences fit")

P.va(7, P.summary_html(7, "People view idleness"), P.Q["VARC"][7]["opts"], "MCQ", "3", "Summary", "Medium",
 "The passage gives two sides: the downside of idealising work, and its benefits.",
 steps(("What the passage says", "<ol><li>Valuing industriousness has made work a way to keep busy, often meaninglessly.</li><li>On the other side, hard work has brought prosperity, health, education and innovation.</li></ol>"),
       ("Choosing", p("Option 3 keeps both sides."))) +
 final("Option 3"),
 "summary",
 [("1", "Adds advice about leisure that isn’t in the passage."), ("2", "Says hard work led to more idleness, which the passage doesn’t."), ("4", "Gives only one side.")])

P.va(8, P.sent_html(8), [], "TITA", "3", "Odd_One_Out", "Medium",
 "Four sentences describe Chinese business schools. One is about Western schools.",
 steps(("The chain", p("2 → 1 → 5 → 4: Chinese schools are growing distinct (2), their courses (1), who they cater to (5), and the draw for students (4).")),
       ("The odd one", p("Sentence 3 is about Western schools and their double degrees. It doesn’t follow the line about what makes Chinese schools distinct."))) +
 final("3"),
 "oddone",
 [("2", "Chinese schools are growing distinct."), ("1", "What their courses include."), ("5", "Whom they cater to."), ("4", "The draw for students.")],
 why_title="How the other sentences fit")

# ---------------- Passage 2: Pinker ----------------
P.rc(9, "P2", "Inference", "4", "Medium",
 "The last paragraph raises a worry about racism and then answers it. How?",
 steps(("The relevant line", ev(4, "Yet Mr. Pinker stresses one point that should allay such fears. Even though there are 4,000 to 6,000 languages today, they are all sufficiently alike to be considered one language")),
       ("Choosing", p("The universality of the language instinct answers the charge that the book is racist."))) +
 final("Option 4"),
 "inference",
 [("1", "The passage says chimps have the vocal apparatus; anatomy isn’t the key."), ("2", "The book argues for something innate, not shaped by culture."), ("3", "The author says this fear should be allayed.")])

P.rc(10, "P2", "Except", "1", "Easy",
 "What does the passage say about chimps?",
 steps(("The relevant line", ev(3, "He effectively disposes of all claims that intelligent nonhuman primates like chimps have any abilities to learn and use language.")),
       ("Choosing", p("Not all intelligent primates have the instinct, so option 1 isn’t true."))) +
 final("Option 1"),
 "except",
 [("2", "¶3: a selective reproductive advantage."), ("3", "¶2: neurosurgeons have located the ‘black box’."), ("4", "True: chimps lack it.")])

P.rc(11, "P2", "Inference", "2", "Easy",
 "Look for ‘Unlike Mr. Chomsky’.",
 steps(("The relevant line", ev(3, "Unlike Mr. Chomsky, Mr. Pinker firmly places the wiring of the brain for language within the framework of Darwinian natural selection and evolution.")),
       ("Choosing", p("They differ on the Darwinian explanation."))) +
 final("Option 2"),
 "inference",
 [("1", "Both believe language skills are inborn."), ("3", "Both accept a language instinct."), ("4", "Universal grammar is Chomsky’s idea, and Pinker uses it.")])

P.rc(12, "P2", "Except", "4", "Medium",
 "Which fields does Pinker draw on, according to the first paragraph?",
 steps(("The relevant line", ev(1, "he has gathered persuasive data from such diverse fields as cognitive neuroscience, developmental psychology and speech therapy") +
          p("Behavioural psychology isn’t one of them; behavioural psychologists are among those the book will annoy.")),
       ("The others", p("He builds on Chomsky, disagrees with him at times, and writes far more readably."))) +
 final("Option 4"),
 "except",
 [("1", "He brings Chomsky’s findings to everyman."), ("2", "“When he disagrees with Mr. Chomsky he tells you so.”"), ("3", "Chomsky is “nearly incomprehensible”; Pinker is “brilliant, witty”.")])

# ---------------- Verbal ability (Q13–14) ----------------
P.va(13, P.summary_html(13, "Brazil’s growth rate"), P.Q["VARC"][13]["opts"], "MCQ", "2", "Summary", "Medium",
 "Two points: most Brazilians feel better off, but the poor are still treated unfairly.",
 steps(("What the passage says", "<ol><li>Despite low growth, most Brazilians feel better off, with rising incomes.</li><li>Inequality is falling, but the economy is still very unequal.</li><li>The poor pay the most tax and get the least back.</li></ol>"),
       ("Choosing", p("Option 2 has both halves."))) +
 final("Option 2"),
 "summary",
 [("1", "The passage doesn’t say Brazilians are misled."), ("3", "Inequality is falling, not rising."), ("4", "Destabilisation is a prediction the passage doesn’t make.")])

P.va(14, P.sent_html(14), [], "TITA", "3214", "Para_Jumble", "Medium",
 "Sentence 2 begins ‘This is in response to…’. Response to what?",
 steps(("The opener", p("Sentence 3: European museums are struggling with their colonial legacy, some returning artefacts.")),
       ("Following it", p("Sentence 2 explains why: pressure from countries like Nigeria. Sentence 1 adds the legal obstacle, and sentence 4, “Legal hurdles notwithstanding”, says France and Germany are going ahead."))) +
 final("3214"),
 "pj",
 [("3", "Museums and their colonial legacy."), ("2", "“This is in response to” pressure."), ("1", "Legal obstacles."), ("4", "“Legal hurdles notwithstanding”.")],
 why_title="Why each sentence goes where it does")

# ---------------- Passage 3: Soft robots ----------------
P.rc(15, "P3", "Main_Idea", "3", "Medium",
 "Who are the heroes, and what is the new threat?",
 steps(("The paragraph", ev(1, "Our mutant heroes had been battling giant robots called Sentinels for years, but suddenly these mechanical overlords spawned a new threat: Nano-Sentinels!")),
       ("Choosing", p("The X-Men were the mutant heroes, and they now faced tiny robots, the Nano-Sentinels."))) +
 final("Option 3"),
 "inference",
 [("1", "The X-Men are the heroes, not the Sentinels."), ("2", "Option 3 matches the paragraph."), ("4", "Infected people became machines, not X-Men.")])

P.rc(16, "P3", "Inference", "3", "Medium",
 "‘If false, supports the passage’: find the statement the passage denies.",
 steps(("The relevant line", ev(2, "No, they won’t be invading our bodies and turning us into Sentinels")),
       ("Choosing", p("Option 3 says such robots will convert people into robots. The passage says the opposite, so this statement being false fits it."))) +
 final("Option 3"),
 "inference",
 [("1", "True according to the passage; if false, it would contradict it."), ("2", "Also true in the passage."), ("4", "The author hopes for this; its being false wouldn’t support the passage.")])

P.rc(17, "P3", "Inference", "2", "Easy",
 "The passage hopes some robots will one day swim through our bloodstream.",
 steps(("The relevant line", ev(2, "some of them could one day swim through our bloodstream to heal us")),
       ("Choosing", p("Robots that find and treat diseases deep in the body take this one step further."))) +
 final("Option 2"),
 "inference",
 [("1", "Mixes the comic with science; the passage keeps them apart."), ("3", "The passage says they won’t do this."), ("4", "Sending messages isn’t mentioned.")])

P.rc(18, "P3", "Main_Idea", "1", "Easy",
 "The passage opens with comics and moves to real research.",
 steps(("Choosing", p("Something from science fiction is now being built in labs. Option 1 says this."))) +
 final("Option 1"),
 "inference",
 [("2", "One example, and the sticky gel isn’t a nano-robot."), ("3", "The passage isn’t about comics."), ("4", "Water-reacting molecules are one example.")])

# ---------------- Passage 4: The unconscious ----------------
P.rc(19, "P4", "Main_Idea", "4", "Medium",
 "The passage describes how many unrelated ideas were drawn together. Under what?",
 steps(("The relevant line", ev(2, "Striving vaguely and independently to give expression to a latent conception, various lines of thought can be brought together by some novel term.")),
       ("Choosing", p("Diverse ideas collected under one term: the unconscious."))) +
 final("Option 4"),
 "inference",
 [("1", "Psychical research is one of many fields."), ("2", "The growing vocabulary is the background, not the subject."), ("3", "The passage is about the concept taking shape, not a discovery.")])

P.rc(20, "P4", "Inference", "3", "Easy",
 "What changed what? Language changed the meanings of old expressions.",
 steps(("Reading it", p("Richer literary and intellectual language changed how people understood traditional expressions."))) +
 final("Option 3"),
 "inference",
 [("1", "Reverses cause and effect."), ("2", "Options 1 and 4 don’t match."), ("4", "The meanings changed; the expressions weren’t ‘enriched’.")])

P.rc(21, "P4", "Main_Idea", "3", "Medium",
 "The passage runs from language, through the unconscious, to its fixed use in psychoanalysis.",
 steps(("Choosing", p("Language (the enriched vocabulary), the unconscious (the concept that collected the ideas), psychoanalysis (where it was finally defined). The other options miss language or pick details."))) +
 final("Option 3"),
 "inference",
 [("1", "Leaves out language."), ("2", "It is conventional language, not just literary language."), ("4", "Details.")])

P.rc(22, "P4", "Except", "4", "Medium",
 "Does the passage mention anaesthesiology as an established field?",
 steps(("What the passage says", p("Anaesthesia appears among the things physiologists and physicians puzzled over. The passage names psychology and psychical research as new disciplines, not anaesthesiology.")),
       ("The others", p("Unrelated practices being linked (option 1), the 1790 date (option 2), and the role of language (option 3) all follow."))) +
 final("Option 4"),
 "except",
 [("1", "¶2: “seemingly unrelated issues” brought together."), ("2", "¶2: before 1790 few spoke of it, so it began in the late 1700s."), ("3", "¶1–2: the new vocabulary made the concept possible.")])

# ---------------- Verbal ability (Q23–24) ----------------
P.va(23, P.summary_html(23, "The human mind is wired"), P.Q["VARC"][23]["opts"], "MCQ", "1", "Summary", "Medium",
 "Intuition is pattern recognition drawing on a large store of experience.",
 steps(("What the passage says", "<ol><li>The mind spots patterns using stored experience.</li><li>Intuition draws on that store, so it is based on data.</li><li>It works through neurochemical signals, faster than rational thought.</li></ol>"),
       ("Choosing", p("Option 1 keeps the mechanism and the source."))) +
 final("Option 1"),
 "summary",
 [("2", "“Infinitely richer” overstates it, and big data isn’t ‘rational thought’."), ("3", "The passage doesn’t say intuitive decisions are better."), ("4", "The passage says intuition is based on data.")])

P.va(24, P.sent_html(24), [], "TITA", "3412", "Para_Jumble", "Medium",
 "Sentence 2 begins ‘But in recent years’. What does it turn against?",
 steps(("The opener", p("Sentence 3: politicians promise to bring jobs back by restricting trade.")),
       ("The real threat", p("Sentence 4: economists say the bigger threat is automation. Sentence 1: businesses value automation. Sentence 2: but it now costs white-collar jobs too."))) +
 final("3412"),
 "pj",
 [("3", "Politicians’ promises."), ("4", "Economists: automation is the threat."), ("1", "Why businesses like it."), ("2", "“But”: the cost in jobs.")],
 why_title="Why each sentence goes where it does")
