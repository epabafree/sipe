# -*- coding: utf-8 -*-
# Batch 22 — CAT 2025 Slot 3: DILR sets 1–5 (Q1–22, in exam order).
from fmt import steps, final, trap, why, table, p
from b22_25s3 import P
import b22_25s3_figs as F

DIR = "Read the information given below and answer the questions that follow."

# ---------------- Set 1: Phone calls between two operators ----------------
P.dilr_set(1, "Set 1 — Calls between friends on two networks", DIR,
 p("Anu, Bijay, Chetan, Deepak, Eshan, and Faruq are six friends. Each of them uses a mobile number from exactly one of the two mobile operators - Xitel and Yocel. During the last month, the six friends made several calls to each other. Each call was made by one of these six friends to another. The table below summarizes the number of minutes of calls that each of the six made to (outgoing minutes) and received from (incoming minutes) these friends, grouped by the operators. Some of the entries are missing.") +
 p("Outgoing minutes, made to friends on each operator:") +
 table(["Friend", "Op.", "To X", "To Y"], [["Anu", "X", "100", ""], ["Bijay", "X", "", "200"], ["Chetan", "Y", "50", "175"], ["Deepak", "Y", "100", "150"], ["Eshan", "Y", "", "100"], ["Faruq", "Y", "0", ""]]) +
 p("Incoming minutes, received from friends on each operator:") +
 table(["Friend", "From X", "From Y"], [["Anu", "50", "225"], ["Bijay", "", "125"], ["Chetan", "250", "150"], ["Deepak", "275", "100"], ["Eshan", "100", "375"], ["Faruq", "100", "150"]]) +
 p("X is Operator Xitel and Y is Operator Yocel. Blank cells are the missing entries.") +
 p("It is known that the duration of calls from Faruq to Eshan was 200 minutes. Also, there were no calls from:") +
 "<ol type=\"i\"><li>Bijay to Eshan,</li><li>Chetan to Anu and Chetan to Deepak,</li><li>Deepak to Bijay and Deepak to Faruq,</li><li>Eshan to Chetan and Eshan to Deepak.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("Calls between the two Xitel users", p("Anu’s calls to Xitel can only go to Bijay: Anu → Bijay 100. Anu’s incoming from Xitel can only come from Bijay: Bijay → Anu 50.")),
       ("Calls to Xitel from Yocel users", p("Faruq made none. Chetan made none to Anu, so Chetan → Bijay 50. Deepak made none to Bijay, so Deepak → Anu 100. Anu receives 225 from Yocel, so Eshan → Anu = 225 − 100 = 125. Bijay receives 125, so Eshan → Bijay = 125 − 50 = 75.")),
       ("Calls among Yocel users", p("Eshan’s 100 to Yocel can only go to Faruq. Faruq receives 150 from Yocel: Eshan 100 plus Chetan 50 (Deepak made none to Faruq). Chetan’s 175 to Yocel: 50 to Faruq, so 125 to Eshan. Eshan receives 375 from Yocel: 200 from Faruq, 125 from Chetan, so 50 from Deepak. Deepak’s 150 to Yocel: 50 to Eshan, so 100 to Chetan. Chetan receives 150 from Yocel: 100 from Deepak, so 50 from Faruq. Deepak receives 100: all from Faruq.")),
       ("Faruq and Anu to Yocel", p("Faruq → Yocel: Chetan 50 + Deepak 100 + Eshan 200 = 350. Eshan receives 100 from Xitel, all from Anu (Bijay made none). Chetan, Deepak and Faruq together receive 250 + 275 + 100 = 625 from Xitel, of which Bijay sent his 200; so Anu sent 425 to them, and 525 to Yocel in all."))) +
 final("Bijay → Anu 50, Anu → Yocel 525, Faruq → Yocel 350, Deepak → Chetan 100. Some of Anu’s and Bijay’s individual calls to Chetan, Deepak and Faruq stay open."),
 p("Start with entries that have only one possible caller or receiver. Each one fixed makes another row or column solvable."),
 p("<b>Two-way tables:</b> every call is someone’s outgoing and someone else’s incoming. Use the zero calls to shrink each sum to one unknown."))
