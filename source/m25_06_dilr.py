# -*- coding: utf-8 -*-
# Simp Mock 6 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_06 import P
import m25_06_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Field datasets (Q1–4) ----------------
SC = table(["Researcher", "R", "S", "W", "M"], [["Amira", "7", "5", "4", "2"], ["Bhavya", "6", "?", "3", "1"], ["Chetan", "?", "6", "?", "2"], ["Divya", "5", "4", "6", "?"], ["Eshan", "4", "5", "2", "1"]])
HN = table(["Researcher", "R", "S", "W", "M"], [["Amira", "10", "6", "5", "?"], ["Bhavya", "7", "6", "4", "1"], ["Chetan", "8", "7", "3", "2"], ["Divya", "6", "?", "5", "1"], ["Eshan", "?", "4", "3", "1"]])
TOT = ("<ul><li>Rainforest 63 (53 known): Chetan SC + Eshan HN = 10</li><li>Savanna 45 (43 known): Bhavya SC + Divya HN = 2</li>"
       "<li>Wetlands 45 (35 known): Chetan SC = 10</li><li>Mountains 27 (11 known): Amira HN + Divya SC = 16</li></ul>")
P.dilr_set(1, "Set 1 — Field datasets", DIR,
 p("A research institute conducted fieldwork across four ecological regions: Rainforest (R), Savanna (S), Wetlands (W) and Mountains (M). Five researchers, Amira, Bhavya, Chetan, Divya and Eshan, collected two types of dataset: Species Count (SC) and Habitat Notes (HN). The percentage distribution of the total number of datasets collected from the four regions was: Rainforest 35%, Savanna 25%, Wetlands 25%, Mountains 15%.") +
 p("Each researcher contributed datasets in both SC and HN formats from each of the four regions, though the numbers vary by researcher and region. It is known that:") +
 "<ul><li>No researcher contributed fewer than 15% of the total number of datasets.</li><li>Each researcher submitted at least one dataset in each format for each region.</li></ul>" +
 p("The tables below give the number of datasets each researcher submitted in each format and region; ‘?’ marks a missing entry.") +
 p("<b>Species Count (SC)</b>") + SC + p("<b>Habitat Notes (HN)</b>") + HN +
 p("Only complete datasets are accepted, so every entry is a natural number. The total number of datasets submitted by the five researchers together was the minimum possible."),
 "DILR::DI::Data_Tabulation",
 steps(("Total is a multiple of 20", p("15% and 35% of the total must be whole numbers, so the total T is a multiple of 20.")),
       ("Smallest T", p("Savanna already has 43 known datasets plus two missing (at least 1 each): 45 ≤ 0.25T, so T ≥ 180. T = 180 gives R 63, S 45, W 45, M 27.")),
       ("Missing entries", TOT),
       ("15% rule", p("Each researcher needs at least 27. Eshan has 20 known, so his Rainforest HN is at least 7; with Chetan’s Rainforest SC at least 1, Eshan’s is 7, 8 or 9. Bhavya’s Savanna SC and Divya’s Savanna HN are both 1. Amira HN (M) + Divya SC (M) = 16 with each at least 1: 15 ways, and every split keeps everyone at 27 or more."))) +
 final("T = 180; Chetan’s Wetlands SC = 10; 3 × 15 = 45 possible tables."),
 p("Use the shares to force T to a multiple of 20, then let the tightest region set the minimum."),
 p("<b>Percent shares of a whole:</b> each share must be a whole number, which fixes what the total can be."))
P.dq(1, "What is the total number of datasets submitted by all five researchers together?", [], "TITA", "180", "Medium",
 "T is a multiple of 20; Savanna needs at least 45.", steps(("T", p("160 gives Savanna only 40 < 45. 180 works."))) + final("180"))
P.dq(2, "When the missing entries are filled with valid values, we get a complete table. How many such distinct valid tables can be formed?", [], "TITA", "45", "Hard",
 "Two free choices: Eshan’s Rainforest HN, and the Mountains split.",
 steps(("Count", p("Eshan R-HN: 7, 8 or 9 (3 ways). Amira M-HN + Divya M-SC = 16: 15 ways. Total 3 × 15 = 45."))) + final("45"))
