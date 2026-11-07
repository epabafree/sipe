# -*- coding: utf-8 -*-
# Batch 13 — CAT 2020 Slot 3: VARC (20 of 26; Q1–4, Q6 and Q7 aren't in the source). DILR and QA: b13_20s3_dilr.py, b13_20s3_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2020, 3, "ex13_20s3.json")
P.passage("P1", "Passage 1 — Explaining the economic crisis", "Economics_and_Management")
P.passage("P2", "Passage 2 — Travel writing and identity", "Arts_and_Literature")
P.passage("P3", "Passage 3 — Bregman on human nature", "Philosophy_and_Psychology")

# ---------------- Passage 2: Travel writing ----------------
P.rc(14, "P2", "Except", "1", "Medium",
 "Look at what the last paragraph says shaped feminist scholars’ readings. Which option is about society rather than the scholars’ own lens?",
 steps(("What shapes their reading", p("The paragraph describes scholars working from a ‘liberal’ feminist perspective, then a poststructural one (option 3), studying how gendered identities were negotiated at home and away (options 2 and 4).")),
       ("The odd one", p("Class comes up only as one of the ties the women worked through. The passage never says scholars brought a knowledge of class tensions to their study."))) +
 final("Option 1"),
 "except",
 [("2", "¶3: identities negotiated differently “at home” and “away”."), ("3", "¶3: the liberal and poststructural perspectives."), ("4", "¶3: the masculinist history and gendered identities.")])

P.rc(15, "P2", "Detail", "4", "Easy",
 "Read the sentence about the road narrative.",
 steps(("The line", ev(1, "emphasizing the independence of road travel and the value of rural folk traditions") +
          p("Independence of road travel is the freedom travel gives."))) +
 final("Option 4"),
 "detail",
 [("1", "The protagonists discover themselves; the passage doesn’t say the genre developed their desire for independence."), ("2", "It values folk traditions; it doesn’t say travellers joined in."), ("3", "They discover themselves, not that they are different from others.")])

P.rc(16, "P2", "Inference", "2", "Medium",
 "Find the sentence about ‘self-development through travel’.",
 steps(("The line", ev(3, "women’s gendered identities were negotiated differently “at home” than they were “away”, thereby showing women’s self-development through travel") +
          p("Away from home, their identity was negotiated differently: it was redefined."))) +
 final("Option 2"),
 "inference",
 [("1", "Their class is mentioned, but it isn’t the reason given."), ("3", "Diverse identities belong to the later, poststructural studies."), ("4", "The perspective is the scholars’, not the women’s.")])

P.rc(17, "P2", "Detail", "2", "Easy",
 "Read the last sentence of the second paragraph.",
 steps(("The line", ev(2, "Said’s work became a model for demonstrating cultural forms of imperialism in travel texts, showing how the political, economic, or administrative fact of dominance relies on legitimating discourses") +
          p("Cultural imperialism legitimised colonial domination."))) +
 final("Option 2"),
 "detail",
 [("1", "It is about representation and the self, not representation versus fact."), ("3", "No comparison of significance is made."), ("4", "Too sweeping; the passage describes the representations, not the westerners.")])

P.rc(18, "P2", "Inference", "2", "Medium",
 "What does travel writing show, again and again, in each paragraph?",
 steps(("The common thread", p("Travel changes ‘identities’, travellers ‘discover themselves’, and women narrate their sense of themselves in new places. Travel writing is the writer’s account of their own experience and self.")),
       ("Choosing", p("That is closest to autobiography."))) +
 final("Option 2"),
 "inference",
 [("1", "Travel writing records real journeys, not fiction."), ("3", "Feminist scholars study it; it isn’t feminist writing itself."), ("4", "It connects to politics, but isn’t journalism.")])

# ---------------- Passage 3: Bregman ----------------
P.rc(19, "P3", "Except", "2", "Medium",
 "Three options misread the passage. Look at the opening lines.",
 steps(("The true one", ev(1, "human nature is something on which most people seem to agree. By and large, according to Rutger Bregman … we have a rather pessimistic view") +
          p("Most people share the Hobbesian, pessimistic view of others."))) +
 final("Option 2"),
 "except",
 [("1", "Only Hobbes believed in a strong state; Rousseau saw it as chains."), ("3", "Bregman sides with Rousseau."), ("4", "Veneer theory is mentioned, but the author doesn’t say he believes it.")])

