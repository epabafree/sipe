# -*- coding: utf-8 -*-
# Batch 12 — CAT 2020 Slot 2: QA (all 26).
from fmt import steps, final, trap, why, table, p
from b12_20s2 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"The distance from B to C is thrice that from A to B. Two trains travel from A to C via B. The speed of train 2 is double that of train 1 while traveling from A to B and their speeds are interchanged while traveling from B to C. The ratio of the time taken by train 1 to that taken by train 2 in traveling from A to C is",
 M("1 : 4", "5 : 7", "4 : 1", "7 : 5"), "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 r"Take AB = \(d\), BC = \(3d\) and speeds \(v\) and \(2v\).",
 steps(("Train 1", p(r"\(\tfrac dv + \tfrac{3d}{2v} = \tfrac{5d}{2v}\).")),
       ("Train 2", p(r"\(\tfrac{d}{2v} + \tfrac{3d}{v} = \tfrac{7d}{2v}\).")),
       ("Ratio", p("5 : 7."))) + final(r"\(5 : 7\), option 2"),
 why_rows=[("1", "Not the ratio of the two totals."), ("3", "Not the ratio of the two totals."), ("4", "Upside down.")])

P.qa(2, r"John takes twice as much time as Jack to finish a job. Jack and Jim together take one-thirds of the time to finish the job than John takes working alone. Moreover, in order to finish the job, John takes three days more than that taken by three of them working together. In how many days will Jim finish the job working alone?",
 [], "TITA", "4", ["Arithmetic::Time_and_Work"], "Medium",
 r"Let Jack take \(t\) days, so John takes \(2t\).",
 steps(("Jim’s rate", p(r"Jack and Jim take \(\tfrac{2t}{3}\), so together they do \(\tfrac{3}{2t}\) a day. Jim alone: \(\tfrac{3}{2t} - \tfrac1t = \tfrac{1}{2t}\).")),
       ("All three", p(r"\(\tfrac{1}{2t} + \tfrac1t + \tfrac{1}{2t} = \tfrac2t\), so they take \(\tfrac t2\) days.")),
       ("Solve", p(r"\(2t = \tfrac t2 + 3\) gives \(t = 2\). Jim takes \(2t = 4\) days."))) + final(r"\(4\)"),
 concept=p("Work with daily rates; times don’t add, rates do."))

P.qa(3, r"Let \(f(x) = x^2 + ax + b\) and \(g(x) = f(x + 1) - f(x - 1)\). If \(f(x) \ge 0\) for all real \(x\), and \(g(20) = 72\), then the smallest possible value of \(b\) is",
 M("1", "4", "0", "16"), "MCQ", "2", ["Algebra::Quadratic_Equations"], "Easy",
 r"Expand \(g(x)\); most of it cancels.",
 steps(("Find a", p(r"\(g(x) = 4x + 2a\), so \(80 + 2a = 72\) and \(a = -4\).")),
       ("Never negative", p(r"\(x^2 - 4x + b \ge 0\) for all \(x\) needs discriminant \(\le 0\): \(16 - 4b \le 0\), so \(b \ge 4\)."))) + final(r"\(4\), option 2"),
 concept=r"\[x^2 + ax + b \ge 0 \text{ for all } x \iff a^2 \le 4b\]",
 why_rows=[("1", "Makes the quadratic dip below zero."), ("3", "Makes the quadratic dip below zero."), ("4", "Works, but isn’t the smallest.")])

P.qa(4, r"For the same principal amount, the compound interest for two years at \(5\%\) per annum exceeds the simple interest for three years at \(3\%\) per annum by Rs \(1125\). Then the principal amount in rupees is",
 [], "TITA", "90000", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Write both interests as a fraction of the principal.",
 steps(("Interests", p(r"Compound: \(1.05^2 - 1 = 0.1025\) of P. Simple: \(3 \times 3\% = 0.09\) of P.")),
       ("Difference", p(r"\(0.0125P = 1125\), so \(P = 90000\)."))) + final(r"\(90000\)"))

