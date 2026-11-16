# -*- coding: utf-8 -*-
# Simp Mock 16 (2025): VARC (24 of 24). DILR and QA: m25_16_dilr.py, m25_16_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(16, "sm25_16.json", series=2025)
P.passage("V1", "Passage 1 — The circuits of aggression", "Science_and_Technology")
P.passage("V2", "Passage 2 — What counts as a sign of alien life", "Science_and_Technology")
P.passage("V3", "Passage 3 — Indianization and Sinicization of Southeast Asia", "Social_Science_and_History")
P.passage("V4", "Passage 4 — Mathiness in economics", "Economics_and_Management")


def listed(n, direc):
    parts = [x.strip() for x in P.Q["VARC"][n]["q"].split("\n\n") if x.strip()]
    return f"<p>{direc}</p><ol class=\"sent\">" + "".join(f"<li>{x}</li>" for x in parts[1:]) + "</ol>"


# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Detail", "4", "Easy",
 "Read the answer to ‘What could scientists possibly find?’",
 steps(("The line", ev(2, "such investigations can shed light on how violence is controlled by the brain") +
          p("The study could reveal the brain circuits behind extreme aggression.")),
       ("Why not 1", p("Treatment is not mentioned as the aim."))) + final("Option 4"),
 "detail", [("1", "Treatment isn’t the stated aim."), ("2", "‘No genetic test for homicidal behavior exists’."), ("3", "Social isolation isn’t discussed.")],
 q="According to the passage, what could scientists hope to find by studying the brain of the gunman in the 2017 Las Vegas attack (“What could scientists possibly find?”)?")
P.rc(2, "V1", "Inference_Except", "1", "Medium",
 "Whose brain was stimulated in the experiment?",
 steps(("The experiment", ev(3, "When Hess stimulated this knot of neurons in a docile cat, it instantly launched into a hissing rage") +
          p("It was a cat’s brain. Humans have the same structure, but the experiment doesn’t show what stimulating a human brain does.")),
       ("The others", p("The same spot drives sex and eating (2), the rage came instantly (3), and aggression is shared across species for survival (4)."))) + final("Option 1"),
 "except", [("2", "‘the same spot where compulsive urges…’"), ("3", "‘instantly’."), ("4", "Survival across species.")])
P.rc(3, "V1", "Inference", "3", "Medium",
 "Which claim is the backbone of the passage?",
 steps(("The core", ev(5, "Physical aggression is life-threatening in any species, so it is tightly regulated and triggered only by specific threats") +
          p("Neural regulation of violence in animals and humans is the central thesis. If it were false, the argument would collapse.")),
       ("The others", p("Genetics (1), external triggers (2) and the usefulness of animal studies (4) are side points; disproving them would hurt less."))) + final("Option 3"),
 "inference", [("1", "A side remark."), ("2", "A secondary point."), ("4", "Supports the method, not the thesis.")])
P.rc(4, "V1", "Inference", "2", "Easy",
 "What does the fighting settle?",
 steps(("The line", ev(6, "Many animals are social, and aggression establishes order") +
          p("Head-butting decides breeding rights: aggression creates a social order."))) + final("Option 2"),
 "inference", [("1", "The opposite."), ("3", "It stabilises."), ("4", "Not said.")])

P.va(5, P.summary_html(5, "Of course capital punishment"), P.Q["VARC"][5]["opts"], "MCQ", "3", "Summary", "Medium",
 "No social rehabilitation, but a chance of spiritual rehabilitation.",
 steps(("The core", p("Execution doesn’t return a prisoner to society, but the time before it can bring remorse and spiritual rehabilitation; this isn’t an argument for the penalty.")),
       ("Choosing", p("Option 3 keeps the contrast and the hedge ‘can provide an opportunity’."))) + final("Option 3"),
 "summary", [("1", "‘leading to spiritual redemption’ overstates it."), ("2", "‘spiritualism’ and the focus on Aquinas."), ("4", "‘leads to’ drops ‘can’.")])

# ---------------- Passage 2 (Q6–9) ----------------
P.rc(6, "V2", "Purpose", "3", "Medium",
 "What did the telescope fail to find, and what does that show?",
 steps(("The context", ev(1, "failed to find an atmosphere around the rocky planet TRAPPIST-1 C") +
          p("Planets in a habitable zone may still lack atmospheres: assessing habitability is uncertain.")),
       ("Why not 4", p("Radiation stripping comes later as a possibility (‘may’), not as what these examples show."))) + final("Option 3"),
 "purpose", [("1", "Not a limitation of the telescope."), ("2", "The opposite."), ("4", "Too definite, and a later point.")])
P.rc(7, "V2", "Detail_Not_True", "2", "Easy",
 "Which item is a proposed solution, not an obstacle?",
 steps(("The line", ev(4, "Some scientists are developing agnostic biosignatures that don’t rely on Earth-like biochemistry") +
          p("Agnostic biosignatures are a remedy for Earth-centric assumptions.")),
       ("The others", p("Poor knowledge of alien geology (1), faint indirect signals (3) and missing time variation (4) are obstacles."))) + final("Option 2"),
 "except", [("1", "‘requiring a deeper understanding’."), ("3", "Barcode via starlight."), ("4", "Seasonal changes would strengthen claims.")])
