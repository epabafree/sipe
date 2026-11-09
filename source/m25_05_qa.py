# -*- coding: utf-8 -*-
# Simp Mock 5 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_05 import P
import m25_05_figs as F

P.qa(1, "Hardik joined a company on 1 January 2024 and agreed to work for 3 months at a monthly salary of ₹25000. Based on his performance, the company increased his monthly salary by 60% with effect from 1 April 2024. Hardik’s monthly expenditure throughout the year was 20% more than his average monthly salary in the first three months. If he managed the deficit in the first three months by borrowing from friends at zero interest, then his annual savings, as a percentage of his annual expenditure, is _____ .",
 [r"\(20\tfrac23\%\)", r"\(20\tfrac34\%\)", r"\(20\tfrac45\%\)", r"\(20\tfrac56\%\)"], "MCQ", "4", ["Arithmetic::Percentages"], "Easy",
 "Expenditure is ₹30000 every month; salary is ₹25000 for 3 months and ₹40000 for 9.",
 steps(("Year", p(r"Income: \(3 \times 25000 + 9 \times 40000 = 435000\). Spending: \(12 \times 30000 = 360000\).")),
       ("Savings", p(r"\(75000 \div 360000 = \tfrac{5}{24} = 20\tfrac56\%\)."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(2, "In how many ways can 8 identical mangoes be distributed among two or more friends, without cutting them, such that each friend receives at least one mango?", [], "TITA", "127", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "Line up the 8 mangoes; each of the 7 gaps can be a split or not.",
 steps(("Splits", p(r"Each choice of split points gives an ordered distribution with every friend getting at least one: \(2^7 = 128\).")),
       ("Two or more", p("Remove the case with no split (one friend): 127."))) + final("127"))

P.qa(3, r"Find the value of \(\dfrac{a^2b^2c^2 + 1}{abc}\), given that \(a + \dfrac1b = m\), \(b + \dfrac1c = n\) and \(c + \dfrac1a = p\).",
 [r"\(m(np - 1) - (n - p)\)", r"\(m(np - 1) + (n + p)\)", r"\(m(np + 1) - (n + p)\)", r"\(m(np - 1) - (n + p)\)"], "MCQ", "4", ["Algebra::Equations_and_Polynomials"], "Medium",
 "The expression is \\(abc + \\tfrac1{abc}\\). Expand \\(mnp\\).",
 steps(("Expand", p(r"Multiplying out, \(mnp = abc + \dfrac1{abc}\) \(+ \left(a + \tfrac1b\right) + \left(b + \tfrac1c\right)\) \(+ \left(c + \tfrac1a\right)\).")),
       ("So", p(r"\(mnp = abc + \tfrac1{abc} + m + n + p\), giving \(abc + \tfrac1{abc} = mnp - m - n - p\) \(= m(np - 1) - (n + p)\)."))) + final("Option 4"),
 why_rows=[("1", "Sign of p wrong."), ("2", "Adds n + p."), ("3", "np + 1 is wrong.")])

P.qa(4, r"If \(x\) is a real number and \(n\) is an integer, find the number of possible values of \(n\) such that the minimum value of \(f(x) = |x + 2| + |x - n| + |x - 8|\) is 10.", [], "TITA", "11", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "The minimum of a sum of distances is at the median point.",
 steps(("Minimum", p(r"At \(x = \) median of \(\{-2, n, 8\}\). If \(-2 \le n \le 8\), the minimum is the spread \(8 - (-2) = 10\). Outside that range it is larger.")),
       ("Count", p(r"\(n = -2, -1, \dots, 8\): 11 values."))) + final("11"))

P.qa(5, r"If \(a^{-1} + b^{-1} + c^{-1} = 0\) and \(a = 2b\), then the value of \((a + b + c)^2 + a^2 + b^2 + c^2\) is:",
 [r"\(\dfrac{98}{4}b^2\)", r"\(\dfrac{49}{9}b^2\)", r"\(\dfrac{98}{4}a^2\)", r"\(\dfrac{98}{9}b^2\)"], "MCQ", "4", ["Algebra::Equations_and_Polynomials"], "Medium",
 "\\(\\tfrac1a + \\tfrac1b + \\tfrac1c = 0\\) means \\(ab + bc + ca = 0\\).",
 steps(("Simplify", p(r"With \(ab + bc + ca = 0\), \((a + b + c)^2 = a^2 + b^2 + c^2\), so the expression is \(2(a^2 + b^2 + c^2)\).")),
       ("c", p(r"\(\tfrac1{2b} + \tfrac1b = -\tfrac1c\) gives \(c = -\tfrac{2b}3\).")),
       ("Value", p(r"\(2\left(4b^2 + b^2 + \tfrac{4b^2}9\right) = 2 \cdot \tfrac{49b^2}9 = \tfrac{98}9 b^2\)."))) + final("Option 4"),
 why_rows=[("1", "Wrong denominator."), ("2", "Forgets to double."), ("3", "In terms of a, and wrong.")])

P.qa(6, "A tea seller mixes two varieties of tea, one costing ₹100 per kg and the other ₹160 per kg. He plans to sell the mixture at ₹140 per kg for a profit of 30%. By mistake, he adds 20% more of the expensive variety than intended, keeping the quantity of the cheaper variety unchanged. He still charges the customer only for the quantity he intended to supply. Find his actual profit percentage.",
 ["21%", "22.33%", "23%", "25.23%"], "MCQ", "4", ["Arithmetic::Mixture_and_Alligation"], "Hard",
 "Planned cost price: \\(140 \\div 1.3 = \\tfrac{1400}{13}\\) per kg. Find the planned ratio.",
 steps(("Ratio", p(r"\(\tfrac{1400}{13} - 100 = \tfrac{100}{13}\) and \(160 - \tfrac{1400}{13} = \tfrac{680}{13}\): cheap : expensive = 680 : 100 = 34 : 5.")),
       ("Planned", p(r"34 kg + 5 kg = 39 kg, sold for \(39 \times 140 = 5460\).")),
       ("Actual cost", p(r"\(34 \times 100 + 6 \times 160 = 4360\). Profit: \(1100 \div 4360 \approx 25.23\%\)."))) +
 trap("Divide the profit by the actual cost (₹4360), not the planned cost (₹4200).") + final("Option 4"),
 why_rows=[("1", "Wrong ratio."), ("2", "Wrong ratio."), ("3", "Wrong ratio.")])

P.qa(7, r"If \(p\) and \(q\) are the roots of \(x^2 + cx - (c^2 + 1) = 0\), where \(c > 0\) and \(|p - q| = 7\), then the values of \(p\) and \(q\) (in any order) are _____ .",
 ["4, −3", "−5, 2", "6, −1", "10, 3"], "MCQ", "2", ["Algebra::Quadratic_Equations"], "Easy",
 "\\((p - q)^2 = (p + q)^2 - 4pq\\).",
 steps(("c", p(r"\(49 = c^2 + 4(c^2 + 1) = 5c^2 + 4\), so \(c = 3\).")),
       ("Roots", p(r"\(x^2 + 3x - 10 = (x + 5)(x - 2)\)."))) + final("−5 and 2, option 2"),
 why_rows=[("1", "Sum must be −3."), ("3", "Product must be −10."), ("4", "Product must be −10.")])

P.qa(8, "The average of all 4-digit natural numbers of the form xyxy that are divisible by 12, where x and y are two distinct digits, is ____.", [], "TITA", "5454", ["Number_System::Factors_and_Divisibility"], "Medium",
 "\\(\\overline{xyxy} = 101 \\times \\overline{xy}\\), and 101 is coprime to 12.",
 steps(("Two-digit part", p("\\(\\overline{xy}\\) must be a two-digit multiple of 12: 12, 24, 36, 48, 60, 72, 84, 96. All have distinct digits.")),
       ("Average", p(r"Average of \(\overline{xy}\): \(432 \div 8 = 54\). So the average is \(101 \times 54 = 5454\)."))) + final("5454"))

P.qa(9, F.TRI + p("In the diagram, BD bisects the median AE at F, and AF = 3.25 cm. If AD = 4 cm and BC = 13 cm, find the area (in sq. cm) of △ABC."), [], "TITA", "30", ["Geometry::Triangles"], "Hard",
 "AE = 6.5 = BE = EC. What does that say about angle A?",
 steps(("Right angle", p(r"\(AE = 2 \times 3.25 = 6.5\), half of BC. The median equals half the side, so E is the circumcentre and \(\angle A = 90^\circ\).")),
       ("AC", p(r"A line from B through the midpoint of median AE cuts AC at the point one-third of the way from A (mass points: B and C weigh 1 each, A weighs 2). So \(AC = 3 \times AD = 12\).")),
       ("Area", p(r"\(AB = \sqrt{13^2 - 12^2} = 5\). Area \(= \tfrac12 \times 5 \times 12 = 30\)."))) + final("30"),
 concept=p("<b>Median = half the side</b> means a right angle at the opposite vertex."))

P.qa(10, "Container A has 80 litres of oil, 50% of which is pure olive oil. Container B has 120 litres of oil, 30% of which is pure olive oil. All of A is poured into B; then 40 litres of the mixture are removed and replaced with pure olive oil. Find the percentage of olive oil in the final mixture in B.",
 ["47.3%", "39.8%", "48.5%", "50.4%"], "MCQ", "4", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Combine first, then remove a fifth.",
 steps(("Combined", p("Olive: 40 + 36 = 76 of 200 litres.")),
       ("Replace", p(r"Removing 40 litres leaves \(76 \times 0.8 = 60.8\); adding 40 gives 100.8 of 200: 50.4%."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Forgets the added olive oil."), ("3", "Arithmetic slip.")])

P.qa(11, "In an infinite geometric progression of positive real numbers with common ratio less than one, the ratio of the first term to the sum of the second and third terms is 25 : 36, and the ratio of the sum of all terms from the fourth term onwards to the sum of the second and third terms is 16 : 9. The common ratio of the GP is _________ .",
 [r"\(\tfrac34\)", r"\(\tfrac45\)", r"\(\tfrac15\)", r"\(\tfrac14\)"], "MCQ", "2", ["Algebra::Progressions_and_Series"], "Medium",
 "\\(\\dfrac{a}{ar + ar^2} = \\dfrac{25}{36}\\).",
 steps(("First ratio", p(r"\(r^2 + r = \tfrac{36}{25}\), so \(25r^2 + 25r - 36 = 0\): \(r = \tfrac45\).")),
       ("Check", p(r"\(\dfrac{ar^3/(1 - r)}{ar(1 + r)} = \dfrac{r^2}{1 - r^2}\) \(= \dfrac{16/25}{9/25} = \dfrac{16}9\). ✓"))) + final("Option 2"),
 why_rows=[("1", r"\(\tfrac34 + \tfrac9{16} \ne \tfrac{36}{25}\)."), ("3", "Too small."), ("4", "Too small.")])

P.qa(12, "A number is formed by writing all positive multiples of 4 side by side in ascending order (4812162024…). What is the position, from the left, of the 15th ‘0’ in this number?", [], "TITA", "126", ["Number_System::Miscellaneous"], "Hard",
 "Count digits block by block and zeros as you go.",
 steps(("Up to 96", p("4 and 8 take positions 1–2. The 22 two-digit multiples 12–96 take positions 3–46, with zeros in 20, 40, 60 and 80: 4 zeros.")),
       ("100 to 196", p("100 (positions 47–49) has 2 zeros, 104 and 108 one each: 8 so far. 120, 140, 160 and 180 add one each: 12 zeros. 196 ends at position 46 + 25 × 3 = 121.")),
       ("Next", p("200 takes positions 122–124: zeros 13 and 14 at 123 and 124. 204 takes 125–127, and its 0 at position 126 is the 15th."))) + final("126"))

P.qa(13, F.CIRC + p("In the diagram, O is the centre of the circle. ∠BAC and ∠ACD are right angles. AB = 12, AC = 2 and CD = 14. What is the radius of the circle?"),
 ["8", "10", "12", "14"], "MCQ", "2", ["Geometry::Circles"], "Medium",
 "Put A at the origin and use coordinates.",
 steps(("Points", p(r"A(0, 0), B(0, −12), C(2, 0), D(2, −14). A, B, D lie on the circle.")),
       ("Centre", p(r"From chord AB, the centre has \(y = -6\). Equal distances to A and D: \(h^2 + 36 = (h - 2)^2 + 64\), so \(h = 8\).")),
       ("Radius", p(r"\(\sqrt{8^2 + 6^2} = 10\)."))) + final("10, option 2"),
 why_rows=[("1", "The centre’s x-coordinate."), ("3", "AB."), ("4", "CD.")])

P.qa(14, "A, B and C work 8 hours a day. B works twice as fast as A. Three times the work C completes in a day equals 4 times the work A and B together complete in a day. If all three work together, the project is completed in one day. How many days will A alone take to finish the project?",
 ["4", "12", "7", "8"], "MCQ", "3", ["Arithmetic::Time_and_Work"], "Easy",
 "Let A’s daily rate be a.",
 steps(("Rates", p(r"B = 2a; \(3C = 4(a + 2a)\), so C = 4a. Together: 7a = 1 project a day.")),
       ("A alone", p("7 days."))) + final("Option 3"),
 why_rows=[("1", "C alone, roughly."), ("2", "Wrong rates."), ("4", "Wrong rates.")])

P.qa(15, r"What is the sum of the squares of all the values of \(x\) satisfying \(\log_2\left(\dfrac{x - 2}{x - 6}\right) = \log_4\left(\dfrac{x - 2}{x - 4}\right) - \dfrac12\)?", [], "TITA", "20", ["Algebra::Logarithms_and_Exponents"], "Hard",
 "Write everything in base 2: \\(\\log_4 y = \\tfrac12 \\log_2 y\\).",
 steps(("Base 2", p(r"\(2\log_2\dfrac{x - 2}{x - 6} = \log_2\dfrac{x - 2}{x - 4} - 1\), so \(\left(\dfrac{x - 2}{x - 6}\right)^2 = \dfrac{x - 2}{2(x - 4)}\).")),
       ("Solve", p(r"\(x \ne 2\): \(2(x - 2)(x - 4) = (x - 6)^2\), so \(x^2 = 20\).")),
       ("Domain", p(r"Both log arguments must be positive: \(x < 2\) or \(x > 6\). \(x = \sqrt{20} \approx 4.47\) fails; \(x = -\sqrt{20}\) works. Sum of squares: 20."))) + final("20"))

P.qa(16, "Find the remainder when 63836383… (200 digits) is divided by 9999.", ["9181", "9998", "9191", "9881"], "MCQ", "1", ["Number_System::Remainders"], "Medium",
 "\\(10^4 \\equiv 1 \\pmod{9999}\\): add the 4-digit blocks.",
 steps(("Blocks", p(r"200 digits = 50 blocks of 6383. Each block is worth 6383 mod 9999: \(50 \times 6383 = 319150\).")),
       ("Reduce", p(r"\(319150 - 31 \times 9999 = 9181\)."))) + final("9181, option 1"),
 why_rows=[("2", "Not the block sum."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(17, r"Two functions are defined for all real \(x\): \(f(x) = |3 - x|\) and \(g(x) = |x - 3|\). Find the value of \(f \circ g \circ f \circ g \circ \dots \circ f \circ g\,(10)\).", ["1", "2", "3", "Cannot be determined"], "MCQ", "2", ["Algebra::Functions"], "Medium",
 "f and g are the same function. Apply it repeatedly to 10.",
 steps(("Iterate", p(r"\(10 \to 7 \to 4 \to 1\) \(\to 2 \to 1 \to 2 \to \dots\)")),
       ("Even count", p("The chain applies an even number of functions (f, g pairs). After four or more steps, an even count always lands on 2."))) + final("2, option 2"),
 why_rows=[("1", "Odd number of steps."), ("3", "Not reached."), ("4", "The pattern settles.")])

P.qa(18, "Pipes P and Q can each act as an inlet or an outlet, but not both at the same time. Working alone as an inlet, pipe P can fill a tank in 30 minutes, and pipe Q in 45 minutes. Pipe P’s flow is 50% lower when emptying than when filling. Pipe Q’s flow is 11.11% higher when filling than when emptying. What is the absolute difference (in minutes) between the times taken to fill the tank in two configurations: first, P inlet and Q outlet; second, Q inlet and P outlet?", [], "TITA", "105", ["Arithmetic::Time_and_Work"], "Medium",
 "11.11% = 1/9: Q’s filling rate is 10/9 of its emptying rate.",
 steps(("Rates", p(r"P: fills \(\tfrac1{30}\), empties \(\tfrac1{60}\). Q: fills \(\tfrac1{45}\), empties \(\tfrac9{10} \times \tfrac1{45} = \tfrac1{50}\).")),
       ("Times", p(r"P in, Q out: \(\tfrac1{30} - \tfrac1{50} = \tfrac1{75}\): 75 min. Q in, P out: \(\tfrac1{45} - \tfrac1{60} = \tfrac1{180}\): 180 min.")),
       ("Difference", p("105 minutes."))) + final("105"))

P.qa(19, "A bus uses only diesel and runs a total distance of 400 km non-stop at constant speed. Apart from fuel, the only other expense is the driver’s wage of ₹300 per hour. The volume of diesel (in litres) used per kilometre is directly proportional to the speed (in km/h). Diesel costs ₹100 per litre. If the bus runs at 50 km/h, the total expense for 400 km is ₹27400. If the total expense for 400 km is only ₹32000, what is the maximum time (in hours) for which the bus can run non-stop?",
 [r"\(6\tfrac23\)", "60", "100", "120"], "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Hard",
 "Expense = fuel (grows with speed) + wages (shrink with speed).",
 steps(("Constant", p(r"Litres per km \(= kv\). At 50 km/h: fuel \(400 \times 50k \times 100 = 2{,}000{,}000k\), wages \(8 \times 300 = 2400\). So \(k = \tfrac1{80}\).")),
       ("Equation", p(r"Expense \(= 500v + \tfrac{120000}{v} = 32000\), so \(v^2 - 64v + 240 = 0\): \(v = 60\) or \(4\).")),
       ("Longest time", p(r"At 4 km/h: \(400 \div 4 = 100\) hours."))) + final("100, option 3"),
 why_rows=[("1", "The time at 60 km/h, the shortest."), ("2", "A speed, not a time."), ("4", "Not a root.")])

P.qa(20, "A sum of ₹2560000 is borrowed from a bank for 5 years at r% per annum, compounded annually. The interest accrued in the 3rd and 4th years is ₹405000 and ₹455625 respectively. If ₹P is invested in a simple-interest scheme at r% per annum for 5 years, the total amount at the end of 5 years is ₹44707. The value of P is _________ .",
 ["28312", "27512", "29712", "26912"], "MCQ", "2", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Consecutive years’ interest grow by the factor (1 + r).",
 steps(("Rate", p(r"\(455625 \div 405000 = 1.125\), so \(r = 12.5\%\).")),
       ("P", p(r"\(P(1 + 5 \times 0.125) = 1.625P = 44707\), so \(P = 27512\)."))) + final("Option 2"),
 why_rows=[("1", "Wrong rate."), ("3", "Wrong rate."), ("4", "Wrong rate.")])

P.qa(21, "Abhay is driving along a road at 40 km/h. Santosh, 200 metres behind him, travels in the same direction at a constant speed. Sanjay, 1 kilometre ahead of Abhay, is coming from the opposite direction at the same speed as Santosh. Santosh and Sanjay both cross Abhay at exactly the same moment. What is Sanjay’s speed in km/h?", [], "TITA", "60", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Relative speeds: s − 40 for Santosh, s + 40 for Sanjay.",
 steps(("Same time", p(r"\(\dfrac{0.2}{s - 40} = \dfrac{1}{s + 40}\), so \(0.2s + 8 = s - 40\) and \(s = 60\)."))) + final("60"))

P.qa(22, "How many six-digit numbers can be formed using the digits 3, 4, 5, 6, 7 and 8, without repetition, such that the digit in the hundreds place is greater than the digit in the units place?", [], "TITA", "360", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Swap the hundreds and units digits: the numbers pair up.",
 steps(("Symmetry", p(r"6! = 720 numbers; in exactly half, hundreds > units: 360."))) + final("360"))
