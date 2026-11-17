# -*- coding: utf-8 -*-
# Simp Mock 4: DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m04 import P

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: A martial-arts school (Q1–5) ----------------
SPLIT = table(["", "Male", "Female", "Total"],
              [["Took part", "38", "37", "75"], ["Age-barred", "37", "43", "80"],
               ["Kept back", "20", "25", "45"], ["Total", "95", "105", "200"]])
P.dilr_set(1, "Set 1 — A Kalaripayattu school at a competition", DIR,
 p("Bhushan Singh runs a small Kalaripayattu school. The sports ministry invited it to a one-day district martial-arts competition. Under the ministry’s rules, participants must be at least 12 and at most 30 years old on the day; those up to 18 compete as Juniors and those over 18 as Seniors.") +
 "<ol><li>The school has 95 male students and some female students.</li>"
 "<li>40% of the school’s students could not take part because of the age limits.</li>"
 "<li>Bhushan lets a student compete only if the student has trained for more than a year. Because of this, another 25 female and some male students could not take part although they met the age rules.</li>"
 "<li>Every student not barred by either rule took part, and one more male than female took part.</li>"
 "<li>Leaving out the 6 female students who are over 30, the number of female students barred by age equals the number of female participants.</li>"
 "<li>The number of female participants is less than the number of male non-participants by 10% of all the students in the school.</li></ol>",
 "DILR::LR::Analytical_Reasoning",
 steps(("Letters", p("Let N female students take part; then N + 1 males take part, N + 6 females are barred by age (fact 5), and females total N + (N + 6) + 25 = 2N + 31. Let p be 10% of all students.")),
       ("Males", p("Male non-participants = N + p (fact 6), so 95 = (N + 1) + (N + p), that is 2N + p = 94.")),
       ("Solve", p("p = 10% of (95 + 2N + 31) = (2N + 126)/10. Then 94 − 2N = (2N + 126)/10 gives 22N = 814, N = 37: 200 students, 105 female, p = 20.")),
       ("Fill in", p("Barred by age: 80 in all, 43 female, so 37 male. Male non-participants 57, so 20 males were kept back by Bhushan.") + SPLIT)) +
 final("Everything follows from N = 37."),
 p("Write every group in terms of the number of female participants; fact 6 then gives one equation."),
 p("<b>Two-way tables:</b> set up rows (took part / barred by age / kept back) against columns (male / female) and fill from the facts."))
