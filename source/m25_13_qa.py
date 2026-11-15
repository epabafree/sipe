# -*- coding: utf-8 -*-
# Simp Mock 13 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_13 import P
import m25_13_figs as F

P.qa(1, "A strawberry seller gives a 20% discount on the marked price of each box and makes a 20% profit. Of his n boxes, 10% turn out rotten and can’t be sold. What discount should he give on the good boxes to earn the same total profit as planned?", ["6.67%", "11.11%", "9.09%", "12.25%"], "MCQ", "2", ["Arithmetic::Profit_and_Loss"], "Medium",
 "The total cost is unchanged, so the total revenue must be too.",
 steps(("Revenue", p("Marked price 100: planned revenue 80n. Now 0.9n boxes must bring in 80n, so each sells for 80 ÷ 0.9 = 88.89.")),
       ("Discount", p(r"\(100 - 88\tfrac89 = 11\tfrac19\%\)."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Divides by 1.1 instead of 0.9."), ("4", "Arithmetic slip.")])

P.qa(2, "Akshay drives from Mumbai to Pune at a steady 120 km/h. He returns by a route 20 km longer, covering part of it at 100 km/h and the rest at 150 km/h, in t hours. At a steady 120 km/h on that longer route he would also have taken exactly t hours. What is the ratio of the distance he drove at 100 km/h to the distance at 150 km/h on the way back?", ["3 : 2", "2 : 3", "1 : 2", "1 : 1"], "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "When is the average speed the harmonic mean?",
 steps(("Average", p("The average speed over the return trip is 120. The harmonic mean of 100 and 150 is 2 × 100 × 150 ÷ 250 = 120, which is the average for equal distances.")),
       ("Ratio", p("1 : 1."))) + final("Option 4"),
 why_rows=[("1", "Ratio of speeds reversed."), ("2", "That ratio holds for equal times."), ("3", "Arithmetic slip.")])

P.qa(3, r"What is the product of the distinct real roots of \(|x^2 - 5x + 6| = x + 3\)?", ["0", "2", "3", "4"], "MCQ", "3", ["Algebra::Quadratic_Equations"], "Medium",
 "Split on the sign of the quadratic.",
 steps(("Outside [2, 3]", p(r"\(x^2 - 6x + 3 = 0\): \(x = 3 \pm \sqrt6\), about 5.45 and 0.55, both outside [2, 3], so both count.")),
       ("Inside [2, 3]", p(r"\(-(x^2 - 5x + 6) = x + 3\) gives \(x^2 - 4x + 9 = 0\), no real roots.")),
       ("Product", p(r"\((3 + \sqrt6)(3 - \sqrt6) = 3\)."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Product of 2 and 3, the zeros of the quadratic."), ("4", "Arithmetic slip.")])

P.qa(4, r"How many factors of \(3^{10} \times 5^{15} \times 10^{20} \times 12^{25}\) are perfect cubes with at least two digits?", ["3456", "3455", "3454", "3453"], "MCQ", "3", ["Number_System::Factors_and_Divisibility"], "Medium",
 "Write it in primes first.",
 steps(("Primes", p(r"\(2^{70} \cdot 3^{35} \cdot 5^{35}\).")),
       ("Cube factors", p("Exponents in multiples of 3: 24 choices for 2 (0 to 69), 12 each for 3 and 5: 24 × 12 × 12 = 3456.")),
       ("Two digits", p("Drop 1 and 8: 3454."))) + final("Option 3"),
 why_rows=[("1", "Includes 1 and 8."), ("2", "Drops only 1."), ("4", "Drops 27 as well.")])

P.qa(5, r"x is a natural number. What is the smallest x satisfying \((x^2 - 5x + 8)^3 = 2^{x^2 - 3x - 1}\)?", [], "TITA", "5", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "The base on the left must be a power of 2.",
 steps(("Try", p(r"\(x^2 - 5x + 8 = 2^k\) with \(3k = x^2 - 3x - 1\). k = 1: x = 2 or 3, exponent −3 or −1, no. k = 2: x = 1 or 4, exponent −3 or 3, no. k = 3: x = 5, exponent 9 = 3 × 3. ✓"))) + final("5"))

P.qa(6, "20 children visited an ice-cream parlour that sells vanilla, mango and pineapple. Each had at least one flavour: 17 had vanilla, 11 mango and 7 pineapple. The number who had both vanilla and mango is one more than the number who had both vanilla and pineapple, which is 5 more than the number who had both mango and pineapple. 5 children had pineapple but not mango. How many had all three?", ["0", "1", "2", "3"], "MCQ", "3", ["Modern_Maths::Set_Theory"], "Medium",
 "Use the pairwise totals and the ‘pineapple without mango’ count.",
 steps(("Pairs", p("Let M∩P = k (including those with all three), V∩P = k + 5, V∩M = k + 6. Pineapple without mango = P − M∩P = 7 − k = 5, so k = 2.")),
       ("All three", p("20 = 17 + 11 + 7 − (8 + 7 + 2) + g = 18 + g, so g = 2."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(7, "Ten identical chairs stand in a row, all facing the same way. In how many ways can four children sit on them, one to a chair, so that no two occupied chairs are next to each other?", ["35", "140", "556", "840"], "MCQ", "4", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Choose non-adjacent chairs, then arrange the children.",
 steps(("Chairs", p(r"Non-adjacent choices of 4 from 10: \(\binom{7}{4} = 35\).")), ("Children", p("35 × 4! = 840."))) + final("Option 4"),
 why_rows=[("1", "Forgets to arrange the children."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(8, "How many of the 1000 consecutive natural numbers starting from 1001! + 2 are prime?", ["0", "1", "more than 1 but less than 10", "10 or more"], "MCQ", "1", ["Number_System::Factors_and_Divisibility"], "Easy",
 "1001! + n for 2 ≤ n ≤ 1001.",
 steps(("Divisible", p("Each 1001! + n is divisible by n, and these are exactly the 1000 numbers."))) + final("Option 1"),
 why_rows=[("2", "Every one is composite."), ("3", "Every one is composite."), ("4", "Every one is composite.")])

P.qa(9, "A culture of bacteria numbering p at the start of a minute numbers 10 + 3p at the start of the next. It has 995 at the start of the first minute. How many does it have at the start of the 11th minute?", [r"\(995 \times 3^{10} + 5\)", r"\(1000 \times 3^{10} - 5\)", r"\(1005 \times 3^{10} - 10\)", r"\(1000^{10} - 5\)"], "MCQ", "2", ["Algebra::Progressions_and_Series"], "Medium",
 "Add 5: the shifted value triples each minute.",
 steps(("Shift", p(r"\(P_{n+1} + 5 = 3(P_n + 5)\).")), ("Answer", p(r"\(P_{11} + 5 = 1000 \times 3^{10}\)."))) + final("Option 2"),
 why_rows=[("1", "Wrong shift."), ("3", "Wrong shift."), ("4", "Not geometric in 1000.")])

P.qa(10, r"x is a natural number with \(\sqrt{3x^2 - 7x - 30}\) \(+ \sqrt{2x^2 - 7x - 5} = x + 5\). What is x?", [], "TITA", "6", ["Algebra::Equations_and_Polynomials"], "Medium",
 "The difference of the two expressions under the roots is x² − 25.",
 steps(("Difference", p(r"\((3x^2 - 7x - 30) - (2x^2 - 7x - 5)\) \(= x^2 - 25\). Dividing by the given sum, the difference of the two roots is x − 5.")),
       ("Add", p(r"\(2\sqrt{3x^2 - 7x - 30} = 2x\), so \(2x^2 - 7x - 30 = 0\), i.e. \((x - 6)(2x + 5) = 0\): x = 6.")),
       ("Check", p("√36 + √25 = 11 = 6 + 5."))) + final("6"))

P.qa(11, "Twenty students with roll numbers 1 to 20 each wrote a number on the board: roll 1 wrote 1, roll 2 wrote 4, roll 3 wrote 3, roll 4 wrote 16, and so on, up to 19 and 400 for the last two. The teacher erased one number, and the rest added up to 1631. Which number was erased?", [], "TITA", "9", ["Algebra::Progressions_and_Series"], "Easy",
 "Odd rolls wrote their number; even rolls wrote its square.",
 steps(("Total", p(r"Odds 1 + 3 + … + 19 = 100; even squares \(4(1^2 + \dots + 10^2) = 4 \times 385 = 1540\). Total 1640.")),
       ("Erased", p("1640 − 1631 = 9, which is on the board."))) + final("9"))

P.qa(12, r"A clock gains 1 minute in the first hour, 2 in the second, 3 in the third, and so on. It is set right at 1:00 PM on 15 August. When does it next show the correct time?",
 [r"\(1{:}17\tfrac{16}{19}\) AM on 17 August", r"\(2{:}26\tfrac{16}{19}\) AM on 17 August", "2:17 AM on 17 August", r"\(1{:}27\tfrac{16}{19}\) AM on 18 August"], "MCQ", "2", ["Arithmetic::Miscellaneous"], "Medium",
 "It must gain 12 hours = 720 minutes.",
 steps(("Whole hours", p(r"After h hours it has gained \(\tfrac{h(h + 1)}{2}\): 37 hours give 703.")),
       ("Last bit", p(r"In hour 38 it gains 38 minutes per hour; 17 more take \(\tfrac{17}{38} \times 60 = 26\tfrac{16}{19}\) minutes.")),
       ("Time", p(r"1 PM + 37 h = 2 AM on 17 August, plus \(26\tfrac{16}{19}\) minutes."))) + final("Option 2"),
 why_rows=[("1", "An hour short."), ("3", "Treats 17 minutes as clock time."), ("4", "A day late.")])

P.qa(13, "A tank has an inlet and an outlet pipe. With the outlet closed, the inlet fills it in n hours; with the outlet open, it takes n + 3 hours. How long does the outlet alone take to empty a full tank?", [r"\(\dfrac{n^2}{6} + n\)", r"\(\dfrac{n}{3} + n\)", r"\(\dfrac{n^2}{3} + n\)", "None of these"], "MCQ", "3", ["Arithmetic::Time_and_Work"], "Easy",
 "Subtract the rates.",
 steps(("Outlet rate", p(r"\(\tfrac1n - \tfrac1{n + 3} = \tfrac{3}{n(n + 3)}\).")), ("Time", p(r"\(\tfrac{n(n + 3)}{3} = \tfrac{n^2}{3} + n\)."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Drops a factor of n."), ("4", "Option 3 fits.")])

P.qa(14, "Ratna, Heera, Meena and Panna have p, q, r and s diamonds, with p : q = q : r = r : s = 2 : 3. After each gives 4 diamonds to Leela, their holdings are in the ratio 7 : 11 : 17 : 26. What is the minimum total they had initially?", ["195", "390", "260", "325"], "MCQ", "3", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "p : q : r : s = 8 : 12 : 18 : 27.",
 steps(("Equation", p("(8k − 4) : (12k − 4) = 7 : 11 gives 88k − 44 = 84k − 28, so k = 4.")),
       ("Check", p("28 : 44 : 68 : 104 = 7 : 11 : 17 : 26. Total 65 × 4 = 260."))) + final("Option 3"),
 why_rows=[("1", "k = 3 doesn’t fit."), ("2", "k = 6 doesn’t fit."), ("4", "k = 5 doesn’t fit.")])

P.qa(15, "Four shops offer these discounts. A: a flat 20%. B: two successive 10% discounts. C: successive 10%, 5% and 5%. D: four successive 5% discounts. Which is the ascending order of effective discount?", ["D, C, B, A", "A, B, C, D", "A, C, B, D", "B, C, D, A"], "MCQ", "1", ["Arithmetic::Percentages"], "Easy",
 "More, smaller steps compound to less.",
 steps(("Prices on 100", p("A 80; B 81; C 81.225; D 81.45.")), ("Order", p("Discounts: D 18.55%, C 18.78%, B 19%, A 20%."))) + final("Option 1"),
 why_rows=[("2", "Descending."), ("3", "Mixed."), ("4", "Mixed.")])

P.qa(16, "In trapezium ABCD, AD ∥ BC, AD = 32 cm and BC = 16 cm. A line parallel to BC meets AB at X, CD at Y, and the diagonals AC and BD at their midpoints P and Q. Find PQ (in cm).", [], "TITA", "8", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "The midpoints of the diagonals lie on the midline.",
 steps(("Midline pieces", p("XP = BC ÷ 2 = 8 (in △ABC) and XQ = AD ÷ 2 = 16 (in △ABD).")), ("PQ", p("16 − 8 = 8, i.e. (AD − BC) ÷ 2."))) + final("8"))

P.qa(17, "An inverted cone-shaped underground tank can be filled from empty by a pump in 1 hour 48 minutes. The tank was already filled to one-third of its height when the pump was started. The pump stopped after some time, when the water had reached two-thirds of the height; no water was drawn meanwhile. For how many minutes did the pump run?", [], "TITA", "28", ["Geometry::Mensuration"], "Medium",
 "Volume scales with the cube of the depth.",
 steps(("Volumes", p("Depth 1 : 2 : 3 gives volume 1 : 8 : 27. The pump added 7 of the 27 parts.")), ("Time", p("108 × 7 ÷ 27 = 28 minutes."))) + final("28"))

P.qa(18, "△ABC is right-angled at B; M and N are the midpoints of AB and BC. If MC = 19 cm and AN = 22 cm, find AC." + F.RIGHT, ["20 cm", "23 cm", "26 cm", "29 cm"], "MCQ", "3", ["Geometry::Triangles"], "Easy",
 "Add the two Pythagoras equations.",
 steps(("Sum", p(r"\(AB^2 + BN^2 + MB^2 + BC^2\) \(= 484 + 361 = 845\), i.e. \(AC^2 + MN^2 = 845\).")),
       ("MN", p(r"MN = AC ÷ 2, so \(\tfrac54AC^2 = 845\): AC² = 676, AC = 26."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(19, "A shopkeeper sells 15 kg of a mixture of grade A and grade B sugar, with no more grade B than grade A. Grade A costs ₹30 per kg more than grade B. He sells the mixture for ₹690 at a 15% profit. Which could be the cost of grade B sugar per kg?", ["₹30", "₹28", "₹26", "₹24"], "MCQ", "4", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Cost 690 ÷ 1.15 = 600.",
 steps(("Equation", p("With x kg of A and B at ₹y: x(y + 30) + (15 − x)y = 600, so 2x + y = 40.")),
       ("Limit", p("x ≥ 7.5 gives y ≤ 25. Only ₹24 fits (x = 8)."))) + final("Option 4"),
 why_rows=[("1", "Needs x = 5, too little grade A."), ("2", "Needs x = 6."), ("3", "Needs x = 7.")])

P.qa(20, "Ajay invested ₹10,00,000 on 1 January 2024 for one year at 20% per annum compounded quarterly. After six months he invested another ₹20,00,000 for the remaining six months on the same terms. Ravi invested ₹X on 1 January 2024 at 25% simple interest for one year. Both received the same amount at the end of the year. Find X.", ["₹27,36,405", "₹23,36,405", "₹24,36,405", "₹25,36,405"], "MCQ", "1", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "5% per quarter.",
 steps(("Ajay", p(r"\(10{,}00{,}000 \times 1.05^4 = 12{,}15{,}506.25\); \(20{,}00{,}000 \times 1.05^2 = 22{,}05{,}000\). Total 34,20,506.25.")),
       ("Ravi", p("1.25X = 34,20,506.25, so X = 27,36,405."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(21, r"If \(P = (2^2 + 1)(2^4 + 1)(2^8 + 1)\) \((2^{16} + 1) \cdots (2^{1024} + 1)\), how many digits does 24P + 8 have? (Take log 2 = 0.3010.)", [], "TITA", "618", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"Multiply by \(2^2 - 1 = 3\) and let it telescope.",
 steps(("Telescope", p(r"\(3P = 2^{2048} - 1\), so \(24P + 8 = 8(3P + 1) = 2^{2051}\).")),
       ("Digits", p(r"\(2051 \times 0.3010 = 617.35\): 618 digits."))) + final("618"))

P.qa(22, r"What is the remainder when \(324586789^{123}\) is divided by 8?", ["7", "5", "3", "1"], "MCQ", "2", ["Number_System::Remainders"], "Easy",
 "Only the last three digits matter for 8.",
 steps(("Base", p("789 = 8 × 98 + 5, so the base leaves 5.")), ("Power", p(r"\(5^2 \equiv 1\), so \(5^{123} \equiv 5\)."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Even power.")])
