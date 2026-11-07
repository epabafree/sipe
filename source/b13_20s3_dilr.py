# -*- coding: utf-8 -*-
# Batch 13 — CAT 2020 Slot 3: DILR sets 1–5 (Q1–24, exam order).
from fmt import steps, final, trap, why, table, p
from b13_20s3 import P

# ---------------- Set 1: Blood tests ----------------
VIALS = table(["Patient", "Vials", "Patient", "Vials"],
              [["1", "B, D, F, H", "9", "A, D, F, H"], ["2", "B, D, F, G", "10", "A, D, F, G"], ["3", "B, D, E, H", "11", "A, D, E, H"], ["4", "B, D, E, G", "12", "A, D, E, G"],
               ["5", "B, C, F, H", "13", "A, C, F, H"], ["6", "B, C, F, G", "14", "A, C, F, G"], ["7", "B, C, E, H", "15", "A, C, E, H"], ["8", "B, C, E, G", "16", "A, C, E, G"]])
P.dilr_set(1, "Set 1 — Sixteen patients, eight vials", "Read the following passage carefully and answer the questions that follow.",
 p("Sixteen patients in a hospital must undergo a blood test for a disease. It is known that exactly one of them has the disease. The hospital has only eight testing kits and has decided to pool blood samples of patients into eight vials for the tests. The patients are numbered 1 through 16, and the vials are labelled A, B, C, D, E, F, G, and H. The following table shows the vials into which each patient’s blood sample is distributed.") + VIALS +
 p("If a patient has the disease, then each vial containing his/her blood sample will test positive. If a vial tests positive, one of the patients whose blood samples were mixed in the vial has the disease. If a vial tests negative, then none of the patients whose blood samples were mixed in the vial has the disease."),
 "DILR::LR::Puzzles",
 steps(("Four pairs", p("Every patient is in exactly one vial of each pair: A or B, C or D, E or F, G or H.")),
       ("What each pair tells you", p("A means 9–16, B means 1–8. C means 5–8 or 13–16. E means 3, 4, 7, 8, 11, 12, 15 or 16. G means an even number.")),
       ("So", p("Exactly one vial of each pair tests positive, and the four positives name the patient. It works like a four-digit binary code."))) +
 final("One positive per pair; four results identify the patient."),
 p("Spot the pairs first. Each question is then a quick lookup."),
 p("<b>Pooling puzzles:</b> look for complementary groups. Each yes/no test halves the candidates, so 4 tests are enough for 16 people."))
P.dq(1, "Suppose vial C tests positive and vials A, E and H test negative. Which patient has the disease?", ["Patient 8", "Patient 2", "Patient 6", "Patient 14"], "MCQ", "3", "Easy",
 "Negative A, E, H mean positive B, F, G.",
 steps(("Narrowing down", p("B: 1–8. C: 5–8. F: 5 or 6. G: even. Patient 6."))) + final("Patient 6, option 3"),
 [("1", "8 is in E, which is negative."), ("2", "2 isn’t in C."), ("4", "14 is in A, which is negative.")])
P.dq(2, "Suppose vial A tests positive and vials D and G test negative. Which of the following vials should we test next to identify the patient with the disease?", ["Vial E", "Vial H", "Vial C", "Vial B"], "MCQ", "1", "Easy",
 "Which pair hasn’t been tested?",
 steps(("What we know", p("A, C and H are positive: patient 13 or 15. They differ only in E/F, so test E."))) + final("Vial E, option 1"),
 [("2", "Already known positive."), ("3", "Already known positive."), ("4", "Already known negative.")])
P.dq(3, "Which of the following combinations of test results is NOT possible?", ["Vials B and D positive, vials F and H negative", "Vials A and E positive, vials C and D negative", "Vials A and G positive, vials D and E negative", "Vial B positive, vials C, F and H negative"], "MCQ", "2", "Easy",
 "One vial from each pair is always positive.",
 steps(("Checking", p("C and D can’t both be negative, since every patient is in one of them."))) + final("Option 2"),
 [("1", "Patient 4."), ("3", "Patient 14."), ("4", "Patient 4.")])
