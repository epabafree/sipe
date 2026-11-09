# -*- coding: utf-8 -*-
# Simp Mock 7 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_07 import P

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Five tests (Q1–4) ----------------
SETS = table(["Test", "Scores", "Sum"], [["Test 4", "20 18 16 14 12", "80"], ["Top 18", "18 16 14 12 10", "70"], ["Top 16", "16 14 12 10 8", "60"], ["Top 14", "14 12 10 8 6", "50"], ["Test 5", "12 10 8 6 4", "40"]])
P.dilr_set(1, "Set 1 — Five students, five tests", DIR,
 p("Abhijit, Bhumika, Chitra, Falguni and Geeta are five students who took five tests at an academy run by Mr Kaprekar. Each test had 20 multiple-choice questions, and every student had to attempt all the questions in each test. Each correct answer earned one mark, and each incorrect answer cost one mark.") +
 p("After the papers were checked, the following facts emerged:") +
 "<ul><li>In each test, the marks scored by the five students were distinct natural numbers.</li><li>Each test was topped by a different student. The toppers’ scores in the five tests were distinct and summed to 80.</li><li>If S1, S2, S3, S4 and S5 are the sums of the five students’ marks in Tests 1 to 5, the average of S1 to S5 was 60.</li><li>The highest score in Test 5 equalled the lowest score in Test 4.</li></ul>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("Scores are even", p(r"With c correct out of 20, the score is \(c - (20 - c) = 2c - 20\): always even. Natural numbers, so 2, 4, …, 20.")),
       ("Toppers", p("Five distinct even toppers summing to 80, none above 20: only 20 + 18 + 16 + 14 + 12.")),
       ("Tests 4 and 5", p("Test 4’s lowest is at least 8 below its top; it must equal Test 5’s top, which is at least 12. So Test 4 is 20, 18, 16, 14, 12, and Test 5 is topped by 12.")),
       ("Totals", p("The five totals sum to 300. Test 4 is 80; Test 5 at most 12 + 10 + 8 + 6 + 4 = 40; the tests topped by 18, 16, 14 at most 70, 60, 50. These maxima add to exactly 300, so every test takes its maximum.")),
       ("Every test", SETS)) +
 final("Each test’s five scores are fixed; only which test (1–3) has which top, and who scored what, are open."),
 p("Plus one / minus one with every question attempted makes every score even."),
 p("<b>Sum at its maximum:</b> when the largest possible totals add up exactly to the given total, each part must be at its largest."))
P.dq(1, "What can be the maximum value of the average score of a student in the third test?", ["12", "13", "14", "15"], "MCQ", "3", "Medium",
 "Test 3 could be the test topped by 18.", steps(("Best case", p("18 + 16 + 14 + 12 + 10 = 70; 70 ÷ 5 = 14."))) + final("14, option 3"),
 [("1", "The 14-topped test."), ("2", "Not a possible average."), ("4", "Would need a total of 75.")])
P.dq(2, "If Bhumika is the highest scorer in the fifth test, but that is not her highest score across the five tests, what can be the maximum value of her total score in the five tests?", ["70", "72", "74", "76"], "MCQ", "2", "Medium",
 "She tops only Test 5, so elsewhere she can be at best second.",
 steps(("Best case", p("12 (Test 5) + 18 (Test 4) + 16 + 14 + 12 (second in the others) = 72."))) + final("72, option 2"),
 [("1", "Not the maximum."), ("3", "She can’t top a second test."), ("4", "She can’t top a second test.")])
P.dq(3, "What can be the minimum score a student received in any of the tests?", ["2", "3", "4", "6"], "MCQ", "3", "Easy",
 "Look at Test 5.", steps(("Lowest", p("Test 5’s lowest score is 4."))) + final("4, option 3"),
 [("1", "Would push the total below 300."), ("2", "Scores are even."), ("4", "4 occurs.")])
