# -*- coding: utf-8 -*-
# Batch 6 — CAT 2022 Slot 2: DILR sets 1–4 (Q1–20, exam order).
from fmt import steps, final, why, table, p
from b6_22s2 import P

# ---------------- Set 1: TRICCEK salesmen ----------------
P.dilr_set(1, "Set 1 — Three salesmen over two days", "Read the instructions given and answer the questions that follow.",
 p("A few salesmen are employed to sell a product called TRICCEK among households in various housing complexes. On each day, a salesman is assigned to visit one housing complex. Once a salesman enters a housing complex, he can meet any number of households in the time available. However, if a household makes a complaint against the salesman, then he must leave the housing complex immediately and cannot meet any other household on that day. A household may buy any number of TRICCEK items or may not buy any item. The salesman needs to record the total number of TRICCEK items sold as well as the number of households met in each day. The success rate of a salesman for a day is defined as the ratio of the number of items sold to the number of households met on that day.") +
 p("Some details about the performances of three salesmen - Tohri, Hokli and Lahur, on two particular days are given below.") +
 "<ol><li>Over the two days, all three of them met the same total number of households, and each of them sold a total of 100 items.</li><li>On both days, Lahur met the same number of households and sold the same number of items.</li><li>Hokli could not sell any item on the second day because the first household he met on that day complained against him.</li><li>Tohri met 30 more households on the second day than on the first day.</li><li>Tohri’s success rate was twice that of Lahur’s on the first day, and it was 75% of Lahur’s on the second day.</li></ol>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("Setting up", p(r"Let Tohri meet \(t\) households on day 1 and \(t + 30\) on day 2. Lahur meets \(l\) households each day and sells 50 items each day, so his success rate is \(\tfrac{50}{l}\) on both days.")),
       ("Tohri’s sales", p(r"Day 1: \(\tfrac{s_1}{t} = \tfrac{100}{l}\), so \(s_1 = \tfrac{100t}{l}\). Day 2: \(\tfrac{s_2}{t + 30} = \tfrac{37.5}{l}\), so \(s_2 = \tfrac{37.5(t + 30)}{l}\). The two add up to 100.")),
       ("Using equal totals", p(r"Tohri and Lahur meet the same number of households in all: \(2t + 30 = 2l\), so \(l = t + 15\). Substituting:") +
         r"\[137.5t + 1125 = 100(t + 15) \;\Rightarrow\; t = 10,\; l = 25\]" +
         p(r"Tohri sells 40 on day 1 and 60 on day 2.")),
       ("Hokli", p("He also met 50 households in all. On day 2 he met just one (who complained), so he met 49 on day 1 and sold all 100 items then."))) +
 table(["", "Day 1 met / sold", "Day 2 met / sold", "Rate day 1", "Rate day 2"],
       [["Tohri", "10 / 40", "40 / 60", "4", "1.5"], ["Hokli", "49 / 100", "1 / 0", "≈ 2.04", "0"], ["Lahur", "25 / 50", "25 / 50", "2", "2"]]) +
 final("Everything is fixed."),
 p("Write Lahur’s rate as 50/l on both days. Both of Tohri’s rates are then multiples of it, and the equal-households clue gives a single equation."),
 p(r"<b>Rates and totals:</b> when two people’s totals are linked, express both through one unknown and use the totals to solve."))
P.dq(1, "What was the total number of households met by Tohri, Hokli and Lahur on the first day?", [], "TITA", "84", "Medium",
 "Work out each salesman’s first-day count.", steps(("Adding", p("10 + 49 + 25 = 84."))) + final(r"\(84\)"))
P.dq(2, "How many TRICCEK items were sold by Tohri on the first day?", [], "TITA", "40", "Medium",
 r"Tohri’s first-day sales are \(\tfrac{100t}{l}\).", steps(("Computing", p(r"\(\tfrac{100 \times 10}{25} = 40\)."))) + final(r"\(40\)"))
