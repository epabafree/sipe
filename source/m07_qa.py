# -*- coding: utf-8 -*-
# Simp Mock 7: QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m07 import P

SLIP = lambda *o: [(x, "Arithmetic slip.") for x in o]

P.qa(1, "In triangle ABC the altitudes AD, BE and CF are in the ratio 7 : 5 : 4. Which is definitely true?", ["Triangle ABC is acute-angled.", "Triangle ABC is obtuse-angled.", "No triangle has altitudes in this ratio.", "More information is needed."], "MCQ", "2", ["Geometry::Triangles"], "Hard",
 "Each side is inversely proportional to its altitude.",
 steps(("Sides", p("BC : CA : AB = 1/7 : 1/5 : 1/4 = 20 : 28 : 35.")),
       ("Triangle?", p("20 + 28 > 35, so it exists.")),
       ("Type", p("35² = 1225 > 20² + 28² = 1184: obtuse."))) + final("Option 2"),
 why_rows=[("1", "The largest angle is obtuse."), ("3", "20 + 28 > 35."), ("4", "The ratio is enough.")])

P.qa(2, "Labour law limits factory work to 8 hours a day. Rama, Shyama and Tama, working 8 hours a day together, finish a job in 7 days; alone, their times are in the ratio 5 : 8 : 10. They work together for 6 hours 48 minutes a day for the first 5 days. At least how many more full days (any part counts as a full day) do Rama and Tama alone need to finish, keeping to the law?", [], "TITA", "4", ["Arithmetic::Time_and_Work"], "Medium",
 "Hourly rates 8 : 5 : 4.",
 steps(("Job", p("7 × 8 × 17 = 952 units.")),
       ("Done", p("5 × 6.8 × 17 = 578 units; 374 left.")),
       ("Rama and Tama", p("12 units an hour, 96 a day: 374 ÷ 96 ≈ 3.9, so 4 days."))) + final("4"))

P.qa(3, "The numbers of sides of regular polygons A and B are in the ratio n : (n + 1), and their interior angles are in the ratio (n + 1) : (n + 2). How many sides does A have?", [], "TITA", "4", ["Geometry::Polygons_and_Quadrilaterals"], "Hard",
 "Let A have nk sides and B (n + 1)k.",
 steps(("Angles", p(r"\(\dfrac{180 - 360/(nk)}{180 - 360/((n+1)k)} = \dfrac{n + 1}{n + 2}\)")),
       ("Simplify", p("This reduces to nk = 4.")),
       ("Check", p("n = 1, k = 4: a square and an octagon, 90° : 135° = 2 : 3."))) + final("4"))

