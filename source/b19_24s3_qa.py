# -*- coding: utf-8 -*-
# Batch 19 — CAT 2024 Slot 3: QA Q1–22 (exam order).
from fmt import steps, final, trap, why, table, p
from b19_24s3 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"If \(3^a = 4\), \(4^b = 5\), \(5^c = 6\), \(6^d = 7\), \(7^e = 8\) and \(8^f = 9\), then the value of the product \(abcdef\) is",
 [], "TITA", "2", ["Algebra::Logarithms_and_Exponents"], "Easy",
 r"Chain them: \(3^{ab} = 4^b = 5\), and so on.",
 steps(p(r"\(3^{abcdef} = 9\), because each step feeds into the next: \(3^a = 4\), \(3^{ab} = 5\), …, \(3^{abcdef} = 8^f = 9\). So \(abcdef = 2\).")) + final(r"\(2\)"),
 shortcut=r"\(abcdef = \log_3 4 \cdot \log_4 5 \cdots \log_8 9\) \(= \log_3 9 = 2\).",
 concept=r"\[\log_a b \cdot \log_b c = \log_a c\]")

P.qa(2, r"The number of distinct integer solutions \((x, y)\) of the equation \(|x + y| + |x - y| = 2\), is",
 [], "TITA", "8", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 r"\(|x + y| + |x - y|\) is twice the larger of \(|x|\) and \(|y|\).",
 steps(("Simplify", p(r"The left side is always twice the larger of \(|x|\) and \(|y|\). So the larger of the two must be 1.")),
       ("Count", p(r"These are the integer points on the square with corners \((\pm1, \pm1)\): \((\pm1, -1)\), \((\pm1, 0)\), \((\pm1, 1)\) and \((0, \pm1)\). That is 8."))) + final(r"\(8\)"),
 concept=p(r"For any numbers, \(|a + b| + |a - b|\) \(= 2\max(|a|, |b|)\)."))

P.qa(3, r"A circular plot of land is divided into two regions by a chord of length \(10\sqrt3\) meters such that the chord subtends an angle of \(120^\circ\) at the center. Then, the area, in square meters, of the smaller region is",
 M(r"20\left(\tfrac{4\pi}{3} + \sqrt3\right)", r"20\left(\tfrac{4\pi}{3} - \sqrt3\right)", r"25\left(\tfrac{4\pi}{3} - \sqrt3\right)", r"25\left(\tfrac{4\pi}{3} + \sqrt3\right)"), "MCQ", "3", ["Geometry::Circles"], "Medium",
 "Find the radius from the chord, then subtract the triangle from the sector.",
 steps(("Radius", p(r"A chord subtending \(120^\circ\) has length \(r\sqrt3\), so \(r = 10\).")),
       ("Sector minus triangle", p(r"Sector: \(\frac{120}{360}\pi \cdot 100 = \frac{100\pi}{3}\). Triangle: \(\frac12 \cdot 100 \cdot \sin 120^\circ = 25\sqrt3\).")),
       ("Area", p(r"\(\frac{100\pi}{3} - 25\sqrt3 = 25\left(\frac{4\pi}{3} - \sqrt3\right)\)."))) + final("Option 3"),
 concept=r"\[\text{segment} = \tfrac{\theta}{360^\circ}\pi r^2 - \tfrac12 r^2 \sin\theta\]",
 why_rows=[("1", "Wrong factor, and it adds the triangle."), ("2", "The factor should be 25."), ("4", "The triangle must be subtracted.")])

