# -*- coding: utf-8 -*-
# Batch 4 — CAT 2023 Slot 3: DILR sets 1–4.
from fmt import steps, final, why, table, p
from b4_s3 import P

# ---------------- Set 1: Online and offline registrations ----------------
P.dilr_set(1, "Set 1 — Online and offline registrations", "Read the instructions given and answer the questions that follow:",
 p("In a coaching class, some students register online, and some others register offline. No student registers both online and offline; hence the total registration number is the sum of online and offline registrations. The following facts and table pertain to these registration numbers for the five months – January to May of 2023. The table shows the minimum, maximum, median registration numbers of these five months, separately for online, offline and total number of registrations.") +
 table(["", "Minimum", "Maximum", "Median"], [["Online", "40", "100", "80"], ["Offline", "30", "80", "50"], ["Total", "110", "130", "120"]]) +
 p("The following additional facts are known.") +
 "<ol><li>In every month, both online and offline registration numbers were multiples of 10.</li><li>In January, the number of offline registrations was twice that of online registrations.</li><li>In April, the number of online registrations was twice that of offline registrations.</li><li>The number of online registrations in March was the same as the number of offline registrations in February.</li><li>The number of online registrations was the largest in May.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("January and April", p(r"Each total is \(3\times\) the smaller part and lies in \(110\)–\(130\), so it must be \(120\). Jan: online \(40\), offline \(80\). Apr: online \(80\), offline \(40\).")),
       ("May", p(r"Online is largest in May, so \(100\). The total is at most \(130\), so offline \(= 30\) (the minimum) and the total is \(130\).")),
       ("Offline medians", p(r"Offline values so far: \(80, 40, 30\). For a median of \(50\), Feb and Mar offline are \(50\) and some \(z \ge 50\).")),
       ("Test the two cases", p(r"<b>Mar offline = 50, Feb offline = z:</b> then Mar online \(= z\). If \(z < 80\), the online median needs Feb online \(\ge 80\), pushing Feb’s total past \(130\). If \(z = 80\), no month can total \(110\). Impossible.") +
        p(r"<b>Feb offline = 50:</b> Mar online \(= 50\). The online median of \(80\) forces Feb online \(= 80\) (below May’s \(100\), total \(130\)). Some month must total \(110\), so Mar offline \(= 60\).")),
      ) +
 table(["Month", "Online", "Offline", "Total"], [["Jan", "40", "80", "120"], ["Feb", "80", "50", "130"], ["Mar", "50", "60", "110"], ["Apr", "80", "40", "120"], ["May", "100", "30", "130"]]) +
 final("Every number is fixed."),
 p("The “twice” clues plus the 110–130 total range fix January and April at once (totals must be multiples of 30). May follows from the maximum online figure."),
 p(r"<b>Median clues:</b> once a few values are known, the median tells you whether the unknowns sit above or below it. That alone usually fixes the case."))
P.dq(1, "What was the total number of registrations in April?", [], "TITA", "120", "Easy",
 "April’s total is 3 × offline and must be between 110 and 130.", steps(("April", p(r"\(3 \times 40 = 120\)"))) + final(r"\(120\)"))
P.dq(2, "What was the number of online registrations in January?", [], "TITA", "40", "Easy",
 "January’s total is 3 × online.", steps(("January", p(r"\(3 \times \text{online} = 120 \Rightarrow 40\)"))) + final(r"\(40\)"))
P.dq(3, "Which of the following statements can be true?<br>I. The number of offline registrations was the smallest in May.<br>II. The total number of registrations was the smallest in February.", ["Only I", "Both I and II", "Neither I nor II", "Only II"],
 "MCQ", "1", "Medium", "Check May’s offline figure and February’s total in the final table.",
 steps(("Check", p(r"I: May offline \(= 30\), the minimum ✓. II: Feb total \(= 130\), the largest, so false."))) + final("Only I — option 1"),
 [("2", "February’s total is 130, not the smallest."), ("3", "Statement I is true."), ("4", "Statement II is false.")])
P.dq(4, "What best can be concluded about the number of offline registrations in February?", ["30 or 50 or 80", "50 or 80", "80", "50"],
 "MCQ", "4", "Medium", "Try Feb offline = 80 (with March offline 50). Does any month total 110?",
 steps(("Rule out 80", p(r"Then Mar online \(= 80\), Mar total \(130\), and Feb total \(= \text{Feb online} + 80\) can’t be \(110\) (online \(\ge 40\)). No month totals \(110\).")),
       ("Rule out 30", p(r"\(30\) is May’s, and May is the only month with offline \(30\)."))) + final(r"\(50\) — option 4"),
 [("1", "30 and 80 both fail."), ("2", "80 fails: no month could total 110."), ("3", "Fails for the same reason.")])
