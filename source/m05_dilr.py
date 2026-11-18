# -*- coding: utf-8 -*-
# Simp Mock 5: DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m05 import P
import m05_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Moving chairs (Q1–5) ----------------
CITY = table(["City", "Left after round"], [["Cuttack", "3"], ["Guwahati", "5"], ["Indore", "Winner"], ["Kolkata", "7"],
                                            ["Patna", "6"], ["Pune", "1"], ["Ranchi", "2"], ["Vizag", "4"]])
SEATS = table(["Chair", "Friend", "City"], [["1", "Ranju", "Indore"], ["2", "Kaka", "Guwahati"], ["3", "Titu", "Ranchi"], ["4", "Sunny", "Kolkata"],
                                            ["5", "Dolly", "Vizag"], ["6", "Pinku", "Pune"], ["7", "Gullu", "Patna"], ["8", "Bhola", "Cuttack"]])
ROUNDS = table(["Rd", "Chairs", "Gaps", "Safe", "Out"],
               [["1", "8", "4.93", "Dolly", "Pinku"], ["2", "7", "4.32", "Kaka", "Titu"], ["3", "6", "3.70", "Gullu", "Bhola"], ["4", "5", "3.08", "Sunny", "Dolly"],
                ["5", "4", "2.47", "Ranju", "Kaka"], ["6", "3", "1.85", "Sunny", "Gullu"], ["7", "2", "1.23", "Ranju", "Sunny"]])
P.dilr_set(1, "Set 1 — Moving chairs", DIR,
 p("Eight friends, born in eight different cities, play ‘Moving chairs’. Eight equally spaced chairs, numbered 1 to 8 in anticlockwise order, stand on a circular track facing outward, one friend on each. A fixed pointer outside the track points at chair 1 at the start.") +
 p("The game has seven rounds. In each round the chairs move clockwise round the track at 6° per second for exactly 37 seconds and then stop.") +
 "<ul><li>If the pointer then points between two chairs, the friend who has just passed the pointer is safe (call this friend A), and the next friend to reach the pointer is out.</li>"
 "<li>If the pointer points exactly at a chair, that friend is out, and the friend who passed the pointer just before is A.</li>"
 "<li>The chair of the friend who is out is removed, the remaining chairs are spaced equally again (keeping their numbers and their friends), and the next round starts with the pointer at A’s chair.</li></ul>" +
 p("One friend goes out in each round; the friend left after seven rounds is the winner. Facing outward, a friend’s left is the anticlockwise direction. Also known about the starting seats:") +
 "<ol><li>The pointer pointed at Ranju’s chair.</li><li>Bhola and Kaka sat next to Ranju.</li>"
 "<li>Dolly sat opposite Ranju, and Titu sat opposite Gullu.</li><li>Kaka sat third to the left of Gullu.</li>"
 "<li>Sunny sat next to both Titu and Dolly.</li><li>The eighth friend is Pinku.</li></ol>" +
 p("The table lists the friends’ birth cities (in no particular order) with the round after which each friend left.") + CITY,
 "DILR::LR::Puzzles",
 steps(("Seats", p("Ranju is on chair 1, Dolly on 5, and Bhola and Kaka on 2 and 8. Titu and Gullu are opposite each other among chairs 3, 4, 6, 7, so they take 3 and 7. Kaka is three places anticlockwise from Gullu, so Gullu is on 7 and Kaka on 2 (Bhola on 8), Titu on 3. Sunny, next to Titu and Dolly, is on 4, leaving Pinku on 6.")),
       ("One round", p("With n chairs, the gap between chairs is 360°/n, and the chairs turn 37 × 6 = 222°, so 222n/360 = 37n/60 gaps pass the pointer. Counting anticlockwise from A’s chair, the last whole chair is the new A and the next is out.") + ROUNDS),
       ("Cities", p("Matching the round each friend left gives every birth city.") + SEATS)) +
 final("Ranju wins."),
 p("Turn time into ‘gaps passed’: 37n/60 with n chairs left."),
 p("<b>Circular elimination:</b> after each removal, restart the count from the safe person with the new spacing."))
