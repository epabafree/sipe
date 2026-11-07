# -*- coding: utf-8 -*-
# Batch 11 — CAT 2020 Slot 1: VARC. DILR and QA: b11_20s1_dilr.py, b11_20s1_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2020, 1, "ex11_20s1.json")
P.passage("P1", "Passage 1 — Nouns, verbs and the rules of grammar", "Arts_and_Literature")
P.passage("P2", "Passage 2 — Money in Tang China", "Social_Science_and_History")
P.passage("P3", "Passage 3 — Elephant seal dialects", "Environment_and_Life_Science")
P.passage("P4", "Passage 4 — Anarchism and the state", "Social_Science_and_History")

# ---------------- Verbal ability (Q1, Q3) ----------------
P.va(1, P.summary_html(1, "As Soviet power declined"), P.Q["VARC"][1]["opts"], "MCQ", "2", "Summary", "Hard",
 "What did Europe actually do at the end of the passage, and why?",
 steps(("What the passage says", "<ol><li>As the world became multi-polar, Europe sought an independent identity.</li><li>It set aside the political mechanisms of three and a half centuries.</li><li>It created a common currency and a common political structure.</li></ol>"),
       ("Choosing", p("Option 2 captures the move: reducing political and economic differences in order to adapt to a multi-polar world."))) +
 final("Option 2"),
 "summary",
 [("1", "Changing in every century is background; the passage is about what Europe did now."), ("3", "Leaves out the common currency and political structure."),
  ("4", "German unification is one motive, not the main point.")])

P.va(3, P.sent_html(3), [], "TITA", "1432", "Para_Jumble", "Hard",
 "Sentence 1 states a difficulty. Which sentence offers a way round it?",
 steps(("The problem", p("Sentence 1: narrative structure alone doesn’t reveal what the San folktales meant.")),
       ("The method and what it finds", p("Sentence 4 gives the method: look beneath the narrative at key words. Sentence 3 says what selected tales reveal: spiritual conflict involving malevolent shamans. Sentence 2 adds the benign shamans’ role in that conflict."))) +
 final("1432"),
 "pj",
 [("1", "The difficulty."), ("4", "How meaning can be drawn out."), ("3", "What the tales reveal."), ("2", "The shamans’ role.")],
 why_title="Why each sentence goes where it does")

# ---------------- Passage 1: Grammar ----------------
P.rc(4, "P1", "Inference", "2", "Medium",
 "‘If false, supports the passage’: find the statement the passage contradicts.",
 steps(("The passage’s claim", ev(2, "Without one of each, no group of words can be a sentence")),
       ("Choosing", p("Option 2 says complete sentences don’t necessarily need nouns and verbs. If that is false, the passage’s claim stands."))) +
 final("Option 2"),
 "inference",
 [("1", "The passage quotes this; it is true, not false."), ("3", "Women writers aren’t discussed."), ("4", "The passage says this; it is true.")])

P.rc(5, "P1", "Application", "4", "Medium",
 "The point is a simple formula that always gives a complete result.",
 steps(("The example", p("Any noun plus any verb always makes a sentence, even an odd one.")),
       ("The parallel", p("Any vegetable plus spices always makes a dish. The others need more than the formula: one tree isn’t an orchard, a group with equipment isn’t a team, and nouns alone aren’t a sentence."))) +
 final("Option 4"),
 "inference",
 [("1", "One apple tree doesn’t make an orchard."), ("2", "Having the same equipment doesn’t make a team."), ("3", "Contradicts the passage: you need a verb.")])

P.rc(6, "P1", "Main_Idea", "4", "Hard",
 "The passage is about why grammar matters. Which quote states that most directly?",
 steps(("The main concern", p("The author argues that a grasp of grammar, at least nouns and verbs, is what lets you write well and know that you are doing so. The quote that sums this up is “Bad grammar produces bad sentences”.")),
       ("Why not the others", p("Options 1 and 3 pick out supporting moments, and option 2 is one step in the argument."))) +
 final("Option 4"),
 "inference",
 [("1", "A comment on one quotation."), ("2", "A definition used in the argument."), ("3", "About simple sentences as a safety net.")])

P.rc(7, "P1", "Except", "2", "Easy",
 "Does the author say grammar exists to keep sentences simple?",
 steps(("The relevant line", ev(5, "The simplicity of noun-verb construction is useful—at the very least it can provide a safety net for your writing.") +
          p("Simple sentences are a fallback, not the purpose of grammar.")),
       ("The others", p("Fragments are allowed, subject–predicate is noun–verb, and the Grammar Police is a metaphor."))) +
 final("Option 2"),
 "except",
 [("1", "¶3: you needn’t write complete sentences every time."), ("3", "¶2: subject (noun) and predicate (verb)."), ("4", "A playful image for strict critics.")])

