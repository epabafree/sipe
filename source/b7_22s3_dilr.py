# -*- coding: utf-8 -*-
# Batch 7 — CAT 2022 Slot 3: DILR sets 1–4 (Q1–20, exam order).
from fmt import steps, final, trap, why, table, p
from b7_22s3 import P

# ---------------- Set 1: Mortality study ----------------
_AGES = ["20 – 30", "30 – 40", "40 – 50", "50 – 60", "60 – 70", "70 – 80", "80 – 90"]
_DATA = {  # age group -> (1990, 2000, 2010, 2020) as "males / females"
    "20 – 30": ("230 / 240", "0 / 0", "0 / 0", "0 / 0"),
    "30 – 40": ("235 / 225", "180 / 210", "0 / 0", "0 / 0"),
    "40 – 50": ("210 / 190", "205 / 175", "150 / 160", "0 / 0"),
    "50 – 60": ("190 / 220", "160 / 150", "165 / 145", "140 / 100"),
    "60 – 70": ("0 / 0", "100 / 120", "90 / 100", "125 / 105"),
    "70 – 80": ("0 / 0", "0 / 0", "25 / 30", "50 / 60"),
    "80 – 90": ("0 / 0", "0 / 0", "0 / 0", "5 / 18"),
}
def _half(cols, ages):
    i = [None, "1990", "2000", "2010", "2020"]
    return table(["Age (years)"] + cols, [[a] + [_DATA[a][i.index(c) - 1] for c in cols] for a in ages])
MORT = (_half(["1990", "2000"], _AGES[:5]) + _half(["2010", "2020"], _AGES[2:]) +
        p("<i>Age groups not listed had nobody alive in those years.</i>"))

P.dilr_set(1, "Set 1 — A forty-year mortality study", "Read the following passage carefully and answer the questions that follow.",
 p("In the following, a year corresponds to 1st of January of that year.") +
 p("A study to determine the mortality rate for a disease began in 1980. The study chose 1000 males and 1000 females and followed them for forty years or until they died, whichever came first. The 1000 males chosen in 1980 consisted of 250; each of ages 10 to less than 20, 20 to less than 30, 30 to less than 40, and 40 to less than 50. The 1000 females chosen in 1980 also consisted of 250; each of ages 10 to less than 20, 20 to less than 30, 30 to less than 40, and 40 to less than 50.") +
 p("The four figures given below depict the age profile of those among the 2000 individuals who were still alive in 1990, 2000, 2010, and 2020. The blue bars in each figure represent the number of males in each age group at that point in time, while the pink bars represent the number of females in each age group at that point in time. The numbers next to the bars give the exact numbers being represented by the bars. For example, we know that 230 males among those tracked and who were alive in 1990 were aged between 20 and 30.") +
 p("<i>The four bar charts are given here as two tables. Each cell shows males / females alive in that age group in that year.</i>") + MORT,
 "DILR::DI::Graphs_and_Charts",
 steps(("Following each group", p("Each group of 250 moves up one age band every ten years. So a row of the table, read diagonally down to the right, follows the same people. The group aged 10–20 in 1980 is in the 20–30 band in 1990, 30–40 in 2000, and so on.")),
       ("The four groups over time", table(["Aged in 1980", "1990", "2000"],
          [["10 – 20", "230 / 240", "180 / 210"], ["20 – 30", "235 / 225", "205 / 175"], ["30 – 40", "210 / 190", "160 / 150"], ["40 – 50", "190 / 220", "100 / 120"]]) +
          table(["Aged in 1980", "2010", "2020"],
          [["10 – 20", "150 / 160", "140 / 100"], ["20 – 30", "165 / 145", "125 / 105"], ["30 – 40", "90 / 100", "50 / 60"], ["40 – 50", "25 / 30", "5 / 18"]]) +
          p("Each group started with 250 males and 250 females in 1980. Deaths in a decade are the drop from one year to the next."))) +
 final("Every question is a lookup or a subtraction in these tables."),
 p("Rewrite the charts by starting group rather than by age band. After that, survivors are a single cell and deaths are a difference of two cells."),
 p("<b>Tracking groups over time:</b> when everyone ages together, follow each group along the diagonal instead of reading the charts year by year."))
