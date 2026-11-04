# -*- coding: utf-8 -*-
# Batch 3 — CAT 2023 Slot 2: VARC (Q1–24). DILR and QA are added by b3_s2_dilr.py and b3_s2_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

PAPER = Paper(2023, 2, "ex3_s2.json")
P = PAPER
P.passage("P1", "Passage 1 — What is a historical fact?", "Social_Science_and_History")
P.passage("P2", "Passage 2 — Netflix and the language of Europe", "Economics_and_Management")
P.passage("P3", "Passage 3 — Has liberalism failed?", "Politics")
P.passage("P4", "Passage 4 — Is second-hand fashion really green?", "Environment_and_Life_Science")

# ---------------- Passage 1 ----------------
P.rc(1, "P1", "Application", "2", "Medium",
 "The author says accuracy about dates and places is necessary but not the historian’s ‘essential function’. What is?",
 steps(("Find the author’s view", ev(3, "The facts speak only when the historian calls on them … The historian is necessarily selective.") +
          p("For this author, the historian’s job is <b>interpretation</b>: choosing facts and explaining their significance, not just listing them.")),
       ("Apply it to Hastings", p("A book in that spirit would ask <i>why</i> the battle mattered, i.e. the social, political and economic forces around it."))) +
 final("Option 2.") + trap("Options 3 and 4 describe exactly the “necessary condition” work the author says is not the historian’s essential function."),
 "inference",
 [("1", "The auxiliary sciences serve accuracy, not interpretation, so “nuanced interpretation by relying on” them is a contradiction."),
  ("3", "A timeline is a list of basic facts: necessary, but not the focus."), ("4", "Deriving facts from documents is the common-sense view the author rejects.")])

P.rc(2, "P1", "Detail", "2", "Easy",
 "Find where archaeology is named. What kind of matters does the historian rely on it for?",
 steps(("Locate archaeology", ev(2, "It is precisely for matters of this kind that the historian is entitled to rely on what have been called the “auxiliary sciences” of history—archaeology, epigraphy, numismatics, chronology")),
       ("“Matters of this kind”", p("These are getting dates and places <b>right</b>: factual accuracy, which is a necessary condition, not the historian’s main job."))) + final("Option 2."),
 "detail",
 [("1", "Locating the oldest civilisations isn’t mentioned."), ("3", "Interpretation is the historian’s own work, not the auxiliary sciences’."),
  ("4", "Accuracy is explicitly <i>not</i> the historian’s “essential function”.")])

P.rc(3, "P1", "Weaken_Except", "2", "Medium",
 "The claim is that facts need a historian to select and order them. Three options say facts are objective and independent. One doesn’t.",
 steps(("State the claim", ev(3, "It used to be said that facts speak for themselves. This is, of course, untrue. The facts speak only when the historian calls on them")),
       ("Sort the options", p("Options 1, 3 and 4 each say facts carry meaning on their own (objective, order-independent, historian-independent), so they <b>weaken</b> the claim. Option 2 says facts are relative to the person, which <b>supports</b> it."))) +
 final("Option 2."), "weaken",
 [("1", "Weakens: “objective and universal, irrespective of context” means facts do speak for themselves."),
  ("3", "Weakens: the author says the historian decides “in what order or context” facts appear."),
  ("4", "Weakens: truth independent of the historian contradicts the author’s view.")])

P.rc(4, "P1", "Except", "4", "Medium",
 "Which option is Parsons’s description, which the author borrows to make his own point?",
 steps(("The common-sense view", ev(1, "History consists of a corpus of ascertained facts. The facts are available to the historian in documents, inscriptions, and so on") +
          p("Positivist, fact-first and science-like: that matches options 1, 2 and 3.")),
       ("The odd one", p("“A selective system of cognitive orientations to reality” is Parsons’s phrase. The author uses it to argue that history is <b>selective</b>, which is the opposite of the common-sense view."))) +
 final("Option 4."), "except",
 [("1", "Matches the positivists’ “cult of facts”."), ("2", "Matches the positivists’ claim for history as a science built on facts."),
  ("3", "Matches “documents, inscriptions”.")])

# ---------------- Passage 2 ----------------
P.rc(5, "P2", "Application", "4", "Easy",
 "Which genre does the passage say travels best across borders?",
 steps(("Find the clue", ev(1, "Not everything works across borders. Comedy sometimes struggles. Whodunits and bloodthirsty maelstroms … have a more universal appeal.")),
       ("Apply it", p("A murder mystery is a whodunit."))) + final("Option 4."),
 "inference",
 [("1", "The passage gives no evidence about romantic dramas."), ("2", "“Comedy sometimes struggles.”"), ("3", "“German television is not always built for export.”")])

