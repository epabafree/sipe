# -*- coding: utf-8 -*-
# Batch 18 — CAT 2024 Slot 2: DILR sets 1–5 (Q1–22, in exam order).
from fmt import steps, final, trap, why, table, p
from b18_24s2 import P
import b18_24s2_figs as F

DIR = "Read the information given below and answer the questions that follow."

# ---------------- Set 1: Numbers in a staircase grid ----------------
P.dilr_set(1, "Set 1 — Ten numbers in a staircase grid", DIR,
 p("The numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10 are placed in ten slots of the following grid based on the conditions below.") + F.GRID10 +
 "<ol><li>Numbers in any row appear in an increasing order from left to right.</li><li>Numbers in any column appear in a decreasing order from top to bottom.</li><li>1 is placed either in the same row or in the same column as 10.</li><li>Neither 2 nor 3 is placed in the same row or in the same column as 10.</li><li>Neither 7 nor 8 is placed in the same row or in the same column as 9.</li><li>4 and 6 are placed in the same row.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Where 10 goes", p("10 must be the last number in its row and the top of its column. The only slot with nothing to its right and nothing above it is Row 1, Column 4.")),
       ("2 and 3", p("They can’t be in Row 1 or Column 4, so they take two of the three slots R2C2, R2C3 and R3C3.")),
       ("Where 9 goes", p("9 must also have nothing bigger to its right or above it except 10, so it is at R1C3 or R2C4. Suppose it is at R2C4. Then 7 and 8 avoid Row 2 and Column 4, and R3C3 is too small for them (it is below R2C3, which is at most 6), so they sit in Row 1 next to 10. Then R2C3 must be bigger than both its neighbours from {2, 3}, so 2 and 3 fill R2C2 and R3C3, and 1, 4, 5, 6 are left for four slots in four different rows. 4 and 6 can’t share a row, which is a contradiction. So 9 is at R1C3.")),
       ("7 and 8", p("They avoid Row 1 and Column 3. R2C2 can’t hold them, because R2C3 would have to lie between them and 9. So they are in Column 4, and the column order gives R2C4 = 8 and R3C4 = 7.")),
       ("4 and 6, then 1", p("Row 2 can’t hold both 4 and 6, because 2 and 3 need two of R2C2, R2C3 and R3C3. So 4 and 6 are R1C1 and R1C2, in that order. 1 must share a row or column with 10, and Row 1 is full, so 1 is at R4C4. The last three numbers, 2, 3 and 5, fill R2C2, R2C3 and R3C3, and R2C3 must be the largest of them: 5.") +
          table(["", "C1", "C2", "C3", "C4"], [["R1", "4", "6", "9", "10"], ["R2", "", "2/3", "5", "8"], ["R3", "", "", "3/2", "7"], ["R4", "", "", "", "1"]]) +
          p("2 and 3 can go either way round."))) +
 final("Every slot is fixed except R2C2 and R3C3, which hold 2 and 3 in either order."),
 p("Place the extremes first: 10 can only go top right. Then try both spots for 9; one quickly runs out of rows for 4 and 6."),
 p("<b>Ordered grids:</b> in a grid that increases along rows and decreases down columns, the largest number sits where nothing is to its right or above it. Work down from the largest values."))
P.dq(1, "What is the row number which has the least sum of numbers placed in that row?", [], "TITA", "4", "Easy",
 "Row 4 has only one slot. What is in it?",
 steps(p("Row 4 holds just 1. The other rows add to 29, 15 or 16, and 10 or 9.")) + final(r"\(4\)"))
P.dq(2, "Which of the following statements MUST be true?<br>I. 10 is placed in a slot in Row 1.<br>II. 1 is placed in a slot in Row 4.", ["Only II", "Both I and II", "Only I", "Neither I nor II"], "MCQ", "2", "Easy",
 "Both placements are fixed in the set solution.",
 steps(p("10 is at the top of Column 4 in Row 1, and 1 is at the bottom of Column 4 in Row 4. Both are certain.")) + final("Both, option 2"),
 [("1", "I is also certain."), ("3", "II is also certain."), ("4", "Both are certain.")])