P.qa(5, r"Let C be a circle of radius \(5\) metres having center at O. Let PQ be a chord of C that passes through points A and B where A is located \(4\) metres north of O and B is located \(3\) metres east of O. Then, the length of PQ, in metres, is nearest to",
 M("7.2", "6.6", "8.8", "7.8"), "MCQ", "3", ["Geometry::Circles"], "Medium",
 "Find the distance from O to the line AB.",
 steps(("Distance", p(r"OAB is a right triangle with legs 4 and 3, so AB = 5 and the height from O is \(\tfrac{3 \times 4}{5} = 2.4\).")),
       ("Chord", p(r"\(PQ = 2\sqrt{25 - 5.76}\) \(= 2\sqrt{19.24}\) \(\approx 8.77\)."))) + final(r"\(8.8\), option 3"),
 concept=r"\[\text{chord} = 2\sqrt{r^2 - d^2}\]",
 why_rows=[("1", "Too short."), ("2", "Too short."), ("4", "Too short.")])

P.qa(6, r"In a car race, car A beats car B by \(45\) km, car B beats car C by \(50\) km, and car A beats car C by \(90\) km. The distance (in km) over which the race has been conducted is",
 M("475", "550", "450", "500"), "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 r"Compare the speed ratio of C to B in two ways.",
 steps(("Two ratios", p(r"When A finishes \(D\): B has run \(D - 45\), C has run \(D - 90\). When B finishes \(D\), C has run \(D - 50\). So \(\tfrac{D - 90}{D - 45} = \tfrac{D - 50}{D}\).")),
       ("Solve", p(r"\(D^2 - 90D = D^2 - 95D + 2250\), so \(D = 450\)."))) + final(r"\(450\), option 3"),
 why_rows=[("1", "The ratios don’t match."), ("2", "The ratios don’t match."), ("4", "The ratios don’t match.")])

P.qa(7, r"How many \(4\)-digit numbers, each greater than \(1000\) and each having all four digits distinct, are there with \(7\) coming before \(3\)?",
 [], "TITA", "315", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "Place 7 and 3 first, then fill the other two places. Watch out for 0 in front.",
 steps(("7 in front", p(r"3 goes in one of the other 3 places; the remaining two take any of the other 8 digits: \(3 \times 8 \times 7 = 168\).")),
       ("7 not in front", p(r"7 and 3 take two of the last three places, 7 first: 3 ways. The front digit can’t be 0: 7 choices, then 7 for the last place: \(3 \times 7 \times 7 = 147\).")),
       ("Total", p("168 + 147 = 315."))) + final(r"\(315\)"),
 concept=p("When 0 is among the digits, fix the first place separately."))

P.qa(8, r"The sum of the perimeters of an equilateral triangle and a rectangle is \(90\) cm. The area, \(T\), of the triangle and the area, \(R\), of the rectangle, both in sq cm, satisfy the relationship \(R = T^2\). If the sides of the rectangle are in the ratio \(1 : 3\), then the length, in cm, of the longer side of the rectangle, is",
 M("18", "27", "21", "24"), "MCQ", "2", ["Geometry::Mensuration"], "Medium",
 r"Use triangle side \(a\) and rectangle sides \(x\), \(3x\).",
 steps(("Areas", p(r"\(3x^2 = \tfrac{3}{16}a^4\), so \(x = \tfrac{a^2}{4}\).")),
       ("Perimeters", p(r"\(3a + 8x = 90\) becomes \(2a^2 + 3a - 90 = 0\), so \(a = 6\) and \(x = 9\).")),
       ("Longer side", p(r"\(3x = 27\)."))) + final(r"\(27\), option 2"),
 why_rows=[("1", "Twice the shorter side."), ("3", "Doesn’t fit the perimeter."), ("4", "Doesn’t fit the perimeter.")])

