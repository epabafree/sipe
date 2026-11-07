# -*- coding: utf-8 -*-
# Batch 12 — CAT 2020 Slot 2: DILR sets 1–5 (Q1–24, exam order).
from fmt import steps, final, trap, why, table, p
from b12_20s2 import P

def grid(rows):
    rows = [r.split() if " " in r else list(r) for r in rows]
    hi = {(i, j + 1) for i, r in enumerate(rows) for j, x in enumerate(r) if x == "R"}
    return table(["", "1", "2", "3", "4", "5"], [[str(i + 1)] + r for i, r in enumerate(rows)], hi=hi)

# ---------------- Set 1: Departmental stores ----------------
SALES = table(["", "Delhi 2018", "Delhi 2019", "Mumbai 2018", "Mumbai 2019", "Bengaluru 2018", "Bengaluru 2019", "Kolkata 2018", "Kolkata 2019"],
              [["Apparels", "—", "—", "—", "—", "—", "—", "—", "54"], ["Electronics", "78", "98", "82", "102", "90", "70", "80", "100"],
               ["Home Decor", "—", "100", "—", "72", "—", "80", "—", "54"]])
P.dilr_set(1, "Set 1 — Sales across four cities", "Read the following passage carefully and answer the questions that follow.",
 p("A chain of departmental stores has outlets in Delhi, Mumbai, Bengaluru and Kolkata. The sales are categorized by its three departments — ‘Apparel’, ‘Electronics’, and ‘HomeDecor’. An Accountant has been asked to prepare a summary of the 2018 and 2019 sales amounts for an internal report. He has collated partial information and prepared the following table.") +
 p("<b>Sales Amounts (Crore Rupees)</b>") + SALES +
 p("The following additional information is known:") +
 "<ol><li>The sales amounts in the Apparel departments were the same for Delhi and Kolkata in 2018.</li><li>The sales amounts in the Apparel departments were the same for Mumbai and Bengaluru in 2018. This sales amount matched the sales amount in the Apparel department for Delhi in 2019.</li><li>The sales amounts in the Home Decor departments were the same for Mumbai and Kolkata in 2018.</li><li>The sum of the sales amounts of four Electronics departments increased by the same amount as the sum of the sales amounts of four Apparel departments from 2018 to 2019.</li><li>The total sales amounts of the four Home Decor departments increased by ₹70 Crores from 2018 to 2019.</li><li>The sales amounts in the Home Decor departments of Delhi and Bengaluru each increased by ₹20 Crores from 2018 to 2019.</li><li>The sales amounts in the Apparel departments of Delhi and Bengaluru each increased by the same amount in 2019 from 2018. The sales amounts in the Apparel departments of Mumbai and Kolkata also each increased by the same amount in 2019 from 2018.</li><li>The sales amounts in the Apparel departments of Delhi, Kolkata and Bengaluru in 2019 followed an Arithmetic Progression.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("Home Decor", p("2019 total: 306, so 2018 total 236. Delhi 80 and Bengaluru 60 in 2018 (fact 6), leaving 96 for Mumbai and Kolkata: 48 each.")),
       ("Apparel", p("Electronics rose by 370 − 330 = 40, so Apparel did too. Let Delhi and Kolkata start at a, Mumbai and Bengaluru at b; Delhi and Bengaluru rise by x, Mumbai and Kolkata by y. Then b = a + x (fact 2), a + y = 54, x + y = 20, and the AP gives 2 × 54 = b + (b + x). Solving: x = 8, y = 12, a = 42, b = 50.") +
       table(["", "Delhi", "Mumbai", "Bengaluru", "Kolkata"],
             [["Apparel 2018 → 2019", "42 → 50", "50 → 62", "50 → 58", "42 → 54"], ["Electronics", "78 → 98", "82 → 102", "90 → 70", "80 → 100"], ["Home Decor", "80 → 100", "48 → 72", "60 → 80", "48 → 54"]]))) +
 final("Every cell is fixed."),
 p("Home Decor is quickest; then turn the Apparel facts into a few equations."),
 p("<b>Partial tables:</b> name the unknowns using the ‘same as’ facts first, so there are as few letters as possible."))
