# -*- coding: utf-8 -*-
# Batch 21 — CAT 2025 Slot 2: DILR sets 1–5 (Q1–22, in exam order).
from fmt import steps, final, trap, why, table, p
from b21_25s2 import P
import b21_25s2_figs as F

DIR = "Read the information given below and answer the questions that follow."

# ---------------- Set 1: Gurus and students ----------------
P.dilr_set(1, "Set 1 — Four musicians and three Gurus", DIR,
 p("Ananya Raga, Bhaskar Tala, Charu Veena, and Devendra Sur are four musicians. Each of them started and completed their training as students under each of three Gurus — Pandit Meghnath, Ustad Samiran, and Acharya Raghunath between 2013 and 2024, including both the years. Each Guru trains any student for consecutive years only, for a span of 2, 3, or 4 years, with each Guru having a different span. During some of these years, a student may not have trained under these Gurus; however, they never trained under multiple Gurus in the same year. In none of these years, any of these Gurus trained more than two of these students at the same time. When two students train under the same Guru at the same time, they are referred to as Gurubhai, irrespective of their gender.") +
 p("The following additional facts are known.") +
 "<ol><li>Ustad Samiran never trained more than one of these students in the same year.</li><li>Acharya Raghunath did not train any of these students during 2015-2018, as well as during 2021-24.</li><li>Ananya and Devendra were never Gurubhai; neither were Bhaskar and Charu. All other pairs of musicians were Gurubhai for exactly 2 years.</li><li>In 2013, Ananya and Bhaskar started their trainings under Pandit Meghnath and under Ustad Samiran, respectively.</li></ol>",
 "DILR::LR::Scheduling",
 steps(("Raghunath’s span", p("He could only teach in 2013–14 and 2019–20, so his span is 2 years, and each student is with him in one of those two blocks. At most two students at a time, so two are with him in 2013–14 and two in 2019–20.")),
       ("Who pairs with whom under Raghunath", p("Ananya is with Meghnath and Bhaskar with Samiran in 2013, so both are with Raghunath in 2019–20: they are Gurubhai there for their 2 years. Charu and Devendra take 2013–14 together, which uses up their 2 years.")),
       ("Samiran and Meghnath", p("Samiran teaches one student at a time, so he can’t create Gurubhai pairs; all the remaining Gurubhai years come from Meghnath. Ananya–Charu and Bhaskar–Devendra each need 2 years together under Meghnath. If Meghnath’s span were 3 (Ananya 2013–15), Charu would need 2014–16 to overlap by 2, but she is with Raghunath in 2014. So Meghnath’s span is 4 (Ananya 2013–16, Charu 2015–18) and Samiran’s is 3.")),
       ("The timetable", table(["", "M", "S", "R"],
          [["Ananya", "13–16", "22–24", "19–20"], ["Bhaskar", "21–24", "13–15", "19–20"], ["Charu", "15–18", "19–21", "13–14"], ["Devendra", "19–22", "16–18", "13–14"]]) +
          p("M, S and R are Meghnath, Samiran and Raghunath; years are 20xx.") +
          p("Gurubhai: Ananya–Bhaskar 2019–20 (Raghunath), Charu–Devendra 2013–14 (Raghunath), Ananya–Charu 2015–16 and Bhaskar–Devendra 2021–22 (Meghnath). No other overlaps."))) +
 final("The timetable is the only one that fits every condition."),
 p("Raghunath’s narrow windows force his span to 2 and split the four students into two pairs. Since Samiran teaches one student at a time, all other Gurubhai years must come from Meghnath."),
 p("<b>Scheduling grids:</b> list each teacher’s possible windows first. A teacher with only a few allowed years usually fixes the whole schedule."))
P.dq(1, "In which of the following years were Ananya and Bhaskar Gurubhai?", ["2021", "2018", "2014", "2020"], "MCQ", "4", "Medium",
 "Both start elsewhere in 2013, so they share Raghunath’s later block.",
 steps(p("Ananya and Bhaskar are with Raghunath in 2019–20.")) + final("2020, option 4"),
 [("1", "In 2021 Ananya isn’t training."), ("2", "In 2018 neither is training."), ("3", "In 2014 they are with different Gurus.")])
