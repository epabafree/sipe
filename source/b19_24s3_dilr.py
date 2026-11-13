# -*- coding: utf-8 -*-
# Batch 19 — CAT 2024 Slot 3: DILR sets 1–5 (Q1–22, in exam order).
from fmt import steps, final, trap, why, table, p
from b19_24s3 import P
import b19_24s3_figs as F

DIR = "Read the information given below and answer the questions that follow."

# ---------------- Set 1: ATMs on a road grid ----------------
P.dilr_set(1, "Set 1 — Six ATMs on a grid of roads", DIR,
 p("The figure below shows a network with three parallel roads represented by horizontal lines R-A, R-B, and R-C and another three parallel roads represented by vertical lines V1, V2, and V3. The figure also shows the distance (in km) between two adjacent intersections. Six ATMs are placed at six of the nine road intersections. Each ATM has a distinct integer cash requirement (in Rs. Lakhs), and the numbers at the end of each line in the figure indicate the total cash requirements of all ATMs placed on the corresponding road. For example, the total cash requirement of the ATM(s) placed on road R-A is Rs. 22 Lakhs.") + F.ROADS +
 p("The following additional information is known.") +
 "<ol><li>The ATMs with the minimum and maximum cash requirements of Rs. 7 Lakhs and Rs. 15 Lakhs are placed on the same road.</li><li>The road distance between the ATM with the second highest cash requirement and the ATM located at the intersection of R-C and V3 is 12 km.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("What the totals allow", p("All six amounts lie between 7 and 15 and are different. The grand total is 22 + 20 + 20 = 62. 7 + 15 = 22, so the other four ATMs add to 40, using four different numbers from 8 to 14.")),
       ("Where 7 and 15 go", p("They share a road and add to 22, which is exactly R-A’s total. So they are the only two ATMs on R-A. (On a vertical road the totals 15, 21, 26 don’t allow 7 + 15 plus anything.) R-B and R-C then hold two ATMs each, adding to 20 each.")),
       ("The 12 km clue", p("There is an ATM at (R-C, V3). An intersection 12 km away by road is (R-B, V2): 7 km along R-B plus 5 km down V3. (R-A, V1) is 19 km away and (R-B, V1) is 16 km away; no other ATM spot works. So the second-highest ATM is at (R-B, V2).")),
       ("Filling in", p("R-C has (R-C, V3) and one other. Testing the column totals leaves two arrangements, both with (R-B, V2) = 12, (R-C, V2) = 9 and (R-C, V3) = 11.") +
          table(["", "V1", "V2", "V3"], [["R-A", "7", "–", "15"], ["R-B", "8", "12", "–"], ["R-C", "–", "9", "11"]]) +
          table(["", "V1", "V2", "V3"], [["R-A", "15", "–", "7"], ["R-B", "–", "12", "8"], ["R-C", "–", "9", "11"]]) +
          p("In the first, V1 = 7 + 8 = 15, V2 = 12 + 9 = 21, V3 = 15 + 11 = 26. In the second, V1 = 15, V2 = 21, V3 = 7 + 8 + 11 = 26. Both fit every clue."))) +
 final("Two arrangements; (R-B, V2) = 12, (R-C, V2) = 9 and (R-C, V3) = 11 in both."),
 p("Start from R-A: its total 22 is exactly 7 + 15. Then the 12 km clue fixes the second-highest ATM."),
 p("<b>Grid totals:</b> when every row and column total is known, the grand total and the extreme values usually fix the first few cells. Road distance on a grid is the sum of the horizontal and vertical legs."))
P.dq(1, "Which of the following statements is correct?", ["The ATM placed at the (R-C, V2) intersection has a cash requirement of Rs. 9 Lakhs.", "The cash requirement of the ATM placed at the (R-C, V2) intersection cannot be uniquely determined.", "The ATM placed at the (R-C, V2) intersection has a cash requirement of Rs. 8 Lakhs.", "There is no ATM placed at the (R-C, V2) intersection."], "MCQ", "1", "Medium",
 "R-C has 11 at V3. What makes its total 20?",
 steps(p("R-C’s total is 20 and (R-C, V3) is 11, so (R-C, V2) is 9 in both arrangements.")) + final("Option 1"),
 [("2", "It is 9 in both arrangements."), ("3", "8 is at (R-B, V1) or (R-B, V3)."), ("4", "There is an ATM there in both arrangements.")])
