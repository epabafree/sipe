# -*- coding: utf-8 -*-
# Simp Mock 5 (2025): VARC (24 of 24). DILR and QA: m25_05_dilr.py, m25_05_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(5, "sm25_05.json", series=2025)
P.passage("V1", "Passage 1 — Banning teenagers from social media", "Science_and_Technology")
P.passage("V2", "Passage 2 — Scarcity, growth and the planet", "Economics_and_Management")
P.passage("V3", "Passage 3 — Zipf’s law in whale song", "Environment_and_Life_Science")
P.passage("V4", "Passage 4 — What fantasy is for", "Arts_and_Literature")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Inference_Except", "3", "Medium",
 "Is the passage worried that age checks are inaccurate, or does it say they have got better?",
 steps(("What pushed governments", ev(1, "concern over social media’s mental-health impact is pushing governments to get tougher") +
          p("Paragraph 1 also shows the rules being dodged (22% of young users have an adult’s birth date; half of British 8–11-year-olds use a 13+ app), so the existing limits are weak. That covers options 1, 2 and 4.")),
       ("The odd one", ev(2, "Now, they can guess within about a year, better than most humans") +
          p("AI age checks are described as available and improving. Their supposed absence is not what prompted the crackdown."))) + final("Option 3"),
 "except", [("1", "Stated: mental-health concern."), ("2", "Stated: false birth dates."), ("4", "Implied: under-13 bans are widely ignored.")])
P.rc(2, "V1", "Purpose", "3", "Medium",
 "What comes right after COPPA is mentioned? Statistics on children getting around it.",
 steps(("Context", ev(1, "Most social-media platforms forbid under-13s, following America’s 1998 COPPA") +
          p("The next lines show how easily that limit is bypassed, and then: ‘Parents and politicians once turned a blind eye.’")),
       ("Its job", p("COPPA stands for the old, weakly enforced baseline. Its failure sets up why Australia went further."))) + final("Option 3"),
 "purpose", [("1", "Australia’s ban is stricter, not COPPA."), ("2", "The passage shows it being evaded."), ("4", "It doesn’t bar them effectively: half of 8–11-year-olds use TikTok.")])
P.rc(3, "V1", "Detail_Not_True", "1", "Medium",
 "Who does Australia make responsible for the checks? Is that voluntary?",
 steps(("The rule", ev(3, "Australia puts the onus on social-media platforms") +
          p("The platforms are made accountable by law. Nothing is voluntary or self-regulatory.")),
       ("The others", p("Option 2: who should do the checks (platforms, operating systems, app stores) is exactly the debate. Option 3: ‘governments are wary of forcing Apple or Google to build global ID registries.’ Option 4: the passage weighs the advertising cost of losing young users."))) + final("Option 1"),
 "notrue", [("2", "Discussed: who must implement the checks."), ("3", "Stated: governments are wary of global ID registries."), ("4", "Discussed: under-16 ads are a low single-digit share.")])
