# -*- coding: utf-8 -*-
# Batch 10 — CAT 2021 Slot 3: QA Q1–22 (exam order).
from fmt import steps, final, trap, why, table, p
from b10_21s3 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"A shop owner bought a total of \(64\) shirts from a wholesale market that came in two sizes, small and large. The price of a small shirt was ₹\(50\) less than that of a large shirt. She paid a total of ₹\(5000\) for the large shirts, and a total of ₹\(1800\) for the small shirts. Then, the price of a large shirt and a small shirt together, in ₹, is",
 M("150", "225", "175", "200"), "MCQ", "4", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 r"With large price \(L\): \(\tfrac{5000}{L} + \tfrac{1800}{L - 50} = 64\). Try the options.",
 steps(("Trying values", p(r"If the pair costs 200, then \(L = 125\) and the small one 75: \(\tfrac{5000}{125} + \tfrac{1800}{75}\) \(= 40 + 24\) \(= 64\). It fits."))) + final(r"\(200\), option 4"),
 shortcut="Each option fixes both prices (sum S, difference 50), so checking the options is quickest.",
 concept=r"\[\text{number bought} = \frac{\text{amount spent}}{\text{price}}\]",
 why_rows=[("1", "Prices 100 and 50 give 50 + 36 = 86 shirts."), ("2", "Prices 137.5 and 87.5 don’t give 64."), ("3", "Prices 112.5 and 62.5 don’t give 64.")])

P.qa(2, r"One day, Rahul started a work at \(9\) AM and Gautam joined him two hours later. They then worked together and completed the work at \(5\) PM the same day. If both had started at \(9\) AM and worked together, the work would have been completed \(30\) minutes earlier. Working alone, the time Rahul would have taken, in hours, to complete the work is",
 M("10", "12", "11.5", "12.5"), "MCQ", "1", ["Arithmetic::Time_and_Work"], "Easy",
 "Rahul works 8 hours and Gautam 6 in the first case; both work 7.5 hours in the second.",
 steps(("Equation", p(r"\(8R + 6G = 7.5R + 7.5G\), so \(0.5R = 1.5G\) and \(R = 3G\).")),
       ("Rahul alone", p(r"The work is \(7.5(R + G) = 7.5 \times \tfrac43 R = 10R\): 10 hours."))) + final(r"\(10\), option 1"),
 concept=r"\[\text{work} = \text{rate} \times \text{time, summed over people}\]",
 why_rows=[("2", "Not 10R."), ("3", "Not 10R."), ("4", "Not 10R.")])

P.qa(3, r"In a tournament, a team has played \(40\) matches so far and won \(30\%\) of them. If they win \(60\%\) of the remaining matches, their overall win percentage will be \(50\%\). Suppose they win \(90\%\) of the remaining matches, then the total number of matches won by the team in the tournament will be",
 M("86", "84", "80", "78"), "MCQ", "2", ["Arithmetic::Percentages"], "Easy",
 "First find how many matches remain.",
 steps(("Remaining matches", p(r"\(12 + 0.6n = 0.5(40 + n)\), so \(n = 80\).")),
       ("Winning 90%", p(r"\(12 + 72 = 84\)."))) + final(r"\(84\), option 2"),
 concept=r"\[\text{overall \%} = \frac{\text{total won}}{\text{total played}}\]",
 why_rows=[("1", "Off by two."), ("3", "Off by four."), ("4", "Off by six.")])

P.qa(4, r"The number of distinct pairs of integers \((m, n)\) satisfying \(|1 + mn| < |m + n| < 5\) is",
 [], "TITA", "12", ["Algebra::Inequalities_and_Absolute_Value"], "Hard",
 "Square the left inequality and factorise.",
 steps(("Left part", p(r"\((1 + mn)^2 < (m + n)^2\) simplifies to \((m^2 - 1)(n^2 - 1) < 0\). For integers, one of them must be 0 and the other must have size at least 2.")),
       ("Right part", p(r"If \(m = 0\), then \(|n| < 5\), so \(n = \pm2, \pm3, \pm4\): 6 pairs. Likewise 6 with \(n = 0\).")),
       ("Total", p("12 pairs."))) + final(r"\(12\)"),
 concept=r"\[|a| < |b| \iff a^2 < b^2\]")

