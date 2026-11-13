# -*- coding: utf-8 -*-
# Batch 17 — CAT 2024 Slot 1: DILR sets 1–5 (Q1–22, in exam order).
from fmt import steps, final, trap, why, table, p
from b17_24s1 import P
import b17_24s1_figs as F

DIR = "Read the information given below and answer the questions that follow."

# ---------------- Set 1: QUIET tournament ----------------
P.dilr_set(1, "Set 1 — A six-team tournament in rounds", DIR,
 p("The game of QUIET is played between two teams. Six teams, numbered 1, 2, 3, 4, 5, and 6, play in a QUIET tournament. These teams are divided equally into two groups. In the tournament, each team plays every other team in the same group only once, and each team in the other group exactly twice. The tournament has several rounds, each of which consists of a few games. Every team plays exactly one game in each round. The following additional facts are known about the schedule of games in the tournament.") +
 "<ol><li>Each team played against a team from the other group in Round 8.</li><li>In Round 4 and Round 7, the match-ups, that is the pair of teams playing against each other, were identical. In Round 5 and Round 8, the match-ups were identical.</li><li>Team 4 played Team 6 in both Round 1 and Round 2.</li><li>Team 1 played Team 5 ONLY once and that was in Round 2.</li><li>Team 3 played Team 4 in Round 3. Team 1 played Team 6 in Round 6.</li><li>In Round 8, Team 3 played Team 6, while Team 2 played Team 5.</li></ol>",
 "DILR::LR::Games_and_Tournaments",
 steps(("Number of rounds", p("Each team plays the 2 others in its group once and the 3 teams in the other group twice: 2 + 6 = 8 games. One game per round means 8 rounds.")),
       ("The groups", p("Teams that meet twice are in different groups; teams that meet only once are in the same group. So 1 and 5 share a group, while 4 and 6, 3 and 6, and 2 and 5 are in different groups. 2 is opposite 5, so 2 is opposite 1 as well. If 3 or 4 joined 1 and 5, then 6 would sit with 2 and the other of 3, 4, but 6 must be apart from both 3 and 4. So the third member is 6: the groups are {1, 5, 6} and {2, 3, 4}.")),
       ("Rounds 5 and 8", p("Round 8 has 3–6 and 2–5, so the third game is 1–4. Round 5 is the same.")),
       ("Rounds 1 to 3", p("Round 2 has 4–6 and 1–5, leaving 2–3. Round 3 has 3–4; team 1 can’t meet 5 again or 6 (that game is in Round 6), so 1–2 and then 5–6. In Round 1, 4–6 is fixed, and team 1 plays 2 or 3.")),
       ("Rounds 4 and 7", p("Whatever team 1 plays in Round 4, it plays again in Round 7. That must be an opponent from the other group, and 4 is used up (Rounds 5 and 8). If it were 2, team 1 would meet 2 in Rounds 3, 4 and 7: three times. So it is 3. Then team 1 plays 2 in Round 1, and 3–5 completes that round. The rest of Rounds 4 and 7 is 2–6 and 4–5, because 4–6 has already been played twice.")),
       ("Round 6", p("1–6 is given. Of 2, 3, 4, 5, the pairs 2–3 and 3–4 are used up, so it is 2–4 and 3–5.") +
          table(["Round", "Games"], [["1", "1–2, 3–5, 4–6"], ["2", "1–5, 2–3, 4–6"], ["3", "1–2, 3–4, 5–6"], ["4", "1–3, 2–6, 4–5"], ["5", "1–4, 2–5, 3–6"], ["6", "1–6, 2–4, 3–5"], ["7", "1–3, 2–6, 4–5"], ["8", "1–4, 2–5, 3–6"]]))) +
 final("Groups {1, 5, 6} and {2, 3, 4}; the full schedule is in the table."),
 p("Count the meetings between each pair of teams: twice means different groups, once means the same group. That fixes the groups at once, and the repeated rounds do the rest."),
 p("<b>Round-robin schedules:</b> the number of rounds equals the number of games each team plays. Use “played twice” versus “played once” to sort teams into groups."))
