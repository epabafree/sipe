# -*- coding: utf-8 -*-
# Batch 3 — CAT 2023 Slot 2: DILR sets 1–4.
from fmt import steps, final, why, table, p
from b3_s2 import P

# ---------------- Set 1: Odsville firms ----------------
P.dilr_set(1, "Set 1 — Five firms raising money", "Read the instructions given and answer the questions that follow:",
 p("Odsville has five firms – Alfloo, Bzygoo, Czechy, Drjbna and Elavalaki. Each of these firms was founded in some year and also closed down a few years later.") +
 p("Each firm raised ₹ 1 crore in its first and last year of existence. The amount each firm raised every year increased until it reached a maximum, and then decreased until the firm closed down. No firm raised the same amount of money in two consecutive years. Each annual increase and decrease was either by ₹ 1 crore or by ₹ 2 crores.") +
 p("The table below provides partial information about the five firms.") +
 table(["Firm", "First year of existence", "Last year of existence", "Total amount raised (₹ crores)"],
       [["Alfloo", "2009", "2016", "21"], ["Bzygoo", "2012", "2015", ""], ["Czechy", "2013", "", "9"], ["Drjbna", "2011", "2015", "10"], ["Elavalaki", "2010", "", "13"]]),
 "DILR::LR::Mathematical_Reasoning",
 steps(("The rules in one line", p(r"Each firm’s yearly amounts start and end at \(1\), rise then fall, change by \(1\) or \(2\) each year, and never repeat back-to-back.")),
       ("Firms with a fixed length", p(r"<b>Drjbna</b> (5 years, total \(10\)): middle three sum to \(8\) ⇒ only \(2, 4, 2\). <b>Bzygoo</b> (4 years): \(1, 2, 3, 1\) or \(1, 3, 2, 1\), total \(7\) either way. <b>Alfloo</b> (8 years, total \(21\)): \(1, 2, 3, 4, 5, 3, 2, 1\) or \(1, 2, 3, 5, 4, 3, 2, 1\).")),
       ("Firms with an open end", p(r"<b>Czechy</b> (total \(9\)): only \(1, 2, 3, 2, 1\) works (2013–2017). <b>Elavalaki</b> (total \(13\)): \(1, 3, 5, 3, 1\) (to 2014), \(1, 2, 3, 4, 2, 1\) or \(1, 2, 4, 3, 2, 1\) (to 2015)."))) +
 table(["Year", "Alfloo", "Bzygoo", "Czechy", "Drjbna", "Elavalaki"], [
   ["2009", "1", "", "", "", ""], ["2010", "2", "", "", "", "1"], ["2011", "3", "", "", "1", "3 / 2 / 2"], ["2012", "4 / 5", "1", "", "2", "5 / 3 / 4"],
   ["2013", "5 / 4", "2 / 3", "1", "4", "3 / 4 / 3"], ["2014", "3", "3 / 2", "2", "2", "1 / 2 / 2"], ["2015", "2", "1", "3", "1", "— / 1 / 1"], ["2016", "1", "", "2", "", ""], ["2017", "", "", "1", "", ""]]) +
 final("Czechy and Drjbna are fully fixed; the others have two or three options."),
 p("Write down each firm’s middle-years sum (total minus the two 1s) and list the few rise-then-fall patterns that make it. Short firms have one pattern; that’s where certainty comes from."),
 p("<b>Unimodal sequences with step limits:</b> a fixed total and length leave very few options, so enumerate them rather than reasoning case by case."))
P.dq(1, "For which firm(s) can the amounts raised by them be concluded with certainty in each year?", ["Only Czechy", "Only Bzygoo and Czechy and Drjbna", "Only Drjbna", "Only Czechy and Drjbna"],
 "MCQ", "4", "Medium", "Find the firms whose total leaves exactly one rise-then-fall pattern.",
 steps(("Count patterns", p("Czechy: one pattern. Drjbna: one. Bzygoo: two (1, 2, 3, 1 or 1, 3, 2, 1). Alfloo: two. Elavalaki: three."))) + final("Only Czechy and Drjbna — option 4"),
 [("1", "Drjbna is also fixed."), ("2", "Bzygoo has two possible patterns."), ("3", "Czechy is also fixed.")])