P.dq(1, "In 2000, what was the ratio of the number of dead males to dead females among those being tracked?",
 ["129 : 131", "71 : 69", "109 : 107", "41 : 43"], "MCQ", "2", "Easy",
 "Add up the survivors in 2000 and subtract from 1000 for each sex.",
 steps(("Survivors in 2000", p("Males: 180 + 205 + 160 + 100 = 645. Females: 210 + 175 + 150 + 120 = 655.")),
       ("Deaths", p("Males: 1000 − 645 = 355. Females: 1000 − 655 = 345. The ratio 355 : 345 simplifies to 71 : 69."))) + final("71 : 69, option 2"),
 [("1", "Not equal to 355 : 345."), ("3", "Not equal to 355 : 345."), ("4", "This would mean more women died than men; it is the other way round.")])
P.dq(2, "How many people who were being tracked and who were between 30 and 40 years of age in 1980 survived until 2010?",
 ["90", "310", "190", "110"], "MCQ", "3", "Easy",
 "In 2010 this group is in the 60–70 band.",
 steps(("Reading it", p("In 2010 the 60–70 band has 90 males and 100 females: 190 people."))) + final("190, option 3"),
 [("1", "Males only."), ("2", "This is the 2000 figure (160 + 150)."), ("4", "Not a sum of any matching cells.")])
P.dq(3, "How many individuals who were being tracked and who were less than 30 years of age in 1980 survived until 2020?",
 ["580", "470", "240", "230"], "MCQ", "2", "Easy",
 "Two groups were under 30 in 1980. In 2020 they are in the 50–60 and 60–70 bands.",
 steps(("Adding", p("50–60 in 2020: 140 + 100 = 240. 60–70 in 2020: 125 + 105 = 230. Together 470."))) + final("470, option 2"),
 [("1", "Too many; this would need survivors from older groups."), ("3", "Only the group aged 10–20 in 1980."), ("4", "Only the group aged 20–30 in 1980.")])
P.dq(4, "How many of the males who were being tracked and who were between 20 and 30 years of age in 1980 died in the period 2000 to 2010?", [], "TITA", "40", "Easy",
 "This group of males is in the 40–50 band in 2000 and the 50–60 band in 2010.",
 steps(("Subtracting", p("205 alive in 2000, 165 alive in 2010: 40 died in between."))) + final(r"\(40\)"))
P.dq(5, "How many of the females who were being tracked and who were between 20 and 30 years of age in 1980 died between the ages of 50 and 60?", [], "TITA", "30", "Hard",
 "Women aged 20–30 in 1980 were 40–50 in 2000 and 50–60 in 2010. The official answer takes the deaths between those two years.",
 steps(("The intended reading", p("The answer key treats this group as reaching the 50–60 band over 2000–2010: 175 alive in 2000 and 145 in 2010, so 30 died.")),
       ("Why it isn’t clear-cut", p("Strictly, these women were aged 50–60 between 2010 and 2020 (they were in the 50–60 band in 2010), and 145 − 105 = 40 died then. The wording allows both readings, but the official answer is 30."))) +
 final(r"\(30\) (official answer)"))

