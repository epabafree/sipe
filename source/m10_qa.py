# -*- coding: utf-8 -*-
# Simp Mock 10: QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m10 import P
import m10_figs as F

SLIP = lambda *o: [(x, "Arithmetic slip.") for x in o]

P.qa(1, "The warden of a hostel was finding the average age of the 35 boys living there. By mistake he included himself, and the average rose by one year. If the warden is 57, what is the boys’ average age?", [], "TITA", "21", ["Arithmetic::Average"], "Easy",
 "36(x + 1) = 35x + 57.",
 steps(("Solve", p("36x + 36 = 35x + 57, so x = 21."))) + final("21"))

P.qa(2, "N is a positive integer and N³ + 96 is divisible by N. How many values can N take?", ["15", "12", "10", "9"], "MCQ", "2", ["Number_System::Factors_and_Divisibility"], "Easy",
 "N must divide 96.",
 steps(("Factors", p("96 = 2⁵ × 3 has 6 × 2 = 12 factors."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(3, "The natural numbers that are neither perfect squares, nor perfect cubes, nor fourth powers are listed in increasing order. What is the 2023rd number in the list?", [], "TITA", "2077", ["Number_System::Miscellaneous"], "Medium",
 "Fourth powers are already squares.",
 steps(("Up to n", p("Count = n − ⌊√n⌋ − ⌊∛n⌋ + ⌊⁶√n⌋.")),
       ("Up to 2077", p("2077 − 45 − 12 + 3 = 2023, and 2077 is neither a square nor a cube."))) + final("2077"))

P.qa(4, "a and k are integers with a² + a − k = 0, 10 ≤ |a| ≤ 99 and 100 ≤ |k| ≤ 999. How many pairs (a, k) are there?", [], "TITA", "44", ["Algebra::Quadratic_Equations"], "Medium",
 "k = a(a + 1), always ≥ 0.",
 steps(("Positive a", p("110 ≤ a(a + 1) ≤ 999 for a = 10 to 31: 22 values.")),
       ("Negative a", p("a = −11 to −32 gives the same products: 22 values.")),
       ("Total", p("44."))) + final("44"))

P.qa(5, "N is the number of even factors of 2³ × 3⁵ × 5⁴. How many factors does N have?", [], "TITA", "12", ["Number_System::Factors_and_Divisibility"], "Easy",
 "Power of 2 from 1 to 3.",
 steps(("N", p("3 × 6 × 5 = 90.")),
       ("Factors of 90", p("90 = 2 × 3² × 5: 2 × 3 × 2 = 12."))) + final("12"))

P.qa(6, "What is the shortest distance between the curves x² + y² = 4 and y = |x − 2| + |x + 2|?", ["0.5 units", "1 unit", "2 units", r"\(2\sqrt{2}\) units"], "MCQ", "3", ["Geometry::Coordinate_Geometry"], "Hard",
 "The second curve is flat at y = 4 for −2 ≤ x ≤ 2.",
 steps(("Shapes", p("A circle of radius 2 at the origin. The other curve is y = 4 on [−2, 2] and rises outside.")),
       ("Gap", p("From the top of the circle (0, 2) to y = 4: 2 units. Points outside [−2, 2] are farther."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(7, "p is real and x² = 1 − (3x − p)² has exactly one real root (a repeated root), which is positive. What is p²?", ["0", "1", "4", "10"], "MCQ", "4", ["Algebra::Quadratic_Equations"], "Hard",
 "10x² − 6px + (p² − 1) = 0.",
 steps(("Discriminant zero", p("36p² − 40(p² − 1) = 0, so p² = 10.")),
       ("Positive", p("The root 3p/10 is positive for p = √10."))) + final("Option 4"),
 why_rows=[("1", "Root 0, not positive."), ("2", "Two roots."), ("3", "Two roots.")])

P.qa(8, r"Neeraj saves some money each month. He puts 25% of it into a recurring deposit, gives \(33\tfrac13\%\) of the rest to his mother, and splits what remains equally between his sisters. If his mother and sisters together get ₹3000 a month, how much (in ₹) does he deposit in a year?", ["1000", "4000", "6000", "12000"], "MCQ", "4", ["Arithmetic::Percentages"], "Medium",
 "Deposit x/4, mother x/4, sisters x/2.",
 steps(("Savings", p("3x/4 = 3000, so x = 4000.")),
       ("Year", p("12 × 1000 = 12,000."))) + final("Option 4"),
 why_rows=[("1", "One month."), ("2", "Monthly savings."), ("3", "Half.")])

P.qa(9, "A shop gets shirts in two boxes. In the first box, 30% of 90 shirts are red. If 70% of the second box were red, 40% of all the shirts would be red. If instead 90% of the second box were red, what percentage of all the shirts would be red?", ["45%", "50%", "60%", "70%"], "MCQ", "1", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Alligation finds the second box.",
 steps(("Second box", p("27 + 0.7y = 0.4(90 + y), so y = 30.")),
       ("New share", p("(27 + 27) ÷ 120 = 45%."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(10, "Prakash, Kumar and Rakesh together finish a project in 10 days; Prakash alone takes 20 days and Kumar 30. Pay is in proportion to work done. If all three work together and Prakash earns ₹81,000, how much (in ₹) does Rakesh earn?", ["81000", "54000", "40500", "27000"], "MCQ", "4", ["Arithmetic::Time_and_Work"], "Medium",
 "Rakesh’s rate is 1/10 − 1/20 − 1/30.",
 steps(("Rakesh", p("1/60 a day.")),
       ("Share", p("Prakash : Rakesh = 3 : 1, so ₹27,000."))) + final("Option 4"),
 why_rows=[("1", "Prakash’s share."), ("2", "Kumar’s share."), ("3", "Half.")])

P.qa(11, "ABC is an equilateral triangle of side 4 cm. D is on BC so that the area of triangle ACD is three times the area of triangle ABD. Find AD in cm.", [r"\(\sqrt{11}\)", r"\(\sqrt{13}\)", r"\(\sqrt{15}\)", r"\(\sqrt{17}\)"], "MCQ", "2", ["Geometry::Triangles"], "Easy",
 "Same height, so CD : BD = 3 : 1.",
 steps(("D", p("BD = 1, so D is 1 cm from the foot of the altitude (2√3).")),
       ("AD", p(r"\(AD^2 = 12 + 1 = 13\)."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(12, "Two runners start at the same time from opposite ends of a 500 m straight track and run to and fro at 3 m/s and 7 m/s. How far (in m) is the slower runner from his starting point when they meet for the third time?", [], "TITA", "450", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Track both positions.",
 steps(("First meeting", p("After 50 s, 150 m from the slower runner’s start.")),
       ("Second", p("The faster runner reaches the slower one’s starting end at t ≈ 71.4 s, turns, and catches him at t = 125 s, 375 m from the slower runner’s start.")),
       ("Third", p("The faster runner reaches the far end at t ≈ 142.9 s and turns back. They meet at t = 150 s, 450 m from the slower runner’s start."))) + final("450"))

P.qa(13, r"\(a = \tfrac{\sqrt5 + \sqrt3}{\sqrt5 - \sqrt3}\) and \(b = \tfrac{\sqrt5 - \sqrt3}{\sqrt5 + \sqrt3}\). Find \(\tfrac{a + b}{2ab}\).", ["16", "8", "4", "2"], "MCQ", "3", ["Algebra::Surds_and_Indices"], "Medium",
 "ab = 1.",
 steps(("a + b", p(r"\(a = 4 + \sqrt{15}\), \(b = 4 - \sqrt{15}\), so a + b = 8.")),
       ("Value", p("8 ÷ 2 = 4."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(14, "f(n) = n³ and g(n + 1) = 10 − g(n) for all positive integers n. If g(n³ − n) = 7 for some n ≥ 2, find f(g(1)) − g(f(2)).", [], "TITA", "20", ["Algebra::Functions"], "Hard",
 "g alternates between g(1) and 10 − g(1).",
 steps(("Parity", p("n³ − n is even, so g(even) = 7 and g(odd) = 3.")),
       ("Value", p("f(g(1)) = 27, g(f(2)) = g(8) = 7: 20."))) + final("20"))

P.qa(15, "A school has 13 teachers, all graduates. Some also hold a Master’s degree and some a B.Ed.; those with both can become Head Master. Exactly 3 teachers hold only a bachelor’s degree. If 7 have a B.Ed. and 5 a Master’s, how many can already become Head Master?", ["1", "2", "3", "4"], "MCQ", "2", ["Modern_Maths::Set_Theory"], "Easy",
 "10 teachers have at least one.",
 steps(("Overlap", p("7 + 5 − 10 = 2."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(16, r"p and q are distinct positive reals and n is a real number with q + n > 0. Which statements are correct?<br>I: if p < q and n < 0, then \(\tfrac{p}{q} > \tfrac{p+n}{q+n}\).<br>II: if p < q and n > 0, then \(\tfrac{p}{q} > \tfrac{p+n}{q+n}\).<br>III: if p > q and n > 0, then \(\tfrac{p}{q} > \tfrac{p+n}{q+n}\).<br>IV: if p > q and n < 0, then \(\tfrac{p}{q} > \tfrac{p+n}{q+n}\).", ["I and II", "III and IV", "II and IV", "I and III"], "MCQ", "4", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Look at the sign of the difference.",
 steps(("Difference", p(r"\(\tfrac{p+n}{q+n} - \tfrac{p}{q} = \tfrac{n(q - p)}{q(q + n)}\), and q(q + n) > 0.")),
       ("Sign", p("p/q is larger when n(q − p) < 0: n < 0 with p < q (I), or n > 0 with p > q (III)."))) + final("Option 4"),
 why_rows=[("1", "II is false."), ("2", "IV is false."), ("3", "Both false.")])

P.qa(17, "Car 1 covers distance D at speed 2s; car 2 covers 2D at speed s. Their times differ by 45 minutes. How long (in hours) does car 2 take?", ["0.25", "0.5", "1", "2"], "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Car 2 takes four times as long.",
 steps(("Times", p("4t − t = 45 min, so t = 15 min and car 2 takes 60 min."))) + final("Option 3"),
 why_rows=[("1", "Car 1’s time."), ("2", "Slip."), ("4", "Slip.")])

P.qa(18, r"Which graph could be \(y = \log_{0.25} x\) for positive real x?" + F.LOGS, ["Graph (1)", "Graph (2)", "Graph (3)", "Graph (4)"], "MCQ", "1", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Base below 1: decreasing, x > 0, through (1, 0).",
 steps(("Domain", p("x > 0 rules out (3) and (4).")),
       ("Direction", p("Base 0.25 < 1, so the graph falls: (1)."))) + final("Option 1"),
 why_rows=[("2", "Rising: base above 1."), ("3", "x < 0."), ("4", "x < 0.")])

P.qa(19, "What is the sum of the coefficients of (x − 2)⁸(x + 3)²?", ["0", "16", "−16", "4"], "MCQ", "2", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Put x = 1.",
 steps(("Value", p("(−1)⁸ × 4² = 16."))) + final("Option 2"),
 why_rows=[("1", "Not a root."), ("3", "Sign slip."), ("4", "Drops the square.")])

P.qa(20, "PQRS is a trapezium with PQ ∥ RS. A and B are the midpoints of PS and QR. AB = 15 cm and the height is 7.5 cm. Find the area in cm².", ["122.5", "112.5", "125.5", "More information is needed"], "MCQ", "2", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "AB is the average of the parallel sides.",
 steps(("Area", p("15 × 7.5 = 112.5."))) + final("Option 2"),
 why_rows=[("1", "Slip."), ("3", "Slip."), ("4", "The midline gives it.")])

P.qa(21, "Number plates in a city are two capital letters followed by two digits. Plates containing both the letter I and the digit 1 are not allowed. How many plates are possible?", ["63,661", "63,631", "66,631", "66,661"], "MCQ", "3", ["Modern_Maths::Permutations_and_Combinations"], "Hard",
 "Subtract plates with at least one I and at least one 1.",
 steps(("All", p("26² × 10² = 67,600.")),
       ("Banned", p("(26² − 25²)(10² − 9²) = 51 × 19 = 969.")),
       ("Allowed", p("66,631."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(22, "x and −x are real roots of 2y³ + ky² − 36y + 126 = 0. What is k?", [r"\(\tfrac72\)", r"\(-\tfrac72\)", "−7", "7"], "MCQ", "3", ["Algebra::Equations_and_Polynomials"], "Hard",
 "Let the third root be z.",
 steps(("Vieta", p("Pair sum: −x² = −18. Product: −x²z = −63, so z = 3.5.")),
       ("k", p("Sum of roots z = −k/2, so k = −7."))) + final("Option 3"),
 why_rows=[("1", "Sign and factor slip."), ("2", "Factor slip."), ("4", "Sign slip.")])