P.dq(3, "How many households did Lahur meet on the second day?", ["more than 35", "between 30 and 35", "20 or less", "between 21 and 29"], "MCQ", "4", "Medium",
 "Lahur met the same number on both days.", steps(("From the table", p("Lahur met 25 households each day."))) + final("Between 21 and 29, option 4"),
 [("1", "Lahur met 25."), ("2", "Lahur met 25."), ("3", "Lahur met 25.")])
P.dq(4, "How many households did Tohri meet on the first day?", ["more than 40", "10 or less", "between 21 and 40", "between 11 and 20"], "MCQ", "2", "Medium",
 "Solve for t.", steps(("From the table", p("Tohri met 10 households on day 1."))) + final("10 or less, option 2"),
 [("1", "That is about his day-2 count (40), not day 1."), ("3", "Tohri met 10."), ("4", "Tohri met 10.")])
P.dq(5, "Which of the following statements is FALSE?", ["Tohri had a higher success rate on the first day compared to the second day.", "Among the three, Tohri had the highest success rate on the first day.", "Among the three, Tohri had the highest success rate on the second day.", "Among the three, Lahur had the lowest success rate on the first day."], "MCQ", "3", "Medium",
 "Compare the success rates in the table.",
 steps(("Checking", p("On day 2, Tohri’s rate is 1.5 and Lahur’s is 2, so Tohri didn’t have the highest rate that day. The other three statements are true."))) + final("Option 3"),
 [("1", "True: 4 on day 1 against 1.5 on day 2."), ("2", "True: 4 is higher than about 2.04 and 2."), ("4", "True: Lahur’s 2 is just below Hokli’s 100/49.")])

# ---------------- Set 2: Widget deliveries ----------------
P.dilr_set(2, "Set 2 — Delivering widgets", "Answer the questions on the basis of the information given below.",
 p("Every day, a widget supplier supplies widgets from the warehouse (W) to four locations – Ahmednagar (A), Bikrampore (B), Chitrachak (C), and Deccan Park (D). The daily demand for widgets in each location is uncertain and independent of each other. Demands and corresponding probability values (in parenthesis) are given against each location (A, B, C, and D) in the figure given below. For example, there is a 40% chance that the demand in Ahmednagar will be 50 units and a 60% chance that the demand will be 70 units. The lines in the figure connecting the locations and warehouse represent two-way roads connecting those places with the distances (in km) shown beside the line. The distances in both the directions along a road are equal. For example, the road from Ahmednagar to Bikrampore and the road from Bikrampore to Ahmednagar are both 6 km long.") +
 '<p class="fig"><img src="sipe_2022S2_DILR_S2.svg" alt="Road map. Roads: A–B 6 km, B–C 4 km, C–D 6 km, A–D 8 km; from the warehouse W: to A 5 km, to B 10 km, to C 12 km, to D 2 km. Demand at A: 50 (40%) or 70 (60%); B: 40 (30%) or 60 (70%); C: 70 (30%) or 100 (70%); D: 30 (40%) or 50 (60%)."></p>' +
 p("Every day, the supplier gets the information about the demand values of the four locations and creates the travel route that starts from the warehouse and ends at a location after visiting all the locations exactly once. While making the route plan, the supplier goes to the locations in decreasing order of demand. If there is a tie for the choice of the next location, the supplier will go to the location closest to the current location. Also, while creating the route, the supplier can either follow the direct path (if available) from one location to another or can take the path via the warehouse. If both paths are available (direct and via warehouse), the supplier will choose the path with minimum distance."),
 "DILR::LR::Routes_and_Networks",
 steps(("Distances between places", table(["", "A", "B", "C", "D"],
          [["W", "5", "10", "12", "2"], ["A", "–", "6", "17 (via W)", "7 (via W)"], ["B", "6", "–", "4", "12 (via W)"], ["C", "17 (via W)", "4", "–", "6"], ["D", "7 (via W)", "12 (via W)", "6", "–"]]) +
          p("A to D is shorter via the warehouse (5 + 2 = 7) than by the direct road (8).")),
       ("Who goes first", p("C’s demand is at least 70, so C comes first, except when C and A are both 70: then the tie is broken from the warehouse, and A (5 km) is closer than C (12 km).")),
       ("Ties later on", p("A and D can tie at 50. From B, A is closer (6 against 12); from C, D is closer (6 against 17)."))) +
 final("Each question fixes the demands; the route then follows from the order and the distance table."),
 p("Build the distance table once, including the via-warehouse paths. Every question is then a matter of ordering four numbers and adding three or four distances."),
 p("<b>Routing with rules:</b> list the shortest allowed distance between every pair first. Questions then reduce to choosing an order."))
