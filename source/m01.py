# -*- coding: utf-8 -*-
# Simp Mock 1: VARC (24 of 24). DILR and QA: m01_dilr.py, m01_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(1, "sm01.json")
P.passage("V1", "Passage 1 — Friendships across class", "Social_Science_and_History")
P.passage("V2", "Passage 2 — Fire’s hidden costs", "Science_and_Technology")
P.passage("V3", "Passage 3 — Store brands", "Economics_and_Management")
P.passage("V4", "Passage 4 — The faded yellow rose", "Arts_and_Literature")

# ---------------- Passage 1: Social capital (Q1–4) ----------------
P.rc(1, "V1", "Main_Idea", "3", "Medium",
 "The passage opens with Putnam’s claim and ends with ‘the imperative for integration’. What ties the two together?",
 steps(("The frame", ev(1, "detailing a steady erosion in the amount of social interaction among people who are not family, close friends or work colleagues") +
          p("Putnam’s worry is that Americans interact less and that this hurts society. The new study ‘strikes a blow in favour of’ that view: the right kind of social ties (across classes) improve schooling, earnings and more.")),
       ("Choosing", p("Option 3 is the thread that runs from the first paragraph to the last: less social interaction, worse outcomes. The other options are each one piece of the passage."))) +
 final("Option 3"),
 "inference",
 [("1", "The Facebook data is the evidence, not the idea it supports."), ("2", "The study finds civic engagement is <i>not</i> linked to better outcomes."),
  ("4", "The closing remarks only, not the passage as a whole.")])

P.rc(2, "V1", "Except", "4", "Medium",
 "Negate each option. Three negations agree with the passage; one does not.",
 steps(("How to read the question", p("“If false, in accordance with the passage” means: the opposite of the option is what the passage says. So three options contradict the passage as written. The answer is the one that already agrees with it.")),
       ("Negating", "<ol><li>Option 1, negated: social capital <i>is</i> important. The passage agrees.</li><li>Option 2, negated: Facebook data <i>can</i> measure it in fine detail. Agrees.</li><li>Option 3, negated: economic connectedness <i>is</i> linked to good outcomes. Agrees.</li><li>Option 4, negated: civic engagement and in-class bonds <i>do</i> improve outcomes. The passage says the opposite.</li></ol>"),
       ("The line", ev(5, "Other classical definitions of social capital such as the extent of civic engagement and the cohesiveness of bonds within social classes did not appear to be correlated with improved life outcomes"))) +
 final("Option 4"),
 "except",
 [("1", "False as written; its opposite matches the passage."), ("2", "The passage says the data allowed a ‘much finer-grained’ estimate."), ("3", "Paragraph 3 links economic connectedness to better outcomes.")])

P.rc(3, "V1", "Inference", "4", "Medium",
 "Paragraph 3 reports a finding. What does the finding argue for?",
 steps(("The paragraph", ev(3, "“economic connectedness”—the extent of friendships across social classes—was strongly associated with increased rates of high-school completion, reduced rates of teenage pregnancy and increased income for those born poorer") +
          p("Friendships across classes go with better lives for poorer children. That is an argument for social integration.")),
       ("Choosing", p("Option 4 states the argument. The others misread details of the paragraph."))) +
 final("Option 4"),
 "inference",
 [("1", "Erosion of interaction is Putnam’s theme in paragraph 1, not this paragraph’s."), ("2", "These are the outcomes, not markers of social capital."),
  ("3", "The ‘moving’ example compares places; moving itself doesn’t raise connectedness.")])

