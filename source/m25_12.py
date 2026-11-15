# -*- coding: utf-8 -*-
# Simp Mock 12 (2025): VARC (24 of 24). DILR and QA: m25_12_dilr.py, m25_12_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(12, "sm25_12.json", series=2025)
P.passage("V1", "Passage 1 — The krill that pump carbon", "Environment_and_Life_Science")
P.passage("V2", "Passage 2 — The names behind the names", "Economics_and_Management")
P.passage("V3", "Passage 3 — A lost Mayan city found by lidar", "Social_Science_and_History")
P.passage("V4", "Passage 4 — The unknowing self", "Philosophy_and_Psychology")


def pj(n):
    parts = [x.strip() for x in P.Q["VARC"][n]["q"].split("\n\n") if x.strip()]
    return f"<p>{P.PJ_DIR}</p><ol class=\"sent\">" + "".join(f"<li>{x}</li>" for x in parts[1:]) + "</ol>"


P.va(1, P.summary_html(1, "Metastasis, when"), P.Q["VARC"][1]["opts"], "MCQ", "3", "Summary", "Medium",
 "Metastasis kills most patients; single escaping cells are the weak point to target.",
 steps(("The core", p("Metastasis causes 90% of cancer deaths; cells that have just broken away are most exposed to the immune system, so attacking them then could help.")),
       ("Choosing", p("Option 3 has both halves: why metastasis matters and the idea of acting at the early stage of spread. Option 4 stops at ‘understanding’ and drops the treatment angle."))) + final("Option 3"),
 "summary", [("1", "‘Eliminate tumors entirely’ overstates the claim."), ("2", "Only recurrence; misses the vulnerable moment."), ("4", "Understanding, not targeting.")])

# ---------------- Passage 1 (Q2–5) ----------------
P.rc(2, "V1", "Purpose", "3", "Easy",
 "The line comes right after ‘collective impact’.",
 steps(("The context", ev(1, "the tiny crustacean’s collective impact across the entire planet is enormous") +
          p("A swarm visible from space is a vivid picture of that scale: the point is how much krill matter together."))) + final("Option 3"),
 "purpose", [("1", "It is an opening image, not a warning of what comes."), ("2", "No assumption is being argued against."), ("4", "Regulation comes much later.")])
P.rc(3, "V1", "Detail_Not_True", "2", "Hard",
 "Which mechanism is named but never explained?",
 steps(("Explained", ev(2, "When krill waste sinks, that carbon goes with it, locking it away") +
          p("Waste carries carbon down (3), to depths where it is stored (1), as part of the biological pump (4).")),
       ("The odd one", p("Molting appears only in Savoca’s list ‘living and molting and pooping and dying’. The passage never says how molting moves carbon, and ‘carbon cycle’ is broader than the sequestration it describes."))) +
 trap("Molting is mentioned, so it feels supported; the question asks what the passage explains.") + final("Option 2"),
 "except", [("1", "Stored for hundreds of years."), ("3", "Sinking waste."), ("4", "The biological pump.")])
P.rc(4, "V1", "Inference_Except", "3", "Medium",
 "Three statements match the passage, so their falsity would contradict it. Find the one that doesn’t match.",
 steps(("Consistent", p("Vulnerability despite numbers (1), the lapsed measure and gridlock (2), and ice loss shifting krill towards predators and fleets (4) are all in the passage.")),
       ("The odd one", ev(5, "it shouldn’t be the burden of consumers to enforce sustainable fishing practices") +
          p("The passage rejects option 3, so its being false would agree with the passage."))) + final("Option 3"),
 "except", [("1", "The passenger pigeon warning."), ("2", "The commission’s failure."), ("4", "The 2023 study.")])
P.rc(5, "V1", "Purpose", "2", "Easy",
 "What happened to the passenger pigeon despite its numbers?",
 steps(("The line", ev(3, "Something can go from being incredibly abundant to extinct") +
          p("Abundance is no guarantee; a thriving species can still vanish."))) + final("Option 2"),
 "purpose", [("1", "No call about all endangered species."), ("3", "Not about ecosystem collapse here."), ("4", "Krill are ‘not at risk of extinction anytime soon’.")])

