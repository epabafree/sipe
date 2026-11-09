# -*- coding: utf-8 -*-
# Simp Mock 8 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_08 import P
import m25_08_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Upskilling workshops (Q1–5) ----------------
MULTI = table(["Workshop", "Total", "Only", "Multi"], [["AI &amp; Ethics", "200", "60", "140"], ["Blockchain", "210", "80", "130"], ["Quantum", "130", "50", "80"], ["Cybersecurity", "240", "100", "140"], ["Edge", "210", "90", "120"]])
P.dilr_set(1, "Set 1 — Upskilling workshops", DIR,
 p("At a mid-sized IT company, employees in technical departments worried about trends that could make their roles redundant, so the company ran an upskilling programme of five workshops: AI &amp; Ethics, Blockchain Today, Quantum Computing, Cybersecurity Trends and Edge Computing. Participation was open to all technical teams.") +
 p("Attendees came from three divisions: Software Engineers (SE), Data Scientists (DS) and IT Security Specialists (ITSec). Each employee attended at least one workshop; many attended more than one, and some attended only one.") +
 p("The graph shows the numbers of SE, DS and ITSec employees who attended each workshop, and the number of employees who attended only that workshop.") + F.WORK,
 "DILR::DI::Graphs_and_Charts",
 steps(("Attendances", MULTI + p("‘Multi’ = attendances by people who went to two or more workshops: 610 in all. Only-one attendees: 380.")),
       ("Fewest people", p("Each multi-attendee goes to AI &amp; Ethics at most once, so there are at least 140 of them. 140 is achievable, so the minimum is 380 + 140 = 520.")),
       ("What the minimum forces", p("With exactly 140 multi-attendees, AI &amp; Ethics and Cybersecurity each have 140 multi-attendances: every multi-attendee went to both.")),
       ("One way to reach it", p("80 attend all five; 40 attend all but Quantum; 10 attend AI, Blockchain and Cybersecurity; 10 attend AI and Cybersecurity only."))) +
 final("Minimum 520; at the minimum, every multi-attendee went to AI &amp; Ethics and Cybersecurity."),
 p("A workshop’s multi-attendances count distinct people, so the largest of them is a floor on how many multi-attendees there are."),
 p("<b>Minimising people:</b> the busiest single slot is a lower bound; check whether it can be met."))
P.dq(1, "What is the minimum possible number of employees who attended at least one workshop?", ["500", "520", "560", "More information is needed to answer this question"], "MCQ", "2", "Medium",
 "At least 140 multi-attendees.", steps(("Minimum", p("380 + 140 = 520."))) + final("520, option 2"),
 [("1", "Below the floor of 140 multi-attendees."), ("3", "Not the minimum."), ("4", "The bound is reachable.")])
P.dq(2, "If all Software Engineers attended only one workshop and the total number of employees who attended at least one workshop was the minimum possible, what can be the minimum number of Data Scientists who attended at least one workshop?", ["75", "90", "100", "More information is needed to answer this question"], "MCQ", "3", "Hard",
 "The 140 multi-attendees are all DS or ITSec, and every one went to AI and Cybersecurity.",
 steps(("Split", p("Let m DS go to several workshops; then 140 − m ITSec do. DS has only 70 at AI, so m ≤ 70.")),
       ("Count DS", p("Each multi-DS covers a workshop at most once, so DS who went only to: AI ≥ 70 − m, Cybersecurity ≥ 90 − m, Edge ≥ 80 − m. With m = 70: DS ≥ 0 + 20 + 10 + 70 = 100. A smaller m only adds more.")),
       ("Check", p("m = 70 works: the only-one totals (after the 250 SE) are met with ITSec taking 20 at AI, 30 at Blockchain, 20 at Quantum, 20 at Edge, 10 at Cybersecurity."))) + final("100, option 3"),
 [("1", "Too few for the DS attendance counts."), ("2", "Would need more than 70 multi-DS, but only 70 DS attended AI."), ("4", "It can be found.")])