P.dq(2, "In which year did Charu begin her training under Pandit Meghnath?", ["2021", "2015", "2016", "2017"], "MCQ", "2", "Hard",
 "Charu must overlap Ananya (2013–16) by exactly 2 years under Meghnath.",
 steps(p("Starting in 2015 gives 2015–18, overlapping Ananya in 2015 and 2016.")) + final("2015, option 2"),
 [("1", "From 2021 she wouldn’t overlap Ananya at all."), ("3", "From 2016 she would overlap Ananya for only one year."), ("4", "From 2017 there is no overlap with Ananya.")])
P.dq(3, "In which of the following years were Bhaskar and Devendra Gurubhai?", ["2018", "2020", "2015", "2022"], "MCQ", "4", "Medium",
 "They overlap under Meghnath.",
 steps(p("Devendra 2019–22 and Bhaskar 2021–24 under Meghnath overlap in 2021 and 2022.")) + final("2022, option 4"),
 [("1", "In 2018 Bhaskar isn’t training."), ("2", "In 2020 Bhaskar is with Raghunath and Devendra with Meghnath."), ("3", "In 2015 Devendra isn’t training.")])
P.dq(4, "Which of the following statements is TRUE?", ["Ananya was training under Ustad Samiran in 2018.", "Charu was training under Ustad Samiran in 2019.", "Ananya was training under Ustad Samiran in 2015.", "Charu was training under Ustad Samiran in 2018."], "MCQ", "2", "Medium",
 "Read Samiran’s column of the timetable.",
 steps(p("Charu was with Samiran in 2019–21.")) + final("Option 2"),
 [("1", "Ananya was with Samiran in 2022–24."), ("3", "In 2015 Ananya was with Meghnath."), ("4", "In 2018 Charu was with Meghnath.")])
P.dq(5, "In how many of the years between 2013-24, were only two of these four musicians training under these three Gurus?", [], "TITA", "4", "Medium",
 "Count, year by year, how many are training.",
 steps(p("2017 and 2018 (Charu and Devendra), 2023 and 2024 (Ananya and Bhaskar). Every other year has three or four students training.")) + final(r"\(4\)"))

# ---------------- Set 2: Sustainability Index ----------------
P.dilr_set(2, "Set 2 — Sustainability index of six countries", DIR,
 p("The Sustainability Index (SI) of a country at a point in time is an integer between 1 and 100. This question is related to SI of six countries – A, B, C, D, E, and F – at three different points in time – 2016, 2020, and 2024. The plot represents the exact changes in their SI, with X-coordinate representing % increase in 2020 from 2016, i.e., (SI in 2020 minus SI in 2016) / (SI in 2016), and Y-coordinate representing % increase in 2024 from 2020. At any point in time, the country with highest SI is ranked 1, while the country with the lowest SI is ranked 6.") + F.SI +
 p("The following additional facts are known.") +
 "<ol><li>In 2016, B, C, E, and A had ranks 1, 2, 3, and 4 respectively.</li><li>F had lower SI than any other country in 2016, 2020, and 2024.</li><li>In 2024, E was the only country with SI of 90.</li><li>The range of SI of the six countries was 60 in 2016 as well as in 2024.</li></ol>",
 "DILR::DI::Graphs_and_Charts",
 steps(("E", p(r"E rose 25% then 20%, so \(1.25 \times 1.2 = 1.5\) times its 2016 value is 90: 60 in 2016, 75 in 2020, 90 in 2024.")),
       ("F", p("In 2024 the range is 60. If E (90) is the top, F is 30. F went ×2 then ×0.75, so it was 20 in 2016 and 40 in 2020.")),
       ("B", p("In 2016 B is top and F (20) is bottom, so B is 80. Then ×0.75 twice: 60 in 2020 and 45 in 2024.")),
       ("C", p(r"C went ×0.8 then ×1.4, so 2016, 2020 and 2024 values are \(c\), \(0.8c\), \(1.12c\). For all three to be whole numbers, c must be a multiple of 25; with 60 < c < 80, c = 75: 75, 60, 84.") +
          table(["", "2016", "2020", "2024"], [["B", "80", "60", "45"], ["C", "75", "60", "84"], ["E", "60", "75", "90"], ["F", "20", "40", "30"]]) +
          p("A and D are ranked 4 and 5 in 2016; their exact values aren’t needed."))) +
 final("B 80 → 60 → 45, C 75 → 60 → 84, E 60 → 75 → 90, F 20 → 40 → 30."),
 p("Start with E: one fixed value (90) and two growth rates give its whole history. The ranges then fix F and B."),
 p("<b>Percentage-change plots:</b> successive changes multiply. A rise of x% then y% is a factor of (1 + x)(1 + y)."))
