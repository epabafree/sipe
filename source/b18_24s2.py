# -*- coding: utf-8 -*-
# Batch 18 — CAT 2024 Slot 2: VARC (Q1–24). DILR and QA are added by b18_24s2_dilr.py and b18_24s2_qa.py.
# Question numbers follow the order of the actual exam.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2024, 2, "ex18_24s2.json")
P.passage("P1", "Passage 1 — Why medieval Europe prized spices", "Social_Science_and_History")
P.passage("P2", "Passage 2 — Opening up peer review data", "Science_and_Technology")
P.passage("P3", "Passage 3 — Inventions and their unintended consequences", "Science_and_Technology")
P.passage("P4", "Passage 4 — What drives attacks by carnivores", "Environment_and_Life_Science")

P.va(1, P.summ(1), P.Q["VARC"][1]["opts"], "MCQ", "3", "Summary", "Easy",
 "The passage has a “but” and a “still”. A good summary keeps both the difficulty and the payoff.",
 steps(("What the passage says", "<ol><li>Important findings have come from physicists working with other scientists.</li><li>Their working cultures clash: physicists discard detail and rely on mathematical models.</li><li>Still, the collaborations are wanted and they pay off.</li></ol>"),
       ("Choosing", p("Option 3 keeps the differences in style and the important findings they still produce."))) +
 final("Option 3."),
 "summary",
 [("1", "The passage says the cultures are still out of sync; the differences haven’t been buried."),
  ("2", "Large data sets aren’t mentioned, and the summary drops the clash of cultures."),
  ("4", "It leaves out the differences, and biologists aren’t social scientists.")])

P.va(2, P.ms(2), ["Option 3", "Option 4", "Option 2", "Option 1"], "MCQ", "1", "Missing_Sentence", "Medium",
 "The sentence says Europeans didn’t invent globalization. Look for the line that says what they did instead.",
 steps(("The link", p("After blank (3) the paragraph says: “They changed and augmented what was already there since 1000.” “They” are the Europeans, and “changed and augmented” is the natural follow-up to “did not invent”: they built on something that already existed.")),
       ("What comes before", p("Just before blank (3), the paragraph contrasts 1000 with 1492. The missing sentence then turns to the Europeans’ role, and the next sentence explains it.")),
       ("Reading the options", p("Blank (3) is listed first, so the answer is option 1."))) +
 final("Blank (3), which is option 1."),
 "missing",
 [("2", "Blank (4) is after “They changed and augmented…”, so that “They” would have no clear subject."),
  ("3", "At blank (2) the paragraph is still describing the routes of the year 1000."),
  ("4", "At blank (1) the paragraph is about Southeast Asian suppliers; Europeans haven’t come up yet.")])

P.va(3, P.summ(3), P.Q["VARC"][3]["opts"], "MCQ", "4", "Summary", "Hard",
 "Check every claim in each option against the passage. Words like “primarily” and “domestic” are where options go wrong.",
 steps(("What the passage says", "<ol><li>States wage war with the DIME model, and information is usually the first target.</li><li>Governments routinely monitor telecom data and communication networks.</li><li>With social media, many governments now use cyber troops to manipulate public opinion online.</li></ol>"),
       ("Choosing", p("Option 4 keeps all three points without adding anything."))) +
 final("Option 4."),
 "summary",
 [("1", "The passage doesn’t say the DIME model is “primarily” used to deploy cyber troops."),
  ("2", "The passage says open data policies worry privacy advocates; it doesn’t say governments exploit them, or that the target is domestic opinion."),
  ("3", "The passage says information attacks come before military operations, not together with them.")])

# ---------------- Passage 1 ----------------
P.rc(4, "P1", "Application", "2", "Hard",
 "What did the snake story explain, and what couldn’t it explain?",
 steps(("The story", ev(6, "The only way to harvest pepper was to burn the trees, which would drive the snakes underground. Of course, this bit of lore would explain the shriveled black peppercorns, but not white, pink or other colors.")),
       ("White pepper arrives", p("The story explained black pepper by burning. White peppercorns don’t fit it, so a European seeing them would have reason to doubt the tale. The other outcomes don’t follow from one trader’s cargo."))) +
 final("Option 2."),
 "inference",
 [("1", "Medieval maps were vague and fanciful; one cargo of peppercorns wouldn’t make them navigational aids."),
  ("3", "A single trader’s goods wouldn’t change the supply, and so wouldn’t lower prices."),
  ("4", "White pepper from India would, if anything, look even more exotic.")])

