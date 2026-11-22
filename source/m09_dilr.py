# -*- coding: utf-8 -*-
# Simp Mock 9: DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m09 import P
import m09_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Cinema seats (Q1–5) ----------------
SEATED = table(["Friend", "Seat", "Type"], [["Ajay", "C-2", "Premium"], ["Hetal", "C-8", "Prime"], ["Girish", "C-9", "Premium"], ["Indra", "C-10", "Ordinary"],
                                           ["Elina", "B-2", "Special"], ["Falguni", "E-3 or E-4", "Prime"], ["Biva", "E-8", "Prime"], ["Chanchal", "E-9", "Premium"], ["Deb", "F-8", "Special"]])
P.dilr_set(1, "Set 1 — Nine friends at the movies", DIR,
 p("Nine friends — Ajay, Biva, Chanchal, Deb, Elina, Falguni, Girish, Hetal and Indra — spent ₹2600 in all on movie tickets. The hall has 70 seats in seven rows of 10. Rows are lettered A to G from the back to the front (the screen). In each row, columns 1–5 are left of the aisle and 6–10 right of it; a seat is named by row and column, e.g. B-6. Two seats on opposite sides of the aisle are not adjacent. There are five seat types: Luxury ₹500, Prime ₹400, Premium ₹300, Special ₹200 and Ordinary ₹100. The plan is shown below; all directions are as seen facing the screen.") + F.SEATS +
 "<ol><li>The friends sat in four different rows. Exactly two of them sat alone in their rows.</li>"
 "<li>Ajay, Hetal, Girish and Indra sat in the same row, in that order from left to right, in seats of three different types.</li>"
 "<li>Ajay and Elina sat in the same column in adjacent rows, Ajay in front.</li>"
 "<li>Hetal’s and Falguni’s seats cost the same.</li>"
 "<li>Chanchal sat to the right of Falguni in the same row, and that row has Ordinary seats.</li>"
 "<li>Chanchal’s, Girish’s and Ajay’s seats cost the same.</li>"
 "<li>Biva’s and Hetal’s seats cost the same, and are in the same column with one row between them.</li>"
 "<li>Hetal, Girish and Indra were the only three friends in three consecutive seats.</li>"
 "<li>The seat immediately to the left of Deb’s cost more than his.</li>"
 "<li>The seat directly in front of Biva’s is of a different price from hers.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Hetal, Girish, Indra", p("They are adjacent with three different types, and Ajay further left matches Girish. Runs of three types: C-2–4, C-8–10, E-8–10. E-8–10 has no Premium seat to its left for Ajay. C-2–4 (Hetal at C-2, Premium) fails clue 7: no Premium two rows away in column 2. So Hetal C-8, Girish C-9, Indra C-10; Ajay is the only Premium left of them, C-2.")),
       ("Elina and Biva", p("Elina sits behind Ajay: B-2. Biva is Prime two rows from C-8: E-8 (A-8 is Luxury); F-8 in front is Special, so clue 10 holds.")),
       ("Prices", p("Falguni Prime (₹400), Chanchal Premium (₹300). Deb pays 2600 − (300 + 400 + 300 + 100 + 200 + 400 + 400 + 300) = ₹200.")),
       ("Falguni and Chanchal", p("A Prime seat with a Premium seat to its right, in a row with Ordinary seats: only row E. Chanchal is E-9; Falguni is E-3 or E-4.")),
       ("Deb", p("A Special seat with a costlier seat on its immediate left: B-9, C-3, E-5 or F-8. Rows B, C and E are already used, and Deb must be alone in a fourth row: F-8.")),
       ("Seats", SEATED)) +
 final("All fixed except Falguni (E-3 or E-4)."),
 p("Begin with the clue that pins a run of seats to the plan, then let prices fix the rest."),
 p("<b>Seat-plan puzzles:</b> scan the plan for patterns the clues need (three types in a row, equal prices one row apart) before trying names."))