P.rc(20, "P3", "Detail", "3", "Medium",
 "How do ‘modern scholars’, as Bregman reports them, see the collapses?",
 steps(("The line", ev(4, "modern scholars, he claims, see them more as a reprieve, in which the enslaved gain their freedom and culture flourishes") +
          p("A time when society and culture change, for the better."))) +
 final("Option 3"),
 "detail",
 [("1", "That is the traditional view, which Bregman rejects."), ("2", "Social action isn’t mentioned."), ("4", "The fear of collapse comes from veneer theory, which he calls unfounded.")])

P.rc(21, "P3", "Purpose", "1", "Medium",
 "What is Bregman’s whole book arguing?",
 steps(("The contrast", p("Before agriculture, people lived in harmony; after it, came property, war, greed and injustice.")),
       ("Its purpose", p("It supports his claim that people are decent at heart and that ‘progress’ made them selfish."))) +
 final("Option 1"),
 "purpose",
 [("2", "He doesn’t advocate going back."), ("3", "Environmental lifestyles aren’t the point."), ("4", "Population growth is the author’s objection, not Bregman’s point.")])

P.rc(22, "P3", "Inference", "4", "Hard",
 "Where does the author say ‘the truth is probably somewhere between’?",
 steps(("Where the author differs", p("Bregman paints civilisation as property, war and injustice, and the time before as an idyll. The author says life grows complex with large settlements, and that humanity encompasses both natures.") +
          ev(5, "it seems equally misleading to offer the false choice of Rousseau and Hobbes")),
       ("Choosing", p("So the author doesn’t share Bregman’s picture of civilised society as coercive and unjust."))) +
 final("Option 4"),
 "inference",
 [("1", "The author accepts this works for 30 or 40 hunter-gatherers."), ("2", "Knowledge grows with settlements, but that isn’t presented as a disagreement about agriculture."), ("3", "“This may be true”: the author accepts it.")])

# ---------------- Passage 1: The economic crisis ----------------
P.rc(9, "P1", "Inference", "4", "Easy",
 "‘For more than two years now’.",
 steps(("The sentence", ev(1, "I’ve been following the economic crisis for more than two years now") +
          p("The author’s interest is at least two years old."))) +
 final("Option 4"),
 "inference",
 [("1", "Travel isn’t mentioned."), ("2", "Nothing about the crisis ending."), ("3", "Reads ‘following’ literally.")])

P.rc(10, "P1", "Main_Idea", "2", "Medium",
 "‘We’re all in this together’ answers decades of individualism.",
 steps(("The paragraph", ev(2, "after decades in which the ideology of the Western world was personally and economically individualistic … we’re all in this together") +
          p("The crisis needs a collective response, not an individualistic one."))) +
 final("Option 2"),
 "inference",
 [("1", "No other ideologies are predicted."), ("3", "A phrase from the paragraph, not its argument."), ("4", "The opposite of the point.")])

P.rc(11, "P1", "Application", "3", "Medium",
 "What gap does the author want to narrow?",
 steps(("The line", ev(1, "there is a much bigger gap between the world of finance and that of the general public and that there is a need to narrow that gap") +
          p("Teaching financial literacy to everyone narrows it."))) +
 final("Option 3"),
 "detail",
 [("1", "Not suggested."), ("2", "Policy design isn’t the author’s interest."), ("4", "Research helps insiders; the gap is with the public.")])

P.rc(12, "P1", "Except", "3", "Hard",
 "The author ties the crisis to the failure of individualism. Which option separates the two?",
 steps(("The argument", p("The crisis shows that individualist ideology doesn’t hold: ‘we’re all in this together’.")),
       ("The odd one", p("Option 3 says a failed system doesn’t mean a failed ideology. That cuts against the author."))) +
 final("Option 3"),
 "except",
 [("1", "Mathematics, economics and psychology are all part of the story."), ("2", "Finance is a priesthood with its own mysteries."), ("4", "Moving away from individualism is what the author suggests.")])

P.rc(13, "P1", "Weaken", "1", "Hard",
 "Negate each option. Which negation sounds like the author?",
 steps(("Negating option 1", p("‘The crisis was a failure of collective action.’ That fits the slow response of the world’s governments and the author’s ‘we’re all in this together’.")),
       ("The others", p("Negating 2 says the science–arts gap hasn’t narrowed, which the author doubts. Negating 3 says most people understand finance, which contradicts him. Negating 4 contradicts his two years."))) +
 final("Option 1"),
 "weaken",
 [("2", "Its negation goes against the author."), ("3", "Its negation goes against the author."), ("4", "Its negation goes against the passage.")])