P.rc(6, "P2", "Main_Idea", "4", "Easy",
 "Read the last paragraph: “They should not be [nervous].” Why not?",
 steps(("Find the author’s stance", ev(3, "Now Netflix and friends pump the same content into homes across a continent, making culture a cross-border endeavour, too.")),
       ("Name it", p("Shared viewing gives Europeans “something in common”: Netflix is a <b>unifying force</b>."))) + final("Option 4.") +
 trap("Option 2 is the politicians’ fear, which the author reports and then rejects."),
 "inference",
 [("1", "No economic threat is argued."), ("2", "That’s the European executives’ view; the author says “They should not be” nervous."),
  ("3", "No “entertainment gap” is mentioned.")])

P.rc(7, "P2", "Detail_Not_True", "2", "Medium",
 "Where do the big decisions at Netflix get made?",
 steps(("Check option 2", ev(2, "Now Netflix has offices across Europe. But ultimately the big decisions rest with American executives.") +
          p("So Netflix has <b>not</b> become a truly European entity."))) + final("Option 2."),
 "notrue",
 [("1", "True: national broadcasters still dominate; streaming is about a third of viewing hours."),
  ("3", "True in substance: about half of Netflix’s original content is now American (down from 75%)."),
  ("4", "True: shows such as “Lupin” can become global hits.")])

P.rc(8, "P2", "Weaken", "1", "Medium",
 "The conclusion is that shared Netflix content gives Europeans something in common. What would show the content isn’t shared?",
 steps(("The conclusion", ev(3, "If Europeans are to … share vaccines in a pandemic, then they need to have something in common—even if it is just bingeing on the same series.")),
       ("Attack it", p("If popularity varies widely between countries, Europeans <b>aren’t</b> watching the same shows, so the common ground disappears."))) + final("Option 1."),
 "weaken",
 [("2", "Differences between age groups don’t touch the cross-border claim."), ("3", "Popularity in North America is irrelevant to European unity."),
  ("4", "Losing share to other streamers could still leave Europeans watching common content.")])

# ---------------- Passage 3 ----------------
P.rc(9, "P3", "Inference", "4", "Medium",
 "The reviewer’s main counter to Deneen is that liberalism can reform itself. Which option says that?",
 steps(("The reviewer’s position", ev(3, "Rather than dying, liberalism reformed itself.")),
       ("Match", p("Option 4, dominant in the past but having to reform itself to stay so, is exactly the reviewer’s historical point."))) + final("Option 4: the one statement he would agree with."),
 "inference",
 [("1", "He rejects the idea that liberalism is dying."), ("2", "That is Deneen’s “essence” claim, which the reviewer disputes."),
  ("3", "He calls the recent record “dismal”, so he doesn’t think the claims are simply exaggerated.")])

P.rc(10, "P3", "Except", "1", "Hard",
 "Three quotes describe failures of liberal society itself. One describes what technology does to work.",
 steps(("Sort the quotes", p("A business aristocracy and vast companies (problems “reappearing today”), democracy as theatre of the absurd, and the gap between liberalism’s claims and reality are all presented as signs of liberalism failing.")),
       ("The odd one", p("Technology turning work into drudgery is a general economic change. The passage doesn’t present it as evidence that <b>liberalism</b> is declining."))) +
 final("Option 1.") + trap("Option 2 is quoted from the 19th-century example, but the reviewer says those problems are “reappearing today”."),
 "except",
 [("2", "Presented as problems “reappearing today”."), ("3", "Deneen’s evidence of democratic decay."), ("4", "Deneen’s core claim that liberalism’s promises have failed.")])

P.rc(11, "P3", "Purpose", "3", "Medium",
 "What’s ironic about 1,000 private jets flying in to discuss a “shared future”?",
 steps(("Find the references", ev(1, "the vision of 1,000 private planes whisking their occupants to Davos to discuss the question of “creating a shared future in a fragmented world”") +
          ev(4, "The biggest enemy of liberalism is not so much atomisation but old-fashioned greed, as members of the Davos elite pile their plates ever higher")),
       ("Name the point", p("The rich preach liberal ideals while grabbing more for themselves: <b>hypocrisy</b>."))) + final("Option 3."),
 "purpose",
 [("1", "The reviewer doesn’t predict whether liberalism can return."), ("2", "The jets mock the “shared future” talk; they aren’t evidence of growing interest."),
  ("4", "Insulation from hardship isn’t the point; greed is.")])

P.rc(12, "P3", "Except", "2", "Medium",
 "One option is something the reviewer actually <i>agrees</i> with Deneen about.",
 steps(("The reviewer’s agreement", ev(4, "He is also right to assert that the world has much to learn from the premodern notions of liberty as self-mastery and self-denial.")),
       ("The faults he finds", p("A narrow definition (option 3), ignoring liberalism’s self-reform (option 4), and treating its failure as final (option 1)."))) + final("Option 2."),
 "except",
 [("1", "Faulted: “not as a funeral oration but as a call to action”."), ("3", "Faulted: liberalism “contains a wide range of intellectual traditions”."),
  ("4", "Faulted: “his failure to recognise liberalism’s ability to reform itself”.")])

