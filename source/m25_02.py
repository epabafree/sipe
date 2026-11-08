# -*- coding: utf-8 -*-
# Simp Mock 2 (2025): VARC (24 of 24). DILR and QA: m25_02_dilr.py, m25_02_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(2, "sm25_02.json", series=2025)
P.passage("V1", "Passage 1 — Training AI without giant clusters", "Science_and_Technology")
P.passage("V2", "Passage 2 — An Iron Age matrilocality", "Social_Science_and_History")
P.passage("V3", "Passage 3 — Quantification fixation", "Economics_and_Management")
P.passage("V4", "Passage 4 — Selling Shangri-La", "Politics")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Main_Idea", "2", "Medium",
 "Which five terms carry the passage’s argument from start to finish?",
 steps(("The argument", p("Ever-bigger GPU clusters hit limits; constant checkpointing wastes time; DiLoCo distributes training across islands and cuts communication; models trained this way generalise better.")),
       ("Choosing", p("Option 2 has the problem (GPU clusters, checkpointing), the solution (distributed training, DiLoCo) and its payoff (generalisation)."))) + final("Option 2"),
 "inference", [("1", "‘Monolithic data centres’ and ‘parallelization’ aren’t the passage’s terms; DiLoCo is missing."), ("3", "Leaves out DiLoCo and distributed training."), ("4", "Consumer devices are a distant dream; checkpointing, the core problem, is missing.")])
P.rc(2, "V1", "Detail_Not_True", "3", "Easy",
 "Generalisation comes up as a <i>benefit</i> of DiLoCo, not as a problem of old methods.",
 steps(("Challenges named", p("Constant synchronisation (option 1), upfront costs of bespoke clusters (option 2), and time spent shuttling data (option 4).")),
       ("The odd one", ev(3, "Models trained this way may be slightly less fine-tuned for tasks they were explicitly trained on, but they often generalise better when confronted with new problems") +
          p("Generalising is the models’ ability, and the passage presents it as a gain of the new method. It is not listed as a failing of GPUs."))) + final("Option 3"),
 "notrue", [("1", "¶2: constant checkpointing."), ("2", "¶1: giant bespoke clusters and their upfront costs."), ("4", "¶1: more time ‘shuttling data around’.")])
P.rc(3, "V1", "Detail_Not_True", "3", "Easy",
 "Does DiLoCo get rid of checkpointing or just reduce it?",
 steps(("The line", ev(2, "Within an island, checkpointing proceeds as usual. Between islands, however, communications plummet") +
          p("Checkpointing still happens inside each island; Prime Intellect did it every 500 steps. It is cut, not eliminated."))) + final("Option 3"),
 "notrue", [("1", "Communication between islands drops five hundredfold."), ("2", "‘They often generalise better.’"), ("4", "Benefits for smaller outfits are ‘immediate’.")])