P.dq(5, "Which pair of months definitely had the same total number of registrations?<br>I. January and April<br>II. February and May", ["Only II", "Neither I nor II", "Both I and II", "Only I"],
 "MCQ", "3", "Easy", "Compare the totals in the final table.",
 steps(("Totals", p(r"Jan \(= \) Apr \(= 120\); Feb \(=\) May \(= 130\)."))) + final("Both — option 3"),
 [("1", "January and April are both 120."), ("2", "Both pairs match."), ("4", "February and May are both 130.")])

# ---------------- Set 2: Police patrols ----------------
P.dilr_set(2, "Set 2 — Police teams patrolling streets", "Answer the questions on the basis of the information given below.",
 p("A, B, C, D, E and F are the six police stations in an area, which are connected by streets as shown below.") +
 '<p class="fig"><img src="sipe_2023S3_DILR_S2.svg" alt="Street map: A is joined to B, C, E and F; C to D; D to E; E to F"></p>' +
 p("Four teams – Team 1, Team 2, Team 3 and Team 4 – patrol these streets continuously between 09:00 hours and 12:00 hours each day. The teams need 30 minutes to cross a street connecting one police station to another. All four teams start from Station A at 09:00 hours and must return to Station A by 12:00 hours. They can also pass via Station A at any point on their journeys.") +
 p("The following facts are known.") +
 "<ol><li>None of the streets has more than one team travelling along it in any direction at any point in time.</li><li>Teams 2 and 3 are the only ones in stations E and D respectively at 10:00 hours.</li><li>Teams 1 and 3 are the only ones in station E at 10:30 hours.</li><li>Teams 1 and 4 are the only ones in stations B and E respectively at 11:30 hours.</li><li>Team 1 and Team 4 are the only teams that patrol the street connecting stations A and E.</li><li>Team 4 never passes through Stations B, D or F.</li></ol>",
 "DILR::LR::Routes_and_Networks",
 steps(("Each team makes six crossings", p("Positions at 09:00, 09:30, …, 12:00, starting and ending at A.")),
       ("Team 3", p("D at 10:00, so C at 09:30 (A–C–D). E at 10:30. It can’t take A–E, and at 11:30 E belongs to Team 4 and B to Team 1, so it goes back: D at 11:00, C at 11:30. <b>A C D E D C A</b>.")),
       ("Team 4", p("Only A, C and E are allowed, so it alternates between A and C or E. At 09:30 C is out (Team 3 is on A–C), so E. At 10:30 E is taken by Teams 1 and 3 only, so C. At 11:30 it is at E. <b>A E A C A E A</b>.")),
       ("Team 2", p("E at 10:00 without A–E: only via F. At 10:30 it must leave E, and D–E is busy (Team 3), so F. It must be next to A at 11:30, so F again. <b>A F E F (A or E) F A</b>.")),
       ("Team 1", p("B at 11:30, so A at 11:00 and E at 10:30, so A at 10:00. At 09:30: A–E (Team 4), A–C (Team 3) and A–F (Team 2) are all busy, so B. <b>A B A E A B A</b>."))) +
 table(["Time", "Team 1", "Team 2", "Team 3", "Team 4"], [["09:30", "B", "F", "C", "E"], ["10:00", "A", "E", "D", "A"], ["10:30", "E", "F", "E", "C"], ["11:00", "A", "A / E", "D", "A"], ["11:30", "B", "F", "C", "E"]]) +
 final("Only Team 2’s 11:00 position has two options."),
 p("Start with the most restricted teams: Team 4 (only A, C, E) and Team 3 (pinned at D then E). The one-team-per-street rule then knocks out Team 1’s and Team 2’s alternatives."),
 p("<b>Timed routes on a graph:</b> list positions at every time step. With fixed step times, each team’s position alternates in parity, which kills many options quickly."))
