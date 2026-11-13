# -*- coding: utf-8 -*-
# Batch 20 — CAT 2025 Slot 1: DILR sets 1–5 (Q1–22, in exam order).
from fmt import steps, final, trap, why, table, p
from b20_25s1 import P
import b20_25s1_figs as F

DIR = "Read the information given below and answer the questions that follow."

# ---------------- Set 1: Train tickets ----------------
P.dilr_set(1, "Set 1 — Seat bookings on a five-station train", DIR,
 p("A train travels from Station A to Station E, passing through stations B, C, and D, in that order. The train has a seating capacity of 200. A ticket may be booked from any station to any other station ahead on the route, but not to any earlier station.") +
 p("A ticket from one station to another reserves one seat on every intermediate segment of the route. For example, a ticket from B to E reserves a seat in the intermediate segments B – C, C – D, and D – E.") +
 p("The occupancy factor for a segment is the total number of seats reserved in the segment as a percentage of the seating capacity. The total number of seats reserved for any segment cannot exceed 200.") +
 p("The following information is known.") +
 "<ol><li>Segment C – D had an occupancy factor of 95%. Only segment B – C had a higher occupancy factor.</li><li>Exactly 40 tickets were booked from B to C and 30 tickets were booked from B to E.</li><li>Among the seats reserved on segment D – E, exactly four-sevenths were from stations before C.</li><li>The number of tickets booked from A to C was equal to that booked from A to E, and it was higher than that from B to E.</li><li>No tickets were booked from A to B, from B to D and from D to E.</li><li>The number of tickets booked for any segment was a multiple of 10.</li></ol>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("The unknowns", p("Let AC = AE = x (more than 30), AD = y, CD = u and CE = v. The known tickets are BC = 40 and BE = 30; AB, BD and DE are zero.")),
       ("Segment loads", p(r"A–B: \(2x + y\). B–C: \(2x + y + 70\). C–D: \(x + y + 30 + u + v = 190\). D–E: \(x + 30 + v\).")),
       ("B–C is the fullest", p(r"B–C must be above 190 and at most 200, so \(2x + y\) is 130 (\(2x + y + 70 = 200\)), as it must be a multiple of 10 between 121 and 130.")),
       ("The four-sevenths clue", p(r"On D–E, the seats from before C are AE and BE: \(x + 30\). So \(x + 30 = \frac47(x + 30 + v)\), which gives \(v = \frac34(x + 30)\). Since \(2x \le 130\) and \(x > 30\), x is 40, 50 or 60; only \(x = 50\) makes v a multiple of 10, giving \(v = 60\).")),
       ("The rest", p(r"\(y = 130 - 100 = 30\). C–D: \(50 + 30 + 30 + u + 60 = 190\), so \(u = 20\).") +
          table(["Ticket", "Count"], [["A–C", "50"], ["A–D", "30"], ["A–E", "50"], ["B–C", "40"], ["B–E", "30"], ["C–D", "20"], ["C–E", "60"]]) +
          p("Loads: A–B 130, B–C 200, C–D 190, D–E 140."))) +
 final("Every ticket count is fixed; see the table."),
 p("Write each segment’s load as the sum of the tickets that pass over it. The 4/7 clue then fixes the long tickets."),
 p("<b>Segment loads:</b> a ticket from i to j occupies every segment between them. A segment’s load is the sum of all tickets that start before it and end after it."))
P.dq(1, "What was the occupancy factor for segment D – E?", ["35%", "70%", "84%", "77%"], "MCQ", "2", "Medium",
 "Which tickets cover D–E?",
 steps(p(r"A–E 50, B–E 30 and C–E 60: 140 seats, \(140 \div 200 = 70\%\).")) + final("70%, option 2"),
 [("1", "This counts only half of the seats."), ("3", "84% would need 168 seats."), ("4", "77% would need 154 seats.")])
P.dq(2, "How many tickets were booked from Station A to Station E?", [], "TITA", "50", "Medium",
 "Use the four-sevenths clue on D–E.",
 steps(p("A–C equals A–E, and the D–E clue together with the multiples of 10 gives 50.")) + final(r"\(50\)"))
P.dq(3, "How many tickets were booked from Station C?", [], "TITA", "80", "Easy",
 "Tickets starting at C go to D or E.",
 steps(p(r"C–D 20 + C–E 60 = 80.")) + final(r"\(80\)"))
