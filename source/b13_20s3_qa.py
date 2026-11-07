# -*- coding: utf-8 -*-
# Batch 13 — CAT 2020 Slot 3: QA (26 of 26).
from fmt import steps, final, trap, why, table, p
from b13_20s3 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"Two alcohol solutions, A and B, are mixed in the proportion \(1 : 3\) by volume. The volume of the mixture is then doubled by adding solution A such that the resulting mixture has \(72\%\) alcohol. If solution A has \(60\%\) alcohol, then the percentage of alcohol in solution B is",
 M(r"90\%", r"94\%", r"89\%", r"92\%"), "MCQ", "4", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Take 1 litre of A and 3 of B, then add 4 more of A.",
 steps(("The final mixture", p(r"5 litres of A and 3 of B, in 8 litres at 72%: \(5(0.6) + 3b = 0.72 \times 8\).")),
       ("Solve", p(r"\(3 + 3b = 5.76\), so \(b = 0.92\)."))) + final(r"\(92\%\), option 4"),
 why_rows=[("1", "Gives 71.25%."), ("2", "Gives 72.75%."), ("3", "Gives 70.875%.")])

P.qa(2, r"A batsman played \(n + 2\) innings and got out on all occasions. His average score in these \(n + 2\) innings was \(29\) runs and he scored \(38\) and \(15\) runs in the last two innings. The batsman scored less than \(38\) runs in each of the first \(n\) innings. In these \(n\) innings, his average score was \(30\) runs and lowest score was \(x\) runs. The smallest possible value of \(x\) is",
 M("1", "2", "4", "3"), "MCQ", "2", ["Arithmetic::Average"], "Medium",
 r"Find \(n\) first, then push the other scores as high as they can go.",
 steps(("Find n", p(r"\(30n + 53 = 29(n + 2)\), so \(n = 5\) and the first five innings total 150.")),
       ("Smallest x", p(r"The other four are at most 37 each: 148. So \(x \ge 2\)."))) + final(r"\(2\), option 2"),
 why_rows=[("1", "Would need another score of 38 or more."), ("3", "Possible, but not the smallest."), ("4", "Possible, but not the smallest.")])

P.qa(3, r"Let \(m\) and \(n\) be positive integers. If \(x^2 + mx + 2n = 0\) and \(x^2 + 2nx + m = 0\) have real roots, then the smallest possible value of \(m + n\) is",
 M("7", "6", "8", "5"), "MCQ", "2", ["Algebra::Quadratic_Equations"], "Medium",
 "Write both discriminant conditions and try small n.",
 steps(("Conditions", p(r"\(m^2 \ge 8n\) and \(4n^2 \ge 4m\), so \(n^2 \ge m\).")),
       ("Small n", p(r"\(n = 1\): \(m \le 1\) but \(m^2 \ge 8\), impossible. \(n = 2\): \(m \le 4\) and \(m^2 \ge 16\), so \(m = 4\) and \(m + n = 6\)."))) + final(r"\(6\), option 2"),
 concept=r"\[\text{real roots} \iff b^2 - 4ac \ge 0\]",
 why_rows=[("1", "Possible, but not the smallest."), ("3", "Possible, but not the smallest."), ("4", "No pair adds to 5.")])

P.qa(4, r"A contractor agreed to construct a \(6\) km road in \(200\) days. He employed \(140\) persons for the work. After \(60\) days, he realized that only \(1.5\) km road has been completed. How many additional people would he need to employ in order to finish the work exactly on time?",
 [], "TITA", "40", ["Arithmetic::Time_and_Work"], "Easy",
 "Work done is proportional to people × days. Find the rate from the first 60 days.",
 steps(("Rate", p(r"\(140 \times 60 = 8400\) person-days built \(1.5\) km.")),
       ("What is left", p(r"\(4.5\) km in \(140\) days needs \(8400 \times 3 = 25200\) person-days, so \(25200 \div 140 = 180\) people.")),
       ("Additional", p(r"\(180 - 140 = 40\)."))) + final(r"\(40\)"),
 concept=r"\[\frac{M_1 D_1}{W_1} = \frac{M_2 D_2}{W_2}\]")