# ---------------- Passage 4 ----------------
P.rc(13, "P4", "Inference", "3", "Easy",
 "What does the author advise second-hand shoppers to buy?",
 steps(("Find the advice", ev(5, "[They would be well advised to buy] high-quality items that shed less and last longer")),
       ("Infer", p("The opposite of disposable fast fashion is clothing that is <b>high quality and long lasting</b>."))) + final("Option 3."),
 "inference",
 [("1", "Even good clothes shed <i>some</i> microfibres; the passage says “shed less”."), ("2", "Vintage clothes can be old and shed more."),
  ("4", "Toxins come from landfill, not from how clothes are made.")])

P.rc(14, "P4", "Except", "1", "Easy",
 "Is it true that Britons don’t buy second-hand at all?",
 steps(("Check option 1", ev(3, "“Thrifting” has increasingly become a trendy practice. London is home to many second-hand … shops") +
          p("So the British <b>do</b> buy second-hand clothing. The ThredUP problem is luxury brands and a generation used to buying new."))) + final("Option 1."),
 "except",
 [("2", "Reason given: brands don’t want stock “sold at a cheaper price”."), ("3", "Reason given: they “would rather put brand before sustainability”."),
  ("4", "Reason given: unless recycling “becomes cost-effective”.")])

P.rc(15, "P4", "Inference", "2", "Medium",
 "Thrifting is done to help the planet. What does the Patagonia study say older clothes do?",
 steps(("The intention", p("People thrift to cut waste and help the planet.")),
       ("The result", ev(5, "older clothes shed more microfibres. These can end up in our rivers and seas after just one wash") +
          p("The green choice creates a new environmental problem: that is the irony."))) + final("Option 2."),
 "inference",
 [("1", "Cheap luxury isn’t ironic, and it isn’t the passage’s point."), ("3", "The passage doesn’t frame thrifting as anti-consumerist."),
  ("4", "Retailer cost-effectiveness concerns luxury resale, not thrifting’s irony.")])

P.rc(16, "P4", "Weaken", "2", "Hard",
 "The central worry is that worn second-hand clothes shed microfibres. What would make that worry vanish?",
 steps(("The central idea", p("Second-hand shopping isn’t automatically green, because older, worn clothes shed more microfibres. Buy high quality.")),
       ("Undermine it", p("If second-hand stores sold <b>only high-quality</b> clothes, the microfibre problem largely disappears and thrifting becomes simply good."))) + final("Option 2."),
 "weaken",
 [("1", "Buying online doesn’t change microfibre shedding."), ("3", "Recycling fast fashion into vintage stores would add more worn clothes, not fewer."),
  ("4", "Landfill burning is background; the central point is microfibres from second-hand clothes.")])

# ---------------- VA ----------------
P.va(17, P.missing_html(17), P.strict_opts(17), "MCQ", "2", "Missing_Sentence", "Medium",
 "“And probably much earlier” needs a date just before it. Which gap follows a date?",
 steps(("Find the hook", p("“And probably much earlier, moving the documentation for kissing back 1,000 years” must follow a sentence that gives a date. Gap (2) follows “kissing was already a well-established practice <b>4,500 years ago</b>”.")),
       ("Check the arithmetic", p("Earlier research said 3,500 years (South Asia); 4,500 years is exactly 1,000 years earlier.")),
       ("Match the label", p("Gap (2) is choice 2, labelled “Option 2”."))) + final("Choice 2."),
 "missing",
 [("1", "“Option 4”: placed after the clay tablets, “much earlier” has no date to refer to."), ("3", "“Option 3”: placed after “cuneiform script”, there’s no date before it."),
  ("4", "“Option 1”: placed after “3,500 years ago”, “1,000 years” back would contradict the new 4,500-year finding.")])

P.va(18, P.missing_html(18), P.strict_opts(18), "MCQ", "2", "Missing_Sentence", "Medium",
 "The sentence contrasts developing and developed countries. Where is that contrast first set up and then questioned?",
 steps(("Find the hook", p("After gap (2): “While <b>this distinction between developing and advanced economies</b> may have made some sense in the 1950s…”. That needs a sentence that draws the distinction.")),
       ("Check the fit", p("Before gap (2), dualism is defined for poor countries. The new sentence extends it into a contrast with developed countries."))) + final("Choice 2 (“Option 2”)."),
 "missing",
 [("1", "Gap (1) comes before dualism has even been defined."), ("3", "Gap (3) is inside the “widening gap” discussion, after the distinction has been dismissed."),
  ("4", "Gap (4) comes after the point that rich countries now face the same problem.")])