P.dq(1, "What type of seat did Deb have?", ["Luxury", "Prime", "Premium", "Special"], "MCQ", "4", "Hard",
 "Deb’s price comes from the total.",
 steps(("Seat", p("F-8, a Special seat."))) + final("Option 4"),
 [("1", "Row A only."), ("2", "Falguni’s type."), ("3", "Ajay’s type.")])
P.dq(2, "For how many of the nine friends can the seat be fixed exactly?", ["All of them", "All but one", "Seven", "Six"], "MCQ", "2", "Hard",
 "Only one friend has a choice.",
 steps(("Count", p("Falguni is E-3 or E-4; the other eight are fixed."))) + final("Option 2"),
 [("1", "Falguni has two seats."), ("3", "Too few."), ("4", "Too few.")])
P.dq(3, "Whose seat cost the most among these four?", ["Deb", "Elina", "Indra", "Girish"], "MCQ", "4", "Hard",
 "Compare prices.",
 steps(("Prices", p("Deb ₹200, Elina ₹200, Indra ₹100, Girish ₹300."))) + final("Option 4"),
 [("1", "₹200."), ("2", "₹200."), ("3", "₹100.")])
P.dq(4, "What was the total price (in ₹) of the seats of the friends in Falguni’s row?", [], "TITA", "1100", "Hard",
 "Row E has Falguni, Biva and Chanchal.",
 steps(("Add", p("400 + 400 + 300 = 1100."))) + final("1100"))
P.dq(5, "Who had the cheapest seat of the nine?", ["Biva", "Deb", "Elina", "Indra"], "MCQ", "4", "Hard",
 "Only one ₹100 seat.",
 steps(("Read", p("Indra, C-10, ₹100."))) + final("Option 4"),
 [("1", "₹400."), ("2", "₹200."), ("3", "₹200.")])

# ---------------- Set 2: Board marks (Q6–10) ----------------
POSS = p("Girija: (a) 54, 78, 85, 93 or (b) 60, 72, 85, 93. Each set below is B, C, P, M.") + table(["#", "G", "Charu", "Vaibhav"], [
 ["1", "a", "36 42 48 84", "30 60 66 72"],
 ["2", "a", "30 48 60 72", "36 42 66 84"],
 ["3", "a", "30 42 66 72", "36 48 60 84"],
 ["4", "b", "36 42 48 84", "30 54 66 78"],
 ["5", "b", "30 48 54 78", "36 42 66 84"],
 ["6", "b", "30 36 66 78", "42 48 54 84"]])
P.dilr_set(2, "Set 2 — Three students’ board marks", DIR,
 p("Three students, Girija, Charu and Vaibhav, compare their board marks in four subjects: Biology, Chemistry, Physics and Mathematics. Each subject is out of 100 and all marks are whole numbers.") +
 "<ul><li>Each student scored lowest in Biology and highest in Mathematics, and more in Physics than in Chemistry.</li>"
 "<li>For each student, the gap between the highest and lowest mark is at most 48.</li>"
 "<li>The twelve marks, in ascending order, are 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 85 and 93.</li>"
 "<li>Girija’s total is 310 and Vaibhav’s is 228. Girija scored at least 50 in every subject.</li></ul>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("Charu’s total", p("All twelve add to 748, so Charu has 748 − 310 − 228 = 210.")),
       ("Girija", p("Ten marks are multiples of 6; 85 and 93 are not. 210 and 228 are multiples of 6, 310 is not, so Girija has 85 and 93 (Physics and Maths). Her other two add to 132, each at least 50: 54 + 78 or 60 + 72.")),
       ("The rest", p("Split the remaining eight into Charu (210) and Vaibhav (228), each with a gap of at most 48. Marks in each set sort as B < C < P < M.")),
       ("All six cases (B, C, P, M)", POSS)) +
 final("Six complete possibilities."),
 p("Use divisibility to find who has the odd marks out, then enumerate."),
 p("<b>Sorted data with totals:</b> check divisibility of totals — it often places the ‘irregular’ values at once."))
