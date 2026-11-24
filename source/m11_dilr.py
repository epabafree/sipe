# -*- coding: utf-8 -*-
# Simp Mock 11: DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m11 import P

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Four share prices (Q1–5) ----------------
SH = table(["", "Apex", "Ban.", "Cob.", "Delta"], [["Mon", "510", "510", "510", "520"], ["Tue", "a", "b", "500", "530"],
                                                         ["Wed", "b", "a", "510", "530"], ["Thu", "530", "530", "510", "530"], ["Fri", "530", "530", "520", "530"]])
P.dilr_set(1, "Set 1 — Four share prices over a week", DIR,
 p("An analyst tracks the shares of four companies — Apex Bank, Banyan Investments, Cobalt Cements and Delta Agro — from Monday to Friday, noting only each share’s highest price of the day. That gives 20 prices, each one of ₹500, ₹510, ₹520 and ₹530.") +
 "<ol><li>The five-day averages of Apex, Banyan, Cobalt and Delta were ₹524, ₹524, ₹510 and ₹528.</li>"
 "<li>The average of Wednesday’s four prices was ₹2.5 more than Tuesday’s.</li>"
 "<li>The daily total of the four prices rose every day from Monday to Friday.</li>"
 "<li>The lowest of the 20 prices occurred only once, and not on Monday or Wednesday.</li>"
 "<li>Delta’s price was higher than Cobalt’s every day.</li>"
 "<li>No share’s price was the same on all five days.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Delta and Cobalt", p("Delta totals 2640: four days at 530, one at 520. Cobalt totals 2550 and is not constant: 500 + 510 × 3 + 520. The single 500 is the lowest price.")),
       ("Apex and Banyan", p("Each totals 2620 with no 500: 510 + 520 + 530 × 3 or 520 × 3 + 530 × 2.")),
       ("Daily totals", p("All 20 add to 10,430. Monday is at least 510 + 510 + 510 + 520 = 2050 and Friday at most 530 × 3 + 520 = 2110. With rising totals and Wednesday = Tuesday + 10, the only fit is 2050, 2080, 2090, 2100, 2110.")),
       ("Prices", SH + p("a and b are 520 and 530 in either order: two cases."))) +
 final("Two cases, differing only on Tuesday and Wednesday."),
 p("Fix the shares with the tightest averages first, then the daily totals."),
 p("<b>Price grids with averages:</b> an average close to an extreme value leaves very few ways to make the total."))
P.dq(1, "What was the total of the four prices on Tuesday?", ["2080", "2070", "Either 2060 or 2070", "Either 2070 or 2080"], "MCQ", "1", "Medium",
 "Daily totals are fixed.",
 steps(("Read", p("2080."))) + final("Option 1"),
 [("2", "Not a fit."), ("3", "Not a fit."), ("4", "Only 2080 works.")])
P.dq(2, "What was Banyan’s price on Wednesday?", ["510", "520", "530", "Either 520 or 530"], "MCQ", "4", "Medium",
 "Apex and Banyan swap.",
 steps(("Read", p("520 or 530."))) + final("Option 4"),
 [("1", "Monday."), ("2", "One case only."), ("3", "One case only.")])
P.dq(3, "On which day was a price of ₹500 noted?", ["Tuesday", "Thursday", "Either Tuesday or Thursday", "Friday"], "MCQ", "1", "Medium",
 "Cobalt’s 500.",
 steps(("Read", p("Tuesday."))) + final("Option 1"),
 [("2", "Cobalt is 510."), ("3", "Only Tuesday."), ("4", "Cobalt is 520.")])
P.dq(4, "Which of these statements is/are necessarily false?<br>A: Cobalt’s price changed from the previous day exactly 3 times.<br>B: The number of times Apex’s price changed from the previous day cannot be determined uniquely.", ["A only", "B only", "Both A and B", "Neither A nor B"], "MCQ", "4", "Medium",
 "Count changes in each case.",
 steps(("A", p("510 → 500 → 510 → 510 → 520: three changes. True.")),
       ("B", p("Apex 510, 520, 530, 530, 530 (2 changes) or 510, 530, 520, 530, 530 (3). True."))) + final("Option 4"),
 [("1", "A is true."), ("2", "B is true."), ("3", "Both are true.")])