# ---------------- Verbal ability ----------------
P.va(5, P.sent_html(5), [], "TITA", "2431", "Para_Jumble", "Hard",
 "Sentence 2 defines exaptation. Sentence 4 says two concepts can be applied to the CNS. What follows naturally from that?",
 steps(("The opener", p("Sentence 2 explains exaptation with examples from bats and feathers.")),
       ("The sequence", p("Sentence 4 says exaptation and the Russian-doll organisation can be applied to the CNS. Sentence 3 explains the Russian-doll structure, and sentence 1 shows the CNS organised in the same ‘nested’ way.")),
       ("A note", p("2341 also reads smoothly, and some answer keys give it. The official answer is 2431."))) +
 final("2431"),
 "pj",
 [("2", "Defines exaptation."), ("4", "Both concepts can apply to the CNS."), ("3", "The Russian-doll structure."), ("1", "The CNS is nested in the same way.")],
 why_title="Why each sentence goes where it does")

P.va(26, P.sent_html(26), [], "TITA", "4123", "Para_Jumble", "Medium",
 "Sentence 1 begins with ‘It’. What does ‘It’ refer to?",
 steps(("The opener", p("Sentence 4 introduces the Chicago school and its consumer welfare standard.")),
       ("The sequence", p("Sentence 1: ‘It’ advocated a conservative approach. Sentence 2: so industries gained market share without official concern. Sentence 3: the new risks posed by tech giants now need new legal solutions."))) +
 final("4123"),
 "pj",
 [("4", "The Chicago school’s standard."), ("1", "“It” advocated restraint."), ("2", "The result: giants grew unchecked."), ("3", "Why new solutions are needed now.")],
 why_title="Why each sentence goes where it does")

P.va(23, P.sent_html(23), [], "TITA", "3", "Odd_One_Out", "Medium",
 "Sentence 5 begins ‘For instance’. Which sentence is it an example of?",
 steps(("The chain", p("2 → 4 → 1 → 5: hate speech detection (2) uses algorithms (4), which pick up biases from their training data (1), for instance with group identifiers (5).")),
       ("The odd one", p("Sentence 3 is about missing context, a different problem from biased training data."))) +
 final("3"),
 "oddone",
 [("2", "The topic."), ("4", "“It” uses algorithms."), ("1", "They learn biases."), ("5", "An example of the bias.")],
 why_title="How the other sentences fit")

P.va(8, P.summary_html(8, "The dominant hypotheses in modern science"), P.Q["VARC"][8]["opts"], "MCQ", "2", "Summary", "Medium",
 "The passage sets out two views side by side. It doesn’t say one replaced the other.",
 steps(("What the passage says", "<ol><li>Most think language evolved to share facts.</li><li>Another view: it evolved for social bonding, which helped survival.</li></ol>"),
       ("Choosing", p("Option 2 keeps both views, and the link to survival."))) +
 final("Option 2"),
 "summary",
 [("1", "Continuous evolution to higher forms isn’t in the passage."), ("3", "Experts ‘challenging’ goes too far."), ("4", "Says scholars have moved on; the passage gives an alternative view only.")])

P.va(24, P.summary_html(24, "Aesthetic political representation"), P.Q["VARC"][24]["opts"], "MCQ", "3", "Summary", "Hard",
 "Autonomy for the representative comes from disinterestedness, which is not indifference.",
 steps(("What the passage says", "<ol><li>The representative has autonomy, but not to abandon responsibility.</li><li>That autonomy rests on disinterestedness, which is different from indifference.</li></ol>"),
       ("Choosing", p("Option 3 says autonomy draws from disinterestedness. Option 4 says it is ‘manifested through’ it, which gets the relation backwards."))) +
 final("Option 3"),
 "summary",
 [("1", "Leaves out autonomy."), ("2", "Adds ‘non-subjective evaluation’."), ("4", "Autonomy draws on disinterestedness; it isn’t manifested through it.")])

P.va(25, P.summary_html(25, "Brown et al."), P.Q["VARC"][25]["opts"], "MCQ", "1", "Summary", "Medium",
 "The passage uses genetic theory as a model for what metabolic theory might do.",
 steps(("What the passage says", "<ol><li>Metabolic theory may do for ecology what genetic theory did for evolutionary biology.</li><li>Genetic theory’s success lies in its wide range of models and applications.</li></ol>"),
       ("Choosing", p("Option 1 keeps both parts and the ‘may’."))) +
 final("Option 1"),
 "summary",
 [("2", "‘Must’ is too strong."), ("3", "Leaves out metabolic theory."), ("4", "The opposite of the suggestion.")])
