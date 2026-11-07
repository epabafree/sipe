# -*- coding: utf-8 -*-
# Batch 6 — CAT 2022 Slot 2: VARC (Q1–24, exam order). DILR and QA: b6_22s2_dilr.py, b6_22s2_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2022, 2, "ex6_22s2.json")
# Bracketed note on chromatophores, which three of the questions refer to.
_p4 = P.P["P4"].split("\n\n")
_p4.insert(2, "[Note: chromatophores are organs in the skin holding elastic sacs of pigment, red, yellow or brown. Each sac is ringed by radial muscles connected to the brain by a nerve. When a signal arrives, the muscles contract, the sac is pulled open and its colour shows. These are the colours that light reflects at the depths where cephalopods live.]")
P.P["P4"] = "\n\n".join(_p4)

P.passage("P1", "Passage 1 — Humans as musicking creatures", "Arts_and_Literature")
P.passage("P2", "Passage 2 — Institutions in the social sciences", "Philosophy_and_Psychology")
P.passage("P3", "Passage 3 — Social justice in engineering education", "Science_and_Technology")
P.passage("P4", "Passage 4 — How octopuses camouflage", "Environment_and_Life_Science")

# ---------------- Passage 1 ----------------
P.rc(1, "P1", "Main_Idea", "1", "Medium",
 "Keywords should cover what the passage keeps coming back to: humans, musicking, its links with language and symbols, and modern humanity.",
 steps(("What the passage is about", p("The author argues that humans are musicking creatures, that the capacities behind musicking mark modern humanity, and that these capacities overlap with language and symbol-making. It ends with how musicking emerged over a long period.")),
       ("Choosing", p("Option 1 names all of these. The other sets include passing details (Cassirer, “antique”, psychological vantage) or terms too general to be useful (capacities, symbols)."))) +
 final("Option 1"),
 "inference",
 [("2", "Cassirer and “psychological vantage” are mentioned only once each."), ("3", "“Antique” describes a word the author uses; it isn’t a theme."), ("4", "Too general: it leaves out musicking, the passage’s central idea.")])

P.rc(2, "P1", "Inference", "1", "Easy",
 "Look at the last paragraph, where the author looks back 20,000 years.",
 steps(("The relevant line", ev(5, "If we look back 20,000 years, a small portion of this long period, we reach the lives of humans whose musical capacities were probably little different from our own.")),
       ("Choosing", p("Option 1 restates this directly. The others either contradict the passage or go further than it does."))) +
 final("Option 1"),
 "detail",
 [("2", "The passage says musicking is neither language-like nor symbol-like, but it doesn’t make the “form of expression” point this option relies on."),
  ("3", "Most capacities overlap with nonmusical ones, but “all musical work” lies in the overlap is far stronger than the passage."),
  ("4", "The first paragraph does say something like this, but it is about who counts as musical, not about how music emerged.")])

P.rc(3, "P1", "Inference", "3", "Easy",
 "The author lists several qualifications, then says they are “moot” in the face of an overarching truth.",
 steps(("Reading the opening", ev(1, "These qualifications, whatever their local merit, are moot in the face of the overarching truth that making music … is the province of all those who perceive and experience what is made.") +
          p("The author admits there are caveats but holds that the plain statement, “humans today make music”, is still true.")),
       ("Choosing", p("Option 3 says exactly this."))) +
 final("Option 3"),
 "inference",
 [("1", "The author doesn’t say the statement needs no qualifications; he lists several."), ("2", "Musical expression isn’t the point here."), ("4", "This defines a bald statement wrongly; a bald statement is a plain one, made without qualifications.")])

P.rc(4, "P1", "Weaken", "1", "Hard",
 "The author’s claim is that musicking is a shared trait of modern humans, rooted in capacities that are partly innate. Which option undercuts that?",
 steps(("The claim", p("Humans are musicking creatures: the capacities for music arise from innate dispositions and are a principal marker of modern humanity.")),
       ("What weakens it", p("If musical capacities were mainly socio-cultural, music would be something particular societies developed, not a shared human trait. That works against the claim. The other options either have no bearing on it or are consistent with it."))) +
 final("Option 1"),
 "weaken",
 [("2", "Musicking can be a shared human trait even if other capacities matter more for survival."), ("3", "Unconscious dispositions are still innate, which fits the author’s view."),
  ("4", "This agrees with the passage’s point about musicking’s ancient emergence.")])

