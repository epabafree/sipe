# -*- coding: utf-8 -*-
# Batch 10 — CAT 2021 Slot 3: DILR sets 1–4 (Q1–20, exam order).
from fmt import steps, final, trap, why, table, p
from b10_21s3 import P

# ---------------- Set 1: Testing bottles ----------------
P.dilr_set(1, "Set 1 — Testing bottles for impurity", "Read the following passage carefully and answer the questions that follow.",
 p("Each of the bottles mentioned in this question contains 50 ml of liquid. The liquid in any bottle can be 100% pure content (P) or can have certain amount of impurity (I). Visually it is not possible to distinguish between P and I. There is a testing device which detects impurity, as long as the percentage of impurity in the content tested is 10% or more.") +
 p("For example, suppose bottle 1 contains only P, and bottle 2 contains 80% P and 20% I. If content from bottle 1 is tested, it will be found out that it contains only P. If content of bottle 2 is tested, the test will reveal that it contains some amount of I. If 10 ml of content from bottle 1 is mixed with 20 ml content from bottle 2, the test will show that the mixture has impurity, and hence we can conclude that at least one of the two bottles has I. However, if 10 ml of content from bottle 1 is mixed with 5 ml of content from bottle 2, the test will not detect any impurity in the resultant mixture."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("How a test works", p("A test only answers yes or no: is the impurity in the sample at least 10%? Mixing samples dilutes them, so you can choose the proportions to make a test sensitive to exactly what you want to know.")),
       ("Counting tests", p("Each test gives one yes/no answer, so telling apart k possibilities needs at least as many tests as it takes to get k different answer patterns."))) +
 final("Each question is a separate puzzle about designing tests."),
 p("Think about what concentration a mixture would have in each possible case, and choose amounts so that the cases fall on different sides of 10%."),
 p("<b>Threshold tests:</b> a yes/no test with a cut-off can still separate many cases if you control how much of each sample goes in."))
P.dq(1, "5 ml of content from bottle A is mixed with 5 ml of content from bottle B. The resultant mixture, when tested, detects the presence of I. If it is known that bottle A contains only P, what BEST can be concluded about the volume of I in bottle B?",
 ["Less than 1 ml", "10 ml", "10 ml or more", "1 ml"], "MCQ", "3", "Easy",
 "The 10 ml mixture has at least 10% impurity, all of it from B.",
 steps(("The sample", p("At least 1 ml of the 10 ml is impurity, and it all came from B’s 5 ml. So B is at least 20% impurity.")),
       ("Bottle B", p("20% of 50 ml is 10 ml, so B has 10 ml of I or more."))) + final("10 ml or more, option 3"),
 [("1", "Too little to be detected."), ("2", "It could be more than 10 ml."), ("4", "That is the minimum in the sample, not in the bottle.")])
P.dq(2, "There are four bottles. Each bottle is known to contain only P or only I. They will be considered to be “collectively ready for despatch” if all of them contain only P. In minimum how many tests, is it possible to ascertain whether these four bottles are “collectively ready for despatch”?", [], "TITA", "1", "Easy",
 "Mix equal amounts from all four.",
 steps(("One test", p("If any bottle is pure I, an equal-parts mixture is at least 25% impurity and the test detects it. If nothing is detected, all four are pure P."))) + final(r"\(1\)"))
P.dq(3, "There are four bottles. It is known that three of these bottles contain only P, while the remaining one contains 80% P and 20% I. What is the minimum number of tests required to definitely identify the bottle containing some amount of I?", [], "TITA", "2", "Medium",
 "There are four possibilities and each test is a yes or no.",
 steps(("At least two", p("One yes/no test can only split four possibilities into two groups, so one test isn’t enough.")),
       ("Two is enough", p("Mix equal amounts of bottles 1 and 2 (10% impurity if either is the bad one). If impurity shows, test bottle 1 alone; if not, test bottle 3 alone. Either way the bottle is found."))) + final(r"\(2\)"))
