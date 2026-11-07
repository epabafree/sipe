# -*- coding: utf-8 -*-
# Batch 14 — CAT 2019 Slot 1: DILR sets 1–8 (Q1–32, exam order).
from fmt import steps, final, trap, why, table, p
from b14_19s1 import P

def fig(src, alt):
    return f'<p class="fig"><img src="{src}" alt="{alt}"></p>'

# ---------------- Set 1: Supermarket shelves ----------------
P.dilr_set(1, "Set 1 — Twelve items, sixteen shelves", "Answer the questions on the basis of the following information.",
 p("A supermarket has to place 12 items (coded A to L) in shelves numbered 1 to 16. Five of these items are types of biscuits, three are types of candies and the rest are types of savouries. Only one item can be kept in a shelf. Items are to be placed such that all items of same type are clustered together with no empty shelf between items of the same type and at least one empty shelf between two different types of items. At most two empty shelves can have consecutive numbers.") +
 p("The following additional facts are known:") +
 "<ol><li>A and B are to be placed in consecutively numbered shelves in increasing order.</li><li>I and J are to be placed in consecutively numbered shelves both higher numbered than the shelves in which A and B are kept.</li><li>D, E and F are savouries and are to be placed in consecutively numbered shelves in increasing order after all the biscuits and candies.</li><li>K is to be placed in shelf number 16.</li><li>L and J are items of the same type, while H is an item of a different type.</li><li>C is a candy and is to be placed in a shelf preceded by two empty shelves.</li><li>L is to be placed in a shelf preceded by exactly one empty shelf.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Savouries", p("Savouries come last, and K is on 16, so K is the fourth savoury: D, E, F, K on 13–16, with 12 empty.")),
       ("Types", p("I and J sit next to each other, so they are the same type; so are A and B. L and J match. The only split that gives 5 biscuits and 3 candies is L, J, I, A, B biscuits and C, G, H candies.")),
       ("Two layouts", p("Shelves 1–11 hold 8 items and 3 empty shelves. Two empties come right before C, and L has exactly one empty shelf before it.") +
       table(["Case", "Shelves 1–11", "Empty"], [["Candies first", "_ _ C G/H H/G _ L A B I/J J/I", "1, 2, 6, 12"], ["Biscuits first", "_ L A B I/J J/I _ _ C G/H H/G", "1, 7, 8, 12"]]))) +
 final("Two layouts, each with 2 × 2 orderings: 8 arrangements."),
 p("Place the savouries first; the facts about K and D, E, F leave no choice."),
 p("<b>Shelf arrangements:</b> count items and empty spaces together. Here 8 items and 3 empties fill exactly 11 shelves."))
P.dq(1, "In how many different ways can the items be arranged on the shelves?", ["8", "4", "2", "1"], "MCQ", "1", "Hard",
 "Can the candies come first, and can the biscuits come first?",
 steps(("From the set solution", p("Both orders work. In each, G and H can swap, and so can I and J: 2 × 4 = 8."))) + final("8, option 1"),
 [("2", "Only one of the two layouts."), ("3", "Leaves out the swaps."), ("4", "Several arrangements work.")])
P.dq(2, "Which of the following items is not a type of biscuit?", ["L", "A", "B", "G"], "MCQ", "4", "Medium",
 "Which items are left for the candies?",
 steps(("From the set solution", p("G is a candy."))) + final("G, option 4"),
 [("1", "L is a biscuit."), ("2", "A is a biscuit."), ("3", "B is a biscuit.")])
P.dq(3, "Which of the following can represent the numbers of the empty shelves in a possible arrangement?", ["1, 7, 11, 12", "1, 5, 6, 12", "1, 2, 6, 12", "1, 2, 8, 12"], "MCQ", "3", "Medium",
 "The two possibilities are 1, 2, 6, 12 and 1, 7, 8, 12.",
 steps(("From the set solution", p("Candies first leaves 1, 2, 6 and 12 empty."))) + final("Option 3"),
 [("1", "Leaves 11 and 12 next to each other with nothing before C."), ("2", "C needs two empties right before it."), ("4", "Doesn’t leave a gap before L.")])