P.rc(4, "V1", "Inference", "2", "Medium",
 "Watch for an option that turns ‘most easily’ into ‘most effective’.",
 steps(("The line", ev(4, "The most important institutions for encouraging these friendships seem to be colleges and universities") +
          ev(4, "The researchers also found that intra-class friendships were most easily struck up in religious settings") +
          p("Colleges matter most for cross-class friendships. Religious settings are where friendships <i>within</i> a class form easily, which is a different thing.")),
       ("Choosing", p("Option 2 calls religious settings the most effective for social capital. The passage gives that title to colleges."))) +
 final("Option 2"),
 "inference",
 [("1", "Last paragraph: hard to vary social capital experimentally."), ("3", "Putnam calls the withdrawal a symptom of anomie, a breakdown of social norms."),
  ("4", "Economic connectedness raised the incomes of those born poorer.")])

# ---------------- Passage 2: Fire (Q5–8) ----------------
P.rc(5, "V2", "Weaken", "4", "Hard",
 "The argument compares modern humans with Neanderthals. What does that comparison quietly assume?",
 steps(("The argument", p("Modern humans carry a mutation that lets them process smoke toxins; Neanderthals did not. The suggestion is that fire’s harm helped modern humans win out, because Neanderthals coped less well with smoke.")),
       ("The weak spot", p("This only works if Neanderthals were exposed to fire and suffered for it. If they were heavy fire users and thrived anyway, the mutation can’t be what set modern humans apart.")),
       ("Choosing", p("Option 4 says exactly that: Neanderthals used fire constantly and were very successful."))) +
 final("Option 4"),
 "weaken",
 [("1", "Disease among Neanderthals fits the story that fire’s harm mattered."), ("2", "Different lineages are compatible with the argument."),
  ("3", "Interbreeding says nothing about fire’s effects.")])

P.rc(6, "V2", "Weaken_Except", "2", "Medium",
 "Three options show fire’s <i>harm</i> shaping humans. One is about why fire was used.",
 steps(("Checking each", p("Option 1: resistance to smoke helped survival. Option 4: smoke shaped the respiratory system. Option 3: tools to control fire show early humans responding to its dangers.")),
       ("The odd one", p("Option 2 says what fire was mostly used for. Warmth or defence, it tells us nothing about fire’s harmful effects."))) +
 final("Option 2"),
 "except",
 [("1", "Smoke resistance improving survival is selection by fire’s harm."), ("3", "Tools to contain fire are a response to its danger."), ("4", "Smoke shaping a body system is fire’s harm shaping development.")])

P.rc(7, "V2", "Detail_Not_True", "1", "Medium",
 "The passage gives ‘at least 70,000 years ago’ for tuberculosis. What does it say about fire at that date?",
 steps(("The line", ev(5, "Many experts believe tuberculosis arose at least 70,000 years ago. By then, humans were most certainly controlling fire") +
          p("‘By then’ means fire was already in use before 70,000 years ago. The two did not arise at about the same time, and the dating comes from ‘many experts’, not the study.")),
       ("The others", p("Option 2 is Chisholm and Tanaka’s belief, option 3 is the model’s result, and option 4 is the last paragraph."))) +
 final("Option 1"),
 "notrue",
 [("2", "¶5: fire ‘might have helped spread other airborne diseases’."), ("3", "¶4: ‘Without fire, the probability was low’."), ("4", "¶6: smoking, climate change and patriarchy.")])

P.rc(8, "V2", "Weaken", "2", "Medium",
 "The model says fire made tuberculosis far more likely to emerge. What would show it emerged without human fire?",
 steps(("The prediction", ev(4, "Without fire, the probability was low. But when the researchers added fire to their model, the likelihood that tuberculosis would emerge jumped") +
          p("The model ties the emergence of TB to humans using fire.")),
       ("Choosing", p("If infectious TB already existed before modern humans and spread through soil or water, it emerged without human fire. Option 2 cuts against the model directly."))) +
 final("Option 2"),
 "weaken",
 [("1", "Genetic change over time doesn’t contradict the model’s prediction."), ("3", "Unknown other factors don’t undo the effect of fire."), ("4", "An interplay of factors can still include fire as the key one.")])

