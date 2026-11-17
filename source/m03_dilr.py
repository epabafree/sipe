# -*- coding: utf-8 -*-
# Simp Mock 3: DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m03 import P
import m03_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Mango orchards (Q1–5) ----------------
V6 = ["Vel", "Vad", "Gon", "Kur", "Kud", "Dab"]
GIVEN = table([""] + V6, [["F1", "3", "", "22", "", "", "8"], ["F2", "23", "", "", "15", "10", "21"],
                          ["F3", "17", "", "", "7", "19", ""], ["F4", "9", "4", "20", "", "11", ""]])
FULL = (table(["", "Vel", "Vad", "Gon"], [["F1", "3", "18", "22"], ["F2", "23", "2", "5"], ["F3", "17", "24", "1"], ["F4", "9", "4", "20"], ["All", "52", "48", "48"]]) +
        table(["", "Kur", "Kud", "Dab"], [["F1", "14", "13", "8"], ["F2", "15", "10", "21"], ["F3", "7", "19", "6"], ["F4", "12", "11", "16"], ["All", "48", "53", "51"]]))
P.dilr_set(1, "Set 1 — Mango orchards in six villages", DIR,
 p("Four farmers, F1, F2, F3 and F4, own mango orchards in six villages: Velas, Vadavali, Gondghar, Kurang, Kudgaon and Dabhol. Each farmer owns at least one orchard in each village, and no farmer owns more than 24 orchards in any village. The 24 numbers (one for each farmer in each village) are all different integers.") +
 p("The following facts are known.") +
 "<ol><li>The total numbers of orchards owned by F4, F3, F2 and F1 form an arithmetic progression in that order, with common difference 2.</li>"
 "<li>The village totals (all four farmers together) of Vadavali, Gondghar and Kurang are equal.</li>"
 "<li>The village totals of Velas, Kudgaon and Dabhol are three consecutive integers, in some order.</li></ol>" +
 p("The table gives some of the numbers (villages shortened to their first three letters).") + GIVEN,
 "DILR::DI::Data_Tabulation",
 steps(("Totals", p("24 different integers from 1 to 24 must be 1 to 24 exactly: 300 in all. So F4 + (F4 + 2) + (F4 + 4) + (F4 + 6) = 300 gives 72, 74, 76, 78 for F4, F3, F2, F1.")),
       ("Numbers left", p("The 14 given numbers leave 1, 2, 5, 6, 12, 13, 14, 16, 18 and 24 for the ten blanks. F4 needs 72 − 44 = 28 more from Kurang and Dabhol: only 12 + 16 works. F2 needs 7 from Vadavali and Gondghar: 1 + 6 or 2 + 5.")),
       ("Village totals", p("Velas = 3 + 23 + 17 + 9 = 52. Kudgaon = F1’s number + 40, and F1’s number is 13 or 14 (10 and 11 are used), so Kudgaon is 53 or 54. If it were 54, Dabhol would be 53 and need F3 + F4 = 24 there, impossible with F4 = 12 or 16. So Kudgaon = 53 (F1 has 13), Dabhol = 51 and the other three villages have (300 − 156) ÷ 3 = 48 each.")),
       ("Fill in", p("Dabhol: F3 + F4 = 22, so F4 = 16, F3 = 6, and F4 has 12 in Kurang. Kurang: F1 = 48 − 34 = 14, so F1 has 78 − 60 = 18 in Vadavali. Gondghar: F2 + F3 = 6 from what is left (1, 2, 5, 24): 5 + 1. Vadavali: F2 = 2, F3 = 24.") + FULL)) +
 final("The whole table is fixed."),
 p("Distinct integers up to 24 in 24 cells means every number from 1 to 24 appears once."),
 p("<b>Magic-square style tables:</b> fix the grand total first, then the row and column totals, then cells."))
P.dq(1, "What is the total number of orchards owned by all four farmers in Kudgaon?", [], "TITA", "53", "Easy",
 "Kudgaon is 53 or 54; one of them breaks Dabhol.",
 steps(("Kudgaon", p("13 + 10 + 19 + 11 = 53."))) + final("53"))
P.dq(2, "Who owns the most orchards in any single village?", ["F1", "F2", "F3", "F4"], "MCQ", "3", "Easy",
 "Where does 24 go?",
 steps(("24", p("F3 has 24 in Vadavali."))) + final("Option 3"),
 [("1", "F1’s largest is 22."), ("2", "F2’s largest is 23."), ("4", "F4’s largest is 20.")])
