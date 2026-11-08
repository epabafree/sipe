# -*- coding: utf-8 -*-
# Simp Mock 4 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_04 import P
import m25_04_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Placements (Q1–4) ----------------
T8 = table(["College", "Foreign", "Indian", "None", "Total"], [["ABC", "160", "120", "60", "300"], ["DEF", "140", "100", "80", "320"], ["GHI", "180", "140", "60", "360"], ["JKL", "160", "100", "60", "300"]])
T7 = table(["College", "Foreign", "Indian", "None", "Total"], [["ABC", "120", "140", "40", "280"], ["DEF", "100", "180", "60", "300"], ["GHI", "260", "180", "20", "400"], ["JKL", "220", "140", "40", "320"]])
BOTH = table(["College", "8th: both", "7th: both"], [["ABC", "40", "20"], ["DEF", "0", "40"], ["GHI", "20", "60"], ["JKL", "20", "80"]])
P.dilr_set(1, "Set 1 — Campus placements", DIR,
 p("Four engineering colleges, ABC, DEF, GHI and JKL, are affiliated with a university campus. Students of the final year, i.e. the 7<sup>th</sup> and 8<sup>th</sup> semesters, are eligible for placements. Indian companies as well as foreign companies participated. "
   "If a student gets an offer from an Indian company, no other Indian company can make an offer to him or her. Similarly, a student can get at most one offer from a foreign company. However, a student can get an offer from one Indian company and one foreign company.") +
 p("The tables below give the number of students who got offers from foreign and from Indian companies, the number who got no offer, and the total number of students, as on the last date of the placement season.") +
 p("<b>8th semester</b>") + T8 + p("<b>7th semester</b>") + T7,
 "DILR::DI::Data_Tabulation",
 steps(("Placed students", p("Placed = total − none. Students with both offers are counted in both columns, so both = foreign + Indian − placed.")), ("Both offers", BOTH)) +
 final("Offers from both kinds of company for each college and semester."),
 p("Foreign + Indian counts the doubly placed twice: subtract the number placed."),
 p("<b>Two overlapping groups:</b> both = A + B − (A or B)."))
P.dq(1, "Which of the following is closest to the percentage of total number of students in the 7<sup>th</sup> and 8<sup>th</sup> semesters in ABC College who got a placement offer?", ["78.5%", "82.75%", "85.65%", "Cannot be determined"], "MCQ", "2", "Easy",
 "Placed = total − no offer.", steps(("ABC", p("Placed: 240 + 240 = 480 out of 580: 82.76%."))) + final("Option 2"), [("1", "Too low."), ("3", "Too high."), ("4", "The table gives it.")])
P.dq(2, "In which of the given four colleges was the number of students in the 8<sup>th</sup> semester who got offers from Indian as well as foreign companies the highest?", ["ABC College", "DEF College", "GHI College", "JKL College"], "MCQ", "1", "Medium",
 "Both = foreign + Indian − placed.", steps(("8th semester", p("ABC 40, DEF 0, GHI 20, JKL 20."))) + final("ABC, option 1"), [("2", "0."), ("3", "20."), ("4", "20.")])
P.dq(3, "How many students of JKL College in the 7<sup>th</sup> semester got offers from both an Indian company as well as a foreign company?", [], "TITA", "80", "Medium",
 "Placed 280.", steps(("JKL 7th", p("220 + 140 − 280 = 80."))) + final("80"))
P.dq(4, "How many students of GHI College in the 7<sup>th</sup> semester got an offer only from a foreign company?", [], "TITA", "200", "Medium",
 "Foreign minus those with both.", steps(("GHI 7th", p("Both: 260 + 180 − 380 = 60. Foreign only: 260 − 60 = 200."))) + final("200"))