# ---------------- Set 2: Neighbourhoods ----------------
P.dilr_set(2, "Set 2 — New cases in four neighbourhoods", "Read the following passage carefully and answer the questions that follow.",
 p("There are only four neighbourhoods in a city - Levmisto, Tyhrmisto, Pesmisto and Kitmisto. During the onset of a pandemic, the number of new cases of a disease in each of these neighbourhoods was recorded over a period of five days. On each day, the number of new cases recorded in any of the neighbourhoods was either 0, 1, 2 or 3.") +
 p("The following facts are also known:") +
 "<ol><li>There was at least one new case in every neighbourhood on Day 1.</li><li>On each of the five days, there were more new cases in Kitmisto than in Pesmisto.</li><li>The number of new cases in the city in a day kept increasing during the five-day period. The number of new cases on Day 3 was exactly one more than that on Day 2.</li><li>The maximum number of new cases in a day in Pesmisto was 2, and this happened only once during the five-day period.</li><li>Kitmisto is the only place to have 3 new cases on Day 2.</li><li>The total numbers of new cases in Levmisto, Tyhrmisto, Pesmisto and Kitmisto over the five-day period were 12,12, 5 and 14, respectively.</li></ol>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("The city’s daily totals", p("Over five days there were 12 + 12 + 5 + 14 = 43 cases. Day 1 has at least 1 + 1 + 1 + 2 = 5 (Kitmisto must beat Pesmisto). A day can have at most 3 + 3 + 3 + 2 = 11, and only one day can reach 11, since Pesmisto has 2 just once. With strictly rising totals, Day 5 ≤ 11, Day 4 ≤ 10.")),
       ("Pinning them down", p("Write the totals as d₁, d₂, d₂ + 1, d₄, d₅. Then d₁ + 2d₂ + 1 + d₄ + d₅ = 43 with d₄ + d₅ ≤ 21, so d₁ + 2d₂ ≥ 21. Since d₁ < d₂, d₂ = 7 fails (d₁ would need to be 7). So d₂ = 8, and then d₁ + d₄ + d₅ = 26 forces d₁ = 5, d₄ = 10, d₅ = 11.")),
       ("Filling in", p("Day 5 = 11 means everyone is at the maximum, with Pesmisto at 2. Day 1 = 5 means 1, 1, 1, 2. Day 4 = 10 means three 3s and Pesmisto 1. On Day 2, Kitmisto has 3, the others at most 2, and Pesmisto at most 1, so 8 means Levmisto 2, Tyhrmisto 2, Pesmisto 1. Pesmisto’s total of 5 then leaves 0 for Day 3, and Day 3 = 9 is three 3s.") +
       table(["", "Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Total"],
             [["Levmisto", "1", "2", "3", "3", "3", "12"], ["Tyhrmisto", "1", "2", "3", "3", "3", "12"], ["Pesmisto", "1", "1", "0", "1", "2", "5"],
              ["Kitmisto", "2", "3", "3", "3", "3", "14"], ["City", "5", "8", "9", "10", "11", "43"]]))) +
 final("The table is unique."),
 p("Start with the city’s daily totals rather than the neighbourhoods. The upper limit per day and the fixed sum of 43 leave only one sequence."),
 p("<b>Bounds before cases:</b> when totals must rise and the grand total is fixed, the largest and smallest possible values often squeeze the sequence into a single option."))
P.dq(6, "Which BEST can be concluded about the total number of new cases in the city on Day 2?",
 ["Exactly 8", "Either 7 or 8", "Exactly 7", "Either 6 or 7"], "MCQ", "1", "Hard",
 "Use the total of 43 and the most a day can have.",
 steps(("From the set solution", p("The daily totals must be 5, 8, 9, 10, 11."))) + final("Exactly 8, option 1"),
 [("2", "7 doesn’t work: Day 1 would then have to be 7 as well."), ("3", "As above."), ("4", "Too low to reach a total of 43.")])
P.dq(7, "What BEST can be concluded about the number of new cases in Levmisto on Day 3?",
 ["Either 0 or 1", "Either 2 or 3", "Exactly 2", "Exactly 3"], "MCQ", "4", "Hard",
 "Day 3 has 9 cases and Pesmisto has none that day.",
 steps(("Day 3", p("Pesmisto has 0, so Levmisto, Tyhrmisto and Kitmisto share 9 cases with at most 3 each. All three have 3."))) + final("Exactly 3, option 4"),
 [("1", "Too low."), ("2", "It can only be 3."), ("3", "It can only be 3.")])