P.dq(2, "What best can be concluded about the total amount of money raised in 2015?", ["It is either ₹ 7 crores or ₹ 8 crores or ₹ 9 crores.", "It is either ₹ 7 crores or ₹ 8 crores.", "It is exactly ₹ 8 crores.", "It is either ₹ 8 crores or ₹ 9 crores."],
 "MCQ", "2", "Medium", "In 2015: Alfloo is fixed at 2, Bzygoo 1, Czechy 3, Drjbna 1. Only Elavalaki varies.",
 steps(("Add 2015", p(r"Alfloo \(2\) + Bzygoo \(1\) + Czechy \(3\) + Drjbna \(1\) \(= 7\), plus Elavalaki: \(0\) (closed in 2014) or \(1\)."))) + final("7 or 8 — option 2"),
 [("1", "9 is impossible: Alfloo’s 2015 value is always 2."), ("3", "7 is also possible."), ("4", "9 is impossible.")])
P.dq(3, "What is the largest possible total amount of money (in ₹ crores) that could have been raised in 2013?", [], "TITA", "17", "Medium",
 "Take the biggest option for each firm in 2013.",
 steps(("Maximise each firm", p(r"Alfloo \(5\), Bzygoo \(3\), Czechy \(1\), Drjbna \(4\), Elavalaki \(4\) (from \(1, 2, 4, 3, 2, 1\))."))) + final(r"\(5 + 3 + 1 + 4 + 4 = 17\)"))
P.dq(4, "If Elavalaki raised ₹ 3 crores in 2013, then what is the smallest possible total amount of money (in ₹ crores) that could have been raised by all the companies in 2012?", ["10", "9", "12", "11"],
 "MCQ", "4", "Hard", "Which Elavalaki patterns give 3 in 2013, and what do they give in 2012?",
 steps(("Elavalaki", p(r"\(3\) in 2013 happens for \(1, 3, 5, 3, 1\) (2012 = \(5\)) and \(1, 2, 4, 3, 2, 1\) (2012 = \(4\)). Take \(4\).")),
       ("Minimise 2012", p(r"Alfloo \(4\) (the \(1, 2, 3, 4, 5, \dots\) pattern), Bzygoo \(1\), Drjbna \(2\), Elavalaki \(4\)."))) + final(r"\(4 + 1 + 2 + 4 = 11\) — option 4"),
 [("1", "10 would need Elavalaki at 3 in 2012, but then 2013 isn’t 3."), ("2", "Too small."), ("3", "Possible, but not the smallest.")])
P.dq(5, "If the total amount of money raised in 2014 is ₹ 12 crores, then which of the following is not possible?", ["Alfloo raised the same amount of money as Drjbna in 2013.", "Bzygoo raised more money than Elavalaki in 2014.", "Bzygoo raised the same amount of money as Elavalaki in 2013.", "Alfloo raised the same amount of money as Bzygoo in 2014."],
 "MCQ", "3", "Hard", "2014 has Alfloo 3, Czechy 2, Drjbna 2 fixed. That leaves Bzygoo + Elavalaki = 5.",
 steps(("Use the 2014 total", p(r"\(3 + 2 + 2 = 7\), so Bzygoo + Elavalaki \(= 5\). Elavalaki’s 2014 value is \(1\) or \(2\), so Bzygoo is \(3\) or \(2\) (sums \(4\) and \(5\)): it must be Bzygoo \(3\) with Elavalaki \(2\).")),
       ("Test option 3", p(r"Bzygoo \(3\) in 2014 means pattern \(1, 2, 3, 1\), so Bzygoo was \(2\) in 2013. Elavalaki at \(2\) in 2014 means \(1, 2, 3, 4, 2, 1\) or \(1, 2, 4, 3, 2, 1\): \(4\) or \(3\) in 2013. Never \(2\)."))) +
 final("Option 3 is not possible"),
 [("1", "Possible: Alfloo 4 and Drjbna 4 in 2013."), ("2", "True: Bzygoo 3 > Elavalaki 2."), ("4", "True: both 3 in 2014.")])

