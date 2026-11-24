# -*- coding: utf-8 -*-
# Simp Mock 12: QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m12 import P
import m12_figs as F

SLIP = lambda *o: [(x, "Arithmetic slip.") for x in o]

P.qa(1, "A frog sits on vertex 1 of a regular hexagon with vertices numbered 1 to 6 clockwise. It jumps clockwise one vertex at a time to vertex 6, then reverses and jumps n times to land on vertex 1 again. From then on it jumps n times clockwise and n times counter-clockwise, alternately. If it is on vertex 5 after a total of m³ jumps (m a natural number), m can be:", ["5", "6", "7", "8"], "MCQ", "2", ["Number_System::Remainders"], "Medium",
 "n = 5, so the pattern repeats every 10 jumps.",
 steps(("Pattern", p("In each 10 jumps it reaches vertex 5 after 4 and after 6 jumps.")),
       ("Cubes", p("m³ must end in 4 or 6: 6³ = 216."))) + final("Option 2"),
 why_rows=[("1", "125 ends in 5."), ("3", "343 ends in 3."), ("4", "512 ends in 2.")])

P.qa(2, "Chitra invests ₹1,40,000 at 6% in bank X, ₹1,00,000 at 4% in bank Y and the rest of her ₹3,20,000 at x% in bank Z, all simple interest. Her yearly interest is 5% of ₹3,20,000. What would one year’s interest be if she put all ₹3,20,000 in bank Z?", ["16000", "12800", "11200", "14400"], "MCQ", "4", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "Find x.",
 steps(("Bank Z", p("16,000 − 8400 − 4000 = 3600 on ₹80,000: 4.5%.")),
       ("All in Z", p("4.5% of 3,20,000 = 14,400."))) + final("Option 4"),
 why_rows=[("1", "5% of the capital."), ("2", "4%."), ("3", "3.5%.")])

