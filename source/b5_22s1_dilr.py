# -*- coding: utf-8 -*-
# Batch 5 — CAT 2022 Slot 1: DILR sets 1–4 (Q1–20, in exam order).
from fmt import steps, final, why, table, p
from b5_22s1 import P

DIR = "Read the instructions given and answer the questions that follow."

# ---------------- Set 1: Metro lines ----------------
P.dilr_set(1, "Set 1 — A city’s metro lines", DIR,
 '<p class="fig"><img src="sipe_2022S1_DILR_S1.svg" alt="Metro map. Two east–west lines: M to N through junctions R and S, and P to Q through junctions T and V. Two north–south lines: A to B through R and T, and C to D through S and V. Between M and R there are 3 stations, between R and S 9, between S and N 5; the P–Q line has the same pattern. On each north–south line there are 2 stations between the terminal and the first junction, 3 between the two junctions, and 2 between the second junction and the other terminal."></p>' +
 p("Given above is the schematic map of the metro lines in a city with rectangles denoting terminal stations (e.g. A), diamonds denoting junction stations (e.g. R) and small filled-up circles denoting other stations. Each train runs either in east-west or north-south direction, but not both. All trains stop for 2 minutes at each of the junction stations on the way and for 1 minute at each of the other stations. It takes 2 minutes to reach the next station for trains going in east-west direction and 3 minutes to reach the next station for trains going in north-south direction. From each terminal station, the first train starts at 6 am; the last train leaves the terminal station at midnight. Otherwise, during the service hours, there are metro services every 15 minutes in the north-south lines and every 10 minutes in the east-west lines. A train must rest for at least 15 minutes after completing a trip at the terminal station, before it can undertake the next trip in the reverse direction.") +
 p("(All questions are related to this metro service only. Assume that if someone reaches a station exactly at the time a train is supposed to leave, (s)he can catch that train.)"),
 "DILR::LR::Routes_and_Networks",
 steps(("Counting the stops", p("On each east–west line there are 20 gaps between stations from one terminal to the other (3 + 1, then 9 + 1, then 5 + 1). On the way, a train passes 17 ordinary stations and 2 junctions. On each north–south line there are 10 gaps, with 7 ordinary stations and 2 junctions.")),
       ("Full trip times", table(["Line", "Travel", "Stops", "Terminal to terminal"],
          [["East–west (M–N, P–Q)", r"\(20 \times 2 = 40\) min", r"\(17 \times 1 + 2 \times 2 = 21\) min", "61 min"],
           ["North–south (A–B, C–D)", r"\(10 \times 3 = 30\) min", r"\(7 \times 1 + 2 \times 2 = 11\) min", "41 min"]], first_col_header=True)),
       ("Times at the junctions", p("It is handy to know when trains leave each junction. A train that leaves M at time t reaches R after 8 minutes of travel and 3 one-minute stops, and leaves R at t + 13 after its 2-minute halt. Exactly the same holds from P to T, from B up to T, and from D up to V. Trains from the far end of an east–west line take 19 minutes to leave the nearer junction (for example, N to S), and trains from the far end of a north–south line take 13 minutes (for example, A to R).")),
       ("How many trains a line needs", p("A train that leaves a terminal returns there after one trip each way plus a 15-minute rest at each end. On a north–south line that is 41 + 15 + 41 + 15 = 112 minutes, so with trains every 15 minutes it can next leave at the 120-minute mark: 8 trains per line. On an east–west line, 61 + 15 + 61 + 15 = 152 minutes rounds up to 160 with a 10-minute frequency: 16 trains per line."))) +
 final("Trip times: 61 min east–west, 41 min north–south. Trains needed: 8 per north–south line, 16 per east–west line."),
 p("Work out the trip time once, including stops, and the time each train leaves a junction. Almost every question is then a matter of reading off the next departure."),
 p("<b>Timetable questions:</b> a train’s time at any station is its departure time plus travel time plus the stops before it. Fixed frequencies mean departures repeat at the same minutes past every hour."))
