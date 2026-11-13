# -*- coding: utf-8 -*-
# Batch 21 — CAT 2025 Slot 2: QA Q1–22 (exam order).
from fmt import steps, final, trap, why, table, p
from b21_25s2 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"The equations \(3x^2 - 5x + p = 0\) and \(2x^2 - 2x + q = 0\) have one common root. The sum of the other roots of these two equations is",
 M(r"\tfrac83 + p + \tfrac13 q", r"\tfrac23 - 2p + \tfrac23 q", r"\tfrac83 - p + \tfrac32 q", r"\tfrac23 - p + \tfrac32 q"), "MCQ", "3", ["Algebra::Quadratic_Equations"], "Medium",
 "Write the other roots as (sum of roots) − (common root). Then find the common root from the two equations.",
 steps(("The other roots", p(r"If the common root is \(\alpha\), the other roots are \(\frac53 - \alpha\) and \(1 - \alpha\), adding to \(\frac83 - 2\alpha\).")),
       ("The common root", p(r"Double the first equation and triple the second at \(\alpha\): \(6\alpha^2 - 10\alpha + 2p = 0\) and \(6\alpha^2 - 6\alpha + 3q = 0\). Subtracting, \(4\alpha = 2p - 3q\), so \(2\alpha = p - \frac32 q\).")),
       ("Sum", p(r"\(\frac83 - p + \frac32 q\)."))) + final("Option 3"),
 concept=r"\[\alpha + \beta = -\frac{b}{a}\]",
 why_rows=[("1", "Signs and coefficients of p and q are wrong."), ("2", "The constant should be 8/3, the sum of 5/3 and 1."), ("4", "The constant should be 8/3.")])

P.qa(2, "Let ABCDEF be a regular hexagon and P and Q be the midpoints of AB and CD, respectively. Then, the ratio of the areas of trapezium PBCQ and hexagon ABCDEF is",
 M("6 : 19", "5 : 24", "7 : 24", "6 : 25"), "MCQ", "2", ["Geometry::Polygons_and_Quadrilaterals"], "Hard",
 "Join P and Q. PQ is parallel to BC; find its length and the height between them.",
 steps(
       ("PQ", p(r"Take side \(s\). P and Q are midpoints of AB and CD, and AD is parallel to BC with \(AD = 2s\). The trapezium ABCD has parallel sides \(s\) and \(2s\); P and Q are midpoints of its legs, so \(PQ = \frac{s + 2s}{2} = \frac32 s\), and PQ sits halfway between BC and AD.")),
       ("Areas", p(r"Trapezium ABCD is half the hexagon, with height \(h\). PBCQ has parallel sides \(s\) and \(\frac32 s\) and height \(\frac h2\): area \(\frac{2.5s}{2} \cdot \frac h2 = \frac{5}{8}sh\). ABCD has area \(\frac{3s}{2}h\). So PBCQ is \(\frac{5/8}{3/2} = \frac{5}{12}\) of half the hexagon, that is \(\frac{5}{24}\) of the whole."))) + final(r"\(5 : 24\), option 2"),
 concept=r"\[\text{midline of a trapezium} = \frac{\text{sum of the parallel sides}}{2}\]",
 why_rows=[("1", "This doesn’t come from the midline split."), ("3", "This would make PQ longer than 1.5s."), ("4", "This doesn’t come from the midline split.")])