# ---------------- Set 2: Entertainment park ----------------
P.dilr_set(2, "Set 2 — Rides in an entertainment park", "Answer the questions on the basis of the information given below.",
 p("Anjali, Bipasha and Chitra visited an entertainment park that has four rides. Each ride lasts one hour and can accommodate one visitor at one point. All rides begin at 9 a.m. and must be completed by 5 p.m. except for Ride-3, for which the last ride has to be completed by 1 p.m. Ride gates open every 30 minutes, for example, 10 a.m., 10:30 a.m., and so on. Whenever a ride gate opens, and there is no visitor inside, the first visitor waiting in the queue buys the ticket just before taking the ride.") +
 p("The ticket prices are ₹ 20, ₹ 50, ₹ 30 and ₹ 40 for Rides 1 to 4, respectively. Each of the three visitors took at least one ride and did not necessarily take all rides. None of them took the same ride more than once. The movement time from one ride to another is negligible, and a visitor leaves the ride immediately after the completion of the ride. No one takes a break inside the park unless mentioned explicitly.") +
 p("The following information is also known.") +
 "<ol><li>Chitra never waited in the queue and completed her visit by 11 a.m. after spending ₹ 50 to pay for the ticket(s).</li><li>Anjali took Ride-1 at 11 a.m. after waiting for 30 min for Chitra to complete it. It was the only ride where Anjali waited.</li><li>Bipasha began her first of three rides at 11:30 a.m. All three visitors incurred the same amount of ticket expense by 12:15 p.m.</li><li>The last ride taken by Anjali and Bipasha was the same, where Bipasha waited 30 min for Anjali to complete her ride. Before standing in the queue for that ride, Bipasha took a 1-hour coffee break after completing her previous ride.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Chitra", p("She was on Ride-1 from 10 to 11 (Anjali waited for her). ₹50 in total with Ride-1 (₹20) means one more ride worth ₹30: Ride-3, 9–10.")),
       ("Anjali to 12:15", p("Ride-1 11–12. Everyone spent ₹50 by 12:15, so Anjali’s next ticket, bought at 12:00, cost ₹30: Ride-3, 12–1 (Ride-3 must end by 1 pm).")),
       ("Bipasha to 12:15", p("Her first ticket at 11:30 must be ₹50: Ride-2, 11:30–12:30.")),
       ("The shared last ride", p("Bipasha has done Ride-2, so the shared ride is Ride-4. Bipasha’s second ride: Ride-1, 12:30–1:30 (Ride-3 is too late). Coffee 1:30–2:30, queue 2:30–3:00, Ride-4 3–4. So Anjali was on Ride-4 2–3, and before that, with no breaks, on Ride-2 1–2."))) +
 table(["Visitor", "Rides (time)", "Spent"], [["Chitra", "R3 9–10, R1 10–11", "₹50"], ["Anjali", "R1 11–12, R3 12–1, R2 1–2, R4 2–3", "₹140"], ["Bipasha", "R2 11:30–12:30, R1 12:30–1:30, (coffee), R4 3–4", "₹110"]]) +
 final("Every ride and time is fixed."),
 p("Start from the “same spend by 12:15” clue: it fixes which ticket each person bought right before 12:15."),
 p("<b>Scheduling puzzles:</b> mark each resource’s busy times on a timeline. A single “waited for X” clue pins two people at once."))
P.dq(6, "What was the total amount spent on tickets (in ₹) by Bipasha?", ["110", "100", "90", "120"], "MCQ", "1", "Medium",
 "Bipasha’s three rides are Ride-2, Ride-1 and Ride-4.", steps(("Add", p(r"\(50 + 20 + 40 = 110\)"))) + final("₹110 — option 1"),
 [("2", "Would need a different ride set."), ("3", "Drops a ride."), ("4", "Would include Ride-3, which she couldn’t take after 12:30.")])
P.dq(7, "Which were all the rides that Anjali completed by 2:00 p.m.?", ["Ride-1 and Ride-3", "Ride-1, Ride-2 and Ride-4", "Ride-1 and Ride-4", "Ride-1, Ride-2 and Ride-3"], "MCQ", "4", "Medium",
 "Anjali never takes a break, so she must be on some ride from 1 to 2.", steps(("Timeline", p("R1 11–12, R3 12–1, R2 1–2."))) + final("Ride-1, Ride-2 and Ride-3 — option 4"),
 [("1", "Misses Ride-2 (1–2)."), ("2", "Ride-4 is 2–3, not before 2."), ("3", "Ride-4 is later.")])
P.dq(8, "Which ride was taken by all three visitors?", ["Ride-1", "Ride-3", "Ride-2", "Ride-4"], "MCQ", "1", "Easy",
 "Check each person’s ride list.", steps(("Lists", p("Chitra: R3, R1. Anjali: R1, R3, R2, R4. Bipasha: R2, R1, R4."))) + final("Ride-1 — option 1"),
 [("2", "Bipasha didn’t take Ride-3."), ("3", "Chitra didn’t take Ride-2."), ("4", "Chitra didn’t take Ride-4.")])
P.dq(9, "How many rides did Anjali and Chitra take in total?", [], "TITA", "6", "Easy",
 "Anjali: four rides. Chitra: two.", steps(("Count", p(r"\(4 + 2 = 6\)"))) + final(r"\(6\)"))