P.dq(2, "How many ATMs have cash requirements of Rs. 10 Lakhs or more?", [], "TITA", "3", "Easy",
 "The amounts are 7, 8, 9, 11, 12 and 15.",
 steps(p("11, 12 and 15.")) + final(r"\(3\)"))
P.dq(3, "Which of the following two statements is/are DEFINITELY true?<br>Statement A: Each of R-A, R-B, and R-C has two ATMs.<br>Statement B: Each of V1, V2, and V3 has two ATMs.", ["Only Statement B", "Neither Statement A nor Statement B", "Both Statement A and Statement B", "Only Statement A"], "MCQ", "4", "Medium",
 "Check the column counts in the second arrangement.",
 steps(p("Every arrangement has two ATMs on each horizontal road. In the second arrangement V1 has one ATM and V3 has three, so B is not certain.")) + final("Only Statement A, option 4"),
 [("1", "B fails in the second arrangement."), ("2", "A holds in both arrangements."), ("3", "B fails in the second arrangement.")])
P.dq(4, "What best can be said about the road distance (in km) between the ATMs having the second highest and the second lowest cash requirements?", ["4 km", "5 km", "Either 4 km or 7 km", "7 km"], "MCQ", "3", "Medium",
 "12 is at (R-B, V2). Where can 8 be?",
 steps(p("8 is at (R-B, V1), 4 km from (R-B, V2), or at (R-B, V3), 7 km away.")) + final("Either 4 km or 7 km, option 3"),
 [("1", "That is only the first arrangement."), ("2", "5 km is the R-B to R-C gap; it isn’t the distance here."), ("4", "That is only the second arrangement.")])
P.dq(5, "What is the number of ATMs whose locations and cash requirements can both be uniquely determined?", [], "TITA", "3", "Medium",
 "Compare the two arrangements cell by cell.",
 steps(p("(R-B, V2) = 12, (R-C, V2) = 9 and (R-C, V3) = 11 are the same in both. The positions of 7, 8 and 15 change.")) + final(r"\(3\)"))

# ---------------- Set 2: OTT subscribers ----------------
P.dilr_set(2, "Set 2 — Subscribers of a streaming platform", DIR,
 p("Over the top (OTT) subscribers of a platform are segregated into three categories: i) Kid, ii) Elder, and iii) Others. Some of the subscribers used one app and the others used multiple apps to access the platform. The figure below shows the percentage of the total number of subscribers in 2023 and 2024 who belong to the ‘Kid’ and ‘Elder’ categories.") + F.OTT +
 p("The following additional facts are known about the numbers of subscribers.") +
 "<ol><li>The total number of subscribers increased by 10% from 2023 to 2024.</li><li>In 2024, 1/2 of the subscribers from the ‘Kid’ category and 2/3 of the subscribers from the ‘Elder’ category subscribers use one app.</li><li>In 2023, the number of subscribers from the ‘Kid’ category who used multiple apps was the same as the number of subscribers from the ‘Elder’ category who used one app.</li><li>10,000 subscribers from the ‘Kid’ category used one app and 15,000 subscribers from the ‘Elder’ category used multiple apps in 2023.</li></ol>",
 "DILR::DI::Graphs_and_Charts",
 steps(("2023 totals", p(r"Let the 2023 total be \(100x\): Kid \(15x\), Elder \(20x\). Kid multiple-app users are \(15x - 10000\), which equals Elder one-app users. So Elder \(= (15x - 10000) + 15000 = 20x\), giving \(x = 1000\). The total is 100,000.")),
       ("The tables", table(["2023", "One", "Multiple", "Total"], [["Kid", "10,000", "5,000", "15,000"], ["Elder", "5,000", "15,000", "20,000"], ["Others", "", "", "65,000"]]) +
          table(["2024", "One", "Multiple", "Total"], [["Kid", "11,000", "11,000", "22,000"], ["Elder", "22,000", "11,000", "33,000"], ["Others", "", "", "55,000"]]) +
          p("The 2024 total is 110,000. The split of ‘Others’ between one and multiple apps is not given."))) +
 final("2023 total 100,000; 2024 total 110,000."),
 p("Set the 2023 total as 100x; the two facts about 2023 give one equation in x."),
 p("<b>Percent-of-total charts:</b> once one actual count is known, every percentage turns into a count."))