P.qa(3, r"If \(\log_{64} x^2 + \log_8 \sqrt y + 3\log_{512}\left(\sqrt y\, z\right) = 4\), where \(x, y\) and \(z\) are positive real numbers, then the minimum possible value of \((x + y + z)\) is",
 M("96", "36", "24", "48"), "MCQ", "4", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Turn every log into base 2.",
 steps(("Base 2", p(r"\(\log_{64} x^2 = \frac13 \log_2 x\), \(\log_8 \sqrt y = \frac16 \log_2 y\), and \(3\log_{512}(\sqrt y\, z) = \frac13\left(\frac12 \log_2 y + \log_2 z\right)\).")),
       ("Combine", p(r"The sum is \(\frac13(\log_2 x + \log_2 y + \log_2 z) = 4\), so \(xyz = 2^{12}\).")),
       ("Minimum", p(r"By AM–GM, \(x + y + z \ge 3\sqrt[3]{2^{12}} = 3 \times 16 = 48\), with \(x = y = z = 16\)."))) + final(r"\(48\), option 4"),
 concept=r"\[\frac{x + y + z}{3} \ge \sqrt[3]{xyz}\]",
 why_rows=[("1", "This doubles the minimum."), ("2", "This is below the AM–GM bound."), ("3", "This uses a cube root of 2⁹.")])

P.qa(4, r"The set of all real values of \(x\) for which \(x^2 - |x + 9| + x > 0\), is",
 [r"\((-\infty, -3) \cup (3, \infty)\)", r"\((-9, -3) \cup (3, \infty)\)", r"\((-\infty, -9) \cup (9, \infty)\)", r"\((-\infty, -9) \cup (3, \infty)\)"], "MCQ", "1", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Split at x = −9.",
 steps(("x ≥ −9", p(r"\(x^2 - x - 9 + x = x^2 - 9 > 0\): \(x < -3\) or \(x > 3\). With \(x \ge -9\): \([-9, -3) \cup (3, \infty)\).")),
       ("x < −9", p(r"\(x^2 + x + 9 + x = x^2 + 2x + 9\) \(= (x + 1)^2 + 8 > 0\) always. So all \(x < -9\) work.")),
       ("Together", p(r"\((-\infty, -3) \cup (3, \infty)\)."))) + final("Option 1"),
 concept=r"\[|t| = t \text{ for } t \ge 0, \; -t \text{ for } t < 0\]",
 why_rows=[("2", "This forgets that every x below −9 also works."), ("3", "Values between 3 and 9 also work."), ("4", "Values between −9 and −3 also work.")])

P.qa(5, "A certain amount of money was divided among Pinu, Meena, Rinu and Seema. Pinu received 20% of the total amount and Meena received 40% of the remaining amount. If Seema received 20% less than Pinu, the ratio of the amounts received by Pinu and Rinu is",
 M("2 : 1", "5 : 8", "1 : 2", "8 : 5"), "MCQ", "2", ["Arithmetic::Percentages"], "Easy",
 "Take the total as 100.",
 steps(p(r"Pinu 20, Meena \(0.4 \times 80 = 32\), Seema \(0.8 \times 20 = 16\), Rinu \(100 - 68 = 32\). Pinu : Rinu \(= 20 : 32 = 5 : 8\).")) + final(r"\(5 : 8\), option 2"),
 concept=r"\[\text{take the total as 100}\]",
 why_rows=[("1", "Rinu gets more than Pinu."), ("3", "Rinu gets 32, not 40."), ("4", "This is Rinu : Pinu.")])

P.qa(6, "Ankita is twice as efficient as Bipin, while Bipin is twice as efficient as Chandan. All three of them start together on a job, and Bipin leaves the job after 20 days. If the job got completed in 60 days, the number of days needed by Chandan to complete the job alone, is",
 [], "TITA", "340", ["Arithmetic::Time_and_Work"], "Easy",
 "Give Chandan 1 unit a day; Bipin 2 and Ankita 4.",
 steps(p(r"Work done: \(2 \times 20 + (4 + 1) \times 60 = 340\) units. Chandan alone does 1 a day, so 340 days.")) + final(r"\(340\)"),
 concept=r"\[\text{work} = \text{rate} \times \text{days}\]")