P.dq(3, "If all Software Engineers attended only one workshop and the total number of employees who attended at least one workshop was the minimum possible, what can be the minimum number of IT Security Specialists who attended at least one workshop?", ["100", "90", "110", "More information is needed to answer this question"], "MCQ", "3", "Hard",
 "Same idea; ITSec has only 80 at Cybersecurity.",
 steps(("Split", p("Let m′ ITSec be multi-attendees: m′ ≤ 80 (Cybersecurity has 80 ITSec).")),
       ("Count ITSec", p("Only-one ITSec at: AI ≥ 90 − m′, Blockchain ≥ 100 − m′, plus m′ multi. With m′ = 80: 10 + 20 + 80 = 110; smaller m′ adds more.")),
       ("Check", p("m′ = 80 leaves 60 multi-DS; the only-one totals are met (e.g. DS 10 at Blockchain, 30 at Edge, 10 at AI, 30 at Cybersecurity, 20 at Quantum)."))) + final("110, option 3"),
 [("1", "Would need more than 80 multi-ITSec."), ("2", "Too few."), ("4", "It can be found.")])
P.dq(4, "Suppose the total number of employees who attended at least one workshop was the minimum possible, and as many of them as possible attended all five workshops. How many employees attended the Quantum Computing workshop together with at most two other workshops?", ["50", "80", "100", "More information is needed to answer this question"], "MCQ", "1", "Medium",
 "Quantum’s 80 multi-attendances cap the all-five group at 80.",
 steps(("All five", p("At most 80 can attend all five (Quantum has 80 multi-attendances); 80 is possible, as in the set solution.")),
       ("Quantum", p("Then every multi-attendee at Quantum went to all five. Only the 50 who went to Quantum alone count."))) + final("50, option 1"),
 [("2", "These went to all five."), ("3", "Not a count from the data."), ("4", "Fixed once the all-five group is largest.")])
P.dq(5, "If the total number of employees who attended the workshops is the minimum possible, then the employees who attended exactly two workshops did not attend the workshops on __________ .", ["Blockchain Today and Quantum Computing", "AI &amp; Ethics, Quantum Computing and Edge Computing", "Blockchain Today, Quantum Computing and Edge Computing", "More information is needed to answer this question"], "MCQ", "3", "Medium",
 "Every multi-attendee went to AI &amp; Ethics and Cybersecurity.",
 steps(("Exactly two", p("Those two workshops use up both slots: they skipped Blockchain, Quantum and Edge."))) + final("Option 3"),
 [("1", "Leaves out Edge."), ("2", "They did attend AI &amp; Ethics."), ("4", "Forced at the minimum.")])

# ---------------- Set 2: Olympic medals (Q6–9) ----------------
MED = table(["Year", "Gold", "Silver", "Bronze"], [["2016", "19", "24", "34"], ["2020", "19", "18", "17"], ["2024", "?", "18", "17"]])
P.dilr_set(2, "Set 2 — Medals over three Games", DIR,
 p("Country XYZ took part in the 2016, 2020 and 2024 Olympics. The following facts are known about its medal winners (medals are Gold, Silver and Bronze):") +
 "<ul><li>All but one of the 2016 Gold medallists won Silver in 2020, and no other athlete won Silver in 2020.</li><li>All but one of the 2020 Silver medallists won Bronze in 2024, and no other athlete won Bronze in 2024.</li><li>All but one of the 2020 Gold medallists won Silver in 2024, and no other athlete won Silver in 2024.</li><li>Apart from these, no athlete won more than one medal across the three Games.</li><li>XYZ had 77 athletes at the 2016 Games, and each of them won exactly one medal.</li><li>Of all the Bronze medallists across the three Games, 50% were from 2016 and 25% from 2024.</li><li>The numbers of Silver medallists in 2020 and 2024 are equal, and the number in 2020 is 75% of the number in 2016.</li></ul>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("In terms of a", p(r"Let 2016 Gold = a. Silver 2020 = a − 1; Bronze 2024 = a − 2. Bronze 2020 is the other 25%, also a − 2; Bronze 2016 = 2(a − 2). Silver 2024 = Silver 2020 = a − 1, so Gold 2020 = a. Silver 2016 = \(\tfrac43(a - 1)\).")),
       ("2016 total", p(r"\(a + \tfrac43(a - 1) + 2(a - 2) = 77\) gives \(13a = 247\), a = 19.")),
       ("Medals", MED)) +
 final("Everything is fixed except 2024 Gold."),
 p("Name one unknown (2016 Gold) and walk the ‘all but one’ chains."),
 p("<b>Chained ‘all but one’:</b> each link subtracts one."))