P.dq(6, "How many subscribers belonged to the ‘Others’ category in 2024?", ["45000", "55000", "Cannot be determined", "65000"], "MCQ", "2", "Easy",
 "Kid and Elder are 50% of 110,000 in 2024.",
 steps(p(r"\(110000 \times 50\% = 55000\).")) + final("55,000, option 2"),
 [("1", "This would be 41% of the total."), ("3", "The total and both percentages are known, so it can be found."), ("4", "65,000 is the 2023 figure.")])
P.dq(7, "What percentage of subscribers in the ‘Kid’ category used multiple apps in 2023?", ["50.00%", "5.00%", "33.33%", "25.50%"], "MCQ", "3", "Easy",
 "Kid had 15,000 subscribers in 2023, of whom 10,000 used one app.",
 steps(p(r"\(5000 \div 15000 = 33.33\%\).")) + final("33.33%, option 3"),
 [("1", "That is the 2024 figure."), ("2", "This is 5,000 as a share of all 100,000 subscribers."), ("4", "This doesn’t match the counts.")])
P.dq(8, "What was the percentage increase in the number of subscribers in the ‘Elder’ category from 2023 to 2024?", ["50%", "65%", "60%", "40%"], "MCQ", "2", "Easy",
 "20% of 100,000 against 30% of 110,000.",
 steps(p(r"From 20,000 to 33,000: \(13000 \div 20000 = 65\%\).")) + final("65%, option 2"),
 [("1", "This compares the percentages 20 and 30 and ignores the growth in the total."), ("3", "This doesn’t match the counts."), ("4", "This doesn’t match the counts.")])
P.dq(9, "What could be the minimum percentage of subscribers who used multiple apps in 2024?", ["20.0%", "10.0%", "22.00%", "16.5%"], "MCQ", "1", "Medium",
 "Kid and Elder multiple-app users are fixed. What is the smallest the ‘Others’ figure can be?",
 steps(p(r"Kid 11,000 + Elder 11,000 = 22,000 at least. If no ‘Others’ subscriber used multiple apps, the share is \(22000 \div 110000 = 20\%\).")) + final("20%, option 1"),
 [("2", "This counts only one category’s 11,000."), ("3", "This divides by 100,000, the 2023 total."), ("4", "This is below the 22,000 already fixed.")])

# ---------------- Set 3: GDP and population ----------------
P.dilr_set(3, "Set 3 — GDP, income per head and growth", DIR,
 p("Out of 10 countries -- Country 1 through Country 10 -- Country 9 has the highest gross domestic product (GDP), and Country 10 has the highest GDP per capita. GDP per capita is the GDP of a country divided by its population. The table below provides the following data about Country 1 through Country 8 for the year 2024.") +
 "<ul><li>Column 1 gives the country’s identity.</li><li>Column 2 gives the country’s GDP as a fraction of the GDP of Country 9.</li><li>Column 3 gives the country’s GDP per capita as a fraction of the GDP per capita of Country 10.</li><li>Column 4 gives the country’s annual GDP growth rate.</li><li>Column 5 gives the country’s annual population growth rate.</li></ul>" +
 table(["Country", "GDP", "GDP per capita"],
       [["1", "0.15", "0.41"], ["2", "0.14", "0.25"], ["3", "0.13", "0.02"], ["4", "0.12", "0.38"], ["5", "0.10", "0.36"], ["6", "0.08", "0.08"], ["7", "0.08", "0.30"], ["8", "0.07", "0.41"]]) +
 table(["Country", "GDP growth", "Population growth"],
       [["1", "0.2%", "–0.12%"], ["2", "0.9%", "–0.41%"], ["3", "6.5%", "0.70%"], ["4", "0.5%", "0.49%"], ["5", "0.7%", "0.31%"], ["6", "3.2%", "0.61%"], ["7", "0.7%", "–0.11%"], ["8", "1.2%", "0.71%"]]) +
 p("Assume that the GDP growth rates and population growth rates of the countries will remain constant for the next three years."),
 "DILR::DI::Data_Tabulation",
 steps(("Population from the table", p("Population = GDP ÷ GDP per capita. Both columns use a common base (Country 9 and Country 10), so the ratio of the two columns compares populations directly.") +
          table(["Country", "GDP ÷ per capita"], [["1", "0.366"], ["2", "0.560"], ["3", "6.5"], ["4", "0.316"], ["5", "0.278"], ["6", "1.0"], ["7", "0.267"], ["8", "0.171"]])),
       ("Growth", p("Each year GDP is multiplied by (1 + GDP growth) and population by (1 + population growth). GDP per capita changes by the ratio of the two."))) +
 final("Relative populations are in the table; every country’s GDP grows faster than its population."),
 p("Divide column 2 by column 3 to get relative populations; the unknown bases cancel when comparing countries."),
 p(r"<b>Per-capita figures:</b> \(\text{population} = \frac{\text{GDP}}{\text{GDP per capita}}\). Per-capita income rises when GDP grows faster than population."))