P.qa(9, r"A sum of money is split among Amal, Sunil and Mita so that the ratio of the shares of Amal and Sunil is \(3 : 2\), while the ratio of the shares of Sunil and Mita is \(4 : 5\). If the difference between the largest and the smallest of these three shares is Rs \(400\), then Sunil’s share, in rupees, is",
 [], "TITA", "800", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Make Sunil’s part the same in both ratios.",
 steps(("Combined ratio", p("Amal : Sunil : Mita = 6 : 4 : 5.")),
       ("Scale", p("Largest − smallest = 6 − 4 = 2 parts = 400, so a part is 200 and Sunil gets 800."))) + final(r"\(800\)"))

P.qa(10, r"The value of \(\log_a\left(\tfrac ab\right) + \log_b\left(\tfrac ba\right)\), for \(1 < a \le b\) cannot be equal to",
 M("1", "-0.5", "-1", "0"), "MCQ", "1", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"Write it in terms of \(t = \log_a b\).",
 steps(("Rewrite", p(r"\(1 - \log_a b + 1 - \log_b a\) \(= 2 - \left(t + \tfrac1t\right)\).")),
       ("Range", p(r"\(t \ge 1\), so \(t + \tfrac1t \ge 2\) and the value is at most 0. It can never be 1."))) + final(r"\(1\), option 1"),
 concept=r"\[\log_a b \cdot \log_b a = 1\]",
 why_rows=[("2", "Reached when t + 1/t = 2.5."), ("3", "Reached when t + 1/t = 3."), ("4", "Reached when a = b.")])

P.qa(11, r"Students in a college have to choose at least two subjects from chemistry, mathematics and physics. The number of students choosing all three subjects is \(18\), choosing mathematics as one of their subjects is \(23\) and choosing physics as one of their subjects is \(25\). The smallest possible number of students who could choose chemistry as one of their subjects is",
 M("20", "19", "22", "21"), "MCQ", "1", ["Modern_Maths::Set_Theory"], "Medium",
 "Everyone takes two or three subjects; nobody takes just one.",
 steps(("Pairs", p("Maths with exactly one other: 23 − 18 = 5. Physics with exactly one other: 25 − 18 = 7. If x take only maths and physics, then 5 − x take maths and chemistry, and 7 − x take physics and chemistry.")),
       ("Chemistry", p(r"\(18 + (5 - x) + (7 - x) = 30 - 2x\), smallest at \(x = 5\): 20."))) + final(r"\(20\), option 1"),
 why_rows=[("2", "Would need x above 5."), ("3", "Not the smallest."), ("4", "Not reachable with whole numbers.")])

P.qa(12, r"In a group of \(10\) students, the mean of the lowest \(9\) scores is \(42\) while the mean of the highest \(9\) scores is \(47\). For the entire group of \(10\) students, the maximum possible mean exceeds the minimum possible mean by",
 M("3", "6", "5", "4"), "MCQ", "4", ["Arithmetic::Average"], "Hard",
 r"Let the total be \(T\). Then the top score is \(T - 378\) and the bottom one \(T - 423\).",
 steps(("The middle eight", p(r"They add up to \(801 - T\), and each sits between the bottom and top scores.")),
       ("Bounds", p(r"\(\tfrac{801 - T}{8} \le T - 378\) gives \(T \ge 425\). \(\tfrac{801 - T}{8} \ge T - 423\) gives \(T \le 465\).")),
       ("Means", p("Between 42.5 and 46.5: a difference of 4."))) + final(r"\(4\), option 4"),
 why_rows=[("1", "Too small."), ("2", "Too large."), ("3", "The gap between 42 and 47, not the means.")])

P.qa(13, r"A and B are two points on a straight line. Ram runs from A to B while Rahim runs from B to A. After crossing each other, Ram and Rahim reach their destinations in one minute and four minutes, respectively. If they start at the same time, then the ratio of Ram’s speed to Rahim’s speed is",
 M("1 : 2", r"\sqrt2 : 1", "2 : 1", r"2\sqrt2 : 1"), "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "There is a standard result for times after meeting.",
 steps(("The rule", p(r"Speed ratio \(= \sqrt{\tfrac{t_2}{t_1}}\), where \(t_1\), \(t_2\) are the times after meeting.")),
       ("Here", p(r"\(\sqrt{\tfrac41} = 2\)."))) + final(r"\(2 : 1\), option 3"),
 concept=r"\[\frac{v_1}{v_2} = \sqrt{\frac{t_2}{t_1}}\]",
 why_rows=[("1", "Upside down."), ("2", "Missing the square root step."), ("4", "Not the formula.")])