P.qa(5, r"For a real number \(a\), if \(\dfrac{\log_{15}a + \log_{32}a}{(\log_{15}a)(\log_{32}a)} = 4\), then \(a\) must lie in the range",
 M("a > 5", "3 < a < 4", "2 < a < 3", "4 < a < 5"), "MCQ", "4", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Split the fraction into two reciprocals.",
 steps(("Simplifying", p(r"The left side is \(\tfrac{1}{\log_{32}a} + \tfrac{1}{\log_{15}a}\) \(= \log_a 32 + \log_a 15\) \(= \log_a 480\).")),
       ("Solving", p(r"\(a^4 = 480\). Since \(4^4 = 256\) and \(5^4 = 625\), \(4 < a < 5\)."))) + final(r"\(4 < a < 5\), option 4"),
 concept=r"\[\frac{1}{\log_b a} = \log_a b\]",
 why_rows=[("1", r"\(5^4 = 625 > 480\)."), ("2", r"\(4^4 = 256 < 480\)."), ("3", "Far too small.")])

P.qa(6, r"The total of male and female populations in a city increased by \(25\%\) from \(1970\) to \(1980\). During the same period, the male population increased by \(40\%\) while the female population increased by \(20\%\). From \(1980\) to \(1990\), the female population increased by \(25\%\). In \(1990\), if the female population is twice the male population, then the percentage increase in the total of male and female populations in the city from \(1970\) to \(1990\) is",
 M("68.75", "68.25", "69.25", "68.50"), "MCQ", "1", ["Arithmetic::Percentages"], "Medium",
 "Use the 1970–80 changes to find the male : female ratio.",
 steps(("1970", p(r"\(1.4m + 1.2f = 1.25(m + f)\) gives \(f = 3m\). Take 1 male and 3 females: total 4.")),
       ("1990", p("Females: 3 × 1.2 × 1.25 = 4.5. Males: half that, 2.25. Total 6.75.")),
       ("Increase", p(r"\(\tfrac{6.75 - 4}{4} = 68.75\%\)."))) + final(r"\(68.75\), option 1"),
 concept=p("Pick numbers in the right ratio and follow them through."),
 why_rows=[("2", "Not 2.75/4."), ("3", "Not 2.75/4."), ("4", "Not 2.75/4.")])

P.qa(7, r"Consider a sequence of real numbers \(x_1, x_2, x_3, \ldots\) such that \(x_{n+1} = x_n + n - 1\) for all \(n \ge 1\). If \(x_1 = -1\), then \(x_{100}\) is equal to",
 M("4949", "4850", "4849", "4950"), "MCQ", "2", ["Algebra::Progressions_and_Series"], "Easy",
 "Add up the increases from 1 to 100.",
 steps(("Adding", p(r"\(x_{100}\) \(= x_1 + \sum_{n=1}^{99}(n - 1)\) \(= -1 + (0 + 1 + \dots + 98)\).")),
       ("Value", p(r"\(-1 + \tfrac{98 \times 99}{2}\) \(= -1 + 4851\) \(= 4850\)."))) + final(r"\(4850\), option 2"),
 concept=r"\[x_N = x_1 + \sum_{n=1}^{N-1}(x_{n+1} - x_n)\]",
 why_rows=[("1", "Sums to 99 instead of 98."), ("3", "Off by one."), ("4", "Sums 0 to 99 without the −1.")])

P.qa(8, r"The arithmetic mean of scores of \(25\) students in an examination is \(50\). Five of these students top the examination with the same score. If the scores of the other students are distinct integers with the lowest being \(30\), then the maximum possible score of the toppers is",
 [], "TITA", "92", ["Arithmetic::Average"], "Medium",
 "To make the toppers’ score high, make the other 20 as low as possible.",
 steps(("The others", p(r"20 distinct integers starting at 30: 30 to 49, adding to 790.")),
       ("Toppers", p(r"Total 1250, so the five toppers share 460: 92 each."))) + final(r"\(92\)"),
 concept=p("To maximise one group, minimise everything else under the constraints."))

P.qa(9, r"One part of a hostel’s monthly expenses is fixed, and the other part is proportional to the number of its boarders. The hostel collects ₹\(1600\) per month from each boarder. When the number of boarders is \(50\), the profit of the hostel is ₹\(200\) per boarder, and when the number of boarders is \(75\), the profit of the hostel is ₹\(250\) per boarder. When the number of boarders is \(80\), the total profit of the hostel, in ₹, will be",
 M("20200", "20500", "20000", "20800"), "MCQ", "2", ["Arithmetic::Profit_Loss_and_Discount"], "Medium",
 r"Expenses are \(F + vn\). Write the two cases.",
 steps(("Two cases", p(r"50 boarders: \(80000 - F - 50v = 10000\). 75 boarders: \(120000 - F - 75v = 18750\).")),
       ("Solving", p(r"\(25v = 31250\): \(v = 1250\), \(F = 7500\).")),
       ("80 boarders", p(r"\(128000 - 7500 - 100000 = 20500\)."))) + final(r"\(20500\), option 2"),
 concept=r"\[\text{profit} = \text{revenue} - (\text{fixed} + \text{variable} \times n)\]",
 why_rows=[("1", "Off by 300."), ("3", "Off by 500."), ("4", "Off by 300.")])

