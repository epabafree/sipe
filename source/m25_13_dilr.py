# -*- coding: utf-8 -*-
# Simp Mock 13 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_13 import P
import m25_13_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Ranking ten leaders (Q1–5) ----------------
WTS = table(["Student", "Eco", "For", "Soc", "Mor"], [["Alex", "30", "20", "10", "40"], ["Bain", "40", "10", "20", "30"], ["Chris", "10", "30", "40", "20"], ["Dennis", "20", "40", "30", "10"]])
SCORES = table(["Leader", "A", "B", "C", "D"],
               [["Tandon", "82", "81", "83", "84"], ["Ellis", "92", "86", "79", "83"], ["Joshi", "65", "69", "69", "57"], ["Nair", "36", "33", "37", "44"], ["Kapoor", "46", "43", "55", "46"],
                ["Rao", "57", "53", "52", "58"], ["Chopra", "63", "73", "70", "74"], ["Bose", "32", "31", "35", "32"], ["Oberoi", "53", "59", "46", "42"], ["Tiwari", "24", "22", "24", "30"]])
P.dilr_set(1, "Set 1 — Four ways to rank ten leaders", DIR,
 p("Four research students, Alex, Bain, Chris and Dennis, came across a survey that ranked a country’s ten heads of government since 1945 from 1 to 10 on four parameters: Economy, Foreign Affairs, Social Schemes and Moral Authority. Rank 1 on a parameter earned 100 points, rank 2 earned 90, and so on down to 10 points for rank 10. The chart shows the points.") + F.POINTS +
 p("Each student computed a scaled score for each leader: the sum, over the four parameters, of (points on the parameter) × (the weightage the student gave it). Each student gave the weightages 40%, 30%, 20% and 10% to the four parameters, one each, and no two students gave the same weightage to the same parameter. Each student ranked the ten leaders by scaled score, and no student gave two leaders the same score.") +
 "<ul><li>Ellis was ranked first by Alex and Bain only; their scores for Ellis were 92 and 86, in some order.</li><li>The lowest scaled score given by any student to any leader was 22, given by Bain to Tiwari. Bain gave Economy 40%.</li><li>The highest scaled score given to Tiwari was 30, given by Dennis.</li></ul>",
 "DILR::DI::Graphs_and_Charts",
 steps(("Bain", p("Tiwari’s points are 30, 50, 10, 10. Bain: 0.4 × 30 = 12, leaving 10 from the rest. Foreign Affairs at 10% gives 5 and the 10-point parameters give the other 5 (any split of 20% and 30%). Ellis from Bain: 36 + 10 + 0.2 × 50 + 0.3 × 100 = 86, or 81 with Social and Moral swapped. 86 must be Bain’s, so Bain is 40, 10, 20, 30, and Alex gave Ellis 92.")),
       ("Dennis", p("Dennis gave Tiwari 30. If his 40% went to Social or Moral, those two would add at most 7, and Economy and Foreign Affairs (with what’s left) can’t make up the 23 to 25. Economy’s 40% is Bain’s, so Dennis gives Foreign Affairs 40%: 20 points, and the other 10 needs Economy 20% (6) with Social and Moral sharing 30% and 10% (3 + 1). Moral can’t be 30% (Bain’s), so Social 30%, Moral 10%.")),
       ("Alex and Chris", p("The remaining weights must form a Latin square. Alex scores Ellis 92: Economy 30%, Foreign 20%, Social 10%, Moral 40% gives 27 + 20 + 5 + 40 = 92. Chris takes what’s left: 10, 30, 40, 20.") + WTS),
       ("All scores", SCORES)) +
 final("Every weightage, and so every score, is fixed."),
 p("Start from Tiwari’s very uneven points: a low score pins down where the big weights went."),
 p("<b>Weighted scores:</b> extreme rows (very low or very high) leave the fewest ways to reach a given total."))
P.dq(1, "Each of the 10 leaders gets a scaled score from each of the four students, giving 40 leader–score pairs. How many of these 40 can be determined uniquely?", [], "TITA", "40", "Medium",
 "Are all four weight patterns fixed?", steps(("Count", p("Yes, so all 40."))) + final("40"))
P.dq(2, "Which weightages did Alex assign to the four parameters?",
 ["Economy 30%, Foreign Affairs 20%, Social Schemes 10%, Moral Authority 40%", "Economy 40%, Foreign Affairs 10%, Social Schemes 20%, Moral Authority 30%",
  "Economy 10%, Foreign Affairs 30%, Social Schemes 40%, Moral Authority 20%", "Economy 20%, Foreign Affairs 40%, Social Schemes 30%, Moral Authority 10%"], "MCQ", "1", "Medium",
 "Alex gave Ellis 92.", steps(("Alex", p("30, 20, 10, 40."))) + final("Option 1"),
 [("2", "Bain’s."), ("3", "Chris’s."), ("4", "Dennis’s.")])