# ---------------- Passage 2 ----------------
P.rc(5, "P2", "Detail_Not_True", "2", "Medium",
 "Three of the options are false according to the passage. Find the one that matches what it says about natural languages.",
 steps(("The line on natural languages", ev(2, "Natural languages are typical examples of what Ferguson called ‘the result of human action, but not the execution of any human design’") +
          p("So natural language develops without conscious design, which is what option 2 says.")),
       ("Why the others are false", p("Culture and tradition are “sub-sets of institutions analytically isolated for explanatory or expository purposes”, so they do have explanatory power. Family and governance are now “very much the product of conscious attempts to mold and plan them”. And the passage says mixtures of formal and informal institutions are the norm."))) +
 final("Option 2"),
 "notrue",
 [("1", "The passage treats culture and tradition as useful for explanation and exposition."), ("3", "These institutions are now consciously shaped by law and planning."), ("4", "The passage stresses that formal and informal institutions are intertwined.")])

P.rc(6, "P2", "Detail", "1", "Medium",
 "Read the first two sentences together. What is being characterised, and in what two ways?",
 steps(("The opening", ev(1, "We begin with the emergence of the philosophy of the social sciences as an arena of thought and as a set of social institutions. The two characterisations overlap but are not congruent.") +
          p("The philosophy of the social sciences is described in two ways: as an arena of thought and as a set of social institutions.")),
       ("Choosing", p("Of the options, only option 1 pairs the philosophy of the social sciences with “a set of social institutions”, the terms the sentence actually uses."))) +
 final("Option 1"),
 "detail",
 [("2", "Academic disciplines come up in the next sentence, as an example of social institutions."), ("3", "These are related terms, but they aren’t the two characterisations."), ("4", "Individuals and social structures appear in the author’s definition of an institution.")])

P.rc(7, "P2", "Inference", "3", "Easy",
 "Why does the author bring up the stock exchange and the black market? Look at the sentence just before.",
 steps(("Context", ev(1, "There are some institutions that come in both informal and formal variants, as well as in mixed ones.") +
          p("The two markets illustrate this: in the same domain, one institution is formal and the other informal.")),
       ("Choosing", p("Option 3 states this."))) +
 final("Option 3"),
 "purpose",
 [("1", "The point is about institutions, not about trading instruments."), ("2", "Rules aren’t the contrast being drawn."), ("4", "Dependence on the market isn’t discussed.")])

P.rc(8, "P2", "Main_Idea", "4", "Medium",
 "After surveying different views, the author settles on a general definition. Which option is it?",
 steps(("The author’s own view", ev(2, "Let us straddle all these versions and present institutions very generally . . . as structures that serve to coordinate the actions of individuals.") +
          p("The rest of the passage, including the section on language, builds on this definition.")),
       ("Choosing", p("Option 4 captures the central idea. The others are details or views the author departs from."))) +
 final("Option 4"),
 "inference",
 [("1", "An example from the first paragraph."), ("2", "This is the usual view, which the author explicitly departs from."), ("3", "The passage calls language the formative institution, not specifically a formal one, and it is still a detail.")])

# ---------------- Passage 3 ----------------
P.rc(9, "P3", "Except", "2", "Easy",
 "What does the author think of technical-social dualism?",
 steps(("The author’s view", ev(1, "This is known as technical-social dualism; the idea that the technical and social dimensions of engineering problems are readily separable") +
          p("The author criticises this approach throughout. Moving towards it is the opposite of what he wants, even if the option adds a positive-sounding description.")),
       ("The others", p("Sustainability, community-based design and responsible problem-solving all match the reforms described in the last two paragraphs."))) +
 final("Option 2"),
 "except",
 [("1", "The author worries about medical waste and emissions, so he would want sustainability built in."), ("3", "This is what the Berkeley course teaches: place-based knowledge in collaboration with communities."),
  ("4", "The author criticises the focus on cost, speed and scale.")])

P.rc(10, "P3", "Except", "3", "Medium",
 "Check how the passage describes the problem with drug dosing for people assigned female at birth.",
 steps(("The dosing problem", ev(3, "Most FDA-approved drugs are incorrectly dosed for people assigned female at birth, leading to unexpected adverse reactions. This is because they have been inadequately represented in clinical trials.") +
          p("The problem is dosing, caused by under-representation in trials. Nothing in the passage says people were incorrectly assigned female at birth.")),
       ("The others", p("Neglected diseases such as endometriosis, under-representation in trials, and spirometers still calibrated on racial assumptions are all given as negative outcomes."))) +
 final("Option 3"),
 "except",
 [("1", "The passage gives endometriosis as an example."), ("2", "This matches the clinical-trials point."), ("4", "This matches the spirometer example.")])