P.qa(14, r"Two circular tracks T1 and T2 of radii \(100\) m and \(20\) m, respectively touch at a point A. Starting from A at the same time, Ram and Rahim are walking on track T1 and track T2 at speeds \(15\) km/hr and \(5\) km/hr respectively. The number of full rounds that Ram will make before he meets Rahim again for the first time is",
 M("4", "2", "5", "3"), "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "The tracks only share A, so they meet when both are back at A.",
 steps(("Round times", p(r"Ram: \(\tfrac{200\pi}{15}\), Rahim: \(\tfrac{40\pi}{5} = 8\pi\), in the same units.")),
       ("First common time", p(r"\(\tfrac{40\pi}{3}\) and \(8\pi\) first meet at \(40\pi\): 3 rounds for Ram, 5 for Rahim."))) + final(r"\(3\), option 4"),
 why_rows=[("1", "They meet earlier."), ("2", "Rahim isn’t at A then."), ("3", "That is Rahim’s count.")])

P.qa(15, r"Let C1 and C2 be concentric circles such that the diameter of C1 is \(2\) cm longer than that of C2. If a chord of C1 has length \(6\) cm and is a tangent to C2, then the diameter, in cm, of C1 is",
 [], "TITA", "10", ["Geometry::Circles"], "Easy",
 "The radius of C2 meets the chord at its middle.",
 steps(("Right triangle", p(r"With C1 radius \(R\), C2 has radius \(R - 1\). Then \(R^2 = (R - 1)^2 + 3^2\).")),
       ("Solve", p(r"\(2R - 1 = 9\), so \(R = 5\) and the diameter is 10."))) + final(r"\(10\)"))

P.qa(16, r"Anil buys \(12\) toys and labels each with the same selling price. He sells \(8\) toys initially at \(20\%\) discount on the labelled price. Then he sells the remaining \(4\) toys at an additional \(25\%\) discount on the discounted price. Thus, he gets a total of Rs \(2112\), and makes a \(10\%\) profit. With no discounts, his percentage of profit would have been",
 M("55", "60", "54", "50"), "MCQ", "4", ["Arithmetic::Profit_Loss_and_Discount"], "Easy",
 r"Call the label price \(L\).",
 steps(("Label", p(r"\(8(0.8L) + 4(0.6L) = 8.8L = 2112\), so \(L = 240\).")),
       ("Cost", p(r"\(\tfrac{2112}{1.1} = 1920\).")),
       ("No discount", p(r"\(12 \times 240 = 2880\), a profit of \(\tfrac{960}{1920} = 50\%\)."))) + final(r"\(50\), option 4"),
 why_rows=[("1", "Too high."), ("2", "Too high."), ("3", "Too high.")])

P.qa(17, r"The number of integers that satisfy the equality \((x^2 - 5x + 7)^{x + 1} = 1\) is",
 M("2", "3", "4", "5"), "MCQ", "2", ["Algebra::Logarithms_and_Exponents", "Algebra::Quadratic_Equations"], "Medium",
 "A power equals 1 in three ways.",
 steps(("Exponent 0", p(r"\(x = -1\); the base is 13, not 0. Works.")),
       ("Base 1", p(r"\(x^2 - 5x + 6 = 0\): \(x = 2, 3\).")),
       ("Base −1", p(r"\(x^2 - 5x + 8 = 0\) has no real roots."))) + final(r"\(3\), option 2"),
 concept=r"\[a^b = 1 \iff b = 0 \;(a \ne 0),\; a = 1,\; \text{or } a = -1 \text{ with } b \text{ even}\]",
 why_rows=[("1", "Misses one case."), ("3", "Counts a base −1 solution that doesn’t exist."), ("4", "Too many.")])