P.qa(3, "a + b = 1 and a² + b² = 2. Find a⁶ + b⁶.", [r"\(\tfrac{13}{2}\)", r"\(\tfrac{15}{2}\)", r"\(\tfrac{11}{2}\)", r"\(\tfrac72\)"], "MCQ", "1", ["Algebra::Equations_and_Polynomials"], "Easy",
 "ab = −½.",
 steps(("Cubes of squares", p("a⁶ + b⁶ = (a² + b²)³ − 3a²b²(a² + b²) = 8 − 3 × ¼ × 2 = 6.5."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(4, r"X and Y are distinct natural numbers, and \(\log_a X > \log_a Y\) implies X < Y. Which can be the value of a?", ["10", "5", "1", "0.5"], "MCQ", "4", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "The log must be decreasing.",
 steps(("Base", p("Decreasing logs need 0 < a < 1: 0.5."))) + final("Option 4"),
 why_rows=[("1", "Increasing."), ("2", "Increasing."), ("3", "Not a valid base.")])

P.qa(5, "Walking up a moving escalator at his normal speed, Remus takes 30 seconds; walking at twice that speed, 18 seconds. How many seconds would he take standing still?", [], "TITA", "90", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Same length both ways.",
 steps(("Equation", p("30(r + e) = 18(2r + e), so r = 2e.")),
       ("Standing", p("Length 90e, time 90 s."))) + final("90"))

P.qa(6, "The price of mangoes falls 25%, and Reshma gets 400 g more for the same budget. How many grams had she planned to buy?", [], "TITA", "1200", ["Arithmetic::Percentages"], "Easy",
 "Same spend: PQ = 0.75P(Q + 0.4).",
 steps(("Solve", p("Q = 1.2 kg = 1200 g."))) + final("1200"))

P.qa(7, "a = 24 and 2a² + 8b² + 9c(a + 2c) = 4b(a + 3c) + 15ca, with a, b, c real. Find b + c.", ["12", "18", "20", "21"], "MCQ", "3", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Sum of three squares.",
 steps(("Rearrange", p("(a − 2b)² + (2b − 3c)² + (3c − a)² = 0, so a = 2b = 3c.")),
       ("Values", p("b = 12, c = 8: 20."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(8, "In triangle ABC, AC = 6 cm. The circle on diameter AC passes through B, and the circle with centre B passes through A and C. Find the area (in cm²) common to the two circles.", ["18(π − 1)", "9(π − 1)", "9π", "9(2π − 1)"], "MCQ", "2", ["Geometry::Circles"], "Medium",
 "ABC is a right isosceles triangle.",
 steps(("Shape", p(r"BA = BC = \(3\sqrt2\), ∠B = 90°.")),
       ("Overlap", p("Half the small circle (4.5π) plus the segment of the big circle beyond AC: (π × 18)/4 − 9 = 4.5π − 9.")),
       ("Total", p("9π − 9 = 9(π − 1)."))) + final("Option 2"),
 why_rows=[("1", "Doubles it."), ("3", "Leaves out the triangle."), ("4", "Adds too much.")])

P.qa(9, "Junior students average 45 kg and senior students 69 kg; the combined average is a whole number. There are 12 more juniors than seniors. What is the difference between the largest and smallest possible numbers of students?", [], "TITA", "128", ["Arithmetic::Average"], "Hard",
 "With k seniors, the average is 57 − 144/(k + 6).",
 steps(("Average", p("(45(k + 12) + 69k) ÷ (2k + 12) = 57 − 144/(2k + 12).")),
       ("Integer", p("2k + 12 divides 144 and exceeds 12: from 16 (k = 2) to 144 (k = 66).")),
       ("Difference", p("144 − 16 = 128."))) + final("128"))

P.qa(10, "Trapezium PQRS has perimeter 30, SR ∥ PQ, and SP perpendicular to both. SR = 9 and PQ = 12. Find its area.", ["36", "39", "42", "45"], "MCQ", "3", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "QR is the hypotenuse over a 3-unit offset.",
 steps(("Height", p(r"\(h + \sqrt{h^2 + 9} = 9\), so h = 4.")),
       ("Area", p("½ × 21 × 4 = 42."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(11, "All roots of ax⁴ + bx³ + cx² + dx + e = 0 (a ≠ 0, all coefficients real) are real, and b² = 2ac. Which is definitely true?", ["The sum of any two roots equals the sum of the other two.", "b + c + d = e", "The product of the roots is not positive.", "All of these"], "MCQ", "4", ["Algebra::Equations_and_Polynomials"], "Hard",
 "Sum of squares of roots = (b² − 2ac)/a².",
 steps(("Roots", p("The squares of the real roots add to 0, so every root is 0.")),
       ("Then", p("b = c = d = e = 0; all three statements hold."))) + final("Option 4"),
 why_rows=[("1", "Others hold too."), ("2", "Others hold too."), ("3", "Others hold too.")])

P.qa(12, "Charan and Damodar are the children of Aabir and Bharti. Damodar is 3 years younger than Charan. Five years ago Aabir was five times Charan’s age. The average age of all four now equals the average of Charan and Bharti, and Bharti was 29 when Charan was born. How old is Damodar?", ["8", "9", "10", "12"], "MCQ", "3", ["Algebra::Linear_Equations"], "Medium",
 "Average condition: a + d = b + c.",
 steps(("Equations", p("a = b + 3, a = 5c − 20, b = c + 29.")),
       ("Solve", p("c + 32 = 5c − 20, so c = 13 and d = 10."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(13, "In a school, 30% of students belong to group A, 20% to B, 12.5% to C and the rest to D. English is spoken by 15% of A, 10% of B, 20% of C and 12% of D. What percentage of English speakers are from D?", [r"\(22\tfrac29\%\)", r"\(27\tfrac{3}{11}\%\)", r"\(33\tfrac13\%\)", r"\(37\tfrac37\%\)"], "MCQ", "3", ["Arithmetic::Percentages"], "Medium",
 "Speakers: 4.5, 2, 2.5 and 4.5 per 100 students.",
 steps(("Share", p("4.5 ÷ 13.5 = ⅓."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(14, r"In the figure, AC ⊥ BC, AC = \(2\sqrt6\) cm and BC = \(2\sqrt3\) cm. CD meets AB at P, and ∠BCD = ∠BAD. Find the radius (in cm) of the circle through A, C and D." + F.QUAD, ["1.5", "3", "4", "6"], "MCQ", "2", ["Geometry::Circles"], "Medium",
 "Equal angles on BD put A, B, C, D on one circle.",
 steps(("Concyclic", p("BD subtends equal angles at C and A, so A, B, C, D are concyclic.")),
       ("Radius", p(r"The circle through A, B, C has AB as diameter (∠C = 90°): \(AB = \sqrt{24 + 12} = 6\), radius 3."))) + final("Option 2"),
 why_rows=[("1", "Quarter of AB."), ("3", "Not from the figure."), ("4", "Diameter.")])

P.qa(15, "Coins in a line are numbered 1, 2, 3, … Raju picks coin 1, skips 1 coin and picks the next, skips 2 and picks the next, skips 3 and picks the next, and so on. What number is on the 100th coin he picks?", [], "TITA", "5050", ["Algebra::Progressions_and_Series"], "Medium",
 "He picks 1, 3, 6, 10, …",
 steps(("Pattern", p("The nth coin is 1 + 2 + … + n.")),
       ("100th", p("5050."))) + final("5050"))

P.qa(16, "Raja, Meera and Abhi alone would finish a project in 15, 30 and 60 days. All three start; Abhi works only on day 1, beyond his usual capacity, then falls ill, and the other two finish. Pay is in proportion to work: of ₹8,00,000, Raja gets ₹4,00,000. By what percentage did Abhi raise his output that day?", [], "TITA", "1400", ["Arithmetic::Time_and_Work"], "Medium",
 "Raja did half the work.",
 steps(("Days", p("Raja does ½ in 7.5 days; Meera does ¼ in that time.")),
       ("Abhi", p("He did ¼ in one day against his normal 1/60: 15 times, a 1400% rise."))) + final("1400"))

P.qa(17, "Solutions of 30%, 40% and 80% acid are mixed in volumes x, y and z ml, with z = 2x < y. What can be said about the highest possible concentration of the mixture (in %)?", ["Less than 54", "At least 54 but less than 55", "At least 55 but less than 56", "56 or more"], "MCQ", "1", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "More 40% solution lowers the mix.",
 steps(("Limit", p("At y = 2x the mix is (30 + 80 + 160) ÷ 5 = 54%. Since y > 2x, it stays below 54."))) + final("Option 1"),
 why_rows=[("2", "54 is never reached."), ("3", "Too high."), ("4", "Too high.")])

P.qa(18, "Tina hits the bullseye with probability 0.7 and Mina with 0.5. They throw alternately, Mina first. What is the probability that Mina hits before Tina?", [r"\(\tfrac{7}{17}\)", r"\(\tfrac23\)", r"\(\tfrac{10}{17}\)", r"\(\tfrac34\)"], "MCQ", "3", ["Modern_Maths::Probability"], "Hard",
 "A geometric series with ratio 0.5 × 0.3.",
 steps(("Sum", p("0.5 ÷ (1 − 0.15) = 10/17."))) + final("Option 3"),
 why_rows=[("1", "Tina’s chance."), ("2", "Slip."), ("4", "Slip.")])

P.qa(19, "Positive integers a, b, c are each at least the smallest prime, with ab + bc = 91 and ac + ab = 51. What is the least value of a + 2b + 3c?", ["47", "45", "43", "41"], "MCQ", "4", ["Number_System::Factors_and_Divisibility"], "Medium",
 "b(a + c) = 91, a(b + c) = 51.",
 steps(("Cases", p("a = 3, b + c = 17. b = 7, a + c = 13 gives c = 10 (sum 47); b = 13, a + c = 7 gives c = 4 (sum 41).")),
       ("Least", p("41."))) + final("Option 4"),
 why_rows=[("1", "The other case."), ("2", "Not a case."), ("3", "Not a case.")])

P.qa(20, "The roots of ax² + bx + c = 0 (a ≠ 0) are two consecutive integers. Which equals a² − b²?", ["4ac", "−4ac", "2ac", "−2ac"], "MCQ", "2", ["Algebra::Quadratic_Equations"], "Medium",
 "The roots differ by 1.",
 steps(("Difference", p("(root gap)² = (b² − 4ac)/a² = 1, so a² − b² = −4ac."))) + final("Option 2"),
 why_rows=[("1", "Sign slip."), ("3", "Factor slip."), ("4", "Factor slip.")])

P.qa(21, "A snack bar sells burgers at ₹80, dosas at ₹50 and juices at ₹35. One day it sold exactly 60 items for ₹2700. What is the largest possible number of burgers sold?", [], "TITA", "13", ["Algebra::Linear_Equations"], "Medium",
 "Eliminate burgers: 2d + 3f = 140.",
 steps(("Solutions", p("Each extra burger moves the solution by 3 dosas and 2 juices: (0, 40, 20), (1, 37, 22), …, (13, 1, 46).")),
       ("Largest", p("13."))) + final("13"))

P.qa(22, "In how many ways can 20 identical balloons be given to 4 children so that every child gets an odd number of balloons?", [], "TITA", "165", ["Modern_Maths::Permutations_and_Combinations"], "Hard",
 "Write each share as 2k + 1.",
 steps(("Reduce", p("k₁ + k₂ + k₃ + k₄ = 8.")),
       ("Count", p("¹¹C₃ = 165."))) + final("165"))