P.dq(4, "Which of the following statements is necessarily true?", ["All biscuits are kept before candies.", "There are two empty shelves between the biscuits and the candies.", "All candies are kept before biscuits.", "There are at least four shelves between items B and C."], "MCQ", "4", "Medium",
 "Check both layouts.",
 steps(("Both layouts", p("Candies first: C on 3, B on 9. Biscuits first: B on 4, C on 9. Either way at least four shelves lie between them."))) + final("Option 4"),
 [("1", "Only in one layout."), ("2", "Only in one layout."), ("3", "Only in one layout.")])

# ---------------- Set 2: Archery ----------------
ARCH = table(["", "Round 1", "Round 2", "Round 3", "Round 4", "Round 5", "Round 6"],
             [["Tanzi", "-", "4", "-", "5", "NP", "NP"], ["Umeza", "-", "-", "-", "1", "2", "NP"], ["Wangdu", "-", "4", "-", "NP", "NP", "NP"],
              ["Xyla", "-", "-", "-", "1", "5", "-"], ["Yonita", "-", "-", "3", "5", "NP", "NP"], ["Zeneca", "-", "-", "-", "5", "5", "NP"]])
P.dilr_set(2, "Set 2 — An archery tournament", "Answer the questions on the basis of the following information.",
 p("Six players - Tanzi, Umeza, Wangdu, Xyla, Yonita and Zeneca competed in an archery tournament. The tournament had three compulsory rounds, Rounds 1 to 3. In each round every player shot an arrow at a target. Hitting the centre of the target (called bull’s eye) fetched the highest score of 5. The only other possible scores that a player could achieve were 4, 3, 2 and 1. Every bull’s eye score in the first three rounds gave a player one additional chance to shoot in the bonus rounds, Rounds 4 to 6. The possible scores in Rounds 4 to 6 were identical to the first three.") +
 p("A player’s total score in the tournament was the sum of his/her scores in all rounds played by him/her. The table below presents partial information on points scored by the players after completion of the tournament. In the table, NP means that the player did not participate in that round, while a hyphen means that the player participated in that round and the score information is missing.") + ARCH +
 p("The following facts are also known:") +
 "<ol><li>Tanzi, Umeza and Yonita had the same total score.</li><li>Total scores for all players, except one, were in multiples of three.</li><li>The highest total score was one more than double of the lowest total score.</li><li>The number of players hitting bull’s eye in Round 2 was double of that in Round 3.</li><li>Tanzi and Zeneca had the same score in Round 1 but different scores in Round 3.</li></ol>",
 "DILR::LR::Games_and_Tournaments",
 steps(("Bull’s eyes", p("Bonus rounds played = bull’s eyes in Rounds 1–3. Tanzi 1, Umeza 2, Wangdu 0, Xyla 3, Yonita 1, Zeneca 2.")),
       ("Where they fall", p("Tanzi’s Round 2 is 4. If his bull’s eye were in Round 3, Zeneca would need bull’s eyes in Rounds 2 and 3 and match Tanzi in Round 3, against fact 5. So Tanzi hit Round 1, and so did Zeneca. Fact 4 then forces 4 bull’s eyes in Round 2 (Xyla, Umeza, Yonita, Zeneca) and 2 in Round 3 (Xyla, Umeza).")),
       ("Scores", p("Tanzi 14 + t₃, Umeza 13 + u₁, Yonita 13 + y₁. Equal totals that must be multiples of 3 give 15, so t₃ = 1 and u₁ = y₁ = 2. Wangdu is at most 12 and is the lowest; the highest is odd, 2 × lowest + 1. Only 12 and 25 work: Wangdu 12, Xyla 25 (the one non-multiple of 3), Zeneca 24."))) +
 final("Totals: Tanzi, Umeza, Yonita 15; Wangdu 12; Xyla 25; Zeneca 24."),
 p("Count bull’s eyes from the bonus rounds first; that is what the table is really telling you."),
 p("<b>Hidden counts:</b> when one round’s entries depend on another’s, the dependency (here, bonus shots) is usually the way in."))