P.dq(6, "Which one among the following stations is visited the largest number of times?", ["Station C", "Station D", "Station E", "Station F"], "MCQ", "3", "Medium",
 "Count each station in the table (09:30 to 11:30).",
 steps(("Count", p("E: Team 1 once, Team 2 once or twice, Team 3 once, Team 4 twice, so 5 or 6. C: 3. D: 2. F: 3."))) + final("Station E — option 3"),
 [("1", "C is visited 3 times."), ("2", "D is visited twice."), ("4", "F is visited 3 times.")])
P.dq(7, "How many times do the teams pass through Station B in a day?", [], "TITA", "2", "Easy",
 "Only Team 1 goes to B.", steps(("Count", p("Team 1 at 09:30 and 11:30."))) + final(r"\(2\)"))
P.dq(8, "Which team patrols the street connecting Stations D and E at 10:15 hours?", ["Team 3", "Team 2", "Team 4", "Team 1"], "MCQ", "1", "Easy",
 "Who is at D at 10:00 and at E at 10:30?", steps(("Look up", p("Team 3: D at 10:00, E at 10:30."))) + final("Team 3 — option 1"),
 [("2", "Team 2 goes E → F at that time."), ("3", "Team 4 is on A → C."), ("4", "Team 1 is on A → E.")])
P.dq(9, "How many times does Team 4 pass through Station E in a day?", [], "TITA", "2", "Easy",
 "Team 4’s route is A E A C A E A.", steps(("Count", p("At 09:30 and 11:30."))) + final(r"\(2\)"))
P.dq(10, "How many teams pass through Station C in a day?", ["3", "2", "1", "4"], "MCQ", "2", "Easy",
 "Check each route for C.", steps(("Check", p("Team 3 (twice) and Team 4 (once)."))) + final(r"\(2\) — option 2"),
 [("1", "Teams 1 and 2 never reach C."), ("3", "Team 4 also passes through C."), ("4", "Too many.")])

# ---------------- Set 3: Project and test scores ----------------
P.dilr_set(3, "Set 3 — Project and test scores", "Answer the questions based on the following information.",
 p("There are only three female students – Amala, Koli and Rini – and only three male students – Biman, Mathew and Shyamal – in a course. The course has two evaluation components, a project and a test. The aggregate score in the course is a weighted average of the two components, with the weights being positive and adding to 1.") +
 p("The projects are done in groups of two, with each group consisting of a female and a male student. Both the group members obtain the same score in the project.") +
 p("The following additional facts are known about the scores in the project and the test.") +
 "<ol><li>The minimum, maximum and the average of both project and test scores were identical – 40, 80 and 60, respectively.</li><li>The test scores of the students were all multiples of 10; four of them were distinct and the remaining two were equal to the average test scores.</li><li>Amala’s score in the project was double that of Koli in the same, but Koli scored 20 more than Amala in the test. Yet Amala had the highest aggregate score.</li><li>Shyamal scored the second highest in the test. He scored two more than Koli, but two less than Amala in the aggregate.</li><li>Biman scored the second lowest in the test and the lowest in the aggregate.</li><li>Mathew scored more than Rini in the project, but less than her in the test.</li></ol>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("Projects", p(r"Three group scores with min \(40\), max \(80\), average \(60\): \(40, 60, 80\). Amala \(=2\times\) Koli ⇒ Amala \(80\), Koli \(40\), Rini \(60\). Mathew beats Rini ⇒ Mathew \(80\), partnered with Amala.")),
       ("Tests", p(r"Sum \(360\), two scores of \(60\), so the four distinct scores sum to \(240\) with min \(40\) and max \(80\): \(40, 50, 70, 80\). Shyamal \(70\), Biman \(50\). Left for Amala, Koli, Rini, Mathew: \(40, 60, 60, 80\).")),
       ("Two cases", p(r"Koli \(=\) Amala \(+ 20\) and Mathew < Rini give (a) Amala \(40\), Koli \(60\), Mathew \(60\), Rini \(80\), or (b) Amala \(60\), Koli \(80\), Mathew \(40\), Rini \(60\).")),
       ("Weights", p(r"Amala − Koli \(= 4\) in aggregate. In both cases this gives test weight \(w = 0.6\). Case (a): Shyamal \(= 54 = 0.6(70) + 0.4p\) ⇒ \(p = 30\), impossible. Case (b): Shyamal \(= 66\) ⇒ \(p = 60\), so Shyamal is with Rini and Biman with Koli."))) +
 table(["Student", "Project", "Test", "Aggregate"], [["Amala", "80", "60", "68"], ["Koli", "40", "80", "64"], ["Rini", "60", "60", "60"], ["Biman", "40", "50", "46"], ["Mathew", "80", "40", "56"], ["Shyamal", "60", "70", "66"]]) +
 final("Pairs: Amala–Mathew, Koli–Biman, Rini–Shyamal; test weight 0.6."),
 p("Project scores fall out immediately (40, 60, 80 with Amala double Koli). The two-point gaps in clue 4 then fix the weight."),
 p(r"<b>Weighted averages:</b> \(\text{agg} = w\,T + (1 - w)P\). The difference between two people is \(w\,\Delta T + (1 - w)\,\Delta P\), which is linear in \(w\) and solves in one step."))