P.qa(18, r"The number of pairs of integers \((x, y)\) satisfying \(x \ge y \ge -20\) and \(2x + 5y = 99\) is",
 [], "TITA", "17", ["Algebra::Linear_Equations"], "Medium",
 r"\(y\) must be odd. Then use \(x \ge y\).",
 steps(("Odd y", p(r"\(2x = 99 - 5y\) needs \(y\) odd.")),
       ("x ≥ y", p(r"\(99 - 5y \ge 2y\) gives \(y \le 14\).")),
       ("Count", p(r"Odd \(y\) from −19 to 13: 17 values."))) + final(r"\(17\)"),
 concept=p("Linear equations in integers: find the step between solutions, then count within the bounds."))

P.qa(19, r"From an interior point of an equilateral triangle, perpendiculars are drawn on all three sides. The sum of the lengths of the three perpendiculars is \(s\). Then the area of the triangle is",
 M(r"\tfrac{s^2}{2\sqrt3}", r"\tfrac{2s^2}{\sqrt3}", r"\tfrac{\sqrt3 s^2}{2}", r"\tfrac{s^2}{\sqrt3}"), "MCQ", "4", ["Geometry::Triangles"], "Easy",
 "Split the triangle into three from the interior point.",
 steps(("Height", p(r"The three small areas add to \(\tfrac12 a s\), which equals \(\tfrac12 a h\). So \(s = h = \tfrac{\sqrt3}{2}a\).")),
       ("Area", p(r"\(a = \tfrac{2s}{\sqrt3}\), and the area is \(\tfrac{\sqrt3}{4}a^2 = \tfrac{s^2}{\sqrt3}\)."))) + final(r"\(\tfrac{s^2}{\sqrt3}\), option 4"),
 concept=p("In an equilateral triangle, the perpendiculars from any interior point always add up to the height."),
 why_rows=[("1", "Half the right value."), ("2", "Twice the right value."), ("3", "Treats s as the side.")])

P.qa(20, r"Let the \(m\)th and \(n\)th terms of a geometric progression be \(\tfrac34\) and \(12\), respectively, where \(m < n\). If the common ratio of the progression is an integer \(r\), then the smallest possible value of \(r + n - m\) is",
 M("6", "-4", "-2", "2"), "MCQ", "3", ["Algebra::Progressions_and_Series"], "Medium",
 r"\(r^{n - m} = 16\). Don’t forget negative \(r\).",
 steps(("Options", p(r"\(r = 2, n - m = 4\): 6. \(r = 4, n - m = 2\): 6. \(r = 16, n - m = 1\): 17. \(r = -2, n - m = 4\): 2. \(r = -4, n - m = 2\): −2.")),
       ("Smallest", p("−2."))) + final(r"\(-2\), option 3"),
 trap("Negative ratios work when the power is even."),
 why_rows=[("1", "Positive r only."), ("2", "r = −16 would need an odd power, giving −16."), ("4", "r = −2 isn’t the smallest.")])

P.qa(21, r"In May, John bought the same amount of rice and the same amount of wheat as he had bought in April, but spent Rs \(150\) more due to price increase of rice and wheat by \(20\%\) and \(12\%\), respectively. If John had spent Rs \(450\) on rice in April, then how much did he spend on wheat in May?",
 ["Rs 560", "Rs 570", "Rs 590", "Rs 580"], "MCQ", "1", ["Arithmetic::Percentages"], "Easy",
 "Rice accounts for part of the 150.",
 steps(("Rice", p("20% of 450 = 90 extra.")),
       ("Wheat", p(r"The other 60 is 12% of April’s wheat spend, so 500. In May, \(500 \times 1.12 = 560\)."))) + final("Rs 560, option 1"),
 why_rows=[("2", "Doesn’t leave 60 for wheat."), ("3", "Doesn’t leave 60 for wheat."), ("4", "Doesn’t leave 60 for wheat.")])