P.dq(1, "How many rounds were there in the tournament?", [], "TITA", "8", "Easy",
 "How many games does each team play in total?",
 steps(p("Each team plays 2 games inside its group and 2 × 3 = 6 against the other group: 8 games, one per round.")) + final(r"\(8\)"))
P.dq(2, "What is the number of the team that played Team 1 in Round 5?", [], "TITA", "4", "Easy",
 "Round 5 is a copy of Round 8. Two of Round 8’s games are given.",
 steps(p("Round 8 has 3–6 and 2–5, so the remaining teams 1 and 4 play each other. Round 5 is identical.")) + final(r"\(4\)"))
P.dq(3, "Which team among the teams numbered 2, 3, 4, and 5 was not part of the same group?", ["4", "5", "3", "2"], "MCQ", "2", "Medium",
 "Team 1 met Team 5 only once. What does that say about their groups?",
 steps(p("Meeting only once means 1 and 5 are in the same group, and the set solution shows the groups are {1, 5, 6} and {2, 3, 4}. So 5 is the odd one out among 2, 3, 4 and 5.")) + final("Team 5, option 2"),
 [("1", "4 is grouped with 2 and 3."), ("3", "3 is grouped with 2 and 4."), ("4", "2 is grouped with 3 and 4.")])
P.dq(4, "What is the number of the team that played Team 1 in Round 7?", [], "TITA", "3", "Hard",
 "Team 1 plays the same opponent in Rounds 4 and 7. Which opponent can it still meet twice?",
 steps(p("Team 1 already meets 4 in Rounds 5 and 8, and 2 in Round 3. A team from the other group that appears in both Rounds 4 and 7 can only be 3; taking 2 would make three games against 2.")) + final(r"\(3\)"))
P.dq(5, "What is the number of the team that played Team 6 in Round 3?", [], "TITA", "5", "Medium",
 "Round 3 has 3–4. Who can team 1 play in that round?",
 steps(p("With 3–4 fixed, teams 1, 2, 5 and 6 remain. Team 1 has already met 5 (its only game against 5), and its game against 6 is in Round 6, so team 1 plays 2. That leaves 5–6.")) + final(r"\(5\)"))

