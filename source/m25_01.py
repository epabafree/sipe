# -*- coding: utf-8 -*-
# Simp Mock 1 (2025): VARC (24 of 24). DILR and QA: m25_01_dilr.py, m25_01_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(1, "sm25_01.json", series=2025)
P.passage("V1", "Passage 1 — Mental time travel", "Philosophy_and_Psychology")
P.passage("V2", "Passage 2 — The ozone hole", "Environment_and_Life_Science")
P.passage("V3", "Passage 3 — The Portuguese spice monopoly", "Social_Science_and_History")
P.passage("V4", "Passage 4 — Why nations are rich or poor", "Economics_and_Management")

P.va(1, P.sent_html(1), [], "TITA", "2", "Odd_One_Out", "Medium",
 "Four sentences praise how the films confront hard subjects. One complains about something else.",
 steps(("The chain", p("1 → 3 → 4 → 5: this year’s contenders tackle contentious topics (1); their storytelling challenges audiences (3); epics and character studies alike show film’s power (4); these films go beyond entertainment (5).")),
       ("The odd one", p("Sentence 2 says the messages are drowned out by publicity campaigns. That criticism runs against the paragraph’s praise and nothing else picks it up."))) + final("2"),
 "oddone", [("1", "Introduces the films and their topics."), ("3", "“Their storytelling”: the films’ energy."), ("4", "Generalises: film’s power to provoke."), ("5", "“These cinematic efforts”: the conclusion.")],
 why_title="How the other sentences fit")

P.rc(2, "V1", "Inference_Except", "1", "Medium",
 "What does the passage say foresight depends on? Does it ever call it fixed or genetic?",
 steps(("What the sentence implies", p("If animals, babies and people with advanced Alzheimer’s lack the ability, it needs developed cognition (option 2). The book argues it was crucial to human evolution (option 3), and the scrub-jay discussion attributes animal look-alikes to associative learning (option 4).")),
       ("The odd one", p("Nothing calls foresight a fixed genetic trait. The passage says it is absent in babies and fades with age, which suggests it develops and changes."))) + final("Option 1"),
 "except", [("2", "Babies and Alzheimer’s patients lack it: it needs developed cognition."), ("3", "¶1: ‘mental time travel was crucial to human evolution’."), ("4", "¶3: jays may rely on ‘associative learning rather than true foresight’.")])

P.rc(3, "V1", "Purpose", "2", "Medium",
 "Where does Homo erectus come up the second time, and what point is made there?",
 steps(("The line", ev(4, "The gap between humans and other animals would seem smaller if other hominins like Neanderthals or Homo erectus still existed") +
          p("Extinct hominins show that human abilities sit on a scale, not on one side of a wall."))) + final("Option 2"),
 "purpose", [("1", "¶1 says Homo erectus <i>had</i> foresight."), ("3", "No comparison of instinct in Homo erectus."), ("4", "‘All species’ goes far beyond the passage.")])

P.rc(4, "V1", "Application", "4", "Easy",
 "Displacement is referring to things remote in space or time.",
 steps(("The definition", ev(2, "Human language, they note, enables “displacement”—the ability to refer to things remote in space and time")),
       ("Checking", p("Options 1–3 all talk about things far away in time or place. Running for shelter from clouds you can see is a reaction to the here and now."))) + final("Option 4"),
 "inference", [("1", "Remote in time and space."), ("2", "Refers to the future."), ("3", "Refers to the distant past.")])

P.rc(5, "V1", "Inference", "4", "Hard",
 "‘If false, inconsistent with the passage’: find the statement the passage needs to be true.",
 steps(("How to read it", p("If the statement were false and that clashes with the passage, then the passage holds the statement true.")),
       ("Checking", p("Option 4 is the book’s claim: foresight underlies tool-making, fire and language. Its denial would contradict the passage. Options 1–3 are already contrary to the passage, so their being false fits it."))) + final("Option 4"),
 "inference", [("1", "Contrary to the passage: foresight enabled or grew with these skills."), ("2", "Contrary: animals show little true foresight."), ("3", "Contrary: ‘Memory is for the future’.")])