P.dq(6, "What was the SI of E in 2016?", [], "TITA", "60", "Easy",
 "Undo the 20% rise and then the 25% rise.",
 steps(p(r"\(90 \div 1.2 = 75\) and \(75 \div 1.25 = 60\).")) + final(r"\(60\)"))
P.dq(7, "What was the SI of F in 2020?", [], "TITA", "40", "Medium",
 "F is the lowest in 2024, 60 below E’s 90.",
 steps(p(r"F is 30 in 2024, after a 25% fall: \(30 \div 0.75 = 40\).")) + final(r"\(40\)"))
P.dq(8, "What was the SI of C in 2024?", [], "TITA", "84", "Hard",
 "C’s values must all be whole numbers, with C between E (60) and B (80) in 2016.",
 steps(p(r"\(1.12c\) is whole only if c is a multiple of 25; between 60 and 80 that is 75. So C is \(1.12 \times 75 = 84\) in 2024.")) + final(r"\(84\)"))
P.dq(9, "What was the SI of B in 2024?", ["54", "60", "45", "80"], "MCQ", "3", "Medium",
 "B tops 2016 with F at 20, and the range is 60.",
 steps(p(r"B is 80 in 2016; two 25% falls give 60 and then 45.")) + final("45, option 3"),
 [("1", "This applies only one fall and the wrong rate."), ("2", "60 is B in 2020."), ("4", "80 is B in 2016.")])

# ---------------- Set 3: Pollution measures ----------------
P.dilr_set(3, "Set 3 — Pollution in three states", DIR,
 p("The two most populous cities and the non-urban region (NUR) of each of three states, Whimshire, Fogglia, and Humbleset, are assigned Pollution Measures (PMs). These nine PMs are all distinct multiples of 10, ranging from 10 to 90. The six cities in increasing order of their PMs are: Blusterburg, Noodleton, Splutterville, Quackford, Mumpypore, Zingaloo.") +
 p("The Pollution Index (PI) of a state is a weighted average of the PMs of its NUR and cities, with a weight of 50% for the NUR, and 25% each for its two cities.") +
 p("There is only one pair of an NUR and a city (considering all cities and all NURs) where the PM of the NUR is greater than that of the city. That NUR and the city both belong to Humbleset.") +
 p("The PIs of all three states are distinct integers, with Humbleset and Fogglia having the highest and the lowest PI respectively."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("The low values", p("Only one NUR beats only one city, so the three NURs and Blusterburg take the four lowest PMs, 10 to 40, with Humbleset’s NUR above Blusterburg alone. So Humbleset’s NUR is 40 and Blusterburg is 30, in Humbleset; the other NURs are 10 and 20.")),
       ("The cities", p("The remaining cities take 50, 60, 70, 80 and 90 in order: Noodleton 50, Splutterville 60, Quackford 70, Mumpypore 80, Zingaloo 90.")),
       ("Whole-number PIs", p("NUR/2 is always a whole number, so the two cities of a state must add to a multiple of 4. With PMs 30 to 90 that means their tens digits add to an even number: 60 pairs with 80, and 30, 50, 70, 90 pair among themselves.")),
       ("Which pairing works", p("Humbleset (NUR 40) has Blusterburg 30 plus 50, 70 or 90, and its PI must be the highest. With 50: Humbleset 40, but the others score at least 40. With 70: Humbleset 45 ties with a 45 elsewhere. With 90: Humbleset 50; then Fogglia (lowest) must be NUR 10 with 50 + 70, giving 35, and Whimshire NUR 20 with 60 + 80, giving 45. Every other split ties or puts Fogglia above Whimshire.") +
          "<ul><li>Humbleset: NUR 40, Blusterburg 30, Zingaloo 90; PI 50</li><li>Whimshire: NUR 20, Splutterville 60, Mumpypore 80; PI 45</li><li>Fogglia: NUR 10, Noodleton 50, Quackford 70; PI 35</li></ul>")) +
 final("Every PM and every state is fixed: PIs 50, 45 and 35."),
 p("The single NUR-above-city pair forces the three NURs into the bottom four values. Integer PIs then force the city pairs."),
 p(r"<b>Weighted averages:</b> \(\text{PI} = \tfrac12 N + \tfrac14 (c_1 + c_2)\). For a whole-number PI, the two city values must add to a multiple of 4."))