P.rc(8, "P1", "Application", "3", "Medium",
 "The author values knowing and following the rules.",
 steps(("The author’s view", ev(3, "“Unless he is certain of doing well, the writer will probably do best to follow the rules.”")),
       ("Choosing", p("Software that keeps writers to standard grammar fits this best."))) +
 final("Option 3"),
 "inference",
 [("1", "The author doesn’t criticise standard rules."), ("2", "He warns against breaking rules unless you are sure."), ("4", "He uses simple sentences as a safety net, not to avoid rhetoric altogether.")])

# ---------------- Passage 2: Tang money ----------------
P.rc(9, "P2", "Application", "3", "Easy",
 "What happens to a bolt of cloth when it is cut?",
 steps(("The relevant line", ev(2, "If consumers cut textiles into smaller pieces to buy or sell something worth less than a full bolt, that too, greatly lessened the value of the textiles.")),
       ("Choosing", p("Cutting an eighth from a new bolt would reduce the value of the whole bolt."))) +
 final("Option 3"),
 "inference",
 [("1", "Grain is less used but was still money."), ("2", "A worn bolt of the right value is a fair exchange."), ("4", "Coins suit small, local transactions.")])

P.rc(10, "P2", "Except", "1", "Easy",
 "Where do ‘steady’ and ‘stable’ appear, and what do they describe?",
 steps(("The relevant lines", ev(3, "textile production was widespread … the dimensions of a bolt of silk held remarkably steady … The values of different textiles were also more stable")),
       ("The odd one", p("Supply, measurements and value are covered. Transport isn’t."))) +
 final("Option 1"),
 "except",
 [("2", "Stable values mean reliable quality."), ("3", "Steady dimensions."), ("4", "Widespread production.")])

P.rc(11, "P2", "Inference", "4", "Medium",
 "The last paragraph compares Tang currency with today’s.",
 steps(("The relevant line", ev(5, "In actuality, our own currency system today has some similarities")),
       ("Choosing", p("Different forms of money for different sizes of transaction, then and now."))) +
 final("Option 4"),
 "inference",
 [("1", "Coins were durable, but not more valuable."), ("2", "Grain was used least."), ("3", "Grain rotted easily but was used for taxes and salaries.")])

P.rc(12, "P2", "Except", "3", "Hard",
 "Which feature is described for today’s system but not for the Tang?",
 steps(("Shared features", p("Both used different currencies for different situations and different materials as money. Tang coins fluctuated in value; so does modern money.")),
       ("The odd one", p("“Changing in front of our eyes” describes today’s system only. The passage doesn’t describe the Tang system as being transformed."))) +
 final("Option 3"),
 "except",
 [("1", "Small and large transactions used different money in both."), ("2", "Tang coin values fluctuated."), ("4", "Grain, coins, textiles; coins, notes, cards.")])

# ---------------- Verbal ability (Q13, Q15) ----------------
P.va(13, P.sent_html(13), [], "TITA", "3", "Odd_One_Out", "Medium",
 "Four sentences are about slaves’ speech in the colonies. One is about the societies they came from.",
 steps(("The chain", p("1 → 2 → 4 → 5: talk was how slaves resisted (1), their words stayed irrepressible (2), slavery depended on dialogue (4), and owners feared slave talk (5).")),
       ("The odd one", p("Sentence 3 is about the importance of oaths in the slaves’ home societies. It is background the paragraph doesn’t use."))) +
 final("3"),
 "oddone",
 [("1", "Talk as resistance."), ("2", "Words stayed irrepressible."), ("4", "Slavery needed dialogue."), ("5", "Owners feared slave talk.")],
 why_title="How the other sentences fit")

P.va(15, P.summary_html(15, "For nearly a century"), P.Q["VARC"][15]["opts"], "MCQ", "3", "Summary", "Medium",
 "What exactly do the biologists question? There are two things.",
 steps(("What the passage says", "<ol><li>Psychologists long held that intelligence is inborn, heritable and measurable.</li><li>Biologists now ask whether a single ‘intelligence’ makes sense.</li><li>They also question how heritability is measured in humans.</li></ol>"),
       ("Choosing", p("Option 3 has both objections."))) +
 final("Option 3"),
 "summary",
 [("1", "Too vague about what is criticised."), ("2", "Garbled; it doesn’t say what is questioned about inheritance."), ("4", "The biologists don’t focus on measurability or immutability.")])

