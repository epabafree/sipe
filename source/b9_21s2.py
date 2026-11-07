# -*- coding: utf-8 -*-
# Batch 9 — CAT 2021 Slot 2: VARC (Q1–24). DILR and QA: b9_21s2_dilr.py, b9_21s2_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2021, 2, "ex9_21s2.json")
P.passage("P1", "Passage 1 — The scandal of knowledge", "Philosophy_and_Psychology")
P.passage("P2", "Passage 2 — Oral languages and monolingualism", "Social_Science_and_History")
P.passage("P3", "Passage 3 — Truth, fiction and power", "Philosophy_and_Psychology")
P.passage("P4", "Passage 4 — Home and world in Indian nationalism", "Politics")

# ---------------- Verbal ability (Q1) ----------------
P.va(1, P.sent_html(1), [], "TITA", "1", "Odd_One_Out", "Medium",
 "Four sentences discuss the ethics of genetic enhancement. One sounds like it is reviewing a book.",
 steps(("The chain", p("3 → 2 → 4 → 5: genetics brings promise and a predicament (3), people find genetic engineering disquieting but can’t say why (2), the ethics of enhancement touch on theology (4), and one argument against it (5).")),
       ("The odd one", p("Sentence 1 praises “this” as an excellent primer. It is about a book, not about the ethics themselves, and “this” has nothing to point back to."))) +
 final("1"),
 "oddone",
 [("3", "The promise and the predicament."), ("2", "Why it feels wrong is hard to say."), ("4", "The questions verge on theology."), ("5", "One argument.")],
 why_title="How the other sentences fit")

# ---------------- Passage 1: Knowledge ----------------
P.rc(2, "P1", "Except", "4", "Medium",
 "The last paragraph says ignoring scepticism is the most common response. Does it say it is the best?",
 steps(("The relevant line", ev(3, "There are a number of ways to handle this situation. The most common is to ignore it.") +
          p("The author describes what most people do. He doesn’t recommend it.")),
       ("The others", p("Options 1, 2 and 3 restate the first two paragraphs."))) +
 final("Option 4"),
 "except",
 [("1", "¶1: philosophers say it “should matter to everyone”."), ("2", "¶2: the sceptic’s claim about reality independent of us."), ("3", "¶1: our actions would be “irrational and unjustifiable”.")])

P.rc(3, "P1", "Inference", "4", "Medium",
 "Put the quoted sentence in plain words. What can’t we do, and why?",
 steps(("The point", p("We can only meet reality through our own perceiving and conceiving. If reality is defined as what exists independently of that, then we can never perceive it.")),
       ("Choosing", p("Option 4 says this directly."))) +
 final("Option 4"),
 "inference",
 [("1", "The opposite: our ideas can’t float above our conceiving."), ("2", "Reverses the point; knowledge can’t be separated from the conceiving."), ("3", "“Perceive our perception” is not the argument.")])

P.rc(4, "P1", "Detail", "2", "Easy",
 "Read the rest of that sentence in the last paragraph.",
 steps(("The sentence", ev(3, "We hold our beliefs and presumptive knowledges more or less confidently, usually depending on how we acquired them … and how broadly and strenuously they seem to be shared or endorsed by various relevant people")),
       ("Choosing", p("How we came to hold them, and how widely they are held: option 2. Option 4 describes what our examining and defending of beliefs depends on, which is the next sentence."))) +
 final("Option 2"),
 "detail",
 [("1", "Options 3 and 4 don’t describe what confidence depends on."), ("3", "Ignoring the problem is how we cope, not what confidence depends on."), ("4", "This is what examining and defending beliefs depends on.")])

P.rc(5, "P1", "Inference", "4", "Medium",
 "What exactly is the ‘scandal’, and on what condition does it arise?",
 steps(("The scandal", ev(2, "the sceptic’s contention that we cannot be sure that we know anything – at least not if we think of knowledge as something like having a correct mental representation of reality, and not if we think of reality as something like things-as-they-are-in-themselves")),
       ("Choosing", p("Option 4 keeps the condition: the problem arises if reality is taken to be independent of us."))) +
 final("Option 4"),
 "inference",
 [("1", "The sceptic says we can’t know such a reality at all."), ("2", "Wide agreement raises confidence, but the author doesn’t say it makes actions justified."),
  ("3", "The author says confidence usually depends on the source.")])

