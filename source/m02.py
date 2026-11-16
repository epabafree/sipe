# -*- coding: utf-8 -*-
# Simp Mock 2: VARC (24 of 24). DILR and QA: m02_dilr.py, m02_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(2, "sm02.json")
P.passage("V1", "Passage 1 — Self-determination after 1918", "Social_Science_and_History")
P.passage("V2", "Passage 2 — Three kinds of money", "Economics_and_Management")
P.passage("V3", "Passage 3 — Saving the parasites", "Environment_and_Life_Science")
P.passage("V4", "Passage 4 — Why humans dance", "Philosophy_and_Psychology")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Main_Idea", "3", "Easy",
 "The passage has two halves: why self-determination was weak, and who gained from it. Which option holds both?",
 steps(("The thread", ev(2, "the geopolitical map of interwar East Central Europe, with its plethora of new, restored, and enlarged so-called nation-states, was not congruent with the real distribution of power in Europe") +
          p("Paragraphs 1–2: the new states were built on self-determination, but the map did not match real power. Paragraphs 3–4: Germany and Soviet Russia, still strong, were the revisionist threats who exploited it.")),
       ("Choosing", p("Option 3 joins the mismatch and the two threats. The others hold one half each."))) +
 final("Option 3"),
 "inference",
 [("1", "Only the last paragraph’s consequences."), ("2", "Only the first half; it also says self-determination simply ‘failed’."), ("4", "Only the German and Russian threat.")])

P.rc(2, "V1", "Detail", "1", "Easy",
 "Read the end of paragraph 1: ‘for all their admitted flaws, they still…’.",
 steps(("The line", ev(1, "for all their admitted flaws, they still freed three times as many people from nationally alien rule as they subjected to such rule") +
          p("Despite the flaws, the arrangements mostly did what self-determination asked: on balance they freed far more people than they placed under alien rule.")),
       ("Choosing", p("Option 1 says this."))) +
 final("Option 1"),
 "detail",
 [("2", "That is the charge of the revisionist apologists, which the author rejects."), ("3", "Stateless nations and aggrieved minorities are different groups; nothing says the losers became stateless."), ("4", "The paragraph defends the arrangements as broadly true to self-determination.")])

P.rc(3, "V1", "Detail", "4", "Easy",
 "Paragraph 2 restates the weakness with ‘in other words’.",
 steps(("The line", ev(2, "The real political weakness of the interwar effort to implement the principle of national self-determination in East Central Europe lay not in its alleged hypocrisy, but in the impossibility of reconciling it with three other important aims") +
          ev(2, "was not congruent with the real distribution of power in Europe")),
       ("Choosing", p("Option 4 is the ‘in other words’ sentence."))) +
 final("Option 4"),
 "detail",
 [("1", "The number of states is not called the weakness."), ("2", "The weakness is a clash of aims, not ignoring people’s wishes; it also leaves out the third aim."), ("3", "The passage says the weakness was not the alleged hypocrisy.")])

