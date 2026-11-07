# -*- coding: utf-8 -*-
# Batch 8 — CAT 2021 Slot 1: QA Q1–22 (exam order).
from fmt import steps, final, trap, why, table, p
from b8_21s1 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"Two trains cross each other in \(14\) seconds when running in opposite directions along parallel tracks. The faster train is \(160\) m long and crosses a lamp post in \(12\) seconds. If the speed of the other train is \(6\) km/hr less than the faster one, its length, in m, is",
 M("184", "192", "190", "180"), "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Find the faster train’s speed from the lamp post, then use the combined length when they cross.",
 steps(("Speeds", p(r"Faster train: \(\tfrac{160}{12} = \tfrac{40}{3}\) m/s, which is 48 km/hr. The other runs at 42 km/hr. Together, 90 km/hr = 25 m/s.")),
       ("Crossing", p(r"In 14 seconds they cover \(25 \times 14 = 350\) m, the two lengths combined. So the other train is \(350 - 160 = 190\) m."))) + final(r"\(190\), option 3"),
 concept=r"\[\text{opposite directions: time} = \frac{L_1 + L_2}{v_1 + v_2}\]",
 why_rows=[("1", "Not 350 − 160."), ("2", "Not 350 − 160."), ("4", "Not 350 − 160.")])

P.qa(2, r"If the area of a regular hexagon is equal to the area of an equilateral triangle of side \(12\) cm, then the length, in cm, of each side of the hexagon is",
 M(r"4\sqrt6", r"2\sqrt6", r"6\sqrt6", r"\sqrt6"), "MCQ", "2", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "A regular hexagon is six equilateral triangles.",
 steps(("Setting up", p(r"Hexagon with side \(s\): \(6 \times \tfrac{\sqrt3}{4}s^2\). Triangle: \(\tfrac{\sqrt3}{4} \times 144\).")),
       ("Solving", p(r"\(6s^2 = 144\), so \(s^2 = 24\) and \(s = 2\sqrt6\)."))) + final(r"\(2\sqrt6\), option 2"),
 shortcut="The hexagon is six small triangles, so each has a sixth of the big triangle’s area: side 12/√6 = 2√6.",
 concept=r"\[\text{regular hexagon} = 6 \times \frac{\sqrt3}{4}s^2\]",
 why_rows=[("1", r"Its area would be four times too big."), ("3", r"Its area would be nine times too big."), ("4", r"Its area would be a quarter of the triangle’s.")])

P.qa(3, r"Suppose the length of each side of a regular hexagon \(ABCDEF\) is \(2\) cm. If \(T\) is the mid point of \(CD\), then the length of \(AT\), in cm is",
 M(r"\sqrt{15}", r"\sqrt{12}", r"\sqrt{14}", r"\sqrt{13}"), "MCQ", "4", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 r"In a regular hexagon, angle \(ACD\) is a right angle.",
 steps(("AC", p(r"\(AC\) skips one vertex, so \(AC = \sqrt3 \times 2 = 2\sqrt3\).")),
       ("Right triangle", p(r"Angle \(ACD = 120^\circ - 30^\circ = 90^\circ\). With \(CT = 1\): \(AT^2 = 12 + 1 = 13\)."))) + final(r"\(\sqrt{13}\), option 4"),
 concept=r"\[\text{in a regular hexagon of side } a: \; AC = a\sqrt3, \quad AD = 2a\]",
 why_rows=[("1", r"Would need \(CT^2 = 3\)."), ("2", r"That is \(AC\) itself."), ("3", r"Would need \(CT^2 = 2\).")])

P.qa(4, r"Anu, Vinu and Manu can complete a work alone in \(15\) days, \(12\) days and \(20\) days, respectively. Vinu works everyday. Anu works only on alternate days starting from the first day while Manu works only on alternate days starting from the second day. Then, the number of days needed to complete the work is",
 [], "TITA", "7", ["Arithmetic::Time_and_Work"], "Easy",
 "Take the work as 60 units and find what each two-day block achieves.",
 steps(("Rates", p("Anu 4, Vinu 5, Manu 3 units a day.")),
       ("Two days at a time", p("Day 1: Vinu + Anu = 9. Day 2: Vinu + Manu = 8. Each pair of days does 17.")),
       ("Finishing", p("Six days give 51. Day 7 (Vinu + Anu) adds 9, making exactly 60."))) + final(r"\(7\)"),
 concept=p("Take the whole job as the LCM of the individual times, so every rate is a whole number."))