P.dq(8, "On which day(s) did Pesmisto not have any new case?",
 ["Both Day 2 and Day 3", "Only Day 3", "Only Day 2", "Both Day 2 and Day 4"], "MCQ", "2", "Hard",
 "Pesmisto’s row is 1, 1, 0, 1, 2.",
 steps(("From the table", p("Pesmisto has no cases only on Day 3."))) + final("Only Day 3, option 2"),
 [("1", "Pesmisto has 1 on Day 2."), ("3", "Pesmisto has 1 on Day 2."), ("4", "Pesmisto has 1 on both these days.")])
P.dq(9, "Which of the two statements given below is/are necessarily false?<br>Statement A: There were 2 new cases in Tyhrmisto on Day 3.<br>Statement B: There were no new cases in Pesmisto on Day 2.",
 ["Both Statement A and Statement B", "Statement B only", "Neither Statement A nor Statement B", "Statement A only"], "MCQ", "1", "Hard",
 "Check both against the unique table.",
 steps(("Checking", p("Tyhrmisto had 3 on Day 3, and Pesmisto had 1 on Day 2. Both statements are false."))) + final("Both, option 1"),
 [("2", "Statement A is false too."), ("3", "Both are false."), ("4", "Statement B is false too.")])
P.dq(10, "On how many days did Levmisto and Tyhrmisto have the same number of new cases?",
 ["4", "5", "3", "2"], "MCQ", "2", "Hard",
 "Compare their two rows.",
 steps(("From the table", p("Both rows are 1, 2, 3, 3, 3, so they match on all five days."))) + final("5, option 2"),
 [("1", "They match on Day 1 as well."), ("3", "They match on Days 1 and 2 as well."), ("4", "They match on every day.")])

# ---------------- Set 3: AI and ML grades ----------------
P.dilr_set(3, "Set 3 — Grades in AI and ML", "Read the following passage carefully and answer the questions that follow.",
 p("All the first-year students in the computer science (CS) department in a university take both the courses: (i) AI and (ii) ML. Students from other departments (non-CS students) can also take one of these two courses, but not both. Students who fail in a course get an F grade; others pass and are awarded A or B or C grades depending on their performance. The following are some additional facts about the number of students who took these two courses this year and the grades they obtained.") +
 "<ol><li>The numbers of non-CS students who took AI and ML were in the ratio 2 : 5.</li><li>The number of non-CS students who took either AI or ML was equal to the number of CS students.</li><li>The numbers of non-CS students who failed in the two courses were the same and their total is equal to the number of CS students who got a C grade in ML.</li><li>In both the courses, 50% of the students who passed got a B grade. But, while the numbers of students who got A and C grades were the same for AI, they were in the ratio 3 : 2 for ML.</li><li>No CS student failed in AI, while no non-CS student got an A grade in AI.</li><li>The numbers of CS students who got A, B and C grades, respectively in AI were in the ratio 3 : 5 : 2, while in ML, the ratio was 4 : 5 : 2.</li><li>The ratio of the total number of non-CS students failing in one of the two courses to the number of CS students failing in one of the two courses was 3:1.</li><li>30 students failed in ML.</li></ol>",
 "DILR::DI::Caselets",
 steps(("Failures first", p(r"Let \(f\) non-CS students fail in each course. No CS student fails AI, so every CS failure is in ML. Fact 7 says \(2f\) is three times the CS failures, so CS failures are \(\tfrac{2f}{3}\). Fact 8: \(f + \tfrac{2f}{3} = 30\), so \(f = 18\) and 12 CS students fail ML.")),
       ("CS students", p("By fact 3, 36 CS students got C in ML. The ML ratio 4 : 5 : 2 then gives 72 A, 90 B, 36 C. Adding the 12 failures, there are 210 CS students. In AI none failed, so 3 : 5 : 2 of 210 gives 63 A, 105 B, 42 C.")),
       ("Non-CS students", p("There are 210 of them too (fact 2), split 2 : 5: 60 took AI and 150 took ML. In each course 18 failed.")),
       ("AI grades", p("Across AI, A and C are equal and B is half of all passes. A total is 63 (no non-CS A grades), so C total is 63 too: non-CS C = 21, and the remaining 21 non-CS passes are B. Check: B = 126, which is half of 252 passes.")),
       ("ML grades", p("ML passes: 198 CS + 132 non-CS = 330. Half are B (165), so non-CS B = 75. A and C share the other 165 as 3 : 2: 99 and 66, so non-CS A = 27 and non-CS C = 30.") +
       table(["", "A", "B", "C", "F", "Total"],
             [["AI, CS", "63", "105", "42", "0", "210"], ["AI, non-CS", "0", "21", "21", "18", "60"],
              ["ML, CS", "72", "90", "36", "12", "210"], ["ML, non-CS", "27", "75", "30", "18", "150"]]))) +
 final("All numbers are fixed."),
 p("Start with failures: facts 7 and 8 give them straight away, and everything else follows from there."),
 p("<b>Find the anchor:</b> in a caselet full of ratios, look for the one fact with an actual number (here, 30 failures) and work outward from it."))
