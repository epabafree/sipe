# -*- coding: utf-8 -*-
# Simp Mock 9: QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m09 import P

SLIP = lambda *o: [(x, "Arithmetic slip.") for x in o]

P.qa(1, r"Let N > 0, N ≠ 1, k > 0 and \(a = \tfrac{1}{N}\). What is \(\dfrac{1}{N^{\log_a k}}\)?", [r"\(\tfrac{1}{k}\)", r"\(\tfrac{N}{k}\)", "k", r"\(k^{-N}\)"], "MCQ", "3", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"\(\log_{1/N} k = -\log_N k\).",
 steps(("Exponent", p(r"\(N^{\log_a k} = N^{-\log_N k} = \tfrac{1}{k}\).")),
       ("Answer", p(r"\(1 \div \tfrac{1}{k} = k\)."))) + final("Option 3"),
 why_rows=[("1", "That is the denominator."), ("2", "Not from the rules."), ("4", "Not from the rules.")])

P.qa(2, r"\(S_N\) is the sum of the first N natural numbers. If \(S_1 + S_2 + \dots + S_{100} = C \times S_{100}\), what is C?", ["17", "34", "32", "16"], "MCQ", "2", ["Algebra::Progressions_and_Series"], "Hard",
 r"Sum of triangular numbers: \(\tfrac{n(n+1)(n+2)}{6}\).",
 steps(("Sum", p(r"\(\tfrac{100 \cdot 101 \cdot 102}{6}\).")),
       ("Divide", p(r"By \(S_{100} = \tfrac{100 \cdot 101}{2}\): C = 102 ÷ 3 = 34."))) + final("Option 2"),
 why_rows=[("1", "Half of it."), ("3", "Slip."), ("4", "Slip.")])