P.dq(10, "What is the PI of Whimshire?", [], "TITA", "45", "Medium",
 "Whimshire has NUR 20 and cities 60 and 80.",
 steps(p(r"\(10 + \frac{140}{4} = 45\).")) + final(r"\(45\)"))
P.dq(11, "What is the PI of Fogglia?", [], "TITA", "35", "Medium",
 "Fogglia has NUR 10 and cities 50 and 70.",
 steps(p(r"\(5 + \frac{120}{4} = 35\).")) + final(r"\(35\)"))
P.dq(12, "What is the PI of Humbleset?", [], "TITA", "50", "Medium",
 "Humbleset has NUR 40 and cities 30 and 90.",
 steps(p(r"\(20 + \frac{120}{4} = 50\).")) + final(r"\(50\)"))
P.dq(13, "Which pair of cities definitely belong to the same state?", ["Blusterburg, Mumpypore", "Mumpypore, Zingaloo", "Noodleton, Quackford", "Splutterville, Quackford"], "MCQ", "3", "Medium",
 "Use the pairing in the set solution.",
 steps(p("Noodleton (50) and Quackford (70) are both in Fogglia.")) + final("Option 3"),
 [("1", "Blusterburg is with Zingaloo."), ("2", "Mumpypore is with Splutterville."), ("4", "Splutterville is with Mumpypore.")])
P.dq(14, "For how many of the cities and NURs is it possible to identify their PM and the state they belong to?", [], "TITA", "9", "Medium",
 "Is anything left undecided?",
 steps(p("All six cities and three NURs are fixed.")) + final(r"\(9\)"))