P.dq(1, "What was the duration of calls (in minutes) from Bijay to Anu?", [], "TITA", "50", "Easy",
 "Anu’s incoming from Xitel can only be from Bijay.",
 steps(p("Anu received 50 minutes from Xitel users, and Bijay is the only other one.")) + final(r"\(50\)"))
P.dq(2, "What was the total duration of calls (in minutes) made by Anu to friends having mobile numbers from Operator Yocel?", [], "TITA", "525", "Hard",
 "Add Anu’s calls to Eshan to what Anu sent Chetan, Deepak and Faruq together.",
 steps(p("Anu → Eshan 100. Chetan, Deepak and Faruq received 625 from Xitel; Bijay’s 200 to Yocel all went to them, so Anu sent 425. Total 525.")) + final(r"\(525\)"))
P.dq(3, "What was the total duration of calls (in minutes) made by Faruq to friends having mobile numbers from Operator Yocel?", [], "TITA", "350", "Medium",
 "Find Faruq’s calls to Chetan and Deepak.",
 steps(p("Faruq → Eshan 200, → Chetan 50, → Deepak 100: 350.")) + final(r"\(350\)"))
P.dq(4, "What was the duration of calls (in minutes) from Deepak to Chetan?", ["100", "0", "125", "50"], "MCQ", "1", "Medium",
 "Deepak’s Yocel calls go only to Chetan and Eshan.",
 steps(p("Deepak → Eshan is 50, so Deepak → Chetan is 150 − 50 = 100.")) + final("100, option 1"),
 [("2", "Deepak called Chetan for 100 minutes."), ("3", "125 is Chetan → Eshan."), ("4", "50 is Deepak → Eshan.")])

# ---------------- Set 2: Travellers and currencies ----------------
P.dilr_set(2, "Set 2 — Three travellers and four currencies", DIR,
 p("Aurevia, Brelosia, Cyrenia and Zerathania are four countries with their currencies being Aurels, Brins, Crowns, and Zentars, respectively. The currencies have different exchange values. Crown’s currency exchange rate with Zentars = 0.5, i.e., 1 Crown is worth 0.5 Zentars.") +
 p("Three travelers, Jano, Kira, and Lian set out from Zerathania visiting exactly two of the countries. Each country is visited by exactly two travelers. Each traveler has a unique Flight Cost, which represents the total cost of airfare in traveling to both the countries and back to Zerathania. The Flight Cost of Jano was 4000 Zentars, while that of the other two travelers were 5000 and 6000 Zentars, not necessarily in that order.") +
 p("When visiting a country, a traveler spent either 1000, 2000 or 3000 in the country’s local currency. Each traveler had different spends (in the country’s local currency) in the two countries he/she visited. Across all the visits, there were exactly two spends of 1000 and exactly one spend of 3000 (in the country’s local currency).") +
 p("The total “Travel Cost” for a traveler is the sum of his/her Flight Cost and the money spent in the countries visited.") +
 p("The citizens of the four countries with knowledge of these travels made a few observations, with spends measured in their respective local currencies:") +
 "<ol type=\"i\"><li>Aurevia citizen: Jano and Kira visited our country, and their Travel Costs were 3500 and 8000, respectively.</li><li>Brelosia citizen: Kira and Lian visited our country, spending 2000 and 3000, respectively. Kira’s Travel Cost was 4000.</li><li>Cyrenia citizen: Lian visited our country and her Travel Cost was 36000.</li></ol>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("Who went where", p("Aurevia: Jano and Kira. Brelosia: Kira and Lian. So Cyrenia: Jano and Lian (each country gets two visitors, each traveller two countries).")),
       ("The spends", p("Lian’s 3000 in Brelosia is the only 3000; the five other spends are two 1000s and three 2000s. Kira spent 2000 in Brelosia, so 1000 in Aurevia; Lian spent 2000 in Cyrenia (she can’t repeat 3000); and Jano’s two spends are 1000 and 2000 in some order.")),
       ("Exchange rates", p(r"Kira’s Travel Cost is 8000 Aurels = 4000 Brins, so 1 Brin = 2 Aurels. Lian’s 36000 Crowns = 18000 Zentars. If Lian’s flight is 5000: \(5000 + 3000B + 1000 = 18000\) (2000 Crowns = 1000 Zentars), so 1 Brin = 4 Zentars and 1 Aurel = 2 Zentars. Kira then costs 4000 Brins = 16000 Zentars = 6000 flight + 8000 + 2000. It all fits. Trying Lian at 6000 leads to Jano’s figures not matching.")),
       ("Jano", p("3500 Aurels = 7000 Zentars, so he spent 3000 Zentars: 1000 Aurels (2000 Z) in Aurevia and 2000 Crowns (1000 Z) in Cyrenia.") +
          table(["", "Flight", "Spend (Z)", "Total (Z)"], [["Jano", "4000", "3000", "7000"], ["Kira", "6000", "10000", "16000"], ["Lian", "5000", "13000", "18000"]]) +
          p("1 Aurel = 2 Zentars, 1 Brin = 4 Zentars, 1 Crown = 0.5 Zentars."))) +
 final("Total Travel Costs: 41000 Zentars."),
 p("Kira’s cost in two currencies gives the Aurel–Brin rate; Lian’s cost in Crowns, with a trial flight cost, gives the Brin–Zentar rate."),
 p("<b>Mixed currencies:</b> convert everything into one currency before adding. The same cost written in two currencies gives an exchange rate."))
