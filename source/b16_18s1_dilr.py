# -*- coding: utf-8 -*-
# Batch 16 — CAT 2018 Slot 1: DILR sets 1–8 (Q1–32, exam order).
from fmt import steps, final, trap, why, table, p
from b16_18s1 import P

# ---------------- Set 1: Majors and minors ----------------
P.dilr_set(1, "Set 1 — Eight students, three institutes", "Answer the questions on the basis of the following information.",
 p("Adriana, Bandita, Chitra, and Daisy are four female students, and Amit, Barun, Chetan, and Deb are four male students. Each of them studies in one of three institutes - X, Y, and Z. Each student majors in one subject among Marketing, Operations, and Finance, and minors in a different one among these three subjects. The following facts are known about the eight students:") +
 "<ol><li>Three students are from X, three are from Y, and the remaining two students, both female, are from Z.</li><li>Both the male students from Y minor in Finance, while the female student from Y majors in Operations.</li><li>Only one male student majors in Operations, while three female students minor in Marketing.</li><li>One female and two male students major in Finance.</li><li>Adriana and Deb are from the same institute. Daisy and Amit are from the same institute.</li><li>Barun is from Y and majors in Operations. Chetan is from X and majors in Finance.</li><li>Daisy minors in Operations.</li></ol>",
 "DILR::LR::Analytical_Reasoning",
 steps(("Institutes", p("Y has two men and one woman, X two men and one woman, Z two women. Deb and Amit can’t be in Z, so Adriana and Daisy aren’t either: Z is Bandita and Chitra.")),
       ("Who is in Y", p("The woman in Y majors in Operations, and Daisy minors in it, so she isn’t that woman. So Adriana and Deb are in Y with Barun; Daisy and Amit are in X with Chetan.")),
       ("Subjects", p("Deb (Y) minors in Finance, so he can’t major in it. The second male Finance major is Amit, and Deb majors in Marketing. Adriana majors in Operations; Adriana, Bandita and Chitra minor in Marketing."))) +
 final("Institutes are fixed; one woman’s Finance major is open."),
 p("Place people in institutes first; fact 2 then pins down Y."),
 p("<b>Grouping puzzles:</b> ‘same institute’ pairs and size limits settle most of the placement quickly."))
P.dq(1, "Who are the students from the institute Z?", ["Chitra and Daisy", "Adriana and Bandita", "Bandita and Chitra", "Adriana and Daisy"], "MCQ", "3", "Medium",
 "Adriana and Daisy each share an institute with a man.",
 steps(("From the set solution", p("Bandita and Chitra."))) + final("Option 3"),
 [("1", "Daisy is with Amit."), ("2", "Adriana is with Deb."), ("4", "Both are paired with men.")])
P.dq(2, "Which subject does Deb minor in?", ["Operations", "Finance", "Marketing", "Cannot be determined uniquely from the given information"], "MCQ", "2", "Medium",
 "Deb is in Y.",
 steps(("From the set solution", p("Both men in Y minor in Finance."))) + final("Finance, option 2"),
 [("1", "He minors in Finance."), ("3", "He majors in Marketing."), ("4", "It is fixed.")])
P.dq(3, "Which subject does Amit major in?", ["Marketing", "Operations", "Cannot be determined uniquely from the given information", "Finance"], "MCQ", "4", "Medium",
 "Two men major in Finance; Deb can’t be one.",
 steps(("From the set solution", p("Chetan and Amit."))) + final("Finance, option 4"),
 [("1", "That is Deb."), ("2", "Only Barun."), ("3", "It is fixed.")])
P.dq(4, "If Chitra majors in Finance, which subject does Bandita major in?", ["Finance", "Cannot be determined uniquely from the given information", "Operations", "Marketing"], "MCQ", "3", "Medium",
 "Only one woman majors in Finance, and Bandita minors in Marketing.",
 steps(("Working it through", p("Bandita can’t major in Finance (Chitra has it) or Marketing (her minor)."))) + final("Operations, option 3"),
 [("1", "Chitra is the woman in Finance."), ("2", "It follows."), ("4", "Her minor.")])

