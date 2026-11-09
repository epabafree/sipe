# -*- coding: utf-8 -*-
# Simp Mock 6 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_06 import P
import m25_06_figs as F

P.qa(1, "Jiten borrows ₹64,000 from a bank at 12.5% per annum, compounded annually, and repays it completely in two instalments. The second instalment is 10% less than the first. The first, paid at the end of the first year, covers part of the principal plus a year’s interest on the whole principal. The second, paid at the end of the second year, covers the remaining principal plus a year’s interest on it. What was the first instalment (in ₹)?", [], "TITA", "40000", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "Let p be the principal repaid in the first instalment.",
 steps(("Instalments", p(r"First: \(p + 8000\). Second: \(1.125(64000 - p)\).")),
       ("Equation", p(r"\(1.125(64000 - p) = 0.9(p + 8000)\) gives \(64800 = 2.025p\), so \(p = 32000\). First instalment: 40000."))) + final("40000"))

P.qa(2, "Three identical circles of radius 1 cm are drawn inside an equilateral triangle so that each circle touches the other two externally and each side of the triangle is tangent to two of the circles, as shown." + F.CIRCLES + "The ratio of the perimeter of the triangle to the sum of the circumferences of the three circles is _________ .",
 ["Less than 0.9", "Between 0.9 and 1", "Between 1 and 1.1", "More than 1.1"], "MCQ", "1", ["Geometry::Circles"], "Hard",
 "Each side = the gap between two centres (2) plus two corner pieces.",
 steps(("Side", p(r"From a corner, the tangent to a circle of radius 1 in a 60° angle is \(\cot 30^\circ = \sqrt3\). Side \(= 2 + 2\sqrt3 \approx 5.46\).")),
       ("Ratio", p(r"\(\dfrac{3(2 + 2\sqrt3)}{6\pi} = \dfrac{1 + \sqrt3}{\pi} \approx 0.87\)."))) + final("Option 1"),
 why_rows=[("2", "Just below 0.9."), ("3", "Too high."), ("4", "Too high.")])

P.qa(3, r"Let \(x\) and \(y\) be positive real numbers. If \(x + \dfrac1x = 5\) and \(y^4 + \dfrac1{y^4} = 1154\), find the value of \(x^2y + \dfrac1{x^2y} + \dfrac{x^2}y + \dfrac y{x^2}\).", [], "TITA", "138", ["Algebra::Surds_and_Indices"], "Medium",
 "The expression factorises.",
 steps(("Factor", p(r"\(\left(x^2 + \tfrac1{x^2}\right)\left(y + \tfrac1y\right)\).")),
       ("Values", p(r"\(x^2 + \tfrac1{x^2} = 23\). \(y^2 + \tfrac1{y^2} = \sqrt{1156} = 34\), so \(y + \tfrac1y = \sqrt{36} = 6\).")),
       ("Product", p(r"\(23 \times 6 = 138\)."))) + final("138"))

P.qa(4, r"If \(a\) and \(b\) are two distinct real numbers such that \(5(\log_{32}a + \log_a 32) = 26\) and \(\dfrac1{26}(\log_{32}b + \log_b 32) = \dfrac15\), then the value of \(a + b\) can be ________ .",
 [r"\(2^{25} + 32\)", r"\(2^{25} + 2\)", r"\(32^{25} + 2\)", r"\(2^{25} - 2\)"], "MCQ", "2", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Both say \\(t + \\tfrac1t = \\tfrac{26}5\\) with \\(t = \\log_{32}\\).",
 steps(("t", p(r"\(t = 5\) or \(\tfrac15\): the number is \(32^5 = 2^{25}\) or \(32^{1/5} = 2\).")),
       ("Distinct", p(r"a and b take one each: \(a + b = 2^{25} + 2\)."))) + final("Option 2"),
 why_rows=[("1", "32 is not a solution."), ("3", r"\(32^{25}\) is too big."), ("4", "A sum, not a difference.")])