P.rc(6, "V2", "Inference_Except", "2", "Medium",
 "What does the last paragraph say people wrongly believe about climate change?",
 steps(("The line", ev(5, "gradual issues like CO2 emissions lack the immediate impact that spurred action on the ozone hole, leading some to mistakenly believe climate change can be as easily resolved") +
          p("The author calls this belief a mistake, so would not support option 2.")),
       ("The others", p("International cooperation (the Montreal Protocol), public fear driving action, and the treaty’s success are all endorsed."))) + final("Option 2"),
 "except", [("1", "24 nations signed the protocol; the author praises it."), ("3", "Fear ‘drove one of history’s greatest environmental victories’."), ("4", "The hole is shrinking and should heal by 2050.")])

P.rc(7, "V2", "Inference", "1", "Easy",
 "What would happen without the layer?",
 steps(("The line", ev(2, "This layer blocks ultraviolet light, offering critical protection. Without it, the sun’s UV rays would sterilize Earth’s surface") +
          p("It shields life from harmful UV radiation."))) + final("Option 1"),
 "inference", [("2", "It blocks UV light, not ‘all forms’ of radiation."), ("3", "Variability is described, but the layer’s role is protection."), ("4", "‘The only factor’ is far too strong.")])

P.rc(8, "V2", "Main_Idea", "3", "Medium",
 "The first paragraph asks a question before it goes into history. What is the question?",
 steps(("The line", ev(1, "Yet, years after its discovery, the ozone hole no longer carries the horror-story weight it once did. How did the conversation change") +
          p("The paragraph is about how perception of the ozone hole has changed; the history is the start of the answer."))) + final("Option 3"),
 "inference", [("1", "Only the opening sentence."), ("2", "The history is background in this paragraph."), ("4", "The passage says the hole is healing.")])

P.rc(9, "V2", "Purpose", "1", "Medium",
 "Read the sentence that introduces the Tibet mini-hole.",
 steps(("The line", ev(3, "The Antarctic ozone hole isn’t unique: a “mini-hole” was found over Tibet in 2003, and Arctic thinning was confirmed in 2005") +
          p("It shows depletion happens in several regions, and the paragraph has just explained the conditions (seasonal warming) under which it forms."))) + final("Option 1"),
 "purpose", [("2", "Nothing is called unpredictable."), ("3", "Severity across regions isn’t compared."), ("4", "It isn’t about the hole lasting despite the CFC ban.")])

P.va(10, P.missing_html(10), P.Q["VARC"][10]["opts"], "MCQ", "4", "Missing_Sentence", "Medium",
 "‘Such a system’ and ‘critics’ need something to answer. Which blank comes right after a claim in favour of the change?",
 steps(("Find the hook", p("The paragraph ends: ‘Supporters argue this change further fosters innovation.’ The new sentence answers that with the critics’ view: the system favours AI developers.")),
       ("Check the others", p("Blank 1 is followed by ‘However, critics argue…’, so a critics’ sentence there would repeat itself. Blanks 2 and 3 sit inside the music-industry argument, which is already a critic speaking."))) + final("Option 4"),
 "missing", [("1", "‘However, critics argue’ follows; two critic sentences in a row with ‘however’ between them don’t work."), ("2", "Between the opt-in proposal and Kiehl’s warning."), ("3", "Inside Kiehl’s own argument.")])

P.va(11, P.summary_html(11, "The way we structure"), P.Q["VARC"][11]["opts"], "MCQ", "3", "Summary", "Hard",
 "Three points: race labels have been senseless, they caused misery, and dropping them needs dropping old and new biases.",
 steps(("What the passage says", "<ol><li>Racial categories built on a small genetic component are a muddle (Channing, Halsey).</li><li>They have caused misery and confusion.</li><li>Society would be better off without them, which means discarding old illusions and newer biases.</li></ol>"),
       ("Choosing", p("Option 3 has the confusion, the suffering, the old and new biases, and the case for getting rid of the categories. Option 2 is close but leaves out the conclusion that the categories themselves should go."))) + final("Option 3"),
 "summary", [("1", "Says race became modern biases; misses the call to drop the categories."), ("2", "Close, but ‘moving beyond such constructs’ is weaker than doing away with them, and confusion is left out."), ("4", "Says they remain entrenched; misses the way forward.")])

P.rc(12, "V3", "Except", "4", "Medium",
 "Which reasons does paragraph 4 give for the monopoly’s short life?",
 steps(("The reasons given", p("The policy was unenforceable (¶2), Asian merchants traded around the Portuguese, officials were corrupt, Middle Eastern routes revived (¶4), and the Dutch and others captured key ports (¶5).")),
       ("The odd one", p("The move to sugar, cotton, tea and so on comes in the last paragraph as a later change in European policy, not as a cause of the Portuguese decline."))) + final("Option 4"),
 "except", [("1", "¶4: ‘resurgence of Middle Eastern land and sea routes’."), ("2", "¶2: ‘this policy proved unenforceable everywhere’."), ("3", "¶5: the Dutch captured Malacca, Colombo and Cochin.")])

