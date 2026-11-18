# -*- coding: utf-8 -*-
# Simp Mock 6: VARC (24 of 24). DILR and QA: m06_dilr.py, m06_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(6, "sm06.json")
P.passage("V1", "Passage 1 — What machine learning cannot do", "Science_and_Technology")
P.passage("V2", "Passage 2 — The fading of han", "Arts_and_Literature")
P.passage("V3", "Passage 3 — Liberalism and peace", "Social_Science_and_History")
P.passage("V4", "Passage 4 — Chaos in ecosystems", "Environment_and_Life_Science")

# Small wording fixes so that each VA item has exactly one defensible answer.
V = P.Q["VARC"]
V[20]["q"] = V[20]["q"].replace("The use of plastic bags has been banned in many countries due to their harmful impact on the environment.",
                                "Plastic bags are cheap, light and convenient, which is why they are used so widely.")
V[21]["q"] = V[21]["q"].replace("_____1____. It weighs only about 3 pounds", "_____1____. The brain weighs only about 3 pounds")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Application", "3", "Medium",
 "The claim is about harm to science or ethics. Which option shows no harm?",
 steps(("The claim", ev(1, "will degrade our science and debase our ethics by incorporating into our technology a fundamentally flawed conception of language and knowledge")),
       ("Choosing", p("Prediction without explanation (option 1) is what the author calls pseudoscience; a biased hiring tool (option 2) debases ethics; reading sarcasm by pattern (option 4) is the flawed view of language. An error-free translation (option 3) shows no degradation."))) +
 final("Option 3"),
 "except",
 [("1", "Prediction without explanation: ‘pseudoscience’."), ("2", "Ethics debased."), ("4", "Language treated as patterns.")])

P.rc(2, "V1", "Inference", "4", "Medium",
 "What does the author grant machine learning?",
 steps(("The line", ev(3, "The crux of machine learning is description and prediction") +
          ev(3, "An explanation includes not only descriptions and predictions but also counterfactual conjectures") +
          p("Humans also describe and predict; they add explanation.")),
       ("Choosing", p("Option 4."))) +
 final("Option 4"),
 "inference",
 [("1", "Only humans have the innate operating system."), ("2", "Only humans think morally."), ("3", "Machine learning posits no causes.")],
 opts=["The innate operating system they use for language acquisition.", "Their capacity for moral thinking and evaluating ethical principles.",
       "Providing causal explanations for observed phenomena.", "Both can describe what is the case and predict what will be the case."])

P.rc(3, "V1", "Detail", "2", "Easy",
 "What makes even a correct prediction pseudoscience?",
 steps(("The line", ev(4, "Even in instances when such programs can successfully generate correct “scientific” predictions without using explanations, such prediction is pseudoscience")),
       ("Choosing", p("Option 2."))) +
 final("Option 2"),
 "detail",
 [("1", "Reversed."), ("3", "The passage’s test is explanation, not the method of prediction."), ("4", "Anecdotes are not mentioned.")])