P.dq(4, "There are four bottles. It is known that either one or two of these bottles contain(s) only P, while the remaining ones contain 85% P and 15% I. What is the minimum number of tests required to ascertain the exact number of bottles containing only P?",
 ["2", "4", "3", "1"], "MCQ", "4", "Medium",
 "Mix equal amounts from all four and work out the impurity in each case.",
 steps(("The two cases", p("One pure bottle: three impure, so the mixture is 15% × 3/4 = 11.25%, which is detected. Two pure bottles: 15% × 2/4 = 7.5%, not detected.")),
       ("So", p("A single test of the full mixture tells the two cases apart."))) + final("1, option 4"),
 [("1", "One is enough."), ("2", "One is enough."), ("3", "One is enough.")])

# ---------------- Set 2: Dhoni's schedule ----------------
P.dilr_set(2, "Set 2 — Five projects in 2020", "Read the following passage and bar graph carefully and answer the questions that follow.",
 '<p class="fig"><img src="sipe_2021S3_DILR_S2.svg" alt="Schedule for 2020 (months inclusive, completion %): Project 1 — Abani Feb–Mar 100%, Bahni Feb–Mar 100%, Tinni Jan–Feb 80%. Project 2 — Danni Feb–Apr 90%, Tinni Mar–Apr 100%. Project 3 — Abani May–Jun 100%, Bahni Apr–Jul 75%, Danni Jun–Aug 100%. Project 4 — Abani Jul–Nov 80%, Danni Sep–Oct 100%, Tinni Jul–Sep 100%. Project 5 — Bahni Oct–Dec 90%, Danni Dec 100%, Tinni Sep–Oct 100%."></p>' +
 p("The figure above shows the schedule of four employees – Abani, Bahni, Danni and Tinni – whom Dhoni supervised in 2020. Altogether there were five projects which started and concluded in 2020 in which they were involved. For each of these projects and for each employee, the starting day was at the beginning of a month and the concluding day was the end of a month, and these are indicated by the left and right end points of the corresponding horizontal bars. The number within each bar indicates the percentage of assigned work completed by the employee for that project, as assessed by Dhoni.") +
 p("For each employee, his/her total project-month (in 2020) is the sum of the number of months (s)he worked across the five project, while his/her annual completion index is the weightage average of the completion percentage assigned from the different projects, with the weights being the corresponding number of months (s)he worked in these projects. For each project, the total employee-month is the sum of the number of months four employees worked in this project, while its completion index is the weightage average of the completion percentage assigned for the employees who worked in this project, with the weights being the corresponding number of months they worked in this project."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Reading the bars", table(["Employee", "Projects (months)", "Total months"],
          [["Abani", "P1 Feb–Mar (2, 100%), P3 May–Jun (2, 100%), P4 Jul–Nov (5, 80%)", "9"],
           ["Bahni", "P1 Feb–Mar (2, 100%), P3 Apr–Jul (4, 75%), P5 Oct–Dec (3, 90%)", "9"],
           ["Danni", "P2 Feb–Apr (3, 90%), P3 Jun–Aug (3, 100%), P4 Sep–Oct (2, 100%), P5 Dec (1, 100%)", "9"],
           ["Tinni", "P1 Jan–Feb (2, 80%), P2 Mar–Apr (2, 100%), P4 Jul–Sep (3, 100%), P5 Sep–Oct (2, 100%)", "9"]])),
       ("By project", table(["Project", "Runs", "Duration", "Employee-months"],
          [["1", "Jan–Mar", "3", "6"], ["2", "Feb–Apr", "3", "5"], ["3", "Apr–Aug", "5", "9"], ["4", "Jul–Nov", "5", "10"], ["5", "Sep–Dec", "4", "6"]]))) +
 final("Everything comes from these two tables."),
 p("Count months inclusively: a bar from Feb 1 to Apr 1 covers February and March, two months."),
 p("<b>Weighted averages:</b> weight each percentage by its months, add, and divide by the total months."))
P.dq(5, "Which of the following statements is/are true?<br>I: The total project-month was the same for the four employees.<br>II: The total employee-month was the same for the five projects.",
 ["Only II", "Neither I nor II", "Both I and II", "Only I"], "MCQ", "4", "Easy",
 "Add months by employee, then by project.",
 steps(("Statement I", p("Each employee has 9 project-months. True.")),
       ("Statement II", p("The projects have 6, 5, 9, 10 and 6 employee-months. False."))) + final("Only I, option 4"),
 [("1", "II is false."), ("2", "I is true."), ("3", "II is false.")])
