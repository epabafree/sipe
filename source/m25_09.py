# -*- coding: utf-8 -*-
# Simp Mock 9 (2025): VARC (24 of 24). DILR and QA: m25_09_dilr.py, m25_09_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(9, "sm25_09.json", series=2025)
P.passage("V1", "Passage 1 — Crony capitalism", "Economics_and_Management")
P.passage("V2", "Passage 2 — The mutations we collect", "Environment_and_Life_Science")
P.passage("V3", "Passage 3 — Translation as a historian’s craft", "Social_Science_and_History")
P.passage("V4", "Passage 4 — Speculative Realism", "Philosophy_and_Psychology")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Inference_Except", "3", "Medium",
 "Find the one statement the author would accept.",
 steps(("The author’s view", ev(6, "It is hard to separate policies that favour specific firms for the greater good from those that benefit them due to personal connections") +
          p("So genuine industrial policy can look like cronyism: the author agrees with option 3.")),
       ("The others", p("The passage dates the crisis to the late 20th century and says some economists ‘reach for’ cronyism, not that it alone caused it (1). Cronyism ‘does not grease the wheels’ (2). Fast growth coexisted with cronyism; it needn’t (4)."))) + final("Option 3"),
 "except", [("1", "‘Alone’ and the wrong century."), ("2", "‘Only limited evidence that cronyism benefits an economy’."), ("4", "‘Must’ is not argued.")])
P.rc(2, "V1", "Inference", "1", "Medium",
 "Cronyism is about relationships; rent-seeking is about competing for specific privileges.",
 steps(("The two", ev(1, "A cosy relationship between governments and firms distorted markets") +
          ev(3, "how governments might issue import licences to favoured companies") +
          p("Crony capitalism rests on close ties; rent-seeking is the chase for particular privileges such as licences."))) + final("Option 1"),
 "inference", [("2", "Neither is called beneficial."), ("3", "Lobbying belongs to rent-seeking too."), ("4", "Not stated.")])
P.rc(3, "V1", "Purpose", "2", "Medium",
 "Why mention leaders becoming ‘synonymous’ with growth?",
 steps(("Context", ev(4, "For all the theory, evidence of aggregate harm can be difficult to spot") +
          p("Growth gets the attention and the credit; the corruption underneath is harder to see."))) + final("Option 2"),
 "purpose", [("1", "‘Invariably’ goes too far."), ("3", "Not the point of the line."), ("4", "The author denies cronyism is beneficial.")])
