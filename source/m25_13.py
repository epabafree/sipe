# -*- coding: utf-8 -*-
# Simp Mock 13 (2025): VARC (24 of 24). DILR and QA: m25_13_dilr.py, m25_13_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(13, "sm25_13.json", series=2025)
P.passage("V1", "Passage 1 — How cash fades", "Economics_and_Management")
P.passage("V2", "Passage 2 — The hunt for dark matter", "Science_and_Technology")
P.passage("V3", "Passage 3 — Two ancestral populations", "Environment_and_Life_Science")
P.passage("V4", "Passage 4 — The Superiority Objection", "Philosophy_and_Psychology")


def listed(n, direc):
    parts = [x.strip() for x in P.Q["VARC"][n]["q"].split("\n\n") if x.strip()]
    return f"<p>{direc}</p><ol class=\"sent\">" + "".join(f"<li>{x}</li>" for x in parts[1:]) + "</ol>"


# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Main_Idea", "3", "Medium",
 "Who, if anyone, is steering the shift?",
 steps(("The line", ev(6, "No single cabal orchestrates it outright; rather, countless small actions converge to make cashless society feel not only practical but inevitable") +
          p("Many forces (profit, social consent, technology), no central control, and a cultural shift in what feels normal."))) + final("Option 3"),
 "inference", [("1", "‘doesn’t rely on an explicit directive’."), ("2", "Preferences are shaped by persuasion, not purely organic."), ("4", "Surveillance is one worry among several, not the thesis.")])
P.rc(2, "V1", "Inference_Except", "3", "Medium",
 "‘Unlikely to disagree with all EXCEPT’: find the one the author would reject.",
 steps(("Agreed", p("Small shops inadvertently join Big Tech (1); defenders say they follow consumers (2); digital platforms can share data with governments (4).")),
       ("The odd one", ev(5, "It is issued by central banks but prized for its anonymity") +
          p("Central banks appear only as the issuers of cash; nothing says they push digital payments to avoid handling it."))) + final("Option 3"),
 "except", [("1", "Paragraph 3."), ("2", "Paragraph 4."), ("4", "Paragraph 5.")])
P.rc(3, "V1", "Tone", "2", "Medium",
 "What does the author fear in the first paragraph?",
 steps(("The line", ev(1, "even people who appreciate using cash may eventually be driven away from it by subtle, systemic forces") +
          p("A worry about cash slipping away, without blaming anyone outright."))) + final("Option 2"),
 "inference", [("1", "Corporations are described, not dismissed."), ("3", "Society’s passivity isn’t criticised here."), ("4", "Not indifferent.")])
P.rc(4, "V1", "Purpose", "4", "Medium",
 "What do local merchants do next in the paragraph?",
 steps(("The context", ev(3, "Local merchants, hoping to stay competitive, often align themselves with automated payments systems") +
          p("A big firm’s set-up pulls others along: the example shows how influential firms shape payment habits.")),
       ("Why not 1", p("The author stresses that no one directs this on purpose; ‘intentionally marginalize’ goes against that."))) + final("Option 4"),
 "purpose", [("1", "No intent claimed."), ("2", "Not a criticism of one firm."), ("3", "The author doubts the consumer-demand story.")])

P.va(5, P.summary_html(5, "Intelligent computing has"), P.Q["VARC"][5]["opts"], "MCQ", "2", "Summary", "Medium",
 "Transformation now, human–AI collaboration as the future.",
 steps(("The core", p("Intelligent computing has transformed linguistics through NLP, speech recognition and more, and its future lies in humans and AI working together.")),
       ("Choosing", p("Option 2 has both the present change and the stated future."))) + final("Option 2"),
 "summary", [("1", "Puts ‘ethical innovation’ at the centre."), ("3", "Inclusivity and diversity are side points."), ("4", "Leaves out the future of the field.")])
P.va(6, P.ms(6), P.Q["VARC"][6]["opts"], "MCQ", "3", "Missing_Sentence", "Easy",
 "The sentence is about how he paints; find where his portraits are described.",
 steps(("Find the spot", p("Blank 3 follows ‘His portraits, painted on perforated newspaper’ and comes before the subjects of the works: technique sits with the description of the portraits.")),
       ("Match the label", p("Blank 3 is choice 3."))) + final("Option 3"),
 "missing", [("1", "His childhood link to the mountains."), ("2", "Before the portraits are mentioned."), ("4", "Among the jerabos and exploitation.")])
P.va(7, listed(7, P.ODD_DIR), [], "TITA", "2", "Odd_One_Out", "Easy",
 "Four sentences track the rising toll of smoking, especially in developing countries.",
 steps(("The chain", p("4 → 1 → 5 → 3: tobacco recognised as deadly (4); alarming given rising smoking in developing countries (1); WHO death figures (5); developing countries’ 80% share (3).")),
       ("The odd one", p("Sentence 2 turns to smokeless tobacco, which nothing else takes up."))) + final("2"),
 "oddone", [("1", "The worry about developing countries."), ("3", "Ends the chain."), ("4", "The opening."), ("5", "The figures.")], why_title="How the other sentences fit")