P.dq(10, "What was the total amount spent on tickets (in ₹) by Anjali?", [], "TITA", "140", "Medium",
 "Anjali took all four rides.", steps(("Add", p(r"\(20 + 30 + 50 + 40 = 140\)"))) + final(r"₹\(140\)"))

# ---------------- Set 3: Random draw ----------------
P.dilr_set(3, "Set 3 — A five-day random draw", "Answer the questions based on the following information.",
 p("Three participants – Akhil, Bimal and Chatur participate in a random draw competition for five days. Every day, each participant randomly picks up a ball numbered between 1 and 9. The number on the ball determines his score on that day. The total score of a participant is the sum of his scores attained in the five days. The total score of a day is the sum of participants’ scores on that day.") +
 p("The 2-day average on a day, except on Day 1, is the average of the total scores of that day and of the previous day. For example, if the total scores of Day 1 and Day 2 are 25 and 20, then the 2-day average on Day 2 is calculated as 22.5. Table 1 gives the 2-day averages for Days 2 through 5.") +
 p("<b>Table 1: 2-day averages for Days 2 through 5</b>") + table(["Day 2", "Day 3", "Day 4", "Day 5"], [["15", "15.5", "16", "17"]], first_col_header=False) +
 p("Participants are ranked each day, with the person having the maximum score being awarded the minimum rank (1) on that day. If there is a tie, all participants with the tied score are awarded the best available rank. For example, if on a day Akhil, Bimal and Chatur score 8, 7 and 7, respectively, then their ranks will be 1, 2 and 2, respectively on that day. These ranks are given in Table 2.") +
 p("<b>Table 2: Ranks of participants on each day</b>") + table(["", "Day 1", "Day 2", "Day 3", "Day 4", "Day 5"], [["Akhil", "1", "2", "2", "3", "3"], ["Bimal", "2", "3", "2", "1", "1"], ["Chatur", "3", "1", "1", "2", "2"]]) +
 p("The following information is also known.") +
 "<ol><li>Chatur always scores in multiples of 3. His score on Day 2 is the unique highest score in the competition. His minimum score is observed only on Day 1, and it matches Akhil’s score on Day 4.</li><li>The total score on Day 3 is the same as the total score on Day 4.</li><li>Bimal’s scores are the same on Day 1 and Day 3.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("Daily totals", p(r"From the averages: \(T_1 + T_2 = 30\), \(T_2 + T_3 = 31\), \(T_3 + T_4 = 32\), \(T_4 + T_5 = 34\). With \(T_3 = T_4\): \(T_3 = T_4 = 16\), \(T_2 = 15\), \(T_1 = 15\), \(T_5 = 18\).")),
       ("Chatur", p(r"Multiples of 3, a unique top score on Day 2 ⇒ \(9\) on Day 2 and no other 9s anywhere. Minimum only on Day 1 ⇒ Day 1 \(= 3\), Days 3–5 \(= 6\). Akhil’s Day 4 \(= 3\).")),
       ("Days 1, 3, 4", p(r"Day 3: Akhil and Bimal tie below Chatur’s \(6\) and sum to \(10\) ⇒ both \(5\). Bimal Day 1 \(= 5\) ⇒ Akhil Day 1 \(= 15 - 3 - 5 = 7\). Day 4: Bimal \(= 16 - 6 - 3 = 7\).")),
       ("Days 2 and 5 (two options each)", p(r"Day 2: Akhil > Bimal, sum \(6\) ⇒ \((5, 1)\) or \((4, 2)\). Day 5: Bimal > 6 > Akhil, sum \(12\), no 9s ⇒ \((A, B) = (5, 7)\) or \((4, 8)\)."))) +
 table(["", "D1", "D2", "D3", "D4", "D5", "Total"], [["Akhil", "7", "5 / 4", "5", "3", "5 / 4", "23–25"], ["Bimal", "5", "1 / 2", "5", "7", "7 / 8", "25–27"], ["Chatur", "3", "9", "6", "6", "6", "30"]]) +
 final("Only Days 2 and 5 for Akhil and Bimal are open."),
 p("Turn the 2-day averages into daily totals first; the “Day 3 = Day 4” clue unlocks all five."),
 p(r"<b>Overlapping averages:</b> \(\tfrac{T_k + T_{k+1}}{2}\) gives a chain of sums. One extra equality fixes every term."))