# ---------------- Set 2: Wheel colouring (Q5–8) ----------------
P.dilr_set(2, "Set 2 — Colouring a wheel", DIR,
 p("The following diagram shows a wheel system made up of 4 concentric circular regions divided into 8 equal sectors, each of which subtends 45° at the centre.") + F.WHEEL +
 p("The innermost circular region is Track-1, the next ring outwards is Track-2, and so on. Thus this wheel has 4 tracks and 8 sectors. The intersection of Track-1 and Sector-1 is T<sub>1</sub>S<sub>1</sub>, that of Track-2 and Sector-5 is T<sub>2</sub>S<sub>5</sub>, and so on: 32 track–sector intersections (TSIs) in all.") +
 p("Think of a similar wheel (any natural numbers of tracks and sectors) divided into N sectors, each subtending \\(\\left(\\tfrac{360}{N}\\right)^\\circ\\) at the centre. Each track is coloured using the same set of exactly C distinct colours such that each TSI in any given track has a distinct colour. Each TSI is coloured with one colour. "
   "All the sectors are precisely aligned across the tracks: a line drawn from the centre along the edge of an innermost sector continues along the corresponding sector edges in all outer tracks.") +
 p("Assume that the wheel system has been coloured as per this guideline and that C = 5."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("Five sectors", p("Every track uses all C = 5 colours, one per TSI, so each track has exactly 5 TSIs: N = 5.")),
       ("Counting rule", p("A wheel can be turned, so colourings that differ only by turning the whole wheel (by 72°) are the same. Count arrangements with sectors labelled, then divide by 5."))) +
 final("N = 5; divide labelled counts by 5 for rotations of the whole wheel."),
 p("Each track is a permutation of the 5 colours; turning the whole wheel gives 5 copies of each colouring."),
 p("<b>Counting up to rotation:</b> if no colouring is unchanged by a turn, divide by the number of turns."))
P.dq(5, "If it is known that the wheel system has four concentric tracks, then the number of ways in which the wheel system can be coloured is ________ .", [], "TITA", "41472000", "Hard",
 "Each track: 5! ways. Then account for turning the wheel.",
 steps(("Labelled", p(r"\(120^4 = 207{,}360{,}000\).")), ("Rotations", p(r"Turning the wheel gives the same colouring 5 ways: \(207{,}360{,}000 \div 5 = 41{,}472{,}000\)."))) + final("41472000"))
P.dq(6, "If it is known that the wheel system has four concentric tracks and no two consecutive TSIs in any sector have the same colour, then the number of ways in which the wheel system can be coloured is ________ .", ["2011106", "2022216", "2033316", "2044416"], "MCQ", "4", "Hard",
 "Each outer track must have no colour in the same sector as the track inside it: a derangement.",
 steps(("Track by track", p(r"Track 1: 120. Each next track must differ from the one inside it in every sector: \(D_5 = 44\) ways.")), ("Total", p(r"\(120 \times 44^3 \div 5 = 2{,}044{,}416\)."))) + final("Option 4"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])
P.dq(7, "Suppose the wheel system has five concentric tracks and each TSI in any given sector has a distinct colour. One of the colours used is red. The order of the colours used in any track starting from the TSI in red in the clockwise direction is the same. The number of ways in which the wheel system can be coloured is ________ .", ["24", "476", "576", "2880"], "MCQ", "3", "Hard",
 "Every track is the same cycle of colours, turned by some amount.",
 steps(("The cycle", p("Starting from red, the order of the other four colours: 4! = 24.")),
       ("Turns", p("Each track is that cycle turned by 0–4 steps. Each sector must have 5 different colours, so the 5 tracks use 5 different turns: 5! = 120.")),
       ("Total", p(r"\(24 \times 120 \div 5 = 576\)."))) + final("576, option 3"),
 [("1", "Only the colour order."), ("2", "Not a valid count."), ("4", "Forgets to divide by the 5 rotations.")])
P.dq(8, "Suppose the wheel system has five concentric tracks and each TSI in any given sector has a distinct colour. Also assume that each concentric track can be rotated clockwise and counterclockwise around the common center freely as many times as desired by integral multiples of 72°. At most, how many sectors can there be with five TSIs of the same color at the end of the rotation?", ["2", "3", "4", "5"], "MCQ", "4", "Hard",
 "If all tracks have the same cyclic order, turning them can line everything up.",
 steps(("Best case", p("When every track has the same cyclic order, turn each one so that red lines up in one sector; then every sector has one colour throughout: 5 sectors."))) + final("5, option 4"),
 [("1", "Not the maximum."), ("2", "Not the maximum."), ("3", "If four sectors match, the fifth must too.")])