P.qa(10, r"The cost of fencing a rectangular plot is ₹\(200\) per ft along one side, and ₹\(100\) per ft along the three other sides. If the area of the rectangular plot is \(60000\) sq. ft, then the lowest possible cost of fencing all four sides, in ₹, is",
 M("120000", "100000", "160000", "90000"), "MCQ", "1", ["Algebra::Inequalities_and_Absolute_Value", "Geometry::Mensuration"], "Medium",
 r"If the expensive side has length \(l\), the cost is \(300l + 200b\).",
 steps(("The cost", p(r"\(200l + 100l + 100b + 100b\) \(= 300l + 200b\), with \(lb = 60000\).")),
       ("Minimum", p(r"By AM ≥ GM, \(300l + 200b\) \(\ge 2\sqrt{300 \times 200 \times 60000}\) \(= 120000\), reached when \(300l = 200b\) (that is, \(l = 200\) and \(b = 300\))."))) + final(r"\(120000\), option 1"),
 concept=p(r"\(x + y \ge 2\sqrt{xy}\), with equality when \(x = y\)."),
 why_rows=[("2", "Below the minimum."), ("3", "Possible but not the lowest."), ("4", "Below the minimum.")])

P.qa(11, r"A park is shaped like a rhombus and has area \(96\) sq m. If \(40\) m of fencing is needed to enclose the park, the cost, in ₹, of laying electric wires along its two diagonals, at the rate of ₹\(125\) per m, is",
 [], "TITA", "3500", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "Side 10; find the sum of the diagonals.",
 steps(("Diagonals", p(r"\(pq = 192\) and \(p^2 + q^2 = 4 \times 100 = 400\), so \((p + q)^2 = 784\) and \(p + q = 28\).")),
       ("Cost", p(r"\(28 \times 125 = 3500\)."))) + final(r"\(3500\)"),
 concept=r"\[\text{rhombus: area} = \tfrac12 pq, \qquad p^2 + q^2 = 4a^2\]")

P.qa(12, r"A tea shop offers tea in cups of three different sizes. The product of the prices, in ₹, of three different sizes is equal to \(800\). The prices of the smallest size and the medium size are in the ratio \(2 : 5\). If the shop owner decides to increase the prices of the smallest and the medium ones by ₹\(6\) keeping the price of the largest size unchanged, the product then changes to \(3200\). The sum of the original prices of three different sizes, in ₹, is",
 [], "TITA", "34", ["Algebra::Quadratic_Equations"], "Medium",
 r"Prices \(2k, 5k, L\). Divide the two products to remove \(L\).",
 steps(("Dividing", p(r"\(\dfrac{(2k + 6)(5k + 6)}{10k^2} = 4\), so \(30k^2 - 42k - 36 = 0\), that is \(5k^2 - 7k - 6 = 0\): \(k = 2\).")),
       ("Prices", p(r"4 and 10, and \(L = \tfrac{800}{40} = 20\). Sum 34."))) + final(r"\(34\)"),
 concept=p("Dividing two equations that share a factor removes it."))

P.qa(13, r"Mira and Amal walk along a circular track, starting from the same point at the same time. If they walk in the same direction, then in \(45\) minutes, Amal completes exactly \(3\) more rounds than Mira. If they walk in opposite directions, then they meet for the first time exactly after \(3\) minutes. The number of rounds Mira walks in one hour is",
 [], "TITA", "8", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Work in rounds per minute.",
 steps(("Two equations", p(r"\(a - m = \tfrac{3}{45} = \tfrac1{15}\) and \(a + m = \tfrac13\).")),
       ("Mira", p(r"\(m\) \(= \tfrac12\left(\tfrac13 - \tfrac1{15}\right)\) \(= \tfrac{2}{15}\) rounds a minute: 8 in an hour."))) + final(r"\(8\)"),
 concept=r"\[\text{opposite directions: first meeting after } \frac{1}{a + m} \text{ rounds of time}\]")