P.dq(11, "What is Akhil’s score on Day 1?", ["7", "6", "5", "8"], "MCQ", "1", "Medium", "Day 1 total is 15, Chatur has 3, and Bimal’s Day 1 equals his Day 3.",
 steps(("Compute", p(r"Bimal Day 1 \(=\) Day 3 \(= 5\), so Akhil \(= 15 - 3 - 5 = 7\)."))) + final(r"\(7\) — option 1"),
 [("2", "Would give Bimal 6, but his Day 3 score is 5."), ("3", "Would tie with Bimal, but Akhil ranks 1 and Bimal 2."), ("4", "Would make Bimal 4.")])
P.dq(12, "Who attains the maximum total score?", ["Bimal", "Chatur", "Cannot be determined", "Akhil"], "MCQ", "2", "Easy", "Chatur’s total is fixed. What are the others’ largest possible totals?",
 steps(("Compare", p(r"Chatur \(30\); Bimal at most \(27\); Akhil at most \(25\)."))) + final("Chatur — option 2"),
 [("1", "At most 27."), ("3", "It is determined: 30 beats both maxima."), ("4", "At most 25.")])
P.dq(13, "What is the minimum possible total score of Bimal?", [], "TITA", "25", "Medium", "Take Bimal’s smaller options on Days 2 and 5.",
 steps(("Add", p(r"\(5 + 1 + 5 + 7 + 7 = 25\)"))) + final(r"\(25\)"))
P.dq(14, "If the total score of Bimal is a multiple of 3, what is the score of Akhil on Day 2?", ["Cannot be determined", "5", "6", "4"], "MCQ", "4", "Medium",
 "Bimal’s total can be 25, 26 or 27. Only one is a multiple of 3.",
 steps(("Bimal = 27", p(r"Needs \(2\) on Day 2 and \(8\) on Day 5. Day 2: Akhil \(= 6 - 2 = 4\)."))) + final(r"\(4\) — option 4"),
 [("1", "It is fixed once Bimal = 27."), ("2", "That pairs with Bimal 1 on Day 2 (total 25 or 26)."), ("3", "Day 2 options are only 5 or 4.")])
P.dq(15, "If Akhil attains a total score of 24, then what is the total score of Bimal?", [], "TITA", "26", "Medium",
 "Akhil = 15 + (Day 2) + (Day 5). Each of his points on those days is a point Bimal doesn’t get.",
 steps(("Akhil", p(r"\(15 + A_2 + A_5 = 24\) ⇒ \(A_2 + A_5 = 9\).")), ("Bimal", p(r"\(B_2 + B_5 = (6 - A_2) + (12 - A_5) = 9\), so Bimal \(= 17 + 9 = 26\)."))) + final(r"\(26\)"))

# ---------------- Set 4: Coins in boxes ----------------
TB = lambda vals: '<div class="tbl"><table><tr><th></th><th>Col 1</th><th>Col 2</th><th>Col 3</th></tr>' + "".join(
    f'<tr><td class="rh">Row {i+1}</td>' + "".join(f"<td>{v}</td>" for v in r) + "</tr>" for i, r in enumerate(vals)) + "</table></div>"