P.dq(11, "What was Rini’s score in the project?", [], "TITA", "60", "Easy",
 "Project scores are 40, 60, 80; Amala and Koli take 80 and 40.", steps(("Remaining", p(r"Rini \(= 60\)."))) + final(r"\(60\)"))
P.dq(12, "What was the weight of the test component?", ["0.75", "0.50", "0.60", "0.40"], "MCQ", "3", "Medium",
 "Use Amala − Koli = 4 in aggregate.",
 steps(("Solve", r"\[\begin{aligned} (80 - 20w) - (40 + 40w) &= 4 \\ 40 - 60w &= 4 \\ w &= 0.6 \end{aligned}\]")) + final(r"\(0.60\) — option 3"),
 [("1", r"Gives Amala − Koli \(= -5\)."), ("2", r"Gives \(10\), not \(4\)."), ("4", r"Gives \(16\), not \(4\); \(0.4\) is the project weight.")])
P.dq(13, "What was the maximum aggregate score obtained by the students?", ["68", "80", "62", "66"], "MCQ", "1", "Medium",
 "Amala has the highest aggregate.", steps(("Amala", p(r"\(0.6 \times 60 + 0.4 \times 80 = 68\)"))) + final(r"\(68\) — option 1"),
 [("2", "No one scores 80 in both components."), ("3", "Not anyone’s aggregate."), ("4", "That is Shyamal’s, second highest.")])
P.dq(14, "What was Mathew’s score in the test?", [], "TITA", "40", "Medium",
 "Only case (b) survives.", steps(("Case (b)", p(r"Mathew \(40\), Rini \(60\)."))) + final(r"\(40\)"))
P.dq(15, "Which of the following pairs of students were part of the same project team?<br>(i) Amala and Biman<br>(ii) Koli and Mathew", ["Both (i) and (ii)", "Neither (i) nor (ii)", "Only (i)", "Only (ii)"], "MCQ", "2", "Easy",
 "Teams: Amala–Mathew, Koli–Biman, Rini–Shyamal.", steps(("Check", p("Neither pair is a team."))) + final("Neither — option 2"),
 [("1", "Amala is with Mathew; Koli with Biman."), ("3", "Amala is with Mathew."), ("4", "Koli is with Biman.")])