# ---------------- Set 2: ATM ----------------
P.dilr_set(2, "Set 2 — An ATM that pays ₹5000", "Answer the questions on the basis of the following information.",
 p("An ATM dispenses exactly ₹5000 per withdrawal using 100, 200 and 500 rupee notes. The ATM requires every customer to give her preference for one of the three denominations of notes. It then dispenses notes such that the number of notes of the customer’s preferred denomination exceeds the total number of other denominations dispensed to her."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("The equation", p("With a, b, c notes of 500, 200, 100: 5a + 2b + c = 50, and the preferred count is more than the other two together.")),
       ("Useful minimums", p("A 500-preferrer needs at least 8 notes of 500. Within 20 notes, a 200-preferrer needs at least 4 of 500 (4, 14, 2), and a 100-preferrer at least 7 (7, 2, 11)."))) +
 final("Each question is a small search over a, b, c."),
 p("Write the equation once; each question is an optimisation on it."),
 p("<b>Note-counting puzzles:</b> fix the big denomination first; the rest follow."))
P.dq(5, "In how many different ways can the ATM serve a customer who gives 500 rupee notes as her preference?", [], "TITA", "7", "Medium",
 "a > b + c with 5a + 2b + c = 50.",
 steps(("Listing", p("a = 10: (0, 0). a = 9: (2, 1), (1, 3), (0, 5). a = 8: (5, 0), (4, 2), (3, 4). Total 7."))) + final(r"\(7\)"))
P.dq(6, "If the ATM could serve only 10 customers with a stock of fifty 500 rupee notes and a sufficient number of notes of other denominations, what is the maximum number of customers among these 10 who could have given 500 rupee notes as their preferences?", [], "TITA", "6", "Medium",
 "Each 500-preferrer needs at least 8 of them.",
 steps(("Count", p("6 × 8 = 48 notes; 7 would need 56. The other four take no 500s (they prefer 100 or 200 with enough small notes)."))) + final(r"\(6\)"))
P.dq(7, "What is the maximum number of customers that the ATM can serve with a stock of fifty 500 rupee notes and a sufficient number of notes of other denominations, if all the customers are to be served with at most 20 notes per withdrawal?", ["12", "10", "13", "16"], "MCQ", "1", "Hard",
 "With 20 notes at most, everyone needs some 500s. Who needs the fewest?",
 steps(("Fewest 500s", p("200-preferrers: 4 notes of 500, 14 of 200, 2 of 100. 100-preferrers need 7, 500-preferrers 8.")),
       ("Count", p("50 ÷ 4 = 12."))) + final("12, option 1"),
 [("2", "Not the maximum."), ("3", "Would need 52 notes."), ("4", "Would need 64 notes.")])
P.dq(8, "What is the number of 500 rupee notes required to serve 50 customers with 500 rupee notes as their preferences and another 50 customers with 100 rupee notes as their preferences, if the total number of notes to be dispensed is the smallest possible?", ["900", "800", "750", "1400"], "MCQ", "1", "Hard",
 "Fewest notes means as many 500s as allowed.",
 steps(("500-preferrers", p("Ten notes of 500 each.")),
       ("100-preferrers", p("Notes = 50 − 4a − b, smallest with a = 8, b = 0, c = 10: 18 notes.")),
       ("Total 500s", p("50 × 10 + 50 × 8 = 900."))) + final("900, option 1"),
 [("2", "Doesn’t fit."), ("3", "Doesn’t fit."), ("4", "Doesn’t fit.")])