P.dq(6, "How many medals did country XYZ win at the 2020 Olympics?", [], "TITA", "54", "Medium",
 "19 + 18 + 17.", steps(("2020", p("54."))) + final("54"))
P.dq(7, "How many athletes won Bronze medals at the 2016 Olympics?", ["30", "31", "33", "34"], "MCQ", "4", "Easy",
 "2(a − 2).", steps(("2016 Bronze", p("2 × 17 = 34."))) + final("34, option 4"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])
P.dq(8, "Which of the following combinations of Games, medal and number of medals is correct?", ["2016 – Gold – 20", "2020 – Silver – 19", "2024 – Bronze – 18", "2020 – Bronze – 17"], "MCQ", "4", "Easy",
 "Check the medal table.", steps(("Check", p("2020 Bronze is 17."))) + final("Option 4"),
 [("1", "19."), ("2", "18."), ("3", "17.")])
P.dq(9, "If 20 athletes won Gold at the 2024 Olympics, how many athletes won at least one medal across the three Games?", [], "TITA", "133", "Medium",
 "Count medals, then remove repeat winners.",
 steps(("Medals", p("2016: 77; 2020: 54; 2024: 20 + 18 + 17 = 55. Total 186.")),
       ("Repeats", p("Every 2020 Silver (18), 2024 Bronze (17) and 2024 Silver (18) went to someone who already had a medal: 186 − 53 = 133."))) + final("133"))

# ---------------- Set 3: Flower show (Q10–14) ----------------
PLANTS = table(["Who", "Plant", "Mo.", "₹"], [["Amit", "Orchid", "Feb", "L+50"], ["Karan", "Hibiscus", "Mar", "680"], ["Varun", "Lavender", "Apr", "L"], ["Priya", "Tulip", "May", "500"], ["Rahul", "Sunflower", "Jun", "750"], ["Sakshi", "Bougain.", "Jul", "400"], ["Meera", "Rose", "Aug", "450"], ["Neha", "Jasmine", "Oct", "300"], ["Rohit", "Daffodil", "Nov", "?"], ["Ananya", "Marigold", "Dec", "350"]])
P.dilr_set(3, "Set 3 — A flower show", DIR,
 p("At a flower show, ten gardeners, Amit, Priya, Rahul, Neha, Karan, Meera, Rohit, Sakshi, Varun and Ananya, show their plants. Each grew a different plant: Bougainvillea, Daffodil, Hibiscus, Jasmine, Lavender, Marigold, Orchid, Rose, Sunflower and Tulip. Each planted in a different month of one calendar year, excluding January and September. Each plant had a different price; the cheapest cost ₹300 and the dearest ₹750.") +
 "<ul><li>Amit planted his Orchid nine months before Rohit and three months before Priya. His plant cost exactly ₹50 more than the Lavender grown by Varun, who planted in April.</li><li>The Tulip, planted in May, cost ₹50 more than the Rose planted by Meera in August.</li><li>Rahul planted his Sunflower a month after Priya planted hers. His plant cost the highest price.</li><li>Neha’s Jasmine, bought at the lowest price, was planted exactly a month before Rohit’s Daffodil. It cost ₹50 less than Ananya’s Marigold.</li><li>Karan planted his Hibiscus in March; it cost ₹180 more than Priya’s Tulip. Rohit planted a month before the Marigold.</li><li>Sakshi planted four months after Karan. Her plant cost ₹100 more than the Jasmine and ₹100 less than the Tulip.</li></ul>",
 "DILR::LR::Puzzles",
 steps(("Months", p("Priya has the Tulip, planted in May; Amit is three months earlier: February. Rohit, nine months after Amit: November. Neha October; Marigold (Ananya) December; Rahul June; Sakshi July. Varun April, Meera August, Karan March.")),
       ("Prices", p("Jasmine 300, Marigold 350, Sakshi 400, Tulip 500, Rose 450, Hibiscus 680, Sunflower 750. Sakshi’s plant is the Bougainvillea.")),
       ("Open", p("Orchid = Lavender + 50 and the Daffodil are not fixed.")),
       ("Results", PLANTS + p("L = the Lavender’s price."))) +
 final("Seven gardeners are fully fixed; Amit’s, Varun’s and Rohit’s prices are open."),
 p("Priya’s Tulip in May anchors the months; Jasmine at ₹300 anchors the prices."),
 p("<b>Month arithmetic:</b> with January and September missing, count only the months in play."))