P.qa(4, "M and N are positive integers with 2M + 3N = 53. What is the average of the largest and smallest possible values of M + N?", ["21", "21.5", "22", "22.5"], "MCQ", "3", ["Algebra::Linear_Equations"], "Easy",
 "2(M + N) + N = 53, so N is odd.",
 steps(("Largest", p("N = 1: M + N = 26.")), ("Smallest", p("N = 17, M = 1: M + N = 18.")),
       ("Average", p("22."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(5, "Naveen expected his electricity use in the four quarters of a year to be in the ratio 3 : 7 : 6 : 4, and budgeted ₹14,000 for the year. His actual bills for the first three quarters differed from plan by +10%, +5% and −4%. By what percentage must he cut his fourth-quarter use to stay within budget? (The bill is proportional to use.)", [r"\(10\tfrac14\)", r"\(12\tfrac23\)", r"\(14\tfrac12\)", r"\(18\tfrac13\)"], "MCQ", "1", ["Arithmetic::Percentages"], "Easy",
 "Planned: 2100, 4900, 4200, 2800.",
 steps(("Overspend", p("210 + 245 − 168 = ₹287.")), ("Cut", p("287 ÷ 2800 = 10.25%."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(6, "Container A holds 1 litre of pure milk. A milkman pours one-third of it into an empty bowl, refills A with water, pours half of A into the bowl, then refills A with water again and pours all of A into the bowl. What percentage of the bowl is milk?", [r"\(45\tfrac{5}{11}\)", r"\(54\tfrac{6}{11}\)", r"\(45\tfrac{6}{11}\)", r"\(54\tfrac{5}{11}\)"], "MCQ", "2", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "All the milk ends in the bowl.",
 steps(("Volume", p("1/3 + 1/2 + 1 = 11/6 litres, with all 1 litre of milk.")), ("Share", p("6/11 = 54 6/11 %."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(7, r"A bacteria colony grows to \((1 + \tfrac11)(1 + \tfrac12)(1 + \tfrac13)\cdots(1 + \tfrac1n)\) times its size at the end of n days. After how many hours is it 100 times its size?", ["99", "2400", "2376", "2352"], "MCQ", "3", ["Algebra::Progressions_and_Series"], "Easy",
 "The product telescopes.",
 steps(("Telescope", p("2 · 3/2 · 4/3 ⋯ (n + 1)/n = n + 1.")), ("Hours", p("n = 99 days = 2376 hours."))) + final("Option 3"),
 why_rows=[("1", "Days, not hours."), ("2", "Uses 100 days."), ("4", "Uses 98 days.")])

P.qa(8, r"\(a_1 \ge a_2 \ge \dots \ge a_n\) are natural numbers with average 100. How many different values can \(a_n\) take?", [], "TITA", "100", ["Arithmetic::Average"], "Easy",
 "The smallest term is at most the average.",
 steps(("Range", p("a<sub>n</sub> ≤ 100 (it is the smallest), and any value from 1 to 100 works.")), ("Count", p("100."))) + final("100"))

P.qa(9, r"a is a non-zero real number and 5/a is a root of \(ax^3 - 5x^2 - 6x + 15 = 0\). Find a.", ["2", "5/2", "−2", "3"], "MCQ", "1", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Substitute x = 5/a.",
 steps(("Substitute", p(r"\(\tfrac{125}{a^2} - \tfrac{125}{a^2} - \tfrac{30}{a} + 15 = 0\), so 30/a = 15.")), ("a", p("a = 2."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(10, "f is a function such that f(x² + x) = 20 for every integer x. Find f(f(f(f(30)))).", [], "TITA", "20", ["Algebra::Functions"], "Easy",
 "x² + x = x(x + 1).",
 steps(("30", p("30 = 5 × 6, so f(30) = 20.")), ("20", p("20 = 4 × 5, so f(20) = 20, and so on."))) + final("20"))

P.qa(11, "In a board exam, 5% of registered students were absent and 8% of those present failed. Those who passed were in first division, second division and pass division in the ratio 5 : 3 : 2. First division exceeded pass division by 2622. How many students sat the exam?", ["10000", "11000", "9500", "11400"], "MCQ", "3", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "0.92N × 3/10 = 2622.",
 steps(("Solve", p("0.276N = 2622, N = 9500."))) + final("Option 3"),
 why_rows=[("1", "Registered students."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(12, "How many 4-digit numbers divisible by 8 can be made from the digits 0, 1, 2, 3 and 4 without repetition?", ["8", "12", "14", "16"], "MCQ", "4", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "Check the last three digits.",
 steps(("Endings", p("The last three digits must form a multiple of 8. With distinct digits from 0–4: 024, 032, 104, 120, 240, 304, 320 (each containing 0) and 312, 432 (no 0).")),
       ("Leading digit", p("An ending with 0 leaves two non-zero digits for the front: 7 × 2 = 14. An ending without 0 leaves 0 and one other digit, and 0 cannot lead: 2 × 1 = 2.")),
       ("Count", p("14 + 2 = 16."))) +
 final("Option 4"),
 why_rows=SLIP("1", "2", "3"))

P.qa(13, "A prime P divides 100! − 1. Which must be true?", ["P = 2", "P = 53", "53 < P ≤ 97", "P ≥ 101"], "MCQ", "4", ["Number_System::Factorials"], "Medium",
 "Every prime up to 100 divides 100!.",
 steps(("Primes ≤ 100", p("They divide 100!, so they leave remainder −1 on 100! − 1.")), ("So", p("P > 100, i.e. P ≥ 101."))) + final("Option 4"),
 why_rows=[("1", "2 divides 100!."), ("2", "53 divides 100!."), ("3", "These divide 100!.")])

P.qa(14, r"How many integers x satisfy \(\dfrac{\log_3 x - 2}{5 - \log_2 x} > 0\)?", ["20", "21", "22", "23"], "MCQ", "3", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Numerator positive for x > 9, denominator positive for x < 32.",
 steps(("Signs", p("Both positive for 9 < x < 32; both negative never.")), ("Count", p("10 to 31: 22 integers."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(15, "A 10-question test is summarised as a string: Y for correct, N for wrong, U for unattempted. A student got at least 8 correct. How many different summaries are possible?", ["190", "191", "200", "201"], "MCQ", "4", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "8, 9 or 10 correct.",
 steps(("8 Y", p("C(10, 8) × 2² = 180.")), ("9 Y", p("10 × 2 = 20.")), ("10 Y", p("1.")), ("Total", p("201."))) + final("Option 4"),
 why_rows=[("1", "Misses some."), ("2", "Misses some."), ("3", "Misses all-correct.")])

P.qa(16, "Five students have different whole-number heights between 135 cm and 170 cm. Their average is 150 cm and exactly two are shorter than 150 cm. What is the difference between the largest and smallest possible heights of the second-tallest?", ["13", "14", "15", "10"], "MCQ", "1", ["Arithmetic::Average"], "Medium",
 "Total 750.",
 steps(("Largest", p("Others as small as possible: 135, 136, 150. The two tallest add to 329, so the second-tallest is at most 164.")),
       ("Smallest", p("148, 149, 150, 151, 152: the second-tallest can be 151.")),
       ("Difference", p("13."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(17, r"How many integers x satisfy \((x^2 + 6x + 8)^{x^2 - x - 20} = 1\)?", [], "TITA", "2", ["Algebra::Quadratic_Equations"], "Hard",
 "Exponent 0, base 1, or base −1 with even exponent.",
 steps(("Exponent 0", p("x = 5 or −4; but x = −4 makes the base 0 (0⁰ is undefined), so only x = 5.")),
       ("Base 1", p("x² + 6x + 7 = 0: no integer roots.")),
       ("Base −1", p("(x + 3)² = 0: x = −3, exponent −8 (even). Works.")),
       ("Count", p("2."))) + final("2"))

P.qa(18, "Mr Sharma invests half his capital at r%, two-fifths at 12.5% and the rest at 25%, all simple interest. In 8 years the total interest equals his capital. Find r.", [], "TITA", "10", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Yearly interest must be 12.5% of capital.",
 steps(("Equation", p("0.5r + 0.4 × 12.5 + 0.1 × 25 = 12.5, so 0.5r = 5.")), ("r", p("10."))) + final("10"))

P.qa(19, r"\(t_1 = 5\), \(t_2 = 5 + 9\), \(t_3 = 5 + 9 + 13\), and so on. Find \(\sum_{n=1}^{20} t_n\).", ["5740", "5950", "6370", "6655"], "MCQ", "3", ["Algebra::Progressions_and_Series"], "Medium",
 r"\(t_n = 2n^2 + 3n\).",
 steps(("Sum", p(r"\(2 \cdot \tfrac{20 \cdot 21 \cdot 41}{6} + 3 \cdot \tfrac{20 \cdot 21}{2}\) \(= 5740 + 630 = 6370\)."))) + final("Option 3"),
 why_rows=[("1", "Only the squares part."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(20, "f(x) = x² + bx + c has minimum value −9 at x = 7. What is the product of the roots of f(x) = 0?", ["33", "27", "40", "More information is needed"], "MCQ", "3", ["Algebra::Quadratic_Equations"], "Easy",
 "f(x) = (x − 7)² − 9.",
 steps(("Expand", p("x² − 14x + 40: product 40 (roots 4 and 10)."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(21, "ABCD is a trapezium with AB ⊥ BC and BC ⊥ CD, and ∠BAD obtuse. tan ∠ADC = 0.75, CD = 7 cm and AD = 5 cm. Find the perimeter (in cm).", [], "TITA", "18", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "Drop AE ⊥ CD.",
 steps(("3-4-5", p("AE : ED = 3 : 4 with AD = 5: AE = 3 = BC, ED = 4.")), ("AB", p("CD − ED = 3.")), ("Perimeter", p("3 + 3 + 7 + 5 = 18."))) + final("18"))

P.qa(22, "Two cars leave a fork in the road at the same time, one going west at W km/h and the other north-east at N km/h. How far apart are they after one hour (in km)?", [r"\(\sqrt{W^2 + N^2 - \sqrt2\,WN}\)", r"\(\sqrt{W^2 + N^2 + \sqrt2\,WN}\)", r"\(\sqrt{W^2 + N^2}\)", "W + N"], "MCQ", "2", ["Geometry::Trigonometry"], "Medium",
 "The angle between west and north-east is 135°.",
 steps(("Cosine rule", p(r"\(d^2 = W^2 + N^2 - 2WN\cos 135°\)") + p(r"\(= W^2 + N^2 + \sqrt2\,WN\)."))) + final("Option 2"),
 why_rows=[("1", "Uses 45°."), ("3", "Uses 90°."), ("4", "Uses 180°.")])
