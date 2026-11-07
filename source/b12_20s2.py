# -*- coding: utf-8 -*-
# Batch 12 — CAT 2020 Slot 2: VARC (26 of 26). DILR and QA: b12_20s2_dilr.py, b12_20s2_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2020, 2, "ex12_20s2.json")
P.passage("P1", "Passage 1 — The study of visual culture", "Arts_and_Literature")
P.passage("P2", "Passage 2 — The costs of renewable energy", "Environment_and_Life_Science")
P.passage("P3", "Passage 3 — Piracy past and present", "Social_Science_and_History")
P.passage("P4", "Passage 4 — Theories of aggression", "Philosophy_and_Psychology")

# ---------------- Verbal ability (Q1) ----------------
P.va(1, P.sent_html(1), [], "TITA", "2143", "Para_Jumble", "Medium",
 "Sentence 4 begins ‘When these are combined’. Which telescopes are ‘these’?",
 steps(("The opener", p("Sentence 2 introduces the Very Large Telescope and its four main telescopes.")),
       ("Building up", p("Sentence 1 adds the four auxiliary telescopes. Sentence 4 says what happens when “these” are combined with the large ones: interferometry. Sentence 3 gives the result of “this configuration”."))) +
 final("2143"),
 "pj",
 [("2", "The VLT."), ("1", "“It also has” auxiliary telescopes."), ("4", "Combining them: interferometry."), ("3", "What this configuration can do.")],
 why_title="Why each sentence goes where it does")

# ---------------- Passage 1: Visual culture ----------------
P.rc(2, "P1", "Inference", "4", "Medium",
 "‘Covenants’ are agreements. Who makes them with whom?",
 steps(("Reading it", p("We see meaningfully because of shared conventions, agreements we hold with images about what they mean. Option 4 says this.")),
       ("Why not the others", p("Options 1–3 rearrange the words without the sense: the covenants are ours, not ‘in images’ or ‘seeing them’."))) +
 final("Option 4"),
 "inference",
 [("1", "Puts the covenants inside the images."), ("2", "Images aren’t ‘operated on’ by covenants."), ("3", "Covenants don’t see images.")])

P.rc(3, "P1", "Except", "4", "Medium",
 "Does the passage say institutions are needed to analyse perception?",
 steps(("What the passage says", p("Institutions are among the things images are put to work in. The passage never says studying perception requires institutional structures.")),
       ("The others", p("Artifacts constructing a world (option 1), visual practice changing worlds (option 2), and studying the structures of perception (option 3) all come from the passage."))) +
 final("Option 4"),
 "except",
 [("1", "¶4: “how artifacts contribute to the construction of a world”."), ("2", "¶1: images build, maintain or transform worlds."), ("3", "¶5: scrutinise the constituents of vision.")])

P.rc(4, "P1", "Vocabulary", "4", "Medium",
 "The sentence contrasts epiphenomena with ‘evidence for explanation’.",
 steps(("Reading it", p("An epiphenomenon is a by-product, something secondary. The author wants images treated as evidence, not as something merely added on to the evidence.")),
       ("Choosing", p("Phenomena supplemental to the evidence."))) +
 final("Option 4"),
 "inference",
 [("1", "Not about collections."), ("2", "The opposite: these are what the author wants images to be."), ("3", "‘Epi’ isn’t ‘epic’.")])

P.rc(5, "P1", "Inference", "3", "Easy",
 "What can’t social analysis account for?",
 steps(("The point", p("Their genius can’t be fully explained by social analysis, though the reception of their work can be studied.")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "They can be studied socially; just not fully explained."), ("2", "Not what the sentence says."), ("4", "Garbles the sentence.")])

P.rc(6, "P1", "Main_Idea", "2", "Medium",
 "The passage lists four concerns for scholars of visual culture. Which option names them?",
 steps(("The concerns", p("All imagery; visual practice; lifeworlds; the constituents of vision (structures of perception).")),
       ("Choosing", p("Option 2 lists exactly these."))) +
 final("Option 2"),
 "inference",
 [("1", "Details and names."), ("3", "Genius and epiphenomena are side points."), ("4", "Aesthetic value is what the author says not to restrict oneself to.")])