P.dq(10, "Which one among the countries 1 through 8, has the smallest population in 2024?", ["Country 8", "Country 5", "Country 3", "Country 7"], "MCQ", "1", "Easy",
 "Divide GDP by GDP per capita.",
 steps(p(r"Country 8: \(0.07 \div 0.41 \approx 0.17\), the smallest. Country 7 is 0.27 and Country 5 is 0.28.")) + final("Country 8, option 1"),
 [("2", "0.28, larger than Country 8."), ("3", "Country 3 has by far the largest population, 6.5."), ("4", "0.27, larger than Country 8.")])
P.dq(11, "The ratio of Country 4’s GDP to Country 5’s GDP in 2026 will be closest to", ["1.032", "1.195", "1.314", "0.963"], "MCQ", "2", "Medium",
 "Two years of growth at 0.5% and 0.7%.",
 steps(p(r"\(\frac{0.12 \times 1.005^2}{0.10 \times 1.007^2} = 1.2 \times \frac{1.0100}{1.0140} \approx 1.195\).")) + final("1.195, option 2"),
 [("1", "This is far below the starting ratio of 1.2."), ("3", "This is above 1.2, though Country 5 grows faster."), ("4", "Country 4’s GDP stays larger than Country 5’s.")])
P.dq(12, "Which one among the countries 1, 4, 5, and 7 will have the largest population in 2027?", ["Country 7", "Country 4", "Country 5", "Country 1"], "MCQ", "4", "Medium",
 "Compare 2024 populations first. Do three years of small growth change the order?",
 steps(p(r"2024: Country 1 0.366, Country 4 0.316, Country 5 0.278, Country 7 0.267. Over three years Country 1 shrinks by about 0.36% to 0.365, while Country 4 grows by about 1.5% to 0.321. Country 1 is still the largest.")) + final("Country 1, option 4"),
 [("1", "Country 7 starts smallest and shrinks."), ("2", "Country 4 grows, but only to about 0.32."), ("3", "Country 5 reaches only about 0.28.")])
P.dq(13, "For how many countries among Country 1 through Country 8 will the GDP per capita in 2027 be lower than that in 2024?", [], "TITA", "0", "Easy",
 "GDP per capita falls only if population grows faster than GDP.",
 steps(p("In every row the GDP growth rate is higher than the population growth rate (Country 4 is closest: 0.5% against 0.49%). So GDP per capita rises everywhere.")) + final(r"\(0\)"))

