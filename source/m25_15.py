# -*- coding: utf-8 -*-
# Simp Mock 15 (2025): VARC (24 of 24). DILR and QA: m25_15_dilr.py, m25_15_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(15, "sm25_15.json", series=2025)
P.passage("V1", "Passage 1 — Assembly theory and the line between life and non-life", "Science_and_Technology")
P.passage("V2", "Passage 2 — Where language ideology comes from", "Philosophy_and_Psychology")
P.passage("V3", "Passage 3 — Archiving authoritarianism", "Social_Science_and_History")
P.passage("V4", "Passage 4 — The theological roots of naturalism", "Philosophy_and_Psychology")


def listed(n, direc):
    parts = [x.strip() for x in P.Q["VARC"][n]["q"].split("\n\n") if x.strip()]
    return f"<p>{direc}</p><ol class=\"sent\">" + "".join(f"<li>{x}</li>" for x in parts[1:]) + "</ol>"


# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Inference_Except", "3", "Medium",
 "Is Walker confirming the current picture of life, or replacing it?",
 steps(("The context", ev(3, "She was struck by how difficult it was to explain life with standard physics theories") +
          p("Walker thinks current theory can’t explain life; her lab prediction rests on a new way to measure and build complexity.")),
       ("The others", p("Making life from inert chemicals (1), moving the search into the lab (2) and measuring and recreating complexity (4) all follow from the remark."))) + final("Option 3"),
 "except", [("1", "The ‘origin-of-life engine’."), ("2", "‘in the lab first’."), ("4", "The assembly index.")])
P.rc(2, "V1", "Detail_Not_True", "4", "Medium",
 "Which objection is about the procedure, not the idea?",
 steps(("Critiques given", ev(7, "Hazen’s team found minerals scoring up to 30, challenging the proposed cutoff") +
          p("An arbitrary threshold (1), complexity outside life (2), and Redfield’s dismissal of a complexity-only definition (3).")),
       ("The odd one", p("No one in the passage questions how hard the measurement is; the laser method is described without objection."))) + final("Option 4"),
 "except", [("1", "Hazen on the threshold."), ("2", "Minerals scoring 30."), ("3", "Redfield’s ‘nonsense’.")])
P.rc(3, "V1", "Inference", "4", "Easy",
 "What does absolute zero give a thermometer?",
 steps(("The line", ev(3, "Scientists had no way to measure how life-like a group of chemicals were, similar to how a thermometer measures temperature") +
          p("Absolute zero is an analogy for a fixed reference point; without one, a scale for ‘life-likeness’ means nothing."))) + final("Option 4"),
 "inference", [("1", "Too sweeping about physics."), ("2", "Takes the analogy literally."), ("3", "Absolute zero isn’t the reference for the index.")])
P.rc(4, "V1", "Weaken", "2", "Easy",
 "Her claim rests on a cutoff of 15.",
 steps(("The claim", ev(6, "an assembly index above 15 could signify a threshold for life") +
          p("Non-living minerals scoring well above 15 would break the line between life and non-life."))) + final("Option 2"),
 "weaken", [("1", "High scores for life support the idea."), ("3", "Hurts the method, but less directly than a counterexample to the threshold."), ("4", "Fits the theory.")])

P.va(5, listed(5, P.PJ_DIR), [], "TITA", "4132", "Para_Jumble", "Easy",
 "Flaw, misleading picture, how it misleads, consequence.",
 steps(("Opening", p("4 states the problem: the poverty line doesn’t reflect real costs.")),
       ("Links", p("1 (‘As a result’) gives the over-optimistic picture; 3 explains how undercounting hides systemic issues; 2 (‘In turn’) ends with the lost urgency for reform."))) + final("4132"),
 "pj", [("1", "‘As a result’ needs a cause."), ("2", "‘In turn’ needs a prior effect."), ("3", "‘the outdated measure’ needs the measure first.")], why_title="Why the others can’t open")