P.rc(5, "P1", "Except", "1", "Hard",
 "The passage links demand for spices to their uses and to how people saw them. Which option ties to neither?",
 steps(("What gave spices their value", ev(4, "refrigeration was not available, and some hot spices have been shown to serve as an anti-bacterial agent") +
          ev(4, "throughout the Middle Ages spices were used as both medicines and condiments") +
          p("Spices served preservation, medicine and cooking. A change in any of these, such as refrigeration, a new system of medicine, or a different cuisine, would take away a reason to want them.")),
       ("Scarcity was a perception", ev(6, "Geographical knowledge has a lot to do with the perceptions of spices' relative scarcity and the reasons for their high prices.") +
          p("The passage ties scarcity and price to what Europeans imagined, not to how much was actually available. It gives no basis for saying greater supply made spices less alluring."))) +
 final("Option 1."),
 "except",
 [("2", "Spices helped where there was no refrigeration; refrigeration removes that need."),
  ("3", "Spices began as medicines; a change in medicine removes that use."),
  ("4", "Spices balanced the qualities of food in medieval recipes; a change in cuisine removes that use.")])

P.rc(6, "P1", "Inference", "2", "Medium",
 "The snake story is about harvesting and scarcity. Which conclusion has nothing to do with either?",
 steps(("What the story suggests", ev(6, "Europeans thought that pepper in India grew on trees \"guarded\" by serpents that would bite and poison anyone who attempted to gather the fruit.") +
          p("Listeners would conclude that gathering pepper is dangerous, so supply is short and the price is high. They might decide not to go themselves.")),
       ("The odd one", p("Nothing in the story touches on why pepper tastes hot. Snakes and burning say nothing about its flavour."))) +
 final("Option 2."),
 "inference",
 [("1", "Poisonous snakes are a good reason not to go harvesting yourself."),
  ("3", "A dangerous harvest justifies a high price."),
  ("4", "A harvest that needs burned trees and dodged snakes explains a limited supply.")])

P.rc(7, "P1", "Inference", "1", "Medium",
 "Look for an option that adds something the passage never says.",
 steps(("What the passage supports", ev(2, "Still, demand was great enough to inspire the voyages of Christopher Columbus and Vasco Da Gama, launching the first fateful wave of European colonialism.") +
          ev(7, "Spices never had the enduring allure or power of gold and silver or the commercial potential of new products such as tobacco, indigo or sugar.")),
       ("The unsupported one", p("The passage never says India was colonised, let alone for spices and gold. Gold is mentioned only as something with more lasting allure than spices."))) +
 final("Option 1."),
 "inference",
 [("2", "Spices lacked the “commercial potential” of tobacco, so tobacco was more marketable."),
  ("3", "Demand for spices inspired the voyages that launched colonialism."),
  ("4", "The same point: the desire for spices helped fuel colonial empires.")])

P.va(8, P.sents(8), [], "TITA", "4", "Odd_One_Out", "Medium",
 "Sentence 5 begins “It underscores”. What does “It” refer to?",
 steps(("The chain", p("Sentence 1 announces the approval of cultivated pet food in the UK. Sentence 5 (“It underscores…”) says what that approval shows. Sentence 3 notes that applications for human food are still being assessed, and sentence 2 says the government must invest to realise the benefits.")),
       ("The extra sentence", p("Sentence 4 is about what the previous government had been planning. It drifts from the current approval and doesn’t connect to the others."))) +
 final(r"\(4\)"),
 "oddone",
 [("1", "The news: approval of cultivated pet food."), ("5", "“It” refers to that approval."), ("3", "The next step: approval for humans."), ("2", "What the government must do.")],
 why_title="How the other sentences fit")

