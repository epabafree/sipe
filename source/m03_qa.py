# -*- coding: utf-8 -*-
# Simp Mock 3: QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m03 import P
import m03_figs as F

SLIP = lambda *o: [(x, "Arithmetic slip.") for x in o]

P.qa(1, "Two containers hold milk and water. In the first, milk and water are in the ratio 5 : 3. Solutions from the first and second containers are mixed in the ratio 2 : 5, and the mixture has milk and water in the ratio 17 : 11. What is the ratio of milk to water in the second container?", ["3 : 2", "2 : 3", "3 : 5", "5 : 3"], "MCQ", "1", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Work with the fraction of milk.",
 steps(("Milk fractions", p("First 5/8, mixture 17/28. Let the second be m.")),
       ("Weighted mean", p("2 × 5/8 + 5m = 7 × 17/28, so 5/4 + 5m = 17/4 and m = 3/5.")),
       ("Ratio", p("Milk 3/5, water 2/5: 3 : 2."))) + final("Option 1"),
 why_rows=[("2", "Swaps milk and water."), ("3", "Arithmetic slip."), ("4", "The first container’s ratio.")])

P.qa(2, "ABCD is a cyclic quadrilateral in a circle with centre O. ∠BAD = 90°, ∠COD = 120° and CD = 10√3 cm. Find BC (in cm)." + F.CIRC, ["5√3", "10", "10√2", "15"], "MCQ", "2", ["Geometry::Circles"], "Medium",
 "∠BAD = 90° makes BD a diameter.",
 steps(("Diameter", p("An angle of 90° in a semicircle: BD is a diameter, so ∠BCD = 90°.")),
       ("Angle at B", p("∠CBD stands on arc CD, so it is half of ∠COD: 60°. Then ∠BDC = 30°.")),
       ("BC", p(r"In right triangle BCD, \(BC = CD \tan 30° = 10\sqrt3 \cdot \tfrac{1}{\sqrt3} = 10\)."))) + final("Option 2"),
 why_rows=[("1", "Uses half of CD."), ("3", "Arithmetic slip."), ("4", "Uses tan 60° the wrong way.")])