P.dq(1, "Who won the game?", ["Kaka", "Gullu", "Ranju", "Sunny"], "MCQ", "3", "Medium",
 "Play the seven rounds.",
 steps(("Rounds", p("Out in order: Pinku, Titu, Bhola, Dolly, Kaka, Gullu, Sunny. Ranju is left."))) + final("Option 3"),
 [("1", "Out in round 5."), ("2", "Out in round 6."), ("4", "Out in round 7.")])
P.dq(2, "At the start, who sat three places to the right of the friend born in Ranchi?", ["The friend born in Cuttack", "The friend born in Pune", "The friend born in Vizag", "The friend born in Kolkata"], "MCQ", "1", "Medium",
 "Ranchi: the friend who left after round 2.",
 steps(("Ranchi", p("Titu (chair 3). Right is clockwise: chairs 2, 1, 8.")),
       ("Answer", p("Bhola, on chair 8, left after round 3: Cuttack."))) + final("Option 1"),
 [("2", "Pinku, chair 6."), ("3", "Dolly, chair 5."), ("4", "Sunny, chair 4.")])
P.dq(3, "If the friends born in Kolkata and Guwahati swap seats before round 1, who sits opposite the friend born in Guwahati?", ["Gullu", "Pinku", "Titu", "Bhola"], "MCQ", "4", "Medium",
 "Kolkata is Sunny, Guwahati is Kaka.",
 steps(("Swap", p("Kaka moves to Sunny’s chair 4; opposite it is chair 8, Bhola."))) + final("Option 4"),
 [("1", "Gullu is opposite chair 3."), ("2", "Pinku is opposite chair 2."), ("3", "Titu is opposite chair 7.")])
P.dq(4, "Would the winner change if, from round 5 onwards, the chairs stopped after 40 seconds instead of 37?", ["The new winner is the friend who started just to the left of the original winner.", "The new winner is the friend who started three places to the left of the original winner.", "The new winner is the friend who started two places to the right of the original winner.", "The winner does not change."], "MCQ", "4", "Medium",
 "Replay rounds 5–7 with 40n/60 gaps.",
 steps(("Round 5", p("4 chairs: 2.67 gaps from Sunny: Gullu, Ranju (safe); Kaka out.")),
       ("Round 6", p("3 chairs: exactly 2 gaps from Ranju: the pointer is at Gullu, who is out; Sunny is A.")),
       ("Round 7", p("2 chairs: 1.33 gaps from Sunny: Ranju safe, Sunny out. Ranju still wins."))) + final("Option 4"),
 [("1", "Ranju still wins."), ("2", "Ranju still wins."), ("3", "Ranju still wins.")])
P.dq(5, "Who would win if the chairs stopped after 40 seconds in every round?", ["Kaka", "Dolly", "Titu", "Bhola"], "MCQ", "1", "Hard",
 "40n/60 gaps; watch for exact stops when n is a multiple of 3.",
 steps(("Rounds", p("Out in order: Gullu, Sunny, Ranju (exact stop), Pinku, Titu, Bhola (exact stop), Dolly.")),
       ("Winner", p("Kaka."))) + final("Option 1"),
 [("2", "Out in round 7."), ("3", "Out in round 5."), ("4", "Out in round 6.")])

# ---------------- Set 2: Ten products (Q6–10) ----------------
COST = table(["Product", "Cost 2020-21"], [["A", "150"], ["B", "40"], ["C", "420"], ["D", "360"], ["E", "576"],
                                           ["F", "800"], ["G", "760"], ["H", "380"], ["I", "330"], ["J", "50"]])
ALL2 = (p("2020-21:") + table(["", "Revenue", "Cost"], [['A', '165', '150'], ['B', '45', '40'], ['C', '495', '420'], ['D', '405', '360'], ['E', '720', '576'], ['F', '990', '800'], ['G', '880', '760'], ['H', '396', '380'], ['I', '220', '330'], ['J', '55', '50']]) +
        p("2021-22:") + table(["", "Revenue", "Cost"], [['A', '198', '165'], ['B', '49.5', '35'], ['C', '445.5', '399'], ['D', '445.5', '351'], ['E', '792', '648'], ['F', '1237.5', '940'], ['G', '792', '646'], ['H', '445.5', '475'], ['I', '198', '198'], ['J', '49.5', '65']]))