P.dq(6, "If the last location visited is Ahmednagar, then what is the total distance covered in the route (in km)?", [], "TITA", "35", "Hard",
 "For A to be last its demand must be 50, and every other demand at least 50.",
 steps(("What the condition needs", p("A = 50, so B = 60 and D = 50, with C first. The order is then C, B, and a tie between A and D.")),
       ("A problem with the question", p("From B, A (6 km) is closer than D (12 km), so the supplier would go to A before D, and A couldn’t be last. Because of this the question was dropped from scoring in the actual exam.")),
       ("The intended answer", p("The intended route is W → C → B → D → A: 12 + 4 + 12 + 7 = 35 km."))) + final(r"\(35\) (this question was not scored in the exam)"))
P.dq(7, "If the total number of widgets delivered in a day is 250 units, then what is the total distance covered in the route (in km)?", [], "TITA", "38", "Medium",
 "Find the only combination of demands that adds to 250.",
 steps(("The demands", p("A + B can be 90, 110 or 130, and C + D can be 100, 120, 130 or 150. The only way to make 250 is 130 + 120: A = 70, B = 60, C = 70, D = 50.")),
       ("The route", p("A and C tie at 70, and A is closer to the warehouse, so A goes first, then C, B and D: 5 + 17 + 4 + 12 = 38 km."))) + final(r"\(38\)"))
P.dq(8, "What is the chance that the total number of widgets delivered in a day is 260 units and the route ends at Bikrampore?", ["7.56%", "33.33%", "17.64%", "10.80%"], "MCQ", "1", "Hard",
 "List the demand combinations that make 260, then check which of them end at B.",
 steps(("Combinations for 260", p("A70 B60 C100 D30; A70 B40 C100 D50; A50 B60 C100 D50.")),
       ("Which end at B", p("B is last only in the second case (order C, A, D, B). In the first, D is last; in the third, the A–D tie is broken from B in favour of A, so D is last.")),
       ("The probability", p(r"\(0.6 \times 0.3 \times 0.7 \times 0.6 = 0.0756\)."))) + final("7.56%, option 1"),
 [("2", "Only one combination works, and its probability is 7.56%."), ("3", "Only one combination works, and its probability is 7.56%."), ("4", "This leaves out one of the four probabilities.")])
P.dq(9, "If the first location visited from the warehouse is Ahmednagar, then what is the chance that the total distance covered in the route is 40 km?", ["5.4%", "18%", "30%", "3.24%"], "MCQ", "2", "Hard",
 "A goes first only when A and C are both 70. After A and C, what makes the remaining distance 18 km?",
 steps(("The start", p("W → A → C costs 5 + 17 = 22 km, so the last two legs must add up to 18.")),
       ("The last two legs", p("C → B → D is 4 + 12 = 16; C → D → B is 6 + 12 = 18. So D must come before B, which needs D = 50 and B = 40.")),
       ("The probability", p(r"Given that A goes first, this has probability \(0.6 \times 0.3 = 0.18\)."))) + final("18%, option 2"),
 [("1", "This also multiplies in the 30% chance that C is 70, which is already given."), ("3", "This uses only one of the two conditions."), ("4", "This also multiplies in the chance that A and C are 70, which is already given.")])