P.dq(1, "What is the difference between the numbers of male and female students in the school?", ["5", "10", "15", "20"], "MCQ", "2", "Medium",
 "Female students total 2N + 31.",
 steps(("Count", p("105 female, 95 male: 10."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "The number p.")])
P.dq(2, "What is (male students kept back by Bhushan) ÷ (female students kept back by Bhushan)?", ["0.6", "0.8", "1.0", "1.25"], "MCQ", "2", "Medium",
 "20 males and 25 females.",
 steps(("Ratio", p("20 ÷ 25 = 0.8."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "The ratio upside down.")])
P.dq(3, "Senior female participants make up 7% of all the students in the school, and the school sent 39 Junior participants in all. How many Junior male participants were there?", ["14", "15", "16", "18"], "MCQ", "3", "Medium",
 "Senior females: 7% of 200.",
 steps(("Females", p("14 Senior, so 37 − 14 = 23 Junior.")),
       ("Males", p("39 − 23 = 16."))) + final("Option 3"),
 [("1", "The number of Senior females."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(4, "As in the previous question, Senior female participants are 7% of all students and there were 39 Junior participants. Exactly 32 male students in the school were of Senior age (over 18 and up to 30). How many male students aged 12 to 18 have trained for a year or less?", ["8", "9", "10", "11"], "MCQ", "3", "Medium",
 "Senior males who took part: 38 − 16.",
 steps(("Senior males", p("38 − 16 = 22 took part, so 32 − 22 = 10 of Senior age were kept back by Bhushan.")),
       ("Junior age", p("Bhushan kept back 20 males in all, so 20 − 10 = 10 were aged 12 to 18."))) + final("Option 3"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(5, "Bhushan says 43 17/21 % of his female students have trained for a year or less, and 18 of these are under 12. How many female students over 30 have trained for more than a year?", [], "TITA", "3", "Medium",
 "43 17/21 % = 46/105.",
 steps(("Short training", p("46 of the 105 female students: 18 under 12, 25 of eligible age (fact 3), so 3 over 30.")),
       ("Over 30", p("6 females are over 30, so 6 − 3 = 3 have trained longer."))) + final("3"))

# ---------------- Set 2: Coins from a four-sided die (Q6–10) ----------------
COINS = table(["Face", "Coin", "Points", "Number"], [["Gold", "Red", "40", "1"], ["Silver", "Yellow", "20", "3"], ["Bronze", "Green", "10", "5"], ["Copper", "Brown", "1", "many"]])
P.dilr_set(2, "Set 2 — A coin game with a long die", DIR,
 p("Kapil, Raman and Pramila play a game with a cuboid die. Its four long faces are marked Gold, Silver, Bronze and Copper; if a square end shows, the same player rolls again. The face rolled wins the player one coin, as below.") + COINS +
 p("The players roll in a fixed turn order (decided by a draw) until all coins are taken. If the coin a player rolls for is already gone, the player gets nothing and the turn passes. If all red, yellow and green coins are taken before any brown coin, the game ends at once."),
 "DILR::LR::Games_and_Tournaments",
 steps(("Non-brown points", p("Red, yellow and green coins are worth 40 + 60 + 50 = 150 points; brown coins add 1 point each.")),
       ("Coin counts", p("There are 9 non-brown coins: 1 red, 3 yellow, 5 green.")),
       ("Equal shares", p("When totals must be equal or in a ratio, split the 150 non-brown points first; brown coins make up the rest."))) +
 final("Each question fixes the share of points and coins."),
 p("Split 150 into the required shares, then check coin counts."),
 p("<b>Coin partitions:</b> list the few ways to make each share from 40s, 20s and 10s."))
P.dq(6, "The game ended with no brown coins taken. Pramila got more yellow coins than Kapil, but Kapil got more green coins than Pramila. The three won different numbers of coins but equal points. How many green coins did Raman win?", ["0", "1", "2", "3"], "MCQ", "2", "Hard",
 "Each has 50 points.",
 steps(("Red holder", p("40 + 10: the red coin and one green (2 coins).")),
       ("Others", p("3 yellows and 4 greens make two 50s: 1Y + 3G (4 coins) and 2Y + 1G (3 coins).")),
       ("Who", p("Pramila has more yellows and Kapil more greens: Pramila 2Y + 1G, Kapil 1Y + 3G. Raman has the red and 1 green."))) + final("Option 2"),
 [("1", "Raman needs 10 more points."), ("3", "Kapil has 3; Raman 1."), ("4", "Kapil’s count.")])
P.dq(7, "In the same game, how many yellow coins did Raman win?", [], "TITA", "0", "Hard",
 "Raman has the red and a green.",
 steps(("Raman", p("40 + 10 = 50: no yellow."))) + final("0"))
P.dq(8, "At the end, Kapil, Raman and Pramila had points in the ratio 1 : 2 : 3 and brown coins in the ratio 3 : 5 : 7. One player took all three yellow coins but not the red. Kapil won two green coins. How many brown coins were won in all?", ["90", "120", "150", "180"], "MCQ", "3", "Hard",
 "Brown coins 3b, 5b, 7b; total points 150 + 15b.",
 steps(("Kapil", p("Kapil has (150 + 15b)/6 = 25 + 2.5b points, of which 3b are brown, so his other coins are worth 25 − 0.5b.")),
       ("Bound", p("Two greens give at least 20, and the value is below 25 and a multiple of 10: 20. So b = 10.")),
       ("Check", p("Raman 100 = 50 brown + 50 (red + green); Pramila 150 = 70 brown + 80 (three yellows + two greens).")),
       ("Total", p("15b = 150."))) + final("Option 3"),
 [("1", "Uses b = 6."), ("2", "Uses b = 8."), ("4", "Uses b = 12.")])
P.dq(9, "In the same game, how many brown coins did Pramila win?", [], "TITA", "70", "Hard",
 "7b with b = 10.",
 steps(("Pramila", p("7 × 10 = 70."))) + final("70"))
P.dq(10, "At the end, all three players had equal points, and each had the same number of non-brown coins. What is the smallest possible number of brown coins won in all?", ["30", "50", "60", "90"], "MCQ", "1", "Medium",
 "Three non-brown coins each; the red holder has at least 60.",
 steps(("Red holder", p("Red plus two of the cheapest coins: 40 + 10 + 10 = 60. So each player must end with at least 60.")),
       ("Brown", p("3 × 60 − 150 = 30. It works: 3 yellows (60) for one player, 3 greens (30) + 30 brown for another, or 2Y + 1G (50) + 10 and 1Y + 2G (40) + 20."))) + final("Option 1"),
 [("2", "Not the least."), ("3", "Not the least."), ("4", "Not the least.")])

# ---------------- Set 3: A row of 15 students (Q11–15) ----------------
ROWS = table(["Case", "Positions 1–15"], [["1", "MTMSMTMSMSSTSTS"], ["2", "MTMSMSMTMSSTSTS"], ["3", "MSMTMTMSMSSTSTS"]])
P.dilr_set(3, "Set 3 — Heights in a group photo", DIR,
 p("Fifteen students stand in a row for a photo. Each is Tall, Medium or Short. There are at least 3 of each kind, and the three counts are all different. Positions are counted from the left.") +
 "<ol><li>Among the first 5 students, exactly one is Short.</li>"
 "<li>Among the first 10, Medium students are the most, then Short, and Tall the fewest (at least one).</li>"
 "<li>Positions 10 and 11 are the only two neighbouring positions with students of the same kind.</li>"
 "<li>Medium is not the most common kind overall.</li>"
 "<li>There is exactly one pair of Tall students with exactly 5 students (none of them Tall) between them.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("First ten", p("No two of positions 1–10 match, so at most 5 of them are Medium. Fact 2 then needs Medium 5, with Short 4 and Tall 1, or Short 3 and Tall 2.")),
       ("Overall counts", p("Positions 11–15 alternate between two kinds. A Medium there would make Medium at least 6; another group would then need at least 7 to be larger, leaving at most 2 for the third, which is too few. So Medium is exactly 5, and positions 11–15 alternate Short and Tall.")),
       ("Positions 10–15", p("If 11, 13, 15 were Tall, position 10 would be Tall too; with (4, 1) all four Shorts would sit in 2, 4, 6, 8, breaking fact 1, and (3, 2) would give Short = 5 = Medium. So 10, 11, 13, 15 are Short and 12, 14 Tall. With (4, 1) there would be no Tall pair six apart, so it is (3, 2): Short 6, Tall 4.")),
       ("Positions 1–9", p("Five Mediums with no two adjacent in positions 1–9 must be at 1, 3, 5, 7, 9. Of 2, 4, 6, 8, two are Short and two Tall, with exactly one Short among 2 and 4 (fact 1). Fact 5 rules out Short at 2 and 6 (no Tall pair six apart) and leaves three arrangements.") + ROWS)) +
 final("Three arrangements; 11 positions are the same in all of them."),
 p("‘Only neighbours that match’ plus ‘Medium the most’ forces Mediums into alternate places."),
 p("<b>Alternating rows:</b> when no neighbours may match, a group can take at most every other place."))
P.dq(11, "Which of these must be true?<br>(1) The student in position 5 is Tall.<br>(2) The student in position 8 is Short.", ["Only (1)", "Only (2)", "Both (1) and (2)", "Neither (1) nor (2)"], "MCQ", "4", "Hard",
 "Look at positions 5 and 8 in the three cases.",
 steps(("Position 5", p("Medium in every case.")),
       ("Position 8", p("Short in cases 1 and 3, Tall in case 2."))) + final("Option 4"),
 [("1", "Position 5 is Medium."), ("2", "Position 8 can be Tall."), ("3", "Neither holds.")])
P.dq(12, "What best describes the number of Short students?", ["Exactly 6", "Exactly 7", "At least 5", "Fewer than 6"], "MCQ", "1", "Hard",
 "Count S in any case.",
 steps(("Count", p("Every case has 6 Short students."))) + final("Option 1"),
 [("2", "One too many."), ("3", "True but not the best."), ("4", "There are 6.")])
P.dq(13, "For how many positions is the category fixed?", [], "TITA", "11", "Hard",
 "Compare the three cases position by position.",
 steps(("Varying", p("Positions 2, 4, 6 and 8 change between cases.")),
       ("Fixed", p("15 − 4 = 11."))) + final("11"))
P.dq(14, "Which statement(s) are definitely true?<br>St-1: Positions 4 and 14 are of the same category.<br>St-2: Positions 7 and 10 are of the same category.<br>St-3: Positions 10 and 15 are of the same category.", ["Only St-1", "Both St-2 and St-3", "Both St-1 and St-3", "Only St-3"], "MCQ", "4", "Hard",
 "Positions 10 and 15 are both Short.",
 steps(("St-1", p("Position 4 is Short in cases 1 and 2 but Tall in case 3; position 14 is Tall.")),
       ("St-2", p("7 is Medium, 10 Short.")),
       ("St-3", p("Both Short."))) + final("Option 4"),
 [("1", "Fails in cases 1 and 2."), ("2", "St-2 is false."), ("3", "St-1 can fail.")])
P.dq(15, "Add up the positions of all the Tall students. In which range must the sum lie?", ["30–32", "33–35", "33–36", "30–34"], "MCQ", "3", "Hard",
 "Sum the Tall positions in each case.",
 steps(("Sums", p("Case 1: 2 + 6 + 12 + 14 = 34. Case 2: 2 + 8 + 12 + 14 = 36. Case 3: 4 + 6 + 12 + 14 = 36.")),
       ("Range", p("34 or 36: only 33–36 covers both."))) + final("Option 3"),
 [("1", "Too low."), ("2", "Misses 36."), ("4", "Misses 36.")])

# ---------------- Set 4: A pre-poll survey (Q16–20) ----------------
URB = table(["Urban", "A", "B", "C"], [["Total", "500", "560", "300"], ["P1", "261", "319", "60"], ["P2", "", "", ""], ["P3", "", "", "119"]])
FULL4 = table(["", "A", "B", "C"], [["P1 urban", "261", "319", "60"], ["P2 urban", "120", "119", "121"], ["P3 urban", "119", "122", "119"],
                                    ["P1 rural", "139", "192", "29"], ["P2 rural", "0", "0", "240"], ["P3 rural", "161", "248", "31"]])
P.dilr_set(4, "Set 4 — A pre-poll survey in three districts", DIR,
 p("Before a state election, a news channel surveyed voters in three districts, A, B and C: 800, 1000 and 600 people respectively. Only three parties, P1, P2 and P3, are contesting, and each respondent named exactly one party (the party’s ‘Pre-vote’). Each district’s survey was split into urban and rural parts.") +
 p("The table gives partial urban data. For example, 560 people were surveyed in urban District B, and 319 of them Pre-voted P1.") + URB +
 "<ol><li>In rural District C, 80% of those surveyed Pre-voted P2.</li>"
 "<li>P3 got 35% of the Pre-votes in District A, 37% in District B and 25% in District C.</li>"
 "<li>Over all three districts, P1 got 25% more Pre-votes than P3.</li>"
 "<li>In urban District A, P2 got more Pre-votes than P3 but fewer than P1.</li>"
 "<li>In urban District C, P2 got more Pre-votes than either other party, but fewer than P3 got in urban District B.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("Party totals", p("P3: 280 + 370 + 150 = 800. P1: 1.25 × 800 = 1000. P2: 2400 − 1800 = 600.")),
       ("Urban C", p("P2 = 300 − 60 − 119 = 121. Rural C has 300 people, so 240 rural P2 votes there.")),
       ("Pin down P2", p("Urban A: P2 + P3 = 239 with P2 > P3, so P2 ≥ 120. Urban B: P3 > 121 (fact 5), so P2 = 241 − P3 ≤ 119. All P2 votes add to 600, of which at least 240 are rural and 121 urban C: urban A + urban B P2 ≤ 239. So urban A P2 = 120 and urban B P2 = 119 exactly, and no rural P2 votes outside C.")),
       ("Rest", p("Urban P3: A 119, B 122. Rural P3 = district P3 − urban P3; rural P1 makes up the rest.") + FULL4)) +
 final("The whole table is fixed."),
 p("The P2 total of 600 is tight: once rural C takes 240, urban A and B have no slack."),
 p("<b>Tight totals:</b> when lower bounds add up to exactly the total, every bound is met with equality."))
P.dq(16, "What is P3’s Pre-vote in rural District B?", [], "TITA", "248", "Hard",
 "District B’s P3 is 370.",
 steps(("Rural B", p("370 − 122 = 248."))) + final("248"))
P.dq(17, "What is the smallest Pre-vote of any party in any district’s rural area?", [], "TITA", "0", "Hard",
 "Where did P2 get rural votes?",
 steps(("P2", p("All of P2’s rural votes are in C; it got 0 in rural A and rural B."))) + final("0"))
P.dq(18, "What is P2’s total Pre-vote?", [], "TITA", "600", "Medium",
 "2400 − P1 − P3.",
 steps(("Total", p("2400 − 1000 − 800 = 600."))) + final("600"))
P.dq(19, "What percentage of District B’s respondents Pre-voted P1 or P2?", ["63", "61", "59", "53"], "MCQ", "1", "Easy",
 "P3 had 37%.",
 steps(("Complement", p("100 − 37 = 63%."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(20, "What is the difference between P2’s Pre-votes in urban and rural District C?", ["118", "119", "120", "121"], "MCQ", "2", "Medium",
 "Urban 121, rural 240.",
 steps(("Difference", p("240 − 121 = 119."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Uses 120 for urban C."), ("4", "Urban C’s value itself.")])