P.dq(4, "What is the difference between the number of tickets booked to Station C and the number of tickets booked to Station D?", [], "TITA", "40", "Medium",
 "Add the tickets ending at C, then those ending at D.",
 steps(p(r"To C: A–C 50 + B–C 40 = 90. To D: A–D 30 + C–D 20 = 50. The difference is 40.")) + final(r"\(40\)"))
P.dq(5, "How many tickets were booked to travel in exactly one segment?", [], "TITA", "60", "Easy",
 "One-segment tickets are A–B, B–C, C–D and D–E.",
 steps(p(r"B–C 40 + C–D 20 = 60 (A–B and D–E had none).")) + final(r"\(60\)"))

# ---------------- Set 2: Elite and Novice ----------------
P.dilr_set(2, "Set 2 — Promotions between two teams", DIR,
 p("At InnovateX, six employees, Asha, Bunty, Chintu, Dolly, Eklavya, and Falguni, were split into two groups of three each: Elite led by Manager Kuku, and Novice led by Manager Lalu.") +
 p("At the end of each quarter, Kuku and Lalu handed out ratings to all members in their respective groups. In each group, each employee received a distinct integer rating from 1 to 3.") +
 p("The score for an employee at the end of a quarter is defined as their cumulative rating from the beginning of the year. At the end of each quarter the employee in Novice with the highest score was promoted to Elite, and the employee in Elite with the minimum score was demoted to Novice. If there was a tie in scores, the employee with a higher rating in the latest quarter was ranked higher.") +
 "<ol><li>Asha, Bunty, and Chintu were in Elite at the beginning of Quarter 1. All of them were in Novice at the beginning of Quarter 4.</li><li>Dolly and Falguni were the only employees who got the same rating across all the quarters.</li><li>The following is known about ratings given by Lalu:<ul><li>Bunty received a rating of 1 in Quarter 2.</li><li>Asha and Dolly received ratings of 1 and 2, respectively, in Quarter 3.</li></ul></li></ol>",
 "DILR::LR::Games_and_Tournaments",
 steps(("One swap per quarter", p("Three moves at the ends of Quarters 1, 2 and 3 take all of Asha, Bunty and Chintu down. So each quarter exactly one of them goes down and one of Dolly, Eklavya and Falguni goes up; nobody moves twice.")),
       ("Quarter 1", p("Bunty is with Lalu in Quarter 2, so he was demoted first, with Elite rating 1. Dolly is rated 2 every quarter. Someone from Novice is promoted; Dolly (2) can’t top a 3, so Falguni has 3 every quarter and goes up. Eklavya gets 1.")),
       ("Quarter 2", p("Asha is with Lalu in Quarter 3, so she is demoted now: in Elite, Asha gets 1, Chintu 2 (Falguni 3). In Novice, Bunty 1, Dolly 2, Eklavya 3. Dolly and Eklavya both have 4; Eklavya’s latest rating is higher, so he goes up.")),
       ("Quarter 3", p("Chintu goes down and Dolly up. Dolly’s 6 must top Novice, so Asha (1) and Bunty (3) are below it. In Elite, Chintu gets 1, Eklavya 2, Falguni 3.") +
          table(["", "Q1", "Q2", "Q3", "Score"], [["Asha", "2/3", "1", "1", "4/5"], ["Bunty", "1", "1", "3", "5"], ["Chintu", "3/2", "2", "1", "5/6"],
                                                  ["Dolly", "2", "2", "2", "6"], ["Eklavya", "1", "3", "2", "6"], ["Falguni", "3", "3", "3", "9"]]) +
          p("Asha and Chintu share the Quarter 1 ratings 2 and 3 in either order."))) +
 final("Only Asha’s and Chintu’s Quarter 1 ratings are open (2 and 3 in some order)."),
 p("Count the moves: three quarters, three demotions, so each of Asha, Bunty and Chintu drops exactly once. Lalu’s ratings tell you the order."),
 p("<b>Promotion puzzles:</b> track who is in which group each quarter. A rating from a particular manager tells you which group someone was in."))
