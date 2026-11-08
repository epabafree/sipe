# -*- coding: utf-8 -*-
# Simp Mock 1 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_01 import P
import charts

DIR = "Read the information below and answer the questions that follow."
PRICE = "<p><b>Additional information for this question:</b> Due to the great demand in slot 1, ticket price was increased by 10% in slot 2. The ticket price was further increased by 10% in slot 3 as compared to slot 2. Similarly, the ticket price was further increased by 10% in slot 4 as compared to slot 3. The same pricing is applicable for all 5 days.</p>"

# ---------------- Set 1: Concert tickets (Q1–4) ----------------
S1 = [13000, 14000, 13500, 11000, 12000]; S2 = [12500, 9500, 13500, 12000, 10500]; S3 = [11500, 12000, 10500, 13000, 14500]
S4 = [45000 - a - b - c for a, b, c in zip(S1, S2, S3)]
K = lambda x: f"{x / 1000:g}"
TICK = table(["Slot", "D1", "D2", "D3", "D4", "D5"],
             [[str(i + 1), *[K(x) for x in S]] for i, S in enumerate([S1, S2, S3, S4])])
FIG1 = charts.hbar_stacked("sipe_SM25-01_DILR_S1", ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"],
                           [("Slot 1: 9:00–9:05", S1), ("Slot 2: 9:05–9:10", S2), ("Slot 3: 9:10–9:15", S3)], 40000, 5000,
                           "Stacked bars of tickets booked in the first three five-minute slots for each of the five days", xlabel="Tickets booked by 9:15 AM")
P.dilr_set(1, "Set 1 — Concert tickets", DIR,
 p("A British rock band is performing in India for the first time in Mumbai for 5 consecutive days from 27th December 2025 to 31st December 2025. The booking for all days started at 9:00 AM on 1st December 2025. "
   "The total number of tickets available for each day is 45,000. All the tickets for all the five days were booked merely in the first 20 minutes. "
   "The number of tickets booked till 9:15 AM in three slots of five minutes each is given in the graph below. (All the values in the graph are multiples of 500.)") + FIG1 +
 p("Slot 4 is 9:15 AM to 9:20 AM."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Read the chart", p("Each bar is split into the three slots; the numbers on the segments are the tickets booked in that slot.")),
       ("Slot 4", p("Every day sells all 45,000 tickets by 9:20, so slot 4 = 45,000 − (slots 1 to 3).") + p("Tickets in thousands; D1–D5 are the days.") + TICK + p("Slot totals over the five days: 63.5, 58, 61.5 and 42 thousand."))) +
 final("Slot totals: 63,500, 58,000, 61,500 and 42,000."),
 p("For revenue with a 10% rise each slot, compare tickets × 1, × 1.1, × 1.21, × 1.331."),
 p("<b>Stacked bars:</b> read each segment’s own length, not where it ends."))

P.dq(1, "What is the average number of tickets sold from 9:15 AM to 9:20 AM for booking over 5 days?", [], "TITA", "8400", "Easy",
 "Slot 4 each day = 45,000 minus what was booked by 9:15.",
 steps(("Slot 4 by day", p("Day 1: 45,000 − 37,000 = 8,000. Day 2: 9,500. Day 3: 7,500. Day 4: 9,000. Day 5: 8,000.")),
       ("Average", p("42,000 ÷ 5 = 8,400."))) + final("8400"))
P.dq(2, "For the booking slots from 9:00 AM to 9:15 AM, in which slot the highest number of tickets were booked (combined all 5 days)?", ["Slot 1", "Slot 2", "Slot 3", "Cannot be determined"], "MCQ", "1", "Easy",
 "Add each slot across the five days.",
 steps(("Totals", p("Slot 1: 63,500. Slot 2: 58,000. Slot 3: 61,500."))) + final("Slot 1, option 1"),
 [("2", "58,000, the least of the three."), ("3", "61,500."), ("4", "The chart gives every value.")])