P.dq(4, "Suppose one of the lab assistants accidentally mixed two patients’ blood samples before they were distributed to the vials. Which of the following correctly represents the set of all possible numbers of positive test results out of the eight vials?", ["{5, 6, 7, 8}", "{4, 5, 6, 7}", "{4, 5}", "{4, 5, 6, 7, 8}"], "MCQ", "4", "Hard",
 "The mixture goes into both patients’ vials. Does it include the sick patient?",
 steps(("Sick patient not involved", p("Only that patient’s four vials are positive: 4.")),
       ("Sick patient involved", p("The mixture reaches the vials of both patients. They share 0 to 3 of the four pairs, so 5, 6, 7 or 8 vials test positive."))) +
 final("{4, 5, 6, 7, 8}, option 4"),
 [("1", "Leaves out the case where the sick patient isn’t mixed."), ("2", "Two patients can differ in all four pairs."), ("3", "Too few cases.")])

# ---------------- Set 2: Grocery deliveries ----------------
ORDERS = table(["Day", "Cumulative orders booked", "Orders delivered on day", "Cumulative orders lost"],
               [["13th", "219", "11", "91"], ["14th", "249", "27", "92"], ["15th", "277", "23", "94"], ["16th", "302", "11", "106"],
                ["17th", "327", "21", "118"], ["18th", "332", "13", "120"], ["19th", "337", "14", "129"]])
P.dilr_set(2, "Set 2 — Two-day delivery", "Read the following passage carefully and answer the questions that follow.",
 p("XYZ organization got into the business of delivering groceries to home at the beginning of the last month. They have a two-day delivery promise. However, their deliveries are unreliable. An order booked on a particular day may be delivered the next day or the day after. If the order is not delivered at the end of two days, then the order is declared as lost at the end of the second day. XYZ then does not deliver the order, but informs the customer, marks the order as lost, returns the payment and pays a penalty for non-delivery.") +
 p("The following table provides details about the operations of XYZ for a week of the last month. The first column gives the date, the second gives the cumulative number of orders that were booked up to and including that day. The third column represents the number of orders delivered on that day. The last column gives the cumulative number of orders that were lost up to and including that day.") + ORDERS +
 p("It is known that the numbers of orders that were booked on the 11th, 12th, and 13th of the last month that took two days to deliver were 4, 6, and 8 respectively."),
 "DILR::DI::Data_Tabulation",
 steps(("The bookkeeping", p("An order booked on day d is delivered on d + 1 (call these x), on d + 2 (call these y), or lost at the end of d + 2. Deliveries on a day = x from the day before + y from two days before.")),
       ("Working forwards", p("Day 13: 11 = x₁₂ + 4, so x₁₂ = 7. Day 14: 27 = x₁₃ + 6, so x₁₃ = 21. Day 15: 23 = x₁₄ + 8, so x₁₄ = 15. Each day’s bookings, minus x and the orders lost two days later, give y.") +
       table(["Booked on", "Orders", "Next day (x)", "Day after (y)", "Lost"],
             [["13th", "31", "21", "8", "2"], ["14th", "30", "15", "3", "12"], ["15th", "28", "8", "8", "12"], ["16th", "25", "13", "10", "2"], ["17th", "25", "3", "13", "9"]]))) +
 final("The 13th booking count comes from 21 + 8 + 2 (lost on the 15th)."),
 p("Set up x and y for each booking day, and walk forward one day at a time."),
 p("<b>Cumulative tables:</b> take differences first. Then link each day’s output to the earlier days that feed it."))
P.dq(5, "Among the following days, the largest fraction of orders booked on which day was lost?", ["14th", "13th", "15th", "16th"], "MCQ", "3", "Medium",
 "Compare lost ÷ booked for each day.",
 steps(("Fractions", p("13th: 2/31. 14th: 12/30 = 0.40. 15th: 12/28 ≈ 0.43. 16th: 2/25."))) + final("15th, option 3"),
 [("1", "0.40, slightly less."), ("2", "Very few lost."), ("4", "Very few lost.")])