P.qa(22, r"If \(x\) and \(y\) are non-negative integers such that \(x + 9 = z\), \(y + 1 = z\) and \(x + y < z + 5\), then the maximum possible value of \(2x + y\) equals",
 [], "TITA", "23", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 r"Put everything in terms of \(z\).",
 steps(("In terms of z", p(r"\(x = z - 9\), \(y = z - 1\), so \(2z - 10 < z + 5\) and \(z \le 14\).")),
       ("Maximum", p(r"\(z = 14\): \(x = 5\), \(y = 13\), \(2x + y = 23\)."))) + final(r"\(23\)"))

P.qa(23, r"Aron bought some pencils and sharpeners. Spending the same amount of money as Aron, Aditya bought twice as many pencils and \(10\) less sharpeners. If the cost of one sharpener is Rs \(2\) more than the cost of a pencil, then the minimum possible number of pencils bought by Aron and Aditya together is",
 M("30", "27", "33", "36"), "MCQ", "3", ["Algebra::Linear_Equations"], "Medium",
 r"The extra pencils cost what the 10 sharpeners did.",
 steps(("Equation", p(r"With \(p\) pencils at \(x\) each: \(px = 10(x + 2)\), so \(p = 10 + \tfrac{20}{x}\).")),
       ("Smallest p", p(r"\(p\) is a whole number above 10, so at least 11 (when \(x = 20\)). Together: \(p + 2p = 33\)."))) + final(r"\(33\), option 3"),
 why_rows=[("1", "Needs p = 10, which can’t happen."), ("2", "Needs p = 9."), ("4", "Possible, but not the minimum.")])

P.qa(24, r"For real \(x\), the maximum possible value of \(\dfrac{x}{\sqrt{1 + x^4}}\) is",
 M(r"\tfrac{1}{\sqrt3}", r"\tfrac{1}{\sqrt2}", r"\tfrac12", "1"), "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Square it and use AM–GM.",
 steps(("Square", p(r"\(\dfrac{x^2}{1 + x^4} = \dfrac{1}{\tfrac{1}{x^2} + x^2} \le \dfrac12\), with equality at \(x = 1\).")),
       ("Back", p(r"The maximum is \(\sqrt{\tfrac12} = \tfrac{1}{\sqrt2}\)."))) + trap("The ½ is the square; take its root.") + final(r"\(\tfrac{1}{\sqrt2}\), option 2"),
 concept=r"\[t + \frac1t \ge 2 \quad (t > 0)\]",
 why_rows=[("1", "Too small."), ("3", "The square of the answer."), ("4", "Never reached.")])

P.qa(25, r"In how many ways can a pair of integers \((x, a)\) be chosen such that \(x^2 - 2|x| + |a - 2| = 0\)?",
 M("7", "6", "5", "4"), "MCQ", "1", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 r"\(|a - 2| = 2|x| - x^2\) must be at least 0.",
 steps(("Possible x", p(r"\(2|x| - x^2 \ge 0\) means \(|x| \le 2\).")),
       ("Count", p(r"\(x = 0\): \(a = 2\). \(x = \pm1\): \(|a - 2| = 1\), two values of \(a\) each. \(x = \pm2\): \(a = 2\). Total 1 + 4 + 2 = 7."))) + final(r"\(7\), option 1"),
 why_rows=[("2", "Misses one."), ("3", "Misses the negative x values."), ("4", "Misses several.")])

P.qa(26, r"If \(x\) and \(y\) are positive real numbers satisfying \(x + y = 102\), then the minimum possible value of \(2601\left(1 + \tfrac1x\right)\left(1 + \tfrac1y\right)\) is",
 [], "TITA", "2704", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Expand the brackets.",
 steps(("Expand", p(r"\(\left(1 + \tfrac1x\right)\left(1 + \tfrac1y\right)\) \(= 1 + \tfrac{x + y + 1}{xy}\) \(= 1 + \tfrac{103}{xy}\).")),
       ("Minimise", p(r"Largest \(xy\) is \(51^2 = 2601\), so the value is \(2601 + 103 = 2704\)."))) + final(r"\(2704\)"),
 concept=p("For a fixed sum, the product is largest when the numbers are equal."))