P.dq(5, "What is the sum of Travel Costs for all travelers in Zentars?", [], "TITA", "41000", "Hard",
 "Convert each traveller’s cost to Zentars.",
 steps(p("7000 + 16000 + 18000 = 41000.")) + final(r"\(41000\)"))
P.dq(6, "How many Zentars did Lian spend in the two countries he visited?", [], "TITA", "13000", "Medium",
 "3000 Brins and 2000 Crowns.",
 steps(p(r"\(3000 \times 4 + 2000 \times 0.5 = 13000\).")) + final(r"\(13000\)"))
P.dq(7, "What was Jano’s total spend in the two countries he visited, in Aurels?", [], "TITA", "1500", "Medium",
 "Jano spent 3000 Zentars; 1 Aurel = 2 Zentars.",
 steps(p(r"1000 Aurels + 2000 Crowns = 1000 + 500 = 1500 Aurels.")) + final(r"\(1500\)"))
P.dq(8, "One Brin is equivalent to how many Crowns?", ["0.5", "8", "0.125", "4"], "MCQ", "2", "Medium",
 "1 Brin = 4 Zentars and 1 Zentar = 2 Crowns.",
 steps(p(r"\(4 \times 2 = 8\) Crowns.")) + final("8, option 2"),
 [("1", "This inverts the Crown–Zentar rate."), ("3", "This is Crowns to Brins."), ("4", "4 is Brins to Zentars.")])
P.dq(9, "Which of the following statements is NOT true about money spent in the local currency?", ["Jano spent 2000 in Aurevia", "Lian spent 2000 in Cyrenia", "Jano spent 2000 in Cyrenia", "Kira spent 1000 in Aurevia"], "MCQ", "1", "Medium",
 "Jano spent 1000 Aurels.",
 steps(p("Jano’s spends were 1000 in Aurevia and 2000 in Cyrenia, so option 1 is false.")) + final("Option 1"),
 [("2", "True."), ("3", "True."), ("4", "True.")])