P.dilr_set(2, "Set 2 — Revenue and cost of ten products", DIR,
 p("Each circle below stands for a different product, A to J. The area of a circle is proportional to the product’s revenue in 2021-22. The centre of a circle shows the percentage change from 2020-21 to 2021-22 in the product’s revenue (horizontal) and in its cost (vertical). The grid squares are 5% wide.") +
 p("One unit of length is half the side of a grid square (2.5%). Every centre lies on a whole number of units, and every diameter is a whole number of units. A circle 1 unit across stands for revenue of ₹495 million (₹49.5 crore).") + F.BUBBLES +
 p("The table gives each product’s total cost in 2020-21, in ₹ crore.") + COST +
 p("Profit = Revenue − Cost (when revenue is higher); Loss = Cost − Revenue (when cost is higher)."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Revenue 2021-22", p("Revenue grows with the square of the diameter: 49.5 × d² crore, so 49.5, 198, 445.5, 792 and 1237.5 for diameters 1 to 5.")),
       ("Back to 2020-21", p("Revenue 2020-21 = revenue 2021-22 ÷ (1 + revenue change); cost 2021-22 = cost 2020-21 × (1 + cost change).")),
       ("All values (₹ crore)", ALL2)) +
 final("Read diameters and centres, then fill the table."),
 p("Area ∝ d²: a circle twice as wide is four times the revenue."),
 p("<b>Bubble charts:</b> three data per bubble — position on each axis and size. Convert all three before calculating."))
P.dq(6, "For how many products did the cost change by more than ₹100 crore (up or down) from 2020-21 to 2021-22?", [], "TITA", "3", "Medium",
 "Cost 2021-22 − cost 2020-21.",
 steps(("Changes", p("F +140, G −114, I −132. All others are within 100 (the next largest is H, +95)."))) + final("3"))
P.dq(7, "Each option gives a product and a possible total 2020-21 revenue (in ₹ crore) of all products in that product’s industry. Each product had the 4th highest 2020-21 revenue in its industry. Which pair is impossible?", ["B: 187", "D: 1618", "E: 2890", "H: 1600"], "MCQ", "2", "Medium",
 "With three larger products, the industry total is more than 4 × the product’s revenue.",
 steps(("Bounds", p("B: > 180. D: > 1620. E: > 2880. H: > 1584.")),
       ("Check", p("Only D’s 1618 falls short."))) + final("Option 2"),
 [("1", "187 > 180."), ("3", "2890 > 2880."), ("4", "1600 > 1584.")])
P.dq(8, "Some products made the same profit in both years. What is the total of that profit (in ₹ crore, for one year)?", [], "TITA", "144", "Medium",
 "Compare profit in each year.",
 steps(("Same profit", p("Only E: 720 − 576 = 144 and 792 − 648 = 144."))) + final("144"))
P.dq(9, "Which statements are true?<br>1. Every product with a loss in 2021-22 lost no more than ₹30 crore.<br>2. Exactly one product had revenue equal to cost in 2021-22.<br>3. Exactly one product made the same profit in both years.", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "All three"], "MCQ", "4", "Medium",
 "Check H, J, I and E.",
 steps(("1", p("Losses: H 29.5, J 15.5. True.")), ("2", p("Only I: 198 and 198. True.")), ("3", p("Only E. True."))) + final("Option 4"),
 [("1", "Statement 3 is also true."), ("2", "Statement 1 is also true."), ("3", "Statement 2 is also true.")])
P.dq(10, "What is the largest percentage increase in profit of any product from 2020-21 to 2021-22?", ["260", "200", "190", "160"], "MCQ", "3", "Medium",
 "Small profits can grow by large percentages.",
 steps(("B", p("5 to 14.5: up 190%.")), ("Others", p("A 120%, D 110%, F about 57%, G about 22%."))) + final("Option 3"),
 [("1", "No product grows this much."), ("2", "No product grows this much."), ("4", "Not the largest.")])

