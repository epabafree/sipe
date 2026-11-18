# -*- coding: utf-8 -*-
# Simp Mock 5: VARC (24 of 24). DILR and QA: m05_dilr.py, m05_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(5, "sm05.json")
P.passage("V1", "Passage 1 — Can a book be great?", "Arts_and_Literature")
P.passage("V2", "Passage 2 — Why lost languages matter", "Social_Science_and_History")
P.passage("V3", "Passage 3 — Horizons of black holes and the universe", "Science_and_Technology")
P.passage("V4", "Passage 4 — Thirty glorious years", "Economics_and_Management")

# Small wording fixes so that each VA item has exactly one defensible answer.
V = P.Q["VARC"]
V[18]["q"] = V[18]["q"].replace("1. Bluetooth, because it requires", "1. Overall, Bluetooth, because it requires")
V[19]["q"] = V[19]["q"].replace("3. We can just step out the front door,", "3. We can instead just step out the front door,")
V[20]["q"] = V[20]["q"].replace("Now the creature represents extinction itself—you can’t get deader than a dodo.",
                                "Between them, these pressures finished the bird off, and now it represents extinction itself—you can’t get deader than a dodo.")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Main_Idea", "1", "Easy",
 "Where does the author end up after the critiques?",
 steps(("The turn", ev(5, "we can contain its paralysing force by eschewing any effort to define a great book – or a classic – with reference to some defining essence") +
          ev(5, "certain works, and not others, have demonstrated a capacity to illuminate the lives of many different kinds of people in many different historical circumstances")),
       ("Choosing", p("Option 1 is the author’s own proposal; the others are the critiques it answers."))) +
 final("Option 1"),
 "inference",
 [("2", "A critique the author reports."), ("3", "The sceptic’s view, not the author’s."), ("4", "Not in the passage.")])

P.rc(2, "V1", "Except", "4", "Medium",
 "Three options are claims the author grants; one is the critics’ conclusion, which the author sets aside.",
 steps(("Granted", ev(2, "the challenge to assigning hierarchical value to cultural expressions – isn’t as preposterous as it might first appear") +
          p("The author accepts options 1–3 as fair points.")),
       ("Set aside", ev(4, "These anti-foundational critiques of ‘greatness’ carry the high-voltage implication that any hierarchy of artistic value is probably complicit in moral corruption") +
          p("Option 4 is the critics’ implication. The author ‘contains its paralysing force’ rather than endorsing it, so it is the least supported by the passage’s own argument."))) +
 final("Option 4"),
 "except",
 [("1", "Paragraph 2 grants it."), ("2", "Paragraph 2 says it."), ("3", "Paragraph 2: preferences shaped by education and prejudice.")])

P.rc(3, "V1", "Inference", "1", "Easy",
 "‘Complicit in moral corruption’ — through what?",
 steps(("Context", ev(3, "the elite forms of cultural power embodied in values of ‘greatness’ are undergirded by the exploitation and dehumanisation of ‘the other’")),
       ("Choosing", p("Ranking works takes part in oppression and exclusion: option 1."))) +
 final("Option 1"),
 "inference",
 [("2", "Moral greatness is not the point."), ("3", "Turns the critique into praise."), ("4", "The critique discourages such judgments.")])