# ---------------- Set 3: Matrix ----------------
P.dilr_set(3, "Set 3 — No two neighbours alike", "Answer the questions on the basis of the following information.",
 p("You are given an n × n square matrix to be filled with numerals so that no two adjacent cells have the same numeral.") +
 p("Two cells are called adjacent if they touch each other horizontally, vertically or diagonally. So, a cell in one of the four corners has three cells adjacent to it, and a cell in the first or last row or column which is not in the corner has five cells adjacent to it. Any other cell has eight cells adjacent to it."),
 "DILR::LR::Puzzles",
 steps(("Any 2 × 2 block", p("Its four cells all touch each other, so they need four different numerals.")),
       ("Four is enough", p("Repeat the block 1 2 / 3 4 across the grid: same numerals are always two steps apart."))) +
 final("Four numerals for any n ≥ 2."),
 p("Look at the smallest block where every cell touches every other."),
 p("<b>Grid colouring:</b> the largest group of mutually adjacent cells gives the lower bound; a repeating tile often meets it."))
P.dq(9, "What is the minimum number of different numerals needed to fill a 3 × 3 square matrix?", [], "TITA", "4", "Easy",
 "Look at any 2 × 2 corner.",
 steps(("From the set solution", p("Four."))) + final(r"\(4\)"))
P.dq(10, "What is the minimum number of different numerals needed to fill a 5 × 5 square matrix?", [], "TITA", "4", "Easy",
 "The repeating 2 × 2 tile works at any size.",
 steps(("From the set solution", p("Four."))) + final(r"\(4\)"))
P.dq(11, "Suppose you are allowed to make one mistake, that is, one pair of adjacent cells can have the same numeral. What is the minimum number of different numerals required to fill a 5 × 5 matrix?", ["4", "16", "9", "25"], "MCQ", "1", "Medium",
 "One mistake can fix at most two of the sixteen 2 × 2 blocks.",
 steps(("Still four", p("Every other 2 × 2 block still needs four numerals."))) + final("4, option 1"),
 [("2", "Far too many."), ("3", "Far too many."), ("4", "Far too many.")])
P.dq(12, "Suppose that all the cells adjacent to any particular cell must have different numerals. What is the minimum number of different numerals needed to fill a 5 × 5 square matrix?", ["25", "4", "16", "9"], "MCQ", "4", "Hard",
 "Every 3 × 3 block is the neighbourhood of its centre.",
 steps(("Lower bound", p("All nine cells of any 3 × 3 block touch its centre or are the centre, so they must all differ.")),
       ("Nine is enough", p("Repeat a 3 × 3 tile of nine numerals: equal numerals are then three steps apart."))) + final("9, option 4"),
 [("1", "Not enough for a 3 × 3 block."), ("2", "More than needed."), ("3", "More than needed.")])

# ---------------- Set 4: Petrol pumps ----------------
P.dilr_set(4, "Set 4 — Contamination at twenty pumps", "Answer the questions on the basis of the following information.",
 p("Fuel contamination levels at each of 20 petrol pumps P<sub>1</sub>, P<sub>2</sub>, …, P<sub>20</sub> were recorded as either high, medium, or low.") +
 "<ol><li>Contamination levels at three pumps among P<sub>1</sub>–P<sub>5</sub> were recorded as high.</li><li>P<sub>6</sub> was the only pump among P<sub>1</sub>–P<sub>10</sub> where the contamination level was recorded as low.</li><li>P<sub>7</sub> and P<sub>8</sub> were the only two consecutively numbered pumps where the same levels of contamination were recorded.</li><li>High contamination levels were not recorded at any of the pumps P<sub>16</sub>–P<sub>20</sub>.</li><li>The number of pumps where high contamination levels were recorded was twice the number of pumps where low contamination levels were recorded.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("P1–P10", p("Three highs in P1–P5 with no two neighbours alike: H M H M H. P6 is L. P7 = P8 and neither is L: both H. Then P9 M, P10 H.")),
       ("P11–P20", p("Neighbours always differ, and no H after P15. Counting H against L (H = 2L) leaves six possibilities.") +
       table(["", "P11–P15", "P16–P20"], [["a", "M H M H M", "L M L M L"], ["b", "M H M H L", "M L M L M"], ["c", "M H M L H", "M L M L M"], ["d", "M H L M H", "M L M L M"], ["e", "M L H M H", "M L M L M"], ["f", "L M H M H", "M L M L M"]]))) +
 final("8 highs, 4 lows and 8 mediums in every case."),
 p("Fill P1–P10 first; it is forced."),
 p("<b>Sequence constraints:</b> ‘no two neighbours alike’ plus a count condition usually leaves only a handful of patterns."))