P.va(6, pj(6), [], "TITA", "2314", "Para_Jumble", "Easy",
 "Which sentence names folk psychology for the first time?",
 steps(("Opening", p("Sentence 2 defines folk psychology as the manifest image of the mind.")),
       ("Links", p("‘It assumes a self’ (3) follows the definition; 1 adds what follows from that self (free will, accountability); 4 closes by contrasting how it is acquired with scientific psychology."))) + final("2314"),
 "pj", [("1", "Uses the term as already known."), ("3", "‘It’ needs a noun before it."), ("4", "‘this model’ needs a model first.")], why_title="Why the others can’t open")
P.va(7, P.summary_html(7, "Drawing on the work"), P.Q["VARC"][7]["opts"], "MCQ", "4", "Summary", "Medium",
 "Lenin’s labour aristocracy, applied to Western Marxism’s neglect of the Global South.",
 steps(("The core", p("A privileged ‘labor aristocracy’ explains why the Western left sides with its bourgeoisie; the author applies the same lens to Western Marxism’s dismissal of Global South revolutions.")),
       ("Choosing", p("Option 4 names the concept and both effects."))) + final("Option 4"),
 "summary", [("1", "Drops the labour aristocracy."), ("2", "‘Allegiance to imperialism’ goes further than the passage."), ("3", "Credits the revolutions to the bourgeoisie.")])

# ---------------- Passage 2 (Q8–11) ----------------
P.rc(8, "V2", "Tone", "4", "Easy",
 "Read the last sentence of the passage.",
 steps(("The line", ev(6, "Critique dies, numb consumption wins, and the creative spirit is devoured by capital") +
          p("Bleak and pained, not hopeful or wistful."))) + final("Option 4"),
 "inference", [("1", "No hope expressed."), ("2", "No looking back to a better past."), ("3", "The mapping is earlier; this paragraph is a verdict.")])
P.rc(9, "V2", "Inference_Except", "4", "Medium",
 "Who does the author blame?",
 steps(("Supported", ev(3, "there’s a lot of capital collecting in a very few hands") +
          p("Less critique and variety (1), power in few hands (2), production giving way to extraction (3).")),
       ("The odd one", p("The target is equity and financial players behind the companies. Bain Capital is a private equity firm, not a legacy media corporation, and the studios aren’t singled out as culprits."))) + final("Option 4"),
 "except", [("1", "‘Critique dies’."), ("2", "Capital in few hands."), ("3", "Extraction cultures.")])
P.rc(10, "V2", "Application", "2", "Easy",
 "A text as a package of assets: one work, many revenue streams.",
 steps(("The idea", ev(5, "financialized texts become sites of capital formation") +
          p("A hit series that spawns spin-offs, ad revenue and remakes is a bundle of assets to be exploited."))) + final("Option 2"),
 "inference", [("1", "Independent art, the opposite."), ("3", "Cost cutting, not a text as assets."), ("4", "Protecting art from that logic.")])
P.rc(11, "V2", "Inference", "3", "Easy",
 "Does the author see any upside in commercialised culture?",
 steps(("The view", ev(6, "leaving little room for radical art") +
          p("Commercialisation narrows art. Option 3 claims it widened opportunity, which the author would reject.")),
       ("The others", p("Passive audiences (1), safe formulaic content (2) and fresh work coming from outside the big circles (4) fit the argument."))) + final("Option 3"),
 "inference", [("1", "‘Numb consumption’."), ("2", "Extraction over production."), ("4", "Implied by ‘little room’ inside.")])

