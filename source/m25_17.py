# -*- coding: utf-8 -*-
# Simp Mock 17 (2025): VARC (24 of 24). DILR and QA: m25_17_dilr.py, m25_17_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(17, "sm25_17.json", series=2025)
P.passage("V1", "Passage 1 — The small words that run a conversation", "Social_Science_and_History")
P.passage("V2", "Passage 2 — Merit needs inclusion", "Economics_and_Management")
P.passage("V3", "Passage 3 — The wandering magnetic north pole", "Science_and_Technology")
P.passage("V4", "Passage 4 — The ends of knowledge", "Philosophy_and_Psychology")

# the source paragraph labels its second blank “3”; restore 2
_q9 = P.Q["VARC"][9]["q"]
P.Q["VARC"][9]["q"] = _q9.replace("_____3____", "_____2____", 1)


def listed(n, direc):
    parts = [x.strip() for x in P.Q["VARC"][n]["q"].split("\n\n") if x.strip()]
    return f"<p>{direc}</p><ol class=\"sent\">" + "".join(f"<li>{x}</li>" for x in parts[1:]) + "</ol>"


# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Inference_Except", "1", "Medium",
 "Are interjections ‘purely cultural’?",
 steps(("The line", ev(2, "In a survey of 31 languages, Dingemanse found all used a short, neutral syllable like 'huh?' as a repair signal") +
          p("The passage stresses shared functions across languages, so ‘purely cultural’ clashes with it.")),
       ("The others", p("Different forms in different languages (2), feedback that shapes storytelling (3), and AI’s struggle (4) are all in the passage."))) + final("Option 1"),
 "except", [("2", "Mandarin, Canadian ‘eh?’."), ("3", "The story experiment."), ("4", "‘a telltale sign of human speech’.")])
P.rc(2, "V1", "Inference_Except", "4", "Hard",
 "Which reason is about ‘acknowledging’ a speaker, not about handling signals?",
 steps(("Reasons implied", p("Meaning depends on context and tone (1: ‘oh’), languages differ (2), and turn-taking and engagement signals are subtle (3).")),
       ("The odd one", ev(7, "you’re acknowledging someone is trying to communicate with you") +
          p("This reflexivity is offered as part of what language is, not as a reason AI fails; the passage never ties AI’s difficulty to conscious recognition."))) + final("Option 4"),
 "except", [("1", "Tone and context."), ("2", "Variation across languages."), ("3", "Turn-taking and continuers.")])
P.rc(3, "V1", "Purpose", "2", "Easy",
 "Mandarin does it one way; English another.",
 steps(("The line", ev(5, "Different languages handle these nuances in distinct ways") +
          p("Mandarin is the contrast case: languages vary in how they mark shared knowledge."))) + final("Option 2"),
 "purpose", [("1", "Mandarin isn’t said to avoid interjections."), ("3", "No frequency comparison."), ("4", "Nothing about misunderstanding.")])
P.rc(4, "V1", "Inference", "3", "Medium",
 "‘Language exists because we need to interact.’",
 steps(("The line", ev(7, "Language exists because we need to interact") +
          p("Interjections are basic to how conversation and social interaction work.")),
       ("Why not 1", p("‘necessary … at all levels’ goes beyond the claim."))) + final("Option 3"),
 "inference", [("1", "Too absolute."), ("2", "‘entirely incomprehensible’ is extreme."), ("4", "Complexity isn’t counted that way.")])

# ---------------- Passage 2 (Q5–8) ----------------
P.rc(5, "V2", "Main_Idea", "4", "Medium",
 "Where does the author end up?",
 steps(("The line", ev(6, "Inclusive merit is about designing systems that recognize and reward talent in all its forms") +
          p("Fairness comes from merit plus inclusion: removing barriers so talent is recognised.")),
       ("The others", p("Option 3 is the history; option 2 the diagnosis; option 1 calls the ideal unattainable, which the author doesn’t."))) + final("Option 4"),
 "summary", [("1", "Too pessimistic."), ("2", "Only the problem."), ("3", "Only the background.")])
P.rc(6, "V2", "Purpose", "1", "Easy",
 "Satire taken as an ideal.",
 steps(("The line", ev(2, "Nevertheless, many readers interpreted the idea of meritocracy as positive") +
          p("Young’s dark satire became a cherished ideal: a misreading.")),
       ("Why not 3", p("‘evolved … to a widely accepted principle’ misses the misinterpretation the author stresses."))) + final("Option 1"),
 "purpose", [("2", "A detail of the satire."), ("3", "Leaves out the misreading."), ("4", "The author doesn’t endorse Young’s society.")])
P.rc(7, "V2", "Detail_Not_True", "3", "Easy",
 "What do perceptions of merit fail to reflect?",
 steps(("The line", ev(3, "Perceptions of merit are frequently shaped by biases and social capital rather than objective performance") +
          p("Objective performance is exactly what perceptions are not based on.")),
       ("The others", p("Harsher judgement of the marginalised (1), social capital (2) and birth circumstances (4) are listed."))) + final("Option 3"),
 "except", [("1", "‘judged more harshly’."), ("2", "‘social capital’."), ("4", "‘circumstances of one’s birth’.")])