P.dq(5, "What was the highest total score?", ["25", "21", "24", "23"], "MCQ", "1", "Hard",
 "2 × lowest + 1, with the lowest a multiple of 3.",
 steps(("From the set solution", p("Xyla’s 25."))) + final("25, option 1"),
 [("2", "Too low."), ("3", "Zeneca’s total."), ("4", "Doesn’t fit fact 3.")])
P.dq(6, "What was Zeneca’s total score?", ["21", "22", "23", "24"], "MCQ", "4", "Hard",
 "20 plus her Round 3 score, which isn’t 1.",
 steps(("From the set solution", p("20 + 4 = 24."))) + final("24, option 4"),
 [("1", "Would need Round 3 = 1, Tanzi’s score."), ("2", "Not a multiple of 3."), ("3", "Not a multiple of 3.")])
P.dq(7, "Which of the following statements is true?", ["Xyla’s score was 23.", "Zeneca’s score was 23.", "Zeneca was the highest scorer.", "Xyla was the highest scorer."], "MCQ", "4", "Hard",
 "Compare 25 and 24.",
 steps(("From the set solution", p("Xyla 25, Zeneca 24."))) + final("Option 4"),
 [("1", "Xyla had 25."), ("2", "Zeneca had 24."), ("3", "Xyla scored more.")])
P.dq(8, "What was Tanzi’s score in Round 3?", ["4", "5", "3", "1"], "MCQ", "4", "Hard",
 "Tanzi’s total must be 15.",
 steps(("From the set solution", p("14 + t₃ = 15, so 1."))) + final("1, option 4"),
 [("1", "Total 18 isn’t possible with Umeza’s scores."), ("2", "A 5 would be a second bull’s eye."), ("3", "Total 17 isn’t a multiple of 3.")])

# ---------------- Set 3: Coded addition ----------------
ADD = table(["", "", "", "", "", "", "", ""],
            [["", "", "B", "H", "A", "A", "G", "F"], ["+", "", "A", "H", "J", "F", "K", "F"], ["", "A", "A", "F", "G", "C", "A", "F"]], first_col_header=False)
P.dilr_set(3, "Set 3 — A coded sum", "Answer the questions on the basis of the following information.",
 p("The following table represents addition of two six-digit numbers given in the first and the second rows, while the sum is given in the third row. In the representation, each of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 has been coded with one letter among A, B, C, D, E, F, G, H, J, K, with distinct letters representing distinct digits.") + ADD,
 "DILR::LR::Mathematical_Reasoning",
 steps(("Leading digit", p("Two six-digit numbers make a seven-digit sum, so A = 1.")),
       ("Column by column, from the right", p("F + F ends in F: F = 0. G + K ends in 1. A + F + carry = C, and C ≠ 1, so the carry is 1, C = 2 and G + K = 11. H + H + carry ends in 0: H = 5 with no carry in, carry out 1. B + 1 + 1 = 11: B = 9. Finally 1 + J = G.")),
       ("What’s left", p("Digits 3, 4, 6, 7, 8 for G, J, K, D, E, with G = J + 1 and G + K = 11.") +
       table(["J", "G", "K", "D and E"], [["3", "4", "7", "6, 8"], ["6", "7", "4", "3, 8"], ["7", "8", "3", "4, 6"]]))) +
 final("A = 1, B = 9, C = 2, F = 0, H = 5; three cases for the rest."),
 p("Start with the leftmost digit of the sum and the rightmost column."),
 p("<b>Cryptarithms:</b> a column like F + F = F, or a sum one digit longer than its parts, fixes a letter at once."))
P.dq(9, "Which digit does the letter A represent?", [], "TITA", "1", "Easy",
 "The sum has one more digit than the numbers added.",
 steps(("From the set solution", p("The carry into the seventh place can only be 1."))) + final(r"\(1\)"))
P.dq(10, "Which digit does the letter B represent?", [], "TITA", "9", "Medium",
 "Look at the leftmost column of the six-digit numbers.",
 steps(("From the set solution", p("B + A + 1 must give 11, so B = 9."))) + final(r"\(9\)"))
