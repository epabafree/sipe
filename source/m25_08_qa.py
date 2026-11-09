# -*- coding: utf-8 -*-
# Simp Mock 8 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_08 import P
import m25_08_figs as F

P.qa(1, "Manish invested a sum at simple interest. It amounts to ₹10,560 in 4 years and ₹12,480 in 7 years. Find the rate of interest.", ["8%", "10%", "12.5%", "Cannot be determined"], "MCQ", "1", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Three years’ interest = 12480 − 10560.",
 steps(("Yearly interest", p("1920 ÷ 3 = 640.")), ("Principal", p("10560 − 4 × 640 = 8000. Rate: 640 ÷ 8000 = 8%."))) + final("Option 1"),
 why_rows=[("2", "Wrong principal."), ("3", "Wrong principal."), ("4", "Two amounts are enough.")])

P.qa(2, r"Find the number of non-zero integer solutions (x, y) if \(\dfrac xy < 0\) and \(7x - 3y = 156\).", ["22", "21", "7", "8"], "MCQ", "3", ["Algebra::Linear_Equations"], "Medium",
 "x must be a multiple of 3.",
 steps(("Parametrise", p(r"x = 3k, y = 7k − 52.")),
       ("Opposite signs", p(r"k > 0 and \(7k < 52\): k = 1 to 7. (k < 0 makes both negative.)"))) + final("7, option 3"),
 why_rows=[("1", "Not the count."), ("2", "Not the count."), ("4", "k = 0 gives x = 0.")])

P.qa(3, "If 4 litres of water are added to a mixture of milk and water, the ratio of milk to water becomes 1 : 2. If another 40 litres of milk are then added, the ratio becomes 3 : 1. Find the percentage of milk in the original mixture.", [], "TITA", "40", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Water after the first step is 2m.",
 steps(("Milk", p(r"\(m + 40 = 3 \times 2m\), so m = 8; water after = 16, originally 12.")),
       ("Percentage", p("8 of 20 = 40%."))) + final("40"))