P.dq(4, "On how many instances was a student’s score in a test a single-digit number?", ["5", "6", "7", "8"], "MCQ", "2", "Easy",
 "Count 4, 6 and 8 across the tests.", steps(("Count", p("Test 5: 8, 6, 4. Topped by 16: 8. Topped by 14: 8, 6. Total 6."))) + final("6, option 2"),
 [("1", "Misses one."), ("3", "Too many."), ("4", "Too many.")])

# ---------------- Set 2: Runs across formats (Q5–8) ----------------
RUNS = table(["Player", "T20", "ODI", "Test"], [["Mohan", "200", "1200", "100"], ["Vikas", "1200", "600", "100"], ["Rahul", "800", "0", "0"], ["Sunil", "500", "400", "1100"], ["Nitin", "400", "200", "100"]]) + p("Totals: Sunil 2000, Vikas 1900, Mohan 1500, Rahul 800, Nitin 700.")
P.dilr_set(2, "Set 2 — Runs across three formats", DIR,
 p("An award goes to the batsman who scores the most total runs for the national team across all three formats (T20, ODI and Test) in a calendar year. In 2024 the national cricket board lost its scorecards, and gathered the following details from the players.") +
 p("Mohan, Vikas, Rahul, Sunil and Nitin are the five highest run scorers of 2024. In T20s, their totals were 200, 400, 500, 800 and 1200, in some order. In ODIs, their totals were 0, 200, 400, 600 and 1200, in some order.") +
 "<ul><li>Mohan’s ODI runs are three times the ODI runs of the batsman (another player) who scored 500 in T20s.</li><li>Vikas scored twice as many runs in T20s as in ODIs.</li><li>Rahul was the only batsman who scored no runs in Tests.</li><li>Sunil scored 2000 runs across the three formats. No other batsman scored 2000 or more.</li><li>Nitin’s T20 runs are double his ODI runs, which are double his Test runs.</li><li>The five batsmen scored 1400 Test runs in total.</li><li>Every batsman’s runs in each format are a non-negative multiple of 100.</li></ul>",
 "DILR::LR::Puzzles",
 steps(("Mohan’s ODI", p("Three times another ODI value: 600 (= 3 × 200) or 1200 (= 3 × 400). If 600, the 500 scorer has ODI 200, and Vikas and Nitin both need a T20 = 2 × ODI pair from what’s left: only 800/400 remains. Impossible. So Mohan has 1200 and the 500 scorer has ODI 400.")),
       ("Vikas and Nitin", p("Their T20/ODI pairs are 400/200 and 1200/600 in some order. The 500 scorer is Rahul or Sunil.")),
       ("Sunil", p("Test runs: Mohan, Vikas and Nitin at least 100 each, so Sunil has at most 1100. If Rahul scored the 500, Sunil would need 1200 or 1800 Test runs. So Sunil: 500 + 400 + 1100 = 2000, and the others share 300 Test runs: 100 each.")),
       ("The rest", p("Nitin’s Test 100 gives ODI 200, T20 400; Vikas 1200/600. Rahul has ODI 0. Mohan’s total must stay below 2000, so his T20 is 200 and Rahul’s 800.")),
       ("Runs", RUNS)) +
 final("Every batsman’s runs in every format are fixed."),
 p("Start from the clue with the fewest options (Mohan’s ODI), then let the Test total cap Sunil."),
 p("<b>Pairing clues:</b> ‘twice’ and ‘three times’ cut each list to a couple of pairs."))
P.dq(5, "For how many batsmen can the runs scored in each of the three formats be determined uniquely?", ["2", "3", "4", "5"], "MCQ", "4", "Medium",
 "Every step was forced.", steps(("Count", p("All five."))) + final("5, option 4"),
 [("1", "All are fixed."), ("2", "All are fixed."), ("3", "All are fixed.")])
P.dq(6, "How many runs did Mohan score in T20s?", [], "TITA", "200", "Easy",
 "His total must stay below 2000.", steps(("Mohan", p("200."))) + final("200"))
P.dq(7, "Who scored the second-highest total runs across all three formats?", ["Mohan", "Vikas", "Nitin", "Rahul"], "MCQ", "2", "Easy",
 "Totals: 2000, 1900, 1500, 800, 700.", steps(("Second", p("Vikas, 1900."))) + final("Option 2"),
 [("1", "1500, third."), ("3", "700, last."), ("4", "800.")])