P.qa(7, r"Let \(a_n\) be the \(n\)th term of a decreasing infinite geometric progression. If \(a_1 + a_2 + a_3 = 52\) and \(a_1a_2 + a_2a_3 + a_3a_1 = 624\), then the sum of this geometric progression is",
 M("54", "60", "57", "63"), "MCQ", "1", ["Algebra::Progressions_and_Series"], "Medium",
 r"With terms \(a, ar, ar^2\), the second sum is \(ar \times (a + ar + ar^2)\).",
 steps(("Middle term", p(r"\(a^2r + a^2r^2 + a^2r^3\) \(= ar(a + ar + ar^2)\) \(= 52\,ar = 624\), so \(ar = 12\).")),
       ("The ratio", p(r"\(\frac{12}{r} + 12 + 12r = 52\) gives \(3r^2 - 10r + 3 = 0\), so \(r = \frac13\) (decreasing). Then \(a = 36\).")),
       ("Sum", p(r"\(\frac{36}{1 - \frac13} = 54\)."))) + final(r"\(54\), option 1"),
 concept=r"\[S_\infty = \frac{a}{1 - r}\]",
 why_rows=[("2", "This doesn’t match a = 36, r = 1/3."), ("3", "This doesn’t match a = 36, r = 1/3."), ("4", "This doesn’t match a = 36, r = 1/3.")])

P.qa(8, r"Let \(f(x) = \frac{x}{2x - 1}\) and \(g(x) = \frac{x}{x - 1}\). Then, the domain of the function \(h(x) = f(g(x)) + g(f(x))\) is all real numbers except",
 [r"\(\frac12, 1\) and \(\frac32\)", r"\(-\frac12, \frac12\) and \(1\)", r"\(-1, \frac12\) and \(1\)", r"\(\frac12\) and \(1\)"], "MCQ", "3", ["Algebra::Functions"], "Medium",
 "Exclude where f or g is undefined, and where the inner value hits the outer function’s bad point.",
 steps(("Direct", p(r"f needs \(x \ne \frac12\); g needs \(x \ne 1\).")),
       ("f(g(x))", p(r"Need \(g(x) \ne \frac12\): \(\frac{x}{x - 1} = \frac12\) gives \(x = -1\).")),
       ("g(f(x))", p(r"Need \(f(x) \ne 1\): \(\frac{x}{2x - 1} = 1\) gives \(x = 1\), already excluded."))) + final(r"\(-1, \frac12, 1\), option 3"),
 concept=r"\[\text{domain of } f(g(x)) = \{x : x \in \text{dom } g,\ g(x) \in \text{dom } f\}\]",
 why_rows=[("1", "3/2 is fine."), ("2", "−1/2 is fine; −1 is the excluded value."), ("4", "This misses x = −1, where g(x) = 1/2.")])

P.qa(9, "A loan of Rs 1000 is fully repaid by two installments of Rs 530 and Rs 594, paid at the end of first and second year, respectively. If the interest is compounded annually, then the rate of interest, in percentage, is",
 M("8", "9", "10", "11"), "MCQ", "1", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Test the options: after a year, pay 530; the rest must grow to 594.",
 steps(p(r"At 8%: \(1080 - 530 = 550\), and \(550 \times 1.08 = 594\). It works.")) + final(r"\(8\%\), option 1"),
 concept=r"\[\text{balance} = (\text{previous} \times (1 + r)) - \text{payment}\]",
 why_rows=[("2", r"\(1090 - 530 = 560\), \(560 \times 1.09 = 610.4\)."), ("3", r"\(570 \times 1.1 = 627\)."), ("4", r"\(580 \times 1.11 = 643.8\).")])

P.qa(10, r"Two tangents drawn from a point P touch a circle with center O at points Q and R. Points A and B lie on PQ and PR, respectively, such that AB is also a tangent to the same circle. If \(\angle AOB = 50^\circ\), then \(\angle APB\), in degrees, equals",
 [], "TITA", "80", ["Geometry::Circles"], "Medium",
 "OA and OB bisect the angles at A and B of the quadrilateral formed with the tangent points.",
 steps(p(r"For a triangle cut off by a third tangent, \(\angle AOB = 90^\circ - \frac12 \angle APB\). So \(50 = 90 - \frac12\angle APB\), giving \(\angle APB = 80^\circ\).")) + final(r"\(80\)"),
 concept=r"\[\angle AOB = 90^\circ - \tfrac12 \angle P\]")