# ---------------- Set 3: Donations (Q9–13) ----------------
DON = p("Quintals of each item (DF dry fruits, L lentils, R rice, W wheat):") + table(["Unit", "DF", "L", "R", "W"], [["A", "2", "—", "10", "10"], ["B", "—", "4", "10", "10"], ["C", "3", "1", "—", "15"], ["D", "1", "2", "15", "—"]])
P.dilr_set(3, "Set 3 — Donations in kind", DIR,
 p("An orphanage has four units named A, B, C and D. It accepts donations only in kind: dry fruits (₹10,000 per quintal), lentils (₹5,000 per quintal), rice (₹2,000 per quintal) and wheat (₹1,000 per quintal). The weight of each type of item donated to any unit is a whole number of quintals.") +
 p("An NGO donated items worth ₹50,000 to each of the four units. It donated exactly three types of items to each unit. No two units received the same combination of items.") +
 p("The NGO donated dry fruits worth ₹60,000, lentils worth ₹35,000, rice worth ₹70,000 and wheat worth ₹35,000. The total weights of donations to units A, B, C and D (in quintals) were 22, 24, 19 and 18 respectively. Unit A received 10 quintals of wheat. The unit that did not receive rice received 3 quintals of dry fruits."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("Totals in quintals", p("Dry fruits 6, lentils 7, rice 35, wheat 35 quintals.")),
       ("Unit A", p("10 quintals of wheat (₹10,000) and 12 more quintals worth ₹40,000 from two items. Dry fruit + rice: \\(10d + 2r = 40\\), \\(d + r = 12\\) gives \\(d = 2, r = 10\\). Lentils + rice gives \\(l = 16/3\\) ✗, dry fruit + lentils too heavy. So A: 2 DF, 10 R, 10 W.")),
       ("The rest", p("Four different 3-item combinations, with the no-rice unit taking 3 DF. Testing weights 24, 19, 18 against the remaining totals gives one arrangement:") + DON)) +
 final("Each unit’s donation is fixed."),
 p("Each unit gives two equations (value and weight). Start with A, where wheat is known."),
 p("<b>Value and weight equations:</b> two items with known totals of value and weight can be solved directly."))
P.dq(9, "Which of the following units did not receive lentils?", ["A", "B", "C", "D"], "MCQ", "1", "Medium", "Check A.", steps(("A", p("A got dry fruit, rice and wheat."))) + final("A, option 1"), [("2", "B got 4."), ("3", "C got 1."), ("4", "D got 2.")])
P.dq(10, "How many quintals of rice did unit B receive?", ["0", "10", "15", "Cannot be determined"], "MCQ", "2", "Medium", "From the table.", steps(("B", p("10 quintals."))) + final("10, option 2"), [("1", "C got none."), ("3", "D got 15."), ("4", "Fixed.")])
P.dq(11, "Which of the following can be best said about the quantity of dry fruits received by unit C?", ["Unit C did not receive any dry fruit.", "Unit C received 1 quintal of dry fruits.", "Unit C received 2 quintals of dry fruits.", "Unit C received 3 quintals of dry fruits."], "MCQ", "4", "Medium",
 "C is the unit without rice.", steps(("C", p("No rice, so 3 quintals of dry fruit."))) + final("Option 4"), [("1", "C got 3."), ("2", "That is D."), ("3", "That is A.")])
P.dq(12, "How many quintals of wheat did unit D receive?", ["0", "10", "15", "Cannot be determined"], "MCQ", "1", "Medium", "D’s three items.", steps(("D", p("Dry fruit, lentils, rice: no wheat."))) + final("0, option 1"), [("2", "A and B got 10."), ("3", "C got 15."), ("4", "Fixed.")])
P.dq(13, "Which of the following is definitely true?", ["Quantity of lentils received by unit C = Quantity of dry fruits received by unit A.", "Quantity of rice received by unit B = Quantity of rice received by unit D.",
 "Quantity of dry fruits received by unit A = Quantity of lentils received by unit D.", "Quantity of wheat received by unit D = Quantity of lentils received by unit B."], "MCQ", "3", "Medium",
 "Compare in the table.", steps(("Check", p("A’s dry fruit 2 = D’s lentils 2."))) + final("Option 3"), [("1", "1 vs 2."), ("2", "10 vs 15."), ("4", "0 vs 4.")])