P.rc(13, "V3", "Detail_Not_True", "3", "Easy",
 "Check each measure against paragraphs 2 and 3.",
 steps(("What the passage lists", p("Passports (the cartaz), confiscation and punishment, licences, customs duties, protected convoys (cafilas), and a limited allowance for local traders.")),
       ("The odd one", p("Convoys protected ships, but a fleet patrolling the spice regions is never mentioned."))) + final("Option 3"),
 "notrue", [("1", "The cartaz system."), ("2", "Confiscation of cargo, punishment of crews."), ("4", "Limited permissions for small quantities, mainly pepper.")])

P.rc(14, "V3", "Inference", "1", "Easy",
 "What did Asian merchants do about the Portuguese rules?",
 steps(("The line", ev(4, "Asian merchants largely avoided the Europeans and continued duty-free trade, with Europe accounting for only about a quarter of global spice trade") +
          p("They kept trading, duty-free, outside the system."))) + final("Option 1"),
 "inference", [("2", "They avoided the Portuguese, convoys included."), ("3", "They worked around the monopoly."), ("4", "Europe had a quarter of the trade; Asian merchants had most of the rest.")])

P.rc(15, "V3", "Detail", "1", "Easy",
 "Paragraph 4 opens with the consequences.",
 steps(("The line", ev(4, "Trade networks shifted, causing established centers like Cochin to decline while others like Goa rose"))) + final("Option 1"),
 "detail", [("2", "The policies displaced old centres; they didn’t simply coexist."), ("3", "The cartaz system punished traders; no benefit is mentioned."), ("4", "Local networks were reshaped, not left alone.")])

P.rc(16, "V4", "Main_Idea", "3", "Hard",
 "Read the last paragraph: what does the author say the prizewinners’ research did for the field?",
 steps(("The frame", ev(1, "Historically, models of economic growth focused on the accumulation of factors of production") +
          ev(4, "the prizewinners’ research underscored historical specificity, moving development economics away from abstract growth models") +
          p("The passage starts from the old models, explains the institutional account and its critics, and ends with the shift in the field.")),
       ("Choosing", p("Options 1, 2 and 4 are parts of the argument the passage describes. Option 3 covers the whole arc."))) + final("Option 3"),
 "inference", [("1", "Settler mortality is the method, not the theme."), ("2", "The dichotomy is described and then questioned by historians."), ("4", "Persistence of institutions is one section (Ghana).")])

P.rc(17, "V4", "Except", "2", "Medium",
 "Which colonies became extractive, according to the hypothesis?",
 steps(("The line", ev(2, "Acemoglu, Johnson, and Robinson hypothesised that wealthier colonies developed extraction methods, while larger populations provided coerced labour") +
          p("Wealthier colonies got extractive institutions, not inclusive ones. Option 2 reverses the finding.")),
       ("The others", p("Settler mortality shaping institutions, property and markets linked to growth, and the lasting effect of colonial institutions are all part of the approach’s results."))) + final("Option 2"),
 "except", [("1", "Settler mortality identified the type of institution."), ("3", "Low-mortality colonies set up property rights and free markets."), ("4", "The reversal of fortune and later persistence.")])

P.rc(18, "V4", "Application", "1", "Medium",
 "Their argument: institutions, set up according to settler mortality, decide long-run wealth, even ahead of education.",
 steps(("Choosing", p("If high-mortality colonies stay poor even after investing in education and technology, institutions are doing the work, not other factors. That is option 1.")),
       ("The others", p("Option 2 is about transitions, option 3 about outside shocks, and option 4 makes extractive institutions good in the short run; none tests the settler-mortality chain."))) + final("Option 1"),
 "inference", [("2", "Says nothing about where the institutions came from."), ("3", "External shocks are a different explanation."), ("4", "Credits extractive institutions with short-term growth, which the passage doesn’t claim.")])