P.dq(10, "For how many gardeners can the plant, cost and month of planting all be determined uniquely?", ["7", "8", "9", "10"], "MCQ", "1", "Medium",
 "Which prices are still open?", steps(("Count", p("All except Amit (Orchid), Varun (Lavender) and Rohit (Daffodil): 7."))) + final("7, option 1"),
 [("2", "Three prices are open."), ("3", "Three prices are open."), ("4", "Three prices are open.")])
P.dq(11, "Which of the following combinations can be true?", ["Priya – Tulip – May – ₹550", "Sakshi – Bougainvillea – July – ₹450", "Karan – Hibiscus – March – ₹650", "None of these"], "MCQ", "4", "Medium",
 "Check each price.", steps(("Prices", p("Tulip 500, Bougainvillea 400, Hibiscus 680: all three are wrong."))) + final("Option 4"),
 [("1", "Tulip is ₹500."), ("2", "Bougainvillea is ₹400."), ("3", "Hibiscus is ₹680.")])
P.dq(12, "Who planted in October?", ["Karan", "Neha", "Rohit", "Ananya"], "MCQ", "2", "Easy",
 "A month before Rohit’s November.", steps(("October", p("Neha."))) + final("Option 2"),
 [("1", "March."), ("3", "November."), ("4", "December.")])
P.dq(13, "Additional information: the average cost of the Rose, Bougainvillea and Daffodil is ₹500, which is ₹100 more than the average cost of the Jasmine, Lavender and Marigold. Find the cost of Rohit’s plant.", [], "TITA", "650", "Easy",
 "Rose + Bougainvillea + Daffodil = 1500.", steps(("Daffodil", p("1500 − 450 − 400 = 650."))) + final("650"))
P.dq(14, "Additional information: the average cost of the Rose, Bougainvillea and Daffodil is ₹500, which is ₹100 more than the average cost of the Jasmine, Lavender and Marigold. Find the cost of Amit’s plant.", [], "TITA", "600", "Easy",
 "Jasmine + Lavender + Marigold = 1200.", steps(("Lavender", p("1200 − 300 − 350 = 550.")), ("Orchid", p("550 + 50 = 600."))) + final("600"))

# ---------------- Set 4: Salaries and efficiency (Q15–18) ----------------
BILL = table(["Co.", "Revenue", "%", "Bill"], [["A", "140", "42", "58.8"], ["B", "200", "51", "102"], ["C", "152", "37.5", "57"], ["D", "205", "48", "98.4"], ["E", "220", "45", "99"], ["F", "180", "30", "54"]])
P.dilr_set(4, "Set 4 — Salaries and efficiency", DIR,
 p("The graph shows six IT companies, A to F. The horizontal axis is each company’s revenue (₹ lakh) in April 2025; the vertical axis is the percentage of that revenue spent on salaries that month. For example, company C earned ₹152 lakh and spent 37.5% of it on salaries. Every other company’s percentage is a natural number.") +
 p("The number in brackets beside each company is the overall efficiency of its employees. For example, company A’s 1.05 means that if it had 100 employees, they would together produce as much as 105 employees at the industry standard.") + F.SCATTER +
 p("The ‘deserving average salary’ of a company is its average salary per employee multiplied by the overall efficiency of its employees. The average salary is the total salary bill for April 2025 divided by the number of employees. In every company, the average salary and the deserving average salary are both whole numbers of rupees."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Salary bills (₹ lakh)", BILL),
       ("Method", p("Bounds on the average (or deserving average) give a range for the number of employees; the whole-number conditions pick one."))) +
 final("Each question fixes a company’s headcount."),
 p("Read revenue and percentage, form the salary bill, then use the integer conditions."),
 p("<b>Divisibility filters:</b> ‘average is an integer’ means the headcount divides the salary bill."))