P.rc(4, "V1", "Inference", "3", "Easy",
 "Why are gaming platforms expected to win?",
 steps(("The condition", ev(4, "The big winners of this crackdown may be gaming, so long as the ban does not expand further") +
          p("Games are exempt now even though children ‘use platforms like Roblox to chat’. If the ban reached chat in games, they would fall under the same rules, including age checks."))) + final("Option 3"),
 "inference", [("1", "Their winning depends on the ban not expanding."), ("2", "Nothing suggests platforms would relax rules."), ("4", "Nothing about advertisers shifting.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Main_Idea", "2", "Medium",
 "The passage moves from the Ehrlichs to eco-leftists to an open debate and a book on the history of scarcity.",
 steps(("The arc", ev(3, "Yet, the broader debate remains unresolved") +
          p("The author lays out scarcity against ingenuity, then welcomes a history that shows the debate is ‘much richer and more ethically nuanced’. It explores views; it doesn’t prove, condemn or promote one."))) + final("Option 2"),
 "inference", [("1", "One part of paragraph 2, not the purpose."), ("3", "The author says the Ehrlichs were wrong about human famine."), ("4", "The author reports degrowth; population control is explicitly set aside.")])
P.rc(6, "V2", "Inference", "4", "Medium",
 "How does the author feel about the labels ‘Ehrlichian’ and ‘neo-Malthusian’?",
 steps(("The line", ev(3, "This debate is overshadowed by its most infamous participants") +
          p("Anyone questioning growth ‘risks being labeled’ and tied to ‘historically discredited figures’. The book is ‘timely’ because scarcity thinking has a richer history than these labels allow. So the labels oversimplify."))) + final("Option 4"),
 "inference", [("1", "Eco-leftists say population growth is not the driver."), ("2", "Mill imagined an end to growth, unlike many classical economists."), ("3", "The author never weighs the two against each other.")])
P.rc(7, "V2", "Detail", "1", "Easy",
 "What do eco-leftists blame, and what do degrowth advocates want?",
 steps(("The lines", ev(2, "the primary driver is the Global North’s insatiable consumption") +
          ev(2, "argue for reducing economic growth in wealthy nations while redistributing resources to the Global South") +
          p("Less consumption in rich countries, more support for poorer ones."))) + final("Option 1"),
 "detail", [("2", "They say population growth does not drive climate change."), ("3", "They want to reduce growth in rich nations."), ("4", "Farming technology isn’t their focus.")])
P.rc(8, "V2", "Inference", "3", "Easy",
 "What does a ‘stationary state’ economy aim for?",
 steps(("The idea", ev(4, "an economy of sufficiency rather than relentless expansion") +
          p("Production stops expanding endlessly; needs are still met."))) + final("Option 3"),
 "inference", [("1", "Raising GDP is the growth Mill questioned."), ("2", "Spurring investment is growth again."), ("4", "Mill’s idea is about sufficiency, not specifically climate policy.")])

# ---------------- Passage 3 (Q9–12) ----------------
P.rc(9, "V3", "Main_Idea", "4", "Medium",
 "Pick the set in which every item is a real topic of the passage, and nothing major is missing.",
 steps(("Key ideas", p("Zipf’s law; whale song; the infant-style statistical segmentation used to find ‘words’; cultural transmission and learnability as the explanation; Menzerath’s law as a second shared feature.")),
       ("Checking", p("Option 4 has all of them. The others slip in minor or foreign items: ‘statistical outliers’, ‘semantic complexity’, or semantic meaning, which whale song is said to lack."))) + final("Option 4"),
 "inference", [("1", "Misses Zipf’s law, the heart of the passage."), ("2", "‘Statistical outliers’ isn’t discussed."), ("3", "Misses Zipf’s law; ‘semantic complexity’ isn’t a theme.")])
P.rc(10, "V3", "Inference_Except", "1", "Medium",
 "Is ‘after dinner’ about what words mean, or about where they break?",
 steps(("The example", ev(2, "children could identify the distinct words in the phrase “after dinner” by noting that certain syllables do not usually go together") +
          p("It shows statistical cues for word boundaries (option 3), that some syllables rarely go together within a word (option 2), and the method later applied to whale song (option 4).")),
       ("The odd one", p("Linking words to meaning is never part of the example."))) + final("Option 1"),
 "except", [("2", "Directly shown."), ("3", "Directly shown."), ("4", "‘Using this method, the team analyzed…’")])
P.rc(11, "V3", "Inference", "1", "Medium",
 "What do whale song and music share, and what do they both lack?",
 steps(("The line", ev(3, "Humpback whale song could be comparable to human music, which also lacks semantic meaning while still adhering to Zipf’s law") +
          p("The common ground is statistical structure in organised sound, not meaning or melody."))) + final("Option 1"),
 "inference", [("2", "Neither conveys ideas the way language does."), ("3", "Both lack semantic meaning."), ("4", "Melody is never compared.")])
P.rc(12, "V3", "Weaken", "3", "Medium",
 "The claim is that the pattern comes from learning. What alternative cause would undercut it?",
 steps(("The claim", p("Whale songs follow Zipf’s law because songs evolved culturally to be easier for novices to learn.")),
       ("The weakener", p("If whale anatomy simply produces repeated patterns, the distribution has a physical cause, and cultural transmission isn’t needed to explain it."))) + final("Option 3"),
 "weaken", [("1", "Supports social spread of the patterns."), ("2", "Supports generational transmission."), ("4", "Supports it: no stable transmission, no pattern.")])

# ---------------- Passage 4 (Q13–16) ----------------
P.rc(13, "V4", "Inference_Except", "4", "Medium",
 "Watch for the option that goes too far.",
 steps(("The line", ev(1, "You can’t just tell a child a blunt fact about the human heart and expect them to believe you") +
          p("Then: ‘You need to show it.’ Direct statements fall short (1); stories teach (2); fantasy gives ‘longhand proof’ for abstract ideas (3).")),
       ("The odd one", p("The author says plain messages are not enough for deep truths, not that children never respond to any brief message."))) + final("Option 4"),
 "except", [("1", "Implied."), ("2", "Implied by ‘you need to show it’."), ("3", "Implied by ‘longhand proof’.")])
P.rc(14, "V4", "Purpose", "3", "Hard",
 "Read Mayor’s quote: what did someone finding the bone think it was?",
 steps(("The lines", ev(2, "The Indigenous American mythological beast, the Thunder Bird, may have stemmed from T-Rex skeletons") +
          ev(2, "might well have identified the fossil as part of some mysterious bird") +
          p("People found real remains and read them as parts of real creatures. That is option 3.")),
       ("Why not 2", p("These are fossils, not archaeological finds, and ‘creation’ suggests deliberate invention; the quote shows people taking the bones as evidence of a real bird."))) +
 trap("Option 2 sounds close; the passage’s point is interpretation of fossils, not discoveries shaping invented stories.") + final("Option 3"),
 "purpose", [("1", "Too broad: ‘natural phenomena’ in general."), ("2", "Fossils aren’t archaeology, and the bones were taken as real evidence."), ("4", "‘Deliberately invented’ is the opposite of believing in them.")])
P.rc(15, "V4", "Inference_Except", "2", "Easy",
 "List the charges the author names, then look for the one not there.",
 steps(("The charges", ev(3, "There are many attacks you can level at fantasy: escapist, ridiculous, indulgent, coy, repetitive") +
          ev(3, "relentless battles, didactic hectoring or crass sentimentalism") +
          p("Sentimentality and preaching (1), repetition (3) and escapism (4) are all named. Appealing to immature minds is not."))) + final("Option 2"),
 "except", [("1", "‘Didactic hectoring or crass sentimentalism’."), ("3", "‘Repetitive’."), ("4", "‘Escapist’.")])
P.rc(16, "V4", "Detail", "3", "Easy",
 "What does Le Guin call escape?",
 steps(("The line", ev(4, "it’s our plain duty to escape, and to take as many people with us as we can") +
          p("Escape is a duty, and it frees the mind. Tolkien ‘never sought to deny that fantasy is escapist: that is its power and glory.’"))) + final("Option 3"),
 "detail", [("1", "They value escapism; it isn’t shallow."), ("2", "Escape is tied to real prisons."), ("4", "Not limited to children.")])

# ---------------- Summaries (Q17–19) ----------------
P.va(17, P.summary_html(17, "Buoyancy is the"), P.Q["VARC"][17]["opts"], "MCQ", "2", "Summary", "Medium",
 "Definition (clarity and stability), then how it’s built (self-regulation and mindfulness), then the payoff (resilience).",
 steps(("Choosing", p("Option 2 keeps all three: what buoyancy does, how self-regulation and mindfulness build it, and the resilience it gives."))) + final("Option 2"),
 "summary", [("1", "Leaves out self-regulation and mindfulness."), ("3", "Makes them a requirement; misses what buoyancy is."), ("4", "‘Neural adaptation’ is a detail; leaves out mindfulness.")])
P.va(18, P.summary_html(18, "Social change is"), P.Q["VARC"][18]["opts"], "MCQ", "4", "Summary", "Hard",
 "Two halves: change is slow and rooted in past policy; in fear we invent breaks.",
 steps(("Choosing", p("Option 4 has gradual change shaped by political and historical forces, and the urge in times of fear to impose breaks."))) +
 trap("Option 1 says history ‘resists’ division, and option 3 says people believe they can separate past from present: both add claims.") + final("Option 4"),
 "summary", [("1", "Leaves out the political roots; ‘history resists’ is added."), ("2", "Leaves out moral panic and fear."), ("3", "Leaves out the slow structural change.")])
P.va(19, P.summary_html(19, "Negative theology is"), P.Q["VARC"][19]["opts"], "MCQ", "3", "Summary", "Medium",
 "Negative theology comes from mysticism, whose experiences are insightful yet can’t be put into words.",
 steps(("Choosing", p("Option 3 has the origin and the paradox, without extra claims."))) + final("Option 3"),
 "summary", [("1", "Reverses the relation: mysticism is the root, and examples are details."), ("2", "‘Grapples with’ is added."), ("4", "Vague; ‘explored in religious teachings’ is added.")])

# ---------------- Missing sentences (Q20–22) ----------------
P.va(20, P.missing_html(20), P.Q["VARC"][20]["opts"], "MCQ", "3", "Missing_Sentence", "Medium",
 "‘This alarming discovery’ needs a discovery about plastic in an organ right before it.",
 steps(("Find the spot", p("Blank 1 follows the finding that plastic gets past the blood-brain barrier into brain cells. The next sentence, ‘And what’s worse…’, adds to the alarm.")),
       ("Match the label", p("Blank 1 is choice 3, labelled ‘Option 1’."))) + final("Choice 3 (“Option 1”)"),
 "missing", [("1", "“Option 4”: the closing line has already moved to the body as a storage tank."), ("2", "“Option 2”: in the middle of the old-versus-new brains comparison."), ("4", "“Option 3”: after a methods note.")])
P.va(21, P.missing_html(21), P.Q["VARC"][21]["opts"], "MCQ", "4", "Missing_Sentence", "Medium",
 "‘The project’ needs a project just before it.",
 steps(("Find the spot", p("Blank 2 follows the new sperm-whale reserve. The sentence sums up its aim, and the paragraph goes on to limited permits that balance visitors with protection.")),
       ("Match the label", p("Blank 2 is choice 4, labelled ‘Option 2’."))) + final("Choice 4 (“Option 2”)"),
 "missing", [("1", "“Option 1”: no project yet."), ("2", "“Option 4”: after the closing line."), ("3", "“Option 3”: after infrastructure, not the reserve.")])
P.va(22, P.missing_html(22), P.Q["VARC"][22]["opts"], "MCQ", "3", "Missing_Sentence", "Medium",
 "‘Also … increase defense spending’ follows Poland’s own spending.",
 steps(("Find the spot", p("Blank 3 comes right after ‘now spending nearly 5% of GDP’, and Tusk’s quote about Europeans spending big follows.")),
       ("Match the label", p("Blank 3 is choice 3, labelled ‘Option 3’."))) + final("Choice 3 (“Option 3”)"),
 "missing", [("1", "“Option 1”: support for Ukraine, not spending."), ("2", "“Option 2”: about US concessions."), ("4", "“Option 4”: after Tusk’s quote, which the sentence should introduce.")])

# ---------------- Odd one out (Q23–24) ----------------
P.va(23, P.sent_html(23), [], "TITA", "4", "Odd_One_Out", "Medium",
 "Four sentences describe an accessibility-first design approach. One is about measuring inclusion.",
 steps(("The chain", p("2 → 5 → 3 → 1: institutions should adopt an accessibility-based framework (2); accessibility shapes solutions from the start (5); a shift from after-the-fact compliance (3); success depends on involving people with disabilities (1).")),
       ("The odd one", p("Sentence 4 is about collecting disaggregated data on financial inclusion, a different subject."))) + final("4"),
 "oddone", [("1", "The condition for success."), ("2", "The proposal."), ("3", "The contrast with today."), ("5", "What the approach means.")], why_title="How the other sentences fit")
P.va(24, P.sent_html(24), [], "TITA", "2", "Odd_One_Out", "Medium",
 "Four sentences build from the quote to the two moments that shaped the old order.",
 steps(("The chain", p("3 → 5 → 4 → 1: the quote (3); its relevance as the order shifts (5); two moments shaped that order, the first after 1945 (4); the second in 1989 (1).")),
       ("The odd one", p("Sentence 2 describes today’s multipolar world, while the paragraph closes on how the old order was formed."))) + final("2"),
 "oddone", [("1", "The second moment."), ("3", "The opening quote."), ("4", "The first moment."), ("5", "Ties the quote to today.")], why_title="How the other sentences fit")