P.dq(11, "Which among the digits 3, 4, 6 and 7 cannot be represented by the letter D?", [], "TITA", "7", "Medium",
 "List D’s possible values from the three cases.",
 steps(("From the set solution", p("D can be 6, 8, 3 or 4, never 7."))) + final(r"\(7\)"))
P.dq(12, "Which among the digits 4, 6, 7 and 8 cannot be represented by the letter G?", [], "TITA", "6", "Medium",
 "G is 4, 7 or 8.",
 steps(("From the set solution", p("G = 6 would need J = 5, which is H."))) + final(r"\(6\)"))

# ---------------- Set 4: Vendors ----------------
P.dilr_set(4, "Set 4 — Five vendors, six aspects", "Answer the questions on the basis of the following information.",
 p("Five vendors are being considered for a service. The evaluation committee evaluated each vendor on six aspects: Cost, Customer Service, Features, Quality, Reach, and Reliability. Each of these evaluations are on a scale of 0 (worst) to 100 (perfect). The evaluation scores on these aspects are shown in the radar chart. For example, Vendor 1 obtains a score of 52 on Reliability, Vendor 2 obtains a score of 45 on Features and Vendor 3 obtains a score of 90 on Cost.") +
 fig("sipe_2019S1_DILR_S4.svg", "Radar chart of scores, approximately. Vendor 1: Reliability 52, Reach 80, Quality 75, Features 40, Customer Service 55, Cost 75. Vendor 2: 40, 55, 70, 45, 40, 80. Vendor 3: 75, 65, 65, 55, 50, 90. Vendor 4: 25, 45, 40, 90, 70, 70. Vendor 5: 60, 70, 50, 75, 30, 60."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Reading the chart", p("Scores to the nearest 5 (Vendor 1’s Reliability is given as 52):") +
       table(["", "V1", "V2", "V3", "V4", "V5"], [["Cost", "75", "80", "90", "70", "60"], ["Cust. Service", "55", "40", "50", "70", "30"], ["Features", "40", "45", "55", "90", "75"],
                                                 ["Quality", "75", "70", "65", "40", "50"], ["Reach", "80", "55", "65", "45", "70"], ["Reliability", "52", "40", "75", "25", "60"]]))) +
 final("Every question can be answered from this table; none of them hinges on a close reading."),
 p("Turn the chart into a table first; then each question is a quick scan."),
 p("<b>Radar charts:</b> read each axis separately, and note only the values you need. Exact values rarely matter."))
P.dq(13, "On which aspect is the median score of the five vendors the least?", ["Customer Service", "Cost", "Reliability", "Quality"], "MCQ", "1", "Medium",
 "Find the middle value on each axis.",
 steps(("Medians", p("Cost 75, Customer Service 50, Reliability 52, Quality 65."))) + final("Customer Service, option 1"),
 [("2", "Its median is 75."), ("3", "Its median is 52, just above."), ("4", "Its median is 65.")])
P.dq(14, "A vendor’s final score is the average of their scores on all six aspects. Which vendor has the highest final score?", ["Vendor 4", "Vendor 2", "Vendor 1", "Vendor 3"], "MCQ", "4", "Medium",
 "Compare totals.",
 steps(("Totals", p("V1 377, V2 330, V3 400, V4 340, V5 345."))) + final("Vendor 3, option 4"),
 [("1", "340."), ("2", "330."), ("3", "377, second.")])
P.dq(15, "List of all the vendors who are among the top two scorers on the maximum number of aspects is:", ["Vendor 2, Vendor 3 and Vendor 4", "Vendor 1 and Vendor 5", "Vendor 2 and Vendor 5", "Vendor 1 and Vendor 2"], "MCQ", "2", "Medium",
 "Write down the top two on each axis.",
 steps(("Top two", p("Cost V3, V2. Customer Service V4, V1. Features V4, V5. Quality V1, V2. Reach V1, V5. Reliability V3, V5.")),
       ("Counting", p("V1 3, V5 3, V2 2, V3 2, V4 2."))) + final("Option 2"),
 [("1", "Two each."), ("3", "Vendor 2 has two."), ("4", "Vendor 2 has two.")])