P.dq(6, "What was Eklavya’s score at the end of Quarter 2?", [], "TITA", "4", "Medium",
 "Eklavya had 1 in Quarter 1. What did he get in Novice in Quarter 2?",
 steps(p("1 + 3 = 4.")) + final(r"\(4\)"))
P.dq(7, "How many employees changed groups more than once up to the beginning of Quarter 4?", [], "TITA", "0", "Medium",
 "Three moves take three people down; can anyone come back?",
 steps(p("All three of Asha, Bunty and Chintu must be in Novice by Quarter 4, using all three demotions. So nobody moves twice.")) + final(r"\(0\)"))
P.dq(8, "What was Bunty’s score at the end of Quarter 3?", [], "TITA", "5", "Medium",
 "Bunty had 1, 1 and then what in Quarter 3?",
 steps(p("In Quarter 3 Lalu gave Asha 1 and Dolly 2, so Bunty got 3: 1 + 1 + 3 = 5.")) + final(r"\(5\)"))
P.dq(9, "For how many employees can the scores at the end of Quarter 3 be determined with certainty?", [], "TITA", "4", "Medium",
 "Whose Quarter 1 ratings are open?",
 steps(p("Asha and Chintu depend on how 2 and 3 were split in Quarter 1. Bunty 5, Dolly 6, Eklavya 6 and Falguni 9 are fixed.")) + final(r"\(4\)"))
P.dq(10, "Which of the following statements is/are NECESSARILY true?<br>I. Asha received a rating of 2 in Quarter 1.<br>II. Asha received a rating of 1 in Quarter 2.", ["Only II", "Only I", "Both I and II", "Neither I nor II"], "MCQ", "1", "Medium",
 "Asha’s Quarter 1 rating could be 2 or 3.",
 steps(p("Asha had 2 or 3 in Quarter 1, so I is not certain. She had to be lowest in Elite after Quarter 2, so she got 1 then: II is certain.")) + final("Only II, option 1"),
 [("2", "I is not certain; she may have had 3."), ("3", "I is not certain."), ("4", "II is certain.")])

# ---------------- Set 3: Round table ----------------
P.dilr_set(3, "Set 3 — Moving around a seven-seat table", DIR,
 p("A round table has seven chairs around it. The chairs are numbered 1 through 7 in a clockwise direction. Four friends, Aslam, Bashir, Chhavi, and Davies, sit on four of the chairs. In the starting position, Aslam and Chhavi are sitting next to each other, while for Bashir as well as Davies, there are empty chairs on either side of the chairs that they are sitting on.") +
 p("The friends take turns moving either clockwise or counter clockwise from their chair. The friend who has to move in a turn occupies the first empty chair in whichever direction (s)he chooses to move. Aslam moves first (Turn 1), followed by Bashir, Chhavi, and Davies (Turns 2, 3, and 4, respectively). Then Aslam moves again followed by Bashir, and Chhavi (Turns 5, 6, and 7, respectively).") +
 p("The following information is known.") +
 "<ol><li>The four friends occupy adjacent chairs only at the end of Turn 2 and Turn 6.</li><li>Davies occupies Chair 2 after Turn 1 and Chair 4 after Turn 5, and Chhavi occupies Chair 7 after Turn 2.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Starting chairs", p("Davies doesn’t move in Turn 1, so he starts in Chair 2, with Chairs 1 and 3 empty. Chhavi doesn’t move before Turn 3, so she starts in Chair 7. Aslam is next to her: Chair 6 (Chair 1 must be empty). Bashir needs empty chairs on both sides: Chair 4.")),
       ("Turns 1 and 2", p("For all four to be adjacent after Turn 2, Aslam moves clockwise to Chair 1 and Bashir counter-clockwise to Chair 3: Chairs 7, 1, 2, 3.")),
       ("Turns 3 and 4", p("Davies is in Chair 4 after Turn 5 and moves only in Turn 4, so Chair 4 must be free then: Chhavi moves counter-clockwise to Chair 6 in Turn 3, and Davies moves clockwise to Chair 4 in Turn 4.")),
       ("Turns 5 to 7", p("For adjacency after Turn 6, Aslam moves counter-clockwise to Chair 7 and Bashir clockwise to Chair 5: Chairs 4, 5, 6, 7. In Turn 7 Chhavi leaves Chair 6 for Chair 1 or Chair 3.") +
          table(["After", "A", "B", "C", "D"], [["Start", "6", "4", "7", "2"], ["Turn 2", "1", "3", "7", "2"], ["Turn 4", "1", "3", "6", "4"], ["Turn 6", "7", "5", "6", "4"], ["Turn 7", "7", "5", "1/3", "4"]]) + p("A, B, C and D are Aslam, Bashir, Chhavi and Davies; the entries are chair numbers."))) +
 final("The table gives everyone’s chair after each stage."),
 p("Fix the start from what people hold before they have moved, then use the two adjacency moments to choose directions."),
 p("<b>Circular moves:</b> “first empty chair in the chosen direction” means skipping over occupied chairs. Track the empty chairs as carefully as the people."))
