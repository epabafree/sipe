# -*- coding: utf-8 -*-
# Simp Mock 5: QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m05 import P
import m05_figs as F

SLIP = lambda *o: [(x, "Arithmetic slip.") for x in o]

P.qa(1, r"Let \(X = \{7^{4n+2} + 50n + 1 : n = 1, 2, 3, \dots\}\) and \(Y = \{50(n + 1) : n = 1, 2, 3, \dots\}\). Which is true?", ["X ⊂ Y", "X − Y ≠ ∅", "Y ⊆ X", "X − Y ≠ ∅ and Y − X ≠ ∅"], "MCQ", "1", ["Modern_Maths::Set_Theory"], "Medium",
 r"\(7^{4n+2} = 49^{2n+1}\), and 49 ≡ −1 (mod 50).",
 steps(("X", p(r"\(49^{2n+1} + 1\) is divisible by 49 + 1 = 50 (odd power), so every element of X is a multiple of 50, at least 117,700.")),
       ("Y", p("Y is every multiple of 50 from 100 on.")),
       ("Compare", p("Every element of X is in Y, but 100 is not in X: X is a proper subset of Y."))) + final("Option 1"),
 why_rows=[("2", "Every element of X is in Y."), ("3", "100 is in Y but not X."), ("4", "X − Y is empty.")])

P.qa(2, r"The smallest integer n with \(5^n > 26^{13}\) is", ["24", "25", "26", "27"], "MCQ", "4", ["Algebra::Logarithms_and_Exponents"], "Hard",
 r"Square both sides: compare \(25^n\) and \(26^{26}\).",
 steps(("Lower bound", p(r"\(5^{26} = 25^{13} < 26^{13}\), so n ≥ 27.")),
       ("n = 27", p(r"Need \(25^{27} > 26^{26}\), i.e. \((26/25)^{26} < 25\). Since \((1 + 1/25)^{26} < e^{26/25} < 3\), it holds."))) + final("Option 4"),
 why_rows=[("1", "Too small."), ("2", "Too small."), ("3", r"\(5^{26} = 25^{13} < 26^{13}\).")])

P.qa(3, "Ten equally efficient people each could finish a job alone in 160 days. In a team, five of them work every day and the other five only on alternate days (days 1, 3, 5, …). If all start together, in how many days is the job done?", [], "TITA", "21", ["Arithmetic::Time_and_Work"], "Easy",
 "Each person does 1 unit a day; the job is 160 units.",
 steps(("Pattern", p("Odd days 10 units, even days 5: 15 every two days.")),
       ("Count", p("20 days give 150; day 21 (odd) adds 10."))) + final("21"))

P.qa(4, "A truck may carry animals weighing at most 1000 kg in total. One animal weighs exactly 103 kg and must be loaded; another weighs exactly 93 kg; every other animal weighs more than 93 kg and less than 103 kg. At most how many animals can be loaded?", [], "TITA", "10", ["Arithmetic::Miscellaneous"], "Easy",
 "Load the 103 kg and 93 kg animals, then the lightest others.",
 steps(("Room left", p("1000 − 196 = 804 kg.")),
       ("Others", p("Each is just over 93 kg: 8 fit (8 × 93.x < 804) but 9 would exceed 837.")),
       ("Total", p("2 + 8 = 10."))) + final("10"))