# ---------------- Passage 2 (Q8–11) ----------------
P.rc(8, "V2", "Inference", "2", "Medium",
 "Why are the leading candidates so hard to catch?",
 steps(("The line", ev(3, "Because they barely interact with ordinary matter, WIMPs are incredibly elusive") +
          p("For decades the search assumed WIMPs, whose weak interaction explains the empty results.")),
       ("Why not 1", p("The neutrino floor is a limit that searches will reach ‘eventually’, not the reason for past failure."))) + final("Option 2"),
 "inference", [("1", "A future barrier."), ("3", "Axions are a newer, separate line."), ("4", "A ‘long shot’ the passage doubts.")])
P.rc(9, "V2", "Detail_Not_True", "1", "Easy",
 "What exactly was odd about the rotation rates?",
 steps(("The line", ev(2, "found there isn’t enough visible matter to account for the observed spin") +
          p("The evidence is too little visible matter for the spin, not uniform rotation.")),
       ("The others", p("Lensing (2), cluster collisions such as the Bullet Cluster (3) and the microwave background (4) are all named."))) + final("Option 1"),
 "except", [("2", "Paragraph 2."), ("3", "The Bullet Cluster."), ("4", "Hot and cold spots.")])
P.rc(10, "V2", "Detail", "3", "Easy",
 "What happens at the floor?",
 steps(("The line", ev(3, "where signals from neutrinos swamp any potential dark matter signal") +
          p("Below that point a detector can’t tell dark matter from neutrinos: its sensitivity has hit a limit."))) + final("Option 3"),
 "detail", [("1", "The microwave background isn’t involved."), ("2", "Neutrinos specifically, not any particle."), ("4", "Dark matter doesn’t change.")])
P.rc(11, "V2", "Weaken", "2", "Medium",
 "What was dark matter first invented to explain?",
 steps(("The origin", ev(2, "The case for dark matter dates back to when astronomers studied galaxy rotation rates") +
          p("If known gravitational forces fully explained galaxy motion, the founding reason for dark matter would disappear."))) + final("Option 2"),
 "weaken", [("1", "Supports axions as a candidate."), ("3", "Hampers detection; doesn’t disprove."), ("4", "Removes one line of evidence among several.")])

# ---------------- Passage 3 (Q12–15) ----------------
P.rc(12, "V3", "Detail_Not_True", "2", "Easy",
 "Have fossils been matched to the genetic ancestors?",
 steps(("The line", ev(4, "although more research will be needed to identify which genetic ancestors corresponded to which fossil group") +
          p("The fossils are only candidates; no definitive link exists.")),
       ("The others", p("The 80% population as the source of Neanderthals and Denisovans (1), the challenge to a single lineage (3), and the use of modern genomes (4) are all stated."))) + final("Option 2"),
 "except", [("1", "Scally’s quote."), ("3", "Durbin’s quote."), ("4", "The team’s method.")])
P.rc(13, "V3", "Purpose", "3", "Medium",
 "What did the shrunken population go on to do?",
 steps(("The line", ev(3, "This population would later contribute about 80% of the genetic material of modern humans") +
          p("A group that nearly collapsed became our main genetic source."))) + final("Option 3"),
 "purpose", [("1", "Homo sapiens didn’t exist yet."), ("2", "The opposite: 80%."), ("4", "No cause of the decline is given.")])
P.rc(14, "V3", "Inference", "3", "Easy",
 "Why does the DNA method help?",
 steps(("The line", ev(2, "enabled them to infer the presence of ancestral populations that may have otherwise left no physical trace") +
          p("Some ancestors may have left no bones at all, so fossils alone can’t tell the whole story."))) + final("Option 3"),
 "inference", [("1", "Not the stated limit."), ("2", "Abundance isn’t the problem."), ("4", "Not said.")])
P.rc(15, "V3", "Strengthen", "2", "Medium",
 "The thesis: populations split, then mixed, and genetic exchange shaped us.",
 steps(("The claim", ev(4, "Interbreeding and genetic exchange have likely played a major role in the emergence of new species") +
          p("DNA from one ancient group showing up in distant modern populations is direct evidence of such mixing.")),
       ("The others", p("No interaction (1), no genetic trace (3) and blocked mixing (4) all point the other way."))) + final("Option 2"),
 "weaken", [("1", "No mixing."), ("3", "Left nothing in us."), ("4", "Prevents mixing.")])

P.va(16, P.summary_html(16, "Hate is destructive"), P.Q["VARC"][16]["opts"], "MCQ", "4", "Summary", "Medium",
 "Harm to the hater, harm to society, and a closing note that it can be unlearned.",
 steps(("The core", p("Hate damages individuals and societies, up to violence, but because it is learned it can be unlearned.")),
       ("Choosing", p("Option 4 keeps the personal and social harm and ends where the passage ends."))) + final("Option 4"),
 "summary", [("1", "Makes reversibility the main clause."), ("2", "‘Helps in healing’ isn’t in the passage."), ("3", "Education and awareness aren’t mentioned.")])