P.dq(11, "How many students took AI?", ["90", "60", "270", "210"], "MCQ", "3", "Medium",
 "All CS students take AI, plus the non-CS students who chose it.",
 steps(("Adding", p("210 CS + 60 non-CS = 270."))) + final("270, option 3"),
 [("1", "Not a total that appears anywhere."), ("2", "Non-CS students only."), ("4", "CS students only.")])
P.dq(12, "How many CS students failed in ML?", [], "TITA", "12", "Medium",
 "Facts 7 and 8 together.",
 steps(("From the set solution", p(r"\(f + \tfrac{2f}{3} = 30\) gives \(f = 18\); CS failures are \(\tfrac{2}{3} \times 18 = 12\)."))) + final(r"\(12\)"))
P.dq(13, "How many non-CS students got an A grade in ML?", [], "TITA", "27", "Medium",
 "Work out A and C for the whole of ML, then subtract the CS students.",
 steps(("From the set solution", p("ML has 330 passes; 165 are A or C, split 3 : 2 as 99 and 66. CS students have 72 A grades, so non-CS have 27."))) + final(r"\(27\)"))
P.dq(14, "How many students got an A grade in AI?", ["63", "42", "84", "99"], "MCQ", "1", "Medium",
 "Non-CS students got no A grades in AI.",
 steps(("From the set solution", p("All the A grades in AI went to CS students: 3/10 of 210 = 63."))) + final("63, option 1"),
 [("2", "That is the CS count of C grades in AI."), ("3", "Not a count that appears."), ("4", "That is the number of A grades in ML.")])
P.dq(15, "How many non-CS students got a B grade in ML?", ["75", "25", "90", "165"], "MCQ", "1", "Medium",
 "Half of all ML passes got B.",
 steps(("From the set solution", p("165 B grades in ML, of which 90 went to CS students: 75 are non-CS."))) + final("75, option 1"),
 [("2", "Too few."), ("3", "That is the CS count."), ("4", "That is the total for both groups.")])