P.dq(6, "On which of the following days was the number of orders booked the highest?", ["14th", "13th", "12th", "15th"], "MCQ", "2", "Medium",
 "The 12th and 13th need working out.",
 steps(("Bookings", p("12th: 7 + 6 + 1 = 14. 13th: 31. 14th: 30. 15th: 28."))) + final("13th, option 2"),
 [("1", "30, one fewer."), ("3", "Only 14."), ("4", "28.")])
P.dq(7, "The delivery ratio for a given day is defined as the ratio of the number of orders booked on that day which are delivered on the next day to the number of orders booked on that day which are delivered on the second day after booking. On which of the following days, was the delivery ratio the highest?", ["16th", "15th", "13th", "14th"], "MCQ", "4", "Medium",
 "x ÷ y for each day.",
 steps(("Ratios", p("13th: 21/8 ≈ 2.6. 14th: 15/3 = 5. 15th: 8/8 = 1. 16th: 13/10 = 1.3."))) + final("14th, option 4"),
 [("1", "1.3."), ("2", "1."), ("3", "About 2.6.")])
P.dq(8, "The average time taken to deliver orders booked on a particular day is computed as follows. Let the number of orders delivered the next day be x and the number of orders delivered the day after be y. Then the average time to deliver order is (x + 2y)/(x + y). On which of the following days was the average time taken to deliver orders booked the least?", ["13th", "14th", "16th", "15th"], "MCQ", "2", "Medium",
 "The bigger x is compared with y, the smaller the average.",
 steps(("Averages", p("13th: 37/29 ≈ 1.28. 14th: 21/18 ≈ 1.17. 15th: 24/16 = 1.5. 16th: 33/23 ≈ 1.43."))) + final("14th, option 2"),
 [("1", "About 1.28."), ("3", "About 1.43."), ("4", "1.5.")])

# ---------------- Set 3: The farmer’s land ----------------
FIELD = table(["", "1", "2", "3", "4"],
              [["X", "12 · C", "", "", ""], ["Y", "21 · A", "", "", "A"], ["Z", "B", "C", "9", "28"]])
P.dilr_set(3, "Set 3 — A farmer’s twelve plots", "Read the following passage carefully and answer the questions that follow.",
 p("A farmer had a rectangular land containing 205 trees. He distributed that land among his four daughters — Abha, Bina, Chitra and Dipti by dividing the land into twelve plots along three rows (X, Y, Z) and four Columns (1, 2, 3, 4) as shown in the figure below:") + FIELD +
 p("The plots in rows X, Y, Z contained mango, teak and pine trees respectively. Each plot had trees in non-zero multiples of 3 or 4 and none of the plots had the same number of trees. Each daughter got an even number of plots. In the figure, the number mentioned in top left corner of a plot is the number of trees in that plot, while the letter in the bottom right corner is the first letter of the name of the daughter who got that plot (For example, Abha got the plot in row Y and column 1 containing 21 trees). Some information in the figure got erased, but the following is known:") +
 p("<i>In the figure above, each cell shows the number of trees, then the daughter’s initial, where known.</i>") +
 "<ol><li>Abha got 20 trees more than Chitra but 6 trees less than Dipti.</li><li>The largest number of trees in a plot was 32, but it was not with Abha.</li><li>The number of teak trees in Column 3 was double of that in Column 2 but was half of that in Column 4.</li><li>Both Abha and Bina got a higher number of plots than Dipti.</li><li>Only Bina, Chitra and Dipti got corner plots.</li><li>Dipti got two adjoining plots in the same row.</li><li>Bina was the only one who got a plot in each row and each column.</li><li>Chitra and Dipti did not get plots which were adjacent to each other (neither in row, column, nor diagonal).</li><li>The number of mango trees was double the number of teak trees.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Plot counts", p("Dipti has at least 2, and Abha and Bina more: 4, 4, 2, 2 for Abha, Bina, Chitra, Dipti. So Chitra has only X1 and Z2.")),
       ("Who gets what", p("Dipti’s pair includes a corner and can’t touch Chitra’s Z2: so X3 and X4. Bina takes Z4, and to cover every row and column, X2 and Y3. Abha gets Y2 and Z3.")),
       ("The numbers", p("Teak: Y2 = t, Y3 = 2t, Y4 = 4t. Mango = 2 × teak, so pine = 142 − 21t and Z1 + Z2 = 105 − 21t. Abha = 30 + 5t = Chitra + 20 = 32 + Z2. Only t = 4 works: Z2 = 18, Z1 = 3, X2 = 30, and X3 + X4 = 56 with one of them 32.") +
       table(["", "1", "2", "3", "4"], [["X", "12 C", "30 B", "32/24 D", "24/32 D"], ["Y", "21 A", "4 A", "8 B", "16 A"], ["Z", "3 B", "18 C", "9 A", "28 B"]]))) +
 final("Abha 50, Bina 69, Chitra 30, Dipti 56. Dipti’s two plots are 32 and 24, in either order."),
 p("Fix who owns which plot first; only then bring in the numbers."),
 p("<b>Grid allotments:</b> plot-count facts and adjacency rules usually settle the ownership before any arithmetic."))