P.dq(13, "Which of the following MUST be true?", ["The contamination level at P<sub>20</sub> was recorded as medium.", "The contamination level at P<sub>13</sub> was recorded as low.", "The contamination level at P<sub>12</sub> was recorded as high.", "The contamination level at P<sub>10</sub> was recorded as high."], "MCQ", "4", "Medium",
 "P1–P10 is forced.",
 steps(("From the set solution", p("P10 is always H."))) + final("Option 4"),
 [("1", "P20 can be L."), ("2", "Not always."), ("3", "Not always.")])
P.dq(14, "What best can be said about the number of pumps at which the contamination levels were recorded as medium?", ["At least 8", "More than 4", "Exactly 8", "At most 9"], "MCQ", "3", "Medium",
 "Count M in each pattern.",
 steps(("From the set solution", p("Always 8."))) + final("Option 3"),
 [("1", "True but not the best."), ("2", "True but not the best."), ("4", "True but not the best.")])
P.dq(15, "If the contamination level at P<sub>11</sub> was recorded as low, then which of the following MUST be true?", ["The contamination level at P<sub>12</sub> was recorded as high.", "The contamination level at P<sub>15</sub> was recorded as medium.", "The contamination level at P<sub>18</sub> was recorded as low.", "The contamination level at P<sub>14</sub> was recorded as medium."], "MCQ", "4", "Medium",
 "Only pattern f starts P11 with L.",
 steps(("Pattern f", p("L M H M H, then M L M L M. P14 is M."))) + final("Option 4"),
 [("1", "P12 is M."), ("2", "P15 is H."), ("3", "P18 is M.")])
P.dq(16, "If contamination level at P<sub>15</sub> was recorded as medium, then which of the following MUST be FALSE?", ["Contamination levels at P<sub>13</sub> and P<sub>17</sub> were recorded as the same.", "Contamination levels at P<sub>11</sub> and P<sub>16</sub> were recorded as the same.", "Contamination level at P<sub>14</sub> was recorded to be higher than that at P<sub>15</sub>.", "Contamination levels at P<sub>10</sub> and P<sub>14</sub> were recorded as the same."], "MCQ", "2", "Medium",
 "Only pattern a has P15 = M.",
 steps(("Pattern a", p("M H M H M, then L M L M L. P11 is M and P16 is L."))) + final("Option 2"),
 [("1", "Both M."), ("3", "H above M: true."), ("4", "Both H.")])

# ---------------- Set 5: LED sales ----------------
SALES = table(["Month", "2016", "2017"],
              [["January", "60", "120"], ["February", "60", "100"], ["March", "60", "160"], ["<b>Q1</b>", "—", "—"],
               ["April", "60", "60"], ["May", "—", "75"], ["June", "—", "65"], ["<b>Q2</b>", "150", "—"],
               ["July", "75", "60"], ["August", "120", "—"], ["September", "55", "70"], ["<b>Q3</b>", "—", "220"],
               ["October", "100", "150"], ["November", "—", "170"], ["December", "—", "—"], ["<b>Q4</b>", "360", "500"]])