P.va(6, P.ms(6), P.Q["VARC"][6]["opts"], "MCQ", "1", "Missing_Sentence", "Easy",
 "‘The results were clear’ follows the method of the second study.",
 steps(("Find the spot", p("Blank 3 comes after the second study’s method (preferences, accelerometers, health records) and before ‘The worst outcomes…’, which develops the results.")),
       ("Match the label", p("Blank 3 is choice 1, labelled ‘Option 3’."))) + final("Choice 1 (“Option 3”)"),
 "missing", [("2", "“Option 2”: the second study is only just introduced."), ("3", "“Option 1”: the first study hasn’t been described yet."), ("4", "“Option 4”: the closing line is already in place.")])

# ---------------- Passage 2 (Q7–10) ----------------
P.rc(7, "V2", "Main_Idea", "2", "Hard",
 "The gist needs the synthesis and what language does in it.",
 steps(("The scope", ev(4, "Thus, human communication through language contains sociopolitical, ideological meaning") +
          p("The passage traces Marxian, Durkheimian and semiotic roots, and shows language as a site of struggle, power and cultural meaning.")),
       ("Choosing", p("Option 2 keeps the blend and the roles of language. Option 1 names only two ancestors; option 3 drops the field and its traditions."))) + final("Option 2"),
 "summary", [("1", "Leaves out semiotics and the role of language."), ("3", "Too general."), ("4", "‘separating’ inverts the passage.")])
P.rc(8, "V2", "Main_Idea", "3", "Easy",
 "‘Still under construction’.",
 steps(("The line", ev(1, "Though the field is still under construction, its influence on linguistic anthropology, linguistics, discourse analysis, and sociolinguistics is considerable") +
          p("A young field joining linguistic ethnography with the social science of ideology."))) + final("Option 3"),
 "inference", [("1", "Not yet well established."), ("2", "Marxism is one of several roots."), ("4", "Nothing argues for separation.")])
P.rc(9, "V2", "Inference_Except", "1", "Easy",
 "Is language neutral, for Bakhtin and Voloshinov?",
 steps(("The line", ev(4, "Bakhtin and Voloshinov saw language as embodying social struggle and conflict, making the linguistic sign deeply ideological") +
          p("Language is far from a neutral carrier.")),
       ("The others", p("Two perspectives (2), semiotics and ethnography (3), and a contested history in scholarship and politics (4) are all in the passage."))) + final("Option 1"),
 "except", [("2", "Paragraphs 2–3."), ("3", "Peirce and Silverstein."), ("4", "‘Nested in scholarship and politics’.")])
P.rc(10, "V2", "Application", "4", "Medium",
 "A symbol represents by convention.",
 steps(("The definition", ev(5, "‘symbols’ (conventionally representing objects)") +
          p("A standard dialect chosen to stand for the nation represents it by convention and carries an ideological load.")),
       ("The others", p("Gestures for needs (1), switching languages (2) and coining technical terms (3) are practical, with no ideological symbol."))) + final("Option 4"),
 "inference", [("1", "Practical communication."), ("2", "Code-switching."), ("3", "Clarity, not ideology.")])

P.va(11, listed(11, P.PJ_DIR), [], "TITA", "1432", "Para_Jumble", "Easy",
 "Assumption, its hubristic extreme, ‘But’, conclusion.",
 steps(("Opening", p("1 states the assumption of tidy rules.")),
       ("Links", p("4 pushes it to the hubristic extreme; 3 (‘But reality defies such neat control’) turns; 2 sums up."))) + final("1432"),
 "pj", [("2", "A conclusion."), ("3", "‘But’ needs a claim to contradict."), ("4", "‘The hubristic view’ builds on an assumption already made.")], why_title="Why the others can’t open")