P.dq(1, "In Home Decor departments of which cities were the sales amounts the highest in 2018 and 2019, respectively?", ["Bengaluru and Delhi", "Delhi and Delhi", "Mumbai and Delhi", "Mumbai and Mumbai"], "MCQ", "2", "Medium",
 "Work out the 2018 Home Decor row.",
 steps(("From the set solution", p("2018: Delhi 80 is highest. 2019: Delhi 100 is highest."))) + final("Option 2"),
 [("1", "Bengaluru had 60 in 2018."), ("3", "Mumbai had 48 in 2018."), ("4", "Mumbai had 48 and 72.")])
P.dq(2, "What was the increase in sales amount, in Crore Rupees, in the Apparel department of Mumbai from 2018 to 2019?", ["8", "12", "10", "5"], "MCQ", "2", "Medium",
 "Mumbai and Kolkata rise by the same amount.",
 steps(("From the set solution", p("y = 12."))) + final("12, option 2"),
 [("1", "That is the Delhi/Bengaluru rise."), ("3", "Not a solution."), ("4", "Not a solution.")])
P.dq(3, "Among all the 12 departments (i.e., the 3 departments in each of the 4 cities), what was the maximum percentage increase in sales amount from 2018 to 2019?", ["50", "75", "25", "28"], "MCQ", "1", "Medium",
 "Look for a small 2018 value with a big rise.",
 steps(("From the set solution", p("Mumbai Home Decor: 48 → 72, a 50% rise. Nothing else comes close."))) + final("50, option 1"),
 [("2", "No department rose that much."), ("3", "Delhi Home Decor or Kolkata Electronics."), ("4", "Kolkata Apparel, 42 → 54.")])
P.dq(4, "What was the total sales amount, in Crore Rupees, in 2019 for the chain of departmental stores?", ["750", "900", "600", "150"], "MCQ", "2", "Medium",
 "Add the three 2019 rows.",
 steps(("Adding", p("Apparel 224 + Electronics 370 + Home Decor 306 = 900."))) + final("900, option 2"),
 [("1", "Too low."), ("3", "Too low."), ("4", "Far too low.")])

# ---------------- Set 2: Election ----------------
VOTES = table(["", "A", "B", "C", "D"],
              [["No. of candidates contesting", "10", "12", "5", "8"], ["Total No. of valid votes polled", "5,00,000", "3,25,000", "6,00,030", ""],
               ["No. of votes polled by the winning candidate", "2,75,000", "48,750", "", ""], ["No. of votes polled by the first runner up", "95000", "", "", "37,500"],
               ["No. of votes polled by the second runner up", "", "", "", "30,000"], ["% of valid votes polled by the third runner up", "", "", "", "10%"]])