P.dq(3, PRICE + "<p>In which slot, the highest revenue was received?</p>", ["Slot 1", "Slot 2", "Slot 3", "Slot 4"], "MCQ", "3", "Medium",
 "Weight each slot’s total by 1, 1.1, 1.21 and 1.331.",
 steps(("Revenue in units of the slot-1 price", table(["Slot", "Tickets", "× price", "Revenue"],
         [["1", "63,500", "1", "63,500"], ["2", "58,000", "1.1", "63,800"], ["3", "61,500", "1.21", "74,415"], ["4", "42,000", "1.331", "55,902"]], hi={(2, 3)}))) + final("Slot 3, option 3"),
 [("1", "Most tickets, but the cheapest."), ("2", "63,800."), ("4", "Few tickets, even at the highest price.")])
P.dq(4, PRICE + "<p>Which of the following is not true?</p>",
 ["The revenue received in slot 3 for day 5 booking was the highest in any slot for any day booking.", "For all the bookings made for day 1, the lowest revenue was received in slot 4.",
  "The revenue received in slot 2 was higher than the revenue received in slot 1 (all 5 days combined).", "For all the bookings made for day 4, the lowest revenue was received in slot 4."], "MCQ", "4", "Medium",
 "Check day 4 slot by slot, with the price factor.",
 steps(("Day 4", p("Slot 1: 11,000 × 1 = 11,000. Slot 4: 9,000 × 1.331 = 11,979. Slot 1 is lower, so option 4 is false.")),
       ("The others", p("Option 1: 14,500 × 1.21 = 17,545, the largest of all slot-day pairs. Option 2: day 1 gives 13,000, 13,750, 13,915 and 10,648. Option 3: 63,800 > 63,500."))) + final("Option 4"),
 [("1", "17,545 tops every other slot-day."), ("2", "10,648 is day 1’s lowest."), ("3", "63,800 against 63,500.")])

# ---------------- Set 2: Artefact grid (Q5–8) ----------------
GIVEN = table(["", "C1", "C2", "C3", "C4"], [["R1", "1612", "", "", ""], ["R2", "1613", "1602", "1611", ""], ["R3", "", "1616", "1605", ""], ["R4", "", "", "", ""]])
SQ = table(["", "C1", "C2", "C3", "C4"], [["R1", "1612", "1607", "1614", "1601"], ["R2", "1613", "1602", "1611", "1608"], ["R3", "1603", "1616", "1605", "1610"], ["R4", "1606", "1609", "1604", "1615"]])
P.dilr_set(2, "Set 2 — The artefact grid", DIR,
 p("The curator of a museum is arranging a total of 16 artefacts in a 4 × 4 grid, as shown below. Each of these artefacts is originally from a different year from 1601 to 1616. The positions of six artefacts is fixed. The years of origin of those six artefacts are as shown below:") + GIVEN +
 p("For this grid, the four rows are denoted as 1 to 4 in that order from top to bottom. Similarly, the four columns are denoted as 1 to 4 in that order from left to right. The cell in the m<sup>th</sup> row and the n<sup>th</sup> column is denoted as RmCn, where ‘m’ and ‘n’ can take values from 1 to 4.") +
 p("Further, the sum of the years of origins of all the artefacts placed in any single row is the same as that of any single column which in turn is same as that of any diagonal."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("Simplify", p("Drop the 1600: the cells hold 1 to 16, and every row, column and diagonal adds to \\((1 + 2 + \\dots + 16) \\div 4 = 34\\).")),
       ("Forced cells", p("Row 2: R2C4 = 34 − 13 − 2 − 11 = 8. Diagonal R1C1–R4C4: R4C4 = 34 − 12 − 2 − 5 = 15. Column 1 needs R3C1 + R4C1 = 9 from unused numbers: only 3 + 6.")),
       ("Two cases", p("Other diagonal: R1C4 + R4C1 = 34 − 11 − 16 = 7. If R4C1 = 3, then R1C4 = 4, R3C4 = 7, and row 1 would need two numbers from {1, 9, 10, 14} adding to 18: impossible. So R4C1 = 6, R3C1 = 3, R1C4 = 1, R3C4 = 10.")),
       ("Finish", p("Row 1: R1C2 + R1C3 = 21; row 4: R4C2 + R4C3 = 13; column 2: R1C2 + R4C2 = 16. With 4, 7, 9, 14 left: R1C2 = 7, R1C3 = 14, R4C2 = 9, R4C3 = 4.") + SQ)) +
 final("The whole grid is fixed."),
 p("Subtract 1600 first: the magic sum is 34, and pairs that must add to a small number leave few choices."),
 p("<b>Magic square sum:</b> for the numbers 1 to \\(n^2\\) in an \\(n \\times n\\) grid, each line adds to \\(\\frac{n(n^2+1)}{2}\\)."))
