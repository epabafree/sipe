# -*- coding: utf-8 -*-
# Simp Mock 19 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_19 import P

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Grades in a mock test (Q1–5) ----------------
GR = [("G1", 26, 44, 18, 40, 33, 36, 3), ("G2", 32, 27, 25, 36, 32, 40, 8),
      ("G3", 31, 38, 41, 27, 23, 31, 9), ("G4", 28, 27, 30, 32, 42, 38, 3),
      ("H1", 22, 37, 44, 25, 31, 37, 4), ("H2", 37, 26, 24, 24, 43, 41, 5),
      ("P1", 29, 34, 44, 34, 26, 31, 2), ("P2", 34, 18, 21, 43, 35, 31, 18)]
for r in GR:
    assert sum(r[1:]) == 200
GRADES = table(["", "A+", "A", "A−", "B+", "B", "B−", "C"], [[r[0]] + [str(x) for x in r[1:]] for r in GR])
TOP = [sum(r[1:4]) for r in GR]          # A− or better: 88, 84, 110, 85, 103, 87, 107, 73
assert sum(TOP) == 737 and min(TOP) == 73
P.dilr_set(1, "Set 1 — Grades in a mock test", DIR,
 p("A coaching institute for a civil-services exam mentors 200 students. Shortly before the final exam it held a mock test in eight papers: four in General Studies (G1 to G4), two in History (H1, H2) and two in Political Science (P1, P2).") +
 p("In each paper a student gets one of seven grades. From best to worst they are A+, A, A−, B+, B, B− and C. The table gives the number of students with each grade in each paper; every row adds up to 200.") + GRADES,
 "DILR::DI::Data_Tabulation",
 steps(("Read the columns", p("Questions about one grade across all papers look down a column: the smallest entry caps how many students can share that grade everywhere, and the largest entry is the fewest who must have it somewhere.")),
       ("Read the rows", p("“A− or better” in a paper is A+ + A + A−: 88, 84, 110, 85, 103, 87, 107 and 73 in the order of the table, 737 grades in all.")),
       ("Count grades, not students", p("When a question asks how many students can have a grade some number of times, divide the total number of such grades by that number, then check that no paper needs more than its column allows."))) +
 final("Columns cap overlaps; totals divided by the repeat count give the most students."),
 p("Overlap questions are min/max of a column; repeat questions are a total divided by the repeat count."),
 p("<b>Maximum overlap:</b> at most as many students share a feature in every paper as the smallest paper count. <b>Minimum union:</b> at least as many as the largest single count."))
P.dq(1, "At most how many students could have received the same grade in all eight papers?", ["128", "132", "138", "142"], "MCQ", "3", "Medium",
 "Do it grade by grade: the smallest number in each column.",
 steps(("Column minima", p("A+ 22, A 18, A− 18, B+ 24, B 23, B− 31, C 2.")),
       ("Add", p("A student who gets the same grade everywhere is counted in one column only, so the groups do not overlap: 22 + 18 + 18 + 24 + 23 + 31 + 2 = 138.")),
       ("Possible?", p("Yes: in each column, the smallest count can be the same students in every paper, and these groups are different students."))) + final("Option 3"),
 [("1", "Leaves out a grade’s column."), ("2", "Arithmetic slip."), ("4", "Uses a larger entry in some column.")])
P.dq(2, "At least how many students received a grade of A− or better in at most three papers?", ["12", "16", "18", "22"], "MCQ", "2", "Hard",
 "There are 737 such grades. Give as many students as possible four or more of them.",
 steps(("Total", p("A− or better: 88 + 84 + 110 + 85 + 103 + 87 + 107 + 73 = 737 grades.")),
       ("Four each", p("A student with four or more uses at least 4 of these grades. 737 ÷ 4 = 184.25, so at most 184 students can have four or more (184 × 4 = 736, and the one spare grade goes to any of them).")),
       ("Rest", p("200 − 184 = 16 students are left with three or fewer (they can have none at all). No paper needs more than 184 of these grades, so the spread is possible."))) + final("Option 2"),
 [("1", "More students than 737 grades can supply four each."), ("3", "Not the least."), ("4", "Not the least.")])
P.dq(3, "At most how many students could have received a B in exactly five papers?", ["47", "49", "53", "55"], "MCQ", "3", "Medium",
 "Add the B column.",
 steps(("B grades", p("33 + 32 + 23 + 42 + 31 + 43 + 26 + 35 = 265.")),
       ("Five each", p("265 ÷ 5 = 53. Every paper’s B count is at most 53, so 53 students can share the 265 Bs five apiece (fill the papers in turn, as in a rota)."))) + final("Option 3"),
 [("1", "Not the most."), ("2", "Not the most."), ("4", "Needs 275 Bs.")])