P.dilr_set(5, "Set 5 — Monthly sales of LED televisions", "Answer the questions on the basis of the following information.",
 p("The multi-layered pie-chart below shows the sales of LED television sets for a big retail electronics outlet during 2016 and 2017. The outer layer shows the monthly sales during this period, with each label showing the month followed by sales figure of that month. For some months, the sales figures are not given in the chart. The middle-layer shows quarter-wise aggregate sales figures (in some cases, aggregate quarter-wise sales numbers are not given next to the quarter). The innermost layer shows annual sales. It is known that the sales figures during the three months of the second quarter (April, May, June) of 2016 form an arithmetic progression, as do the three monthly sales figures in the fourth quarter (October, November, December) of that year.") +
 p("<i>The figures shown in the chart, as a table (— where the chart gives no figure):</i>") + SALES,
 "DILR::DI::Graphs_and_Charts",
 steps(("2016", p("Q2: 60 + May + June = 150 in an AP, so 60, 50, 40. Q4: 100 + Nov + Dec = 360 in an AP, so 100, 120, 140. Q1 = 180, Q3 = 250.")),
       ("2017", p("Q1 = 380, Q2 = 200, August = 220 − 130 = 90, December = 500 − 320 = 180."))) +
 final("Every month and quarter is now known."),
 p("Fill the gaps with the AP facts and quarter totals first."),
 p("<b>Partial charts:</b> use totals to recover missing parts before answering anything."))
P.dq(17, "What is the percentage increase in sales in December 2017 as compared to the sales in December 2016?", ["38.46", "22.22", "28.57", "50.00"], "MCQ", "3", "Medium",
 "December 2016 comes from the AP.",
 steps(("From the set solution", p("140 → 180: 40 ÷ 140 ≈ 28.57%."))) + final("Option 3"),
 [("1", "Wrong base."), ("2", "Uses 180 as the base."), ("4", "Wrong figures.")])
P.dq(18, "In which quarter of 2017 was the percentage increase in sales from the same quarter of 2016 the highest?", ["Q<sub>2</sub>", "Q<sub>1</sub>", "Q<sub>4</sub>", "Q<sub>3</sub>"], "MCQ", "2", "Medium",
 "Compare 2017 and 2016 quarter by quarter.",
 steps(("Changes", p("Q1 180 → 380 (+111%). Q2 150 → 200. Q3 250 → 220 (down). Q4 360 → 500."))) + final("Q1, option 2"),
 [("1", "+33%."), ("3", "+39%."), ("4", "A fall.")])
P.dq(19, "During which quarter was the percentage decrease in sales from the previous quarter’s sales the highest?", ["Q<sub>2</sub> of 2017", "Q<sub>4</sub> of 2017", "Q<sub>2</sub> of 2016", "Q<sub>1</sub> of 2017"], "MCQ", "1", "Medium",
 "Only falls count.",
 steps(("Falls", p("2016 Q1 → Q2: 180 → 150 (−17%). 2017 Q1 → Q2: 380 → 200 (−47%)."))) + final("Q2 of 2017, option 1"),
 [("2", "A rise."), ("3", "A smaller fall."), ("4", "A rise.")])
P.dq(20, "During which month was the percentage increase in sales from the previous month’s sales the highest?", ["March of 2017", "October of 2017", "March of 2016", "October of 2016"], "MCQ", "2", "Medium",
 "Compare each with the month before.",
 steps(("Rises", p("March 2017: 100 → 160 (60%). October 2017: 70 → 150 (114%). March 2016: no change. October 2016: 55 → 100 (82%)."))) + final("October 2017, option 2"),
 [("1", "60%."), ("3", "No change."), ("4", "82%.")])