P.dq(3, "Which of the following statements MUST be true?<br>I. 2 is placed in a slot in Column 2.<br>II. 3 is placed in a slot in Column 3.", ["Neither I nor II", "Only I", "Both I and II", "Only II"], "MCQ", "1", "Medium",
 "2 and 3 can swap places. Does either statement hold in both versions?",
 steps(p("2 and 3 occupy R2C2 and R3C3 in either order. If 3 is in Column 2, statement I fails, and statement II fails too. Neither must be true.")) + final("Neither, option 1"),
 [("2", "2 could be at R3C3, in Column 3."), ("3", "Both statements fail when 2 and 3 swap."), ("4", "3 could be at R2C2, in Column 2.")])
P.dq(4, "For how many slots in the grid, placement of numbers CANNOT be determined with certainty?", [], "TITA", "2", "Easy",
 "Which numbers can swap without breaking any rule?",
 steps(p("Only 2 and 3 can swap, so two slots, R2C2 and R3C3, are uncertain.")) + final(r"\(2\)"))
P.dq(5, "What is the sum of the numbers placed in Column 4?", [], "TITA", "26", "Easy",
 "Read Column 4 from top to bottom.",
 steps(p(r"\(10 + 8 + 7 + 1 = 26\).")) + final(r"\(26\)"))

# ---------------- Set 2: Walkways around lakes ----------------
P.dilr_set(2, "Set 2 — Walkways and lakes in a gated area", DIR,
 F.WALK +
 p("The above is a schematic diagram of walkways (indicated by all the straight lines) and lakes (3 of them, each in the shape of rectangles — shaded in the diagram) of a gated area. Different points on the walkway are indicated by letters (A through P) with distances being OP = 150 m, ON = MN = 300 m, ML = 400 m, EL = 200 m, DE = 400 m.") +
 p("The following additional information about the facilities in the area is known.") +
 "<ol><li>The only entry/exit point is at C.</li><li>There are many residences within the gated area; all of them are located on the path AH and ML with four of them being at A, H, M, and L.</li><li>The post office is located at P and the bank is located at B.</li></ol>",
 "DILR::LR::Routes_and_Networks",
 steps(("The grid of distances", p("The width is OP + ON + NM = 150 + 300 + 300 = 750 m, and the height is DE + EL + LM = 400 + 200 + 400 = 1000 m. Every vertical line is split the same way (400, 200, 400), and every horizontal line the same way (150, 300, 300). So, for example, AB = HG = IJ = 150, BC = GF = JK = 300, BG = 400, GJ = 200 and CF = 400.")),
       ("The two diagonals", p(r"IG crosses a 150 × 200 rectangle: \(\sqrt{150^2 + 200^2} = 250\) m. OK crosses a 300 × 400 square: \(\sqrt{300^2 + 400^2} = 500\) m.")),
       ("Walkways next to a lake", p("The lake edges are C–D, D–E, E–F, F–C (top right); G–F, F–K, K–J, J–G (middle); and K–L, L–M, M–N, N–K (bottom right)."))) +
 final("All edge lengths follow from the six given distances and two right triangles."),
 p("Write the length on every edge of the diagram before you start. Each question is then a matter of choosing a route."),
 p("<b>Route questions:</b> for shortest routes, compare the few sensible paths. For “no point twice” or “no path twice”, check whether the graph lets you return to the start, and drop the shortest detours last."))
P.dq(6, "One resident whose house is located at L, needs to visit the post office as well as the bank. What is the minimum distance (in m) he has to walk starting from his residence and returning to his residence after visiting both the post office and the bank?", ["3200", "3000", "3000", "2700"], "MCQ", "1", "Medium",
 "Go from L to P, from P to B, and from B back to L, each by its shortest route. The diagonals help.",
 steps(("L to P", p("L–K–O–P: 300 + 500 + 150 = 950 m.")),
       ("P to B", p("P–I–G–B: 400 + 250 + 400 = 1050 m.")),
       ("B back to L", p("B–C–D–E–L: 300 + 300 + 400 + 200 = 1200 m (B–C–F–E–L is the same length).")),
       ("Total", p("950 + 1050 + 1200 = 3200 m."))) + final("3200 m, option 1"),
 [("2", "A 3000 m loop would need a shorter leg somewhere, and each leg is already the shortest."), ("3", "This is the same value as option 2."), ("4", "2700 m is shorter than any route that reaches both P and B.")])