P.qa(4, "A train travelled a certain distance at a uniform speed. Had the speed been 6 km per hour more, it would have needed 4 hours less. Had the speed been 6 km per hour less, it would have needed 6 hours more. The distance, in km, travelled by the train is",
 M("800", "720", "780", "640"), "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Write each condition as an equation for the distance in terms of the speed v.",
 steps(("First condition", p(r"\(\frac{d}{v} - \frac{d}{v + 6} = 4\) gives \(d = \frac{2v(v + 6)}{3}\).")),
       ("Second condition", p(r"\(\frac{d}{v - 6} - \frac{d}{v} = 6\) gives \(d = v(v - 6)\).")),
       ("Solve", p(r"\(\frac{2(v + 6)}{3} = v - 6\), so \(v = 30\) and \(d = 30 \times 24 = 720\)."))) + final(r"\(720\) km, option 2"),
 concept=r"\[\frac{d}{v} - \frac{d}{v + k} = \frac{dk}{v(v + k)}\]",
 why_rows=[("1", "This doesn’t fit a whole-number speed for both conditions."), ("3", "This doesn’t satisfy either condition."), ("4", "This doesn’t satisfy either condition.")])

P.qa(5, "Rajesh and Vimal own 20 hectares and 30 hectares of agricultural land, respectively, which are entirely covered by wheat and mustard crops. The cultivation area of wheat and mustard in the land owned by Vimal are in the ratio of 5 : 3. If the total cultivation area of wheat and mustard are in the ratio 11 : 9, then the ratio of cultivation area of wheat and mustard in the land owned by Rajesh is",
 M("4 : 3", "3 : 7", "1 : 1", "7 : 9"), "MCQ", "4", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Find the wheat area overall and on Vimal’s land.",
 steps(p(r"Total wheat: \(\frac{11}{20} \times 50 = 27.5\). Vimal’s wheat: \(\frac58 \times 30 = 18.75\). Rajesh’s wheat is 8.75 and his mustard \(20 - 8.75 = 11.25\): \(8.75 : 11.25 = 7 : 9\).")) + final(r"\(7 : 9\), option 4"),
 concept=r"\[\text{part} = \frac{\text{its share}}{\text{sum of shares}} \times \text{whole}\]",
 why_rows=[("1", "This would give Rajesh more wheat than mustard."), ("2", "That gives Rajesh only 6 hectares of wheat."), ("3", "That gives Rajesh 10 hectares of wheat.")])

P.qa(6, "Aman invests Rs 4000 in a bank at a certain rate of interest, compounded annually. If the ratio of the value of the investment after 3 years to the value of the investment after 5 years is 25 : 36, then the minimum number of years required for the value of the investment to exceed Rs 20000 is",
 [], "TITA", "9", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "Two years of growth multiply the value by 36/25.",
 steps(("The rate", p(r"\((1 + r)^2 = \frac{36}{25}\), so \(1 + r = 1.2\).")),
       ("Reaching 5 times", p(r"We need \(1.2^n > 5\). \(1.2^8 \approx 4.30\) and \(1.2^9 \approx 5.16\). So 9 years."))) + final(r"\(9\)"),
 concept=r"\[A = P(1 + r)^n\]")

P.qa(7, r"If \(10^{68}\) is divided by \(13\), the remainder is", M("9", "5", "8", "4"), "MCQ", "1", ["Number_System::Remainders"], "Easy",
 r"\(10^3 = 1000\). What is its remainder when divided by 13?",
 steps(p(r"\(1001 = 7 \times 11 \times 13\), so \(10^3 \equiv -1\) and \(10^6 \equiv 1 \pmod{13}\). \(68 = 6 \times 11 + 2\), so \(10^{68} \equiv 10^2 = 100 = 7 \times 13 + 9\).")) + final(r"\(9\), option 1"),
 concept=r"\[10^3 \equiv -1 \pmod{7, 11, 13}\]",
 why_rows=[("2", "This doesn’t match any power of 10 here."), ("3", "This doesn’t match the cycle."), ("4", r"This is \(-9\), the remainder of \(10^5\).")])