# ---------------- Set 3: Puzzle competition ----------------
P.dilr_set(3, "Set 3 — A ten-puzzle race", DIR,
 p("Anirbid, Chandranath, Koushik, and Suranjan participated in a puzzle solving competition. The competition comprised 10 puzzles that had to be solved in the same sequence, i.e., a competitor got access to a puzzle as soon as they solved the previous puzzle. Some of the puzzles were visual puzzles and the others were number-based puzzles. The winner of the competition was the one who solved all puzzles in the least time.") +
 p("The following charts describe their progress in the competition. The first chart shows the number of puzzles solved by each competitor at a given time (in minutes) after the start of the competition. The second chart shows the number of visual puzzles solved by each competitor at a given time (in minutes) after the start of the competition.") + F.ALL + F.VIS,
 "DILR::DI::Graphs_and_Charts",
 steps(("Completion times", table(["#", "Anir.", "Chan.", "Kou.", "Sur."],
          [[str(i + 1)] + [str(F.T[k][i]) for k in F.T] for i in range(10)]) + p("Minutes at which each puzzle was solved.")),
       ("Which puzzles are visual", p("Each visual step coincides with a step on the first chart. For everyone, the visual puzzles are numbers 1, 4, 8 and 9; the other six are number-based."))) +
 final("Visual puzzles: 1, 4, 8, 9. Number-based: 2, 3, 5, 6, 7, 10."),
 p("Line up the two charts: a visual step at the same moment as an overall step tells you which puzzle was visual."),
 p("<b>Step charts:</b> each step up marks the moment a puzzle was finished; the width of a step is the time spent on the next puzzle."))
P.dq(10, "Who had solved the largest number of puzzles by the 20-th minute from the start of the competition?", ["Suranjan", "Chandranath", "Koushik", "Anirbid"], "MCQ", "3", "Easy",
 "Read each line at minute 20.",
 steps(p("Koushik 7, Anirbid 5, Chandranath 5, Suranjan 4.")) + final("Koushik, option 3"),
 [("1", "Suranjan had 4."), ("2", "Chandranath had 5."), ("4", "Anirbid had 5.")])
P.dq(11, "How many minutes did Suranjan take to solve the third visual puzzle in the competition?", [], "TITA", "2", "Medium",
 "The third visual puzzle is puzzle 8.",
 steps(p("Suranjan finished puzzle 7 at 26 and puzzle 8 at 28: 2 minutes.")) + final(r"\(2\)"))
P.dq(12, "At what number in the sequence was the fourth number-based puzzle?", [], "TITA", "6", "Medium",
 "Number-based puzzles are 2, 3, 5, 6, 7, 10.",
 steps(p("The fourth of them is puzzle 6.")) + final(r"\(6\)"))
P.dq(13, "Which of the following is the closest to the average time taken by Anirbid to solve the number-based puzzles in the competition?", ["3.3 minutes", "2.5 minutes", "4.0 minutes", "3.8 minutes"], "MCQ", "3", "Medium",
 "Find Anirbid’s time on puzzles 2, 3, 5, 6, 7 and 10.",
 steps(p("5, 2, 5, 3, 5 and 4 minutes: 24 in all, an average of 4.")) + final("4.0 minutes, option 3"),
 [("1", "This divides by more than six puzzles."), ("2", "Too low."), ("4", "Slightly too high: 24 ÷ 6 is exactly 4.")])

# ---------------- Set 4: Trade between countries ----------------
P.dilr_set(4, "Set 4 — Trade among three countries and the rest", DIR,
 p("Three countries — Pumpland (P), Xiland (X) and Cheeseland (C) — trade among themselves and with the (other countries in) Rest of World (ROW). All trade volumes are given in IC (international currency). The following terminology is used:") +
 "<ul><li>Trade balance = Exports – Imports</li><li>Total trade = Exports + Imports</li><li>Normalized trade balance = Trade balance / Total trade, expressed in percentage terms</li></ul>" +
 p("The following information is known.") +
 "<ol><li>The normalized trade balances of P, X and C are 0%, 10%, and –20%, respectively.</li><li>40% of exports of X are to P. 22% of imports of P are from X.</li><li>90% of exports of C are to P; 4% are to ROW.</li><li>12% of exports of ROW are to X, 40% are to P.</li><li>The export volumes of P, in IC, to X and C are 600 and 1200, respectively. P is the only country that exports to C.</li></ol>",
 "DILR::DI::Caselets",
 steps(("C", p("C imports only from P: 1200. A −20% balance means exports : imports = 2 : 3, so C exports 800: 720 to P, 32 to ROW and the remaining 48 to X.")),
       ("Ratios", p("P: exports = imports = a. X: exports 55b, imports 45b (balance 10%). X sends 40% of its exports to P: 22b, which is 22% of P’s imports, so a = 100b. Let ROW export 100d: 40d to P, 12d to X, 48d to itself.")),
       ("Solving", p(r"P’s imports: \(22b + 720 + 40d = 100b\). X’s imports: \(600 + 48 + 12d = 45b\). These give \(b = 20\), \(d = 21\), so a = 2000.") +
          table(["From \\ to", "P", "X", "C", "ROW"], [["P", "–", "600", "1200", "200"], ["X", "440", "–", "0", "660"], ["C", "720", "48", "–", "32"], ["ROW", "840", "252", "0", "1008"]]) +
          p("Exports: P 2000, X 1100, C 800, ROW 2100. Imports: P 2000, X 900, C 1200, ROW 1900."))) +
 final("The full trade matrix is in the table."),
 p("Begin with C, which imports only from P. Its balance then fixes its exports, and the percentages give the rest."),
 p(r"<b>Normalized balance:</b> \(\frac{E - I}{E + I} = k\) gives \(E : I = (1 + k) : (1 - k)\)."))
