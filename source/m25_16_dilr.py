# -*- coding: utf-8 -*-
# Simp Mock 16 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_16 import P
import m25_16_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Night shift (Q1–5) ----------------
SHIFT = table(["Hour", "A", "B", "C", "Units"],
              [["9–10", "S", "S", "S", "300"], ["10–11", "B", "S", "S", "350"], ["11–12", "S", "S", "B", "350"], ["12–1", "S", "S", "M", "200"],
               ["1–2", "B", "B", "S", "400"], ["2–3", "S", "S", "B", "350"], ["3–4", "S", "S", "S", "300"], ["4–5", "S", "S", "S", "300"], ["5–6", "S", "B", "B", "400"]])
P.dilr_set(1, "Set 1 — Three assembly lines on a night shift", DIR,
 p("A plant runs three assembly lines, A, B and C, on a night shift from 9 PM to 6 AM. Each line runs in STANDARD mode (100 units an hour) or BOOST mode (50% more, 150 units an hour), or is shut for maintenance, which lasts exactly one hour. Modes change only on the hour.") +
 "<ul><li>All three lines started in STANDARD mode at 9 PM.</li><li>Lines A and B each ran in BOOST mode for 2 hours in all; line C for 3 hours, and C was under maintenance from midnight to 1 AM.</li>"
 "<li>Before midnight no two lines were in BOOST mode at the same time. After midnight, in more than one hour exactly two lines were in BOOST mode together.</li>"
 "<li>The plant produced 2,950 units in the shift.</li><li>Line A was in STANDARD mode in the last hour.</li>"
 "<li>Successive switches of line C into BOOST mode started exactly 3 hours apart.</li><li>Output from midnight to 1 AM differed from output from 1 AM to 2 AM.</li></ul>" +
 table(["Interval", "Plant output"], [["9 PM – midnight", "1000"], ["midnight – 3 AM", "950"], ["10 PM – 2 AM", "1300"], ["2 AM – 5 AM", "950"], ["11 PM – 2 AM", "950"]]),
 "DILR::LR::Scheduling",
 steps(("Hour counts", p("BOOST hours: 2 + 2 + 3 = 7, giving 1,050 units. The other 1,900 units are 19 STANDARD hours; with 1 maintenance hour that fills all 27 line-hours.")),
       ("Hourly totals", p("The first hour is 300. From the table: 10–12 make 700, 12–2 make 600, 2–3 makes 350, 3–5 make 600 (all STANDARD), and 5–6 makes 400.")),
       ("Before midnight", p("10–11 and 11–12 each have exactly one BOOST (350 each).")),
       ("Midnight to 2", p("600 with C down at 12–1: if both BOOST lines were in 12–1 it would equal 1–2’s 300, so A and B boost at 1–2.")),
       ("C’s pattern", p("C boosts at 11, 2 and 5 (3 hours apart); A boosts at 10 (its two hours), and B at 5–6.") + SHIFT)) +
 final("Every line’s mode in every hour is fixed."),
 p("Turn the interval totals into hourly totals; each hourly total tells you how many lines were boosting."),
 p("<b>Hourly totals:</b> 300 + 50 × (number of BOOST lines), less 100 for a line under maintenance."))
P.dq(1, "For how many of the three lines can the mode (STANDARD, BOOST or maintenance) be determined for all 9 hours of the shift?", [], "TITA", "3", "Hard",
 "Is the whole grid forced?", steps(("Count", p("Yes: all three lines."))) + final("3"))
P.dq(2, "What is the difference between the highest and the lowest hourly output of the plant during the shift (in units)?", [], "TITA", "200", "Medium",
 "Highest 400, lowest 200.", steps(("Difference", p("400 (1–2 and 5–6) − 200 (12–1) = 200."))) + final("200"))
P.dq(3, "In which two hours was line A in BOOST mode?", ["10 PM to 11 PM and 2 AM to 3 AM", "10 PM to 11 PM and 1 AM to 2 AM", "11 PM to midnight and 2 AM to 3 AM", "11 PM to midnight and 1 AM to 2 AM"], "MCQ", "2", "Medium",
 "Read row A.", steps(("A", p("10–11 and 1–2."))) + final("Option 2"),
 [("1", "C boosts at 2–3."), ("3", "C’s hours."), ("4", "C boosts at 11–12.")])