# ---------------- Set 4: Research papers ----------------
P.dilr_set(4, "Set 4 — Papers by four authors", DIR,
 p("The following charts depict details of research papers written by four authors, Arman, Brajen, Chintan, and Devon. The papers were of four types, single-author, two-author, three-author, and four-author, that is, written by one, two, three, or all four of these authors, respectively. No other authors were involved in writing these papers.") + F.BY_AUTHOR + F.BY_TYPE +
 p("The following additional facts are known.") +
 "<ol><li>Each of the authors wrote at least one of each of the four types of papers.</li><li>The four authors wrote different numbers of single-author papers.</li><li>Both Chintan and Devon wrote more three-author papers than Brajen.</li><li>The number of single-author and two-author papers written by Brajen were the same.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Four-author and single-author papers", p("The 2 four-author papers count for everyone. The 10 single-author papers are split 1, 2, 3, 4 in some order (four different positive numbers adding to 10).")),
       ("Arman", p("5 papers = 2 four-author + at least 1 of each other type: exactly 1 single, 1 two-author, 1 three-author.")),
       ("Three-author papers", p("There are 3, so 9 author slots. Arman has 1; Chintan and Devon each need more than Brajen, who has at least 1. So Brajen 2, Chintan 3, Devon 3 (2 + 3 + 3 + 1 = 9): the papers are ACD, BCD, BCD.")),
       ("Brajen", p("8 = 2 (four) + 2 (three) + s + t with s = t, so 2 single and 2 two-author.")),
       ("Chintan and Devon", p("They share singles 3 and 4. Two-author slots total 8: Arman 1, Brajen 2, leaving 5 for Chintan and Devon. Chintan: 12 − 2 − 3 = 7 = single + two. Devon: 10 − 2 − 3 = 5 = single + two. So either Chintan 4 + 3, Devon 3 + 2, or Chintan 3 + 4, Devon 4 + 1.") +
          table(["", "1", "2", "3", "4"], [["Arman", "1", "1", "1", "2"], ["Brajen", "2", "2", "2", "2"], ["Chintan", "4/3", "3/4", "3", "2"], ["Devon", "3/4", "2/1", "3", "2"]]) + p("Columns are single-, two-, three- and four-author papers; “4/3” means 4 in the first case and 3 in the second."))) +
 final("Two cases, differing only in Chintan’s and Devon’s single- and two-author counts."),
 p("Arman’s small total fixes his row at once, and the three three-author papers can only be split 1, 2, 3, 3."),
 p("<b>Counting authorships:</b> a paper with k authors adds k to the author totals. Count “slots” per type: two-author papers give 8 slots here, three-author papers 9."))
P.dq(15, "What was the total number of two-author and three-author papers written by Brajen?", [], "TITA", "4", "Medium",
 "Brajen has 2 three-author papers and equal single and two-author counts.",
 steps(p("2 two-author + 2 three-author = 4.")) + final(r"\(4\)"))
P.dq(16, "Which of the following statements is/are NECESSARILY true?<br>i. Chintan wrote exactly three two-author papers.<br>ii. Chintan wrote more single-author papers than Devon.", ["Only ii", "Both i and ii", "Neither i nor ii", "Only i"], "MCQ", "3", "Hard",
 "Check both cases.",
 steps(p("In one case Chintan has 4 singles and 3 two-author papers; in the other, 3 singles and 4 two-author papers (and Devon 4 singles). Neither statement holds in both.")) + final("Neither, option 3"),
 [("1", "In the second case Devon has more singles."), ("2", "Neither holds in both cases."), ("4", "In the second case Chintan has 4 two-author papers.")])
P.dq(17, "Which of the following statements is/are NECESSARILY true?<br>i. Arman wrote three-author papers only with Chintan and Devon.<br>ii. Brajen wrote three-author papers only with Chintan and Devon.", ["Only i", "Neither i or ii", "Only ii", "Both i and ii"], "MCQ", "4", "Medium",
 "What are the three three-author papers?",
 steps(p("They are ACD, BCD and BCD in every case. So Arman’s is with Chintan and Devon, and both of Brajen’s are too.")) + final("Both, option 4"),
 [("1", "ii is also certain."), ("2", "Both are certain."), ("3", "i is also certain.")])
P.dq(18, "If Devon wrote more than one two-author papers, then how many two-author papers did Chintan write?", [], "TITA", "3", "Medium",
 "Which case gives Devon 2 two-author papers?",
 steps(p("Devon with 2 two-author papers means Chintan has 4 singles and 3 two-author papers.")) + final(r"\(3\)"))