P.dq(5, "For how many places in the grid can we determine the years of origin of the artefact placed?", [], "TITA", "16", "Medium",
 "Try to finish the square; is any choice left open?",
 steps(("Result", p("Only one arrangement works (see the set solution), so all 16 cells are known."))) + final("16"))
P.dq(6, "The artefact with the year of origin 1601 has been placed in the cell ________.", ["R1C4", "R1C3", "R3C4", "Cannot be determined"], "MCQ", "1", "Medium",
 "1 must pair with 6 on the diagonal through R4C1.",
 steps(("Placement", p("R1C4 + R4C1 = 7 and R4C1 = 6, so R1C4 = 1, the year 1601."))) + final("R1C4, option 1"),
 [("2", "R1C3 is 1614."), ("3", "R3C4 is 1610."), ("4", "The grid is unique.")])
P.dq(7, "The sum of the years of origin of the artefacts placed in the four corners of the grid is _______ . (Write ‘0’ if your answer is ‘Cannot be determined’)", [], "TITA", "6434", "Medium",
 "Read off the corners of the finished grid.",
 steps(("Corners", p("1612 + 1601 + 1606 + 1615 = 6434. (In a 4 × 4 magic square the corners always add to the magic sum: 34 + 6400.)"))) + final("6434"))
P.dq(8, "What is the year of origin of the artefact placed in the cell R4C2?", ["1604", "1609", "1608", "1615"], "MCQ", "2", "Medium",
 "Column 2 has 2 and 16; the other two cells add to 16.",
 steps(("Column 2", p("R1C2 + R4C2 = 16 from {4, 7, 9, 14}: 7 + 9. Row 4 needs R4C2 + R4C3 = 13, so R4C2 = 9 and R4C3 = 4."))) + final("1609, option 2"),
 [("1", "1604 is R4C3."), ("3", "1608 is R2C4."), ("4", "1615 is R4C4.")])

# ---------------- Set 3: Tour enquiries (Q9–13) ----------------
FUN = table(["Stage", "P", "Q", "R", "S", "T"],
            [["I", "e", "d", "a", "f", "32"], ["II", "20", "18", "15.5", "19", "27.5"], ["III", "23", "b", "18", "22", "i"],
             ["IV", "g", "16", "19", "h", "24"], ["V", "18", "18", "c", "24", "k"]]) + p("Total number of people: stage I 40,000; stage II 36,000; stage IV 28,000. (The totals for stages III and V are not given.)")
P.dilr_set(3, "Set 3 — Tour enquiries", DIR,
 p("A popular travel company arranges tours to five tourist destinations, named P, Q, R, S and T. The company receives a large number of enquiries for tours, which they classify into the following stages:") +
 "<p>Stage I: the number of enquiries received.<br>Stage II: the number of people who booked the tour by paying a token amount.<br>Stage III: the number of people who submitted the necessary documents (such as passport and Aadhaar card) to initiate the process of making reservations for the tour.<br>Stage IV: the number of people who paid the balance amount for the tour booked.<br>Stage V: the number of people who actually travelled to their destination.</p>" +
 p("It is known that all the people who travelled to their destination necessarily passed through the five stages for the same destination in that order. However, not all people necessarily proceeded to the next stage and some people dropped out at every stage.") +
 p("The table below gives, for a specific period, the percentage of the people at each stage who were for each destination.") + FUN +
 p("Interpretation of the table: out of all the people who completed stage I (of enquiry), 32% were for destination T. Out of all the people who completed stage III, b% were for destination Q and so on.") +
 p("It is known that the number of people who completed stage III was 77% of the total number of people who completed stage I. Only 87.5% of the people who completed stage IV completed stage V (i.e. they actually travelled to their destination).") +
 p("It is also known that a, b, c, d, e, f, g, h, and i are consecutive natural numbers in that order."),
 "DILR::DI::Data_Tabulation",
 steps(("Find a", p("Stage I adds to 100%: e + d + a + f = 68. With b = a + 1, …, so d = a + 3, e = a + 4, f = a + 5: \\(4a + 12 = 68\\), \\(a = 14\\).")),
       ("All letters", p("a 14, b 15, c 16, d 17, e 18, f 19, g 20, h 21, i 22. Check: stage III 23 + 15 + 18 + 22 + 22 = 100; stage IV 20 + 16 + 19 + 21 + 24 = 100. Stage V: k = 100 − 18 − 18 − 16 − 24 = 24.")),
       ("Totals", p("Stage III: 77% of 40,000 = 30,800. Stage V: 87.5% of 28,000 = 24,500."))) +
 final("Totals by stage: 40,000; 36,000; 30,800; 28,000; 24,500."),
 p("A row of percentages adds to 100: that pins down the unknown letters at once."),
 p("<b>Percent tables:</b> number = row total × percentage; never add percentages from different rows."))