P.dq(5, "On how many days did Apex and Banyan have the same price?", ["1", "2", "3", "4"], "MCQ", "3", "Medium",
 "They differ only on Tuesday and Wednesday.",
 steps(("Count", p("Monday, Thursday, Friday: 3."))) + final("Option 3"),
 [("1", "Too few."), ("2", "Too few."), ("4", "Tuesday and Wednesday differ.")])

# ---------------- Set 2: Fractions of the maximum marks (Q6–10) ----------------
FR = table(["", "Phy.", "Chem.", "Maths", "Stat."], [["A", r"\(\tfrac58\)", r"\(\tfrac23\)", r"\(\tfrac34\)", r"\(\tfrac78\)"], ["B", r"\(\tfrac34\)", r"\(\tfrac56\)", r"\(\tfrac{19}{20}\)", r"\(\tfrac34\)"],
                                                    ["C", r"\(\tfrac56\)", r"\(\tfrac79\)", r"\(\tfrac89\)", r"\(\tfrac{7}{10}\)"], ["D", r"\(\tfrac{7}{12}\)", r"\(\tfrac{23}{30}\)", r"\(\tfrac23\)", r"\(\tfrac{11}{16}\)"]])
CASES = table(["#", "Phy.", "Chem.", "Maths", "Stat."], [["1", "240", "270", "180", "320"], ["2", "240", "270", "180", "400"], ["3", "240", "270", "180", "480"], ["4", "240", "360", "180", "480"]])
CMARKS = table(["#", "C: Chem.", "C: Stat.", "C: total"], [["1", "210", "224", "794"], ["2", "210", "280", "850"], ["3", "210", "336", "906"], ["4", "280", "336", "976"]])
P.dilr_set(2, "Set 2 — Marks as fractions of the maximum", DIR,
 p("Four students, A, B, C and D, sit an entrance test with four papers: Physics, Chemistry, Mathematics and Statistics. The table gives each student’s mark in each paper as a fraction of that paper’s maximum marks.") + FR +
 "<ol><li>Each student’s marks are in descending order: Statistics, Chemistry, Physics, Mathematics. Every mark is a natural number.</li>"
 "<li>The maximum marks are in the same descending order: Statistics, Chemistry, Physics, Mathematics.</li>"
 "<li>Mathematics has maximum marks above 100; Statistics below 500.</li>"
 "<li>Every paper’s maximum marks are a multiple of 10.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("Multiples", p("Whole marks need the maximum to be a multiple of the denominators’ LCM and of 10: Physics 120, Chemistry 90, Maths 180, Statistics 80.")),
       ("Order and limits", p("Maths 180 or 360; Physics above Maths; Chemistry above Physics; Statistics above Chemistry and below 500.")),
       ("Each student’s order", p("Checking every student’s marks against rule 1 leaves four cases:") + CASES),
       ("C’s marks", p("Physics 200, Maths 160 in every case.") + CMARKS)) +
 final("Physics and Maths fixed; Chemistry and Statistics vary."),
 p("Turn fractions into ‘multiple of’ conditions first, then apply the order rules."),
 p("<b>Fraction tables:</b> the LCM of the denominators in a column is the step size for that column’s maximum."))
P.dq(6, "In how many of the four papers can every student’s mark be determined exactly?", [], "TITA", "2", "Medium",
 "Which maxima are fixed?",
 steps(("Read", p("Physics (240) and Maths (180)."))) + final("2"))
P.dq(7, "What is the difference between C’s largest and smallest possible totals over the four papers?", [], "TITA", "182", "Medium",
 "Use C’s totals in the four cases.",
 steps(("Difference", p("976 − 794 = 182."))) + final("182"))
