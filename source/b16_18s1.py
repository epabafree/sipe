# -*- coding: utf-8 -*-
# Batch 16 — CAT 2018 Slot 1: VARC (21 of 34). DILR and QA: b16_18s1_dilr.py, b16_18s1_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2018, 1, "ex16_18s1.json")
P.passage("P1", "Passage 1 — Elephants and trauma", "Environment_and_Life_Science")
P.passage("P3", "Passage 3 — Measuring happiness", "Economics_and_Management")
P.passage("P4", "Passage 4 — More than genes", "Science_and_Technology")

# ---------------- Verbal ability (Q2–4) ----------------
P.va(2, P.sent_html(2), [], "TITA", "4213", "Para_Jumble", "Easy",
 "A story in time order. Where does it start?",
 steps(("The order", p("4: it started with a lump. 2: nobody knew what it was. 1: the diagnosis, and all seemed well. 3: then it came back."))) +
 final("4213"),
 "pj",
 [("4", "“It started with…”"), ("2", "Nobody knew what it was."), ("1", "The diagnosis and treatment."), ("3", "“Then” it came back.")],
 why_title="Why each sentence goes where it does")

P.va(3, P.summary_html(3, "Artificial embryo twinning"), P.Q["VARC"][3]["opts"], "MCQ", "1", "Summary", "Medium",
 "The passage stresses three things: low-tech, mimics nature, and genetically identical results.",
 steps(("What the passage says", "<ol><li>Embryo twinning is a low-tech way to clone.</li><li>It copies how identical twins form naturally, when an early embryo splits after fertilisation.</li><li>The individuals are genetically identical.</li></ol>"),
       ("Choosing", p("Option 1 keeps all three."))) +
 final("Option 1"),
 "summary",
 [("2", "Leaves out ‘genetically identical’ and the timing."), ("3", "Says ‘unlike’; it is like."), ("4", "Twins form after fertilisation, not during it.")])

P.va(4, P.sent_html(4), [], "TITA", "2", "Odd_One_Out", "Medium",
 "Which sentence talks about a ‘factoid’ the others never set up?",
 steps(("The chain", p("1 → 5 → 3 → 4: translators are like bumblebees (1); in 1934 the bumblebee’s flight was ‘proved’ impossible (5); similar claims dog translation (3); both carry on regardless (4).")),
       ("The odd one", p("Sentence 2 calls the claim a disproved factoid that is still trotted out. That shifts to the claim’s afterlife, which the paragraph doesn’t follow."))) +
 final("2"),
 "oddone",
 [("1", "The analogy."), ("5", "The bumblebee claim."), ("3", "The same for translation."), ("4", "Both carry on.")],
 why_title="How the other sentences fit")

# ---------------- Passage 1: Elephants ----------------
P.rc(5, "P1", "Main_Idea", "2", "Medium",
 "What do Bradshaw and her colleagues argue, against the usual explanations?",
 steps(("The argument", ev(2, "today’s elephant populations are suffering from a form of chronic stress, a kind of species-wide trauma") +
          p("The rest of the passage supports this."))) +
 final("Option 2"),
 "inference",
 [("1", "A supporting point at the end."), ("3", "The starting observation, not the argument."), ("4", "A supporting point.")])

P.rc(6, "P1", "Vocabulary", "2", "Easy",
 "Can a society literally fray?",
 steps(("The phrase", p("Fabric fraying is an image for the social network being damaged by poaching, culling and habitat loss."))) +
 final("Option 2"),
 "detail",
 [("1", "It is figurative, not a literal description."), ("3", "The author finds the evidence compelling."), ("4", "Not an ode.")])

P.rc(7, "P1", "Except", "4", "Medium",
 "Which claim is about mothers adapting, not failing?",
 steps(("What the passage says", p("Calves are now raised by younger, inexperienced mothers, and there is ‘inattentive mothering’.")),
       ("The odd one", p("Nothing about mothers evolving new ways to rear calves."))) +
 final("Option 4"),
 "except",
 [("1", "The extended, lifelong network."), ("2", "Poaching and culling cause stress."), ("3", "PTSD-like behaviour.")])