# ---------------- Set 4: AC dealers ----------------
P.dilr_set(4, "Set 4 — Air conditioner dealers", "Answer the questions based on the following information.",
 p("An air conditioner (AC) company has four dealers – D1, D2, D3 and D4 in a city. It is evaluating sales performances of these dealers. The company sells two variants of ACs – Window and Split. Both these variants can be either Inverter type or Non-inverter type. It is known that of the total number of ACs sold in the city, 25% were of Window variant, while the rest were of Split variant. Among the Inverter ACs sold, 20% were of Window variant.") +
 p("The following information is also known:") +
 "<ol><li>Every dealer sold at least two Window ACs.</li><li>D1 sold 13 Inverter ACs, while D3 sold 5 Non-inverter ACs.</li><li>A total of six Window Non-inverter ACs and 36 Split Inverter ACs were sold in the city.</li><li>The number of Split ACs sold by D1 was twice the number of Window ACs sold by it.</li><li>D3 and D4 sold an equal number of Window ACs and this number was one-third of the number of similar ACs sold by D2.</li><li>D2 and D3 were the only ones who sold Window Non-inverter ACs. The number of these ACs sold by D2 was twice the number of these ACs sold by D3.</li><li>D3 and D4 sold an equal number of Split Inverter ACs. This number was half the number of similar ACs sold by D2.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("City totals", p(r"Split Inverter \(36\) is \(80\%\) of Inverter, so Inverter \(= 45\) and Window Inverter \(= 9\). Window \(= 9 + 6 = 15 = 25\%\), so total \(= 60\), Split \(= 45\), Split Non-inverter \(= 9\).")),
       ("Window by dealer", p(r"D3 \(=\) D4 \(= w\), D2 \(= 3w\), D1 \(= 15 - 5w \ge 2\) ⇒ \(w = 2\): D1 \(5\), D2 \(6\), D3 \(2\), D4 \(2\). Window Non-inverter: D2 \(4\), D3 \(2\).")),
       ("Split Inverter", p(r"D1 has \(13\) Inverter, all \(5\) Window ones included ⇒ Split Inverter \(8\). \(8 + 4s = 36\) ⇒ D3 \(=\) D4 \(= 7\), D2 \(= 14\).")),
       ("Split Non-inverter", p(r"D1 Split \(= 2 \times 5 = 10\) ⇒ \(2\) Non-inverter. D3 Non-inverter \(5\) (\(2\) Window) ⇒ \(3\). D2 + D4 \(= 9 - 5 = 4\), split unknown."))) +
 table(["Dealer", "Window Inv", "Window Non-inv", "Split Inv", "Split Non-inv", "Total"],
       [["D1", "5", "0", "8", "2", "15"], ["D2", "2", "4", "14", "x", "20 + x"], ["D3", "0", "2", "7", "3", "12"], ["D4", "2", "0", "7", "4 − x", "13 − x"], ["Total", "9", "6", "36", "9", "60"]]) +
 final("Only D2’s and D4’s Split Non-inverter numbers are open (they add to 4)."),
 p("Turn the percentages into city totals first: 36 is 80% of the Inverter ACs. Everything else is dealer-by-dealer subtraction."),
 p(r"<b>Two-way splits:</b> for variant × type, fill a \(2 \times 2\) grid of city totals before going dealer by dealer; every percentage clue fixes one cell."))
P.dq(16, "How many Split Inverter ACs did D2 sell?", [], "TITA", "14", "Medium",
 "D1’s Split Inverter is 13 − 5. The rest is 36 − 8 split as s, s, 2s.", steps(("Solve", p(r"\(4s = 28 \Rightarrow s = 7\); D2 \(= 2s = 14\)."))) + final(r"\(14\)"))
P.dq(17, "What percentage of ACs sold were of Non-inverter type?", ["75.00%", "33.33%", "25.00%", "20.00%"], "MCQ", "3", "Easy",
 "Inverter = 45 out of 60.", steps(("Compute", p(r"Non-inverter \(= 6 + 9 = 15\); \(\tfrac{15}{60} = 25\%\)."))) + final(r"\(25\%\) — option 3"),
 [("1", "That’s the Inverter share."), ("2", "Ratio of Non-inverter to Inverter."), ("4", "Mixes up the 20% clue.")])
P.dq(18, "What was the total number of ACs sold by D2 and D4?", [], "TITA", "33", "Medium",
 "D2 and D4’s unknowns add up to 4.", steps(("Add", p(r"\((20 + x) + (13 - x) = 33\)"))) + final(r"\(33\)"))
P.dq(19, "Which of the following statements is necessarily false?", ["D1 and D3 together sold more ACs as compared to D2 and D4 together.", "D2 sold the highest number of ACs.", "D1 and D3 sold an equal number of Split ACs.", "D4 sold more Split ACs as compared to D3."],
 "MCQ", "1", "Medium", "D1 + D3 is fixed; D2 + D4 is fixed too.",
 steps(("Compare", p(r"D1 + D3 \(= 15 + 12 = 27\) < D2 + D4 \(= 33\), always."))) + final("Option 1"),
 [("2", r"Always true: D2 \(\ge 20\)."), ("3", r"Always true: both \(10\)."), ("4", r"Can be true: D4 Split \(= 11 - x > 10\) when \(x = 0\).")])
P.dq(20, "If D3 and D4 sold an equal number of ACs, then what was the number of Non-inverter ACs sold by D2?", ["6", "5", "4", "7"], "MCQ", "2", "Medium",
 "D3 = 12, D4 = 13 − x.", steps(("Solve", p(r"\(13 - x = 12 \Rightarrow x = 1\). D2 Non-inverter \(= 4 + 1 = 5\)."))) + final(r"\(5\) — option 2"),
 [("1", r"Would need \(x = 2\)."), ("3", "Forgets D2’s one Split Non-inverter."), ("4", r"Would need \(x = 3\).")])