# ---------------- Set 6: Committees ----------------
P.dilr_set(6, "Set 6 — Three committees of twenty-four", "Answer the questions on the basis of the following information.",
 p("Twenty four people are part of three committees which are to look at research, teaching, and administration respectively. No two committees have any member in common. No two committees are of the same size. Each committee has three types of people: bureaucrats, educationalists, and politicians, with at least one from each of the three types in each committee. The following facts are also known about the committees:") +
 "<ol><li>The numbers of bureaucrats in the research and teaching committees are equal, while the number of bureaucrats in the research committee is 75% of the number of bureaucrats in the administration committee.</li><li>The number of educationalists in the teaching committee is less than the number of educationalists in the research committee. The number of educationalists in the research committee is the average of the numbers of educationalists in the other two committees.</li><li>60% of the politicians are in the administration committee, and 20% are in the teaching committee.</li></ol>",
 "DILR::LR::Analytical_Reasoning",
 steps(("Forms", p("Bureaucrats 3k, 3k, 4k. Politicians 1, 1, 3 for every 5. Educationalists form an AP with teaching smallest.")),
       ("Totals", p("Only k = 1 and 5 politicians fit 24 people, leaving 9 educationalists: teaching, research, admin = 1, 3, 5 or 2, 3, 4.") +
       table(["", "Bureaucrats", "Educationalists", "Politicians", "Size"], [["Research", "3", "3", "1", "7"], ["Teaching", "3", "1 or 2", "1", "5 or 6"], ["Administration", "4", "5 or 4", "3", "12 or 11"]]))) +
 final("Two cases."),
 p("Write each type in terms of one unknown, then use the total of 24."),
 p("<b>Percentages of small groups:</b> 60% and 20% of politicians force a multiple of 5."))
P.dq(21, "Based on the given information, which of the following statements MUST be FALSE?", ["In the teaching committee the number of educationalists is equal to the number of politicians", "In the administration committee the number of bureaucrats is equal to the number of educationalists", "The size of the research committee is less than the size of the teaching committee", "The size of the research committee is less than the size of the administration committee"], "MCQ", "3", "Medium",
 "Research has 7; teaching 5 or 6.",
 steps(("From the set solution", p("Research is always bigger than teaching."))) + final("Option 3"),
 [("1", "True in the first case."), ("2", "True in the second case."), ("4", "Always true.")])
P.dq(22, "What is the number of bureaucrats in the administration committee?", [], "TITA", "4", "Medium",
 "4k with k = 1.",
 steps(("From the set solution", p("4."))) + final(r"\(4\)"))
P.dq(23, "What is the number of educationalists in the research committee?", [], "TITA", "3", "Medium",
 "The middle of the AP.",
 steps(("From the set solution", p("3."))) + final(r"\(3\)"))
P.dq(24, "Which of the following CANNOT be determined uniquely based on the given information?", ["The size of the teaching committee", "The size of the research committee", "The total number of bureaucrats in the three committees", "The total number of educationalists in the three committees"], "MCQ", "1", "Medium",
 "Which number differs between the two cases?",
 steps(("From the set solution", p("Teaching is 5 or 6."))) + final("Option 1"),
 [("2", "Always 7."), ("3", "Always 10."), ("4", "Always 9.")])

# ---------------- Set 7: Satellites ----------------
P.dilr_set(7, "Set 7 — 1600 satellites", "Answer the questions on the basis of the following information.",
 p("1600 satellites were sent up by a country for several purposes. The purposes are classified as broadcasting (B), communication (C), surveillance (S), and others (O). A satellite can serve multiple purposes; however a satellite serving either B, or C, or S does not serve O. The following facts are known about the satellites:") +
 "<ol><li>The numbers of satellites serving B, C, and S (though may be not exclusively) are in the ratio 2 : 1 : 1.</li><li>The number of satellites serving all three of B, C, and S is 100.</li><li>The number of satellites exclusively serving C is the same as the number of satellites exclusively serving S. This number is 30% of the number of satellites exclusively serving B.</li><li>The number of satellites serving O is the same as the number of satellites serving both C and S but not B.</li></ol>",
 "DILR::LR::Venn_Diagrams",
 steps(("Unknowns", p("Exclusive B = b, exclusive C = exclusive S = 0.3b, C and S only = O = y. C = S forces B and C only = B and S only = x.")),
       ("Equations", p("B = 2C gives b = 5y + 250. The total of 1600 gives x = 550 − 5y.")),
       ("Ranges", p("x ≥ 0 means y ≤ 110. C = S = 725 − 2.5y, between 450 and 725."))) +
 final("Everything depends on y, between 0 and 110."),
 p("Name the regions, write the four facts as equations, and keep one unknown."),
 p("<b>Venn with a ratio:</b> express everything through one region and read off ranges."))