P.dq(16, "List of all the vendors who are among the top three vendors on all six aspects is:", ["Vendor 1 and Vendor 3", "Vendor 1", "Vendor 3", "None of the Vendors"], "MCQ", "3", "Medium",
 "Vendor 1 is last on Features.",
 steps(("Checking Vendor 3", p("1st on Cost and Reliability, 3rd on Reach, Quality, Features and Customer Service."))) + final("Vendor 3, option 3"),
 [("1", "Vendor 1 is last on Features."), ("2", "Vendor 1 is last on Features."), ("4", "Vendor 3 qualifies.")])

# ---------------- Set 5: Crimes by foreigners ----------------
RANKS = table(["", "IPC Crimes", "SLL Crimes", "Other Crimes"],
              [["Delhi", "*", "*", "*"], ["Goa", "*", "4", "*"], ["Haryana", "8", "6", "*"], ["Karnataka", "3", "2", "*"], ["Kerala", "*", "9", "*"],
               ["Maharashtra", "3", "4", "8"], ["Puducherry", "13", "29", "*"], ["Tamil Nadu", "11", "7", "*"], ["Telangana", "6", "9", "8"], ["West Bengal", "17", "*", "16"]])
P.dilr_set(5, "Set 5 — Crimes registered against foreigners", "Answer the questions on the basis of the following information.",
 p("The Ministry of Home Affairs is analysing crimes committed by foreigners in different states and union territories (UT) of India. All cases refer to the ones registered against foreigners in 2016.") +
 p("The number of cases - classified into three categories: IPC crimes, SLL crimes and other crimes - for nine states/UTs are shown in the figure below. These nine belong to the top ten states/UTs in terms of the total number of cases registered. The remaining state (among top ten) is West Bengal, where all the 520 cases registered were SLL crimes.") +
 fig("sipe_2019S1_DILR_S5.svg", "Stacked bar chart of cases (IPC, SLL, Other), approximately: Telangana 4, 14, 6; Puducherry 1, 0, 30; Kerala 8, 14, 12; Haryana 3, 27, 7; Maharashtra 16, 33, 6; Tamil Nadu 2, 24, 34; Goa 27, 33, 19; Karnataka 16, 49, 26; Delhi 64, 34, 46.") +
 p("The table below shows the ranks of the ten states/UTs mentioned above among ALL states/UTs of India in terms of the number of cases registered in each of the three category of crimes. A state/UT is given rank r for a category of crimes if there are (r – 1) states/UTs having a larger number of cases registered in that category of crimes. For example, if two states have the same number of cases in a category, and exactly three other states/UTs have larger numbers of cases registered in the same category, then both the states are given rank 4 in that category. Missing ranks in the table are denoted by *.") + RANKS,
 "DILR::DI::Graphs_and_Charts",
 steps(("Who is outside the top ten", p("Every other state/UT has a smaller total than the smallest of these ten. That caps how many cases they can have in any one category.")),
       ("Reading ranks", p("Rank r means exactly r − 1 states/UTs are ahead. A known rank tells you how many states sit above that state, and so where the missing ranks fall."))) +
 final("Combine the chart (sizes) with the rank table (positions among all states)."),
 p("Use the given ranks as anchors and slot the missing ones around them."),
 p("<b>Ranks with ties:</b> two states at rank 3 means no state has rank 4."))
P.dq(17, "What is the rank of Kerala in the ‘IPC crimes’ category?", [], "TITA", "5", "Hard",
 "Telangana is 6th. How many states are ahead of it?",
 steps(("Ahead of Telangana", p("Exactly 5: Delhi, Goa, Karnataka, Maharashtra, and one more. Kerala has more IPC cases than Telangana, so it is that fifth state.")),
       ("Kerala’s rank", p("Delhi 1, Goa 2, Karnataka and Maharashtra 3, Kerala 5."))) + final(r"\(5\)"))