P.rc(11, "P3", "Except", "1", "Medium",
 "Three quotations explain why marginalised people lose out. One is about something else.",
 steps(("The odd one", p("The quotation about devices not being built sustainably is about medical waste and greenhouse gas emissions. It is a separate problem, not a reason why marginalised people are discriminated against.")),
       ("The others", p("Racial correction factors, subjective beliefs treated as facts, and technical ideals shaped by a privileged culture all explain how inequity gets built in."))) +
 final("Option 1"),
 "except",
 [("2", "The eugenics-based adjustments are a direct example of discrimination built into devices."), ("3", "This is the author’s general point about how inequities get encoded."), ("4", "Technical ideals that serve the privileged explain who gets left out.")])

P.rc(12, "P3", "Main_Idea", "3", "Easy",
 "The first paragraph describes how engineering is taught now. What does the author say students are trained to do?",
 steps(("The claim", ev(1, "This way of teaching primes students to believe that their decision-making is purely objective, as it is grounded in math and science.") +
          p("Students are taught to aim for technical ideals and treat social dimensions as separate. That is option 3.")),
       ("Why not the others", p("Option 2 gets technical-social dualism backwards, and options 1 and 4 add claims the passage doesn’t make."))) +
 final("Option 3"),
 "inference",
 [("1", "The passage doesn’t talk about a shift from humanism to technological perfection."), ("2", "Technical-social dualism separates social concerns from technical ones; it doesn’t incorporate them."),
  ("4", "The passage doesn’t say this approach produces much-needed universal solutions.")])

# ---------------- Passage 4 ----------------
P.rc(13, "P4", "Except", "3", "Easy",
 "Misfits means unlike their relatives. Which option is not about how octopuses differ from other molluscs?",
 steps(("How they differ", p("Unlike other molluscs, cephalopods have no shell, are “all arms”, and some have large brains. Each of these sets them apart.")),
       ("The odd one", p("Being eaten by humans and other animals is given as the reason they need protection, not as something that makes them different from their relatives."))) +
 final("Option 3"),
 "except",
 [("1", "Large brains for an invertebrate set them apart."), ("2", "Other molluscs are mostly shelled."), ("4", "Cephalopods are “all arms”, unlike their relatives.")])

P.rc(14, "P4", "Detail_Not_True", "3", "Easy",
 "The passage describes cephalopods matching textures and the colours around them. Does it ever mention predators’ colours?",
 steps(("What the passage describes", p("Papillae change texture, chromatophores and iridophores change colour, and leucophores let them take on the colour of the water around them.")),
       ("The odd one", p("Nothing in the passage says they take on the colour of a predator."))) +
 final("Option 3"),
 "notrue",
 [("1", "Papillae change the texture of the skin."), ("2", "Chromatophores and iridophores change colour."), ("4", "Leucophores let them appear blue or green with the water.")])

P.rc(15, "P4", "Weaken", "1", "Medium",
 "Three options interfere with a step in how camouflage works: the nerve signal, the muscles, or the colours available. One doesn’t affect any step.",
 steps(("How chromatophores work", p("A nerve signal makes the radial muscles contract and open the pigment sac. The pigments are red, yellow and brown, the colours light reflects at those depths.")),
       ("Testing the options", p("Blocking nerve signals or muscle movement would stop the sacs opening. Light reflecting green instead of brown would make the pigments mismatch the surroundings. But the number of chromatophores compared with other cell types isn’t tied to anything in the passage, so it wouldn’t weaken the camouflage."))) +
 final("Option 1"),
 "weaken",
 [("2", "Chromatophores depend on nerve signals from the brain."), ("3", "Radial muscles have to contract to open the sacs."), ("4", "The pigments only match the surroundings if light reflects red, yellow and brown.")])

P.rc(16, "P4", "Inference", "4", "Easy",
 "Which of these does the passage link to octopus camouflage, and which is mentioned only as a relative?",
 steps(("Comparisons in the passage", p("Squid and cuttlefish use papillae and leucophores in the same way as octopuses. A polar bear’s fur is compared with leucophores, which scatter light to look white.")),
       ("The odd one", p("Sea snails appear only as shelled relatives, with no link to camouflage at all, so they are the least similar."))) +
 final("Option 4"),
 "inference",
 [("1", "Cuttlefish use leucophores and papillae too."), ("2", "Squid imitate coral reefs with papillae."), ("3", "Leucophores work like a polar bear’s white fur.")])