P.dq(9, "How many travellers who enquired about tours in region Q submitted documents?", ["4620", "4520", "4650", "4220"], "MCQ", "1", "Easy",
 "Stage III, destination Q: b% of the stage III total.",
 steps(("Compute", p("b = 15. 15% of 30,800 = 4,620."))) + final("4620, option 1"),
 [("2", "Arithmetic slip."), ("3", "Wrong total."), ("4", "Wrong percentage.")])
P.dq(10, "What is the value of (a + k)?", ["40", "38", "36", "None of these"], "MCQ", "2", "Easy",
 "Find a from stage I and k from stage V.",
 steps(("Values", p("a = 14, k = 24: 38."))) + final("38, option 2"),
 [("1", "Uses a = 16."), ("3", "Uses k = 22."), ("4", "38 is listed.")])
P.dq(11, "What percentage of people who enquired about destination P actually travelled to that destination?", ["71.2", "67.5", "61.25", "72.4"], "MCQ", "3", "Medium",
 "Stage V for P over stage I for P.",
 steps(("Numbers", p("Enquired: e = 18% of 40,000 = 7,200. Travelled: 18% of 24,500 = 4,410.")), ("Percentage", p("4,410 ÷ 7,200 = 61.25%."))) + final("61.25, option 3"),
 [("1", "Wrong stage total."), ("2", "Wrong stage total."), ("4", "Wrong stage total.")])
P.dq(12, "How many people actually visited destination R through the company?", [], "TITA", "3920", "Easy",
 "Stage V, destination R: c%.",
 steps(("Compute", p("c = 16. 16% of 24,500 = 3,920."))) + final("3920"))
P.dq(13, "The sum of the number of people who made an enquiry for tours in Q and S was ______ .", [], "TITA", "14400", "Easy",
 "Stage I: d + f percent.",
 steps(("Compute", p("d + f = 17 + 19 = 36%. 36% of 40,000 = 14,400."))) + final("14400"))

# ---------------- Set 4: Marbles (Q14–18) ----------------
MARB = table(["Player", "After round 1", "After round 2"],
             [["A", "7", "1"], ["B", "6", "9"], ["F", "5", "8"], ["E", "1", "4"], ["I", "3", "7"], ["C, D", "8 and 9", "2 and 6"], ["G, H", "2 and 4", "3 and 5"]])