P.va(9, P.ms(9), ["Option 4", "Option 3", "Option 2", "Option 1"], "MCQ", "2", "Missing_Sentence", "Medium",
 "The sentence begins “Yet”. It needs a puzzle to set itself against, and it should come before the explanation.",
 steps(("The puzzle", p("Before blank (3), the paragraph says the hens kept pecking at mica, and that no trace of it stayed in their gizzards. The missing sentence adds the second half of the puzzle: “Yet” the hens laid eggs with calcium shells though the land had no limestone.")),
       ("The answer follows", p("After blank (3): “It took Kervran many years to establish that the chickens were transmuting one element into another.” That explains the calcium. So the sentence goes at blank (3), listed as option 2."))) +
 final("Blank (3), which is option 2."),
 "missing",
 [("1", "Blank (4) is after the explanation; the puzzle would arrive too late."),
  ("3", "Blank (2) comes before the mystery of the vanishing mica is described."),
  ("4", "Blank (1) comes before the paragraph has mentioned the mica.")])

# ---------------- Passage 2 ----------------
P.rc(10, "P2", "Except", "4", "Easy",
 "List the reasons the passage gives for reviewing, then find the one that isn’t there.",
 steps(("The reasons given", ev(1, "Some do it as a way to keep abreast with developments in their field; some simply see it as a duty to the discipline.") +
          ev(2, "some scientists have begun posting their reviews online, mainly to claim credit for their work")),
       ("The missing one", p("Expanding one’s influence in the academic community is never given as a reason."))) +
 final("Option 4."),
 "except",
 [("1", "Posting reviews online to claim credit is a way of publicising one’s review work."),
  ("2", "“A duty to the discipline” is a form of service."),
  ("3", "“To keep abreast with developments in their field”.")])

P.rc(11, "P2", "Inference", "1", "Easy",
 "Read the last paragraph. Which way does the author want the norm to shift?",
 steps(("The author’s position", ev(7, "But the norm should shift from opacity in all cases to opacity only when necessary.")),
       ("So", p("The author favours more transparency across peer review, while allowing exceptions."))) +
 final("Option 1."),
 "inference",
 [("2", "The author supports both, wherever possible; sharing data rather than reviews is offered only as a fallback."),
  ("3", "This is the opponents’ view, which the author answers."),
  ("4", "Screening reviewers for expertise isn’t discussed.")])

P.rc(12, "P2", "Detail_Not_True", "4", "Medium",
 "Find the benefits the author lists for sharing data: fraud, inefficiency, bias. Which option isn’t among them?",
 steps(("The benefits given", ev(3, "Sharing peer review data could help journals stamp out fraud, inefficiency, and systemic bias in academic publishing.") +
          ev(4, "Peer review data could also help root out bias.") +
          ev(4, "Openly publishing peer review data could perhaps also help journals address another problem in academic publishing: fraudulent peer reviews.")),
       ("The one not given", p("Choosing appropriately qualified reviewers is never mentioned."))) +
 final("Option 4."),
 "notrue",
 [("1", "Fraud and inefficiency are named directly."),
  ("2", "The eLife study showed women and non-Westerners were underrepresented."),
  ("3", "Authors posing as outside experts to review their own work is given as an example.")])

P.rc(13, "P2", "Except", "3", "Medium",
 "Read the opponents’ paragraph. One option turns their worry upside down.",
 steps(("The opponents’ worries", ev(5, "referees may be less critical of manuscripts if their reports are published") +
          ev(5, "open reviewing may deter referees from agreeing to judge manuscripts in the first place, or that they'll take longer to do so out of fear of scrutiny")),
       ("The odd one", p("Opponents fear that open review exposes reviewers to scrutiny. Option 3 says it leaves them unexposed, which is the opposite and certainly not a reason to oppose it."))) +
 final("Option 3."),
 "except",
 [("1", "Reviewers being less critical is the first worry."),
  ("2", "Reviewers taking longer out of fear of scrutiny."),
  ("4", "Reviewers being deterred from agreeing to review at all.")])

# ---------------- Passage 3 ----------------
P.rc(14, "P3", "Except", "3", "Hard",
 "Check each view against what the passage says about leaded fuel, carbon and CFCs.",
 steps(("Leaded fuel", ev(5, "Ethyl (leaded fuel) and Freon belonged to the same general class of secondary effect: innovations whose unintended consequences stem from some kind of waste by-product that they emit.") +
          p("The passage blames leaded fuel’s waste by-products for health threats. Carbon build-up is linked to the Industrial Revolution, not to leaded fuel.")),
       ("The others", p("The last paragraph says it is becoming easier for small groups to cause global effects; Ethyl’s dangers were visible in the 1920s, so they could have been addressed sooner; and the passage moves from benign early effects to climate change and CFCs."))) +
 final("Option 3."),
 "except",
 [("1", "“it becomes increasingly possible for individuals or small groups to create new scientific advances … setting off unintended consequences that reverberate on a global scale”."),
  ("2", "The health threats of Ethyl “were visible in the 1920s”, so the author would agree they should have been tackled earlier."),
  ("4", "The passage opens with innocuous or beneficial effects and ends with global threats.")])