# ---------------- Verbal ability ----------------
P.va(17, P.sent_html(17), [], "TITA", "3142", "Para_Jumble", "Medium",
 "One sentence states the idea; the others trace the word “cheer” through history.",
 steps(("The opener", p("Sentence 3 states the idea: taking on a cheerful expression changes the self.")),
       ("The history", p("Sentence 1 links this to the word “cheer”, from Old French for “face”. Sentence 4 shows the medieval use, where cheer is still an expression and a body part. Sentence 2 shows the later, more abstract “cheerfulness” that came with Bible translations."))) +
 final("3142"),
 "pj",
 [("3", "States the idea."), ("1", "Introduces the word’s origin."), ("4", "The medieval meaning."), ("2", "The later, abstract meaning.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.summary_html(18, "Today, many of the debates"), P.Q["VARC"][18]["opts"], "MCQ", "2", "Summary", "Medium",
 "The passage is about a debate that has come back: old fears about control now attached to big data.",
 steps(("What the passage says", "<ol><li>Debates about control in the age of big data echo Cold War fears.</li><li>Personal data exposes us to influence rather than freeing us.</li><li>This has renewed calls for solitude and disconnection.</li></ol>"),
       ("Choosing", p("Option 2 captures the renewed debate about freedom and privacy in the age of big data."))) +
 final("Option 2"),
 "summary",
 [("1", "The Cold War comparison is background, not the main point."), ("3", "The passage talks about algorithms and big data; “artificial intelligence” shifts the focus."), ("4", "“Enslaving” is much stronger than the passage.")])

P.va(19, P.summary_html(19, "There’s a common idea"), P.Q["VARC"][19]["opts"], "MCQ", "2", "Summary", "Easy",
 "The passage corrects a common belief about artworks. What is the correction?",
 steps(("What the passage says", "<ol><li>Artworks are often thought of as timeless.</li><li>In fact many decay, through “inherent vice”.</li><li>Hirst’s shark is an example of a work that began to decompose.</li></ol>"),
       ("Choosing", p("Option 2 keeps the main point: artworks deteriorate, and the task is to slow that down."))) +
 final("Option 2"),
 "summary",
 [("1", "It still calls the works “timeless”, which is the belief the passage questions."), ("3", "The passage doesn’t discuss museums’ changing role."), ("4", "Moral responsibility and artists’ lifespans aren’t in the passage.")])

P.va(20, P.sent_html(20), [], "TITA", "2143", "Para_Jumble", "Medium",
 "Start with the sentence that sets out the general debate. One sentence begins “This would require”; what does “this” refer to?",
 steps(("The opener", p("Sentence 2 introduces the debate: it focuses on emissions, but ecosystem collapse has many causes.")),
       ("Building the argument", p("Sentence 1 explains why no single technical fix will do. Sentence 4 concludes that political solutions are needed, such as stable-state economies.")),
       ("The close", p("Sentence 3, “This would require legislation…”, describes what that political path would need, so it comes last."))) +
 final("2143"),
 "pj",
 [("2", "Introduces the debate."), ("1", "Many causes, no single tech fix."), ("4", "So political solutions are needed."), ("3", "What those solutions would require.")],
 why_title="Why each sentence goes where it does")

P.va(21, P.summary_html(21, "Several of the world’s earliest"), P.Q["VARC"][21]["opts"], "MCQ", "2", "Summary", "Medium",
 "Notice the passage’s wording: “several” of the earliest cities, and “some regions”. A good summary keeps that scope.",
 steps(("What the passage says", "<ol><li>Several early cities were organised along egalitarian lines.</li><li>City life doesn’t necessarily imply a particular political form.</li><li>This evidence opens up egalitarian possibilities.</li></ol>"),
       ("Choosing", p("Option 2 says we now have evidence that some ancient cities were far less hierarchical, which keeps both the claim and its scope."))) +
 final("Option 2"),
 "summary",
 [("1", "The passage doesn’t trace a transformation into today’s hierarchies."), ("3", "The absence of temples and palaces is evidence the passage uses, not its main point."),
  ("4", "“Ancient cities were not organised in this way” is too broad; the passage says only some were egalitarian.")])

P.va(22, P.sent_html(22), [], "TITA", "2431", "Para_Jumble", "Medium",
 "The general idea of food as individual choice comes first. Then follow how the paragraph narrows down.",
 steps(("The opener", p("Sentence 2 introduces the framing of food as individual choice.")),
       ("Narrowing down", p("Sentence 4 says this framing appeals to a desire for agency but hides structural obstacles. Sentence 3 adds that this is especially so in a neoliberal context. Sentence 1 gives the specific case of women and cooking."))) +
 final("2431"),
 "pj",
 [("2", "Introduces the framing."), ("4", "Its appeal and its blind spot."), ("3", "“Particularly so” in a neoliberal context."), ("1", "The specific case of women.")],
 why_title="Why each sentence goes where it does")

MS23 = ('<p>There is a sentence that is missing in the paragraph given below. Look at the paragraph and decide in which blank (option 1, 2, 3, or 4) the following sentence would best fit.</p>'
        '<p class="quote"><b>Sentence:</b> This was years in the making but fast-tracked during the pandemic, when “people started being more mindful about their food,” he explained.</p>'
        '<p class="quote"><b>Paragraph:</b> For millennia, ghee has been a venerated staple of the subcontinental diet, but it fell out of favour a few decades ago when saturated fats were largely considered to be unhealthy. ___(1)___ But more recently, as the thinking around saturated fats is shifting globally, Indians are finding their own way back to this ingredient that is so integral to their cuisine. ___(2)___ For Karmakar, a renewed interest in ghee is emblematic of a return-to-basics movement in India. ___(3)___ This movement is also part of an overall trend towards “slow food”. In keeping with the movement’s philosophy, ghee can be produced locally (even at home) and has inextricable cultural ties. ___(4)___ At a basic level, ghee is a type of clarified butter believed to have originated in India as a way to preserve butter from going rancid in the hot climate.</p>')
P.va(23, MS23, ["Option 1", "Option 2", "Option 3", "Option 4"], "MCQ", "3", "Missing_Sentence", "Medium",
 "“This was years in the making” needs something that was building up, and “he explained” needs a man to have been named.",
 steps(("What the sentence needs", p("A person (“he”) and a development that took years (“this”).")),
       ("Finding the spot", p("Karmakar is introduced just before blank (3), with the return-to-basics movement. The sentence explains that this movement had been building for years and sped up during the pandemic. The next sentence, “This movement is also part of…”, continues naturally.")),
       ("The other blanks", p("At (1) and (2) no one has been named yet, and at (4) the paragraph has moved on to what ghee is."))) +
 final("Option 3"),
 "missing",
 [("1", "No speaker has been introduced yet, so “he explained” has no one to refer to."), ("2", "Karmakar is introduced only after this blank."), ("4", "The paragraph has moved on to defining ghee.")])

MS24 = ('<p>There is a sentence that is missing in the paragraph given below. Look at the paragraph and decide in which blank (option 1, 2, 3, or 4) the following sentence would best fit.</p>'
        '<p class="quote"><b>Sentence:</b> Most were first-time users of a tablet and a digital app.</p>'
        '<p class="quote"><b>Paragraph:</b> Aage Badhein’s USP lies in the ethnographic research that constituted the foundation of its development process. Customisations based on learning directly from potential users were critical to making this self-paced app suitable for both a literate and non-literate audience. ___(1)___ The user interface caters to a Hindi-speaking audience who have minimal to no experience with digital services and devices. ___(2)___ The content and functionality of the app are suitable for a wide audience. This includes youth preparing for an independent role in life or a student ready to create a strong foundation of financial management early in her life. ___(3)___ Household members desirous of improving their family’s financial strength to reach their aspirations can also benefit. We piloted Aage Badhein in early 2021 with over 400 women from rural areas. ___(4)___ The digital solution generated a large amount of interest in the communities.</p>')
P.va(24, MS24, ["Option 1", "Option 2", "Option 3", "Option 4"], "MCQ", "4", "Missing_Sentence", "Easy",
 "“Most were first-time users” needs a group of people mentioned just before it.",
 steps(("What “most” refers to", p("The sentence describes a group of people, most of whom had never used a tablet or an app.")),
       ("Finding the spot", p("The 400 rural women in the pilot are mentioned just before blank (4). The sentence describes them, and the next one, about the interest the app generated, follows on."))) +
 final("Option 4"),
 "missing",
 [("1", "No group of users has been mentioned yet."), ("2", "This part describes the interface, not actual users."), ("3", "This is a list of possible audiences, not people who used the app.")])