P.dilr_set(2, "Set 2 — Four constituencies", "Read the following passage carefully and answer the questions that follow.",
 p("In an election several candidates contested for a constituency. In any constituency, the winning candidate was the one who polled the highest number of votes, the first runner up was the one who polled the second highest number of votes, the second runner up was the one who polled the third highest number of votes, and so on. There were no ties (in terms of number of votes polled by the candidates) in any of the constituencies in this election.") +
 p("In an electoral system, a security deposit is the sum of money that a candidate is required to pay to the election commission before he or she is permitted to contest. Only the defeated candidates (i.e, one who is not the winning candidate) who fail to secure more than one sixth of the valid votes polled in the constituency, lose their security deposits.") +
 p("The following table provides some incomplete information about votes polled in four constituencies: A, B, C and D, in this election.") + VOTES +
 p("The following additional facts are known:") +
 "<ol><li>The first runner up polled 10,000 more votes than the second runner up in constituency A.</li><li>None of the candidates who contested in constituency C lost their security deposit. The difference in votes polled by any pair of candidates in this constituency was at least 10,000.</li><li>The winning candidate in constituency D polled 5% of valid votes more than that of the first runner up. All the candidates who lost their security deposits while contesting for this constituency, put together, polled 35% of the valid votes.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("A", p("Second runner up: 85,000, which is above one sixth (83,333). The other 7 share 45,000 and all lose their deposits.")),
       ("B", p("The winner has 48,750, below one sixth of 3,25,000 (54,167). So all 11 defeated candidates are below it too and lose their deposits: 2,76,250 votes.")),
       ("C", p("Each defeated candidate needs more than 1,00,005, and they differ by at least 10,000: at least 1,00,006 + 1,10,006 + 1,20,006 + 1,30,006 = 4,60,024. The winner then has at most 1,40,006, and must beat 1,30,006 by 10,000: exactly 1,40,006.")),
       ("D", p("With V valid votes, the winner has 37,500 + 0.05V. The third runner up (10%) and everyone below lose deposits; the second runner up keeps it. So (37,500 + 0.05V) + 37,500 + 30,000 + 0.35V = V, giving V = 1,75,000 and the winner 46,250."))) +
 final("A: 7 lose deposits; B: 11; C: none; D: losers poll 61,250."),
 p("Work out each constituency separately. ‘More than one sixth’ is the line to check every time."),
 p("<b>Thresholds:</b> compare each known vote count with one sixth of the valid votes before anything else; it tells you who loses a deposit."))
P.dq(5, "What is the percentage of votes polled in total by all the candidates who lost their security deposits while contesting for constituency A?", [], "TITA", "9", "Medium",
 "Only the seven candidates below the second runner up lose deposits.",
 steps(("From the set solution", p(r"\(\tfrac{45000}{500000} = 9\%\)."))) + final(r"\(9\)"))
P.dq(6, "How many candidates who contested in constituency B lost their security deposit?", [], "TITA", "11", "Medium",
 "Even the winner is below one sixth.",
 steps(("From the set solution", p("All 11 defeated candidates."))) + final(r"\(11\)"))
P.dq(7, "What BEST can be concluded about the number of votes polled by the winning candidate in constituency C?", ["between 1,40,005 and 1,40,010", "1,40,006", "1,40,010", "less than 2,00,010"], "MCQ", "2", "Hard",
 "Push the four losers as low as the rules allow.",
 steps(("From the set solution", p("The bounds meet at exactly 1,40,006."))) + final("1,40,006, option 2"),
 [("1", "True but not the best conclusion."), ("3", "Too many."), ("4", "True but much weaker.")])
P.dq(8, "What was the number of valid votes polled in constituency D?", ["1,75,000", "62,500", "1,25,000", "1,50,000"], "MCQ", "1", "Medium",
 "Add the winner, the two runners up and the deposit-losers.",
 steps(("From the set solution", p(r"\(105000 + 0.4V = V\), so \(V = 175000\)."))) + final("1,75,000, option 1"),
 [("2", "Too small for the known votes."), ("3", "Doesn’t balance."), ("4", "Doesn’t balance.")])
P.dq(9, "The winning margin of a constituency is defined as the difference of votes polled by the winner and that of the first runner up. Which of the following CANNOT be the list of constituencies, in increasing order of winning margin?", ["B, D, C, A", "D, B, C, A", "D, C, B, A", "B, C, D, A"], "MCQ", "4", "Hard",
 "Margins: A 1,80,000; C 10,000; D 8,750; B somewhere below about 23,600.",
 steps(("Margins", p("D’s 8,750 is always below C’s 10,000, and A is always largest. B can fall anywhere below A.")),
       ("Choosing", p("Option 4 puts C before D, which can’t happen."))) + final("Option 4"),
 [("1", "Possible if B’s margin is under 8,750."), ("2", "Possible if B is between D and C."), ("3", "Possible if B is above 10,000.")])