P.rc(15, "P3", "Main_Idea", "1", "Medium",
 "The printing press leads to spectacles, lenses, telescopes and microscopes. What does that chain show?",
 steps(("The paragraph", ev(1, "The history of any major technological or industrial advance is inevitably shadowed by a less predictable history of unintended consequences and secondary effects") +
          p("The Gutenberg chain shows how effects ripple outwards, far beyond what the inventor intended, and only over time.")),
       ("Choosing", p("Option 1 captures that the full impact can’t be seen in the short run because the ripples spread so far."))) +
 final("Option 1."),
 "inference",
 [("2", "The paragraph doesn’t tell us how inventions should be judged."),
  ("3", "It says the effects are sometimes innocuous or beneficial, not that most were."),
  ("4", "Further inventions are one example of a secondary effect, not the measure of an invention.")])

P.rc(16, "P3", "Except", "3", "Medium",
 "An externality is an unintended effect. Which option describes what the inventor actually intended?",
 steps(("Carrier’s intention", ev(2, "the technology was primarily intended for industrial use: ensuring cool, dry air for factories that required low-humidity environments")),
       ("So", p("Cooling and drying factories was the purpose of air-conditioning, not a side effect. The externality was the migration it set off."))) +
 final("Option 3."),
 "except",
 [("1", "CFCs are given as a by-product threat, a secondary effect."),
  ("2", "Edison expected dictation; music recording was the unexpected use."),
  ("4", "The loom inspired by toys led on to programmable technology, an effect nobody intended.")])

P.rc(17, "P3", "Purpose", "1", "Medium",
 "Each inventor had one aim and saw another result. What do the three examples share?",
 steps(("The examples", p("Carrier wanted to cool factories and ended up reshaping where Americans live. Edison wanted a dictation machine and ended up with the music industry. Babbage’s computer grew out of toys.")),
       ("The point", p("None of them could have foreseen how their inventions would end up affecting society."))) +
 final("Option 1."),
 "purpose",
 [("2", "The passage makes no claim that these effects were mostly beneficial."),
  ("3", "“Typically” and “entirely different” overstate it; the examples show unforeseen effects, not a rule."),
  ("4", "Only the Babbage example is about new inventions; migration and the music industry aren’t inventions.")])

# ---------------- Passage 4 ----------------
P.rc(18, "P4", "Application", "1", "Easy",
 "Which option matches one of the risky behaviours the passage names?",
 steps(("Risky behaviours", ev(4, "Two of the most common risky behaviours are parents leaving their children to play outside unattended and walking an unleashed dog, according to the study.")),
       ("So", p("Letting dogs off the leash where large carnivores are common is exactly the kind of behaviour that raises the risk of conflict."))) +
 final("Option 1."),
 "inference",
 [("2", "Photographing from secured areas keeps people away from the animals."),
  ("3", "Addressing climate change would reduce competition for resources, not increase conflict."),
  ("4", "Managing food waste stops carnivores from getting used to human food.")])

P.rc(19, "P4", "Weaken", "4", "Hard",
 "Read the question as: which statement clashes with the passage’s concerns about what drives conflict, so that the passage would need it to be false?",
 steps(("Climate change as a driver", ev(5, "Experts believe climate change also plays a part in the escalation of human-carnivore conflicts") +
          p("The passage raises climate change as one driver of conflict, with the example of lion attacks during a drought. A statement that climate change has had negligible effects goes directly against this concern.")),
       ("The others", p("Option 1 conflicts with a fact (predatory attacks are rare) rather than with a driver the passage worries about. Options 2 and 3 agree with the passage."))) +
 final("Option 4."),
 "weaken",
 [("1", "The passage says predatory attacks are rare, but they aren’t one of the drivers it is concerned about."),
  ("2", "This agrees with the finding that 50% of attacks could have been avoided."),
  ("3", "This is what the passage says: reliance on human food erodes their fear.")])

