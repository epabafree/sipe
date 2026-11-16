# -*- coding: utf-8 -*-
# Simp Mock 2: QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m02 import P
import m02_figs as F

SLIP = lambda *o: [(x, "Arithmetic slip.") for x in o]

P.qa(1, "A copper sulphate solution has strength x% if 100 ml of it contains x g of copper sulphate. Three solutions of different strengths are mixed. In the ratio 5 : 3 : 2 the mixture has strength 32%; in the ratio 3 : 2 : 5 it has strength 37%; in equal volumes it has strength 35%. What is the highest strength (in %) among the three solutions?", ["45", "48", "50", "52"], "MCQ", "1", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Three linear equations in the strengths a, b, c.",
 steps(("Equations", p("5a + 3b + 2c = 320, 3a + 2b + 5c = 370, a + b + c = 105.")),
       ("Eliminate", p("First minus twice the third: 3a + b = 110. Second minus twice the third: a + 3c = 160.")),
       ("Solve", p("Substituting b = 110 − 3a and c = (160 − a)/3 into a + b + c = 105 gives a = 25, so b = 35 and c = 45.")),
       ("Check", p("125 + 105 + 90 = 320 ✓."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(2, "Twelve turtles were tracked on a beach in Goa. Each type-A turtle covered 19,300 units and each type-B turtle 13,000 units, 1,87,500 units in all. If the numbers of type-A and type-B turtles were swapped, how would the total change?", ["12,600 units more", "38,600 units more", "26,000 units less", "6,300 units more"], "MCQ", "1", ["Algebra::Linear_Equations"], "Easy",
 "Find the split, then swap.",
 steps(("Split", p("a + b = 12 and 19300a + 13000b = 187500 give 6300a = 31500: a = 5, b = 7.")),
       ("Swap", p("Two more A’s and two fewer B’s: 2 × (19300 − 13000) = 12,600 more."))) + final("Option 1"),
 why_rows=[("2", "Two A’s, not the difference."), ("3", "Wrong direction."), ("4", "Only one turtle’s change.")])

P.qa(3, "PQRSTU is a regular hexagon with side 12 cm. A lies on PU and B lies on RS, with PA = BS = 8 cm. Find AB." + F.HEX, ["8√7 cm", "10 cm", "4√21 cm", "12√3 cm"], "MCQ", "1", ["Geometry::Polygons_and_Quadrilaterals"], "Hard",
 "A and B are mirror images through the centre O, so AB = 2·OA.",
 steps(("Symmetry", p("P and S are opposite vertices, as are U and R. A is 8 from P along PU and B is 8 from S along SR, so B is A rotated 180° about the centre O.")),
       ("OA", p(r"In triangle OPU (equilateral, side 12), A is 8 from P. By the cosine rule with angle 60° at P:") + p(r"\(OA^2 = 12^2 + 8^2 - 2 \cdot 12 \cdot 8 \cdot \tfrac12 = 112\)")),
       ("AB", p(r"\(AB = 2\sqrt{112} = 8\sqrt7\) ≈ 21.2 cm."))) + final("Option 1"),
 why_rows=[("2", "Far too short."), ("3", "≈ 18.3 cm."), ("4", "≈ 20.8 cm, the distance between opposite sides.")])

P.qa(4, "A function f on the natural numbers, with natural-number values, satisfies f(ab) = f(a) f(b) for all natural a and b, and f(3) > f(2) > f(1). If f(54) = 375, find f(48).", ["395", "405", "415", "425"], "MCQ", "2", ["Algebra::Functions"], "Medium",
 "f(1) = 1, and 54 = 2 · 3³.",
 steps(("f(1)", p("f(2) = f(1) f(2), so f(1) = 1.")),
       ("54", p(r"\(f(2) \cdot f(3)^3 = 375 = 3 \cdot 5^3\). f(3) > 1, and 5 is the only cube root available, so f(3) = 5, f(2) = 3.")),
       ("48", p(r"\(48 = 2^4 \cdot 3\): \(3^4 \times 5 = 405\)."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(5, "C is 100 km from A, and B and D lie on the road in the order A, B, D, C. AB is 25% of AD, and DC is 25% of BC. Ashish usually rides A to B at 10 km/h and B to C at 20 km/h. Today he rode A to D at his usual average speed for A to C, and the rest at 6.25 km/h. What was his average speed today from A to C?", ["16.67 km/h", "15.07 km/h", "14.7 km/h", "12.5 km/h"], "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Find AB : BD : DC first.",
 steps(("Distances", p("AB : BD = 1 : 3 and BD : DC = 3 : 1, so AB : BD : DC = 1 : 3 : 1: 20, 60 and 20 km.")),
       ("Usual", p("2 h + 4 h = 6 h, so the usual average is 100/6 km/h.")),
       ("Today", p("AD = 80 km takes 80 ÷ (100/6) = 4.8 h; DC takes 20 ÷ 6.25 = 3.2 h. 100 ÷ 8 = 12.5 km/h."))) + final("Option 4"),
 why_rows=[("1", "The usual average."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(6, "From a rhombus-shaped sheet with side 70 cm and area 1960 cm², the largest possible circular disc is cut out. What is the circumference of the disc (in cm)? (Use π = 22/7.)", [], "TITA", "88", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "The largest circle in a rhombus is its incircle; its diameter is the rhombus’s height.",
 steps(("Height", p("Area = side × height: 1960 = 70h, so h = 28 cm and r = 14 cm.")),
       ("Circumference", p("2 × 22/7 × 14 = 88."))) + final("88"))

P.qa(7, "A shopkeeper bought 100 shirts. He sold 50% of them at 10% profit, 20% of the rest at 15% profit and 30% of what was then left at 20% profit. The remaining shirts went in a sale at the MRP, which is 25% above cost, with one shirt free for every 6 bought. If one customer bought all the sale shirts, what was his overall profit percentage?", ["1.09", "10.90", "10.00", "11.87"], "MCQ", "2", ["Arithmetic::Profit_and_Loss"], "Medium",
 "Take cost ₹1 a shirt; count shirts at each stage.",
 steps(("Before the sale", p("50 shirts at 0.10 = 5; 10 at 0.15 = 1.5; 12 at 0.20 = 2.4.")),
       ("Sale", p("28 shirts left = 4 lots of 6 paid + 1 free. Each lot brings 6 × 1.25 = 7.5 for a cost of 7: profit 0.5, so 2 in all.")),
       ("Total", p("5 + 1.5 + 2.4 + 2 = 10.9 on a cost of 100: 10.9%."))) + final("Option 2"),
 why_rows=[("1", "Decimal slip."), ("3", "Arithmetic slip."), ("4", "Charges for every sale shirt.")])

P.qa(8, "How many pairs of integers (a, b) satisfy a ≤ b ≤ −10 and 2b − 3a = 69?", ["18", "19", "20", "21"], "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "b must be a multiple of 3.",
 steps(("Form", p("3a = 2b − 69, so b = 3k and a = 2k − 23.")),
       ("Bounds", p("b ≤ −10 gives k ≤ −4. a ≤ b gives 2k − 23 ≤ 3k, so k ≥ −23.")),
       ("Count", p("k from −23 to −4: 20 values."))) + final("Option 3"),
 why_rows=[("1", "Drops both ends."), ("2", "Drops one end."), ("4", "Counts one too many.")])

P.qa(9, "A shopkeeper had X packets of chips. The first customer bought 2 packets. The second bought half of what remained plus 1. The third bought a third of what then remained plus 2. Four packets were left. How many did the second customer buy?", [], "TITA", "11", ["Algebra::Linear_Equations"], "Easy",
 "Work backwards.",
 steps(("Third", p("Before the third customer: (4 + 2) × 3/2 = 9.")),
       ("Second", p("Before the second: (9 + 1) × 2 = 20, so he bought 20 − 9 = 11.")),
       ("Check", p("X = 22: 22 → 20 → 9 → 4 ✓."))) + final("11"))

P.qa(10, "Resham invested ₹1,00,000 at 6% for 5 years and Reshma invested ₹90,000 at 7% for 4 years, both at simple interest. How much must be invested at 15% simple interest for 8 years to earn their combined interest?", ["₹45,500", "₹45,000", "₹46,000", "₹46,500"], "MCQ", "3", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Add the two interests.",
 steps(("Interest", p("30,000 + 25,200 = ₹55,200.")),
       ("Principal", p("55,200 ÷ (0.15 × 8) = 55,200 ÷ 1.2 = ₹46,000."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(11, "A train leaves Howrah for Kharagpur at 10 am, and another leaves Kharagpur for Howrah at 11 am. They cross at 1 pm at Kolaghat, halfway between the two. Each turns back as soon as it reaches the far end, and they meet again at Panskura. If Howrah and Kharagpur are 120 km apart, how far is Panskura from Howrah (in km)?", [], "TITA", "84", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "60 km in 3 hours and in 2 hours.",
 steps(("Speeds", p("The Howrah train does 60 km in 3 h: 20 km/h. The Kharagpur train does 60 km in 2 h: 30 km/h.")),
       ("At 4 pm", p("The slow train reaches Kharagpur at 4 pm. The fast one reached Howrah at 3 pm and is 30 km out by 4 pm.")),
       ("Meet", p("Gap 90 km, closing at 50 km/h: 1.8 h. The fast train covers 54 km more: 30 + 54 = 84 km from Howrah."))) + final("84"))

P.qa(12, "ABCD is a square of side 6 cm. X is a point inside it with BX = 3 cm and ∠XBC = 60°. P is the point on AD with XP ⊥ AD. Find the area of triangle XPD." + F.SQ,
 [r"\(\tfrac{9}{8}(4 - \sqrt3)\) cm²", r"\(\tfrac{9}{4}(4 + \sqrt3)\) cm²", r"\(\tfrac{27}{8}(2 - \sqrt3)\) cm²", r"\(\tfrac{27}{8}(4 - \sqrt3)\) cm²"], "MCQ", "4", ["Geometry::Triangles"], "Hard",
 "Drop a perpendicular from X to BC; its foot Q lines up with P.",
 steps(("30-60-90", p(r"In triangle XQB, BX = 3 and ∠XBQ = 60°: BQ = 3/2 and \(XQ = \tfrac{3\sqrt3}{2}\).")),
       ("Legs", p(r"PD = QC = 6 − 3/2 = 9/2, and \(XP = 6 - \tfrac{3\sqrt3}{2}\).")),
       ("Area", p(r"\(\tfrac12 \cdot \tfrac92 \cdot \left(6 - \tfrac{3\sqrt3}{2}\right) = \tfrac{27}{8}(4 - \sqrt3)\) ≈ 7.66 cm²."))) + final("Option 4"),
 why_rows=[("1", "A third of the area: an arithmetic slip."), ("2", "Adds XQ to the side instead of subtracting."), ("3", "Arithmetic slip.")])

P.qa(13, "Ashok can finish a job alone in 25 days and Suresh in 20 days. Ashok starts; Suresh joins after 4 days, and Badal joins them 3 days after that; together they finish the job. Badal did 30% of the work. In how many days could Badal do the whole job alone?", ["10", "12", "15", "20"], "MCQ", "1", ["Arithmetic::Time_and_Work"], "Medium",
 "Take the job as 100 units: Ashok 4 a day, Suresh 5.",
 steps(("Ashok and Suresh", p("They did 70 units. If Ashok worked D days, 4D + 5(D − 4) = 70, so D = 10.")),
       ("Badal", p("He worked 10 − 7 = 3 days for 30 units: 10 a day, so 10 days alone."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(14, "A wholesaler bought 15 kg of cabbage and 16 kg of cauliflower. He paid three times as much for 2 kg of cauliflower as for 1 kg of cabbage. He sold them to a trader at 33⅓% profit on cabbage and 25% on cauliflower. The trader lost 3 kg of cabbage and 4 kg of cauliflower to spoilage, sold the rest at ₹30 a kg and made 44% profit overall. What did the wholesaler pay per kg of cabbage (in ₹)?", [], "TITA", "10", ["Arithmetic::Profit_and_Loss"], "Easy",
 "Cabbage ₹x a kg, cauliflower ₹1.5x a kg.",
 steps(("Trader’s cost", p("15 × 4x/3 + 16 × 1.5x × 5/4 = 20x + 30x = 50x.")),
       ("Revenue", p("24 kg × 30 = 720 = 1.44 × 50x = 72x, so x = 10."))) + final("10"))

P.qa(15, r"What is the smallest positive integer value of \(\dfrac{x^2 + 12x + 35}{x^2 - 2x - 35}\) for real x?", ["4", "3", "2", "1"], "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Cancel the common factor.",
 steps(("Simplify", p(r"\(\dfrac{(x + 5)(x + 7)}{(x + 5)(x - 7)} = \dfrac{x + 7}{x - 7}\), for x ≠ −5.")),
       ("Positive values", p("For x < −7 it lies between 0 and 1. For x > 7 it is 1 + 14/(x − 7), always above 1.")),
       ("Smallest integer", p("2, at x = 21."))) + final("Option 3"),
 why_rows=[("1", "Not the smallest."), ("2", "Not the smallest."), ("4", "Would need 14/(x − 7) = 0.")])

P.qa(16, "A 5-character code uses letters (A–Z), digits (0–9) and symbols (@, #, %, $), with at least one of each kind and all characters different. It starts and ends with the same kind, either letters or symbols; the 2nd and 4th characters are of the same kind; and no two neighbouring characters are of the same kind. In the worst case, how many wrong codes might someone try before finding the right one?", [], "TITA", "418079", ["Modern_Maths::Permutations_and_Combinations"], "Hard",
 "Fix the pattern of kinds first.",
 steps(("Patterns", p("Ends L or S; 2nd = 4th, different from the ends; the middle must be the third kind. So LSDSL, LDSDL, SLDLS, SDLDS.")),
       ("Count", p("26·25·4·3·10 = 78,000; 26·25·10·9·4 = 2,34,000; 4·3·26·25·10 = 78,000; 4·3·10·9·26 = 28,080. Total 4,18,080.")),
       ("Wrong tries", p("At worst all the others come first: 4,18,079."))) + final("418079"))

P.qa(17, "In an arithmetic progression, the average of the first seven terms is 3/7 of the average of the 7th to 13th terms. The average of the first four terms is", ["twice the second term", "twice the common difference", "twice the first term", "the sum of the first two terms"], "MCQ", "3", ["Algebra::Progressions_and_Series"], "Medium",
 "The average of seven terms in AP is the middle term.",
 steps(("Middles", p("a + 3d = (3/7)(a + 9d), so 7a + 21d = 3a + 27d and 2a = 3d.")),
       ("Four terms", p("Average = a + 1.5d = a + a = 2a."))) + final("Option 3"),
 why_rows=[("1", "2(a + d) is larger."), ("2", "2d = 4a/3."), ("4", "2a + d.")])

P.qa(18, "Three positive numbers have squares adding up to 1883, and the sum of their products taken two at a time is 1871. What is their sum?", ["65", "75", "55", "85"], "MCQ", "2", ["Algebra::Equations_and_Polynomials"], "Easy",
 "Square the sum.",
 steps(("Square", p("1883 + 2 × 1871 = 5625 = 75²."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(19, "P, Q and R alone take 30, 40 and 50 days for a job. They work one at a time in cycles: P, Q, R for one day each (days 1–3); then two days each (days 4–9); then three days each (days 10–18); and so on, each turn growing by a day per cycle. On which day is the job finished?", [], "TITA", "37", ["Arithmetic::Time_and_Work"], "Medium",
 "Take the job as 600 units: P 20, Q 15, R 12 a day.",
 steps(("Cycles", p("Cycle k does 47k units. Four cycles: 47 × 10 = 470 units in 30 days.")),
       ("Finish", p("130 left. P works 5 days in cycle 5: 100 units. Q then needs 2 days for 30.")),
       ("Day", p("30 + 5 + 2 = 37."))) + final("37"))

P.qa(20, "In a six-digit number, the 6th digit is the sum of the first three, the 5th is the sum of the first two, the 3rd equals the 1st and the 2nd is twice the 1st. The number is divisible by 11. How many such numbers are there?", [], "TITA", "1", ["Number_System::Factors_and_Divisibility"], "Medium",
 "Write it as a, 2a, a, d, 3a, 4a.",
 steps(("Digits", p("4a ≤ 9, so a = 1 or 2.")),
       ("Rule of 11", p("Alternating sum: a − 2a + a − d + 3a − 4a = −(a + d), a multiple of 11 only if a + d = 11.")),
       ("Count", p("a = 2, d = 9: 242968. One number."))) + final("1"))

P.qa(21, r"For which values of x is \(\log_{10}\dfrac{7x - 2x^2}{5} \ge 0\)?", ["0 ≤ x ≤ 2.5", "1 ≤ x ≤ 3", "1 ≤ x ≤ 2.5", "1 ≤ x ≤ 5"], "MCQ", "3", ["Algebra::Logarithms_and_Exponents"], "Easy",
 "log ≥ 0 means the argument is at least 1.",
 steps(("Inequality", p(r"\(7x - 2x^2 \ge 5\), so \(2x^2 - 7x + 5 \le 0\), that is \((x - 1)(2x - 5) \le 0\).")),
       ("Range", p("1 ≤ x ≤ 2.5 (the argument is then positive too)."))) + final("Option 3"),
 why_rows=[("1", "x near 0 makes the log negative or undefined."), ("2", "x = 3 gives a negative argument."), ("4", "Too wide.")])

P.qa(22, r"How many distinct real roots does \(x(x - 2) + \dfrac{1 - 2x}{x^2} + 3 = 0\) have?", [], "TITA", "0", ["Algebra::Quadratic_Equations"], "Hard",
 r"Group into \(x + \tfrac1x\).",
 steps(("Regroup", p(r"\(x^2 + \tfrac{1}{x^2} + 2 - 2\left(x + \tfrac1x\right) + 1 = 0\), that is \(\left(x + \tfrac1x - 1\right)^2 = 0\).")),
       ("No real root", p(r"\(x + \tfrac1x = 1\) is impossible for real x, since |x + 1/x| ≥ 2."))) + final("0"))