P.qa(8, "The average of three distinct real numbers is 28. If the smallest number is increased by 7 and the largest number is reduced by 10, the order of the numbers remains unchanged, and the new arithmetic mean becomes 2 more than the middle number, while the difference between the largest and the smallest numbers becomes 64. Then, the largest number in the original set of three numbers is",
 [], "TITA", "70", ["Arithmetic::Average"], "Medium",
 "The new total is 84 − 3 = 81. That fixes the middle number.",
 steps(("Middle", p(r"New average 27 = middle + 2, so the middle number is 25.")),
       ("The other two", p(r"Original smallest + largest \(= 84 - 25 = 59\). After the changes their difference is 64, so originally it was \(64 + 17 = 81\). The largest is \(\frac{59 + 81}{2} = 70\)."))) + final(r"\(70\)"),
 concept=r"\[\text{total} = \text{average} \times \text{count}\]")

P.qa(9, "In a group of 250 students, the percentage of girls was at least 44% and at most 60%. The rest of the students were boys. Each student opted for either swimming or running or both. If 50% of the boys and 80% of the girls opted for swimming while 70% of the boys and 60% of the girls opted for running, then the minimum and maximum possible number of students who opted for both swimming and running, are",
 ["75 and 96, respectively", "75 and 90, respectively", "72 and 88, respectively", "72 and 80, respectively"], "MCQ", "4", ["Modern_Maths::Set_Theory"], "Medium",
 "Everyone picks at least one sport, so both = swimmers + runners − 250.",
 steps(("Both", p(r"With \(G\) girls and \(250 - G\) boys: swimmers + runners \(= 1.2(250 - G) + 1.4G\) \(= 300 + 0.2G\). Both \(= 50 + 0.2G\).")),
       ("Range", p(r"\(G\) runs from 110 (44%) to 150 (60%), so both runs from 72 to 80. Both ends give whole numbers of boys and girls in each group."))) + final("72 and 80, option 4"),
 concept=p(r"\(n(A \cap B) = n(A) + n(B) - n(A \cup B)\)"),
 why_rows=[("1", "This doesn’t follow from 50 + 0.2G."), ("2", "This doesn’t follow from 50 + 0.2G."), ("3", "The maximum is 80, at 150 girls.")])

P.qa(10, r"If \(\left(a + b\sqrt3\right)^2 = 52 + 30\sqrt3\), where \(a\) and \(b\) are natural numbers, then \(a + b\) equals",
 M("8", "10", "7", "9"), "MCQ", "1", ["Algebra::Surds_and_Indices"], "Easy",
 r"Match the rational part and the \(\sqrt3\) part.",
 steps(p(r"\(a^2 + 3b^2 = 52\) and \(2ab = 30\), so \(ab = 15\). Trying \(a = 5, b = 3\): \(25 + 27 = 52\). So \(a + b = 8\).")) + final(r"\(8\), option 1"),
 concept=r"\[(a + b\sqrt3)^2 = a^2 + 3b^2 + 2ab\sqrt3\]",
 why_rows=[("2", r"\(a = 3, b = 5\) gives \(9 + 75 = 84\)."), ("3", "No such natural numbers."), ("4", "No such natural numbers.")])

P.qa(11, r"The midpoints of sides AB, BC, and AC in \(\triangle ABC\) are M, N, and P, respectively. The medians drawn from A, B, and C intersect the line segments MP, MN and NP at X, Y, and Z, respectively. If the area of \(\triangle ABC\) is 1440 sq cm, then the area, in sq cm, of \(\triangle XYZ\) is",
 [], "TITA", "90", ["Geometry::Triangles"], "Medium",
 "The median from A bisects MP. So X, Y and Z are midpoints of the sides of triangle MNP.",
 steps(("Medial triangle", p(r"\(\triangle MNP\) joins the midpoints of ABC, so its area is \(\frac14 \times 1440 = 360\).")),
       ("Its midpoints", p(r"MP is parallel to BC, and the median AN cuts it at its midpoint X. In the same way Y and Z are the midpoints of MN and NP. So XYZ is the medial triangle of MNP: \(\frac14 \times 360 = 90\)."))) + final(r"\(90\)"),
 concept=r"\[\text{triangle joining the midpoints} = \tfrac14 \text{ of the area}\]")