# ---------------- Set 4: Betting tournament ----------------
P.dilr_set(4, "Set 4 — Four players over eight rounds", "Read the following passage carefully and answer the questions that follow.",
 p("Pulak, Qasim, Ritesh, and Suresh participated in a tournament comprising eight rounds. In each round, they formed two pairs, with each of them being in exactly one pair. The only restriction in the pairing was that the pairs would change in successive rounds. For example, if Pulak formed a pair with Qasim in the first round, then he would have to form a pair with Ritesh or Suresh in the second round. He would be free to pair with Qasim again in the third round. In each round, each pair decided whether to play the game in that round or not. If they decided not to play, then no money was exchanged between them. If they decided to play, they had to bet either ₹1 or ₹2 in that round. For example, if they chose to bet ₹2, then the player winning the game got ₹2 from the one losing the game.") +
 p("At the beginning of the tournament, the players had ₹10 each. The following table shows partial information about the amount that the players had at the end of each of the eight rounds. It shows every time a player had ₹10 at the end of a round, as well as every time, at the end of a round, a player had either the minimum or the maximum amount that he would have had across the eight rounds. For example, Suresh had ₹10 at the end of Rounds 1, 3, and 8 and not after any of the other rounds. The maximum amount that he had at the end of any round was ₹13 (at the end of Round 5), and the minimum amount he had at the end of any round was ₹8 (at the end of Round 2). At the end of all other rounds, he must have had either ₹9, ₹11, or ₹12.") +
 table(["", "Pulak", "Qasim", "Ritesh", "Suresh"],
       [["Round 1", "", "₹8", "₹10", "₹10"], ["Round 2", "₹13", "₹10", "", "₹8"], ["Round 3", "", "", "", "₹10"], ["Round 4", "", "", "", ""],
        ["Round 5", "₹10", "₹10", "", "₹13"], ["Round 6", "", "", "", ""], ["Round 7", "", "₹12", "₹4", ""], ["Round 8", "₹13", "", "", "₹10"]]) +
 p("It was also known that Pulak and Qasim had the same amount of money with them at the end of Round 4."),
 "DILR::LR::Puzzles",
 steps(("What the blanks can be", p("Pulak is 11 or 12 in his blank rounds (never 10, and 13 only in Rounds 2 and 8). Qasim is 9 or 11. Ritesh is between 5 and 9. Suresh is 9, 11 or 12. The four amounts always add up to 40.")),
       ("Rounds 1 and 2", p("Qasim lost ₹2 in Round 1 while Ritesh and Suresh stayed at 10, so Qasim played Pulak, who went to 12, and Ritesh–Suresh didn’t exchange money. In Round 2 the pairs must change. Qasim gained 2 and Suresh lost 2, which only works if they played each other; so Pulak played Ritesh, and Pulak’s +1 puts Ritesh at 9.")),
       ("Rounds 4 and 5", p("At the end of Round 4, Pulak and Qasim are equal; the only common value is 11. In Round 5 both drop to 10, so they weren’t paired together. Ritesh is 7 in Round 5 (the total is 40), and Suresh reaches 13. Either way, Ritesh was 6 and Suresh 12 at the end of Round 4.")),
       ("Back to Round 3", p("If Round 3 were Pulak–Qasim and Ritesh–Suresh, Round 4 would need pairs that can turn (12, 11, 7, 10) into (11, 11, 6, 12), and neither of the allowed pairings balances. So Round 3 is Pulak–Suresh (Pulak 11, Suresh 10) and Qasim–Ritesh (Qasim 11, Ritesh 8), and Round 4 is Pulak–Qasim (no money) and Ritesh–Suresh (₹2 to Suresh).")),
       ("Rounds 6 to 8", p("Qasim has to reach 12 in Round 7, so he is 11 after Round 6. Trying the two possible Round 5 pairings, only Pulak–Suresh with Qasim–Ritesh in Round 5 leads to an allowed path; the other forces Pulak to 13 or Suresh to 10 in Round 7, and the table shows neither. That gives the table below.") +
       table(["", "Pulak", "Qasim", "Ritesh", "Suresh", "Pairs"],
             [["Round 1", "12", "8", "10", "10", "PQ, RS"], ["Round 2", "13", "10", "9", "8", "PR, QS"], ["Round 3", "11", "11", "8", "10", "PS, QR"],
              ["Round 4", "11", "11", "6", "12", "PQ, RS"], ["Round 5", "10", "10", "7", "13", "PS, QR"], ["Round 6", "12", "11", "5", "12", "PR, QS"],
              ["Round 7", "12", "12", "4", "12", "PS, QR"], ["Round 8", "13", "11", "6", "10", "PQ, RS"]]))) +
 final("The table is unique. Games with a ₹2 bet: Rounds 1, 2, 3, 4, 6 and 8, one each."),
 p("Fill the forced rounds first (1, 2, 4 and 5), then test the few pairings that remain. The ‘every max and min is shown’ rule rules out most branches quickly."),
 p("<b>Partial tables:</b> when a table promises to show every extreme value, the blanks are restricted too. Write down what each blank can be before you start."))