# ---------------- Verbal ability (Q7–8) ----------------
P.va(7, P.sent_html(7), [], "TITA", "2", "Odd_One_Out", "Hard",
 "Four sentences are about information as property versus information as abundant. One talks about a new kind of capitalism in general.",
 steps(("The chain", p("3 → 1 → 5 → 4: Arrow says inventions exist to create property rights (3), e-business shows it (1), yet information is abundant (5), and a different dynamic is growing (4).")),
       ("The odd one", p("Sentence 2 makes a broad claim about a new capitalism. The paragraph is specifically about information and ownership."))) +
 final("2"),
 "oddone",
 [("3", "Arrow’s view."), ("1", "E-business proves it."), ("5", "“Yet” information is abundant."), ("4", "A different dynamic.")],
 why_title="How the other sentences fit")

P.va(8, P.sent_html(8), [], "TITA", "2413", "Para_Jumble", "Medium",
 "Sentence 1 begins with ‘But’, and sentence 3 with ‘however’. Which is the contrast to which?",
 steps(("The opener", p("Sentence 2: nuclear fission is the most dangerous change man has introduced.")),
       ("The sequence", p("Sentence 4: the resulting radiation is the gravest pollutant. Sentence 1: but the public notices only the bomb. Sentence 3: the peaceful uses, however, may be far more dangerous."))) +
 final("2413"),
 "pj",
 [("2", "Fission is the most dangerous change."), ("4", "Its radiation."), ("1", "“But” the public watches the bomb."), ("3", "“However”: peaceful uses are worse.")],
 why_title="Why each sentence goes where it does")

# ---------------- Verbal ability (Q9–10) ----------------
P.va(9, P.sent_html(9), [], "TITA", "4", "Odd_One_Out", "Hard",
 "Four sentences are about how stories of assault are told and what they leave out. One is about the questions put to victims.",
 steps(("The chain", p("5 → 2 → 1 → 3: stories of assault have become a genre (5); in these narratives we give perpetrators futures and victims pasts (2); the victim’s life after the assault gets little attention next to the moment of damage (1); one result is that we lack words for the victim’s life afterwards (3).")),
       ("The odd one", p("Sentence 4 is about questioning victims to understand or corroborate details. That is about investigation, not about how the stories are told, and nothing before or after it picks it up."))) +
 trap("Sentence 5 can look like loose background, but it brings in the ‘narratives’ that sentence 2 talks about. Without it the paragraph has no subject.") +
 final("4 (official answer)"),
 "oddone",
 [("5", "Opens: these stories have become a genre."), ("2", "Narratives sort perpetrators into futures and victims into pasts."), ("1", "Expands on the victims’ past: attention goes to the moment of damage."), ("3", "“One result”: no vocabulary for life afterwards.")],
 why_title="How the other sentences fit")

P.va(10, P.sent_html(10), [], "TITA", "1342", "Para_Jumble", "Medium",
 "Sentence 3 begins with ‘It’. What is ‘it’?",
 steps(("The opener", p("Sentence 1: you may think you notice every change around you, but there is too much information for your brain to process.")),
       ("The sequence", p("Sentence 3: ‘It’ (your brain) can’t be aware of everything. Sentence 4: so big shifts can happen without your noticing. Sentence 2: psychologists call ‘this tendency’ change blindness."))) +
 final("1342"),
 "pj",
 [("1", "Too much information for the brain."), ("3", "“It” is the brain."), ("4", "The result: big changes go unnoticed."), ("2", "“This tendency” gets its name.")],
 why_title="Why each sentence goes where it does")

# ---------------- Verbal ability (Q11) ----------------
P.va(11, P.summary_html(11, "All humans make decisions"), P.Q["VARC"][11]["opts"], "MCQ", "2", "Summary", "Medium",
 "The passage compares the two kinds of decision; it doesn’t say which is better.",
 steps(("What the passage says", "<ol><li>Decisions come from intuition or information.</li><li>Intuitive ones are fast but hard to explain.</li><li>Information-based ones are slow but can be explained.</li></ol>"),
       ("Choosing", p("Option 2 keeps the comparison on speed and explanation."))) +
 final("Option 2"),
 "summary",
 [("1", "The passage doesn’t say one is better."), ("3", "Time available isn’t the basis."), ("4", "Covers only intuition.")])