P.dq(8, "How many total runs did Rahul score across all three formats?", [], "TITA", "800", "Easy",
 "800 + 0 + 0.", steps(("Rahul", p("800."))) + final("800"))

# ---------------- Set 3: The computer lab (Q9–13) ----------------
TL = table(["Student", "In", "Out"], [["Neha", "11:00", "11:30"], ["Kishan", "11:08", "11:20"], ["Ravi", "11:13–11:20", "11:35"], ["Teja", "11:25", "11:36"], ["Disha", "11:30", "11:50"], ["Jiten", "11:35", "11:52"], ["Ambika", "11:50", "12:00"]])
P.dilr_set(3, "Set 3 — Who was in the lab", DIR,
 p("Seven college students, 3 girls and 4 boys, visited the college computer lab between 11:00 AM and 12 noon on a particular day. The first student entered exactly at 11:00 AM, when no one else was inside, and the last student left exactly at 12 noon. No one else entered the lab in that hour, and at least one student was inside at every instant. Among the girls, Neha was the first and Ambika the last to enter; the other girl was Disha. No two girls were inside the lab at the same time. Each student entered and left only once.") +
 p("Entries and exits happened only on whole minutes from 11:00 AM to 12:00 noon (61 possible instants). Further:") +
 "<ol><li>The smallest and largest gaps between two consecutive entries were 5 minutes and 15 minutes.</li><li>The gap between Neha’s entry and the next student’s entry equalled the time Ambika was alone in the lab.</li><li>Disha was in the lab for 100% longer than Ambika, and \\(33\\tfrac13\\%\\) less time than Neha.</li><li>Kishan was in the lab with exactly one of the three girls for some time.</li><li>Jiten was in the lab for 17 minutes; Ambika was with him for 2 minutes, and one other girl for 15 minutes.</li><li>Jiten was the only boy who was in the lab with Ambika. Ambika was alone for the last 8 minutes before she left.</li><li>Ravi and Teja, who entered one after the other in some order, are the only boys who were in the lab with both Disha and Neha (not with both at once). Teja left one minute after Ravi.</li><li>The boy who entered immediately after Neha stayed for 12 minutes.</li><li>Disha and Teja were together in the lab for exactly 6 minutes. Teja stayed one minute longer than Ambika.</li></ol>",
 "DILR::LR::Scheduling",
 steps(("The girls fill the hour", p("Ambika stays at least 2 + 8 = 10 minutes. Neha : Disha : Ambika = 3 : 2 : 1 and they never overlap, so 6 × Ambika ≤ 60: Ambika 10, Disha 20, Neha 30. They cover the whole hour: Neha 11:00–11:30, Disha 11:30–11:50, Ambika 11:50–12:00.")),
       ("Kishan", p("Ambika was alone 8 minutes in all, so the second entrant came at 11:08 and stayed 12 minutes (to 11:20), meeting only Neha. Ravi and Teja met both girls and Jiten met Ambika, so this is Kishan.")),
       ("Jiten and Teja", p("Jiten leaves at 11:52 (2 minutes with Ambika) and entered at 11:35. Teja stays 11 minutes and has 6 with Disha, never meeting Ambika: in 11:25, out 11:36. Ravi leaves at 11:35.")),
       ("Order and gaps", p("Entries: Neha 0, Kishan 8, then Ravi and Teja, Disha 30, Jiten 35 (gap 5), Ambika 50 (gap 15). Teja third would leave a 17-minute gap after Kishan, so Ravi is third and Teja fourth. Gaps of 5–15 put Ravi between 11:13 and 11:20.")),
       ("Timeline", TL)) +
 final("Everything is fixed except Ravi’s entry, anywhere from 11:13 to 11:20."),
 p("The girls’ 3 : 2 : 1 ratio and no overlaps fill the hour, which pins down everyone else."),
 p("<b>Timelines:</b> write each person as an interval; overlaps and gaps then read straight off."))