# ---------------- Passage 3: Private labels (Q9–12) ----------------
P.rc(9, "V3", "Inference_Except", "1", "Medium",
 "Do retailers make private-label goods themselves?",
 steps(("What the passage shows", p("Private labels are sold under the store’s own name (Kroger’s ‘house-brand products’), they appeal to shoppers after price and quality, and a team ‘develops’ them. Amazon’s partnerships are with goods ‘made by other companies’.")),
       ("The odd one", p("Nothing says retailers manufacture the goods themselves. Developing a product is not making it, so option 1 can’t be inferred."))) +
 final("Option 1"),
 "except",
 [("2", "Retailers develop the products; others make them."), ("3", "‘House-brand products’, sold under the store’s name."), ("4", "Shoppers who want low prices, high quality, or both.")])

P.rc(10, "V3", "Inference", "3", "Easy",
 "Half of millennials don’t mind whether a product is branded. Which kind of shopper is that?",
 steps(("The lines", ev(1, "informed, savvy consumers who are less loyal to specific brands and stores than to getting a good deal") +
          ev(2, "roughly half of Millennial shoppers said that they were indifferent to whether a product is brand-name or private-label") +
          p("The Gartner finding is offered as evidence of these ‘agnostic shoppers’."))) +
 final("Option 3"),
 "inference",
 [("1", "Kroger and Amazon are never compared as millennials’ choices."), ("2", "Indifferent to brand, not to price and quality."), ("4", "A good deal can be on price, quality or both; ‘equally’ isn’t said.")])

P.rc(11, "V3", "Detail", "3", "Easy",
 "Read the Amazon paragraph: who makes the exclusive products?",
 steps(("The line", ev(5, "goods that are made by other companies but can’t be purchased anywhere except on Amazon. Forming exclusive brand partnerships allows Amazon to add unique products and plug assortment gaps in high-demand categories") +
          p("Other companies make them, Amazon alone sells them, and the aim is to fill gaps."))) +
 final("Option 3"),
 "detail",
 [("1", "No discounts are mentioned."), ("2", "The point is that Amazon does <i>not</i> develop or manufacture them."), ("4", "Not reselling scarce goods; these are made only for Amazon.")])

P.rc(12, "V3", "Inference_Except", "3", "Easy",
 "The battery story is about trust. Which option says something the story doesn’t?",
 steps(("The story", p("Batteries priced 60% below the brand barely sold; at 25% below, sales rose about seven times. Shoppers read a very low price as a sign of poor quality.")),
       ("The odd one", p("Option 3 claims private labels are <i>always</i> as good as branded goods. The passage only says these batteries were comparable."))) +
 final("Option 3"),
 "except",
 [("1", "‘These are so cheap—I don’t trust them.’"), ("2", "The consultant searched for a price shoppers would trust."), ("4", "Comparable batteries sold badly at the lowest price.")])

# ---------------- Passage 4: The yellow rose (Q13–16) ----------------
P.rc(13, "V4", "Except", "3", "Medium",
 "Which substances are the cause, and which are the result?",
 steps(("The chain", p("Orpiment, the yellow pigment, degraded into two lead arsenates, schultenite and mimetite, which are ‘largely transparent’. Paragraph 1 says paint is degraded by light, humidity, temperature, solvents and incompatible pigments.")),
       ("The odd one", p("Schultenite and mimetite are the products of the breakdown. The passage never says they themselves are unstable."))) +
 final("Option 3"),
 "except",
 [("1", "Orpiment degraded."), ("2", "‘Reaction products that are largely transparent.’"), ("4", "Solvents and incompatible pigments in ¶1.")])