P.qa(5, r"If \(x_1 = -1\) and \(x_m = x_{m+1} + (m + 1)\) for every positive integer \(m\), then \(x_{100}\) equals",
 M("-5151", "-5150", "-5051", "-5050"), "MCQ", "4", ["Algebra::Progressions_and_Series"], "Easy",
 r"Each step subtracts \(m + 1\).",
 steps(("Unrolling", p(r"\(x_{m+1} = x_m - (m + 1)\), so \(x_{100}\) \(= -1 - (2 + 3 + \dots + 100)\).")),
       ("Sum", p(r"\(2 + \dots + 100 = 5049\), so \(x_{100} = -5050\)."))) + final(r"\(-5050\), option 4"),
 why_rows=[("1", "Subtracts up to 101."), ("2", "Off by 100."), ("3", "Off by one term.")])

P.qa(6, r"If \(\log_a 30 = A\), \(\log_a\left(\tfrac53\right) = -B\) and \(\log_2 a = \tfrac13\), then \(\log_3 a\) equals",
 M(r"\tfrac{A + B - 3}{2}", r"\tfrac{A + B}{2} - 3", r"\tfrac{2}{A + B} - 3", r"\tfrac{2}{A + B - 3}"), "MCQ", "4", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"Add the first two: \(\log_a 30 + \log_a \tfrac35\).",
 steps(("Combine", p(r"\(A + B = \log_a 18\) \(= \log_a 2 + 2\log_a 3\).")),
       ("Use log₂ a", p(r"\(\log_a 2 = 3\), so \(\log_a 3 = \tfrac{A + B - 3}{2}\) and \(\log_3 a = \tfrac{2}{A + B - 3}\)."))) + final(r"Option 4"),
 trap(r"The question asks for \(\log_3 a\), the reciprocal of \(\log_a 3\).") ,
 concept=r"\[\log_a b = \frac{1}{\log_b a}\]",
 why_rows=[("1", r"That is \(\log_a 3\)."), ("2", "Misplaced bracket."), ("3", "Misplaced bracket.")])

P.qa(7, r"Dick is thrice as old as Tom and Harry is twice as old as Dick. If Dick’s age is \(1\) year less than the average age of all three, then Harry’s age, in years, is",
 [], "TITA", "18", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 r"Tom \(t\), Dick \(3t\), Harry \(6t\).",
 steps(("Average", p(r"\(\tfrac{10t}{3} - 1 = 3t\), so \(t = 3\).")),
       ("Harry", p(r"\(6t = 18\)."))) + final(r"\(18\)"))

P.qa(8, r"Vimla starts for office every day at \(9\) a.m. and reaches exactly on time if she drives at her usual speed of \(40\) km/hr. She is late by \(6\) minutes if she drives at \(35\) km/hr. One day, she covers two-thirds of her distance to office in one-thirds of her usual time to reach office, and then stops for \(8\) minutes. The speed, in km/hr, at which she should drive the remaining distance to reach office exactly on time is",
 M("29", "27", "26", "28"), "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Find the distance from the 6-minute delay.",
 steps(("Distance", p(r"\(\tfrac{d}{35} - \tfrac{d}{40} = \tfrac{1}{10}\), so \(d = 28\) km and the usual time is 42 minutes.")),
       ("That day", p(r"\(\tfrac23\) of the way takes 14 minutes, plus 8 stopped: 22. That leaves 20 minutes for \(\tfrac{28}{3}\) km.")),
       ("Speed", p(r"\(\tfrac{28}{3} \div \tfrac13 = 28\) km/hr."))) + final(r"\(28\), option 4"),
 why_rows=[("1", "Too fast."), ("2", "Too slow."), ("3", "Too slow.")])

P.qa(9, r"Let \(m\) and \(n\) be natural numbers such that \(n\) is even and \(0.2 < \tfrac{m}{20}, \tfrac nm, \tfrac{n}{11} < 0.5\). Then \(m - 2n\) equals",
 M("4", "3", "1", "2"), "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 r"Bound \(n\) first; it has very few choices.",
 steps(("n", p(r"\(2.2 < n < 5.5\) and even: \(n = 4\).")),
       ("m", p(r"\(4 < m < 10\) and \(0.2 < \tfrac4m < 0.5\) gives \(8 < m < 20\). So \(m = 9\).")),
       ("Answer", p(r"\(9 - 8 = 1\)."))) + final(r"\(1\), option 3"),
 why_rows=[("1", "Doesn’t fit the bounds."), ("2", "Doesn’t fit the bounds."), ("4", "Doesn’t fit the bounds.")])