# ---------------- Verbal ability (Q21) ----------------
P.va(21, P.sent_html(21), [], "TITA", "1324", "Para_Jumble", "Medium",
 "Sentence 2 begins ‘These dangers’. Which sentence describes the dangers?",
 steps(("The opener", p("Sentence 1: poison has been used for assassination since ancient times.")),
       ("The sequence", p("Sentence 3: microbiology made biological weapons more feasible. Sentence 2: these dangers led to international declarations. Sentence 4: the treaties had no means of control, so they failed."))) +
 final("1324"),
 "pj",
 [("1", "Poison since ancient times."), ("3", "Microbiology opens new prospects."), ("2", "“These dangers” led to treaties."), ("4", "The treaties failed.")],
 why_title="Why each sentence goes where it does")

# ---------------- Passage 3: Seals ----------------
P.rc(22, "P3", "Except", "3", "Hard",
 "What happened to the calls as immigrants kept arriving?",
 steps(("The relevant line", ev(4, "the calls in all locations would have eventually regressed to the average pulse rate of the founder colony") +
          p("Año Nuevo’s rate rose towards the founder colony’s average; it wouldn’t overshoot it.")),
       ("The others", p("Individuals kept their signatures (option 1), dialects came from recolonisation after near-extinction (option 2), and Año Nuevo’s average rose (option 4)."))) +
 final("Option 3"),
 "except",
 [("1", "¶3: a male keeps his vocal signature for life."), ("2", "¶3: dialects came from isolation after recolonisation."), ("4", "¶2–4: the rate rose until the dialects vanished.")])

P.rc(23, "P3", "Inference", "2", "Hard",
 "Dialects disappeared because immigrants kept their own tempo and blended the averages.",
 steps(("Why they vanished", p("Immigrants brought their own pulse rates, so each colony’s average drifted towards the overall average.")),
       ("What would prevent it", p("If immigrants changed their calls to match their new colony, local averages would stay put and dialects would survive."))) +
 final("Option 2"),
 "inference",
 [("1", "Residents adopting the immigrants’ tempo would still erase local differences."), ("3", "Another founder colony with the same tempo changes nothing."), ("4", "A colony with no migration doesn’t affect the others.")])

P.rc(24, "P3", "Main_Idea", "3", "Medium",
 "Compare the 1960s calls with today’s on three counts.",
 steps(("Then and now", ev(4, "Modern males exhibit more individual diversity, and their calls are more complex.") +
          p("Then: simple calls, little individual variety, clear regional dialects. Now: complex calls, more individual variety, dialects gone.")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "Covers only the pulse rate."), ("2", "Gets the direction of change wrong."), ("4", "Reverses individual and regional variety.")])

P.rc(25, "P3", "Inference", "3", "Medium",
 "The passage explains dialects as an accident of who settled each site first.",
 steps(("The founder idea", ev(3, "At other sites, where the scientists found faster pulse rates, the opposite would have happened—seals with faster rates would have happened to arrive first.")),
       ("Choosing", p("The southern rookeries were probably first settled by seals with fast calls."))) +
 final("Option 3"),
 "inference",
 [("1", "Explains Año Nuevo’s change, not the southern rate."), ("2", "Complex structure is a modern feature, everywhere."), ("4", "Migration from slow-call Año Nuevo would slow the south down.")])

# ---------------- Verbal ability (Q26) ----------------
P.va(26, P.sent_html(26), [], "TITA", "3124", "Para_Jumble", "Medium",
 "Sentence 4 begins ‘These concerns’. Which sentence raises them?",
 steps(("The opener", p("Sentence 3: South East Asia’s security environment has seen continuity and change since the 1990s.")),
       ("Continuity, change, consequence", p("Sentence 1: tensions remain (continuity). Sentence 2: China’s rise is a new concern (change). Sentence 4: these concerns draw in outside states."))) +
 final("3124"),
 "pj",
 [("3", "Continuity and change."), ("1", "Tensions remain."), ("2", "China’s rise."), ("4", "“These concerns” bring outside interest.")],
 why_title="Why each sentence goes where it does")


# ---------------- Verbal ability (Q2, Q14) ----------------
P.va(2, P.summary_html(2, "For years, movies"), P.Q["VARC"][2]["opts"], "MCQ", "2", "Summary", "Medium",
 "Who has the wrong idea, and where did it come from?",
 steps(("What the passage says", "<ol><li>Films and TV shows give an unrealistic picture of the ‘science of voices’.</li><li>One film scene shows an expert reading a speaker’s origin and age from a short clip, and a computer matching the voice with 90% certainty.</li><li>These misimpressions have caused errors in real trials: the ‘CSI effect’, where judges expect too much of forensic science.</li></ol>"),
       ("Choosing", p("Option 2 keeps both halves: the screen is the source, and the false belief is that forensic phonetics is reliable."))) +
 final("Option 2"),
 "summary",
 [("1", "True in spirit, but it drops films and television, which are the whole point."), ("3", "The passage says the screen version is unrealistic, not that it is used in real life."),
  ("4", "The passage is about false expectations, not about voice analysis becoming more common.")])