P.qa(5, r"The sum of the absolute values of the roots of \(12x^4 + 4x^3 - 41x^2 + 4x + 12 = 0\) is _______ .",
 [r"\(\tfrac{14}3\)", "5", "4", r"\(\tfrac{13}3\)"], "MCQ", "1", ["Algebra::Equations_and_Polynomials"], "Medium",
 "The coefficients are symmetric: divide by \\(x^2\\) and set \\(u = x + \\tfrac1x\\).",
 steps(("Reduce", p(r"\(12(u^2 - 2) + 4u - 41 = 0\), so \(12u^2 + 4u - 65 = 0\): \(u = \tfrac{13}6\) or \(-\tfrac52\).")),
       ("Roots", p(r"\(u = \tfrac{13}6\): \(x = \tfrac32, \tfrac23\). \(u = -\tfrac52\): \(x = -2, -\tfrac12\).")),
       ("Sum", p(r"\(\tfrac32 + \tfrac23 + 2 + \tfrac12 = \tfrac{14}3\)."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(6, r"In a class of only girls and boys, 30% of the students are girls. 70% of the boys and 30% of the girls are from urban areas; the rest are from rural areas. All students from urban areas are rich, \(\tfrac13\) of the girls from rural areas are poor, and \(\tfrac37\) of the boys from rural areas are poor. What percentage of the students in the class are poor?",
 ["12%", "14%", "16%", "19%"], "MCQ", "3", ["Arithmetic::Percentages"], "Easy",
 "Take 100 students.",
 steps(("Rural", p("Girls 30: rural 21. Boys 70: rural 21.")),
       ("Poor", p(r"\(\tfrac13 \times 21 + \tfrac37 \times 21 = 7 + 9 = 16\)."))) + final("16%, option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(7, r"\(\dfrac nd\) is a proper fraction in its lowest terms. If n is increased three times in succession by 60% each time and d is decreased three times in succession by 10% each time, the new fraction is the reciprocal of the original. Find \(d - n\), given that n and d are natural numbers.", [], "TITA", "37", ["Arithmetic::Percentages"], "Medium",
 "\\(\\dfrac{1.6^3 n}{0.9^3 d} = \\dfrac dn\\).",
 steps(("Square", p(r"\(\left(\tfrac nd\right)^2 = \tfrac{0.729}{4.096} = \tfrac{729}{4096}\), so \(\tfrac nd = \tfrac{27}{64}\).")),
       ("Answer", p("64 − 27 = 37."))) + final("37"))

P.qa(8, r"Find the value of \(\dfrac{1}{\left(1 - \tfrac1{2^2}\right)\left(1 - \tfrac1{3^2}\right)\left(1 - \tfrac1{4^2}\right)\cdots}\) (an infinite number of factors).", [], "TITA", "2", ["Algebra::Progressions_and_Series"], "Easy",
 "\\(1 - \\tfrac1{k^2} = \\tfrac{(k - 1)(k + 1)}{k \\cdot k}\\): the product telescopes.",
 steps(("Telescoping", p(r"Up to k = n the product is \(\tfrac{n + 1}{2n}\), which tends to \(\tfrac12\).")),
       ("Reciprocal", p("2."))) + final("2"))

P.qa(9, r"Which of the following values cannot be taken by \(\dfrac{x}{x^2 + 2x + 5}\) for real \(x\)?",
 [r"\(-\tfrac16\)", r"\(-\tfrac17\)", r"\(\tfrac17\)", r"\(\tfrac16\)"], "MCQ", "4", ["Algebra::Quadratic_Equations"], "Medium",
 "Set it equal to y; the quadratic in x needs a real root.",
 steps(("Discriminant", p(r"\(yx^2 + (2y - 1)x + 5y = 0\) needs \((2y - 1)^2 \ge 20y^2\), i.e. \(16y^2 + 4y - 1 \le 0\).")),
       ("Range", p(r"\(\dfrac{-1 - \sqrt5}8 \le y \le \dfrac{-1 + \sqrt5}8\), about −0.40 to 0.155. \(\tfrac16 \approx 0.167\) is outside."))) + final("Option 4"),
 why_rows=[("1", "−0.167 is inside."), ("2", "Inside."), ("3", "0.143 is inside.")])

P.qa(10, "A zoo has two types of animal, A and B. The number of type B animals is at least 10% more than that of type A. Each type A animal has 5 heads and 7 legs; each type B animal has 2 heads and 3 legs. If there are 100 animals in all, which of the following cannot be the difference between the total numbers of legs and heads?",
 ["106", "129", "142", "148"], "MCQ", "4", ["Arithmetic::Miscellaneous"], "Easy",
 "With a type A animals, difference = 100 + a.",
 steps(("Difference", p(r"Heads \(200 + 3a\), legs \(300 + 4a\): difference \(100 + a\).")),
       ("Range of a", p(r"\(100 - a \ge 1.1a\) gives \(a \le 47\). So the difference is at most 147."))) + final("148, option 4"),
 why_rows=[("1", "a = 6."), ("2", "a = 29."), ("3", "a = 42.")])

P.qa(11, "The area of trapezium ABCD is 168 cm². Side AD is perpendicular to both AB and CD. If AB = 18 cm and CD = 24 cm, find the perimeter (in cm) of ABCD.", [], "TITA", "60", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "AD is the height.",
 steps(("Height", p(r"\(\tfrac{18 + 24}2 \times h = 168\), so \(h = 8\).")),
       ("Slant side", p(r"\(BC = \sqrt{8^2 + 6^2} = 10\). Perimeter: 18 + 24 + 8 + 10 = 60."))) + final("60"))

P.qa(12, "A vessel contains a 30% acid solution (acid and water). 40 litres of the solution are removed and replaced with water, and the new concentration of acid is 25%. Find the total content of the vessel (in litres).", [], "TITA", "240", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "The concentration falls by the fraction removed.",
 steps(("Fraction", p(r"\(0.30\left(1 - \tfrac{40}V\right) = 0.25\), so \(\tfrac{40}V = \tfrac16\) and \(V = 240\)."))) + final("240"))

P.qa(13, r"If \(a, b, c, d\) are four distinct natural numbers such that \(a = b^{3/4}\) and \(c = d^{5/6}\), and \(b - d = 17\), the value of the product \(ac\) is ________ .",
 ["1024", "432", "864", "512"], "MCQ", "3", ["Number_System::Miscellaneous"], "Medium",
 "b must be a fourth power and d a sixth power.",
 steps(("Write", p(r"\(b = m^4, a = m^3\); \(d = n^6, c = n^5\). Then \(m^4 - n^6 = (m^2 - n^3)(m^2 + n^3) = 17\).")),
       ("Solve", p(r"\(m^2 - n^3 = 1\), \(m^2 + n^3 = 17\): \(m = 3, n = 2\). So \(a = 27, c = 32\), \(ac = 864\)."))) + final("864, option 3"),
 why_rows=[("1", "Wrong m, n."), ("2", "Wrong m, n."), ("4", "Wrong m, n.")])

P.qa(14, "Cities A and B are 136 km apart. Two men start walking at the same time from A and B towards each other. The man from A walks at a constant 4 km/h. The man from B walks at 2 km/h in the first hour, 2.25 km/h in the second hour, 2.5 km/h in the third hour, and so on. How far from City B (in km) will they meet?", [], "TITA", "68", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "In t whole hours, B covers an arithmetic series.",
 steps(("Equation", p(r"\(4t + \left[2t + \tfrac{0.25\,t(t - 1)}2\right] = 136\), so \(t^2 + 47t - 1088 = 0\) and \(t = 17\).")),
       ("Distance", p(r"A has walked 68 km, so they meet \(136 - 68 = 68\) km from B."))) + final("68"))

P.qa(15, "Ramesh and Suresh have trousers and shirts of the same quality. Ramesh packs 3 trousers and 5 shirts in a box and sells it for ₹4800 at a profit of 25%. Suresh packs 5 trousers and 3 shirts in a box and sells it for ₹4800 at a profit of 11.11%. What is the difference between the cost price of a trouser and that of a shirt?",
 ["360", "270", "420", "240"], "MCQ", "4", ["Arithmetic::Profit_and_Loss"], "Easy",
 "Cost of each box: 4800 ÷ 1.25 and 4800 ÷ (10/9).",
 steps(("Costs", p(r"\(3T + 5S = 3840\), \(5T + 3S = 4320\).")),
       ("Subtract", p(r"\(2(T - S) = 480\): \(T - S = 240\)."))) + final("240, option 4"),
 why_rows=[("1", "Wrong cost."), ("2", "Wrong cost."), ("3", "Wrong cost.")])

P.qa(16, r"A function f is defined on the whole numbers such that \(f(x + y) = f(x + 1) \times f(y - 1)\) and \(f(9) = 10\). Find \(|f(1) \times f(2) \times \cdots \times f(9)|\).",
 ["10000", "100000", "20000", "200000"], "MCQ", "2", ["Algebra::Functions"], "Medium",
 "Put y = 1, then x = 0.",
 steps(("f(0)", p(r"\(y = 1\): \(f(x + 1) = f(x + 1)f(0)\), so \(f(0) = 1\).")),
       ("Pattern", p(r"\(x = 0\): \(f(y) = f(1)f(y - 1)\), so \(f(n) = f(1)^n\) and \(f(1)^9 = 10\).")),
       ("Product", p(r"\(f(1)^{1 + 2 + \cdots + 9} = f(1)^{45} = 10^5\)."))) + final("100000, option 2"),
 why_rows=[("1", r"\(10^4\)."), ("3", "Not a power of 10."), ("4", "Not a power of 10.")])

P.qa(17, "In the diagram, O is the centre of the circle and AB is a chord." + F.SEGMENT + r"If ∠AOB = 120° and AB = \(16\sqrt3\) cm, the ratio of the area of the shaded region to the area of the circle is ________ .",
 [r"\(\left(\tfrac16 - \tfrac{\sqrt3}{4\pi}\right) : 1\)", r"\(\left(\tfrac13 - \tfrac{\sqrt3}{8\pi}\right) : 1\)", r"\(\left(\tfrac13 - \tfrac{\sqrt3}{4\pi}\right) : 1\)", r"\(\left(\tfrac16 - \tfrac{\sqrt3}{8\pi}\right) : 1\)"], "MCQ", "3", ["Geometry::Circles"], "Medium",
 "Shaded = sector − triangle.",
 steps(("Radius", p(r"\(AB = 2r\sin 60^\circ = r\sqrt3 = 16\sqrt3\), so \(r = 16\).")),
       ("Segment", p(r"Sector \(\tfrac13\pi r^2\), triangle \(\tfrac12 r^2 \sin 120^\circ = \tfrac{\sqrt3}4 r^2\).")),
       ("Ratio", p(r"Divide by \(\pi r^2\): \(\tfrac13 - \tfrac{\sqrt3}{4\pi}\)."))) + final("Option 3"),
 why_rows=[("1", "Uses a 60° sector."), ("2", "Halves the triangle twice."), ("4", "Both parts wrong.")])

P.qa(18, "A company plans to change the salaries of Amey, Bhavesh and Charan. If Amey’s salary is reduced by 25% and Bhavesh’s is increased by 20%, Bhavesh’s salary becomes twice Amey’s. If Bhavesh’s salary is increased by 50% and Charan’s by 20%, their salaries become equal. Amey’s salary is increased by P% and Charan’s decreased by Q% to make their salaries equal, where Q is 80% of P. What is P − Q?",
 ["4", "5", "6", "8"], "MCQ", "2", ["Arithmetic::Percentages"], "Medium",
 "Express B and C in terms of A.",
 steps(("Ratios", p(r"\(1.2B = 1.5A\): \(B = 1.25A\). \(1.5B = 1.2C\): \(C = 1.25B = 1.5625A\).")),
       ("P", p(r"\(1 + P = 1.5625(1 - 0.8P)\) gives \(2.25P = 0.5625\): P = 25%, Q = 20%."))) + final("5, option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(19, "If (10 − a), (10 − b), (10 − c), (10 − d) and (10 − e) are five distinct integers whose product is 45, what is the maximum possible value of abcde?",
 ["41580", "40950", "45045", "38600"], "MCQ", "3", ["Number_System::Factors_and_Divisibility"], "Medium",
 "Five distinct integers with product 45: try ±1, ±3, 5.",
 steps(("The integers", p("45 = 3² × 5 needs five distinct factors, so ±1 must both appear: −1, 1, −3, 3, 5 (product 45). No other set works.")),
       ("a to e", p(r"10 minus each: 11, 9, 13, 7, 5. Product \(= 45045\)."))) + final("45045, option 3"),
 why_rows=[("1", "Not achievable."), ("2", "Not achievable."), ("4", "Not achievable.")])

P.qa(20, "A group of n friends planned a trip and split the cost by the number of rides each took. Every friend’s contribution was different, and the average contribution was ₹5000. Ramesh, who had contributed the least, then raised his share to 9 times his original contribution, and the new average became ₹6000. If all contributions were multiples of ₹10, how many values could Ramesh’s original contribution have taken?", [], "TITA", "19", ["Arithmetic::Average"], "Hard",
 "The total rises by 8r = 1000n.",
 steps(("r", p(r"\(8r = 1000n\), so \(r = 125n\). A multiple of 10 needs n even.")),
       ("Bound", p(r"r is the smallest of different contributions, so it is below the average: \(125n < 5000\), \(n < 40\).")),
       ("Count", p("n = 2, 4, …, 38: 19 values."))) + final("19"))

P.qa(21, "A workshop has 12 identical machines that together finish assembling a product in 10 hours. A group of 6 machines starts at 10:00 AM, and one more machine joins every 2 hours, starting at 2:00 PM. When will the assembly be finished?",
 ["12:15 PM", "12:15 AM", "12:30 AM", "12:45 AM"], "MCQ", "3", ["Arithmetic::Time_and_Work"], "Medium",
 "Total work: 120 machine-hours.",
 steps(("By the clock", table(["Period", "Machines", "Work", "Total"], [["10–2", "6", "24", "24"], ["2–4", "7", "14", "38"], ["4–6", "8", "16", "54"], ["6–8", "9", "18", "72"], ["8–10", "10", "20", "92"], ["10–12", "11", "22", "114"]])),
       ("Last bit", p("From midnight, 12 machines do the last 6 in 30 minutes."))) + final("12:30 AM, option 3"),
 why_rows=[("1", "Midday, far too early."), ("2", "Too early."), ("4", "Too late.")])

P.qa(22, r"If \(\big||x - 5| - 6\big| > 4\), which of the following is the range of x?",
 [r"\((-\infty, \infty)\)", r"\((-\infty, -5) \cup (15, \infty)\)", r"\((-\infty, -5) \cup [3, 7] \cup (15, \infty)\)", r"\((-\infty, -5) \cup (3, 7) \cup (15, \infty)\)"], "MCQ", "4", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "Open the outer bars: \\(|x - 5| > 10\\) or \\(|x - 5| < 2\\).",
 steps(("Cases", p(r"\(|x - 5| > 10\): \(x < -5\) or \(x > 15\). \(|x - 5| < 2\): \(3 < x < 7\)."))) + final("Option 4"),
 why_rows=[("1", "x = 0 fails."), ("2", "Misses (3, 7)."), ("3", "3 and 7 give exactly 4, not more.")])