P.dq(1, "If Hari is ready to board a train at 8:05 am from station M, then when is the earliest that he can reach station N?", ["9:06 am", "9:01 am", "9:13 am", "9:11 am"], "MCQ", "4", "Easy",
 "Trains leave M every 10 minutes from 6:00. Which is the first one after 8:05, and how long does the whole line take?",
 steps(("Catching the train", p("Trains leave M at 8:00, 8:10 and so on, so Hari takes the 8:10.")),
       ("Riding to the end", p("A full east–west trip takes 61 minutes, so he reaches N at 9:11 am."))) + final("9:11 am, option 4"),
 [("1", "This would mean leaving M at 8:05, but there is no train at that time."), ("2", "That is too early for a train that leaves M at 8:10 and needs 61 minutes."), ("3", "This adds two extra minutes that the trip doesn’t need.")])
P.dq(2, "If Priya is ready to board a train at 10:25 am from station T, then when is the earliest that she can reach station S?", ["11:28 am", "11:12 am", "11:07 am", "11:22 am"], "MCQ", "2", "Medium",
 "There are two ways from T to S: north to R and then east, or east to V and then north. Try both.",
 steps(("Going north first", p("Northbound trains leave T at 13, 28, 43 and 58 minutes past the hour, so Priya takes the 10:28. The ride to R takes 4 × 3 = 12 minutes of travel and 3 one-minute stops, so she reaches R at 10:43. Eastbound trains leave R at 3, 13, 23, 33, 43 and 53 past, so she catches the 10:43. From R to S is 10 × 2 = 20 minutes of travel and 9 stops, so she arrives at 11:12.")),
       ("Going east first", p("Eastbound trains leave T at 3, 13, 23, 33… past, so she would take the 10:33 and reach V at 11:02. Northbound trains leave V at 13, 28, 43 and 58 past, so she waits for the 11:13 and reaches S at 11:28."))) +
 final("11:12 am, option 2"),
 [("1", "That is the route through V, which is slower."), ("3", "No combination of trains gets her there this early."), ("4", "This doesn’t match either route’s timings.")])
P.dq(3, "Haripriya is expected to reach station S late. What is the latest time by which she must be ready to board at station S if she must reach station B before 1 am via station R?", ["11:39 pm", "11:35 pm", "11:49 am", "11:43 pm"], "MCQ", "1", "Hard",
 "Work backwards from the last southbound train out of R, since the last train leaves A at midnight.",
 steps(("The last train south", p("The last train leaves A at midnight and leaves R at 12:13 am. From R it reaches B 28 minutes later, at 12:41 am, which is before 1 am.")),
       ("Getting to R in time", p("Westbound trains leave S at 19 minutes after they leave N, so at 9, 19, 29, 39 and 49 past the hour. The ride from S to R takes 29 minutes. The 11:39 pm train reaches R at 12:08 am, in time for the 12:13. The 11:49 pm train would reach R at 12:18, too late."))) +
 final("11:39 pm, option 1"),
 [("2", "No westbound train leaves S at 11:35."), ("3", "This is a morning time, which is far too early to be the latest."), ("4", "No westbound train leaves S at 11:43.")])
P.dq(4, "What is the minimum number of trains that are required to provide the service on the AB line (considering both north and south directions)?", [], "TITA", "8", "Medium",
 "How long before a train that leaves A can leave A again?",
 steps(("One round", p("A to B takes 41 minutes, then 15 minutes of rest, then 41 minutes back and 15 more of rest: 112 minutes in all.")),
       ("Fitting the timetable", p("Trains leave A every 15 minutes, so the train can next take the departure 120 minutes later. Covering 120 minutes at one train every 15 minutes needs 120 ÷ 15 = 8 trains."))) + final(r"\(8\)"))
P.dq(5, "What is the minimum number of trains that are required to provide the service in this city?", [], "TITA", "48", "Hard",
 "Do the same calculation for an east–west line, then add up all four lines.",
 steps(("East–west lines", p("61 + 15 + 61 + 15 = 152 minutes for a round, so a train can next leave at the 160-minute mark. With trains every 10 minutes that needs 16 trains per line.")),
       ("Adding up", p("Two north–south lines with 8 trains each and two east–west lines with 16 each: 16 + 32 = 48."))) + final(r"\(48\)"))