P.dq(3, "What is the difference between the highest and lowest scaled scores given to Nair by the four students?", [], "TITA", "11", "Easy",
 "Nair’s points: 40, 70, 20, 20.", steps(("Scores", p("Alex 36, Bain 33, Chris 37, Dennis 44: 44 − 33 = 11."))) + final("11"))
P.dq(4, "What scaled score did Dennis give Tandon?", ["78", "80", "83", "84"], "MCQ", "4", "Easy",
 "Tandon’s points: 80, 90, 80, 80.", steps(("Dennis", p("16 + 36 + 24 + 8 = 84."))) + final("Option 4"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Chris’s score.")])
P.dq(5, "What is the average of the scaled scores Chris gave the ten leaders?", ["55", "56", "53.5", "51.5"], "MCQ", "1", "Medium",
 "Weight the column totals of points.",
 steps(("Totals", p("Points add to 550 for every parameter (100 + 90 + … + 10), so any weighting gives a total of 550 and an average of 55."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

# ---------------- Set 2: An athletics meet (Q6–9) ----------------
ROTA = table(["Event", "Entrants"], [["1", "A, B, C"], ["2", "B, C, D"], ["3", "C, D, E"], ["4", "D, E, G"], ["5", "E, G, A"], ["6", "G, A, B"]])
RESULT = table(["No.", "Event", "Medal"], [["1", "LJ or JT", "Chirayu, silver"], ["2", "High Jump", "Biresh, bronze"], ["3", "Pole Vault", "Daanesh, gold"],
                                         ["4", "Triple Jump", "Ekaaksh, bronze"], ["5", "Shot Put", "Abhay, gold"], ["6", "JT or LJ", "Gagan, bronze"]])
P.dilr_set(2, "Set 2 — Six athletes, six events", DIR,
 p("Six students of a school, Abhay, Biresh, Chirayu, Daanesh, Ekaaksh and Gagan, took part in an inter-school athletics meet with six events: High Jump, Javelin Throw, Long Jump, Pole Vault, Shot Put and Triple Jump (not necessarily held in that order). A school could enter at most 3 students per event. The top three in each event won gold, silver and bronze; there were no ties. The school won 2 golds, 1 silver and 3 bronzes in all.") +
 p("The PE teacher numbered the students 1 to 6 in alphabetical order (Abhay 1, Biresh 2, and so on) and sent students 1–3 to the 1st event, 2–4 to the 2nd, 3–5 to the 3rd, 4–6 to the 4th, 5, 6 and 1 to the 5th, and 6, 1 and 2 to the 6th. So each student took part in exactly three events.") +
 "<ul><li>No student won more than one medal.</li><li>The school never won the same type of medal in two consecutive events, and never more than one medal in an event.</li>"
 "<li>Abhay did not take part in the High Jump. Chirayu took part in the High Jump but won no medal in it.</li><li>Daanesh won the school’s first gold, in the Pole Vault, which was the third event. The second gold came in the Shot Put.</li>"
 "<li>Biresh won a bronze. Gagan won a medal in the last event.</li><li>Ekaaksh won a medal in the Triple Jump.</li></ul>",
 "DILR::LR::Puzzles",
 steps(("One each", p("Six medals, at most one per event and per student: every event and every student has exactly one.") + ROTA),
       ("Medal pattern", p("Gold in event 3 is the first gold, so the second is in event 5 or 6 (not 4, next to 3). If it were 6, events 4–5 and events 1–2 would each need a silver and a bronze: two silvers. So gold in event 5, the Shot Put. Events 4 and 6 sit next to golds and take bronzes; events 1 and 2 share the silver and the last bronze.")),
       ("Who", p("Gagan has event 6 (bronze). Event 4 (D, E, G) then goes to Ekaaksh, so event 4 is the Triple Jump; event 5 goes to Abhay (gold). Biresh’s bronze is in event 1 or 2, and Chirayu has the other.")),
       ("High Jump", p("Without Abhay but with Chirayu: event 2 (B, C, D). Chirayu didn’t medal there, so Biresh won bronze in event 2 and Chirayu silver in event 1.")),
       ("Result", RESULT)) +
 final("Only the order of Long Jump and Javelin Throw (events 1 and 6) is open."),
 p("Count medals first: six medals, six events, six students forces one of each."),
 p("<b>No-repeat sequences:</b> place the fixed medals, then see which slots the rest can take."))
P.dq(6, "Who won the silver medal?", ["Abhay", "Chirayu", "Ekaaksh", "Gagan"], "MCQ", "2", "Medium",
 "The silver is in event 1 or 2.", steps(("Silver", p("Chirayu, event 1."))) + final("Option 2"),
 [("1", "Gold."), ("3", "Bronze."), ("4", "Bronze.")])
P.dq(7, "Who won a medal in the Javelin Throw?", ["Chirayu", "Ekaaksh", "Gagan", "Either Chirayu or Gagan"], "MCQ", "4", "Medium",
 "Javelin is event 1 or 6.", steps(("Javelin", p("Chirayu (event 1) or Gagan (event 6)."))) + final("Option 4"),
 [("1", "Only if it is event 1."), ("2", "Triple Jump."), ("3", "Only if it is event 6.")])
P.dq(8, "In the list of the six events, what was the position of the Triple Jump?", ["first", "second", "fourth", "sixth"], "MCQ", "3", "Easy",
 "Ekaaksh’s medal.", steps(("Position", p("Event 4."))) + final("Option 3"),
 [("1", "LJ or JT."), ("2", "High Jump."), ("4", "LJ or JT.")])
P.dq(9, "Which pair of events cannot be consecutive?", ["Long Jump and High Jump", "High Jump and Triple Jump", "Shot Put and Javelin Throw", "Long Jump and Shot Put"], "MCQ", "2", "Easy",
 "High Jump is 2nd, Triple Jump 4th.", steps(("Check", p("2 and 4 are never next to each other."))) + final("Option 2"),
 [("1", "If LJ is 1st."), ("3", "If JT is 6th."), ("4", "If LJ is 6th.")])

# ---------------- Set 3: Staff at three branches (Q10–14) ----------------
STAFF = table(["Group", "AW", "BW", "NP"],
              [["Male ₹20k", "0", "30", "40"], ["Male ₹30k", "45", "35", "0"], ["Female ₹20k", "10", "0", "20"], ["Female ₹30k", "25", "15", "30"], ["Total", "80", "80", "90"]])
P.dilr_set(3, "Set 3 — Staff at three branches", DIR,
 p("A company has 250 employees in three branches: Andheri West, Bandra West and Nariman Point. Each employee is male or female and earns either ₹20,000 or ₹30,000 a month.") +
 "<ul><li>The number of women at Andheri equals the number of men at Bandra earning ₹30,000.</li>"
 "<li>The number of men at Nariman earning ₹20,000 equals the number of women at Andheri earning ₹30,000 plus the number of women at Bandra earning ₹30,000.</li>"
 "<li>The number of men at Bandra earning ₹20,000 equals the number of women at Nariman earning ₹30,000.</li>"
 "<li>No man at Andheri earns ₹20,000, no woman at Bandra earns ₹20,000, and no man at Nariman earns ₹30,000.</li>"
 "<li>Men at Nariman earning ₹20,000 are twice as many as women at Nariman earning ₹20,000.</li>"
 "<li>Men at Andheri earning ₹30,000 outnumber men at Nariman earning ₹20,000 by 5.</li>"
 "<li>Andheri and Bandra have 80 employees each.</li><li>The monthly salaries at Nariman total ₹21,00,000.</li><li>There are 50 more men than women in the company.</li></ul>",
 "DILR::DI::Caselets",
 steps(("Nariman", p("90 staff: 20a + 30b = 2100 (in thousands) with a + b = 90 gives 60 on ₹20k and 30 on ₹30k. The ₹20k group is men : women = 2 : 1, so 40 men and 20 women; the 30 on ₹30k are women (no men).")),
       ("Andheri men, Bandra ₹20k men", p("Andheri men on ₹30k = 40 + 5 = 45. Bandra men on ₹20k = Nariman women on ₹30k = 30.")),
       ("The rest", p("Men = 150. So Bandra men on ₹30k = 150 − 45 − 30 − 40 = 35, which equals Andheri’s women: 80 − 45 = 35 ✓. Bandra women (all ₹30k) = 80 − 65 = 15. Andheri women on ₹30k = 40 − 15 = 25, on ₹20k = 10.")),
       ("Table (AW Andheri West, BW Bandra West, NP Nariman Point)", STAFF)) +
 final("Every cell is fixed."),
 p("Nariman’s headcount and salary bill give its two pay groups at once."),
 p("<b>Two equations, two unknowns:</b> a headcount and a wage bill split any group by pay level."))
P.dq(10, "How many men work at Nariman Point?", [], "TITA", "40", "Easy",
 "No man there earns ₹30k.", steps(("Men", p("40."))) + final("40"))
P.dq(11, "What is the total monthly salary (in ₹) of all employees at Andheri West?", [], "TITA", "2300000", "Easy",
 "70 on ₹30k, 10 on ₹20k.", steps(("Total", p("70 × 30,000 + 10 × 20,000 = 23,00,000."))) + final("2300000"))
P.dq(12, "How many women earn ₹30,000 at Bandra West?", ["15", "18", "20", "None of these"], "MCQ", "1", "Easy",
 "Bandra has no women on ₹20k.", steps(("Count", p("80 − 30 − 35 = 15."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "15 is listed.")])
P.dq(13, "Which statement is definitely correct?",
 ["Andheri West has no more women than Bandra West.", "Bandra West has the most employees earning ₹30,000 among the three branches.",
  "Nariman Point has the most women earning ₹20,000 among the three branches.", "None of the above"], "MCQ", "3", "Easy",
 "Read the table.", steps(("Check", p("Women on ₹20k: 10, 0, 20. Nariman leads."))) + final("Option 3"),
 [("1", "35 against 15."), ("2", "Andheri has 70, Bandra 50."), ("4", "Option 3 holds.")])
P.dq(14, "What is the ratio of women earning ₹30,000 at Andheri West to those at Bandra West?", ["3 : 5", "3 : 4", "5 : 3", "4 : 3"], "MCQ", "3", "Easy",
 "25 and 15.", steps(("Ratio", p("25 : 15 = 5 : 3."))) + final("Option 3"),
 [("1", "Reversed."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

# ---------------- Set 4: Dividing an estate (Q15–18) ----------------
GRID = table(["", "C1", "C2", "C3", "C4", "C5", "C6"],
             [["R1", "A", "C", "E", "D", "F", "B"], ["R2", "F", "D", "B", "E", "A", "C"], ["R3", "D", "A", "F", "C", "B", "E"],
              ["R4", "E", "B", "C", "A", "D", "F"], ["R5", "C", "F", "A", "B", "E", "D"], ["R6", "B", "E", "D", "F", "C", "A"]])
P.dilr_set(4, "Set 4 — Dividing an estate", DIR,
 p("A landowner’s estate of 3,60,000 sq ft was split into six equal sections of 60,000 sq ft, each for one purpose: House Land (HL), Farm Land (FL), Barn Land (BL), Garden Land (GL), Utility Land (UL) and Pond Land (PL). Each section is divided into six plots, laid out as a 6 × 6 grid of rows R1–R6 and columns C1–C6, as shown.") +
 p("His will divides the plots among his six sons, Anand (A), Biswas (B), Chetan (C), Dilip (D), Eshwar (E) and Fulchand (F), so that each son gets exactly one plot of each land type, and no son gets two plots in the same row or the same column. Some plots are already named in the will:") + F.ESTATE,
 "DILR::LR::Puzzles",
 steps(("A 6 × 6 sudoku", p("Each row, column and 2 × 3 block holds each son once.")),
       ("Start", p("Row 1 needs A, C, D, and House Land already has D, E, F, so R1C1 and R1C2 are A and C; that puts D in R1C4 and B in R2C3. Carry on cell by cell with the row, column and block checks; every cell is forced.")),
       ("Solution", GRID)) +
 final("All 36 plots are fixed."),
 p("Fill the cells with the fewest options first, checking row, column and block each time."),
 p("<b>Sudoku logic:</b> each row, column and box is a permutation; a value missing from a unit must go in the one cell that allows it."))
P.dq(15, "Who got plot HL – R1C1?", ["Anand", "Biswas", "Chetan", "Dilip"], "MCQ", "1", "Medium",
 "R1C1 in the grid.", steps(("Plot", p("A, Anand."))) + final("Option 1"),
 [("2", "R1C6."), ("3", "R1C2."), ("4", "R1C4.")])
P.dq(16, "For how many of the 36 plots can the owner be determined uniquely?", [], "TITA", "36", "Medium",
 "The grid has one solution.", steps(("Count", p("All 36."))) + final("36"))
P.dq(17, "Who got plot UL – R6C5?", ["Fulchand", "Dilip", "Chetan", "Cannot be determined"], "MCQ", "3", "Easy",
 "Row 6 is B, E, D, F, C, A.", steps(("Plot", p("Chetan."))) + final("Option 3"),
 [("1", "R6C4."), ("2", "R6C3."), ("4", "Unique.")])
P.dq(18, "Who got plot GL – R5C2?", ["Dilip", "Fulchand", "Eshwar", "Cannot be determined"], "MCQ", "2", "Easy",
 "Row 5 is C, F, A, B, E, D.", steps(("Plot", p("Fulchand."))) + final("Option 2"),
 [("1", "R5C6."), ("3", "R5C5."), ("4", "Unique.")])

# ---------------- Set 5: Predicting the winners (Q19–22) ----------------
_P = {"Am": "RKTANI", "Bh": "IRTKAN", "Ch": "RKTNIA", "De": "ATRNKI", "El": "IRTANK", "Ga": "KAIRTN"}
PRED = table(["Year"] + list(_P), [[str(2020 + y)] + [v[y] for v in _P.values()] for y in range(6)])
CASES = ("<ul><li><b>Case 1</b>: R, K, T, N, A, I. Correct: Am 4, Bh 2, Ch 4, De 2, El 1, Ga 0</li>"
         "<li><b>Case 2</b>: A, R, T, K, N, I. Correct: Am 3, Bh 3, Ch 1, De 2, El 3, Ga 0</li>"
         "<li><b>Case 3</b>: I, R, T, K, N, A. Correct: Am 2, Bh 4, Ch 2, De 0, El 4, Ga 0</li>"
         "<li><b>Case 4</b>: I, R, T, N, A, K. Correct: Am 1, Bh 4, Ch 2, De 1, El 4, Ga 0</li></ul>")
P.dilr_set(5, "Set 5 — Predicting six winners", DIR,
 p("On a televised cooking competition, six food critics, Amrita, Bhaskar, Charu, Dev, Elina and Gaurav, each predicted the ‘Top Chef of the Year’ for every year from 2020 to 2025. Six chefs, Riya (R), Kabir (K), Tanvi (T), Aarav (A), Neel (N) and Isha (I), each won in exactly one year. The predictions, with each critic shown by the first two letters of their name:") + PRED +
 "<ul><li>Kabir did not win in 2020.</li><li>Neither Aarav nor Tanvi won in 2021.</li><li>Neither Isha nor Riya won in 2022.</li><li>Neither Aarav nor Riya won in 2023.</li><li>Neither Isha, Kabir nor Tanvi won in 2024.</li><li>Neel did not win in 2025.</li>"
 "<li>For each year, at least one critic named the winner correctly.</li></ul>",
 "DILR::LR::Analytical_Reasoning",
 steps(("Candidates", p("Each year’s winner must be someone predicted for that year and not ruled out. 2020: R, I, A. 2021: K, R. 2022: T only. 2023: K, N. 2024: N, A. 2025: I, A, K.")),
       ("Fix 2022", p("Tanvi won 2022. Then try the 2021 choice and run through the rest.")),
       ("Cases", CASES)) +
 final("Four possible results; Tanvi in 2022 in all of them."),
 p("List the allowed names year by year; a year with one name fixes itself."),
 p("<b>Candidate lists:</b> intersect ‘someone predicted it’ with ‘not ruled out’ before trying cases."))
P.dq(19, "Who won in 2022?", ["Tanvi", "Riya", "Isha", "Cannot be determined"], "MCQ", "1", "Easy",
 "Only one allowed name for 2022.", steps(("2022", p("Tanvi."))) + final("Option 1"),
 [("2", "Ruled out."), ("3", "Ruled out."), ("4", "Fixed.")])
P.dq(20, "Which critic failed to predict the winner correctly in every year?", ["Bhaskar", "Gaurav", "Elina", "More than one of the above"], "MCQ", "2", "Medium",
 "Check the last column of the cases.", steps(("Zero", p("Gaurav scores 0 in all four cases."))) + final("Option 2"),
 [("1", "At least 2."), ("3", "At least 1."), ("4", "Only Gaurav.")])
P.dq(21, "How many critics correctly predicted the 2023 winner?", ["1", "2", "3", "Cannot be determined"], "MCQ", "4", "Medium",
 "Kabir or Neel won 2023.", steps(("Count", p("Kabir: only Bhaskar (1). Neel: Charu and Dev (2). Both happen."))) + final("Option 4"),
 [("1", "Only if Kabir won."), ("2", "Only if Neel won."), ("3", "Never.")])
P.dq(22, "What is the maximum possible number of correct predictions by a single critic?", ["2", "4", "3", "5"], "MCQ", "2", "Medium",
 "Highest count in any case.", steps(("Max", p("4 (for example Amrita and Charu in case 1)."))) + final("Option 2"),
 [("1", "Too low."), ("3", "Too low."), ("4", "Never reached.")])
