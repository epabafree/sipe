# -*- coding: utf-8 -*-
# Simp Mock 6: QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m06 import P

SLIP = lambda *o: [(x, "Arithmetic slip.") for x in o]

P.qa(1, "ABCD is a parallelogram with A(4, 5), B(−1, 1) and D(5, −3). Find C.", ["(0, −6)", "(0, −7)", "(−6, −7)", "(−6, −6)"], "MCQ", "2", ["Geometry::Coordinate_Geometry"], "Easy",
 "The diagonals bisect each other: A + C = B + D.",
 steps(("C", p("C = B + D − A = (−1 + 5 − 4, 1 − 3 − 5) = (0, −7)."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(2, "In how many ways can 12 children be split into three groups of four, the groups not being labelled?", ["5775", "34650", "15400", "11550"], "MCQ", "1", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Divide by 3! for unlabelled groups.",
 steps(("Count", p("12! ÷ (4!·4!·4!·3!) = 34650 ÷ 6 = 5775."))) + final("Option 1"),
 why_rows=[("2", "Treats the groups as labelled."), ("3", "Arithmetic slip."), ("4", "Divides by 3 instead of 3!.")])

P.qa(3, "A milkman doubles the volume of pure milk by adding water, then adds pure milk to increase the volume by a further 25%. What percentage of the final mixture is milk?", [], "TITA", "60", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Start with 2 litres of milk.",
 steps(("Steps", p("2 L milk + 2 L water = 4 L. Add 1 L milk: 3 L milk in 5 L.")), ("Share", p("60%."))) + final("60"))

P.qa(4, "x, y and z are different primes with (xy + zx)(x + z) = 1001. Find x² + y² + z².", [], "TITA", "150", ["Number_System::Factors_and_Divisibility"], "Medium",
 "(xy + zx)(x + z) = x(y + z)(x + z), and 1001 = 7 × 11 × 13.",
 steps(("Parity", p("All three factors are odd, so y + z and x + z are odd: z = 2.")),
       ("Factors", p("x and x + 2 are two of 7, 11, 13: x = 11, x + 2 = 13, and y + 2 = 7, so y = 5.")),
       ("Sum", p("121 + 25 + 4 = 150."))) + final("150"))

P.qa(5, "p, q, r and n are non-zero reals with 2pn + q = 0, and f(x) = px² + qx + r. If |p| > p, which is correct?", ["f(n) = f(n − 5)", "f(n) < f(n + 5)", "f(n) > f(n + 5)", "f(n) < f(n − 5)"], "MCQ", "3", ["Algebra::Quadratic_Equations"], "Easy",
 "|p| > p means p < 0.",
 steps(("Vertex", p("n = −q/(2p) is the vertex, and p < 0 makes it a maximum.")),
       ("Compare", p("f(n) is larger than f at any other point, including n + 5."))) + final("Option 3"),
 why_rows=[("1", "Equal only for points symmetric about n."), ("2", "f(n) is the maximum."), ("4", "f(n) is the maximum.")])

P.qa(6, "Walking at 8 km/h, a man reaches his office 10 minutes late; at 12 km/h he is 4 minutes early. One day, a motorcyclist leaves the office as the man leaves home at 8 km/h, meets him on the way and takes him back to the office, arriving exactly on time. Find the motorcycle’s speed. (Ignore time for turning or getting on.)", ["13.0 km/h", "12.5 km/h", "12.0 km/h", "11.5 km/h"], "MCQ", "1", ["Arithmetic::Time_Speed_and_Distance"], "Hard",
 "D/8 − D/12 = 14 minutes.",
 steps(("Distance", p("D/24 = 14/60, so D = 5.6 km; on time means 42 − 10 = 32 minutes.")),
       ("Meeting", p("The motorcycle rides out and back the same stretch, so it meets him at the halfway time: 16 minutes.")),
       ("Speed", p("Together they close 5.6 km in 16 minutes: 21 km/h, so the motorcycle does 21 − 8 = 13 km/h."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(7, "Three different primes have average 97, the largest two-digit prime. Adding a fourth prime, larger than each of the three, makes the average 101, the smallest three-digit prime. How many such sets of four primes are there?", ["0", "1", "2", "3"], "MCQ", "3", ["Number_System::Miscellaneous"], "Medium",
 "The fourth prime is 404 − 291 = 113.",
 steps(("Fourth", p("113, so the other three are primes below 113 adding to 291.")),
       ("Search", p("Largest 109: the other two add to 182, giving 79 + 103. Largest 107: 184, giving 83 + 101. Smaller largest values give nothing.")),
       ("Count", p("2 sets."))) + final("Option 3"),
 why_rows=[("1", "Two sets exist."), ("2", "Misses one."), ("4", "Only two.")])

P.qa(8, "Ram and Shyam stand in a queue of more than 240 but fewer than 250 people, with 7 people between them. The ratio of people ahead of Ram to people behind Shyam is 12 : 13. How many people are in the queue?", [], "TITA", "243", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "Try Ram ahead of Shyam, then Shyam ahead.",
 steps(("Ram ahead", p("Total 12k + 13k + 9 = 25k + 9: 234 or 259, out of range.")),
       ("Shyam ahead", p("The groups overlap: total 25k − 7. k = 10 gives 243."))) + final("243"))

P.qa(9, "A trader mixes 5 kg, 7 kg and 10 kg of three kinds of rice and marks the mixture to make ₹286 profit. She sells half at the marked price and half at 20% off, making ₹250 profit. What did she pay for all the rice (in ₹)?", [], "TITA", "74", ["Arithmetic::Profit_and_Loss"], "Medium",
 "The discount cost ₹36.",
 steps(("Discount", p("20% of the marked price of half the rice = 286 − 250 = 36, so the marked price of all of it is 2 × 180 = ₹360.")),
       ("Cost", p("360 − 286 = ₹74."))) + final("74"))

P.qa(10, "3 < x < 4, and |x − a| + |x − b| = 4 with a ≤ 3 and b ≥ 4. What are the smallest possible a and the largest possible b?", ["0, 5", "0, 4", "1, 6", "0, 7"], "MCQ", "4", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "x lies between a and b, so b − a = 4.",
 steps(("Distance", p("|x − a| + |x − b| = b − a = 4.")),
       ("Extremes", p("Smallest a with b ≥ 4: a = 0. Largest b with a ≤ 3: b = 7."))) + final("Option 4"),
 why_rows=[("1", "Largest b is 7."), ("2", "Largest b is 7."), ("3", "a can go down to 0.")])

P.qa(11, "A square sheet and a triangular sheet are joined along an edge, without overlap, to form a trapezium of area 660 cm². The triangle has area 84 cm². Find the perimeter of the triangle (in cm).", [], "TITA", "56", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "The square is 576 cm².",
 steps(("Square", p("660 − 84 = 576: side 24.")),
       ("Triangle", p("A right triangle on one side of the square (making a trapezium): ½ × 24 × b = 84, b = 7, hypotenuse 25.")),
       ("Perimeter", p("7 + 24 + 25 = 56."))) + final("56"))

P.qa(12, r"f(x) is the smallest integer greater than or equal to x. Find \(\sum_{x=1}^{100} f\left(\tfrac27 + \tfrac{x}{49}\right)\).", ["175", "179", "181", "183"], "MCQ", "3", ["Algebra::Functions"], "Medium",
 "2/7 + x/49 = (14 + x)/49.",
 steps(("Values", p("1 for x = 1–35; 2 for x = 36–84; 3 for x = 85–100.")),
       ("Sum", p("35 + 98 + 48 = 181."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(13, "In a college, men and women students are in the ratio 17 : 19. Each takes Humanities or Commerce. Half the Humanities students are women; in Commerce, men and women are 7 : 9. There are 91 men in Commerce. How many students are there?", [], "TITA", "468", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "Commerce 7c and 9c, Humanities h and h.",
 steps(("Ratio", p("(7c + h) : (9c + h) = 17 : 19 gives h = 10c.")),
       ("c", p("7c = 91, c = 13, h = 130.")),
       ("Total", p("16 × 13 + 260 = 468."))) + final("468"))

P.qa(14, "One kind of mango costs 12.5% more than another. A trader buys 50 kg of each, sells 25 kg of the dearer kind at 12% profit and 30 kg of the cheaper kind at 10% profit, and the remaining 45 kg at ₹57 a kg, making 11% profit overall. What did he pay per kg for the dearer kind?", [], "TITA", "54", ["Arithmetic::Profit_and_Loss"], "Medium",
 "Cheaper kind ₹d, dearer ₹1.125d.",
 steps(("Cost", p("50d + 56.25d = 106.25d.")),
       ("Revenue", p("25 × 1.125d × 1.12 + 30d × 1.1 + 45 × 57 = 64.5d + 2565 = 1.11 × 106.25d.")),
       ("Solve", p("53.4375d = 2565, d = 48; the dearer kind costs ₹54."))) + final("54"))

P.qa(15, "Real numbers x and y satisfy x(y² + x² + 2y²) = 158 and y(x² + y² + 2x²) = 185. Find (x + y)² + 1.", ["37", "49", "50", "65"], "MCQ", "3", ["Algebra::Equations_and_Polynomials"], "Easy",
 "x³ + 3xy² and y³ + 3x²y add to (x + y)³.",
 steps(("Add", p("(x + y)³ = 343, so x + y = 7.")), ("Answer", p("49 + 1 = 50."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(16, "A man invests 37.5% of his savings in scheme A for 4 years and the rest in scheme B for 3 years, both at simple interest, earning equal interest from each. A pays 15% a year. What does B pay?", ["8%", "10%", "11.25%", "12%"], "MCQ", "4", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "0.375 × 4 × 15 = 0.625 × 3 × r.",
 steps(("Solve", p("22.5 = 1.875r, r = 12."))) + final("Option 4"),
 why_rows=SLIP("1", "2", "3"))

P.qa(17, "90 people visited a cafe that serves samosa, pav bhaji and sandwiches; each ordered at least one. 40 ordered samosa, 35 pav bhaji and 56 sandwiches. At most how many ordered exactly one kind?", ["68", "69", "70", "71"], "MCQ", "2", ["Modern_Maths::Set_Theory"], "Medium",
 "Orders total 131: 41 more than people.",
 steps(("Extra orders", p("Exactly-two people add 1 each and all-three people add 2: n₂ + 2n₃ = 41.")),
       ("Maximise singles", p("Make n₂ + n₃ smallest: n₃ = 20, n₂ = 1, so singles = 90 − 21 = 69 (it fits: 19 samosa only, 15 pav bhaji only, 35 sandwich only)."))) + final("Option 2"),
 why_rows=[("1", "Not the most."), ("3", "Would need n₂ + n₃ = 20, impossible with n₂ + 2n₃ = 41."), ("4", "Too many.")])

P.qa(18, "The sum of the first N terms of an AP is 2N + 3N². What is the smallest N for which the Nth term is composite?", ["6", "7", "8", "9"], "MCQ", "1", ["Algebra::Progressions_and_Series"], "Easy",
 "The Nth term is 6N − 1.",
 steps(("Terms", p("5, 11, 17, 23, 29, 35, …: 35 = 5 × 7 at N = 6."))) + final("Option 1"),
 why_rows=[("2", "N = 6 already works."), ("3", "N = 6 already works."), ("4", "N = 6 already works.")])

P.qa(19, "A rhombus circumscribes a circle, and the quadrilateral formed by joining the midpoints of the rhombus’s sides is a square. C is the circle’s circumference and S the rhombus’s perimeter. Find C : S. (Use π = 22/7.)", ["11 : 14", "14 : 11", "7 : 11", "11 : 7"], "MCQ", "1", ["Geometry::Circles"], "Medium",
 "Joining the midpoints of a rhombus gives a rectangle; it is a square only when the diagonals are equal.",
 steps(("Square", p("A rhombus with equal diagonals is a square, of side 2r.")),
       ("Ratio", p("2πr : 8r = π : 4 = 22/7 : 4 = 11 : 14."))) + final("Option 1"),
 why_rows=[("2", "Upside down."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(20, "In a group of 20, 8 are women. The women’s average weight is a whole number of kg greater than 50 and less than 55; the men’s average is 1/3 kg more. The total weight is a perfect square. Find the women’s average weight (in kg).", [], "TITA", "51", ["Arithmetic::Average"], "Easy",
 "Total = 8w + 12(w + 1/3) = 20w + 4.",
 steps(("Try", p("w = 51: 1024 = 32². w = 52, 53, 54 give 1044, 1064, 1084, none square."))) + final("51"))

P.qa(21, r"If \(x = \dfrac{78^{95} - 77^{95}}{78^{94} + 77^{94}}\), which is true?", ["x < 0.1", "0.1 < x < 0.5", "0.5 < x < 1", "x > 1"], "MCQ", "4", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"Compare the numerator with the denominator.",
 steps(("Numerator", p(r"\(78^{95} - 77^{95} > 78^{95} - 77 \cdot 78^{94} = 78^{94}\).")),
       ("Compare", p(r"Also \(78^{95} - 77^{95} = 78 \cdot 78^{94} - 77 \cdot 77^{94}\) \(> 78^{94} + 77^{94}\) since \(77 \cdot 78^{94} > 78 \cdot 77^{94}\). So x > 1."))) + final("Option 4"),
 why_rows=[("1", "x is well above 1."), ("2", "x is well above 1."), ("3", "x is well above 1.")])

P.qa(22, r"Find the remainder when \((176 \times 512)^{10!}\) is divided by 100.", ["12", "44", "36", "76"], "MCQ", "4", ["Number_System::Remainders"], "Medium",
 "176 × 512 ≡ 12 (mod 100). Split 100 into 4 × 25.",
 steps(("Mod 4", p("12 is a multiple of 4, so the power is 0 mod 4.")),
       ("Mod 25", p(r"\(12^{20} \equiv 1\) (mod 25) and 20 divides 10!, so the power is 1 mod 25.")),
       ("Combine", p("The number ending in a multiple of 4 and ≡ 1 mod 25 is 76."))) + final("Option 4"),
 why_rows=[("1", "12 is the base, not the power."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])