P.dilr_set(4, "Set 4 — Two rounds of marbles", DIR,
 p("Nine friends—A, B, C, D, E, F, G, H, and I—played a game of two rounds with a total of 45 marbles. None of them had any marbles before the game.") +
 p("In the first round, the winner received 9 marbles, the first runner-up received 8 marbles, the second runner-up received 7 marbles, and so on, with each subsequent position receiving one marble less than the previous.") +
 p("In the second round, the winner took 9 marbles from the winner of the first round, the first runner-up took 8 marbles from the first runner-up of the first round, the second runner-up took 7 marbles from the second runner-up of the first round, and so on.") +
 p("The following information is known:") +
 "<ol><li>No individual secured the same rank in both rounds.</li><li>Only the winner, first runner-up, and second runner-up of the first round had fewer marbles at the end of the second round than they had at the end of the first round.</li>"
 "<li>The number of marbles with B at the end of each round was a multiple of 3.</li><li>G and H were the only two players who had exactly one more marble at the end of the second round compared to the end of the first round.</li>"
 "<li>E was the only player to have a perfect square number of marbles at the end of both rounds. E was not the winner of the first round.</li><li>I had ‘x’ more marbles at the end of the second round than at the end of the first round, where ‘x’ was a perfect square.</li>"
 "<li>At the end of the first round, the number of marbles with A and B were consecutive numbers and at the end of the second round, the difference between B and A was the maximum among all pairs.</li><li>F and B had marble counts that were consecutive integers at the end of each round.</li></ol>",
 "DILR::LR::Games_and_Tournaments",
 steps(("What the rounds do", p("After round 1, the player ranked \\(r\\) holds \\(10 - r\\). In round 2, each player loses everything won in round 1 and gains what their round-2 rank gives. So after round 2, rank \\(r\\) in round 2 holds \\(10 - r\\). Both rounds hand out 1 to 9 marbles, one count per player.")),
       ("A and B", p("B ends round 2 with the largest gap over A, so B has 9 and A has 1. B’s round-1 count is 3 or 6 and differs from A’s by 1. By clue 2, A (whose count fell) was in the top three of round 1, holding 7, 8 or 9: so B 6, A 7.")),
       ("F and E", p("F is next to B both times: 5 then 8. E has squares both times, not 9 in round 1, and its count must rise (E isn’t top three): 1 then 4.")),
       ("I, G and H", p("Counts that rose by exactly 1 belong only to G and H. The values left are 2, 3, 4, 8, 9 (round 1) and 2, 3, 5, 6, 7 (round 2). I rose by a square other than 1: 3 → 7 (+4). G and H take 2 → 3 and 4 → 5. C and D take round-1 counts 8 and 9 and round-2 counts 2 and 6.") + MARB)) +
 final("A, B, E, F and I are fixed in both rounds; C/D and G/H can swap."),
 p("Every count is a rank turned upside down: 10 − rank. Work with counts 1–9 in each round."),
 p("<b>Redistribution games:</b> track each player’s change; here a player’s round-2 count depends only on their round-2 rank."))
P.dq(14, "For how many players, their rankings can be determined uniquely at the end of both the rounds?", ["4", "5", "6", "7"], "MCQ", "2", "Hard",
 "Which players can swap with someone else?",
 steps(("Fixed", p("A, B, E, F and I have one possible pair of counts each. C and D can swap, and so can G and H."))) + final("5, option 2"),
 [("1", "Leaves one of A, B, E, F, I out."), ("3", "C/D or G/H can still swap."), ("4", "C/D or G/H can still swap.")])
P.dq(15, "Who was the winner of 1<sup>st</sup> round of the game?", ["C", "D", "A", "Cannot be determined"], "MCQ", "4", "Medium",
 "Who holds 9 after round 1?",
 steps(("Round-1 counts of 8 and 9", p("C and D, in either order. A holds 7."))) + final("Option 4"),
 [("1", "Could also be D."), ("2", "Could also be C."), ("3", "A has 7 after round 1: second runner-up.")])
P.dq(16, "At the end of 2<sup>nd</sup> round, I had _____ marbles.", ["6", "7", "5", "Cannot be determined"], "MCQ", "2", "Medium",
 "I rose by a perfect square other than 1.",
 steps(("I", p("Only 3 → 7 (+4) fits the values left. I has 7."))) + final("7, option 2"),
 [("1", "6 belongs to C or D."), ("3", "5 belongs to G or H."), ("4", "I is fixed.")])
P.dq(17, "Which of the following is definitely true?", ["G had more marbles than H at the end of round 1.", "C had fewer marbles than D at the end of round 2.", "I had more marbles than C at the end of round 2.", "I had more marbles than D at the end of round 1."], "MCQ", "3", "Medium",
 "Compare using the final table; watch out for pairs that can swap.",
 steps(("Check", p("I has 7 after round 2; C has 2 or 6. Either way I has more."))) + final("Option 3"),
 [("1", "G and H can swap."), ("2", "C and D can swap."), ("4", "D has 8 or 9 after round 1; I has 3.")])
P.dq(18, "What the best can be said about the number of marbles with D at the end of round 2?", ["Either 2 or 7", "Either 6 or 7", "Either 2 or 6", "Either 2 or 3"], "MCQ", "3", "Medium",
 "C and D share the round-2 counts left over.",
 steps(("Leftovers", p("Round-2 counts 2 and 6 go to C and D in some order."))) + final("Option 3"),
 [("1", "7 is I’s."), ("2", "7 is I’s."), ("4", "3 belongs to G or H.")])