P.dq(10, "For all the four constituencies taken together, what was the approximate number of votes polled by all the candidates who lost their security deposit expressed as a percentage of the total valid votes from these four constituencies?", ["32.00%", "23.91%", "38.25%", "23.54%"], "MCQ", "2", "Hard",
 "Add the deposit-losers’ votes from each constituency.",
 steps(("Totals", p("Losers: 45,000 + 2,76,250 + 0 + 61,250 = 3,82,500. Valid votes: 16,00,030.")),
       ("Percentage", p("About 23.91%."))) + final("23.91%, option 2"),
 [("1", "Too high."), ("3", "Too high."), ("4", "Close, but not the computed value.")])

# ---------------- Set 3: Beads ----------------
P.dilr_set(3, "Set 3 — Twenty-five beads", "Read the following passage carefully and answer the questions that follow.",
 p("Twenty five coloured beads are to be arranged in a grid comprising of five rows and five columns. Each cell in the grid must contain exactly one bead. Each bead is coloured either Red, Blue or Green.") +
 p("While arranging the beads along any of the five rows or along any of the five columns, the rules given below are to be followed:") +
 "<ol><li>Two adjacent beads along the same row or column are always of different colours.</li><li>There is at least one Green bead between any two Blue beads along the same row or column.</li><li>There is at least one Blue and at least one Green bead between any two Red beads along the same row or column.</li></ol>" +
 p("Every unique, complete arrangement of twenty five beads is called a configuration."),
 "DILR::LR::Puzzles",
 steps(("One line at a time", p("Reds must be at least three apart in a row (an R, then both a B and a G, then R), so a row or column holds at most 2 Reds. Blues must have a Green between them, and no two neighbours match.")),
       ("Two colours", p("Red can’t pair with either colour alone: Red–Blue–Red lacks a Green, Red–Green–Red lacks a Blue. Blue and Green alternating in a chessboard works, in 2 ways (Blue or Green in the corner).")),
       ("Most Reds", p("A diagonal pattern reaches 9 Reds:") +
          grid(["RBGRB", "GRBGR", "BGRBG", "RBGRB", "GRBGR"])),
       ("Fewest Blues", p("Greens can sit between Blues and between Reds, so lean on Green. Each line needs at least one Blue, and the minimum is 6:") +
          grid(["RBGRG", "BGRGB", "GRGBG", "RGBGR", "GBGRG"]))) +
 final("Two-colour configurations: 2. Most Reds: 9. Fewest Blues: 6."),
 p("Work out what a single row can look like first; the grid answers follow from patterns that repeat diagonally."),
 p("<b>Grid colourings:</b> a pattern that shifts by one each row (a diagonal pattern) satisfies row and column rules at the same time."))
P.dq(11, "The total number of possible configurations using beads of only two colours is:", [], "TITA", "2", "Medium",
 "Which pair of colours can work without the third?",
 steps(("From the set solution", p("Only Blue and Green, alternating, in 2 ways."))) + final(r"\(2\)"))
P.dq(12, "What is the maximum possible number of Red beads that can appear in any configuration?", [], "TITA", "9", "Hard",
 "At most 2 Reds per row; the diagonal pattern gets close.",
 steps(("From the set solution", p("The repeating diagonal R-B-G pattern places 9 Reds, and 10 isn’t possible."))) + final(r"\(9\)"))
P.dq(13, "What is the minimum number of Blue beads in any configuration?", [], "TITA", "6", "Hard",
 "Use Greens as separators wherever possible.",
 steps(("From the set solution", p("6 Blues, as in the grid shown; fewer leaves some row or column with Reds and no Blue between them."))) + final(r"\(6\)"))
P.dq(14, "Two Red beads have been placed in ‘second row, third column’ and ‘third row, second column’. How many more Red beads can be placed so as to maximise the number of Red beads used in the configuration?", [], "TITA", "6", "Hard",
 "With these two fixed, the best diagonal pattern changes.",
 steps(("A pattern", grid(["RBGRB", "BGRBG", "GRBGR", "RBGRB", "BGRBG"]) +
          p("This has 8 Reds, including the two placed, and 8 is the most possible with them fixed. So 6 more."))) + final(r"\(6\)"))

