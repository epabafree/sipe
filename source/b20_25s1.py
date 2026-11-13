# -*- coding: utf-8 -*-
# Batch 20 — CAT 2025 Slot 1: VARC (Q1–24). DILR and QA are added by b20_25s1_dilr.py and b20_25s1_qa.py.
# Question numbers follow the order of the actual exam.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2025, 1, "ex20_25s1.json")
P.passage("P1", "Passage 1 — Madness, medicine and the law", "Social_Science_and_History")
P.passage("P2", "Passage 2 — Does inequality help or hurt growth?", "Economics_and_Management")
P.passage("P3", "Passage 3 — Is electronic music really music?", "Arts_and_Literature")
P.passage("P4", "Passage 4 — Noise, tail events and complex systems", "Science_and_Technology")

P.va(1, P.ms(1), P.Q["VARC"][1]["opts"], "MCQ", "4", "Missing_Sentence", "Medium",
 "Ava’s quote is a general statement about method. Should it come before or after the specific examples?",
 steps(("The fit", p("The first sentence says the sisters follow their great-grandfather’s ways. Ava’s quote, “Everything is old-world, traditional techniques from Mexico”, sums that up in her own words. The paragraph then gives the details: tacote wood, carving by hand, no power tools. So the quote belongs at blank (1), between the general claim and the examples.")),
       ("Reading the options", p("Blank (1) is listed fourth, so the answer is option 4."))) +
 final("Blank (1), which is option 4."),
 "missing",
 [("1", "Blank (3) is about the waitlist and famous customers, which has moved on from technique."),
  ("2", "At blank (2) the techniques have already been described; the summing-up would come after its own examples."),
  ("3", "Blank (4) is about the sisters’ childhood, far from the discussion of technique.")])

P.va(2, P.summ(2), P.Q["VARC"][2]["opts"], "MCQ", "3", "Summary", "Medium",
 "The passage ends by saying appropriation matters beyond art. Which summary keeps that point?",
 steps(("What the passage says", "<ol><li>Artists draw on many cultures; respectful inspiration builds understanding.</li><li>The line with appropriation is thin: borrowing without understanding, respect or acknowledgement.</li><li>Appropriation’s effects reach beyond art, shaping perceptions and power imbalances.</li></ol>"),
       ("Choosing", p("Option 3 keeps the navigation between the two and the wider social impact. Option 2 is close but stops at commodification and stereotypes, leaving out the broader effects the passage stresses."))) +
 final("Option 3."),
 "summary",
 [("1", "The choice isn’t about acknowledging other works; it’s about how artists borrow."),
  ("2", "It omits the wider societal impact, which the passage calls essential to recognise."),
  ("4", "The passage doesn’t say artists must draw from every culture to appeal to all.")])

P.va(3, P.summ(3), P.Q["VARC"][3]["opts"], "MCQ", "2", "Summary", "Medium",
 "Follow the chain: ageing, clearance, accumulation, inflammation, disease.",
 steps(("What the passage says", "<ol><li>Senescent “zombie” cells can’t divide and are cleared by apoptosis.</li><li>With age, clearance becomes less efficient, so they build up.</li><li>They release inflammatory chemicals that, over time, damage healthy cells and lead to chronic disease.</li></ol>"),
       ("Choosing", p("Option 2 is the only one that carries the whole chain from ageing to disease."))) +
 final("Option 2."),
 "summary",
 [("1", "It stops at accumulation, and says the cells “resist” apoptosis, whereas the passage says clearance becomes less efficient."),
  ("3", "This is a definition, not a summary."),
  ("4", "The cells aren’t dead; they are damaged cells that still use energy.")])

P.va(4, P.sents(4), [], "TITA", "1", "Odd_One_Out", "Medium",
 "Sentence 5 says “to enable this”. What is “this”?",
 steps(("The chain", p("Sentence 3: Neagley says pre-Renaissance people engaged with art visually, physically and through movement. Sentence 5: the tapestry was hung at eye level “to enable this”. Sentence 2: if it hung in a square, people stood in the centre. Sentence 4: that would make it an immersive space.")),
       ("The extra sentence", p("Sentence 1 is about the tapestry’s purpose, telling the story of the Normans, and its “therefore” has nothing to follow from."))) +
 final(r"\(1\)"),
 "oddone",
 [("3", "Neagley’s idea about how people engaged with art."), ("5", "“To enable this”: hung at eye level."), ("2", "“So if…” the square arrangement."), ("4", "“That would make it” an immersive space.")],
 why_title="How the other sentences fit")