# ---------------- Set 4: Medal tally (Q14–18) ----------------
MED = table(["Athlete", "G", "S", "B", "Total"], [["Ajay (A3)", "3", "2", "1", "6"], ["Bhushan (A1)", "1", "5", "4", "10"], ["Chandru (A2)", "2", "1", "5", "8"], ["Dinesh (A5)", "5", "4", "3", "12"], ["Hari (A4)", "4", "3", "2", "9"]])
P.dilr_set(4, "Set 4 — Medals and disguises", DIR,
 p("Ajay, Bhushan, Chandru, Dinesh and Hari are five athletes who represented their country at various international championships. The numbers of gold, silver and bronze medals won by each of them were each one of 1, 2, 3, 4 and 5. Each athlete’s three counts were three different numbers. No two athletes won an equal number of medals of any one type. The total number of medals won by each athlete was different.") +
 p("When they met on the birthday of one of them, the following conversation took place (the five are disguised as A1 to A5):") +
 "<p><b>A1:</b> Out of the five of us, the birthday boy is the only one who won an odd number of total medals. Dinesh’s bronze, silver and gold counts form an arithmetic progression (in that order) with positive common difference.</p>"
 "<p><b>A2:</b> My total is one less than Hari’s. My bronze count is three more than A4’s.</p>"
 "<p><b>A3:</b> Dinesh’s total is twice mine. Bhushan’s silver count is two more than A5’s bronze count.</p>"
 "<p><b>A4:</b> My total is the median of our five totals. My silver count is the median of my three counts.</p>"
 "<p><b>A5:</b> Bhushan’s total is two more than Chandru’s. Ajay’s silver count is one-third of his total.</p>"
 "<p>All the statements were true.</p>",
 "DILR::LR::Puzzles",
 steps(("Each medal type is 1–5 once", p("So the five totals add to 45, and each total is between 6 and 12.")),
       ("Ajay", p("Silver = total ÷ 3 and the three counts are different: Ajay’s totals of 6, 9 or 12 with silver 2, 3, 4. Dinesh’s counts form an AP (bronze < silver < gold); Dinesh’s total is even and twice A3’s, so A3 has 6 and Dinesh 12 (5, 4, 3).")),
       ("Who is who", p("A3 has 6: that is Ajay (3, 2, 1). Bhushan = Chandru + 2, A2 = Hari − 1, only one odd total. The only fit: Chandru 8, Bhushan 10, Hari 9 (odd: the birthday boy), A2 = Chandru, A4 = Hari (median total 9), A1 = Bhushan, A5 = Dinesh.") + MED)) +
 final("All counts and all disguises are fixed; Hari is the birthday boy."),
 p("Totals add to 45 and lie between 6 and 12; ‘twice’ and ‘one-third’ clues settle Ajay and Dinesh quickly."),
 p("<b>Disguised speakers:</b> pin down people by facts about named athletes first, then match speakers."))
P.dq(14, "Who was the birthday boy?", ["Ajay", "Bhushan", "Chandru", "Hari"], "MCQ", "4", "Hard", "The only odd total.", steps(("Odd total", p("Hari, with 9."))) + final("Hari, option 4"), [("1", "6."), ("2", "10."), ("3", "8.")])
P.dq(15, "The number of athletes whose disguises can be uniquely determined is ______ .", [], "TITA", "5", "Hard", "Is anything left open?", steps(("All fixed", p("A1 Bhushan, A2 Chandru, A3 Ajay, A4 Hari, A5 Dinesh."))) + final("5"))
P.dq(16, "Which of the following combinations of disguises, names of the athletes and the total number of medals is false?", ["A1-Bhushan-10", "A2-Chandru-8", "A3-Hari-9", "A5-Dinesh-12"], "MCQ", "3", "Hard",
 "A3 is Ajay.", steps(("Check", p("A3 is Ajay with 6; Hari is A4 with 9."))) + final("Option 3"), [("1", "True."), ("2", "True."), ("4", "True.")])