P.dq(11, "What is the number of the chair initially occupied by Bashir?", [], "TITA", "4", "Medium",
 "Davies is in 2 with 1 and 3 empty; Aslam and Chhavi are in 6 and 7.",
 steps(p("The only remaining chair with empty neighbours is 4.")) + final(r"\(4\)"))
P.dq(12, "Who sits on the chair numbered 4 at the end of Turn 3?", ["Bashir", "Chhavi", "Davies", "No one"], "MCQ", "4", "Medium",
 "Davies moves into Chair 4 in Turn 4.",
 steps(p("Bashir left Chair 4 in Turn 2, Chhavi went to 6 in Turn 3, and Davies arrives only in Turn 4. So it is empty.")) + final("No one, option 4"),
 [("1", "Bashir moved to Chair 3 in Turn 2."), ("2", "Chhavi moved to Chair 6."), ("3", "Davies arrives a turn later.")])
P.dq(13, "Which of the chairs are occupied at the end of Turn 6?", ["Chairs numbered 1, 2, 6, and 7", "Chairs numbered 2, 3, 4, and 5", "Chairs numbered 1, 2, 3, and 4", "Chairs numbered 4, 5, 6, and 7"], "MCQ", "4", "Medium",
 "All four are adjacent then, with Davies in 4 and Chhavi in 6.",
 steps(p("Aslam 7, Bashir 5, Chhavi 6, Davies 4.")) + final("Option 4"),
 [("1", "Davies is in Chair 4, not 2."), ("2", "Chhavi is in 6."), ("3", "Chhavi is in 6 and Aslam in 7.")])
P.dq(14, "Which of the following BEST describes the friends sitting on chairs adjacent to the one occupied by Bashir at the end of Turn 7?", ["Davies only", "Chhavi and Davies", "Aslam and Chhavi", "Chhavi only"], "MCQ", "1", "Medium",
 "Chhavi leaves Chair 6 in Turn 7.",
 steps(p("Bashir is in 5. Chair 4 has Davies; Chair 6 is now empty, because Chhavi moved to 1 or 3.")) + final("Davies only, option 1"),
 [("2", "Chhavi has left Chair 6."), ("3", "Aslam is in 7, not next to 5."), ("4", "Chhavi has left Chair 6.")])