P.dq(4, "At least how many students received an A+ in at least one of the eight papers?", [], "TITA", "37", "Easy",
 "Let the same students take the A+ grades everywhere.",
 steps(("Largest column entry", p("H2 alone has 37 A+ grades, so at least 37 students. The A+ students of every other paper (at most 34) can be chosen from these 37."))) + final("37"))
P.dq(5, "At most how many students received a grade of A− or better in all eight papers?", [], "TITA", "73", "Easy",
 "Smallest row total of A+, A and A−.",
 steps(("Smallest", p("P2 has only 34 + 18 + 21 = 73 such grades; every other paper has more, so all 73 can be the same students."))) + final("73"))

# ---------------- Set 2: A doctor's portfolio (Q6–9) ----------------
PT = table(["", "IT", "Pharma", "Mfg", "Auto"],
           [["Stocks", "12", "6", "10", "8"], ["Total", "1150", "720", "540", ""],
            ["Platinum", "725", "210", "", ""], ["Gold", "", "125", "", "90"],
            ["Silver", "120", "", "", ""], ["Cuprium", "", "", "115", ""]])
FIN = table(["", "IT", "Pharma", "Auto"],
            [["Platinum", "725", "210", "180"], ["Gold", "145", "125", "90"],
             ["Silver", "120", "110", "45"], ["Cuprium", "≤ 120", "95", "< 45"]])
P.dilr_set(2, "Set 2 — Platinum, Gold, Silver and Futile", DIR,
 p("Dr Patankar, a doctor, has invested in the stock market for twenty years. He holds stocks in four sectors: Information Technology (IT), Pharmaceuticals (Pharma), Manufacturing (Mfg) and Automobiles (Auto) — 12 IT companies, 6 Pharma, 10 Mfg and 8 Auto.") +
 p("Within each sector he ranks his holdings by market value. The highest is the <b>Platinum</b> stock, the second the <b>Gold</b>, the third the <b>Silver</b> and the fourth the <b>Cuprium</b>. A stock worth less than 12.5% of the total value of that sector’s holdings is called <b>Futile</b>.") +
 p("The table gives partial information about the market values on 1 October 2025, in thousands of rupees.") + PT +
 p("The following facts are also known.") +
 "<ol><li>In IT, the Gold stock is worth ₹25,000 more than the Silver stock.</li>"
 "<li>In Pharma, no stock is Futile. Two of the stocks together are worth 25% of the sector’s total, and the values of three of the stocks are in arithmetic progression.</li>"
 "<li>A Platinum stock is never Futile.</li>"
 "<li>In Auto, the Platinum, Gold and Silver stocks are in the ratio 4 : 2 : 1, and the remaining stocks together are worth 30% of the sector’s total.</li>"
 "<li>Every stock’s value (in ₹) is a multiple of 50, and there is exactly one instance of two stocks in the same sector having the same value.</li></ol>",
 "DILR::DI::Caselets",
 steps(("IT", p("Gold = 120 + 25 = 145 thousand. The Futile line is 12.5% of 1150 = 143.75 thousand, so Gold is not Futile but Silver and everything below it are.")),
       ("Pharma", p("No stock is Futile, so each is at least 12.5% of 720 = 90 thousand. Two stocks worth 25% = 180 thousand must then be exactly 90 each: this is the one tie, and they are the two smallest. Silver + Cuprium = 720 − 210 − 125 − 180 = 205 thousand.")),
       ("Pharma AP", p("Gold, Silver, Cuprium in AP: S = (125 + C) ÷ 2 with S + C = 205 gives S = 110, C = 95. (Gold, Silver and a 90 in AP gives S = 107.5, C = 97.5, also allowed; Silver, Cuprium, 90 needs C = 98.33…, not a multiple of 50 rupees.)")),
       ("Auto", p("Gold 90 gives Platinum 180 and Silver 45: together 315 thousand = 70%, so the total is 450 thousand and the other five stocks share 135 thousand, each below 45.") + FIN)) +
 final("Values in thousands of rupees; Mfg is worked out in Q9."),
 p("Turn every percentage into a rupee line first: 12.5% of the total is the Futile cut-off."),
 p("<b>Forced equality:</b> if two items are each at least m and add up to exactly 2m, both equal m."))
