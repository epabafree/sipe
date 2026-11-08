# -*- coding: utf-8 -*-
# Simp Mock 4 (2025): VARC (24 of 24). DILR and QA: m25_04_dilr.py, m25_04_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(4, "sm25_04.json", series=2025)
P.passage("V1", "Passage 1 — A studio’s deal with an AI firm", "Arts_and_Literature")
P.passage("V2", "Passage 2 — The laws of chemistry", "Science_and_Technology")
P.passage("V3", "Passage 3 — Defining life", "Philosophy_and_Psychology")
P.passage("V4", "Passage 4 — Choosing good managers", "Economics_and_Management")

P.va(1, P.missing_html(1), P.Q["VARC"][1]["opts"], "MCQ", "3", "Missing_Sentence", "Medium",
 "‘Continue to marvel’ follows new discoveries about the builders.",
 steps(("Find the spot", p("Before blank 3: ‘Excavations since 1993 have uncovered additional temples and monuments that reveal the city’s rich traditions.’ The new sentence responds to those finds; the paragraph then moves to UNESCO and present-day threats.")),
       ("Check the others", p("Blank 1 comes before the site is described; blank 2 interrupts the description of monuments; blank 4 follows the threats."))) + final("Option 3"),
 "missing", [("1", "The site hasn’t been described yet."), ("2", "Mid-way through the monuments."), ("4", "After the modern challenges.")])

# ---------------- Passage 1 (Q2–5) ----------------
P.rc(2, "V1", "Detail", "1", "Easy",
 "Read the sentence after the one quoted.",
 steps(("The line", ev(2, "Hollywood has always developed projects based on existing literary works, and produced spin-offs on the back of successful TV shows and films") +
          p("Hollywood has always reused material, so fussing about IP now is naive."))) + final("Option 1"),
 "detail", [("2", "The author doesn’t see the deal as creative progress."), ("3", "The author’s worry, not the reason for this remark."), ("4", "‘Lost cause’ goes too far.")])
P.rc(3, "V1", "Main_Idea", "1", "Medium",
 "What does the author compare the deal with?",
 steps(("The argument", p("The deal fits a long Hollywood habit of reworking existing content, and the author fears AI will push it further: ‘ChatGPT-style film-making has, arguably, always been a feature of Hollywood in spirit, but now the technology has caught up.’")),
       ("Choosing", p("Option 1 states that continuity."))) + final("Option 1"),
 "inference", [("2", "‘Will lead’ is a certainty the author avoids; AI ‘could be a fascinating new generator of creativity’."), ("3", "The author is wary, not celebratory."), ("4", "The author fears a big impact.")])
P.rc(4, "V1", "Purpose", "1", "Medium",
 "What did the drinkers do about the gassy beer?",
 steps(("The line", ev(3, "comparable to the outrage seen in the early 70s among pub customers at the introduction of homogenous gassy, ghastly Double Diamond-type beer, which resulted in the Campaign for Real Ale") +
          p("Consumer revolt pushed back a mass-produced product. The author wants the same against AI content."))) + final("Option 1"),
 "purpose", [("2", "The opposite: it was rejected."), ("3", "The author doesn’t treat AI content as inevitable."), ("4", "The author calls for pushback; it isn’t predicted.")])
P.rc(5, "V1", "Weaken", "1", "Hard",
 "The author concedes AI ‘could be a fascinating new generator of creativity’. So which option actually cuts against the argument?",
 steps(("The argument", p("AI-made ‘proprietary schlock’ threatens original film-making, and audiences and critics must push back.")),
       ("Choosing", p("If audiences <i>and critics</i> warmly embrace films made entirely by AI, the premise that this is schlock to be resisted fails. Option 4 is a possibility the author already allows, so it doesn’t invalidate the argument.")),
       ("Why not 4", p("A surge of original AI films is the hopeful side the author mentions; it doesn’t remove the warning about corporate replication."))) + final("Option 1"),
 "weaken", [("2", "About CGI, not this argument."), ("3", "Supports the author’s hope for human-made film."), ("4", "A possibility the author already concedes.")])

P.va(6, P.sent_html(6), [], "TITA", "2", "Odd_One_Out", "Easy",
 "Four sentences are about the approval and what it means. One is a dosage instruction.",
 steps(("The chain", p("1 → 3 → 4 → 5: the FDA approves a new class of painkiller (1); trials show opioid-level relief without addiction (3); a milestone against the opioid crisis (4); an important step forward (5).")),
       ("The odd one", p("Sentence 2 gives the dose and schedule, a detail that doesn’t serve the significance the paragraph is about."))) + final("2"),
 "oddone", [("1", "The news."), ("3", "The evidence."), ("4", "Why it matters."), ("5", "The conclusion.")], why_title="How the other sentences fit")
P.va(7, P.summary_html(7, "To be in command"), P.Q["VARC"][7]["opts"], "MCQ", "3", "Summary", "Medium",
 "Old idea, new extreme: self-control was always tied to selfhood; now it means being responsible for outside events too.",
 steps(("Choosing", p("Option 3 keeps the historical link to selfhood and the modern demand to account for external events."))) + final("Option 3"),
 "summary", [("1", "Leaves out the historical link to selfhood."), ("2", "Leaves out the historical link."), ("4", "‘Unrealistic’ adds a judgment, and the history is missing.")])