P.qa(11, "A mixture of coffee and cocoa, 16% of which is coffee, costs Rs 240 per kg. Another mixture of coffee and cocoa, of which 36% is coffee, costs Rs 320 per kg. If a new mixture of coffee and cocoa costs Rs 376 per kg, then the quantity, in kg, of coffee in 10 kg of this new mixture is",
 M("6", "2.5", "4", "5"), "MCQ", "4", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Each 20% more coffee adds Rs 80 per kg.",
 steps(("Prices", p(r"Going from 16% to 36% coffee adds 80, so each 1% of coffee adds Rs 4. Pure cocoa: \(240 - 64 = 176\); pure coffee: \(176 + 400 = 576\).")),
       ("New mixture", p(r"\(376 - 176 = 200\), which is 50% coffee. In 10 kg, that is 5 kg."))) + final(r"\(5\), option 4"),
 concept=r"\[\text{price} = \text{coffee share} \times c + \text{cocoa share} \times k\]",
 why_rows=[("1", "This would cost 416 a kg."), ("2", "This would cost 276 a kg."), ("3", "This would cost 336 a kg.")])

P.qa(12, r"If \(a, b, c\) and \(d\) are integers such that their sum is 46, then the minimum possible value of \((a - b)^2 + (a - c)^2 + (a - d)^2\) is",
 [], "TITA", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Keep all four close to 46 ÷ 4 = 11.5.",
 steps(p(r"All four can’t be equal (46 isn’t a multiple of 4), and the sum of the three differences is \(46 - 4a\), which is never 0. With \(a = 11\): \(b + c + d = 35\), e.g. 11, 12, 12, giving \(0 + 1 + 1 = 2\). With \(a = 12\): \(b + c + d = 34\), e.g. 11, 11, 12, also 2. A total of 1 would need two differences of 0, forcing \(46 - 4a = \pm 1\), impossible.")) + final(r"\(2\)"),
 concept=r"\[\text{squares are smallest when the numbers are as equal as possible}\]")

P.qa(13, "The average number of copies of a book sold per day by a shopkeeper is 60 in the initial seven days and 63 in the initial eight days, after the book launch. On the ninth day, she sells 11 copies less than the eighth day, and the average number of copies sold per day from second day to ninth day becomes 66. The number of copies sold on the first day of the book launch is",
 [], "TITA", "49", ["Arithmetic::Average"], "Easy",
 "Use totals.",
 steps(p(r"First 7 days: 420. First 8: 504, so day 8 is 84 and day 9 is 73. Days 1–9: 577. Days 2–9: \(8 \times 66 = 528\). Day 1: \(577 - 528 = 49\).")) + final(r"\(49\)"),
 concept=r"\[\text{total} = \text{average} \times \text{count}\]")

P.qa(14, r"If \(9^{x^2 + 2x - 3} - 4\left(3^{x^2 + 2x - 2}\right) + 27 = 0\), then the product of all possible values of \(x\) is",
 M("15", "20", "5", "30"), "MCQ", "2", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"Let \(y = 3^{x^2 + 2x - 2}\). Then the first term is \(\frac{y^2}{9}\).",
 steps(("Quadratic in y", p(r"\(\frac{y^2}{9} - 4y + 27 = 0\), so \(y^2 - 36y + 243 = 0\): \(y = 27\) or \(9\).")),
       ("Back to x", p(r"\(x^2 + 2x - 2 = 3\) gives \(x^2 + 2x - 5 = 0\) (product −5). \(x^2 + 2x - 2 = 2\) gives \(x^2 + 2x - 4 = 0\) (product −4). All four roots are real and distinct.")),
       ("Product", p(r"\((-5)(-4) = 20\)."))) + final(r"\(20\), option 2"),
 concept=r"\[a^{2m} = (a^m)^2\]",
 why_rows=[("1", "This multiplies the wrong products."), ("3", "This uses only one of the two quadratics."), ("4", "This doesn’t match −5 × −4.")])