# ---------------- Passage 3 (Q12–15) ----------------
P.rc(12, "V3", "Detail", "1", "Medium",
 "How did the student come across the data?",
 steps(("The line", ev(1, "I was on something like page 16 of a Google search and found a laser survey") +
          p("The lidar survey already existed; the find came from searching deep in online results.")),
       ("Why not 3", p("He didn’t carry out a lidar scan; he found an old survey someone else had made."))) +
 trap("Lidar is everywhere in the passage, but it isn’t how this discovery was made.") + final("Option 1"),
 "detail", [("2", "No thermal imaging."), ("3", "The scan was done by an environmental monitoring organisation a decade earlier."), ("4", "No old maps.")])
P.rc(13, "V3", "Inference_Except", "1", "Medium",
 "Was interconnectivity already known?",
 steps(("The line", ev(3, "these findings challenge the long-held belief that the Maya civilization was composed mainly of small, isolated villages") +
          p("The finds overturn an old view; they don’t confirm something already known. Option 1 is inconsistent.")),
       ("The others", p("The changed perception (2), highways and production chains (3), and ideas travelling with goods (4) are all in the passage."))) + final("Option 1"),
 "except", [("2", "Paragraph 3."), ("3", "Causeways and jade."), ("4", "Schieber de Lavarreda.")])
P.rc(14, "V3", "Inference", "2", "Hard",
 "Which claim is backed across several paragraphs without going further than the text?",
 steps(("Support", ev(3, "Lidar has instead uncovered a vast, interconnected network of cities, roads, and infrastructure") +
          p("Plazas, pyramids, ball courts, reservoirs and causeways show cities that were architecturally and infrastructurally advanced.")),
       ("Why not 4", p("The broad planning comes from the whole regional network, not from Valeriana alone; option 4 pins it on one site."))) + final("Option 2"),
 "inference", [("1", "‘One of the densest’, not the single centre."), ("3", "‘Superhighway’ is a comparison of scale, not function."), ("4", "Attributes regional findings to one city.")])
P.rc(15, "V3", "Inference", "2", "Medium",
 "What makes the traces ‘invisible’?",
 steps(("The line", ev(4, "There are also ‘invisible’ traces of raw materials") +
          p("Jade moved hundreds of kilometres and was shaped in stages: the chain is worked out from how materials flowed, not from finished objects."))) + final("Option 2"),
 "inference", [("1", "Traces do remain."), ("3", "No secrecy."), ("4", "Lidar maps structures, not material flows.")])

P.va(16, P.ms(16), P.Q["VARC"][16]["opts"], "MCQ", "4", "Missing_Sentence", "Easy",
 "The sentence announces a trend; the next line quotes ‘high-touch will overshadow high-tech’.",
 steps(("Find the spot", p("Blank 1: the sentence introduces the trend, and the next sentence names it as a notion already set up.")),
       ("Match the label", p("Blank 1 is choice 4, labelled ‘Option 1’."))) + final("Choice 4 (“Option 1”)"),
 "missing", [("1", "“Option 4”: the paragraph already ends on balancing tech and touch."), ("2", "“Option 2”: breaks the notion from its elaboration."), ("3", "“Option 3”: inside the customer discussion.")])
P.va(17, pj(17), [], "TITA", "2431", "Para_Jumble", "Medium",
 "Mysteries, past successes, the people needed, then the critique.",
 steps(("Opening", p("Sentence 2 sets out the unsolved scripts.")),
       ("Links", p("4 shows such puzzles have been cracked by innovative talent; 3 says universities must nurture such people; 1 ends with what universities should stop doing instead."))) + final("2431"),
 "pj", [("1", "‘Instead of…’ answers a point made earlier."), ("3", "Needs the scripts as context first."), ("4", "‘Past successes’ need the present mysteries.")], why_title="Why the others can’t open")

# ---------------- Passage 4 (Q18–21) ----------------
P.rc(18, "V4", "Main_Idea", "3", "Medium",
 "‘Not solely’ a psychological need.",
 steps(("The line", ev(1, "None of these disorders develops solely to gratify a psychological need. It seems to be in the wiring") +
          p("Some delusions start in the brain, not only in psychological needs.")),
       ("Why not 2", p("‘Rather than’ excludes psychological motives, and ‘as was previously believed’ adds a history the paragraph doesn’t give."))) + final("Option 3"),
 "inference", [("1", "The opposite."), ("2", "Too absolute, and adds a past belief."), ("4", "Danger isn’t the point.")])
