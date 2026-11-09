# -*- coding: utf-8 -*-
# Simp Mock 7 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_07 import P
import m25_07_figs as F

P.qa(1, r"Find the product of all the real roots of the equation \(x^{\sqrt{x^3}} = \sqrt[3]{x^{2x}}\).", ["0", "1", r"\(\tfrac23\)", r"\(\tfrac49\)"], "MCQ", "4", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Same base on both sides: \\(x^{x^{3/2}} = x^{2x/3}\\).",
 steps(("x = 1", p("Both sides are 1: a root.")),
       ("Equal exponents", p(r"\(x^{3/2} = \tfrac{2x}3\) gives \(\sqrt x = \tfrac23\), so \(x = \tfrac49\). (x must be positive for \(\sqrt{x^3}\); 0 gives \(0^0\).)")),
       ("Product", p(r"\(1 \times \tfrac49 = \tfrac49\)."))) + final("Option 4"),
 why_rows=[("1", "0 isn’t a root."), ("2", "Misses 4/9."), ("3", r"\(\sqrt x\), not x.")])

P.qa(2, "In the figure (not to scale), AB and CD are chords of a circle with centre O. ∠AOB = 90° and ∠COD = 120°. The perimeter of △COD is more than that of △AOB by \\(2\\sqrt{2 + \\sqrt3}\\,(\\sqrt3 - \\sqrt2)\\) cm. Find the absolute difference (in cm²) between the areas of △AOB and △COD." + F.CHORDS,
 [r"\(\dfrac{\sqrt2}3\)", "1", "2", "3"], "MCQ", "2", ["Geometry::Circles"], "Hard",
 "AB = r√2 and CD = r√3; the radii cancel in the perimeter difference.",
 steps(("Radius", p(r"Perimeter difference \(= r(\sqrt3 - \sqrt2)\), so \(r = 2\sqrt{2 + \sqrt3}\) and \(r^2 = 4(2 + \sqrt3)\).")),
       ("Areas", p(r"△AOB \(= \tfrac{r^2}2\); △COD \(= \tfrac12 r^2 \sin 120^\circ = \tfrac{\sqrt3}4 r^2\).")),
       ("Difference", p(r"\(\tfrac{r^2}4(2 - \sqrt3) = (2 + \sqrt3)(2 - \sqrt3) = 1\)."))) + final("1, option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Forgets the ¼."), ("4", "Arithmetic slip.")])

P.qa(3, "A, B and C together can complete a task in 5 days. A works alone for 4 days and stops. Then B and C work together for the next 4 days. Then C stops, and B finishes the remaining work alone in 3 days. In how many days can A and C together complete the task?",
 ["7.5 days", "8.5 days", "9.5 days", "Cannot be determined"], "MCQ", "1", ["Arithmetic::Time_and_Work"], "Easy",
 "A’s 4 days + B and C’s 4 days = 4 days of all three.",
 steps(("B", p(r"\(4 \times \tfrac15 + 3B = 1\), so \(B = \tfrac1{15}\).")),
       ("A + C", p(r"\(\tfrac15 - \tfrac1{15} = \tfrac2{15}\): 7.5 days."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "The 4-day blocks combine.")])

P.qa(4, "A business school’s exchange council forms teams to help incoming exchange students. It forms 20 teams of three students each to receive the students at the airport, and y teams of four students each to help them settle on campus. If each of the council’s x members is in 5 different airport teams and 6 different settling teams, find x + y.", [], "TITA", "30", ["Arithmetic::Miscellaneous"], "Easy",
 "Count memberships two ways.",
 steps(("Airport", p(r"\(20 \times 3 = 5x\), so \(x = 12\).")),
       ("Settling", p(r"\(4y = 6 \times 12\), so \(y = 18\). x + y = 30."))) + final("30"))

P.qa(5, r"Find the value of \(\dfrac1{\sqrt2}\left\{a^4 + b^4 + (a + b)^4\right\}^{1/2}\).",
 [r"\((a + b)^2 + ab\)", r"\((a + b)^2 - ab\)", r"\(\sqrt{a^4 + b^4 - a^2b^2}\)", r"\(\sqrt{a^4 + b^4 + 4a^2b^2 + 2ab}\)"], "MCQ", "2", ["Algebra::Equations_and_Polynomials"], "Medium",
 "\\(a^4 + b^4 + (a + b)^4 = 2(a^2 + ab + b^2)^2\\).",
 steps(("Identity", p(r"Expand: \(2a^4 + 4a^3b + 6a^2b^2\) \(+ 4ab^3 + 2b^4\) \(= 2(a^2 + ab + b^2)^2\).")),
       ("Value", p(r"\(\tfrac1{\sqrt2} \cdot \sqrt2\,(a^2 + ab + b^2)\) \(= (a + b)^2 - ab\)."))) + final("Option 2"),
 why_rows=[("1", "Sign of ab wrong."), ("3", "Not a perfect square."), ("4", "Not a perfect square.")])

P.qa(6, "Arjun, Bhaskar and Charan start a business. Arjun invests ₹1,20,000 for the whole year. Bhaskar joins 3 months after Arjun with ₹1,60,000, but withdraws half of it 3 months after joining. Charan joins 6 months after Arjun with ₹2,40,000 and increases his investment by 50% two months before the year ends. The year’s profit is ₹4,25,000. Find the difference between Bhaskar’s and Charan’s shares (in ₹).", [], "TITA", "75000", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "Capital × months for each.",
 steps(("Capital-months (₹ thousand)", p("Arjun 120 × 12 = 1440. Bhaskar 160 × 3 + 80 × 6 = 960. Charan 240 × 4 + 360 × 2 = 1680. Total 4080.")),
       ("Shares", p(r"Bhaskar \(\tfrac{960}{4080} \times 425000 = 100000\); Charan \(\tfrac{1680}{4080} \times 425000 = 175000\). Difference 75,000."))) + final("75000"))

P.qa(7, r"If \(\alpha\) and \(\beta\) are the roots of \(2x^2 + 3x + 4k = 0\), and \(\alpha\) and \(\theta\) are the roots of \(2x^2 - 3x + k = 0\), find \(\beta + \theta - k\), given that k is a non-zero real number.", ["−1", "0", "1", "5"], "MCQ", "2", ["Algebra::Quadratic_Equations"], "Medium",
 "Subtract the equations at the common root α.",
 steps(("α", p(r"\(6\alpha + 3k = 0\), so \(\alpha = -\tfrac k2\). In the second equation: \(\tfrac{k^2}2 + \tfrac{5k}2 = 0\), so \(k = -5\), \(\alpha = \tfrac52\).")),
       ("β and θ", p(r"\(\beta = -\tfrac32 - \tfrac52 = -4\); \(\theta = \tfrac32 - \tfrac52 = -1\). \(\beta + \theta - k = -5 + 5 = 0\)."))) + final("0, option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Forgets to subtract k.")])