# ---------------- Verbal ability (Q6) ----------------
P.va(6, P.sent_html(6), [], "TITA", "2143", "Para_Jumble", "Medium",
 "Two sentences give the two countries’ positions. Which one introduces the Passage?",
 steps(("The opener", p("Sentence 2 introduces the Northwest Passage and Canada’s claim.")),
       ("Positions, then outcome", p("Sentence 1 gives the US position. Sentence 4 says the question was never settled but there is an agreement. Sentence 3 closes: the dispute may not last, because the ice is melting."))) +
 final("2143"),
 "pj",
 [("2", "Canada’s claim, with the background."), ("1", "The US position."), ("4", "Never settled; the current agreement."), ("3", "Why the dispute may not last.")],
 why_title="Why each sentence goes where it does")

# ---------------- Passage 2: Languages ----------------
P.rc(7, "P2", "Except", "4", "Easy",
 "How does the author see the internet’s effect on languages?",
 steps(("The author’s view", ev(4, "Internet technology offers powerful ways for oral traditions and cultural practices to survive, even thrive") +
          p("The internet is presented as a help, not a cause of decline.")),
       ("The others", p("State neglect, catastrophes and language shift are all given as causes in the third paragraph."))) +
 final("Option 4"),
 "except",
 [("1", "¶3: “state coercion or neglect”."), ("2", "¶3: war, famine and disasters; the Tasmanian example."), ("3", "¶3: shifts “for economic and educational reasons”.")])

P.rc(8, "P2", "Except", "4", "Medium",
 "Three options restate the passage. One says something about documentation that the passage never says.",
 steps(("What the passage says", p("Indigenous languages carry traditional knowledge (¶2), communities are working to protect them (¶2, ¶4), and orality makes them vulnerable (¶2).")),
       ("The odd one", p("The passage calls their words and grammar “unusual” and “intriguing”, but never says they are hard to document."))) +
 final("Option 4"),
 "except",
 [("1", "¶2: cultural traditions, environmental understandings, medicinal plants."), ("2", "¶2: communities are “increasingly involved in projects to protect their languages”."), ("3", "¶2: “orality is fragile and contributes to linguistic vulnerability”.")])

P.rc(9, "P2", "Inference", "4", "Easy",
 "Read the last two paragraphs.",
 steps(("The author’s view", ev(6, "Monolingualism, then not globalization, should be our primary concern.") + ev(7, "Multilingualism can help us live in a more connected and more interdependent world.")),
       ("Choosing", p("The author favours greater multilingualism."))) +
 final("Option 4"),
 "inference",
 [("1", "The author warns against homogenisation."), ("2", "Language shift is a cause of decline."), ("3", "The author doesn’t call for a bigger state role; the state is often part of the problem.")])

P.rc(10, "P2", "Purpose", "2", "Medium",
 "Welsh is mentioned right after the discussion of language shift and state neglect.",
 steps(("The context", ev(3, "Such trading up and out of a speech form occurs … often amplified by state coercion or neglect. Welsh, long stigmatized and disparaged by the British state, has rebounded with vigor.")),
       ("Choosing", p("Welsh went through shift and disparagement and still came back. It shows a language can revive after a language shift."))) +
 final("Option 2"),
 "purpose",
 [("1", "The passage doesn’t say integration efforts failed."), ("3", "The state disparaged Welsh; the revival wasn’t credited to state effort."), ("4", "Globalisation isn’t connected to Welsh in the passage.")])

# ---------------- Verbal ability (Q11–12) ----------------
P.va(11, P.summary_html(11, "The unlikely alliance"), P.Q["VARC"][11]["opts"], "MCQ", "3", "Summary", "Medium",
 "Who benefits from the alliance, and how?",
 steps(("What the passage says", "<ol><li>In a downturn, industrialists and the unemployed form an unlikely alliance.</li><li>Industrialists fear competition; the unemployed organise easily.</li><li>The capitalist uses the workers’ organisation to capture the political agenda.</li></ol>"),
       ("Choosing", p("Option 3 says who uses whom and to what end."))) +
 final("Option 3"),
 "summary",
 [("1", "Treats them as equal partners; the passage says the capitalist captures the agenda."), ("2", "The downturn doesn’t create competition; it makes capitalists fear it."), ("4", "Stifling competition may be the motive, but the summary leaves out the alliance’s mechanism.")])