# ---------------- Passage 3 (Q12–15) ----------------
P.rc(12, "V3", "Detail_Not_True", "1", "Easy",
 "Does erasure serve public access?",
 steps(("The point", ev(1, "Authoritarians wield their power to silence dissent, suppress disfavored narratives, cover up misdeeds") +
          p("Erasure removes records; nothing about managing archives for the public.")),
       ("The others", p("Rewriting history (2), silencing critics (3) and wiping inconvenient evidence (4) are all named."))) + final("Option 1"),
 "except", [("2", "Tiananmen, Sichuan."), ("3", "Exiled journalists."), ("4", "AI-driven censorship.")])
P.rc(13, "V3", "Detail_Not_True", "3", "Easy",
 "What do governments use AI for?",
 steps(("The line", ev(6, "Automation and AI facilitate targeted censorship, erasing inconvenient narratives while promoting approved messages") +
          p("Governments use AI to erase, not to restore.")),
       ("The others", p("Independent archives (1), international support (2) and exiled journalists’ records (4) appear in the last paragraph."))) + final("Option 3"),
 "except", [("1", "China Digital Times, GreatFire.org."), ("2", "‘More systematic international support’."), ("4", "Russian Independent Media Archive.")])
P.rc(14, "V3", "Inference", "4", "Medium",
 "How do archives help defeat a regime?",
 steps(("The support", ev(4, "Historical records of authoritarian regimes have proven essential in holding these regimes accountable") +
          p("Archives preserve evidence of oppression, used in trials and exposés.")),
       ("Why not 2", p("True of regimes, but it’s about their view, not what follows from archiving."))) + final("Option 4"),
 "inference", [("1", "Beyond the statement."), ("2", "About regimes, not archives."), ("3", "The UK example contradicts it.")])
P.rc(15, "V3", "Weaken", "4", "Medium",
 "What makes erasure powerful in the first place?",
 steps(("The core", ev(1, "Repressive governments can make websites, archives, and social media accounts disappear instantly") +
          p("The power of erasure depends on deleted content staying gone. If it were recoverable, the tool would lose its force.")),
       ("Why not 1", p("‘Completely wipe’ is close, but option 4 states the dependence directly: suppression is effective because deletion is permanent."))) + final("Option 4"),
 "weaken", [("1", "Limits reach, less directly."), ("2", "Speed and scale, not the core."), ("3", "A comparison with old methods.")])

P.va(16, P.summary_html(16, "Naming a drug"), P.Q["VARC"][16]["opts"], "MCQ", "3", "Summary", "Medium",
 "Recognisable names, but not so recognisable that the trademark is lost.",
 steps(("The core", p("A good drug name is recognisable, but too much success risks ‘genericide’, the loss of the trademark.")),
       ("Choosing", p("Option 3 names both sides: recognisability and legal protection."))) + final("Option 3"),
 "summary", [("1", "Misses the trademark risk."), ("2", "‘market reputation’ isn’t the risk."), ("4", "‘overexposed’ distorts it.")])

# ---------------- Passage 4 (Q17–20) ----------------
P.rc(17, "V4", "Main_Idea", "4", "Medium",
 "What does the author call ‘half true’ and ‘selective’?",
 steps(("The line", ev(1, "But that version is, at best, half true") +
          p("The target is the tidy story of science freeing itself from religion; Huxley’s history ‘was selective’.")),
       ("Why not 1", p("The author does question naturalism’s neutrality, but only as part of correcting the history."))) + final("Option 4"),
 "purpose", [("1", "A consequence, not the main target."), ("2", "The author affirms it."), ("3", "The author affirms it.")])
P.rc(18, "V4", "Detail_Not_True", "3", "Medium",
 "Were natural laws brute facts for them?",
 steps(("The line", ev(3, "laws of nature were originally seen as divine volitions rather than brute, intrinsic facts") +
          p("Option 3 describes the later naturalist view, not theirs.")),
       ("The others", p("Acts of God (1), religion as foundational (2), and laws replacing inner powers (4) are all stated."))) + final("Option 3"),
 "except", [("1", "Motion as recreation by God."), ("2", "‘foundational to their work’."), ("4", "Paragraph 1.")])