P.qa(10, r"How many integers in the set \(\{100, 101, 102, \dots, 999\}\) have at least one digit repeated?",
 [], "TITA", "252", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Count the ones with all digits different and subtract.",
 steps(("All different", p(r"\(9 \times 9 \times 8 = 648\).")),
       ("Repeated", p(r"\(900 - 648 = 252\)."))) + final(r"\(252\)"),
 concept=p("‘At least one’ is usually easiest as the total minus ‘none’."))

P.qa(11, r"In the final examination, Bishnu scored \(52\%\) and Asha scored \(64\%\). The marks obtained by Bishnu is \(23\) less, and that by Asha is \(34\) more than the marks obtained by Ramesh. The marks obtained by Geeta, who scored \(84\%\), is",
 M("439", "357", "399", "417"), "MCQ", "3", ["Arithmetic::Percentages"], "Easy",
 "The gap between Asha and Bishnu is 12% of the total.",
 steps(("Total", p(r"\(12\% = 23 + 34 = 57\), so the total is 475.")),
       ("Geeta", p(r"\(84\%\) of 475 is 399."))) + final(r"\(399\), option 3"),
 why_rows=[("1", "Not 84% of 475."), ("2", "Not 84% of 475."), ("4", "Not 84% of 475.")])

P.qa(12, r"If \(a\), \(b\), \(c\) are non-zero and \(14^a = 36^b = 84^c\), then \(6b\left(\tfrac1c - \tfrac1a\right)\) is equal to",
 [], "TITA", "3", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"Set each power equal to \(k\) and take logs to base \(k\).",
 steps(("Reciprocals", p(r"\(\tfrac1a = \log_k 14\), \(\tfrac1c = \log_k 84\), so \(\tfrac1c - \tfrac1a = \log_k 6\).")),
       ("b", p(r"\(b = \tfrac{1}{\log_k 36} = \tfrac{1}{2\log_k 6}\).")),
       ("Product", p(r"\(6 \times \tfrac{1}{2\log_k 6} \times \log_k 6 = 3\)."))) + final(r"\(3\)"),
 concept=r"\[x^a = k \iff \frac1a = \log_k x\]")

P.qa(13, r"A person invested a certain amount of money at \(10\%\) annual interest, compounded half-yearly. After one and a half years, the interest and principal together became Rs \(18522\). The amount, in rupees, that the person had invested is",
 [], "TITA", "16000", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Three half-years at 5%.",
 steps(("Growth", p(r"\(1.05^3 = 1.157625\).")),
       ("Principal", p(r"\(18522 \div 1.157625 = 16000\)."))) + final(r"\(16000\)"))

P.qa(14, r"A man buys \(35\) kg of sugar and sets a marked price in order to make a \(20\%\) profit. He sells \(5\) kg at this price, and \(15\) kg at a \(10\%\) discount. Accidentally, \(3\) kg of sugar is wasted. He sells the remaining sugar by raising the marked price by \(p\) percent so as to make an overall profit of \(15\%\). Then \(p\) is nearest to",
 M("31", "25", "22", "35"), "MCQ", "2", ["Arithmetic::Profit_Loss_and_Discount"], "Medium",
 "Take the cost as Rs 1 a kg.",
 steps(("So far", p(r"Cost 35, target 40.25. Marked price 1.2. Sales: \(5 \times 1.2 + 15 \times 1.08 = 22.2\).")),
       ("The last 12 kg", p(r"They must bring in 18.05, so \(1.2(1 + p) = \tfrac{18.05}{12} \approx 1.504\) and \(p \approx 25\%\)."))) + final(r"\(25\), option 2"),
 why_rows=[("1", "Too high."), ("3", "Too low."), ("4", "Too high.")])

P.qa(15, r"The points \((2, 1)\) and \((-3, -4)\) are opposite vertices of a parallelogram. If the other two vertices lie on the line \(x + 9y + c = 0\), then \(c\) is",
 M("15", "12", "13", "14"), "MCQ", "4", ["Geometry::Coordinate_Geometry"], "Easy",
 "The diagonals of a parallelogram bisect each other.",
 steps(("Midpoint", p(r"\(\left(-\tfrac12, -\tfrac32\right)\) lies on the other diagonal.")),
       ("Substitute", p(r"\(-\tfrac12 - \tfrac{27}{2} + c = 0\), so \(c = 14\)."))) + final(r"\(14\), option 4"),
 why_rows=[("1", "The midpoint isn’t on that line."), ("2", "The midpoint isn’t on that line."), ("3", "The midpoint isn’t on that line.")])