P.dq(25, "What best can be said about the number of satellites serving C?", ["Must be at least 100", "Cannot be more than 800", "Must be between 450 and 725", "Must be between 400 and 800"], "MCQ", "3", "Hard",
 "C = 725 − 2.5y with 0 ≤ y ≤ 110.",
 steps(("From the set solution", p("Between 450 and 725."))) + final("Option 3"),
 [("1", "True but weak."), ("2", "True but weak."), ("4", "True but weaker.")])
P.dq(26, "What is the minimum possible number of satellites serving B exclusively?", ["250", "100", "500", "200"], "MCQ", "1", "Hard",
 "b = 5y + 250.",
 steps(("From the set solution", p("Smallest at y = 0: 250."))) + final("250, option 1"),
 [("2", "Below the minimum."), ("3", "Not the minimum."), ("4", "Below the minimum.")])
P.dq(27, "If at least 100 of the 1600 satellites were serving O, what can be said about the number of satellites serving S?", ["At most 475", "Exactly 475", "No conclusion is possible based on the given information", "At least 475"], "MCQ", "1", "Hard",
 "y is now between 100 and 110.",
 steps(("From the set solution", p("S = 725 − 2.5y, between 450 and 475."))) + final("Option 1"),
 [("2", "Only at y = 100."), ("3", "A range follows."), ("4", "Reversed.")])
P.dq(28, "If the number of satellites serving at least two among B, C, and S is 1200, which of the following MUST be FALSE?", ["The number of satellites serving B exclusively is exactly 250", "The number of satellites serving B is more than 1000", "The number of satellites serving C cannot be uniquely determined", "All 1600 satellites serve B or C or S"], "MCQ", "3", "Hard",
 "At least two: 2x + y + 100.",
 steps(("Solve", p("1200 − 9y = 1200, so y = 0. Then b = 250, x = 550, B = 1450, C = 725 and O = 0."))) + final("Option 3"),
 [("1", "True."), ("2", "True: 1450."), ("4", "True: O = 0.")])

# ---------------- Set 8: Written test ----------------
MARKS = table(["Candidate", "DI", "WE", "GA"],
              [["Ajay", "8", "", "16"], ["Bala", "", "9", "11"], ["Chetna", "19", "4", "12"], ["Danish", "8", "15", ""], ["Ester", "12", "18", "16"],
               ["Falak", "15", "7", "10"], ["Geeta", "14", "", "6"], ["Harini", "5", "", ""], ["Indu", "", "8", ""], ["Jatin", "", "16", "14"]])