P.dq(6, "In how many ways can all twelve marks be assigned to students and subjects?", ["3", "6", "9", "18"], "MCQ", "2", "Hard",
 "Count the table rows.",
 steps(("Count", p("Three for each of Girija’s two options: 6."))) + final("Option 2"),
 [("1", "One Girija option only."), ("3", "Not a product of choices."), ("4", "Counts orders within a set.")])
P.dq(7, "Whose set of four marks can be chosen in the most ways?", ["Girija", "Charu", "Vaibhav", "Charu and Vaibhav equally"], "MCQ", "4", "Hard",
 "Count different sets per student.",
 steps(("Count", p("Girija 2; Charu 5 (rows 1 and 4 match); Vaibhav 5 (rows 2 and 5 match)."))) + final("Option 4"),
 [("1", "Only 2."), ("2", "Ties with Vaibhav."), ("3", "Ties with Charu.")])
P.dq(8, "What is the lowest possible Mathematics mark for any of them?", ["60", "66", "72", "78"], "MCQ", "3", "Hard",
 "Look at the last mark in each set.",
 steps(("Read", p("Maths marks seen: 72, 78, 84, 93. Lowest 72."))) + final("Option 3"),
 [("1", "Never a highest mark."), ("2", "Never a highest mark."), ("4", "72 occurs.")])
P.dq(9, "Who could have scored the lowest possible Chemistry mark?", ["Girija", "Charu", "Vaibhav", "More than one of them"], "MCQ", "2", "Hard",
 "Chemistry is the second mark in each set.",
 steps(("Read", p("The lowest Chemistry mark is 36, only in row 6 for Charu."))) + final("Option 2"),
 [("1", "At least 72."), ("3", "At least 42."), ("4", "Only Charu.")])
P.dq(10, "Write out all six possibilities. For each subject, count how many times each mark appears in that subject across all students in all six. How many (subject, mark) pairs appear exactly once?", ["1", "2", "3", "4"], "MCQ", "4", "Hard",
 "Tally each column.",
 steps(("Tally", p("Biology: 42 once. Chemistry: 36, 54, 60 once each. Physics and Maths: none.")),
       ("Total", p("4."))) + final("Option 4"),
 [("1", "Biology only."), ("2", "Too few."), ("3", "Chemistry only.")])

# ---------------- Set 3: Ten films in ten days (Q11–15) ----------------
FILMS = table(["Language", "Sub-category", "Films"], [["Hindi", "Feature", "3"], ["Hindi", "Documentary", "1"], ["English", "Indian", "1"], ["English", "International", "2"],
                                                     ["Regional", "Bengali", "1"], ["Regional", "Non-Bengali", "2"]]) + p("The two Non-Bengali films are one Tamil and one Marathi film.")
SCHED = table(["Date", "Film", "Date", "Film"], [["1", "EX", "6", "NB"], ["2", "B", "7", "HF"], ["3", "HF", "8", "EX or NB"],
                                                 ["4", "EI", "9", "HF"], ["5", "HD", "10", "NB or EX"]]) + p("HF/HD = Hindi Feature/Documentary, EI/EX = English Indian/International, B = Bengali, NB = Non-Bengali.")