P.dq(10, "If Ahmednagar is not the first location to be visited in a route and the total route distance is 29 km, then which of the following is a possible number of widgets delivered on that day?", ["220", "200", "250", "210"], "MCQ", "4", "Hard",
 "C goes first (12 km), so the other three legs must add to 17.",
 steps(("The route", p("Of the possible orders after C, only C → B → A → D gives 4 + 6 + 7 = 17.")),
       ("The demands", p("B before A needs B = 60 and A = 50. D can be 30 or 50 (a 50 tie with A is broken from B in A’s favour). C can be 70 or 100.")),
       ("Totals", p("60 + 50 + C + D gives 210, 230, 240 or 260. Only 210 is among the options."))) + final("210, option 4"),
 [("1", "Not a possible total for this route."), ("2", "Not a possible total for this route."), ("3", "Not a possible total for this route.")])

# ---------------- Set 3: Four companies ----------------
P.dilr_set(3, "Set 3 — Revenue, costs and employees of four companies", "Answer the questions based on the following information.",
 p("The two plots given below show data for four companies code-named A, B, C, and D over three years - 2019, 2020, and 2021.") +
 p("The first plot shows the revenues and costs incurred by the companies during these years. For example, in 2021, company C earned ₹ 100 crores in revenue and spent ₹ 30 crores. The profit of a company is defined as its revenue minus its costs.") +
 '<p class="fig"><img src="sipe_2022S2_DILR_S3a.svg" alt="Scatter plot of revenue (x) against costs (y), in ₹ crores. 2019: A (90, 85), B (100, 75), C (25, 20), D (50, 40). 2020: A (90, 65), B (90, 40), C (70, 60), D (20, 50). 2021: A (60, 30), B (30, 30), C (100, 30), D (70, 70)."></p>' +
 p("The second plot shows the number of employees employed by the company (employee strength) at the start of each of these three years, as well as the number of new employees hired each year (new hires). For example, Company B had 250 employees at the start of 2021, and 30 new employees joined the company during the year.") +
 '<p class="fig"><img src="sipe_2022S2_DILR_S3b.svg" alt="Scatter plot of employee strength at the start of the year (x) against new hires (y). 2019: A (150, 20), B (210, 35), C (330, 45), D (400, 30). 2020: A (140, 35), B (240, 45), C (330, 40), D (410, 35). 2021: A (150, 25), B (250, 30), C (330, 35), D (400, 40)."></p>',
 "DILR::DI::Graphs_and_Charts",
 steps(("Profits", table(["", "2019", "2020", "2021"],
          [["A", "90 − 85 = 5", "90 − 65 = 25", "60 − 30 = 30"], ["B", "100 − 75 = 25", "90 − 40 = 50", "30 − 30 = 0"],
           ["C", "25 − 20 = 5", "70 − 60 = 10", "100 − 30 = 70"], ["D", "50 − 40 = 10", "20 − 50 = −30", "70 − 70 = 0"]])),
       ("Employees lost", p("Employees lost in a year = strength at the start + new hires − strength at the start of the next year.") +
          table(["", "2019", "2020", "Total"], [["A", "150 + 20 − 140 = 30", "140 + 35 − 150 = 25", "55"], ["B", "210 + 35 − 240 = 5", "240 + 45 − 250 = 35", "40"],
                                                ["C", "330 + 45 − 330 = 45", "330 + 40 − 330 = 40", "85"], ["D", "400 + 30 − 410 = 20", "410 + 35 − 400 = 45", "65"]]))) +
 final("All answers come from these two tables."),
 p("Turn both plots into tables first: profit is the horizontal minus the vertical value in the first plot."),
 p("<b>Scatter plots:</b> each point is a pair of values. Reading them into a small table before answering avoids repeated misreading."))