P.dq(8, "Which of these cannot be a student’s mark in Statistics?", ["300", "325", "330", "360"], "MCQ", "2", "Medium",
 "List the possible Statistics marks.",
 steps(("Marks", p("Maximum 320: 280, 240, 224, 220. 400: 350, 300, 280, 275. 480: 420, 360, 336, 330.")),
       ("Answer", p("325 never occurs."))) + final("Option 2"),
 [("1", "B at 400."), ("3", "D at 480."), ("4", "B at 480.")])
P.dq(9, "If C scored 280 in Chemistry, what is A’s total in Maths and Statistics?", ["555", "485", "Either 555 or 485", "C cannot score 280 in Chemistry"], "MCQ", "1", "Medium",
 "280 needs Chemistry out of 360: case 4.",
 steps(("Case 4", p("A: Maths 135, Statistics 420. Total 555."))) + final("Option 1"),
 [("2", "Uses the wrong case."), ("3", "Only case 4 fits."), ("4", "It is possible.")])
P.dq(10, "If D scored 140 in Physics, which can be C’s total in Chemistry and Statistics?", ["484", "520", "616", "D cannot score 140 in Physics"], "MCQ", "3", "Medium",
 "D always scores 140 in Physics.",
 steps(("C’s totals", p("434, 490, 546 or 616."))) + final("Option 3"),
 [("1", "Not a case."), ("2", "Not a case."), ("4", "Always 140.")])

# ---------------- Set 3: Codes for states and UTs (Q11–15) ----------------
CODES = ("<ul><li>1: Chandigarh + one pair of Delhi/Dadra… or Ladakh/Lakshadweep</li><li>2: Haryana, Goa, Gujarat, Himachal</li>"
         "<li>3: Kerala, Sikkim, Jharkhand, Nagaland, Karnataka</li><li>4: Andaman &amp; Nicobar, J&amp;K, Puducherry</li>"
         "<li>5: Assam, Uttarakhand, Andhra, Arunachal, UP</li><li>6: Tripura, Chhattisgarh, Tamil Nadu, Telangana</li>"
         "<li>7: Mizoram, Bihar, MP, Maharashtra, Manipur, Meghalaya</li><li>8: West Bengal, Odisha, Punjab, Rajasthan</li><li>9: the other UT pair</li></ul>")