P.dilr_set(4, "Set 4 — Coins in a 3 × 3 grid of boxes", "Answer the questions based on the following information.",
 p("There are nine boxes arranged in a 3 × 3 array as shown in Tables 1 and 2. Each box contains three sacks. Each sack has a certain number of coins, between 1 and 9, both inclusive.") +
 p("The average number of coins per sack in the boxes are all distinct integers. The total number of coins in each row is the same. The total number of coins in each column is also the same.") +
 p("<b>Table 1</b>") + TB([["", "9", "6"], ["2", "", ""], ["8", "", ""]]) +
 p("<b>Table 2</b>") + TB([["1**", "2*", "2*"], ["1**", "0*", "3*"], ["3*", "2**", "0**"]]) +
 p("Table 1 gives information regarding the median of the numbers of coins in the three sacks in a box for some of the boxes. In Table 2, each box has a number which represents the number of sacks in that box having more than 5 coins. That number is followed by a * if the sacks in that box satisfy exactly one among the following three conditions, and it is followed by ** if two or more of these conditions are satisfied.") +
 "<ol type=\"i\"><li>The minimum among the numbers of coins in the three sacks in the box is 1.</li><li>The median of the numbers of coins in the three sacks is 1.</li><li>The maximum among the numbers of coins in the three sacks in the box is 9.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("The averages form a magic-style grid", p(r"Nine distinct integer averages between 1 and 9 are exactly \(1, 2, \dots, 9\). The grand total is \(3 \times 45 = 135\), so each row and each column holds \(45\) coins, and each row and column of <i>averages</i> sums to \(15\).")),
       ("Boxes fixed by their clues", p(r"Row 2, Col 1 (median 2, 1**): conditions min 1 and max 9 ⇒ \((1, 2, 9)\), avg \(4\). Row 3, Col 1 (median 8, 3*): max 9 only ⇒ \((7, 8, 9)\), avg \(8\). Row 1, Col 2 (median 9, 2*): \((x, 9, 9)\) with \(x = 3\) for an integer average ⇒ avg \(7\).")),
       ("Fill the averages", p(r"Col 1: \(15 - 4 - 8 = 3\). Row 1: \(15 - 3 - 7 = 5\). The rest (\(1, 2, 6, 9\)) satisfy Row 2 \(= 11\), Row 3 \(= 7\), Col 2 \(= 8\): Row 2 \((2, 9)\), Row 3 \((6, 1)\).")),
       ("Turn averages into sacks", p(r"Avg 3 with 1** ⇒ \((1, 1, 7)\). Avg 5, median 6, 2* ⇒ \((1, 6, 8)\). Avg 2, 0* ⇒ \((1, 2, 3)\). Avg 9 ⇒ \((9, 9, 9)\). Avg 6, 2** ⇒ \((1, 8, 9)\). Avg 1 ⇒ \((1, 1, 1)\)."))) +
 table(["", "Col 1", "Col 2", "Col 3"], [["Row 1", "1, 1, 7 (avg 3)", "3, 9, 9 (avg 7)", "1, 6, 8 (avg 5)"], ["Row 2", "1, 2, 9 (avg 4)", "1, 2, 3 (avg 2)", "9, 9, 9 (avg 9)"], ["Row 3", "7, 8, 9 (avg 8)", "1, 8, 9 (avg 6)", "1, 1, 1 (avg 1)"]]) +
 final("Every sack is fixed."),
 p("Spot that “distinct integer averages from 1–9” plus equal rows and columns turns the averages into a grid where every row and column sums to 15. Three boxes are fixed straight from their clues, and the grid does the rest."),
 p(r"<b>Equal row/column totals:</b> if all cells are a permutation of \(1..n^2\), each row and column sums to \(\tfrac{n(n^2+1)}{2}\) (15 for a 3 × 3 grid)."))
P.dq(16, "What is the total number of coins in all the boxes in the 3rd row?", ["36", "30", "15", "45"], "MCQ", "4", "Easy",
 "All nine averages are 1–9, so the total is fixed.", steps(("Total", p(r"\(3 \times (1 + \dots + 9) = 135\); three equal rows ⇒ \(45\) each."))) + final(r"\(45\) — option 4"),
 [("1", "Not a third of 135."), ("2", "Not a third of 135."), ("3", "15 is the sum of averages, not coins.")])
P.dq(17, "How many boxes have at least one sack containing 9 coins?", ["3", "8", "5", "4"], "MCQ", "3", "Medium", "Check the final grid for 9s.",
 steps(("Count", p("(3, 9, 9), (1, 2, 9), (9, 9, 9), (7, 8, 9), (1, 8, 9)."))) + final(r"\(5\) — option 3"),
 [("1", "Too few."), ("2", "Too many."), ("4", "Misses one; check (1, 8, 9).")])
P.dq(18, "For how many boxes are the average and median of the numbers of coins contained in the three sacks in that box the same?", [], "TITA", "4", "Medium",
 "Compare each box’s middle value with its average.", steps(("Check", p("(1, 2, 3), (9, 9, 9), (7, 8, 9), (1, 1, 1)."))) + final(r"\(4\)"))
P.dq(19, "How many sacks have exactly one coin?", [], "TITA", "9", "Medium", "Count the 1s across the grid.",
 steps(("Count", p(r"\((1, 1, 7)\): 2, \((1, 6, 8)\): 1, \((1, 2, 9)\): 1, \((1, 2, 3)\): 1, \((1, 8, 9)\): 1, \((1, 1, 1)\): 3."))) + final(r"\(9\)"))
P.dq(20, "In how many boxes do all three sacks contain different numbers of coins?", [], "TITA", "5", "Medium", "Look for boxes with no repeated number.",
 steps(("Check", p("(1, 6, 8), (1, 2, 9), (1, 2, 3), (7, 8, 9), (1, 8, 9)."))) + final(r"\(5\)"))