P.dq(18, "In the two states where the highest total number of cases are registered, the ratio of the total number of cases in IPC crimes to the total number in SLL crimes is closest to", ["3 : 2", "19 : 20", "11 : 10", "1 : 9"], "MCQ", "4", "Medium",
 "Don’t forget West Bengal’s 520 cases.",
 steps(("The two states", p("West Bengal (520) and Delhi (about 144).")),
       ("Ratio", p("IPC: 0 + 64. SLL: 520 + 34. About 64 : 554, close to 1 : 9."))) + final("1 : 9, option 4"),
 [("1", "Leaves out West Bengal."), ("2", "Uses Delhi and Karnataka."), ("3", "Leaves out West Bengal.")])
P.dq(19, "Which of the following is DEFINITELY true about the ranks of states/UT in the ‘other crimes’ category?<br>(i) Tamil Nadu: 2<br>(ii) Puducherry: 3", ["both (i) and (ii)", "only (ii)", "neither (i) nor (ii)", "only (i)"], "MCQ", "1", "Hard",
 "Could a state outside the top ten have more ‘other’ cases than Puducherry?",
 steps(("Outside the top ten", p("Any other state has a total below Telangana’s 24, so fewer than 24 ‘other’ cases.")),
       ("So", p("Delhi 46, Tamil Nadu 34, Puducherry 30 take ranks 1, 2 and 3."))) + final("Option 1"),
 [("2", "(i) holds too."), ("3", "Both hold."), ("4", "(ii) holds too.")])
P.dq(20, "What is the sum of the ranks of Delhi in the three categories of crimes?", [], "TITA", "5", "Medium",
 "West Bengal leads in SLL; Karnataka is 2nd.",
 steps(("Delhi", p("IPC 1, SLL 3, Other 1."))) + final(r"\(5\)"))

# ---------------- Set 6: Street map ----------------
P.dilr_set(6, "Set 6 — Who can see whom", "Answer the questions on the basis of the following information.",
 p("The figure below shows the street map for a certain region with the street intersections marked from a through l. A person standing at an intersection can see along straight lines to other intersections that are in her line of sight and all other people standing at these intersections. For example, a person standing at intersection g can see all people standing at intersections b, c, e, f, h, and k. In particular, the person standing at intersection g can see the person standing at intersection e irrespective of whether there is a person standing at intersection f.") +
 fig("sipe_2019S1_DILR_S6.svg", "Street map: three vertical streets (a-b-c-d, e-f-g-h, i-j-k-l) and four horizontal streets (a-e-i, b-f-j, c-g-k, d-h-l), plus a diagonal street from b to g.") +
 p("Six people U, V, W, X, Y, and Z, are standing at different intersections. No two people are standing at the same intersection.") +
 p("The following additional facts are known.") +
 "<ol><li>X, U, and Z are standing at the three corners of a triangle formed by three street segments.</li><li>X can see only U and Z.</li><li>Y can see only U and W.</li><li>U sees V standing in the next intersection behind Z.</li><li>W cannot see V or Z.</li><li>No one among the six is standing at intersection d.</li></ol>",
 "DILR::LR::Routes_and_Networks",
 steps(("The triangle", p("The only triangles are b-f-g and b-c-g, both using the diagonal.")),
       ("Placing them", p("Trying each corner for X, U and Z with facts 2 and 4 leaves one layout: X at b, U at g, Z at f, so V is at e. Y must see U and W only: Y at k with W at l. W at l can’t see e or f.") +
       table(["Person", "U", "V", "W", "X", "Y", "Z"], [["Intersection", "g", "e", "l", "b", "k", "f"]]))) +
 final("A single arrangement."),
 p("Start with the triangle; there are only two."),
 p("<b>Line-of-sight puzzles:</b> list the lines (streets) first; each ‘can see only’ fact then rules out a lot."))
P.dq(21, "Who is standing at intersection a?", ["W", "Y", "No one", "V"], "MCQ", "3", "Hard",
 "Check the arrangement.",
 steps(("From the set solution", p("Nobody is at a."))) + final("No one, option 3"),
 [("1", "W is at l."), ("2", "Y is at k."), ("4", "V is at e.")])
P.dq(22, "Who can V see?", ["Z only", "U, W and Z only", "U and Z only", "U only"], "MCQ", "3", "Hard",
 "V is at e: column e-f-g-h and row a-e-i.",
 steps(("From the set solution", p("Down the column: Z (f) and U (g). Nobody on the row."))) + final("Option 3"),
 [("1", "U is on the same street."), ("2", "W is at l."), ("4", "Z is on the same street.")])