P.qa(8, "Shops A and B sell identical products. Shop A sells at 12% above its marked price; Shop B gives a 20% discount on its marked price. The ratio of the two shops’ marked prices for any product is the same. Once, Shop B marked a product at ₹1,500 and Shop A sold the same product for ₹1,792. If Shop B sells another product for ₹2,880 after its usual discount, what is that item’s marked price at Shop A (in ₹)?", [], "TITA", "3840", ["Arithmetic::Profit_and_Loss"], "Easy",
 "Find the ratio of marked prices first.",
 steps(("Ratio", p(r"A’s marked price: \(1792 \div 1.12 = 1600\); ratio A : B = 1600 : 1500 = 16 : 15.")),
       ("New item", p(r"B’s marked price: \(2880 \div 0.8 = 3600\). A’s: \(3600 \times \tfrac{16}{15} = 3840\)."))) + final("3840"))

P.qa(9, "Akhilesh drives from home to office every day, leaving at a fixed time and arriving at a fixed time at a fixed speed. One day he drove 20% slower because of bad weather and reached at 10:17 AM. The next day he drove 25% faster than usual and reached at 9:50 AM. If he leaves the office at 6:00 PM and drives home at his usual speed on the same route, when will he reach home?",
 ["6:58 PM", "7:00 PM", "7:04 PM", "7:10 PM"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Time scales by 5/4 and 4/5.",
 steps(("Usual time", p(r"\(1.25t - 0.8t = 27\) minutes, so \(t = 60\).")),
       ("Home", p("6:00 PM + 60 minutes = 7:00 PM."))) + final("Option 2"),
 why_rows=[("1", "Wrong t."), ("3", "Wrong t."), ("4", "Wrong t.")])

P.qa(10, "How many numbers from 1001 to 10100 (inclusive) are divisible by 6 but not by 20?", [], "TITA", "1365", ["Number_System::Factors_and_Divisibility"], "Medium",
 "Divisible by both 6 and 20 means divisible by 60.",
 steps(("By 6", p(r"\(\lfloor 10100/6 \rfloor - \lfloor 1000/6 \rfloor\) \(= 1683 - 166 = 1517\).")),
       ("By 60", p(r"\(168 - 16 = 152\). Answer: 1517 − 152 = 1365."))) + final("1365"))

P.qa(11, r"How many integers satisfy \(x^2 + |3x| - 10 < 0\)?", ["0", "1", "2", "3"], "MCQ", "4", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "Write t = |x|: \\(t^2 + 3t - 10 < 0\\).",
 steps(("Solve", p(r"\((t + 5)(t - 2) < 0\) gives \(|x| < 2\): x = −1, 0, 1."))) + final("3, option 4"),
 why_rows=[("1", "Some integers work."), ("2", "Misses one."), ("3", "Misses one.")])

P.qa(12, "ABCDEFGH is a regular octagon with side 1 cm. What is the ratio of the area of quadrilateral CDGH to the area of the octagon?", ["1 : 3", "1 : 2", r"\(1 : 3\sqrt2\)", r"\(1 : 2\sqrt2\)"], "MCQ", "2", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "CD and GH are opposite sides: CDGH is a rectangle across the octagon.",
 steps(("Rectangle", p(r"Sides 1 and the octagon’s width \(1 + \sqrt2\): area \(1 + \sqrt2\).")),
       ("Octagon", p(r"Area \(2(1 + \sqrt2)\). Ratio 1 : 2."))) + final("Option 2"),
 why_rows=[("1", "Wrong octagon area."), ("3", "Wrong octagon area."), ("4", "Wrong octagon area.")])

P.qa(13, r"Find the value of \(\dfrac1x - \dfrac1y\), if \(18^x = 2^y = 729\).", ["1", r"\(\tfrac13\)", r"\(\tfrac12\)", r"\(\tfrac14\)"], "MCQ", "2", ["Algebra::Logarithms_and_Exponents"], "Easy",
 "\\(\\tfrac1x = \\log_{729}18\\), \\(\\tfrac1y = \\log_{729}2\\).",
 steps(("Subtract", p(r"\(\log_{729}\tfrac{18}2 = \log_{729}9 = \tfrac13\), since \(729 = 9^3\)."))) + final("Option 2"),
 why_rows=[("1", "Forgets the base."), ("3", "9 is 729^(1/3)."), ("4", "Arithmetic slip.")])

P.qa(14, F.TRI + p("In △ABC, BE bisects ∠DBC and AB = AE. If AB = 10 cm and EC = 5 cm, find the length (in cm) of AD."), [r"\(6\tfrac23\)", "10", r"\(8\tfrac13\)", "15"], "MCQ", "1", ["Geometry::Triangles"], "Hard",
 "AB = AE makes ∠ABE = ∠AEB; use the exterior angle at E.",
 steps(("Angles", p(r"∠AEB = ∠EBC + ∠C (exterior angle). ∠ABE = ∠ABD + ∠DBE, and ∠DBE = ∠EBC. So ∠ABD = ∠C.")),
       ("Similar triangles", p(r"△ABD ~ △ACB, so \(AB^2 = AD \times AC\): \(100 = AD \times 15\), \(AD = \tfrac{20}3\)."))) + final("Option 1"),
 why_rows=[("2", "AE, not AD."), ("3", "Arithmetic slip."), ("4", "AC.")])

P.qa(15, "A milkman adds x litres of water to 100 litres of milk and sells the mixture at the cost price of milk, making a 25% profit. Later he adds more water, so that the water-to-milk ratio becomes 3 : 5, keeping the price unchanged. By how many percentage points has his profit increased?", ["24", "29", "35", "39"], "MCQ", "3", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Profit % = water ÷ milk.",
 steps(("First", p("25% means x = 25.")), ("Second", p("3 : 5 means 60% profit. Increase: 35 points."))) + final("35, option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(16, "Three natural numbers satisfy a < b < c. First, one-fourth of the smallest number is added to each of the three numbers. Then the first new number is decreased by one-fifth of its value, the second by one-fourth, and the third by one-third. The final values are in the ratio 2 : 3 : 4. If b = 35, find a + c.", [], "TITA", "75", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "The first final value is \\(\\tfrac45 \\cdot \\tfrac{5a}4 = a\\).",
 steps(("a", p(r"Final values \(a,\ \tfrac34\left(35 + \tfrac a4\right),\ \tfrac23\left(c + \tfrac a4\right)\) = 2k, 3k, 4k. So \(a = 2k\) and \(35 + \tfrac a4 = 4k = 2a\): \(a = 20, k = 10\).")),
       ("c", p(r"\(\tfrac23(c + 5) = 40\), so \(c = 55\). a + c = 75."))) + final("75"))

P.qa(17, "A sequence S consists of all natural numbers up to 500 that are neither perfect squares nor perfect cubes. What is the sum of all the numbers in S?", [], "TITA", "120736", ["Number_System::Miscellaneous"], "Medium",
 "Subtract squares and cubes, add back numbers that are both.",
 steps(("Pieces", p(r"1 to 500: 125250. Squares \(1^2 \dots 22^2\): 3795. Cubes \(1^3 \dots 7^3\): 784. Both (1 and 64): 65.")),
       ("Sum", p("125250 − 3795 − 784 + 65 = 120736."))) + final("120736"))

P.qa(18, "In a store, the average cost of 24 stationery items is ₹44. Exactly 16 of these items cost no more than ₹45 each. If every item costs a whole number of rupees, what is the maximum possible average cost of these 16 items (in ₹)?", [], "TITA", "43", ["Arithmetic::Average"], "Medium",
 "The other 8 cost at least ₹46 each.",
 steps(("Total", p(r"\(24 \times 44 = 1056\). The 8 dearer items cost at least \(8 \times 46 = 368\).")),
       ("The 16", p(r"At most \(1056 - 368 = 688\): average 43."))) + final("43"))

P.qa(19, r"Find the area (in square units) of the closed region bounded by \(|x| + |y| = 5\sqrt2\).", [], "TITA", "100", ["Geometry::Coordinate_Geometry"], "Easy",
 "A square with diagonals along the axes.",
 steps(("Area", p(r"Diagonals \(10\sqrt2\) each: area \(\tfrac12 \times 10\sqrt2 \times 10\sqrt2 = 100\)."))) + final("100"))

P.qa(20, r"Let \(X = \{x : x \in \mathbb N,\ x^2 - 8x + 12 < 0\}\) and \(Y = \{y : y \in \mathbb Z,\ 15y^2 - 46y - 33 < 0\}\). How many of these statements are true?<br>I. The average of the numbers of elements in the two sets is more than 3.<br>II. The two sets are distinct.<br>III. The sum of all the elements of the two sets is 18.<br>IV. The product of all the elements of the sets is 360.", ["1", "2", "3", "4"], "MCQ", "3", ["Modern_Maths::Set_Theory"], "Medium",
 "Solve both inequalities.",
 steps(("Sets", p(r"\((x - 2)(x - 6) < 0\): X = {3, 4, 5}. \((5y + 3)(3y - 11) < 0\): \(-0.6 < y < 3.67\), Y = {0, 1, 2, 3}.")),
       ("Statements", p("I: (3 + 4)/2 = 3.5, true. II: true. III: 12 + 6 = 18, true. IV: Y contains 0, so the product is 0, false."))) + final("3, option 3"),
 why_rows=[("1", "More are true."), ("2", "More are true."), ("4", "IV fails because of 0.")])

P.qa(21, r"Find the value of x if the arithmetic mean of two distinct positive real numbers a and b is \(\dfrac{a^{x^2 + 2x + 1} + b^{x^2 + 2x + 1}}{a^{x^2 + 2x} + b^{x^2 + 2x}}\).", ["−2", "−1", "0", "More than one of the above"], "MCQ", "4", ["Algebra::Equations_and_Polynomials"], "Medium",
 "With n = x² + 2x, \\(\\dfrac{a^{n+1} + b^{n+1}}{a^n + b^n} = \\dfrac{a + b}2\\) only when n = 0.",
 steps(("n = 0", p(r"Then the fraction is \(\tfrac{a + b}2\). (For a ≠ b, other n give a different mean.)")),
       ("x", p(r"\(x^2 + 2x = 0\): x = 0 or −2. Both are listed."))) + final("Option 4"),
 why_rows=[("1", "One of two values."), ("2", "Gives n = −1: the harmonic-type mean."), ("3", "One of two values.")])

P.qa(22, r"Which of the following equals \(\dfrac{4 + m}{4 - m}\), given that \(\log_{15}625 = m\)? (log means log to base 10.)",
 [r"\(\dfrac{1 + \log 3 - \log 4}{\log 3}\)", r"\(\dfrac{1 + \log 3 - \log 2}{\log 3}\)", r"\(\dfrac{2 + \log 3 - \log 4}{\log 3}\)", r"\(\dfrac{2 + \log 3 - \log 2}{\log 3}\)"], "MCQ", "3", ["Algebra::Logarithms_and_Exponents"], "Hard",
 "m = 4 log₁₅5, so divide through by 4.",
 steps(("Simplify", p(r"\(\dfrac{1 + \log_{15}5}{1 - \log_{15}5} = \dfrac{\log_{15}75}{\log_{15}3}\) \(= \dfrac{\log 75}{\log 3}\).")),
       ("Base 10", p(r"\(\log 75 = \log 3 + 2\log 5\) \(= \log 3 + 2 - 2\log 2\) \(= 2 + \log 3 - \log 4\)."))) + final("Option 3"),
 why_rows=[("1", r"Uses \(\log 5 = 1 - \log 2\) only once."), ("2", "Same slip."), ("4", r"\(2\log 2 = \log 4\), not \(\log 2\).")])