P.dq(4, "Let a, b and c be the medians of the hourly outputs of lines A, B and C over the shift. Which is correct?", ["a = b = c", "a > b > c", "a < b < c", "a > b = c"], "MCQ", "1", "Easy",
 "Each line has at least five STANDARD hours.", steps(("Medians", p("Of 9 hourly values, the middle one is 100 for every line: a = b = c."))) + final("Option 1"),
 [("2", "All equal."), ("3", "All equal."), ("4", "All equal.")])
P.dq(5, "For how many hours were all three lines in STANDARD mode?", [], "TITA", "3", "Easy",
 "Hours with output 300.", steps(("Hours", p("9–10, 3–4 and 4–5."))) + final("3"))

# ---------------- Set 2: R&D outputs (Q6–9) ----------------
SPLIT = table(["Div.", "Papers", "Patents", "Rev."],
              [["Bio", "75", "45", "120"], ["Chem", "30", "60", "150"], ["Data", "45", "30", "60"], ["Clin", "60", "30", "90"],
               ["Form", "60", "90", "120"], ["Reg", "30", "45", "60"]])
P.dilr_set(2, "Set 2 — Papers, patents and revenue", DIR,
 p("A pharmaceutical company assessed the research outputs of six divisions: BioTech, ChemSynth, DataAnalysis, ClinicalTrials, Formulations and Regulations. Each output is either a published paper or a patent filed. There were 600 outputs in all, 90 of them from ClinicalTrials.") +
 p("The company sells a paper for ₹1,00,000 and a patent for ₹2,00,000; not every output was sold. Revenue from these sales was ₹6 crore.") +
 p("The first chart shows each division’s share of all papers and of all patents; the second shows each division’s share of the revenue.") + F.OUTPUTS + F.REVENUE,
 "DILR::DI::Graphs_and_Charts",
 steps(("Totals", p("Papers x, patents y: x + y = 600 and 0.2x + 0.1y = 90 give x = y = 300.")),
       ("By division (revenue in ₹ lakh)", SPLIT),
       ("Selling", p("A division’s revenue is papers sold × 1 + patents sold × 2 (in lakh). Its ceiling is papers + 2 × patents; ChemSynth’s ceiling, 150, equals its revenue."))) +
 final("Compare each division’s revenue with what selling everything would bring."),
 p("Solve for the totals first; then each division is a small sell-how-many puzzle."),
 p("<b>Bounds:</b> revenue between ‘only patents’ and ‘everything’ tells you what must have been sold."))
P.dq(6, "How many of the 600 outputs were published papers?", [], "TITA", "300", "Easy",
 "Use ClinicalTrials’ 90.", steps(("Solve", p("0.2x + 0.1(600 − x) = 90 gives x = 300."))) + final("300"))
P.dq(7, "For how many divisions were all the papers and patents sold?", ["1", "2", "3", "4"], "MCQ", "1", "Medium",
 "Compare revenue with the full-sale value.",
 steps(("Full sale", p("BioTech 165, ChemSynth 150, DataAnalysis 105, ClinicalTrials 120, Formulations 240, Regulations 120 (lakh). Only ChemSynth’s revenue reaches it."))) + final("Option 1"),
 [("2", "Only one division."), ("3", "Only one."), ("4", "Only one.")])
P.dq(8, "What is the least possible number of papers sold?", ["90", "120", "150", "180"], "MCQ", "1", "Medium",
 "In each division sell as many patents as the revenue allows.",
 steps(("Papers needed", p("BioTech 120 − 90 = 30; ChemSynth 30; ClinicalTrials 90 − 60 = 30; DataAnalysis, Formulations and Regulations can earn everything from patents.")),
       ("Total", p("30 + 30 + 30 = 90."))) + final("Option 1"),
 [("2", "Not the minimum."), ("3", "Not the minimum."), ("4", "Not the minimum.")])
P.dq(9, "Which of these divisions could have earned all its revenue from patents?", ["BioTech", "ChemSynth", "ClinicalTrials", "DataAnalysis"], "MCQ", "4", "Easy",
 "Patents × 2 lakh must reach the revenue.", steps(("Check", p("DataAnalysis: 30 patents bring 60, its whole revenue. BioTech (90 < 120), ChemSynth (120 < 150), ClinicalTrials (60 < 90) fall short."))) + final("Option 4"),
 [("1", "90 < 120."), ("2", "120 < 150."), ("3", "60 < 90.")])