P.qa(5, r"The amount Neeta and Geeta together earn in a day equals what Sita alone earns in \(6\) days. The amount Sita and Neeta together earn in a day equals what Geeta alone earns in \(2\) days. The ratio of the daily earnings of the one who earns the most to that of the one who earns the least is",
 M("11 : 3", "3 : 2", "7 : 3", "11 : 7"), "MCQ", "1", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Write N + G = 6S and S + N = 2G, and put S = 1.",
 steps(("Solving", p(r"With \(S = 1\): \(N + G = 6\) and \(N = 2G - 1\). So \(3G - 1 = 6\), \(G = \tfrac73\), \(N = \tfrac{11}{3}\).")),
       ("Most and least", p(r"Neeta earns most and Sita least: \(\tfrac{11}{3} : 1 = 11 : 3\)."))) + final(r"\(11 : 3\), option 1"),
 concept=p("With two equations in three unknowns, fix one of them at 1 and solve for the ratios."),
 why_rows=[("2", "Not the ratio of the largest to the smallest."), ("3", "Geeta to Sita."), ("4", "Neeta to Geeta.")])

P.qa(6, r"Onion is sold for \(5\) consecutive months at the rate of ₹\(10\), ₹\(20\), ₹\(25\), ₹\(25\), and ₹\(50\) per kg, respectively. A family spends a fixed amount of money on onion for each of the first three months, and then spends half that amount on onion for each of the next two months. The average expense for onion, in rupees per kg, for the family over these \(5\) months is closest to",
 M("16", "26", "20", "18"), "MCQ", "4", ["Arithmetic::Average"], "Easy",
 "Average price = total money ÷ total kilograms. Pick a convenient monthly amount.",
 steps(("Pick an amount", p("Say ₹100 a month for three months and ₹50 for the next two. Total spent ₹400.")),
       ("Kilograms bought", p("10 + 5 + 4 + 2 + 1 = 22 kg.")),
       ("Average", p(r"\(\tfrac{400}{22} \approx 18.2\)."))) + trap("Averaging the five prices gives 26, but that ignores how much was bought at each price.") + final(r"\(18\), option 4"),
 concept=r"\[\text{average price} = \frac{\text{total spent}}{\text{total quantity}}\]",
 why_rows=[("1", "Too low."), ("2", "The plain average of the five prices."), ("3", "Too high.")])

P.qa(7, r"The number of groups of three or more distinct numbers that can be chosen from \(1, 2, 3, 4, 5, 6, 7\) and \(8\) so that the groups always include \(3\) and \(5\), while \(7\) and \(8\) are never included together is",
 [], "TITA", "47", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "With 3 and 5 fixed, choose any non-empty set from the other six numbers, but not 7 and 8 together.",
 steps(("The free choices", p("From 1, 2, 4, 6: any subset, 16 ways. From 7 and 8: neither, 7 only or 8 only, 3 ways. That gives 48.")),
       ("Size at least three", p("Only the empty choice gives a group smaller than three. 48 − 1 = 47."))) + final(r"\(47\)"),
 concept=r"\[\text{a set of } n \text{ elements has } 2^n \text{ subsets}\]")

P.qa(8, r"Amal purchases some pens at ₹\(8\) each. To sell these, he hires an employee at a fixed wage. He sells \(100\) of these pens at ₹\(12\) each. If the remaining pens are sold at ₹\(11\) each, then he makes a net profit of ₹\(300\), while he makes a net loss of ₹\(300\) if the remaining pens are sold at ₹\(9\) each. The wage of the employee, in INR, is",
 [], "TITA", "1000", ["Arithmetic::Profit_Loss_and_Discount"], "Easy",
 "The two cases differ only in the ₹2 per pen on the remaining pens.",
 steps(("Remaining pens", p("Selling them at ₹11 instead of ₹9 turns a ₹300 loss into a ₹300 profit: ₹600 more. So there are 300 remaining pens and 400 pens in all.")),
       ("The wage", p(r"Revenue in the first case: \(1200 + 3300 = 4500\). Cost of pens: 3200. Profit 300 means the wage is \(4500 - 3200 - 300 = 1000\)."))) + final(r"\(1000\)"),
 concept=r"\[\text{profit} = \text{revenue} - \text{cost of goods} - \text{fixed costs}\]")