P.rc(8, "V2", "Tone", "2", "Easy",
 "Diagnosis, then a proposal.",
 steps(("The tone", p("The author examines how merit is misused and argues for inclusive merit: analytical and constructive, not cynical."))) + final("Option 2"),
 "inference", [("1", "Not dismissive of merit."), ("3", "Too upbeat for the critique."), ("4", "The author takes a position.")])

P.va(9, P.ms(9), P.Q["VARC"][9]["opts"], "MCQ", "1", "Missing_Sentence", "Easy",
 "Stunting has to be introduced before ‘stunting rates’.",
 steps(("Find the spot", p("Blank 4 follows ‘Chronic undernutrition leads to stunting, which impairs brain development’.")),
       ("Match the label", p("Blank 4 is choice 1, labelled ‘Option 4’."))) + final("Choice 1 (“Option 4”)"),
 "missing", [("2", "“Option 2”: before stunting is mentioned."), ("3", "“Option 1”: too early."), ("4", "“Option 3”: still on poverty.")])
P.va(10, listed(10, P.PJ_DIR), [], "TITA", "3241", "Para_Jumble", "Easy",
 "Scale, a gender fact, consequences, ‘Moreover’ for women.",
 steps(("Opening", p("3 gives the global scale.")),
       ("Links", p("2 adds that disability is more common among women; 4 states the obstacles; 1 (‘Moreover … even more severe’) adds the worse outcomes for women."))) + final("3241"),
 "pj", [("1", "‘Moreover’ needs a prior point."), ("2", "‘some facts are clear’ follows an introduction."), ("4", "Needs the group introduced.")], why_title="Why the others can’t open")

# ---------------- Passage 3 (Q11–14) ----------------
P.rc(11, "V3", "Detail_Not_True", "4", "Medium",
 "What is said to drive the pole?",
 steps(("Named", ev(2, "This field is generated by the churning of molten iron and nickel in the outer core") +
          p("The geodynamo (1), uneven strength near Canada and Siberia (2), and a weakening field (3).")),
       ("The odd one", p("‘Geologic realignment of the poles’ isn’t offered; reversal is speculative and about the future."))) + final("Option 4"),
 "except", [("1", "Geodynamo."), ("2", "Beggan."), ("3", "‘weakened … unevenly’.")])
P.rc(12, "V3", "Detail_Not_True", "1", "Medium",
 "Is there agreement on what pulls the pole?",
 steps(("The line", ev(4, "Some researchers believe shifts in the magnetic field’s strength near Canada and Siberia influence its movement") +
          p("Only ‘some researchers’ hold this, and the ‘pull’ is uneven strength, not weakening as such.")),
       ("Agreed", p("Acceleration over the century (2), the record slowdown (3) and unclear causes (4)."))) + final("Option 1"),
 "except", [("2", "6 to 31 miles a year."), ("3", "‘biggest deceleration’."), ("4", "‘remain unclear’.")])
P.rc(13, "V3", "Detail_Not_True", "4", "Medium",
 "Which effect does the passage actually describe?",
 steps(("Described", ev(5, "In 2019, scientists released the WMM a year early because the pole was moving unusually fast") +
          p("Navigation errors (1), frequent updates (2) and the early release (3) all appear.")),
       ("The odd one", p("Animals are said to rely on the field’s stability, but changed migration is never described."))) + final("Option 4"),
 "except", [("1", "93 miles off course."), ("2", "Updated every five years."), ("3", "2019.")],
 q="Which of the following is NOT described in the passage as a consequence of the changing magnetic field?")
P.rc(14, "V3", "Inference", "3", "Easy",
 "What do scientists say about the timing?",
 steps(("The line", ev(5, "However, scientists cannot predict when the next will happen") +
          p("The author treats the timing of a reversal as unpredictable."))) + final("Option 3"),
 "inference", [("1", "No timing given."), ("2", "Reversals have happened; only timing is uncertain."), ("4", "Not claimed.")])

P.va(15, P.ms(15), P.Q["VARC"][15]["opts"], "MCQ", "2", "Missing_Sentence", "Easy",
 "‘these vaccines’ in the next sentence needs vaccines just named.",
 steps(("Find the spot", p("Blank 3 comes after the 1950s research and before ‘Researchers are testing these vaccines’.")),
       ("Match the label", p("Blank 3 is choice 2, labelled ‘Option 3’."))) + final("Choice 2 (“Option 3”)"),
 "missing", [("1", "“Option 1”: before the discovery."), ("3", "“Option 2”: still in the 19th century."), ("4", "“Option 4”: after the conclusion.")])
