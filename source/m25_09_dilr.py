# -*- coding: utf-8 -*-
# Simp Mock 9 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_09 import P
import m25_09_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Scholarships (Q1–4) ----------------
YEARS = table(["Year", "Total", "Applied", "Awarded"], [["2021", "96000", "67200", "43680"], ["2022", "108000", "86400", "60480"], ["2023", "129600", "64800", "55080"], ["2024", "121500", "91125", "36450"], ["2025", "133650", "26730", "16038"]])
P.dilr_set(1, "Set 1 — Scholarships over five years", DIR,
 p("In the engineering colleges across the state of Rajasthan, students fall into two categories based on their living arrangements: resident students, who stay in hostels on campus, and day scholars, who commute from home. The state government supports meritorious students with scholarships.") +
 p("The charts below cover 2021 to 2025: the percentage of resident students among all students, the percentage of all students who applied for scholarships, and the percentage of applicants who were awarded one.") +
 p("<b>Resident students (% of all students)</b>") + F.RES + p("<b>Applied for a scholarship (% of all students)</b>") + F.APP + p("<b>Awarded a scholarship (% of applicants)</b>") + F.GOT +
 p("Further: in 2022 the total number of students rose by 12.5% over 2021; in 2023 it rose by 20% over 2022; in 2024 it fell by 6.25% from 2023; and in 2025 it rose by 10% over 2024. There were 96,000 students in 2021."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Totals", p(r"96,000 → ×1.125 → 1,08,000 → ×1.2 → 1,29,600 → ×0.9375 → 1,21,500 → ×1.1 → 1,33,650.")),
       ("Applied and awarded", YEARS),
       ("Day scholars", p("100% minus residents: 40%, 60%, 40%, 50%, 50% of the totals: 38,400; 64,800; 51,840; 60,750; 66,825."))) +
 final("Every count follows from the totals and the three percentages."),
 p("Build the yearly totals first; everything else is a percentage of them."),
 p("<b>Chained percentages:</b> apply each change to the previous year, not to 2021."))
P.dq(1, "In which year was the number of day scholars the highest?", ["2022", "2023", "2024", "2025"], "MCQ", "4", "Easy",
 "Day scholars = (100 − resident %) × total.", steps(("Compare", p("2025: 50% of 1,33,650 = 66,825, ahead of 2022’s 64,800."))) + final("2025, option 4"),
 [("1", "64,800."), ("2", "51,840."), ("3", "60,750.")])
P.dq(2, "How many students got scholarships in 2024?", ["43680", "54675", "36450", "55080"], "MCQ", "3", "Easy",
 "1,21,500 × 75% × 40%.", steps(("2024", p("91,125 applied; 40% of them = 36,450."))) + final("Option 3"),
 [("1", "2021’s figure."), ("2", "60% instead of 40%."), ("4", "2023’s figure.")])