# ---------------- Set 4: Air-conditioner ----------------
P.dilr_set(4, "Set 4 — An air-conditioner through the night", DIR,
 p("The air-conditioner (AC) in a large room can be operated either in REGULAR mode or in POWER mode to reduce the temperature.") +
 p("If the AC operates in REGULAR mode, then it brings down the temperature inside the room (called inside temperature) at a constant rate to the set temperature in 1 hour. If it operates in POWER mode, then this is achieved in 30 minutes.") +
 p("If the AC is switched off, then the inside temperature rises at a constant rate so as to reach the temperature outside at the time of switching off in 1 hour. The temperature outside has been falling at a constant rate from 7 pm onward until 3 am on a particular night. The following graph shows the inside temperature between 11 pm (23:00) and 2 am (2:00) that night.") + F.AC +
 p("The following facts are known about the AC operation that night.") +
 "<ul><li>The AC was turned on for the first time that night at 11 pm (23:00).</li><li>The AC setting was changed (including turning it on/off, and/or setting different temperatures) only at the beginning of the hour or at 30 minutes after the hour.</li><li>The AC was used in POWER mode for longer duration than in REGULAR mode during this 3-hour period.</li></ul>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("On and off", p("The temperature falls while the AC is on and rises while it is off. So it was on 23:00–00:00, off 00:00–00:30, on 00:30–01:00, off 01:00–01:30 and on 01:30–02:00.")),
       ("The outside temperature", p("The AC had not been on before 23:00, so the room was at the outside temperature, 38 °C. When the AC goes off at 00:00, the room rises 5 °C in 30 minutes, so it would reach the outside temperature at 00:00, 36 °C, in an hour. So the outside temperature falls 2 °C an hour. Check: from 01:00 the room rises 4 °C in 30 minutes, heading for 34 °C, the outside temperature at 01:00.")),
       ("The modes", p("The AC was on for 2 hours in all, so POWER must cover more than 1 hour. The 23:00–00:00 drop is a straight line of 12 °C an hour. POWER mode set to 26 °C would get there by 23:30, too fast, so a single setting can’t give that line with POWER. The line needs a change at 23:30: either POWER to 32 °C, then a new setting; or REGULAR for the first half-hour and POWER for the second. Either way, POWER covers at least 30 minutes of that hour, plus at most 30 minutes in each later on-period, and there is a change at 23:30."))) +
 final("Outside temperature: 38 °C at 23:00, falling 2 °C an hour. AC off at 00:00 and 01:00, on again at 00:30 and 01:30, with a change at 23:30."),
 p("Read the graph as on (falling) and off (rising) segments. The rise after switching off reveals the outside temperature."),
 p("<b>Rate puzzles:</b> a constant rate that reaches a target in a known time tells you the target. Here, the rise in 30 minutes is half the gap to the outside temperature."))
P.dq(14, "How many times the AC must have been turned off between 11:01 pm and 1:59 am?", ["0", "2", "1", "cannot be determined"], "MCQ", "2", "Easy",
 "Count the points where the temperature starts rising.",
 steps(p("The room starts warming at 00:00 and at 01:00, so the AC was turned off twice.")) + final("2, option 2"),
 [("1", "The temperature rises twice, so it was switched off."), ("3", "There are two rising stretches."), ("4", "The graph settles it.")])
P.dq(15, "What was the temperature outside, in degree Celsius, at 1 am?", [], "TITA", "34", "Medium",
 "From 01:00 the room warms 4 °C in half an hour.",
 steps(p("At 01:00 the room is 26 °C and rises 4 °C in 30 minutes, so it would gain 8 °C in an hour, reaching 34 °C: the outside temperature at 01:00.")) + final(r"\(34\)"))
P.dq(16, "What was the temperature outside, in degree Celsius, at 9 pm?", [], "TITA", "42", "Medium",
 "Find the outside temperature at 23:00 and the rate at which it falls.",
 steps(p("It is 38 °C at 23:00 and falls 2 °C an hour, so two hours earlier it was 42 °C.")) + final(r"\(42\)"))
P.dq(17, "What best can be concluded about the number of times the AC must have either been turned on or the AC temperature setting been altered between 11:01 pm and 1:59 am?", ["Exactly 2", "Either 2 or 3", "More than 3", "Exactly 3"], "MCQ", "4", "Hard",
 "Two switch-ons are clear from the graph. Is a change at 23:30 forced by the POWER-mode condition?",
 steps(("Turned on", p("At 00:30 and 01:30.")),
       ("A forced change", p("Without a change at 23:30, the 23:00–00:00 line could only be REGULAR to 26 °C for the full hour. Then POWER could cover at most the two later half-hours, 1 hour, not more than REGULAR’s hour. So the setting must change at 23:30.")),
       ("Total", p("2 + 1 = 3, and nothing else is forced."))) + final("Exactly 3, option 4"),
 [("1", "This misses the change forced at 23:30."), ("2", "The change at 23:30 is required, not optional."), ("3", "No other change is forced.")])
P.dq(18, "What was the maximum difference between temperature outside and inside temperature, in degree Celsius, between 11:01 pm and 1:59 am?", [], "TITA", "10", "Medium",
 "Check the moments when the room is coolest.",
 steps(p("At 00:00 the room is 26 °C and outside is 36 °C: a gap of 10. At 01:00 it is 26 against 34: 8. At other times the gap is smaller.")) + final(r"\(10\)"))