# ---------------- Passage 2: Renewables ----------------
P.rc(12, "P2", "Main_Idea", "2", "Medium",
 "The last paragraph says renewables offer a possibility, not a certainty.",
 steps(("The paragraph", ev(4, "renewable energy systems offer a possibility but not a certainty for more democratic energy futures") +
          p("Renewables could democratise energy, but profits pull towards concentration.")),
       ("Choosing", p("A double-edged sword."))) +
 final("Option 2"),
 "inference",
 [("1", "Efficiency isn’t discussed."), ("3", "The passage doesn’t say corporate control makes them democratic."), ("4", "Small-scale ones are less profitable; the passage doesn’t say most are unprofitable.")])

P.rc(13, "P2", "Inference", "3", "Easy",
 "The first paragraph says renewables need scrutiny.",
 steps(("The relevant line", ev(1, "But renewables need to be further scrutinized before being championed as forging a path towards a low-carbon future.")),
       ("Choosing", p("The author has reservations about renewables’ consequences."))) +
 final("Option 3"),
 "inference",
 [("1", "The paragraph is about renewables."), ("2", "Profit is one of several concerns."), ("4", "Efficiency isn’t raised.")])

P.rc(14, "P2", "Inference", "2", "Medium",
 "‘If false, supports’: find what the passage denies.",
 steps(("The passage", p("Renewables impose costs on people and the environment: dispossession, mining, waste.")),
       ("Choosing", p("If “renewables have little or no environmental impact” is false, that fits the passage."))) +
 final("Option 2"),
 "inference",
 [("1", "Cost relative to non-renewables isn’t argued."), ("3", "Profit compared with non-renewables isn’t argued."), ("4", "The passage roughly agrees, so its being false wouldn’t help.")])

P.rc(15, "P2", "Except", "3", "Hard",
 "Three options restate claims in the passage. One adds a recommendation the passage doesn’t make.",
 steps(("The claims made", p("Marginalised people suffer from extraction (option 1); agricultural finance shows concentration drives profit (option 2); toxic waste perpetuates injustice (option 4).")),
       ("The odd one", p("The passage says renewables need scrutiny before being championed as a path to a low-carbon future. It doesn’t tie that scrutiny to their being offered as investments. This is the official answer."))) +
 final("Option 3"),
 "except",
 [("1", "¶2: minerals under marginalised communities."), ("2", "¶4: concentration of control facilitates profit."), ("4", "¶3: waste flows perpetuate injustice.")])

P.rc(16, "P2", "Application", "4", "Medium",
 "Which harm does the author describe most directly as an injustice?",
 steps(("The relevant line", ev(3, "The disposal of toxic waste has long perpetuated social injustice through the flows of waste to the Global South")),
       ("Choosing", p("Stricter rules for fair waste disposal address a harm the author names. The author is cautious about small-scale systems’ prospects and doesn’t argue for carbon fuels."))) +
 final("Option 4"),
 "inference",
 [("1", "The author isn’t promoting carbon-based fuels."), ("2", "Not the passage’s concern."), ("3", "The author notes these are unlikely to attract capital; he doesn’t champion them.")])

# ---------------- Passage 3: Piracy ----------------
P.rc(17, "P3", "Tone", "1", "Medium",
 "The question answers itself. What does that suggest about the tone?",
 steps(("Reading it", p("The rhetorical question makes piracy sound like the obvious choice. It is wry about why so many became pirates.")),
       ("Choosing", p("Ironic."))) +
 final("Option 1"),
 "inference",
 [("2", "It isn’t an analysis of contrasts."), ("3", "No indignation."), ("4", "It isn’t mocking the peasants’ hardship.")])

P.rc(18, "P3", "Inference", "3", "Medium",
 "The previous paragraph compares emperors with pirates.",
 steps(("The relevant line", ev(2, "By this logic, European empire-builders were the most successful pirates of all time.")),
       ("Choosing", p("The author thinks colonialism can be seen as organised piracy."))) +
 final("Option 3"),
 "inference",
 [("1", "No comparison of skill."), ("2", "Not claimed."), ("4", "The author notes Lehr’s scope, not his blame.")])

P.rc(19, "P3", "Inference", "1", "Medium",
 "What are the ‘root causes’ of piracy, according to Lehr?",
 steps(("The relevant line", ev(4, "where abject poverty and the daily struggle for survival are still a reality, the root causes of piracy are still the same")),
       ("Choosing", p("In the long run, remove poverty and disparity. Patrols and technology are shown to fail."))) +
 final("Option 1"),
 "inference",
 [("2", "Welfare helped in Malaysia but depended on money reaching the poor; ‘lucrative’ misstates it."), ("3", "Diplomacy is plagued by distrust."), ("4", "Technology only shifts the targets.")])