P.rc(20, "P4", "Inference", "3", "Easy",
 "Wilkinson’s quote explains why heterogeneous landscapes see more encounters.",
 steps(("The quote", ev(6, "There are a lot of working landscapes in the Global South that are really heterogeneous, that are interspersed with carnivore habitats, forests and savannahs, which creates a lot more opportunity for these encounters, just statistically")),
       ("So", p("Farmland mixed in with carnivore habitat raises the statistical chance of meeting."))) +
 final("Option 3."),
 "inference",
 [("1", "The passage talks about mixed landscapes, not contiguous wilderness."),
  ("2", "Uniform landscapes aren’t discussed."),
  ("4", "This reverses the passage: mixing raises the chance of conflict.")])

P.rc(21, "P4", "Detail", "2", "Easy",
 "What happens to carnivores that get used to human food?",
 steps(("The passage", ev(1, "As they become more reliant on human food they might find at campsites or in rubbish bins, they become less avoidant of humans. Losing that instinctive fear response puts them into more situations where they could get into an altercation with a human")),
       ("So", p("Habituation comes from losing their fear because they depend on human food."))) +
 final("Option 2."),
 "detail",
 [("1", "Treating humans as prey is the rare predatory attack, not habituation."),
  ("3", "Aggression in defence of young or food is a separate driver."),
  ("4", "Climate change brings more contact, but the passage doesn’t link it to habituation.")])

P.va(22, P.sents(22), [], "TITA", "2", "Odd_One_Out", "Medium",
 "Four sentences are about the political discomfort with biological explanations of gender. Which one turns to a different point?",
 steps(("The chain", p("Sentence 1 states the empirical position: gender is neither all nature nor all nurture. Sentence 4 (“Despite this empirical truth”) says researchers of its biological basis face pushback. Sentence 3 says many people are uncomfortable with gender not being purely social, and sentence 5 explains why: a political preference for gender being entirely malleable.")),
       ("The extra sentence", p("Sentence 2 argues that biology doesn’t excuse complacency about sexism. That is a separate point, not part of the account of the pushback."))) +
 final(r"\(2\)"),
 "oddone",
 [("1", "The empirical position."), ("4", "“Despite this empirical truth”: the pushback."), ("3", "The discomfort behind it."), ("5", "The political preference that explains it.")],
 why_title="How the other sentences fit")

P.va(23, P.ms(23), ["Option 2", "Option 4", "Option 3", "Option 1"], "MCQ", "1", "Missing_Sentence", "Medium",
 "The sentence is a triumphant overstatement. Which line in the paragraph pulls it back?",
 steps(("The fit", p("After “Now, however, we are having the last laugh”, the sentence “Science has officially crowned us superior to our early-rising brethren” states the news with a flourish. The next line, “It may be a tad more complicated than that”, then tones down exactly that overstatement.")),
       ("Reading the options", p("Blank (2) is listed first, so the answer is option 1."))) +
 final("Blank (2), which is option 1."),
 "missing",
 [("2", "Blank (4) comes after “it’s legit”, just before the study’s details; a boast there leaves nothing to tone it down."),
  ("3", "At blank (3) the study has already been introduced cautiously; the boast would contradict the caution."),
  ("4", "At blank (1) the paragraph hasn’t yet described how night owls were maligned, so “the last laugh” would come later anyway.")])

P.va(24, P.summ(24), P.Q["VARC"][24]["opts"], "MCQ", "1", "Summary", "Medium",
 "What does Cleese say creativity needs, and what is killing it?",
 steps(("What the passage says", "<ol><li>You can only create in an atmosphere of freedom, building without knowing where you’re going.</li><li>Comedians now check every idea against what got others into trouble.</li><li>That fear is the death of creativity.</li></ol>"),
       ("Choosing", p("Option 1 keeps both halves: comedy needs freedom and creativity, and fear of offending stifles originality."))) +
 final("Option 1."),
 "summary",
 [("2", "This turns his description of creativity into instructions and drops the point about fear."),
  ("3", "Cleese talks about the death of creativity, not of comedy as an art form, and he says limits have always existed."),
  ("4", "He doesn’t say criticism must come later; he says constant self-checking blocks creation.")])