P.dq(23, "What is the minimum number of street segments that X must cross to reach Y?", ["1", "4", "2", "3"], "MCQ", "3", "Hard",
 "Use the diagonal.",
 steps(("Route", p("b to g along the diagonal, then g to k."))) + final("2, option 3"),
 [("1", "b and k aren’t joined directly."), ("2", "Longer than needed."), ("4", "Longer than needed.")])
P.dq(24, "Should a new person stand at intersection d, who among the six would she see?", ["W and X only", "U and W only", "U and Z only", "V and X only"], "MCQ", "1", "Hard",
 "d is on column a-b-c-d and row d-h-l.",
 steps(("From the set solution", p("X at b and W at l."))) + final("Option 1"),
 [("2", "U at g isn’t in line."), ("3", "Neither is in line."), ("4", "V at e isn’t in line.")])

# ---------------- Set 7: Dance finals ----------------
P.dilr_set(7, "Set 7 — Four dancers, four composers", "Answer the questions on the basis of the following information.",
 p("Princess, Queen, Rani and Samragni were the four finalists in a dance competition. Ashman, Badal, Gagan and Dyu were the four music composers who individually assigned items to the dancers. Each dancer had to individually perform in two dance items assigned by the different composers. The first item performed by the four dancers were all assigned by different music composers. No dancer performed her second item before the performance of the first item by any other dancer. The dancers performed their second items in the same sequence of their performance of their first items.") +
 p("The following additional facts are known:") +
 "<ol type=\"a\"><li>No composer who assigned item to Princess, assigned any item to Queen.</li><li>No composer who assigned item to Rani, assigned any item to Samragni.</li><li>The first performance was by Princess; this item was assigned by Badal.</li><li>The last performance was by Rani; this item was assigned by Gagan.</li><li>The items assigned by Ashman were performed consecutively. The number of performances between items assigned by each of the remaining composers was the same.</li></ol>",
 "DILR::LR::Scheduling",
 steps(("The order", p("Eight performances: the four dancers once, then again in the same order. Princess is 1st, Rani 4th, so Rani’s items are 4 and 8.")),
       ("Composers", p("Each composer has two items. Badal is at 1, Gagan at 8, Ashman’s two are adjacent, and Badal, Gagan and Dyu each have the same gap g. Trying g = 0 to 6, only g = 4 works.") +
       table(["Performance", "1", "2", "3", "4", "5", "6", "7", "8"], [["Composer", "B", "D", "G", "A", "A", "B", "D", "G"]])),
       ("Dancers", p("Princess has B and A, so Queen has D and G: performances 3 and 7. That leaves Samragni at 2 and 6 (D and B), which fits fact b."))) +
 final("Order: Princess, Samragni, Queen, Rani, twice."),
 p("Work out the composers by position before worrying about dancers."),
 p("<b>Equal-gap conditions:</b> try each gap size in turn; there are only a few."))
P.dq(25, "Which of the following is TRUE?", ["The second performance was composed by Dyu.", "The third performance was composed by Dyu.", "The third performance was composed by Ashman.", "The second performance was composed by Gagan."], "MCQ", "1", "Hard",
 "Read off the composer row.",
 steps(("From the set solution", p("Performance 2 is Dyu’s."))) + final("Option 1"),
 [("2", "3 is Gagan’s."), ("3", "3 is Gagan’s."), ("4", "2 is Dyu’s.")])
P.dq(26, "Which of the following is FALSE?", ["Samragni did not perform in any item composed by Ashman.", "Princess did not perform in any item composed by Dyu.", "Rani did not perform in any item composed by Badal.", "Queen did not perform in any item composed by Gagan."], "MCQ", "4", "Hard",
 "Queen performed 3 and 7.",
 steps(("From the set solution", p("Queen’s 3rd performance was Gagan’s."))) + final("Option 4"),
 [("1", "True: Samragni had D and B."), ("2", "True: Princess had B and A."), ("3", "True: Rani had A and G.")])