P.rc(14, "V4", "Detail", "3", "Medium",
 "What did the fluorescence map show that the eye can’t see?",
 steps(("The line", ev(3, "Their presence revealed painterly features—light and shadows defining the separate petals and stamens—that are optically invisible in the actual image") +
          p("The map showed how the rose originally looked. That is how it helped.")),
       ("Choosing", p("Option 2 describes what the technique does, not how it helped. Options 1 and 4 talk about restoring the painting, which nobody did."))) +
 final("Option 3"),
 "detail",
 [("1", "Nothing was restored."), ("2", "True, but it describes the technique, not what it gave the team."), ("4", "The painting itself was not changed.")])

P.rc(15, "V4", "Except", "4", "Medium",
 "The diffraction scan found <i>what</i> the orpiment turned into. Did it find <i>why</i>?",
 steps(("What the scan found", p("Lead arsenates explaining the colourless rose (option 1); the iron-rich ocher underpaint and goethite (option 3); together these reveal Mignon’s layered method (option 2).")),
       ("The odd one", p("The passage never says why the orpiment degraded."))) +
 final("Option 4"),
 "except",
 [("1", "Lead arsenates account for the colourless rose."), ("2", "The scan shows the underpaint, part of his multistep method."), ("3", "Orpiment, yellow ocher, goethite.")])

P.rc(16, "V4", "Purpose", "4", "Medium",
 "Read the end of paragraph 1. Why does the rose matter to the author?",
 steps(("The frame", ev(1, "By reconstructing how a painting deteriorated, conservators may be able to forestall further damage and better preserve it") +
          p("The rose is a worked example of that general point.")),
       ("Choosing", p("Options 1 and 3 describe the example; option 2 is about challenges and original appearance. Option 4 states the point the example serves."))) +
 final("Option 4"),
 "purpose",
 [("1", "Describes the case study, not why it is told."), ("2", "Original appearance is one step; the aim is preservation."), ("3", "The techniques are details within the example.")])