P.dq(7, "One person enters the gated area and decides to walk as much as possible before leaving the area without walking along any path more than once and always walking next to one of the lakes. Note that he may cross a point multiple times. How much distance (in m) will he walk within the gated area?", ["3200", "2800", "3000", "3800"], "MCQ", "4", "Hard",
 "Only lake-side walkways can be used. Can all twelve be walked in one loop from C back to C?",
 steps(("The lake-side walkways", p("Top lake: 300 + 400 + 300 + 400 = 1400. Middle lake: 300 + 200 + 300 + 200 = 1000. Bottom lake: 300 + 400 + 300 + 400 = 1400. In all, 3800 m.")),
       ("One loop", p("C–D–E–F–K–L–M–N–K–J–G–F–C uses every one of them once. F and K are passed twice, which is allowed."))) + final("3800 m, option 4"),
 [("1", "This leaves out some lake-side walkways that can be included."), ("2", "This walks round only two lakes."), ("3", "This also leaves out walkways that fit in the loop.")])
P.dq(8, "One resident takes a walk within the gated area starting from A and returning to A without going through any point (other than A) more than once. What is the maximum distance (in m) she can walk in this way?", [], "TITA", "5100", "Hard",
 "Try to pass through all sixteen points in one loop, using the long edges where you can.",
 steps(("A loop through every point", p("A–B–G–F–C–D–E–L–M–N–K–J–O–P–I–H–A.")),
       ("Its length", p("150 + 400 + 300 + 400 + 300 + 400 + 200 + 400 + 300 + 400 + 300 + 400 + 150 + 400 + 200 + 400 = 5100 m.")),
       ("Why it is the longest", p("It visits all 16 points, so it has 16 edges, the most possible. The only edges left out are the short ones and the two diagonals. Using O–K (500) or I–G (250) would force out two other edges with more total length, or would skip points."))) + final("5100 m"))
P.dq(9, "Visitors coming for morning walks are allowed to enter as long as they do not pass by any of the residences and do not cross any point (except C) more than once. What is the maximum distance (in m) that such a visitor can walk within the gated area?", [], "TITA", "3500", "Hard",
 "Remove A, H, L and M and every walkway through them. Find the longest loop from C back to C.",
 steps(("What is left", p("Without A, H, L and M, the walkways from E go only to D and F, and those from N only to O and K. The left side is reached through B, G, I, J, O and P.")),
       ("The longest loop", p("C–B–G–J–I–P–O–N–K–F–E–D–C: 300 + 400 + 200 + 150 + 400 + 150 + 300 + 400 + 200 + 300 + 400 + 300 = 3500 m. The route C–B–G–I–P–O–N… swaps G–J–I (350) for G–I (250) and is shorter; going O–K directly skips N and is shorter too."))) + final("3500 m"))

# ---------------- Set 3: Product ratings ----------------
P.dilr_set(3, "Set 3 — Daily and cumulative product ratings", DIR,
 p("An online e-commerce firm receives daily integer product ratings from 1 through 5 given by buyers. The daily average is the average of the ratings given on that day. The cumulative average is the average of all ratings given on or before that day.") +
 p("The rating system began on Day 1, and the cumulative averages were 3 and 3.1 at the end of Day 1 and Day 2, respectively. The distribution of ratings on Day 2 is given in the figure below.") + F.RATINGS +
 p("The following information is known about ratings on Day 3.") +
 "<ol><li>100 buyers gave product ratings on Day 3.</li><li>The modes of the product ratings were 4 and 5.</li><li>The numbers of buyers giving each product rating are non-zero multiples of 10.</li><li>The same number of buyers gave product ratings of 1 and 2, and that number is half the number of buyers who gave a rating of 3.</li></ol>",
 "DILR::DI::Graphs_and_Charts",
 steps(("Day 2", p(r"50 buyers gave ratings adding to \(5 + 20 + 15 + 80 + 50 = 170\), an average of 3.4.")),
       ("Day 1", p(r"With \(x\) buyers on Day 1 averaging 3: \(\frac{3x + 170}{x + 50} = 3.1\), so \(3x + 170 = 3.1x + 155\) and \(x = 150\).")),
       ("Day 3", p(r"Let ratings 1 and 2 have \(10k\) buyers each and rating 3 have \(20k\). Ratings 4 and 5 are the two modes, so they have equal counts, \(10m\) each, larger than \(20k\). Then \(40k + 20m = 100\), so \(2k + m = 5\). With \(k \ge 1\) and \(10m > 20k\), only \(k = 1, m = 3\) works.") +
          table(["Rating", "1", "2", "3", "4", "5"], [["Buyers", "10", "10", "20", "30", "30"]]) +
          p(r"Sum: \(10 + 20 + 60 + 120 + 150 = 360\), a daily average of 3.6.")),
       ("Cumulative after Day 3", p(r"\(\frac{450 + 170 + 360}{300} = \frac{980}{300} \approx 3.267\)."))) +
 final("Day 1: 150 buyers. Day 3: 10, 10, 20, 30, 30 buyers for ratings 1 to 5."),
 p("Use the cumulative average to recover Day 1’s count, and the multiples-of-10 rule to pin Day 3 down to a single distribution."),
 p(r"<b>Combined averages:</b> \(\text{combined average} = \frac{\text{total of all ratings}}{\text{total number of ratings}}\). Work with totals, not with averages of averages."))