P.dq(6, "Which of the following could be the market value of the Cuprium stock in the Pharma sector?", ["₹1,10,000", "₹1,05,000", "₹95,000", "₹90,000"], "MCQ", "3", "Medium",
 "Silver + Cuprium = ₹2,05,000; find the arithmetic progression.",
 steps(("Bottom two", p("Each stock is at least ₹90,000, so the two worth ₹1,80,000 together are ₹90,000 each, and Silver + Cuprium = ₹2,05,000.")),
       ("AP", p("If Gold, Silver and Cuprium are in AP, then 2S = 1,25,000 + C. With S + C = 2,05,000 this gives S = ₹1,10,000 and C = ₹95,000.")),
       ("Other options", p("₹1,10,000 and ₹1,05,000 would make Cuprium at least as large as Silver; ₹90,000 would be a second tie."))) + final("Option 3"),
 [("1", "That is the Silver stock."), ("2", "Then Silver is ₹1,00,000, smaller than Cuprium."), ("4", "A second pair of equal values.")])
P.dq(7, "The total value of all Futile stocks in the IT sector is approximately what percentage of the sector’s total value?", ["18.75%", "21.55%", "24.35%", "27.15%"], "MCQ", "3", "Medium",
 "Futile line = ₹1,43,750.",
 steps(("Not Futile", p("Platinum ₹7,25,000 and Gold ₹1,45,000: ₹8,70,000.")),
       ("Futile", p("Everything else: 11,50,000 − 8,70,000 = ₹2,80,000.")),
       ("Share", p("2,80,000 ÷ 11,50,000 ≈ 24.35%."))) + final("Option 3"),
 [("1", "Counts only the stocks below Silver."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(8, "In the Auto sector the smallest stock is worth ₹23,000. What is the least possible difference between the values of the Platinum and Cuprium stocks?", ["₹1,33,700", "₹1,37,300", "₹1,73,300", "₹1,77,300"], "MCQ", "2", "Hard",
 "Make Cuprium as big as possible by keeping the other four small.",
 steps(("Five stocks", p("Cuprium and four smaller stocks share ₹1,35,000, all different (the only tie is in Pharma) and multiples of ₹50.")),
       ("Smallest four", p("23,000 + 23,050 + 23,100 + 23,150 = ₹92,300.")),
       ("Cuprium", p("1,35,000 − 92,300 = ₹42,700, which is below Silver’s ₹45,000, as it must be.")),
       ("Difference", p("1,80,000 − 42,700 = ₹1,37,300."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(9, "The difference between the values of the Platinum and Gold stocks in a sector is its Top Margin. Which sector has the third highest Top Margin?", ["IT", "Pharma", "Mfg", "Auto"], "MCQ", "2", "Hard",
 "Bound the Mfg margin.",
 steps(("Known", p("IT 725 − 145 = 580 thousand; Auto 180 − 90 = 90 thousand; Pharma 210 − 125 = 85 thousand.")),
       ("Mfg", p("Platinum + Gold + Silver = 540 − 115 − (six smaller stocks) ≤ 540 − 115 − 1.05 = 423.95 thousand, the six smallest being at least ₹50, ₹100, …, ₹300. Silver is at least 115.05 and Gold at least 115.1, so Platinum ≤ 193.8 and the margin is at most 78.7 thousand.")),
       ("Order", p("IT > Auto > Pharma > Mfg."))) + final("Option 2"),
 [("1", "Highest."), ("3", "Always the lowest."), ("4", "Second highest.")])

# ---------------- Set 3: Shooting planes (Q10–13) ----------------
PTS = table(["Planes", "Points for 1, 2, 3, … hits"],
            [["4", "−1, 3, 6, 10"], ["5", "−2, 1, 5, 8, 12"], ["6", "−3, 0, 4, 7, 10, 14"]])
P.dilr_set(3, "Set 3 — Shooting down planes", DIR,
 p("Raghav, Indu, Dhruv, Shekhar and Kanti each play a computer game of shooting down enemy planes. One person plays at a time, and a game has three rounds. In each round the player fires exactly one cannon ball at each plane on the screen; a hit shoots the plane down, a miss lets it survive.") +
 p("Round 1 always starts with 4 planes. After each round:") +
 "<ul><li>if the player shot down fewer than half the planes, the next round has the same number of planes;</li>"
 "<li>if the player shot down at least half but not all of them, the next round has the same number of planes and the player earns 1 bonus point;</li>"
 "<li>if the player shot down all of them, the next round has one plane more and the player earns 2 bonus points.</li></ul>" +
 p("The bonus is earned in the third round too, even though no round follows. A player gets 2 points for every plane shot down and loses 1 point for every plane that survives. Every player shoots down at least one plane in every round."),
 "DILR::LR::Games_and_Tournaments",
 steps(("One round", p("With N planes and k hits the round scores 3k − N, plus the bonus.") + PTS),
       ("Planes in a game", p("Round 1 has 4. Round 2 has 5 only after a perfect round 1 (10 points); round 3 has 6 only after perfect rounds 1 and 2 (10 and 12).")),
       ("Two-round totals", p("Without a perfect first round: two scores from −1, 3, 6, 10, giving −2, 2, 5, 6, 9, 12, 13, 16. With one: 10 plus −2, 1, 5, 8 or 12, giving 8, 11, 15, 18, 22."))) +
 final("Use the points table and track how many planes each round has."),
 p("Some scores occur with only one number of planes: 0, 4, 7 and 14 need six planes, so they pin down the whole game."),
 p("<b>Rule-driven states:</b> list every score a round can give for each starting state before reading the questions."))
P.dq(10, "Shekhar scored 0 points in one round. What was his total score for the game?", [], "TITA", "22", "Medium",
 "Which number of planes allows a score of 0?",
 steps(("0 points", p("0 = 3k − N with no bonus needs N = 6, k = 2 (two of six is fewer than half). So this was round 3 with six planes.")),
       ("Rounds 1 and 2", p("Six planes in round 3 needs perfect rounds before: 10 and 12.")),
       ("Total", p("10 + 12 + 0 = 22."))) + final("22"))
P.dq(11, "After two rounds the players stated their totals: Raghav 19, Shekhar 17, Kanti 10, Indu 14 and Dhruv 15. Only one of them stated the true score. Who? (Enter 1 for Raghav, 2 for Shekhar, 3 for Kanti, 4 for Indu, 5 for Dhruv.)", [], "TITA", "5", "Medium",
 "List the possible two-round totals.",
 steps(("Possible totals", p("−2, 2, 5, 6, 9, 12, 13, 16 and 8, 11, 15, 18, 22.")),
       ("Check", p("19, 17, 10 and 14 are not on the list; 15 is (10 in round 1, then 5 with three of five planes)."))) + final("5"))
P.dq(12, "Indu’s second round started with 5 planes. What is the largest possible difference between two of his possible game totals?", [], "TITA", "30", "Medium",
 "Round 1 was perfect: 10 points.",
 steps(("Best", p("Perfect rounds 2 and 3: 10 + 12 + 14 = 36.")),
       ("Worst", p("One hit in round 2 (−2) keeps five planes; one hit in round 3 (−2): 10 − 2 − 2 = 6.")),
       ("Difference", p("36 − 6 = 30."))) + final("30"))
P.dq(13, "Kanti scored 7 points in one round. How many planes appeared on the screen during Kanti’s whole game?", [], "TITA", "15", "Easy",
 "7 appears in only one row of the points table.",
 steps(("7 points", p("Only six planes with four hits gives 7 (12 − 2 + 1 bonus). So round 3 had six planes, and rounds 1 and 2 had four and five.")),
       ("Total", p("4 + 5 + 6 = 15."))) + final("15"))

# ---------------- Set 4: Coded words (Q14–18) ----------------
WORDS = table(["Word", "Code"], [["violin", "112246"], ["expert", "667889"], ["pressure", "22466888"], ["caliber", "2345678"],
                                 ["summary", "2344558"], ["reserve", "1266688"], ["distress", "12222689"], ["wildlife", "12234469"]])
KEY = table(["Digit", "Letters"], [["1", "d, v, and one of o / n"], ["2", "s, i"], ["3", "a, and one of w / f"], ["4", "l, u, y"],
                                   ["5", "m, and one of b / c"], ["6", "e, and one of o / n"], ["7", "x, and one of b / c"],
                                   ["8", "r, p"], ["9", "t, and one of w / f"]])
P.dilr_set(4, "Set 4 — Sorted digit codes", DIR,
 p("In a code, each letter is replaced by one of the digits 1 to 9, and then the digits of the word are written in ascending order. Each digit stands for two or three letters. These words and their codes are known:") + WORDS,
 "DILR::LR::Analytical_Reasoning",
 steps(("Repeated letters", p("reserve has three e’s and one digit appears three times: e = 6. distress has three s’s: s = 2. pressure then has r twice: r = 8.")),
       ("i and l", p("violin has two i’s, so i is 1 or 2; caliber has no 1, so i = 2. wildlife has two l’s: l = 4.")),
       ("summary and caliber", p("summary has two m’s: m = 5, so a and y are 3 and 4. caliber has one 3 and one 4 and l = 4, so a = 3, y = 4, and u = 4.")),
       ("The rest", p("pressure’s third 8 is p. expert leaves x, t = 7, 9; distress has a 9 and no 7, so t = 9, x = 7. reserve leaves v = 1; violin then has o, n = 1, 6; distress gives d = 1. caliber leaves c, b = 5, 7 and wildlife leaves w, f = 3, 9.") + KEY)) +
 final("Three pairs (o/n, b/c, w/f) are open; letters such as g, h, j, k, q, z are never used."),
 p("A digit that appears as often as a repeated letter is the place to start."),
 p("<b>Sorted codes:</b> the order is lost, so match counts — how many times each digit appears — rather than positions."))
P.dq(14, "What is the code for ‘m’?", ["7", "5", "3", "1"], "MCQ", "2", "Easy",
 "summary has two m’s.",
 steps(("summary", p("2344558 has only one repeated digit besides 4: 5. The two m’s are 5."))) + final("Option 2"),
 [("1", "That is x."), ("3", "That is a."), ("4", "That is d and v.")])
P.dq(15, "The digit 9 is definitely not the code for which letter?", ["t", "f", "x", "w"], "MCQ", "3", "Easy",
 "x and t share 7 and 9 in expert.",
 steps(("x", p("t = 9, so x = 7.")), ("w, f", p("One of them is 9."))) + final("Option 3"),
 [("1", "t = 9."), ("2", "f may be 9."), ("4", "w may be 9.")])
P.dq(16, "Which of these is definitely the code for ‘textile’?", ["2466799", "2446799", "2366799", "2466779"], "MCQ", "1", "Easy",
 "t 9, e 6, x 7, i 2, l 4.",
 steps(("Digits", p("t, e, x, t, i, l, e = 9, 6, 7, 9, 2, 4, 6. Sorted: 2466799."))) + final("Option 1"),
 [("2", "Two 4s."), ("3", "A 3 in place of 4."), ("4", "Two 7s.")])
P.dq(17, "For which word can the code not be determined uniquely?", ["warfare", "climber", "monetary", "bonafide"], "MCQ", "4", "Medium",
 "A word with both letters of a pair is fine; one with only one of them is not.",
 steps(("Pairs", p("o/n, b/c and w/f each share two digits between them.")),
       ("Check", p("warfare has w and f; climber has c and b; monetary has o and n; bonafide has b without c and f without w."))) + final("Option 4"),
 [("1", "Has both w and f."), ("2", "Has both c and b."), ("3", "Has both o and n.")])
P.dq(18, "If the code for ‘newspaper’ is 123366888, what must the code for ‘profiles’ be?", ["22346688", "22466889", "12246889", "24466889"], "MCQ", "2", "Medium",
 "Remove the known letters from the code.",
 steps(("Known", p("e, s, p, a, p, e, r = 6, 2, 8, 3, 8, 6, 8. Removing these leaves 1 and 3 for n and w.")),
       ("Settle pairs", p("w is 3 or 9, so w = 3, n = 1; then f = 9 and o = 6.")),
       ("profiles", p("8, 8, 6, 9, 2, 4, 6, 2 sorted: 22466889."))) + final("Option 2"),
 [("1", "Takes f = 3."), ("3", "Takes o = 1."), ("4", "Drops one s.")])

# ---------------- Set 5: Nine friends on a hike (Q19–22) ----------------
GRP = table(["Group", "Cooking", "Tenting"], [["X", "Prakash, Raja", "Aakash"], ["Y", "Tarun", "Biva, Chitra"], ["Z", "Mansi, Neha", "Dhanush"]])
P.dilr_set(5, "Set 5 — Nine friends on a hike", DIR,
 p("Aakash, Biva, Chitra, Dhanush, Mansi, Neha, Prakash, Raja and Tarun are nine friends going on a hike in the Chitrakut hills. Three come from each of three states: Chhattisgarh, Jharkhand and Madhya Pradesh. On the hike each friend does exactly one of two jobs, cooking or tenting. Every state has at least one cook and at least one tent-pitcher, and there is one more cook than tent-pitcher.") +
 p("The following facts are also known.") +
 "<ol><li>Aakash, Biva and Neha are from three different states. Aakash and Biva do the same job.</li>"
 "<li>Prakash and Raja are from the same state and do the same job.</li>"
 "<li>Tarun is the only cook from his state.</li>"
 "<li>Dhanush is the only tent-pitcher from his state.</li>"
 "<li>Mansi and Neha do the same job.</li>"
 "<li>Aakash and Chitra are from different states.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Shape", p("5 cooks and 4 tent-pitchers. With at least one of each per state, two states have 2 cooks + 1 tent-pitcher and one state has 1 cook + 2 tent-pitchers.")),
       ("Tarun and Dhanush", p("Tarun’s state is the 1 cook + 2 tents state; call it Y. Dhanush’s state has only one tent-pitcher, so it is a 2 + 1 state; call it Z, and the third state X.")),
       ("Prakash and Raja", p("Aakash, Biva and Neha put one person in every state. If Prakash and Raja pitched tents they would fill Y with Tarun; if they cooked in Z they would fill Z with Dhanush. Either way that state would have no room for Aakash, Biva or Neha. So they are X’s two cooks, and X’s third member is a tent-pitcher.")),
       ("Everyone else", p("Aakash and Biva are in different states but do the same job. Only Z has two free cook places, both in one state, so they both pitch tents: one fills X’s place and the other is in Y. Neha is then in Z and cooks, and Mansi cooks with her, also in Z. Chitra takes the last place in Y; she is not with Aakash, so Aakash is in X and Biva in Y.") + GRP)) +
 final("Groups and jobs fixed; which state is X, Y or Z is not."),
 p("Count the cooks and tent-pitchers per state first: the 2–1 / 2–1 / 1–2 shape does most of the work."),
 p("<b>Frameworks:</b> fix the shape of the answer from the totals, then place people into it."))
P.dq(19, "Which three friends are from the same state?", ["Dhanush, Mansi, Neha", "Biva, Prakash, Raja", "Chitra, Prakash, Raja", "None of these"], "MCQ", "1", "Easy",
 "Use the grouping.",
 steps(("Groups", p("{Aakash, Prakash, Raja}, {Biva, Chitra, Tarun}, {Dhanush, Mansi, Neha}."))) + final("Option 1"),
 [("2", "Biva is with Tarun."), ("3", "Chitra is with Tarun."), ("4", "Option 1 works.")])
P.dq(20, "For how many of the friends can the job be determined?", ["6", "7", "8", "9"], "MCQ", "4", "Easy",
 "Every job is fixed.",
 steps(("Jobs", p("Cooks: Mansi, Neha, Prakash, Raja, Tarun. Tents: Aakash, Biva, Chitra, Dhanush."))) + final("Option 4"),
 [("1", "Every job is fixed."), ("2", "Every job is fixed."), ("3", "Every job is fixed.")])
P.dq(21, "Which statements together are enough to fix the state of all nine friends?<br>I. Two people from Madhya Pradesh pitch tents.<br>II. Two people from Jharkhand cook, and Raja is not one of them.<br>III. Only one person from Chhattisgarh pitches tents, and it is not Dhanush.", ["I and II", "I and III", "II and III", "Any two of them"], "MCQ", "4", "Medium",
 "Each statement names one group.",
 steps(("Each alone", p("I: Y is Madhya Pradesh. II: two cooks, not Raja, means Z is Jharkhand. III: one tent-pitcher, not Dhanush, means X is Chhattisgarh.")),
       ("Pairs", p("Any two name two groups, and the third state is left for the third group."))) + final("Option 4"),
 [("1", "Works, but so do the others."), ("2", "Works, but so do the others."), ("3", "Works, but so do the others.")])
P.dq(22, "Biva, Chitra, Mansi and Neha are the only girls in the group. Which of these could be the number of girls from each state?", ["Chhattisgarh 0, Jharkhand 1, Madhya Pradesh 3", "Chhattisgarh 0, Jharkhand 2, Madhya Pradesh 2", "Chhattisgarh 1, Jharkhand 1, Madhya Pradesh 2", "Cannot be determined"], "MCQ", "2", "Easy",
 "Biva and Chitra are together; so are Mansi and Neha.",
 steps(("Split", p("The girls go 2, 2 and 0 by group. Only option 2 has that shape, with Y and Z being Jharkhand and Madhya Pradesh in some order."))) + final("Option 2"),
 [("1", "No state has three girls."), ("3", "No state has exactly one girl."), ("4", "Option 2 is possible.")])