# ---------------- Set 2: Hockey goals ----------------
P.dilr_set(2, "Set 2 — Goals scored by four hockey players", "Answer the questions on the basis of the information given below.",
 p("The management of a university hockey team was evaluating the performance of four women players - Amla, Bimla, Harita and Sarita for their possible selection in the university team for the next year. For this purpose, the management was looking at the number of goals scored by them in the past 8 matches, numbered 1 through 8. The four players together had scored a total of 12 goals in these matches. In the 8 matches, each of them had scored at least one goal. No two players had scored the same total number of goals.") +
 p("The following facts are known about the goals scored by these four players only. All the questions refer only to the goals scored by these four players.") +
 "<ol><li>Only one goal was scored in every even numbered match.</li><li>Harita scored more goals than Bimla.</li><li>The highest goal scorer scored goals in exactly 3 matches, including Match 4 and Match 8.</li><li>Bimla scored a goal in Match 1 and one each in three other consecutive matches.</li><li>An equal number of goals were scored in Match 3 and Match 7, which was different from the number of goals scored in either Match 1 or Match 5.</li><li>The match in which the highest number of goals was scored was unique and it was not Match 5.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Each player’s total", p("Four different totals, each at least 1, adding to 12, can only be 1, 2, 3, 6 or 1, 2, 4, 5. Bimla scored in Match 1 and in three more matches, so she has at least 4 goals. Harita has more than Bimla. That leaves 1, 2, 4, 5: Bimla 4, Harita 5, and Amla and Sarita share 1 and 2.")),
       ("Harita’s goals", p("Harita is the top scorer, so she scored in exactly 3 matches, including Matches 4 and 8. Even-numbered matches have only one goal each, so her other 3 goals all came in one odd-numbered match.")),
       ("Bimla’s goals", p("Bimla scored one goal in Match 1 and one in each of three consecutive matches. Matches 4 and 8 already belong to Harita, so the only possible run is Matches 5, 6 and 7.")),
       ("Goals per match", p("The odd matches share 8 goals between them. Trying Harita’s three goals in each odd match, only Match 1 works with the other clues: Matches 1, 3, 5, 7 then have 4, 1, 2, 1 goals. Match 1 is the unique highest, and Matches 3 and 7 are equal but differ from Matches 1 and 5.")),
       ("Who scored where", p("Amla and Sarita’s three goals come one each in Matches 2, 3 and 5."))) +
 table(["Match", "1", "2", "3", "4", "5", "6", "7", "8"],
       [["Goals", "4", "1", "1", "1", "2", "1", "1", "1"], ["Harita", "3", "", "", "1", "", "", "", "1"], ["Bimla", "1", "", "", "", "1", "1", "1", ""],
        ["Amla / Sarita", "", "1", "1", "", "1", "", "", ""]]) +
 final("Totals: Harita 5, Bimla 4, and Amla and Sarita 1 and 2 between them, scored in Matches 2, 3 and 5."),
 p("The totals clue is the key: only two sets of four different totals make 12, and Bimla’s four goals settle which one it is."),
 p("<b>Distinct totals:</b> when a few people have different totals that add to a small number, list the possible sets first. There are usually only one or two."))
P.dq(6, "How many goals were scored in Match 7?", ["3", "1", "2", "Cannot be determined"], "MCQ", "2", "Medium",
 "Only one arrangement of goals in the odd matches fits all the clues.",
 steps(("From the table", p("Match 7 had just Bimla’s goal."))) + final("1, option 2"),
 [("1", "Three goals in Match 7 would make Matches 3 and 7 the equal highest, which clue 6 rules out."), ("3", "The arrangement doesn’t allow two goals in Match 7."), ("4", "The clues fix the arrangement completely.")])