# ---------------- Verbal ability (Q17–24) ----------------
P.va(17, P.sent_html(17), [], "TITA", "4132", "Para_Jumble", "Easy",
 "Sentence 1 says ‘this issue’. Which sentence describes an issue?",
 steps(("The opener", p("Sentence 4 describes the problem: the Arctic’s albedo effect is being lost.")),
       ("The sequence", p("Sentence 1: ‘to address this issue’, a plan to make white clouds. Sentence 3: ‘this project’ could restabilise the Arctic. Sentence 2 closes: mitigation and adaptation aren’t enough for systems already broken."))) +
 final("4132"),
 "pj",
 [("4", "The problem."), ("1", "“This issue”: the proposed fix."), ("3", "“This project”."), ("2", "The broader conclusion.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.sent_html(18), [], "TITA", "1324", "Para_Jumble", "Easy",
 "‘Participants and observers’ appear in two sentences. Which one introduces them?",
 steps(("The opener", p("Sentence 1: the writer has spent a lifetime trying to understand the world.")),
       ("The sequence", p("Sentence 3: understanding will stay imperfect because we are both participants and observers. Sentence 2 defines the two aims. Sentence 4: ‘as a result’, the aims get in each other’s way."))) +
 final("1324"),
 "pj",
 [("1", "The writer’s life’s work."), ("3", "Introduces participants and observers."), ("2", "What each wants."), ("4", "“As a result”: the aims clash.")],
 why_title="Why each sentence goes where it does")

P.va(19, P.sent_html(19), [], "TITA", "3124", "Para_Jumble", "Medium",
 "Sentence 3 defines speculation and names two sides. In what order do the next sentences take them?",
 steps(("The opener", p("Sentence 3: speculation has both destructive and constructive potential.")),
       ("The sequence", p("Sentence 1: it can burst bubbles (destructive) but is also a necessary lubricant. Sentence 2 explains the lubricant role. Sentence 4: ‘however’, in a frenzy traders lose touch with fundamentals, contrasting with sentence 2."))) +
 final("3124"),
 "pj",
 [("3", "Defines speculation: two sides."), ("1", "Bubbles, but also a lubricant."), ("2", "How it helps the market."), ("4", "“However”: the frenzy.")],
 why_title="Why each sentence goes where it does")

P.va(20, P.missing_html(20), P.strict_opts(20), "MCQ", "1", "Missing_Sentence", "Easy",
 "The sentence gives everyday examples of AI. Where does the paragraph still need them?",
 steps(("Find the spot", p("Blank 1 comes right after AI is defined. Examples of where you meet it fit naturally there, before the paragraph moves on to how AI learns.")),
       ("Check the others", p("Blanks 2–4 sit in the middle of discussions of advantages and challenges, where a list of examples would break the thread."))) +
 final("Option 1"),
 "missing",
 [("2", "Between learning from data and analysing data: off topic."), ("3", "After ‘not without its challenges’, examples of uses don’t fit."), ("4", "After malicious uses, it would end on a neutral list.")])

P.va(21, P.missing_html(21), P.strict_opts(21), "MCQ", "3", "Missing_Sentence", "Easy",
 "The next sentence after the right blank must pick up ‘inequality’.",
 steps(("Find the hook", p("After blank 3: ‘This has led to renewed interest in policies that aim to reduce inequality’. ‘This’ needs a sentence about inequality just before it.")),
       ("Check the fit", p("The paragraph lists developments with ‘one’, ‘another’, ‘also’ and ‘finally’. ‘There is also’ fits as the third."))) +
 final("Option 3"),
 "missing",
 [("1", "Before the list has started."), ("2", "Inside the data-driven point."), ("4", "After the inequality policies, where ‘there is also’ comes too late.")])

P.va(22, P.summary_html(22, "Many scholars agree"), P.Q["VARC"][22]["opts"], "MCQ", "3", "Summary", "Medium",
 "Who says what? The scholars give three factors; the authors add a fourth.",
 steps(("What the passage says", "<ol><li>Scholars: meaning comes from coherence, purpose and existential mattering.</li><li>The authors add a fourth element, experiential appreciation: drawing value from experiences as they happen, which can change how people view their lives.</li></ol>"),
       ("Choosing", p("Option 3 keeps the three factors and the addition, without crediting the addition to the scholars."))) +
 final("Option 3"),
 "summary",
 [("1", "Credits all four to the scholars."), ("2", "‘Not as much on … as on’ ranks them; the passage doesn’t."), ("4", "Also says scholars agree on the fourth element.")])

P.va(23, P.summary_html(23, "The act of doomscrolling"), P.Q["VARC"][23]["opts"], "MCQ", "1", "Summary", "Easy",
 "The passage ends with ‘moderation is key’. Which summary keeps both the harm and the fix?",
 steps(("What the passage says", "<ol><li>Doomscrolling and social-media envy harm health more than thought: depression, anxiety, loneliness, self-harm, suicide.</li><li>It is hard to disconnect, especially as many get their news this way.</li><li>Moderation is key.</li></ol>"),
       ("Choosing", p("Option 1 has the difficulty, the need for moderation and the harms."))) +
 final("Option 1"),
 "summary",
 [("2", "Leaves out moderation."), ("3", "Narrows it to news readers and drops the harms."), ("4", "‘Majority’ distorts ‘one in five’.")])

P.va(24, P.summary_html(24, "Studies show that reading"), P.Q["VARC"][24]["opts"], "MCQ", "2", "Summary", "Easy",
 "The passage presents two camps. Does it pick one?",
 steps(("What the passage says", "<ol><li>Reading ability tracks vocabulary and spoken language more than age.</li><li>Many children, especially disadvantaged ones, start school behind.</li><li>Some want early formal reading teaching; others want immersion in language.</li></ol>"),
       ("Choosing", p("Option 2 reports the debate without taking a side."))) +
 final("Option 2"),
 "summary",
 [("1", "The debate is about teaching reading early, not training in spoken language."), ("3", "Picks immersion as best."), ("4", "Calls immersion ‘the only way’.")])
