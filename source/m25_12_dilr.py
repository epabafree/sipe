# -*- coding: utf-8 -*-
# Simp Mock 12 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_12 import P

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: A quiz (Q1–6) ----------------
SCORES = table(["Name", "1-mk", "2-mk", "Total"],
               [["Mrinali", "12", "13", "38"], ["Manikarnika", "20", "11", "42"], ["Prabneebh", "16", "15", "46"],
                ["Kalakruti", "14", "18", "50"], ["Gajanand", "10", "22", "54"], ["Rajkumari", "24", "17", "58"]])
P.dilr_set(1, "Set 1 — Six contestants in a quiz", DIR,
 p("Six participants took a quiz entrance test with 24 questions worth 1 mark each and 24 questions worth 2 marks each. The numbers of 1-mark questions the six answered correctly were six distinct integers, and so were the numbers of 2-mark questions; altogether these were 12 distinct numbers. The six participants’ total marks were in arithmetic progression. There was no penalty for a wrong answer or for leaving a question out.") +
 "<ul><li>Gajanand did not score the highest marks.</li><li>The highest marks scored by anyone were 58.</li><li>Mrinali scored the least.</li><li>Rajkumari answered 24 of the 1-mark questions correctly.</li>"
 "<li>The numbers of 1-mark questions answered correctly by Gajanand, Mrinali, Kalakruti and Prabneebh, in that order, are in arithmetic progression with a positive common difference.</li>"
 "<li>Manikarnika answered 20 of the 1-mark and 11 of the 2-mark questions correctly.</li><li>Mrinali’s numbers of correct 1-mark and 2-mark answers were consecutive integers.</li>"
 "<li>Prabneebh scored less than Gajanand, Kalakruti and Rajkumari.</li><li>The fewest and most correct 1-mark answers by anyone were 10 and 24.</li></ul>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("Common difference", p("Totals are 58 − 5d, …, 58. Manikarnika has 20 + 22 = 42, which is not the lowest (Mrinali is), so 58 − 42 = 16 is less than 5d: d ≥ 4. Mrinali’s 1-mark count is above Gajanand’s, so at least 11, and her 2-mark count differs by one, so at least 10: she has at least 31 marks, and 58 − 5d ≥ 31 gives d ≤ 5. 16 must be a multiple of d, so d = 4.")),
       ("Totals", p("38, 42, 46, 50, 54, 58. Mrinali has the lowest, 38. With n and n ± 1 correct, 3n ± 2 = 38 gives n = 12, so 12 one-mark and 13 two-mark.")),
       ("One-mark counts", p("Gajanand, Mrinali, Kalakruti, Prabneebh form an AP through 12; the minimum 10 must be Gajanand’s (Rajkumari 24, Manikarnika 20). So 10, 12, 14, 16.")),
       ("Totals placed", p("Prabneebh is below three others but above Mrinali and is not 42, so he has 46 (15 two-mark). Kalakruti: 14 + 2x is 50, 54 or 58, giving x = 18, 20 or 22; 20 is Manikarnika’s 1-mark count, and x = 22 would give Kalakruti 58, leaving 50 or 54 for Rajkumari with 13 or 15 two-mark answers, both already taken. So Kalakruti has 50, Gajanand (not top) 54, Rajkumari 58.")),
       ("Result", SCORES)) +
 final("All six rows are fixed."),
 p("Bound the common difference first: Manikarnika’s 42 and the top score 58 must both be terms."),
 p("<b>Two terms of an AP:</b> their difference is a multiple of the common difference."))
P.dq(1, "How many 2-mark questions did Kalakruti answer correctly?", ["15", "18", "22", "17"], "MCQ", "2", "Medium",
 "Kalakruti scored 50 with 14 one-mark answers.", steps(("2-mark", p("(50 − 14) ÷ 2 = 18."))) + final("Option 2"),
 [("1", "Prabneebh’s."), ("3", "Gajanand’s."), ("4", "Rajkumari’s.")])
P.dq(2, "Who scored the highest marks among the six participants?", ["Gajanand", "Kalakruti", "Rajkumari", "None of these"], "MCQ", "3", "Easy",
 "Gajanand is ruled out directly.", steps(("Top", p("Rajkumari, 58."))) + final("Option 3"),
 [("1", "54."), ("2", "50."), ("4", "Rajkumari is listed.")])