P.va(5, P.sents(5), [], "TITA", "4", "Odd_One_Out", "Hard",
 "Sentence 2 begins “But”. What does it push back against?",
 steps(("The chain", p("Sentence 5: freedom is a contested notion, and the author won’t settle the big controversies. Sentence 2: “But” freedom over death should be central. Sentence 1: technology and culture have given us more of this freedom. Sentence 3: legalising assisted dying is a further step in realising it.")),
       ("The extra sentence", p("Sentence 4 turns to how many people endorse a right to medical help in dying. It is about public opinion, which breaks the author’s line of argument."))) +
 final(r"\(4\)"),
 "oddone",
 [("5", "Freedom is contested."), ("2", "“But” freedom over death is central."), ("1", "We now have more of this freedom."), ("3", "Assisted dying is a further step.")],
 why_title="How the other sentences fit")

# ---------------- Passage 1 ----------------
P.rc(6, "P1", "Inference", "1", "Hard",
 "The men were bound together by background, yet something also drew their professions into the same arena.",
 steps(("The last paragraph", ev(4, "But for all their affinities, men of medicine and law were divided by contests over the borders of criminal responsibility, as much within each profession as between them.") +
          p("Their shared professional ground was the question of criminal responsibility. They argued over its borders, but that very contest is what connected doctors and lawyers in the courtroom.")),
       ("The others", p("The other options are details from elsewhere in the passage, not what links these men."))) +
 final("Option 1."),
 "inference",
 [("2", "These are symptoms some alienists classed as mental disease."),
  ("3", "Empathy and imagination describe how jurors inferred mental states, in the first paragraph."),
  ("4", "Family and neighbours’ opinions are what experts replaced.")])

P.rc(7, "P1", "Main_Idea", "3", "Medium",
 "Which set covers the passage’s core: judging minds, madness and guilt?",
 steps(p("The passage is about how courts judged a defendant’s mental state, how insanity was diagnosed, and how criminal responsibility was tied to punishment. “Judgement, Insanity, Punishment, Responsibility” covers all of it.")) +
 final("Option 3."),
 "inference",
 [("1", "Patronage and accounts are side details."),
  ("2", "Business and prosecution are peripheral."),
  ("4", "Patriotism is a minor detail about what bound the men together.")])

P.rc(8, "P1", "Detail", "4", "Easy",
 "The passage defines the term in the second paragraph.",
 steps(ev(2, "In the nineteenth century, physicians who specialized in the study of madness and the care of the insane held themselves out as experts in the new field of mental science. Often called alienists or mad doctors")) +
 final("Option 4."),
 "detail",
 [("1", "Alienists did push their field’s boundaries, but that isn’t what the word means."),
  ("2", "Alienists weren’t lawyers, and immigrants aren’t mentioned."),
  ("3", "Extraterrestrials have nothing to do with the passage.")])

P.rc(9, "P1", "Vocabulary", "2", "Medium",
 "Confession sits in a list with disease, gender and race. What kind of difference would fit that list?",
 steps(p("The list names ways a defendant could seem unlike the officials. “Confession” here means a religious denomination, as in “the Protestant confession”. The last paragraph confirms religion mattered: the officials were bound by Protestantism.")) +
 final("Option 2."),
 "detail",
 [("1", "It isn’t about claiming a gender, race or disease as a defence."),
  ("3", "“Struck officials as” means “seemed to officials”, not an attack."),
  ("4", "“By dint of” means “by means of”; it has nothing to do with “didn’t”.")])

# ---------------- Passage 2 ----------------
P.rc(10, "P2", "Application", "4", "Medium",
 "The incentive argument says pay must be linked to effort and results.",
 steps(ev(1, "paying compensations without taking into account the economic performance achieved by individual agents will fail to elicit optimum effort from the agents") +
       p("So inequality helps growth when higher pay rewards higher performance. Option 4 does exactly that.")) +
 final("Option 4."),
 "inference",
 [("1", "Concentrated ownership is the third, governance argument, not the incentive one."),
  ("2", "Pay by tenure ignores output, which is what the incentive argument warns against."),
  ("3", "Rents that don’t link pay to results give no incentive.")])

P.rc(11, "P2", "Main_Idea", "3", "Hard",
 "The passage has two halves. Does it take a side, or report both?",
 steps(("The first half", p("Three channels by which inequality may help growth: investment indivisibilities, incentives and governance. One study finds short-run gains and long-run harm.")),
       ("The second half", p("Most studies find a negative link, through human capital, fertility, instability, social capital and politics.")),
       ("Choosing", p("Option 3 is the best of the four: it names the three channels and the short-term gain with long-term drawbacks. The others misstate what the passage does."))) +
 final("Option 3."),
 "inference",
 [("1", "The passage doesn’t argue that inequality accelerates growth; it reports views on both sides."),
  ("2", "The passage does discuss human capital, fertility and redistribution."),
  ("4", "The passage never makes this methodological claim.")])