P.dq(9, "Number the students 1–7 in order of entry (entry serial numbers), and separately 1–7 in order of leaving (exit serial numbers). For how many students are the two serial numbers the same?", [], "TITA", "5", "Medium",
 "Exit order: Kishan 11:20, Neha 11:30, Ravi, Teja, Disha, Jiten, Ambika.",
 steps(("Compare", p("Entry: Neha, Kishan, Ravi, Teja, Disha, Jiten, Ambika. Exit: Kishan, Neha, then the same. Only Neha and Kishan differ: 5 match."))) + final("5"))
P.dq(10, "How many distinct groups of three students were definitely in the lab together at some time?", [], "TITA", "3", "Hard",
 "Check triples in every possible timeline.",
 steps(("Always", p("Neha, Ravi, Teja (11:25–11:30); Disha, Ravi, Teja (11:30–11:35); Disha, Jiten, Teja (11:35–11:36).")),
       ("Not always", p("Neha, Kishan, Ravi meet only if Ravi enters before 11:20; at 11:20 Kishan leaves as Ravi enters."))) + final("3"))
P.dq(11, "What is the minimum duration (in minutes) for which some particular group of 3 students was together in the lab?", ["1", "2", "3", "Cannot be determined"], "MCQ", "1", "Medium",
 "Disha, Jiten and Teja.", steps(("Shortest", p("Disha, Jiten and Teja: 11:35–11:36, 1 minute."))) + final("1, option 1"),
 [("2", "Too long."), ("3", "Too long."), ("4", "Fixed by the timeline.")])
P.dq(12, "What is the total duration (in minutes) during which at least one boy was in the lab?", ["42", "44", "52", "A unique value cannot be determined"], "MCQ", "2", "Medium",
 "Boys from 11:08 to 11:52 without a break.",
 steps(("Span", p("Kishan 11:08–11:20, Ravi from 11:20 at the latest, Teja to 11:36, Jiten 11:35–11:52: no gap. 44 minutes."))) + final("44, option 2"),
 [("1", "Misses a stretch."), ("3", "Counts girls’ time."), ("4", "Ravi’s entry doesn’t matter.")])
P.dq(13, "Which of the following cannot be Ravi’s entry time?", ["11:13 AM", "11:15 AM", "11:19 AM", "None of these"], "MCQ", "4", "Medium",
 "Ravi enters from 11:13 to 11:20.", steps(("Range", p("All three times are possible."))) + final("Option 4"),
 [("1", "Possible."), ("2", "Possible."), ("3", "Possible.")])