# ---------------- Set 3: Five former presidents (Q11–15) ----------------
P3 = table(["Name", "City", "Expert on"], [["Bose", "Atl./Bos.", "Japan"], ["Chawla", "New York", "Germany"], ["Kapur", "Chicago", "China"],
                                           ["Oberoi", "Bos./Atl.", "Australia"], ["Tandon", "Miami", "India"]])
P.dilr_set(3, "Set 3 — Five former presidents", DIR,
 p("A country’s president meets five former presidents — Bose, Chawla, Kapur, Oberoi and Tandon — to consult them on foreign policy. Each has retired to a different one of Atlanta, Boston, Chicago, Miami and New York, and each is an expert on relations with a different one of Australia, China, Germany, India and Japan.") +
 "<ol><li>The Japan expert has not settled in New York.</li><li>Tandon and Oberoi are not experts on Germany or Japan.</li>"
 "<li>Kapur is not an expert on Australia or India.</li><li>Bose and Chawla have not settled in Chicago or Miami, and neither is an expert on China or India.</li>"
 "<li>Oberoi is not an expert on India.</li><li>The Australia expert has not settled in Miami.</li>"
 "<li>Whoever settled in Chicago is not an expert on Germany or Japan.</li><li>Tandon and Oberoi have not settled in New York or Chicago.</li>"
 "<li>Chawla is not an expert on Japan.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Chicago", p("Bose, Chawla, Tandon and Oberoi are all ruled out of Chicago, so Kapur is there; he is not a Germany, Japan, Australia or India expert, so China.")),
       ("India and Japan", p("India: not Bose, Chawla, Kapur or Oberoi, so Tandon. Japan: not Tandon, Oberoi or Chawla, so Bose.")),
       ("The rest", p("Oberoi cannot do Germany, so Chawla does Germany and Oberoi Australia. Bose (Japan) is not in New York, so Chawla is; Oberoi (Australia) is not in Miami, so Tandon is. Bose and Oberoi share Atlanta and Boston.") + P3)) +
 final("Two cases: Bose and Oberoi can swap Atlanta and Boston."),
 p("Start with the city everyone else is barred from."),
 p("<b>Two-attribute matching:</b> look for a row or column with only one option left, fix it, and repeat."))
P.dq(11, "For how many of the five are both the city and the country fixed?", [], "TITA", "3", "Easy",
 "Bose and Oberoi share two cities.",
 steps(("Fixed", p("Chawla, Kapur and Tandon."))) + final("3"))
P.dq(12, "Statement A: Kapur settled in Chicago. Statement B: Kapur is a China expert. Which is right?", ["Only A is correct.", "Only B is correct.", "Both are correct.", "A may or may not be correct, but B is correct."], "MCQ", "3", "Easy",
 "Both follow from the first step.",
 steps(("Both", p("Kapur is in Chicago and is the China expert."))) + final("Option 3"),
 [("1", "B is also correct."), ("2", "A is also correct."), ("4", "A is certain.")])
P.dq(13, "Who settled in New York?", ["Chawla", "Tandon", "The Japan expert", "The India expert"], "MCQ", "1", "Easy",
 "The Japan expert, Bose, is not in New York.",
 steps(("New York", p("Only Bose and Chawla could be there; Bose is the Japan expert, so Chawla."))) + final("Option 1"),
 [("2", "Miami."), ("3", "Bose is not in New York."), ("4", "Tandon is in Miami.")])
P.dq(14, "If Oberoi settled in Atlanta, where did Bose settle?", ["Chicago", "Boston", "Miami", "Oberoi cannot be in Atlanta"], "MCQ", "2", "Easy",
 "Bose and Oberoi share Atlanta and Boston.",
 steps(("Bose", p("Boston."))) + final("Option 2"),
 [("1", "Kapur is in Chicago."), ("3", "Tandon is in Miami."), ("4", "Atlanta is possible.")])
P.dq(15, "Which combination is definitely correct?", ["Chawla – Chicago – Germany", "Tandon – Miami – India", "Kapur – Boston – China", "More than one of these"], "MCQ", "2", "Easy",
 "Check each against the table.",
 steps(("Check", p("Chawla is in New York; Kapur is in Chicago; Tandon – Miami – India is right."))) + final("Option 2"),
 [("1", "Chawla is in New York."), ("3", "Kapur is in Chicago."), ("4", "Only option 2.")])