# ---------------- Set 5: Balls and hoops ----------------
P.dilr_set(5, "Set 5 — Balls through hoops", DIR,
 p("There are six spherical balls, B1, B2, B3, B4, B5, and B6, and four circular hoops H1, H2, H3, and H4.") +
 p("Each ball was tested on each hoop once, by attempting to pass the ball through the hoop. If the diameter of a ball is not larger than the diameter of the hoop, the ball passes through the hoop and makes a “ping”. Any ball having a diameter larger than that of the hoop gets stuck on that hoop and does not make a ping.") +
 p("The following additional information is known:") +
 "<ol><li>B1 and B6 each made a ping on H4, but B5 did not.</li><li>B4 made a ping on H3, but B1 did not.</li><li>All balls, except B3, made pings on H1.</li><li>None of the balls, except B2, made a ping on H2.</li></ol>",
 "DILR::LR::Analytical_Reasoning",
 steps(("Extremes", p("B3 alone fails on H1, so it is the largest ball, and since every other ball passes H1, H1 is the largest hoop B3 fails on; B3 fails everywhere. B2 alone passes H2, so it is the smallest ball and passes every hoop; H2 is the smallest hoop.")),
       ("Order of balls", p("On H4, B1 and B6 pass but B5 doesn’t: B5 is larger than B1 and B6. On H3, B4 passes but B1 doesn’t: B1 is larger than B4. So B2 < B4 < B1 < B5 < B3, and B6 < B5.")),
       ("Order of hoops", p("H4 lets B1 through but H3 doesn’t, so H3 < H4. H1 lets B5 through but H4 doesn’t, so H4 < H1. Hence H2 < H3 < H4 < H1.")),
       ("Pings", table(["Ball", "H1", "H2", "H3", "H4", "Pings"], [["B1", "✓", "✗", "✗", "✓", "2"], ["B2", "✓", "✓", "✓", "✓", "4"], ["B3", "✗", "✗", "✗", "✗", "0"], ["B4", "✓", "✗", "✓", "✓", "3"], ["B5", "✓", "✗", "✗", "✗", "1"], ["B6", "✓", "✗", "?", "✓", "2 or 3"]]) +
          p("Only B6 on H3 is undecided."))) +
 final("Balls: B2 < B4 < B1 < B5 < B3, with B6 below B5. Hoops: H2 < H3 < H4 < H1. Total pings 12 or 13."),
 p("A ball that fails on the largest hoop is the largest ball; a ball that passes the smallest hoop is the smallest. Each ping/no-ping pair on the same hoop gives one size comparison."),
 p("<b>Ordering from comparisons:</b> if X passes a hoop that Y doesn’t, X is smaller than Y. Chain the comparisons into one order and leave undecided pairs open."))
P.dq(19, "What was the total number of pings made by B1, B2, and B3?", [], "TITA", "6", "Medium",
 "Read their rows in the table.",
 steps(p("B1 2, B2 4, B3 0: 6.")) + final(r"\(6\)"))
P.dq(20, "Which of the following statements about the relative sizes of the balls is NOT NECESSARILY true?", ["B1 &lt; B6 &lt; B3", "B2 &lt; B1 &lt; B5", "B4 &lt; B5 &lt; B3", "B1 &lt; B5 &lt; B3"], "MCQ", "1", "Medium",
 "Where does B6 sit relative to B1?",
 steps(p("B6 is only known to be smaller than B5; it may be smaller or larger than B1.")) + final("Option 1"),
 [("2", "B2 < B4 < B1 < B5 always."), ("3", "B4 < B1 < B5 < B3 always."), ("4", "B1 < B5 < B3 always.")])
P.dq(21, "Which of the following statements about the relative sizes of the hoops is true?", ["H2 &lt; H4 &lt; H3 &lt; H1", "H2 &lt; H3 &lt; H4 &lt; H1", "H1 &lt; H3 &lt; H4 &lt; H2", "H1 &lt; H4 &lt; H3 &lt; H2"], "MCQ", "2", "Medium",
 "B1 passes H4 but not H3.",
 steps(p("H2 is smallest and H1 largest; B1 shows H3 < H4.")) + final("Option 2"),
 [("1", "B1 shows H3 is smaller than H4."), ("3", "H1 is the largest, not the smallest."), ("4", "H1 is the largest.")])
P.dq(22, "What BEST can be said about the total number of pings from all the tests undertaken?", ["12 or 13 or 14", "13 or 14", "At least 9", "12 or 13"], "MCQ", "4", "Medium",
 "Only one test is undecided.",
 steps(p("2 + 4 + 0 + 3 + 1 + 2 = 12, plus 1 if B6 passes H3.")) + final("12 or 13, option 4"),
 [("1", "Only one result is open, so 14 is impossible."), ("2", "12 is possible."), ("3", "True but not the best description.")])
