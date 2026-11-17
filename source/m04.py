# -*- coding: utf-8 -*-
# Simp Mock 4: VARC (24 of 24). DILR and QA: m04_dilr.py, m04_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(4, "sm04.json")
P.passage("V1", "Passage 1 — Public goods provided privately", "Economics_and_Management")
P.passage("V2", "Passage 2 — Growth after trauma", "Philosophy_and_Psychology")
P.passage("V3", "Passage 3 — Gradients that shape the Earth", "Science_and_Technology")
P.passage("V4", "Passage 4 — Misinformation and social epistemology", "Philosophy_and_Psychology")

# Q18: sentence 2 made to follow sentence 1 unambiguously.
P.Q["VARC"][18]["q"] = P.Q["VARC"][18]["q"].replace("2. The ability to think abstractly is linked to higher intelligence", "2. Thinking abstractly is also linked to higher intelligence")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Except", "2", "Medium",
 "Which option brings in examples the quotation never touches?",
 steps(("Paragraph 1", ev(1, "the provision of public or collective goods is the fundamental function of organizations generally") +
          ev(1, "There is no suggestion here that states or other organizations provide only public or collective goods")),
       ("Choosing", p("Options 1, 3 and 4 follow from it: governments are organisations whose basic job is collective goods; other organisations can provide them too; and such goods give a generalised benefit. Unemployment, housing and food assistance are never mentioned, and they go to particular people, so option 2 is not implied."))) +
 final("Option 2"),
 "except",
 [("1", "Governments are organisations whose basic function this is."), ("3", "‘States or other organizations’: others provide them too."), ("4", "‘An inseparable, generalized benefit’.")],
 opts=["The provision of collective goods is a key responsibility of governments.",
       "Unemployment, housing and food assistance are examples of collective goods.",
       "Organisations other than governments can also provide collective goods.",
       "Organisations provide offerings whose benefits reach consumers generally."])