P.rc(4, "V1", "Inference", "4", "Hard",
 "Look for the option that has all of the author’s contrast: description and prediction against explanation and error correction.",
 steps(("The lines", ev(3, "The crux of machine learning is description and prediction; it does not posit any causal mechanisms or physical laws") +
          ev(3, "Human-style thought is based on possible explanations and error correction, a process that gradually limits what possibilities can be rationally considered")),
       ("Choosing", p("Option 4 has both halves. Options 2 and 3 have parts of it."))) +
 final("Option 4"),
 "inference",
 [("1", "‘Prehuman’ is a description, not the key distinction."), ("2", "Leaves out explanation and error correction."), ("3", "Leaves out error correction and the limiting of possibilities.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Main_Idea", "3", "Easy",
 "The passage covers the term’s use, its origin and its decline.",
 steps(("The thread", ev(2, "it is important to explore its exact origin and meanings")),
       ("Choosing", p("Option 3 covers history and present significance; options 2 and 4 cover one part each."))) +
 final("Option 3"),
 "inference",
 [("1", "Only the use in media."), ("2", "Only the decline."), ("4", "Only the history.")])

P.rc(6, "V2", "Purpose", "2", "Medium",
 "What does the author do with the examples next?",
 steps(("The line", ev(2, "Seen from the perspective of han, such emotions seem to be the common theme running throughout all the works. That notion is a questionable one")),
       ("Choosing", p("The examples show how han is read into work after work: option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "The author questions that han is ingrained."), ("3", "The emotions are listed, but the point is the recurring reading."), ("4", "The struggle is described later, not by the examples.")])

P.rc(7, "V2", "Detail", "2", "Easy",
 "From central to irrelevant.",
 steps(("The lines", ev(4, "major literary figures […] claimed han to be the central aesthetic principle in Korean art and literature") +
          ev(6, "the larger idea of han as a defining characteristic feels increasingly like a retrograde notion from the past")),
       ("Choosing", p("Option 2."))) +
 final("Option 2"),
 "detail",
 [("1", "Only the first half."), ("3", "Disparity is a separate issue."), ("4", "Prosperity made han fade.")])

P.rc(8, "V2", "Except", "3", "Medium",
 "What do Parasite and Squid Game allegorise, according to the author?",
 steps(("The line", ev(5, "Of course, the people of the country experience economic disparity, as brilliantly allegorised in Parasite and Squid Game")),
       ("Choosing", p("They allegorise economic disparity, and the author questions reading han into them: option 3."))) +
 final("Option 3"),
 "except",
 [("1", "Fits the decline."), ("2", "Stated."), ("4", "Stated.")])

# ---------------- Passage 3 (Q9–12) ----------------
P.rc(9, "V3", "Except", "2", "Easy",
 "Liberals sort states into good and bad.",
 steps(("The line", ev(1, "For liberals, therefore, there are \"good\" and \"bad\" states in the international system")),
       ("Choosing", p("Option 2 says all states are good, against the passage."))) +
 final("Option 2"),
 "except",
 [("1", "One of liberalism’s theories."), ("3", "The second core belief."), ("4", "Another liberal theory.")],
 q="Which of the following is NOT part of liberalism’s view of international politics as described in the passage?")

P.rc(10, "V3", "Except", "2", "Medium",
 "Which option is about something the economic argument does not cover?",
 steps(("The argument", ev(2, "Many wars are waged to gain or preserve wealth, but states have much less motive to initiate war if they are already wealthy")),
       ("Choosing", p("Options 1, 3 and 4 follow from it. Wars for ideology or territory (option 2) lie outside it."))) +
 final("Option 2"),
 "except",
 [("1", "Interdependence pushes states to settle disputes."), ("3", "Restates the wealth argument."), ("4", "‘Biting the hand that feeds them’.")],
 opts=["Tensions arising from economic interdependence push states to settle disputes amicably.",
       "States may go to war for reasons other than wealth, such as ideology or territory.",
       "Prosperous states have less motive to start wars to gain wealth.",
       "Economic interdependence makes offending states more vulnerable to sanctions and disruption."])

P.rc(11, "V3", "Weaken", "1", "Medium",
 "The claim: institutions change state behaviour and push states from war.",
 steps(("The claim", ev(4, "Liberals claim that these institutions or rules can fundamentally change state behaviour")),
       ("Choosing", p("Options 2–4 show institutions failing to change behaviour. Option 1 (slow to adapt, contested norms) does not show that."))) +
 final("Option 1"),
 "weaken",
 [("2", "States ignore the rules."), ("3", "Institutions serve power."), ("4", "They fail without universal support.")])

P.rc(12, "V3", "Structure", "2", "Medium",
 "Liberalism plus its three main theories, leading to peace.",
 steps(("Topics", p("Liberalism, then three theories: economic interdependence, democratic peace and international institutions, all about peace.")),
       ("Choosing", p("Option 2 names all three theories. Option 4 leaves out democratic peace and institutions."))) +
 final("Option 2"),
 "summary",
 [("1", "Vague: ‘Economic Cooperation’."), ("3", "Leaves out democratic peace."), ("4", "Leaves out two of the three theories.")])

# ---------------- Passage 4 (Q13–16) ----------------
P.rc(13, "V4", "Inference", "4", "Medium",
 "Which statement matches the description of chaos?",
 steps(("The line", ev(2, "may be predictable over short periods but is subject to increasingly dramatic shifts the further out you go")),
       ("Choosing", p("Option 4 matches. Options 2 and 3 contradict the passage; option 1 is not in it."))) +
 final("Option 4"),
 "inference",
 [("1", "Not discussed."), ("2", "Nonlinear systems do behave chaotically."), ("3", "Random events are unpredictable.")],
 q="Which of the following statements is consistent with the passage?")

P.rc(14, "V4", "Main_Idea", "3", "Easy",
 "The last paragraph adds a caution.",
 steps(("The line", ev(7, "The classical concept of chaos is fundamentally a stationary concept") +
          ev(7, "scientists will have to be conscious of this ever-shifting baseline")),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "inference",
 [("1", "Overstates the promise."), ("2", "That is an earlier paragraph."), ("4", "Earlier studies missed chaos for a different reason.")])

P.rc(15, "V4", "Inference", "2", "Medium",
 "How does a chaotic system’s predictability change over time?",
 steps(("The line", ev(2, "But a chaotic system — one ruled by nonlinear responses to events — may be predictable over short periods but is subject to increasingly dramatic shifts the further out you go")),
       ("Choosing", p("Option 2 has both halves; option 1 only the long-term half."))) +
 final("Option 2"),
 "inference",
 [("1", "Only the long term."), ("3", "Stable systems change little."), ("4", "That is a stable system.")],
 opts=["A chaotic system exhibits unpredictable and dramatic shifts over longer timescales.",
       "A chaotic system may be predictable in the short term but becomes increasingly unpredictable further out.",
       "The apparently predictable behaviour of stable systems is ultimately unpredictable.",
       "A chaotic system may remain constant, with changes within predictable bounds."])

P.rc(16, "V4", "Detail", "2", "Easy",
 "Only one statement matches the last paragraph.",
 steps(("The line", ev(7, "It is built on the assumption that chaotic fluctuations represent a departure from some predictable, stable norm")),
       ("Choosing", p("Option 2."))) +
 final("Option 2"),
 "detail",
 [("1", "The passage says such models could help, not that they have ended overfishing."), ("3", "Ecologists caution against too much faith."), ("4", "Ecosystems are becoming less stable.")],
 q="Which of the following is true about chaos-conscious models in ecological forecasting, according to the passage?",
 opts=["Improved chaos-conscious models have already ended overfishing.",
       "The classical concept of chaos assumes that chaotic fluctuations represent a departure from some predictable, stable norm.",
       "Some ecologists believe that chaos-conscious models should be relied upon entirely for ecological forecasting.",
       "As climate change progresses, real-world ecosystems are becoming more predictable over time."])

# ---------------- Verbal ability (Q17–24) ----------------
P.va(17, P.sent_html(17), [], "TITA", "4312", "Para_Jumble", "Easy",
 "Need, problem, solution, detail.",
 steps(("Order", p("Sentence 4: innovation is essential. Sentence 3: many firms are trapped. Sentence 1: ‘this challenge’ — foster innovation. Sentence 2: ‘This may involve’ — the specifics."))) +
 final("4312"),
 "pj",
 [("4", "Topic."), ("3", "Problem."), ("1", "“This challenge”."), ("2", "“This may involve”.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.sent_html(18), [], "TITA", "3241", "Para_Jumble", "Medium",
 "Follow the events in time.",
 steps(("Order", p("Sentence 3: McClellan halts outside Richmond. Sentence 2: Lincoln refuses reinforcements. Sentence 4: Johnston’s surprise attack. Sentence 1: McClellan’s slow counterattack and the result."))) +
 final("3241"),
 "pj",
 [("3", "Setting."), ("2", "The halt drags on."), ("4", "The attack."), ("1", "The response.")],
 why_title="Why each sentence goes where it does")

P.va(19, P.sent_html(19), [], "TITA", "2413", "Para_Jumble", "Medium",
 "‘However’ and ‘Nonetheless’ each need something before them.",
 steps(("Pairs", p("2–4: the polycrisis, ‘however’ other problems too. 1–3: rethinking neglected economics, ‘nonetheless’ feminist economics advances.")),
       ("Order", p("Problems first, then the response: 2413."))) +
 final("2413"),
 "pj",
 [("2", "The polycrisis."), ("4", "“However”: more problems."), ("1", "Rethinking needed."), ("3", "“Nonetheless”: progress.")],
 why_title="Why each sentence goes where it does")

P.va(20, P.missing_html(20), P.strict_opts(20), "MCQ", "1", "Missing_Sentence", "Easy",
 "‘However’ after blank 1 needs a point in favour of plastic bags.",
 steps(("Find the spot", p("Blank 1: bags are cheap and convenient. ‘However, plastic bags take a significant toll…’ then turns against them.")),
       ("Check the others", p("Blanks 2–4 are in the middle of the case against bags and the alternatives."))) +
 final("Option 1"),
 "missing",
 [("2", "Inside the harms."), ("3", "Inside the alternatives."), ("4", "After the conclusion.")])

P.va(21, P.missing_html(21), P.strict_opts(21), "MCQ", "2", "Missing_Sentence", "Easy",
 "‘This complexity’ needs complexity named just before it.",
 steps(("Find the spot", p("Blank 2 comes right before ‘This complexity allows us…’.")),
       ("Check the others", p("At blank 1 the word ‘complexity’ would be four sentences away from ‘This complexity’; blanks 3 and 4 come after it."))) +
 final("Option 2"),
 "missing",
 [("1", "Too far from ‘This complexity’."), ("3", "After it."), ("4", "After it.")])

P.va(22, P.summary_html(22, "While the economic inequalities"), P.Q["VARC"][22]["opts"], "MCQ", "3", "Summary", "Medium",
 "Grievances, respect, and the narrow economic model.",
 steps(("What the passage says", "<ol><li>Economic grievances from globalisation sharpen when tied to indignity.</li><li>Economic motives are partly about status and respect.</li><li>So the utility-maximising model is too narrow.</li></ol>"),
       ("Choosing", p("Option 3."))) +
 final("Option 3"),
 "summary",
 [("1", "Says the assumption worsens grievances."), ("2", "‘Rather than just wealth’ is fine, but it drops globalisation and the model’s narrowness."), ("4", "Says the assumption worsens inequality.")])

P.va(23, P.summary_html(23, "Every technology is"), P.Q["VARC"][23]["opts"], "MCQ", "2", "Summary", "Medium",
 "Four categories, with the fourth singled out.",
 steps(("What the passage says", "<ol><li>Technologies express human will.</li><li>They fall into four groups: strength, senses, reshaping nature, intellect.</li><li>Intellectual technologies are the most intimate, shaping identity.</li></ol>"),
       ("Choosing", p("Option 2 keeps the four groups and the intimate role of the last."))) +
 final("Option 2"),
 "summary",
 [("1", "‘Relationship with nature’ blurs ‘reshaping nature’."), ("3", "Drops the nature group."), ("4", "Merges physical and mental skills.")])

P.va(24, P.summary_html(24, "Psychologists"), P.Q["VARC"][24]["opts"], "MCQ", "4", "Summary", "Medium",
 "The new research replaces the old explanation.",
 steps(("What the passage says", "<ol><li>The old view: conservatives see the world as more dangerous.</li><li>New research contradicts it.</li><li>The main difference is belief in a hierarchical world.</li></ol>"),
       ("Choosing", p("Option 4."))) +
 final("Option 4"),
 "summary",
 [("1", "Keeps the danger view the research rejects."), ("2", "Same error."), ("3", "Same error.")])