# ---------------- Set 3: Film festival (Q10–14) ----------------
FILMS = table(["Film", "Genre", "Day 1", "Day 2"],
              [["A", "Rom/Thr", "Ba/Ta", "Te"], ["B, D, E", "Com", "En/Ta/Te", "Hi"], ["C", "Act", "En", "Ba"], ["F", "Act", "En", "Te"],
               ["G", "Rom", "Ba", "Hi"], ["H", "Thr", "En", "Ta"], ["I", "Rom/Thr", "Ba/Ta", "Te"], ["J", "Rom", "Ba", "Ta"]]) + p("Hi Hindi, En English, Ba Bangla, Ta Tamil, Te Telugu.")
P.dilr_set(3, "Set 3 — A film festival in five languages", DIR,
 p("A multilingual film festival chose ten films, A to J, to screen on 14 and 15 December (day 1 and day 2). Three were Romance, three Comedy, two Action and two Thriller. Each film was screened once on each day, in a different language each day, from Hindi, English, Bangla, Tamil and Telugu. No two films had the same pair of languages.") +
 "<ul><li>On day 1 all three Romance films were in Bangla, and no film was in Hindi.</li><li>On day 2 no film was in English.</li>"
 "<li>B, D and E were Comedy films, each screened in Hindi on day 2.</li><li>C and F were the Action films, screened in English on day 1.</li><li>A, F and I were screened in Telugu on day 2.</li>"
 "<li>J was not screened in Hindi, and H was not screened in Bangla.</li></ul>",
 "DILR::LR::Puzzles",
 steps(("Pairs", p("There are exactly C(5, 2) = 10 language pairs and 10 films, so every pair is used once and each language appears in 4 pairs.")),
       ("Genres", p("H avoids Bangla, so it isn’t Romance: Thriller. A and I share day-2 Telugu; both Romance would repeat Bangla–Telugu, so one is Romance and one Thriller, and G, J are Romance.")),
       ("Pairs placed", p("English–Bangla must be C (H avoids Bangla). G takes Bangla–Hindi (J avoids Hindi), J takes Bangla–Tamil, H takes English–Tamil. B, D, E use English, Tamil, Telugu with Hindi in some order.") + FILMS)) +
 final("B, D, E and A, I can swap; everything else is fixed."),
 p("Ten films and ten possible language pairs: every pair is used exactly once."),
 p("<b>Counting pairs:</b> when items equal the number of possible pairs, each pair appears once."))
P.dq(10, "In which language was film H screened on 14 December?", ["Telugu", "English", "Tamil", "Hindi"], "MCQ", "2", "Medium",
 "H takes English–Tamil.", steps(("Day 1", p("English (Tamil on day 2)."))) + final("Option 2"),
 [("1", "Not H’s pair."), ("3", "Day 2."), ("4", "No Hindi on day 1.")])
P.dq(11, "In which language was film B screened on 14 December?", ["Telugu", "English", "Tamil", "Cannot be determined"], "MCQ", "4", "Easy",
 "B, D and E share three pairs.", steps(("Open", p("Any of English, Tamil, Telugu."))) + final("Option 4"),
 [("1", "Possible, not certain."), ("2", "Possible, not certain."), ("3", "Possible, not certain.")])
P.dq(12, "Which film – genre – day 1 language – day 2 language combination is definitely correct?", ["D – Comedy – English – Hindi", "E – Comedy – Bangla – Hindi", "J – Romance – Bangla – Tamil", "G – Romance – Bangla – Telugu"], "MCQ", "3", "Easy",
 "Which rows are fully fixed?", steps(("J", p("J is fixed as Romance, Bangla then Tamil."))) + final("Option 3"),
 [("1", "Possible only."), ("2", "E isn’t in Bangla."), ("4", "G is Bangla–Hindi.")])
P.dq(13, "How many films were screened in Tamil on 14 December?", [], "TITA", "2", "Medium",
 "One of A/I and one of B/D/E.", steps(("Count", p("H and J use Tamil on day 2; on day 1 Tamil goes to one of A, I and one of B, D, E: 2."))) + final("2"))
