# -*- coding: utf-8 -*-
# Simp Mock 16 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_16 import P

P.qa(1, "Six distinct letters go into six matching addressed envelopes, one per envelope. In how many ways can exactly 3 letters go into their correct envelopes and the other 3 into wrong ones?", [], "TITA", "40", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Choose the correct three, then derange the rest.",
 steps(("Choose", p(r"\(\binom63 = 20\).")), ("Derange", p("Three letters, all wrong: 2 ways.")), ("Total", p("40."))) + final("40"))

P.qa(2, r"Let \(f_1(x) = \tfrac1x\), \(f_2(x) = x + 2\) and \(f_3(x) = \tfrac{1}{x - 2}\). Find \(f_3(f_2(f_1(f_3(f_2(f_1(4))))))\).", ["16", r"\(\tfrac1{16}\)", "4", "6"], "MCQ", "3", ["Algebra::Functions"], "Easy",
 r"What does \(f_3(f_2(f_1(x)))\) do?",
 steps(("Composite", p(r"\(f_2(f_1(x)) = \tfrac1x + 2\), so \(f_3\) of it is \(\tfrac{1}{1/x} = x\).")), ("Apply twice", p("4 comes back as 4."))) + final("Option 3"),
 why_rows=[("1", "Squares it."), ("2", "Reciprocal of 16."), ("4", "Arithmetic slip.")])

