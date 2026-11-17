# -*- coding: utf-8 -*-
# Simp Mock 4: QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m04 import P
import m04_figs as F

SLIP = lambda *o: [(x, "Arithmetic slip.") for x in o]

P.qa(1, "A factory has 8 workers numbered 1 to 8. Worker n works (9 − n) hours a day, and the work he does each hour is proportional to n. A job is finished when all 8 work for one day. How many hours would worker 8 alone take to do the job?", [], "TITA", "15", ["Arithmetic::Time_and_Work"], "Medium",
 "Worker n does n·k units an hour for 9 − n hours.",
 steps(("Job", p("k(1·8 + 2·7 + 3·6 + 4·5 + 5·4 + 6·3 + 7·2 + 8·1) = 120k.")),
       ("Worker 8", p("8k an hour: 120k ÷ 8k = 15 hours."))) + final("15"))

P.qa(2, "A box holds cubes made either of wood or of metal, each red or green. There are three times as many red cubes as green. 44% of the red cubes and 48% of the green cubes are metal. What percentage of the cubes are wooden?", ["55", "52", "48", "45"], "MCQ", "1", ["Arithmetic::Percentages"], "Easy",
 "Take n green and 3n red.",
 steps(("Metal", p("0.44 × 3n + 0.48 × n = 1.8n.")),
       ("Wood", p("4n − 1.8n = 2.2n, which is 55%."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "The green metal share."), ("4", "The metal share.")])

P.qa(3, "x is positive and x² = 3x + 1. Find x³.", [r"\(18 - 5\sqrt{13}\)", r"\(18 + 5\sqrt{13}\)", r"\(15 + 5\sqrt{13}\)", r"\(18 + 3\sqrt{13}\)"], "MCQ", "2", ["Algebra::Surds_and_Indices"], "Medium",
 "Multiply the equation by x.",
 steps(("Reduce", p(r"\(x^3 = 3x^2 + x\) \(= 3(3x + 1) + x\) \(= 10x + 3\).")),
       ("x", p(r"\(x = \dfrac{3 + \sqrt{13}}{2}\) (the positive root).")),
       ("Answer", p(r"\(5(3 + \sqrt{13}) + 3 = 18 + 5\sqrt{13}\)."))) + final("Option 2"),
 why_rows=[("1", "Uses the negative root."), ("3", "Drops the +3."), ("4", "Arithmetic slip.")])

P.qa(4, "How many pairs (a, b) of integers satisfy a² + 48 = b²?", [], "TITA", "12", ["Number_System::Factors_and_Divisibility"], "Medium",
 "(b − a)(b + a) = 48, with both factors even.",
 steps(("Factor pairs", p("Both factors have the same parity, so both even: 2 × 24, 4 × 12, 6 × 8.")),
       ("Positive solutions", p("(a, b) = (11, 13), (4, 8), (1, 7).")),
       ("Signs", p("a and b can each be negated independently: 3 × 4 = 12 pairs."))) + final("12"))

P.qa(5, "Parallelogram ABCD has area 240 cm², ∠ABC = 150° and BC = 12 cm. Find the diagonal AC (in cm).", [r"\(4\sqrt{109 - 30\sqrt3}\)", r"\(4\sqrt{109 + 30\sqrt3}\)", r"\(4\sqrt{109 + 15\sqrt3}\)", r"\(2\sqrt{109 + 30\sqrt3}\)"], "MCQ", "2", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "Find AB from the area, then use the cosine rule at B.",
 steps(("AB", p("240 = 12 · AB · sin 150° = 6 · AB, so AB = 40.")),
       ("Cosine rule", p(r"\(AC^2 = 40^2 + 12^2 - 2 \cdot 40 \cdot 12 \cos 150°\) \(= 1744 + 480\sqrt3\).")),
       ("Simplify", p(r"\(1744 + 480\sqrt3 = 16(109 + 30\sqrt3)\), so \(AC = 4\sqrt{109 + 30\sqrt3}\) ≈ 50.9."))) + final("Option 2"),
 why_rows=[("1", "That is the shorter diagonal BD."), ("3", "Arithmetic slip."), ("4", "Forgets the factor 16 → 4.")])

P.qa(6, "A circle passes through (2, −2), (−2, 1) and (5, 2). The line 11y + 5x = c passes through its centre. Find c.", ["24", "16", "0", "−8"], "MCQ", "1", ["Geometry::Coordinate_Geometry"], "Medium",
 "Check for a right angle.",
 steps(("Right angle", p("From A(2, −2): AB = (−4, 3) and AC = (3, 4), dot product −12 + 12 = 0. So BC is a diameter.")),
       ("Centre", p("Midpoint of B(−2, 1) and C(5, 2): (3/2, 3/2).")),
       ("c", p("11 × 3/2 + 5 × 3/2 = 24."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(7, "For sets A and B, let A Δ B = (A ∪ B) − (A ∩ B). W = {a, b, c, d}, X = {b, c, e, f}, Y = {a, c, g, h, i} and Z = {b, d, i, j}. How many elements does (W Δ X) Δ (Y ∪ Z) have?", ["8", "6", "5", "7"], "MCQ", "1", ["Modern_Maths::Set_Theory"], "Easy",
 "Work out each part.",
 steps(("W Δ X", p("{a, d, e, f}.")), ("Y ∪ Z", p("{a, b, c, d, g, h, i, j}.")),
       ("Δ", p("Remove the common a and d from the union: {b, c, e, f, g, h, i, j}, 8 elements."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(8, "Rishabh buys equal numbers of two kinds of mango, paying ₹150 a dozen for one and ₹180 a dozen for the other. He sells them all at ₹170 a dozen and makes ₹500 profit. How many mangoes did he buy?", ["1080", "1200", "1320", "1344"], "MCQ", "2", ["Arithmetic::Profit_and_Loss"], "Easy",
 "Equal numbers: average cost ₹165 a dozen.",
 steps(("Profit per dozen", p("170 − 165 = ₹5.")),
       ("Dozens", p("500 ÷ 5 = 100 dozen = 1200 mangoes."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(9, "In an election, 3/7 of the voters promised to vote for Kushal and the rest for Vishal. 5% of Kushal’s promised voters switched to Vishal, and P% of Vishal’s switched to Kushal. The winning margin was 10% of all votes. Which of these can P be?", ["10", "15", "20", "25"], "MCQ", "4", ["Arithmetic::Percentages"], "Medium",
 "Take 70 voters: 30 and 40.",
 steps(("Votes", p("Kushal 28.5 + 0.4P, Vishal 41.5 − 0.4P. Difference |13 − 0.8P| = 7.")),
       ("Solve", p("P = 7.5 or 25."))) + final("Option 4"),
 why_rows=SLIP("1", "2", "3"))

P.qa(10, r"f(x + y) = f(x)·f(y) for positive integers x, y, and f(1) = 3. If \(f(a + 1) + f(a + 2) + \dots + f(a + n)\) \(= \dfrac{243(3^n - 1)}{2}\) for all n, find a.", [], "TITA", "4", ["Algebra::Functions"], "Easy",
 "f(n) = 3ⁿ.",
 steps(("Sum", p(r"\(3^{a+1} + \dots + 3^{a+n}\) \(= \dfrac{3^{a+1}(3^n - 1)}{2}\).")),
       ("Match", p("3<sup>a+1</sup> = 243 = 3⁵, so a = 4."))) + final("4"))

P.qa(11, "Basketball players of different heights stand in decreasing order of height from left to right. Leaving out the 5 players at the right end raises the average height by 2 cm; leaving out the 5 at the left end lowers it by 2 cm. The 5 at the left end total 920 cm and the 5 at the right end 680 cm. How many players are there?", [], "TITA", "65", ["Arithmetic::Average"], "Medium",
 "Write both averages and subtract.",
 steps(("Equations", p("(na − 680)/(n − 5) = a + 2 and (na − 920)/(n − 5) = a − 2.")),
       ("Subtract", p("240/(n − 5) = 4, so n = 65 (and a = 160)."))) + final("65"))

P.qa(12, "Bacteria population Alpha falls 20% every hour; population Beta falls 10% every hour. Starting together, they are equal after 4 hours. If Alpha started at 19,683 million, what was Beta’s starting population (in million)?", ["21228", "11288", "12288", "12828"], "MCQ", "3", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "A × 0.8⁴ = B × 0.9⁴.",
 steps(("Ratio", p("A : B = 9⁴ : 8⁴ = 6561 : 4096.")),
       ("Scale", p("19683 = 3 × 6561, so B = 3 × 4096 = 12,288."))) + final("Option 3"),
 why_rows=[("1", "Digits swapped."), ("2", "Digits swapped."), ("4", "Digits swapped.")])

P.qa(13, "Two runners, Ravi and Kiran, start together from the same point on a circular track and run in opposite directions at steady speeds. Between any two meetings Kiran always runs 50% farther than Ravi. Kiran runs a lap in 54 seconds. How many seconds does Ravi take for a lap?", ["81", "56", "45", "36"], "MCQ", "1", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Same time, so distances are in the ratio of speeds.",
 steps(("Speeds", p("Kiran : Ravi = 3 : 2.")),
       ("Lap", p("Ravi takes 54 × 3/2 = 81 seconds."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Uses 2/3 the wrong way.")])

P.qa(14, r"The cubic \(ax^3 + bx^2 + cx = 0\) (a ≠ 0) has three real roots α, β, γ. What is \(\tfrac1\alpha + \tfrac1\beta + \tfrac1\gamma\)?", ["1", "0", "3", "Undefined"], "MCQ", "4", ["Algebra::Equations_and_Polynomials"], "Easy",
 "There is no constant term.",
 steps(("Root 0", p("x = 0 is a root, so one of 1/α, 1/β, 1/γ is undefined, and so is the sum."))) + final("Option 4"),
 why_rows=[("1", "A root is 0."), ("2", "A root is 0."), ("3", "A root is 0.")])

P.qa(15, "How many ordered pairs of integers (x, y) satisfy 1/x + 1/y = 1/2?", ["7", "6", "5", "4"], "MCQ", "3", ["Number_System::Factors_and_Divisibility"], "Medium",
 "(x − 2)(y − 2) = 4.",
 steps(("Factor", p("(x − 2)(y − 2) = 4 with factor pairs (1, 4), (2, 2), (4, 1), (−1, −4), (−2, −2), (−4, −1).")),
       ("Check", p("These give (3, 6), (4, 4), (6, 3), (1, −2), (0, 0), (−2, 1). (0, 0) is not allowed: 5 pairs."))) + final("Option 3"),
 why_rows=[("1", "Counts extra pairs."), ("2", "Keeps (0, 0)."), ("4", "Misses one.")])

P.qa(16, "Bishnu and Sarathi start towards each other from the two ends of a 45 km path. Bishnu takes 3 hours longer than Sarathi to cover the whole path. Sarathi reaches Bishnu’s starting point 7 hours after Bishnu has covered one-third of the path. How many hours does Sarathi take for the whole path?", ["10", "12", "15", "18"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Let Sarathi take S hours.",
 steps(("Equation", p("Bishnu covers a third in (S + 3)/3 hours, so (S + 3)/3 + 7 = S.")),
       ("Solve", p("S + 24 = 3S, S = 12."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(17, "A filling station has four points. Point 1 has one small pipe, point 2 one large pipe, and points 3 and 4 one small and one large pipe each. Four identical empty tanks are attached, one at each point, and filling starts at the same time. Tanks 1, 2 and 3 are full at 6 PM, 9 AM and 6 AM on the same day. At point 4 the small and large pipes run alternately, one hour at a time, starting with the small pipe. When is tank 4 full? (All small pipes are identical, as are all large pipes.)", ["2 PM", "12 noon", "4 PM", "2:40 PM"], "MCQ", "2", ["Arithmetic::Time_and_Work"], "Hard",
 "If tank 3 takes x hours, tank 2 takes x + 3 and tank 1 takes x + 12.",
 steps(("Times", p("1/(x + 3) + 1/(x + 12) = 1/x gives x² = 36, x = 6. So both together 6 h, large 9 h, small 18 h; filling began at midnight.")),
       ("Alternating", p("With a 36-litre tank, small 2 L/h and large 4 L/h: 6 litres every 2 hours, so 12 hours (the last hour is the large pipe’s, and it finishes exactly).")),
       ("Time", p("Midnight + 12 h = 12 noon."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(18, "Let f(x) = min{2x², 52 − 5x} for real x. For how many integers x is f(x) = 2x²?", [], "TITA", "11", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "Solve 2x² ≤ 52 − 5x.",
 steps(("Inequality", p("2x² + 5x − 52 ≤ 0, that is (x − 4)(2x + 13) ≤ 0, so −6.5 ≤ x ≤ 4.")),
       ("Count", p("−6 to 4: 11 integers."))) + final("11"))

P.qa(19, "200 litres of a milk-water mixture is 10% water. How many litres of water must be added to make it 40% water?", [], "TITA", "100", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "The milk stays at 180 litres.",
 steps(("New total", p("180 litres must be 60%: 300 litres.")),
       ("Added", p("300 − 200 = 100."))) + final("100"))

P.qa(20, "Two circles, with centres O₁ and O₂, meet at B and C. P lies on line CB extended beyond B. PA touches the circle with centre O₁ at A, and a line through P cuts the circle with centre O₂ at D and E (D nearer P). PA = 12 cm and PE = 16 cm. Find DE (in cm)." + F.CIRC2, [], "TITA", "7", ["Geometry::Circles"], "Easy",
 "Both circles share the power of P: PB · PC.",
 steps(("Power of P", p("PA² = PB · PC = PD · PE.")),
       ("PD", p("144 = PD × 16, so PD = 9.")),
       ("DE", p("16 − 9 = 7."))) + final("7"))

P.qa(21, "f(xy) = f(x)·f(y) for all positive integers x and y, and f(2) ≠ f(3). Find f(1).", [], "TITA", "1", ["Algebra::Functions"], "Easy",
 "Put x = y = 1.",
 steps(("f(1)", p("f(1) = f(1)², so f(1) is 0 or 1.")),
       ("Rule out 0", p("If f(1) = 0, then f(2) = f(2)f(1) = 0 = f(3), which is not allowed."))) + final("1"))

P.qa(22, r"If \(7^x = 9^y = 3969\), what is \(\dfrac{2xy}{x + y}\)?", ["1", "2", "4", "8"], "MCQ", "3", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "3969 = 63² = (7 × 9)².",
 steps(("Reciprocals", p(r"\(\tfrac1x = \log_{3969} 7\), \(\tfrac1y = \log_{3969} 9\), so \(\tfrac1x + \tfrac1y = \log_{3969} 63 = \tfrac12\).")),
       ("Answer", p(r"\(\dfrac{2xy}{x + y} = \dfrac{2}{1/x + 1/y} = 4\)."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))