P.dq(3, "Who answered the most 2-mark questions correctly?", ["Gajanand", "Kalakruti", "Rajkumari", "Prabneebh"], "MCQ", "1", "Easy",
 "Low 1-mark count, high total.", steps(("Most", p("Gajanand, 22."))) + final("Option 1"),
 [("2", "18."), ("3", "17."), ("4", "15.")])
P.dq(4, "Which of the following statements is correct?", ["Kalakruti scored 58 marks.", "Rajkumari scored 54 marks.", "Prabneebh scored 46 marks.", "Gajanand scored 50 marks."], "MCQ", "3", "Easy",
 "Read off the table.", steps(("Check", p("Prabneebh 46 is right."))) + final("Option 3"),
 [("1", "Kalakruti scored 50."), ("2", "Rajkumari scored 58."), ("4", "Gajanand scored 54.")])
P.dq(5, "What is the median of the numbers of 2-mark questions answered correctly by the six participants?", [], "TITA", "16", "Easy",
 "Sort the six 2-mark counts.", steps(("Sorted", p("11, 13, 15, 17, 18, 22: median (15 + 17) ÷ 2 = 16."))) + final("16"))
P.dq(6, "How many participants answered more 2-mark questions correctly than 1-mark questions?", [], "TITA", "3", "Easy",
 "Compare the two columns.", steps(("Count", p("Mrinali (13 > 12), Kalakruti (18 > 14), Gajanand (22 > 10)."))) + final("3"))

# ---------------- Set 2: Robots (Q7–11) ----------------
ROUTES = table(["Robot", "From", "To"], [["R1", "S3", "S4"], ["R2", "S6", "S1"], ["R3", "S4", "S2"], ["R4", "S1", "S3"], ["R5", "S5", "S6"], ["R6", "S2", "S5"]])
ORDERS = ("<ul><li><b>Case 1</b>: R5, R2, R1, R4, R3, R6</li><li><b>Case 2</b>: R5, R3, R6, R4, R2, R1</li>"
          "<li><b>Case 3</b>: R2, R1, R5, R3, R6, R4</li><li><b>Case 4</b>: R3, R6, R5, R2, R1, R4</li></ul>")
P.dilr_set(2, "Set 2 — Six robots, six stations", DIR,
 p("In a robotics training facility, six robots R1 to R6 move between six stations S1 to S6. Each robot starts at its own station (no two at the same one) and, as programmed, moves once to a different station, taking exactly 10 minutes; no two robots have the same destination. All the moves happen between 10 AM and 11 AM, and no two robots move at the same time.") +
 "<ul><li>R1 starts from S3 at the moment R2 reaches its destination, S1.</li><li>R4 reaches its destination 40 minutes after R5 starts from S5.</li><li>R6 starts from S2 at the moment R3 reaches its destination, S2.</li>"
 "<li>R4 does not start from S6, and R2 does not start from S4.</li><li>R1’s destination is not S5, and R6’s destination is not S4.</li><li>The robot that starts at S1 goes to S3, and the robot that starts at S5 goes to S6.</li></ul>",
 "DILR::LR::Scheduling",
 steps(("Timing", p("Six 10-minute moves fit into one hour with no overlap, so the moves fill the slots 10:00, 10:10, …, 10:50 back to back.")),
       ("Starts", p("R1, R5, R6 start at S3, S5, S2. R2 is not at S1 (its own destination) or S4, so S6. R3 can’t start at S1 (it would have to go to S3, not S2), so R3 is at S4 and R4 at S1.")),
       ("Destinations", p("R2 → S1, R3 → S2, R4 → S3, R5 → S6. R1 and R6 take S4 and S5; R1 can’t go to S5.") + ROUTES),
       ("Order", p("R2 is immediately followed by R1, R3 by R6, and R4 starts three slots after R5. The two slots between R5 and R4 hold one pair; the other pair goes before or after.") + ORDERS)) +
 final("Routes fixed; four possible orders."),
 p("A full hour with six 10-minute moves leaves no gaps, so ‘at the same time’ clues become ‘next slot’."),
 p("<b>Back-to-back slots:</b> when the total time is used up exactly, every gap is zero."))
P.dq(7, "For how many of the six robots can both the starting station and the destination be uniquely determined?", [], "TITA", "6", "Medium",
 "Use the start clues, then the one-destination-each rule.", steps(("Count", p("All six routes are fixed."))) + final("6"))