P.dq(9, "How many mango trees were there in total?", ["49", "126", "84", "98"], "MCQ", "4", "Medium",
 "Mango is twice teak.",
 steps(("From the set solution", p("Teak 21 + 4 + 8 + 16 = 49, so mango 98."))) + final("98, option 4"),
 [("1", "That’s teak."), ("2", "Too many."), ("3", "Not twice the teak.")])
P.dq(10, "Which of the following is the correct sequence of trees received by Abha, Bina, Chitra and Dipti in that order?", ["50, 69, 30, 56", "60, 39, 40, 66", "44, 87, 24, 50", "54, 57, 34, 60"], "MCQ", "1", "Hard",
 "Abha = Chitra + 20 = Dipti − 6.",
 steps(("From the set solution", p("50, 69, 30, 56, adding up to 205."))) + final("Option 1"),
 [("2", "Fits fact 1 but not the grid."), ("3", "Fits fact 1 but not the grid."), ("4", "Fits fact 1 but not the grid.")])
P.dq(11, "How many pine trees did Chitra receive?", ["15", "21", "30", "18"], "MCQ", "4", "Medium",
 "Chitra’s pine plot is Z2.",
 steps(("From the set solution", p("Z2 = 18."))) + final("18, option 4"),
 [("1", "Not a multiple of 3 or 4 that fits."), ("2", "21 is Abha’s teak plot."), ("3", "Chitra’s total.")])
P.dq(12, "Who got the plot with the smallest number of trees and how many trees did that plot have?", ["Abha, 4 trees", "Dipti, 6 trees", "Bina, 3 trees", "Bina, 4 trees"], "MCQ", "3", "Medium",
 "Look at Z1.",
 steps(("From the set solution", p("Z1, Bina’s, has 3."))) + final("Option 3"),
 [("1", "Y2 has 4, but Z1 has fewer."), ("2", "Dipti has 24 and 32."), ("4", "Bina’s Z1 has 3.")])
P.dq(13, "Which of the following statements is NOT true?", ["Chitra got 12 mango trees.", "Dipti got 56 mango trees.", "Abha got 41 teak trees.", "Bina got 32 pine trees."], "MCQ", "4", "Medium",
 "Bina’s pine plots are Z1 and Z4.",
 steps(("From the set solution", p("Bina’s pine: 3 + 28 = 31."))) + final("Option 4"),
 [("1", "X1."), ("2", "X3 + X4."), ("3", "21 + 4 + 16.")])
P.dq(14, "Which column had the highest number of trees?", ["Cannot be determined", "3", "2", "4"], "MCQ", "4", "Medium",
 "Try both ways round for Dipti’s plots.",
 steps(("Column totals", p("Column 1: 36. Column 2: 52. Column 3: 49 or 41. Column 4: 68 or 76. Column 4 either way."))) + final("Column 4, option 4"),
 [("1", "The answer doesn’t depend on the open choice."), ("2", "At most 49."), ("3", "52.")])