# ---------------- Set 4: A three-day event (Q14–18) ----------------
SOLD = table(["Date", "General", "VIP", "Exclusive"], [["15 Aug", "12,000", "", "13,000"], ["16 Aug", "", "18,000", "15,600"], ["17 Aug", "", "19,800", "17,160"]])
CAT = table(["Category", "1 day", "2 days", "3 days"], [["General", "21,120", "12,672", "8,448"], ["VIP", "31,680", "13,200", "7,920"], ["Exclusive", "34,320", "6,864", "4,576"]])
P.dilr_set(4, "Set 4 — A three-day event", DIR,
 p("A theme-park event was held over three days (15, 16 and 17 August) in Singapore. Tickets were sold in three categories: General, VIP and Exclusive. Visitors could attend on one, two or all three days. No one booked in advance, and each person bought one ticket.") +
 "<ul><li>People who bought on 15 August bought tickets for one, two or three days.</li><li>People who bought on 16 August bought for one or two days.</li><li>People who bought on 17 August bought only for that day.</li><li>Everyone attended for as many days as they paid for. Those who bought two-day tickets on 15 August could attend any two of the three days. One-day ticket holders attended on the day they bought.</li></ul>" +
 p("Further:") +
 "<ul><li>Tickets sold rose by 20% from 15 to 16 August and by 10% from 16 to 17 August, reaching 52,800 on 17 August.</li><li>Of all General ticket holders, 50%, 30% and 20% attended for one, two and three days.</li><li>For VIP: 60%, 25% and 15%.</li><li>For Exclusive: 75%, 15% and 10%.</li></ul>" +
 p("Partial table of tickets sold each day in each category:") + SOLD,
 "DILR::DI::Data_Tabulation",
 steps(("Daily totals", p("17 Aug: 52,800 = 1.32 × (15 Aug), so 15 Aug 40,000 and 16 Aug 48,000. Missing cells: VIP 15 Aug 15,000; General 16 Aug 14,400 and 17 Aug 15,840.")),
       ("Category totals", p("General 42,240, VIP 52,800, Exclusive 45,760. Split by days:") + CAT),
       ("Who bought when", p("Three-day tickets come only from 15 Aug; 17 Aug buyers are all one-day. Let a, b, c be the one-day buyers on 15 Aug (General, VIP, Exclusive).")),
       ("General", p("15 Aug: 12,000 = a + two-day + 8,448, so two-day = 3,552 − a. One-day on 16 Aug: 21,120 − a − 15,840 = 5,280 − a; two-day on 16 Aug: 9,120 + a.")),
       ("VIP and Exclusive", p("VIP: two-day on 15 Aug = 7,080 − b; one-day on 16 Aug = 11,880 − b. Exclusive: two-day on 15 Aug = 8,424 − c; one-day on 16 Aug = 17,160 − c ≤ 15,600, so c ≥ 1,560.")),
       ("Ranges", p("0 ≤ a ≤ 3,552; 0 ≤ b ≤ 7,080; 1,560 ≤ c ≤ 8,424."))) +
 final("Each question picks a value of a, b or c, or a bound."),
 p("Three-day tickets all date from 15 Aug and all 17 Aug tickets are one-day: these fix most cells."),
 p("<b>Unknowns with bounds:</b> express every cell in one or two unknowns, then read off the ranges."))
P.dq(14, "Among VIP ticket holders who attended on only one day, on which day did the largest number buy their tickets?", ["15 August", "16 August", "17 August", "Cannot be determined"], "MCQ", "3", "Medium",
 "17 Aug: 19,800 one-day VIP buyers.",
 steps(("Compare", p("15 Aug: b ≤ 7,080. 16 Aug: 11,880 − b ≤ 11,880. 17 Aug: 19,800, always the most."))) + final("Option 3"),
 [("1", "At most 7,080."), ("2", "At most 11,880."), ("4", "17 August wins in every case.")])
P.dq(15, "If the number of General one-day tickets bought on 15 August equals the number of General two-day tickets bought on 15 August, how many General two-day tickets were bought on 16 August? (Enter 0 if it cannot be determined.)", [], "TITA", "10896", "Medium",
 "a = 3,552 − a.",
 steps(("a", p("a = 1,776.")), ("16 Aug", p("9,120 + 1,776 = 10,896."))) + final("10896"))
P.dq(16, "Which of the following can be the number of Exclusive one-day tickets bought on 15 August?", ["1,500", "5,000", "8,500", "10,000"], "MCQ", "2", "Medium",
 "1,560 ≤ c ≤ 8,424.", steps(("Range", p("Only 5,000 is in range."))) + final("Option 2"),
 [("1", "Below 1,560."), ("3", "Above 8,424."), ("4", "Above 8,424.")])
P.dq(17, "What can be the maximum number of people attending the event on 16 August?", ["93,304", "88,024", "88,000", "86,440"], "MCQ", "4", "Hard",
 "Everyone who bought on 16 Aug, all three-day holders, and as many 15 Aug two-day holders as possible.",
 steps(("Fixed", p("Bought on 16 Aug: 48,000. Three-day: 8,448 + 7,920 + 4,576 = 20,944.")),
       ("15 Aug two-day", p("At most 3,552 + 7,080 + 6,864 = 17,496, if all choose 16 Aug.")),
       ("Total", p("48,000 + 20,944 + 17,496 = 86,440."))) + final("Option 4"),
 [("1", "Counts more than exist."), ("2", "Ignores c ≥ 1,560."), ("3", "Not reachable.")])