P.dilr_set(3, "Set 3 — Digit codes for states and union territories", DIR,
 p("Neeta coded India’s 28 states and 8 union territories (UTs) with the digits 1 to 9, using every digit. Each state and UT gets one digit.") +
 "<ol><li>Each digit codes only states or only UTs.</li>"
 "<li>No digit codes 4 or more UTs, and every digit that codes UTs codes at least two. UT codes are perfect squares. Digit 9 codes half as many UTs as there are states with code 2. Delhi, Ladakh and Chandigarh are not coded 4.</li>"
 "<li>States (or UTs) with the same initial letter get the same code; e.g. Ladakh and Lakshadweep share a code.</li>"
 "<li>Digit 7 alone codes the most states: 6.</li>"
 "<li>Tripura and Chhattisgarh share a code, one less than that of Mizoram and Bihar and one more than that of Assam and Uttarakhand.</li>"
 "<li>Kerala, Sikkim, Jharkhand and Nagaland share a code. Haryana’s and Goa’s codes are prime; West Bengal’s is not.</li>"
 "<li>The fewest states coded by any digit is more than the most UTs coded by any digit.</li></ol>" +
 p("The other 15 states are Andhra Pradesh, Arunachal Pradesh, Gujarat, Himachal Pradesh, Karnataka, Madhya Pradesh, Maharashtra, Manipur, Meghalaya, Odisha, Punjab, Rajasthan, Tamil Nadu, Telangana and Uttar Pradesh. The 8 UTs are Delhi, Ladakh, Chandigarh, Lakshadweep, Andaman &amp; Nicobar Islands, Dadra &amp; Nagar Haveli and Daman &amp; Diu, Jammu &amp; Kashmir, and Puducherry."),
 "DILR::LR::Puzzles",
 steps(("UT digits", p("1, 4 and 9 code all 8 UTs, at most 3 each: 3, 3, 2. If 9 coded 3, digit 2 would code 6 states, clashing with clue 4. So 9 codes 2, digit 2 codes 4 states, and 1 and 4 code 3 each.")),
       ("State counts", p("Digit 7 has 6, digit 2 has 4; the other 18 go to 3, 5, 6, 8, each with 4 or 5 (clue 7 and clue 4): 4 + 4 + 5 + 5.")),
       ("Letters", p("M-states with Mizoram and Bihar make 6: digit 7. So Tripura’s group is 6 and Assam’s is 5, with Andhra, Arunachal and UP: five states. Digit 6: Tripura, Chhattisgarh, Tamil Nadu, Telangana.")),
       ("The rest", p("H and G states (Haryana, Himachal, Goa, Gujarat) take prime 2. K, S, J, N states (five) take 3. West Bengal, Odisha, Punjab, Rajasthan take 8.")),
       ("UTs", p("Digit 4 cannot have Delhi, Ladakh, Chandigarh or their initial-mates, so 4 codes Andaman & Nicobar, J&K, Puducherry. Chandigarh joins one D/L pair on 1; the other pair is 9.") + CODES)) +
 final("Only the D-pair and L-pair of UTs can swap between 1 and 9."),
 p("Count first (how many per digit), then use initial letters to move whole groups."),
 p("<b>Coding with group rules:</b> a ‘same initial letter’ rule turns names into blocks of fixed size — match block sizes to digit counts."))
P.dq(11, "How many states and UTs in all are coded with one of 1, 3, 5, 6 and 8?", ["21", "22", "19", "Cannot be determined"], "MCQ", "1", "Medium",
 "Digit 1 codes 3 UTs; 3, 5, 6, 8 code 18 states.",
 steps(("Count", p("3 + 18 = 21."))) + final("Option 1"),
 [("2", "Off by one."), ("3", "Off by two."), ("4", "The counts are fixed.")])
P.dq(12, "What is the code for Andaman and Nicobar Islands?", ["4", "1", "9", "Cannot be determined"], "MCQ", "1", "Medium",
 "Who can take digit 4?",
 steps(("Read", p("Digit 4: Andaman & Nicobar, J&K, Puducherry."))) + final("Option 1"),
 [("2", "Chandigarh’s code."), ("3", "A D- or L-pair."), ("4", "It is fixed.")])
P.dq(13, "For how many digits is the complete list of states and UTs known?", ["8", "7", "6", "5"], "MCQ", "2", "Medium",
 "Only 1 and 9 are unsure.",
 steps(("Count", p("Digits 2 to 8: 7."))) + final("Option 2"),
 [("1", "1 and 9 are open."), ("3", "Too few."), ("4", "Too few.")])
P.dq(14, "Which group need NOT be coded with the same digit?", ["J&K, Puducherry, Andaman & Nicobar", "Ladakh, Chandigarh, Lakshadweep", "Odisha, Punjab, Rajasthan", "Manipur, Bihar, Maharashtra"], "MCQ", "2", "Medium",
 "Ladakh’s pair may be on 9.",
 steps(("Check", p("Chandigarh is 1; Ladakh and Lakshadweep are 1 or 9."))) + final("Option 2"),
 [("1", "All 4."), ("3", "All 8."), ("4", "All 7.")])
P.dq(15, "What is West Bengal’s code?", [], "TITA", "8", "Medium",
 "Not prime.",
 steps(("Read", p("8."))) + final("8"))