P.dq(10, "How many buyers gave ratings on Day 1?", [], "TITA", "150", "Medium",
 "Day 2 had 50 ratings averaging 3.4. What Day 1 count brings the overall average to 3.1?",
 steps(p(r"\(\frac{3x + 170}{x + 50} = 3.1 \Rightarrow 0.1x = 15 \Rightarrow x = 150\).")) + final(r"\(150\)"))
P.dq(11, "What is the daily average rating of Day 3?", ["3.6", "3.5", "3.0", "3.2"], "MCQ", "1", "Medium",
 "Find the Day 3 distribution first.",
 steps(p(r"10, 10, 20, 30 and 30 buyers give \(360 \div 100 = 3.6\).")) + final("3.6, option 1"),
 [("2", "3.5 would need a total of 350."), ("3", "3.0 is Day 1’s average."), ("4", "3.2 would need a total of 320.")])
P.dq(12, "What is the median of all ratings given on Day 3?", [], "TITA", "4", "Easy",
 "With 100 ratings, look at the 50th and 51st.",
 steps(p("Ratings 1 to 3 cover the first 40 buyers; ratings of 4 cover the 41st to 70th. The 50th and 51st are both 4.")) + final(r"\(4\)"))
P.dq(13, "Which of the following is true about the cumulative average ratings of Day 2 and Day 3?<br>1. The cumulative average of Day 3 decreased from Day 2.<br>2. The cumulative average of Day 3 increased by more than 8% from Day 2.<br>3. The cumulative average of Day 3 increased by less than 5% from Day 2.<br>4. The cumulative average of Day 3 increased by a percentage between 5% and 8% from Day 2.", ["Statement 1", "Statement 2", "Statement 3", "Statement 4"], "MCQ", "4", "Medium",
 "Find the cumulative average after Day 3 and compare it with 3.1.",
 steps(p(r"\(\frac{980}{300} \approx 3.267\). The rise is \(\frac{0.167}{3.1} \approx 5.4\%\), which is between 5% and 8%.")) + final("Statement 4, option 4"),
 [("1", "Day 3’s average of 3.6 is above 3.1, so the cumulative average rises."), ("2", "An 8% rise would need about 3.35."), ("3", "A 5% rise is only 3.255; the new average is a little higher.")])

# ---------------- Set 4: Profits, staff and R&D ----------------
P.dilr_set(4, "Set 4 — Profits, employees and R&D of six firms", DIR,
 p("The two plots below give the following information about six firms A, B, C, D, E, and F for 2019 and 2023.") +
 "<ul><li>PAT: The firm's profits after taxes in Rs. crores,</li><li>ES: The firm's employee strength, that is the number of employees in the firm, and</li><li>PRD: The percentage of the firm’s PAT that they spend on Research and Development (R&amp;D).</li></ul>" +
 p("In the plots, the horizontal and vertical coordinates of point representing each firm gives their ES and PAT values respectively. The PRD values of each firm are proportional to the areas around the points representing each firm. The areas are comparable between the two plots, i.e., equal areas in the two plots represent the same PRD values for the two years.") + F.B19 + F.B23,
 "DILR::DI::Graphs_and_Charts",
 steps(("Reading the circles", p("Areas grow with the square of the radius. Taking D’s 2019 circle as 1 unit, the other circles have twice or three times its radius (four times for E in 2019), so their PRD values are 4, 9 or 16 units.")),
       ("The data", table(["Firm", "2019", "2023"],
          [["A", "800, 3000, 4", "1300, 3900, 4"], ["B", "1000, 2800, 9", "1000, 3800, 9"], ["C", "600, 2400, 9", "800, 3000, 4"],
           ["D", "600, 3900, 1", "800, 2400, 4"], ["E", "1200, 2400, 16", "1400, 3500, 9"], ["F", "800, 2500, 4", "1000, 3200, 4"]]) +
          p("Each entry is ES, PAT (Rs crore), PRD (in units)."))) +
 final("The table gives every firm’s employees, profit and R&D share in both years."),
 p("Turn the plot into a table first. Circle areas only need to be compared, so units of “D’s 2019 area” are enough."),
 p("<b>Bubble charts:</b> the value is proportional to the area, so a circle with twice the radius stands for four times the value."))