P.qa(3, r"The terms \(a_1, a_2, a_3, \dots\) form an infinite geometric progression with common ratio 1/5. For every n, \(a_n = k(a_{n+1} + a_{n+2} + \dots)\). Find k.", ["3", "4", "5", "6"], "MCQ", "2", ["Algebra::Progressions_and_Series"], "Easy",
 "The tail after a term is a GP too.",
 steps(("Tail", p(r"\(a_{n+1} + a_{n+2} + \dots = \dfrac{a_n/5}{1 - 1/5} = \dfrac{a_n}{4}\).")),
       ("k", p("a<sub>n</sub> = k · a<sub>n</sub>/4, so k = 4."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(4, "Two positive numbers have product 624, and the sum of their cubes divided by their sum is 628. What is their sum?", ["61", "55", "50", "86"], "MCQ", "3", ["Algebra::Equations_and_Polynomials"], "Easy",
 r"\(\dfrac{x^3 + y^3}{x + y} = x^2 - xy + y^2\).",
 steps(("Squares", p(r"\(x^2 + y^2 = 628 + 624 = 1252\).")),
       ("Sum", p(r"\((x + y)^2 = 1252 + 1248 = 2500\), so x + y = 50."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(5, "A vendor sells samosas at ₹10 each. On a festival day he planned a flat 30% discount and would still have made 40% profit. He made 100 samosas, but 20 spoiled and only 80 could be sold. What discount should he now give so that his profit in rupees equals what he would have made by selling all 100?", ["25%", "12.5%", "10%", "8.5%"], "MCQ", "2", ["Arithmetic::Profit_and_Loss"], "Medium",
 "Selling price after discount is ₹7, which is 140% of cost.",
 steps(("Cost", p("7 = 1.4 × cost, so cost = ₹5 a samosa: ₹500 for 100.")),
       ("Planned profit", p("100 × (7 − 5) = ₹200.")),
       ("New price", p("80 samosas must bring 500 + 200 = ₹700: ₹8.75 each, a discount of 12.5%."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(6, r"Positive integers \(a_1 < a_2 < \dots < a_{50}\) have mean 50, and \(a_2, a_3, \dots, a_{50}\) have mean 51. What is the difference between the largest and smallest possible values of \(a_{50}\)?", ["1051", "1176", "1200", "1225"], "MCQ", "3", ["Arithmetic::Average"], "Hard",
 r"\(a_1 = 2500 - 2499\).",
 steps(("a<sub>1</sub>", p("50 × 50 − 49 × 51 = 1.")),
       ("Largest", p("Keep a<sub>2</sub> to a<sub>49</sub> as small as possible: 2 to 49, adding to 1224. a<sub>50</sub> = 2499 − 1224 = 1275.")),
       ("Smallest", p("49 different numbers averaging 51 have the smallest top value when they are consecutive: 27 to 75. So a<sub>50</sub> ≥ 75.")),
       ("Difference", p("1275 − 75 = 1200."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Takes the sum 1 + 2 + … + 49 as the answer.")])

P.qa(7, "What is the smallest possible value of the sum of the squares of the roots of x² − (3p + 4)x − (3p + 5) = 0, where p is real?", ["0", "1", "2", "4"], "MCQ", "2", ["Algebra::Quadratic_Equations"], "Easy",
 "Sum of squares = (sum)² − 2 × product.",
 steps(("Expression", p(r"\((3p + 4)^2 + 2(3p + 5)\) \(= 9p^2 + 30p + 26\) \(= (3p + 5)^2 + 1\).")),
       ("Least", p("1, when p = −5/3. (The discriminant (3p + 4)² + 4(3p + 5) is always positive, so the roots are real.)"))) + final("Option 2"),
 why_rows=[("1", "The square term can be 0, but the +1 stays."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(8, "10 women can finish a job in 24 days. With 6 children joining them, they finish it in 20 days. Which group finishes the job in 10 days?", ["18 women and 20 children", "20 women and 15 children", "15 women and 20 children", "18 women and 18 children"], "MCQ", "4", ["Arithmetic::Time_and_Work"], "Easy",
 "The children’s 20 days of work replace 4 days of the women’s.",
 steps(("Rates", p("6 children × 20 = 10 women × 4, so a woman does 3 times a child’s work. The job is 240 woman-days = 720 child-days.")),
       ("10 days", p("Needed: 72 child-units a day. 18 women and 18 children: 54 + 18 = 72."))) + final("Option 4"),
 why_rows=[("1", "74 a day: faster than 10 days."), ("2", "75 a day."), ("3", "65 a day: too slow.")])

P.qa(9, "A tank has small and large inlet pipes. One small and two large pipes fill it in 30 minutes; four small and two large fill it in 20 minutes. How many minutes do 5 small pipes take?", [], "TITA", "36", ["Arithmetic::Time_and_Work"], "Easy",
 "Rates x (small) and y (large).",
 steps(("Equal tanks", p("30(x + 2y) = 20(4x + 2y), so 3x + 6y = 8x + 4y and 2y = 5x.")),
       ("Tank", p("30(x + 5x) = 180x.")),
       ("5 small", p("180x ÷ 5x = 36 minutes."))) + final("36"))

P.qa(10, r"Simplify \(\log\left(\dfrac{81}{32 \cdot 343}\right)^5 + \log\left(\dfrac{16}{27 \cdot 49}\right)^3\) \(+ \log\left(\dfrac{117649 \cdot 16}{9}\right)^4\).", ["3 log 40", "5 log 42", "3 log 42", "5 log 40"], "MCQ", "3", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Write everything in powers of 2, 3 and 7 (117649 = 7⁶).",
 steps(("Powers", p("5(4 log 3 − 5 log 2 − 3 log 7) + 3(4 log 2 − 3 log 3 − 2 log 7) + 4(6 log 7 + 4 log 2 − 2 log 3).")),
       ("Collect", p("log 3: 20 − 9 − 8 = 3. log 2: −25 + 12 + 16 = 3. log 7: −15 − 6 + 24 = 3.")),
       ("Answer", p("3(log 2 + log 3 + log 7) = 3 log 42."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(11, "Two boats make a round trip between A and B on a river. The fast boat takes 30% less time than the slow boat. The slow boat’s speed in still water is 5 times the speed of the current. Find the ratio of the slow boat’s still-water speed to the fast boat’s.", ["5 : 7", "5 : 6", "4 : 5", "5 : 8"], "MCQ", "1", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Round-trip time for still-water speed s and current w is 2Ds/(s² − w²).",
 steps(("Slow", p("s = 5w: time ∝ 5w/24w² = 5/(24w).")),
       ("Fast", p(r"\(\dfrac{f}{f^2 - w^2} = 0.7 \times \dfrac{5}{24w}\), so \(7f^2 - 48fw - 7w^2 = 0\).")),
       ("Solve", p("(f − 7w)(7f + w) = 0, so f = 7w. Ratio 5 : 7."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(12, "If p > 3 and q < −1, which statement is always true?", ["3p + 4q > 5/2", "If p < −q, then 5p + 4q > 1", "If p > q², then p + 3q < −1", "None of these"], "MCQ", "4", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "Try values that satisfy the conditions.",
 steps(("1", p("p = 4, q = −3: 3p + 4q = 0.")),
       ("2", p("p = 4, q = −5: 4 < 5, but 5p + 4q = 0.")),
       ("3", p("p = 10, q = −3: 10 > 9, but p + 3q = 1."))) + final("Option 4"),
 why_rows=[("1", "Fails at p = 4, q = −3."), ("2", "Fails at p = 4, q = −5."), ("3", "Fails at p = 10, q = −3.")])

P.qa(13, "A trader buys the same quantities of potatoes and onions every month. This month potato prices rose 25% and onion prices 20%, and he spent ₹3000 more than usual. He used to spend ₹8000 a month on potatoes. How much did he spend on onions this month (in ₹)?", ["4500", "5000", "5500", "6000"], "MCQ", "4", ["Arithmetic::Percentages"], "Easy",
 "Split the ₹3000.",
 steps(("Potatoes", p("25% of 8000 = 2000 extra.")),
       ("Onions", p("₹1000 extra = 20% of the old spend, so the old spend was ₹5000 and now it is ₹6000."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "The old onion spend."), ("3", "Arithmetic slip.")])

P.qa(14, "Identical chocolates are shared among Ram, Shyam and Uma, each getting at least one and at most 20 being given out in all. Shyam gets fewer than Ram and Uma together. Uma gets at least 2 more than Ram, and Shyam at least 2 more than Uma. In how many ways can this be done?", [], "TITA", "6", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "R ≤ U − 2 ≤ S − 4, and S < R + U.",
 steps(("Bound S", p("R + U ≤ (S − 4) + (S − 2) = 2S − 6, and R + U ≥ S + 1, so S ≥ 7. Also 2S + 1 ≤ R + U + S ≤ 20, so S ≤ 9.")),
       ("List", p("For each S, R + U runs from S + 1 to 20 − S, with U from R + 2 up to S − 2.") +
          "<ol><li>S = 7: R + U = 8, U ≤ 5: (3, 5).</li><li>S = 8: R + U = 9 or 10, U ≤ 6: (3, 6), (4, 6).</li><li>S = 9: R + U = 10 or 11, U ≤ 7: (3, 7), (4, 6), (4, 7).</li></ol>"),
       ("Count", p("1 + 2 + 3 = 6."))) +
 final("6"))

P.qa(15, "Positive integers a, b, c and d satisfy a : b = 3 : 4 and c : d = 2 : 3. b and d differ by 5, and c − a = 1. Find a + b + c + d.", [], "TITA", "104", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "a = 3k, b = 4k, c = 2m, d = 3m.",
 steps(("Which is bigger", p("c > a means 2m > 3k, so k/m < 2/3 < 3/4, and then 4k < 3m: d > b. So 3m − 4k = 5.")),
       ("Solve", p("2m − 3k = 1 and 3m − 4k = 5 give k = 7, m = 11.")),
       ("Sum", p("21 + 28 + 22 + 33 = 104."))) + final("104"))

P.qa(16, r"What is the sum of the smallest and second smallest integers x satisfying \(\dfrac{(4x^2 - 1)(3x - 1)}{2x^2 + 3x - 2} \ge 0\)?", ["−3", "−1", "0", "1"], "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Factor and cancel 2x − 1 (keeping x ≠ ½).",
 steps(("Factor", p(r"\(\dfrac{(2x - 1)(2x + 1)(3x - 1)}{(2x - 1)(x + 2)}\) \(= \dfrac{(2x + 1)(3x - 1)}{x + 2}\), with x ≠ ½ and x ≠ −2.")),
       ("Signs", p("Critical points −2, −½, ⅓. The expression is ≥ 0 on (−2, −½] and on [⅓, ∞) except ½.")),
       ("Integers", p("Smallest −1, then 1: sum 0."))) + final("Option 3"),
 why_rows=[("1", "Includes −2."), ("2", "Takes −1 and 0, but 0 gives a negative value."), ("4", "Takes 0 and 1.")])

P.qa(17, r"A sequence satisfies \(\sum_{i=1}^{n} (-1)^{i-1} x_i = n^2\) for every natural number n. Find the absolute value of \(x_1 + x_2 + \dots + x_{10}\).", [], "TITA", "10", ["Algebra::Progressions_and_Series"], "Medium",
 "Subtract consecutive sums.",
 steps(("Terms", p(r"\((-1)^{n-1} x_n = n^2 - (n - 1)^2\) \(= 2n - 1\), so \(x_n = (-1)^{n-1}(2n - 1)\): 1, −3, 5, −7, …")),
       ("Sum", p("1 − 3 + 5 − 7 + … − 19 = 5 × (−2) = −10. Absolute value 10."))) + final("10"))

P.qa(18, "Boxes 1 and 3 hold the same number of fruits, and boxes 2 and 4 hold the same number. The numbers in boxes 1 and 2 multiply to 800. Fruits in box 1 cost ₹30 each and in the other boxes ₹10 each. What is the lowest possible total cost of all the fruits (in ₹)?", ["2000", "1800", "1600", "1200"], "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Cost = 30x + 10(x + 2y) with xy = 800.",
 steps(("Cost", p("40x + 20y, with xy = 800.")),
       ("AM–GM", p(r"\(40x + 20y \ge 2\sqrt{800 \cdot 800} = 1600\), with equality when 40x = 20y: x = 20, y = 40."))) + final("Option 3"),
 why_rows=[("1", "Not the minimum."), ("2", "Not the minimum."), ("4", "Below the AM–GM bound.")])

P.qa(19, "In a garden, 59% of the trees are coconut and the rest mango; there are 180 more coconut trees than mango trees. 54% of all the trees, including 245 mango trees, are more than 10 years old. What percentage of the coconut trees are 10 years old or younger?", [], "TITA", "50", ["Arithmetic::Percentages"], "Easy",
 "18% of the trees = 180.",
 steps(("Trees", p("1000 trees: 590 coconut, 410 mango.")),
       ("Older", p("540 are older; 540 − 245 = 295 of them are coconut.")),
       ("Younger coconut", p("590 − 295 = 295, which is 50%."))) + final("50"))

P.qa(20, "AB, MN and DC are each perpendicular to BC, with M the point where AC and BD cross and N on BC. AB = 12 cm and MN = 4 cm. Find CD (in cm)." + F.LAD, ["5", "6", "8", "9"], "MCQ", "2", ["Geometry::Triangles"], "Medium",
 "Similar triangles give MN/AB + MN/DC = 1.",
 steps(("Similar triangles", p("In triangle ABC, MN/AB = NC/BC. In triangle DCB, MN/DC = BN/BC.")),
       ("Add", p("MN/AB + MN/DC = (NC + BN)/BC = 1.")),
       ("Solve", p("4/12 + 4/DC = 1, so DC = 6."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(21, "Amay started a business with ₹20,000 at the start of the year, and Vinay joined after 6 months. Vinay alone managed the business and was paid 12.5% of the profit for it. At year end, both received the same total amount. How much did Vinay invest?", ["₹15,000", "₹20,000", "₹30,000", "₹40,000"], "MCQ", "3", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "After the 12.5% fee, the rest is split by capital × time.",
 steps(("Shares", p("Each ends with 50%. Vinay’s 50% = 12.5% fee + 37.5% share, so the shares are 50 : 37.5 = 4 : 3.")),
       ("Capital × time", p("20,000 × 12 : 6x = 4 : 3, so 6x = 1,80,000 and x = ₹30,000."))) + final("Option 3"),
 why_rows=[("1", "Ignores the 6 months."), ("2", "Ignores the fee."), ("4", "Arithmetic slip.")])

P.qa(22, "Students are asked to draw a scalene triangle ABC with AB < BC < AC, every side a whole number of centimetres, and perimeter 12 cm. How many different triangles can be drawn?", [], "TITA", "1", ["Geometry::Triangles"], "Easy",
 "The longest side is less than half the perimeter.",
 steps(("Longest side", p("AC < 6, and AC > 4 (it is the largest of three different sides adding to 12), so AC = 5.")),
       ("Others", p("AB + BC = 7 with AB < BC < 5: only 3 and 4.")),
       ("Answer", p("Just the 3–4–5 triangle: 1."))) + final("1"))