P.qa(12, r"The sum of all distinct real values of \(x\) that satisfy the equation \(10^x + \frac{4}{10^x} = \frac{91}{2}\), is",
 M(r"\log_{10} 2", r"3\log_{10} 2", r"2\log_{10} 2", r"4\log_{10} 2"), "MCQ", "3", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"Put \(t = 10^x\). You need the product of the two values of t.",
 steps(p(r"\(2t^2 - 91t + 8 = 0\) has two positive roots with product 4. Since \(10^{x_1} \cdot 10^{x_2} = 4\), \(x_1 + x_2 = \log_{10} 4 = 2\log_{10} 2\).")) + final("Option 3"),
 concept=r"\[10^{x_1} \cdot 10^{x_2} = 10^{x_1 + x_2}\]",
 why_rows=[("1", "This is half the product’s log."), ("2", "This would need a product of 8."), ("4", "This would need a product of 16.")])

P.qa(13, r"The number of distinct real values of \(x\), satisfying the equation \(\max\{x, 2\} - \min\{x, 2\}\) \(= |x + 2| - |x - 2|\), is",
 [], "TITA", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 r"\(\max\{x, 2\} - \min\{x, 2\} = |x - 2|\).",
 steps(("Rewrite", p(r"The equation becomes \(2|x - 2| = |x + 2|\).")),
       ("Cases", p(r"\(x \ge 2\): \(2x - 4 = x + 2\), so \(x = 6\). \(-2 \le x < 2\): \(4 - 2x = x + 2\), so \(x = \frac23\). \(x < -2\): \(4 - 2x = -x - 2\) gives \(x = 6\), not in range. Two solutions."))) + final(r"\(2\)"),
 concept=r"\[\max\{a, b\} - \min\{a, b\} = |a - b|\]")

P.qa(14, "A certain amount of water was poured into a 300 litre container and the remaining portion of the container was filled with milk. Then an amount of this solution was taken out from the container which was twice the volume of water that was earlier poured into it, and water was poured to refill the container again. If the resulting solution contains 72% milk, then the amount of water, in litres, that was initially poured into the container was",
 [], "TITA", "30", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "With w litres of water, the milk left is (300 − w) × (1 − 2w/300).",
 steps(("Equation", r"\[(300 - w)\left(1 - \frac{2w}{300}\right) = 216\]" + p(r"so \((300 - w)(300 - 2w) = 64800\), which gives \(w^2 - 450w + 12600 = 0\).")),
       ("Solve", p(r"\(w = 30\) or \(420\). Only 30 fits in a 300-litre container."))) + final(r"\(30\)"),
 concept=r"\[\text{milk left} = \text{milk} \times \left(1 - \frac{\text{removed}}{\text{total}}\right)\]")

P.qa(15, r"For any non-zero real number \(x\), let \(f(x) + 2f\left(\frac1x\right) = 3x\). Then, the sum of all possible values of \(x\) for which \(f(x) = 3\), is",
 M("-2", "3", "2", "-3"), "MCQ", "4", ["Algebra::Functions"], "Medium",
 r"Replace \(x\) with \(\frac1x\) to get a second equation, then solve for \(f(x)\).",
 steps(("Two equations", p(r"\(f(x) + 2f(1/x) = 3x\) and \(f(1/x) + 2f(x) = \frac3x\). Doubling the second and subtracting: \(3f(x) = \frac6x - 3x\), so \(f(x) = \frac2x - x\).")),
       ("Solve", p(r"\(\frac2x - x = 3\) gives \(x^2 + 3x - 2 = 0\), whose roots are real and add to \(-3\)."))) + final(r"\(-3\), option 4"),
 concept=r"\[f(x) + kf(1/x) = g(x) \;\Rightarrow\; \text{swap } x \leftrightarrow 1/x \text{ and solve the pair}\]",
 why_rows=[("1", "This is the product of the roots."), ("2", "Wrong sign."), ("3", "Wrong sign and value.")])