P.rc(20, "P3", "Except", "3", "Medium",
 "Is there a claim that surveillance has decreased?",
 steps(("What the passage says", p("Ransoms (Le Ponant), more shipping, and colonialism disturbing power balances are all named. The passage says there are never enough warships, not that surveillance has fallen.")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "except",
 [("1", "The $2 million ransom drew opportunists."), ("2", "“A rise in global shipping has meant rich pickings.”"), ("4", "“European colonialism weakened delicate balances of power.”")])

# ---------------- Verbal ability (Q21–22) ----------------
P.va(21, P.summary_html(21, "The rural-urban continuum"), P.Q["VARC"][21]["opts"], "MCQ", "3", "Summary", "Medium",
 "Fixed metrics miss the diversity; a richer set of criteria needs human judgement.",
 steps(("What the passage says", "<ol><li>Urban settings are diverse, so one or two fixed metrics fall short.</li><li>Richer criteria would help, but interpreting them needs judgement.</li></ol>"),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "summary",
 [("1", "‘No longer relevant’ goes too far."), ("2", "The judgement is in interpreting criteria, not in judging the methodology."), ("4", "Leaves out the human judgement.")])

P.va(22, P.summary_html(22, "With the Treaty of Westphalia"), P.Q["VARC"][22]["opts"], "MCQ", "2", "Summary", "Medium",
 "People give up rights in return for security: an exchange.",
 steps(("What the passage says", "<ol><li>After Westphalia, a theory of secular order was needed.</li><li>Hobbes: people handed rights to a sovereign in return for security.</li></ol>"),
       ("Choosing", p("Option 2 has the exchange and the insecurity behind it."))) +
 final("Option 2"),
 "summary",
 [("1", "Sovereign equality isn’t what the people sought."), ("3", "Leaves out what they got in return."), ("4", "Hobbes’s aim wasn’t to limit the papacy.")])

# ---------------- Passage 4: Aggression ----------------
P.rc(23, "P4", "Except", "3", "Hard",
 "The passage mentions low neural inhibition and testosterone separately. Does it link them?",
 steps(("What the passage says", p("Humans have abnormally low neural inhibition of aggressive impulses; separately, testosterone increases aggression. Option 3 merges the two into ‘low neural regulation of testosterone’, which the passage doesn’t say.")),
       ("The others", p("The avoidance condition (option 1) is stated, and the Freud options follow from his theory as reported."))) +
 final("Option 3"),
 "except",
 [("1", "¶1: victims must wish to avoid it."), ("2", "Self-directed aggression, as Freud describes it, sits uneasily with that condition."), ("4", "¶2: mental illness possibly due to suppressing aggressive urges.")])

P.rc(24, "P4", "Detail", "4", "Easy",
 "Read the end of the first paragraph.",
 steps(("The relevant line", ev(1, "The first variable is the aggressor him/herself. The second is the social situation or circumstance in which the aggressive acts occur. The third variable is the target or victim of aggression.")),
       ("Choosing", p("Aggressor, circumstances, victim."))) +
 final("Option 4"),
 "detail",
 [("1", "Severity isn’t one of the three."), ("2", "Disciplines aren’t the variables."), ("3", "These are types of aggression and one cause.")])

P.rc(25, "P4", "Purpose", "3", "Easy",
 "The example illustrates instrumental aggression.",
 steps(("The relevant line", ev(1, "Instrumental aggression is an aggressive act that is regarded as a means to an end other than pain or injury.")),
       ("Choosing", p("Pain is only a means to another end."))) +
 final("Option 3"),
 "purpose",
 [("1", "Reliability isn’t discussed."), ("2", "Effectiveness isn’t discussed."), ("4", "The example says there may be no hostility.")])

P.rc(26, "P4", "Except", "1", "Easy",
 "Does the passage say anything about keeping aggression under control?",
 steps(("Choosing", p("The passage never discusses societies controlling aggression by moderating the death instinct. Intent, hormones and biology are all discussed."))) +
 final("Option 1"),
 "except",
 [("2", "¶1: categorised by intent."), ("3", "¶2: testosterone and men."), ("4", "¶2: biological basis.")])