P.rc(8, "V2", "Inference", "2", "Easy",
 "‘Agnostic’ about what?",
 steps(("The line", ev(4, "you’re assuming alien life is like Earth’s") +
          p("Agnostic markers drop that assumption: life elsewhere may use other chemistry."))) + final("Option 2"),
 "inference", [("1", "True of single gases, but not what ‘agnostic’ means."), ("3", "The opposite."), ("4", "Too sweeping.")])
P.rc(9, "V2", "Inference_Except", "4", "Easy",
 "Does any measure here prove life?",
 steps(("The caution", ev(6, "The search for exoplanet life won’t yield a smoking gun but will be a gradual accumulation of evidence") +
          p("A weirdness score points to candidates; it proves nothing.")),
       ("The others", p("Finding odd atmospheres (1, 3) and catching non-Earth-like life (2) are the benefits."))) + final("Option 4"),
 "except", [("1", "Its purpose."), ("2", "It is chemistry-agnostic."), ("3", "Focus on the weirdest.")])

P.va(10, P.ms(10), P.Q["VARC"][10]["opts"], "MCQ", "3", "Missing_Sentence", "Easy",
 "‘Ultimately’ signals a conclusion.",
 steps(("Find the spot", p("Blank 4 ends the paragraph after the two co-operative hits, and ‘these games’ refers to them.")),
       ("Match the label", p("Blank 4 is choice 3, labelled ‘Option 4’."))) + final("Choice 3 (“Option 4”)"),
 "missing", [("1", "“Option 3”: before the earlier hit is described."), ("2", "“Option 2”: the studio is just introduced."), ("4", "“Option 1”: still on competitive games.")])
P.va(11, P.summary_html(11, "As AI arises"), P.Q["VARC"][11]["opts"], "MCQ", "2", "Summary", "Medium",
 "Natural bioethics versus a human-made, unnatural thing.",
 steps(("The core", p("Bioethics has dealt with natural beings; AI is a human creation, and a bioethics of AI is needed so it doesn’t stray into harm.")),
       ("Choosing", p("Option 2 has the contrast and the purpose (preventing harm)."))) + final("Option 2"),
 "summary", [("1", "Misses the contrast with traditional bioethics."), ("3", "Built on AI’s lack of feeling."), ("4", "Misses the risk of harm.")])

# ---------------- Passage 3 (Q12–15) ----------------
P.rc(12, "V3", "Inference_Except", "4", "Medium",
 "Is native leadership said to have declined?",
 steps(("Supported", ev(2, "local syncretism often produced exuberant variations, which, despite familiar appearances, were expressions of local genius") +
          p("Merged traditions (1), local versions of imported styles (2), and rejected views of women (3).")),
       ("The odd one", p("Nothing says Chinese methods weakened native leadership; the passage stresses local agency."))) + final("Option 4"),
 "except", [("1", "‘exuberant variations’."), ("2", "‘more original, indigenous interpretations’."), ("3", "Views of women rejected.")])
P.rc(13, "V3", "Inference_Except", "4", "Medium",
 "Were local traditions erased?",
 steps(("The point", ev(2, "indigenous peoples shaped the adaption and adoption of outside influences") +
          p("Selective adoption, not erasure; Vietnam fought Chinese rule for generations.")),
       ("The others", p("A remote Han province (1), independence in 939 (2), and Vietnam taking the Chinese model (3: ‘only the Vietnamese accepted the Chinese model’)."))) + final("Option 4"),
 "except", [("1", "Paragraph 1."), ("2", "Paragraph 1."), ("3", "‘accepted the Chinese model’.")])
P.rc(14, "V3", "Purpose", "2", "Medium",
 "Imported forms, local grandeur.",
 steps(("The line", ev(3, "at first very much in the Indian image and hewing close to current styles and later in more original, indigenous interpretations") +
          p("The monuments show how far local adaptation of imported traditions went.")),
       ("Why not 4", p("Seriousness is mentioned, but the examples show grandeur and adaptation, not only how seriously rulers took influence."))) + final("Option 2"),
 "purpose", [("1", "These are Indian-influenced sites."), ("3", "Not mere copies."), ("4", "Narrower than the point.")])
P.rc(15, "V3", "Inference", "3", "Easy",
 "Conquest on one side, none on the other.",
 steps(("The line", ev(1, "From India, however, there is no evidence of conquests, colonization, or even extensive migration") +
          p("China ruled Vietnam directly; Indian ideas spread without rule."))) + final("Option 3"),
 "inference", [("1", "Reversed."), ("2", "Not stated."), ("4", "Different approaches to rule.")])