# ---------------- Set 5: Nutrients in food grains ----------------
P.dilr_set(5, "Set 5 — Nutrients in seven food grains", DIR,
 p("The table given below shows the amount, in grams, of carbohydrate, protein, fat and all other nutrients, per 100 grams of nutrients in seven food grains. The first column shows the foodgrain category and the second column its codename. The table has some missing values.") +
 p("C1 and C2 are cereals, M1, M2 and M3 are millets, and P1 and P2 are pseudo-cereals. Amounts are in grams per 100 grams of nutrients; “Other” is all other nutrients.") +
 table(["Grain", "Carb", "Protein", "Fat", "Other"],
       [["C1", "", "", "0", "12"], ["C2", "", "", "3", "10"], ["M1", "62", "10", "", ""], ["M2", "", "", "7", "16"],
        ["M3", "56", "", "12", ""], ["P1", "66", "", "", "10"], ["P2", "", "14", "", "8"]]) +
 p("The following additional facts are known.") +
 "<ol><li>Both the pseudo-cereals had higher amounts of carbohydrate as well as higher amounts of protein than any millet.</li><li>Both the cereals had higher amounts of carbohydrate than any pseudo-cereal.</li><li>All the missing values of carbohydrate amounts (in grams) for all the foodgrains are non-zero multiples of 5.</li><li>All the missing values of protein, fat and other nutrients amounts (in grams) for all the foodgrains are non-zero multiples of 4.</li><li>P1 contained double the amount of protein that M3 contains.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("Each row adds to 100", p("Carbohydrate gaps are multiples of 5 and the others multiples of 4.")),
       ("C1 and C2", p("C1: carb + protein = 88. The carbs must exceed every pseudo-cereal (at least 66) and be a multiple of 5, with protein a multiple of 4: only 80 + 8 works. C2: carb + protein = 87: only 75 + 12 works.")),
       ("M2", p("Carb + protein = 77, with carb below 66 (pseudo-cereals have more) and protein below 14 (P2 has more): 65 + 12.")),
       ("M3 and P1", p("M3: protein + other = 32. P1: 2 × (M3 protein) + fat = 24, and P1’s protein must exceed 12 (M2’s): M3 protein 8, P1 protein 16, P1 fat 8, M3 other 24.")),
       ("P2", p("Carb + fat = 78, carb above 62 and below 75 (C2): 70 + 8. M1’s fat and other add to 28 but aren’t needed.") +
          table(["Grain", "Carb", "Protein", "Fat", "Other"],
                [["C1", "80", "8", "0", "12"], ["C2", "75", "12", "3", "10"], ["M1", "62", "10", "?", "?"], ["M2", "65", "12", "7", "16"],
                 ["M3", "56", "8", "12", "24"], ["P1", "66", "16", "8", "10"], ["P2", "70", "14", "8", "8"]]))) +
 final("Every value is fixed except M1’s fat and other nutrients, which add to 28."),
 p("Each row sums to 100, so every row with two gaps gives a sum. The multiples-of-5 and multiples-of-4 rules then leave one choice."),
 p("<b>Missing-value tables:</b> combine the row total with divisibility conditions; the order conditions remove the remaining choices."))
P.dq(19, "How many foodgrains had a higher amount of carbohydrate per 100 grams of nutrients than M1?", [], "TITA", "5", "Medium",
 "M1 has 62 g. Count the grains above it.",
 steps(p("C1 80, C2 75, P2 70, P1 66 and M2 65. Only M3 (56) is lower.")) + final(r"\(5\)"))
P.dq(20, "How many grams of protein were there in 100 grams of nutrients in M2?", [], "TITA", "12", "Medium",
 "M2’s carbohydrate and protein add to 77.",
 steps(p("Carbohydrate must be a multiple of 5 below 66 and protein a multiple of 4 below 14: 65 and 12.")) + final(r"\(12\)"))
P.dq(21, "How many grams of other nutrients were there in 100 grams of nutrients in M3?", [], "TITA", "24", "Hard",
 "Use P1 to find M3’s protein first.",
 steps(p("P1’s protein is double M3’s and P1’s protein plus fat is 24. P1 must have more protein than M2’s 12, so P1 has 16 and M3 has 8. Then M3’s other nutrients are 100 − 56 − 8 − 12 = 24.")) + final(r"\(24\)"))
P.dq(22, "What is the median of the number of grams of protein in 100 grams of nutrients among these food grains?", [], "TITA", "12", "Medium",
 "List the seven protein values in order.",
 steps(p("8, 8, 10, 12, 12, 14, 16. The middle (fourth) value is 12.")) + final(r"\(12\)"))