# ---------------- Set 4: Seminars ----------------
P.dilr_set(4, "Set 4 — Eight seminars", "Read the following passage carefully and answer the questions that follow.",
 p("The Humanities department of a college is planning to organize eight seminars, one for each of the eight doctoral students – A, B, C, D, E, F, G and H. Four of them are from Economics, three from Sociology and one from Anthropology department. Each student is guided by one among P, Q, R, S and T. Two students are guided by each of P, R and T, while one student is guided by each of Q and S. Each student is guided by a guide belonging to their department.") +
 p("Each seminar is to be scheduled in one of four consecutive 30-minute slots starting at 9:00 a.m., 9:30 a.m., 10:00 a.m. and 10:30 a.m. on the same day. More than one seminars can be scheduled in a slot, provided the guide is free. Only three rooms are available and hence at the most three seminars can be scheduled in a slot. Students who are guided by the same guide must be scheduled in consecutive slots.") +
 p("The following additional facts are also known:") +
 "<ol><li>Seminars by students from Economics are scheduled in each of the four slots.</li><li>A’s is the only seminar that is scheduled at 10:00 a.m. A is guided by R.</li><li>F is an Anthropology student whose seminar is scheduled at 10:30 a.m.</li><li>The seminar of a Sociology student is scheduled at 9:00 a.m.</li><li>B and G are both Sociology students, whose seminars are scheduled in the same slot. The seminar of an Economics student, who is guided by T, is also scheduled in the same slot.</li><li>P, who is guiding both B and C, has students scheduled in the first two slots.</li><li>A and G are scheduled in two consecutive slots.</li></ol>",
 "DILR::LR::Scheduling",
 steps(("Slots", p("A, alone at 10:00, must be the Economics seminar there. G is next to A, and B and G share a slot within P’s first two slots, so B and G are at 9:30 with T’s Economics student. P’s other student, C, is at 9:00 and is the Sociology student there.")),
       ("Guides", p("P guides Sociology (B, C). G needs another Sociology guide and F an Anthropology guide: these are Q and S, one each. So R and T guide Economics: R has A (10:00) and the 10:30 Economics student; T has the 9:30 one and the 9:00 one.") +
       table(["Slot", "Seminars"], [["9:00", "C (P), Economics (T)"], ["9:30", "B (P), G (Q or S), Economics (T)"], ["10:00", "A (R)"], ["10:30", "F (S or Q), Economics (R)"]]) +
       p("D, E and H are the three Economics students in the 9:00, 9:30 and 10:30 slots, in some order."))) +
 final("Open: which of D, E, H goes where, and whether Q guides G or F."),
 p("Facts 2, 5, 6 and 7 together pin down the 9:30 slot. Start there."),
 p("<b>Scheduling with guides:</b> ‘same guide, consecutive slots’ is the strongest rule; use it to place pairs."))
P.dq(15, "Which one of the following statements is true?", ["Two seminars are scheduled in the first slot.", "Three seminars are scheduled in the last slot.", "Only one seminar is scheduled in the second slot.", "Three seminars are scheduled in the first slot."], "MCQ", "1", "Medium",
 "Count the 9:00 slot.",
 steps(("From the set solution", p("9:00 has C and one Economics student."))) + final("Option 1"),
 [("2", "10:30 has two."), ("3", "9:30 has three."), ("4", "9:00 has two.")])
P.dq(16, "Who all are NOT guiding any Economics students?", ["P, Q and R", "P, Q and S", "Q, R and S", "P, R and S"], "MCQ", "2", "Medium",
 "R and T guide the Economics students.",
 steps(("From the set solution", p("P (Sociology), Q and S (Sociology and Anthropology)."))) + final("Option 2"),
 [("1", "R guides A."), ("3", "R guides A."), ("4", "R guides A.")])