# ---------------- Set 4: Tapping game ----------------
P.dilr_set(4, "Set 4 — Yes, no and maybe by foot taps", DIR,
 p("Alia, Badal, Clive, Dilshan, and Ehsaan played a game in which each asks a unique question to all the others and they respond by tapping their feet, either once or twice or thrice. One tap means “Yes”, two taps mean “No”, and three taps mean “Maybe”.") +
 p("A total of 40 taps were heard across the five questions. Each question received at least one “Yes”, one “No”, and one “Maybe.”") +
 p("The following information is known.") +
 "<ol><li>Alia tapped a total of 6 times and received 9 taps to her question. She responded “Yes” to the questions asked by both Clive and Dilshan.</li><li>Dilshan and Ehsaan tapped a total of 11 and 9 times respectively. Dilshan responded “No” to Badal.</li><li>Badal, Dilshan, and Ehsaan received equal number of taps to their respective questions.</li><li>No one responded “Yes” more than twice.</li><li>No one’s answer to Alia’s question matched the answer that Alia gave to that person’s question. This was also true for Ehsaan.</li><li>Clive tapped more times in total than Badal.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Alia’s row", p("She tapped 1 + 1 to Clive and Dilshan, leaving 4 for Badal and Ehsaan. 1 + 3 would be a third “Yes”, so both get “No” (2 + 2).")),
       ("Dilshan’s row", p("He tapped 2 for Badal and 9 for the other three: “Maybe” to Alia, Clive and Ehsaan.")),
       ("Taps received", p("40 = 9 (Alia) + 3p + q, where p is what Badal, Dilshan and Ehsaan each received and q is Clive’s. Each question has at least one of each answer (6 taps or more) and four answers. Badal already has two “No”s, which rules out p = 7, and q = 4 is too few. So p = 8 and q = 7.")),
       ("Badal and Clive", p("Badal + Clive tapped 40 − 6 − 11 − 9 = 14, Clive more than Badal. Badal at 5 would need three “Yes”s, not allowed; so Badal 6 (1, 1, 2, 2) and Clive 8.")),
       ("The grid", p("Using rule 5 for Alia and Ehsaan fills in the rest. Rows are who answered; columns are whose question.") +
          table(["", "A", "B", "C", "D", "E"], [["A", "–", "N", "Y", "Y", "N"], ["B", "Y", "–", "N", "N", "Y"], ["C", "N", "Y", "–", "M", "N"], ["D", "M", "N", "M", "–", "M"], ["E", "M", "M", "Y", "N", "–"]]) +
          p("Taps received: Alia 9, Badal 8, Clive 7, Dilshan 8, Ehsaan 8. Taps given: Alia 6, Badal 6, Clive 8, Dilshan 11, Ehsaan 9."))) +
 final("The grid above is the only arrangement."),
 p("Start with the rows that are almost fixed (Alia, Dilshan), then use the 40-tap total to find how many taps each question got."),
 p("<b>Response grids:</b> put answerers in rows and questions in columns. Row totals and column totals come from different clues; “at least one of each” sets a floor of 6 taps per question."))
P.dq(15, "How many taps did Clive receive for his question?", [], "TITA", "7", "Hard",
 "Write the 40 taps as Alia’s 9 plus three equal amounts plus Clive’s.",
 steps(p(r"\(9 + 3p + q = 40\). The only workable choice is \(p = 8\), so \(q = 7\).")) + final(r"\(7\)"))
P.dq(16, "Which two people tapped an equal number of times in total?", ["Badal and Dilshan", "Clive and Ehsaan", "Dilshan and Clive", "Alia and Badal"], "MCQ", "4", "Hard",
 "Badal and Clive share 14 taps, with Clive ahead.",
 steps(p("Badal tapped 6 and Clive 8; Alia also tapped 6.")) + final("Alia and Badal, option 4"),
 [("1", "Badal 6, Dilshan 11."), ("2", "Clive 8, Ehsaan 9."), ("3", "Dilshan 11, Clive 8.")])
P.dq(17, "What was Clive’s response to Ehsaan’s question?", ["Yes", "Maybe", "Cannot be determined", "No"], "MCQ", "4", "Hard",
 "Ehsaan answered Clive “Yes”. By rule 5, Clive’s answer to Ehsaan must differ.",
 steps(p("Clive’s row adds to 8 with A = 2 (not Yes, since Alia said Yes to him), B = 1 and D = 3. That leaves 2 for Ehsaan: “No”.")) + final("No, option 4"),
 [("1", "Ehsaan said Yes to Clive, so Clive can’t say Yes back."), ("2", "That would make Clive’s total 9."), ("3", "The totals fix it.")])
P.dq(18, "How many “Yes” responses were received across all the questions?", [], "TITA", "6", "Medium",
 "Count the Y entries in the grid.",
 steps(p("Alia 2, Badal 2, Clive 1, Ehsaan 1, Dilshan 0: 6.")) + final(r"\(6\)"))