P.dq(3, "Let A be the number of students who got scholarships in 2023, and B the number who applied but did not get one in 2023. What is A − B?", ["36450", "25920", "40405", "45360"], "MCQ", "4", "Easy",
 "64,800 applied; 85% got one.", steps(("2023", p("A = 55,080, B = 9,720. A − B = 45,360."))) + final("Option 4"),
 [("1", "Wrong year."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])
P.dq(4, "What was the average number of students who applied for scholarships from 2021 to 2025?", ["67251", "67200", "64800", "65721"], "MCQ", "1", "Medium",
 "Add the five applicant counts.", steps(("Average", p("(67,200 + 86,400 + 64,800 + 91,125 + 26,730) ÷ 5 = 3,36,255 ÷ 5 = 67,251."))) + final("Option 1"),
 [("2", "2021 only."), ("3", "2023 only."), ("4", "Digits swapped.")])

# ---------------- Set 2: Six batsmen (Q5–8) ----------------
BAT = table(["Name", "Surname", "Runs", "Order"], [["Yuvan", "Pandey", "52", "1"], ["Sameer", "Grewal", "56", "2"], ["Arjun", "Sharma", "48", "3 / 4"], ["Nikhil", "Joshi", "58", "4 / 3"], ["Shiv", "Rao / Sethi", "54", "5"], ["Rohan", "Sethi / Rao", "60", "6"]])
P.dilr_set(2, "Set 2 — Six batsmen", DIR,
 p("Six cricketers, Arjun, Yuvan, Shiv, Sameer, Nikhil and Rohan, have the surnames Sharma, Pandey, Joshi, Grewal, Rao and Sethi (not necessarily in that order). In a match, each scored a different number of runs: 48, 52, 54, 56, 58 and 60 (not necessarily in that order).") +
 p("After the match, this conversation took place in the dressing room:") +
 "<ul><li>Sameer (to everyone): “My surname is Grewal. I batted second and scored 56 runs.”</li><li>Shiv (talking to Joshi): “I scored 54 runs, and I batted fifth.”</li><li>Arjun (talking to Rohan): “My surname is Sharma. I scored 48 runs, and I batted after Sameer, not necessarily immediately after him. By the way, Rohan, you once told Pandey that you batted sixth and scored 60 runs.”</li><li>Yuvan (thinking to himself): “My surname isn’t Joshi. I know that Nikhil batted after me, not necessarily immediately.”</li><li>Pandey (announcing): “I scored 52 runs.”</li><li>Nikhil (reflecting): “At least two batsmen scored fewer runs than me.”</li><li>Joshi (quietly to himself): “I didn’t score the most runs.”</li></ul>" +
 p("Everything said is true, and a person who speaks to someone is a different person from that someone."),
 "DILR::LR::Puzzles",
 steps(("Runs", p("Sameer 56, Shiv 54, Arjun 48, Rohan 60. Yuvan and Nikhil share 52 and 58; Nikhil needs two below him, so he has 58 and Yuvan 52.")),
       ("Surnames", p("Pandey scored 52: Yuvan. Joshi isn’t Yuvan, Shiv (who speaks to Joshi), Sameer, Arjun, or the top scorer Rohan: Nikhil is Joshi. Shiv and Rohan are Rao and Sethi in some order.")),
       ("Order", p("Sameer 2, Shiv 5, Rohan 6. Arjun bats after Sameer and Nikhil after Yuvan, so Yuvan is first and Arjun and Nikhil take 3 and 4.")),
       ("Result", BAT)) +
 final("Runs are fixed; two surnames and two batting places are open."),
 p("Start with the runs (four are stated), then let ‘talking to’ rule people out of surnames."),
 p("<b>Conversation puzzles:</b> a speaker addressing X is not X."))
P.dq(5, "How many runs did Yuvan score?", [], "TITA", "52", "Easy",
 "Nikhil needs two scores below his.", steps(("Yuvan", p("52."))) + final("52"))
P.dq(6, "What best can be said about Arjun’s batting order?", ["He definitely batted 3rd.", "He batted 4th.", "He definitely did not bat 3rd.", "He definitely batted either 3rd or 4th."], "MCQ", "4", "Medium",
 "Places 3 and 4 go to Arjun and Nikhil.", steps(("Arjun", p("3rd or 4th; either is possible."))) + final("Option 4"),
 [("1", "Could be 4th."), ("2", "Could be 3rd."), ("3", "He could bat 3rd.")])
P.dq(7, "For how many players can the surname be determined uniquely?", [], "TITA", "4", "Medium",
 "Shiv and Rohan share Rao and Sethi.", steps(("Count", p("Sameer, Arjun, Yuvan, Nikhil: 4."))) + final("4"))
P.dq(8, "How many runs did Joshi score?", [], "TITA", "58", "Easy",
 "Joshi is Nikhil.", steps(("Joshi", p("58."))) + final("58"))

# ---------------- Set 3: Metro passengers (Q9–13) ----------------
CASES = table(["", "b", "c", "e", "f", "g", "h", "i"], [["1", "7", "10", "8", "5", "2", "9", "3"], ["2", "8", "9", "7", "5", "3", "10", "2"], ["3", "10", "7", "5", "8", "2", "9", "3"]])
P.dilr_set(3, "Set 3 — Metro passengers", DIR,
 p("Austin, Baltimore, Christchurch, Denver and East Windsor are five metro stations, in that order, on a city metro line. The UP service runs from Austin to East Windsor; the DOWN service runs the opposite way.") +
 p("On a particular day, 55 scientists travelled on the UP service from various stations, as shown below. Rows are boarding stations and columns are alighting stations; a, b, c, d, e, f, g, h, i and j are ten distinct natural numbers from 1 to 10. The totals refer to the non-blank cells in each row or column.") + F.METRO +
 p("For example, a is the number of scientists who boarded at Austin and got off at Baltimore."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("Fixed", p("Baltimore column: a = 4. Denver row: j = 6. East Windsor column: d + g + i = 6, so d, g, i are 1, 2, 3.")),
       ("h and i", p("h + i = 12 with i ≤ 3: (h, i) = (10, 2) or (9, 3). Christchurch column: b + e = 15. Denver column: c + f = 24 − h = 14 or 15.")),
       ("Left over", p("Remaining numbers for b, c, e, f: 5, 7, 8 and whichever of 9, 10 h didn’t take. Austin row: b + c + d = 18.")),
       ("Three cases", CASES + p("In all three, a = 4, d = 1, j = 6."))) +
 final("Three valid tables; only a, d and j are fixed."),
 p("The single-cell row and column (j and a) are free; then 1, 2, 3 are forced into the East Windsor column."),
 p("<b>Distinct-digit grids:</b> small sums pin the smallest numbers first."))
P.dq(9, "How many different sets of values of a to j are possible?", [], "TITA", "3", "Hard",
 "Branch on h = 9 or 10.", steps(("Count", p("Three, as tabulated."))) + final("3"))
P.dq(10, "Consider the numbers 5, 6, 7 and 8. How many of them can be the number of scientists who boarded at Baltimore and got off at Denver?", ["1", "2", "3", "4"], "MCQ", "2", "Medium",
 "That is f.", steps(("f", p("f is 5, 5 or 8 across the cases: 5 and 8."))) + final("2, option 2"),
 [("1", "Both 5 and 8 occur."), ("3", "6 is j and 7 never occurs as f."), ("4", "6 and 7 don’t occur.")])
P.dq(11, "With which station is the number 9 definitely associated (as the number of scientists boarding there for one destination, or alighting there from one origin)?", ["Austin", "Christchurch", "Denver", "None of these"], "MCQ", "3", "Medium",
 "Where is 9 in each case?",
 steps(("Each case", p("Cases 1 and 3: h = 9 (Christchurch → Denver). Case 2: c = 9 (Austin → Denver). Denver appears every time."))) + final("Denver, option 3"),
 [("1", "Only in case 2."), ("2", "Not in case 2."), ("4", "Denver always.")])
P.dq(12, "Of the ten numbers a to j, how many can be determined uniquely?", [], "TITA", "3", "Medium",
 "Compare the three cases.", steps(("Fixed", p("a = 4, d = 1, j = 6."))) + final("3"))
P.dq(13, "If g = 2, what is h?", [], "TITA", "9", "Easy",
 "Cases 1 and 3 have g = 2.", steps(("h", p("9 in both."))) + final("9"))

# ---------------- Set 4: Coloured darts (Q14–17) ----------------
P.dilr_set(4, "Set 4 — A coloured dartboard", DIR,
 p("Vivek made a square dartboard with a 5 × 5 grid. Of the 25 squares, 12 are black, 12 are white, and the central square is red. The rules:") +
 "<ul><li>A player gets 8 throws in a game.</li><li>Hitting a black, a white or the red square earns 1, 2 or 5 points.</li><li>A dart on a border line or common corner of squares, or off the board, earns nothing.</li><li>Hitting squares of the same colour on consecutive throws earns 1 extra point for each such consecutive pair. For example, two blacks in a row earn 1 + 1 + 1 = 3; three whites in a row earn 2 + 2 + 2 + 1 + 1 = 8; four whites in a row earn 2 + 2 + 2 + 2 + 1 + 1 + 1 = 11.</li></ul>",
 "DILR::LR::Games_and_Tournaments",
 steps(("Scoring", p("A game is a string of 8 colours. Score = face points + one point for each adjacent pair of the same colour.")),
       ("Counting", p("Each question fixes the colours used, so count arrangements of the string."))) +
 final("Count colour strings that meet each condition."),
 p("Treat a run that must stay together as one block."),
 p("<b>Arrangements with blocks:</b> glue the block, arrange the units, then subtract the unwanted patterns."))
P.dq(14, "In a game, a player earned points on every throw: black 3 times, white 4 times and red once. All the whites were on consecutive throws. In how many ways can the colours have come, given that the player scored at least 20 points?", ["16", "20", "18", "19"], "MCQ", "3", "Medium",
 "Base score with the white block: 3 + 8 + 5 + 3 = 19. One more point needs two blacks together.",
 steps(("All with the block", p(r"Units: [WWWW], R, B, B, B: \(\tfrac{5!}{3!} = 20\).")),
       ("No two blacks together", p("Arrange the block and R (2 ways); the three blacks then fill the three gaps, one each: 2 strings.")),
       ("Answer", p("20 − 2 = 18."))) + final("18, option 3"),
 [("1", "Over-subtracts."), ("2", "Doesn’t subtract."), ("4", "Subtracts one.")])
P.dq(15, "In the situation of the previous question (black 3, white 4 together, red once, at least 20 points), in how many ways can the red hit come in one of the last three throws?", [], "TITA", "8", "Medium",
 "Count by red’s position: 8th, 7th or 6th.",
 steps(("Red 8th", p("Arrange [WWWW], B, B, B with two blacks together: 4 ways.")),
       ("Red 7th", p("Throw 8 must be black: arrange the block and two blacks: 2 ways (the blacks together).")),
       ("Red 6th", p("Throws 7 and 8 are black (already together): block and one black: 2 ways.")),
       ("Total", p("4 + 2 + 2 = 8."))) + final("8"))
P.dq(16, "In a game, a player earned points on every throw: black exactly twice and red once. In how many ways can the colours have come, given that the player scored the least possible number of points?", ["8", "9", "10", "12"], "MCQ", "4", "Hard",
 "The other five throws are white; avoid same-colour neighbours as far as possible.",
 steps(("Least score", p("Face points: 2 + 5 + 10 = 17. Five whites and three other hits can’t all be kept apart, so at least one pair of whites touches: the least score is 18.")),
       ("Count", p("For exactly one white pair and no black pair, whites take both ends. The five whites leave four gaps; put B, B and R into three of them, one per gap, and leave one gap empty (that is the white pair). Empty gap: 4 ways; order of B, B, R: 3 ways. 4 × 3 = 12."))) + final("12, option 4"),
 [("1", "Misses arrangements."), ("2", "Misses arrangements."), ("3", "Misses arrangements.")])
P.dq(17, "In the situation of the previous question (black twice, red once, least possible score), let N be the throw on which black was first hit. What is the largest possible N?", [], "TITA", "5", "Medium",
 "Fill as much as possible before the first black.",
 steps(("Latest", p("W W R W B W B W (or W R W W B W B W): the first black is the 5th throw; later would force two blacks or three whites together."))) + final("5"))

# ---------------- Set 5: Quiz teams (Q18–22) ----------------
SEATS = table(["Seat", "Who", "Subject", "Team"], [["1", "P", "Math", "Gamma"], ["2", "R", "Sci", "Gamma"], ["3", "B", "Econ", "Gamma"], ["4", "C", "Math", "Delta"], ["5", "E", "Geog", "Delta"], ["6", "Q", "Econ", "Delta"], ["7", "S", "Pol", "Beta"], ["8", "A", "Sci", "Beta"], ["9", "F", "Hist", "Beta"], ["10", "U", "Pol", "Alpha"], ["11", "D", "Geog", "Alpha"], ["12", "T", "Hist", "Alpha"]])
P.dilr_set(5, "Set 5 — Quiz teams around a table", DIR,
 p("Six students, A, B, C, D, E and F, from 11th grade and six students, P, Q, R, S, T and U, from 12th grade sit around a circular table for a quiz, equally spaced and facing the centre. They form four teams, Alpha, Beta, Gamma and Delta, of exactly three students each, and each team’s three students sit together. Each student chose exactly one subject among Science, Mathematics, Economics, History, Geography and Political Science, and each subject was chosen by exactly two students.") +
 "<ol><li>Three students who chose Geography, History and Political Science sit together as a team, and it is not Team Beta.</li><li>S, who chose Political Science, sits immediately to the right of the 11th-grade student who chose Science. The two Science students sit diametrically opposite each other.</li><li>Each team has at least one student from each grade, and no two members of a team chose the same subject.</li><li>T, of Team Alpha, chose History and sits opposite Q, who chose Economics. The other History student also sits opposite the other Economics student.</li><li>P and C both chose Mathematics; exactly two students sit between them.</li><li>Each Political Science student sits between two students of different teams.</li><li>E chose Geography, belongs to Team Delta, and sits between the other two members of his team, who chose Mathematics and Economics.</li><li>A sits third to the right of D, who chose Geography.</li><li>A student of Team Alpha sits immediately to the left of a student of Team Beta.</li><li>U, who chose Political Science, is in Team Alpha.</li><li>R chose Science, belongs to Team Gamma, and sits between his teammates P and B, who chose Mathematics and Economics respectively.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Teams by subject", p("Gamma: P (Maths), R (Science), B (Economics). Delta: Maths, E (Geography), Economics. Alpha has T (History) and U (Political Science), so it is the Geography–History–Political Science team. Beta then has Science, History and Political Science; S (Political Science) sits next to the 11th-grade Science student, so S is in Beta.")),
       ("Placing", p("The Science students R and A sit opposite; Q (Economics, Delta) sits opposite T; the two Geography students E and D sit opposite. D is in Alpha, F (History) in Beta, C (Maths) in Delta.")),
       ("Seats, going clockwise (to each person’s left)", SEATS)) +
 final("Seats, subjects and teams are all fixed."),
 p("Group subjects into teams first: Gamma and Delta are almost given."),
 p("<b>Circular seating, facing in:</b> a person’s right is the next seat anticlockwise."))