P.qa(3, "Mahesh walks up a moving up-escalator in a mall, then at once walks back down the same escalator at the same speed. The round trip takes 80 seconds. At twice his speed it would take 32 seconds. What is the ratio of his speed to the escalator’s?", ["3 : 2", "2 : 1", "4 : 3", "More information is needed"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Hard",
 "Up at m + e, down at m − e.",
 steps(("Equations", p(r"\(\tfrac{2mN}{m^2 - e^2} = 80\) and \(\tfrac{4mN}{4m^2 - e^2} = 32\).")),
       ("Divide", p(r"\(5(m^2 - e^2) = 4m^2 - e^2\), so \(m^2 = 4e^2\): m : e = 2 : 1."))) + final("Option 2"),
 why_rows=[("1", "Does not fit both times."), ("3", "Does not fit both times."), ("4", "The two trips fix the ratio.")])

P.qa(4, "In isosceles triangle ABC, AB = AC and BC = 8 cm. O is the midpoint of BC, and P is a point on side AC with OP = 4 cm. Find ∠BPC in degrees.", ["90", "60", "45", "More information is needed"], "MCQ", "1", ["Geometry::Triangles"], "Medium",
 "OB = OC = OP.",
 steps(("Circle", p("P lies on the circle with diameter BC, so the angle in a semicircle is 90°."))) + final("Option 1"),
 why_rows=[("2", "Equilateral thinking."), ("3", "Not forced."), ("4", "OP = 4 settles it.")])

P.qa(5, "A cricket ball weighs 25% of a football. A tennis ball and a cricket ball together weigh 40% of a football and a tennis ball together. A tennis ball weighs what percentage of a football?", [], "TITA", "25", ["Arithmetic::Percentages"], "Easy",
 "f = 4c.",
 steps(("Equation", p("5(c + t) = 2(f + t) = 8c + 2t, so 3t = 3c.")),
       ("Answer", p("t = c = 25% of f."))) + final("25"))

P.qa(6, "A maker sells a laptop to a distributor for ₹36,000. The distributor sells it to a retailer at a 12.5% profit. The retailer must make a profit of at least 35% and at most 40%, and the final price must be a multiple of ₹100. How many different prices can the retailer charge?", ["22", "21", "20", "19"], "MCQ", "2", ["Arithmetic::Profit_and_Loss"], "Medium",
 "Retailer’s cost 40,500.",
 steps(("Range", p("40,500 × 1.35 = 54,675; 40,500 × 1.4 = 56,700.")),
       ("Count", p("54,700 to 56,700 in hundreds: 567 − 547 + 1 = 21."))) + final("Option 2"),
 why_rows=[("1", "Includes 54,600."), ("3", "Misses an end."), ("4", "Misses both ends.")])

P.qa(7, "A rectangle has perimeter 20 cm. What is the least value of the product of the lengths (in cm) of its two diagonals?", [], "TITA", "50", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "The diagonals are equal.",
 steps(("Product", p("d² = l² + b² = 100 − 2lb, with l + b = 10.")),
       ("Least", p("lb is largest at l = b = 5: 100 − 50 = 50."))) + final("50"))

P.qa(8, r"\(f(x) = \tfrac{1}{x^2}\) and \(g(x) = \sqrt{x}\). Find \(g\big(x + 4f(f(g(x))) + f(f(x))\big)\) at x = 4.", ["12", "14", "16", "18"], "MCQ", "4", ["Algebra::Functions"], "Easy",
 "f(f(x)) = x⁴.",
 steps(("Pieces", p("g(4) = 2, f(f(2)) = 16; f(f(4)) = 256.")),
       ("Answer", p("g(4 + 64 + 256) = √324 = 18."))) + final("Option 4"),
 why_rows=SLIP("1", "2", "3"))

P.qa(9, "If |3x − 7| + |9 − 4x| = |2 − x|, which best describes x?", [r"\(\tfrac94 < x < \tfrac73\)", r"\(\tfrac94 \le x \le \tfrac73\)", r"\(x \ge \tfrac73\) or \(x \le \tfrac94\)", r"\(x > \tfrac73\) or \(x < \tfrac94\)"], "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "(3x − 7) + (9 − 4x) = 2 − x.",
 steps(("Rule", p("|a| + |b| = |a + b| exactly when a and b do not have opposite signs.")),
       ("Signs", p("Both ≥ 0 needs x ≥ 7/3 and x ≤ 9/4: impossible. Both ≤ 0: 9/4 ≤ x ≤ 7/3."))) + final("Option 2"),
 why_rows=[("1", "Drops the ends, where one term is 0."), ("3", "The complement."), ("4", "The complement.")])

P.qa(10, r"\(a_1 = \tfrac{1}{1\cdot2}\), \(a_2 = \tfrac{1}{2\cdot4}\), \(a_3 = \tfrac{1}{4\cdot7}\), \(a_4 = \tfrac{1}{7\cdot11}\), … Find \(a_1 + 2a_2 + 3a_3 + \dots + 10a_{10}\).", ["1", r"\(\tfrac{99}{100}\)", r"\(\tfrac{77}{78}\)", r"\(\tfrac{55}{56}\)"], "MCQ", "4", ["Algebra::Progressions_and_Series"], "Hard",
 "Consecutive denominators differ by k.",
 steps(("Telescoping", p(r"\(k a_k = \tfrac{1}{d_k} - \tfrac{1}{d_{k+1}}\), with d = 1, 2, 4, 7, 11, …, 46, 56.")),
       ("Sum", p(r"\(1 - \tfrac{1}{56} = \tfrac{55}{56}\)."))) + final("Option 4"),
 why_rows=[("1", "Infinite sum."), ("2", "Wrong last term."), ("3", "Wrong last term.")])

P.qa(11, r"How many real solutions does \(\tfrac{1}{3^x} + \tfrac{1}{5^x} = 6x - x^2 - 10\) have?", ["Infinitely many", "2", "1", "0"], "MCQ", "4", ["Algebra::Surds_and_Indices"], "Hard",
 "Complete the square on the right.",
 steps(("Right side", p("6x − x² − 10 = −1 − (x − 3)² < 0.")),
       ("Left side", p("Always positive. No solution."))) + final("Option 4"),
 why_rows=[("1", "Signs never match."), ("2", "Signs never match."), ("3", "Signs never match.")])

P.qa(12, r"How many integers x with −10 ≤ x ≤ 10 satisfy \(2x < \tfrac{x+1}{x}\)?", ["9", "10", "11", "12"], "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Split by the sign of x.",
 steps(("x < 0", p("2x² > x + 1, i.e. (x − 1)(2x + 1) > 0: x < −½. Integers −1 to −10.")),
       ("x > 0", p("(x − 1)(2x + 1) < 0: 0 < x < 1, no integer. x = 0 is excluded."))) + final("Option 2"),
 why_rows=[("1", "Misses one."), ("3", "Counts 0 or 1."), ("4", "Too many.")])

P.qa(13, "a and b are non-negative integers with a + 8 = c, b + 2 = c and a + b > c + 3. What is the least possible value of 2a + 3b − c?", [], "TITA", "34", ["Algebra::Linear_Equations"], "Medium",
 "b = a + 6, c = a + 8.",
 steps(("Condition", p("2a + 6 > a + 11, so a ≥ 6.")),
       ("Value", p("2a + 3(a + 6) − (a + 8) = 4a + 10, least at a = 6: 34."))) + final("34"))

P.qa(14, "A batsman averaged 35 in 9 innings and never scored more than 50 in an innings. His highest score in the first 5 innings was 31. What is the largest possible difference between his two lowest scores?", ["21", "27", "31", "32"], "MCQ", "3", ["Arithmetic::Average"], "Hard",
 "The second-lowest is at most 31.",
 steps(("Try", p("0, 31, 31, 31, 31 in the first five (124). The last four need 191, e.g. 47 + 48 + 48 + 48.")),
       ("Difference", p("31 − 0 = 31."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(15, "x and y are positive and x + y = 15. What is the largest value of x²y³?", [], "TITA", "26244", ["Algebra::Inequalities_and_Absolute_Value"], "Hard",
 "Split into x/2, x/2, y/3, y/3, y/3.",
 steps(("AM–GM", p("Five parts summing to 15 are equal at 3: x = 6, y = 9.")),
       ("Value", p("36 × 729 = 26,244."))) + final("26244"))

P.qa(16, "Stations P, Q, R and S lie in that order on a line. PQ is one-third of QR, and RS is half of PQ. Trains X and Y run non-stop from P to S. From P to Q, X is three times as fast as Y; from Q to R their speeds are swapped; from R to S they return to their first speeds. What is the ratio of X’s journey time to Y’s?", ["7 : 5", "5 : 7", "3 : 5", "5 : 3"], "MCQ", "1", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Let PQ = 2, QR = 6, RS = 1; Y’s first speed 1.",
 steps(("X", p("2/3 + 6/1 + 1/3 = 7.")),
       ("Y", p("2/1 + 6/3 + 1/1 = 5.")),
       ("Ratio", p("7 : 5."))) + final("Option 1"),
 why_rows=[("2", "Reversed."), ("3", "Slip."), ("4", "Slip.")])

P.qa(17, "An orchard has 100 flowering plants, each with red, blue or yellow flowers (some with more than one colour). 37 have red, 53 blue and 43 yellow; 15 have red and blue, 12 blue and yellow, and 13 red and yellow. How many have only red flowers?", ["25", "23", "17", "16"], "MCQ", "4", ["Modern_Maths::Set_Theory"], "Medium",
 "Inclusion–exclusion gives all three.",
 steps(("All three", p("100 = 37 + 53 + 43 − 40 + g, so g = 7.")),
       ("Only red", p("37 − (15 − 7) − (13 − 7) − 7 = 16."))) + final("Option 4"),
 why_rows=SLIP("1", "2", "3"))

P.qa(18, "Three solid cuboids of different metals each have a square cross-section of 49 cm². Each is melted and recast, without waste, into identical cubes of one metal, each cube having surface area 294 cm². Which could be the lengths (in cm) of the three cuboids?", ["91, 63, 154", "90, 63, 154", "91, 69, 152", "90, 69, 150"], "MCQ", "1", ["Geometry::Mensuration"], "Easy",
 "Cube face = 49, edge 7.",
 steps(("Rule", p("Each cuboid is 7 × 7 × L, so L must be a multiple of 7.")),
       ("Check", p("Only 91, 63, 154."))) + final("Option 1"),
 why_rows=[("2", "90."), ("3", "69, 152."), ("4", "90, 69, 150.")])

P.qa(19, "Money is shared among Prakash, Vikas and Bala. Prakash : Vikas = 3 : 5 and Vikas : Bala = 2 : 5. The largest share exceeds the smallest by ₹570. What is Prakash’s share in ₹?", ["150", "180", "120", "90"], "MCQ", "2", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Combine to 6 : 10 : 25.",
 steps(("Part", p("25 − 6 = 19 parts = 570, so 1 part = 30.")),
       ("Prakash", p("6 × 30 = 180."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(20, "John can finish a job in 15 days and David in 21 days. They start together, and John leaves after 5 days. How many more days does David take to finish?", ["14", "12", "9", "7"], "MCQ", "3", ["Arithmetic::Time_and_Work"], "Easy",
 "John does a third in 5 days.",
 steps(("David", p("David does the other two-thirds: 14 days in all.")),
       ("More days", p("14 − 5 = 9."))) + final("Option 3"),
 why_rows=[("1", "David’s total."), ("2", "Slip."), ("4", "Slip.")])

P.qa(21, "p and q are odd integers and r is even. Which is TRUE?", ["(p² + 2r)q³ is even.", "(2p + r²)q² is odd.", "(q⁴ + r³)(p + 2) is odd.", "(r³ − p³)(r + p) is even."], "MCQ", "3", ["Number_System::Miscellaneous"], "Easy",
 "Track parity.",
 steps(("Option 3", p("q⁴ odd + r³ even = odd; p + 2 odd; product odd."))) + final("Option 3"),
 why_rows=[("1", "Odd × odd: odd."), ("2", "Even × odd: even."), ("4", "Odd × odd: odd.")])

P.qa(22, "An investor can choose 20% a year compounded annually or 30% a year simple interest. The first option gives more only when the money stays invested for at least N whole years. What is N?", [], "TITA", "6", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "Compare 1.2ᴺ − 1 with 0.3N.",
 steps(("N = 5", p("1.2⁵ = 2.488: 148.8% against 150%.")),
       ("N = 6", p("1.2⁶ = 2.986: 198.6% against 180%. From here the compound option stays ahead."))) + final("6"))
