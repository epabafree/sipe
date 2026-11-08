# -*- coding: utf-8 -*-
# Simp Mock 2 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_02 import P
import m25_02_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Film releases (Q1–4) ----------------
REL = table(["Week", "Actor", "Actress"], [["1", "Jiten", "Nupur"], ["2", "Amal", "Swati"], ["3", "Sohan", "Mitali"], ["4", "Dinesh", "Shreya"], ["5", "Ankit", "Jaya"]])
P.dilr_set(1, "Set 1 — Five festival releases", DIR,
 p("Durga Puja and Diwali are the two major festivals when film producers try to release their movies in West Bengal. Five actors namely Amal, Ankit, Dinesh, Jiten and Sohan played the role of lead actors in five new movies that will be released this year in and around these two festivals. Each of these five actors acted in only one movie. "
   "The five actresses namely Jaya, Mitali, Nupur, Shreya and Swati played the roles of lead actresses in these five movies against the previously mentioned lead actors. Each of these five actresses acted in only one movie. Each movie has positions of only one lead actor and one lead actress. "
   "These five movies will be released in five consecutive weeks, i.e., one movie in each week. No other movie will be released during these five weeks.") +
 p("Further, the following facts are known about these five movies:") +
 "<ol><li>Jaya’s movie will be released after Dinesh’s movie.</li><li>Release dates of exactly two movies have been scheduled between the movies of Amal and Ankit.</li>"
 "<li>Nupur’s movie will be released before Swati’s movie. Swati’s movie will be released before Shreya’s movie but not in consecutive weeks.</li>"
 "<li>Exactly one movie will be released between the movies of Jiten and Mitali, where Mitali’s movie will be released later.</li>"
 "<li>The movie of Dinesh will be released in the week immediately preceding the week in which the movie of Ankit will be released.</li><li>Nupur and Dinesh did not work in the same movie.</li></ol>",
 "DILR::LR::Scheduling",
 steps(("Actors first", p("Amal and Ankit are 3 weeks apart (weeks 1 & 4 or 2 & 5), and Dinesh is just before Ankit. If Ankit is in week 4, Dinesh is in 3 and Amal in 1. If Ankit is in 1, Dinesh has no slot. If Ankit is in 2, Amal is in 5 and Dinesh in 1. If Ankit is in 5, Amal is in 2 and Dinesh in 4.")),
       ("Actresses", p("Nupur < Swati < Shreya with a gap of at least one week between Swati and Shreya. Mitali is two weeks after Jiten. Jaya is after Dinesh.")),
       ("Testing", p("Only Ankit 5, Amal 2, Dinesh 4 survives: Jiten and Sohan take weeks 1 and 3; Mitali two after Jiten means Jiten 1, Mitali 3; Jaya after Dinesh means Jaya 5; then Nupur 1, Swati 2, Shreya 4 (not consecutive with Swati, and Nupur isn’t with Dinesh).") + REL)) +
 final("The schedule is unique."),
 p("Start with the tightest clue: Dinesh–Ankit adjacent plus Amal–Ankit three apart leaves only three cases."),
 p("<b>Linear scheduling:</b> place the pieces with fixed gaps first, then fill in."))
P.dq(1, "We assume that the first movie among these five movies will be released in week-1, the second movie will be released in week-2, and so on. What is the week number in which Jaya’s movie will be released?", [], "TITA", "5", "Medium",
 "Jaya must follow Dinesh, who is in week 4.", steps(("From the schedule", p("Jaya’s movie is in week 5, with Ankit."))) + final("5"))
P.dq(2, "The number of movies that will be released between the movies of Nupur and Dinesh is ________ .", [], "TITA", "2", "Medium",
 "Nupur is in week 1, Dinesh in week 4.", steps(("Count", p("Weeks 2 and 3 lie between: 2 movies."))) + final("2"))
P.dq(3, "Who played the role of lead actress in the movie in which the role of the lead actor was played by Jiten?", ["Nupur", "Swati", "Shreya", "Jaya"], "MCQ", "1", "Medium",
 "Jiten is in week 1.", steps(("Week 1", p("Jiten and Nupur."))) + final("Option 1"), [("2", "Swati is with Amal."), ("3", "Shreya is with Dinesh."), ("4", "Jaya is with Ankit.")])