P.rc(19, "V4", "Inference_Except", "3", "Medium",
 "Does the author want self-deception eliminated?",
 steps(("Supported", ev(2, "Some delusions reflect benign self-ignorance. Other delusions require active work") +
          p("Neurological roots (1), a range from benign to active (2), and a half-aware state (4: ‘not asleep, but neither are they fully attentive’).")),
       ("The odd one", p("The author even entertains that self-evasion might be a skill; nowhere does he say it must be eliminated."))) + final("Option 3"),
 "except", [("1", "Paragraph 1."), ("2", "Paragraph 2."), ("4", "Paragraph 2.")])
P.rc(20, "V4", "Purpose", "2", "Medium",
 "Two selves that both knew the way home.",
 steps(("The line", ev(3, "how we can be not at one with ourselves, yet still somehow the same") +
          p("The quip captures the oddity of being divided yet one, a common experience."))) + final("Option 2"),
 "purpose", [("1", "Knowing the way home shows they aren’t fully separate."), ("3", "No clinical comparison."), ("4", "Not about writers.")])
P.rc(21, "V4", "Purpose", "3", "Medium",
 "Religious traditions reject self-evasion ‘for good reason’; the story is the reason.",
 steps(("The lead-in", ev(3, "But no religious tradition accepts this view—and for good reason") +
          p("David can condemn the rich man but doesn’t see himself until Nathan says ‘You are the man’. Not knowing himself led to grave wrongs.")),
       ("The next paragraph", ev(5, "we find this tragic"))) + final("Option 3"),
 "purpose", [("1", "Punishment isn’t the focus."), ("2", "Redemption isn’t the focus."), ("4", "Nothing about the burden of authority.")])

P.va(22, P.summary_html(22, "On a daily basis"), P.Q["VARC"][22]["opts"], "MCQ", "1", "Summary", "Hard",
 "We assume consciousness mirrors the real world, but ontology itself must be defined subjectively.",
 steps(("The core", p("Being able to build a model of the world doesn’t show we have captured the true ontology; ontology must be defined from the content of the mind.")),
       ("Choosing", p("Option 1 keeps the assumption and the turn to subjectively grounded ontology, with the passage’s caution."))) + final("Option 1"),
 "summary", [("2", "‘Misguided’ is too strong."), ("3", "Centres on classical physics."), ("4", "‘Depends more on’ weighs two sources; the passage names one.")])
P.va(23, P.ms(23), P.Q["VARC"][23]["opts"], "MCQ", "1", "Missing_Sentence", "Easy",
 "A myth about the humps, right before the truth about them.",
 steps(("Find the spot", p("Blank 2 comes after the humps are introduced and before ‘The humps are composed of fatty tissue’, which corrects the myth.")),
       ("Match the label", p("Blank 2 is choice 1, labelled ‘Option 2’."))) + final("Choice 1 (“Option 2”)"),
 "missing", [("2", "“Option 1”: the humps haven’t appeared yet."), ("3", "“Option 4”: the paragraph is wrapping up."), ("4", "“Option 3”: after the correction.")])
P.va(24, P.ms(24), P.Q["VARC"][24]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "A line of praise that frames what the chip is.",
 steps(("Find the spot", p("Blank 1 follows ‘moving toward reality’ and comes before the description of what the technology does; the praise sets up the details.")),
       ("Match the label", p("Blank 1 is choice 1, labelled ‘Option 1’."))) + final("Choice 1 (“Option 1”)"),
 "missing", [("2", "“Option 2”: between functions and applications."), ("3", "“Option 3”: among the concerns."), ("4", "“Option 4”: the ending is already strong.")])
