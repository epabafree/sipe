# -*- coding: utf-8 -*-
# Simp Mock 3: VARC (24 of 24). DILR and QA: m03_dilr.py, m03_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(3, "sm03.json")
P.passage("V1", "Passage 1 — Two early critics of representation", "Philosophy_and_Psychology")
P.passage("V2", "Passage 2 — Maps of the Baltic provinces", "Social_Science_and_History")
P.passage("V3", "Passage 3 — Why continents developed differently", "Social_Science_and_History")
P.passage("V4", "Passage 4 — The building blocks of life", "Science_and_Technology")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Main_Idea", "4", "Easy",
 "The first sentence announces the plan: ‘two significant voices’.",
 steps(("The plan", ev(1, "two significant voices were raised that questioned its meaning and value at the root") +
          p("The first four paragraphs give Rousseau’s objection; the last two give Condorcet’s.")),
       ("Choosing", p("Option 4 restates this plan."))) +
 final("Option 4"),
 "inference",
 [("1", "The passage does not trace how they influenced democracy’s development."), ("2", "No history of representative democracy is given."), ("3", "England and the ancient republics are only Rousseau’s examples.")])

P.rc(2, "V1", "Except", "3", "Easy",
 "Rousseau objects to representation itself, not to how representatives are chosen.",
 steps(("His view", ev(1, "sovereignty cannot be represented for the same reason that it cannot be transferred") +
          ev(3, "it is the existence of representation in itself that is called into question")),
       ("Matching", "<ol><li>Option 1: representation clashes with the general will.</li><li>Option 2: sovereignty that is represented has no legitimacy.</li><li>Option 4: the English are free only at elections.</li><li>Option 3 talks about how representation can be achieved. Rousseau says it cannot be achieved at all.</li></ol>")) +
 final("Option 3"),
 "except",
 [("1", "Stated in paragraph 2."), ("2", "Follows from ‘cannot be represented’."), ("4", "The English example.")])

P.rc(3, "V1", "Except", "2", "Hard",
 "Paragraph 3 says what Rousseau was not concerned with.",
 steps(("The line", ev(3, "It is striking that he is not especially concerned with highlighting the severe limits that the ‘‘free\" English system placed on representation") +
          p("The warning is about representation as such, not the defects of the English system.")),
       ("Choosing", p("Options 1, 3 and 4 are parts of the admonition (representation is illegitimate) or the premonition (a separate political class, lost freedom). Option 2 is the thing he did not stress."))) +
 final("Option 2"),
 "except",
 [("1", "The logical basis of the admonition."), ("3", "The premonition: a political class."), ("4", "Devaluing plus a warning.")])