# ---------------- Set 4: Hi-Lo ----------------
P.dilr_set(4, "Set 4 — The Hi-Lo game", "Read the following passage carefully and answer the questions that follow.",
 p("The Hi-Lo game is a four-player game played in six rounds. In every round, each player chooses to bid Hi or Lo. The bids are made simultaneously. If all four bid Hi, then all four lose 1 point each. If three players bid Hi and one bids Lo, then the players bidding Hi gain 1 point each and the player bidding Lo loses 3 points. If two players bid Hi and two bid Lo, then the players bidding Hi gain 2 points each and the players bidding Lo lose 2 points each. If one player bids Hi and three bid Lo, then the player bidding Hi gains 3 points and the players bidding Lo lose 1 point each. If all four bid Lo, then all four gain 1 point each.") +
 p("Four players Arun, Bankim, Charu, and Dipak played the Hi-Lo game. The following facts are known about their game:") +
 "<ol><li>At the end of three rounds, Arun had scored 6 points, Dipak had scored 2 points, Bankim and Charu had scored –2 points each.</li><li>At the end of six rounds, Arun had scored 7 points, Bankim and Dipak had scored –1 point each, and Charu had scored –5 points.</li><li>Dipak’s score in the third round was less than his score in the first round but was more than his score in the second round.</li><li>In exactly two out of the six rounds, Arun was the only player who bid Hi.</li></ol>",
 "DILR::LR::Games_and_Tournaments",
 steps(("Round totals", p("Every round adds 0 points in total, except all-Hi (−4) and all-Lo (+4). Rounds 1–3 add +4 and rounds 4–6 add −4.")),
       ("Rounds 1–3", p("Dipak needs three different scores with round 3 in the middle. Working through the cases leaves one possibility: round 1 Hi Lo Lo Hi (Arun and Dipak +2), round 2 Arun alone Hi (+3), round 3 all Lo (+1).")),
       ("Rounds 4–6", p("In some order: Arun alone Hi, Bankim alone Hi, all Hi. In the table, H and L are the bids; the last three rows can come in any order.") +
       table(["Round", "A", "B", "C", "D"], [["1", "H +2", "L −2", "L −2", "H +2"], ["2", "H +3", "L −1", "L −1", "L −1"], ["3", "L +1", "L +1", "L +1", "L +1"],
                                                            ["4–6", "H +3", "L −1", "L −1", "L −1"], ["", "L −1", "H +3", "L −1", "L −1"], ["", "H −1", "H −1", "H −1", "H −1"]]))) +
 final("Rounds 1–3 are fixed; the last three rounds can come in any order."),
 p("Use the round totals to see which kinds of rounds are possible, then use Dipak’s three scores."),
 p("<b>Scoring games:</b> add up each round across players first. Totals often rule out most combinations."))
P.dq(15, "What were the bids by Arun, Bankim, Charu and Dipak, respectively in the first round?", ["Hi, Lo, Lo, Hi", "Hi, Hi, Lo, Lo", "Lo, Lo, Lo, Hi", "Hi, Lo, Lo, Lo"], "MCQ", "1", "Hard",
 "Dipak scored more in round 1 than in rounds 2 and 3.",
 steps(("From the set solution", p("Round 1: Arun and Dipak Hi."))) + final("Option 1"),
 [("2", "Bankim would gain 2."), ("3", "Arun would lose."), ("4", "That’s round 2.")])
P.dq(16, "In how many rounds did Arun bid Hi?", [], "TITA", "4", "Hard",
 "Count from the table.",
 steps(("From the set solution", p("Rounds 1 and 2, the other ‘Arun alone’ round, and the all-Hi round."))) + final(r"\(4\)"))
P.dq(17, "In how many rounds did Bankim bid Lo?", [], "TITA", "4", "Hard",
 "Bankim bid Hi only in his own round and the all-Hi round.",
 steps(("From the set solution", p("Rounds 1, 2, 3 and the ‘Arun alone’ round in 4–6."))) + final(r"\(4\)"))
P.dq(18, "In how many rounds did all four players make identical bids?", [], "TITA", "2", "Hard",
 "All Lo once, all Hi once.",
 steps(("From the set solution", p("Round 3 (all Lo) and one of rounds 4–6 (all Hi)."))) + final(r"\(2\)"))
P.dq(19, "In how many rounds did Dipak gain exactly 1 point?", [], "TITA", "1", "Hard",
 "Only an all-Lo round gives +1 to a Lo bidder.",
 steps(("From the set solution", p("Only round 3."))) + final(r"\(1\)"))