P.dq(18, "Who sits diametrically opposite A?", ["C", "T", "R", "B"], "MCQ", "3", "Easy",
 "The two Science students.", steps(("Opposite", p("R (seat 2) faces A (seat 8)."))) + final("R, option 3"),
 [("1", "Seat 4."), ("2", "Seat 12."), ("4", "Seat 3.")])
P.dq(19, "Which group of students is Team Delta?", ["S - Q - E", "Q - E - D", "Q - F - A", "Q - E - C"], "MCQ", "4", "Easy",
 "E sits between the Maths and Economics students.", steps(("Delta", p("C, E, Q."))) + final("Option 4"),
 [("1", "S is in Beta."), ("2", "D is in Alpha."), ("3", "F and A are in Beta.")])
P.dq(20, "Which pair of teams each have two students from 11th grade?", ["Alpha and Beta", "Beta and Delta", "Gamma and Alpha", "Delta and Gamma"], "MCQ", "2", "Easy",
 "Count A–F in each team.", steps(("Count", p("Beta: A, F. Delta: C, E. Alpha and Gamma have one each."))) + final("Option 2"),
 [("1", "Alpha has only D."), ("3", "One each."), ("4", "Gamma has only B.")])
P.dq(21, "Which of these pairs chose the same subject and sit diametrically opposite each other?<br>(i) A and R (ii) D and E (iii) T and Q", ["Only (i)", "Only (ii)", "Only (iii)", "Both (i) and (ii)"], "MCQ", "4", "Easy",
 "Science pair and Geography pair.", steps(("Check", p("A and R (Science) and D and E (Geography) are opposite. T and Q chose different subjects."))) + final("Option 4"),
 [("1", "(ii) also works."), ("2", "(i) also works."), ("3", "Different subjects.")])
P.dq(22, "Each option is a pair of subjects. In three of them, some team has two members who chose those subjects with the second subject’s student sitting immediately to the right of the first subject’s student. Which pair is the odd one?", ["Geography, Political Science", "Science, Political Science", "Science, Mathematics", "Mathematics, Economics"], "MCQ", "4", "Hard",
 "To a seated person’s right is the next seat anticlockwise (seat number − 1).",
 steps(("Check", p("Alpha: U (Political Science) is right of D (Geography). Beta: S is right of A (Science). Gamma: P (Maths) is right of R (Science). Mathematics → Economics: in Gamma and Delta the Economics student sits to the Maths student’s left."))) + final("Option 4"),
 [("1", "Alpha fits."), ("2", "Beta fits."), ("3", "Gamma fits.")])