P.dq(27, "The sixth performance was composed by:", ["Badal", "Dyu", "Ashman", "Gagan"], "MCQ", "1", "Hard",
 "Badal’s second item.",
 steps(("From the set solution", p("6 is Badal’s."))) + final("Badal, option 1"),
 [("2", "Dyu has 2 and 7."), ("3", "Ashman has 4 and 5."), ("4", "Gagan has 3 and 8.")])
P.dq(28, "Which pair of performances were composed by the same composer?", ["The first and the seventh", "The third and the seventh", "The second and the sixth", "The first and the sixth"], "MCQ", "4", "Hard",
 "Badal’s items are 1 and 6.",
 steps(("From the set solution", p("1 and 6, both Badal."))) + final("Option 4"),
 [("1", "B and D."), ("2", "G and D."), ("3", "D and B.")])

# ---------------- Set 8: Game show ----------------
P.dilr_set(8, "Set 8 — A hundred mystery boxes", "Answer the questions on the basis of the following information.",
 p("A new game show on TV has 100 boxes numbered 1, 2, . . ., 100 in a row, each containing a mystery prize. The prizes are items of different types, a, b, c, . . ., in decreasing order of value. The most expensive item is of type a, a diamond ring, and there is exactly one of these. You are told that the number of items at least doubles as you move to the next type. For example, there would be at least twice as many items of type b as of type a, at least twice as many items of type c as of type b and so on. There is no particular order in which the prizes are placed in the boxes."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("The smallest counts", p("With k types, the counts are at least 1, 2, 4, …, 2ᵏ⁻¹, a total of 2ᵏ − 1.")),
       ("What that allows", p("Six types fit (at least 63 items); seven need at least 127. Two types also work: 1 and 99. The last type can always absorb the leftover boxes."))) +
 final("Between 2 and 6 types."),
 p("Think about the minimum each type can have, then put the slack in the last type."),
 p("<b>Doubling sequences:</b> 1 + 2 + 4 + … + 2ᵏ⁻¹ = 2ᵏ − 1."))
P.dq(29, "What is the minimum possible number of different types of prizes?", [], "TITA", "2", "Easy",
 "Can everything except the ring be one type?",
 steps(("From the set solution", p("1 ring and 99 of type b."))) + final(r"\(2\)"))
P.dq(30, "What is the maximum possible number of different types of prizes?", [], "TITA", "6", "Medium",
 "1 + 2 + 4 + 8 + 16 + 32 = 63.",
 steps(("From the set solution", p("Six types fit, for example 1, 2, 4, 8, 16, 69. Seven would need 127 boxes."))) + final(r"\(6\)"))
P.dq(31, "Which of the following is not possible?", ["There are exactly 75 items of type e.", "There are exactly 30 items of type b.", "There are exactly 45 items of type c.", "There are exactly 60 items of type d."], "MCQ", "3", "Medium",
 "With 45 of type c, type b has at most 22.",
 steps(("Option 3", p("Types a to c hold at most 1 + 22 + 45 = 68. A type d would need at least 90 more. Neither way reaches exactly 100.")),
       ("The others", p("1, 2, 4, 18, 75; 1, 30, 69; and 1, 9, 30, 60 all work."))) + final("Option 3"),
 [("1", "1, 2, 4, 18, 75 works."), ("2", "1, 30, 69 works."), ("4", "1, 9, 30, 60 works.")])
P.dq(32, "You ask for the type of item in box 45. Instead of being given a direct answer, you are told that there are 31 items of the same type as box 45 in boxes 1 to 44 and 43 items of the same type as box 45 in boxes 46 to 100. What is the maximum possible number of different types of items?", ["5", "6", "4", "3"], "MCQ", "1", "Hard",
 "That type has 75 items. It must be the last.",
 steps(("The big type", p("31 + 1 + 43 = 75. Nothing can come after it, so the other types share 25.")),
       ("Before it", p("1 + 2 + 4 + 18 = 25 gives four types, and five more would need at least 31."))) + final("5, option 1"),
 [("2", "Five earlier types need at least 31."), ("3", "Not the maximum."), ("4", "Not the maximum.")])
