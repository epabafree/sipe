# -*- coding: utf-8 -*-
# Simp Mock 11: QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m11 import P

SLIP = lambda *o: [(x, "Arithmetic slip.") for x in o]

P.qa(1, "ABCD is a parallelogram with A(−3, −4), B(2, 6) and C(−6, 10). What is its area in square units?", ["120", "100", "96", "72"], "MCQ", "2", ["Geometry::Coordinate_Geometry"], "Easy",
 "Check angle B.",
 steps(("Sides", p("AB² = 125, BC² = 80, AC² = 205 = 125 + 80, so angle B is 90°: a rectangle.")),
       ("Area", p(r"\(\sqrt{125} \times \sqrt{80} = 100\)."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(2, "How many five-digit numbers have digit sum 9?", [], "TITA", "495", ["Modern_Maths::Permutations_and_Combinations"], "Hard",
 "Stars and bars; no digit can exceed 9 anyway.",
 steps(("All strings", p("⁹⁺⁴C₄ = ¹³C₄ = 715.")),
       ("Leading zero", p("First digit 0: ¹²C₃ = 220.")),
       ("Answer", p("715 − 220 = 495."))) + final("495"))

P.qa(3, "Cars P and Q drive the 270 km from city X to city Y. Car P is already 30 km along when Q starts. Both drive the first 90 km at 60 km/h, the next 90 km at 90 km/h and the last 90 km at 120 km/h. How far apart (in km) are they when P reaches Y?", ["60", "55", "50", "45"], "MCQ", "1", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "P needs 1 + 1 + ¾ hours.",
 steps(("P", p("60 km at 60, 90 at 90, 90 at 120: 2 h 45 min.")),
       ("Q", p("In that time: 90 + 90 + 120 × ¼ = 210 km.")),
       ("Gap", p("270 − 210 = 60."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(4, "A milkman mixes 30 litres of pure milk with 10 litres of a milk–water solution; the result is 12.5% water. Had he sold just the 10 litres of solution at the cost price of pure milk, what would his profit percentage have been?", [], "TITA", "100", ["Arithmetic::Profit_and_Loss"], "Easy",
 "All the water came from the 10 litres.",
 steps(("Water", p("12.5% of 40 = 5 litres, half the solution.")),
       ("Profit", p("He pays for 5 litres of milk and sells 10: 100%."))) + final("100"))

P.qa(5, "a, b, c are non-negative integers with a + bc = 49 and ab + c = 50. What is the smallest possible a + b + c?", [], "TITA", "35", ["Algebra::Linear_Equations"], "Medium",
 "Subtract: (b − 1)(a − c) = 1.",
 steps(("Case b = 2", p("a − c = 1, a + 2c = 49: a = 17, c = 16. Sum 35.")),
       ("Case b = 0", p("a = 49, c = 50. Sum 99.")),
       ("Least", p("35."))) + final("35"))

P.qa(6, r"f(x) = N(x) ÷ D(x) for real x, where \(N(x) = 9x^4 + 72x^3\) \(+\, 222x^2 + 312x + 170\) and \(D(x) = 3x^2 + 12x + 13\). M is the least value of f. Which is true?", ["1 ≤ M < 2", "2 ≤ M < 3", "3 ≤ M < 4", "4 ≤ M < 5"], "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Hard",
 "The numerator is (denominator)² + 1.",
 steps(("Rewrite", p("With y = 3x² + 12x + 13 = 3(x + 2)² + 1 ≥ 1, f = y + 1/y.")),
       ("Least", p("y + 1/y ≥ 2, reached at y = 1 (x = −2). M = 2."))) + final("Option 2"),
 why_rows=[("1", "M is 2."), ("3", "Too high."), ("4", "Too high.")])

P.qa(7, "Three sisters average 17 years. With their brother included, the average of the four is an odd whole number. If the brother is at least 2, what is his least possible age?", ["3", "5", "9", "13"], "MCQ", "3", ["Arithmetic::Average"], "Easy",
 "51 + b must be 4 × an odd number.",
 steps(("Try", p("52 needs b = 1; 56 gives average 14 (even); 60 gives 15 with b = 9."))) + final("Option 3"),
 why_rows=[("1", "Average 13.5."), ("2", "Average 14, even."), ("4", "Not the least.")])

P.qa(8, "p is an even natural number and q an odd one. (17ᵖ − 12ᵖ)(7ᵠ + 2ᵠ) is certainly divisible by:", ["3", "87", "261", "All of the above"], "MCQ", "4", ["Number_System::Factors_and_Divisibility"], "Easy",
 "aⁿ − bⁿ (n even) divides by a + b; aⁿ + bⁿ (n odd) by a + b.",
 steps(("Factors", p("29 divides the first, 9 the second: 261 divides the product.")),
       ("So", p("3, 87 and 261 all divide it."))) + final("Option 4"),
 why_rows=[("1", "Also 87, 261."), ("2", "Also 3, 261."), ("3", "Also 3, 87.")])

P.qa(9, "Jameela buys 7 kg of apricots, 13 kg of blackberries and 8 kg of cherries. 9 kg of apricots cost the same as 24 kg of blackberries or 16 kg of cherries. She mixes them and sets a price P per kg that would give ₹90 profit on the whole lot. In fact she sells 21 kg at 20% above P and the rest at P, making ₹300 profit. How much (in ₹) did the blackberries cost her?", [], "TITA", "390", ["Arithmetic::Profit_and_Loss"], "Hard",
 "Prices per kg in ratio 16 : 6 : 9.",
 steps(("Cost", p("7 × 16k + 13 × 6k + 8 × 9k = 262k.")),
       ("Equations", p("28P = 262k + 90 and 32.2P = 262k + 300, so 4.2P = 210, P = 50, k = 5.")),
       ("Blackberries", p("13 × 6 × 5 = 390."))) + final("390"))

P.qa(10, r"\(4 + \sqrt3\) is a root of ax² + px + q = 0 and \(5 + \sqrt2\) a root of ay² + my + n = 0, where a, p, q, m, n are integers. Find \(\tfrac{2(p + q)}{m} - \tfrac{5p - 4q}{n}\).", ["3", "1", "2", "5"], "MCQ", "1", ["Algebra::Quadratic_Equations"], "Medium",
 "Conjugate roots.",
 steps(("Coefficients", p("p = −8a, q = 13a, m = −10a, n = 23a.")),
       ("Value", p("2(5a)/(−10a) = −1; (−40a − 52a)/(23a) = −4. −1 − (−4) = 3."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(11, "Four circles of radius 12 sit inside a larger circle; each touches two of the others externally and the large circle internally. Find the large circle’s radius.", [r"\(24\sqrt2\)", r"\(12 + 12\sqrt2\)", r"\(12 + 24\sqrt2\)", r"\(24 + 24\sqrt2\)"], "MCQ", "2", ["Geometry::Circles"], "Easy",
 "Centres form a square of side 24.",
 steps(("Centres", p(r"Half-diagonal: \(12\sqrt2\).")),
       ("Radius", p(r"\(12\sqrt2 + 12\)."))) + final("Option 2"),
 why_rows=[("1", "Diagonal only."), ("3", "Full diagonal plus r."), ("4", "Diameter.")])

P.qa(12, "f(p) + 2f(1 − p) = p + 3 for all p. Find f(2).", [r"\(\tfrac13\)", r"\(-\tfrac13\)", r"\(-\tfrac72\)", r"\(\tfrac32\)"], "MCQ", "2", ["Algebra::Functions"], "Medium",
 "Use p = 2 and p = −1.",
 steps(("Equations", p("f(2) + 2f(−1) = 5 and f(−1) + 2f(2) = 2.")),
       ("Solve", p("−3f(2) = 1, so f(2) = −⅓."))) + final("Option 2"),
 why_rows=[("1", "Sign slip."), ("3", "Slip."), ("4", "Slip.")])

P.qa(13, r"Find \(\left(\dfrac{5 \cdot 13^3 + 5 \cdot 17^3 + 5 \cdot 19^3}{5 \cdot 91^3 + 5 \cdot 119^3 + 5 \cdot 133^3}\right)^{-1/3}\).", [], "TITA", "7", ["Algebra::Surds_and_Indices"], "Medium",
 "91 = 7 × 13, 119 = 7 × 17, 133 = 7 × 19.",
 steps(("Ratio", p("The fraction is 1/7³.")),
       ("Power", p(r"\((7^{-3})^{-1/3} = 7\)."))) + final("7"))

P.qa(14, "N people finish 42% of a project working 7 hours a day for 8 days. Then 14 leave, and the rest finish it in 16 days at 6 hours a day. Find N.", ["36", "72", "66", "58"], "MCQ", "2", ["Arithmetic::Time_and_Work"], "Medium",
 "56N : 96(N − 14) = 42 : 58.",
 steps(("Solve", p("3248N = 4032N − 56,448, so N = 72."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(15, "a, b ≥ 0 with a² + ab + 3a = 25 and b² + ab + 3b = 45. Find (a + b)².", ["100", "42.25", "49", "72.25"], "MCQ", "3", ["Algebra::Quadratic_Equations"], "Easy",
 "Add the equations.",
 steps(("Sum", p("(a + b)(a + b + 3) = 70, so a + b = 7.")),
       ("Square", p("49."))) + final("Option 3"),
 why_rows=[("1", "Uses −10."), ("2", "Slip."), ("4", "Slip.")])

P.qa(16, "₹78,000 is split 4 : 6 : 3 between schemes A (5% simple interest), B (10% compound, yearly) and C (20% compound, yearly). What is the ratio of the interest earned in three years, A : B : C?", ["100 : 331 : 364", "120 : 331 : 364", "120 : 331 : 336", "100 : 333 : 336"], "MCQ", "1", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "Amounts 24,000, 36,000, 18,000.",
 steps(("Interest", p("A 3600; B 36,000 × 0.331 = 11,916; C 18,000 × 0.728 = 13,104.")),
       ("Ratio", p("Divide by 36: 100 : 331 : 364."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(17, "₹1 lakh is invested on day 1. On day n (n ≥ 2) its value rises by 1/n of the previous day’s value. On day k it has appreciated by 500%. Find k.", ["10", "11", "12", "None of these"], "MCQ", "2", ["Algebra::Progressions_and_Series"], "Medium",
 "Telescoping product.",
 steps(("Value", p("After day k: (3/2)(4/3)…((k + 1)/k) = (k + 1)/2 times.")),
       ("Six times", p("(k + 1)/2 = 6, so k = 11."))) + final("Option 2"),
 why_rows=[("1", "Off by one."), ("3", "Off by one."), ("4", "11 works.")])

P.qa(18, r"\(P = \tfrac{1}{1 \cdot 3} + \tfrac{1}{3 \cdot 5} + \tfrac{1}{5 \cdot 7} + \dots\) to 30 terms. Find 122P.", [], "TITA", "60", ["Algebra::Progressions_and_Series"], "Medium",
 "Last term 1/(59 × 61).",
 steps(("Telescoping", p(r"\(P = \tfrac12\left(1 - \tfrac{1}{61}\right) = \tfrac{30}{61}\).")),
       ("Answer", p("122 × 30/61 = 60."))) + final("60"))

P.qa(19, "A rectangle has area 50 cm². What is the least possible length of its diagonal (in cm)?", [], "TITA", "10", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "x² + y² ≥ 2xy.",
 steps(("Bound", p("d² = x² + y² ≥ 100, equal for a square.")),
       ("Answer", p("10."))) + final("10"))

P.qa(20, r"Let \(S = 21(10^2 + 11^2)(10^4 + 11^4)(10^8 + 11^8)\). Find n if \(\sqrt[4]{S + 10000^n} = 14641\).", ["16", "12", "4", "2"], "MCQ", "3", ["Algebra::Surds_and_Indices"], "Medium",
 "21 = (11 − 10)(11 + 10).",
 steps(("Product", p(r"The product telescopes to \(11^{16} - 10^{16}\).")),
       ("Solve", p(r"\(14641^4 = 11^{16}\), so \(10000^n = 10^{16}\) and n = 4."))) + final("Option 3"),
 why_rows=[("1", "Power of 10, not of 10000."), ("2", "Slip."), ("4", "Slip.")])

P.qa(21, "Cycling at 15 km/h a man arrives at 2 p.m.; at 20 km/h he arrives at 12 noon. At what speed must he cycle to arrive at 1 p.m.?", [r"\(15\tfrac12\) km/h", r"\(17\tfrac17\) km/h", r"\(16\tfrac23\) km/h", "20 km/h"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Times differ by 2 hours.",
 steps(("Time", p("At 20 km/h he takes t hours: 20t = 15(t + 2), t = 6; distance 120 km.")),
       ("Speed", p("120 ÷ 7 = 17⅐ km/h."))) + final("Option 2"),
 why_rows=[("1", "Not 120/7."), ("3", "Not 120/7."), ("4", "Arrives at noon.")])

P.qa(22, "4x + 3|y| + 2y = 19 and 3x + |x| + 5y = 1. Find 4x + 5y.", ["0", "−1", "1", r"\(\tfrac12\)"], "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Hard",
 "Try the four sign cases.",
 steps(("x ≥ 0, y < 0", p("4x − y = 19 and 4x + 5y = 1 give x = 4, y = −3, which fit.")),
       ("Others", p("y ≥ 0 with x ≥ 0 is inconsistent; the x < 0 cases give positive x.")),
       ("Value", p("16 − 15 = 1."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))