P.dq(14, "Assume that the annual rate of growth in PAT over the previous year (ARG) remained constant over the years for each of the six firms. Which among the firms A, B, C, and E had the highest ARG?", ["Firm E", "Firm B", "Firm A", "Firm C"], "MCQ", "1", "Easy",
 "A constant growth rate over the same four years means the biggest overall ratio wins.",
 steps(p(r"2023 PAT ÷ 2019 PAT: A \(3900/3000 = 1.30\), B \(3800/2800 \approx 1.36\), C \(3000/2400 = 1.25\), E \(3500/2400 \approx 1.46\). E grew the most.")) + final("Firm E, option 1"),
 [("2", "B grew by about 36%, less than E’s 46%."), ("3", "A grew by 30%."), ("4", "C grew by 25%.")])
P.dq(15, "The ratio of the amount of money spent by Firm C on R&amp;D in 2019 to that in 2023 is closest to", ["5 : 6", "9 : 5", "5 : 9", "9 : 4"], "MCQ", "2", "Medium",
 "R&D spending is PRD × PAT. C’s circle shrank from 9 units to 4.",
 steps(p(r"2019: \(9 \times 2400 = 21600\). 2023: \(4 \times 3000 = 12000\). The ratio is \(21600 : 12000 = 9 : 5\).")) + final("9 : 5, option 2"),
 [("1", "This ignores the change in PRD."), ("3", "This is the ratio the wrong way round."), ("4", "This compares only the PRD values and ignores PAT.")])
P.dq(16, "Which among the firms A, C, E, and F had the maximum PAT per employee in 2023?", ["Firm C", "Firm A", "Firm F", "Firm E"], "MCQ", "1", "Easy",
 "Divide PAT by ES for each firm in 2023.",
 steps(p(r"A \(3900/1300 = 3\), C \(3000/800 = 3.75\), E \(3500/1400 = 2.5\), F \(3200/1000 = 3.2\).")) + final("Firm C, option 1"),
 [("2", "A has 3."), ("3", "F has 3.2."), ("4", "E has only 2.5.")])
P.dq(17, "Which among the firms C, D, E, and F had the least amount of R &amp; D spending per employee in 2023?", ["Firm E", "Firm D", "Firm F", "Firm C"], "MCQ", "2", "Medium",
 "Compute PRD × PAT ÷ ES in units.",
 steps(p(r"C \(4 \times 3000 / 800 = 15\). D \(4 \times 2400 / 800 = 12\). E \(9 \times 3500 / 1400 = 22.5\). F \(4 \times 3200 / 1000 = 12.8\). D is the least.")) + final("Firm D, option 2"),
 [("1", "E spends the most per employee."), ("3", "F, at 12.8, is just above D’s 12."), ("4", "C spends 15 per employee.")])

