# -*- coding: utf-8 -*-
# Batch 15 — CAT 2019 Slot 2: DILR (24 of 32).
from fmt import steps, final, trap, why, table, p
from b15_19s2 import P

def fig(src, alt):
    return f'<p class="fig"><img src="{src}" alt="{alt}"></p>'

# ---------------- Set 1: Rifle shooting ----------------
PTS = table(["Player No.", "Player’s Name", "Points after Round 6", "Points after Round 10"],
            [["1", "Amita", "8", "18"], ["2", "Bala", "2", "5"], ["3", "Chen", "3", "6"], ["4", "David", "6", "6"], ["5", "Eric", "3", "10"],
             ["6", "Fatima", "10", "10"], ["7", "Gordon", "17", "17"], ["8", "Hansa", "1", "4"], ["9", "Ikea", "2", "17"], ["10", "Joshin", "14", "17"]])
P.dilr_set(1, "Set 1 — A ten-round shooting competition", "Answer the questions on the basis of the following information.",
 p("Ten players, as listed in the table below, participated in a rifle shooting competition comprising of 10 rounds. Each round had 6 participants. Players numbered 1 through 6 participated in Round 1, players 2 through 7 in Round 2, ..., players 5 through 10 in Round 5, players 6 through 10 and 1 in Round 6, players 7 through 10, 1 and 2 in Round 7 and so on. The top three performances in each round were awarded 7, 3 and 1 points respectively. There were no ties in any of the 10 rounds. The table below gives the total number of points obtained by the 10 players after Round 6 and Round 10.") + PTS +
 p("The following information is known about Rounds 1 through 6:") +
 "<ol><li>Gordon did not score consecutively in any two rounds.</li><li>Eric and Fatima both scored in a round.</li></ol>" +
 p("The following information is known about Rounds 7 through 10:") +
 "<ol><li>Only two players scored in three consecutive rounds. One of them was Chen. No other player scored in any two consecutive rounds.</li><li>Joshin scored in Round 7, while Amita scored in Round 10.</li><li>No player scored in all the four rounds.</li></ol>",
 "DILR::LR::Games_and_Tournaments",
 steps(("Each round", p("A round hands out 7 + 3 + 1 = 11 points among its six participants. Gordon’s 17 must be 7 + 7 + 3, in three non-consecutive rounds: 2, 4 and 6.")),
       ("Rounds 1–6", p("Working the totals round by round leaves one pattern, apart from Chen and David swapping their 3 points between Rounds 1 and 2.") +
       table(["Round", "7", "3", "1"], [["1", "Amita", "Chen / David", "Bala"], ["2", "Gordon", "David / Chen", "Bala"], ["3", "Fatima", "Eric", "Hansa"],
                                     ["4", "Gordon", "David", "Ikea"], ["5", "Joshin", "Fatima", "Ikea"], ["6", "Joshin", "Gordon", "Amita"]])),
       ("Rounds 7–10", p("Ikea gains 15 = 7 + 7 + 1 and Chen 3 = 1 + 1 + 1, the two three-in-a-row scorers.") +
       table(["Round", "7", "3", "1"], [["7", "Amita", "Joshin", "Ikea"], ["8", "Ikea", "Hansa", "Chen"], ["9", "Ikea", "Bala", "Chen"], ["10", "Eric", "Amita", "Chen"]]))) +
 final("Everything is fixed except who of Chen and David scored in Round 1."),
 p("Start with the big scores: Gordon’s 17 and Ikea’s 15 can only be made a few ways."),
 p("<b>Points tables:</b> break each total into the allowed point values first (here 7, 3, 1)."))
P.dq(1, "What were the scores of Chen, David, and Eric respectively after Round 3?", ["3, 6, 3", "3, 3, 3", "3, 3, 0", "3, 0, 3"], "MCQ", "2", "Hard",
 "Chen and David each have one 3 in Rounds 1–2.",
 steps(("From the set solution", p("Chen 3, David 3, Eric 3 (Round 3)."))) + final("Option 2"),
 [("1", "David’s Round 4 points come later."), ("3", "Eric scored in Round 3."), ("4", "David scored in Round 1 or 2.")])
