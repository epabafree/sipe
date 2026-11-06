# -*- coding: utf-8 -*-
# Batch 7 — CAT 2022 Slot 3: VARC (Q1–24). DILR and QA: b7_22s3_dilr.py, b7_22s3_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2022, 3, "ex7_22s3.json")
P.passage("P1", "Passage 1 — The Chicago School on crime and migration", "Social_Science_and_History")
P.passage("P2", "Passage 2 — Bios and Technos", "Science_and_Technology")
P.passage("P3", "Passage 3 — Orientalism and the Indian past", "Social_Science_and_History")
P.passage("P4", "Passage 4 — What helpful software does to skill", "Science_and_Technology")

# ---------------- Verbal ability (Q1) ----------------
P.va(1, P.sent_html(1), [], "TITA", "4312", "Para_Jumble", "Easy",
 "One sentence explains what beacons are. Start there.",
 steps(("The opener", p("Sentence 4 defines beacons: small devices that send signals to nearby Bluetooth devices.")),
       ("How they work, then where", p("Sentence 3 explains how phones pick up the signals and estimate distance. Sentence 1 lists the industries using them, and sentence 2 gives the retail example in detail."))) +
 final("4312"),
 "pj",
 [("4", "Defines beacons."), ("3", "How the signal is picked up."), ("1", "Industries that use them."), ("2", "A retail example.")],
 why_title="Why each sentence goes where it does")

# ---------------- Passage 1 ----------------
P.rc(2, "P1", "Main_Idea", "2", "Easy",
 "The passage keeps returning to one cause of rising crime. What is it?",
 steps(("The central claim", ev(1, "Sociologists working in the Chicago School tradition have focused on how rapid or dramatic social change causes increases in crime.") +
          ev(4, "The combination of rapid population growth with the diversity of those moving into the cities created what the Chicago School sociologists called social disorganisation.")),
       ("Choosing", p("Option 2 joins these: rapid growth and diversity cause social disorganisation, which feeds crime."))) +
 final("Option 2"),
 "inference",
 [("1", "The passage never recommends segregation; it names segregation as part of the problem."), ("3", "Chicago is the setting of the research, not the place where most American crime happens."), ("4", "Racial disparity is one factor, but the passage doesn’t call it the best condition for crime.")])

P.rc(3, "P1", "Detail_Not_True", "3", "Medium",
 "Check what the passage gives as the reason African American migrants were not integrated.",
 steps(("What the passage says", ev(3, "These migrants, unlike their white counterparts, were not integrated into the cities they now called home. In fact, most American cities … were characterised by high levels of racial residential segregation") +
          p("The passage points to segregation and to how different the migrants looked from the city’s residents. It never says they were less organised.")),
       ("The others", p("Options 1, 2 and 4 restate lines in the second and third paragraphs."))) +
 final("Option 3"),
 "notrue",
 [("1", "¶2: until the “new place” adapts, rapid change is a criminogenic influence."), ("2", "¶3: failure to integrate, with crowding and poverty, made crime rates climb."), ("4", "¶2: migrants’ lives were disrupted by the differences between urban and rural life.")])

P.rc(4, "P1", "Main_Idea", "4", "Easy",
 "Good keywords cover the theory, the cause, and the effect.",
 steps(("What runs through the passage", p("The Chicago School, social (dis)organisation, migration into cities, and crime.")),
       ("Choosing", p("Option 4 has all four. The others pick out supporting details or names."))) +
 final("Option 4"),
 "inference",
 [("1", "Heavy industry is a detail; it misses the theory being discussed."), ("2", "Leaves out crime, the passage’s main concern."), ("3", "A list of names, not the issues.")])

P.rc(5, "P1", "Inference", "1", "Easy",
 "The statement describes Americans moving from rural to urban areas. Which option fits that?",
 steps(("What the statement implies", p("If most Americans were rural in 1900 and urban by 1950, people must have left rural areas in large numbers.")),
       ("Choosing", p("Option 1, a strong outmigration from rural areas, agrees with it. The others place most people, or most workers, in rural areas in the mid-century."))) +
 final("Option 1"),
 "inference",
 [("2", "A 1952 census showing a rural majority would contradict the statement."), ("3", "A rural labour force always being the largest goes against an urban majority by mid-century."),
  ("4", "Needing mainly rural data for mid-century income suggests most people were still rural.")])