P.dq(11, "Considering all the three years, which company had the highest annual profit?", ["Company A", "Company B", "Company C", "Company D"], "MCQ", "3", "Easy",
 "Find the single largest profit in the table.", steps(("Reading it off", p("C made 70 crores in 2021, the highest."))) + final("Company C, option 3"),
 [("1", "A’s best year is 30."), ("2", "B’s best year is 50."), ("4", "D’s best year is 10.")])
P.dq(12, "Which of the four companies experienced the highest annual loss in any of the years?", ["Company A", "Company D", "Company C", "Company B"], "MCQ", "2", "Easy",
 "Only one company has a negative profit.", steps(("Reading it off", p("D lost 30 crores in 2020."))) + final("Company D, option 2"),
 [("1", "A made a profit every year."), ("3", "C made a profit every year."), ("4", "B never made a loss; its worst year broke even.")])
P.dq(13, "The ratio of a company’s annual profit to its annual costs is a measure of its performance. Which of the four companies had the lowest value of this ratio in 2019?", ["Company C", "Company A", "Company B", "Company D"], "MCQ", "2", "Easy",
 "Compute profit ÷ cost for 2019.", steps(("2019 ratios", p("A: 5/85 ≈ 0.06; B: 25/75 ≈ 0.33; C: 5/20 = 0.25; D: 10/40 = 0.25."))) + final("Company A, option 2"),
 [("1", "C’s ratio is 0.25."), ("3", "B’s ratio is the highest."), ("4", "D’s ratio is 0.25.")])
P.dq(14, "The total number of employees lost in 2019 and 2020 was the least for:", ["Company D", "Company C", "Company A", "Company B"], "MCQ", "4", "Medium",
 "Use the employees-lost table.", steps(("Totals", p("A 55, B 40, C 85, D 65."))) + final("Company B, option 4"),
 [("1", "D lost 65."), ("2", "C lost 85."), ("3", "A lost 55.")])
P.dq(15, "Profit per employee is the ratio of a company’s profit to its employee strength. For this purpose, the employee strength in a year is the average of the employee strength at the beginning of that year and the beginning of the next year. In 2020, which of the four companies had the highest profit per employee?", ["Company B", "Company A", "Company C", "Company D"], "MCQ", "1", "Medium",
 "Average the 2020 and 2021 starting strengths, then divide the 2020 profit by it.",
 steps(("2020 figures", p("A: 25 ÷ 145 ≈ 0.17. B: 50 ÷ 245 ≈ 0.20. C: 10 ÷ 330 ≈ 0.03. D made a loss."))) + final("Company B, option 1"),
 [("2", "A’s ratio is about 0.17."), ("3", "C’s ratio is about 0.03."), ("4", "D made a loss in 2020.")])