P.dq(6, "Which employees did not work in multiple projects for any of the months in 2020?",
 ["All four of them", "Only Tinni", "Only Abani and Bahni", "Only Abani, Bahni and Danni"], "MCQ", "4", "Easy",
 "Look for overlapping bars in each employee’s row.",
 steps(("Checking", p("Tinni works on Project 4 (Jul–Sep) and Project 5 (Sep–Oct): both in September. Abani, Bahni and Danni never overlap."))) + final("Option 4"),
 [("1", "Tinni overlaps in September."), ("2", "Tinni is the one who did overlap."), ("3", "Danni doesn’t overlap either.")])
P.dq(7, "The project duration, measured in terms of the number of months, is the time during which at least one employee worked in the project. Which of the following pairs of the projects had the same duration?",
 ["Project 3, Project 5", "Project 1, Project 5", "Project 4, Project 5", "Project 3, Project 4"], "MCQ", "4", "Easy",
 "Find the first and last month of each project.",
 steps(("Durations", p("Project 1: 3, Project 2: 3, Project 3: 5 (Apr–Aug), Project 4: 5 (Jul–Nov), Project 5: 4 (Sep–Dec)."))) + final("Projects 3 and 4, option 4"),
 [("1", "5 and 4."), ("2", "3 and 4."), ("3", "5 and 4.")])
P.dq(8, "The list of employees in decreasing order of annual completion index is:",
 ["Danni, Tinni, Abani, Bahni", "Tinni, Danni, Abani, Bahni", "Bahni, Abani, Tinni, Danni", "Danni, Tinni, Bahni, Abani"], "MCQ", "1", "Medium",
 "Each employee has 9 months, so compare the weighted totals.",
 steps(("Weighted totals", p("Abani: 200 + 200 + 400 = 800. Bahni: 200 + 300 + 270 = 770. Danni: 270 + 300 + 200 + 100 = 870. Tinni: 160 + 200 + 300 + 200 = 860.")),
       ("Order", p("Danni, Tinni, Abani, Bahni."))) + final("Option 1"),
 [("2", "Danni is just ahead of Tinni."), ("3", "Roughly the reverse."), ("4", "Abani is ahead of Bahni.")])