P.qa(16, "Gopi marks a price on a product in order to make 20% profit. Ravi gets 10% discount on this marked price, and thus saves Rs 15. Then, the profit, in rupees, made by Gopi by selling the product to Ravi, is",
 M("10", "20", "15", "25"), "MCQ", "1", ["Arithmetic::Profit_Loss_and_Discount"], "Easy",
 "The Rs 15 saving is 10% of the marked price.",
 steps(p(r"Marked price 150, so cost \(150 \div 1.2 = 125\). Ravi pays 135, so Gopi’s profit is 10.")) + final(r"\(10\), option 1"),
 concept=r"\[\text{MP} = \text{CP} \times (1 + \text{markup})\]",
 why_rows=[("2", "A profit of 20 would need a discount of only Rs 5."), ("3", "That is Ravi’s saving, not Gopi’s profit."), ("4", "That is the profit before the discount.")])

P.qa(17, r"Consider the sequence \(t_1 = 1\), \(t_2 = -1\) and \(t_n = \left(\frac{n - 3}{n - 1}\right)t_{n-2}\) for \(n \ge 3\). Then, the value of the sum \(\frac{1}{t_2} + \frac{1}{t_4} + \frac{1}{t_6} + \cdots + \frac{1}{t_{2022}} + \frac{1}{t_{2024}}\), is",
 M("-1022121", "-1026169", "-1024144", "-1023132"), "MCQ", "3", ["Algebra::Progressions_and_Series"], "Medium",
 r"Work out \(t_4\) and \(t_6\) and spot the pattern.",
 steps(("The pattern", p(r"\(t_4 = \frac13 t_2 = -\frac13\), \(t_6 = \frac35 t_4 = -\frac15\). In general \(t_{2k} = -\frac{1}{2k - 1}\).")),
       ("The sum", p(r"\(\frac{1}{t_{2k}} = -(2k - 1)\). For \(k = 1\) to 1012 this is minus the sum of the first 1012 odd numbers: \(-1012^2 = -1024144\)."))) + final(r"\(-1024144\), option 3"),
 concept=r"\[1 + 3 + 5 + \cdots + (2n - 1) = n^2\]",
 why_rows=[("1", r"This is \(-1011^2\), one term too few."), ("2", r"This is \(-1013^2\), one term too many."), ("4", r"This is \(-1011 \times 1012\).")])

P.qa(18, "The number of all positive integers up to 500 with non-repeating digits is",
 [], "TITA", "378", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Count 1-digit, 2-digit and 3-digit numbers separately. 500 itself repeats a digit.",
 steps(p(r"1-digit: 9. 2-digit: \(9 \times 9 = 81\). 3-digit from 100 to 499: \(4 \times 9 \times 8 = 288\). Total 378.")) + final(r"\(378\)"),
 concept=r"\[\text{fill places one at a time, avoiding digits already used}\]")

P.qa(19, "After two successive increments, Gopal's salary became 187.5% of his initial salary. If the percentage of salary increase in the second increment was twice of that in the first increment, then the percentage of salary increase in the first increment was",
 M("20", "25", "27.5", "30"), "MCQ", "2", ["Arithmetic::Percentages"], "Easy",
 "Test the options: (1 + x)(1 + 2x) = 1.875.",
 steps(p(r"\(x = 0.25\): \(1.25 \times 1.5 = 1.875\). It works.")) + final(r"\(25\%\), option 2"),
 concept=r"\[\text{successive increases multiply: } (1 + x)(1 + y)\]",
 why_rows=[("1", r"\(1.2 \times 1.4 = 1.68\)."), ("3", r"\(1.275 \times 1.55 \approx 1.98\)."), ("4", r"\(1.3 \times 1.6 = 2.08\).")])