P.dq(8, "Which of the following robots definitely did not start at 10:10?", ["R2", "R3", "R5", "R6"], "MCQ", "3", "Easy",
 "R5 starts first or third.", steps(("Slot 2", p("Cases 1–2 put R2 or R3 second; cases 3–4 put R1 or R6 second. R5 is never second."))) + final("Option 3"),
 [("1", "Case 1."), ("2", "Case 2."), ("4", "Case 4.")])
P.dq(9, "Which of the following can be correct?",
 ["R1 moves from S3 to S1 and is the first robot to start moving.", "R1 moves from S3 to S4 and is the second robot to start moving.",
  "R5 moves from S5 to S6 and is the second robot to start moving.", "R5 moves from S5 to S4 and is the fourth robot to start moving."], "MCQ", "2", "Easy",
 "Check routes, then slots.", steps(("Check", p("R1 goes S3 → S4 and is second in case 3."))) + final("Option 2"),
 [("1", "R1 goes to S4."), ("3", "R5 is first or third."), ("4", "R5 goes to S6.")])
P.dq(10, "If R4 is the last robot to start moving, which robot can be the first to start moving?", ["Only R2", "Only R3", "Either R2 or R3", "Neither R2 nor R3"], "MCQ", "3", "Easy",
 "R4 last puts R5 third.", steps(("Cases", p("Cases 3 and 4: R2 or R3 first."))) + final("Option 3"),
 [("1", "Case 4 has R3."), ("2", "Case 3 has R2."), ("4", "Both are possible.")])
P.dq(11, "If R5 is the first robot to start moving, for how many robots other than R5 can the starting times be uniquely determined?", ["1", "2", "More than 2", "R5 cannot be the first robot to start moving"], "MCQ", "1", "Medium",
 "R5 first fixes R4 fourth.", steps(("Cases 1 and 2", p("Only R4 (10:30) is fixed; the two pairs can swap."))) + final("Option 1"),
 [("2", "The pairs still swap."), ("3", "The pairs still swap."), ("4", "Cases 1 and 2 have R5 first.")])

# ---------------- Set 3: Five films (Q12–17) ----------------
GIVEN = table(["Film", "Wk 1", "Peak", "Wk 6"],
              [["Undertow", "5", "10 in wk 3", "3"], ["Freedom", "4", "12 in wk 4", "7"], ["Dog Days", "8", "13 in wk 4", "7"],
               ["Auction", "10", "12 in wk 2", "6"], ["Dunes", "6", "11 in wk 4", "5"]]) + p("Six-week totals: Freedom 48, Auction 55, Dunes 46; the other two totals are not known.")
FULL = ("<ul><li><b>Freedom</b>: 4, 6, 9, 12, 10, 7</li><li><b>Auction</b>: 10, 12, 11, 9, 7, 6</li><li><b>Dunes</b>: 6, 7, 9, 11, 8, 5</li>"
        "<li><b>Dog Days</b>: 8, then weeks 2–3 are 9, 11 or 9, 12 or 11, 12, then 13, 10, 7</li><li><b>Undertow</b>: 5, 7 or 8, 10, then five ways down to 3 (see Q14)</li></ul>")
UND = table(["Weeks 1–6", "Total"], [["5, 7, 10, 9, 6, 3", "40"], ["5, 7, 10, 8, 6, 3", "39"], ["5, 8, 10, 9, 6, 3", "41"], ["5, 8, 10, 7, 6, 3", "39"], ["5, 8, 10, 7, 4, 3", "37"]])
P.dilr_set(3, "Set 3 — Six weeks at the box office", DIR,
 p("Five films, Auction, Dog Days, Freedom, Dunes and Undertow, were released together in a city’s cinemas and drew large crowds for their first six weeks. Their weekly box office collections (in lakh euros) were recorded, but some entries are missing.") +
 "<ul><li>Each film’s weekly collection rose for a few weeks and then fell every week up to the sixth.</li><li>Each week-on-week change, up or down, was 1, 2 or 3 lakh euros.</li><li>No film collected the same amount in two different weeks.</li></ul>" +
 p("The table gives each film’s week 1 and week 6 collections, and its highest weekly collection with the week in which it came; the other entries are missing.") + GIVEN,
 "DILR::DI::Data_Tabulation",
 steps(("Shape", p("Each film rises to its peak week (the middle figure given) and falls after it, in steps of 1 to 3.")),
       ("Freedom", p("4 to 12 in three steps needs a total rise of 8; 12 to 7 in two steps needs 5. With total 48, weeks 2, 3, 5 sum to 25. Week 5 is 9 or 10. If 9, weeks 2–3 sum to 16 and the only rise is 7, 9, repeating 9. So week 5 = 10 and weeks 2–3 are 6, 9 (sum 15).")),
       ("Auction and Dunes", p("Auction falls 12 → 6 over four weeks (total 6) with weeks 3–5 summing 27: 11, 9, 7 (10, 9, 8 would repeat week 1’s 10). Dunes: 6 → 11 in three steps and 11 → 5 in two (both 3s); weeks 2, 3 sum 16: 7, 9.")),
       ("Results", FULL)) +
 final("Freedom, Auction and Dunes are fixed; Dog Days and Undertow have a few options."),
 p("Lock the films with totals first; for the others, list the few ways each rise and fall can go."),
 p("<b>Bounded steps:</b> a fixed number of steps of 1 to 3 between two known values leaves only a few paths."))