P.qa(15, r"Suppose \(a, b, c\) are three distinct natural numbers, such that \(3ac = 8(a + b)\). Then, the smallest possible value of \(3a + 2b + c\) is",
 [], "TITA", "12", ["Number_System::Miscellaneous"], "Medium",
 r"Rearrange to \(8b = a(3c - 8)\) and try small a and c.",
 steps(p(r"\(c\) must be at least 3. \(a = 1\): \(3c - 8\) must be a multiple of 8, so \(c = 8, b = 2\): total 15. \(a = 2\): \(3c - 8\) a multiple of 4, so \(c = 4, b = 1\): total \(6 + 2 + 4 = 12\). Larger a only raises 3a. So 12.")) + final(r"\(12\)"),
 concept=r"\[\text{isolate one variable and use divisibility}\]")

P.qa(16, "In a ∆ABC, points D and E are on the sides BC and AC, respectively. BE and AD intersect at point T such that AD : AT = 4 : 3, and BE : BT = 5 : 4. Point F lies on AC such that DF is parallel to BE. Then, BD : CD is",
 M("9 : 4", "7 : 4", "15 : 4", "11 : 4"), "MCQ", "4", ["Geometry::Triangles"], "Hard",
 "Use mass points: AT : TD = 3 : 1 and BT : TE = 4 : 1.",
 steps(("Masses", p(r"Give A mass 1. From AT : TD = 3 : 1, D has mass 3. From BT : TE = 4 : 1, E has 4 times B’s mass.")),
       ("Solve", p(r"D’s mass is B + C = 3 and E’s is A + C = 4B. So \(4B = 1 + 3 - B\), giving \(B = 0.8\) and \(C = 2.2\).")),
       ("Ratio", p(r"\(BD : DC = C : B = 2.2 : 0.8 = 11 : 4\)."))) + final(r"\(11 : 4\), option 4"),
 concept=r"\[\text{mass points: } \frac{BD}{DC} = \frac{m_C}{m_B}\]",
 why_rows=[("1", "This mixes up the two given ratios."), ("2", "This mixes up the two given ratios."), ("3", "This mixes up the two given ratios.")])

P.qa(17, r"The number of divisors of \(2^6 \times 3^5 \times 5^3 \times 7^2\), which are of the form \(3r + 1\), where \(r\) is a non-negative integer, is",
 [], "TITA", "42", ["Number_System::Factors_and_Divisibility"], "Medium",
 "No factor of 3 allowed. Modulo 3, 2 and 5 are −1 and 7 is 1.",
 steps(("The form", p(r"A divisor \(2^a 5^b 7^c\) leaves remainder \((-1)^{a+b}\) when divided by 3, so we need \(a + b\) even.")),
       ("Count", p(r"a from 0 to 6, b from 0 to 3: even–even \(4 \times 2 = 8\), odd–odd \(3 \times 2 = 6\), total 14. c has 3 choices: \(14 \times 3 = 42\)."))) + final(r"\(42\)"),
 concept=r"\[2 \equiv 5 \equiv -1, \quad 7 \equiv 1 \pmod 3\]")

P.qa(18, "Rita and Sneha can row a boat at 5 km/h and 6 km/h in still water, respectively. In a river flowing with a constant velocity, Sneha takes 48 minutes more to row 14 km upstream than to row the same distance downstream. If Rita starts from a certain location in the river, and returns downstream to the same location, taking a total of 100 minutes, then the total distance, in km, Rita will cover is",
 [], "TITA", "8", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Find the stream speed from Sneha’s timings.",
 steps(("Stream", p(r"\(\frac{14}{6 - v} - \frac{14}{6 + v} = 0.8\) gives \(v^2 + 35v - 36 = 0\), so \(v = 1\).")),
       ("Rita", p(r"Upstream 4 km/h, downstream 6 km/h. \(\frac{x}{4} + \frac{x}{6} = \frac53\) h gives \(x = 4\). The round trip is 8 km."))) + final(r"\(8\)"),
 concept=r"\[\text{upstream} = b - v, \quad \text{downstream} = b + v\]")