P.qa(20, "Sam can complete a job in 20 days when working alone. Mohit is twice as fast as Sam and thrice as fast as Ayna in the same job. They undertake a job with an arrangement where Sam and Mohit work together on the first day, Sam and Ayna on the second day, Mohit and Ayna on the third day, and this three-day pattern is repeated till the work gets completed. Then, the fraction of total work done by Sam is",
 M(r"\tfrac{3}{20}", r"\tfrac{3}{10}", r"\tfrac15", r"\tfrac{1}{20}"), "MCQ", "2", ["Arithmetic::Time_and_Work"], "Medium",
 "Use 60 units of work: Sam 3 a day, Mohit 6, Ayna 2.",
 steps(("A cycle", p("Day 1: 9 units, day 2: 5, day 3: 8. That is 22 units per three days.")),
       ("Finishing", p("Two cycles give 44. Day 7 adds 9 (53), day 8 adds 5 (58), and Mohit and Ayna finish the last 2 on day 9.")),
       ("Sam’s share", p(r"Sam works days 1, 2, 4, 5, 7 and 8: \(6 \times 3 = 18\) units, which is \(\frac{18}{60} = \frac{3}{10}\)."))) + final(r"\(\tfrac{3}{10}\), option 2"),
 concept=r"\[\text{take total work as the LCM of the individual times}\]",
 why_rows=[("1", "This counts only half of Sam’s days."), ("3", "This counts only four of Sam’s six days."), ("4", "This is a single day of Sam’s work.")])

P.qa(21, "A regular octagon ABCDEFGH has sides on length 6 cm each. Then the area, in sq. cm, of the square ACEG is",
 M(r"36\left(2 + \sqrt2\right)", r"72\left(1 + \sqrt2\right)", r"36\left(1 + \sqrt2\right)", r"72\left(2 + \sqrt2\right)"), "MCQ", "1", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 r"The angle ABC of a regular octagon is \(135^\circ\). Find AC with the cosine rule.",
 steps(p(r"\(AC^2 = 6^2 + 6^2 - 2 \cdot 36 \cos 135^\circ\) \(= 72 + 36\sqrt2 = 36(2 + \sqrt2)\). That is the area of the square ACEG.")) + final("Option 1"),
 concept=r"\[c^2 = a^2 + b^2 - 2ab\cos C\]",
 why_rows=[("2", r"This is the area of the whole octagon, \(2(1 + \sqrt2)a^2\)."), ("3", "This is half the octagon’s area."), ("4", "This doubles the square’s area.")])

P.qa(22, r"For some constant real numbers \(p\), \(k\) and \(a\) consider the following system of linear equations in \(x\) and \(y\):<br>\(px - 4y = 2\)<br>\(3x + ky = a\)<br>A necessary condition for the system to have no solution for \((x, y)\) is",
 M("ap - 6 = 0", "ap + 6 = 0", r"2a + k \ne 0", r"kp + 12 \ne 0"), "MCQ", "3", ["Algebra::Linear_Equations"], "Medium",
 "No solution means the lines are parallel but different.",
 steps(("Parallel", p(r"\(\frac{p}{3} = \frac{-4}{k}\), so \(kp = -12\).")),
       ("Not the same line", p(r"\(\frac{-4}{k} \ne \frac{2}{a}\), so \(-4a \ne 2k\), that is \(2a + k \ne 0\)."))) + final("Option 3"),
 concept=r"\[\frac{a_1}{a_2} = \frac{b_1}{b_2} \ne \frac{c_1}{c_2} \;\Rightarrow\; \text{no solution}\]",
 why_rows=[("1", "This isn’t required for parallel lines."), ("2", "This isn’t required either."), ("4", "This is the opposite: no solution needs kp + 12 = 0.")])