# ---------------- Passage 2 ----------------
P.rc(6, "P2", "Main_Idea", "1", "Medium",
 "Keywords should cover the passage’s argument: complex systems, the two logics, and their convergence.",
 steps(("The argument", p("Complex systems need bio-logic; the logic of Bios is moving into machines while the logic of Technos moves into life (bioengineering); the two are converging.")),
       ("Choosing", p("Option 1 captures all of this. The others mix in examples like carrots, milk cows or Holsteins."))) +
 final("Option 1"),
 "inference",
 [("2", "Self-repair and Holsteins are details."), ("3", "Carrots and milk cows are examples, not the main ideas."), ("4", "Mostly examples; leaves out bio-logic and convergence.")])

P.rc(7, "P2", "Inference", "1", "Easy",
 "Read the sentence that follows the quoted one.",
 steps(("The next sentence", ev(6, "The meanings of “mechanical” and “life” are both stretching until all complicated things can be perceived as machines, and all self-sustaining machines can be perceived as alive.")),
       ("Choosing", p("The two words used to point to separate things; now their meanings overlap. Option 1 says this."))) +
 final("Option 1"),
 "inference",
 [("2", "The passage says the two are converging, not that they produce mutually exclusive meanings."), ("3", "Artificial intelligence isn’t mentioned here."), ("4", "This is the opposite: the words are becoming compatible.")])

P.rc(8, "P2", "Inference", "3", "Medium",
 "Strip away the metaphor of the veil. What is the author saying about organic and manufactured things?",
 steps(("The point", p("Made things are behaving more like living things, and living things are becoming more engineered, so it is getting hard to tell the two apart. Option 3 says this in plain words.")),
       ("Why not the others", p("Options 1 and 2 reshuffle the words of the sentence without its meaning, and option 4 introduces a distinction the author doesn’t make."))) +
 final("Option 3"),
 "inference",
 [("1", "Rearranges the sentence’s words into something it doesn’t say."), ("2", "Also rearranges the words; the veil is between organic and manufactured, not apparent and manufactured."), ("4", "The author isn’t distinguishing apparent from organic reality.")])

P.rc(9, "P2", "Inference", "1", "Hard",
 "Three statements go beyond the passage. One follows from its comparison of breeders and genetic engineers.",
 steps(("The relevant lines", ev(5, "Genetic engineering is precisely what cattle breeders do when they select better strains of Holsteins, only bioengineers employ more precise and powerful control. … modern genetic engineers can use directed artificial evolution—purposeful design") +
          p("The passage uses “genetic engineers” and “bioengineers” for the same people, who direct evolution artificially.")),
       ("The others", p("Philosophers only “suspected” the laws of life could be abstracted; the passage makes no claim about purposeful design being the pinnacle of progress; and it doesn’t give complexity as the reason Bios is imported into machines."))) +
 final("Option 1"),
 "inference",
 [("2", "“Pinnacle of scientific expertise” and “civilisational progress” are not in the passage."), ("3", "Philosophers “suspected” it; they didn’t know."), ("4", "The passage doesn’t give this as the reason.")])

# ---------------- Verbal ability (Q10–12) ----------------
P.va(10, P.summary_html(10, "Tamsin Blanchard"), P.Q["VARC"][10]["opts"], "MCQ", "1", "Summary", "Medium",
 "The passage is about borrowing from other cultures without credit. Which option keeps credit, compensation and respect together?",
 steps(("What the passage says", "<ol><li>Designers increasingly lift motifs and techniques from other cultures.</li><li>Social media has accelerated this.</li><li>The original communities get no credit or compensation.</li></ol>"),
       ("Choosing", p("Option 1 keeps the central point: taking from a culture without credit, compensation or respect."))) +
 final("Option 1"),
 "summary",
 [("2", "Says media encouraged mass production, which the passage doesn’t claim."), ("3", "Narrows it to embroidery and textiles and drops credit and respect."), ("4", "Cultural collaboration isn’t the passage’s point.")])