P.dq(17, "Out of the five athletes, who won exactly 3 gold medals?", ["Ajay", "Hari", "Dinesh", "Cannot be determined"], "MCQ", "1", "Hard", "Read the gold column.", steps(("Gold 3", p("Ajay."))) + final("Ajay, option 1"), [("2", "Hari 4."), ("3", "Dinesh 5."), ("4", "Fixed.")])
P.dq(18, "The number of athletes for whom the numbers of medals of the three types won by them can be uniquely determined is _______ .", [], "TITA", "5", "Hard", "Is any count open?", steps(("All fixed", p("The table is unique."))) + final("5"))

# ---------------- Set 5: Branch offices (Q19–22) ----------------
P.dilr_set(5, "Set 5 — Five branch offices", DIR,
 p("A technology company has a total of 1700 employees working in its five branch offices: Bengaluru, Hyderabad, Chennai, Delhi and Kolkata. The bar graph below shows the percentage of all male and of all female employees working in each branch. For example, 15% of all male employees work in Kolkata. Every employee is male or female, and the company has no other offices.") + F.BARS,
 "DILR::DI::Graphs_and_Charts",
 steps(("Whole numbers", p("Male counts use 25%, 15% and 20% of M, so M is a multiple of 20. Female counts use 30%, 20%, 10%, 25%, 15% of F, so F is a multiple of 20 too. M + F = 1700.")),
       ("Branch by branch", p("Each branch: (male %) × M and (female %) × F. Every question fixes M (and so F) by a condition."))) +
 final("M and F are multiples of 20 adding to 1700."),
 p("Find which multiples of 20 are allowed, then apply each question’s condition."),
 p("<b>Two percentage bars with different bases:</b> a taller bar doesn’t mean more people; multiply by the group’s total."))
P.dq(19, "What will be the difference between the number of male and female employees working in the Hyderabad branch office, given that taking all the five branches together the total number of female employees is less than that of the male employees and their difference is minimal?", ["19", "23", "31", "37"], "MCQ", "4", "Medium",
 "Closest split with F < M: M = 860, F = 840.", steps(("Hyderabad", p("0.25 × 860 = 215 men, 0.3 × 840 = 252 women: difference 37."))) + final("37, option 4"), [("1", "Wrong split."), ("2", "Wrong split."), ("3", "Wrong split.")])
P.dq(20, "How many male employees work in the Bengaluru branch office if it is known that the difference between male and female employees working in that office is minimal?", ["129", "137", "141", "147"], "MCQ", "4", "Medium",
 "Bengaluru: 0.15M against 0.2F.",
 steps(("Try values", p(r"\(0.15M - 0.2(1700 - M)\) \(= 0.35M - 340\). Closest to 0 with M a multiple of 20: M = 980 gives 147 − 144 = 3; M = 960 gives 144 − 148 = −4.")), ("Men", p("147."))) + final("147, option 4"),
 [("1", "Not a possible count."), ("2", "Not a possible count."), ("3", "Not a possible count.")])
P.dq(21, "If the Chennai branch office has a total of 383 employees, then the difference between the number of employees working in the Delhi branch office and Kolkata branch office will be ________ .", ["41", "43", "47", "49"], "MCQ", "1", "Medium",
 "\\(0.2M + 0.25F = 383\\).",
 steps(("Find M", p(r"\(0.2M + 0.25(1700 - M)\) \(= 425 - 0.05M = 383\), so \(M = 840,\ F = 860\).")),
       ("Delhi and Kolkata", p("Delhi 210 + 86 = 296. Kolkata 0.15 × 1700 = 255. Difference 41."))) + final("41, option 1"), [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(22, "What can be the maximum number of female employees working in the company so that in each branch office the number of male employees becomes more than that of female employees?", [], "TITA", "720", "Medium",
 "The tightest branch is Bengaluru: 0.15M > 0.2F.",
 steps(("Tightest condition", p(r"Bengaluru needs \(M > \tfrac43F\); Chennai needs \(M > 1.25F\); Hyderabad \(M > 1.2F\). With \(M = 1700 - F\): \(F < 728.6\).")),
       ("Multiple of 20", p("F = 720 (M = 980: Bengaluru 147 men vs 144 women)."))) + final("720"))