P.rc(19, "V4", "Inference_Except", "1", "Hard",
 "Which statement is the old view the passage moves away from, rather than a conclusion of its own?",
 steps(("Option 1", ev(1, "The greater the capital stock per worker and its productive use, the richer a country would be. Yet that left a gap") +
          p("This is how earlier growth models saw it. The author immediately says it left a gap, and the rest of the passage argues that institutions explain why capital builds up in the first place. It is the conclusion least supported by the passage.")),
       ("The others", p("Option 2 restates the opening and the prizewinners’ thesis; option 4 is Glaeser’s criticism; option 3 fits the reversal of fortune, where rich, urbanised colonies of 1500 did not stay rich."))) +
 trap("Option 3 can look wrong because urbanisation did matter, in reverse. But the passage’s point is that it did not carry through to modern wealth, which is what option 3 says.") + final("Option 1"),
 "inference", [("2", "¶1: living standards depend on when and where you are born; the winners point to government."), ("3", "The reversal of fortune: early urban wealth did not last."), ("4", "Glaeser: education, not just institutions.")])

P.va(20, P.missing_html(20), P.Q["VARC"][20]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "The sentence sums up: rethinking waste helps the environment <i>and</i> nutrition. Where have both points been made?",
 steps(("Find the spot", p("By blank 4, the paragraph has covered both: peels are nutrient-rich, and wasted food drives emissions; and it has just said peels are edible. The sentence closes the paragraph.")),
       ("Match the label", p("Blank 4 is choice 1, labelled ‘Option 4’."))) + final("Choice 1 (“Option 4”)"),
 "missing", [("2", "“Option 3”: before the methane point, the environmental case isn’t finished."), ("3", "“Option 2”: before any environmental point."), ("4", "“Option 1”: before nutrition has been mentioned.")])

P.va(21, P.missing_html(21), P.Q["VARC"][21]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "The next sentence after the right blank begins ‘This fusion of nature and relaxation’.",
 steps(("Find the hook", p("After blank 3: ‘This fusion of nature and relaxation positions Sweden…’. That needs a sentence linking nature to rest just before it, and the new sentence does exactly that.")),
       ("Match the label", p("Blank 3 is choice 1, labelled ‘Option 3’."))) + final("Choice 1 (“Option 3”)"),
 "missing", [("2", "“Option 2”: before Sweden’s nature has been described."), ("3", "“Option 1”: the paragraph has to open with sleep tourism."), ("4", "“Option 4”: after the conclusion.")])

P.va(22, P.sent_html(22), [], "TITA", "4", "Odd_One_Out", "Easy",
 "The paragraph is about the appeal of vintage audio. One sentence is about a modern product.",
 steps(("The chain", p("1 → 2 → 3 → 5: demand for authentic analog equipment (1); its warm sound (2); nostalgia for classic designs (3); its solid build (5).")),
       ("The odd one", p("Sentence 4 is about portable Bluetooth speakers that trade sound for convenience, the opposite of what the paragraph praises."))) + final("4"),
 "oddone", [("1", "Rising demand for analog equipment."), ("2", "Reason one: sound."), ("3", "Reason two: nostalgia and craftsmanship."), ("5", "Reason three: build quality.")],
 why_title="How the other sentences fit")

P.va(23, P.summary_html(23, "\"Doomscrolling\" refers"), P.Q["VARC"][23]["opts"], "MCQ", "4", "Summary", "Medium",
 "Cause, harm, remedy. Which option keeps all three without distorting any?",
 steps(("What the passage says", "<ol><li>Doomscrolling feeds on curiosity and fear.</li><li>It worsens stress and depression; algorithms deepen it.</li><li>Mindful media habits protect mental health.</li></ol>"),
       ("Choosing", p("Option 4 has cause, harm and remedy."))) + final("Option 4"),
 "summary", [("1", "Leaves out the mental-health harm."), ("2", "Says we are forced to fixate; misses the remedy."), ("3", "Leaves out what drives the habit.")])

P.va(24, P.summary_html(24, "Stem cell research remains"), P.Q["VARC"][24]["opts"], "MCQ", "1", "Summary", "Medium",
 "The passage lists the tools driving progress and ends on oversight.",
 steps(("What the passage says", "<ol><li>Stem cell research is advancing fast: reprogrammed cells, CRISPR, organoids, trials.</li><li>It promises therapies.</li><li>Ethical debate continues; oversight and responsible innovation matter.</li></ol>"),
       ("Choosing", p("Option 1 names the tools, the promise and the need for oversight."))) + final("Option 1"),
 "summary", [("2", "Leaves out the specific advances and the stress on oversight."), ("3", "‘Balancing ethical considerations’ softens the call for oversight."), ("4", "Drops the tools that drive progress.")])