# ---------------- Set 5: Warehouse (Q19–22) ----------------
FIG5 = charts.pie("sipe_SM25-01_DILR_S5", ["Television", "Microwave oven", "Washing machine", "Refrigerator"], [35, 20, 12.5, 32.5],
                  "Pie chart: television 35%, microwave oven 20%, washing machine 12.5%, refrigerator 32.5%", fmt=lambda v: f"{v:g}%")
WH = table(["Product", "All", "S", "G"],
           [["Washing m/c", "345", "100", "245"], ["Microwave", "552", "200", "352"], ["Refrigerator", "897", "300", "597"], ["Television", "966", "400", "566"], ["Total", "2760", "1000", "1760"]])
P.dilr_set(5, "Set 5 — The warehouse", DIR,
 p("A warehouse of consumer durable electronics goods has exactly four types of products, namely microwave oven, refrigerator, television, and washing machine. The following pie diagram shows the different products as a percentage of total number of products in the warehouse.") + FIG5 +
 p("There are only two manufacturer brands for each type of product: Brand S and Brand G. The number of washing machines, microwave ovens, refrigerators, and television sets of Brand S in the warehouse are in the ratio 1 : 2 : 3 : 4. Among the Brand G products, 566 are television sets and 597 are refrigerators."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Two equations", p("Let the total be \\(N\\) and Brand S’s counts be \\(k, 2k, 3k, 4k\\). Televisions: \\(0.35N = 4k + 566\\). Refrigerators: \\(0.325N = 3k + 597\\).")),
       ("Solve", p("Multiply the first by 3 and the second by 4 and subtract: \\(1.3N - 1.05N = 2388 - 1698\\), so \\(0.25N = 690\\), \\(N = 2760\\) and \\(k = 100\\).")),
       ("Everything", p("S and G are the two brands.") + WH)) + final("2,760 products: Brand S 1,000, Brand G 1,760."),
 p("Two products with known Brand G counts give two equations in N and k."),
 p("<b>Pie plus a ratio:</b> express each slice two ways (share of N, and brand counts) and equate."))
P.dq(19, "The total number of products in the warehouse is __________ .", [], "TITA", "2760", "Medium",
 "Write the TV and refrigerator counts two ways.",
 steps(("Solve", p("\\(0.35N = 4k + 566\\) and \\(0.325N = 3k + 597\\) give \\(N = 2760\\)."))) + final("2760"))
P.dq(20, "The number of microwave ovens of Brand G as percentage of all products of Brand G is ________ .", ["18", "20", "24.5", "25"], "MCQ", "2", "Medium",
 "Microwaves total 20% of 2,760; Brand S has 200 of them.",
 steps(("Brand G microwaves", p("552 − 200 = 352.")), ("Percentage", p("352 ÷ 1,760 = 20%."))) + final("20, option 2"),
 [("1", "Wrong base."), ("3", "Wrong base."), ("4", "Uses 440.")])
P.dq(21, "Which of the following statements is true?", ["Total number of Brand G products is 76% more than that of Brand S products.", "Total number of Brand G products is 56% more than that of Brand S products.",
  "Total number of Brand G products is 56% less than that of Brand S products.", "Total number of Brand G products is 76% less than that of Brand S products."], "MCQ", "1", "Easy",
 "Brand S has 10k = 1,000.",
 steps(("Compare", p("Brand G: 2,760 − 1,000 = 1,760, which is 76% more than 1,000."))) + final("Option 1"),
 [("2", "Not the right percentage."), ("3", "Brand G has more, not less."), ("4", "Brand G has more, not less.")])
P.dq(22, "If p% of refrigerators in the warehouse belong to the Brand S then _________ .", ["30 < p < 31", "31 < p < 32", "32 < p < 33", "33 < p < 34"], "MCQ", "4", "Easy",
 "Brand S refrigerators over all refrigerators.",
 steps(("Compute", p("300 ÷ 897 ≈ 33.4%."))) + final("Option 4"),
 [("1", "Too low."), ("2", "Too low."), ("3", "Too low: 300/897 is just over a third.")])