MS11 = ('<p>There is a sentence that is missing in the paragraph given below. Look at the paragraph and decide in which blank (option 1, 2, 3, or 4) the following sentence would best fit.</p>'
        '<p class="quote"><b>Sentence:</b> When people socially learn from each other, they often learn without understanding why what they’re copying—the beliefs and behaviours and technologies and know-how—works.</p>'
        '<p class="quote"><b>Paragraph:</b> ___(1)___. The dual-inheritance theory ....says.... that inheritance is itself an evolutionary system. It has variation. What makes us a new kind of animal, and so different and successful as a species, is we rely heavily on social learning to the point where socially acquired information is effectively a second line of inheritance, the first being our genes.... ___(2)___. People tend to home in on who seems to be the smartest or most successful person around, as well as what everybody seems to be doing—the majority of people have something worth learning. ___(3)___. When you repeat this process over time, you can get, around the world, cultural packages—beliefs or behaviours or technology or other solutions—that are adapted to the local conditions. People have different psychologies, effectively. ___(4)___.</p>')
P.va(11, MS11, ["Option 1", "Option 2", "Option 3", "Option 4"], "MCQ", "2", "Missing_Sentence", "Medium",
 "The sentence describes how social learning works. Which sentence goes on to describe who people copy?",
 steps(("What the sentence does", p("It describes social learning: people copy without knowing why things work.")),
       ("Finding the spot", p("Blank (2) comes right after social learning is introduced as a second line of inheritance. The sentence then explains how that learning happens, and the next sentence describes whom people copy: the most successful, or the majority."))) +
 final("Option 2"),
 "missing",
 [("1", "The paragraph needs to introduce the theory before describing how social learning works."), ("3", "This interrupts the link between choosing whom to copy and repeating the process."), ("4", "By now the paragraph has moved on to its conclusion about different psychologies.")])

P.va(12, P.summary_html(12, "“It does seem to me"), P.Q["VARC"][12]["opts"], "MCQ", "1", "Summary", "Medium",
 "Atkinson makes two points: every joke has a victim, and nothing should be off limits.",
 steps(("What the passage says", "<ol><li>Comedy has the potential to offend; every joke has a victim.</li><li>Rules about whom you may joke about are a problem.</li><li>In a free society you should be able to joke about anything.</li></ol>"),
       ("Choosing", p("Option 1 keeps both points and the link to cancel culture."))) +
 final("Option 1"),
 "summary",
 [("2", "Atkinson doesn’t say comedians have a duty to mock everyone."), ("3", "Politicians and royalty aren’t mentioned."), ("4", "The point isn’t that jokes need to include lower classes; it is that no group should be off limits.")])

# ---------------- Passage 3 ----------------
P.rc(13, "P3", "Application", "4", "Hard",
 "How did Orientalist scholars build their picture of India? From what material, and how much of it?",
 steps(("Their method", ev(3, "There was an attempt to formulate Indian culture as uniform, such formulations being derived from texts that were given priority. The so-called ‘discovery’ of India was largely through selected literature in Sanskrit.") +
          p("They generalised about a whole culture from a narrow, selected body of texts.")),
       ("The parallel", p("Judging contemporary America from Hollywood action films does the same thing: a narrow, selected source standing in for the whole culture."))) +
 final("Option 4"),
 "inference",
 [("1", "Reading about early settlers and later migration is a broad, historical approach."), ("2", "Travellers’ accounts tell you about the travellers’ views, which is a different kind of study."), ("3", "Studying excavated artefacts is archaeology, not selective reading of texts.")])

P.rc(14, "P3", "Inference", "3", "Medium",
 "Look at the last paragraph. What does it say about the West’s technical abilities compared with India’s?",
 steps(("The relevant line", ev(5, "It was a consolation to the Indian intelligentsia for its perceived inability to counter the technical superiority of the west, a superiority viewed as having enabled Europe to colonise Asia")),
       ("Applying it", p("The passage treats the West’s technical superiority as part of why colonisation happened. The author wouldn’t say India matched the West technically."))) +
 final("Option 3"),
 "inference",
 [("1", "Wordsworth and Coleridge turned to fantasies of the Orient, so the author would agree."), ("2", "The author criticises the view that India ignored tangible aspects of life."), ("4", "The author criticises the idea of an unchanging continuity over 3,000 years.")])