P.qa(5, "A company’s Mumbai and Kolkata branches each have Finance, Marketing and Operations departments, with staff in the ratio 1 : 3 : 2 in Mumbai and 3 : 7 : 5 in Kolkata. Both branches have the same number of staff. What is the ratio of Mumbai’s Finance staff to Kolkata’s Operations staff?", ["5 : 7", "1 : 2", "3 : 5", "2 : 5"], "MCQ", "2", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Make both totals 30.",
 steps(("Scale", p("Mumbai 5 : 15 : 10, Kolkata 6 : 14 : 10.")),
       ("Ratio", p("5 : 10 = 1 : 2."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(6, "In triangle ABC, AD, BE and CF are medians. P on AD has 3AP = 2AD. The quadrilateral PDCE has area 60 cm². Find the area of quadrilateral BCEF (in cm²).", ["120", "135", "145", "160"], "MCQ", "2", ["Geometry::Triangles"], "Medium",
 "P is the centroid.",
 steps(("Centroid", p("The medians split the triangle into six equal parts; PDCE is two of them, so the triangle is 180.")),
       ("BCEF", p("Triangle AFE is a quarter of ABC: BCEF = ¾ × 180 = 135."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(7, "APBC is a semicircle with diameter AC = 84 cm and centre O. BQC is a semicircle drawn outward on chord BC, with area one-quarter of APBC’s. Find the area of the shaded crescent (inside BQC, outside APBC), in cm². (Use π = 22/7.)" + F.LUNE,
 [r"\(924 - 441\sqrt3\)", r"\(441\sqrt3 - 462\)", r"\(1617 - 441\sqrt3\)", r"\(441\sqrt3 - 231\)"], "MCQ", "4", ["Geometry::Circles"], "Hard",
 "Crescent = small semicircle − the segment of the big circle cut off by BC.",
 steps(("BC", p("Areas 1 : 4 mean diameters 1 : 2, so BC = 42 = OB = OC: triangle OBC is equilateral and ∠BOC = 60°.")),
       ("Segment", p(r"Sector OBC − triangle OBC = \(\tfrac16 \cdot \tfrac{22}{7} \cdot 42^2 - \tfrac{\sqrt3}{4} \cdot 42^2\) \(= 924 - 441\sqrt3\).")),
       ("Crescent", p(r"Small semicircle \(= \tfrac12 \cdot \tfrac{22}{7} \cdot 21^2 = 693\). Crescent \(= 693 - (924 - 441\sqrt3)\) \(= 441\sqrt3 - 231\) ≈ 533."))) + final("Option 4"),
 why_rows=[("1", "The segment, not the crescent."), ("2", "Arithmetic slip."), ("3", "Adds the segment instead of subtracting.")])

P.qa(8, "How many pairs of integers (m, n) satisfy |2 − mn| < m − n ≤ 2?", ["3", "4", "5", "6"], "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "m − n is 1 or 2.",
 steps(("m − n = 1", p("|2 − mn| = 0: mn = 2 with m = n + 1 gives (2, 1) and (−1, −2).")),
       ("m − n = 2", p("|2 − mn| ≤ 1: mn = 1, 2 or 3 with m = n + 2. Only mn = 3 works: (3, 1) and (−1, −3).")),
       ("Count", p("4."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(9, "In triangle ABC, ∠BAC = 60°, AB = 8 cm and BC = 10 cm. Find the area of the triangle (in cm²).", [r"\(8\sqrt3 + 4\sqrt{39}\)", r"\(4\sqrt3 + 4\sqrt{39}\)", r"\(8\sqrt3 + 2\sqrt{39}\)", r"\(16\sqrt3 + 4\sqrt{13}\)"], "MCQ", "1", ["Geometry::Triangles"], "Medium",
 "Find AC with the cosine rule at A.",
 steps(("AC", p(r"\(100 = 64 + b^2 - 8b\), so \(b^2 - 8b - 36 = 0\) and \(b = 4 + 2\sqrt{13}\).")),
       ("Area", p(r"\(\tfrac12 \cdot 8 \cdot b \cdot \sin 60° = 2\sqrt3\,(4 + 2\sqrt{13})\) \(= 8\sqrt3 + 4\sqrt{39}\)."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(10, "50 identical chocolates are shared among 7 children, each getting at least one. What is the smallest possible value of the largest share?", ["5", "6", "7", "8"], "MCQ", "4", ["Arithmetic::Average"], "Easy",
 "Share as evenly as possible.",
 steps(("Even split", p("50 ÷ 7 is just over 7, so someone gets at least 8: 6 × 7 + 8 = 50."))) + final("Option 4"),
 why_rows=[("1", "Too few."), ("2", "Too few."), ("3", "7 × 7 = 49 < 50.")])

P.qa(11, r"x and y are integers with xy = 16. What is the largest possible value of \(\sqrt{(1 - 3x)(1 - 3y)}\)?", [], "TITA", "14", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 r"Expand: \(1 + 9xy - 3(x + y)\).",
 steps(("Expand", p("(1 − 3x)(1 − 3y) = 145 − 3(x + y).")),
       ("Maximise", p("Make x + y as negative as possible: x = −16, y = −1 gives 145 + 51 = 196.")),
       ("Root", p("√196 = 14."))) + final("14"))

P.qa(12, "For f(x) = |x| + |x − 1|, at how many integers x does f take its smallest value?", ["0", "1", "2", "More than 2"], "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "f is constant between 0 and 1.",
 steps(("Shape", p("For 0 ≤ x ≤ 1, f(x) = 1; outside, f > 1.")),
       ("Integers", p("x = 0 and 1."))) + final("Option 3"),
 why_rows=[("1", "f(0) = f(1) = 1."), ("2", "Both 0 and 1 work."), ("4", "f(2) = 3.")])

P.qa(13, r"a and b are integers with \(2^{a+4} \cdot 27^{b} = 13.5\). Find a + 5b.", ["−1", "0", "1", "3"], "MCQ", "2", ["Algebra::Surds_and_Indices"], "Easy",
 r"13.5 = 27/2 = \(2^{-1} \cdot 3^3\).",
 steps(("Match powers", p(r"\(2^{a+4} \cdot 3^{3b} = 2^{-1} \cdot 3^3\): a + 4 = −1 and 3b = 3.")),
       ("Answer", p("a = −5, b = 1, so a + 5b = 0."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(14, "At how many points does the line y = 10 meet the curve y = |x² − 12x + 20|?", [], "TITA", "4", ["Algebra::Quadratic_Equations"], "Easy",
 "The curve has a ‘bump’ of height 16 between x = 2 and x = 10.",
 steps(("Shape", p("x² − 12x + 20 = (x − 2)(x − 10), lowest −16 at x = 6. The absolute value flips that dip up to a peak of 16.")),
       ("Meet", p("y = 10 crosses the outer branches once each and the bump twice: 4 points."))) + final("4"))

P.qa(15, r"If \(2(x_1 + x_2 + \dots + x_n) = 7(3^n - 1)\) for every n ≥ 1, find \(x_7\).", [], "TITA", "5103", ["Algebra::Progressions_and_Series"], "Easy",
 "Subtract the sums for n = 6 and n = 7.",
 steps(("Difference", p(r"\(2x_7 = 7(3^7 - 3^6) = 7 \cdot 1458\), so \(x_7 = 5103\)."))) + final("5103"))

P.qa(16, "For a positive integer n, f(n) = n(n + 1)/2 if n is even and n(n − 1)/2 if n is odd. If 7f(x + 3) − 10f(x) = 25, find x.", [], "TITA", "8", ["Algebra::Quadratic_Equations"], "Medium",
 "Try x odd and x even.",
 steps(("x odd", p("x + 3 is even: 7(x + 3)(x + 4)/2 − 10x(x − 1)/2 = 25 gives 3x² − 59x − 34 = 0, with no integer root.")),
       ("x even", p("x + 3 is odd: 7(x + 3)(x + 2)/2 − 10x(x + 1)/2 = 25 gives 3x² − 25x + 8 = 0, so x = 8.")),
       ("Check", p("7 × 55 − 10 × 36 = 25."))) + final("8"))

P.qa(17, r"Find \(\dfrac{1}{\sqrt2 + 1} + \dfrac{1}{\sqrt3 + \sqrt2}\) \(+ \dots + \dfrac{1}{\sqrt{16} + \sqrt{15}}\).", ["2", "3", "4", r"\(\sqrt{15} - 1\)"], "MCQ", "2", ["Algebra::Surds_and_Indices"], "Easy",
 "Rationalise each term.",
 steps(("Each term", p(r"\(\dfrac{1}{\sqrt{k+1} + \sqrt k} = \sqrt{k+1} - \sqrt k\).")),
       ("Telescope", p(r"The sum is \(\sqrt{16} - 1 = 3\)."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", r"Forgets to subtract \(\sqrt1\)."), ("4", "Stops one term early.")])

P.qa(18, "A motorbike’s wheels have radii 21 cm and 28 cm. It covers 99 km in 1 hour 15 minutes at constant speed. What is the difference in the wheels’ revolutions per minute?", ["250", "225", "220", "200"], "MCQ", "1", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Distance per minute ÷ circumference.",
 steps(("Per minute", p("99 km ÷ 75 = 1.32 km = 132,000 cm.")),
       ("Revolutions", p("Small wheel (132 cm): 1000. Large wheel (176 cm): 750. Difference 250."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(19, "A town’s adult population was 9,12,800 in 2019 and 10,40,592 in 2022. Adult men increased by 12.5% and adult women by 15.5%. How many adult men were there in 2022?", ["514350", "513450", "456400", "454600"], "MCQ", "2", ["Arithmetic::Percentages"], "Medium",
 "The overall rise is 14%: halfway between 12.5 and 15.5.",
 steps(("Split", p("1040592 ÷ 912800 = 1.14, exactly between the two rates, so men and women were equal in 2019: 4,56,400 each.")),
       ("Men now", p("456400 × 1.125 = 5,13,450."))) + final("Option 2"),
 why_rows=[("1", "Digits swapped."), ("3", "The 2019 figure."), ("4", "Digits swapped.")])

P.qa(20, "b is a natural number, and both x² + 8x + b = 0 and x² + bx + 8 = 0 have real roots. How many values can b take?", ["8", "9", "10", "11"], "MCQ", "4", ["Algebra::Quadratic_Equations"], "Easy",
 "Two discriminant conditions.",
 steps(("Conditions", p("64 ≥ 4b gives b ≤ 16; b² ≥ 32 gives b ≥ 6.")),
       ("Count", p("6 to 16: 11 values."))) + final("Option 4"),
 why_rows=SLIP("1", "2", "3"))

P.qa(21, "A motorcyclist leaves Kolkata at 7 am and reaches Kharagpur at 10 am. From 7:01 am, a car leaves Kharagpur for Kolkata every 10 minutes. If the motorcyclist doubles his speed and the cars leave every 20 minutes instead, everything else unchanged, how many cars does he meet on the road?", ["7", "6", "5", "4"], "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "He now arrives at 8:30.",
 steps(("Cars", p("Leaving at 7:01, 7:21, 7:41, 8:01 and 8:21 — all before he arrives at 8:30. The 8:41 car leaves after.")),
       ("Count", p("5."))) + final("Option 3"),
 why_rows=[("1", "Uses the old schedule."), ("2", "Counts the 8:41 car."), ("4", "Misses the 8:21 car.")])

P.qa(22, "In a circle of radius 2 cm with centre O, arc AB subtends an obtuse angle θ radians at O. The sector OAB has twice the area of triangle AOB. Which equation does θ satisfy?", ["2 sin θ = θ", "sin(θ/2) = θ", "sin(θ/2) cos(θ/2) = θ", "2 sin(θ/2) cos(θ/2) = θ"], "MCQ", "1", ["Geometry::Trigonometry"], "Medium",
 "Sector ½r²θ, triangle ½r² sin θ.",
 steps(("Equation", p("½r²θ = 2 × ½r² sin θ, so θ = 2 sin θ."))) + final("Option 1"),
 why_rows=[("2", "Not equivalent."), ("3", "Equals ½ sin θ = θ."), ("4", "Equals sin θ = θ.")])