# ---------------- Set 5: Tariffs and trade ----------------
P.dilr_set(5, "Set 5 — Tariffs between five countries", DIR,
 p("Five countries engage in trade with each other. Each country levies import tariffs on the other countries. The import tariff levied by Country X on Country Y is calculated by multiplying the corresponding tariff percentage with the total imports of Country X from Country Y.") +
 p("The radar chart below depicts different import tariff percentages charged by each of the five countries on the others. For example, US (the blue line in the chart) charges 20%, 40%, 30%, and 30% import tariff percentages on imports from France, India, Japan, and UK, respectively. The bar chart depicts the import tariffs levied by each country on other countries. For example, US charged import tariff of 3 billion USD on UK.") +
 F.RADAR + F.BARS +
 p("Assume that imports from one country to another equals the exports from the latter to the former.") +
 p("The trade surplus of Country X with Country Y is defined as follows. Trade surplus = Exports from Country X to Country Y – Imports to Country X from Country Y.") +
 p("A negative trade surplus is called trade deficit."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Imports", p("Imports of X from Y = tariff collected ÷ tariff rate. For example, the US collects 6 billion on France at 20%, so it imports 30 billion from France.")),
       ("The import table", "<ul><li>US imports: France 30, India 11.25, Japan 23.3, UK 10</li><li>France imports: US 18.3, India 16.25, Japan 13.3, UK 11.25</li><li>India imports: US 22.5, France 10, Japan 7, UK 25</li><li>Japan imports: US 10, France 10, India 16, UK 7.5</li><li>UK imports: US 12.5, France 13.3, India 10, Japan 15</li></ul>" +
          p("All figures are in billion USD. A country’s exports to X are X’s imports from it."))) +
 final("All imports follow from tariff ÷ rate; see the table."),
 p("Read each bar with the matching percentage: import = tariff ÷ rate. Exports are just the other country’s imports."),
 p(r"<b>Tariff arithmetic:</b> \(\text{tariff} = \text{rate} \times \text{imports}\), so \(\text{imports} = \frac{\text{tariff}}{\text{rate}}\)."))
P.dq(19, "How much is Japan's export to India worth?", ["8.5 Billion USD", "7.0 Billion USD", "16.0 Billion USD", "1.75 Billion USD"], "MCQ", "2", "Easy",
 "It equals India’s imports from Japan.",
 steps(p(r"India charges Japan 3.5 billion at 50%: \(3.5 \div 0.5 = 7\).")) + final("7.0 billion, option 2"),
 [("1", "This adds the tariffs instead of dividing."), ("3", "16 is Japan’s imports from India."), ("4", "This multiplies by 50% instead of dividing.")])
P.dq(20, "Which among the following is the highest?", ["Exports by France to Japan", "Imports by France from India", "Imports by US from France", "Exports by Japan to UK"], "MCQ", "3", "Medium",
 "Turn each into an import, then compute tariff ÷ rate.",
 steps(p(r"France → Japan = Japan’s imports from France: \(3 \div 0.3 = 10\). France from India: \(6.5 \div 0.4 = 16.25\). US from France: \(6 \div 0.2 = 30\). Japan → UK = UK’s imports from Japan: \(6 \div 0.4 = 15\).")) + final("Imports by US from France, option 3"),
 [("1", "10 billion."), ("2", "16.25 billion."), ("4", "15 billion.")])
P.dq(21, "What is the trade surplus/trade deficit of India with UK?", ["Deficit of 10.0 Billion USD", "Surplus of 15.0 Billion USD", "Surplus of 10.0 Billion USD", "Deficit of 15.0 Billion USD"], "MCQ", "4", "Medium",
 "India’s exports to the UK are the UK’s imports from India.",
 steps(p(r"Exports: UK’s imports from India \(= 3 \div 0.3 = 10\). Imports: India from UK \(= 5 \div 0.2 = 25\). Surplus \(= 10 - 25 = -15\), a deficit of 15.")) + final("Deficit of 15 billion, option 4"),
 [("1", "The gap is 15, not 10."), ("2", "The sign is reversed."), ("3", "10 is India’s exports, not the balance.")])
P.dq(22, "Among France and UK, who has/have trade surplus(es) with US?", ["Neither France nor UK", "Both France and UK", "Only France", "Only UK"], "MCQ", "3", "Medium",
 "Compare each country’s exports to the US with its imports from the US.",
 steps(("France", p(r"Exports to the US \(= 30\); imports from the US \(= 5.5 \div 0.3 \approx 18.3\). Surplus.")),
       ("UK", p(r"Exports to the US \(= 3 \div 0.3 = 10\); imports from the US \(= 2.5 \div 0.2 = 12.5\). Deficit."))) + final("Only France, option 3"),
 [("1", "France has a surplus."), ("2", "The UK has a deficit of 2.5."), ("4", "The UK is the one in deficit.")])