# ---------------- Set 3: Javelin ----------------
R1 = table(["Player", "Distance (in m)"], [["P1", "82.9"], ["P3", "81.5"], ["P5", "86.4"], ["P6", "82.5"], ["P7", "87.2"], ["P9", "84.1"]])
R3 = table(["Player", "Distance (in m)"], [["P1", "88.6"], ["P3", "79.0"], ["P9", "81.4"]])
P.dilr_set(3, "Set 3 — A javelin event", "Read the following passage and tables carefully and answer the questions that follow.",
 p("10 players – P1, P2, … , P10 – competed in an international javelin throw event. The number (after P) of a player reflects his rank at the beginning of the event, with rank 1 going to the topmost player. There were two phases in the event with the first phase consisting of rounds 1, 2 and 3, and the second phase consisting of rounds 4, 5 and 6. A throw is measured in terms of the distance it covers (in meters, up to one decimal point accuracy), only if the throw is a ‘valid’ one. For an invalid throw, the distance is taken as zero. A player’s score at the end of a round is the maximum distance of all his throws up to that round. Players are re-ranked after every round based on their current scores. In case of a tie in scores, the player with a prevailing higher rank retains the higher rank. This ranking determines the order in which the players go for their throws in the next round.") +
 p("In each of the rounds in the first phase, the players throw in increasing order of their latest rank, i.e., the player ranked 1 at that point throws first, followed by the player ranked 2 at that point and so on. The top six players at the end of the first phase qualify for the second phase. In each of the rounds in the second phase, the players throw in decreasing order of their latest rank i.e., the player ranked 6 at that point throws first, followed by the player ranked 5 at that point and so on. The players ranked 1, 2 and 3 at the end of the sixth round receive gold, silver and bronze medals respectively.") +
 p("All the valid throws of the event were of distinct distances (as per stated measurement accuracy). The tables below show distances (in meters) covered by all valid throws in the first and the third round in the event.") +
 p("<b>Distances covered by all the valid throws in the first round</b>") + R1 +
 p("<b>Distances covered by all the valid throws in the third round</b>") + R3 +
 p("The following facts are also known.") +
 "<ol type=\"i\"><li>Among the throws in the second round, only the last two were valid. Both the throws enabled these players to qualify for the second phase, with one of them qualifying with the least score. None of these players won any medal.</li><li>If a player throws first in a round and he was also the last (among the players in the current round) to throw in the previous round, then the player is said to get a double. Two players got a double.</li><li>In each round of the second phase, exactly one player improved his score. Each of these improvements was by the same amount.</li><li>The gold and bronze medalists improved their scores in the fifth and the sixth rounds respectively. One medal winner improved his score in the fourth round.</li><li>The difference between the final scores of the gold medalist and the silver medalist, as well as the difference between the final scores of the silver medalist and the bronze medalist was 1.0 m.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("After round 1", p("Order: P7 87.2, P5 86.4, P9 84.1, P1 82.9, P6 82.5, P3 81.5, then P2, P4, P8, P10 on zero. So round 2 ends with P8 and P10, the only valid throws. Both qualify, so both beat 82.5.")),
       ("Who can get a double", p("In round 3 the first thrower is whoever leads after round 2; P10 threw last in round 2, so P10 gets a double only if he now leads, which needs more than 87.2. In round 4, the qualifier who threw last among the six in round 3 gets a double if he is now 6th. Later rounds can’t produce one: the leader can’t drop to 6th in a single round.")),
       ("P8 and P10", p("So P10 throws over 87.2, and the other double is P8 in round 4. That needs P8 to sit below P1 (82.9) after round 2 and then be 6th after round 3: P8 is between 82.5 and 82.9, the qualifier with the least score. After round 3 the six are P1 88.6, P10, P7 87.2, P5 86.4, P9 84.1, P8.")),
       ("Medals", p("Gold, silver, bronze are g, g − 1, g − 2. The gold medallist improves in round 5 and the bronze in round 6, each by the same amount d, and a medallist also improves in round 4. Trying the candidates, only one fits: P7 improves in rounds 4 and 5 (87.2 → 88.4 → 89.6, so d = 1.2), P5 improves in round 6 (86.4 → 87.6), and P1 stays at 88.6. P10 stays between 87.2 and 87.6, out of the medals.") +
       table(["Medal", "Player", "Final score"], [["Gold", "P7", "89.6"], ["Silver", "P1", "88.6"], ["Bronze", "P5", "87.6"]]))) +
 final("Doubles: P10 (round 3) and P8 (round 4)."),
 p("Use the ‘double’ rule to work out where P8 and P10 must be; the medal facts then leave one combination."),
 p("<b>Rules about order:</b> when a puzzle defines who throws first and last, work out which rounds can produce the event at all. Here only two rounds can."))
P.dq(9, "Which two players got the double?", ["P8, P10", "P2, P4", "P1, P10", "P1, P8"], "MCQ", "1", "Hard",
 "P10 throws last in round 2.",
 steps(("From the set solution", p("P10 in round 3 and P8 in round 4."))) + final("Option 1"),
 [("2", "Neither qualifies or leads."), ("3", "P1 never throws first after throwing last."), ("4", "P1 never throws first after throwing last.")])
P.dq(10, "Who won the silver medal?", ["P7", "P9", "P1", "P5"], "MCQ", "3", "Hard",
 "Silver must be the medallist who didn’t improve in phase 2.",
 steps(("From the set solution", p("P1, with 88.6."))) + final("P1, option 3"),
 [("1", "P7 won gold."), ("2", "P9 didn’t medal."), ("4", "P5 won bronze.")])