# ---------------- Set 4: Tokens on a number line (Q16–20) ----------------
P.dilr_set(4, "Set 4 — Tokens on a number line", DIR,
 p("Ajay and Vijay play a game on a number line marked at every integer. Both tokens start at 0.") +
 p("<b>Round 1.</b> The computer generates a random natural number from 1 to 10 for each player (the two may be equal), and each moves his token to that number.") +
 p("<b>Round 2 onwards.</b> Each player again gets a number from 1 to 10, never equal to his own number in the previous round. If this round’s number a is larger than the previous round’s b, he moves a units right; if smaller, a units left. The game can go on for any number of rounds."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("Moves", p("A rising number moves right by the new number; a falling one moves left by it.")),
       ("Extremes", p("To go far right, keep numbers rising; to go far left, keep them falling. Repeated numbers are allowed only with a different number in between."))) +
 final("Track position as a running sum with signs."),
 p("Build extremes by choosing sequences that keep rising (right) or falling (left)."),
 p("<b>Rule-based movement:</b> write the position as a sum of signed terms; the sign depends only on whether the sequence rises or falls."))
P.dq(16, "Both players got the same number in round 1. What is the largest possible distance between the tokens after round 6?", [], "TITA", "68", "Hard",
 "One goes as far right as possible, the other as far left.",
 steps(("Best start", p("Checking every round-1 number, a shared 10 gives the widest spread.")),
       ("Two paths", p("Right: 10, 1, 7, 8, 9, 10 gives 10 − 1 + 7 + 8 + 9 + 10 = 43. Left: 10, 9, 8, 7, 6, 5 gives 10 − 9 − 8 − 7 − 6 − 5 = −25.")),
       ("Distance", p("43 − (−25) = 68."))) + final("68"))
P.dq(17, "Ajay got 1 in round 1 and is at 0 after round 4. If all numbers in rounds 1–4 are single-digit, in how many ways can he get from 1 to 0 in rounds 2–4?", [], "TITA", "12", "Hard",
 "Round 2 rises to x + 1; then two falls a > b with a + b = x + 1.",
 steps(("Round 2", p("Any x from 2 to 9 moves him to x + 1.")),
       ("Rounds 3–4", p("He must fall twice: x > a > b with a + b = x + 1.")),
       ("Count", p("x = 4: 1; 5: 1; 6: 2; 7: 2; 8: 3; 9: 3. Total 12."))) + final("12"))
P.dq(18, "In the first 10 rounds, each player’s numbers are all different. What is the largest possible distance between the tokens after round 10?", ["95", "90", "110", "100"], "MCQ", "2", "Hard",
 "Numbers 1 to 10 once each.",
 steps(("Right", p("Ascending: 1 + 2 + … + 10 = 55.")),
       ("Left", p("Descending: 10 − 9 − 8 − … − 1 = −35.")),
       ("Distance", p("90."))) + final("Option 2"),
 [("1", "Slip."), ("3", "Slip."), ("4", "Slip.")])
P.dq(19, "Vijay’s numbers in the first 10 rounds are all different and 10 came in round 5. What is the farthest right he can be after round 10?", ["45", "49", "55", "53"], "MCQ", "4", "Hard",
 "After 10 there must be a fall.",
 steps(("Best", p("Rising to 10, then 1 (a fall of only 1), then rising again: e.g. 6, 7, 8, 9, 10, 1, 2, 3, 4, 5.")),
       ("Position", p("6 + 7 + 8 + 9 + 10 − 1 + 2 + 3 + 4 + 5 = 53."))) + final("Option 4"),
 [("1", "Not the best."), ("2", "Not the best."), ("3", "Needs no fall.")])
P.dq(20, "In the situation of the previous question, in how many ways can Vijay reach that farthest point?", ["1", "2", "12", "70"], "MCQ", "4", "Hard",
 "Choose which four numbers come before 10.",
 steps(("Count", p("Pick 4 of the 8 numbers 2–9 for rounds 1–4 (ascending); the rest follow 1 in ascending order: ⁸C₄ = 70."))) + final("Option 4"),
 [("1", "Order is forced, but the choice is not."), ("2", "Too few."), ("3", "Too few.")])