P.qa(14, r"If a certain weight of an alloy of silver and copper is mixed with \(3\) kg of pure silver, the resulting alloy will have \(90\%\) silver by weight. If the same weight of the initial alloy is mixed with \(2\) kg of another alloy which has \(90\%\) silver by weight, the resulting alloy will have \(84\%\) silver by weight. Then, the weight of the initial alloy, in kg, is",
 M("3", "2.5", "3.5", "4"), "MCQ", "1", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 r"Let the alloy weigh \(W\) with \(S\) kg of silver.",
 steps(("Equations", p(r"\(S + 3 = 0.9(W + 3)\) and \(S + 1.8 = 0.84(W + 2)\).")),
       ("Solving", p(r"\(S = 0.9W - 0.3 = 0.84W - 0.12\), so \(0.06W = 0.18\) and \(W = 3\)."))) + final(r"\(3\), option 1"),
 concept=r"\[\text{silver after mixing} = \text{sum of silver in each part}\]",
 why_rows=[("2", "Doesn’t satisfy both."), ("3", "Doesn’t satisfy both."), ("4", "Doesn’t satisfy both.")])

P.qa(15, r"In a triangle \(ABC\), \(\angle BCA = 50^\circ\). \(D\) and \(E\) are points on \(AB\) and \(AC\), respectively, such that \(AD = DE\). If \(F\) is a point on \(BC\) such that \(BD = DF\), then \(\angle FDE\), in degrees, is equal to",
 M("96", "100", "80", "72"), "MCQ", "3", ["Geometry::Triangles"], "Medium",
 "Both small triangles are isosceles. The three angles at D add up to 180°.",
 steps(("Angles at D", p(r"\(\angle ADE = 180^\circ - 2A\) and \(\angle BDF = 180^\circ - 2B\).")),
       ("FDE", p(r"\(\angle FDE\) \(= 180^\circ - (180^\circ - 2A) - (180^\circ - 2B)\) \(= 2(A + B) - 180^\circ\) \(= 2 \times 130^\circ - 180^\circ\) \(= 80^\circ\)."))) + final(r"\(80\), option 3"),
 concept=r"\[\text{angles on a straight line add to } 180^\circ\]",
 why_rows=[("1", "Not 2(A + B) − 180."), ("2", "Not 2(A + B) − 180."), ("4", "Not 2(A + B) − 180.")])

P.qa(16, r"Bank A offers \(6\%\) interest rate per annum compounded half yearly. Bank B and Bank C offer simple interest but the annual interest rate offered by Bank C is twice that of Bank B. Raju invests a certain amount in Bank B for a certain period and Rupa invests ₹\(10,000\) in Bank C for twice that period. The interest that would accrue to Raju during that period is equal to the interest that would have accrued had he invested the same amount in Bank A for one year. The interest accrued, in ₹, to Rupa is",
 M("1436", "2346", "2436", "3436"), "MCQ", "3", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "Bank A gives 1.03² − 1 = 6.09% in a year.",
 steps(("Raju", p(r"Rate × time in Bank B = 6.09%.")),
       ("Rupa", p(r"Double the rate and double the time: \(4 \times 6.09\% = 24.36\%\) of ₹10,000 = ₹2,436."))) + final(r"\(2436\), option 3"),
 concept=r"\[\text{half-yearly compounding: } \left(1 + \tfrac{r}{2}\right)^2 - 1\]",
 why_rows=[("1", "Not 24.36% of 10,000."), ("2", "Digits swapped."), ("4", "Not 24.36% of 10,000.")])

P.qa(17, r"If \(f(x) = x^2 - 7x\) and \(g(x) = x + 3\), then the minimum value of \(f(g(x)) - 3x\) is",
 M("-15", "-20", "-16", "-12"), "MCQ", "3", ["Algebra::Functions"], "Easy",
 "Expand and complete the square.",
 steps(("Expanding", p(r"\((x + 3)^2 - 7(x + 3) - 3x\) \(= x^2 - 4x - 12\).")),
       ("Minimum", p(r"At \(x = 2\): \(4 - 8 - 12 = -16\)."))) + final(r"\(-16\), option 3"),
 concept=r"\[x^2 + bx + c \text{ has minimum } c - \tfrac{b^2}{4}\]",
 why_rows=[("1", "Off by one."), ("2", "Too low."), ("4", "The value at x = 0.")])

P.qa(18, r"Anil can paint a house in \(12\) days while Barun can paint it in \(16\) days. Anil, Barun and Chandu undertake to paint the house for ₹\(24000\) and the three of them together complete the painting in \(6\) days. If Chandu is paid in proportion to the work done by him, then the amount in ₹ received by him is",
 [], "TITA", "3000", ["Arithmetic::Time_and_Work"], "Easy",
 "Take the job as 48 units.",
 steps(("Rates", p("Anil 4, Barun 3, all three 8 a day, so Chandu 1 a day.")),
       ("Share", p(r"Chandu did 6 of 48 units: \(\tfrac18 \times 24000 = 3000\)."))) + final(r"\(3000\)"),
 concept=r"\[\text{pay} \propto \text{work done}\]")