P.qa(9, r"A basket of \(2\) apples, \(4\) oranges and \(6\) mangoes costs the same as a basket of \(1\) apple, \(4\) oranges and \(8\) mangoes, or a basket of \(8\) oranges and \(7\) mangoes. Then the number of mangoes in a basket of mangoes that has the same cost as the other baskets is",
 M("13", "12", "11", "10"), "MCQ", "1", ["Algebra::Linear_Equations"], "Easy",
 "Compare the first two baskets to get the apple in terms of mangoes.",
 steps(("Apple", p(r"\(2a + 4o + 6m = a + 4o + 8m\) gives \(a = 2m\).")),
       ("Orange", p(r"\(a + 4o + 8m = 8o + 7m\) becomes \(10m + 4o = 8o + 7m\), so \(4o = 3m\).")),
       ("The basket", p(r"\(8o + 7m = 6m + 7m = 13m\)."))) + final(r"\(13\), option 1"),
 concept=p("Express everything in one unit (here, mangoes) and compare."),
 why_rows=[("2", "Off by one mango."), ("3", "Off by two."), ("4", "Off by three.")])

P.qa(10, r"The number of integers \(n\) that satisfy the inequalities \(|n - 60| < |n - 100| < |n - 20|\) is",
 M("19", "18", "20", "21"), "MCQ", "1", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 r"\(|n - a| < |n - b|\) means \(n\) is closer to \(a\) than to \(b\).",
 steps(("First part", p(r"Closer to 60 than to 100: \(n < 80\).")),
       ("Second part", p(r"Closer to 100 than to 20: \(n > 60\).")),
       ("Counting", p("61 to 79: 19 integers."))) + final(r"\(19\), option 1"),
 concept=r"\[|n - a| < |n - b| \iff n \text{ is on } a\text{'s side of } \tfrac{a + b}{2}\]",
 why_rows=[("2", "Leaves out one end."), ("3", "Includes 60 or 80, where one inequality becomes an equality."), ("4", "Includes both 60 and 80.")])

P.qa(11, r"How many three-digit numbers are greater than \(100\) and increase by \(198\) when the three digits are arranged in the reverse order?",
 [], "TITA", "70", ["Number_System::Miscellaneous"], "Easy",
 r"Reversing \(\overline{abc}\) changes it by \(99(c - a)\).",
 steps(("The condition", p(r"\(99(c - a) = 198\), so \(c = a + 2\).")),
       ("Counting", p(r"\(a\) can be 1 to 7 (so \(c\) is 3 to 9) and the middle digit anything: \(7 \times 10 = 70\)."))) + final(r"\(70\)"),
 concept=r"\[\overline{cba} - \overline{abc} = 99(c - a)\]")

P.qa(12, r"Anil invests some money at a fixed rate of interest, compounded annually. If the interests accrued during the second and third year are ₹\(806.25\) and ₹\(866.72\), respectively, the interest accrued, in INR, during the fourth year is nearest to",
 M("931.72", "926.84", "929.48", "934.65"), "MCQ", "1", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Each year’s interest is the previous year’s times (1 + r).",
 steps(("The rate", p(r"\(\tfrac{866.72}{806.25} \approx 1.075\), so 7.5%.")),
       ("Fourth year", p(r"\(866.72 \times 1.075 \approx 931.72\)."))) + final(r"\(931.72\), option 1"),
 concept=r"\[I_{n+1} = I_n (1 + r) \text{ under compound interest}\]",
 why_rows=[("2", "Uses a slightly lower rate."), ("3", "Uses a slightly lower rate."), ("4", "Uses a slightly higher rate.")])

P.qa(13, r"Suppose hospital A admitted \(21\) less Covid infected patients than hospital B, and all eventually recovered. The sum of recovery days for patients in hospitals A and B were \(200\) and \(152\), respectively. If the average recovery days for patients admitted in hospital A was \(3\) more than the average in hospital B, then the number admitted in hospital A was",
 [], "TITA", "35", ["Arithmetic::Average"], "Medium",
 r"Let A admit \(a\) patients and B \(a + 21\). Compare the two averages.",
 steps(("Equation", r"\[\frac{200}{a} = \frac{152}{a + 21} + 3\]"),
       ("Solving", p(r"\(200a + 4200 = 152a + 3a^2 + 63a\), so \(a^2 + 5a - 1400 = 0\): \((a + 40)(a - 35) = 0\), and \(a = 35\)."))) + final(r"\(35\)"),
 concept=r"\[\text{average} = \frac{\text{total}}{\text{count}}\]")