P.va(14, P.sent_html(14), [], "TITA", "3", "Odd_One_Out", "Medium",
 "Four sentences describe how feminist criticism of reading began. One describes what androcentric books do to readers.",
 steps(("The chain", p("1 → 5 → 4 → 2: for feminists, how we read is tied to what we read (1); more specifically, the inquiry begins with seeing that the canon is androcentric and harms women readers (5); documenting this realisation was an early task (4); Showalter’s critique of the curriculum is an example of that work (2).")),
       ("The odd one", p("Sentence 3 explains how androcentric literature shapes the reading experience by gender. It is a claim about books, while the paragraph is about what feminist critics did."))) +
 final("3"),
 "oddone",
 [("1", "Opens: how we read and what we read."), ("5", "“More specifically” narrows sentence 1."), ("4", "“This realization” is the one in sentence 5."), ("2", "“This work” is the documenting in sentence 4.")],
 why_title="How the other sentences fit")

# ---------------- Passage 4: Anarchism (Q16–20) ----------------
P.rc(16, "P4", "Except", "2", "Medium",
 "Three options are stated in the passage. Look for the one about how the public sees anarchism.",
 steps(("Checking each", p("Option 1 is in paragraphs 2–3: the revolution ended in terror and a new ruling caste. Option 3 is in the last paragraph. Option 4 is in paragraphs 3–4.")),
       ("The odd one", p("The passage never discusses a popular view of anarchism as lawlessness and violence, or a mistrust of collectivism. Anarchist-communism is in fact collectivist."))) +
 final("Option 2"),
 "except",
 [("1", "Paragraphs 2–3: the outcome of the Revolution and the betrayal by the new politicians."), ("3", "Last paragraph: ‘several traditions of individualist anarchism’, all about autonomy."),
  ("4", "Paragraphs 3–4: the state is the enemy; new rulers used violence and terror.")])

P.rc(17, "P4", "Inference", "4", "Medium",
 "Who made the revolution possible, and what did the new rulers do to them?",
 steps(("The line", ev(3, "workers and peasants, grasping the chance that arose to bring an end to centuries of exploitation and tyranny, were inevitably betrayed by the new class of politicians") +
          p("The workers’ uprising brought the new class to power, and it then used terror, a secret police and an army to control them."))) +
 final("Option 4"),
 "inference",
 [("1", "The new rulers were not anarchists; anarchists opposed them."), ("2", "Says nothing about how the workers were betrayed."), ("3", "No deal with the old ruling class is mentioned.")])

P.rc(18, "P4", "Detail", "2", "Medium",
 "Read the last sentence: how do these thinkers differ from free-market liberals?",
 steps(("The line", ev(6, "in protecting our own autonomy and associating with others for common advantages, we are promoting the good of all. These thinkers differed from free-market liberals in their absolute mistrust of American capitalism, and in their emphasis on mutualism") +
          p("Shared: individual autonomy. Different: mutualism, which the liberals don’t stress."))) +
 final("Option 2"),
 "detail",
 [("1", "Neither group is said to favour a people’s state or state intervention."), ("3", "The anarchists mistrust capitalism; they don’t argue for it."), ("4", "Altruism and a ‘mystical’ market are not in the passage.")])

P.rc(19, "P4", "Main_Idea", "3", "Easy",
 "Which set names the passage’s subject?",
 steps(("The concerns", p("The passage is about anarchism, its view of the state as the enemy, and the individual’s freedom and autonomy in the individualist strands.")),
       ("Choosing", p("Option 3 covers all of these."))) +
 final("Option 3"),
 "inference",
 [("1", "Leaves out anarchism; ‘strike’ never comes up."), ("2", "Leaves out anarchism; liberals are mentioned only once."), ("4", "Power and the state overlap, and betrayal is one episode, not a concern of the whole passage.")])

P.rc(20, "P4", "Detail", "3", "Easy",
 "What do all anarchists treat as the enemy?",
 steps(("The line", ev(4, "For anarchists the state itself is the enemy") +
          p("Anarchist-communism ‘differs from state socialism in opposing the concept of any central authority’. Every strand rejects centralised state power."))) +
 final("Option 3"),
 "detail",
 [("1", "The passage does name a common idea."), ("2", "Proudhon adopted the word; the passage doesn’t trace all forms to him."), ("4", "Only the individualist strands put the individual first.")])