# ---------------- Set 5: Gymnastics coaches ----------------
P.dilr_set(5, "Set 5 — Three coaches and eight gymnasts", DIR,
 p("Eight gymnastics players numbered 1 through 8 underwent a training camp where they were coached by three coaches - Xena, Yuki, and Zara. Each coach trained at least two players. Yuki trained only even numbered players, while Zara trained only odd numbered players. After the camp, the coaches evaluated the players and gave integer ratings to the respective players trained by them on a scale of 1 to 7, with 1 being the lowest rating and 7 the highest.") +
 p("The following additional information is known.") +
 "<ol><li>Xena trained more players than Yuki.</li><li>Player-1 and Player-4 were trained by the same coach, while the coaches who trained Player-2, Player-3 and Player-5 were all different.</li><li>Player-5 and Player-7 were trained by the same coach and got the same rating. All other players got a unique rating.</li><li>The average of the ratings of all the players was 4.</li><li>Player-2 got the highest rating.</li><li>The average of the ratings of the players trained by Yuki was twice that of the players trained by Xena and two more than that of the players trained by Zara.</li><li>Player-4's rating was double of Player-8's and less than Player-5's.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Who trains whom", p("Players 1 and 4 (odd and even) share a coach, so it must be Xena. Players 5 and 7 share a coach: Xena or Zara. If it were Xena, Zara could train only player 3, but every coach trains at least two. So Zara trains 5 and 7. Players 2, 3 and 5 have different coaches: 3 goes to Xena and 2 to Yuki.")),
       ("The ratings that are fixed", p("The ratings add to 32. Seven different values from 1 to 7 add to 28, so the shared rating of players 5 and 7 is 4. Player 2 has the top rating, 7. Player 4 is twice player 8 and less than 4, so player 4 has 2 and player 8 has 1.")),
       ("The averages", p("Zara’s average is 4, so Yuki’s is 6 and Xena’s is 3. If Xena trains m players, Yuki trains 6 − m, and the totals give 3m + 6(6 − m) + 8 = 32, so m = 4. Yuki trains 2 players with a total of 12: player 2 (7) and a player rated 5.")),
       ("Players 6 and 8", p("Player 8 has rating 1, so Yuki’s other player is 6, with rating 5. Xena trains 1, 3, 4 and 8. The remaining ratings, 3 and 6, go to players 1 and 3 in some order (Xena’s total 1 + 2 + 3 + 6 = 12 checks).") +
          table(["Coach", "Players", "Ratings"], [["Xena", "1, 3, 4, 8", "3/6, 6/3, 2, 1"], ["Yuki", "2, 6", "7, 5"], ["Zara", "5, 7", "4, 4"]]))) +
 final("Xena: 1, 3, 4, 8. Yuki: 2, 6. Zara: 5, 7. Only players 1 and 3 have ratings that can swap (3 and 6)."),
 p("Fix the coaches from the odd/even rules first, then use the total of 32 to find the shared rating."),
 p(r"<b>Averages across groups:</b> write each group’s total as average × size, and add them up to the grand total."))
P.dq(18, "What best can be concluded about the number of players coached by Zara?", ["Exactly 2", "Either 2 or 3", "Exactly 3", "Either 2 or 3 or 4"], "MCQ", "1", "Medium",
 "Zara trains only odd players. Which odd players are taken by Xena?",
 steps(p("Players 1 and 3 are with Xena, so Zara has only 5 and 7.")) + final("Exactly 2, option 1"),
 [("2", "Zara can’t train player 3, because 3 and 5 have different coaches."), ("3", "Only two odd players are left for her."), ("4", "Only two odd players are left for her.")])
P.dq(19, "What was the rating of Player-7?", [], "TITA", "4", "Medium",
 "The eight ratings add to 32, and seven of them are different.",
 steps(p(r"\(32 - (1 + 2 + \cdots + 7) = 32 - 28 = 4\). Players 5 and 7 share this rating.")) + final(r"\(4\)"))
P.dq(20, "What was the rating of Player-6?", [], "TITA", "5", "Hard",
 "Yuki’s players average 6. Who is Yuki’s second player?",
 steps(p("Yuki has two players totalling 12. Player 2 has 7, so the other has 5. That player is even and not 4 or 8, so it is player 6.")) + final(r"\(5\)"))
P.dq(21, "For how many players the ratings can be determined with certainty?", [], "TITA", "6", "Medium",
 "Which two players’ ratings could swap?",
 steps(p("Players 2, 4, 5, 6, 7 and 8 are fixed. Players 1 and 3 have 3 and 6 in either order. So 6 ratings are certain.")) + final(r"\(6\)"))
P.dq(22, "Who all were the players trained by Xena?", ["Player-1, Player-4, Player-6, Player-8", "Player-1, Player-3, Player-4, Player-6", "Player-1, Player-3, Player-4, Player-8", "Player-1, Player-3, Player-4"], "MCQ", "3", "Medium",
 "Xena trains four players, and player 6 is with Yuki.",
 steps(p("Xena trains 1, 3, 4 and 8.")) + final("Option 3"),
 [("1", "Player 6 is with Yuki, and player 3 is missing."), ("2", "Player 6 is with Yuki; player 8 is Xena’s."), ("4", "Xena trains four players, including 8.")])