P.rc(4, "V1", "Detail", "4", "Easy",
 "Find the ‘as the West was then inhibited…’ clause.",
 steps(("The line", ev(4, "as the West was then inhibited by its commitments to the successor states from paying the Soviet Union’s price for such cooperation") +
          p("The Soviet price was East Central Europe’s independence, and the West’s commitments to those states stopped it from paying.")),
       ("Choosing", p("Option 4 gives that reason."))) +
 final("Option 4"),
 "detail",
 [("1", "Explains Germany’s strength, not the failure to cooperate."), ("2", "Collaboration is a separate effect, and ‘till the late 1930s’ is not stated."), ("3", "Not stated.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Except", "4", "Easy",
 "In a pure hard-money system, are there any ‘claims’ at all?",
 steps(("Paragraph 2", ev(2, "Hard money is the most restrictive system because money can’t be created unless the supply of the metal or other intrinsically valuable commodity that is the money is increased") +
          p("Claims on hard money belong to the second system, where their ratio to the metal ‘rises’ as money and credit are created.")),
       ("Choosing", p("Options 1–3 follow from the paragraph. Option 4 puts claims into the hard-money system and says they always exceed the metal, which the paragraph does not allow."))) +
 final("Option 4"),
 "except",
 [("1", "Stated directly."), ("2", "Claims grow as more money and credit are wanted: they track the money the economy uses."), ("3", "The metal itself is the hard money held.")])

P.rc(6, "V2", "Detail", "2", "Easy",
 "What does the central bank no longer have to hand over?",
 steps(("The line", ev(3, "there is just paper money that the central bank can print without restriction. As a result, there is no risk that the central bank will have its stash of hard money drawn down") +
          p("No default is possible because the bank can always create the money it owes.")),
       ("Choosing", p("Option 2 says this."))) +
 final("Option 2"),
 "detail",
 [("1", "That is the danger of fiat money, not the reason default is ruled out."), ("3", "Also part of the danger."), ("4", "Describes the second system.")])

P.rc(7, "V2", "Inference", "3", "Easy",
 "Type 1 is the metal, Type 2 a claim on it. What is Type 3?",
 steps(("The line", ev(3, "No hard money is involved in fiat systems") +
          p("Fiat money is neither a commodity nor a claim to one.")),
       ("Choosing", p("Option 3 is the only one that fits Type 3 alone."))) +
 final("Option 3"),
 "inference",
 [("1", "Type 1."), ("2", "Type 2."), ("4", "The passage says too much fiat money drives people out of it.")])

P.rc(8, "V2", "Inference", "2", "Medium",
 "The cycle lasts 50 to 75 years and ends by restructuring the monetary system. What moves over those decades?",
 steps(("The lines", ev(4, "it naturally moves from Type 1 to Type 2, or Type 2 to Type 3") +
          ev(5, "This ‘big cycle’ typically plays out over something like 50 to 75 years; its ending is characterized by a restructuring of debts and the monetary system itself")),
       ("Choosing", p("Option 2 has the movement through the three types and the restructuring that ends it."))) +
 final("Option 2"),
 "inference",
 [("1", "The passage says the effects can be long-lasting, not that restructuring avoids them."), ("3", "That is the short crisis phase, not the whole cycle."), ("4", "Booms and slumps of the economy are not what the passage describes.")],
 opts=["The long-term ups and downs of monetary systems, in which old debt is restructured so as to avoid long-lasting consequences.",
       "The movement of money from hard money to paper money to fiat money over decades, ending in a restructuring of debts and of the monetary system itself.",
       "The short period, from a few months to three years, in which debt and currency crises play out.",
       "The swings of an economy between expansion and contraction that weaken the currency and confidence in the monetary system."])

# ---------------- Passage 3 (Q9–12) ----------------
P.rc(9, "V3", "Detail", "4", "Easy",
 "One option says the opposite of paragraph 2.",
 steps(("Paragraph 2", ev(2, "Since parasites by definition need other species, they’re particularly vulnerable to the phenomenon") +
          p("Parasites are more, not less, exposed to extinction.")),
       ("Choosing", p("Option 4 is contradicted. Options 1 and 3 are in the passage; option 2 is simply not discussed."))) +
 final("Option 4"),
 "detail",
 [("1", "Paragraph 1: they fill an open niche."), ("2", "Not discussed, so not contradicted."), ("3", "Paragraph 5: they manipulate hosts.")],
 q="Which of the following statements about parasites is contradicted by the passage?")

P.rc(10, "V3", "Inference", "3", "Medium",
 "Co-extinction: a parasite dies with its only host. Which parasite does not hang on one host?",
 steps(("The idea", ev(2, "Since parasites by definition need other species, they’re particularly vulnerable to the phenomenon") +
          p("A parasite tied to one endangered host goes when the host goes.")),
       ("Choosing", ev(5, "Nematomorph worms, for instance, mature inside crickets but then need to be in water to mate") +
          p("The worms pass through crickets and then leave for the water. Spread over hosts and habitats, they are the least likely to vanish with one species."))) +
 final("Option 3"),
 "inference",
 [("1", "The passage’s own example of co-extinction."), ("2", "Already lost with the condors’ de-lousing."), ("4", "Mostly eliminated in some countries already.")])

P.rc(11, "V3", "Inference", "2", "Easy",
 "Paragraph 4 says what happens if parasites vanish.",
 steps(("The line", ev(4, "Without parasites keeping them in check, populations of some animals would explode")),
       ("Choosing", p("Parasites keep host populations in check: option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "The manipulation helps the parasite, and feeds the predator; it does not ‘benefit’ the next host."), ("3", "The immune system evolved alongside parasites; they are not ‘responsible’ for it."), ("4", "Parasites check their hosts, which need not be predators; in paragraph 5 they feed predators.")])

P.rc(12, "V3", "Weaken", "4", "Easy",
 "The argument: losing intestinal parasites brings autoimmune disease. What gives another cause?",
 steps(("The argument", ev(6, "where we have eliminated most intestinal parasites, we have autoimmune diseases that are virtually unheard of in places where everyone still has those parasites") +
          p("The paragraph credits parasites with preventing autoimmune disease.")),
       ("Choosing", p("If infections such as viruses often trigger these diseases, the pattern may have another cause. Option 4 weakens the argument."))) +
 final("Option 4"),
 "weaken",
 [("1", "Calling the question contentious favours neither side."), ("2", "Supports the argument."), ("3", "Supports the background of the argument.")])

# ---------------- Passage 4 (Q13–16) ----------------
P.rc(13, "V4", "Inference", "3", "Easy",
 "Read the sentence that judges both approaches.",
 steps(("The line", ev(1, "While the first type of reasoning struggles to explain why so many humans choose to dance, the second struggles to explain why humans continue to dance") +
          p("Both fail to explain why people today still choose to dance: one cannot say why so many pick dance, the other why it survives once language and religion arrive.")),
       ("Choosing", p("Option 3 joins the two failures."))) +
 final("Option 3"),
 "inference",
 [("1", "The second approach is about social bonds, not physical activity."), ("2", "Both approaches are about meanings: personal and communal."), ("4", "They are the psychological and anthropological views.")])

P.rc(14, "V4", "Detail", "4", "Easy",
 "The second approach says dance is replaced. Then why do people still dance?",
 steps(("The line", ev(1, "In these accounts, dancing is eventually replaced by more rational and effective means of social bonding that the dancing itself makes possible, such as language, morality and religion")),
       ("Choosing", p("On that account humans no longer need dance for bonding, so it cannot explain why they continue to dance: option 4."))) +
 final("Option 4"),
 "detail",
 [("1", "The explanations are not replaced; dancing is, in their account."), ("2", "A claim, not the reason the approach fails."), ("3", "That is the first approach.")])

P.rc(15, "V4", "Except", "1", "Medium",
 "List the three capacities and match each option.",
 steps(("The line", ev(3, "to notice and recreate movement patterns; to remember and share movement patterns; and to mobilise these movement patterns as a means for sensing and responding to whatever appears")),
       ("Matching", "<ol><li>Option 2: noticing movement, one’s own and others’.</li><li>Option 3: sharing movement patterns.</li><li>Option 4: sensing whatever appears.</li><li>Option 1: controlling the environment, which the passage never says; it speaks of sensing and responding.</li></ol>")) +
 final("Option 1"),
 "except",
 [("2", "The first capacity."), ("3", "The second capacity."), ("4", "The third capacity.")])

P.rc(16, "V4", "Inference", "1", "Medium",
 "‘Becoming’ is about growth. What grows, and through what?",
 steps(("The lines", ev(5, "every aspect of a human bodily self – from chromosomal couplet to sense organ to limb shape – is a capacity for moving that develops through a process of its own movement making") +
          ev(6, "A human is always creating patterns of bodily movement, where every new movement unfolds along an open-ended trajectory made possible by movements already made")),
       ("Choosing", p("The body is always developing through its own movement: option 1."))) +
 final("Option 1"),
 "inference",
 [("2", "Moves the patterns into the environment."), ("3", "The idea is about every human, not each dancer’s style."), ("4", "One result of the process, not the process itself.")])


# ---------------- Verbal ability (Q17–24) ----------------
P.va(17, P.sent_html(17), [], "TITA", "3241", "Para_Jumble", "Easy",
 "Sentence 1 says inflation can ‘also’ occur. What came before it?",
 steps(("The opener", p("Sentence 3 introduces inflation as normal and healthy if kept in check.")),
       ("The sequence", p("Sentence 2: prices rise as populations and demand grow. Sentence 4: companies raise prices to meet demand and higher costs. Sentence 1 adds a different cause, governments injecting money."))) +
 final("3241"),
 "pj",
 [("3", "Introduces inflation."), ("2", "Demand-side causes."), ("4", "Companies’ response."), ("1", "“Also”: another cause.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.sent_html(18), [], "TITA", "3124", "Para_Jumble", "Medium",
 "‘In reality’ corrects a view. Which sentence states that view?",
 steps(("The opener", p("Sentence 3: we talk of the ‘future of work’ as something at a distance in time.")),
       ("The sequence", p("Sentence 1: in reality it is not so different from today. Sentence 2: ‘they’, the management practices, rest on the same foundations. Sentence 4: ‘these goals’ are those foundations, pursued through oversight."))) +
 final("3124"),
 "pj",
 [("3", "The common view."), ("1", "“In reality”: the correction."), ("2", "“They” = management practices."), ("4", "“These goals” = efficiency and the rest.")],
 why_title="Why each sentence goes where it does")

P.va(19, P.sent_html(19), [], "TITA", "2413", "Para_Jumble", "Medium",
 "Sentence 3 explains repetition. Which sentence mentions repetition?",
 steps(("The opener", p("Sentence 2 sets the topic: how machine-written prompts differ from human ones.")),
       ("The sequence", p("Sentence 4 gives the first difference: fluent but less nuanced. Sentence 1 adds another: repetitions and odd word combinations. Sentence 3 explains why: models reproduce patterns in their data."))) +
 final("2413"),
 "pj",
 [("2", "The topic."), ("4", "First difference."), ("1", "“Additionally”: repetitions."), ("3", "“This is because”: explains the repetitions.")],
 why_title="Why each sentence goes where it does")

P.va(20, P.missing_html(20), P.strict_opts(20), "MCQ", "3", "Missing_Sentence", "Easy",
 "The sentence is a step in a transaction. Where is a transaction being described?",
 steps(("Find the spot", p("Before blank 3: the receiver sends a public key to the sender. The missing step is the sender signing with a private key and sending the transaction out. After it, the paragraph moves on to the ledger.")),
       ("Check the others", p("Blanks 1 and 2 come before keys or users have been mentioned; blank 4 is after the ledger, too late for the transfer itself."))) +
 final("Option 3"),
 "missing",
 [("1", "Still about who created Bitcoin."), ("2", "Before keys are explained."), ("4", "After the transaction has been recorded.")])

P.va(21, P.missing_html(21), P.strict_opts(21), "MCQ", "3", "Missing_Sentence", "Easy",
 "‘That period’ needs a period just named.",
 steps(("Find the spot", p("Before blank 3: ‘From that time until its transfer back to China in the late 20th century’. The sentence compares China over that same period, which fits right after the different paths are mentioned.")),
       ("Check the others", p("At blank 1 or 2 no period has yet been defined; blank 4 is after the return, where the contrast is no longer the topic."))) +
 final("Option 3"),
 "missing",
 [("1", "No period named yet."), ("2", "The sentence after it starts ‘From that time’ about Hong Kong; inserting China breaks the link."), ("4", "The story has moved to the handover.")])

P.va(22, P.summary_html(22, "While the problem of humanization"), P.Q["VARC"][22]["opts"], "MCQ", "1", "Summary", "Medium",
 "Follow the chain: concern → recognition → doubt.",
 steps(("What the passage says", "<ol><li>Humanization has always been humankind’s central problem, and is now unavoidable.</li><li>Concern for it leads to recognising dehumanization as a reality.</li><li>Seeing its extent, one may ask whether humanization is possible.</li></ol>"),
       ("Choosing", p("Option 1 keeps the chain in order."))) +
 final("Option 1"),
 "summary",
 [("2", "Leaves out the central problem and muddles the chain."), ("3", "Drops the doubt about viability."), ("4", "Calls the concern itself questionable.")])

P.va(23, P.summary_html(23, "The matter of being able to define"), P.Q["VARC"][23]["opts"], "MCQ", "4", "Summary", "Medium",
 "Who does what to whom? The elites use creativity; its enemies are portrayed badly.",
 steps(("What the passage says", "<ol><li>Defining creativity matters to the intellectual elite, who work by manipulating esteem.</li><li>Its enemies are portrayed as immoral, stupid and crude.</li><li>Calling oneself creative has become a claim to status.</li></ol>"),
       ("Choosing", p("Option 4 keeps all three without changing who does what."))) +
 final("Option 4"),
 "summary",
 [("1", "‘Those not deemed creative’ is not ‘its enemies’."), ("2", "Says the targets are immoral, rather than portrayed so."), ("3", "Leaves out the enemies.")])

P.va(24, P.summary_html(24, "If we wished to sum up"), P.Q["VARC"][24]["opts"], "MCQ", "2", "Summary", "Hard",
 "Why did people accept the stronger tyranny?",
 steps(("What the passage says", "<ol><li>A century of revolutions replaced weak individual tyranny with strong collective tyranny.</li><li>A people wanting equality, and holding governments responsible, found the first unbearable but endure the second.</li><li>So the State’s tyranny grew.</li></ol>"),
       ("Choosing", p("Option 2 has the revolutions, the replacement and the readiness to endure it."))) +
 final("Option 2"),
 "summary",
 [("1", "Leaves out why people accept it."), ("3", "Leaves out why people accept it."), ("4", "Drops the century of revolutions and says the desire for equality led to the change directly.")])