P.dq(14, "How much is exported from C to X, in IC?", [], "TITA", "48", "Medium",
 "C exports 800; 90% to P and 4% to ROW.",
 steps(p(r"\(800 - 720 - 32 = 48\).")) + final(r"\(48\)"))
P.dq(15, "How much is exported from P to ROW, in IC?", [], "TITA", "200", "Hard",
 "P exports 2000 in all.",
 steps(p(r"\(2000 - 600 - 1200 = 200\).")) + final(r"\(200\)"))
P.dq(16, "How much is exported from ROW to ROW, in IC?", [], "TITA", "1008", "Hard",
 "ROW’s exports are 100d with d = 21.",
 steps(p(r"48% of 2100 = 1008.")) + final(r"\(1008\)"))
P.dq(17, "What is the trade balance of ROW?", ["200", "0", "-200", "100"], "MCQ", "1", "Medium",
 "ROW exports 2100. What does it import?",
 steps(p(r"Imports: 200 + 660 + 32 + 1008 = 1900. Balance \(2100 - 1900 = 200\).")) + final("200, option 1"),
 [("2", "ROW exports more than it imports."), ("3", "The sign is reversed."), ("4", "The gap is 200.")])
P.dq(18, "Which among the countries P, X, and C has/have the least total trade?", ["Only P", "Both X and C", "Only C", "Only X"], "MCQ", "2", "Medium",
 "Total trade is exports plus imports.",
 steps(p("P 4000, X 2000, C 2000. X and C tie for the least.")) + final("Both X and C, option 2"),
 [("1", "P has the most."), ("3", "X ties with C."), ("4", "C ties with X.")])