# ---------------- Set 2: Countries visited ----------------
P.dilr_set(2, "Set 2 — Countries visited by three travellers", DIR,
 p("The chart below provides complete information about the number of countries visited by Dheeraj, Samantha and Nitesh, in Asia, Europe and the rest of the world (ROW).") + F.COUNTRIES +
 p("The following additional facts are known about the countries visited by them.") +
 "<ol><li>32 countries were visited by at least one of them.</li><li>USA (in ROW) is the only country that was visited by all three of them.</li><li>China (in Asia) is the only country that was visited by both Dheeraj and Nitesh, but not by Samantha.</li><li>France (in Europe) is the only country outside Asia, which was visited by both Dheeraj and Samantha, but not by Nitesh.</li><li>Half of the countries visited by both Samantha and Nitesh are in Europe.</li></ol>",
 "DILR::LR::Venn_Diagrams",
 steps(("Totals", p("Dheeraj visited 3 + 7 + 1 = 11 countries, Samantha 0 + 9 + 4 = 13 and Nitesh 1 + 6 + 12 = 19: 43 visits in all. 32 different countries were visited, so the 11 extra visits come from overlaps. USA counts 2 extra, so the countries visited by exactly two people number 11 − 2 = 9.")),
       ("Dheeraj and Samantha together", p("Samantha visited no Asian country, so Dheeraj and Samantha share nothing in Asia; outside Asia they share only France. So exactly D and S: 1 (France).")),
       ("Who else overlaps", p("Exactly D and N: 1 (China). So exactly S and N: 9 − 1 − 1 = 7. Add USA and Samantha and Nitesh share 8 countries, half of them, 4, in Europe. Samantha has no Asian countries, so the other 4 are in ROW: USA plus 3 more.")),
       ("Filling each continent", p("Asia: D has 3 including China, so 2 only-D; N’s 1 is China; total 3. Europe: S has 9 = France + 4 shared with N + 4 only-S. N has 6 = 4 shared with S + 2 only-N. D has 7 = France + 6 only-D. ROW: D’s 1 is USA. S has 4 = USA + 3 shared with N, so 0 only-S. N has 12 = USA + 3 + 8 only-N.") +
          table(["", "Asia", "Europe", "ROW"],
                [["D only", "2", "6", "0"], ["S only", "0", "4", "0"], ["N only", "0", "2", "8"], ["Shared", "1", "5", "4"], ["Total", "3", "17", "12"]]) +
          p("“Shared” means visited by two or three of them. Asia: China (D and N). Europe: France (D and S) and 4 shared by S and N. ROW: USA (all three) and 3 shared by S and N. The totals add to 32, as required."))) +
 final("Asia 3 countries, Europe 17, ROW 12."),
 p("Use the overlap count: total visits minus distinct countries gives the extra visits, which pins down how many countries were seen by exactly two people."),
 p("<b>Three-set counting:</b> total visits = (exactly one) + 2 × (exactly two) + 3 × (all three), while the number of distinct countries is the sum of the three “exactly” counts."))
P.dq(6, "How many countries in Asia were visited by at least one of Dheeraj, Samantha and Nitesh?", [], "TITA", "3", "Easy",
 "Samantha visited no Asian country. Who shares China?",
 steps(p("Dheeraj’s 3 Asian countries include China, and Nitesh’s only Asian country is China. So the countries are China plus Dheeraj’s other two.")) + final(r"\(3\)"))
P.dq(7, "How many countries in Europe were visited only by Nitesh?", [], "TITA", "2", "Medium",
 "Nitesh shares 4 European countries with Samantha. Does he share any with Dheeraj?",
 steps(p("Nitesh’s 6 European countries: none with Dheeraj (their only shared country is China), and 4 with Samantha. That leaves 2 that only he visited.")) + final(r"\(2\)"))
P.dq(8, "How many countries in the ROW were visited by both Nitesh and Samantha?", [], "TITA", "4", "Medium",
 "Samantha and Nitesh share 8 countries in all, half in Europe. Include USA.",
 steps(p("They share 8 countries, 4 in Europe. Samantha has nothing in Asia, so the other 4 are in ROW, including USA.")) + final(r"\(4\)"))
P.dq(9, "How many countries in Europe were visited by exactly one of Dheeraj, Samantha and Nitesh?", ["5", "10", "12", "14"], "MCQ", "3", "Medium",
 "Add up the three “only” counts in Europe.",
 steps(p("Only Dheeraj 6, only Samantha 4, only Nitesh 2: 12.")) + final("12, option 3"),
 [("1", "This is the number of European countries visited by two people (France plus 4)."), ("2", "This leaves out Nitesh’s 2."), ("4", "This counts France twice.")])