P.dq(7, "Which of the following is the correct sequence of goals scored in matches 1, 3, 5 and 7?", ["5, 1, 0, 1", "3, 1, 2, 1", "4, 1, 2, 1", "3, 2, 1, 2"], "MCQ", "3", "Medium",
 "Bimla scored in Match 5, so it can’t have zero goals, and the odd matches together have 8 goals.",
 steps(("From the table", p("Match 1: 4 goals, Match 3: 1, Match 5: 2, Match 7: 1."))) + final("4, 1, 2, 1, option 3"),
 [("1", "Bimla scored in Match 5, so it can’t have 0 goals."), ("2", "These add up to 7, but the odd matches must share 8 goals."), ("4", "Match 1 has Harita’s three goals and Bimla’s goal, so it can’t have only 3.")])
P.dq(8, "Which of the following statement(s) is/are true?<br>Statement-1: Amla and Sarita never scored goals in the same match.<br>Statement-2: Harita and Sarita never scored goals in the same match.", ["None of the statements", "Statement-1 only", "Statement-2 only", "Both the statements"], "MCQ", "4", "Medium",
 "Amla and Sarita’s goals come one at a time in Matches 2, 3 and 5. Where did Harita score?",
 steps(("Checking each statement", p("Matches 2, 3 and 5 each have just one goal from Amla or Sarita, so they never scored in the same match. Harita scored only in Matches 1, 4 and 8, which Sarita never scored in. Both statements are true."))) + final("Both, option 4"),
 [("1", "Both statements hold."), ("2", "Statement 2 is also true."), ("3", "Statement 1 is also true.")])
P.dq(9, "Which of the following statement(s) is/are false?<br>Statement-1: In every match, at least one player scored a goal.<br>Statement-2: No two players scored goals in the same number of matches.", ["Statement-2 only", "None of the statements", "Both the statements", "Statement-1 only"], "MCQ", "2", "Medium",
 "Look at the goals-per-match row, then count how many matches each player scored in.",
 steps(("Statement 1", p("Every match in the table has at least one goal, so it is true.")),
       ("Statement 2", p("Harita scored in 3 matches and Bimla in 4. Amla and Sarita share Matches 2, 3 and 5, so one scored in 2 matches and the other in 1. All four numbers are different, so this is true too."))) +
 final("Neither is false, option 2"),
 [("1", "Statement 2 is true: the counts are 3, 4, 2 and 1."), ("3", "Both statements are true."), ("4", "Statement 1 is true: no match is goalless.")])
P.dq(10, "If Harita scored goals in one more match as compared to Sarita, which of the following statement(s) is/are necessarily true?<br>Statement-1: Amla scored goals in consecutive matches.<br>Statement-2: Sarita scored goals in consecutive matches.", ["None of the statements", "Both the statements", "Statement-1 only", "Statement-2 only"], "MCQ", "1", "Hard",
 "Harita scored in 3 matches, so Sarita scored in 2 and Amla in 1.",
 steps(("What the condition tells us", p("Sarita scored in two of Matches 2, 3 and 5, and Amla in the remaining one.")),
       ("Checking the statements", p("Amla scored in only one match, so she can’t have scored in consecutive matches. Sarita could have scored in Matches 2 and 3, which are consecutive, but she could equally have scored in 3 and 5 or in 2 and 5. So neither statement must be true."))) +
 final("None, option 1"),
 [("2", "Neither statement has to hold."), ("3", "Amla scored in just one match."), ("4", "Sarita might have scored in Matches 3 and 5, which aren’t consecutive.")])