P.dq(14, "Which film was screened in Hindi and Bangla?", ["B", "G", "D", "E"], "MCQ", "2", "Easy",
 "J avoids Hindi.", steps(("G", p("Bangla on day 1, Hindi on day 2."))) + final("Option 2"),
 [("1", "B has no Bangla."), ("3", "D has no Bangla."), ("4", "E has no Bangla.")])

# ---------------- Set 4: A shooting tournament (Q15–18) ----------------
ROUNDS = table(["Round", "10", "5", "3"],
               [["1", "P6", "P3", "P1"], ["2", "P4", "P7", "P2"], ["3", "P7", "P5", "P4"], ["4", "P9", "P7", "P4"], ["5", "P9", "P8", "P7"],
                ["6", "P6", "P1", "P10"], ["7", "P8", "P2", "P9"], ["8", "P2", "P8", "P1"], ["9", "P3", "P4", "P2"], ["10", "P10", "P1", "P5"]])
P.dilr_set(4, "Set 4 — Ten rounds of shooting", DIR,
 p("Ten shooters, P1 to P10, took part in a 10-round rifle tournament. Six players shot in each round: P1–P6 in round 1, P2–P7 in round 2, P3–P8 in round 3, and so on, wrapping round (round 6 is P6–P10 and P1). So each player shot in exactly 6 rounds.") +
 p("In every round exactly one player hit the inner circle (10 points), one the middle circle (5 points) and one the outer circle (3 points); the other three scored nothing. The chart gives each player’s running total after rounds 4, 7 and 10.") + F.SHOOT +
 "<ul><li>P6 scored 10 in round 1, and P8 scored 5 in round 5.</li><li>In round 4, P9, P7 and P4 scored 10, 5 and 3.</li><li>P7 did not score 10 in round 2, and P6 did not score 10 in round 5.</li>"
 "<li>P5 scored 5 in round 3. P10 scored only in rounds 6 and 10.</li><li>P4 scored nothing in round 10. P2 scored a 10 before P3 did.</li></ul>",
 "DILR::LR::Games_and_Tournaments",
 steps(("Rounds 1–4", p("P1 shot only in round 1 by then, so its 3 is from round 1; P2’s 3 must be round 2. P7 has 15 more from rounds 2–3 and can’t take 10 in round 2: 5 then 10. That leaves P3 5 in round 1, P4 10 in round 2 and 3 in round 3.")),
       ("Rounds 5–7", p("P2 plays only round 7 of these: 5 there; P1 then takes 5 in round 6. P6 gains 10 in round 6, P8 10 in round 7, P9 10 in round 5, P10 3 in round 6, P9 3 in round 7, P7 3 in round 5.")),
       ("Rounds 8–10", p("Only one 10 per round, so no one gets two 5s here. P10 10 and P5 3 in round 10, P8 5 in round 8, P4 5 in round 9, P1 5 in round 10; P2’s 10 is round 8 and P3’s round 9.") + ROUNDS)) +
 final("The whole score sheet is fixed."),
 p("Work checkpoint by checkpoint; players with few rounds before a checkpoint are forced first."),
 p("<b>Running totals:</b> the gain between checkpoints must be split among the rounds a player actually shot."))
P.dq(15, "How many players hit all three circles?", [], "TITA", "3", "Medium",
 "Look for a 10, a 5 and a 3 for one player.", steps(("Players", p("P2, P4 and P7."))) + final("3"))
P.dq(16, "How many players never hit the inner circle?", [], "TITA", "2", "Easy",
 "Who is missing from the 10 column?", steps(("Players", p("P1 and P5."))) + final("2"))
P.dq(17, "After the first half (three) of their own six rounds, who had the lowest score?", ["P3", "P5", "P8", "P10"], "MCQ", "4", "Medium",
 "P10’s first three rounds are 5, 6 and 7.", steps(("Scores", p("P10: 0 + 3 + 0 = 3. P3, P5 and P8 have 5 each; others more."))) + final("Option 4"),
 [("1", "5."), ("2", "5."), ("3", "5.")])