# ---------------- Set 3: Candlesticks ----------------
P.dilr_set(3, "Set 3 — Share prices on a candlestick chart", DIR,
 p("The chart below shows the price data for seven shares– A, B, C, D, E, F, and G as a candlestick plot for a particular day. The vertical axis shows the price of the share in rupees. A share whose closing price (price at the end of the day) is more than its opening price (price at the start of the day) is called a bullish share; otherwise, it is called a bearish share. All bullish and bearish shares are shown in green and red colour respectively.") + F.CANDLES,
 "DILR::DI::Graphs_and_Charts",
 steps(("Reading the chart", p("For a red (bearish) candle, the top of the box is the opening price and the bottom is the closing price; for a green (bullish) one it is the other way round. The thin line runs from the day’s low to the day’s high.") +
          table(["Share", "Open → Close", "Low – High"],
                [["A", "2200 → 1800", "1200 – 2400"], ["B", "2000 → 1700", "1400 – 2000"], ["C", "800 → 1200", "800 – 1400"], ["D", "500 → 1000", "300 – 1200"],
                 ["E", "1300 → 1100", "1100 – 1400"], ["F", "1800 → 1600", "1200 – 2000"], ["G", "1200 → 1700", "1000 – 1900"]])),
       ("Bullish and bearish", p("C, D and G are bullish (green). A, B, E and F are bearish (red)."))) +
 final("All seven shares’ prices are in the table."),
 p("Write the four prices of every share in a table first. Every question is then a one-line calculation."),
 p("<b>Candlesticks:</b> the box spans the open and close; the wick spans the day’s low to high. Green means the close was above the open."))
SPV = table(["Share", "Range", "Average", "SPV"],
            [["A", "1200", "2000", "0.60"], ["B", "600", "1850", "0.32"], ["C", "600", "1000", "0.60"], ["D", "900", "750", "1.20"],
             ["E", "300", "1200", "0.25"], ["F", "800", "1700", "0.47"], ["G", "900", "1450", "0.62"]])
P.dq(10, "Daily Share Price Variability (SPV) is defined as (Day’s high price - Day’s low price) /(Average of the opening and closing prices during the day). Which among the shares A, C, D and F had the highest SPV on that day?", ["A", "C", "F", "D"], "MCQ", "4", "Easy",
 "D’s range is large but its prices are low. That makes its ratio big.",
 steps(p(r"A: \(1200 \div 2000 = 0.6\). C: \(600 \div 1000 = 0.6\). F: \(800 \div 1700 \approx 0.47\). D: \(900 \div 750 = 1.2\).")) + final("D, option 4"),
 [("1", "A’s SPV is 0.6."), ("2", "C’s SPV is 0.6."), ("3", "F’s SPV is about 0.47.")])
P.dq(11, "Daily Share Price Variability (SPV) is defined as (Day’s high price - Day’s low price) / (Average of the opening and closing prices during the day). How many shares had an SPV greater than 0.5 on that day?", [], "TITA", "4", "Medium",
 "Work out SPV for all seven shares. A and C are exactly at 0.6, comfortably above 0.5.",
 steps(p("Range is high minus low; average is the mean of the opening and closing prices.") + SPV, p("A, C, D and G are above 0.5.")) + final(r"\(4\)"))
P.dq(12, "Daily loss for a share is defined as (Opening price — Closing price) / (Opening price). Which among the shares A, B, F and G had the highest daily loss on that day?", ["G", "F", "A", "B"], "MCQ", "3", "Easy",
 "G is green, so it gained rather than lost. Compare the other three.",
 steps(p(r"A: \(400 \div 2200 \approx 0.18\). B: \(300 \div 2000 = 0.15\). F: \(200 \div 1800 \approx 0.11\). G closed higher than it opened, so its “loss” is negative.")) + final("A, option 3"),
 [("1", "G is bullish; it made a gain."), ("2", "F lost about 11%."), ("4", "B lost 15%, less than A’s 18%.")])
P.dq(13, "What would have been the percentage wealth gain for a trader, who bought equal numbers of all bullish shares at opening price and sold them at their day’s high?", ["50%", "100%", "72%", "80%"], "MCQ", "4", "Medium",
 "With equal numbers of shares, compare total cost with total proceeds per set of one share each.",
 steps(("Bullish shares", p("C, D and G.")),
       ("One of each", p(r"Cost at opening: \(800 + 500 + 1200 = 2500\). Sold at the highs: \(1400 + 1200 + 1900 = 4500\). Gain: \(2000 \div 2500 = 80\%\)."))) + final("80%, option 4"),
 [("1", "This would need proceeds of 3750."), ("2", "This would need the money to double."), ("3", "The totals give 4500 against 2500, which is an 80% gain.")])

