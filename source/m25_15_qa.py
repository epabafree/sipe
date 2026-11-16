# -*- coding: utf-8 -*-
# Simp Mock 15 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_15 import P
import m25_15_figs as F

P.qa(1, "Two toy cars, A and B, start together from the same point in the same direction and reach a point 150 m away at the same time. Car A starts at 10 m per minute and doubles its speed every 30 seconds; car B moves at a steady speed throughout. If car B covers D metres non-stop in T minutes at that speed, with D and T natural numbers, what is the least possible D?", [], "TITA", "4800", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Find car A’s exact time.",
 steps(("Car A", p("Half-minute stretches: 5 + 10 + 20 + 40 = 75 m in 2 minutes. The last 75 m at 160 m/min take 15/32 min: total 79/32 min.")),
       ("Car B", p(r"Speed \(150 \div \tfrac{79}{32} = \tfrac{4800}{79}\) m/min, so \(T = \tfrac{79D}{4800}\).")),
       ("Least D", p("79 and 4800 share no factor, so D must be a multiple of 4800."))) + final("4800"))

P.qa(2, "Anish can finish a job alone in 18 days. He works for n days (n a natural number) and leaves, and Biren finishes the rest; the job takes 21 days in all. Anish is 20% more efficient than Biren. Find n.", ["6", "5", "4", "3"], "MCQ", "4", ["Arithmetic::Time_and_Work"], "Easy",
 "Rates 12 and 10 units a day.",
 steps(("Equation", p("12 × 18 = 12n + 10(21 − n), so 2n = 6.")), ("n", p("3."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(3, "From 1 April 2025, Anil writes one page a day for five days. From 6 April he writes 20% more each day for the next five days, from 11 April another 20% more, and so on, raising his daily output by 20% every five days. Roughly how many pages does he write in April?", ["49.65 pages", "53.75 pages", "61.67 pages", "68.45 pages"], "MCQ", "1", ["Algebra::Progressions_and_Series"], "Easy",
 "Six five-day blocks: 5, 6, 7.2, … a GP.",
 steps(("Sum", p(r"\(5 \cdot \tfrac{1.2^6 - 1}{0.2} = 25(2.985984 - 1) \approx 49.65\)."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Seven blocks."), ("4", "Arithmetic slip.")])

P.qa(4, "In the figure (not to scale), AB ⊥ BC and AD ⊥ CD, and AD and BC meet at O. AO = CO = 2x cm and DO = x cm. Find the area of quadrilateral ABDC (in sq. cm)." + F.ORTH,
 [r"\(\tfrac{9\sqrt3}{2}x^2\)", r"\(\tfrac{9\sqrt3}{4}x^2\)", r"\(4\sqrt3x^2\)", r"\(\tfrac{4\sqrt3}{9}x^2\)"], "MCQ", "2", ["Geometry::Triangles"], "Hard",
 "Extend AB and CD to meet at P; O is the orthocentre of △ACP.",
 steps(("Congruent", p("△ABO and △CDO have equal right angles, equal vertical angles and AO = CO, so BO = DO = x.")),
       ("Equilateral", p("O divides the altitudes AD and CB in the ratio 2 : 1, so it is also the centroid: △ACP is equilateral, with B and D the midpoints of AP and CP.")),
       ("Area", p(r"Circumradius AO = 2x gives side \(2\sqrt3x\) and area \(3\sqrt3x^2\). ABDC is △ACP minus the corner △PBD (a quarter): \(\tfrac34 \cdot 3\sqrt3x^2 = \tfrac{9\sqrt3}{4}x^2\)."))) + final("Option 2"),
 why_rows=[("1", "Double."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(5, "In the figure (not to scale), PQ is a chord of length 204 cm, RS = 35 cm and RS ⊥ PQ, with R on the circle. Find the diameter of the circle (in cm)." + F.CHORD, [], "TITA", "325", ["Geometry::Circles"], "Medium",
 "In △PRQ, product of two sides = diameter × altitude.",
 steps(("Sides", p(r"PS = 84, SQ = 120. \(PR = \sqrt{84^2 + 35^2} = 91\), \(QR = \sqrt{120^2 + 35^2} = 125\).")),
       ("Diameter", p(r"Draw diameter RT. △RPS ∼ △RTQ (right angles, and ∠RPQ = ∠RTQ on the same arc), so \(RT = \tfrac{PR \cdot QR}{RS} = \tfrac{91 \times 125}{35} = 325\)."))) + final("325"))

P.qa(6, r"A trader buys two varieties of coconut oil, paying 20% more per litre for the costlier one; he buys 20% more litres of the cheaper one. He first sells 10 litres of the costlier and 20 litres of the cheaper, both at a 20% markup. He then mixes what is left and sells all of it at a \(9\tfrac1{11}\%\) markup. His overall profit is 12%. How many litres did he buy in all?", ["88", "99", "110", "132"], "MCQ", "3", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Prices ₹6 and ₹5 a litre; volumes 5V and 6V.",
 steps(("Cost", p("30V + 30V = 60V. First sales: (60 + 100) × 1.2 = 192.")),
       ("Equation", p(r"\(192 + (60V - 160) \cdot \tfrac{12}{11} = 1.12 \times 60V\). Times 11: 2112 + 720V − 1920 = 739.2V, so V = 10.")),
       ("Total", p("11V = 110."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(7, "a, b and c are non-zero digits of the three-digit number abc, and 49a + 7b + c = 224. Find abc.", [], "TITA", "437", ["Number_System::Miscellaneous"], "Easy",
 "Bound a first; the rest is small.",
 steps(("a", p("49 × 5 = 245 > 224, so a ≤ 4. With a ≤ 3, 7b + c would be at least 77, more than 7 × 9 + 9 = 72. So a = 4.")),
       ("b and c", p("7b + c = 28, so c is a multiple of 7: c = 7, b = 3."))) + final("437"))

P.qa(8, "m and n are integers with 5m + 3 = 3n + 7 and 50 < 4m + 6 ≤ 64. Which of these can be the value of mn + m + n?", ["254", "299", "307", "344"], "MCQ", "4", ["Algebra::Linear_Equations"], "Easy",
 "m is 12, 13 or 14; 5m − 4 must be a multiple of 3.",
 steps(("m", p("Only m = 14 works: n = 22.")), ("Value", p("308 + 36 = 344."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "mn alone is 308.")])

P.qa(9, r"If \(f(x) = x^2(1 - x)^2\) for real x, find \(f\big(\tfrac{1}{499}\big) - f\big(\tfrac{2}{499}\big)\) \(+ f\big(\tfrac{3}{499}\big) - f\big(\tfrac{4}{499}\big) + \dots\) \(+ f\big(\tfrac{497}{499}\big) - f\big(\tfrac{498}{499}\big)\).", ["250", "498", "0", "1"], "MCQ", "3", ["Algebra::Functions"], "Easy",
 "f(x) = f(1 − x).",
 steps(("Pairs", p(r"\(f\big(\tfrac{k}{499}\big)\) \(= f\big(\tfrac{499 - k}{499}\big)\), and k and 499 − k have opposite parity, so they carry opposite signs and cancel.")), ("Sum", p("0."))) + final("Option 3"),
 why_rows=[("1", "Counts pairs."), ("2", "Counts terms."), ("4", "Arithmetic slip.")])

P.qa(10, r"If \(a + b = \sqrt{3\sqrt5 - \sqrt2}\) and \(a - b = \sqrt{3\sqrt2 - \sqrt5}\), what is ab?", [r"\(\sqrt5 + \sqrt2\)", r"\(\sqrt5 - \sqrt2\)", r"\(\sqrt3 - \sqrt2\)", r"\(\sqrt5 - \sqrt3\)"], "MCQ", "2", ["Algebra::Surds_and_Indices"], "Easy",
 r"\(4ab = (a + b)^2 - (a - b)^2\).",
 steps(("Value", p(r"\(\tfrac14[(3\sqrt5 - \sqrt2) - (3\sqrt2 - \sqrt5)]\) \(= \tfrac14(4\sqrt5 - 4\sqrt2) = \sqrt5 - \sqrt2\)."))) + final("Option 2"),
 why_rows=[("1", "Sign slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(11, r"\(m^4 + 4n^4\) is prime. How many ordered pairs (m, n) of positive integers are there?", [], "TITA", "1", ["Number_System::Factors_and_Divisibility"], "Medium",
 "Sophie Germain’s identity.",
 steps(("Factor", p(r"\(m^4 + 4n^4\) \(= [(m + n)^2 + n^2]\) \(\times [(m - n)^2 + n^2]\).")),
       ("Prime", p(r"The smaller factor must be 1: \((m - n)^2 + n^2 = 1\) gives n = 1, m = 1 (value 5)."))) + final("1"))

P.qa(12, r"Find the term free of x in the expansion of \(\left(x^2 + \tfrac{1}{x^3}\right)^{10}\).", [], "TITA", "210", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 r"General term \(\binom{10}{r}x^{20 - 5r}\).",
 steps(("r", p("20 − 5r = 0 gives r = 4.")), ("Term", p(r"\(\binom{10}{4} = 210\)."))) + final("210"))

P.qa(13, r"If \(0° < A \le 90°\), what is the minimum value of \(\left(\dfrac{\sin^2 A + 10\sin A + 1}{\sin A}\right)^2\)?", ["100", "144", "81", r"\(50\sqrt2\)"], "MCQ", "2", ["Geometry::Trigonometry"], "Easy",
 "Split the fraction.",
 steps(("Rewrite", p(r"\(\left(\sin A + \tfrac{1}{\sin A} + 10\right)^2\).")),
       ("Minimum", p(r"\(\sin A + \tfrac1{\sin A} \ge 2\), with equality at A = 90°: \(12^2 = 144\)."))) + final("Option 2"),
 why_rows=[("1", "Drops the 2."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(14, "Pravin invests ₹10 crore at r% a year, compounded annually. The second year’s interest exceeds the first year’s by ₹6,40,000, and the third year’s exceeds the second’s by ₹6,91,200. By how much (in ₹) does the fourth year’s interest exceed the third’s?", [], "TITA", "746496", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Successive differences grow by the factor (1 + r).",
 steps(("Rate", p("691200 ÷ 640000 = 1.08.")), ("Next", p("691200 × 1.08 = 7,46,496."))) + final("746496"))

P.qa(15, "Alex, Ben and Charlie walk at speeds in the ratio 1 : 2 : 3. On a moving up-escalator, Alex takes 40 steps and Ben 60 steps to reach the top. How many steps does Charlie take?", ["80", "72", "90", "Cannot be determined"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Steps on the escalator = time × (walker’s speed + escalator’s speed).",
 steps(("Escalator", p("40(e + 1) = 30(e + 2) gives e = 2; 120 steps.")), ("Charlie", p("120 ÷ 5 = 24 seconds, taking 3 steps a second: 72."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Ignores the escalator."), ("4", "The data suffice.")])

P.qa(16, "The average of 100 three-digit numbers is 108. What is the largest possible value among them?", [], "TITA", "900", ["Arithmetic::Average"], "Easy",
 "Make the other 99 as small as possible.", steps(("Largest", p("10800 − 99 × 100 = 900."))) + final("900"))

P.qa(17, "The product of two positive numbers is 432. The difference of their cubes divided by the cube of their difference is 37. What is their sum?", ["27", "36", "42", "45"], "MCQ", "3", ["Algebra::Equations_and_Polynomials"], "Medium",
 r"\(a^3 - b^3 = (a - b)^3 + 3ab(a - b)\).",
 steps(("Difference", p(r"\(1 + \tfrac{3ab}{(a - b)^2} = 37\), so \((a - b)^2 = \tfrac{3 \times 432}{36} = 36\).")),
       ("Sum", p(r"\((a + b)^2 = 36 + 1728 = 1764\): 42 (24 and 18)."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(18, "Team A of six students is picked from b boys and 7 girls and has exactly 4 boys; it can be picked in 315 ways. The rest form Team B. On Monday each boy of Team A plays each girl of Team B, and on Tuesday each girl of Team A plays each boy of Team B. What is the ratio of Monday’s matches to Tuesday’s?", ["4 : 1", "5 : 1", "5 : 4", "1 : 5"], "MCQ", "2", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 r"\(\binom b4 \times \binom72 = 315\).",
 steps(("b", p(r"\(\binom b4 = 15\), so b = 6. Team A: 4 boys, 2 girls; Team B: 2 boys, 5 girls.")), ("Ratio", p("4 × 5 : 2 × 2 = 20 : 4 = 5 : 1."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Reversed.")])

P.qa(19, "PQS is isosceles with PQ = PS. R is on QS and T on PS with PR = PT. If ∠QPR = 40°, find ∠TRS." + F.ISO, ["40°", "10°", "20°", "30°"], "MCQ", "3", ["Geometry::Triangles"], "Easy",
 "Let ∠Q = ∠S = x, ∠PRT = ∠PTR = y, ∠TRS = z.",
 steps(("Exterior angles", p("At R in △PQR: x + 40 = y + z. At T in △TRS: y = x + z.")), ("Solve", p("x + 40 = x + 2z, so z = 20°."))) + final("Option 3"),
 why_rows=[("1", "∠QPR itself."), ("2", "Quarter of it."), ("4", "Arithmetic slip.")])

P.qa(20, "A rectangle has length ℓ and breadth b. Cutting a square of side b from it leaves a smaller rectangle with the same length-to-breadth ratio as the original. What is ℓ : b?", [r"\((1 + \sqrt5) : 1\)", r"\((1 + \sqrt5) : 2\)", r"\((1 + \sqrt3) : 1\)", r"\((1 + \sqrt3) : 2\)"], "MCQ", "2", ["Geometry::Mensuration"], "Easy",
 r"\(\tfrac{\ell}{b} = \tfrac{b}{\ell - b}\).",
 steps(("Equation", p(r"\(\ell^2 - \ell b - b^2 = 0\), so \(\tfrac{\ell}{b} = \tfrac{1 + \sqrt5}{2}\), the golden ratio."))) + final("Option 2"),
 why_rows=[("1", "Forgets to halve."), ("3", "Wrong discriminant."), ("4", "Wrong discriminant.")])

P.qa(21, "A company has departments X and Y, each with supervisors and workers. Both have the same number of workers, Y has 25% more employees than X, and supervisors in X and Y are in the ratio 2 : 7. What percentage of all employees in the two departments are supervisors?", ["20%", r"\(16\tfrac23\%\)", "25%", r"\(28\tfrac47\%\)"], "MCQ", "1", ["Arithmetic::Percentages"], "Easy",
 "Supervisors 2a and 7a, workers b each.",
 steps(("Equation", p("7a + b = 1.25(2a + b), so b = 18a.")), ("Share", p("9a out of 9a + 36a = 45a: 20%."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(22, "A, B and C share a business’s first-year profit in the ratio 3 : 2 : 9, having invested in the ratio 2 : 1 : 4. Each invested for a whole number of months; the business started on the first day of the year, and every month had at least one partner’s money in it. A partner who withdrew did not reinvest that year. What is the least number of months in which all three had money in the business at the same time?", ["0", "1", "2", "More than 2"], "MCQ", "3", ["Arithmetic::Ratio_and_Proportion"], "Hard",
 "First find the months: 2a : b : 4c = 3 : 2 : 9.",
 steps(("Months", p("a : b : c = 6 : 8 : 9 (the only fit within 12 months).")),
       ("Overlap", p("A and C together need 15 months, so overlap at least 3; B’s 8 months must cover any month the others leave empty. Example: A months 1–6, C months 4–12, B months 5–12: all three in months 5 and 6.")),
       ("Can’t be fewer", p("Checking every placement of the three blocks, the triple overlap never drops below 2."))) + final("Option 3"),
 why_rows=[("1", "Impossible with 23 investor-months in 12."), ("2", "One overlap month is not enough."), ("4", "2 is achievable.")])