P.dq(16, "What BEST can be said about the amount of money that Ritesh had with him at the end of Round 8?",
 ["Exactly ₹6", "Exactly ₹5", "₹5 or ₹6", "₹4 or ₹5"], "MCQ", "1", "Hard",
 "Round 8 is Pulak–Qasim and Ritesh–Suresh. Suresh drops from 12 to 10.",
 steps(("From the set solution", p("Suresh loses ₹2 to Ritesh, who goes from 4 to 6."))) + final("Exactly ₹6, option 1"),
 [("2", "Ritesh gains 2, not 1."), ("3", "Only 6 is possible."), ("4", "4 is his minimum, reached only in Round 7.")])
P.dq(17, "What BEST can be said about the amount of money that Pulak had with him at the end of Round 6?",
 ["₹12 or ₹13", "₹11 or ₹12", "Exactly ₹12", "Exactly ₹11"], "MCQ", "3", "Hard",
 "Pulak can’t have 13 in Round 6, since the table shows every time he reached his maximum.",
 steps(("From the set solution", p("Pulak wins ₹2 from Ritesh in Round 6 and has ₹12."))) + final("Exactly ₹12, option 3"),
 [("1", "13 would have appeared in the table."), ("2", "Only 12 is possible."), ("4", "Only 12 is possible.")])
P.dq(18, "How much money (in ₹) did Ritesh have at the end of Round 4?", [], "TITA", "6", "Hard",
 "The total is always 40. In Round 5 Ritesh has 40 − 10 − 10 − 13.",
 steps(("From the set solution", p("Ritesh has 7 after Round 5 and gained ₹1 in it, so he had ₹6 after Round 4."))) + final(r"\(6\)"))
P.dq(19, "How many games were played with a bet of ₹2?", [], "TITA", "6", "Hard",
 "Count the pairs whose amounts changed by 2 in a round.",
 steps(("Counting", p("Round 1 (Pulak–Qasim), Round 2 (Qasim–Suresh), Round 3 (Pulak–Suresh), Round 4 (Ritesh–Suresh), Round 6 (Pulak–Ritesh) and Round 8 (Ritesh–Suresh): six games."))) + final(r"\(6\)"))
P.dq(20, "Which of the following pairings was made in Round 5?",
 ["Pulak and Qasim", "Pulak and Suresh", "Pulak and Ritesh", "Qasim and Suresh"], "MCQ", "2", "Hard",
 "Pulak and Qasim both lose ₹1 in Round 5, so they weren’t paired together.",
 steps(("From the set solution", p("Round 5 is Pulak–Suresh and Qasim–Ritesh. The other choice, Pulak–Ritesh with Qasim–Suresh, leads to Pulak having 13 or Suresh having 10 in Round 7, and the table shows neither."))) +
 final("Pulak and Suresh, option 2"),
 [("1", "Both lost ₹1, so they can’t have played each other."), ("3", "This branch leads to a contradiction in Round 7."), ("4", "Belongs to the same failed branch as option 3.")])