P.rc(4, "V1", "Detail", "3", "Easy",
 "What do the surviving works have in common?",
 steps(("The line", ev(5, "These works somehow transcended the conditions of their own creation – they spoke within their time, but also beyond it")),
       ("Choosing", p("Look for works with universality: option 3. Surveying the texts (option 4) is only the method, not the test."))) +
 final("Option 3"),
 "detail",
 [("1", "The author rejects defining essences."), ("2", "Those viewpoints are the ones set aside."), ("4", "The survey is a step, not the criterion.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Main_Idea", "4", "Easy",
 "Each paragraph gives a reason languages matter.",
 steps(("The reasons", p("Heritage (paragraph 2), culture (3), knowledge (4) and ways of thinking (5).")),
       ("Choosing", p("Option 4 holds them together."))) +
 final("Option 4"),
 "inference",
 [("1", "One comparison only."), ("2", "The closing detail."), ("3", "Writing is a side point.")])

P.rc(6, "V2", "Detail", "1", "Easy",
 "What do the ‘who cares’ people say?",
 steps(("The line", ev(1, "Some people argue that language loss, like species loss, is simply a fact of life on an ever-evolving planet")),
       ("Choosing", p("Option 1."))) +
 final("Option 1"),
 "detail",
 [("2", "Turin’s argument for preservation."), ("3", "Also part of the case for preservation."), ("4", "A paraphrase of the dismissive attitude, not an argument.")])

P.rc(7, "V2", "Except", "4", "Medium",
 "The passage compares languages to ecosystems; does it say languages help conserve biodiversity?",
 steps(("The line", ev(4, "Another argument mirrors that of biodiversity conservation. Just as ecosystems provide a wealth of services for humanity, languages, too, are ripe with possibility") +
          p("The parallel is about languages being valuable like ecosystems, not about languages helping biodiversity conservation.")),
       ("Choosing", p("Option 4 twists the comparison."))) +
 final("Option 4"),
 "except",
 [("1", "Lost knowledge and practices."), ("2", "Lost stories and ways of seeing."), ("3", "Turin’s point.")])

P.rc(8, "V2", "Purpose", "2", "Medium",
 "Cherokee appears in three different paragraphs. What does it show in all of them?",
 steps(("The uses", p("Paragraph 3: words for culture and emotion. Paragraph 4: knowledge of plants. Paragraph 5: a different way of thinking.")),
       ("Choosing", p("Together they argue that a lost language takes knowledge, heritage and culture with it: option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "Paragraph 3 only."), ("3", "Ancient origins and precision are side points."), ("4", "Linguists’ efforts are a different topic.")])

# ---------------- Passage 3 (Q9–12) ----------------
P.rc(9, "V3", "Except", "2", "Hard",
 "Which option describes the other horizon in paragraph 4?",
 steps(("Particle horizon", ev(4, "This refers to the distance beyond which light emitted in the early universe has not yet had time to reach us here on Earth")),
       ("Choosing", p("Option 2 is the particle horizon, not the cosmological event horizon."))) +
 final("Option 2"),
 "except",
 [("1", "Beyond it, light never reaches us."), ("3", "Where expansion outruns light."), ("4", "The passage’s ‘leaving everything beyond a certain distance in darkness’.")])

P.rc(10, "V3", "Structure", "1", "Medium",
 "Follow the order of the passage’s topics.",
 steps(("Topics", p("Event horizons; black holes; the cosmological horizon; Hawking radiation; the information paradox.")),
       ("Choosing", p("Option 1 follows the passage. The others give space to side points like the particle horizon or the singularity."))) +
 final("Option 1"),
 "summary",
 [("2", "The particle horizon is set aside by the author."), ("3", "Dark energy is only mentioned in passing."), ("4", "Singularity and particle horizon are side points.")])

P.rc(11, "V3", "Inference", "2", "Medium",
 "Light from beyond it has not reached us yet.",
 steps(("The line", ev(4, "This refers to the distance beyond which light emitted in the early universe has not yet had time to reach us here on Earth")),
       ("Choosing", p("What lies inside it is all we can see so far: the observable universe, option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "Not discussed."), ("3", "It limits what we see, not what exists."), ("4", "The author keeps the two apart.")])

P.rc(12, "V3", "Detail", "3", "Medium",
 "What does the paradox do to physics?",
 steps(("The line", ev(6, "it is a deep puzzle complicating the quest to combine quantum mechanics and gravity")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "detail",
 [("1", "Hawking’s work created the paradox; the 2019 work only made progress."), ("2", "The 2019 advances helped with it."), ("4", "Hawking radiation does that.")],
 opts=["was created and fully resolved by Hawking’s 1974 work.", "is incompatible with the recent technical advances.",
       "complicates efforts to combine quantum mechanics and gravity.", "causes black holes to eventually evaporate away."])

# ---------------- Passage 4 (Q13–16) ----------------
P.rc(13, "V4", "Detail", "1", "Easy",
 "What were growth rates like in North America?",
 steps(("The line", ev(3, "the Trente Glorieuses never existed there: per capita output grew at roughly the same rate of 1.5–2 percent per year throughout the period 1820–2012")),
       ("Choosing", p("No burst of fast growth, only the steady slow pace: option 1."))) +
 final("Option 1"),
 "detail",
 [("2", "State intervention is not given as the reason."), ("3", "Gap-closing concerns Europe."), ("4", "Not the reason given.")])

P.rc(14, "V4", "Main_Idea", "1", "Easy",
 "The passage explains a difference in public opinion.",
 steps(("The line", ev(4, "These very different collective experiences of growth in the twentieth century largely explain why public opinion in different countries varies so widely")),
       ("Choosing", p("Option 1."))) +
 final("Option 1"),
 "inference",
 [("2", "The author denies both policies the credit."), ("3", "The author doubts it."), ("4", "Too absolute.")])

P.rc(15, "V4", "Detail", "2", "Easy",
 "What did Thatcher and Reagan promise?",
 steps(("The line", ev(5, "promised to “roll back the welfare state” that had allegedly sapped the animal spirits of Anglo-Saxon entrepreneurs and thus to return to pure nineteenth-century capitalism, which would allow the United States and Britain to regain the upper hand")),
       ("Choosing", p("Option 2 states the promise. The author does not grant that it succeeded."))) +
 final("Option 2"),
 "detail",
 [("1", "The opposite."), ("3", "Not claimed."), ("4", "Not claimed for most countries.")],
 opts=["It aimed to increase government intervention in the economy.",
       "It promised to return Britain and the US to nineteenth-century capitalism and so let them regain the upper hand.",
       "It brought Britain and the United States to the forefront of technological advance.",
       "It ushered in an era of liberalisation, globalisation and growth in most countries."])

P.rc(16, "V4", "Inference", "3", "Medium",
 "The author denies both policies the credit, and explains opinion through experience.",
 steps(("The argument", ev(6, "neither the economic liberalization that began around 1980 nor the state interventionism that began in 1945 deserves such praise or blame") +
          ev(4, "These very different collective experiences of growth in the twentieth century largely explain why public opinion in different countries varies so widely")),
       ("Choosing", p("Option 3 agrees with the author. Options 1 and 2 give policies the credit, and option 4 contradicts the author’s suggestion about rivalry."))) +
 final("Option 3"),
 "inference",
 [("1", "Credits state intervention."), ("2", "Credits liberalisation."), ("4", "The author suggests rivalry ‘played an important part’.")],
 q="Which of the following is in line with the author’s argument in the passage?")

# ---------------- Verbal ability (Q17–24) ----------------
P.va(17, P.sent_html(17), [], "TITA", "4231", "Para_Jumble", "Easy",
 "Names first, then pronouns.",
 steps(("The opener", p("Sentence 4 names Gandhi and his quest.")),
       ("The sequence", p("Sentence 2: in South Africa, friends who quickened his interest. Sentence 3: what he read. Sentence 1: the conclusion he drew."))) +
 final("4231"),
 "pj",
 [("4", "Names Gandhi."), ("2", "South Africa."), ("3", "His reading."), ("1", "His conclusion.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.sent_html(18), [], "TITA", "2431", "Para_Jumble", "Easy",
 "General contrast first; ‘Overall’ last.",
 steps(("The opener", p("Sentence 2: the two differ.")),
       ("The sequence", p("Sentence 4: their purposes. Sentence 3: how many devices. Sentence 1 sums up the trade-off with ‘Overall’."))) +
 final("2431"),
 "pj",
 [("2", "Topic."), ("4", "Purpose."), ("3", "Capacity."), ("1", "“Overall”: summary.")],
 why_title="Why each sentence goes where it does")

P.va(19, P.sent_html(19), [], "TITA", "2413", "Para_Jumble", "Medium",
 "‘Instead’ in sentence 3 answers ‘we don’t need to visit a museum’.",
 steps(("Pairs", p("1–3: no museum needed; instead, step out of the front door. 4–1: ‘This’ (detaching to see life for ourselves) is Kant’s freedom of art.")),
       ("The opener", p("Sentence 2 introduces the art of walking and the contrast with screens: 2413."))) +
 final("2413"),
 "pj",
 [("2", "Introduces walking."), ("4", "What walking does."), ("1", "“This”: Kant."), ("3", "“Instead”: step outside.")],
 why_title="Why each sentence goes where it does")

P.va(20, P.missing_html(20), P.strict_opts(20), "MCQ", "4", "Missing_Sentence", "Easy",
 "‘These pressures’ needs the threats to be listed first.",
 steps(("Find the spot", p("Humans, and then monkeys and rats, are the pressures. The sentence sums them up and closes the paragraph at blank 4.")),
       ("Check the others", p("At blanks 1–3 the threats have not all been described."))) +
 final("Option 4"),
 "missing",
 [("1", "Nothing described yet."), ("2", "Only humans mentioned."), ("3", "Predators not yet mentioned.")])

P.va(21, P.missing_html(21), P.strict_opts(21), "MCQ", "1", "Missing_Sentence", "Easy",
 "‘The slowdown’ needs the slowing to be named.",
 steps(("Find the spot", p("Blank 1 follows the news that the core’s spin may have slowed; the sentence gives its importance before the study’s method.")),
       ("Check the others", p("Blanks 2–4 are about method, background and earlier findings."))) +
 final("Option 1"),
 "missing",
 [("2", "Method."), ("3", "Background."), ("4", "Earlier findings.")])

P.va(22, P.summary_html(22, "There are fair reasons"), P.Q["VARC"][22]["opts"], "MCQ", "2", "Summary", "Medium",
 "‘Connections … perhaps not inevitable’: careful wording.",
 steps(("What the passage says", "<ol><li>There are fair reasons to mistrust knowledge.</li><li>It is used to exclude and creates hierarchies that affect justice and representation.</li><li>It has historical links with colonialism and plunder.</li></ol>"),
       ("Choosing", p("Option 2 keeps all three. Option 3 says knowledge was used to subjugate groups, stronger than the passage’s ‘connections … perhaps not inevitable’."))) +
 final("Option 2"),
 "summary",
 [("1", "Garbled: ‘exclude hosts of socio-political classes’."), ("3", "Overstates the colonial link."), ("4", "Garbled: excludes ‘variables’.")])

P.va(23, P.summary_html(23, "A radical reformulation"), P.Q["VARC"][23]["opts"], "MCQ", "1", "Summary", "Easy",
 "From changing the student to changing the world.",
 steps(("What the passage says", "<ol><li>Education has turned away from improving young people’s inner fibre.</li><li>It now tries to make the outer world softer for them.</li></ol>"),
       ("Choosing", p("Option 1."))) +
 final("Option 1"),
 "summary",
 [("2", "Leaves out ‘inner fibre’."), ("3", "Says education is no longer about young people."), ("4", "Misstates the old aim as success.")])

P.va(24, P.summary_html(24, "In a society now dominated"), P.Q["VARC"][24]["opts"], "MCQ", "4", "Summary", "Medium",
 "Why do people want contrary ideas silenced?",
 steps(("What the passage says", "<ol><li>Bradbury predicted people would demand censorship for themselves.</li><li>The internet lets us choose our own silos.</li><li>That leads to the wish to stamp out contrary ideas.</li></ol>"),
       ("Choosing", p("Option 4 has the prediction and the cause."))) +
 final("Option 4"),
 "summary",
 [("1", "Leaves out the internet cause."), ("2", "Only examples."), ("3", "Says people limit exposure, not that they demand censorship.")])