P.dilr_set(3, "Set 3 — A ten-day film festival", DIR,
 p("A cinema hall will screen ten films, one a day, from 1 to 10 December during a film festival. The ten films are:") + FILMS +
 p("A friend who knows the schedule says:") +
 "<ol><li>Films on odd dates are in Hindi or English.</li><li>Films on even dates are in English or a regional language.</li>"
 "<li>Films on dates that are multiples of 3 are in Hindi or a regional language.</li><li>The films from 1st to 6th cover all six sub-categories.</li>"
 "<li>Every Non-Bengali film comes the day after a Hindi film.</li><li>The film on the 6th is not Bengali.</li>"
 "<li>A Hindi Feature film, the English Indian film and the Hindi Documentary are shown on three consecutive days, in that order.</li>"
 "<li>The film on the 4th is not English International.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Languages by date", p("3 and 9: Hindi. 6: regional. 1, 5, 7: Hindi or English. 2, 4, 8, 10: English or regional.")),
       ("The 6th", p("Regional, not Bengali: Non-Bengali, so the 5th is Hindi.")),
       ("The run of three", p("The middle day is an even date allowing English, with Hindi on both sides: 1-2-3, 3-4-5 or 7-8-9. 7-8-9 puts two sub-categories after the 6th (clue 4). 1-2-3 leaves only the 4th for both English International and Bengali, since the 5th must be Hindi. So 3-4-5: 4th English Indian, 5th Hindi Documentary.")),
       ("1st and 2nd", p("1–6 must include English International and Bengali: the 1st is English International, the 2nd Bengali.")),
       ("7th to 10th", p("Left: two Hindi Features, one English International, one Non-Bengali. 7th and 9th are Hindi Feature; the 8th and 10th take the other two either way (each Non-Bengali follows a Hindi film).")),
       ("Schedule", SCHED)) +
 final("Two schedules, differing on the 8th and 10th."),
 p("Turn the date rules into a language grid first; it leaves very few choices."),
 p("<b>Calendar puzzles:</b> overlapping divisibility rules (odd, even, multiple of 3) fix some dates outright."))
P.dq(11, "What is the largest possible gap (in days, not counting the screening dates) between two consecutive English films?", [], "TITA", "5", "Medium",
 "English films: 1st, 4th and two of the last four days.",
 steps(("Case", p("If the 10th is English International (8th Non-Bengali), the English films are on 1, 4 and 10: a gap of 5 days (5th to 9th)."))) + final("5"))
P.dq(12, "Which film is shown on 10 December?", ["Non-Bengali", "Hindi Feature", "English International", "Non-Bengali or English International"], "MCQ", "4", "Medium",
 "The 8th and 10th can swap.",
 steps(("Read", p("Either Non-Bengali or English International."))) + final("Option 4"),
 [("1", "Not certain."), ("2", "The 9th."), ("3", "Not certain.")])
P.dq(13, "On which date can the Tamil film NOT be shown?", ["2 December", "6 December", "8 December", "10 December"], "MCQ", "1", "Medium",
 "Where are the Non-Bengali films?",
 steps(("Read", p("Non-Bengali films are on the 6th and on the 8th or 10th. The 2nd is Bengali."))) + final("Option 1"),
 [("2", "Possible."), ("3", "Possible."), ("4", "Possible.")])
P.dq(14, "Three of the four Hindi films, ‘Dhoop’, ‘Saaya’ and ‘Kinara’, are shown in that order with no Hindi film between them. Which may be the Hindi Documentary?", ["Dhoop", "Saaya", "Saaya or Kinara", "Dhoop or Saaya"], "MCQ", "4", "Medium",
 "Hindi films: 3rd (Feature), 5th (Doc), 7th, 9th (Feature).",
 steps(("Runs of three", p("3-5-7: the Documentary is second. 5-7-9: it is first.")),
       ("Answer", p("Dhoop or Saaya."))) + final("Option 4"),
 [("1", "Saaya also possible."), ("2", "Dhoop also possible."), ("3", "Kinara would be last, never the Documentary.")])
P.dq(15, "Which of the following can be true?", ["An English film comes right after a Hindi Feature film on three occasions.", "The Marathi film comes right after, and right before, a Hindi Feature film.", "The Hindi Documentary is followed the next day by a Bengali film.", "The English Indian film is followed the next day by a Hindi Feature film."], "MCQ", "2", "Medium",
 "Check each against the schedule.",
 steps(("Option 2", p("If the Marathi film is on the 8th, it sits between the Hindi Features on the 7th and 9th.")),
       ("Others", p("Only two English films follow a Hindi Feature (4th, and 8th or 10th). The 6th is Non-Bengali. The 5th, after the English Indian film, is the Documentary."))) + final("Option 2"),
 [("1", "Only two."), ("3", "The 6th is Non-Bengali."), ("4", "The 5th is the Documentary.")])