P.dq(11, "Who threw the last javelin in the event?", ["P10", "P9", "P1", "P7"], "MCQ", "4", "Hard",
 "In round 6 the leader after round 5 throws last.",
 steps(("From the set solution", p("After round 5, P7 leads with 89.6, so he throws last in round 6."))) + final("P7, option 4"),
 [("1", "P10 isn’t leading."), ("2", "P9 isn’t leading."), ("3", "P1 is second after round 5.")])
P.dq(12, "What was the final score (in m) of the silver-medalist?", ["87.2", "88.6", "89.6", "88.4"], "MCQ", "2", "Hard",
 "Silver didn’t improve in phase 2.",
 steps(("From the set solution", p("P1 keeps 88.6."))) + final("88.6, option 2"),
 [("1", "P7’s score after phase 1."), ("3", "The gold medallist’s score."), ("4", "P7 after round 4.")])
P.dq(13, "Which of the following can be the final score (in m) of P8?", ["0", "81.9", "85.1", "82.7"], "MCQ", "4", "Hard",
 "P8 is between 82.5 and 82.9.",
 steps(("From the set solution", p("Only 82.7 lies in that range. P8 doesn’t improve in phase 2 (the improvers are P7 and P5)."))) + final("82.7, option 4"),
 [("1", "P8 qualified, so he has a valid throw."), ("2", "Below 82.5, so he wouldn’t qualify."), ("3", "Above 82.9, so there would be no double for P8.")])
P.dq(14, "By how much did the gold medalist improve his score (in m) in the second phase?", ["2.4", "2.0", "1.0", "1.2"], "MCQ", "1", "Hard",
 "P7 improves twice by the same amount.",
 steps(("From the set solution", p("87.2 to 89.6: 2.4 m, in two steps of 1.2."))) + final("2.4, option 1"),
 [("2", "Not 89.6 − 87.2."), ("3", "The gap between medals."), ("4", "One step, not both.")])

# ---------------- Set 4: Reviewers ----------------
P.dilr_set(4, "Set 4 — Reviewing thirteen questions", "Read the following passage carefully and answer the questions that follow.",
 p("Three reviewers Amal, Bimal and Komal are tasked with selecting questions from a pool of 13 questions (Q01 to Q13). Questions can be created by external “subject matter experts” (SMEs) or by one of the three reviewers. Each of the reviewers either approves or disapproves a question that is shown to them. Their decisions lead to eventual acceptance or rejection of the question in the manner described below.") +
 p("If a question is created by an SME, it is reviewed first by Amal, and then by Bimal. If both of them approve the question, then the question is accepted and is not reviewed by Komal. If both disapprove the question, it is rejected and is not reviewed by Komal. If one of them approves the question and the other disapproves it, then the question is reviewed by Komal. Then the question is accepted only if she approves it.") +
 p("A question created by one of the reviewers is decided upon by the other two. If a question is created by Amal, then it is first reviewed by Bimal. If Bimal approves the question, then it is accepted. Otherwise, it is reviewed by Komal. The question is then accepted only if Komal approves it. A similar process is followed for questions created by Bimal, whose questions are first reviewed by Komal, and then by Amal only if Komal disapproves it. Questions created by Komal are first reviewed by Amal, and then, if required, by Bimal.") +
 p("The following facts are known about the review process after its completion.") +
 "<ol><li>Q02, Q06, Q09, Q11, and Q12 were rejected and the other questions were accepted.</li><li>Amal reviewed only Q02, Q03, Q04, Q06, Q08, Q10, Q11 and Q13.</li><li>Bimal reviewed only Q02, Q04, Q06 through Q09, Q12 and Q13.</li><li>Komal reviewed only Q01 through Q05, Q07, Q08, Q09, Q11 and Q12.</li></ol>",
 "DILR::LR::Analytical_Reasoning",
 steps(("Who sees what", p("SME: Amal and Bimal, plus Komal on a split. Amal’s question: Bimal, plus Komal if Bimal says no. Bimal’s: Komal, plus Amal if Komal says no. Komal’s: Amal, plus Bimal if Amal says no.")),
       ("Matching each question", table(["Q", "Reviewed by", "Result", "Creator and votes"],
          [["01", "K", "Accepted", "Bimal; K yes"], ["02", "A, B, K", "Rejected", "SME; split, K no"], ["03", "A, K", "Accepted", "Bimal; K no, A yes"],
           ["04", "A, B, K", "Accepted", "SME; split, K yes"], ["05", "K", "Accepted", "Bimal; K yes"], ["06", "A, B", "Rejected", "SME or Komal; A no, B no"],
           ["07", "B, K", "Accepted", "Amal; B no, K yes"], ["08", "A, B, K", "Accepted", "SME; split, K yes"], ["09", "B, K", "Rejected", "Amal; B no, K no"],
           ["10", "A", "Accepted", "Komal; A yes"], ["11", "A, K", "Rejected", "Bimal; K no, A no"], ["12", "B, K", "Rejected", "Amal; B no, K no"],
           ["13", "A, B", "Accepted", "SME (both yes) or Komal (A no, B yes)"]]))) +
 final("Only Q06 and Q13 have two possible creators; the SME splits leave Amal’s and Bimal’s votes open on Q02, Q04 and Q08."),
 p("The set of reviewers alone nearly identifies each creator. Write the pattern for each creator type, then match."),
 p("<b>Process puzzles:</b> list the possible paths through the process and the trace each one leaves. Then read each item’s trace backwards."))