P.dq(17, "Which of the following statements is necessarily true?", ["S is guiding F.", "H is an Economics student.", "Q is guiding G.", "B is scheduled in the first slot."], "MCQ", "2", "Medium",
 "Which students are left for Economics?",
 steps(("From the set solution", p("D, E and H are all Economics students."))) + final("Option 2"),
 [("1", "Could be Q."), ("3", "Could be S."), ("4", "B is at 9:30.")])
P.dq(18, "If D is scheduled in a slot later than Q’s, then which of the following two statement(s) is (are) true?<br>(i) E and H are guided by T.<br>(ii) G is guided by Q.", ["Both (i) and (ii)", "Neither (i) nor (ii)", "Only (i)", "Only (ii)"], "MCQ", "1", "Hard",
 "Q’s student is G (9:30) or F (10:30).",
 steps(("Working it through", p("If Q guided F at 10:30, nothing could be later. So Q guides G, D is at 10:30 with R, and E and H are T’s students at 9:00 and 9:30."))) + final("Both, option 1"),
 [("2", "Both hold."), ("3", "(ii) holds too."), ("4", "(i) holds too.")])
P.dq(19, "If E and Q are both scheduled in the same slot, then which of the following statements BEST describes the relationship between D, H, and T?", ["Both D and H are guided by T.", "Neither D nor H is guided by T.", "At least one of D and H is guided by T.", "Exactly one of D and H is guided by T."], "MCQ", "3", "Hard",
 "E is with G at 9:30, or with F at 10:30.",
 steps(("Two cases", p("E at 9:30 (T): D and H are at 9:00 (T) and 10:30 (R): exactly one with T. E at 10:30 (R): D and H are at 9:00 and 9:30, both with T.")),
       ("Best description", p("At least one of D and H is guided by T."))) + final("Option 3"),
 [("1", "Only in one case."), ("2", "Never."), ("4", "Only in one case.")])
P.dq(20, "If D is scheduled in the slot immediately before Q’s, then which of the following is NOT necessarily true?", ["E is guided by R.", "F is guided by S.", "D is guided by T.", "G is guided by Q."], "MCQ", "1", "Hard",
 "Q’s student can’t be F, because 10:00 is only A’s.",
 steps(("Working it through", p("Q guides G at 9:30, so D is at 9:00 with T, and S guides F. E is at 9:30 (T) or 10:30 (R)."))) + final("Option 1"),
 [("2", "Necessarily true."), ("3", "Necessarily true."), ("4", "Necessarily true.")])

# ---------------- Set 5: Parking ----------------
P.dilr_set(5, "Set 5 — A narrow parking lot", "Read the following passage carefully and answer the questions that follow.",
 p("A shopping mall has a large basement parking lot with parking slots painted in it along a single row. These slots are quite narrow; a compact car can fit in a single slot but an SUV requires two slots. When a car arrives, the parking attendant guides the car to the first available slot from the beginning of the row into which the car can fit.") +
 p("For our purpose, cars are numbered according to the order in which they arrive at the lot. For example, the first car to arrive is given a number 1, the second a number 2, and so on. This numbering does not indicate whether a car is a compact or an SUV. The configuration of a parking lot is a sequence of the car numbers in each slot. Each single vacant slot is represented by letter V.") +
 p("For instance, suppose cars numbered 1 through 5 arrive and park, where cars 1, 3 and 5 are compact cars and 2 and 4 are SUVs. At this point, the parking lot would be described by the sequence 1, 2, 3, 4, 5. If cars 2 and 5 now vacate their slots, the parking lot would now be described as 1, V, V, 3, 4. If a compact car (numbered 6) arrives subsequently followed by an SUV (numbered 7), the parking lot would be described by the sequence 1, 6, V, 3, 4, 7.") +
 p("Answer the following questions INDEPENDENTLY of each other."),
 "DILR::LR::Puzzles",
 steps(("How to read a sequence", p("Each number is one car, whatever its size. A V is one empty slot. A gap of two slots is two Vs, so an SUV can’t fit into a single V.")),
       ("How to work", p("Replay the arrivals and departures slot by slot. Each new car takes the first gap from the left that is wide enough."))) +
 final("Each question is a separate replay."),
 p("Draw the slots, not the sequence. An SUV takes two boxes."),
 p("<b>Simulation sets:</b> when the rules are mechanical, the safest method is to replay them exactly rather than reason about the end state."))