P.rc(4, "V1", "Inference", "4", "Medium",
 "What did corruption evolve into?",
 steps(("The line", ev(5, "These are then formalised and legalised, perhaps through campaign finance") +
          p("The claim assumes corruption can take institutional, even legal, forms."))) + final("Option 4"),
 "inference", [("1", "‘Worldwide … eliminated’ is too strong."), ("2", "Not about who pioneered it."), ("3", "‘Accepted frameworks of governance’ overstates.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Detail_Not_True", "4", "Easy",
 "Which outcome is never mentioned?",
 steps(("Mentioned", p("Cancers (1), neurological diseases (2) and a one-third lower Alzheimer’s risk (3).")),
       ("Not mentioned", p("Nothing about reversing inherited disorders."))) + final("Option 4"),
 "notrue", [("1", "Blood cancer risk."), ("2", "‘neurological diseases’."), ("3", "‘one-third lower risk of Alzheimer’s’.")])
P.rc(6, "V2", "Inference", "3", "Easy",
 "Why is it a ‘miracle’?",
 steps(("Context", ev(3, "With around 30 trillion cells and 4 million dividing every second, even rare mistakes build up") +
          p("Despite thousands of typos per cell, the body keeps working well for decades."))) + final("Option 3"),
 "inference", [("1", "Errors ‘pile up despite’ repair."), ("2", "We are ‘riddled with them’."), ("4", "Mutations are acquired, not inherited.")])
P.rc(7, "V2", "Inference", "4", "Medium",
 "Clones: higher risk of some diseases, lower risk of one.",
 steps(("The line", ev(5, "were linked to higher risks of blood cancer, heart disease, and stroke—yet surprisingly, they were also tied to a one-third lower risk of Alzheimer’s") +
          p("Their growth advantage cuts both ways."))) + final("Option 4"),
 "inference", [("1", "They persist for decades."), ("2", "Not ‘invariably’: Alzheimer’s risk falls."), ("3", "The reverse for Alzheimer’s.")])
P.rc(8, "V2", "Weaken", "2", "Medium",
 "The claim: reproductive cells accumulate far fewer errors.",
 steps(("The claim", ev(3, "Errors are far fewer in cells that give rise to eggs and sperm")),
       ("The weakener", p("If reproductive cells pile up errors at the same rate as others, the ‘pristine DNA’ claim fails."))) + final("Option 2"),
 "weaken", [("1", "Supports it."), ("3", "About blood clones, not reproductive cells."), ("4", "About somatic tissue; consistent with the claim.")])

# ---------------- Passage 3 (Q9–12) ----------------
P.rc(9, "V3", "Inference_Except", "4", "Medium",
 "Does the author favour modernising old texts?",
 steps(("The interplay", ev(2, "Translators do not just translate words; they also translate a universe of discourse, a poetics, and an ideology") +
          p("Ideology in language (1), cultural and temporal context (2) and events shaped by how language encodes them (3) all follow.")),
       ("The odd one", p("Modernising the language risks losing exactly that context; the author never suggests it preserves meaning."))) + final("Option 4"),
 "except", [("1", "‘an ideology’."), ("2", "‘universe of discourse’."), ("3", "Language and history interplay.")])
P.rc(10, "V3", "Inference_Except", "4", "Easy",
 "What does the author do with other primary sources?",
 steps(("The line", ev(3, "To verify the accuracy of both substance and style, I lean on other primary sources") +
          p("The author uses other sources; option 4 says the opposite."))) + final("Option 4"),
 "except", [("1", "‘historical practices in linguistic decisions’."), ("2", "‘the history gets lost in translation no matter how clear the words’."), ("3", "Context and ideology.")])
P.rc(11, "V3", "Main_Idea", "2", "Medium",
 "Paragraph 3: translation is treated as technical, but it needs history.",
 steps(("The point", ev(3, "Yet translating primary sources requires more than language comprehension") +
          p("Historical knowledge and careful interpretation are the main argument."))) + final("Option 2"),
 "inference", [("1", "The author wants historians themselves to do it."), ("3", "A detail."), ("4", "The opposite.")])
P.rc(12, "V3", "Purpose", "3", "Medium",
 "Why bring in literary theory and historical linguistics?",
 steps(("The line", ev(4, "They will help us all understand better both history in translation and translation in history") +
          p("Related fields help keep translations true to their historical context."))) + final("Option 3"),
 "purpose", [("1", "Not about technical skills."), ("2", "Poetry isn’t the comparison."), ("4", "Not instead of historiography.")])

# ---------------- Passage 4 (Q13–16) ----------------
P.rc(13, "V4", "Detail", "4", "Medium",
 "What role does the passage give to objects?",
 steps(("The line", ev(4, "are not merely backdrops to human drama but active participants in a shared reality") +
          p("Nonhuman entities act in the world."))) + final("Option 4"),
 "detail", [("1", "It critiques correlationism but doesn’t ‘demonstrate irrelevance’."), ("2", "The opposite."), ("3", "Climate and AI are examples, not its focus.")])
P.rc(14, "V4", "Purpose", "3", "Easy",
 "‘Regardless of whether we believe’.",
 steps(("The point", ev(2, "the Earth’s systems operate independently of our debates or biases") +
          p("Reality works independently of perception."))) + final("Option 3"),
 "purpose", [("1", "Policy delay is a side remark."), ("2", "The opposite."), ("4", "Human causes aren’t discussed.")])
P.rc(15, "V4", "Detail", "3", "Easy",
 "How do proponents answer the critics?",
 steps(("The reply", ev(3, "the world’s material and nonhuman elements must be understood alongside the human-centered issues") +
          p("Power, justice and identity stay central, studied together with the nonhuman."))) + final("Option 3"),
 "detail", [("1", "They’re not dismissed."), ("2", "Not overshadowed."), ("4", "Not called unreal.")])
P.rc(16, "V4", "Tone", "2", "Easy",
 "Concepts explained, critics answered, a balanced close.",
 steps(("The tone", p("The passage explains correlationism, gives examples, presents the critics and the reply, and ends on ‘a much-needed debate’: objective and explanatory."))) + final("Option 2"),
 "inference", [("1", "Its examples are concrete, not mere speculation."), ("3", "Calm, not alarmist."), ("4", "Not ‘selectively’, and critics are given space.")])

# ---------------- Summaries (Q17–19) ----------------
P.va(17, P.summary_html(17, "Words and sentences"), P.Q["VARC"][17]["opts"], "MCQ", "2", "Summary", "Hard",
 "Context changes meaning; first-person present ‘I believe’ makes itself true and isn’t testable.",
 steps(("Choosing", p("Option 2 has both: context-dependence, and the self-instantiating, untestable first-person use."))) + final("Option 2"),
 "summary", [("1", "Leaves out ‘not testable’."), ("3", "Leaves out ‘not testable’ and the context point."), ("4", "Leaves out the broader point about context.")])
P.va(18, P.summary_html(18, "Yes, life is"), P.Q["VARC"][18]["opts"], "MCQ", "3", "Summary", "Hard",
 "Life as waiting; death all around; we forget it by wandering in symbols and philosophy.",
 steps(("Choosing", p("Option 3 keeps waiting, the avoidance of death, and the immersion in symbols, philosophy and metaphysical wandering."))) + final("Option 3"),
 "summary", [("1", "‘Ongoing confrontation’ misses the waiting."), ("2", "‘Coping mechanisms’ is added."), ("4", "Misses the waiting and forgetting.")])
P.va(19, P.summary_html(19, "Pregnancy profoundly reshapes"), P.Q["VARC"][19]["opts"], "MCQ", "1", "Summary", "Medium",
 "The trigger is the abrupt hormonal withdrawal after pregnancy.",
 steps(("Choosing", p("Option 1 has the sudden shift, the overstimulated emotional and compulsive regions, and writing as a way to cope with grief."))) + final("Option 1"),
 "summary", [("2", "Pregnancy itself isn’t the trigger."), ("3", "Leaves out the overstimulated regions."), ("4", "Makes bipolar disorder central.")])

# ---------------- Missing sentences (Q20–22) ----------------
P.va(20, P.missing_html(20), P.Q["VARC"][20]["opts"], "MCQ", "3", "Missing_Sentence", "Hard",
 "‘The result’ restates a fusion of nostalgia and technology.",
 steps(("Find the spot", p("Blank 4 follows ‘viewers experienced an unprecedented fusion of nostalgia and technical brilliance’. The sentence unpacks it: regal gravitas fans cherish (nostalgia), elevated by digital wizardry (technical brilliance). Then the close credits Ferrara.")),
       ("Match the label", p("Blank 4 is choice 3, labelled ‘Option 4’."))) +
 trap("Blank 3 is tempting, but ‘Thanks to these innovations’ must follow the VR description directly.") + final("Choice 3 (“Option 4”)"),
 "missing", [("1", "“Option 3”: would split the VR account from ‘Thanks to these innovations’."), ("2", "“Option 1”: nothing has been made yet."), ("4", "“Option 2”: before the VR explanation.")])
P.va(21, P.missing_html(21), P.Q["VARC"][21]["opts"], "MCQ", "2", "Missing_Sentence", "Easy",
 "The sentence opens the list of troubles that follows.",
 steps(("Find the spot", p("Blank 2 follows the design’s selection in 1957; then come costs, technical challenges and Utzon’s resignation.")),
       ("Match the label", p("Blank 2 is choice 2, labelled ‘Option 2’."))) + final("Choice 2 (“Option 2”)"),
 "missing", [("1", "“Option 1”: before the design was chosen."), ("3", "“Option 3”: costs already described."), ("4", "“Option 4”: after the resignation.")])
P.va(22, P.missing_html(22), P.Q["VARC"][22]["opts"], "MCQ", "3", "Missing_Sentence", "Medium",
 "Protests and defiance follow courage under repression.",
 steps(("Find the spot", p("Blank 3 follows ‘displayed remarkable courage and resilience’ and comes before ‘Its legacy’.")),
       ("Match the label", p("Blank 3 is choice 3, labelled ‘Option 3’."))) + final("Choice 3 (“Option 3”)"),
 "missing", [("1", "“Option 4”: after the close."), ("2", "“Option 1”: before the movement is described."), ("4", "“Option 2”: before the repression.")])

# ---------------- Odd one out (Q23–24) ----------------
P.va(23, P.sent_html(23), [], "TITA", "3", "Odd_One_Out", "Medium",
 "Four sentences are about studying whether cutting social media helps. One is a general claim about decline.",
 steps(("The chain", p("2 → 4 → 5 → 1: a link exists but causation is disputed (2); such studies are hard to design (4); groups should quit together (5); a control group is needed (1).")),
       ("The odd one", p("Sentence 3 states the decline in teen mental health, background the chain doesn’t use."))) + final("3"),
 "oddone", [("1", "The design requirement."), ("2", "The question."), ("4", "The difficulty."), ("5", "The proposed design.")], why_title="How the other sentences fit")
P.va(24, P.sent_html(24), [], "TITA", "3", "Odd_One_Out", "Medium",
 "Four sentences move from the Year of Glaciers to the Hindu Kush Himalayas. One is a quote.",
 steps(("The chain", p("2 → 4 → 1 → 5: the UN year and melting ice (2); climate change accelerating it in the Hindu Kush Himalayas (4); that range warming fast (1); what 3°C would do (5).")),
       ("The odd one", p("Sentence 3, the launch quote, breaks the line from the global to the regional."))) + final("3"),
 "oddone", [("1", "The range described."), ("2", "The opening."), ("4", "The region named."), ("5", "The consequence.")], why_title="How the other sentences fit")