# ---------------- Passage 2 (Q8–11) ----------------
P.rc(8, "V2", "Detail", "4", "Hard",
 "What reason follows ‘poor cousin’ directly?",
 steps(("The line", ev(1, "The knowledge it produces is indispensable for forming a complete and accurate picture of nature and our place in it") +
          p("Chemistry gives knowledge no other science supplies; paragraph 2 adds that new patterns emerge beyond single atoms, which physics can’t describe conveniently.")),
       ("Why not 1", p("That chemistry’s laws are as law-like as physics’ is the argument the passage builds later, to show the knowledge is lawful. The opening reason is that its patterns aren’t covered by other sciences."))) + final("Option 4"),
 "detail", [("1", "The later supporting argument, not the opening reason."), ("2", "Scales of complexity explain why the patterns are new, but this is the setting, not the reason."), ("3", "Practical usefulness isn’t the reason given.")])
P.rc(9, "V2", "Detail_Not_True", "3", "Easy",
 "Paragraph 3 defines laws.",
 steps(("The line", ev(3, "A law does not single out one specific event at one specific time; rather, it applies to all relevant instances") +
          p("Specificity is what laws lack."))) + final("Option 3"),
 "notrue", [("1", "Universality."), ("2", "Predictive power."), ("4", "Supporting counterfactuals.")])
P.rc(10, "V2", "Inference", "2", "Easy",
 "Why did Mendeleev’s table win?",
 steps(("The line", ev(2, "Mendeleev’s table prevailed because it could predict elements that were yet to be discovered"))) + final("Option 2"),
 "inference", [("1", "Not discussed."), ("3", "It reveals chemical patterns, not simplifications of physics."), ("4", "It embodies laws; it isn’t itself a law ‘like thermodynamics’.")])
P.rc(11, "V2", "Weaken", "3", "Medium",
 "The author’s case: chemistry states fundamental, law-like truths.",
 steps(("Undermining", p("If chemistry dealt mainly with practical applications and not fundamental truths, the claim that its regularities deserve to stand beside physics’ laws would fall."))) + final("Option 3"),
 "weaken", [("1", "Supports the argument."), ("2", "Supports it."), ("4", "The author calls the table more than a practical tool; this option is about tools, not truths.")])

# ---------------- Passage 3 (Q12–15) ----------------
P.rc(12, "V3", "Main_Idea", "3", "Medium",
 "‘Vast, repetitive, and utterly inconclusive’.",
 steps(("The theme", p("The passage surveys why definitions of life disagree: individuals or collectives, material or functional, sharp boundaries or a continuum, and eliminativist views. Option 3."))) + final("Option 3"),
 "inference", [("1", "One strand of the passage."), ("2", "The opening says most accept a real distinction."), ("4", "Scientists vs philosophers is a side remark.")])
P.rc(13, "V3", "Inference", "4", "Hard",
 "What does it mean for a definition to ‘presume a theory’?",
 steps(("Reading it", p("Like other theoretical terms, ‘life’ is defined by the theory that explains it, and that theory comes first. The comparison with ‘early chemical theory’ makes this point.")),
       ("Choosing", p("Option 4."))) + final("Option 4"),
 "inference", [("1", "Not about telling processes from abstractions."), ("2", "‘Over theoretical coherence’ isn’t implied."), ("3", "That is eliminativism, a different view.")])
P.rc(14, "V3", "Detail", "2", "Hard",
 "Parke maps the choices definitions make. One of those choices is between material and functional bases.",
 steps(("The line", ev(2, "Parke also points out that some definitions seek a material basis, perhaps limiting life’s substrate to the biochemistry we know on Earth, while others are functional") +
          p("Of the options, only 2 reflects her map: definitions differ in whether they rest on biology or function, and a full account needs both aspects.")),
       ("The others", p("Option 1 takes a side on boundaries she only reports; option 3 is one view she reports; option 4 is about universality, which is Sagan’s worry."))) + final("Option 2"),
 "detail", [("1", "She reports the boundary debate without taking a side."), ("3", "One position she lists, not hers."), ("4", "Not her point.")])
P.rc(15, "V3", "Inference_Except", "3", "Easy",
 "A ‘useful fiction’ is anything but a settled definition.",
 steps(("Reading it", p("Cowie’s phrase means nothing in the world matches the theoretical definition, but the concept is still handy (options 1, 2, 4).")),
       ("The odd one", p("Calling it ‘the only conclusive and consensual definition’ contradicts both the phrase and the passage’s point about disagreement."))) + final("Option 3"),
 "except", [("1", "Denies it exists as a category."), ("2", "Not a natural kind."), ("4", "Not real but useful.")])