P.va(12, P.sent_html(12), [], "TITA", "3214", "Para_Jumble", "Hard",
 "Sentence 4 begins ‘This invention’. Which invention?",
 steps(("The opener", p("Sentence 3 names the greatest invention: the scientific method.")),
       ("Following it", p("Sentence 2 says what the method involves. Sentence 1 looks ahead to fusion power, and sentence 4, “This invention”, says fusion depends on the scientific method."))) +
 final("3214"),
 "pj",
 [("3", "The scientific method, the über-invention."), ("2", "What the method requires."), ("1", "A future invention: fusion."), ("4", "“This invention” depends on the method.")],
 why_title="Why each sentence goes where it does")

# ---------------- Passage 3: Truth and power ----------------
P.rc(13, "P3", "Main_Idea", "2", "Medium",
 "The passage ends with a choice that scholars had to make. What is it?",
 steps(("The last paragraph", ev(4, "scholars often had to decide whether they served the truth or social harmony.")),
       ("Choosing", p("The passage weighs social cohesion against objective truth. Option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "Distinguishing groups is one advantage of fiction, not the central choice."), ("3", "Truth and power are not opposites here; the choice is truth or cohesion."), ("4", "Whether leaders know they spread fictions isn’t discussed.")])

P.rc(14, "P3", "Except", "4", "Medium",
 "Which option matches the third advantage of fiction: the truth is painful?",
 steps(("The relevant line", ev(3, "the truth is often painful and disturbing. Hence if you stick to unalloyed reality, few people will follow you.")),
       ("Choosing", p("Option 4 says people can’t handle the plain truth, so leaders keep power by moving away from it. The others add limits on fiction that the author never sets."))) +
 final("Option 4"),
 "except",
 [("1", "The author doesn’t say a leader who spreads only myths will lose."), ("2", "The author sets no limit on myths."), ("3", "The author doesn’t say leaders should stay close to the truth.")])

P.rc(15, "P3", "Inference", "2", "Hard",
 "Scholars had to decide between truth and social harmony. What would a successful leader have to do?",
 steps(("The parallel", p("The author shows that both truth (the first kind of power) and shared stories (the second kind) matter, and that a candidate who tells the whole truth loses. A leader, like a scholar, has to manage the tension between truth and unity.")),
       ("Choosing", p("Option 2: knowing how to balance truth and social unity."))) +
 final("Option 2"),
 "inference",
 [("1", "Myths give the second type of power, not the first."), ("3", "The comparison with scholars is about truth versus unity, not two types of power."), ("4", "The passage doesn’t compare leaders today with the past.")])

P.rc(16, "P3", "Inference", "1", "Hard",
 "Which quote assumes fiction is the only way to unite people?",
 steps(("The quote", p("Option 1 presents the choice as fiction (unity) or truth (disunity). That leaves no room for uniting people around true stories, which overstates the role of fiction.")),
       ("The others", p("Options 2, 3 and 4 are about the complicated relationship between truth and power; none of them makes fiction necessary."))) +
 final("Option 1"),
 "inference",
 [("2", "A neutral statement that power has two meanings."), ("3", "About the first kind of power, which depends on truth."), ("4", "Questions a myth about truth; it doesn’t make fiction essential.")])

# ---------------- Verbal ability (Q17–18) ----------------
P.va(17, P.summary_html(17, "Creativity is now"), P.Q["VARC"][17]["opts"], "MCQ", "3", "Summary", "Medium",
 "The passage says creativity is valued so highly that its meaning has worn away, and this gets in the way of real creativity.",
 steps(("What the passage says", "<ol><li>Creativity is prized and widely studied.</li><li>Its value has made its meaning impossible to pin down.</li><li>The obsession now hinders real creativity.</li></ol>"),
       ("Choosing", p("Option 3 has the cause (the value placed on it), the loss of meaning, and the effect."))) +
 final("Option 3"),
 "summary",
 [("1", "The passage says its meaning can’t be policed, not that people can’t define it at all."), ("2", "“Proliferated” and “mutating identity” misread the passage."), ("4", "“Destroyed” is too strong; the passage says it “gets in the way”.")])

P.va(18, P.sent_html(18), [], "TITA", "2413", "Para_Jumble", "Medium",
 "Sentence 1 begins ‘But today’. What does it contrast with?",
 steps(("The opener", p("Sentence 2: we are at a crossroads in development.")),
       ("Past, present, response", p("Sentence 4 gives the past: development began as a hope that was lost. Sentence 1, “But today”, gives the new challenge of shared responsibility. Sentence 3, “This calls for”, gives the response."))) +
 final("2413"),
 "pj",
 [("2", "The crossroads."), ("4", "Half a century ago."), ("1", "“But today”: the new challenge."), ("3", "“This calls for”: the ethical response.")],
 why_title="Why each sentence goes where it does")

# ---------------- Passage 4: Nationalism ----------------
P.rc(19, "P4", "Inference", "3", "Medium",
 "The first paragraph explains what nationalism had to take from the West, and what it could not take.",
 steps(("The pulls", ev(1, "the colonized people had to learn those superior techniques of organizing material life and incorporate them within their own cultures.... But this could not mean the imitation of the West in every aspect of life")),
       ("Choosing", p("Nationalism fought the coloniser but had to borrow from it in the material sphere. Option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "The borrowing was in the material sphere; the spiritual was to be protected."), ("2", "Describes a situation, not two pulls in opposite directions."), ("4", "Spiritual superiority wasn’t a pull towards the coloniser.")])

P.rc(20, "P4", "Except", "2", "Medium",
 "Did the dichotomy continue old oppositions unchanged? Read the start of the third paragraph.",
 steps(("The relevant line", ev(3, "The colonial situation, and the ideological response of nationalism to the critique of Indian tradition, introduced an entirely new substance to [these dichotomies] and effected their transformation.") +
          p("So the dichotomy was transformed, not simply continued.")),
       ("The others", p("Options 1, 3 and 4 restate the passage."))) +
 final("Option 2"),
 "except",
 [("1", "¶3: it protected the inner core of national culture."), ("3", "¶2: the inner/outer distinction separates ghar and bahir."), ("4", "¶2: inner/outer was “ideologically far more powerful”.")])

P.rc(21, "P4", "Weaken", "1", "Medium",
 "The author says the spiritual, inner sphere was kept apart from Western influence. What would contradict that?",
 steps(("The claim", p("Nationalists borrowed in the material sphere and protected the spiritual sphere.")),
       ("What weakens it", p("If Indian culture was hybridised in all realms, the spiritual sphere wasn’t protected after all. Option 1."))) +
 final("Option 1"),
 "weaken",
 [("2", "The passage already says nationalism responded to colonial forces."), ("3", "Rejecting English education for women fits the home being kept separate."), ("4", "Britain’s economic strength fits the passage.")])

P.rc(22, "P4", "Detail", "1", "Medium",
 "What do liberals despair at, according to the last paragraph?",
 steps(("The relevant line", ev(4, "It would be a grave error to see in this, as liberals are apt to in their despair at the many marks of social conservatism in nationalist practice, a total rejection of the West.")),
       ("Choosing", p("Liberals saw social conservatism, especially in the roles given to women. Option 1."))) +
 final("Option 1"),
 "detail",
 [("2", "The opposite of social conservatism."), ("3", "This is the author’s view, not the liberals’."), ("4", "This is the author’s framework, not the liberal perception.")])

# ---------------- Verbal ability (Q23–24) ----------------
P.va(23, P.summary_html(23, "Biologists who publish"), P.Q["VARC"][23]["opts"], "MCQ", "3", "Summary", "Medium",
 "The passage contrasts physicists and biologists. A good summary keeps that contrast.",
 steps(("What the passage says", "<ol><li>Physicists routinely publish preprints; biologists who do are called rogue.</li><li>Preprints speed up the spread of research.</li><li>Biologists’ conservative community is the biggest barrier.</li></ol>"),
       ("Choosing", p("Option 3 keeps the contrast and the benefit."))) +
 final("Option 3"),
 "summary",
 [("1", "“Most scientific communities” is wrong; physicists accept preprints."), ("2", "“Almost all” journals overstates “some journals”."), ("4", "Reverses the passage: biologists are the reluctant ones.")])

P.va(24, P.sent_html(24), [], "TITA", "5", "Odd_One_Out", "Medium",
 "Four sentences are about neuromarketing. One is about marketing borrowing from psychology in general.",
 steps(("The chain", p("3 → 4 → 1 → 2: neuromarketing introduced (3), seen as making advertising a science (4), welcomed in advertising (1), but met with little enthusiasm by scientists (2).")),
       ("The odd one", p("Sentence 5 is about older borrowing from psychology and focus groups. It doesn’t mention neuromarketing at all."))) +
 final("5"),
 "oddone",
 [("3", "Introduces neuromarketing."), ("4", "How some see it."), ("1", "Its glow in advertising."), ("2", "Scientists’ lack of enthusiasm.")],
 why_title="How the other sentences fit")