P.rc(8, "P1", "Detail", "2", "Easy",
 "Read why Bradshaw chooses the word.",
 steps(("The line", ev(1, "I use the term ‘violence’ because of the intentionality associated with it") +
          p("Intentionality is purposefulness."))) +
 final("Option 2"),
 "detail",
 [("1", "Not his reason."), ("3", "True but not why he uses the word."), ("4", "Not his reason.")])

P.rc(9, "P1", "Application", "1", "Medium",
 "Bradshaw sees the aggression as trauma, like PTSD in humans.",
 steps(("Choosing", p("If the cause is trauma, treatment modelled on PTSD treatment follows."))) +
 final("Option 1"),
 "inference",
 [("2", "General research, not addressing the problem."), ("3", "Isolation is the problem, not a study he would push."), ("4", "Testosterone is the explanation he moves away from.")])

# ---------------- Passage 3: Happiness ----------------
P.rc(15, "P3", "Inference", "2", "Hard",
 "The author isn’t against psychology in economics, but is uneasy about how it is used.",
 steps(("The tone", ev(3, "There is nothing automatically sinister about this trend. But it is disquieting") +
          p("Use psychology, but carefully."))) +
 final("Option 2"),
 "inference",
 [("1", "Neuroscientists are mentioned, not recommended."), ("3", "That is the measuring the author worries about."), ("4", "Not the author’s concern.")])

P.rc(16, "P3", "Detail", "3", "Medium",
 "What are happiness measures increasingly used for?",
 steps(("The line", ev(5, "they are increasingly used as a basis to transform or discipline individuals") +
          p("Wearables and social media are examples of this."))) +
 final("Option 3"),
 "detail",
 [("1", "Reducing stress is one product’s pitch, not the trend."), ("2", "Not claimed."), ("4", "The result, not what the technologies contribute to most.")])

P.rc(17, "P3", "Inference", "3", "Medium",
 "Since the 1970s, depression has been seen as the individual’s defect.",
 steps(("The line", ev(6, "All of this simply escalates the sense of responsibility each of us feels for our own feelings, and with it, the sense of failure") +
          p("More stress, as people carry their own happiness."))) +
 final("Option 3"),
 "inference",
 [("1", "Not suggested."), ("2", "The author isn’t welcoming it."), ("4", "Neuroscience comes up separately.")])

P.rc(18, "P3", "Weaken", "1", "Medium",
 "The author worries about growing data collection on well-being.",
 steps(("Undermining", p("If stakeholders were moving away from collecting such data, the worry would lose its basis."))) +
 final("Option 1"),
 "weaken",
 [("2", "Supports the trend."), ("3", "Supports the trend."), ("4", "Supports the trend.")])

P.rc(19, "P3", "Detail", "2", "Easy",
 "Read the Dubai sentence.",
 steps(("The line", ev(4, "dream up ever-more elaborate and intrusive ways of collecting data on well-being") +
          p("Monitoring its inhabitants’ states of mind."))) +
 final("Option 2"),
 "detail",
 [("1", "That is Facebook."), ("3", "It has pledged to; the passage doesn’t say it is on its way."), ("4", "Not mentioned.")])

# ---------------- Verbal ability (Q20, Q22) ----------------
P.va(20, P.sent_html(20), [], "TITA", "1432", "Para_Jumble", "Medium",
 "Follow the sunlight: canopy, insects above it, swifts hunting them.",
 steps(("The order", p("1: sunlight falls on the canopy. 4: insects fly above it, prey to swifts. 3: swifts are built to chase insects. 2: they hunt wherever insects are, not only woodlands."))) +
 final("1432"),
 "pj",
 [("1", "The canopy and sunlight."), ("4", "Insects above the canopy, and swifts."), ("3", "How swifts hunt."), ("2", "Not only woodlands.")],
 why_title="Why each sentence goes where it does")