# ---------------- Passage 4 (Q16–19) ----------------
P.rc(16, "V4", "Purpose", "2", "Medium",
 "Most of the passage is the Weidmann study and what it recommends.",
 steps(("The structure", p("A management question, poor current practice (no training, Peter Principle), the study’s findings, and a better way to choose managers: test the relevant skills.")),
       ("Choosing", p("Option 2."))) + final("Option 2"),
 "purpose", [("1", "The Ig Nobel frame is a bookend."), ("3", "Critique is part of it, but the passage proposes a method."), ("4", "Humour is the frame, not the subject.")])
P.rc(17, "V4", "Inference_Except", "1", "Medium",
 "Who was surveyed?",
 steps(("The line", ev(2, "four in every five people entering management had received no formal training") +
          p("People entering management, not ‘good managers’. Option 1 can’t be inferred.")),
       ("The others", p("Overconfident would-be managers did worse (2); promoting on past performance gives the Peter Principle (3); the self-promoters were mostly men (4)."))) + final("Option 1"),
 "except", [("2", "Teams led by eager self-promoters did worse."), ("3", "The Benson study and the Peter Principle."), ("4", "‘They also tended to be men.’")])
P.rc(18, "V4", "Application", "3", "Easy",
 "Star salespeople promoted, then their teams slip.",
 steps(("Choosing", p("This is the Benson finding: promoting on past performance ignores the skills a manager needs. Option 3."))) + final("Option 3"),
 "inference", [("1", "No company ‘openly follows’ the Peter Principle."), ("2", "Training is a separate issue."), ("4", "No deliberate testing.")])
P.rc(19, "V4", "Inference_Except", "3", "Easy",
 "The sentence defends funny research. Does it say anything about serious research?",
 steps(("Reading it", p("Humorous research can be valuable and deserves attention (options 1, 2, 4). Nothing is said about serious research overlooking practical matters."))) + final("Option 3"),
 "except", [("1", "Exactly the point."), ("2", "The random-promotion paper is an example."), ("4", "Worth scrutiny, not dismissal.")])

P.va(20, P.sent_html(20), [], "TITA", "4", "Odd_One_Out", "Easy",
 "The paragraph is about moths’ defence against bat echolocation.",
 steps(("The chain", p("1 → 2 → 3 → 5: bats hunt moths by echolocation (1); moths have sound-absorbing scales (2); this helps them evade bats (3); a study shows its role in the arms race (5).")),
       ("The odd one", p("Sentence 4, on bats using calls for social communication, is off the predator–prey thread."))) + final("4"),
 "oddone", [("1", "Bats and moths."), ("2", "The defence."), ("3", "How it helps."), ("5", "The study.")], why_title="How the other sentences fit")
P.va(21, P.missing_html(21), P.Q["VARC"][21]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "‘This discrepancy’ needs a discrepancy just before it.",
 steps(("Find the hook", p("Just before blank 3, the paragraph names the ‘Hubble tension’: 72 against 68 km/s/Mpc. The sentence comments on it, and the paragraph closes with continuing investigations.")),
       ("Match the label", p("Blank 3 is choice 1, labelled ‘Option 3’."))) + final("Choice 1 (“Option 3”)"),
 "missing", [("2", "“Option 2”: the 50-vs-100 debate is earlier history, not ‘the discrepancy’ the paragraph builds to."), ("3", "“Option 1”: no discrepancy has been mentioned."), ("4", "“Option 4”: after the closing sentence.")])
P.va(22, P.missing_html(22), P.Q["VARC"][22]["opts"], "MCQ", "4", "Missing_Sentence", "Medium",
 "The sentence opens the debate that the paragraph then sets out: supporters, then detractors.",
 steps(("Find the spot", p("Blank 2 comes right after the killing is described and before ‘The incident sparked worldwide outrage… Supporters of such hunting argue…’. The sentence frames that debate.")),
       ("Match the label", p("Blank 2 is choice 4, labelled ‘Option 2’."))) + final("Choice 4 (“Option 2”)"),
 "missing", [("1", "“Option 1”: before Cecil has been described."), ("2", "“Option 4”: the debate is already over by then."), ("3", "“Option 3”: between the two sides.")])
P.va(23, P.summary_html(23, "On one hand"), P.Q["VARC"][23]["opts"], "MCQ", "4", "Summary", "Hard",
 "Loss of history, and AI filling the gap with a self-feeding loop of errors.",
 steps(("Choosing", p("Option 4 has the erosion of digital history, AI filling the void, and the misinformation cycle."))) + final("Option 4"),
 "summary", [("1", "Leaves out the loop."), ("2", "Close, but misses that what is lost is history."), ("3", "‘Privacy’ is not in the passage.")])
P.va(24, P.summary_html(24, "Aphasia is a"), P.Q["VARC"][24]["opts"], "MCQ", "3", "Summary", "Medium",
 "Causes, effect on communication, and the existential questions.",
 steps(("Choosing", p("Option 3 has all three without narrowing to writers."))) + final("Option 3"),
 "summary", [("1", "Leaves out the communication impairment."), ("2", "Leaves out the specific questions about connection and identity."), ("4", "Leaves out causes and over-weights writers.")])