P.dq(3, "The number of datasets submitted by Chetan for the Wetlands region in the SC format is _____.", ["10", "8", "12", "Cannot be determined"], "MCQ", "1", "Easy",
 "Wetlands total is 45.", steps(("Wetlands", p("45 − 35 = 10."))) + final("10, option 1"),
 [("2", "Wrong total."), ("3", "Wrong total."), ("4", "It’s the only missing Wetlands cell.")])
P.dq(4, "The maximum possible difference between the total number of datasets submitted by Amira and by Divya is ______.", ["15", "20", "25", "Cannot be determined"], "MCQ", "3", "Medium",
 "Amira = 39 + her Mountains HN; Divya = 28 + her Mountains SC.",
 steps(("Difference", p(r"With \(a + d = 16\): \((39 + a) - (28 + d) = 27 - 2d\). Largest at \(d = 1\): 25."))) + final("25, option 3"),
 [("1", "Not the maximum."), ("2", "Not the maximum."), ("4", "The range is bounded.")])

# ---------------- Set 2: Car sales mix (Q5–8) ----------------
P.dilr_set(2, "Set 2 — Car sales mix", DIR,
 p("A leading car company sells four varieties of car: sedans, SUVs, hatchbacks and electric vehicles (EVs). The bar graph shows each variety’s sales as a percentage of the company’s total car sales in each of four quarters (Q1–Q4).") + F.SALES,
 "DILR::DI::Graphs_and_Charts",
 steps(("Reading", p("Each bar is one quarter’s 100%. Shares can’t be compared across quarters without knowing the quarters’ totals; each question supplies a link."))) +
 final("Turn each condition into the quarter totals, then compare."),
 p("Percent bars give shares of different totals: fix the totals first."),
 p("<b>100% stacked bars:</b> a larger share doesn’t mean a larger number unless the totals match."))