P.dq(20, "In which of the following rounds, was Arun DEFINITELY the only player to bid Hi?", ["Third", "Second", "First", "Fourth"], "MCQ", "2", "Hard",
 "Rounds 4–6 can come in any order.",
 steps(("From the set solution", p("Round 2 is fixed. The other ‘Arun alone’ round could be 4, 5 or 6."))) + final("Second, option 2"),
 [("1", "Everyone bid Lo."), ("3", "Dipak bid Hi too."), ("4", "Possible, but not definite.")])

# ---------------- Set 5: Online teaching survey ----------------
P.dilr_set(5, "Set 5 — 600 schools, four facilities", "Read the following passage carefully and answer the questions that follow.",
 p("A survey of 600 schools in India was conducted to gather information about their online teaching learning processes (OTLP). The following four facilities were studied.") +
 "<ul><li>F1: Own software for OTLP</li><li>F2: Trained teachers for OTLP</li><li>F3: Training materials for OTLP</li><li>F4: All students having Laptops</li></ul>" +
 p("The following observations were summarized from the survey.") +
 "<ol><li>80 schools did not have any of the four facilities — F1, F2, F3, F4.</li><li>40 schools had all four facilities.</li><li>The number of schools with only F1, only F2, only F3, and only F4 was 25, 30, 26 and 20 respectively.</li><li>The number of schools with exactly three of the facilities was the same irrespective of which three were considered.</li><li>313 schools had F2.</li><li>26 schools had only F2 and F3 (but neither F1 nor F4).</li><li>Among the schools having F4, 24 had only F3, and 45 had only F2.</li><li>162 schools had both F1 and F2.</li><li>The number of schools having F1 was the same as the number of schools having F4.</li></ol>",
 "DILR::LR::Venn_Diagrams",
 steps(("Unknowns", p("Let each exactly-three region be t, and the only-F1-and-F2, only-F1-and-F3, only-F1-and-F4 regions be a, b, c. Fact 7 gives only F3 and F4 = 24 and only F2 and F4 = 45.")),
       ("Equations", p("F1 and F2: a + 2t + 40 = 162. F2: 30 + 26 + 45 + a + 3t + 40 = 313. So t = 50 and a = 22.")),
       ("The rest", p("F1 = F4 gives 25 + a + b = 89, so b = 42. All schools with some facility: 101 + 95 + a + b + c + 4t + 40 = 520, so c = 20."))) +
 final("Exactly three: 50 each. Only F1 and F2: 22; only F1 and F3: 42; only F1 and F4: 20."),
 p("Write the four-set regions as letters, then use the F1-and-F2 and F2 counts first."),
 p("<b>Four-set Venn problems:</b> a table of regions is easier than a drawing."))
P.dq(21, "What was the total number of schools having exactly three of the four facilities?", ["80", "64", "200", "50"], "MCQ", "3", "Medium",
 "Four regions of t each.",
 steps(("From the set solution", p(r"\(4 \times 50 = 200\)."))) + final("200, option 3"),
 [("1", "Doesn’t fit the equations."), ("2", "Doesn’t fit the equations."), ("4", "That’s one region.")])
P.dq(22, "What was the number of schools having facilities F2 and F4?", ["95", "45", "185", "85"], "MCQ", "3", "Medium",
 "Include the three-facility and four-facility schools.",
 steps(("Adding", p("Only F2 and F4: 45. Two exactly-three regions with both: 100. All four: 40. Total 185."))) + final("185, option 3"),
 [("1", "Leaves out a region."), ("2", "Only the ‘only F2 and F4’ schools."), ("4", "Leaves out the all-four schools.")])
P.dq(23, "What was the number of schools having only facilities F1 and F3?", [], "TITA", "42", "Medium",
 "This is b.",
 steps(("From the set solution", p(r"\(b = 42\)."))) + final(r"\(42\)"))
P.dq(24, "What was the number of schools having only facilities F1 and F4?", [], "TITA", "20", "Medium",
 "This is c.",
 steps(("From the set solution", p(r"\(c = 20\)."))) + final(r"\(20\)"))