P.rc(12, "P2", "Purpose", "1", "Medium",
 "What do the three arguments have in common, and in what time frame does the evidence apply?",
 steps(p("Each argument names a setting where inequality might help: large sunk costs without financial markets, the need for incentives, and the benefits of concentrated ownership. The evidence cited shows gains in the short and medium term.")) +
 final("Option 1."),
 "purpose",
 [("2", "This reverses the governance argument: dispersed ownership slows decisions."),
  ("3", "“Every period” contradicts the long-run negative finding."),
  ("4", "The passage doesn’t say mature stock markets harm investment.")])

P.rc(13, "P2", "Application", "4", "Medium",
 "Democratization extends the vote. The opposite would take the vote away and close down opposition.",
 steps(ev(2, "when democratization extends suffrage to a wider class of people, the increased political power of low- and middle-income voters results in broader support for income redistribution") +
       p("Narrowing suffrage and banning opposition parties is the reverse.")) +
 final("Option 4."),
 "inference",
 [("1", "Term limits and judicial review limit power; calling them autocratic doesn’t make them so."),
  ("2", "Capping donations and public funding widen fairness; the label “oligarchy” is just how it was portrayed."),
  ("3", "Participatory budgeting and recall elections increase democracy, whatever a press release calls them.")])

P.va(14, P.ms(14), ["Option 4", "Option 3", "Option 1", "Option 2"], "MCQ", "3", "Missing_Sentence", "Hard",
 "The second sentence of the paragraph refers to “this need”. What need?",
 steps(("The link", p("“Timothy Schroder put it succinctly in suggesting that electric light and eating in the kitchen eroded this need.” “This need” has to be stated before it. The missing sentence supplies it: silver’s role in “show”, display in houses, churches and diplomacy. So the sentence opens the paragraph at blank (1).")),
       ("Reading the options", p("Blank (1) is listed third, so the answer is option 3."))) +
 final("Blank (1), which is option 3."),
 "missing",
 [("1", "Blank (4) is the very end, after the museums; “this need” would have nothing to refer to."),
  ("2", "Blank (3) sits before “Another factor”, which follows the collectors; it is too late to introduce the need."),
  ("4", "Blank (2) is after Schroder’s quote, which already depends on “this need”.")])

P.va(15, P.sents(15, P.PJ_DIR), [], "TITA", "3421", "Para_Jumble", "Medium",
 "Find the general claim about women and anger, then the coach’s experience.",
 steps(("The opener", p("Sentence 3: women, unlike men, are taught to keep a lid on their anger.")),
       ("The example", p("Sentence 4: “Many of them” are so uneasy with aggression that the coach has to stop them pulling their punches. Sentence 2: once the taboo is broken, it feels liberating.")),
       ("The close", p("Sentence 1, beginning “But man, woman or otherwise”, widens the point to everyone."))) +
 final("3421"),
 "pj",
 [("3", "Women are taught to suppress anger."), ("4", "“Many of them” pull their punches."), ("2", "Breaking the taboo liberates them."), ("1", "“But man, woman or otherwise”: the general lesson.")],
 why_title="Why each sentence goes where it does")

P.va(16, P.sents(16, P.PJ_DIR), [], "TITA", "3142", "Para_Jumble", "Hard",
 "Sentence 3 names the panoptic mechanism. Which sentences then use “it”?",
 steps(("The opener", p("Sentence 3 introduces the panoptic mechanism and what it does.")),
       ("Elaboration", p("Sentence 1 (“It can in fact be integrated into any function…”) gives the details. Sentence 4 (“In short”) sums them up.")),
       ("The close", p("Sentence 2 is a closing remark: an idea that seems easy once someone has thought of it."))) +
 final("3142"),
 "pj",
 [("3", "Names the mechanism."), ("1", "“It can in fact…”: the details."), ("4", "“In short”: the summary."), ("2", "A closing remark on its simplicity.")],
 why_title="Why each sentence goes where it does")

# ---------------- Passage 3 ----------------
P.rc(17, "P3", "Inference", "2", "Medium",
 "The first question asks whether electronic music is music at all. What does the author say about the communication problem?",
 steps(ev(2, "When the new structural procedures of electronic music are at last fully understood by the listener the barriers between him and the work he faces will be removed.") +
       p("The new vocabulary of forms is a barrier to accepting electronic music as music, but one that can be overcome with understanding.")) +
 final("Option 2."),
 "inference",
 [("1", "The author says the barrier can be removed, not that it settles the question against electronic music."),
  ("3", "The passage never says music must be hard to understand."),
  ("4", "The communication problem is directly tied to the first question.")])