P.dq(5, "If the number of SUVs sold in Q2, hatchbacks sold in Q4, sedans sold in Q3 and EVs sold in Q1 are the same, then the total sales in Q1, as a percentage of total sales across all quarters, is closest to _________ .", ["46.54%", "48.39%", "54.62%", "56.34%"], "MCQ", "2", "Medium",
 "Call the common number x; each quarter total is x divided by its share.",
 steps(("Totals", p(r"Q1: \(x / 0.10 = 10x\). Q2: \(x / 0.25 = 4x\). Q3: \(x / 0.30 = \tfrac{10x}3\). Q4: \(x / 0.30 = \tfrac{10x}3\).")),
       ("Share", p(r"\(10 \div \left(10 + 4 + \tfrac{20}3\right) = \tfrac{30}{62} \approx 48.39\%\)."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Too high."), ("4", "Too high.")])
P.dq(6, "Assuming total sales in Q1 are 100,000 units, and sales in each subsequent quarter increase by 10% over the previous quarter, what are the total annual sales of sedans?", ["1,36,555", "1,24,775", "1,53,855", "1,48,575"], "MCQ", "4", "Easy",
 "Totals: 100000, 110000, 121000, 133100.",
 steps(("Sedans", p("35,000 + 44,000 + 36,300 + 33,275 = 1,48,575."))) + final("Option 4"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])
P.dq(7, "If EV sales in Q1, Q2, Q3 and Q4 are in the ratio 1 : 2 : 3 : 4, in which quarter was the second-highest number of sedans sold? (Enter the quarter number.)", [], "TITA", "3", "Medium",
 "Quarter total = EV units ÷ EV share.",
 steps(("Totals", p(r"Q1: \(1/0.10 = 10\). Q2: \(2/0.15 = 13.3\). Q3: \(3/0.15 = 20\). Q4: \(4/0.15 = 26.7\).")),
       ("Sedans", p("Q1 3.5, Q2 5.33, Q3 6, Q4 6.67. Second highest: Q3."))) + final("3"))
P.dq(8, "If the number of hatchbacks sold is the same in each quarter, in which quarter were SUV sales the lowest?", ["Q1", "Q2", "Q3", "Q4"], "MCQ", "4", "Easy",
 "SUVs = hatchbacks × (SUV share ÷ hatchback share).",
 steps(("Ratio", p("Q1 30/25 = 1.2; Q2 25/20 = 1.25; Q3 35/20 = 1.75; Q4 30/30 = 1. Lowest: Q4."))) + final("Q4, option 4"),
 [("1", "1.2."), ("2", "1.25."), ("3", "1.75, the highest.")])

# ---------------- Set 3: Judges and contestants (Q9–13) ----------------
JT = table(["", "J1", "J2", "J3"], [['C1', '1', '', '6'], ['C2', '', '', ''], ['C3', '3', '', ''], ['C4', '', '2', '1'], ['C5', '', '', ''], ['C6', '5', '', '']]) + table(["", "J4", "J5", "J6"], [['C1', '', '2', ''], ['C2', '6', '', ''], ['C3', '', '', '1'], ['C4', '', '6', ''], ['C5', '4', '', ''], ['C6', '', '3', '6']])
SOLS = table(["", "J1", "J2", "J3"], [['C1', '1', '3/5', '6'], ['C2', '2', '·', '·'], ['C3', '3', '6', '4/5'], ['C4', '4', '2', '1'], ['C5', '6', '·', '3/5'], ['C6', '5', '4', '2']]) + table(["", "J4", "J5", "J6"], [['C1', '3/5', '2', '4'], ['C2', '6', '·', '3/5'], ['C3', '2', '4/5', '1'], ['C4', '3/5', '6', '3/5'], ['C5', '4', '1/5', '2'], ['C6', '1', '3', '6']])
P.dilr_set(3, "Set 3 — Six judges, six chefs", DIR,
 p("Twenty contestants took part in a cooking competition with six judges. Each judge gave each contestant points from 1 to 6, and a contestant’s final score is the sum of the six judges’ points. The final scores of the top 6 contestants were the same. No two judges gave equal points to any of the top 6 contestants, and no two of the top 6 contestants got equal points from any judge.") +
 p("The table gives partial information about the points the 6 judges (J1–J6) gave the top 6 contestants (C1–C6).") + JT,
 "DILR::LR::Puzzles",
 steps(("A Latin square", p("Each contestant gets 1–6 once each (no two judges equal), and each judge gives 1–6 once each to the top six. So the table is a 6 × 6 Latin square; equal scores of 21 follow automatically.")),
       ("J1’s column", p("J1 has given 1, 3 and 5, so C2, C4 and C5 get 2, 4 and 6. C4 already has 2 (J2) and 6 (J5), so C4 gets 4; C2 already has 6 (J4), so C2 gets 2 and C5 gets 6. Working the same way through the rows and columns fixes C6 completely (5, 4, 2, 1, 3, 6) and gives C5 2 from J6.")),
       ("What’s left", p("Exactly five complete squares remain. The cells they agree on, and the choices for the rest:")),
       ("Common cells", SOLS + p("‘3/5’ = one of the two; ‘·’ = three possible values.")),
       ("The five squares", p("C1 J2/J4: (3, 5) in three squares, (5, 3) in two. C2 J5 can be 5, 4 or 1; never 3."))) +
 final("Five valid squares; each question fixes or counts among them."),
 p("Recognise the Latin square, then fill the column or row with the fewest gaps first."),
 p("<b>Latin squares:</b> every row and column holds each symbol once; count completions by branching on the least-free cell."))
P.dq(9, "How many points did J6 give to C5?", [], "TITA", "2", "Medium",
 "J6 has 1 (C3) and 6 (C6). Look at C5’s other judges.",
 steps(("Forced", p("In every valid square, J6 gives C5 2 points."))) + final("2"))
P.dq(10, "If J6 gave 5 points to C2, what best can be said about the points J5 gave C2?", ["J5 gave 3 points to C2.", "J5 gave 1, 3 or 4 points to C2.", "J5 gave 4 points to C2.", "J5 gave either 1 or 4 points to C2."], "MCQ", "4", "Hard",
 "Keep only the squares where J6 → C2 is 5.",
 steps(("Two squares", p("Two of the five squares have J6 giving C2 5. In them, J5 gives C2 4 in one and 1 in the other."))) + final("Option 4"),
 [("1", "3 never occurs for J5 → C2."), ("2", "3 is impossible."), ("3", "1 is also possible.")])
P.dq(11, "If J4 gave 3 points to C1, in how many ways can the points of the six contestants be determined?", ["2", "3", "4", "5"], "MCQ", "1", "Hard",
 "Count squares with C1’s J4 = 3.",
 steps(("Count", p("Two of the five squares have J4 → C1 = 3 (and J2 → C1 = 5)."))) + final("2, option 1"),
 [("2", "That’s the count for J4 → C1 = 5."), ("3", "Too many."), ("4", "All five squares.")])
P.dq(12, "Which of the following is definitely incorrect?", ["J5 gave 3 points to C2.", "J4 gave either 3 or 5 points to C1.", "J3 gave 4 points to C3.", "None of these"], "MCQ", "1", "Medium",
 "C6 already got 3 from J5.",
 steps(("Check", p("J5 gave C6 3, so J5 can’t give C2 3: definitely wrong. J4 → C1 is 3 or 5 in every square; J3 → C3 is 4 in two squares."))) + final("Option 1"),
 [("2", "Always true."), ("3", "Possible."), ("4", "Option 1 is definitely wrong.")])
P.dq(13, "If J6 gave 3 points to C2, in how many ways can the points of the six contestants be determined?", [], "TITA", "3", "Hard",
 "Count squares with J6 → C2 = 3.",
 steps(("Count", p("Three of the five squares have J6 giving C2 3."))) + final("3"))

# ---------------- Set 4: Club election (Q14–18) ----------------
P.dilr_set(4, "Set 4 — A three-round election", DIR,
 p("A club has 450 members, including its president. The new president is chosen by election, in which all members (including the candidates) vote. There are three rounds. Exactly seven candidates take part in round 1; the two with the fewest votes are eliminated and the other five contest round 2. Again the two with the fewest votes are eliminated, and the remaining three contest round 3. The candidate with the most votes in the final round becomes president.") +
 p("An eligible member can cast only one vote in a round. Only the retiring president abstains from voting, unless there is a tie after the final round.") +
 p("In each round, the candidate with the most votes is ranked 1, the next is ranked 2, and so on. The results:") +
 "<ul><li><b>Round 1</b>: The sixth ranker received 25% more votes than the seventh ranker, and the fifth ranker received 14% more votes than the sixth ranker. Starting from the fourth ranker, each candidate received at least 10% more votes than the candidate ranked just below. Each of the first, second and third rankers received a prime number of votes.</li>"
 "<li><b>Round 2</b>: The fourth ranker received 26% more votes than the fifth ranker, and the third ranker received \\(33\\tfrac13\\%\\) more votes than the fourth ranker. There was a tie between the two candidates with the most votes.</li>"
 "<li><b>Round 3</b>: The three candidates received different numbers of votes. The first ranker, who received 7 more votes than the second ranker, received 40% more votes than the third ranker.</li></ul>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("Votes per round", p("449 members vote in every round (the retiring president abstains).")),
       ("Round 1", p(r"Sixth = \(\tfrac54\) × seventh, fifth = 1.14 × sixth \(= \tfrac{57}{50}\) × sixth, so sixth is a multiple of 50 and seventh a multiple of 40. Seventh 40: sixth 50, fifth 57, leaving 302. Fourth ≥ 62.7 → 63; third ≥ 69.3 and prime → 71; second ≥ 78.1 → 79; first ≥ 86.9 → 89. 63 + 71 + 79 + 89 = 302 exactly. (Seventh 80 leaves far too little.)")),
       ("Round 2", p(r"Fifth a multiple of 50 (fourth = 1.26 × fifth). Fifth 50: fourth 63, third 84; the top two share \(449 - 197 = 252\): 126 each. Fifth 100 leaves only 55 for the top two.")),
       ("Round 3", p(r"First \(= 1.4t\), second \(= 1.4t - 7\), third \(= t\): \(3.8t - 7 = 449\), \(t = 120\). Votes 168, 161, 120.")),
       ("Results", table(["Round", "Votes by rank"], [["1", "89, 79, 71, 63, 57, 50, 40"], ["2", "126, 126, 84, 63, 50"], ["3", "168, 161, 120"]]))) +
 final("Every round’s votes are fixed."),
 p("Percentage increases like 25% and 14% force multiples; the smallest multiple usually fits the total exactly."),
 p("<b>Integer percentages:</b> a 14% rise needs a base that is a multiple of 50."))
P.dq(14, "In which round of voting is the difference between the maximum and minimum number of votes received by the candidates the smallest?", ["Round 1", "Round 2", "Round 3", "Both round 1 and round 3"], "MCQ", "3", "Easy",
 "Range in each round.", steps(("Ranges", p("Round 1: 89 − 40 = 49. Round 2: 126 − 50 = 76. Round 3: 168 − 120 = 48."))) + final("Round 3, option 3"),
 [("1", "49 > 48."), ("2", "76."), ("4", "They differ by one.")])
P.dq(15, "The average number of votes received in the first round by the three candidates with the most votes is _________ .", [r"\(77\tfrac23\)", r"\(78\tfrac23\)", r"\(79\tfrac23\)", "80"], "MCQ", "3", "Easy",
 "89, 79, 71.", steps(("Average", p(r"\(239 \div 3 = 79\tfrac23\)."))) + final("Option 3"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Rounded.")])
P.dq(16, "The median number of votes received by the seven candidates in round 1 falls in the range __________ .", ["62.5 – 63.5", "63.5 – 64.5", "64.5 – 65.5", "65.5 – 66.5"], "MCQ", "1", "Easy",
 "The fourth of seven.", steps(("Median", p("The fourth ranker: 63."))) + final("Option 1"),
 [("2", "Too high."), ("3", "Too high."), ("4", "Too high.")])
P.dq(17, "The difference between the mean and the median number of votes received by the candidates in round 2 is _______ .", ["5.4", "5.8", "6.2", "6.4"], "MCQ", "2", "Easy",
 "Mean 449/5.", steps(("Compare", p("Mean 89.8, median 84: difference 5.8."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(18, "Suppose some members who voted for the first ranker of round 3 change their minds and vote for the third ranker instead, making him the new first ranker. What is the maximum number of votes the new third ranker would then be left with?", [], "TITA", "126", "Medium",
 "Move x votes from 168 to 120. The old first must drop to third.",
 steps(("Conditions", p(r"New first: \(120 + x > 161\), so \(x \ge 42\). Then the old first has \(168 - x \le 126\), below 161, so he is third.")),
       ("Maximum", p(r"\(x = 42\): votes 162, 161, 126."))) + final("126"))

# ---------------- Set 5: Parking slots (Q19–22) ----------------
LOT = table(["Row", "Column I", "Column II"], [["1", "1: R", "9: B"], ["2", "2: B", "10: R"], ["3", "3: R", "11: R"], ["4", "4: Y", "12: Y"], ["5", "5: R", "13: Y"], ["6", "6: B / Y", "14: B"], ["7", "7: R", "15: B"], ["8", "8: Y / B", "16: Y"]], hi={(5, 1), (7, 1)})
P.dilr_set(5, "Set 5 — Coloured cars in a parking lot", DIR,
 p("A company owns 16 cars parked in a lot with 16 slots, arranged in 2 columns and 8 rows. The slots in column I are numbered 1 to 8 and those in column II are numbered 9 to 16 (slot 1 is beside slot 9, slot 2 beside slot 10, and so on). Each car is red, blue or yellow.") +
 "<ul><li>Column I has 4 red cars; column II does not.</li><li>In column I there are equally many blue and yellow cars; the same is true of column II.</li><li>In column II, exactly 2 red cars occupy adjacent slots, and the same is true of yellow cars and of blue cars.</li><li>No red car is in slots 13 to 16 or in slot 8.</li><li>The largest difference between the slot numbers of red cars is 10; for blue cars it is 13; for yellow cars it is 12.</li><li>Slot 10 has a red car and slot 14 a blue car.</li><li>No two red cars in column I are in adjacent slots.</li></ul>",
 "DILR::LR::Puzzles",
 steps(("Column I reds", p("Four reds in slots 1–7 with no two adjacent: 1, 3, 5, 7. Then blue and yellow share 2, 4, 6, 8, two each.")),
       ("Reds in column II", p("The lowest red is slot 1 and the spread is 10, so the highest red is 11. Slot 10 is red, slots 13–16 can’t be, and 12 would make the spread 11. Exactly two reds are adjacent, so the column II reds are 10 and 11 only (9 would make three in a row). Column II then has 3 blue and 3 yellow.")),
       ("Blue and yellow spreads", p("Some blue is in column I and slot 1 is red, so blue runs from 2 to 15 (3 to 16 would need slot 3, which is red). Yellow spans 12: 4 to 16. So 2 blue, 4 yellow, 15 blue, 16 yellow.")),
       ("Rest of column II", p("Blues 14, 15 and one of 9, 12, 13. Blue may have only one adjacent pair, so not 13. If blue were 12, the yellows 9, 13, 16 would have no adjacent pair. So 9 is blue and 12, 13 are yellow.")),
       ("Column I", p("2 blue, 4 yellow; slots 6 and 8 hold one blue and one yellow, either way.")),
       ("Two arrangements", LOT)) +
 final("Only slots 6 and 8 are uncertain (one blue, one yellow)."),
 p("Start with the non-adjacent reds in column I; the spreads then fix the end points of each colour."),
 p("<b>Spread clues:</b> a maximum difference fixes the lowest and highest positions of that colour."))
P.dq(19, "Which of the following sets of three slots definitely have cars of three different colours?", ["2, 6, 11", "5, 8, 15", "7, 12, 16", "6, 8, 11"], "MCQ", "4", "Medium",
 "Slots 6 and 8 always differ.",
 steps(("Check", p("6 and 8 are one blue and one yellow, and 11 is red: always three colours."))) + final("Option 4"),
 [("1", "2 is blue; 6 may be blue."), ("2", "5 red, 15 blue, 8 may be blue."), ("3", "12 and 16 are both yellow.")])
P.dq(20, "Which of the following pairs of adjacent slots has cars of the same colour?", ["9 and 10", "11 and 12", "13 and 14", "14 and 15"], "MCQ", "4", "Easy",
 "Column II: B R R Y Y B B Y.", steps(("Pairs", p("14 and 15 are both blue."))) + final("Option 4"),
 [("1", "Blue and red."), ("2", "Red and yellow."), ("3", "Yellow and blue.")])
P.dq(21, "What is the colour of the car in slot 16?", ["Red", "Blue", "Yellow", "Blue or yellow"], "MCQ", "3", "Easy",
 "Yellow spans 4 to 16.", steps(("Slot 16", p("Yellow."))) + final("Option 3"),
 [("1", "No reds in 13–16."), ("2", "Blue ends at 15."), ("4", "It’s fixed.")])
P.dq(22, "The cars are to be rearranged so that all blue cars occupy adjacent slots starting from slot 1, all yellow cars occupy adjacent slots ending with slot 16, and the remaining slots are occupied by red cars. What is the minimum number of cars that must be moved?", ["8", "9", "10", "7"], "MCQ", "2", "Hard",
 "5 blue (slots 1–5), 6 red (6–11), 5 yellow (12–16). Count cars already in place.",
 steps(("Target", p("Blue 1–5, red 6–11, yellow 12–16.")),
       ("Already in place", p("Slot 2 (blue), 7, 10, 11 (red), 12, 13, 16 (yellow): 7 cars, in either arrangement.")),
       ("Moves", p("16 − 7 = 9."))) + final("9, option 2"),
 [("1", "Counts one car too few."), ("3", "Counts one too many."), ("4", "Too few.")])