P.dq(3, "How many orchards does F1 own in Kurang?", ["12", "13", "14", "16"], "MCQ", "3", "Easy",
 "Kurang totals 48.",
 steps(("Kurang", p("48 − (15 + 7 + 12) = 14."))) + final("Option 3"),
 [("1", "F4’s number in Kurang."), ("2", "F1’s number in Kudgaon."), ("4", "F4’s number in Dabhol.")])
P.dq(4, "What is the difference between F2’s numbers of orchards in Vadavali and Gondghar?", ["2", "3", "4", "5"], "MCQ", "2", "Easy",
 "F2 has 2 and 5.",
 steps(("F2", p("Vadavali 2, Gondghar 5: difference 3."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Uses 1 and 6.")])
P.dq(5, "How many orchards does F3 own in Dabhol?", ["1", "5", "6", "10"], "MCQ", "3", "Easy",
 "Dabhol totals 51.",
 steps(("Dabhol", p("51 − (8 + 21 + 16) = 6."))) + final("Option 3"),
 [("1", "F3’s number in Gondghar."), ("2", "F2’s number in Gondghar."), ("4", "F2’s number in Kudgaon.")])

# ---------------- Set 2: Picking coins (Q6–10) ----------------
P.dilr_set(2, "Set 2 — Picking up coins to make 100", DIR,
 p("Baby and Chubby play a game in steps. Before the first step each rolls a fair die once; if the numbers are equal they roll again until they differ. The lower number is the Lower Limit (LL) and the higher the Higher Limit (HL). There is a large pile of plastic coins.") +
 "<ul><li>In each step exactly one player picks up coins, and the players take turns.</li>"
 "<li>Step 1: the player who rolled LL picks up 1 coin.</li>"
 "<li>Every later step: the player picks up at least LL times and at most HL times the number of coins the other player picked up in the previous step.</li>"
 "<li>The game stops when the total picked up by both players is exactly 100.</li>"
 "<li>If every allowed pick would take the total above 100, nobody picks and the game is abandoned.</li></ul>",
 "DILR::LR::Games_and_Tournaments",
 steps(("Ranges", p("If the previous pick was n, the next pick is between LL·n and HL·n. So picks grow by a factor of at least LL each step.")),
       ("Reaching 100 exactly", p("Work backwards: with total T and previous pick n, the game can still finish only if some allowed pick lands exactly on 100, now or later. Once the smallest allowed pick overshoots and no smaller path exists, the game is lost.")),
       ("With LL = 1, HL = 2", p("Picks can stay level or at most double. The fastest finish is 1, 2, 4, 8, 16, 32, … : seven steps are needed, since six steps give at most 63."))) +
 final("Each question is a short calculation with the pick ranges."),
 p("For ‘exactly 100’ questions, compare what is left with the smallest and largest totals the remaining steps can reach."),
 p("<b>Bounded growth:</b> with each term between LL and HL times the last, the reachable sums after k more terms form a range you can bound quickly."))
P.dq(6, "Baby rolled 2 and Chubby 3. The game went: Baby 1, Chubby 3, Baby 8, Chubby 18, Baby 45; after that it was abandoned. Call a player the loser if he was the first to make a pick after which 100 could no longer be reached. Who lost, and with which pick?", ["Chubby, picking 3 in step 2.", "Baby, picking 8 in step 3.", "Chubby, picking 18 in step 4.", "Baby, picking 45 in step 5."], "MCQ", "3", "Medium",
 "After step 3 the total is 12. Could Chubby still have saved it?",
 steps(("After step 3", p("Total 12. Chubby may pick 16 to 24; Baby then picks 2 to 3 times that. Chubby 22, 23 or 24 lets Baby pick 66, 65 or 64 to make 100. So the game was still alive.")),
       ("Chubby’s 18", p("Total 30. Baby must pick 36 to 54 (total 66 to 84), and Chubby would then need 16 to 34 but must pick at least twice Baby’s pick. 100 can no longer be reached."))) + final("Option 3"),
 [("1", "100 was still reachable after step 2."), ("2", "Still reachable after step 3."), ("4", "Already lost after step 4.")])
P.dq(7, "Baby rolled 2 and Chubby 3. The first three steps were Baby 1, Chubby 3, Baby 8. The game must finish in exactly 5 steps. How many different pairs of picks (Chubby in step 4, Baby in step 5) are possible?", [], "TITA", "3", "Medium",
 "They must add to 88.",
 steps(("Ranges", p("Chubby picks c from 16 to 24; Baby picks 88 − c, which must be between 2c and 3c.")),
       ("Solve", p("88 − c ≥ 2c gives c ≤ 29 (always true here); 88 − c ≤ 3c gives c ≥ 22. So c = 22, 23, 24."))) + final("3"))
P.dq(8, "Baby rolled 1 and Chubby 2. The player whose pick makes the total exactly 100 wins. The first steps were Baby 1, Chubby 2, Baby 4, Chubby 8, Baby 16. Baby went on to win. In how many different ways could the rest of the game have gone?", [], "TITA", "16", "Hard",
 "31 coins so far; 69 to go, ending on Baby’s turn.",
 steps(("Two more steps", p("Chubby c (16 to 32), Baby 69 − c, which must be between c and 2c: c from 23 to 32, giving 10 ways.")),
       ("Four more steps", p("Picks w ≤ x ≤ y ≤ z, each at most double the last, starting from at least 16, adding to 69. These are 16+16+16+21, 16+16+17+20, 16+16+18+19, 16+17+17+19, 16+17+18+18 and 17+17+17+18: 6 ways.")),
       ("Six or more", p("Six picks of at least 16 already exceed 69.")),
       ("Total", p("10 + 6 = 16."))) + final("16"))
P.dq(9, "Baby rolled 1 and Chubby 2. The game finished, with a total of exactly 100, in the fewest possible steps. What is the largest number of coins that could have been picked in the last step?", [], "TITA", "48", "Medium",
 "Six steps reach at most 63, so seven are needed.",
 steps(("Seven steps", p("Doubling every time gives 1 + 2 + 4 + 8 + 16 + 32 = 63 after six, so the game needs seven steps.")),
       ("Big last pick", p("To make the last pick large, the first six should add up to little while the sixth is large. 1, 2, 4, 7, 14, 24, 48: the last pick 48 is double 24, and the total is 100. A last pick of 49 or more needs a sixth pick of at least 25, so the first five add to at most 100 − 49 − 25 = 26. But then the fifth pick is at least 13, the fourth at least 7, the third at least 4 and the second at least 2: with the first pick of 1 that is already 27."))) + final("48"))
P.dq(10, "Baby rolled 1 and Chubby 2. The game had to finish in exactly 10 steps. Which of these sets of the first eight picks (Baby, Chubby, Baby, …) can still lead to a total of exactly 100?<br>Set 1: 1, 2, 2, 3, 3, 5, 8, 10<br>Set 2: 1, 2, 2, 4, 4, 4, 8, 8<br>Set 3: 1, 1, 2, 3, 4, 6, 6, 11<br>Set 4: 1, 1, 2, 2, 3, 3, 6, 11", ["Only Set 1", "Only Set 2", "Only Set 3", "More than one set"], "MCQ", "3", "Medium",
 "Compare what is left with the largest two more picks.",
 steps(("Set 1", p("Total 34, last 10: at most 20 + 40 = 60 more. Short.")),
       ("Set 2", p("Total 33, last 8: at most 16 + 32 = 48. Short.")),
       ("Set 3", p("Total 34, last 11: 22 + 44 = 66 exactly. Works.")),
       ("Set 4", p("Total 29, last 11: at most 66, but 71 is needed. Short."))) + final("Option 3"),
 [("1", "Can add only 60."), ("2", "Can add only 48."), ("4", "Only Set 3 works.")])

# ---------------- Set 3: Medicine stocks (Q11–15) ----------------
OPEN = table(["", "M", "Tu", "W", "Th", "F", "Sa"], [["L", "200", "171", "144", "108", "72", "36"], ["S", "200", "162", "117", "72", "54", "36"]])
ALL = (p("Sales:") + table(["Day", "L", "S"], [["Mon", "48", "56"], ["Tue", "43", "58"], ["Wed", "48", "53"], ["Thu", "44", "24"], ["Fri", "40", "22"], ["Sat", "27", "24"]]) +
       p("Purchases that night:") + table(["Day", "L", "S"], [["Mon", "19", "18"], ["Tue", "16", "13"], ["Wed", "12", "8"], ["Thu", "8", "6"], ["Fri", "4", "4"], ["Sat", "191", "188"]]))
P.dilr_set(3, "Set 3 — Restocking two medicines", DIR,
 p("A pharmacy is open Monday to Saturday. It sells two medicines, L and S. From Monday to Friday, after closing each night, it buys more of each medicine: exactly 12.5% of that medicine’s stock left at the end of the day. On Saturday night it buys enough of each to bring the opening stock on Monday back to 200.") +
 p("The chart shows the opening stock of each medicine from Monday to Saturday of one week; the values are also listed below. Stock, purchases and sales are in the same units.") + F.STOCK + OPEN +
 p("<b>Daily Stock Turnover %</b> = (sales that day ÷ opening stock that day) × 100. On Saturday it was 75% for L and 66⅔% for S."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Link the days", p("From Monday to Friday, next opening = 1.125 × (opening − sales). So sales = opening − (8/9) × next opening, and the purchase = next opening ÷ 9.")),
       ("Saturday", p("Sales = 75% of 36 = 27 for L and ⅔ of 36 = 24 for S. The Saturday purchase brings the stock back to 200: 200 − (36 − sales).")),
       ("All values", ALL)) +
 final("Every sale and purchase is now known."),
 p("Each night’s purchase is one-ninth of the next morning’s stock: no percentages needed."),
 p("<b>Stock flows:</b> opening − sales + purchases = next opening; write it once and reuse it for every day."))
P.dq(11, "What were the combined sales of both medicines on Wednesday?", [], "TITA", "101", "Medium",
 "Sales = Wednesday’s opening − (8/9) × Thursday’s opening.",
 steps(("L", p("144 − (8/9)(108) = 144 − 96 = 48.")),
       ("S", p("117 − (8/9)(72) = 117 − 64 = 53.")),
       ("Total", p("101."))) + final("101"))
P.dq(12, "What was the daily stock turnover % of medicine S on Thursday?", ["35⅘", "45⅜", "33⅓", "40⁵⁄₇"], "MCQ", "3", "Medium",
 "Thursday sales of S.",
 steps(("Sales", p("72 − (8/9)(54) = 72 − 48 = 24.")),
       ("Turnover", p("24 ÷ 72 = 33⅓%."))) + final("Option 3"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(13, "What was the average nightly purchase of medicine L from Monday to Friday?", ["11.8", "10.6", "9.8", "8.6"], "MCQ", "1", "Medium",
 "Each purchase is the next opening stock ÷ 9.",
 steps(("Purchases", p("171/9, 144/9, 108/9, 72/9, 36/9 = 19, 16, 12, 8, 4.")),
       ("Average", p("59 ÷ 5 = 11.8."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(14, "On how many days were the purchases of the two medicines equal?", [], "TITA", "1", "Medium",
 "Compare next-day openings, or the Saturday top-ups.",
 steps(("Mon–Fri", p("L: 19, 16, 12, 8, 4. S: 18, 13, 8, 6, 4. Equal only on Friday.")),
       ("Saturday", p("L 191, S 188."))) + final("1"))
P.dq(15, "The Weekly Stock Turnover % is (total sales Monday to Saturday ÷ sum of the six opening stocks) × 100. What is it for medicine S, to the nearest whole number?", ["37", "36", "35", "34"], "MCQ", "1", "Medium",
 "Add S’s sales and S’s opening stocks.",
 steps(("Sales", p("56 + 58 + 53 + 24 + 22 + 24 = 237.")),
       ("Openings", p("200 + 162 + 117 + 72 + 54 + 36 = 641.")),
       ("Ratio", p("237 ÷ 641 ≈ 36.97%, about 37."))) + final("Option 1"),
 [("2", "Rounds down."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

# ---------------- Set 4: Consulting teams (Q16–20) ----------------
WAYS = table(["Way", "M2 in", "M7 in"],
             [["1", "a, b, c", "B, C, D"], ["2", "a, b, d", "A, C, D"], ["3", "a, c, d", "A, B, D"], ["4", "b, c, d", "A, B, C"]])
P.dilr_set(4, "Set 4 — Six consulting teams", DIR,
 p("A consulting firm has ten managers, M1 to M10. M1, M4, M5 and M10 studied at School P; M3, M6, M8 and M9 at School Q; and the other two, M2 and M7, at School R. The firm forms six teams for different projects.") +
 "<ol><li>Each team has five members: two from P, two from Q and one from R.</li>"
 "<li>Each manager is in exactly three teams.</li>"
 "<li>M2 and M8 are never in the same team; nor are M3 and M9.</li>"
 "<li>M4 and M5 always work together: any team with one of them has the other.</li>"
 "<li>No two teams have the same five members.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("School R", p("Six teams with one R member each, and each R manager in three teams: three teams have M2 and three have M7.")),
       ("School Q with M2", p("M2’s teams cannot have M8, and cannot have both M3 and M9. So each has M6 and one of M3, M9. M6 is then in all three M2 teams and in no M7 team, so M7’s teams have M8 and one of M3, M9.")),
       ("School P", p("M4 and M5 come as a pair, in three teams; M1 and M10 fill the P places of the other three teams, so M1 and M10 are together in the other three. Each team’s P pair is {M4, M5} or {M1, M10}.")),
       ("Count", p("M2’s possible teams: a = {M2, M6, M3, M4, M5}, b = {M2, M6, M9, M4, M5}, c = {M2, M6, M3, M1, M10}, d = {M2, M6, M9, M1, M10}. M7’s: A, B, C, D with M8 in place of M6 and M7 in place of M2. M3, M9, the pair M4–M5 and the pair M1–M10 must each end up in exactly three teams. Once M2’s three teams are chosen, this fixes M7’s three: if M2 leaves out a, M7 must leave out D, and so on.") + WAYS)) +
 final("Four ways to form the teams."),
 p("Start from the school with only two managers: they split the six teams three and three."),
 p("<b>Design counting:</b> when each person must appear a fixed number of times, the choices for one group often fix the other completely."))
P.dq(16, "In how many ways can the six teams be formed?", [], "TITA", "4", "Medium",
 "Choose M2’s three teams out of four candidates.",
 steps(("Choice", p("M2’s teams are three of a, b, c, d: 4 choices. Each choice fixes M7’s teams, because M3, M9 and the two P pairs must each reach exactly three teams."))) + final("4"))
P.dq(17, "If M1 and M2 are together in exactly two teams, which pair(s) are together in three teams?", ["Only M2 & M6", "Only M7 & M8", "Both M2 & M6 and M7 & M8", "Neither pair"], "MCQ", "3", "Medium",
 "M6 is in every M2 team; M8 is in every M7 team.",
 steps(("Always", p("In every way of forming the teams, M2 and M6 share three teams, and so do M7 and M8."))) + final("Option 3"),
 [("1", "M7 & M8 are also together three times."), ("2", "M2 & M6 are also together three times."), ("4", "Both pairs are.")])
P.dq(18, "If M3 and M6 are together in exactly two teams, which of these pairs is also together in exactly two teams?", ["M8 and M9", "M3 and M8", "M4 and M5", "No such pair"], "MCQ", "1", "Medium",
 "M3 is in two of M2’s teams, so in one of M7’s.",
 steps(("M3", p("M3 has three teams; two are with M2 (and M6), so one is with M7 (and M8). M9 is then with M7 and M8 in the other two M7 teams.")),
       ("Check", p("M8 and M9: two teams. M3 and M8: one. M4 and M5: three."))) + final("Option 1"),
 [("2", "Together only once."), ("3", "Always three times."), ("4", "M8 and M9 qualify.")])
P.dq(19, "Statement A: if M3 and M8 are together in exactly two teams, M7 is with them in both.<br>Statement B: M2 is with both M1 and M10 in exactly two teams.<br>Which is right?", ["Only A is definitely correct; B may or may not be.", "Only B is definitely correct; A may or may not be.", "Both are definitely correct.", "Both are definitely incorrect."], "MCQ", "1", "Medium",
 "M8 is only ever in M7’s teams.",
 steps(("A", p("Every team with M8 has M7, so A is always true.")),
       ("B", p("M2 is with M1 and M10 in teams c and d. Depending on which three of a–d M2 takes, that happens once or twice."))) + final("Option 1"),
 [("2", "A is always true; B is not."), ("3", "B can fail."), ("4", "A always holds.")])
P.dq(20, "Which of these cannot be a team?", ["M2, M3, M4, M5, M6", "M3, M4, M5, M7, M8", "M2, M4, M5, M6, M9", "M2, M4, M6, M7, M8"], "MCQ", "4", "Easy",
 "Count the School R members.",
 steps(("Option 4", p("It has both M2 and M7 from School R, and only one School P manager."))) + final("Option 4"),
 [("1", "Team a."), ("2", "Team A."), ("3", "Team b.")])
