# -*- coding: utf-8 -*-
# Simp Mock 18 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_18 import P
import m25_18_figs as F

P.qa(1, r"What is the absolute value of the smallest integer x with \(x^3 - 20 > 4x - 5x^2\)?", [], "TITA", "4", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "Factorise the cubic.",
 steps(("Factor", p(r"\(x^3 + 5x^2 - 4x - 20\) \(= (x - 2)(x + 2)(x + 5) > 0\).")), ("Solve", p("−5 < x < −2 or x > 2: smallest integer −4."))) + final("4"))

P.qa(2, "Vijay walks up a down-moving escalator at a steady pace. At 2 steps a second he takes 60 steps to reach the top; at 3 steps a second, 45 steps. How many steps does he take at 4 steps a second?", ["42", "40", "36", "32"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Steps on the escalator = time × (walking speed − escalator speed).",
 steps(("Escalator", p("30(2 − e) = 15(3 − e) gives e = 1; 30 steps.")), ("At 4", p("30 ÷ 3 = 10 seconds, so 40 steps."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(3, "A circle touches the x-axis at (24, 0) but does not touch the y-axis. Its nearest point is 18 units from the origin. Its farthest point is N units from the origin. Find N.", ["30", "32", "36", "38"], "MCQ", "2", ["Geometry::Coordinate_Geometry"], "Medium",
 "Centre (24, r).",
 steps(("Radius", p(r"\(\sqrt{576 + r^2} - r = 18\) gives 36r = 252, r = 7; centre 25 from the origin.")), ("Farthest", p("25 + 7 = 32."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(4, "A boat takes 5 hours in all to go 36 km downstream and 16 km upstream. Its speed in still water is 10 km/h. What is the speed of the current (km/h)?", ["1", "2", "3", "4"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Try the options.",
 steps(("w = 2", p("36 ÷ 12 + 16 ÷ 8 = 3 + 2 = 5. ✓ (The equation reduces to (w − 2)² = 0.)"))) + final("Option 2"),
 why_rows=[("1", "Gives 5.05 h."), ("3", "Gives 5.06 h."), ("4", "Gives 5.25 h.")])

P.qa(5, r"N is a positive integer with \(N = \dfrac{160!}{12^n}\). What is the largest possible n?", ["72", "74", "76", "78"], "MCQ", "3", ["Number_System::Factorials"], "Medium",
 r"\(12^n = 2^{2n} \cdot 3^n\).",
 steps(("Twos", p("80 + 40 + 20 + 10 + 5 + 2 + 1 = 158: up to 79 fours.")), ("Threes", p("53 + 17 + 5 + 1 = 76.")), ("n", p("The smaller, 76."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Uses the twos.")])

P.qa(6, "A teacher shares her prize money of ₹X equally among some students. With five fewer students, each would get ₹2 more; with four more students, each would get ₹1 less. If each student got ₹4 more than they actually did, how many students would there be?", ["8", "9", "10", "12"], "MCQ", "4", ["Algebra::Linear_Equations"], "Easy",
 "n students, ₹p each.",
 steps(("Equations", p("2n − 5p = 10 and 4p − n = 4 give n = 20, p = 6: X = 120.")), ("At ₹10 each", p("120 ÷ 10 = 12."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(7, r"\(f(x) = x^3 + ax^2 + bx + c\), with integer a, b, c, is divisible by x − 2, x − 3 and x − 5. For an integer x, which of these cannot be the remainder when f(x) is divided by 7?", ["0", "3", "5", "6"], "MCQ", "2", ["Number_System::Remainders"], "Medium",
 "f(x) = (x − 2)(x − 3)(x − 5); try x = 0 to 6.",
 steps(("Values mod 7", p("x = 0: −30 ≡ 5; 1: −8 ≡ 6; 4: −2 ≡ 5; 6: 12 ≡ 5; 2, 3, 5: 0.")), ("Missing", p("Only 0, 5, 6 occur."))) + final("Option 2"),
 why_rows=[("1", "x = 2."), ("3", "x = 0."), ("4", "x = 1.")])

P.qa(8, "Class A has boys and girls in the ratio 3 : 7; class B has girls and boys in the ratio 4 : 11. The class strengths are in the ratio 5 : 3. Both classes gather in the auditorium, and then a group four times as large, with boys and girls in the ratio 1 : 4, joins them. What percentage of those in the auditorium are boys?", ["25.25%", "27.50%", "32.50%", "34.25%"], "MCQ", "1", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Take 50 and 30 students.",
 steps(("Classes", p("Boys 15 + 22 = 37 of 80.")), ("Newcomers", p("320, of whom 64 boys.")), ("Share", p("101 of 400 = 25.25%."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(9, "A workshop makes handcrafted tables. Its fixed cost is ₹20,000 a day and each table costs ₹4,000 to make. At ₹8,000 a table it sells 30 a day; each ₹500 rise in price loses one sale a day. If the price can only change from ₹8,000 in steps of ₹500, what is the largest daily profit?", ["₹1,52,000", "₹1,60,500", "₹1,66,000", "₹1,55,500"], "MCQ", "2", ["Algebra::Quadratic_Equations"], "Medium",
 "x price steps: profit (4000 + 500x)(30 − x) − 20,000.",
 steps(("Profit", p(r"\(-500x^2 + 11000x + 100000\), largest at x = 11.")), ("Value", p("−60,500 + 1,21,000 + 1,00,000 = 1,60,500."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(10, "ABCDEF is a regular hexagon. HK ⊥ BF, with H on AF and K on BF, and AB = BK = 6 cm. Find HK." + F.HEX, [r"\((6 + \sqrt3)\) cm", r"\((6 - \sqrt3)\) cm", r"\((6 + 2\sqrt3)\) cm", r"\((6 - 2\sqrt3)\) cm"], "MCQ", "4", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "Drop AN ⊥ BF; △ANF ∼ △HKF.",
 steps(("Lengths", p(r"AN = 3, BN = NF = \(3\sqrt3\), so KF = \(6\sqrt3 - 6\).")),
       ("Similar", p(r"\(\tfrac{HK}{KF} = \tfrac{AN}{NF} = \tfrac{1}{\sqrt3}\): \(HK = 6 - 2\sqrt3\)."))) + final("Option 4"),
 why_rows=[("1", "Sign and factor slips."), ("2", "Factor slip."), ("3", "Sign slip.")])

P.qa(11, "In a 45-minute test for n participants, the average completion time was 20 minutes. One participant took 28 minutes; without him the average was 19 minutes. Times are whole minutes, the shortest was 16 minutes, and no one finished at the last minute. What is the longest time any participant could have taken?", [], "TITA", "40", ["Arithmetic::Average"], "Easy",
 "20n − 28 = 19(n − 1).",
 steps(("n", p("n = 9; total 180.")), ("Maximise", p("Seven at 16, one at 28: 180 − 112 − 28 = 40."))) + final("40"))

P.qa(12, r"Let \(N = 2025^{2050}\). How many divisors of N are multiples of \(2025^{2025}\)?", [], "TITA", "5151", ["Number_System::Factors_and_Divisibility"], "Easy",
 r"Such a divisor is \(2025^{2025} \times\) a divisor of \(2025^{25}\).",
 steps(("Count", p(r"\(2025^{25} = 3^{100} \cdot 5^{50}\): 101 × 51 = 5151 divisors."))) + final("5151"))

P.qa(13, "In △ABC, AB = 12 and BC = 24. D is on AC with AD = 8, and ∠ABD = ∠ACB. The area of △BDC is:", ["Less than 55", "Between 55 and 57", "Between 57 and 59", "Between 59 and 61"], "MCQ", "3", ["Geometry::Triangles"], "Medium",
 "△ABC ∼ △ADB.",
 steps(("Sides", p(r"\(AB^2 = AD \cdot AC\): AC = 18, CD = 10; BD = 24 × 12 ÷ 18 = 16.")),
       ("Heron", p(r"Sides 10, 16, 24, s = 25: \(\sqrt{25 \cdot 15 \cdot 9 \cdot 1} = 15\sqrt{15} \approx 58.1\)."))) + final("Option 3"),
 why_rows=[("1", "Too small."), ("2", "Too small."), ("4", "Too big.")])

P.qa(14, "What is the probability that an 8-digit odd number is divisible by 25?", [r"\(\tfrac1{25}\)", r"\(\tfrac1{20}\)", r"\(\tfrac1{50}\)", r"\(\tfrac1{10}\)"], "MCQ", "1", ["Modern_Maths::Probability"], "Easy",
 "Only the last two digits matter.",
 steps(("Endings", p("Odd endings: 10 × 5 = 50 equally likely; 25 and 75 work.")), ("Probability", p("2 ÷ 50 = 1/25."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Counts one ending."), ("4", "Arithmetic slip.")])

P.qa(15, "Arjun and Bhavin start a spice export business. Arjun puts in ₹2,00,000 for the whole year. Bhavin puts in ₹1,20,000 and adds ₹60,000 after 4 months. Chitra joins after 3 months with ₹1,50,000. The year’s profit is ₹1,44,000. First each partner is paid 6% annual interest on capital for the time it was used; the rest of the profit is shared in proportion to capital × months. What does Bhavin get in all?", ["₹40,932", "₹47,762", "₹48,762", "₹49,232"], "MCQ", "3", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "Interest is also proportional to capital × months.",
 steps(("Capital-months (₹ thousand)", p("Arjun 2400, Bhavin 480 + 1440 = 1920, Chitra 1350: 80 : 64 : 45.")),
       ("Bhavin", p("Interest and share both follow this ratio: 1,44,000 × 64 ÷ 189 ≈ 48,762."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(16, r"If \(8.246^p = 0.008246^q = 10^7\), find \(\tfrac1p - \tfrac1q\).", [r"\(\tfrac12\)", r"\(\tfrac37\)", r"\(\tfrac47\)", r"\(\tfrac73\)"], "MCQ", "2", ["Algebra::Logarithms_and_Exponents"], "Easy",
 r"\(\tfrac1p = \tfrac{\log 8.246}{7}\).",
 steps(("Difference", p(r"\(\tfrac17\log\tfrac{8.246}{0.008246} = \tfrac17\log 10^3 = \tfrac37\)."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Inverted.")])

P.qa(17, r"How many terms does the expansion of \((1 + x + x^2)^{10}\) have?", [], "TITA", "21", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Powers from 0 to 20.", steps(("Count", p("Every power 0–20 appears: 21 terms."))) + final("21"))

P.qa(18, "Two sprinters start together from the same point of a circular track and run the same way at different steady speeds. They meet at the start and at exactly two other points, each 400 m from the start along the track (the shorter way). The faster one runs 10 laps in 25 minutes. Which could be the slower one’s speed (m/s)?", ["1.75", "2", "2.5", "3"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Three meeting points: speeds in a coprime ratio (n + 3) : n; track 1200 m.",
 steps(("Faster", p("12,000 m in 1,500 s = 8 m/s.")), ("Slower", p("8n ÷ (n + 3): n = 1 gives 2; 1.75, 2.5 and 3 need non-integer n."))) + final("Option 2"),
 why_rows=[("1", "No whole n."), ("3", "No whole n."), ("4", "No whole n.")])

P.qa(19, "A necklace has 6 precious stones: one natural diamond and five artificial stones of different colours. In how many ways can the necklace be made?", ["360", "60", "120", "720"], "MCQ", "2", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Six distinct beads on a necklace.", steps(("Count", p(r"\(\tfrac{(6 - 1)!}{2} = 60\) (rotations and flips are the same necklace)."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Ignores flips."), ("4", "Ignores both.")])

P.qa(20, "A sum invested at simple interest amounts to ₹19,840 after 4 years and ₹22,720 after 7 years. After how many years does the amount first exceed ₹30,000?", ["13", "15", "17", "19"], "MCQ", "2", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "₹960 a year.",
 steps(("Need", p("30,000 − 22,720 = 7,280: 8 more years (7,680).")), ("Year", p("7 + 8 = 15."))) + final("Option 2"),
 why_rows=[("1", "Not yet."), ("3", "Not the first."), ("4", "Not the first.")])

P.qa(21, "A chair’s marked price is 40% above cost, and it sells at the marked price. If the cost rose 30% and the marked price 20%, selling at the new marked price would cut the profit by ₹15. What is the profit (₹) if the chair is sold at 10% off the original marked price?", [], "TITA", "195", ["Arithmetic::Profit_and_Loss"], "Easy",
 "On cost 100, profit falls from 40 to 38.",
 steps(("Scale", p("A fall of 2 is ₹15, so cost = ₹750, marked ₹1,050.")), ("Profit", p("945 − 750 = 195."))) + final("195"))

P.qa(22, "A spy must visit three bases B, C and D, starting and ending at the hideout A. Distances: A–B 5 km, A–C 8 km, A–D 10 km, B–C 6 km, B–D 7 km, C–D 9 km. Add up the lengths of all the different routes that start at A, visit each base exactly once and return to A.", [], "TITA", "180", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "3! = 6 orders.",
 steps(("Routes", p("A–B–C–D–A 30, A–B–D–C–A 29, A–C–B–D–A 31, and each in reverse.")), ("Sum", p("2 × (30 + 29 + 31) = 180."))) + final("180"))