P.rc(4, "V1", "Tone", "4", "Medium",
 "The author reports benefits but keeps the hedges: ‘may not be urgent’, ‘if the tricky engineering can be mastered’.",
 steps(("Signals", p("Positive: DiLoCo cuts costs and complexity, generalises better, works across continents. Cautious: big labs may not need it yet; full decentralisation depends on hard engineering.")),
       ("Choosing", p("Hopeful but measured: option 4."))) + final("Option 4"),
 "inference", [("1", "‘Sceptical’ is too negative."), ("2", "‘Enthusiastic advocacy’ overstates; the author reports, with caveats."), ("3", "The passage does offer an alternative.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Detail", "3", "Medium",
 "What did the genetics show, and why does it point to wives staying put?",
 steps(("The line", ev(2, "Many of the Durotriges could be traced back to the same shared female ancestor, including an adult woman, her daughter, her granddaughters and potentially her great-grandson") +
          p("A maternal line unbroken over generations means daughters stayed in the community. That is the core evidence. The unrelated men support it, but only because the female line was continuous.")),
       ("Choosing", p("Option 3."))) + final("Option 3"),
 "detail", [("1", "‘All the mtDNA… females’ is wrong: men inherit mtDNA too, and not everyone shared it."), ("2", "Scholars are unsure the Romans actually observed this."), ("4", "Supporting evidence; on its own it doesn’t show matrilocality.")])
P.rc(6, "V2", "Inference_Except", "3", "Medium",
 "Watch the word in option 3.",
 steps(("The line", ev(3, "It’s still not clear exactly how prevalent matrilocal communities were in Iron Age Britain") +
          p("The question raised is about <i>matrilocal</i> communities. ‘Matriarchal’ means women rule, and the passage says men still usually held power.")),
       ("The others", p("New family structures in Europe (option 1), women’s support networks and influence (option 2), and mtDNA as evidence of maternal ancestry (option 4) all follow."))) + final("Option 3"),
 "except", [("1", "A pattern ‘never seen before in prehistoric Europe’."), ("2", "Women stayed with their families and had more influence."), ("4", "mtDNA ‘gets passed down from mothers to children’.")])
P.rc(7, "V2", "Weaken", "1", "Hard",
 "The interpretation rests on the women being related and the men not.",
 steps(("The logic", p("Most men lacked the shared maternal DNA, so they are taken to have married in. If most adult males were closely related through their mothers too, they would be local, and the sign of men moving in disappears.")),
       ("Choosing", p("Option 1 knocks out the key contrast."))) + final("Option 1"),
 "weaken", [("2", "Alternating customs still allow this community to be matrilocal."), ("3", "Grave goods and diet don’t speak to who moved."), ("4", "A short, homogeneous burial period doesn’t undo the kinship pattern.")])
P.rc(8, "V2", "Purpose", "4", "Medium",
 "Is the author using the Romans to prove something?",
 steps(("The line", ev(4, "But scholars are divided as to whether the Romans actually observed these women or were merely spinning cautionary tales") +
          p("The Roman accounts are brought in as outside, historical descriptions of British women, and the author flags that they may not be reliable.")),
       ("Choosing", p("Option 4 describes their role without claiming they prove anything."))) + final("Option 4"),
 "purpose", [("1", "Roman norms aren’t compared."), ("2", "They speak of power and husbands, not of who moved; and their reliability is in doubt."), ("3", "The author notes the doubt but doesn’t argue against the texts.")])

P.va(9, P.missing_html(9), P.Q["VARC"][9]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "‘Wetlands also play…’ adds roles beyond something already mentioned. Which blank follows a sentence saying there is more to them?",
 steps(("Find the hook", p("The paragraph ends: ‘Their vital role extends far beyond wildlife. ____4____.’ The new sentence names those other roles: floods, water, carbon.")),
       ("Match the label", p("Blank 4 is choice 1, labelled ‘Option 4’."))) + final("Choice 1 (“Option 4”)"),
 "missing", [("2", "“Option 2”: inside the discussion of definitions."), ("3", "“Option 3”: before ‘beyond wildlife’ has been said."), ("4", "“Option 1”: inside the history of the term.")])

# ---------------- Passage 3 (Q10–13) ----------------
P.rc(10, "V3", "Main_Idea", "1", "Medium",
 "Paragraph 1 lists reasons managers are better equipped, then turns on ‘But’.",
 steps(("The line", ev(1, "But as the pendulum swings inexorably away from gut instinct towards data-based decisions, firms need to be alive to a different set of dangers") +
          p("Firms now lean on data, yet there are new dangers. Option 1 has both halves.")),
       ("The others", p("Options 2 and 4 keep only the first half; option 3 isn’t said."))) + final("Option 1"),
 "inference", [("2", "Leaves out the warning."), ("3", "Nothing about closing off debate."), ("4", "Leaves out the dangers; ‘more accurate’ isn’t claimed.")])
P.rc(11, "V3", "Detail", "4", "Medium",
 "What happened in the promotion experiment when only one factor had a number?",
 steps(("The finding", ev(2, "When only promotion likelihood was given a numerical value, participants tended to prioritize it in their decision") +
          p("Putting a number on something gives it extra weight, even when an unquantified factor matters as much.")),
       ("Choosing", p("Option 4."))) + final("Option 4"),
 "detail", [("1", "Reversed: the risk is overlooking what isn’t measured."), ("2", "The authors don’t prescribe gut instinct."), ("3", "They say quantifying everything isn’t possible; some things are ‘mushier’.")])
P.rc(12, "V3", "Inference_Except", "3", "Medium",
 "Does the passage treat algorithms as infallible?",
 steps(("The context", p("Managers were blamed for ignoring machines when things went wrong but got no credit when they were right. So following the algorithm protects you (options 1 and 4), and the HBO example shows it can stifle bold choices (option 2).")),
       ("The odd one", ev(4, "Numbers promise rigour, certainty and objectivity. They have flaws, too") +
          p("Calling algorithms infallible contradicts the passage."))) + final("Option 3"),
 "except", [("1", "Following the machine shields you from blame."), ("2", "Data-driven choices might have killed HBO’s bold shows."), ("4", "The social pressure the phrase describes.")])
P.rc(13, "V3", "Application", "1", "Easy",
 "What did HBO’s executives do with unconventional shows?",
 steps(("The line", ev(3, "Early HBO executives used instinct and contrarianism to commission shows that broke the mould") +
          p("For a novel script, existing data says little; instinct and contrarian judgment are the author’s answer."))) + final("Option 1"),
 "inference", [("2", "The HBO shows succeeded; ‘less profitable’ isn’t implied."), ("3", "Past patterns can’t judge radically new ideas."), ("4", "The opposite of the HBO lesson.")])

P.va(14, P.missing_html(14), P.Q["VARC"][14]["opts"], "MCQ", "1", "Missing_Sentence", "Hard",
 "‘This ongoing inquiry’ needs a description of philosophers questioning further and further just before it.",
 steps(("Find the hook", p("Before blank 2, philosophers reflect and find that many certainties are questionable. ‘This ongoing inquiry’ names that process, and the sentence explains why it marks out philosophy. The paragraph then explains where ‘these doubts’ come from.")),
       ("Match the label", p("Blank 2 is choice 1, labelled ‘Option 2’."))) + final("Choice 1 (“Option 2”)"),
 "missing", [("2", "“Option 1”: at the very start, ‘this inquiry’ has nothing to refer to."), ("3", "“Option 3”: the case for studying knowledge is already concluding."), ("4", "“Option 4”: after the closing sentence.")])
P.va(15, P.sent_html(15), [], "TITA", "3", "Odd_One_Out", "Medium",
 "Four sentences are about economic change and his character. One brings in social policy.",
 steps(("The chain", p("1 → 4 → 5 → 2: he drove economic reforms (1); India went from poor and slow to a rising power (4); his tenure cemented that reputation (5); his manner made him a global statesman (2).")),
       ("The odd one", p("Sentence 3, on education and healthcare drawing bipartisan praise, shifts away from the economic transformation and nothing picks it up."))) + final("3"),
 "oddone", [("1", "Introduces him and the reforms."), ("4", "The result of the reforms."), ("5", "“His tenure”: the legacy."), ("2", "His manner and standing.")], why_title="How the other sentences fit")
P.va(16, P.summary_html(16, "Philosophers examine the nature"), P.Q["VARC"][16]["opts"], "MCQ", "3", "Summary", "Medium",
 "Four reasons: science, philosophical issues (counterfactuals, explanation), induction, and the puzzle of accidental truths.",
 steps(("Choosing", p("Option 3 keeps all four reasons in their own terms, including the puzzle of telling laws from accidental truths."))) + final("Option 3"),
 "summary", [("1", "Leaves out counterfactuals, explanation and induction."), ("2", "Leaves out counterfactuals; ‘generalisations and true laws’ blurs the puzzle (both are true generalisations)."), ("4", "Leaves out counterfactuals and the specific puzzle.")])

# ---------------- Passage 4 (Q17–20) ----------------
P.rc(17, "V4", "Purpose", "2", "Medium",
 "Follow the order: theme-park tourism, then ‘a deeper political agenda’, then erasure.",
 steps(("The line", ev(3, "Beijing’s immense tourism investments mask a deeper political agenda") +
          p("The author first shows the tourist face, then what it hides: land, language and culture under pressure.")),
       ("Choosing", p("Option 2."))) + final("Option 2"),
 "purpose", [("1", "Cultural exchange isn’t the point; the passage argues the opposite."), ("3", "Details, not the organising idea."), ("4", "Resentment is one later strand.")])
P.rc(18, "V4", "Detail", "2", "Medium",
 "What was the new name modelled on?",
 steps(("The line", ev(1, "a Tibetan border region renamed after the 1933 novel Lost Horizon, which idealized Tibet as a timeless utopia") +
          p("The renaming tied the town to an imagined utopia as part of a tourism model."))) + final("Option 2"),
 "detail", [("1", "The novel idealised; it wasn’t historical or cultural significance."), ("3", "Nearly all tourists are Chinese; foreign entry is restricted."), ("4", "The political agenda comes later in the passage; the name itself follows the tourism model.")])
P.rc(19, "V4", "Application", "2", "Medium",
 "What does the author object to most?",
 steps(("The concern", p("Erasure of Tibetan identity and repression: resettlement, Chinese boarding schools, arrests of cultural advocates, checkpoints.")),
       ("Choosing", p("Less surveillance and more freedom for cultural advocates address that directly."))) + final("Option 2"),
 "inference", [("1", "More tourism deepens the problem."), ("3", "Government-led tourism ‘preservation’ is what the author distrusts."), ("4", "Restricting access doesn’t touch the repression.")])
P.rc(20, "V4", "Tone", "4", "Hard",
 "Is the waitress only talking about the costumes?",
 steps(("Reading it", p("The remark is the passage’s last line, after paragraphs on Tibet turned into a theme park. Pointing at tourists dressed up as Tibetans, she judges the whole business of selling a costume version of her culture.")),
       ("Choosing", p("The costumes stand for the larger commodification: a figurative use, as option 4 says."))) + final("Option 4"),
 "inference", [("1", "Not only about looks."), ("2", "Not an exaggeration; a pointed judgment."), ("3", "She isn’t being ironic; she means it, and the target is wider than the tourists.")])

P.va(21, P.summary_html(21, "Liberal nationalists see"), P.Q["VARC"][21]["opts"], "MCQ", "3", "Summary", "Medium",
 "Three ideas: the two outlooks go together, some trade-off is needed, and national identity builds solidarity for social justice.",
 steps(("Choosing", p("Option 3 states the claim, the trade-off and the solidarity argument, without pinning it all on Tamir."))) + final("Option 3"),
 "summary", [("1", "Pins it all on Tamir and omits the compatibility claim."), ("2", "Leaves out the trade-off."), ("4", "Turns the trade-off into a balance and drops social justice.")])
P.va(22, P.summary_html(22, "Evolutionary game theory began"), P.Q["VARC"][22]["opts"], "MCQ", "2", "Summary", "Hard",
 "Origin in biology; then three reasons social scientists took it up.",
 steps(("Choosing", p("Option 2 has the biological origin and the three reasons: cultural evolution, better rationality assumptions, and its dynamic character."))) + final("Option 2"),
 "summary", [("1", "Leaves out why social scientists adopted it."), ("3", "Only the third reason."), ("4", "Leaves out the more suitable rationality assumptions as a reason and the biological origin is an afterthought.")])
P.va(23, P.missing_html(23), P.Q["VARC"][23]["opts"], "MCQ", "3", "Missing_Sentence", "Easy",
 "The sentence explains what the design was for. It belongs right after the design is described.",
 steps(("Find the spot", p("Before blank 1: a conga drum tuned by a single crank instead of many screws. The new sentence gives its purpose; the patents follow.")),
       ("Match the label", p("Blank 1 is choice 3, labelled ‘Option 1’."))) + final("Choice 3 (“Option 1”)"),
 "missing", [("1", "“Option 3”: after the drummer’s verdict, too late."), ("2", "“Option 2”: after his death."), ("4", "“Option 4”: after the closing remark.")])
P.va(24, P.sent_html(24), [], "TITA", "4", "Odd_One_Out", "Medium",
 "Two sentences on universal humanism and two on Ukraine fit together. One is a general historical claim.",
 steps(("The chain", p("1 → 3 → 2 → 5: humanists oppose banning enemy art (1); they think art transcends politics (3); but chauvinism can be resistance, as in Ukraine (2); there, rejecting Russian culture asserts independence (5).")),
       ("The odd one", p("Sentence 4 states how such bans have historically been viewed, a general observation the paragraph’s contrast doesn’t need."))) + final("4"),
 "oddone", [("1", "The humanist objection."), ("3", "Its basis."), ("2", "The counter-case."), ("5", "Ukraine in detail.")], why_title="How the other sentences fit")