# ---------------- Passage 4 (Q17–20) ----------------
P.rc(17, "V4", "Inference_Except", "3", "Medium",
 "Who is the target of the laughter in every version of the objection?",
 steps(("Present", p("Confucian worry about hierarchy and harmony (1), the Kantian ‘mere means’ (2), and laughing at reality for failing our demand for resolution (4).")),
       ("The odd one", ev(4, "conceiving the comical object as inferior and the diverted subject as superior") +
          p("The objection is about looking down on an object. Laughing at oneself as the source of fun isn’t part of it; Hobbes’s ‘former selves’ is about feeling superior, not self-mockery."))) + final("Option 3"),
 "except", [("1", "The Confucian objection."), ("2", "The Kantian view."), ("4", "Humoristic Absurdism.")])
P.rc(18, "V4", "Purpose", "2", "Easy",
 "Why bring in a philosopher who wanted some jokes forbidden?",
 steps(("The line", ev(2, "perhaps they should have forbidden some kinds of jokes") +
          p("An early instance of the Superiority Objection: humor as morally troubling."))) + final("Option 2"),
 "purpose", [("1", "Not about norms."), ("3", "Only ‘some kinds’, and only ‘perhaps’."), ("4", "Nothing political.")])
P.rc(19, "V4", "Inference_Except", "4", "Medium",
 "Sudden glory is one-sided.",
 steps(("The line", ev(3, "laughter arises from a sense of sudden glory — a feeling of superiority over others or over our own former selves") +
          p("A gap in worth (1), a demeaning edge (2), a quick lift of the ego (3).")),
       ("The odd one", p("Nothing is shared or mutual: the glory belongs to the one laughing."))) + final("Option 4"),
 "except", [("1", "Superiority."), ("2", "The critical reading of paragraph 4."), ("3", "‘Sudden’.")])
P.rc(20, "V4", "Inference", "2", "Easy",
 "What fails, in Humoristic Absurdism?",
 steps(("The line", ev(1, "it is not a person which violates a norm, but reality, by failing to meet our demand for resolution") +
          p("Reality is the object of ridicule."))) + final("Option 2"),
 "inference", [("1", "Not a person."), ("3", "Incongruity isn’t the theory described."), ("4", "The objection says the opposite.")])

P.va(21, P.summary_html(21, "The Keynesian idea"), P.Q["VARC"][21]["opts"], "MCQ", "1", "Summary", "Medium",
 "A rebuttal of the Keynesian view, with its reasons.",
 steps(("The core", p("Government spending doesn’t drive growth: it takes from the private sector, crowds out investment, lowers productivity and costs taxpayers.")),
       ("Choosing", p("Option 1 keeps the anti-Keynesian frame and the reasons. Option 3 drops the frame; option 4 makes it Friedman’s view alone."))) + final("Option 1"),
 "summary", [("2", "Only the states example."), ("3", "Misses the Keynesian frame."), ("4", "Credits the whole case to Friedman.")])
P.va(22, P.ms(22), P.Q["VARC"][22]["opts"], "MCQ", "2", "Missing_Sentence", "Medium",
 "‘Rather than championing…’: what is he turning away from, and what follows?",
 steps(("Find the spot", p("Blank 2 follows the inward, pre-war tradition of rejecting global leadership and comes before ‘His policy emphasizes traditional great power politics’. The sentence moves from the history to his own stance.")),
       ("Match the label", p("Blank 2 is choice 2."))) + final("Option 2"),
 "missing", [("1", "Before the history that explains the throwback."), ("3", "Among the details on spheres of influence."), ("4", "Just before the closing line.")])
P.va(23, P.ms(23), P.Q["VARC"][23]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "‘Many’ firms turning overseas; the next sentence says ‘These firms’.",
 steps(("Find the spot", p("Blank 3 follows the weak yen and wider international reach, and comes before ‘These firms are reimagining the industrial future’, which needs firms just mentioned.")),
       ("Match the label", p("Blank 3 is choice 1, labelled ‘Option 3’."))) + final("Choice 1 (“Option 3”)"),
 "missing", [("2", "“Option 2”: before the yen point."), ("3", "“Option 4”: after the summary."), ("4", "“Option 1”: still on domestic industry.")])
P.va(24, listed(24, P.ODD_DIR), [], "TITA", "1", "Odd_One_Out", "Hard",
 "Four sentences trace the Code from start to end. One looks back to an earlier failure.",
 steps(("The chain", p("5 → 3 → 2 → 4: the Code defined (5); its bans (3); filmmakers working within them (2); abandoned in 1968 (4).")),
       ("The odd one", p("Sentence 1 is about Hays’s earlier guidelines failing, a different stage that doesn’t link to ‘This code’ or the rest."))) + final("1"),
 "oddone", [("2", "Effects."), ("3", "Contents."), ("4", "The end."), ("5", "The opening.")], why_title="How the other sentences fit")