P.rc(4, "V1", "Inference", "3", "Easy",
 "Follow the cycle: A beats B, B beats C, C beats A.",
 steps(("The line", ev(6, "It follows that A defeats B and B defeats C. However, C also defeats A") +
          p("Each option loses to another, so none beats all the rest.")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "Voters’ feelings are not discussed."), ("2", "Some winner can still be declared; it is just not meaningful."), ("4", "Each head-to-head is won 2–1: no ties.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Main_Idea", "4", "Medium",
 "The passage has two sets of maps. Which option covers both?",
 steps(("The close", ev(5, "These maps demonstrated how ethnographic cartography was not only a tool of imperial legitimation in the Baltic provinces but could also be a powerful means of expressing the political claims for Estonian and Latvian self-determination") +
          p("Rittikh’s maps legitimised empire; Latvian maps pushed back. Both show maps as political tools.")),
       ("Choosing", p("Option 4 holds both sides."))) +
 final("Option 4"),
 "inference",
 [("1", "Only the Russian half."), ("2", "Only the Russian half."), ("3", "Too general; the passage is about one region and one period.")])

P.rc(6, "V2", "Inference", "3", "Easy",
 "Paragraph 2 defines it.",
 steps(("The line", ev(2, "the particularities of imperial rule in the Baltic, the ‘Baltic Question’, sparked debates among intellectuals about how to justify Russian imperial rule over non-Russian populations and the relationship between the empire and emerging ideas around a distinctive Russian national culture")),
       ("Choosing", p("Option 3 restates it."))) +
 final("Option 3"),
 "inference",
 [("1", "Self-determination comes in only at the end."), ("2", "Other European powers are not discussed."), ("4", "The region’s role in Europe’s geopolitics is not the question.")])

P.rc(7, "V2", "Except", "2", "Easy",
 "What did Rittikh’s maps show about diversity?",
 steps(("The line", ev(1, "Rittikh’s maps painted a vivid portrait of a multi-ethnic and confessionally diverse imperial borderlands") +
          p("The maps showed the diversity; they did not suppress it.")),
       ("Choosing", p("Option 2 is false."))) +
 final("Option 2"),
 "except",
 [("1", "German elites, Lutheran faith, ‘the West’."), ("3", "Incorporated over the 18th century and ruled after."), ("4", "Estonian and Latvian mapmakers of the late 19th century.")])

P.rc(8, "V2", "Except", "1", "Easy",
 "Imperial legitimation was Rittikh’s use of maps, not Siliņš’s.",
 steps(("The line", ev(5, "They signified a radical departure from seeing the Baltics only through the lens of Russian or German possessions or sphere of influence")),
       ("Choosing", p("The Latvian maps challenged imperial claims; they did not show maps as a tool of imperial legitimation. Option 1."))) +
 final("Option 1"),
 "except",
 [("2", "A ‘radical departure’ from Russian and German views."), ("3", "The last sentence."), ("4", "Stated directly.")])

# ---------------- Passage 3 (Q9–12) ----------------
P.rc(9, "V3", "Main_Idea", "2", "Easy",
 "Where does the passage end up?",
 steps(("The close", ev(6, "history followed different courses for different peoples because of differences among peoples’ environments, not because of biological differences among peoples themselves")),
       ("Choosing", p("Differences in wealth and power come from history and environment: option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "The view the author rejects."), ("3", "A supporting point only."), ("4", "Genetics is rejected.")])

P.rc(10, "V3", "Inference", "1", "Medium",
 "What does the author conclude about racist explanations?",
 steps(("The line", ev(4, "The objection to such racist explanations is not just that they are loathsome, but also that they are wrong") +
          p("IQ studies cannot separate genes from environment, so racist explanations do not survive scrutiny.")),
       ("Choosing", p("Option 1."))) +
 final("Option 1"),
 "inference",
 [("2", "Calls the objections, not the explanations, loathsome."), ("3", "The problem is environment, not technical flaws."), ("4", "The author leaves ‘pure innate intelligence’ open (‘whatever that is’).")])

P.rc(11, "V3", "Inference", "1", "Medium",
 "Why is the missing ultimate explanation a ‘moral gap’?",
 steps(("The line", ev(6, "Much more serious, though, is the moral gap left unfilled") +
          p("Without an accepted ultimate explanation, people fall back on biological, racist ones (paragraphs 3–4).")),
       ("Choosing", p("The gap leaves room for racist explanations: option 1."))) +
 final("Option 1"),
 "inference",
 [("2", "The gap does not repudiate racism; it leaves space for it."), ("3", "The proximate explanations remain ‘clear’."), ("4", "Not linked to pure intelligence.")],
 opts=["Leaves room for racist explanations.", "Repudiates racism.", "Forces a rejection of proximate explanations.", "Undermines the concept of pure intelligence."])

P.rc(12, "V3", "Weaken", "4", "Medium",
 "The last paragraph says environment, not biology, explains history. Which option agrees with it?",
 steps(("The claim", ev(6, "because of differences among peoples’ environments, not because of biological differences among peoples themselves")),
       ("Choosing", p("Options 1–3 point to innate differences and so undermine the claim. Option 4 explains differences by social disadvantage, which fits it."))) +
 final("Option 4"),
 "weaken",
 [("1", "Links technology to intelligence: a biological account."), ("2", "Innate differences."), ("3", "Suggests something beyond technology and circumstance keeps groups down.")])

# ---------------- Passage 4 (Q13–16) ----------------
P.rc(13, "V4", "Main_Idea", "4", "Easy",
 "Where does the argument land?",
 steps(("The close", ev(4, "perhaps the earliest entities that reproduced and evolved were made of RNA, not DNA and proteins") +
          p("The building blocks lead to a chicken-and-egg problem, and RNA is offered as the way out.")),
       ("Choosing", p("Option 4 is the conclusion the passage builds to."))) +
 final("Option 4"),
 "inference",
 [("1", "The first step only."), ("2", "A side remark about the universe."), ("3", "The problem, without the answer.")])

P.rc(14, "V4", "Structure", "3", "Hard",
 "Name each stage of the passage with a heading.",
 steps(("Stages", "<ol><li>The building blocks: nucleotides, sugars, phosphate, bases, lipids.</li><li>How they formed: early Earth conditions, meteorites.</li><li>DNA and protein synthesis: the chicken-and-egg problem.</li><li>RNA as the alternative.</li></ol>"),
       ("Choosing", p("Option 3 names these four stages at the same level. Options 1 and 4 mix details with headings; option 2 starts with DNA alone and misses the other building blocks."))) +
 final("Option 3"),
 "summary",
 [("1", "Lists details, not the passage’s stages."), ("2", "‘DNA composition’ leaves out lipids and the other blocks."), ("4", "Starts with details; the key idea of protein synthesis is lost.")])

P.rc(15, "V4", "Inference", "4", "Medium",
 "What do the experiments and meteorites show?",
 steps(("The line", ev(2, "the principal building blocks of life, the molecules from which our cells are built, can form from natural processes") +
          p("Life’s components come from chemistry, which supports life arising from non-living matter.")),
       ("Choosing", p("Option 4."))) +
 final("Option 4"),
 "inference",
 [("1", "The passage doubts this."), ("2", "RNA evolving in the lab is not shown to be self-replicating on the early Earth."), ("3", "Only one step of the story.")])

P.rc(16, "V4", "Except", "3", "Easy",
 "Which ability of RNA is set against DNA?",
 steps(("The line", ev(4, "RNA stores information, like its cousin DNA, but some RNAs act like enzymes") +
          p("Information storage is shared; enzyme work is RNA’s and once thought to belong only to proteins.")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "except",
 [("1", "Shared: ‘like its cousin DNA’."), ("2", "Both are bound up with making proteins."), ("4", "Both carry and control genetic information.")])

# ---------------- Verbal ability (Q17–24) ----------------
P.va(17, P.sent_html(17), [], "TITA", "3142", "Para_Jumble", "Easy",
 "‘This has been endorsed’: what is ‘this’?",
 steps(("The opener", p("Sentence 3 states the problem: teenagers lack sleep.")),
       ("The sequence", p("Sentence 1 gives causes, including school start times. Sentence 4 offers the fix: start later. Sentence 2: ‘this’ fix has been endorsed and adopted."))) +
 final("3142"),
 "pj",
 [("3", "The problem."), ("1", "Causes."), ("4", "The fix."), ("2", "“This” = the fix.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.sent_html(18), [], "TITA", "3241", "Para_Jumble", "Medium",
 "‘The concept’ needs a concept named first.",
 steps(("The opener", p("Sentence 3 names “transitory inflation”.")),
       ("The sequence", p("Sentence 2: the concept assumes away the need to adjust. Sentence 4: the Fed’s own example. Sentence 1: the lesson — keep an open mind."))) +
 final("3241"),
 "pj",
 [("3", "The concept."), ("2", "What is wrong with it."), ("4", "An example."), ("1", "The conclusion.")],
 why_title="Why each sentence goes where it does")

P.va(19, P.sent_html(19), [], "TITA", "4132", "Para_Jumble", "Medium",
 "‘These questions’ and ‘the dichotomy’ point back.",
 steps(("The opener", p("Sentence 4 introduces the debate about technofixes.")),
       ("The sequence", p("Sentence 1 gives the two opinions. Sentence 3: ‘these questions’ divide politics into two sides. Sentence 2: recognising this ‘dichotomy’ helps."))) +
 final("4132"),
 "pj",
 [("4", "The debate."), ("1", "Two opinions."), ("3", "“These questions”."), ("2", "“The dichotomy”.")],
 why_title="Why each sentence goes where it does")

P.va(20, P.missing_html(20), P.strict_opts(20), "MCQ", "2", "Missing_Sentence", "Easy",
 "‘These risks’ must follow a list of risks.",
 steps(("Find the spot", p("Blank 2 comes right after the warnings about heart attacks, cancer and pregnancy complications. The sentence links them to smoke breathed in through the mouth, and the next sentence turns to the eyes with ‘But what is less often spotlighted’.")),
       ("Check the others", p("Blank 1 comes before any risks are named. Blanks 3 and 4 follow eye diseases, which are not caused by smoke in the mouth."))) +
 final("Option 2"),
 "missing",
 [("1", "No risks named yet."), ("3", "After eye diseases."), ("4", "After the cornea finding.")])

P.va(21, P.missing_html(21), P.strict_opts(21), "MCQ", "4", "Missing_Sentence", "Easy",
 "The writer then does the opposite of what is described just before.",
 steps(("Find the spot", p("Blank 4 follows the plan to make ChatGPT use an honour-code violation. ‘That’s the wrong approach’ rejects it, and the next sentence gives the writer’s own approach: students may use ChatGPT.")),
       ("Check the others", p("Blanks 1–3 come before the alternative is set up, and the writer still describes others’ worries or proposals there."))) +
 final("Option 4"),
 "missing",
 [("1", "Nothing yet to reject."), ("2", "Before any approach is proposed."), ("3", "The UCLA plan follows; the rejection should come after it.")])

P.va(22, P.summary_html(22, "Not all distractions are bad"), P.Q["VARC"][22]["opts"], "MCQ", "2", "Summary", "Hard",
 "Who does the work during the break, and what does it need?",
 steps(("What the passage says", "<ol><li>A break from a hard problem brings fresh ideas.</li><li>The unconscious mind works on the problem during the break.</li><li>It does so only if the problem was clearly defined by the conscious mind.</li></ol>"),
       ("Choosing", p("Option 2 has all three in the right relation."))) +
 final("Option 2"),
 "summary",
 [("1", "Says the unconscious mind needs a clear problem ‘to be effective’, not to start at all."), ("3", "Shifts the stress to defining the problem."), ("4", "Leaves out the unconscious mind.")])

P.va(23, P.summary_html(23, "The modern man seemingly"), P.Q["VARC"][23]["opts"], "MCQ", "4", "Summary", "Hard",
 "Is the weakening of Civil Society a cause of the loss of cohesion, or the same thing?",
 steps(("What the passage says", "<ol><li>People now see themselves as autonomous individuals, not members of groups.</li><li>This shows in the loss of social cohesion, which is the decline of Civil Society.</li><li>People look to the State instead.</li></ol>"),
       ("Choosing", p("Option 4 keeps this. Option 1 treats the weakening of Civil Society as a cause of lost cohesion, though the passage says they are the same thing."))) +
 final("Option 4"),
 "summary",
 [("1", "Makes Civil Society’s decline a cause of lost cohesion."), ("2", "Turns autonomy into a result of the State’s actions."), ("3", "Adds a fall in intelligence.")])

P.va(24, P.summary_html(24, "The offloading of memory"), P.Q["VARC"][24]["opts"], "MCQ", "1", "Summary", "Hard",
 "Is culture reduced to binary code, or more than it?",
 steps(("What the passage says", "<ol><li>Offloading memory threatens both the self and shared culture.</li><li>Technology drains our inner cultural inheritance and makes us ‘pancake people’.</li><li>Culture stays alive only when each generation renews it in their minds.</li></ol>"),
       ("Choosing", p("Option 1 keeps the threat, the pancake image and the loss of vitality."))) +
 final("Option 1"),
 "summary",
 [("2", "The passage says culture is more than binary code, not that we are reduced to it."), ("3", "Says technology imposes a new self; the passage says the self evolves under its pressure."), ("4", "Same binary-code error.")])
