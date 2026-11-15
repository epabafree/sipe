# -*- coding: utf-8 -*-
# Simp Mock 12 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_12 import P
import m25_12_figs as F

P.qa(1, "How many integer values of k satisfy (k + 4)(k − 7) − (2k − 4) ≤ 0?", [], "TITA", "12", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "Expand and factorise.",
 steps(("Expand", p(r"\(k^2 - 5k - 24 \le 0\), i.e. \((k - 8)(k + 3) \le 0\).")), ("Count", p("−3 to 8: 12 integers."))) + final("12"))

P.qa(2, r"What is the smallest positive integer k for which \(2^{269} + k\) is divisible by 255?", ["63", "137", "187", "223"], "MCQ", "4", ["Number_System::Remainders"], "Easy",
 r"\(255 = 2^8 - 1\), so \(2^8 \equiv 1\).",
 steps(("Remainder", p(r"\(269 = 8 \times 33 + 5\), so \(2^{269} \equiv 2^5 = 32\).")), ("k", p("255 − 32 = 223."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(3, r"What is the largest integer that can be written as \(\sqrt[n]{x} + \sqrt[n]{y} + \sqrt[n]{z}\), where x, y, z and n are distinct positive integers with x + y + z < 1000 and n > 2?", [], "TITA", "20", ["Algebra::Surds_and_Indices"], "Medium",
 "For a whole-number sum, each root must itself be whole; cube roots grow fastest.",
 steps(("Use n = 3", p("Higher roots are smaller, and a whole-number total of positive cube roots needs each root to be whole, so take three perfect cubes.")),
       ("Best cubes", p(r"Need \(a^3 + b^3 + c^3 < 1000\) with a, b, c distinct. 8, 7, 6: 1071, too big. 8, 7, 5: 512 + 343 + 125 = 980. So 20.")),
       ("Upper bound", p(r"Even for real numbers, \(3\sqrt[3]{333} \approx 20.8\), so 21 is out of reach."))) + final("20"))

P.qa(4, "A carpenter cuts a rectangular wooden board, 198 cm by 162 cm, into identical circular discs, each with an integer radius, laid out in a grid so that the board is used up with no leftover strip wide enough for another disc. What is the minimum possible number of discs?", ["97", "98", "99", "100"], "MCQ", "3", ["Number_System::Factors_and_Divisibility"], "Easy",
 "Fewest discs means the largest diameter that fits both sides exactly.",
 steps(("Diameter", p("HCF(198, 162) = 18, radius 9.")), ("Count", p("11 × 9 = 99."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(5, "Two distinct positive numbers a and b add up to 32. The sum of their reciprocals equals their harmonic mean multiplied by the reciprocal of their geometric mean. What is ab?", [], "TITA", "64", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Write everything in terms of ab.",
 steps(("Equation", p(r"\(\tfrac{32}{ab} = \tfrac{2ab}{32} \cdot \tfrac{1}{\sqrt{ab}}\), so \((ab)^{3/2} = 512\).")), ("ab", p(r"\(512^{2/3} = 64\)."))) + final("64"))

P.qa(6, "Siddhesh took a loan of ₹5,00,000 at 8% per annum, compounded annually. At the end of two years he repaid ₹M. Three years after that, he paid ₹5,66,870.40 to clear the loan. What is M?", ["₹83,200", "₹1,33,200", "₹1,83,200", "₹2,33,200"], "MCQ", "2", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "Work back three years from the final payment.",
 steps(("After two years", p(r"\(500000 \times 1.08^2 = 583200\).")),
       ("Balance left", p(r"\(1.08^3 = 1.259712\), and \(566870.40 \div 1.259712\) \(= 450000\).")),
       ("M", p("583,200 − 450,000 = 1,33,200."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(7, r"p and q are distinct rational numbers, and \(3 + \sqrt2\) is a root of \(x^2 + px + q = 0\). What is |p + q|?", [], "TITA", "1", ["Algebra::Quadratic_Equations"], "Easy",
 r"Rational coefficients: \(3 - \sqrt2\) is the other root.",
 steps(("Roots", p("Sum 6 = −p, product 9 − 2 = 7 = q.")), ("Value", p("|−6 + 7| = 1."))) + final("1"))

P.qa(8, "Find the area (in sq. units) of the region bounded by |x + y| = 2 and |y| = 1.", [], "TITA", "8", ["Geometry::Coordinate_Geometry"], "Easy",
 "Two pairs of parallel lines: a parallelogram.",
 steps(("Vertices", p("(−3, 1), (1, 1), (3, −1), (−1, −1).")), ("Area", p("Base 4 between the horizontal lines, height 2: 8."))) + final("8"))

P.qa(9, r"If \(x^2 + 2x + 5\) is a factor of \(x^4 + Px^2 + Q\), what is P + Q?", ["17", "21", "25", "31"], "MCQ", "4", ["Algebra::Equations_and_Polynomials"], "Easy",
 "An even polynomial: the other factor is the same with x → −x.",
 steps(("Product", p(r"\((x^2 + 2x + 5)(x^2 - 2x + 5)\) \(= x^4 + 6x^2 + 25\).")), ("Sum", p("6 + 25 = 31."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Q alone.")])

P.qa(10, "A share starts at ₹X. On day 1 it falls 10%, and on day 2 it rises a%, back to ₹X. On day 3 it falls a%, and on day 4 it rises b%, back to ₹X. On day 5 it falls b%, and on day 6 it rises c%, back to ₹X, and so on: each odd day it falls by the previous rise, and each even day it rises back to ₹X. On which day does the price first reach half of ₹X?", ["17th day", "18th day", "19th day", "20th day"], "MCQ", "1", ["Arithmetic::Percentages"], "Medium",
 "Track the price after each fall as a fraction of X.",
 steps(("Pattern", p(r"Day 1: \(\tfrac{9}{10}X\). To return, a = \(\tfrac19\), so day 3: \(\tfrac89X\). Then b = \(\tfrac18\), day 5: \(\tfrac78X\), and so on.")),
       ("Half", p(r"After the k-th fall (day 2k − 1) the price is \(\tfrac{10 - k}{11 - k}X\), which is \(\tfrac12X\) at k = 9: day 17."))) + final("Option 1"),
 why_rows=[("2", "An even day returns to X."), ("3", "One fall too many."), ("4", "An even day.")])

P.qa(11, "Ravi, Sneha and Karan gave different amounts to a relief fund. The sums Ravi + Sneha, Sneha + Karan and Ravi + Karan were in the ratio 11 : 15 : 23. What is the ratio of their individual amounts in descending order?", ["27 : 17 : 3", "25 : 19 : 3", "27 : 19 : 5", "27 : 19 : 3"], "MCQ", "4", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Half the total of the three sums is the grand total.",
 steps(("Total", p("(11 + 15 + 23) ÷ 2 = 24.5.")), ("Each", p("Karan 24.5 − 11 = 13.5, Ravi 24.5 − 15 = 9.5, Sneha 24.5 − 23 = 1.5: 27 : 19 : 3."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(12, "A salesman gives a 25% discount on the marked price and makes a 20% profit. If he wants a profit of at least 44%, what is the largest discount he can give?", ["10%", "8%", "6%", "5%"], "MCQ", "1", ["Arithmetic::Profit_and_Loss"], "Easy",
 "Take the marked price as 100.",
 steps(("Cost", p("SP 75 = 1.2 × CP, so CP = 62.5.")), ("New price", p("1.44 × 62.5 = 90: a discount of 10%."))) + final("Option 1"),
 why_rows=[("2", "Profit would exceed 44%, but a larger discount is allowed."), ("3", "Not the maximum."), ("4", "Not the maximum.")])

P.qa(13, "A shopkeeper mixes 2m kg of organic tur dal with m kg of unpolished tur dal. Organic dal costs him twice as much per kg as unpolished dal. He sells the mixture at ₹x per kg, which is 20% below the cost price of organic dal. What is his profit or loss percentage?", ["Loss of 5%", "Profit of 5%", "Profit of 4%", "Loss of 4%"], "MCQ", "4", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Let the costs be 2t and t.",
 steps(("Cost", p("2m × 2t + m × t = 5mt for 3m kg.")), ("Sales", p("3m × 1.6t = 4.8mt: loss 0.2mt, i.e. 4%."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Wrong sign."), ("3", "Wrong sign.")])

P.qa(14, "Anuj can finish a job alone in 120 days. He works alone on day 1. On day 2 a second person, twice as efficient as Anuj, joins him; on day 3 a third, twice as efficient as the second, joins; and so on, each new person twice as efficient as the previous one, until the job is done. In how many days is the work completed?", [], "TITA", "6", ["Arithmetic::Time_and_Work"], "Easy",
 "Anuj does 1 unit a day; the job is 120 units.",
 steps(("Daily work", p(r"Day n: \(1 + 2 + \dots + 2^{n-1} = 2^n - 1\): 1, 3, 7, 15, 31, 63.")),
       ("Running total", p("1, 4, 11, 26, 57, 120."))) + final("6"))

P.qa(15, "Every day Seeta and Geeta leave their homes at 5:00 PM and walk towards each other, meeting after time t. One day Seeta doubles her speed while Geeta walks as usual, and they meet in 37.5% less time. On another day Geeta walks away from Seeta while Seeta walks towards her at her usual speed, and Seeta catches up after time t₁. By what percentage is t less than t₁?", ["80%", "62.5%", "50%", "Cannot be determined"], "MCQ", "1", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "The time ratio fixes the speed ratio.",
 steps(("Speeds", p(r"\(S + G = 0.625(2S + G)\), so \(0.375G = 0.25S\): S = 1.5G.")),
       ("Times", p(r"\(t = \tfrac{D}{2.5G}\), \(t_1 = \tfrac{D}{0.5G}\) = 5t.")),
       ("Percentage", p("(5t − t) ÷ 5t = 80%."))) + final("Option 1"),
 why_rows=[("2", "The 37.5% figure reversed."), ("3", "Arithmetic slip."), ("4", "The ratio is fixed.")])

P.qa(16, "In △ABC, AB ⊥ BC. E is the midpoint of AC and D is the midpoint of EC, and BD ⊥ AC. EF bisects ∠AEB, with F on AB. Find EF : BD.", [r"\(1 : \sqrt3\)", r"\(\sqrt3 : 2\)", r"\(\sqrt3 : 4\)", "None of these"], "MCQ", "1", ["Geometry::Triangles"], "Medium",
 "BD is both median and altitude in △BEC.",
 steps(("Angles", p("BE = BC (BD is median and altitude), and BE = EC (median to the hypotenuse), so △BEC is equilateral: ∠C = 60°, ∠A = 30°, ∠AEB = 120°.")),
       ("Lengths", p(r"Let AE = a. BD is the height of an equilateral triangle of side a: \(\tfrac{\sqrt3}{2}a\). In △AEF, ∠A = 30° and ∠AEF = 60°, so ∠F = 90° and EF = \(\tfrac a2\).")),
       ("Ratio", p(r"\(\tfrac a2 : \tfrac{\sqrt3}{2}a = 1 : \sqrt3\)."))) + final("Option 1"),
 why_rows=[("2", "BD : BE."), ("3", "Arithmetic slip."), ("4", "Option 1 fits.")])

P.qa(17, "P is the centre of the circle. △LMP is equilateral and NQ = ML. Find the difference between the arcs MN and NR (in degrees)." + F.SECANT, ["100°", "20°", "80°", "None of these"], "MCQ", "3", ["Geometry::Circles"], "Medium",
 "NQ equals the radius; chase angles from ∠Q = x.",
 steps(("Isosceles", p("NQ = ML = PN, so ∠NPQ = ∠NQP = x and ∠PNM = 2x (exterior). PM = PN gives ∠PMN = 2x.")),
       ("Solve", p("∠LPM is exterior to △PMQ: 2x + x = 60°, so x = 20°.")),
       ("Arcs", p("∠MPN = 180° − 80° = 100°; arc NR = ∠NPR = 20°. Difference 80°."))) + final("Option 3"),
 why_rows=[("1", "Arc MN alone."), ("2", "Arc NR alone."), ("4", "Option 3 fits.")])

P.qa(18, "From a cube, two prisms are cut away along PQ, RS and SC, as shown on the top face ABCD; each prism is as tall as the cube. PS ∥ AB, Q and R are the midpoints of AB and BC, and △RSC is equilateral. If PD = a cm, find the surface area of what remains." + F.CUBE,
 [r"\(4(13 + \sqrt{13} - 4\sqrt3)a^2\) sq. cm", r"\((78 + 4\sqrt{13} - 2\sqrt3)a^2\) sq. cm", r"\((52 + 4\sqrt{13} - 2\sqrt3)a^2\) sq. cm", r"\((65 + 4\sqrt{13} - 4\sqrt3)a^2\) sq. cm"], "MCQ", "2", ["Geometry::Mensuration"], "Hard",
 "S sits above the midpoint T of RC, and PS ∥ AB puts P directly above T.",
 steps(("Side", p("R is the midpoint of BC and S lies above the midpoint T of RC, so BT is ¾ of the side; PS ∥ AB makes AP = BT. So PD = a is ¼ of the side: side 4a, AP = 3a, AQ = BQ = BR = RC = 2a, RS = SC = 2a.")),
       ("Top and bottom", p(r"Each face: \(16a^2 - \tfrac12 \cdot 3a \cdot 2a - \sqrt3a^2\) \(= (13 - \sqrt3)a^2\). Both: \((26 - 2\sqrt3)a^2\).")),
       ("Sides", p(r"Perimeter BQ + QP + PD + DC + CS + SR + RB \(= (2 + \sqrt{13} + 1 + 4 + 2 + 2 + 2)a\) \(= (13 + \sqrt{13})a\); times height 4a: \((52 + 4\sqrt{13})a^2\).")),
       ("Total", p(r"\((78 + 4\sqrt{13} - 2\sqrt3)a^2\)."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Lateral faces plus only the cut triangles."), ("4", "Arithmetic slip.")])

P.qa(19, r"A is the centre of the regular hexagon PQRSTU, and the area of quadrilateral ABCD is \(3\sqrt3\) sq. cm. Find the area of the hexagon." + F.HEX,
 [r"\(54\sqrt3\) sq. cm", r"\(18\sqrt3\) sq. cm", r"\(108\sqrt3\) sq. cm", r"\(27\sqrt3\) sq. cm"], "MCQ", "1", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "APQR and AQPU are rhombuses, so D and B are midpoints.",
 steps(("Medians", p("The diagonals of a rhombus bisect each other, so PD and QB are medians of the equilateral △PQA, and C is its centroid.")),
       ("Area", p(r"The three medians cut △PQA into six equal parts, and ABCD is two of them: △PQA = \(3 \times 3\sqrt3 = 9\sqrt3\).")),
       ("Hexagon", p(r"Six such triangles: \(54\sqrt3\)."))) + final("Option 1"),
 why_rows=[("2", "Only two triangles."), ("3", "Double counted."), ("4", "Three triangles.")])

P.qa(20, "What is the 2500th term of the sequence 2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 8, …, in which each even number 2k appears 2k times?", ["96", "98", "100", "102"], "MCQ", "3", ["Algebra::Progressions_and_Series"], "Easy",
 "The last 2n is the n(n + 1)th term.",
 steps(("Position", p("49 × 50 = 2450 < 2500 ≤ 50 × 51 = 2550, so n = 50.")), ("Term", p("2 × 50 = 100."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "The block before."), ("4", "The block after.")])

P.qa(21, "A set of m parallel lines intersects another set of m − 1 parallel lines, forming 18 parallelograms. Find m.", [], "TITA", "4", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Choose two lines from each set.",
 steps(("Equation", p(r"\(\binom m2 \binom{m-1}{2} = 18\).")), ("Try", p("m = 4: 6 × 3 = 18."))) + final("4"))

P.qa(22, r"How many solutions does \(\log_{10}(5^x - 2) + x = x\log_{10}2 + \log_{10}3\) have?", ["0", "1", "2", "3"], "MCQ", "2", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"Write x as \(\log_{10}10^x\).",
 steps(("Combine", p(r"\((5^x - 2) \cdot 10^x = 3 \cdot 2^x\), so \((5^x - 2) \cdot 5^x = 3\).")),
       ("Solve", p(r"With \(k = 5^x\): \(k^2 - 2k - 3 = 0\), k = 3 (k = −1 is impossible). \(5^x = 3\) gives one x, and \(5^x - 2 = 1 > 0\)."))) + final("Option 2"),
 why_rows=[("1", "k = 3 works."), ("3", "k = −1 is rejected."), ("4", "Arithmetic slip.")])