P.dq(2, "Which three players were in the last three positions after Round 4?", ["Bala, Ikea, Joshin", "Bala, Hansa, Ikea", "Bala, Chen, Gordon", "Hansa, Ikea, Joshin"], "MCQ", "4", "Hard",
 "Add up Rounds 1–4.",
 steps(("After Round 4", p("Joshin 0, Hansa 1, Ikea 1, then Bala 2."))) + final("Option 4"),
 [("1", "Bala has 2, more than Hansa."), ("2", "Leaves out Joshin, who has 0."), ("3", "Gordon has 14.")])
P.dq(3, "Which player scored points in maximum number of rounds?", ["Joshin", "Chen", "Amita", "Ikea"], "MCQ", "4", "Hard",
 "Count rounds, not points.",
 steps(("From the set solution", p("Ikea scored in Rounds 4, 5, 7, 8 and 9: five rounds."))) + final("Ikea, option 4"),
 [("1", "Three rounds."), ("2", "Four rounds."), ("3", "Four rounds.")])
P.dq(4, "Which players scored points in the last round?", ["Amita, Eric, Joshin", "Amita, Chen, David", "Amita, Bala, Chen", "Amita, Chen, Eric"], "MCQ", "4", "Hard",
 "Round 10.",
 steps(("From the set solution", p("Eric 7, Amita 3, Chen 1."))) + final("Option 4"),
 [("1", "Joshin didn’t score in Round 10."), ("2", "David didn’t score after Round 4."), ("3", "Bala scored in Round 9.")])