P.rc(15, "P3", "Except", "4", "Medium",
 "What does the author criticise Orientalist scholars for? A better approach would avoid those mistakes.",
 steps(("The mistakes", p("Relying on selected Sanskrit texts, ignoring the worldview of their teachers, and setting up a dichotomy of spiritual India and materialistic Europe “with little attempt to juxtapose these values with the reality of Indian society”.")),
       ("The odd one", p("Developing an oppositional framework is exactly the dichotomy the author criticises. The other three would correct the mistakes."))) +
 final("Option 4"),
 "except",
 [("1", "Reading widely corrects the reliance on selected texts."), ("2", "The scholars were shaped by colonial concerns and European ideas; examining one’s own biases helps."), ("3", "The author faults them for ignoring the reality of Indian society.")])

P.rc(16, "P3", "Except", "2", "Easy",
 "Who did India’s image as spiritual console, according to the last paragraph?",
 steps(("The relevant line", ev(5, "At the height of anti-colonial nationalism it acted as a salve for having been made a colony of Britain.") +
          p("The salve was for Indians, not for the European colonisers.")),
       ("The others", p("Indian texts did shape Orientalist scholars, their work was tied to colonial concerns, and Indian opinion took up their image of India."))) +
 final("Option 2"),
 "except",
 [("1", "The scholars studied Indian texts, especially Sanskrit literature."), ("3", "¶1: interpretations were “influenced by colonial concerns and interests”."), ("4", "¶4: the theme was “endorsed by a section of Indian opinion”.")])

# ---------------- Passage 4 ----------------
P.rc(17, "P4", "Inference", "2", "Medium",
 "What do the researchers say the templates were good at, and what did that cost?",
 steps(("The researchers’ point", ev(4, "These highly constrained tools … are optimised for data capture but at the expense of sacrificing their utility for appropriate triage and diagnosis, leading users to miss the forest for the trees.") +
          p("The doctors followed the data the templates were built to capture, and lost sight of the larger picture.")),
       ("Choosing", p("Option 2 says this. Option 3 is close, but “forced” is too strong; the researchers say the templates “probably helped to induce” tunnel vision."))) +
 final("Option 2"),
 "inference",
 [("1", "The problem wasn’t the type of template but how templates are designed."), ("3", "“Forced” overstates “probably helped to induce”."), ("4", "The passage doesn’t say too little data was collected.")])

P.rc(18, "P4", "Except", "4", "Medium",
 "Three options describe harms the passage gives. Does the author ever say computers will replace people?",
 steps(("The harms described", p("Users learn less (the Utrecht study), stop thinking for themselves, and can be misled (the Ebola case).")),
       ("The odd one", p("The author doesn’t worry that computers will replace humans; he worries that they weaken people’s skills. His preferred model even keeps the human as the expert."))) +
 final("Option 4"),
 "except",
 [("1", "The opening paragraph: people become less likely to sharpen their know-how."), ("2", "The Ebola case shows software misleading doctors."), ("3", "Helpful software “short-circuited their thinking and learning”.")])

P.rc(19, "P4", "Except", "1", "Medium",
 "In human-centred automation, people lead and software assists. Which option has software acting on its own?",
 steps(("The model", ev(5, "In “human-centred automation,” the talents of people take precedence.... In this model, software plays an essential but secondary role.")),
       ("The odd one", p("Auto-complete writes for the user without being asked. The other three act only when the person asks, or offer optional feedback."))) +
 final("Option 1"),
 "except",
 [("2", "Interpretations are offered only on request."), ("3", "The system follows the resident’s instructions."), ("4", "The feedback is optional, so the doctor stays in charge.")])

P.rc(20, "P4", "Inference", "3", "Easy",
 "Which group was clicking around, and what was their software like?",
 steps(("The study", ev(2, "The people using the more advanced software, meanwhile, would often “aimlessly click around” when confronted with a tricky problem. The supposedly helpful software actually short-circuited their thinking and learning.")),
       ("Reading it", p("They had grown used to the software doing the thinking, so they clicked around hoping it would solve the problem."))) +
 final("Option 3"),
 "inference",
 [("1", "The simple-software group made fewer mistakes; avoiding mistakes isn’t why the other group clicked around."), ("2", "Both groups did the same tasks; the difference was the software."), ("4", "Nothing suggests they were reacting to the other group.")])