P.rc(19, "V4", "Purpose", "1", "Hard",
 "Read the question in the sense of paragraph 1: away from powers inside things.",
 steps(("The shift", ev(1, "they divested natural objects of inherent causal virtues and instead attributed all change to natural laws") +
          p("Descartes and Newton mark the move from Aristotelian inner powers to change governed by laws: nature run by laws rather than by agents within objects.")),
       ("The others", p("Their faith matters to their science, not their private lives (2); there was no split (3); observation isn’t the point (4)."))) + final("Option 1"),
 "purpose", [("2", "Not about personal lives."), ("3", "The passage denies a split."), ("4", "Not discussed.")])
P.rc(20, "V4", "Tone", "2", "Easy",
 "‘Yet Huxley’s history was selective’.",
 steps(("The line", ev(2, "Yet Huxley’s history was selective") +
          p("The author doubts their account because it leaves out the religious commitments of the founders."))) + final("Option 2"),
 "inference", [("1", "The author isn’t appreciative."), ("3", "The author evaluates."), ("4", "‘completely ignoring’ and ‘undermined progress’ overstate it.")])

P.va(21, P.summary_html(21, "The introduction of tiny"), P.Q["VARC"][21]["opts"], "MCQ", "1", "Summary", "Medium",
 "Health threat plus the shift to land-based sources.",
 steps(("The core", p("Airborne microplastics threaten health, especially breathing; a new study says land, not sea, should be the first target for mitigation.")),
       ("Choosing", p("Option 1 has both."))) + final("Option 1"),
 "summary", [("2", "Only the harm."), ("3", "Drops the harm."), ("4", "Misses land-based sources.")])
P.va(22, P.summary_html(22, "Somatic sensations have"), P.Q["VARC"][22]["opts"], "MCQ", "2", "Summary", "Hard",
 "‘Mineness’ is stronger for touch than for the exteroceptive senses.",
 steps(("The core", p("Touch carries a feeling of ‘mineness’ more strongly than hearing or sight, building a continuous bodily self.")),
       ("Choosing", p("Option 2 keeps the contrast with exteroceptive senses. Options 1 and 4 drop it."))) + final("Option 2"),
 "summary", [("1", "‘personal identity’ goes beyond the passage."), ("3", "‘extraneous experiences’ misreads ‘exteroceptive’."), ("4", "Misses the contrast.")])
P.va(23, P.ms(23), P.Q["VARC"][23]["opts"], "MCQ", "3", "Missing_Sentence", "Easy",
 "‘This shift’ needs the shift described just before.",
 steps(("Find the spot", p("Blank 3 follows ‘The talent that once powered innovation… now flows into finance’, and the next line explains why it matters.")),
       ("Match the label", p("Blank 3 is choice 3, labelled ‘Option 3’."))) + final("Choice 3 (“Option 3”)"),
 "missing", [("1", "“Option 4”: after the call to action."), ("2", "“Option 1”: the shift isn’t described yet."), ("4", "“Option 2”: the paragraph is still describing the trend.")])
P.va(24, P.ms(24), P.Q["VARC"][24]["opts"], "MCQ", "2", "Missing_Sentence", "Medium",
 "A present-tense claim about significance.",
 steps(("Find the spot", p("Blank 4 follows ‘a bold step toward new transportation modes’ and leads into ‘may completely change how we all move in cities’. The earlier blanks are in the narrative of the test.")),
       ("Match the label", p("Blank 4 is choice 2, labelled ‘Option 4’."))) + final("Choice 2 (“Option 4”)"),
 "missing", [("1", "“Option 1”: the car is barely introduced."), ("3", "“Option 3”: between ‘unique’ and the earlier attempts."), ("4", "“Option 2”: mid-test description.")])