P.dilr_set(8, "Set 8 — A recruitment test", "Answer the questions on the basis of the following information.",
 p("A company administers a written test comprising of three sections of 20 marks each - Data Interpretation (DI), Written English (WE) and General Awareness (GA), for recruitment. A composite score for a candidate (out of 80) is calculated by doubling her marks in DI and adding it to the sum of her marks in the other two sections. Candidates who score less than 70% marks in two or more sections are disqualified. From among the rest, the four with the highest composite scores are recruited. If four or less candidates qualify, all who qualify are recruited.") +
 p("Ten candidates appeared for the written test. Their marks in the test are given in the table below. Some marks in the table are missing, but the following facts are known:") +
 "<ol><li>No two candidates had the same composite score.</li><li>Ajay was the unique highest scorer in WE.</li><li>Among the four recruited, Geeta had the lowest composite score.</li><li>Indu was recruited.</li><li>Danish, Harini, and Indu had scored the same marks in GA.</li><li>Indu and Jatin both scored 100% in exactly one section and Jatin’s composite score was 10 more than Indu’s.</li></ol>" +
 p("<b>Marks out of 20</b>") + MARKS,
 "DILR::DI::Data_Tabulation",
 steps(("Who qualifies", p("70% is 14. Chetna, Falak and Bala fail two sections. Indu must have DI and GA at 14 or more; Geeta must have WE at 14 or more.")),
       ("Indu and Jatin", p("Jatin’s 100% can only be DI: composite 40 + 16 + 14 = 70. Indu: 60. If Indu’s 100% were DI, her GA would be 12 and she’d fail two sections, so GA = 20 and DI = 16. Danish and Harini also have GA 20.")),
       ("Ajay and Geeta", p("Ester 58, Danish 51. Geeta must beat Ajay. Ajay’s WE is 19 or 20; 19 ties him with Danish at 51, so 20 (composite 52). Geeta then needs WE 19: 53.") +
       table(["", "DI", "WE", "GA", "Composite"], [["Jatin", "20", "16", "14", "70"], ["Indu", "16", "8", "20", "60"], ["Ester", "12", "18", "16", "58"], ["Geeta", "14", "19", "6", "53"], ["Ajay", "8", "20", "16", "52"], ["Danish", "8", "15", "20", "51"]]))) +
 final("Recruited: Jatin, Indu, Ester, Geeta. Bala’s DI and Harini’s WE stay open."),
 p("Disqualify first; then Indu and Jatin’s 100% clue fixes the top."),
 p("<b>Missing-cell tables:</b> eliminations (here, disqualification) usually shrink the field before any arithmetic."))
P.dq(29, "Which of the following statements MUST be true?<br>1. Jatin’s composite score was more than that of Danish.<br>2. Indu scored less than Chetna in DI.<br>3. Jatin scored more than Indu in GA.", ["Both 2 and 3", "Only 1", "Only 2", "Both 1 and 2"], "MCQ", "4", "Hard",
 "Check each against the table.",
 steps(("From the set solution", p("70 > 51, and 16 < 19. Jatin’s GA (14) is less than Indu’s (20)."))) + final("Option 4"),
 [("1", "3 is false."), ("2", "2 also holds."), ("3", "1 also holds.")])
P.dq(30, "Which of the following statements MUST be FALSE?", ["Bala scored same as Jatin in DI", "Harini’s composite score was less than that of Falak", "Bala’s composite score was less than that of Ester", "Chetna scored more than Bala in DI"], "MCQ", "1", "Hard",
 "What would Bala’s composite be with DI 20?",
 steps(("Bala at 20", p("40 + 9 + 11 = 60, the same as Indu. Not allowed."))) + final("Option 1"),
 [("2", "Possible if Harini’s WE is low."), ("3", "Possible."), ("4", "Possible.")])
P.dq(31, "If all the candidates except Ajay and Danish had different marks in DI, and Bala’s composite score was less than Chetna’s composite score, then what is the maximum marks that Bala could have scored in DI?", [], "TITA", "13", "Hard",
 "Chetna’s composite is 54.",
 steps(("Bound", p("2 × DI + 20 < 54, so DI ≤ 16.")),
       ("Distinct", p("16, 15, 14 and 12 are taken. 13 is free."))) + final(r"\(13\)"))
P.dq(32, "If all the candidates scored different marks in WE then what is the maximum marks that Harini could have scored in WE?", [], "TITA", "14", "Hard",
 "WE values taken: 20, 19, 18, 16, 15, 9, 8, 7, 4. And watch composites.",
 steps(("Free values", p("17 is free, but gives Harini 10 + 17 + 20 = 47, Falak’s composite. 14 is the next free value: 44."))) + final(r"\(14\)"))