P.dq(15, "The average salary and the deserving average salary in company A are both more than ₹70,000 and less than ₹80,000. How many employees work in company A?", [], "TITA", "80", "Medium",
 "Bill ₹58,80,000; headcount 74 to 83.",
 steps(("Candidates", p(r"Headcounts 74–83 that divide 58,80,000: 75 and 80.")),
       ("Check", p(r"75: average 78,400, deserving \(78400 \times 1.05 = 82320\), too high. 80: average 73,500, deserving 77,175. ✓"))) + final("80"))
P.dq(16, "The average salary in company E is ₹500 more than in company D, and both are more than ₹80,000 and less than ₹85,000. What is the difference (in ₹) between the deserving average salaries of the two companies?", [], "TITA", "25150", "Hard",
 "D’s bill ₹98,40,000: headcount 116–122.",
 steps(("D", p("Only 120 divides the bill: average 82,000, deserving 65,600.")),
       ("E", p(r"Average 82,500 (bill 99,00,000, 120 employees), deserving \(82500 \times 1.1 = 90750\).")),
       ("Difference", p("90,750 − 65,600 = 25,150."))) + final("25150"))
P.dq(17, "The employees of company F produce output equal to the standard output of 54 employees. The average salary (in ₹) of an employee in this company is _________ .", ["108000", "108500", "114500", "116640"], "MCQ", "1", "Easy",
 "54 ÷ 1.08 = 50 employees.", steps(("Average", p("54,00,000 ÷ 50 = 1,08,000."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "That is the deserving average.")])
P.dq(18, "The deserving average salaries in companies B and C are both more than ₹86,000 and less than ₹91,000. What is the difference (in ₹) between the average salaries of the two companies?", ["11250", "9500", "7000", "Either 11250 or 7000"], "MCQ", "3", "Hard",
 "Turn the deserving range into an average range, then a headcount range.",
 steps(("B", p("Average between 86,000/0.85 and 91,000/0.85: headcount 96–100. Only 100 gives whole numbers: average 1,02,000 (deserving 86,700). 96 gives a deserving average of 90,312.5.")),
       ("C", p("Headcount 60–62; only 60 divides 57,00,000: average 95,000.")),
       ("Difference", p("7,000."))) + final("Option 3"),
 [("1", "Uses 96 employees for B, which fails the integer condition."), ("2", "Arithmetic slip."), ("4", "Only 100 works for B.")])

# ---------------- Set 5: Consistency awards (Q19–22) ----------------
AVG = table(["Player", "LC", "SS", "CC", "PL", "NT"], [["Asha", "70", "65", "80", "60", "75"], ["Bhavna", "60", "75", "85", "65", "80"], ["Charu", "85", "60", "70", "75", "65"], ["Diya", "55", "80", "65", "85", "70"], ["Esha", "75", "70", "55", "60", "85"], ["Farah", "80", "55", "75", "70", "60"]])
MAT = table(["Player", "LC", "SS", "CC", "PL", "NT"], [["Asha", "4", "3", "5", "2", "3"], ["Bhavna", "3", "4", "3", "3", "5"], ["Charu", "3", "2", "4", "4", "3"], ["Diya", "5", "5", "3", "5", "4"], ["Esha", "4", "4", "5", "3", "5"], ["Farah", "5", "3", "4", "5", "3"]])
WIN = ("<ul><li><b>LC</b>: weighted average 70.4, median 4 — Asha, Esha, Farah</li><li><b>SS</b>: 69.5, median 3.5 — Bhavna, Diya, Esha</li>"
       "<li><b>CC</b>: 71.0, median 4 — Asha, Charu, Farah</li><li><b>PL</b>: 71.4, median 3.5 — Charu, Farah</li><li><b>NT</b>: 74.1, median 3.5 — Bhavna, Diya, Esha</li></ul>")
P.dilr_set(5, "Set 5 — Consistency awards", DIR,
 p("Six cricketers, Asha, Bhavna, Charu, Diya, Esha and Farah, played in five tournaments: LeagueCup (LC), SuperSeries (SS), ChampionshipCup (CC), PremierLeague (PL) and NationsTrophy (NT). The board gives a ‘Consistency Award’ in a tournament to each player who meets both criteria:") +
 "<ul><li><b>Performance:</b> the player’s average score in the tournament is within ±12.5 points of the weighted average score of the six players in that tournament (weighted by matches played).</li><li><b>Participation:</b> the player played at least the median number of matches played by the six players in that tournament.</li></ul>" +
 p("<b>Average scores</b>") + AVG + p("<b>Matches played</b>") + MAT +
 "<ul><li>The board decided to give 15 awards in all across the five tournaments. If fewer than 15 instances meet both criteria, the board may give the remaining award(s) to players who did not meet one or both criteria, based on commitment.</li><li>If more than 15 instances qualify, the 15 awards are decided by lucky draw.</li><li>In three of the five tournaments, the player with the highest average score received the award.</li></ul>",
 "DILR::DI::Data_Tabulation",
 steps(("Each tournament", WIN),
       ("Count", p("3 + 3 + 3 + 2 + 3 = 14 qualify, so one award goes outside the criteria.")),
       ("Top scorers", p("SS’s top (Diya, 80) and NT’s top (Esha, 85) already qualify. The third tournament’s top scorer gets the 15th award: Charu (LC), Bhavna (CC) or Diya (PL)."))) +
 final("14 awards by the criteria; the 15th goes to the top scorer of LC, CC or PL."),
 p("Weighted average = Σ(score × matches) ÷ Σ matches; median of six = average of the middle two."),
 p("<b>Weighted averages:</b> weight each score by its matches, not by player."))
P.dq(19, "How many Consistency Awards were given based on the two criteria?", ["12", "13", "14", "15"], "MCQ", "3", "Medium",
 "Count qualifiers in each tournament.", steps(("Count", p("14."))) + final("14, option 3"),
 [("1", "Misses two."), ("2", "Misses one."), ("4", "One award is outside the criteria.")])
P.dq(20, "In which tournament did exactly two players receive Consistency Awards based on the two criteria?", ["SuperSeries", "PremierLeague", "ChampionshipCup", "LeagueCup"], "MCQ", "2", "Easy",
 "See the qualifier table.", steps(("PL", p("Charu and Farah."))) + final("Option 2"),
 [("1", "Three."), ("3", "Three."), ("4", "Three.")])
P.dq(21, "Which of the following players definitely received exactly two Consistency Awards?", ["Asha", "Bhavna", "Charu", "Diya"], "MCQ", "1", "Medium",
 "Who might get the 15th award?",
 steps(("By criteria", p("Asha 2 (LC, CC), Bhavna 2, Charu 2, Diya 2.")),
       ("15th award", p("It may go to Charu, Bhavna or Diya. Asha is safe at exactly two."))) + final("Asha, option 1"),
 [("2", "Could get a third (CC top)."), ("3", "Could get a third (LC top)."), ("4", "Could get a third (PL top).")])
P.dq(22, "If the remaining award is given to the highest scorer so that every tournament ends with an equal number of awards, which of the following players receives it?", ["Asha", "Bhavna", "Charu", "Diya"], "MCQ", "4", "Easy",
 "Equal numbers means PL needs a third award.", steps(("PL", p("The highest scorer in PL is Diya (85)."))) + final("Option 4"),
 [("1", "Not a top scorer."), ("2", "Top of CC, which already has 3."), ("3", "Top of LC, which already has 3.")])