P.rc(2, "V1", "Application", "3", "Medium",
 "An externality falls on someone other than the intended user or buyer.",
 steps(("The idea", ev(2, "This is known as \"extending the role of the firm\" to solve externalities") +
          p("An externality is a side effect on others: a spill-over benefit or a cost no one paid for.")),
       ("Choosing", p("R&D knowledge that others use, factory noise and global warming all fall on people outside the deal. The resident enjoying a park is its intended user, so that benefit is not an externality: option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "A spill-over benefit to others."), ("2", "A cost borne by neighbours."), ("4", "A cost borne by everyone.")],
 q="Which of the following is NOT an externality?")

P.rc(3, "V1", "Inference", "3", "Medium",
 "Negate each option and see which negation clashes with the passage.",
 steps(("Negations", p("If options 1, 2 and 4 are false, their opposites are exactly what the passage says (norms help, coupling helps, people care about others).")),
       ("Option 3", ev(1, "Governments often provide noncollective goods like electric power and they usually sell such goods on the market") +
          p("If option 3 were false, government provision would always make a good non-rival and non-excludable. Electric power sold on the market shows otherwise."))) +
 final("Option 3"),
 "inference",
 [("1", "Its negation agrees with paragraph 4."), ("2", "Its negation agrees with paragraph 2."), ("4", "Its negation agrees with paragraph 3.")])

P.rc(4, "V1", "Detail", "2", "Easy",
 "What do repeated games and norms do in the last paragraph?",
 steps(("The line", ev(4, "In repeated games norms like fairness and equality can increase private contributions") +
          ev(4, "The punishment of norm-violators through social sanctions will help to make people follow the norm without the government having to police norm following")),
       ("Choosing", p("Option 2."))) +
 final("Option 2"),
 "detail",
 [("1", "No comparison with government provision."), ("3", "Game theory explains; it is not offered as a rule for decisions."), ("4", "Norms help private provision; no preference for government.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Main_Idea", "3", "Medium",
 "Most of the passage argues for one approach.",
 steps(("The thread", p("Paragraph 2 sets out the problem with the evidence. Paragraphs 3–5 argue that PTG should be studied as personality change, which clarifies theory and shows which kinds of change occur.")),
       ("Choosing", p("Option 3 states that argument."))) +
 final("Option 3"),
 "inference",
 [("1", "One benefit only."), ("2", "The problem, not the argument."), ("4", "One example from paragraph 4.")])

P.rc(6, "V2", "Except", "3", "Easy",
 "One option is a reason designs are used, not a weakness.",
 steps(("The line", ev(2, "most research on PTG has employed cross-sectional designs, which are economical and feasible, but potentially reflect post hoc reconstruction of change rather than actual change")),
       ("Choosing", p("Being cheaper and quicker is an advantage: option 3."))) +
 final("Option 3"),
 "except",
 [("1", "‘Misremember their prior state’."), ("2", "‘Social desirability pressures resulting from the cultural narrative’."), ("4", "Measured right after the event, they cannot show lasting change.")])

P.rc(7, "V2", "Inference", "4", "Medium",
 "Paragraph 3 recommends the personality framework.",
 steps(("The line", ev(3, "Given that theories of PTG frame the phenomenon in terms of personality change, it should be evaluated in those terms") +
          ev(3, "Doing so opens a set of interesting questions that can be answered through a personality framework")),
       ("Choosing", p("Option 4 says this."))) +
 final("Option 4"),
 "inference",
 [("1", "The paragraph calls personality ‘relatively enduring’."), ("2", "The paragraph argues for personality measures, not their limits."), ("3", "Not discussed.")],
 q="Which of the following statements is most in line with the third paragraph?")

P.rc(8, "V2", "Inference", "1", "Easy",
 "Which method does the author criticise?",
 steps(("The line", ev(2, "potentially reflect post hoc reconstruction of change rather than actual change")),
       ("Choosing", p("The author would not support cross-sectional designs and reconstructed change: option 1."))) +
 final("Option 1"),
 "inference",
 [("2", "The ‘levels’ in which PTG appears."), ("3", "Life narratives and behaviour: paragraph 3."), ("4", "Fits the author’s concern with actual change.")])

# ---------------- Passage 3 (Q9–12) ----------------
P.rc(9, "V3", "Except", "3", "Easy",
 "‘Can … evolve’ is not ‘must’.",
 steps(("The line", ev(1, "can determine non-linearity, chaos and self-organization that can ultimately evolve into catastrophic collective behaviors")),
       ("Choosing", p("Catastrophe is possible, not inevitable: option 3 cannot be inferred."))) +
 final("Option 3"),
 "except",
 [("1", "Gradients arise in many parameters."), ("2", "Several gradients together give non-linearity."), ("4", "The definition in the first sentence.")])

P.rc(10, "V3", "Except", "4", "Easy",
 "Can anything defy gravity in the passage?",
 steps(("The line", ev(3, "gravity never stops working")),
       ("Choosing", p("Self-organisation is mentioned, but defying the laws of physics is not: option 4."))) +
 final("Option 4"),
 "except",
 [("1", "Landslides and eruptions are gradient effects."), ("2", "Catastrophic collective behaviour."), ("3", "Gradients make Earth able to host life.")])

P.rc(11, "V3", "Main_Idea", "2", "Hard",
 "Paragraph 2 ties several processes to life on Earth.",
 steps(("The line", ev(2, "Earth hosts Life because of the mobility of its mantle, thermal gradients inducing volcanic eruptions and velocity differences among crustal volumes provoking faulting, mountain growth and ocean spreading") +
          p("Gradients drive linked processes — mantle, volcanoes, faults, oceans — that shape the planet and let it sustain life.")),
       ("Choosing", p("Option 2 has both the linked processes and their role."))) +
 final("Option 2"),
 "inference",
 [("1", "Life is one outcome; the paragraph is about how gradients drive the planet."), ("3", "Leaves out why it matters."), ("4", "The mantle is one of several factors.")])

P.rc(12, "V3", "Except", "3", "Hard",
 "The quoted gradients smooth the surface. Which option builds irregularities?",
 steps(("The line", ev(3, "it is a succession of gradients that shape the Earth’s surface, with a tendency to decrease or eliminate morphological irregularities")),
       ("Choosing", p("Dunes piling up in some places add irregularity: option 3 goes against the quoted tendency."))) +
 final("Option 3"),
 "except",
 [("1", "Restates the tendency."), ("2", "Erosion that smooths."), ("4", "Gradients producing regular patterns.")])

# ---------------- Passage 4 (Q13–16) ----------------
P.rc(13, "V4", "Inference", "1", "Medium",
 "Negate each option.",
 steps(("Negations", p("If option 1 is false, social epistemology can help understand disinformation — which the passage says. The negations of options 2, 3 and 4 clash with the passage.")),
       ("Evidence", ev(3, "social epistemology has much to say to those faced with the challenging task of protecting democracy from misinformation"))) +
 final("Option 1"),
 "inference",
 [("2", "Its negation clashes with paragraph 3."), ("3", "Its negation denies the ‘social aspects of knowledge and belief formation’."), ("4", "Its negation makes knowledge individual, against ‘human beliefs are deeply social’.")])

P.rc(14, "V4", "Detail", "4", "Medium",
 "What does the passage say epistemic injustices do to democracy?",
 steps(("The line", ev(5, "Epistemic injustices may leave some members of society ill-equipped to engage in the debates that fuel a well-functioning democracy")),
       ("Choosing", p("Option 4 says this for epistemic injustice in general. Option 1 is the effect of testimonial injustice only."))) +
 final("Option 4"),
 "detail",
 [("1", "Only testimonial injustice."), ("2", "A form of injustice, not the threat to democracy."), ("3", "Misinformation is a separate threat.")])

P.rc(15, "V4", "Application", "2", "Medium",
 "Hermeneutical injustice is lacking the concepts to make sense of an experience, because one’s group is powerless.",
 steps(("The line", ev(4, "This occurs when, as a result of a group being socially powerless, members of the group lack the conceptual resources to make sense of certain distinctive social experiences")),
       ("Choosing", p("Options 1, 3 and 4 are all about missing concepts. In option 2 the woman can name and understand the wrong done to her; the injustice is economic, not a gap in understanding."))) +
 final("Option 2"),
 "inference",
 [("1", "No word yet for the experience."), ("3", "No shared words, because of no voice."), ("4", "No concepts, because kept out of institutions.")],
 opts=["Before the term ‘sexual harassment’ came into use, women struggled to describe their experiences at work, even to themselves.",
       "A woman is offered lower pay than a man for doing the same work.",
       "Workers in an unrecognised informal trade have no shared words for the harms of their working conditions, because they have had no voice in public debate.",
       "A marginalised community lacks the concepts to make sense of a new form of exclusion, because its members are kept out of the institutions where such ideas are formed."])

P.rc(16, "V4", "Main_Idea", "2", "Medium",
 "Which option covers misinformation, social epistemology and epistemic injustice?",
 steps(("The thread", ev(3, "social epistemology has much to say to those faced with the challenging task of protecting democracy from misinformation") +
          p("The passage moves from misinformation to social epistemology, then to epistemic injustice and the free-speech dilemma — all as threats to democratic knowledge.")),
       ("Choosing", p("Option 2 covers the whole."))) +
 final("Option 2"),
 "inference",
 [("1", "A detail from paragraph 2."), ("3", "Only the first paragraphs."), ("4", "Only paragraphs 4 and 5.")],
 opts=["The development of algorithms to judge whether online stories are true.",
       "How social epistemology bears on threats to democracy, from online misinformation to epistemic injustice.",
       "The spread of fake news on the internet and the failure of algorithms to stop it.",
       "The notion of epistemic injustice and its forms."])

Q24_OPTS = ["The human psyche has three parts — desire, reason and thymos — as Socrates and Adeimantus saw over two millennia ago; thymos, overlooked by modern economics, is the seat of judgments of worth, bringing pride, or anger or shame, depending on recognition by others.",
       "Socrates and Adeimantus saw that besides desire and reason the psyche has thymos, the seat of judgments of worth, which come mostly from within a person and bring pride or shame; modern economics has ignored it.",
       "Thymos, the third part of the psyche recognised by Socrates and Adeimantus, decides judgments of worth and brings pride, or anger or shame, depending on others’ recognition, while desire and reason play minor roles; modern economics does not acknowledge it.",
       "Socrates and Adeimantus understood thymos, unrecognised by modern economics, as the seat of judgments of worth, essential for understanding desire and reason and their link with pride, anger or shame, depending on recognition by others."]

# ---------------- Verbal ability (Q17–24) ----------------
P.va(17, P.sent_html(17), [], "TITA", "1234", "Para_Jumble", "Medium",
 "‘Despite the many different perspectives and debates’ looks back at debates already described.",
 steps(("The opener", p("Sentence 1 introduces time as central but elusive.")),
       ("The sequence", p("Sentence 2: thinkers have explored it and proposed many theories. Sentence 3: the most influential of them, Einstein’s. Sentence 4 sums up: despite all the debates, time is fundamental."))) +
 final("1234"),
 "pj",
 [("1", "Introduces the topic."), ("2", "Many theories."), ("3", "The most influential one."), ("4", "“Despite the … debates”: the conclusion.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.sent_html(18), [], "TITA", "1243", "Para_Jumble", "Easy",
 "‘Also’ in sentence 2 and ‘these limitations’ in sentence 3.",
 steps(("The opener", p("Sentence 1 introduces abstract thought.")),
       ("The sequence", p("Sentence 2 adds another benefit (‘also’). Sentence 4 turns to limits (‘However’). Sentence 3 closes: despite these limitations, it is worth studying."))) +
 final("1243"),
 "pj",
 [("1", "Introduces abstract thought."), ("2", "“Also”: a further benefit."), ("4", "“However”: limits."), ("3", "“Despite these limitations”.")],
 why_title="Why each sentence goes where it does")

P.va(19, P.sent_html(19), [], "TITA", "2134", "Para_Jumble", "Medium",
 "‘One of the main challenges’ cannot open; which sentence sets the scene?",
 steps(("The opener", p("Sentence 2 introduces AI and its progress.")),
       ("The sequence", p("Sentence 1 raises the question of machine consciousness. Sentence 3 gives the two sides. Sentence 4 names a main obstacle: we do not know what consciousness is."))) +
 final("2134"),
 "pj",
 [("2", "Sets the scene."), ("1", "The question."), ("3", "Two sides."), ("4", "A challenge.")],
 why_title="Why each sentence goes where it does")

P.va(20, P.missing_html(20), P.strict_opts(20), "MCQ", "4", "Missing_Sentence", "Medium",
 "‘Moreover’ adds a new kind of benefit after the list of travellers’ practices.",
 steps(("Find the spot", p("Blanks 2 and 3 are inside a run about what travellers do (cut plastic, support local businesses, respect customs; minimise waste, save energy). The sentence turns from travellers’ behaviour to the economic benefit to communities, so it fits after that run, at blank 4.")),
       ("Check the others", p("Blank 1 comes before sustainable tourism is defined. At blank 3 it would repeat ‘supporting local businesses’ and split the ‘also promotes responsible travel behaviors’ sentence from the list it continues."))) +
 final("Option 4"),
 "missing",
 [("1", "Before the topic is introduced."), ("2", "Before the practices are listed."), ("3", "Breaks the list of practices.")])

P.va(21, P.missing_html(21), P.strict_opts(21), "MCQ", "3", "Missing_Sentence", "Easy",
 "‘Furthermore’ adds another harm of lack of sleep.",
 steps(("Find the spot", p("Blank 3 follows the list of health problems; the sentence adds harm to thinking, and ‘In addition, … more likely to make mistakes’ follows naturally.")),
       ("Check the others", p("Blanks 1 and 2 come before sleep deprivation is mentioned; blank 4 is after the mistakes and accidents, just before the conclusion."))) +
 final("Option 3"),
 "missing",
 [("1", "No sleep deprivation yet."), ("2", "Still on the benefits of sleep."), ("4", "Mistakes depend on the cognitive harm, so it should come first.")])

P.va(22, P.summary_html(22, "A few months before he died"), P.Q["VARC"][22]["opts"], "MCQ", "4", "Summary", "Medium",
 "Story, its turn and what it says about Kafka.",
 steps(("What the passage says", "<ol><li>In ‘The Burrow’ a creature builds a home for protection.</li><li>It is soon consumed by doubt about its defences.</li><li>The story reflects Kafka’s own lifelong anxiety about disease.</li></ol>"),
       ("Choosing", p("Option 4 has all three."))) +
 final("Option 4"),
 "summary",
 [("1", "Leaves out the story itself."), ("2", "Makes the creature a metaphor for medical defences only."), ("3", "Generalises to all humans; Kafka disappears.")])

P.va(23, P.summary_html(23, "People with long COVID"), P.Q["VARC"][23]["opts"], "MCQ", "3", "Summary", "Medium",
 "Symptoms, scale, neurological core, unknown cause.",
 steps(("What the passage says", "<ol><li>Long COVID brings pain, fatigue and brain fog to millions.</li><li>Its most common and disabling symptoms are neurological.</li><li>Its cause is uncertain; several are being studied.</li></ol>"),
       ("Choosing", p("Option 3 keeps all three without picking a cause."))) +
 final("Option 3"),
 "summary",
 [("1", "States the causes as fact."), ("2", "The controversy is about the syndrome’s cause, not its symptoms’ causes alone; ‘mired in controversy’ overstates it."), ("4", "Too much detail and leaves the cause sounding settled between two options.")])

P.va(24, P.summary_html(24, "More than two millennia"), Q24_OPTS, "MCQ", "1", "Summary", "Hard",
 "Thymos acts independently of desire and reason; worth is judged mostly by others.",
 steps(("What the passage says", "<ol><li>Socrates and Adeimantus saw a third part of the psyche, thymos, which modern economics misses.</li><li>Thymos seeks judgments of one’s worth.</li><li>These come mostly from others; recognition brings pride, its absence anger or shame.</li></ol>"),
       ("Choosing", p("Option 1 keeps all three."))) +
 final("Option 1"),
 "summary",
 [("2", "Says judgments of worth come mostly from within."), ("3", "Adds that desire and reason play minor roles."), ("4", "Makes thymos essential for understanding desire and reason, though it acts independently of them.")])