# ---------------- Set 4: Stars to bloggers ----------------
P.dilr_set(4, "Set 4 — Stars given to four bloggers", DIR,
 p("Six web surfers M, N, O, P, X, and Y each had 30 stars which they distributed among four bloggers A, B, C, and D. The number of stars received by A and B from the six web surfers is shown in the figure below.") + F.STARS +
 p("The following additional facts are known regarding the number of stars received by the bloggers from the surfers.") +
 "<ol><li>The numbers of stars received by the bloggers from the surfers were all multiples of 5 (including 0).</li><li>The total numbers of stars received by the bloggers were the same.</li><li>Each blogger received a different number of stars from M.</li><li>Two surfers gave all their stars to a single blogger.</li><li>D received more stars than C from Y.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("Each blogger’s total", p(r"There are \(6 \times 30 = 180\) stars, so each blogger gets 45. A gets 10 + 25 + 5 + 5 = 45 and B gets 25 + 20 = 45, as expected.")),
       ("What C and D get from each surfer", p("M: 20 between them. N: 5. O: 30. P: 0. X: 30. Y: 5, and since D gets more than C, D gets 5 and C gets 0.")),
       ("The two surfers", p("O and X gave A and B nothing, and P split its stars between A and B. Of the others, M gives to at least three bloggers, and N and Y can’t give everything to one person. So the two surfers are O and X, each giving 30 stars to C or to D. Both to C would give C 60, over 45; both to D would give D 65. So one goes to C and one to D.")),
       ("M and N", p("M’s 20 must be split so that every blogger gets a different amount from M. A has 10 and B has 0, so C and D get 5 and 15 in some order. C: 30 + (M) + (N) = 45 needs 15 from M and N together. D: 30 + (M) + (N) + 5 = 45 needs 10. C taking 15 from M leaves 0 from N; D then takes 5 from M and 5 from N. The other split (C 5 from M) would need 10 from N, which is impossible.") +
          table(["Surfer", "A", "B", "C", "D"],
                [["M", "10", "0", "15", "5"], ["N", "25", "0", "0", "5"], ["O, X", "0", "0", "30*", "30*"], ["P", "5", "25", "0", "0"], ["Y", "5", "20", "0", "5"]]) +
          p("* One of O and X gives all 30 to C and the other gives all 30 to D; which is which is not fixed."))) +
 final("Each blogger gets 45 stars; only the O and X split between C and D is open."),
 p("Begin with the equal totals: 45 each. The two “all to one” surfers must be the two that A and B didn’t touch."),
 p("<b>Distribution tables:</b> fix row totals (30 per surfer) and column totals (45 per blogger), then use the special conditions to place the remaining blocks."))
P.dq(14, "What was the total number of stars received by D?", [], "TITA", "45", "Easy",
 "All four bloggers received the same total.",
 steps(p(r"\(180 \div 4 = 45\).")) + final(r"\(45\)"))
P.dq(15, "What was the number of stars received by D from Y?", ["10", "0", "5", "cannot be determined"], "MCQ", "3", "Easy",
 "Y gave 25 to A and B. How can the other 5 be split if D gets more than C?",
 steps(p("C and D share 5 stars from Y in multiples of 5, and D gets more, so D gets 5.")) + final("5, option 3"),
 [("1", "Only 5 stars are left for C and D."), ("2", "That would give C more than D."), ("4", "The rule about D and C settles it.")])
P.dq(16, "How many surfers distributed their stars among exactly 2 bloggers?", [], "TITA", "2", "Medium",
 "Use the finished table and count the non-zero entries in each surfer’s row.",
 steps(p("M gives to three bloggers, N to two (A and D), O and X to one each, P to two (A and B), and Y to three. So N and P.")) + final(r"\(2\)"))