P.va(16, P.ms(16), P.Q["VARC"][16]["opts"], "MCQ", "2", "Missing_Sentence", "Easy",
 "‘This situation’ needs the 1.2% impact chance.",
 steps(("Find the spot", p("Blank 4 follows the predicted impact probability for 2032: the situation that calls for monitoring.")),
       ("Match the label", p("Blank 4 is choice 2, labelled ‘Option 4’."))) + final("Choice 2 (“Option 4”)"),
 "missing", [("1", "“Option 1”: only car-sized rocks so far."), ("3", "“Option 3”: before the trajectory."), ("4", "“Option 2”: before the risk is described.")])
P.va(17, listed(17, P.ODD_DIR), [], "TITA", "2", "Odd_One_Out", "Medium",
 "Definition, origins, a hypothesis, its mechanism.",
 steps(("The chain", p("5 → 3 → 1 → 4: definition; multifactorial origins; one hypothesis on receptor genes; how those variations act.")),
       ("The odd one", p("Sentence 2 talks about the difficulty of separating factors; ‘this combination’ has no clear place in the chain."))) + final("2"),
 "oddone", [("1", "The hypothesis."), ("3", "Origins."), ("4", "Mechanism."), ("5", "Definition.")], why_title="How the other sentences fit")

# ---------------- Passage 4 (Q18–21) ----------------
P.rc(18, "V4", "Main_Idea", "1", "Medium",
 "What turns a theory into pseudoscience, for the author?",
 steps(("The line", ev(4, "When mathematical theory becomes the ultimate arbiter of truth, distinguishing science from pseudoscience becomes difficult") +
          p("Mathematics used as a badge of legitimacy without empirical checks pushes economics towards pseudoscience.")),
       ("The others", p("Biases (2) and sunk costs (3) are reasons it persists; the astrology parallel (4) is an analogy."))) + final("Option 1"),
 "summary", [("2", "A supporting point."), ("3", "A supporting point."), ("4", "An analogy.")])
P.rc(19, "V4", "Purpose", "4", "Medium",
 "What does the author call this veneration?",
 steps(("The line", ev(1, "This veneration of mathematics leads to a method that often subverts empirical science") +
          p("The quote shows maths used to look rigorous while hiding weaknesses."))) + final("Option 4"),
 "purpose", [("1", "Too general."), ("2", "Restates the quote rather than its role."), ("3", "Not the point.")])
P.rc(20, "V4", "Application", "3", "Medium",
 "Trust in tradition when no scientific test existed.",
 steps(("The line", ev(1, "They had no way to evaluate scientific merit—‘science’ in its modern sense didn’t exist") +
          p("An emperor trusting court soothsayers by tradition matches.")),
       ("Why not 1", p("‘despite the absence of systematic verification’ suggests a test was possible; option 3 keeps the reliance on tradition."))) + final("Option 3"),
 "inference", [("1", "Weaker match."), ("2", "Science exists there."), ("4", "The opposite.")])
P.rc(21, "V4", "Purpose", "3", "Easy",
 "Why is admitting failure painful?",
 steps(("The line", ev(3, "If you’ve invested heavily in a flawed model, admitting its failures is painful") +
          p("Reluctance to admit mistakes keeps failed models alive."))) + final("Option 3"),
 "purpose", [("1", "Close, but the passage stresses admitting failure."), ("2", "That is the conflict-of-interest point."), ("4", "Not about complexity.")])

P.va(22, P.summary_html(22, "All animals have the ability"), P.Q["VARC"][22]["opts"], "MCQ", "1", "Summary", "Medium",
 "Simple pitched sounds count as music for both ethnomusicologists and biologists.",
 steps(("The core", p("Since simple pitched vocalisations count as music, vocal music may go back to the earliest humans.")),
       ("Choosing", p("Option 1 keeps the hedge (‘may have’) and both disciplines."))) + final("Option 1"),
 "summary", [("2", "‘intricate’ contradicts the passage."), ("3", "‘lyrical’ and too certain."), ("4", "‘uniformly recognized’ is too absolute.")])
P.va(23, P.ms(23), P.Q["VARC"][23]["opts"], "MCQ", "3", "Missing_Sentence", "Medium",
 "‘This simplistic label’ needs an example of arbitrary labelling right before it.",
 steps(("Find the spot", p("Blank 3 comes after the critiques of steps and heating and before ‘This simplistic label of ultra-processed food’, which the bread example sets up.")),
       ("Match the label", p("Blank 3 is choice 3."))) + final("Option 3"),
 "missing", [("1", "Before the system is critiqued."), ("2", "Between the step critique and heating."), ("4", "Among the consequences.")])
P.va(24, listed(24, P.ODD_DIR), [], "TITA", "3", "Odd_One_Out", "Medium",
 "Challenge, vulnerability, extremes, water stress.",
 steps(("The chain", p("5 → 2 → 1 → 4: adaptation will be hard; India is poorer, hotter and crowded; extreme weather in 2024; water stress adds a layer.")),
       ("The odd one", p("Sentence 3 is about an unknown death toll and an election-day incident, a turn away from adaptation."))) + final("3"),
 "oddone", [("1", "Evidence."), ("2", "Context."), ("4", "Another layer."), ("5", "Opening.")], why_title="How the other sentences fit")