P.dq(15, "How many questions were DEFINITELY created by Amal?", [], "TITA", "3", "Medium",
 "Amal’s questions are seen only by Bimal and Komal.",
 steps(("From the set solution", p("Q07, Q09 and Q12."))) + final(r"\(3\)"))
P.dq(16, "How many questions were DEFINITELY created by Komal?", [], "TITA", "1", "Medium",
 "A question seen only by Amal can only be Komal’s.",
 steps(("From the set solution", p("Q10 for certain. Q06 and Q13 could be Komal’s or an SME’s."))) + final(r"\(1\)"))
P.dq(17, "How many questions were DEFINITELY created by the SMEs?", [], "TITA", "3", "Medium",
 "Only SME questions can be seen by all three.",
 steps(("From the set solution", p("Q02, Q04 and Q08."))) + final(r"\(3\)"))
P.dq(18, "How many questions were DEFINITELY disapproved by Bimal?", ["3", "4", "5", "7"], "MCQ", "2", "Medium",
 "Include Q06, where Bimal says no in both possible cases.",
 steps(("From the set solution", p("Q07, Q09, Q12 (Amal’s questions that went on to Komal) and Q06. His votes on Q02, Q04 and Q08 aren’t known."))) + final("4, option 2"),
 [("1", "Misses Q06."), ("3", "Counts an SME split as certain."), ("4", "Counts all the splits as certain.")])
P.dq(19, "The approval ratio of a reviewer is the ratio of the number of questions (s)he approved to the number of questions (s)he reviewed. Which option best describes Amal’s approval ratio?",
 ["lies between 0.25 and 0.50", "either 0.25 or 0.75", "0.25", "lies between 0.25 and 0.75"], "MCQ", "4", "Hard",
 "Amal reviewed 8. Count her certain yeses, certain nos, and the open ones.",
 steps(("Amal’s votes", p("Yes: Q03, Q10. No: Q06, Q11. Open: Q02, Q04, Q08 (SME splits) and Q13.")),
       ("Range", p("Anywhere from 2 to 6 approvals out of 8: from 0.25 to 0.75."))) + final("Option 4"),
 [("1", "She could approve up to 6."), ("2", "Values in between are possible too."), ("3", "Only the lowest case.")])
P.dq(20, "How many questions created by Amal or Bimal were disapproved by at least one of the other reviewers?", ["2", "5", "7", "4"], "MCQ", "2", "Medium",
 "Amal’s: Q07, Q09, Q12. Bimal’s: Q01, Q03, Q05, Q11.",
 steps(("Counting", p("Amal’s three were all disapproved by Bimal. Of Bimal’s, Komal disapproved Q03 and Q11. Total 5."))) + final("5, option 2"),
 [("1", "Only Bimal’s."), ("3", "Counts Q01 and Q05, which Komal approved."), ("4", "Misses one.")])