P.dq(17, "Which of the following can be determined with certainty?<br>I. The number of stars received by C from M<br>II. The number of stars received by D from O", ["Neither I nor II", "Both I and II", "Only I", "Only II"], "MCQ", "3", "Medium",
 "O and X each give all their stars to C or D, but which goes where?",
 steps(p("C gets 15 from M in every valid arrangement, so I is fixed. O could give its 30 to C or to D, with X taking the other, so D’s stars from O are 0 or 30: II is not fixed.")) + final("Only I, option 3"),
 [("1", "I is fixed at 15."), ("2", "D’s stars from O could be 0 or 30."), ("4", "This is the wrong way round.")])

# ---------------- Set 5: Election campaigns ----------------
P.dilr_set(5, "Set 5 — Two candidates and their campaigns", DIR,
 p("Two students, Amiya and Ramya are the only candidates in an election for the position of class representative. Students will vote based on the intensity level of Amiya’s and Ramya’s campaigns and the type of campaigns they run. Each campaign is said to have a level of 1 if it is a staid campaign and a level of 2 if it is a vigorous campaign. Campaigns can be of two types, they can either focus on issues, or on attacking the other candidate.") +
 p("If Amiya and Ramya both run campaigns focusing on issues, then") +
 "<ul><li>The percentage of students voting in the election will be 20 times the sum of the levels of campaigning of the two students. For example, if Amiya and Ramya both run vigorous campaigns, then 20 × (2 + 2)%, that is, 80% of the students will vote in the election.</li><li>Among voting students, the percentage of votes for each candidate will be proportional to the levels of their campaigns. For example, if Amiya runs a staid (i.e., level 1) campaign while Ramya runs a vigorous (i.e., level 2) campaign, then Amiya will receive 1/3 of the votes cast, and Ramya will receive the other 2/3.</li></ul>" +
 p("The above-mentioned percentages change as follows if at least one of them runs a campaign attacking their opponent.") +
 "<ul><li>If Amiya runs a campaign attacking Ramya and Ramya runs a campaign focusing on issues, then 10% of the students who would have otherwise voted for Amiya will vote for Ramya, and another 10% who would have otherwise voted for Amiya, will not vote at all.</li><li>If Ramya runs a campaign attacking Amiya and Amiya runs a campaign focusing on issues, then 20% of the students who would have otherwise voted for Ramya will vote for Amiya, and another 5% who would have otherwise voted for Ramya, will not vote at all.</li><li>If both run campaigns attacking each other, then 10% of the students who would have otherwise voted for them had they run campaigns focusing on issues, will not vote at all.</li></ul>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("The neat simplification", p(r"With both on issues, the turnout is \(20(a + r)\%\) and Amiya takes \(\frac{a}{a + r}\) of it, where \(a\) and \(r\) are the levels. So Amiya gets \(20a\%\) of all students and Ramya \(20r\%\).")),
       ("The four cases", table(["Campaigns", "Amiya", "Ramya"],
          [["Issues", "20a", "20r"], ["A attacks", "16a", "20r + 2a"], ["R attacks", "20a + 4r", "15r"], ["Both attack", "18a", "18r"]]) +
          p("All figures are percentages of all students. When Amiya attacks, she loses 20% of her 20a: half to Ramya, half to nobody. When Ramya attacks, she loses 25% of her 20r: 4r to Amiya and r to nobody.")),
       ("Every outcome", p("With both on issues the shares are simply 20a and 20r: 20–20, 20–40, 40–20 or 40–40.") +
          table(["a, r", "A attacks", "R attacks", "Both"],
          [["1, 1", "16–22", "24–15", "18–18"], ["1, 2", "16–42", "28–30", "18–36"], ["2, 1", "32–24", "44–15", "36–18"], ["2, 2", "32–44", "48–30", "36–36"]]) +
          p("Rows are the levels (a, r). Each entry is Amiya’s share – Ramya’s share, as percentages of all students."))) +
 final("All sixteen outcomes are in the table."),
 p("Notice that each candidate’s share of all students is simply 20 times her level when both focus on issues. That turns every case into simple arithmetic."),
 p("<b>Rule-based cases:</b> convert every rule into a formula in the same unit (here, percent of all students) and tabulate all combinations."))