P.qa(19, "An item with a cost price of Rs. 1650 is sold at a certain discount on a fixed marked price to earn a profit of 20% on the cost price. If the discount was doubled, the profit would have been Rs. 110. The rate of discount, in percentage, at which the profit percentage would be equal to the rate of discount, is nearest to",
 M("18", "12", "16", "14"), "MCQ", "4", ["Arithmetic::Profit_Loss_and_Discount"], "Medium",
 "The extra discount costs 1980 − 1760 = 220.",
 steps(("Marked price", p(r"Selling prices 1980 and 1760, so one discount’s worth is 220 and \(M = 1980 + 220 = 2200\) (discount 10%).")),
       ("Equal rates", p(r"\(2200(1 - x) = 1650(1 + x)\), so \(x = \frac{550}{3850} \approx 14.3\%\)."))) + final(r"\(14\), option 4"),
 concept=r"\[\text{SP} = M(1 - d) = C(1 + p)\]",
 why_rows=[("1", "Too high: at 18% discount the profit is about 9%."), ("2", "At 12% discount the profit is about 17%."), ("3", "At 16% discount the profit is about 12%.")])

P.qa(20, r"The sum of digits of the number \((625)^{65} \times (128)^{36}\), is",
 [], "TITA", "25", ["Number_System::Miscellaneous"], "Medium",
 "Write both as powers of 5 and 2, then pair them into 10s.",
 steps(p(r"\(5^{260} \times 2^{252} = 10^{252} \times 5^8\). \(5^8 = 390625\), whose digits add to \(3 + 9 + 0 + 6 + 2 + 5 = 25\); the trailing zeros add nothing.")) + final(r"\(25\)"),
 concept=r"\[2^n \times 5^n = 10^n\]")

P.qa(21, "The ratio of expenditures of Lakshmi and Meenakshi is 2 : 3, and the ratio of income of Lakshmi to expenditure of Meenakshi is 6 : 7. If excess of income over expenditure is saved by Lakshmi and Meenakshi, and the ratio of their savings is 4 : 9, then the ratio of their incomes is",
 M("3 : 5", "5 : 6", "7 : 8", "2 : 1"), "MCQ", "1", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "Let Meenakshi’s expenditure be 21k so that both ratios give whole numbers.",
 steps(p(r"Expenditures: Lakshmi 14k, Meenakshi 21k. Lakshmi’s income 18k, so she saves 4k. Then Meenakshi saves 9k and earns 30k. Incomes \(18 : 30 = 3 : 5\).")) + final(r"\(3 : 5\), option 1"),
 concept=r"\[\text{saving} = \text{income} - \text{expenditure}\]",
 why_rows=[("2", "Meenakshi earns 30k, not 21.6k."), ("3", "This doesn’t use the savings ratio."), ("4", "Lakshmi earns less.")])

P.qa(22, r"If \(m\) and \(n\) are integers such that \((m + 2n)(2m + n) = 27\), then the maximum possible value of \(2m - 3n\) is",
 [], "TITA", "17", ["Algebra::Linear_Equations"], "Medium",
 r"Let \(u = m + 2n\) and \(v = 2m + n\); then \(uv = 27\) and \(u + v = 3(m + n)\) must be a multiple of 3.",
 steps(("Factor pairs", p(r"\(u + v\) divisible by 3 leaves \((3, 9), (9, 3), (-3, -9), (-9, -3)\).")),
       ("Solve each", p(r"\(m = \frac{2v - u}{3}\), \(n = \frac{2u - v}{3}\). (3, 9): m = 5, n = −1, giving 13. (9, 3): m = −1, n = 5, giving −17. (−3, −9): m = −5, n = 1, giving −13. (−9, −3): m = 1, n = −5, giving 17.")),
       ("Maximum", p("17."))) + final(r"\(17\)"),
 concept=r"\[\text{factor a product equation and test each factor pair}\]")