# ---------------- Set 3: Funding tokens ----------------
P.dilr_set(3, "Set 3 — Tokens and funding", "Answer the questions based on the following information.",
 p("Adhara, Bithi, Chhaya, Dhanavi, Esther, and Fathima are the interviewers in a process that awards funding for new initiatives. Every interviewer individually interviews each of the candidates individually and awards a token only if she recommends funding. A token has a face value of 2, 3, 5, 7, 11, or 13. Each interviewer awards tokens of a single face value only. Once all six interviews are over for a candidate, the candidate receives a funding that is ₹ 1000 times the product of the face values of all the tokens. For example, if a candidate has tokens with face values 2, 5, and 7, then they get a funding of ₹ 1000 × (2 × 5 × 7) = ₹ 70,000.") +
 p("Pragnyaa, Qahira, Rasheeda, Smera, and Tantra were five candidates who received funding. The funds they received in descending order, were ₹ 390,000, ₹ 210,000, ₹ 165,000, ₹ 77,000, and ₹ 66,000.") +
 p("The following additional facts are known:") +
 "<ol><li>Fathima awarded tokens to everyone except Qahira, while Adhara awarded tokens to no one except Pragnyaa.</li><li>Rasheeda received the highest number of tokens that anyone received, but she did not receive one from Esther.</li><li>Bithi awarded a token to Smera but not to Qahira, while Dhanavi awarded a token to Qahira but not to Smera.</li></ol>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("Breaking the amounts into primes", p("Dividing by 1000: 390 = 2 × 3 × 5 × 13, 210 = 2 × 3 × 5 × 7, 165 = 3 × 5 × 11, 77 = 7 × 11 and 66 = 2 × 3 × 11. Each prime in a product is one token, so the primes show exactly which face values each candidate received.")),
       ("Adhara and Fathima", p("Adhara gave a token only to Pragnyaa, so her value appears in just one product. Only 13 does that, so Adhara is 13 and Pragnyaa got 390. Fathima gave tokens to four candidates; only 3 appears in exactly four products, so Fathima is 3, and the candidate without a 3, the 77, is Qahira.")),
       ("Rasheeda and Esther", p("Rasheeda has the most tokens, four, and Pragnyaa already has 390, so Rasheeda has 210 = 2 × 3 × 5 × 7. She got nothing from Esther, so Esther’s value is not 2, 3, 5 or 7. With 13 taken, Esther is 11.")),
       ("The rest", p("Qahira’s 77 is 7 × 11, and Dhanavi gave her a token, so Dhanavi is 7. Bithi and Chhaya are 2 and 5 in some order. Smera and Tantra are 165 and 66 in some order. Bithi gave Smera a token, so if Smera has 165, Bithi is 5, and if Smera has 66, Bithi is 2."))) +
 table(["Candidate", "Amount", "Tokens"], [["Pragnyaa", "₹ 3,90,000", "2, 3, 5, 13"], ["Rasheeda", "₹ 2,10,000", "2, 3, 5, 7"], ["Qahira", "₹ 77,000", "7, 11"], ["Smera / Tantra", "₹ 1,65,000 and ₹ 66,000", "3, 5, 11 and 2, 3, 11"]]) +
 final("Adhara 13, Fathima 3, Esther 11, Dhanavi 7; Bithi and Chhaya are 2 and 5 in some order."),
 p("Count how many products each prime appears in. Adhara’s “only one candidate” and Fathima’s “all but one” match a unique prime each, and the rest follows quickly."),
 p("<b>Prime factorisation in DILR:</b> when a value is a product of distinct primes, each prime is a separate piece of information. Counting how often each prime appears often identifies who is who."))
P.dq(11, "How many tokens did Qahira receive?", [], "TITA", "2", "Easy",
 "Qahira is the candidate without a 3 in her amount.", steps(("Reading it off", p("77 = 7 × 11, so Qahira received two tokens."))) + final(r"\(2\)"))
P.dq(12, "Who among the following definitely received a token from Bithi but not from Dhanavi?", ["Qahira", "Pragnyaa", "Rasheeda", "Tantra"], "MCQ", "2", "Medium",
 "Dhanavi’s value is 7, and Bithi’s is either 2 or 5. Who has both 2 and 5 but no 7?",
 steps(("Checking", p("Pragnyaa’s tokens are 2, 3, 5, 13. She has both 2 and 5, so she received Bithi’s token whichever value Bithi has, and she has no 7, so nothing from Dhanavi."))) + final("Pragnyaa, option 2"),
 [("1", "Qahira received Dhanavi’s 7 and nothing from Bithi."), ("3", "Rasheeda received a 7 from Dhanavi."), ("4", "Tantra may or may not have Bithi’s token, depending on which amount is hers.")])