P.va(22, P.sent_html(22), [], "TITA", "5", "Odd_One_Out", "Medium",
 "The paragraph is about slow, invisible displacement. Which sentence is about something else?",
 steps(("The chain", p("3 → 2 → 4 → 1: Bengal is an interesting case (3); erosion from the Ganges causes it (2); being slow, it stays invisible (4); so it doesn’t seem significant (1).")),
       ("The odd one", p("Sentence 5 speculates about rapid displacement, which isn’t this case."))) +
 final("5"),
 "oddone",
 [("3", "Introduces the case."), ("2", "The cause."), ("4", "Why it is invisible."), ("1", "“Thus”: the conclusion.")],
 why_title="How the other sentences fit")

# ---------------- Passage 4: Evolution ----------------
P.rc(23, "P4", "Detail", "2", "Medium",
 "What do the many dogs stand for?",
 steps(("The line", ev(3, "All these tugs represent the influence of developmental factors, including epigenetics, antibodies and hormones passed on by parents, as well as the ecological legacies and culture they bequeath") +
          p("Plus the genes, the dog-walker."))) +
 final("Option 2"),
 "detail",
 [("1", "Leaves out epigenetics and developmental factors as such."), ("3", "Leaves out ecology and development."), ("4", "Leaves out development and ecology.")])

P.rc(24, "P4", "Main_Idea", "2", "Easy",
 "‘Evolution is more complex than we once assumed’.",
 steps(("The argument", p("Natural selection plus genetic inheritance isn’t the whole story; epigenetic, cultural and parental factors matter too."))) +
 final("Option 2"),
 "inference",
 [("1", "Wilson’s metaphor needs revising."), ("3", "That is the dominant view the author questions."), ("4", "Not argued.")])

P.rc(25, "P4", "Weaken", "1", "Medium",
 "The message is that more than natural selection and genes is at work.",
 steps(("Negating", p("A study showing natural selection and inheritance alone drive evolution would contradict it."))) +
 final("Option 1"),
 "weaken",
 [("2", "Supports the message."), ("3", "Ecology is one of the factors."), ("4", "Culture is one of the factors.")])

P.rc(26, "P4", "Inference", "2", "Medium",
 "‘The inheritance of acquired characteristics is impossible’ — except here it happened.",
 steps(("The line", ev(1, "Generations of school children have been taught that the inheritance of acquired characteristics is impossible") +
          p("The fear was acquired by the parents and inherited: an acquired characteristic."))) +
 final("Option 2"),
 "inference",
 [("1", "Too narrow; the point is about acquired characteristics in general."), ("3", "Not the passage’s term."), ("4", "Not personality.")])

# ---------------- Verbal ability (Q28–29) ----------------
P.va(28, P.sent_html(28), [], "TITA", "1324", "Para_Jumble", "Hard",
 "Sentence 4 ends with ‘impartiality and objectivity’; sentence 1 starts with them. Which is the frame?",
 steps(("The opener", p("Sentence 1 introduces impartiality and objectivity as difficult ideals.")),
       ("The sequence", p("Sentence 3 quotes Twitter’s ‘…and much more’. Sentence 2 picks up those words. Sentence 4 explains why: we can’t see the algorithm, so we can’t judge its impartiality."))) +
 final("1324"),
 "pj",
 [("1", "Sets up the two ideals."), ("3", "Twitter’s own description."), ("2", "“It” and the words “…and much more”."), ("4", "Why that is a problem.")],
 why_title="Why each sentence goes where it does")

P.va(29, P.summary_html(29, "Production and legitimation"), P.Q["VARC"][29]["opts"], "MCQ", "4", "Summary", "Hard",
 "The passage describes the professions-approach and then its limitation.",
 steps(("What the passage says", "<ol><li>The professions-approach looks at how a body of knowledge is institutionalised.</li><li>It restricts knowledge production to a select few and treats power as exclusion.</li></ol>"),
       ("Choosing", p("Option 4 has both the aim and the restriction."))) +
 final("Option 4"),
 "summary",
 [("1", "Leaves out the restriction."), ("2", "Only the first sentence."), ("3", "Overstates how much it is relied on.")])