P.dq(18, "Which of the following is the smallest?", ["The number of people who attended for two days under General", "The number who attended for two days under VIP", "The number who attended for one day under General", "The number who attended for one day under VIP"], "MCQ", "1", "Easy",
 "Read the category table.", steps(("Values", p("12,672; 13,200; 21,120; 31,680."))) + final("Option 1"),
 [("2", "13,200."), ("3", "21,120."), ("4", "31,680.")])

# ---------------- Set 5: Dinner orders (Q19–22) ----------------
ORD = table(["Amit", "Bina", "Chetan", "Divya"], [["CC", "VB", "VB", "PBM"], ["CC", "VB", "PBM", "VB"], ["CC", "PBM", "VB", "VB"], ["CC", "PBM", "VB", "PBM"], ["PBM", "VB", "CC", "VB"], ["PBM", "VB", "CC", "PBM"], ["PBM", "CC", "VB", "PBM"], ["PBM", "PBM", "VB", "CC"], ["PBM", "PBM", "CC", "VB"]])
P.dilr_set(5, "Set 5 — Dinner orders", DIR,
 p("Amit, Bina, Chetan and Divya went to dinner. Each ordered exactly one dish: Veg Biryani (VB), Chicken Curry (CC) or Paneer Butter Masala (PBM).") +
 "<ul><li>If Amit orders VB, then Bina orders the same dish as Chetan.</li><li>If Bina orders CC, then Amit orders the same dish as Divya.</li><li>If Chetan orders PBM, then Bina orders the same dish as Divya.</li><li>If Divya orders CC, then Amit orders the same dish as Bina.</li><li>Amit and Chetan do not order the same dish.</li></ul>" +
 p("At most two people ordered the same dish, and each dish was ordered by at least one person."),
 "DILR::LR::Analytical_Reasoning",
 steps(("Shape", p("Four people, three dishes, at most two per dish: one dish is shared by two people, the others by one each.")),
       ("Amit can’t have VB", p("Then Bina = Chetan, both not VB (Chetan ≠ Amit), so that dish is taken twice and Divya has the third dish. If the pair is CC, Bina’s CC makes Amit = Divya, which fails. If the pair is PBM, Chetan’s PBM makes Bina = Divya, which fails.")),
       ("All orders", ORD)) +
 final("Nine possible combinations; Amit has CC or PBM."),
 p("Test Amit = VB first; every ‘if’ then forces a clash."),
 p("<b>Conditionals:</b> only the ‘if’ part being true triggers the rule; check each case against the counts."))
P.dq(19, "How many combinations of dishes ordered by the four people are possible?", ["Less than 7", "7", "8", "More than 8"], "MCQ", "4", "Hard",
 "List them case by case.", steps(("Count", p("Nine combinations, listed in the set solution."))) + final("Option 4"),
 [("1", "Too few."), ("2", "Too few."), ("3", "Misses one.")])
P.dq(20, "If Amit ordered Chicken Curry, which dish did Bina order?", ["Either VB or PBM", "Either CC or PBM", "Either CC or VB", "CC only"], "MCQ", "1", "Medium",
 "Amit CC rows.", steps(("Bina", p("VB or PBM. (Bina CC would need Divya = Amit = CC, three CCs.)"))) + final("Option 1"),
 [("2", "Bina can’t have CC."), ("3", "Bina can’t have CC."), ("4", "Impossible.")])
P.dq(21, "Which of the following dishes cannot be ordered by Amit?", ["PBM", "VB", "CC", "No such dish"], "MCQ", "2", "Medium",
 "Amit = VB always clashes.", steps(("Amit", p("VB is impossible."))) + final("Option 2"),
 [("1", "Possible."), ("3", "Possible."), ("4", "VB is ruled out.")])
P.dq(22, "If Chetan ordered Paneer Butter Masala, how many combinations of dishes are possible?", ["1", "2", "3", "More than 3"], "MCQ", "1", "Medium",
 "Chetan PBM forces Bina = Divya.", steps(("One", p("Amit CC, Bina VB, Chetan PBM, Divya VB: the only one."))) + final("Option 1"),
 [("2", "Only one."), ("3", "Only one."), ("4", "Only one.")])