# ---------------- Set 4: Votes for philosophers (Q16–20) ----------------
VOTES = table(["Years", "A", "B", "C", "D", "E"], [["1–5", "26", "28", "17", "17", "19"], ["6–10", "19", "10", "18", "16", "19"],
                                                 ["11–15", "21", "25", "25", "42", "34"], ["15+", "16", "40", "46", "40", "22"]])
P.dilr_set(4, "Set 4 — The most influential philosopher", DIR,
 p("A philosophy association asked 500 scholars to name the most influential philosopher in the history of Europe. The scholars are grouped by years of research experience: 1–5, 6–10, 11–15 and more than 15. Each scholar voted for exactly one of Locke, Mill, Smith, Ricardo and Spencer, disguised in the table as A to E in some order.") + VOTES +
 "<ol><li>Spencer and Locke received equal votes in exactly one group. So did Ricardo and Smith, Mill and Ricardo, and Mill and Smith.</li>"
 "<li>Mill received more votes than Spencer in exactly three of the four groups.</li>"
 "<li>Smith received more votes than Ricardo in exactly one group.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("Equal pairs", p("In the table the equal entries are A–E (6–10), C–D (1–5), B–C (11–15) and B–D (15+). Mill, Ricardo and Smith each appear in two of the four named pairs, so they are B, C and D; Spencer and Locke are A and E.")),
       ("Mill and Spencer", p("B beats A in three groups but E in only two; C beats A in two and E in one; D beats A in two and E in two. Only B against A gives three, so Mill = B, Spencer = A, Locke = E.")),
       ("Smith and Ricardo", p("D beats C only in 11–15 (42 > 25), while C beats D in 6–10 and 15+ (they tie in 1–5). Smith beats Ricardo in exactly one group, so Smith = D and Ricardo = C.")),
       ("Key", p("A Spencer, B Mill, C Ricardo, D Smith, E Locke."))) +
 final("All five disguises are fixed."),
 p("Count how often each name appears in the equal-vote pairs: names appearing twice form one block."),
 p("<b>Disguised tables:</b> use the pattern of ties first, then ‘more than in k groups’ counts."))
P.dq(16, "For how many philosophers can the disguise be fixed?", [], "TITA", "5", "Medium",
 "Ties, then Mill, then Smith.",
 steps(("All", p("A Spencer, B Mill, C Ricardo, D Smith, E Locke."))) + final("5"))
P.dq(17, "How many votes did Smith receive in the ‘more than 15 years’ group? (Enter 0 if it cannot be determined.)", [], "TITA", "40", "Easy",
 "Smith is D.",
 steps(("D, 15+", p("40."))) + final("40"))
P.dq(18, "Which statement is incorrect?", ["Smith received more votes than Mill in exactly two groups.", "Spencer received more votes than Ricardo in only one group.", "Ricardo received more votes than Locke in only one group.", "Locke received more votes than Mill in exactly two groups."], "MCQ", "2", "Medium",
 "Compare the columns.",
 steps(("1", p("D > B in 6–10 and 11–15: two. Correct.")), ("2", p("A > C in 1–5 and 6–10: two, not one. Incorrect.")),
       ("3", p("C > E only in 15+. Correct.")), ("4", p("E > B in 6–10 and 11–15. Correct."))) + final("Option 2"),
 [("1", "True."), ("3", "True."), ("4", "True.")])
P.dq(19, "In which group did Mill receive the most votes?", ["More than 15 years", "11 to 15 years", "6 to 10 years", "1 to 5 years"], "MCQ", "1", "Easy",
 "Mill is B.",
 steps(("B", p("28, 10, 25, 40: most in 15+."))) + final("Option 1"),
 [("2", "25."), ("3", "10."), ("4", "28.")])
P.dq(20, "What is the ratio of Mill’s votes in the 6–10 group to Smith’s votes in the 15+ group?", ["1 : 1", "1 : 4", "2 : 1", "4 : 1"], "MCQ", "2", "Easy",
 "B in 6–10, D in 15+.",
 steps(("Ratio", p("10 : 40 = 1 : 4."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Upside down.")])