# ---------------- Verbal ability (Q21–24) ----------------
P.va(21, P.sent_html(21), [], "TITA", "3214", "Para_Jumble", "Medium",
 "One sentence states the idea of meritocracy; another begins “But”.",
 steps(("The opener", p("Sentence 3 introduces meritocracy as a natural principle of a free society.")),
       ("The turn", p("Sentence 2 begins “But” and presents books that stress luck. Sentence 1 develops that: if achievements are largely outside our control, so are failures. Sentence 4, “And that, in turn”, closes with the effect on humility and compassion."))) +
 final("3214"),
 "pj",
 [("3", "Introduces meritocracy."), ("2", "“But”: the case for luck."), ("1", "What accepting luck means."), ("4", "“In turn”: the result.")],
 why_title="Why each sentence goes where it does")

P.va(22, P.sent_html(22), [], "TITA", "2314", "Para_Jumble", "Medium",
 "Sentences 1 and 4 go together: one describes being made to feel guilty, the other says how that felt.",
 steps(("The opener", p("Sentence 2 introduces the mother wanting the children out in the sun.")),
       ("Background, then the effect", p("Sentence 3 gives her own outdoor childhood as the reason. Sentence 1 describes the guilt of staying indoors, and sentence 4 says how that felt to an introverted child."))) +
 final("2314"),
 "pj",
 [("2", "Introduces the mother’s wish."), ("3", "Her own childhood, the background."), ("1", "The author made to feel guilty."), ("4", "How it felt, and still feels.")],
 why_title="Why each sentence goes where it does")

P.va(23, P.summary_html(23, "To defend the sequence"), P.Q["VARC"][23]["opts"], "MCQ", "2", "Summary", "Medium",
 "The passage explains why alphabetical order took so long to catch on. Which option gives both reasons?",
 steps(("What the passage says", "<ol><li>Alphabetical order didn’t follow straight from the alphabet.</li><li>Religious tradition held medieval scholars back.</li><li>Later needs (the classics, bureaucracy) showed its usefulness.</li></ol>"),
       ("Choosing", p("Option 2 has the long delay and both causes: religious belief and a late appreciation of its usefulness."))) +
 final("Option 2"),
 "summary",
 [("1", "Leaves out why it took so long."), ("3", "“Ban” overstates scholars’ reluctance, and it leaves out the later practical needs."), ("4", "The passage doesn’t say adopting the alphabet itself was easy.")])

MS24 = ('<p>There is a sentence that is missing in the paragraph given below. Look at the paragraph and decide in which blank (option 1, 2, 3, or 4) the following sentence would best fit.</p>'
        '<p class="quote"><b>Sentence:</b> This has meant a lot of uncertainty around what a wide-scale return to office might look like in practice.</p>'
        '<p class="quote"><b>Paragraph:</b> Bringing workers back to their desks has been a rocky road for employers and employees alike. The evolution of the pandemic has meant that best laid plans have often not materialised. ___(1)___ The flow of workers back into offices has been more of a trickle than a steady stream. ___(2)___ Yet while plenty of companies are still working through their new policies, some employees across the globe are now back at their desks, whether on a full-time or hybrid basis. ___(3)___ That means we’re beginning to get some clarity on what return-to-office means - what’s working, as well as what has yet to be settled. ___(4)___</p>')
P.va(24, MS24, ["Option 1", "Option 2", "Option 3", "Option 4"], "MCQ", "2", "Missing_Sentence", "Medium",
 "The sentence talks about uncertainty. The paragraph later turns to “some clarity”, introduced by “Yet”.",
 steps(("What the sentence does", p("It sums up the slow, uneven return as uncertainty.")),
       ("Finding the spot", p("After “more of a trickle than a steady stream”, the sentence draws the consequence: uncertainty. Then “Yet …” turns to the workers who are back, which leads to “some clarity”. This is blank (2)."))) +
 final("Option 2"),
 "missing",
 [("1", "“This” would then refer to the failed plans, and the trickle sentence would follow awkwardly."), ("3", "The paragraph has already turned to people returning, so uncertainty no longer fits."), ("4", "The paragraph ends on clarity; going back to uncertainty would undo it.")])