P.dq(12, "What was Freedom’s collection (in lakh euros) in the fifth week?", [], "TITA", "10", "Easy",
 "12 down to 7 in two steps, with the total 48.", steps(("Week 5", p("48 − (4 + 6 + 9 + 12 + 7) = 10."))) + final("10"))
P.dq(13, "What was Auction’s average weekly collection in the first four weeks?", ["10.0 lakh euros", "10.5 lakh euros", "11.0 lakh euros", "Cannot be determined"], "MCQ", "2", "Easy",
 "Auction is 10, 12, 11, 9, ….", steps(("Average", p("(10 + 12 + 11 + 9) ÷ 4 = 10.5."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Auction is fully fixed.")])
P.dq(14, "If Undertow’s total for the six weeks is P lakh euros, how many distinct values can P take?", [], "TITA", "4", "Medium",
 "List the paths 5 → 10 → 3.",
 steps(("Paths", p("Week 2 is 7 or 8; weeks 4–5 fall from 10 to 3 in three steps of 1 to 3, without repeating a value.") + UND),
       ("Totals", p("37, 39, 40, 41."))) + final("4"))
P.dq(15, "What is the minimum possible total collection (in lakh euros) of all five films in the fifth week?", [], "TITA", "39", "Medium",
 "Only Undertow’s week 5 varies.", steps(("Week 5", p("Undertow 4, Freedom 10, Dog Days 10, Auction 7, Dunes 8: 39."))) + final("39"))
P.dq(16, "Which of the following statements is definitely true?",
 ["The collections of Dog Days and Freedom were equal in exactly three of the six weeks.", "Undertow and Dunes collected the same amount in week 2.",
  "In no week did Undertow collect more than Dog Days.", "None of these"], "MCQ", "3", "Hard",
 "Compare week by week with the extremes.",
 steps(("Option 3", p("Undertow’s highest possible values (5, 8, 10, 9, 6, 3) stay below Dog Days’ lowest (8, 9, 11, 13, 10, 7) in every week.")),
       ("Others", p("Dog Days and Freedom match only in weeks 5 and 6. Undertow’s week 2 may be 8, unlike Dunes’ 7."))) + final("Option 3"),
 [("1", "Only two weeks."), ("2", "Not definite: 7 or 8."), ("4", "Option 3 holds.")])
P.dq(17, "What is the maximum possible number of instances in which a film’s weekly collection fell by 3 lakh euros from the previous week?", [], "TITA", "7", "Hard",
 "Count the 3-drops for each film, choosing the best path where there is a choice.",
 steps(("Count", p("Freedom 1 (10 → 7); Auction 0; Dunes 2; Dog Days 2 (13 → 10 → 7); Undertow at most 2 (10 → 7 → 4)."))) + final("7"))

# ---------------- Set 4: Five food items (Q18–22) ----------------
COSTS = (table(["Item", "C1", "C2", "C3", "C4", "C5"],
              [["A", "12", "15", "a", "10", "13"], ["B", "a", "b", "30", "18", "15"],
               ["C", "9", "6", "5", "b% of Q", "4"], ["D", "22", "38", "15", "d", "e"], ["E", "d", "e", "8", "12", "f"]]) +
         table(["Item", "CP", "SP", "Profit %"],
              [["A", "50 + a", "98", "2a"], ["B", "P", "T", "V"], ["C", "Q", "U", "W"], ["D", "R", "149", "X"], ["E", "S", "149", "Y"]]))
SOLVED = table(["Item", "CP", "SP", "Profit %"], [["A", "70", "98", "40"], ["B", "108", "135", "25"], ["C", "32", "40", "25"], ["D", "100", "149", "49"], ["E", "50", "149", "198"]])
P.dilr_set(4, "Set 4 — Costs of five food items", DIR,
 p("A fast-food shop sells five ready-to-eat items, A, B, C, D and E, all at a profit. It splits the cost of preparing each item into five components, C1 to C5. The tables give, per unit, each item’s cost components, cost price (CP), selling price (SP) and profit percentage, where profit % = (SP − CP) ÷ CP × 100.") +
 p("Every entry in the tables, whether a numeral or a letter, is a positive integer, in ₹.") + COSTS +
 "<ul><li>CP = C1 + C2 + C3 + C4 + C5.</li><li>For item B, C1 ≤ C2 ≤ C3.</li><li>The five cost prices are all different.</li><li>d = e + 1.</li><li>V = W = b.</li></ul>",
 "DILR::DI::Data_Tabulation",
 steps(("A", p(r"\(98 = (50 + a)(1 + \tfrac{2a}{100})\) \(= \tfrac{2(50 + a)^2}{100}\), so \((50 + a)^2 = 4900\): a = 20, CP 70, profit 40%.")),
       ("C fixes b", p(r"\(Q = 24 + \tfrac{bQ}{100}\), so \(Q = \tfrac{2400}{100 - b}\) with \(20 \le b \le 30\): b = 20 (Q = 30) or b = 25 (Q = 32).")),
       ("B decides", p("P = 83 + b and T = P(1 + b/100) must be whole. b = 20 gives 103 × 1.2 = 123.6, so b = 25: P = 108, T = 135, and C: Q = 32, U = 40.")),
       ("D and E", p(r"X whole needs R to divide 14,900 = \(2^2 \cdot 5^2 \cdot 149\). R = 76 + 2e lies between 78 and 148, so R = 100: e = 12, d = 13, X = 49. S = 45 + f must also divide 14,900, differ from 100 and stay below 149: S = 50, f = 5, Y = 198.")),
       ("Result", SOLVED)) +
 final("a = 20, b = 25, d = 13, e = 12, f = 5."),
 p("A’s row has one unknown; solve it, then let ‘b% of Q’ and whole-number prices pin down b."),
 p("<b>Integer percentages:</b> (SP − CP)/CP × 100 is whole only if CP divides 100 × SP."))
P.dq(18, "If the selling price of A is changed to ₹84 per unit, what will the profit percentage be?", ["12", "20", "40", "50"], "MCQ", "2", "Easy",
 "CP of A is 70.", steps(("Profit", p("(84 − 70) ÷ 70 = 20%."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "The original profit."), ("4", "Arithmetic slip.")])
P.dq(19, "What is the value of Y − (V + W + X)?", [], "TITA", "99", "Hard",
 "Y = 198, V = W = 25, X = 49.", steps(("Value", p("198 − 99 = 99."))) + final("99"))
P.dq(20, r"Raw material prices rise, and the new profit percentage on C at ₹U per unit is \(11\tfrac19\%\). By how much (in ₹) did the cost of one unit of C rise?", ["3", "4", "5", "6"], "MCQ", "2", "Medium",
 r"U = 40 and profit is \(\tfrac19\).", steps(("New CP", p(r"\(40 \div \tfrac{10}{9} = 36\); rise 36 − 32 = 4."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(21, "What is the median of a, b, d and e?", ["15", "16", "16.5", "17.5"], "MCQ", "3", "Easy",
 "a = 20, b = 25, d = 13, e = 12.", steps(("Median", p("12, 13, 20, 25: (13 + 20) ÷ 2 = 16.5."))) + final("Option 3"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(22, "One day the shop sold 18 units of A, 11 of B, 33 of C, 21 of D and 14 of E, and nothing else. What was the profit (in ₹) that day?", ["3480", "3520", "3740", "3800"], "MCQ", "1", "Medium",
 "Per-unit profits: 28, 27, 8, 49, 99.",
 steps(("Profit", p("18 × 28 + 11 × 27 + 33 × 8 + 21 × 49 + 14 × 99 = 504 + 297 + 264 + 1029 + 1386 = 3480."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