P.va(19, P.sent_html(19), [], "TITA", "3", "Odd_One_Out", "Medium",
 "Four sentences define latchkey children and report findings. One adds a research caveat.",
 steps(("Chain", p("<b>2 → 4 → 5 → 1</b>: define latchkey children (2), the newer term “self-care” (4), parents think it helps but research says otherwise (5), the specific negative outcomes (1).")),
       ("Odd one", p("Sentence 3 adds a caveat about long-term research. It interrupts the finding-to-evidence flow and has no clear place."))) + final("3"),
 "oddone",
 [("2", "Opens with the definition."), ("4", "The renamed term."), ("5", "Belief versus research."), ("1", "The specific negative outcomes.")],
 why_title="How the other sentences fit")

P.va(20, P.sent_html(20), [], "TITA", "2", "Odd_One_Out", "Medium",
 "Four sentences report book-banning facts in the US. One is an opinion about authors.",
 steps(("Chain", p("<b>3 → 5 → 4 → 1</b>: banning has escalated (3), the 2022 figures (5), Northern Lights as an example (4), what that ban foreshadows (1).")),
       ("Odd one", p("Sentence 2 is a general opinion about silencing brave authors. It breaks the factual, US-specific thread."))) + final("2"),
 "oddone",
 [("3", "Opens: an unprecedented escalation."), ("5", "The numbers that support it."), ("4", "A concrete example."), ("1", "The example’s significance.")],
 why_title="How the other sentences fit")

P.va(21, P.sent_html(21), [], "TITA", "4132", "Para_Jumble", "Medium",
 "Start with the definition of consciousness as emergent; the ant analogy comes next.",
 steps(("Opener", p("Sentence 4 introduces the idea: consciousness is an <b>emergent property</b>.")),
       ("Analogy, then contrast", p("Sentence 1: like ants, no single neuron holds complex information. Sentence 3: “<b>Nonetheless</b>, the sum of all neurons” generates emotions.")),
       ("Close", p("Sentence 2 generalises: the mechanism isn’t understood, but interconnections give rise to qualities of the whole."))) + final("4132"),
 "pj",
 [("4123", "Sentence 2’s general conclusion would interrupt the 1 → 3 contrast (“no single neuron… Nonetheless, the sum…”)."),
  ("4312", "“Nonetheless” (3) needs the single-neuron point (1) before it.")], why_title="Why not another order")

P.va(22, P.sent_html(22), [], "TITA", "4312", "Para_Jumble", "Hard",
 "Sentence 1 names the novel; sentence 2 names its author. Which must come first?",
 steps(("Opener", p("Sentence 4 states the Western denial of African tradition.")),
       ("Rebuttal", p("Sentence 3, “<b>However</b>, their views contradict the reality”, answers it.")),
       ("Example, then author", p("Sentence 1 introduces <i>The Bottled Leopard</i> as voicing “this theme”. Sentence 2 then names Chukwuemeka Ike and how he treats the conflict."))) + final("4312"),
 "pj",
 [("4321", "Sentence 2 refers to the conflict through the author before sentence 1 has introduced his novel."),
  ("3412", "“However” (3) can’t open the paragraph.")], why_title="Why not another order")

P.va(23, P.summary_html(23, "Heatwaves are becoming"), P.Q["VARC"][23]["opts"], "MCQ", "3", "Summary", "Medium",
 "The passage moves from the danger of heatwaves to why the media’s framing matters.",
 steps(("Points", "<ol><li>Heatwaves are worsening; some groups are especially vulnerable.</li><li>Even vulnerable people don’t see themselves at risk, so warnings fail.</li><li>The news media play a central role in warning people.</li></ol>"),
       ("Pick", p("Option 3 keeps the risk and the media’s pivotal role."))) + final("Option 3."),
 "summary",
 [("1", "Leaves out the media, the passage’s conclusion."), ("2", "Says news stories “have to become more effective”, which goes beyond the text."),
  ("4", "Blames reports and policies; the passage blames how people perceive risk.")])

P.va(24, P.summary_html(24, "People spontaneously create"), P.Q["VARC"][24]["opts"], "MCQ", "1", "Summary", "Medium",
 "The passage lists many reasons people create counterfactuals, then says the ability develops through childhood.",
 steps(("Points", "<ol><li>People create counterfactuals for many reasons (explaining, preparing, emotions, morality).</li><li>The ability develops through childhood.</li></ol>"),
       ("Pick", p("Option 1 keeps both: “a variety of reasons” and “part of one’s developmental process”."))) + final("Option 1."),
 "summary",
 [("2", "Picks one minor use (others’ beliefs) as if it were central."), ("3", "Covers only future planning."),
  ("4", "“Reverse past and future actions” misstates the idea.")])