P.dq(18, "The winner has the highest total after 10 rounds; a tie is broken by more inner-circle hits. Who wins?", ["P7", "P9", "Either P7 or P9", "The tie cannot be resolved"], "MCQ", "2", "Easy",
 "Both have 23.", steps(("Tie-break", p("P9 hit the inner circle twice, P7 once."))) + final("Option 2"),
 [("1", "One inner hit."), ("3", "The tie-break decides it."), ("4", "It can be resolved.")])

# ---------------- Set 5: Truth-tellers and liars (Q19–22) ----------------
P.dilr_set(5, "Set 5 — Five speakers", DIR,
 p("Alfred, Boris, Chris, David and Elizabeth are each either a truth-teller or a liar, and each makes one statement. Alfred’s and David’s statements have two parts; a speaker of a two-part statement is a truth-teller only if both parts are true.") +
 "<ul><li><b>Alfred:</b> “If Boris tells the truth, then Chris lies; and David does not tell the truth.”</li><li><b>Boris:</b> “Exactly one of Alfred and David tells the truth.”</li>"
 "<li><b>Chris:</b> “Elizabeth and I are both truth-tellers or both liars.”</li><li><b>David:</b> “Boris lies; and Elizabeth tells the truth.”</li><li><b>Elizabeth:</b> “At least two of us tell the truth.”</li></ul>",
 "DILR::LR::Analytical_Reasoning",
 steps(("Elizabeth", p("If Chris tells the truth, Elizabeth matches him: truthful. If Chris lies, they differ, so Elizabeth is truthful again.")),
       ("Boris and David", p("David’s second part holds, so David is truthful exactly when Boris lies. Then exactly one of Boris, David is truthful, and Boris’s claim forces Alfred to be a truth-teller either way.")),
       ("Alfred", p("Alfred truthful means David lies, so Boris is truthful, and then Chris lies.")),
       ("Result", p("Truth-tellers: Alfred, Boris, Elizabeth. Liars: Chris, David."))) +
 final("A unique assignment."),
 p("Chris’s statement pins down Elizabeth no matter what Chris is."),
 p("<b>Self-reference:</b> ‘X and I are alike’ is true exactly when X is a truth-teller."))
P.dq(19, "Who are the truth-tellers?", ["Alfred and Boris only", "Alfred, Boris and Elizabeth", "Boris and Elizabeth only", "Alfred and Elizabeth only"], "MCQ", "2", "Medium",
 "Elizabeth is always truthful.", steps(("Answer", p("Alfred, Boris and Elizabeth."))) + final("Option 2"),
 [("1", "Misses Elizabeth."), ("3", "Misses Alfred."), ("4", "Misses Boris.")])
P.dq(20, "Who are the liars?", ["Alfred and David", "Boris and Chris", "Boris and David", "Chris and David"], "MCQ", "4", "Medium",
 "The other two.", steps(("Answer", p("Chris and David."))) + final("Option 4"),
 [("1", "Alfred is truthful."), ("2", "Boris is truthful."), ("3", "Boris is truthful.")])
P.dq(21, "Given the actual truth-tellers and liars, which statement holds?", ["If David lies, then Boris tells the truth.", "If Chris lies, then Elizabeth lies.", "If Elizabeth tells the truth, then exactly two people tell the truth.", "If Alfred tells the truth, then David tells the truth."], "MCQ", "1", "Medium",
 "Check each against the actual result.", steps(("Check", p("David lies and Boris is truthful: (1) holds. (2) Chris lies but Elizabeth is truthful. (3) Three tell the truth. (4) David lies."))) + final("Option 1"),
 [("2", "Elizabeth is truthful."), ("3", "Three are truthful."), ("4", "David lies.")])
P.dq(22, "Which of the following is correct?", ["Both Alfred and David tell the truth or both are liars.", "If Boris tells the truth, then David is a liar.", "If Elizabeth tells the truth, then Boris is a liar.", "Both Chris and Elizabeth tell the truth or both are liars."], "MCQ", "2", "Medium",
 "Boris truthful, David lying.", steps(("Check", p("Option 2 holds; Alfred and David differ, Boris is truthful, and Chris and Elizabeth differ."))) + final("Option 2"),
 [("1", "They differ."), ("3", "Boris is truthful."), ("4", "They differ.")])