P.qa(14, r"A circle of diameter \(8\) inches is inscribed in a triangle \(ABC\) where \(\angle ABC = 90^\circ\). If \(BC = 10\) inches, then the area of the triangle in square inches is",
 [], "TITA", "120", ["Geometry::Triangles", "Geometry::Circles"], "Medium",
 "Tangents from a point to a circle are equal. From the right-angle corner, both tangents equal the radius.",
 steps(("Tangent lengths", p(r"The radius is 4, so the tangents from B are 4. On BC, the tangent from C is \(10 - 4 = 6\). Let \(AB = x\); the tangent from A is \(x - 4\), so \(AC = (x - 4) + 6 = x + 2\).")),
       ("Pythagoras", p(r"\(x^2 + 100 = (x + 2)^2\) gives \(x = 24\).")),
       ("Area", p(r"\(\tfrac12 \times 24 \times 10 = 120\)."))) + final(r"\(120\)"),
 shortcut=r"For a right triangle, the inradius is \(\tfrac{a + b - c}{2}\).",
 concept=r"\[r = \frac{a + b - c}{2} \text{ (right triangle with legs } a, b\text{)}\]")

P.qa(15, r"\(f(x) = \dfrac{x^2 + 2x - 15}{x^2 - 7x - 18}\) is negative if and only if",
 [r"\(x < -5\) or \(-2 < x < 3\)", r"\(-5 < x < -2\) or \(3 < x < 9\)", r"\(-2 < x < 3\) or \(x > 9\)", r"\(x < -5\) or \(3 < x < 9\)"], "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "Factorise top and bottom and mark the four critical points on a number line.",
 steps(("Factorising", p(r"\(f(x) = \dfrac{(x + 5)(x - 3)}{(x - 9)(x + 2)}\). Critical points: \(-5, -2, 3, 9\).")),
       ("Signs", p(r"For \(x > 9\) every factor is positive, so \(f > 0\). The sign then flips at each critical point: negative on \((3, 9)\), positive on \((-2, 3)\), negative on \((-5, -2)\), positive below \(-5\)."))) +
 final(r"\(-5 < x < -2\) or \(3 < x < 9\), option 2"),
 concept=r"\[\text{wavy curve: the sign alternates across each simple root}\]",
 why_rows=[("1", "Both intervals are where it is positive."), ("3", "Positive intervals."), ("4", r"\(x < -5\) is positive.")])

P.qa(16, r"If \(5 - \log_{10}\sqrt{1 + x}\) \(+\, 4\log_{10}\sqrt{1 - x}\) \(= \log_{10}\dfrac{1}{\sqrt{1 - x^2}}\), then \(100x\) equals",
 [], "TITA", "99", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"Write everything in terms of \(\log(1 + x)\) and \(\log(1 - x)\).",
 steps(("Expanding", p(r"Left: \(5 - \tfrac12\log(1 + x)\) \(+\, 2\log(1 - x)\). Right: \(-\tfrac12\log(1 + x)\) \(-\, \tfrac12\log(1 - x)\).")),
       ("Simplifying", p(r"The \(\log(1 + x)\) terms cancel: \(5 + \tfrac52\log(1 - x) = 0\), so \(\log(1 - x) = -2\).")),
       ("Solving", p(r"\(1 - x = 0.01\), \(x = 0.99\), \(100x = 99\)."))) + final(r"\(99\)"),
 concept=r"\[\log\sqrt{a} = \tfrac12\log a, \qquad \log\frac1a = -\log a\]")

P.qa(17, r"Amar, Akbar and Anthony are working on a project. Working together Amar and Akbar can complete the project in \(1\) year, Akbar and Anthony can complete in \(16\) months, Anthony and Amar can complete in \(2\) years. If the person who is neither the fastest nor the slowest works alone, the time in months he will take to complete the project is",
 [], "TITA", "32", ["Arithmetic::Time_and_Work"], "Medium",
 "Take the project as 48 units (LCM of 12, 16, 24 months).",
 steps(("Pair rates", p("Amar + Akbar 4, Akbar + Anthony 3, Anthony + Amar 2 units a month. Adding: twice the total is 9, so all three do 4.5.")),
       ("Each person", p("Amar 1.5, Akbar 2.5, Anthony 0.5. Amar is in the middle.")),
       ("Amar alone", p(r"\(\tfrac{48}{1.5} = 32\) months."))) + final(r"\(32\)"),
 concept=r"\[a = \frac{(a + b) + (c + a) - (b + c)}{2}\]")

P.qa(18, r"If \(x_0 = 1\), \(x_1 = 2\), and \(x_{n+2} = \dfrac{1 + x_{n+1}}{x_n}\), \(n = 0, 1, 2, 3, \ldots\), then \(x_{2021}\) is equal to",
 M("1", "2", "3", "4"), "MCQ", "2", ["Algebra::Progressions_and_Series"], "Easy",
 "Work out a few terms. The sequence repeats.",
 steps(("Terms", p(r"\(x_2 = 3\), \(x_3 = 2\), \(x_4 = 1\), \(x_5 = 1\), \(x_6 = 2\). It repeats every 5 terms.")),
       ("x₂₀₂₁", p(r"\(2021 = 5 \times 404 + 1\), so \(x_{2021} = x_1 = 2\)."))) + final(r"\(2\), option 2"),
 concept=p("For an unfamiliar recurrence, compute terms until one pair repeats; from then on the sequence cycles."),
 why_rows=[("1", r"That is \(x_0\) or \(x_4\)."), ("3", r"That is \(x_2\)."), ("4", "Never appears in the sequence.")])