P.qa(19, r"If \(n\) is a positive integer such that \(\left(\sqrt[7]{10}\right)\left(\sqrt[7]{10}\right)^2 \cdots \left(\sqrt[7]{10}\right)^n > 999\), then the smallest value of \(n\) is",
 [], "TITA", "6", ["Algebra::Logarithms_and_Exponents"], "Easy",
 "Add the exponents.",
 steps(("The product", p(r"\(10^{\frac{1 + 2 + \cdots + n}{7}}\) \(= 10^{\frac{n(n + 1)}{14}}\).")),
       ("Condition", p(r"It must reach 1000, so \(n(n + 1) \ge 42\). \(n = 6\) gives exactly 42; \(n = 5\) gives 30."))) + final(r"\(6\)"),
 concept=r"\[a^p \cdot a^q = a^{p + q}\]")

P.qa(20, r"A four-digit number is formed by using only the digits \(1, 2\) and \(3\) such that both \(2\) and \(3\) appear at least once. The number of all such four-digit numbers is",
 [], "TITA", "50", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Count all, then remove those missing a 2 or missing a 3.",
 steps(("Inclusion–exclusion", p(r"\(3^4 - 2^4 - 2^4 + 1^4\) \(= 81 - 16 - 16 + 1\) \(= 50\)."))) + final(r"\(50\)"),
 concept=r"\[|A \cup B| = |A| + |B| - |A \cap B|\]")

P.qa(21, r"Let \(ABCD\) be a parallelogram. The lengths of the side \(AD\) and the diagonal \(AC\) are \(10\) cm and \(20\) cm, respectively. If the angle \(\angle ADC\) is equal to \(30^\circ\), then the area of the parallelogram, in sq cm, is",
 M(r"25(\sqrt3 + \sqrt{15})", r"\tfrac{25(\sqrt5 + \sqrt{15})}{2}", r"\tfrac{25(\sqrt3 + \sqrt{15})}{2}", r"25(\sqrt5 + \sqrt{15})"), "MCQ", "1", ["Geometry::Polygons_and_Quadrilaterals", "Geometry::Triangles"], "Medium",
 "Use the cosine rule in triangle ADC to find DC.",
 steps(("DC", p(r"\(400 = 100 + x^2 - 2 \cdot 10x \cos 30^\circ\), so \(x^2 - 10\sqrt3\,x - 300 = 0\) and \(x = 5(\sqrt3 + \sqrt{15})\).")),
       ("Area", p(r"\(AD \cdot DC \cdot \sin 30^\circ\) \(= 10 \times 5(\sqrt3 + \sqrt{15}) \times \tfrac12\) \(= 25(\sqrt3 + \sqrt{15})\)."))) +
 final(r"\(25(\sqrt3 + \sqrt{15})\), option 1"),
 concept=r"\[c^2 = a^2 + b^2 - 2ab\cos C, \qquad \text{area} = ab\sin C\]",
 why_rows=[("2", "Wrong surds and halved."), ("3", "Half the area: that is triangle ADC."), ("4", "Wrong surds.")])

P.qa(22, r"If \(3x + 2|y| + y = 7\) and \(x + |x| + 3y = 1\), then \(x + 2y\) is",
 M(r"-\tfrac43", "1", "0", r"\tfrac83"), "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value", "Algebra::Linear_Equations"], "Medium",
 r"Try the sign cases for \(x\) and \(y\).",
 steps(("x negative?", p(r"Then \(3y = 1\), \(y = \tfrac13\), and the first equation gives \(x = 2\), which isn’t negative. So \(x \ge 0\) and \(2x + 3y = 1\).")),
       ("y", p(r"If \(y \ge 0\): \(3x + 3y = 7\), giving \(x = 6\), \(y = -\tfrac{11}{3}\), a contradiction. So \(y < 0\): \(3x - y = 7\), and with \(2x + 3y = 1\), \(x = 2\), \(y = -1\).")),
       ("Answer", p(r"\(x + 2y = 0\)."))) + final(r"\(0\), option 3"),
 concept=p("With absolute values, split into sign cases and keep only the consistent one."),
 why_rows=[("1", "From an inconsistent case."), ("2", "Not 2 − 2."), ("4", "From an inconsistent case.")])