P.va(16, P.summary_html(16, "In the early 2010s"), P.Q["VARC"][16]["opts"], "MCQ", "4", "Summary", "Medium",
 "Cause (passive listeners) and effect (a homogeneous genre).",
 steps(("The core", p("Targeting background listeners rewarded bland music and produced ‘Spotifycore’.")),
       ("Choosing", p("Option 4 has the shift and the resulting genre. Option 1 stops before the genre; option 2 credits an algorithm."))) + final("Option 4"),
 "summary", [("1", "Misses the genre."), ("2", "‘algorithm-driven’ isn’t in the passage."), ("3", "Too general.")])

# ---------------- Passage 4 (Q17–20) ----------------
P.rc(17, "V4", "Detail_Not_True", "1", "Medium",
 "Which item is a response the authors reject, not a cause?",
 steps(("Causes", ev(1, "technological advances—such as new artificial intelligence programmes—may soon outstrip human ingenuity") +
          p("Technology (2), loss of trust in certifying systems (3) and political attacks on objectivity (4).")),
       ("The odd one", p("Economic utilitarianism appears only as something reorienting ‘need not mean capitulating to’."))) + final("Option 1"),
 "except", [("2", "AI."), ("3", "Systems ‘have either ended or are ending’."), ("4", "Extreme political movements.")])
P.rc(18, "V4", "Detail_Not_True", "2", "Medium",
 "Do the authors promise measurable outcomes?",
 steps(("Reasons given", ev(3, "scholars must identify the goal of their work—both to advance the Enlightenment project of useful knowledge and to defend themselves from mischaracterisation") +
          p("Defence (1), articulating goals (3), rethinking boundaries (4).")),
       ("The odd one", p("Nothing guarantees tangible, measurable results; ‘ends’ include purposes, not just outputs."))) + final("Option 2"),
 "except", [("1", "‘defend themselves’."), ("3", "‘articulate why they do what they do’."), ("4", "Last paragraph.")])
P.rc(19, "V4", "Inference", "1", "Easy",
 "Read the sentence before it.",
 steps(("The line", ev(6, "We are only at the beginning of rethinking our scholarly futures") +
          p("The rethinking has just begun; its effects lie ahead."))) + final("Option 1"),
 "inference", [("2", "Too gloomy."), ("3", "Not said."), ("4", "Not said.")])
P.rc(20, "V4", "Application", "3", "Medium",
 "Confronting an end that clarifies purpose and method.",
 steps(("The idea", ev(2, "The prospect of an imposed end can help clarify both the purpose and endpoint of scholarship") +
          p("Alchemy’s end gave rise to chemistry with a clear purpose and method.")),
       ("Why not 2", p("Astrology’s fade is mere replacement; the alchemy case stresses clarified purpose."))) + final("Option 3"),
 "inference", [("1", "About language, not purpose."), ("2", "Replacement without the clarifying."), ("4", "A tool, not a knowledge project.")])

P.va(21, P.summary_html(21, "In 1949, perhaps"), P.Q["VARC"][21]["opts"], "MCQ", "3", "Summary", "Hard",
 "Shannon’s work unsettles the idea that purpose makes writing coherent.",
 steps(("The core", p("We assume purpose makes writing coherent; Shannon’s statistics suggest we may be following probable word sequences unconsciously.")),
       ("Choosing", p("Option 3 names the challenge and its source."))) + final("Option 3"),
 "summary", [("1", "Reverses where the question comes from."), ("2", "Pierce raises the doubt; he doesn’t settle it."), ("4", "‘instinctive understanding of nuances’ distorts statistics.")])
P.va(22, P.summary_html(22, "Instinct doesn’t dictate"), P.Q["VARC"][22]["opts"], "MCQ", "1", "Summary", "Medium",
 "Emotions adjust choices; how they work is unknown.",
 steps(("The core", p("Instinct works through emotions, which shift our choices and are needed to decide at all, yet their mechanisms are a mystery.")),
       ("Choosing", p("Option 1 keeps both halves without narrowing to risk."))) + final("Option 1"),
 "summary", [("2", "Risk is one example."), ("3", "Misses how emotions act."), ("4", "Narrows to risk perception.")])
P.va(23, P.ms(23), P.Q["VARC"][23]["opts"], "MCQ", "3", "Missing_Sentence", "Easy",
 "‘Their behaviors’ follows the courtship display.",
 steps(("Find the spot", p("Blank 3 follows the dances and displays and comes before ‘Their ability to thrive in challenging, competitive environments’.")),
       ("Match the label", p("Blank 3 is choice 3."))) + final("Option 3"),
 "missing", [("1", "Before any behaviour."), ("2", "Still on feathers."), ("4", "In the wrap-up.")])
P.va(24, listed(24, P.PJ_DIR), [], "TITA", "2413", "Para_Jumble", "Easy",
 "Promise, concern, deeper cost, weighing up.",
 steps(("Opening", p("2 introduces brain-to-brain interfaces.")),
       ("Links", p("4 says removing language exposes our raw selves; 1 names the privacy concern of ‘unmediated access’; 3 closes with the weighing of costs and benefits."))) + final("2413"),
 "pj", [("1", "Needs the technology first."), ("3", "A conclusion."), ("4", "‘the linguistic filter’ needs the interface first.")], why_title="Why the others can’t open")