P.dq(4, "Who played the role of lead actor in the movie in which the role of the lead actress was played by Jaya?", ["Amal", "Sohan", "Dinesh", "Ankit"], "MCQ", "4", "Medium",
 "Jaya is in week 5.", steps(("Week 5", p("Ankit and Jaya."))) + final("Option 4"), [("1", "Amal is in week 2."), ("2", "Sohan is in week 3."), ("3", "Dinesh is in week 4; Jaya comes after him.")])

# ---------------- Set 2: Candlesticks (Q5–8) ----------------
OHLC = p("Days are in January.") + table(["Day", "Open", "High", "Low", "Close"], [[d.split()[0], str(o), str(h), str(l), str(c)] for d, o, h, l, c in F.CANDLES])
P.dilr_set(2, "Set 2 — A share’s candlestick chart", DIR,
 p("The candlestick chart below represents the share prices of a pharmaceutical company over 10 different days. Each candle consists of two parts: a rectangular body, which can either be green or red in colour, and a vertical line segment (called ‘wick’) passing through the body of the candle. It may be possible that the top or bottom of the wick coincides with either the top or the bottom of the body of the candle, respectively.") +
 p("In a red candle, the top end of the body of the candle represents the opening value and the bottom end of the body of the candle represents the closing value of the share on a particular day. On the other hand, in a green candle, the bottom end of the body of the candle represents the opening value and the top end of the body of the candle represents the closing value of the share on a particular day. The top and bottom of the wick represent the highest and the lowest value of the share on a particular day respectively.") +
 F.CANDLE_FIG + p("All values are multiples of ₹5, except the high on 7th January, which is ₹1428."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Read every candle", p("Red: open at the top of the body, close at the bottom. Green: the other way round.") + OHLC)) + final("Open, high, low and close for all ten days."),
 p("Write the four values for each day first; every question is then arithmetic on the table."),
 p("<b>Candlesticks:</b> the body runs from open to close (colour tells the direction); the wick runs from low to high."))
P.dq(5, "Yogesh purchased 200 units of shares at the lowest value available on 7th January and sold all of them on 13th January at the closing value. Instead, if he had sold all the shares at the highest value of the day on 14th January, what would have been the difference in the profit/loss%?",
 [r"\(\tfrac{5}{14}\)", r"\(\tfrac{3}{7}\)", r"\(\tfrac{1}{2}\)", r"\(\tfrac{4}{7}\)"], "MCQ", "1", "Medium",
 "Buy at ₹1400. Compare selling at ₹1405 with selling at ₹1410.",
 steps(("Profits", p(r"At ₹1405: \(\tfrac{5}{1400}\) = \(\tfrac{5}{14}\%\). At ₹1410: \(\tfrac{10}{1400} = \tfrac{5}{7}\%\).")),
       ("Difference", p(r"\(\tfrac57 - \tfrac{5}{14} = \tfrac{5}{14}\) percentage points. (The number of shares doesn’t matter.)"))) + final(r"\(\tfrac{5}{14}\), option 1"),
 [("2", "Not the difference."), ("3", "Not the difference."), ("4", "Not the difference.")])
P.dq(6, "The Three Day Moving Average (TDMA) of a share price is the average of the three most recent closing values. Starting from 8th January, when did the TDMA become lowest in its value (in ₹) and what is the corresponding value?",
 [r"14th January, \(1358\tfrac13\)", r"15th January, \(1376\tfrac23\)", r"16th January, \(1368\tfrac13\)", r"16th January, \(1358\tfrac13\)"], "MCQ", "3", "Medium",
 "The three lowest closes are on 14th, 15th and 16th January.",
 steps(("Closes", p("14th 1375, 15th 1350, 16th 1380: the three lowest, and they are consecutive.")),
       ("TDMA on 16th", p(r"\(\tfrac{1375 + 1350 + 1380}{3} = 1368\tfrac13\). (15th: \(1376\tfrac23\); 17th: \(1383\tfrac13\).)"))) + final("Option 3"),
 [("1", "14th’s TDMA is (1410 + 1405 + 1375)/3 = 1396⅔."), ("2", "Higher than 16th’s."), ("4", "Right day, wrong value.")])
P.dq(7, "The number of instances in these ten days when the difference between the lowest value and highest value of each share for the day is more than 3% of the opening value of that day is _______.", [], "TITA", "5", "Medium",
 "3% of about 1,400 is about 42. Which days had a range above that?",
 steps(("Check each day", table(["Day", "Range", "3% of open", "More?"],
        [["6", "40", "42.9", "No"], ["7", "28", "42.3", "No"], ["8", "30", "42.9", "No"], ["9", "40", "43.5", "No"], ["10", "50", "43.2", "Yes"], ["13", "40", "42", "No"],
         ["14", "50", "42.15", "Yes"], ["15", "50", "41.1", "Yes"], ["16", "50", "40.5", "Yes"], ["17", "70", "41.7", "Yes"]]))) + final("5"))
P.dq(8, "Rama purchased 200 shares on 6th January at the opening value. She sold the first lot of 50 shares on 9th January at high value of the day, second lot of 50 shares on 13th January at low value of the day, third lot of 50 shares on 15th January at closing value of the day, and last lot of 50 shares on 17th January at high value of the day. How much loss or gain did she make through these transactions?",
 ["Loss of ₹4000", "Profit of ₹4000", "Loss of ₹3500", "Profit of ₹3500"], "MCQ", "3", "Medium",
 "Bought at ₹1430. Compare each sale price with 1430.",
 steps(("Per share", p("9th high 1460: +30. 13th low 1390: −40. 15th close 1350: −80. 17th high 1450: +20. Net −70 per lot share.")),
       ("Total", p("50 × (−70) = −3,500: a loss of ₹3,500."))) + final("Option 3"),
 [("1", "Slip in one of the four prices."), ("2", "Wrong direction."), ("4", "Wrong direction.")])

# ---------------- Set 3: Three currencies (Q9–13) ----------------
CUR = table(["Peno", "Dollam", "Rupay", "Units"], [["1", "17", "1", "19"], ["2", "14", "2", "18"], ["3", "11", "3", "17"], ["4", "8", "4", "16"], ["5", "5", "5", "15"], ["6", "2", "6", "14"]])
P.dilr_set(3, "Set 3 — Three currencies", DIR,
 p("Six persons namely P, Q, R, S, T and U have 3 types of currencies namely, Rupay, Dollam and Peno. Each one of them has at least one unit of each type of currency. 1 Peno is equal to 2.5 Dollam and 1 Dollam is equal to 2 Rupay. The total value of the units of the three currencies taken together with each person is equivalent to 20 Dollam.") +
 p("No two persons have an equal number of units of the same type of currency. Also, the sum of the number of units of the three types of currencies with each of them is a unique natural number. The individual who has the maximum units of Peno has the same number of units of Rupay as well. The sum of the number of units of the three currencies with each of them is less than 20."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("One equation", p("In Rupay: 1 Peno = 5 Rupay, 1 Dollam = 2 Rupay, and 20 Dollam = 40 Rupay. So \\(r + 2d + 5p = 40\\), with \\(r + d + p \\le 19\\).")),
       ("Peno counts", p("Six people with different Peno counts, all at least 1. With \\(p \\ge 8\\) there’s no room, so the counts are 1 to 7 less one value. With \\(p = 7\\), \\(r + 2d = 5\\) gives \\((r, d) = (1, 2)\\) or \\((3, 1)\\), neither with \\(r = 7\\); so the maximum isn’t 7 and the counts are 1 to 6, with the 6-Peno person holding 6 Rupay.")),
       ("Fill in from p = 1 upward", p("Units \\(= 40 - d - 4p\\), which must be below 20, and \\(r \\ge 1\\). For \\(p = 1\\) the only choice is \\(d = 17, r = 1\\) (19 units). For \\(p = 2\\): 13 or 14 Dollam; 13 would repeat 19 units, so 14 (2 Rupay, 18 units). For \\(p = 3\\): of 9–12 Dollam, only 11 avoids a used total or Rupay count (3 Rupay, 17 units). Likewise \\(p = 4\\): 8 Dollam; \\(p = 5\\): 5 Dollam; \\(p = 6\\): 2 Dollam with 6 Rupay.") + CUR)) +
 final("Each person holds k Peno, k Rupay and 20 − 3k Dollam, for k = 1 to 6."),
 p("Convert everything to the smallest unit: one linear equation, then use ‘all different’ to pin the values."),
 p("<b>Distinct values with a fixed sum:</b> when six different counts must fit a small range, the range itself is forced."))
P.dq(9, "What can be the maximum number of units of Peno currency that any person can have?", [], "TITA", "6", "Medium",
 "Can anyone have 7 Peno?", steps(("Check 7", p("7 Peno leaves 5 Rupay of value: (1 Rupay, 2 Dollam) or (3, 1). The top Peno holder must have equal Rupay, so 7 fails. The maximum is 6."))) + final("6"))
P.dq(10, "What can be the minimum sum of the number of units of the three currencies with any person?", [], "TITA", "14", "Medium",
 "Totals are 20 − k for k = 1 to 6.", steps(("Smallest", p("6 + 2 + 6 = 14."))) + final("14"))
P.dq(11, "The number of units of Dollam currency with the individual having 3 units of Peno currency is ________.", ["5", "7", "9", "11"], "MCQ", "4", "Medium",
 "Dollam = 20 − 3k.", steps(("k = 3", p("20 − 9 = 11."))) + final("11, option 4"), [("1", "That is the 5-Peno person."), ("2", "Not in the table."), ("3", "Not in the table.")])
P.dq(12, "The sum of the number of units of Dollam currency with the six persons taken together is ________.", ["54", "55", "56", "57"], "MCQ", "4", "Medium",
 "Add 17, 14, 11, 8, 5, 2.", steps(("Sum", p("17 + 14 + 11 + 8 + 5 + 2 = 57."))) + final("57, option 4"), [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])
P.dq(13, "The number of units of Peno currency with the individual having 2 units of Rupay currency is ________.", [], "TITA", "2", "Easy",
 "Everyone has equal Rupay and Peno.", steps(("Read off", p("2 Rupay goes with 2 Peno."))) + final("2"))

# ---------------- Set 4: Marks (Q14–18) ----------------
def fr(s): return f"\\({s}\\)"
T1 = table(["", "A", "B", "C", "D", "E"],
           [["Phy", fr(r"16\tfrac23"), fr(r"10\tfrac57"), fr(r"14\tfrac23"), "15", fr(r"20\tfrac56")], ["Che", fr(r"13\tfrac13"), "10", "12", "10", fr(r"16\tfrac23")],
            ["Mat", fr(r"23\tfrac13"), fr(r"19\tfrac27"), "16", fr(r"21\tfrac23"), fr(r"12\tfrac12")], ["His", fr(r"23\tfrac13"), fr(r"31\tfrac37"), fr(r"33\tfrac13"), fr(r"33\tfrac13"), fr(r"31\tfrac23")],
            ["Civ", fr(r"23\tfrac13"), fr(r"28\tfrac47"), "24", "20", fr(r"18\tfrac13")]])
T2 = table(["", "Phy", "Che", "Mat", "His", "Civ"],
           [["A", "20", "20", fr(r"23\tfrac13"), "14", fr(r"18\tfrac23")], ["B", "15", "17.5", "22.5", "22", fr(r"26\tfrac23")], ["C", "22", "22.5", "20", "25", "24"],
            ["D", "18", "15", fr(r"21\tfrac23"), "20", "16"], ["E", "25", "25", "12.5", "19", fr(r"14\tfrac23")]])
BASE = table(["", "Phy", "Che", "Mat", "His", "Civ"],
             [["A", "20", "16", "28", "28", "28"], ["B", "15", "14", "27", "44", "40"], ["C", "22", "18", "24", "50", "36"],
              ["D", "18", "12", "26", "40", "24"], ["E", "25", "20", "15", "38", "22"]]) + p("Totals: A 120, B 140, C 150, D 120, E 120 (all × t).")
P.dilr_set(4, "Set 4 — Marks in two tables", DIR,
 p("Five students named A, B, C, D and E appeared for an examination on five subjects, namely Physics, Chemistry, Mathematics, History and Civics. It is known that the maximum marks in Physics, Chemistry, History and Civics were multiples of 50.") +
 p("The following table shows the marks scored by each student in each subject, expressed as a percentage of the total marks scored by that student in all the five subjects.") + T1 +
 p("Interpretation of the table: out of the total marks scored by A in all the five subjects, \\(16\\tfrac23\\)% was scored in Physics. Other entries are to be similarly interpreted.") +
 p("The following table shows the marks scored by each student in each subject, expressed as a percentage of the sum of the marks scored by the five students in that subject.") + T2 +
 p("Interpretation of the table: out of the sum of the marks scored by the five students in Physics, 20% was scored by A. Other entries are to be similarly interpreted.") +
 p("It is known that no student scored full marks in Mathematics. However, at least one student scored full marks in each of the other four subjects. The marks scored by each student in each subject was a natural number."),
 "DILR::DI::Data_Tabulation",
 steps(("Link the tables through Physics", p("A student’s Physics mark is (row % of their total) and also (column % of the Physics total). If the Physics total is 100 units, A scored 20, so A’s total is \\(20 \\div 16\\tfrac23\\% = 120\\); B’s is \\(15 \\div 10\\tfrac57\\% = 140\\); C 150, D 120, E 120.")),
       ("Every mark", p("Multiply each student’s total by the first table’s percentages. Up to one common factor \\(t\\), the marks are:") + BASE),
       ("The factor t", p("Full marks are reached in Physics, Chemistry, History and Civics, so each subject’s maximum is the top score there: \\(25t, 20t, 50t, 40t\\). All must be multiples of 50, so \\(t\\) is a multiple of 10."))) +
 final("Marks = table × t, with t = 10, 20, 30, …"),
 p("Pick one subject total as a unit, get every student’s total, then fill the table; scaling conditions come last."),
 p("<b>Two percentage tables:</b> a cell is (row % × row total) and (column % × column total); equate them to link the totals."))
P.dq(14, "Which of the following is the highest?", ["Marks scored by A in Mathematics", "Marks scored by B in History", "Marks scored by B in Civics", "Marks scored by E in Chemistry"], "MCQ", "2", "Medium",
 "Compare in units of t.", steps(("Values", p("A Maths 28t, B History 44t, B Civics 40t, E Chemistry 20t."))) + final("Option 2"),
 [("1", "28t."), ("3", "40t."), ("4", "20t.")])
P.dq(15, "Which of the following can be the sum of marks scored by B and E in Mathematics?", ["105", "210", "315", "420"], "MCQ", "4", "Medium",
 "B + E in Maths = 42t, and t is a multiple of 10.", steps(("Possible values", p("42 × 10 = 420, 840, … Only 420 is listed."))) + final("420, option 4"),
 [("1", "Needs t = 2.5."), ("2", "Needs t = 5."), ("3", "Needs t = 7.5.")])
P.dq(16, "What is the ratio of the marks scored by E in Chemistry to the marks scored by C in Mathematics?", ["5 : 6", "6 : 5", "12 : 13", "13 : 12"], "MCQ", "1", "Medium",
 "Both scale with t.", steps(("Ratio", p("20t : 24t = 5 : 6."))) + final("Option 1"), [("2", "Upside down."), ("3", "Wrong cells."), ("4", "Wrong cells.")])
P.dq(17, "What can be the minimum value of the sum of maximum possible marks that can be scored in Physics, Chemistry, History and Civics?", ["1250", "1300", "1350", "1400"], "MCQ", "3", "Hard",
 "Maximum marks = top score in each of these four subjects.", steps(("With t = 10", p("250 + 200 + 500 + 400 = 1,350."))) + final("1350, option 3"),
 [("1", "Not achievable with t a multiple of 10."), ("2", "Not achievable."), ("4", "Possible only with other t; not the minimum.")])
P.dq(18, "What can be the minimum value of the sum of the marks that can be scored by student D in all the five subjects taken together?", ["1000", "1100", "1200", "1250"], "MCQ", "3", "Medium",
 "D’s total is 120t.", steps(("t = 10", p("120 × 10 = 1,200."))) + final("1200, option 3"),
 [("1", "Needs t below 10."), ("2", "Needs t below 10."), ("4", "Not a multiple of 120 × 10.")])

# ---------------- Set 5: Box cricket (Q19–22) ----------------
SCHED = table(["Day", "Matches"], [["1", "UR–SC, SW–KH, SW–KR"], ["2", "KH–SC, SS–UR, SS–KR"], ["3", "UR–KH, UR–KR, SC–SS"], ["4", "SW–SC, SW–SS, KH–KR"]])
P.dilr_set(5, "Set 5 — Box cricket", DIR,
 p("A neighbourhood association organised an underarm box cricket tournament for women, held over four days, with six women’s teams participating. The teams were: Kaushalya Hitters, Sumitra Warriors, Urmila Rangers, Shabri Chargers, Sita Strikers, and Kaikayi Royals. In the tournament, each team played one match against exactly four other teams. An equal number of matches were played each day.") +
 "<ol><li>Sumitra Warriors played two matches each on the 1st and the 4th days. Urmila Rangers played two matches on the 3rd day while Sita Strikers played two matches on the 2nd day. Other than these, no other team played two matches on any day.</li>"
 "<li>Urmila Rangers did not play any match on the 4th day while Sita Strikers did not play any match on the 1st day.</li><li>Urmila Rangers played with Shabri Chargers on the 1st day.</li><li>Kaushalya Hitters played with Shabri Chargers on the 2nd day.</li></ol>",
 "DILR::LR::Games_and_Tournaments",
 steps(("Count", p("Each team plays 4, so there are \\(6 \\times 4 \\div 2 = 12\\) matches, 3 a day. Each team skips exactly one opponent.")),
       ("Sumitra and Urmila", p("KH = Kaushalya, SW = Sumitra, UR = Urmila, SC = Shabri, SS = Sita, KR = Kaikayi. SW plays 2 on day 1 and 2 on day 4: all its 4 matches. UR plays SC on day 1, 2 matches on day 3, none on day 4, so one on day 2.")),
       ("Day by day", p("Day 1: UR–SC, and SW’s two must be against teams other than SS (SS doesn’t play day 1) and other than UR/SC (already playing): KH and KR. Day 2: KH–SC plus SS’s two, one of them against UR, the other against KR. Day 3: UR’s two (KH and KR) and the remaining SC–SS. Day 4: SW’s two (SC and SS) and KH–KR.") + SCHED)) +
 final("The whole schedule is fixed."),
 p("Teams that play twice on a day use up most of that day’s three matches; place them first."),
 p("<b>Round counts:</b> total matches = teams × games each ÷ 2; spread evenly over days."))
P.dq(19, "Kaushalya Hitters played against Kaikayi Royals on day _________ .", [], "TITA", "4", "Medium",
 "Check day 4’s third match.", steps(("Day 4", p("SW–SC, SW–SS and KH–KR."))) + final("4"))
P.dq(20, "For how many teams can we uniquely identify their opponent teams in all the matches they played?", ["3", "4", "5", "6"], "MCQ", "4", "Medium",
 "Is anything in the schedule left open?", steps(("All fixed", p("The schedule is unique, so all six teams’ opponents are known."))) + final("6, option 4"),
 [("1", "Every team is fixed."), ("2", "Every team is fixed."), ("3", "Every team is fixed.")])
P.dq(21, "Which of the following combinations of day and the pair of teams that played a match against each other on that day is correct?",
 ["Day 2 - Kaikayi Royals vs Kaushalya Hitters", "Day 3 - Urmila Rangers vs Sita Strikers", "Day 4 - Sumitra Warriors vs Shabri Chargers", "None of these"], "MCQ", "3", "Medium",
 "Check each against the schedule.", steps(("Check", p("KR–KH is on day 4; UR–SS is on day 2; SW–SC is on day 4. Option 3."))) + final("Option 3"),
 [("1", "That match is on day 4."), ("2", "That match is on day 2."), ("4", "Option 3 is correct.")])
P.dq(22, "On which day did Shabri Chargers play against Sita Strikers?", ["Day 1", "Day 2", "Day 3", "Day 4"], "MCQ", "3", "Medium",
 "Day 3’s third match.", steps(("Day 3", p("UR–KH, UR–KR and SC–SS."))) + final("Day 3, option 3"),
 [("1", "SS doesn’t play on day 1."), ("2", "SS plays UR and KR on day 2."), ("4", "SC plays SW on day 4.")])