P.rc(18, "P3", "Vocabulary", "2", "Medium",
 "The composer looks beyond traditional patterns towards languages unique to the new medium.",
 steps(ev(3, "he feels that it is in the exploration of sui generis languages and forms that the aesthetic magic of the new medium lies") +
       p("“Sui generis” means of its own kind, peculiar to itself. “Particular” is closest.")) +
 final("Option 2."),
 "detail",
 [("1", "The languages are new, not beyond description."),
  ("3", "The author sees aesthetic magic in them."),
  ("4", "“Generic” is the opposite of one-of-a-kind.")])

P.rc(19, "P3", "Main_Idea", "2", "Easy",
 "The passage opens with two objections and answers each one.",
 steps(p("The first objection, that it isn’t music, is answered with the modern view of music and the hope of overcoming the communication barrier. The second, that it is inhuman, is answered by pointing out that the composer makes every decision. The author is defending electronic music.")) +
 final("Option 2."),
 "inference",
 [("1", "The contrast between centuries is one step in the argument, not its goal."),
  ("3", "The author is defending electronic music as music, not separating it from other music."),
  ("4", "Hiller and Stravinsky are cited in support, not attacked.")])

P.rc(20, "P3", "Except", "4", "Hard",
 "Stravinsky’s definition widens what counts as music. Does it give a test for which sounds are musical?",
 steps(ev(1, "many composers have preferred more objective definitions of music, epitomized in Stravinsky’s description of it as “a form of speculation in terms of sound and time”") +
       p("The definition responds to the 19th-century idea of music as emotional expression, complicates what music communicates, and lets electronic music count. It offers no way of sorting musical sounds from non-musical ones.")) +
 final("Option 4."),
 "except",
 [("1", "It moves music away from emotional communication."),
  ("2", "Accepting it brings the layman closer to electronic music."),
  ("3", "It answers the 19th-century view of music.")])

# ---------------- Passage 4 ----------------
P.rc(21, "P4", "Except", "2", "Medium",
 "Look for an option with absolute words like “solely” and “overriding”.",
 steps(ev(4, "Some of these dynamics are potentially attributable to former sports bettors") +
       p("The passage says “some” and “potentially”. Option 2 turns that into the sole and overriding cause, which isn’t supported.")) +
 final("Option 2."),
 "except",
 [("1", "A first-order tail event changes the rules and raises the odds of further ones."),
  ("3", "Bank runs and toilet-paper scrambles are given as contagion examples."),
  ("4", "Heavy tails make extreme events more frequent and larger.")])

P.rc(22, "P4", "Weaken", "1", "Medium",
 "Strengthen “one big shock raises the odds of more”. Which observation shows extremes clustering after a crash?",
 steps(ev(3, "once a first-order tail event occurs, the rules change, and the probability of a second-order tail event increases") +
       p("Option 1 shows extreme days clustering for weeks after a crash, far more often than normal. That is direct support.")) +
 final("Option 1."),
 "weaken",
 [("2", "No aftershocks would weaken the claim."),
  ("3", "Isolated spikes with no later rise would weaken it."),
  ("4", "Thin, normal tails regardless of storms cut against heavy-tailed behaviour.")])

P.rc(23, "P4", "Main_Idea", "4", "Easy",
 "Track the sequence: noise and order, heavy tails, second-order events, nonstationarity.",
 steps(p("The passage moves from noise producing order, to heavy-tailed cascades in contagious settings, to how a first shock raises the odds of more by changing the rules (nonstationarity), with the COVID-19 market as an example. Option 4 follows that path.")) +
 final("Option 4."),
 "inference",
 [("1", "“Always” and “invariably” overstate a tentative example."),
  ("2", "The passage says social outcomes are often heavy-tailed, not normal."),
  ("3", "Nonstationarity applies well beyond biology, including markets.")])

P.rc(24, "P4", "Inference", "1", "Hard",
 "For the apps to backfire, individual reactions must add up to a collective pattern. What has to be true of how people move?",
 steps(ev(1, "If each of us changes our behaviour to avoid the infected, we might generate a collective pattern we had aimed to avoid") +
       p("This only works if people adjust their movement based on infections and on what others do, so that small local responses combine into large-scale patterns. Option 1 states that assumption.")) +
 final("Option 1."),
 "inference",
 [("2", "If apps had no predictable effect on movement, the suggestion would collapse."),
  ("3", "Perfect accuracy isn’t needed; the issue is how people react."),
  ("4", "This makes interdependence negligible, the opposite of what is needed.")])