P.qa(4, "Satish bought a bicycle and soon sold it to his brother Rajesh at a 21% discount, for ₹6,320. Rajesh’s friend Kumar then bought it from Rajesh at a price 13% higher than Satish’s purchase price, and spent another 10% of his purchase price adding features. What is the total amount Kumar spent on the bicycle?", ["₹9,040", "₹9,140", "₹9,440", "₹9,944"], "MCQ", "4", ["Arithmetic::Percentages"], "Easy",
 "Satish paid 6320 ÷ 0.79.",
 steps(("Satish", p("₹8,000.")), ("Kumar", p(r"\(8000 \times 1.13 = 9040\); plus 10%: 9944."))) + final("Option 4"),
 why_rows=[("1", "Leaves out the features."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(5, r"In \(z = 3x^2 + y^2 + 7x + ny + 11\), x, y and z are real numbers and n is a natural number. Find the largest value of n for which z can never be zero.", ["4", "5", "6", "None of these"], "MCQ", "2", ["Algebra::Quadratic_Equations"], "Medium",
 "Complete the squares; the minimum must stay positive.",
 steps(("Minimum", p(r"\(z_{\min} = 11 - \tfrac{49}{12} - \tfrac{n^2}4\).")),
       ("Positive", p(r"\(\tfrac{n^2}4 < \tfrac{83}{12}\), so \(n^2 < 27.7\): n ≤ 5."))) + final("5, option 2"),
 why_rows=[("1", "Not the largest."), ("3", "36/4 = 9 > 6.9."), ("4", "5 works.")])

P.qa(6, r"If a is a non-negative real number, how many solutions does \(\left[a^2\left(a^2 + 5^2 + \dfrac{5^2}{a^2}\right)\right]^{1/2} = a - 5\) have?", [], "TITA", "0", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Square both sides, and remember a − 5 ≥ 0.",
 steps(("Square", p(r"\(a^4 + 25a^2 + 25 = a^2 - 10a + 25\), so \(a(a^3 + 24a + 10) = 0\).")),
       ("Check", p(r"a = 0 isn’t allowed (and gives 5 = −5); \(a^3 + 24a + 10 > 0\) for a ≥ 0. No solutions."))) + final("0"))

P.qa(7, r"The function \(f(x) = \dfrac{x - 3}{(x + 1)(x^2 - 2x - 3)}\) is positive for all real x except ________ distinct real numbers.", [], "TITA", "2", ["Algebra::Functions"], "Easy",
 "\\(x^2 - 2x - 3 = (x - 3)(x + 1)\\).",
 steps(("Simplify", p(r"\(f(x) = \dfrac1{(x + 1)^2}\) for x ≠ 3, −1: always positive.")),
       ("Exceptions", p("Undefined at x = −1 and x = 3: 2 numbers."))) + final("2"))

P.qa(8, "A shopkeeper buys articles at ₹100 each and marks them up 40%. He always sells at a 15% discount on the marked price. He then buys a new batch equal to 10% of the original quantity, made of cheaper material at ₹60 each, mixes them in, and keeps the marked price unchanged. What is his overall profit percentage after selling all the articles?", ["20.78%", "23.49%", "19.72%", "7.10%"], "MCQ", "2", ["Arithmetic::Profit_and_Loss"], "Medium",
 "Take 100 original articles.",
 steps(("Selling price", p(r"\(140 \times 0.85 = 119\) each; 110 articles: 13,090.")),
       ("Cost", p("100 × 100 + 10 × 60 = 10,600. Profit 2,490: 23.49%."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Profit on the original batch only."), ("4", "Arithmetic slip.")])

P.qa(9, "In the figure (not to scale), AB is a diameter of the circle. PR and PQ are tangents from an external point P, touching the circle at A and C respectively, and line AB extended meets PQ at Q. ∠ABC = 54°. Find the absolute difference (in degrees) between ∠APC and ∠BQC." + F.TANGENT, [], "TITA", "54", ["Geometry::Circles"], "Medium",
 "Use the centre O: OB = OC.",
 steps(("∠BOC", p(r"△OBC is isosceles with base angles 54°, so ∠BOC = 72° and ∠AOC = 108°.")),
       ("∠APC", p(r"In PAOC the angles at A and C are 90°: ∠APC = 180° − 108° = 72°.")),
       ("∠BQC", p(r"△OCQ has a right angle at C and ∠COQ = 72°: ∠BQC = 18°. Difference 54°."))) + final("54"))

P.qa(10, "A publisher must arrange k books on p shelves, each holding exactly 53 books. After filling all the shelves, 32 books are left over. If k is divisible by p, what is the average of all possible values of k?", ["588.5", "592.5", "584.5", "596.5"], "MCQ", "1", ["Number_System::Factors_and_Divisibility"], "Medium",
 "k = 53p + 32 is divisible by p exactly when p divides 32.",
 steps(("Values", p("p = 1, 2, 4, 8, 16, 32: k = 85, 138, 244, 456, 880, 1728.")),
       ("Average", p("3531 ÷ 6 = 588.5."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(11, F.STRIPS + p("In the figure (not to scale), ABCD and EFGH are rectangles. AD = 15 cm and GH = 8 cm. Find the area (in cm²) of quadrilateral PQRS, given that ∠APS = 30°."), ["120", r"\(120\sqrt3\)", r"\(\dfrac{240}{\sqrt3}\)", "240"], "MCQ", "4", ["Geometry::Mensuration"], "Medium",
 "PQRS is a parallelogram with base PQ on AB and height AD.",
 steps(("PQ", p(r"The strip is 8 cm wide and meets AB at 30°: \(PQ = 8 \div \sin 30^\circ = 16\).")),
       ("Area", p(r"\(16 \times 15 = 240\)."))) + final("240, option 4"),
 why_rows=[("1", "Uses 8 for PQ."), ("2", "Wrong trig ratio."), ("3", "Wrong trig ratio.")])

P.qa(12, "A and B can complete a piece of work in 20 days and 30 days respectively. They start together; after n days A leaves, and B alone finishes the rest in n + 2 days. How many days did A work?", [], "TITA", "8", ["Arithmetic::Time_and_Work"], "Easy",
 "Together they do 1/12 a day.",
 steps(("Equation", p(r"\(\tfrac n{12} + \tfrac{n + 2}{30} = 1\): \(5n + 2n + 4 = 60\), n = 8."))) + final("8"))

P.qa(13, "In a game, a player receives an amount (in ₹) equal to three times the number on the top face of a fair die. How much should the player pay per roll to win ₹5 per roll in the long run?", ["₹3.5", "₹4.5", "₹5.5", "₹6.5"], "MCQ", "3", ["Modern_Maths::Probability"], "Easy",
 "Expected receipt: 3 × 3.5.",
 steps(("Pay", p("10.5 − 5 = 5.5."))) + final("Option 3"),
 why_rows=[("1", "The expected face."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(14, "A point P is equidistant from (2, 5) and (3, 4). How many of the following cannot be the coordinates of P?<br>(i) (0, −2)<br>(ii) (1, 3)<br>(iii) (2.5, 4.5)<br>(iv) (4, −6)", ["1", "2", "3", "4"], "MCQ", "2", ["Geometry::Coordinate_Geometry"], "Easy",
 "P lies on the perpendicular bisector: y = x + 2.",
 steps(("Check", p("(1, 3) and (2.5, 4.5) lie on it; (0, −2) and (4, −6) don’t."))) + final("2, option 2"),
 why_rows=[("1", "Two fail."), ("3", "Two work."), ("4", "Two work.")])

P.qa(15, "A pencil has a cylindrical body (diameter 2 cm, length 12 cm) and a conical tip (length 3 cm)." + F.PENCIL + "The body breaks into two parts along a plane parallel to the base. Part A is the unbroken part still attached to the tip; part B is the broken-off part. If (volume of A) : (volume of B) equals (volume of B) : (volume of the tip), what is the length (in cm) of part B?", [], "TITA", "3", ["Geometry::Mensuration"], "Medium",
 "With radius 1, a cylinder of length L has volume πL; the tip has volume π.",
 steps(("Equation", p(r"\(\dfrac{12 - b}b = \dfrac b1\): \(b^2 + b - 12 = 0\), b = 3."))) + final("3"))

P.qa(16, r"Find the maximum possible value of \(\log_m\left(\dfrac{m^2}n\right) + \log_n\left(\dfrac{n^2}m\right)\), where \(m \ge n > 1\).", ["0", "1", "2", "3"], "MCQ", "3", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Write t = log_m n > 0.",
 steps(("Simplify", p(r"\((2 - t) + \left(2 - \tfrac1t\right) = 4 - \left(t + \tfrac1t\right)\).")),
       ("Maximum", p(r"\(t + \tfrac1t \ge 2\), equal at t = 1 (m = n): maximum 2."))) + final("2, option 3"),
 why_rows=[("1", "Not the maximum."), ("2", "Not the maximum."), ("4", r"\(t + \tfrac1t\) can’t be 1.")])

P.qa(17, "On level ground, a train’s speed falls in proportion to the square of the number of carriages: with 3 carriages it runs at 90 km/h, with 5 at 58 km/h. Uphill its speed drops by 6 km/h; downhill it rises by 9 km/h. With 6 carriages, how long does a 12 km ride take if half of it is uphill and half downhill?", ["15 minutes", "20 minutes", "24 minutes", "18 minutes"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "v = v₀ − kc².",
 steps(("Constants", p(r"\(16k = 32\): k = 2, \(v_0 = 108\). With 6 carriages: 36 km/h.")),
       ("Time", p(r"\(\tfrac6{30} + \tfrac6{45} = \tfrac13\) h = 20 minutes."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Ignores the slopes."), ("4", "Arithmetic slip.")])

P.qa(18, "44 terms of an arithmetic progression, in ascending order, are split into four groups A, B, C and D of 11 consecutive terms each. The average of group A is 32 and of group D is 197. What is the square of the difference between the averages of groups C and B?", [], "TITA", "3025", ["Algebra::Progressions_and_Series"], "Easy",
 "Each group’s average is its middle term.",
 steps(("d", p(r"Terms 6 and 39: \(33d = 165\), d = 5.")),
       ("C − B", p(r"Terms 28 and 17: \(11d = 55\); \(55^2 = 3025\)."))) + final("3025"))

P.qa(19, "In the series (0, 2, 4); (6, 8, 10, 12, 14, 16); (18, 20, …, 34); … there are 100 such brackets. What is the 33rd term in the 51st bracket?", ["7314", "7714", "7804", "None of these"], "MCQ", "2", ["Algebra::Progressions_and_Series"], "Medium",
 "Bracket k has 3k terms of the even numbers 0, 2, 4, …",
 steps(("Before bracket 51", p(r"\(3(1 + 2 + \dots + 50) = 3825\) terms.")),
       ("Value", p(r"The 3858th even number from 0: \(2 \times 3857 = 7714\)."))) + final("Option 2"),
 why_rows=[("1", "Off by 200 terms."), ("3", "Arithmetic slip."), ("4", "Option 2 is right.")])

P.qa(20, "x and y are natural numbers such that HCF(x, y) × x × y = 4116. What is the minimum possible value of x + y?", [], "TITA", "49", ["Number_System::Factors_and_Divisibility"], "Medium",
 "Write x = ha, y = hb with a, b coprime: h³ab = 4116 = 2² × 3 × 7³.",
 steps(("h", p(r"\(h^3\) divides 4116: h = 1 or 7.")),
       ("Best", p(r"h = 7: ab = 12 with a, b coprime: (3, 4) gives 7 × 7 = 49. h = 1 gives much larger sums."))) + final("49"))

P.qa(21, "The incomes of Prabhat and Komal are in the ratio 7 : 4 and their expenses in the ratio 5 : 4. If their savings are in the ratio 25 : 4, what percentage of her income does Komal save?", ["25%", "20%", "15%", "10%"], "MCQ", "4", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Incomes 7k, 4k; expenses 5e, 4e.",
 steps(("Solve", p(r"\(4(7k - 5e) = 25(4k - 4e)\) gives e = 0.9k.")),
       ("Komal", p(r"Saves \(4k - 3.6k = 0.4k\): 10%."))) + final("Option 4"),
 why_rows=[("1", "Wrong e."), ("2", "Wrong e."), ("3", "Wrong e.")])

P.qa(22, r"For real x, let f(x) be the greatest integer less than or equal to x. How many distinct values can \(f(y - 3x)\) take, given that \(y = 3f(x) + 4 = 4f(x - 3) + 5\)?", ["2", "3", "4", "5"], "MCQ", "3", ["Algebra::Functions"], "Hard",
 "\\(f(x - 3) = f(x) - 3\\).",
 steps(("f(x)", p(r"\(3f(x) + 4 = 4f(x) - 7\): f(x) = 11, y = 37, and \(11 \le x < 12\).")),
       ("y − 3x", p(r"\(37 - 3x\) runs over \((1, 4]\): floor values 1, 2, 3, 4."))) + final("4, option 3"),
 why_rows=[("1", "Misses values."), ("2", "Misses x = 11, which gives 4."), ("4", "1 < y − 3x, so 0 can’t occur.")])