# ---------------- Set 5: Passing the Buck ----------------
P.dilr_set(5, "Set 5 — Passing the Buck around a circle", DIR,
 p("Seven children, Aarav, Bina, Chirag, Diya, Eshan, Farhan, and Gaurav, are sitting in a circle facing inside (not necessarily in the same order) and playing a game of ‘Passing the Buck’.") +
 p("The game is played over 10 rounds. In each round, the child holding the Buck must pass it directly to a child sitting in one of the following positions:") +
 "<ul><li>Immediately to the left;</li><li>Immediately to the right;</li><li>Second to the left; or</li><li>Second to the right.</li></ul>" +
 p("The game starts with Bina passing the Buck and ends with Chirag receiving the Buck. The table below provides some information about the pass types and the child receiving the Buck. Some information is missing and labelled as ‘?’.") +
 table(["Round", "Pass type", "Received by"], [["1", "Left 1", "Aarav"], ["2", "Right 2", "?"], ["3", "Right 1", "Diya"], ["4", "?", "?"], ["5", "?", "Aarav"],
                                                ["6", "Left 2", "?"], ["7", "Left 1", "Gaurav"], ["8", "Left 1", "?"], ["9", "?", "Farhan"], ["10", "?", "Chirag"]]) +
 p("Left 1 means immediately to the left, Left 2 second to the left, and likewise for Right."),
 "DILR::LR::Puzzles",
 steps(("Seats around Aarav", p("Write the circle going to the left: Bina, then Aarav (round 1). Round 2 goes two to the right of Aarav, past Bina, to the child just right of Bina. Round 3 goes one more to the right and lands on Diya. So, going right from Bina: Bina, X, Diya.")),
       ("The later rounds", p("Round 5 ends at Aarav and round 6 goes two to his left, then rounds 7 and 8 go one to the left each, with round 7 landing on Gaurav. Round 9 reaches Farhan and round 10 Chirag, each in one pass.")),
       ("Fitting the names", p("The only seating that satisfies every round is, going to the left from Bina: Bina, Aarav, Chirag, Farhan, Gaurav, Diya, Eshan. So Eshan sits immediately to Bina’s right.")),
       ("The rounds", table(["Round", "Type", "To"], [["1", "Left 1", "Aarav"], ["2", "Right 2", "Eshan"], ["3", "Right 1", "Diya"], ["4", "?", "E / B / F"], ["5", "?", "Aarav"],
                                                     ["6", "Left 2", "Farhan"], ["7", "Left 1", "Gaurav"], ["8", "Left 1", "Diya"], ["9", "Right 2", "Farhan"], ["10", "Right 1", "Chirag"]]) +
          p("E / B / F is Eshan, Bina or Farhan. Rounds 4 and 5 can be Diya → Eshan → Aarav (left 1 then left 2), Diya → Bina → Aarav (left 2 then left 1), or Diya → Farhan → Aarav (right 2 twice)."))) +
 final("Circle (going left from Bina): Bina, Aarav, Chirag, Farhan, Gaurav, Diya, Eshan. Only rounds 4 and 5 are open."),
 p("Work the fixed passes around Bina and Aarav first; the seating falls out, and only the two rounds without any information stay open."),
 p("<b>Circular moves:</b> number the seats around the circle; a pass is ±1 or ±2 seats. Fixed start and end points with known moves pin down the seating."))
P.dq(19, "Who is sitting immediately to the right of Bina?", ["Eshan", "Farhan", "Aarav", "Chirag"], "MCQ", "1", "Hard",
 "Round 2 goes two to the right of Aarav, past Bina.",
 steps(p("The seating going left from Bina ends with Eshan, so Eshan is on Bina’s right.")) + final("Eshan, option 1"),
 [("2", "Farhan is three seats to Bina’s left."), ("3", "Aarav is to Bina’s left."), ("4", "Chirag is two to Bina’s left.")])
P.dq(20, "Who is sitting third to the left of Eshan?", ["Gaurav", "Chirag", "Diya", "Aarav"], "MCQ", "2", "Medium",
 "Going left from Eshan: Bina, Aarav, …",
 steps(p("Eshan → Bina → Aarav → Chirag. Chirag is third to the left.")) + final("Chirag, option 2"),
 [("1", "Gaurav is second to Eshan’s right."), ("3", "Diya is immediately to Eshan’s right."), ("4", "Aarav is second to the left.")])
P.dq(21, "For which of the following pass types can the total number of occurrences be uniquely determined?", ["Immediately to the right", "Second to the right", "Second to the left", "Immediately to the left"], "MCQ", "1", "Hard",
 "Rounds 4 and 5 can be left 1 + left 2, left 2 + left 1, or right 2 twice. Which type never appears there?",
 steps(p("“Immediately to the right” is used in rounds 3 and 10 only, in every case: 2 times. The other three types change with the choice for rounds 4 and 5.")) + final("Option 1"),
 [("2", "Right 2 occurs 2 or 4 times."), ("3", "Left 2 occurs 1 or 2 times."), ("4", "Left 1 occurs 3 or 4 times.")])
P.dq(22, "For which of the following children is it possible to determine how many times they received the Buck?", ["Bina", "Eshan", "Farhan", "Gaurav"], "MCQ", "4", "Hard",
 "Who could receive the Buck in round 4?",
 steps(p("Round 4 goes to Eshan, Bina or Farhan, so their counts can change. Gaurav receives it only in round 7: once in every case.")) + final("Gaurav, option 4"),
 [("1", "Bina receives it 0 or 1 times."), ("2", "Eshan receives it 1 or 2 times."), ("3", "Farhan receives it 2 or 3 times.")])