# ---------------- Set 4: A consultancy’s staff (Q16–20) ----------------
STAFF = table(["Office", "M", "F", "Mgr", "Exec"], [["Mumbai", "252", "108", "54", "306"], ["Chennai", "99", "81", "54", "126"],
                                                  ["Bhub.", "24", "36", "12", "48"], ["Total", "375", "225", "120", "480"]])
P.dilr_set(4, "Set 4 — Staff of a consultancy", DIR,
 p("A consultancy firm has 600 employees in three offices: Mumbai, Chennai and Bhubaneswar. Each employee is male or female, and either a Manager or an Executive.") +
 "<ul><li>The Bhubaneswar office has 10% of the staff; the Mumbai office has 500% more employees than Bhubaneswar.</li>"
 "<li>Men are 40% of the Bhubaneswar office and 55% of the Chennai office.</li>"
 "<li>In Chennai, 3 in every 10 employees are Managers; in Mumbai, 3 in every 20.</li>"
 "<li>Across the firm, 37.5% of employees are women and four-fifths are Executives.</li></ul>",
 "DILR::DI::Caselets",
 steps(("Offices", p("Bhubaneswar 60, Mumbai 6 × 60 = 360, Chennai 180.")),
       ("Gender", p("Women 225 in all. Bhubaneswar 24 M, 36 F; Chennai 99 M, 81 F; Mumbai 252 M, 108 F.")),
       ("Roles", p("Managers 120 in all. Chennai 54, Mumbai 54, Bhubaneswar 12.")),
       ("Summary (M = male, F = female)", STAFF)) +
 final("Office totals fixed; the gender–role split inside each office is open."),
 p("Get office sizes first; every other figure is a percentage of one of them."),
 p("<b>Two independent splits:</b> knowing male/female and manager/executive totals does not fix the cross-cells — only bounds them."))
P.dq(16, "How many Managers work in the Chennai office?", [], "TITA", "54", "Easy",
 "30% of 180.",
 steps(("Compute", p("0.3 × 180 = 54."))) + final("54"))
P.dq(17, "If half of the Bhubaneswar Managers are men, male Executives in Bhubaneswar are what percentage of all the firm’s Executives?", ["37.5", "25", "12.5", "3.75"], "MCQ", "4", "Easy",
 "24 men, 6 of them Managers.",
 steps(("Count", p("Male Executives in Bhubaneswar: 24 − 6 = 18.")),
       ("Percent", p("18 ÷ 480 = 3.75%."))) + final("Option 4"),
 [("1", "Share of women."), ("2", "Wrong base."), ("3", "Wrong base.")])
P.dq(18, "What is the smallest possible number of male Executives in the Chennai office?", [], "TITA", "45", "Easy",
 "Put as many women as possible among the Executives.",
 steps(("Compute", p("126 Executives; at most 81 are women; so at least 45 are men."))) + final("45"))
P.dq(19, "Which of these is a perfect square?", ["Largest possible number of female Executives in Mumbai", "Largest possible number of female Managers in Bhubaneswar", "Largest possible number of female Executives in Chennai", "Largest possible number of female Managers in Mumbai"], "MCQ", "3", "Easy",
 "Each maximum is the smaller of two totals.",
 steps(("Values", p("108, 12, 81 and 54. Only 81 is a square."))) + final("Option 3"),
 [("1", "108."), ("2", "12."), ("4", "54.")])
P.dq(20, r"If \(17\tfrac{11}{17}\%\) of Mumbai’s Executives are women, how many Mumbai Executives are men?", [], "TITA", "252", "Easy",
 r"\(17\tfrac{11}{17}\% = \tfrac{300}{17}\%\).",
 steps(("Women", p("306 × 300 ÷ 1700 = 54.")),
       ("Men", p("306 − 54 = 252."))) + final("252"))