P.qa(16, r"A and B are two railway stations \(90\) km apart. A train leaves A at 9:00 a.m., heading towards B at a speed of \(40\) km/hr. Another train leaves B at 10:30 a.m., heading towards A at a speed of \(20\) km/hr. The trains meet each other at",
 ["11:20 a.m.", "11:45 a.m.", "11:00 a.m.", "10:45 a.m."], "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Where is the first train at 10:30?",
 steps(("Head start", p("By 10:30 it has gone 60 km, leaving 30.")),
       ("Closing", p("Together they close 60 km an hour: 30 minutes."))) + final("11:00 a.m., option 3"),
 why_rows=[("1", "Too late."), ("2", "Too late."), ("4", "Too early.")])

P.qa(17, r"Let \(N\), \(x\) and \(y\) be positive integers such that \(N = x + y\), \(2 < x < 10\) and \(14 < y < 23\). If \(N > 25\), then how many distinct values are possible for \(N\)?",
 [], "TITA", "6", ["Number_System::Miscellaneous"], "Easy",
 r"Find the largest possible \(N\).",
 steps(("Range", p(r"\(x \le 9\), \(y \le 22\), so \(N \le 31\). With \(N > 25\): 26 to 31.")),
       ("Count", p("6 values, each reachable."))) + final(r"\(6\)"))

P.qa(18, r"Let \(k\) be a constant. The equations \(kx + y = 3\) and \(4x + ky = 4\) have a unique solution if and only if",
 M(r"|k| \ne 2", "k = 2", r"k \ne 2", "|k| = 2"), "MCQ", "1", ["Algebra::Linear_Equations"], "Easy",
 "Unique when the lines aren’t parallel.",
 steps(("Determinant", p(r"\(k \cdot k - 4 \ne 0\), so \(k \ne \pm 2\)."))) + final(r"\(|k| \ne 2\), option 1"),
 concept=r"\[a_1x + b_1y = c_1,\ a_2x + b_2y = c_2 \text{ unique} \iff a_1b_2 \ne a_2b_1\]",
 why_rows=[("2", "Then there is no solution."), ("3", "Leaves out k = −2."), ("4", "The opposite.")])

P.qa(19, r"How many of the integers \(1, 2, \dots, 120\), are divisible by none of \(2\), \(5\) and \(7\)?",
 M("41", "42", "43", "44"), "MCQ", "1", ["Number_System::Factors_and_Divisibility", "Modern_Maths::Set_Theory"], "Medium",
 "Use inclusion–exclusion.",
 steps(("Divisible by at least one", p("60 + 24 + 17 − 12 − 8 − 3 + 1 = 79.")),
       ("None", p("120 − 79 = 41."))) + final(r"\(41\), option 1"),
 why_rows=[("2", "Off by one."), ("3", "Miscounted overlap."), ("4", "Miscounted overlap.")])

P.qa(20, r"How many pairs \((a, b)\) of positive integers are there such that \(a \le b\) and \(ab = 4^{2017}\)?",
 M("2017", "2018", "2019", "2020"), "MCQ", "2", ["Number_System::Factors_and_Divisibility"], "Medium",
 r"\(4^{2017} = 2^{4034}\). Count its divisors.",
 steps(("Divisors", p(r"4035 divisors, one of which is the square root \(2^{2017}\).")),
       ("Pairs", p(r"\(\tfrac{4035 + 1}{2} = 2018\)."))) + final(r"\(2018\), option 2"),
 concept=p("For a perfect square with d divisors, the pairs with a ≤ b number (d + 1)/2."),
 why_rows=[("1", "Misses the square pair."), ("3", "Too many."), ("4", "Too many.")])

P.qa(21, r"Anil, Sunil, and Ravi run along a circular path of length \(3\) km, starting from the same point at the same time, and going in the clockwise direction. If they run at speeds of \(15\) km/hr, \(10\) km/hr, and \(8\) km/hr, respectively, how much distance in km will Ravi have run when Anil and Sunil meet again for the first time at the starting point?",
 M("4.2", "4.8", "5.2", "4.6"), "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "When are both Anil and Sunil back at the start?",
 steps(("Lap times", p("Anil: 0.2 hours. Sunil: 0.3 hours. Both at the start after 0.6 hours.")),
       ("Ravi", p(r"\(8 \times 0.6 = 4.8\) km."))) + final(r"\(4.8\), option 2"),
 why_rows=[("1", "Wrong time."), ("3", "Wrong time."), ("4", "Wrong time.")])