P.dq(13, "How many tokens did Chhaya award?", [], "TITA", "3", "Medium",
 "Chhaya’s value is whichever of 2 and 5 Bithi doesn’t have. Count how many amounts contain each.",
 steps(("Both cases", p("2 appears in 390, 210 and 66. 5 appears in 390, 210 and 165. Either way, Chhaya awarded 3 tokens."))) + final(r"\(3\)"))
P.dq(14, "How many tokens did Smera receive?", [], "TITA", "3", "Easy",
 "Smera has either 165 or 66.", steps(("Both cases", p("165 = 3 × 5 × 11 and 66 = 2 × 3 × 11 each have three factors, so Smera received 3 tokens."))) + final(r"\(3\)"))
P.dq(15, "Which of the following could be the amount of funding that Tantra received?<br>(a) ₹ 66,000<br>(b) ₹ 165,000", ["Both (a) and (b)", "Neither (a) nor (b)", "Only (b)", "Only (a)"], "MCQ", "1", "Medium",
 "Is anything stopping either arrangement of Smera and Tantra?",
 steps(("Both work", p("If Smera has 165, Bithi is 5 and Tantra has 66. If Smera has 66, Bithi is 2 and Tantra has 165. Both arrangements fit every clue."))) + final("Both, option 1"),
 [("2", "Both amounts are possible."), ("3", "Tantra could also have 66."), ("4", "Tantra could also have 165.")])

# ---------------- Set 4: Get-together ----------------
P.dilr_set(4, "Set 4 — Who wants to come to the get-together", "Answer the questions based on the following information.",
 p("There are 15 girls and some boys among the graduating students in a class. They are planning a get-together, which can be either a 1-day event, or a 2-day event, or a 3-day event. There are 6 singers in the class; 4 of them are boys. There are 10 dancers in the class; 4 of them are girls. No dancer in the class is a singer.") +
 p("Some students are not interested in attending the get-together. Those students who are interested in attending a 3-day event are also interested in attending a 2-day event; those who are interested in attending a 2-day event are also interested in attending a 1-day event.") +
 p("The following facts are also known:") +
 "<ol><li>All the girls and 80% of the boys are interested in attending a 1-day event. 60% of the boys are interested in attending a 2-day event.</li><li>Some of the girls are interested in attending a 1-day event, but not a 2-day event; some of the other girls are interested in attending both.</li><li>70% of the boys who are interested in attending a 2-day event are neither singers nor dancers. 60% of the girls who are interested in attending a 2-day event are neither singers nor dancers.</li><li>No girl is interested in attending a 3-day event. All male singers and 2 of the dancers are interested in attending a 3-day event.</li><li>The number of singers interested in attending a 2-day event is one more than the number of dancers interested in attending a 2-day event.</li></ol>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("The number of boys", p(r"Boys interested in a 2-day event are \(0.6b\), and 70% of them, \(0.42b\), are neither singers nor dancers. For \(0.42b = \tfrac{21b}{50}\) to be a whole number, \(b\) must be a multiple of 50. With \(b = 100\) there would be 18 singing or dancing boys at the 2-day level, but there are only 10 such boys. So \(b = 50\).")),
       ("Boys at the 2-day level", p("That is 30 boys: 21 are neither, and 9 sing or dance. All 4 male singers are in (they want 3 days, so they also want 2), which leaves 5 male dancers.")),
       ("Girls at the 2-day level", p(r"If \(g\) girls are interested in 2 days, 60% of them are neither, so \(g\) is 5 or 10, and \(0.4g\) of them sing or dance. Now use clue 5: singers at 2 days \(= 4 + \) female singers, dancers \(= 5 + \) female dancers, and singers are one more. That forces 2 female singers and 0 female dancers, so \(0.4g = 2\) and \(g = 5\).")),
       ("The 1-day level", p("Forty boys want a 1-day event: the 30 above plus 10 more, drawn from the 1 remaining male dancer and the 19 remaining boys who neither sing nor dance."))) +
 table(["", "Boys", "Girls", "Class"], [["Total", "50", "15", "65"], ["Interested in 1 day", "40", "15", "55"], ["Interested in 2 days", "30", "5", "35"],
        ["2-day: singers / dancers / neither", "4 / 5 / 21", "2 / 0 / 3", ""]]) +
 final("50 boys; 35 of the 65 students want a 2-day event."),
 p("The 70% clue fixes the number of boys straight away, because 0.42b has to be a whole number and there are only ten singing or dancing boys."),
 p("<b>Percentages of percentages:</b> when one percentage applies to a group that is itself a percentage, multiply them. The product must give whole numbers, which often pins down the total."))
