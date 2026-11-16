# -*- coding: utf-8 -*-
# Simp Mock 19 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_19 import P
import m25_19_figs as F

SLIP = lambda *o: [(x, "Arithmetic slip.") for x in o]

P.qa(1, "In trapezium ABCD, AB ∥ CD and ∠ABC = 90°. AB = 30 cm and CD = 60 cm, and a circle inside the trapezium touches all four sides. Find the area of the trapezium (in cm²)." + F.TRAP,
 ["1800", "2000", "2400", "3600"], "MCQ", "1", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "A quadrilateral with an incircle has equal sums of opposite sides.",
 steps(("Tangential", p("Let BC = h. Then h + AD = AB + CD = 90, so AD = 90 − h.")),
       ("Pythagoras", p("Drop a perpendicular from A to CD. It has length h and leaves 60 − 30 = 30 cm towards D, so") + p(r"\(h^2 + 30^2 = (90 - h)^2\)") + p("900 = 8100 − 180h, so h = 40.")),
       ("Area", p("½ × (30 + 60) × 40 = 1800."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Takes 60 × 40."), ("4", "Forgets the ½.")])

P.qa(2, r"The roots of \(x^4 - 10x^3 + 35x^2 - 50x + k = 0\) are all positive integers. What is k?", ["24", "36", "48", "64"], "MCQ", "1", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Sum of roots 10; use the sum of squares.",
 steps(("Squares", p(r"\(\sum a^2 = 10^2 - 2 \cdot 35 = 30\).")),
       ("Roots", p("Four positive integers adding to 10 with squares adding to 30: 1, 2, 3, 4. (Check: the sum of products of three is 6 + 8 + 12 + 24 = 50.)")),
       ("k", p("Product of the roots: 24."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(3, r"Find the HCF of \(x^4 + 2x^3 - 2x - 1\) and \(x^3 - x^2 - 5x - 3\).", ["(x − 1)", "(x + 1)", "(x − 1)²", "(x + 1)²"], "MCQ", "4", ["Algebra::Equations_and_Polynomials"], "Easy",
 "Factor both; x = 1 and x = −1 are good first tries.",
 steps(("First", p(r"\(x^4 + 2x^3 - 2x - 1\) \(= (x^4 - 1) + 2x(x^2 - 1)\) \(= (x^2 - 1)(x^2 + 2x + 1)\) \(= (x - 1)(x + 1)^3\).")),
       ("Second", p(r"x = 3 is a root: \(x^3 - x^2 - 5x - 3\) \(= (x - 3)(x^2 + 2x + 1)\) \(= (x - 3)(x + 1)^2\).")),
       ("HCF", p(r"\((x + 1)^2\)."))) + final("Option 4"),
 why_rows=[("1", "x − 1 does not divide the second."), ("2", "A common factor, but not the highest."), ("3", "x − 1 does not divide the second.")])

P.qa(4, "In triangle ABC, AB = 9 cm and AC = 14 cm. For the area of the triangle to be as large as possible, BC lies", ["below 14 cm", "between 14 and 15 cm", "between 15 and 16 cm", "between 16 and 17 cm"], "MCQ", "4", ["Geometry::Triangles"], "Easy",
 "Area = ½ · AB · AC · sin A.",
 steps(("Angle", p("The area is largest when sin A = 1, that is, A = 90°.")),
       ("BC", p(r"\(BC = \sqrt{81 + 196} = \sqrt{277}\), and 16² = 256 < 277 < 289 = 17²."))) + final("Option 4"),
 why_rows=[("1", "Too short for a right angle at A."), ("2", "Too short."), ("3", "Too short.")])

P.qa(5, r"For integers x, let \(f(x) = (x + 2)^3 (5 - x)^3\). How many different non-negative values can f(x) take?", ["3", "6", "4", "Infinitely many"], "MCQ", "3", ["Algebra::Functions"], "Easy",
 "f(x) ≥ 0 exactly when (x + 2)(5 − x) ≥ 0.",
 steps(("Range", p("−2 ≤ x ≤ 5.")),
       ("Symmetry", p("(x + 2)(5 − x) is symmetric about x = 1.5: the values for x = −2, −1, 0, 1 are 0, 6, 10, 12, repeated for 5, 4, 3, 2.")),
       ("Count", p("Four distinct values: 0, 216, 1000, 1728."))) + final("Option 3"),
 why_rows=[("1", "Leaves out 0."), ("2", "Counts x = 1 and 2 and so on as different values."), ("4", "Outside −2 to 5 the value is negative.")])

P.qa(6, "A team of 8 men and 6 women can finish a job in 52 days. If 9 children join the team, it takes 9 days fewer. A team of 4 men, 4 women and 28 children can finish the same job in 43 days. By what percentage is a man more efficient than a woman? (All men work at one rate, as do all women and all children.)", ["20", "30", "40", "50"], "MCQ", "3", ["Arithmetic::Time_and_Work"], "Medium",
 "Let a man, a woman and a child do M, W and C units a day.",
 steps(("Children", p("In 43 days the 9 children do the work the original team would do in the 9 saved days: 9 × 43C = 9(8M + 6W), so 8M + 6W = 43C.")),
       ("Third team", p("52(8M + 6W) = 43(4M + 4W + 28C) simplifies to 61M + 35W = 301C.")),
       ("Solve", p("With C = 1: 8M + 6W = 43 and 61M + 35W = 301 give M = 3.5, W = 2.5.")),
       ("Compare", p("3.5 ÷ 2.5 = 1.4: 40% more."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(7, "A train runs non-stop at a constant speed and arrives on schedule. Had it been 5 km/h faster, it would have taken 2 hours less; had it been 6 km/h slower, it would have taken 3 hours more. How many hours would the journey take at twice the original speed?", [], "TITA", "11", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Speed S, time t; expand both products against St.",
 steps(("Faster", p("(S + 5)(t − 2) = St gives 5t − 2S = 10.")),
       ("Slower", p("(S − 6)(t + 3) = St gives 3S − 6t = 18.")),
       ("Solve", p("S = 50 km/h, t = 22 hours; at double speed, 11 hours."))) + final("11"))

P.qa(8, "A scientist mixes liquids A and B. One ml of A weighs 1.2 g and one ml of B weighs 0.9 g, and 12 litres of the mixture weigh 12 kg. Three litres of the mixture are then replaced by 3 litres of A, and this is done three times in all. What is the ratio of the volume of A to that of B at the end?", ["23 : 9", "17 : 13", "15 : 7", "13 : 5"], "MCQ", "1", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Find the starting volume of B, then track only B.",
 steps(("Start", p("Average density 1. By alligation A : B = (1 − 0.9) : (1.2 − 1) = 1 : 2, so 4 litres of A and 8 of B.")),
       ("Replace", p(r"Each replacement keeps ¾ of the B: \(8 \times (3/4)^3 = 27/8\) litres.")),
       ("Ratio", p("A = 12 − 27/8 = 69/8, so A : B = 69 : 27 = 23 : 9."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(9, "A diamond’s value is proportional to the square of its weight. It breaks into four pieces with weights in the ratio 8 : 6 : 5 : 2. The smallest piece is worth ₹50,000. By how much does the largest piece’s value exceed the second largest’s?", ["₹1,37,500", "₹2,15,000", "₹2,80,000", "₹3,50,000"], "MCQ", "4", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Values go as 64 : 36 : 25 : 4.",
 steps(("Unit", p("4 parts = ₹50,000, so 1 part = ₹12,500.")),
       ("Difference", p("(64 − 36) × 12,500 = ₹3,50,000."))) + final("Option 4"),
 why_rows=[("1", "Uses 6 and 5."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(10, "A shopkeeper gives a 30% discount on the marked price of sugar but uses a scale that shows 1000 g when the true weight is 800 g. His overall profit is 40%. If sugar costs him ₹80 a kg, what is its marked price per kg (in ₹)?", [], "TITA", "128", ["Arithmetic::Profit_and_Loss"], "Medium",
 "Work per true kg.",
 steps(("Selling price", p("40% profit: ₹112 per true kg.")),
       ("Customer pays", p("For each “kg” on the scale (800 g true) he charges 0.7M; per true kg that is 0.7M × 1000 ÷ 800 = 0.875M.")),
       ("Marked price", p("0.875M = 112 gives M = 128."))) + final("128"))

P.qa(11, "When 4 soldiers leave a group of 28, the average weight rises by 4 kg. If instead 4 new soldiers with the same total weight as those 4 had joined the group, the average would have fallen by 3 kg. The original average (in kg) is a prime between 50 and 70, and the average of the 4 who left is not a prime. What is the average weight of the 32-soldier group?", [], "TITA", "56", ["Arithmetic::Average"], "Medium",
 "Write the leavers’ average in terms of the original average w.",
 steps(("Leavers", p("28w − 24(w + 4) = 4w − 96, so the 4 leavers average w − 24.")),
       ("Primes", p("w = 53, 59, 61, 67 give w − 24 = 29, 35, 37, 43. Only 35 is not prime, so w = 59.")),
       ("32 soldiers", p("The 32-soldier average is w − 3 = 56 (indeed (28 × 59 + 4 × 35) ÷ 32 = 1792 ÷ 32 = 56)."))) + final("56"))

P.qa(12, "The salaries of N and M together are five times L’s salary, and the salaries of N and L together are three times M’s. What is the ratio of the highest salary to the lowest?", ["9 : 4", "8 : 3", "7 : 2", "11 : 4"], "MCQ", "3", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Subtract the two equations.",
 steps(("Subtract", p("N + M = 5L and N + L = 3M give M − L = 5L − 3M, so 2M = 3L: M : L = 3 : 2.")),
       ("N", p("With L = 2, M = 3: N = 5L − M = 7.")),
       ("Ratio", p("7 : 2."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(13, "V and T invest at the same time. V’s scheme pays 10% a year compounded annually; T’s pays r% a year compounded half-yearly. V invested 10% more than T, yet after one year both had the same amount. Find r.", ["15", "18", "20", "24"], "MCQ", "3", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Take T’s investment as 1.",
 steps(("Equation", p(r"\(1.1 \times 1.1 = (1 + r/200)^2\).")),
       ("Solve", p("1 + r/200 = 1.1, so r = 20."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(14, "A share price moves in a two-month cycle: up m% in the first month, then down (m + 5)% in the second. The cycle happens twice. After the first cycle the price is ₹200 lower than at the start; after the second it is a further ₹184 lower. What was the starting price (in ₹)?", [], "TITA", "2500", ["Arithmetic::Percentages"], "Medium",
 "Each cycle multiplies the price by the same factor.",
 steps(("Same factor", p("X, X − 200 and X − 384 are in geometric progression:") + p(r"\((X - 200)^2 = X(X - 384)\)")),
       ("Solve", p("−400X + 40000 = −384X, so X = 2500.")),
       ("Check", p("Factor 2300/2500 = 0.92 = 1.15 × 0.80, so m = 15."))) + final("2500"))

P.qa(15, "In triangle ABC, AD is a median and F is a point on AB. CF meets AD at E, with AE : ED = 1 : 2. If AF = 2.8 cm, find AB (in cm).", [], "TITA", "14", ["Geometry::Triangles"], "Medium",
 "Menelaus on triangle ABD with the line F–E–C.",
 steps(("Menelaus", p("(AF/FB) · (BC/CD) · (DE/EA) = 1, and BC/CD = 2, DE/EA = 2.")),
       ("Ratio", p("AF/FB = 1/4, so FB = 11.2.")),
       ("AB", p("2.8 + 11.2 = 14."))) + final("14"),
 shortcut=p("Draw DG ∥ AB with G on CF: DG = ½ BF (D is the midpoint of BC) and DG = 2AF (AE : ED = 1 : 2), so BF = 4AF."))

P.qa(16, "Five shirts and six trousers, all of different colours, are placed on a row of eleven stands. Trousers must be at both ends and a shirt in the middle. In how many ways can this be done?", ["175 × 8!", "180 × 8!", "150 × 8!", "210 × 8!"], "MCQ", "3", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Fill the three special stands first.",
 steps(("Ends", p("6 × 5 = 30 ordered choices of trousers.")),
       ("Middle", p("5 shirts.")),
       ("Rest", p("The other 8 items on 8 stands: 8!.")),
       ("Total", p("30 × 5 × 8! = 150 × 8!."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(17, r"What is the remainder when \(5^{2025} + 7^{2025} + 9^{2025}\) \(+\, 11^{2025} + 13^{2025} + 15^{2025}\) is divided by 20?", ["0", "1", "11", "19"], "MCQ", "1", ["Number_System::Remainders"], "Easy",
 "For odd n, a + b divides aⁿ + bⁿ.",
 steps(("Pairs", p("5 + 15, 7 + 13 and 9 + 11 each make 20, and the power is odd, so each pair is a multiple of 20."))) + final("Option 1"),
 why_rows=[("2", "Treats each term as 1."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(18, r"Positive integers x and y satisfy \(5^x - 2^y = 2869\) and \(5^{x-1} + 2^{y+1} = 1137\). Find \(y^2 - x^2\).", [], "TITA", "39", ["Algebra::Logarithms_and_Exponents"], "Easy",
 r"Put \(p = 5^x\), \(q = 2^y\).",
 steps(("Equations", p("p − q = 2869 and p/5 + 2q = 1137, that is p + 10q = 5685.")),
       ("Solve", p("11q = 2816: q = 256, y = 8; p = 3125, x = 5.")),
       ("Answer", p("64 − 25 = 39."))) + final("39"))

P.qa(19, "A natural number X has 3 digits in base 2, and a natural number Y has n digits in base 3. The largest possible value of Y − X is 76. What is the smallest possible value of Y − X?", ["18", "20", "22", "38"], "MCQ", "2", ["Number_System::Miscellaneous"], "Medium",
 "X is between 4 and 7.",
 steps(("Largest Y", p("Largest Y − X = Y<sub>max</sub> − 4 = 76, so Y<sub>max</sub> = 80 = 2222 in base 3: n = 4.")),
       ("Smallest", p("The smallest 4-digit base-3 number is 1000 = 27. Smallest difference 27 − 7 = 20."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Uses X = 5."), ("4", "Not the least possible.")])

P.qa(20, r"Rhea bought tickets for herself and her friends for a ride. Because she bought more than four tickets, she paid for only \(n - \lfloor n/4 \rfloor\) of them, where n is the number of tickets and ⌊a⌋ is the greatest integer not exceeding a. Each ticket cost ₹400 and she paid ₹5200. How many tickets did she buy?", ["13", "16", "17", "20"], "MCQ", "3", ["Number_System::Miscellaneous"], "Easy",
 "She paid for 13 tickets.",
 steps(("Paid", p("5200 ÷ 400 = 13.")),
       ("Try", p("n = 16 gives 12; n = 17 gives 13; n = 18 gives 14. So n = 17."))) + final("Option 3"),
 why_rows=[("1", "Ignores the free tickets."), ("2", "Pays for only 12."), ("4", "Pays for 15.")])

P.qa(21, r"If \(f(x^2 + 2) = x^4 + 5x^2 + m\) and \(f(x^3 + 3) = x^6 + 7x^3 + n\), find n − m.", [], "TITA", "6", ["Algebra::Functions"], "Easy",
 "Write both in terms of a single variable.",
 steps(("First", p(r"With \(a = x^2\): \(f(a + 2) = a^2 + 5a + m\), so \(f(t) = (t - 2)^2 + 5(t - 2) + m\).")),
       ("Second", p(r"With \(b = x^3\): \(f(b + 3) = b^2 + 7b + n\).")),
       ("Match", p(r"From the first, \(f(b + 3) = (b + 1)^2 + 5(b + 1) + m\) \(= b^2 + 7b + m + 6\). So n = m + 6."))) + final("6"))

P.qa(22, "All natural numbers whose digits are only 1, 2 and 3 (1, 2, 3, 11, 12, 13, 21, …) are written in ascending order and joined into one long number. What is its 6000th digit from the left?", [], "TITA", "3", ["Number_System::Miscellaneous"], "Hard",
 "There are 3ᵏ such numbers with k digits.",
 steps(("Up to five digits", p("3 × 1 + 9 × 2 + 27 × 3 + 81 × 4 + 243 × 5 = 3 + 18 + 81 + 324 + 1215 = 1641 digits.")),
       ("Six-digit block", p("6000 − 1641 = 4359 = 726 × 6 + 3: the 3rd digit of the 727th six-digit number.")),
       ("Which number", p("Number 727 has index 726 from 0. 726 in base 3 is 222220; adding 1 to each digit gives 333331.")),
       ("Digit", p("Its 3rd digit is 3."))) + final("3"))