P.qa(22, r"In a trapezium ABCD, AB is parallel to DC, BC is perpendicular to DC and \(\angle BAD = 45^\circ\). If \(DC = 5\) cm, \(BC = 4\) cm, the area of the trapezium in sq. cm is",
 [], "TITA", "28", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "Drop a perpendicular from D to AB.",
 steps(("AB", p(r"The 45° angle makes a right isosceles triangle with legs 4, so \(AB = 5 + 4 = 9\).")),
       ("Area", p(r"\(\tfrac12(5 + 9) \times 4 = 28\)."))) + final(r"\(28\)"))

P.qa(23, r"The area, in sq. units, enclosed by the lines \(x = 2\), \(y = |x - 2| + 4\), the X-axis and the Y-axis is equal to",
 M("6", "8", "12", "10"), "MCQ", "4", ["Geometry::Coordinate_Geometry"], "Easy",
 r"Between \(x = 0\) and \(2\), \(y = 6 - x\).",
 steps(("The shape", p(r"A trapezium with parallel sides 6 (at \(x = 0\)) and 4 (at \(x = 2\)), width 2.")),
       ("Area", p(r"\(\tfrac12(6 + 4) \times 2 = 10\)."))) + final(r"\(10\), option 4"),
 why_rows=[("1", "Too small."), ("2", "Uses height 4 throughout."), ("3", "Uses height 6 throughout.")])

P.qa(24, r"If \(f(x + y) = f(x)f(y)\) and \(f(5) = 4\), then \(f(10) - f(-10)\) is equal to",
 M("15.9375", "0", "3", "14.0625"), "MCQ", "1", ["Algebra::Functions"], "Easy",
 r"Find \(f(0)\) first.",
 steps(("Values", p(r"\(f(10) = 16\). \(f(0) = 1\), so \(f(-10) = \tfrac{1}{16}\).")),
       ("Difference", p(r"\(16 - 0.0625 = 15.9375\)."))) + final(r"\(15.9375\), option 1"),
 why_rows=[("2", r"\(f(-10)\) isn’t 16."), ("3", "No basis."), ("4", "Subtracts the wrong amount.")])

P.qa(25, r"\(\dfrac{2 \times 4 \times 8 \times 16}{(\log_2 4)^2 (\log_4 8)^3 (\log_8 16)^4}\) equals",
 [], "TITA", "24", ["Algebra::Logarithms_and_Exponents"], "Easy",
 "Work out each log separately.",
 steps(("Logs", p(r"\(\log_2 4 = 2\), \(\log_4 8 = \tfrac32\), \(\log_8 16 = \tfrac43\).")),
       ("Denominator", p(r"\(4 \times \tfrac{27}{8} \times \tfrac{256}{81} = \tfrac{128}{3}\).")),
       ("Answer", p(r"\(1024 \div \tfrac{128}{3} = 24\)."))) + final(r"\(24\)"),
 concept=r"\[\log_{2^a} 2^b = \frac ba\]")

P.qa(26, r"The vertices of a triangle are \((0, 0)\), \((4, 0)\) and \((3, 9)\). The area of the circle passing through these three points is",
 M(r"\tfrac{205\pi}{9}", r"\tfrac{123\pi}{7}", r"\tfrac{14\pi}{3}", r"\tfrac{12\pi}{5}"), "MCQ", "1", ["Geometry::Coordinate_Geometry", "Geometry::Circles"], "Medium",
 r"The centre lies on \(x = 2\).",
 steps(("Centre", p(r"\((2, k)\) is equidistant from \((0, 0)\) and \((3, 9)\): \(4 + k^2 = 1 + (9 - k)^2\), so \(k = \tfrac{13}{3}\).")),
       ("Radius", p(r"\(r^2 = 4 + \tfrac{169}{9} = \tfrac{205}{9}\)."))) + final(r"\(\tfrac{205\pi}{9}\), option 1"),
 why_rows=[("2", "Not the circumcircle."), ("3", "Not the circumcircle."), ("4", "Not the circumcircle.")])