P.dq(16, "How many boys are there in the class?", [], "TITA", "50", "Medium",
 "70% of 60% of the boys has to be a whole number.", steps(("Solving", p(r"\(0.42b\) must be whole, so \(b\) is a multiple of 50, and 100 is too many for the 10 singing or dancing boys. So \(b = 50\)."))) + final(r"\(50\)"))
P.dq(17, "Which of the following can be determined from the given information?<br>I. The number of boys who are interested in attending a 1-day event and are neither dancers nor singers.<br>II. The number of female dancers who are interested in attending a 1-day event.", ["Neither I nor II", "Only II", "Only I", "Both I and II"], "MCQ", "2", "Medium",
 "All the girls want a 1-day event. Is that also true of the boys who neither sing nor dance?",
 steps(("Statement I", p("The 10 extra 1-day boys can include the one remaining male dancer or not, so the number of 1-day boys who neither sing nor dance is either 30 or 31. It isn’t fixed.")),
       ("Statement II", p("Every girl wants a 1-day event, so all 4 female dancers do. This is fixed."))) + final("Only II, option 2"),
 [("1", "Statement II can be determined."), ("3", "Statement I can’t be determined."), ("4", "Statement I can’t be determined.")])
P.dq(18, "What fraction of the class is interested in attending a 2-day event?", [r"\(\dfrac{9}{13}\)", r"\(\dfrac{2}{3}\)", r"\(\dfrac{7}{10}\)", r"\(\dfrac{7}{13}\)"], "MCQ", "4", "Medium",
 "Thirty boys and five girls want a 2-day event, out of 65 students.",
 steps(("Computing", p(r"\(\dfrac{30 + 5}{65} = \dfrac{35}{65} = \dfrac{7}{13}\)"))) + final(r"\(\tfrac{7}{13}\), option 4"),
 [("1", "This would need 45 students at the 2-day level."), ("2", "This doesn’t come from the class of 65."), ("3", "This uses the wrong total.")])
P.dq(19, "What BEST can be concluded about the number of male dancers who are interested in attending a 1-day event?", ["6", "4 or 6", "5", "5 or 6"], "MCQ", "4", "Medium",
 "Five male dancers are already counted at the 2-day level. What about the sixth?",
 steps(("Counting", p("The 5 male dancers who want 2 days also want 1 day. The sixth may or may not be among the 10 extra 1-day boys. So the number is 5 or 6."))) + final("5 or 6, option 4"),
 [("1", "The sixth male dancer might not be interested."), ("2", "At least 5 are interested, so 4 is impossible."), ("3", "The sixth could also be interested.")])
P.dq(20, "How many female dancers are interested in attending a 2-day event?", ["Cannot be determined", "2", "1", "0"], "MCQ", "4", "Medium",
 "Use clue 5: singers at the 2-day level are one more than dancers.",
 steps(("From clue 5", p("4 + female singers = 5 + female dancers + 1, so female singers = female dancers + 2. With only 2 female singers, female dancers must be 0."))) + final("0, option 4"),
 [("1", "Clue 5 settles it."), ("2", "That is the number of female singers at the 2-day level."), ("3", "This would need 3 female singers, but there are only 2.")])