P.dq(18, "If both of them run staid campaigns attacking the other, then what percentage of students will vote in the election?", ["60%", "64%", "40%", "36%"], "MCQ", "4", "Easy",
 "Start from the turnout with issue campaigns at level 1 each, then remove 10%.",
 steps(p(r"Issue campaigns at levels 1 and 1 would bring out 40%. Attacking each other loses 10% of those: \(0.9 \times 40 = 36\%\).")) + final("36%, option 4"),
 [("1", "60% is the turnout for levels that add to 3."), ("2", "64% would need vigorous campaigns, not staid ones."), ("3", "This forgets that 10% stay home.")])
P.dq(19, "What is the minimum percentage of students who will vote in the election?", ["32%", "40%", "36%", "38%"], "MCQ", "3", "Medium",
 "Turnout is smallest with staid campaigns. Which campaign types lose the most voters?",
 steps(p("At levels 1 and 1 the turnouts are 40 (issues), 38 (Amiya attacks), 39 (Ramya attacks) and 36 (both attack). Higher levels only raise turnout. The minimum is 36%.")) + final("36%, option 3"),
 [("1", "No combination drops below 36%."), ("2", "40% is the turnout when both are staid and focus on issues."), ("4", "38% is the turnout when only Amiya attacks.")])
P.dq(20, "If Amiya runs a campaign focusing on issues, then what is the maximum percentage of votes that she can get?", ["40%", "36%", "48%", "44%"], "MCQ", "3", "Medium",
 "Amiya gains from Ramya attacking her. Make both campaigns vigorous.",
 steps(p(r"If Ramya also focuses on issues, Amiya gets at most \(20 \times 2 = 40\%\). If Ramya attacks, Amiya gets \(20a + 4r\), which is largest at \(a = r = 2\): \(40 + 8 = 48\%\).")) + final("48%, option 3"),
 [("1", "This is her best with both on issues; Ramya attacking helps her more."), ("2", "36% is what she gets in the both-attack case at level 2."), ("4", "44% comes from a staid Ramya; a vigorous Ramya hands over more voters.")])
P.dq(21, "If Ramya runs a campaign attacking Amiya, then what is the minimum percentage of votes that she is guaranteed to get?", ["30%", "15%", "12%", "18%"], "MCQ", "2", "Medium",
 "Take Ramya’s weakest level and the worst response from Amiya.",
 steps(p(r"If Amiya focuses on issues, Ramya gets \(15r\); if Amiya also attacks, Ramya gets \(18r\). The smallest is at \(r = 1\) with Amiya on issues: 15%.")) + final("15%, option 2"),
 [("1", "30% needs Ramya to campaign vigorously."), ("3", "No case gives Ramya as little as 12%."), ("4", "18% is what she gets when both attack, not the worst case.")])
P.dq(22, "What is the maximum possible voting margin with which one of the candidates can win?", ["20%", "29%", "26%", "28%"], "MCQ", "2", "Hard",
 "Look along the outcome table for the widest gap.",
 steps(p("The widest gaps: both issues 20; Amiya attacking with a = 1, r = 2 gives 42 − 16 = 26; Ramya attacking with a = 2, r = 1 gives 44 − 15 = 29; both attacking gives at most 18. The maximum is 29%.")) + final("29%, option 2"),
 [("1", "20% is the most with both on issues."), ("3", "26% is the best margin when Amiya attacks."), ("4", "No outcome gives a margin of 28.")])