# ---------------- Set 4: Supermarket products ----------------
P.dilr_set(4, "Set 4 — Products and approvals in a supermarket", "Answer the questions based on the following information.",
 p("A speciality supermarket sold 320 products. Each of these products was either a cosmetic product or a nutrition product. Each of these products was also either a foreign product or a domestic product. Each of these products had at least one of the two approvals – FDA or EU.") +
 p("The following facts are also known:") +
 "<ol><li>There were equal numbers of domestic and foreign products.</li><li>Half of the domestic products were FDA approved cosmetic products.</li><li>None of the foreign products had both the approvals, while 60 domestic products had both the approvals.</li><li>There were 140 nutrition products; half of them were foreign products.</li><li>There were 200 FDA approved products. 70 of them were foreign products and 120 of them were cosmetic products.</li></ol>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("Basic counts", p("160 domestic and 160 foreign. Nutrition: 70 foreign, 70 domestic, so cosmetic: 90 foreign, 90 domestic. Domestic FDA cosmetic: 80.")),
       ("FDA approvals", p("FDA total 200: 70 foreign, 130 domestic. FDA cosmetic 120, of which 80 are domestic, so 40 are foreign. Foreign FDA nutrition is then 70 − 40 = 30, and domestic FDA nutrition is 130 − 80 = 50.")),
       ("EU only", p("Foreign products have exactly one approval, so foreign EU-only products are 160 − 70 = 90: cosmetic 90 − 40 = 50, nutrition 70 − 30 = 40. Domestic EU-only: 160 − 130 = 30, made up of cosmetic 90 − 80 = 10 and nutrition 70 − 50 = 20.")),
       ("Both approvals", p(r"60 domestic products have both; they are among the 80 FDA cosmetic and 50 FDA nutrition products. If \(x\) are cosmetic, then \(60 - x \le 50\), so \(10 \le x \le 60\)."))) +
 table(["", "FDA only", "Both", "EU only"], [["Foreign cosmetic", "40", "0", "50"], ["Foreign nutrition", "30", "0", "40"],
        ["Domestic cosmetic", "80 − x", "x", "10"], ["Domestic nutrition", "50 − (60 − x)", "60 − x", "20"]]) +
 final(r"Everything is fixed except \(x\), the number of domestic cosmetic products with both approvals (10 to 60)."),
 p("Fill a grid of origin × type × approval, starting from the cells the facts give directly. Only one number stays open."),
 p("<b>Three-way splits:</b> with three yes/no attributes, a small table of all combinations keeps the counting straight."))
P.dq(16, "How many foreign products were FDA approved cosmetic products?", [], "TITA", "40", "Medium",
 "FDA cosmetic products are 120, and 80 of them are domestic.", steps(("Subtracting", p("120 − 80 = 40."))) + final(r"\(40\)"))
P.dq(17, "How many cosmetic products did not have FDA approval?", ["50", "Cannot be determined", "60", "10"], "MCQ", "3", "Easy",
 "180 cosmetic products, 120 of them FDA approved.", steps(("Subtracting", p("180 − 120 = 60."))) + final("60, option 3"),
 [("1", "That is only the foreign ones."), ("2", "It can be determined."), ("4", "That is only the domestic ones.")])
P.dq(18, "Which among the following options best represents the number of domestic cosmetic products that had both the approvals?", ["At least 10 and at most 80", "At least 10 and at most 60", "At least 20 and at most 70", "At least 20 and at most 50"], "MCQ", "2", "Medium",
 "At most 50 of the 60 can be nutrition products, and no more than 60 have both approvals in all.",
 steps(("The range", p(r"\(60 - x \le 50\) gives \(x \ge 10\), and \(x \le 60\) because only 60 domestic products have both."))) + final("At least 10, at most 60, option 2"),
 [("1", "At most 60 domestic products have both approvals."), ("3", "The minimum is 10, and the maximum isn’t 70."), ("4", "Both bounds are off.")])
P.dq(19, "If 70 cosmetic products did not have EU approval, then how many nutrition products had both the approvals?", ["30", "10", "50", "20"], "MCQ", "2", "Medium",
 "Cosmetic products without EU approval are the FDA-only ones.",
 steps(("Solving", p(r"FDA-only cosmetic products: \(40 + (80 - x) = 70\), so \(x = 50\). Nutrition products with both approvals: \(60 - 50 = 10\)."))) + final("10, option 2"),
 [("1", "This would need x = 30."), ("3", "This would need x = 10."), ("4", "This would need x = 40.")])
P.dq(20, "If 50 nutrition products did not have EU approval, then how many domestic cosmetic products did not have EU approval?", [], "TITA", "50", "Medium",
 "Nutrition products without EU approval are the FDA-only ones.",
 steps(("Solving", p(r"FDA-only nutrition: \(30 + 50 - (60 - x) = 50\), so \(x = 30\). Domestic cosmetic without EU: \(80 - 30 = 50\)."))) + final(r"\(50\)"))