P.qa(3, "Pawan borrows ₹20,00,000 at 8% a year, compounded annually, to be repaid in two equal instalments at the ends of the first and second years. The first instalment covers the first year’s interest on the whole loan plus part of the principal; the second covers the rest of the principal plus one year’s interest on it. Roughly how much is each instalment?", ["₹10,61,238", "₹10,91,538", "₹11,21,538", "₹11,51,338"], "MCQ", "3", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "First instalment = 1,60,000 + p.",
 steps(("Equation", p("(20,00,000 − p) × 1.08 = 1,60,000 + p, so 2.08p = 20,00,000: p ≈ 9,61,538.")), ("Instalment", p("1,60,000 + 9,61,538 = 11,21,538."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(4, "Sahil buys n dozen strawberry candies at ₹18 a dozen and n dozen mango candies at ₹15 a dozen, and sells all of them at ₹22 a dozen for a profit of more than ₹100. What is the least number of dozens he could have bought in all (n a natural number)?", ["10", "12", "19", "20"], "MCQ", "4", ["Arithmetic::Profit_and_Loss"], "Easy",
 "Profit per pair of dozens: 44 − 33 = 11.",
 steps(("n", p("11n > 100 needs n = 10.")), ("Total", p("2n = 20 dozen."))) + final("Option 4"),
 why_rows=[("1", "n, not 2n."), ("2", "Arithmetic slip."), ("3", "Profit 99 is not more than 100.")])

P.qa(5, r"The LCM of the positive integers \(6^{32}\), \(15^9\) and K is \(45^9 \times 12^{16}\). How many values can K take?", ["330", "288", "248", "220"], "MCQ", "1", ["Number_System::Factors_and_Divisibility"], "Medium",
 "Write everything in primes.",
 steps(("LCM", p(r"\(2^{32} \cdot 3^{34} \cdot 5^9\); the given numbers supply \(2^{32}\), \(3^{32}\) and \(5^9\).")),
       ("K", p(r"K must supply \(3^{34}\) exactly; 2’s exponent 0–32 (33 ways), 5’s 0–9 (10 ways).")), ("Count", p("33 × 10 = 330."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(6, r"If \(\log_3[1 + \log_4(10 + 2\log_3 x)] = 1\), find x.", ["3", "9", "27", "81"], "MCQ", "3", ["Algebra::Logarithms_and_Exponents"], "Easy",
 "Peel from the outside.",
 steps(("Unwrap", p(r"\(1 + \log_4(\cdot) = 3\), so \(10 + 2\log_3x = 16\) and \(\log_3x = 3\).")), ("x", p("27."))) + final("Option 3"),
 why_rows=[("1", "Stops early."), ("2", "Stops early."), ("4", "Overshoots.")])

P.qa(7, "In a circle of radius 13 cm, PQ is a diameter and RS a chord of length 22 cm. RS meets PQ at a point T inside the circle with PT = 5 cm. What is the difference between RT and TS (in cm)?", ["2", "4", "6", "8"], "MCQ", "4", ["Geometry::Circles"], "Easy",
 "Intersecting chords: RT × TS = PT × TQ.",
 steps(("Product", p("5 × 21 = 105, with RT + TS = 22.")), ("Lengths", p("15 and 7: difference 8."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(8, r"Find \(\tfrac{9!}{11!} + \tfrac{8!}{10!} + \tfrac{7!}{9!} + \tfrac{6!}{8!} + \tfrac{5!}{7!}\).", [r"\(\tfrac15\)", r"\(\tfrac3{10}\)", r"\(\tfrac5{11}\)", r"\(\tfrac5{66}\)"], "MCQ", "4", ["Algebra::Progressions_and_Series"], "Easy",
 r"\(\tfrac{(n-2)!}{n!} = \tfrac{1}{n(n-1)} = \tfrac{1}{n-1} - \tfrac1n\).",
 steps(("Telescope", p(r"\(\big(\tfrac1{10} - \tfrac1{11}\big) + \dots + \big(\tfrac16 - \tfrac17\big)\) \(= \tfrac16 - \tfrac1{11} = \tfrac5{66}\)."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(9, r"If \(x^2 - 1 = 13k\), where k is prime and x an integer, how many values can x take?", [], "TITA", "2", ["Number_System::Factors_and_Divisibility"], "Medium",
 "(x − 1)(x + 1) = 13k: one factor is ±13, the other ±k.",
 steps(("Cases", p("x + 1 = 13 gives k = 11 (prime), x = 12. x − 1 = 13 gives k = 15, not prime. Likewise x = −12 works and x = −14 doesn’t.")),
       ("Other splits", p("A factor of ±1 makes the other ±3, not 13k."))) + final("2"))

P.qa(10, "Find the minimum value of |x − 1| + |x − 2| + |x − 3| + … + |x − 100|.", [], "TITA", "2500", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "The sum is least at a median.",
 steps(("Pairing", p("Pair |x − 1| with |x − 100|, |x − 2| with |x − 99|, …: each pair is at least the gap, 99, 97, …, 1, reached for x between 50 and 51.")),
       ("Sum", p(r"\(1 + 3 + \dots + 99 = 50^2 = 2500\)."))) + final("2500"))

P.qa(11, "Rectangle ABCD has integer length and breadth, with length greater than breadth, and its area is numerically twice its perimeter. How many such rectangles are there?", [], "TITA", "2", ["Geometry::Mensuration"], "Easy",
 "ℓb = 4(ℓ + b) factorises.",
 steps(("Factor", p("(ℓ − 4)(b − 4) = 16.")), ("Pairs", p("16 × 1 and 8 × 2 give (20, 5) and (12, 6); 4 × 4 is a square."))) + final("2"))

P.qa(12, "In a regular polygon, the exterior and interior angles are in the ratio 1 : 3. How many sides does it have?", [], "TITA", "8", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "They add to 180°.", steps(("Exterior", p("45°, so 360 ÷ 45 = 8 sides."))) + final("8"))

P.qa(13, "A and B together finish a job in 40 days, B and C in 60 days, and A and C in 50 days. How long would the most efficient of the three take alone?", ["more than 70 but less than 71 days", "more than 72 but less than 73 days", "more than 73 but less than 75 days", "None of these"], "MCQ", "1", ["Arithmetic::Time_and_Work"], "Medium",
 "Take the job as 600 units.",
 steps(("Rates", p("A + B = 15, B + C = 10, A + C = 12; all three 18.5. A = 8.5, B = 6.5, C = 3.5.")), ("A alone", p("600 ÷ 8.5 ≈ 70.6 days."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Option 1 fits.")])

P.qa(14, "10 litres of a milk–water mixture gets 5 more litres of pure water, and the ratio of milk to water is reversed. How many litres of water are in the final mixture?", [], "TITA", "9", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "m : w becomes w : m.",
 steps(("Equation", p(r"\(\tfrac{m}{w + 5} = \tfrac{w}{m}\) gives \(m^2 = w(w + 5)\); with m = 10 − w, 100 − 20w = 5w, so w = 4.")), ("Final", p("4 + 5 = 9."))) + final("9"))

P.qa(15, r"A ping-pong ball is dropped from 100 m. After each bounce it rises to a fraction of the height it fell from, alternating \(\tfrac34\), \(\tfrac12\), \(\tfrac34\), \(\tfrac12\), … forever. What total vertical distance does it travel before coming to rest?", ["460 m", "480 m", "560 m", "580 m"], "MCQ", "1", ["Algebra::Progressions_and_Series"], "Medium",
 r"Every two bounces multiply the height by \(\tfrac38\).",
 steps(("Heights", p(r"Rises: 75, 37.5, then \(\tfrac38\) of those, and so on.")),
       ("Sum", p(r"\(100 + 2(75 + 37.5) \cdot \tfrac{1}{1 - 3/8}\) \(= 100 + 225 \times \tfrac85 = 460\)."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(16, "The average score of 60 students in a test is 62. The top 20% average 90 and the bottom 30% average 40. The rest are split into two groups, A and B, each with at least one student; both group averages are natural numbers, and group A’s average is 6 more than group B’s. How many ordered pairs (n<sub>A</sub>, n<sub>B</sub>) of group sizes are possible?", [], "TITA", "5", ["Arithmetic::Average"], "Medium",
 "The middle 30 students average 64.",
 steps(("Middle group", p("3720 − 1080 − 720 = 1920 for 30 students.")),
       ("Equation", p(r"With group A’s average a: \(30a - 6n_B = 1920\), so \(n_B = 5a - 320\), a multiple of 5.")),
       ("Count", p(r"\(n_B\) = 5, 10, 15, 20, 25: five pairs."))) + final("5"))

P.qa(17, "Prashant, Rajesh and Sanjay start a business with ₹60,000, ₹20,000 and ₹80,000. Prashant changes nothing. Rajesh adds ₹10,000 at the start of the (n + 1)th month and again at the start of the (2n + 1)th month. Sanjay withdraws ₹20,000 at the start of the (m + 1)th month and again at the start of the (2m + 1)th month. The year’s profit is shared 12 : 6 : 13. Find n + m.", ["10", "9", "8", "Less than 8"], "MCQ", "2", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "Capital × months, in thousands.",
 steps(("Rajesh", p("240 + 10(12 − n) + 10(12 − 2n) = 480 − 30n.")), ("Sanjay", p("960 − 20(12 − m) − 20(12 − 2m) = 480 + 60m.")),
       ("Ratio", p("Prashant’s 720 is 12 parts of 60: 480 − 30n = 360 gives n = 4; 480 + 60m = 780 gives m = 5."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(18, "A body thrown straight up from the ground with speed u m/s has risen ut − kt² metres after t seconds, for some constant k. The distances it covers in the 3rd and 8th seconds are in the ratio 2 : 1. What is the ratio of the distances covered in the 5th and 6th seconds?", ["6 : 5", "7 : 6", "8 : 7", "More information is needed"], "MCQ", "3", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Distance in the t-th second: u − k(2t − 1).",
 steps(("Ratio", p("(u − 5k) = 2(u − 15k), so u = 25k.")), ("5th and 6th", p("16k : 14k = 8 : 7."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "The ratio fixes u : k.")])

P.qa(19, r"Which of these is a factor of \(x^6 + 20x^3 - 8\)?", [r"\(x^2 - 2x + 2\)", r"\(x^2 + 2x - 2\)", r"\(x^2 - 2x - 2\)", r"\(x^2 + 2x + 2\)"], "MCQ", "2", ["Algebra::Equations_and_Polynomials"], "Medium",
 r"\(a^3 + b^3 + c^3 - 3abc\) has the factor a + b + c.",
 steps(("Match", p(r"With \(a = x^2\), \(b = 2x\), \(c = -2\): \(a^3 + b^3 + c^3 = x^6 + 8x^3 - 8\) and \(-3abc = 12x^3\).")), ("Factor", p(r"\(x^2 + 2x - 2\)."))) + final("Option 2"),
 why_rows=[("1", "Signs wrong."), ("3", "Signs wrong."), ("4", "Signs wrong.")])

P.qa(20, "Bus A leaves Mumbai for Kolhapur; an hour later bus B leaves Kolhapur for Mumbai at four-fifths of A’s speed. They meet at a point three-fifths of the way from Mumbai. How long does B take from Kolhapur to Mumbai?", ["10 hours", "10.5 hours", "12 hours", "12.5 hours"], "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Speeds 5s and 4s; distance 5D.",
 steps(("Meeting", p("B covers 2D while A covers 2.5D in the same time, so A’s first hour covered 0.5D: A takes 10 hours for 5D.")), ("B", p("B is ⅘ as fast: 12.5 hours."))) + final("Option 4"),
 why_rows=[("1", "Bus A’s time."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(21, "n students sit in chairs numbered 1 to n. A camp runs n rounds; at the end of round 1 the student in chair 1 leaves, at the end of round 2 the one in chair 2 leaves, and so on. At the start of each round the mentor adds up the chair numbers of the students present. The average of these n sums is 426. Find n.", ["23", "33", "35", "73"], "MCQ", "3", ["Algebra::Progressions_and_Series"], "Medium",
 "Chair k is counted in k sums.",
 steps(("Total", p(r"\(\sum k^2 = \tfrac{n(n + 1)(2n + 1)}{6}\); average \(\tfrac{(n + 1)(2n + 1)}{6} = 426\).")), ("n", p("(n + 1)(2n + 1) = 2556 = 36 × 71: n = 35."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(22, "360 students attended a sports meet; 17 played no sport. 12 played all three of football, cricket and basketball. Football players outnumbered basketball players by 60, and 220 played cricket. Those who played football and cricket but not basketball equalled those who played cricket and basketball but not football, and this number was 2 more than those who played only cricket. Those who played football and basketball but not cricket were a quarter of those who played only basketball. How many played only football?", ["86", "82", "88", "80"], "MCQ", "3", ["Modern_Maths::Set_Theory"], "Medium",
 "Start from cricket.",
 steps(("Cricket", p("c + 2(c + 2) + 12 = 220 gives only-cricket c = 68 and the two pair regions 70 each.")),
       ("Football vs basketball", p("Only-basketball z, football-and-basketball-only z/4: F − B = only-football − z = 60.")),
       ("Total", p("343 = (z + 60) + z + 68 + 140 + z/4 + 12, so 2.25z = 63, z = 28: only football 88."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])