P.qa(19, r"The strength of an indigo solution in percentage is equal to the amount of indigo in grams per \(100\) cc of water. Two \(800\) cc bottles are filled with indigo solutions of strengths \(33\%\) and \(17\%\), respectively. A part of the solution from the first bottle is thrown away and replaced by an equal volume of the solution from the second bottle. If the strength of the indigo solution in the first bottle has now changed to \(21\%\) then the volume, in cc, of the solution left in the second bottle is",
 [], "TITA", "200", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Mix 33% and 17% to get 21%. Alligation gives the ratio.",
 steps(("Alligation", p(r"\(\tfrac{33\% \text{ part}}{17\% \text{ part}} = \tfrac{21 - 17}{33 - 21} = \tfrac{4}{12} = \tfrac13\). So 200 cc of the first solution stays and 600 cc comes from the second bottle.")),
       ("Second bottle", p(r"\(800 - 600 = 200\) cc left."))) + final(r"\(200\)"),
 concept=r"\[\frac{q_1}{q_2} = \frac{c_2 - c}{c - c_1}\]")

P.qa(20, r"Identical chocolate pieces are sold in boxes of two sizes, small and large. The large box is sold for twice the price of the small box. If the selling price per gram of chocolate in the large box is \(12\%\) less than that in the small box, then the percentage by which the weight of chocolate in the large box exceeds that in the small box is nearest to",
 M("135", "124", "127", "144"), "MCQ", "3", ["Arithmetic::Percentages"], "Easy",
 "Weight = price ÷ price per gram.",
 steps(("Ratio of weights", p(r"\(\dfrac{W_L}{W_S} = \dfrac{2}{0.88} \approx 2.273\).")),
       ("Excess", p("So the large box has about 127% more."))) + final(r"\(127\), option 3"),
 concept=r"\[\text{quantity} = \frac{\text{price}}{\text{price per unit}}\]",
 why_rows=[("1", "Too high."), ("2", "Uses 2 × 1.12 = 2.24, treating 12% less as dividing by 1.12."), ("4", "Too high.")])

P.qa(21, r"The natural numbers are divided into groups as \((1), (2, 3, 4), (5, 6, 7, 8, 9), \ldots\) and so on. Then, the sum of the numbers in the \(15\)th group is equal to",
 M("4941", "6090", "6119", "7471"), "MCQ", "3", ["Algebra::Progressions_and_Series"], "Easy",
 r"Group \(k\) ends at \(k^2\).",
 steps(("The 15th group", p(r"It runs from \(14^2 + 1 = 197\) to \(15^2 = 225\): 29 numbers.")),
       ("Sum", p(r"\(29 \times \tfrac{197 + 225}{2} = 29 \times 211 = 6119\)."))) + final(r"\(6119\), option 3"),
 concept=r"\[\text{group } k \text{ has } 2k - 1 \text{ terms and ends at } k^2\]",
 why_rows=[("1", "The sum of the 14th group, 170 to 196."), ("2", "Not the sum of 197 to 225."), ("4", "The sum of the 16th group, 226 to 256.")])

P.qa(22, r"If \(r\) is a constant such that \(|x^2 - 4x - 13| = r\) has exactly three distinct real roots, then the value of \(r\) is",
 M("15", "21", "18", "17"), "MCQ", "4", ["Algebra::Inequalities_and_Absolute_Value", "Algebra::Quadratic_Equations"], "Medium",
 r"Picture \(y = |x^2 - 4x - 13|\). A horizontal line meets it in three points only at one height.",
 steps(("The graph", p(r"\(x^2 - 4x - 13\) has its minimum \(-17\) at \(x = 2\). Taking the absolute value flips that dip up into a hump of height 17.")),
       ("Three roots", p(r"The line \(y = r\) meets the graph in four points for \(0 < r < 17\), in three when it touches the top of the hump (\(r = 17\)), and in two above that."))) +
 final(r"\(17\), option 4"),
 concept=p(r"\(|f(x)| = r\) can have an odd number of roots only when \(r\) is the height of a turning point."),
 why_rows=[("1", "Below 17: four roots."), ("2", "Above 17: two roots."), ("3", "Above 17: two roots.")])