# ---------------- Set 2: Monsoon rainfall ----------------
P.dilr_set(2, "Set 2 — Rainfall against the long period average", "Answer the questions on the basis of the following information.",
 p("To compare the rainfall data, India Meteorological Department (IMD) calculated the Long Period Average (LPA) of rainfall during period June-August for each of the 16 states. The figure given below shows the actual rainfall (measured in mm) during June-August, 2019 and the percentage deviations from LPA of respective states in 2018. Each state along with its actual rainfall is presented in the figure.") +
 fig("sipe_2019S2_DILR_S2.svg", "Scatter chart, state with 2019 rainfall in mm and deviation from LPA in %: Maharashtra 1000, 30; Gujarat 600, 25; Sikkim 1350, 25; Karnataka 600, 20; Rajasthan 300, 15; Goa 2700, 15; MP 600, 10; Mizoram 1100, 10; Assam 600, −10; Arunachal 1000, −10; Kerala 1500, −10; Meghalaya 1750, −15; WB 600, −30; Jharkhand 400, −35; Delhi 300, −40; Manipur 400, −60."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Reading the chart", p("Each point gives a state’s rainfall (across) and its deviation from LPA (up). Most questions just pick out a group of states and count or average."))) +
 final("Read the points carefully; the questions are about grouping them."),
 p("For each question, list the states that qualify before computing anything."),
 p("<b>Scatter charts:</b> a vertical or horizontal cut-off line through the chart quickly picks out the states you need."))
P.dq(5, "If a ‘Heavy Monsoon State’ is defined as a state with actual rainfall from June-August, 2019 of 900 mm or more, then approximately what percentage of ‘Heavy Monsoon States’ have a negative deviation from respective LPAs in 2019?", ["42.86", "75.00", "57.14", "14.29"], "MCQ", "1", "Easy",
 "Count the states at 900 mm or more.",
 steps(("Heavy states", p("Maharashtra, Arunachal, Mizoram, Sikkim, Kerala, Meghalaya, Goa: 7.")),
       ("Negative", p("Arunachal, Kerala, Meghalaya: 3 of 7, about 42.86%."))) + final("Option 1"),
 [("2", "Wrong count."), ("3", "The share with positive deviation."), ("4", "1 of 7.")])
P.dq(6, "If a ‘Low Monsoon State’ is defined as a state with actual rainfall from June-August, 2019 of 750 mm or less, then what is the median ‘deviation from LPA’ (as defined in the y-axis of the figure) of ‘Low Monsoon States’?", ["–10%", "10%", "–20%", "–30%"], "MCQ", "1", "Easy",
 "Nine states; take the fifth.",
 steps(("Sorted", p("−60, −40, −35, −30, −10, 10, 15, 20, 25. The middle one is −10."))) + final("−10%, option 1"),
 [("2", "Sixth, not fifth."), ("3", "Not one of the values."), ("4", "Fourth.")])
P.dq(7, "What is the average rainfall of all states that have actual rainfall of 600 mm or less in 2019 and have a negative deviation from LPA?", ["367 mm", "500 mm", "450 mm", "460 mm"], "MCQ", "4", "Easy",
 "Five states below the axis at 600 mm or less.",
 steps(("States", p("Assam 600, WB 600, Jharkhand 400, Manipur 400, Delhi 300.")),
       ("Average", p("2300 ÷ 5 = 460."))) + final("460 mm, option 4"),
 [("1", "Leaves out the 600s."), ("2", "Wrong group."), ("3", "Wrong group.")])
P.dq(8, "The LPA of a state for a year is defined as the average rainfall in the preceding 10 years considering the period of June-August. For example, LPA in 2018 is the average rainfall during 2009-2018 and LPA in 2019 is the average rainfall during 2010-2019. It is also observed that the actual rainfall in Gujarat in 2019 is 20% more than the rainfall in 2009. The LPA of Gujarat in 2019 is closest to", ["475 mm", "505 mm", "490 mm", "525 mm"], "MCQ", "3", "Medium",
 "The chart’s 25% is against the 2018 LPA, the average of 2009–2018.",
 steps(("2018 LPA", p("600 is 25% above it, so it is 480, and 2009–2018 adds up to 4800.")),
       ("2009", p("600 is 20% more than 2009, so 2009 had 500.")),
       ("2019 LPA", p("Swap 2009 for 2019: (4800 − 500 + 600) ÷ 10 = 490."))) + final("490 mm, option 3"),
 [("1", "Close to the 2018 LPA."), ("2", "Too high."), ("4", "Too high.")])

# ---------------- Set 3: Question papers ----------------
P.dilr_set(3, "Set 3 — Setting the midterm and endterm", "Answer the questions on the basis of the following information.",
 p("The first year students in a business school are split into six sections. In 2019 the Business Statistics course was taught in these six sections by Annie, Beti, Chetan, Dave, Esha, and Fakir. All six sections had a common midterm (MT) and a common endterm (ET) worth 100 marks each. ET contained more questions than MT. Questions for MT and ET were prepared collectively by the six faculty members. Considering MT and ET together, each faculty member prepared the same number of questions.") +
 p("Each of MT and ET had at least four questions that were worth 5 marks, at least three questions that were worth 10 marks, and at least two questions that were worth 15 marks. In both MT and ET, all the 5-marks questions preceded the 10-marks questions, and all the 15-marks questions followed the 10-marks questions.") +
 p("The following additional facts are known:") +
 "<ol type=\"a\"><li>Annie prepared the fifth question for both MT and ET. For MT, this question carried 5 marks.</li><li>Annie prepared one question for MT. Every other faculty member prepared more than one questions for MT.</li><li>All questions prepared by a faculty member appeared consecutively in MT as well as ET.</li><li>Chetan prepared the third question in both MT and ET; and Esha prepared the eighth question in both.</li><li>Fakir prepared the first question of MT and the last in ET. Dave prepared the last question of MT and the first one in ET.</li></ol>",
 "DILR::LR::Analytical_Reasoning",
 steps(("Possible papers", p("5a + 10b + 15c = 100 with a ≥ 4, b ≥ 3, c ≥ 2 gives 11, 12 or 13 questions. Together the two papers must split equally among six people, and ET is longer: MT 11, ET 13, four questions each.")),
       ("MT", p("Annie has one, everyone else two: Fakir 1–2, Chetan 3–4, Annie 5, Beti 6–7, Esha 8–9, Dave 10–11. The 5th is a 5-marker, so MT is 5 × 5, 3 × 10, 3 × 15.")),
       ("ET", p("Each person’s total is 4, so Annie has 3 in ET, everyone else 2: Dave 1–2, Chetan 3–4, Annie 5–7, Esha 8–9, Beti 10–11, Fakir 12–13. ET is 8 × 5, 3 × 10, 2 × 15.") +
       table(["", "5 marks", "10 marks", "15 marks"], [["MT", "1–5", "6–8", "9–11"], ["ET", "1–8", "9–11", "12–13"]]))) +
 final("Both papers are fully fixed."),
 p("Find the paper lengths from ‘same number each’ before placing anyone."),
 p("<b>Equal-share conditions:</b> they often fix totals that look free at first."))
P.dq(9, "The second question in ET was prepared by:", ["Chetan", "Beti", "Esha", "Dave"], "MCQ", "4", "Hard",
 "Dave starts ET with two questions.",
 steps(("From the set solution", p("Dave prepared 1 and 2."))) + final("Dave, option 4"),
 [("1", "Chetan has 3 and 4."), ("2", "Beti has 10 and 11."), ("3", "Esha has 8 and 9.")])
P.dq(10, "How many 5-mark questions were there in MT and ET combined?", ["13", "12", "10", "Cannot be determined"], "MCQ", "1", "Hard",
 "5 in MT and 8 in ET.",
 steps(("From the set solution", p("5 + 8 = 13."))) + final("13, option 1"),
 [("2", "Miscounts ET."), ("3", "Miscounts."), ("4", "The papers are fixed.")])
P.dq(11, "Who prepared 15-mark questions for MT and ET?", ["Only Beti, Dave, Esha and Fakir", "Only Dave and Fakir", "Only Esha and Fakir", "Only Dave, Esha and Fakir"], "MCQ", "4", "Hard",
 "MT 9–11, ET 12–13.",
 steps(("From the set solution", p("MT: Esha (9), Dave (10, 11). ET: Fakir (12, 13)."))) + final("Option 4"),
 [("1", "Beti’s questions are 10-markers."), ("2", "Leaves out Esha."), ("3", "Leaves out Dave.")])
P.dq(12, "Which of the following questions did Beti prepare in ET?", ["Seventh question", "Fourth question", "Ninth question", "Tenth question"], "MCQ", "4", "Hard",
 "Beti comes between Esha and Fakir in ET.",
 steps(("From the set solution", p("Beti has 10 and 11."))) + final("Option 4"),
 [("1", "Annie’s."), ("2", "Chetan’s."), ("3", "Esha’s.")])

# ---------------- Set 4: Pouches ----------------
POUCH = table(["", "Column 1", "Column 2", "Column 3"], [["Row 1", "(2, 4)", "(6, 8)", "(1, 3)"], ["Row 2", "(3, 5)", "(1, 1)", "(6, 20)"], ["Row 3", "(1, 2)", "(1, 2)", "(2, 5)"]])
P.dilr_set(4, "Set 4 — Coins in twenty-seven pouches", "Answer the questions on the basis of the following information.",
 p("Three pouches (each represented by a filled circle) are kept in each of the nine slots in a 3 × 3 grid. Every pouch has a certain number of one-rupee coins. The minimum and maximum amounts of money (in rupees) among the three pouches in each of the nine slots are given in the table. For example, we know that among the three pouches kept in the second column of the first row, the minimum amount in a pouch is ₹6 and the maximum amount is ₹8.") + POUCH +
 p("There are nine pouches in any of the three columns, as well as in any of the three rows. It is known that the average amount of money (in rupees) kept in the nine pouches in any column or in any row is an integer. It is also known that the total amount of money kept in the three pouches in the first column of the third row is ₹4."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("What’s unknown", p("Only the middle pouch in each slot, which lies between the slot’s minimum and maximum.")),
       ("Divisibility", p("Each row and column of nine pouches must total a multiple of 9. Checking the few possibilities leaves one grid of slot totals:") +
       table(["", "Col 1", "Col 2", "Col 3", "Row total"], [["Row 1", "10 (2, 4, 4)", "20 (6, 6, 8)", "6 (1, 2, 3)", "36"], ["Row 2", "13 (3, 5, 5)", "3 (1, 1, 1)", "38 (6, 12, 20)", "54"],
                                                           ["Row 3", "4 (1, 1, 2)", "4 (1, 1, 2)", "10 (2, 3, 5)", "18"], ["Col total", "27", "27", "54", ""]]))) +
 final("Every pouch is fixed."),
 p("Start with the slots whose middle pouch has only one or two options."),
 p("<b>Row-and-column sums:</b> divisibility by 9 is a strong filter; small ranges make the search short."))
P.dq(13, "What is the total amount of money (in rupees) in the three pouches kept in the first column of the second row?", [], "TITA", "13", "Medium",
 "Row 2, column 1.",
 steps(("From the set solution", p("3 + 5 + 5 = 13."))) + final(r"\(13\)"))
P.dq(14, "How many pouches contain exactly one coin?", [], "TITA", "8", "Medium",
 "Count the 1s.",
 steps(("From the set solution", p("Row 1 column 3: 1. Row 2 column 2: 3. Row 3 columns 1 and 2: 2 each. Total 8."))) + final(r"\(8\)"))
P.dq(15, "What is the number of slots for which the average amount (in rupees) of its three pouches is an integer?", [], "TITA", "2", "Medium",
 "Which slot totals are multiples of 3?",
 steps(("From the set solution", p("6 and 3 only."))) + final(r"\(2\)"))
P.dq(16, "The number of slots for which the total amount in its three pouches strictly exceeds ₹10 is", [], "TITA", "3", "Medium",
 "Totals above 10.",
 steps(("From the set solution", p("20, 13 and 38."))) + final(r"\(3\)"))

# ---------------- Set 5: The clinic ----------------
ROOMS = table(["Room No.", "Monday & Tuesday", "Wednesday & Thursday", "Friday & Saturday"], [["1", "Ben", "Wayne", "Kane"], ["2", "Kane", "Ben", "Wayne"], ["3", "Wayne", "Kane", "Ben"]])
P.dilr_set(5, "Set 5 — Three doctors, three rooms", "Answer the questions on the basis of the following information.",
 p("Three doctors, Dr. Ben, Dr. Kane and Dr. Wayne visit a particular clinic Monday to Saturday to see patients. Dr. Ben sees each patient for 10 minutes and charges ₹100. Dr. Kane sees each patient for 15 minutes and charges ₹200, while Dr. Wayne sees each patient for 25 minutes and charges ₹300. The clinic has three rooms numbered 1, 2 and 3 which are assigned to the three doctors as per the following table.") + ROOMS +
 p("The clinic is open from 9 a.m. to 11:30 a.m. every Monday to Saturday.") +
 p("On arrival each patient is handed a numbered token indicating their position in the queue, starting with token number 1 every day. As soon as any doctor becomes free, the next patient in the queue enters that emptied room for consultation.") +
 p("If at any time, more than one room is free then the waiting patient enters the room with the smallest number. For example, if the next two patients in the queue have token numbers 7 and 8 and if rooms numbered 1 and 3 are free, then patient with token number 7 enters room number 1 and patient with token number 8 enters room number 3."),
 "DILR::LR::Scheduling",
 steps(("A full day", p("In 150 minutes, Ben can see 15 patients, Kane 10 and Wayne 6.")),
       ("Simulating", p("For the token and Thursday questions, follow the queue minute by minute: each patient takes the lowest-numbered free room."))) +
 final("Each question is a short simulation."),
 p("Write each room’s busy times on a timeline."),
 p("<b>Queue simulations:</b> track when each server is next free; the next customer goes to the earliest (and here, lowest-numbered) one."))
P.dq(17, "What is the maximum number of patients that the clinic can cater to on any single day?", ["12", "30", "31", "15"], "MCQ", "3", "Medium",
 "Keep every doctor busy all morning.",
 steps(("Count", p("15 + 10 + 6 = 31."))) + final("31, option 3"),
 [("1", "Too few."), ("2", "One short."), ("4", "Ben alone.")])
P.dq(18, "The queue is never empty on one particular Saturday. Which of the three doctors would earn the maximum amount in consultation charges on that day?", ["Dr. Wayne", "Dr. Kane", "Dr. Ben", "Both Dr. Wayne and Dr. Kane"], "MCQ", "2", "Medium",
 "Patients per day times the fee.",
 steps(("Earnings", p("Ben 15 × 100 = 1500. Kane 10 × 200 = 2000. Wayne 6 × 300 = 1800."))) + final("Dr. Kane, option 2"),
 [("1", "1800."), ("3", "1500."), ("4", "They differ.")])
P.dq(19, "Mr. Singh visited the clinic on Monday, Wednesday, and Friday of a particular week, arriving at 8:50 a.m. on each of the three days. His token number was 13 on all three days. On which day was he at the clinic for the maximum duration?", ["Same duration on all three days", "Friday", "Monday", "Wednesday"], "MCQ", "3", "Hard",
 "Twelve patients are ahead of him each day. Who does he end up with?",
 steps(("When he goes in", p("On all three days he is called in at 9:50.")),
       ("Who he sees", p("Monday: Wayne in room 3, out at 10:15. Wednesday and Friday: Ben, out at 10:00."))) + final("Monday, option 3"),
 [("1", "Monday is longer."), ("2", "Ben, only 10 minutes."), ("4", "Ben, only 10 minutes.")])
P.dq(20, "On a slow Thursday, only two patients are waiting at 9 a.m. After that two patients keep arriving at exact 15-minute intervals starting at 9:15 a.m., i.e., at 9:15 a.m., 9:30 a.m., 9:45 a.m. etc. Then the total duration in minutes when all three doctors are simultaneously free is", ["30", "10", "15", "0"], "MCQ", "4", "Hard",
 "Thursday: Wayne in room 1, Ben in room 2, Kane in room 3.",
 steps(("The pattern", p("9:00: Wayne and Ben start. 9:15: Ben and Kane. 9:30: Wayne and Ben. 9:45: Ben and Kane. It repeats every 30 minutes.")),
       ("All free?", p("Each time Wayne and Ben finish (9:25), Kane is still busy until 9:30, when two more arrive. So never."))) + final("0, option 4"),
 [("1", "Never all free."), ("2", "Never all free."), ("3", "Never all free.")])

# ---------------- Set 8: Two proposals ----------------
P.dilr_set(8, "Set 8 — Two proposals, two candidates", "Answer the questions on the basis of the following information.",
 p("Students in a college are discussing two proposals:") +
 "<ol type=\"A\"><li>a proposal by the authorities to introduce dress code on campus, and</li><li>a proposal by the students to allow multinational food franchises to set up outlets on college campus.</li></ol>" +
 p("A student does not necessarily support either of the two proposals.") +
 p("In an upcoming election for student union president, there are two candidates in fray: Sunita and Ragini. Every student prefers one of the two candidates.") +
 p("A survey was conducted among the students by picking a sample of 500 students. The following information was noted from this survey.") +
 "<ol><li>250 students supported proposal A and 250 students supported proposal B.</li><li>Among the 200 students who preferred Sunita as student union president, 80% supported proposal A.</li><li>Among those who preferred Ragini, 30% supported proposal A.</li><li>20% of those who supported proposal B preferred Sunita.</li><li>40% of those who did not support proposal B preferred Ragini.</li><li>Every student who preferred Sunita and supported proposal B also supported proposal A.</li><li>Among those who preferred Ragini, 20% did not support any of the proposals.</li></ol>",
 "DILR::LR::Venn_Diagrams",
 steps(("Sunita’s 200", p("160 support A. 50 support B, all of them also A. So A and B 50, A only 110, B only 0, neither 40.")),
       ("Ragini’s 300", p("90 support A, 200 support B, 60 neither. Not supporting B: 100, of whom 60 support neither, so A only is 40. Then A and B 50, B only 150.") +
       table(["", "A only", "A and B", "B only", "Neither", "Total"], [["Sunita", "110", "50", "0", "40", "200"], ["Ragini", "40", "50", "150", "60", "300"]]))) +
 final("Every cell is fixed."),
 p("Split by candidate and fill a four-cell Venn for each."),
 p("<b>Two-proposal surveys:</b> a small table (candidate × support pattern) is easier than a diagram."))
P.dq(29, "Among the students surveyed who supported proposal A, what percentage preferred Sunita for student union president?", [], "TITA", "64", "Medium",
 "160 of the 250 A supporters.",
 steps(("From the set solution", p("160 ÷ 250 = 64%."))) + final(r"\(64\)"))
P.dq(30, "What percentage of the students surveyed who did not support proposal A preferred Ragini as student union president?", [], "TITA", "84", "Medium",
 "250 didn’t support A.",
 steps(("From the set solution", p("Ragini: 150 + 60 = 210 of 250, 84%."))) + final(r"\(84\)"))
P.dq(31, "What percentage of the students surveyed who supported both proposals A and B preferred Sunita as student union president?", ["40", "25", "20", "50"], "MCQ", "4", "Medium",
 "50 and 50.",
 steps(("From the set solution", p("50 of 100."))) + final("50, option 4"),
 [("1", "Wrong split."), ("2", "Wrong split."), ("3", "Wrong split.")])
P.dq(32, "How many of the students surveyed supported proposal B, did not support proposal A and preferred Ragini as student union president?", ["150", "210", "200", "40"], "MCQ", "1", "Medium",
 "B only, Ragini.",
 steps(("From the set solution", p("150."))) + final("150, option 1"),
 [("2", "Everyone with Ragini not supporting A."), ("3", "All of Ragini’s B supporters."), ("4", "Ragini’s A only.")])