P.dq(21, "Initially cars numbered 1, 2, 3, and 4 arrive among which 1 and 4 are SUVs while 2 and 3 are compact cars. Car 1 then leaves, followed by the arrivals of car 5 (a compact car) and car 6 (an SUV). Car 4 then leaves. Then car 7 (an SUV) and car 8 (a compact car) arrive. At this moment, which among the following numbered car is parked next to car 3?",
 ["6", "5", "8", "7"], "MCQ", "4", "Medium",
 "Slots 1–2 are car 1’s. Follow each step.",
 steps(("Replay", p("1 1 2 3 4 4 → car 1 leaves → 5 takes slot 1 → 6 goes after 4 (slots 7–8) → 4 leaves → 7 takes slots 5–6 → 8 takes slot 2.")),
       ("Result", p("5, 8, 2, 3, 7, 6: car 3 sits between 2 and 7."))) + final("7, option 4"),
 [("1", "Car 6 is at the end."), ("2", "Car 5 is in slot 1."), ("3", "Car 8 is in slot 2.")])
P.dq(22, "Suppose eight cars have arrived, of which two have left. Also suppose that car 4 is a compact and car 7 is an SUV. Which of the following is a POSSIBLE current configuration of the parking lot?", ["V, 2, 3, 7, 5, 6, 8", "8, 2, 3, V, 6, 5, 7", "8, 2, 3, V, 5, 7, 6", "8, 2, 3, V, 5, 6, 7"], "MCQ", "4", "Hard",
 "An SUV can’t take a single slot left by a compact.",
 steps(("Option 4", p("Cars 1 (compact) and 4 (compact) leave; 8 later takes car 1’s slot. 5, 6 and 7 parked after 4, and 4’s slot is the V. This works.")),
       ("The others", p("In option 1, SUV 7 sits where compact 4 was, with no room. In options 2 and 3, 5, 6 and 7 are out of arrival order with no gap that would explain it."))) +
 final("Option 4"),
 [("1", "SUV 7 can’t fit in compact 4’s single slot."), ("2", "6 can’t be parked before 5 here."), ("3", "7 can’t be parked before 6 here.")])
P.dq(23, "Suppose the sequence at some point of time is 4, 5, 6, V, 3. Which of the following is NOT necessarily true?", ["Car 1 is an SUV.", "Car 5 is a compact.", "Car 4 is a compact.", "Car 3 is an SUV."], "MCQ", "4", "Hard",
 "Cars 1 and 2 have left. Replay the cases that give this sequence.",
 steps(("What must hold", p("Every history that produces this sequence has car 1 an SUV and cars 4 and 5 compact. Car 3 can be either size."))) + final("Option 4"),
 [("1", "Always true."), ("2", "Always true."), ("3", "Always true.")])
P.dq(24, "Suppose that car 4 is not the first car to leave and that the sequence at a time between the arrival of the car 7 and car 8 is V, 7, 3, 6, 5. Then which of the following statements MUST be false?",
 ["Car 2 is a compact.", "Car 7 is a compact.", "Car 4 is an SUV.", "Car 6 is a compact."], "MCQ", "4", "Hard",
 "Cars 1, 2 and 4 have left. Where could car 6 have parked?",
 steps(("Replay", p("In every history that fits, car 6 takes two slots: it is an SUV. Car 2 and car 7 are compacts and car 4 an SUV."))) + final("Option 4"),
 [("1", "Always true here."), ("2", "Always true here."), ("3", "Always true here.")])
