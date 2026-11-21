# -*- coding: utf-8 -*-
# Simp Mock 8: QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m08 import P
import m08_figs as F

SLIP = lambda *o: [(x, "Arithmetic slip.") for x in o]

P.qa(1, "Three workers, Arun, Bala and Chetan, finish a job working two at a time, one pair a day. Starting on 1 July, Arun and Bala work on day 1, Bala and Chetan on day 2, Chetan and Arun on day 3, and this three-day roster repeats in order up to 28 July. On 29 July Bala is absent and the other worker finishes the job alone. Each works the same hours every day. In how many days would all three working together finish the job?", [], "TITA", "19", ["Arithmetic::Time_and_Work"], "Medium",
 "Each three-day cycle is two days of all three together.",
 steps(("Cycles", p("Days 1–27 are 9 cycles: 9 × 2 = 18 days’ worth of all three.")),
       ("Last two days", p("28 July: Arun and Bala. 29 July: Chetan alone. Together that is one more day of all three.")),
       ("Total", p("19."))) + final("19"))

P.qa(2, "Two identical jugs, each holding 1 litre when full, are numbered 1 and 2. Jug 1 holds x ml of pure acid and jug 2 holds x ml of pure water; neither is full. Acid from jug 1 is poured into jug 2 until jug 2 is full. Then the mixture from jug 2 is poured into jug 1 until jug 1 is full. Jug 1 now has acid and water in the ratio 17 : 8. What is x?", ["200 ml", "750 ml", "600 ml", "800 ml"], "MCQ", "4", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Work with u = x/1000.",
 steps(("First pour", p("1000 − x of acid moves; jug 1 keeps 2x − 1000. Jug 2’s acid fraction is (1000 − x)/1000.")),
       ("Second pour", p("Jug 1 receives 2000 − 2x of the mixture. With u = x/1000, water in jug 1 = 2u(1 − u) litres, out of 1 litre, so 2u(1 − u) = 8/25.")),
       ("Solve", p("25u² − 25u + 4 = 0, so u = 0.8 or 0.2. Jug 1 cannot hold less than half, so u = 0.8: x = 800 ml."))) + final("Option 4"),
 why_rows=[("1", "Gives u = 0.2, but then jug 1 runs dry."), ("2", "Not a root."), ("3", "Not a root.")])

P.qa(3, r"m is a real number such that f(x) = 2x² + mx + 7 is zero at \(x = -\tfrac{m}{4}\). Which follows?", ["f(x) = 0 has non-real roots.", "f(x) = 0 has two distinct real roots.", "The roots of f(x) = 0 are real and equal.", r"\(f(x) \le f\!\left(-\tfrac{m}{4}\right)\) for all real x."], "MCQ", "3", ["Algebra::Quadratic_Equations"], "Easy",
 r"\(-\tfrac{m}{4}\) is the vertex of the parabola.",
 steps(("Vertex", p(r"For 2x² + mx + 7 the vertex is at \(x = -\tfrac{m}{4}\).")),
       ("Root at the vertex", p("The parabola touches the axis there: equal roots."))) + final("Option 3"),
 why_rows=[("1", "It has a real root."), ("2", "The vertex is the only root."), ("4", "Opens upward: f(x) ≥ 0.")])

P.qa(4, r"What is the largest value of \(\dfrac{5 - x}{x^2 - 10x + 26}\) over all real x?", [r"\(\tfrac{1}{2}\)", "2", "−2", r"\(-\tfrac{1}{2}\)"], "MCQ", "1", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Put t = 5 − x.",
 steps(("Substitute", p(r"The expression is \(\dfrac{t}{t^2 + 1}\).")),
       ("AM–GM", p(r"\(t^2 + 1 \ge 2t\), so it is at most \(\tfrac12\), reached at t = 1 (x = 4)."))) + final("Option 1"),
 why_rows=[("2", "Inverts the bound."), ("3", "Below zero."), ("4", "That is the minimum.")])

P.qa(5, "A trader mixes two varieties of rice costing ₹50 and ₹60 per kg. The mixture costs a whole number of rupees per kg, and there is 5 kg more of the cheaper variety. What is the largest possible weight (in kg) of the mixture?", [], "TITA", "25", ["Arithmetic::Mixture_and_Alligation"], "Hard",
 "Cheaper : costlier = (60 − G) : (G − 50), G the mixture price.",
 steps(("G below 55", p("More cheap rice means G < 55: G is 51 to 54.")),
       ("Each G", p("54: 3 : 2, a 1-part gap = 5 kg, total 25. 53: 7 : 3, total 12.5. 52: 4 : 1, total 8⅓. 51: 9 : 1, total 6.25.")),
       ("Largest", p("25 kg."))) + final("25"))

P.qa(6, "In triangle ABC, AB = 8 cm, BC = 12 cm and CA = 16 cm. What is the length of the median BD?", [r"\(2\sqrt{10}\) cm", r"\(\sqrt{10}\) cm", r"\(4\sqrt{10}\) cm", r"\(2\sqrt{5}\) cm"], "MCQ", "1", ["Geometry::Triangles"], "Easy",
 "Apollonius: AB² + BC² = 2BD² + 2AD².",
 steps(("Apollonius", p("64 + 144 = 2BD² + 2 × 64, so BD² = 40.")),
       ("Length", p(r"\(BD = 2\sqrt{10}\)."))) + final("Option 1"),
 why_rows=[("2", "Halves it."), ("3", "Doubles it."), ("4", "√20.")])

P.qa(7, "All the distinct 4-digit numbers formed by rearranging the digits of 1236 are listed. How many of them are greater than their average?", ["7", "8", "9", "12"], "MCQ", "2", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "Each digit sits in each place equally often.",
 steps(("Average", p("Average digit is 3, so the average number is 3333.")),
       ("Count", p("Starting with 6: 6 numbers. Starting with 3: only 3612 and 3621 exceed 3333. Total 8."))) + final("Option 2"),
 why_rows=[("1", "Misses one."), ("3", "Off by one."), ("4", "Half of 24.")])

P.qa(8, "₹20,000 is split into A = ₹7000, B = ₹9000 and C = the rest. The three parts earn simple interest at 5.5%, 7% and 7.5% a year, one rate each. If the yearly interest is ₹1300, which matching is right?", ["A 5.5%, B 7%, C 7.5%", "A 7.5%, B 7%, C 5.5%", "A 7.5%, B 5.5%, C 7%", "A 5.5%, B 7.5%, C 7%"], "MCQ", "3", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Look at the last two digits.",
 steps(("Rule out", p("7% of 9000 = 630 cannot make a total ending in 00 with the others, so B is not at 7%.")),
       ("Check", p("525 + 495 + 280 = 1300."))) + final("Option 3"),
 why_rows=[("1", "1315."), ("2", "1365."), ("4", "1340.")])

P.qa(9, "Two sprinters start together from the same point on a circular track and run in opposite directions, one twice as fast as the other. Each time they meet, they instantly swap speeds and directions. At how many distinct points on the track do they meet if they run forever?", [], "TITA", "3", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Swapping speeds and directions is the same as passing through each other.",
 steps(("Meetings", p("Speeds 1 : 2, so in each meeting interval they cover the track together: the slower one 1/3 of it.")),
       ("Points", p("Meetings fall 1/3, 2/3 and 1 lap along: 3 points, the start included."))) + final("3"))

P.qa(10, "f(x) = |x| + |x − 1| for real x. How many integers x satisfy f(f(x)) = f(x)?", ["0", "1", "2", "More than 2"], "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "f(x) is at least 1 everywhere.",
 steps(("For y ≥ 1", p("f(y) = 2y − 1, which equals y only at y = 1.")),
       ("So", p("f(x) = 1, true for 0 ≤ x ≤ 1: the integers 0 and 1."))) + final("Option 3"),
 why_rows=[("1", "Two work."), ("2", "Both 0 and 1."), ("4", "Only 0 and 1.")])

P.qa(11, r"[r] is the greatest integer not more than r. A sequence has \(T_n = \left[\tfrac14 + \tfrac{n}{20}\right]\). If the sum of the first k terms is 50, what is k?", [], "TITA", "49", ["Algebra::Functions", "Algebra::Progressions_and_Series"], "Medium",
 r"\(T_n = \left[\tfrac{n + 5}{20}\right]\).",
 steps(("Blocks", p("n = 1–14: 0. n = 15–34: 1 (sum 20). n = 35–54: 2 each.")),
       ("Reach 50", p("30 more needs 15 terms of 2: k = 34 + 15 = 49."))) + final("49"))

P.qa(12, "Mr Bose stands on an escalator and rides half way up. He then sees his cat waiting at the bottom, walks down at three times the escalator’s speed (against it), picks the cat up instantly, and rides up without walking. The whole trip takes 63 seconds. How long would he have taken to reach the top without going back?", ["32", "36", "39", "42"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Let t be the time to ride half way.",
 steps(("Going down", p("Net speed 3e − e = 2e, twice the escalator: t/2.")),
       ("Total", p("t + t/2 + 2t = 3.5t = 63, so t = 18.")),
       ("Without going back", p("2t = 36 seconds."))) + final("Option 2"),
 why_rows=SLIP("1", "3", "4"))

P.qa(13, "Ten distinct natural numbers have average 31. What is the largest possible average of the two largest of them?", ["35.5", "73.5", "117", "137"], "MCQ", "4", ["Arithmetic::Average"], "Medium",
 "Make the other eight as small as possible.",
 steps(("Sum", p("310 in all. The smallest eight: 1 to 8, sum 36.")),
       ("Top two", p("274, average 137."))) + final("Option 4"),
 why_rows=SLIP("1", "2", "3"))

P.qa(14, "The equation x² − 2(k − 2)x + 64 = 0 has equal roots, and k is positive. What is k?", ["−6", "6", "10", "−10"], "MCQ", "3", ["Algebra::Quadratic_Equations"], "Easy",
 "Discriminant zero.",
 steps(("Discriminant", p("4(k − 2)² − 256 = 0, so k − 2 = ±8.")),
       ("Positive", p("k = 10 or −6; k = 10."))) + final("Option 3"),
 why_rows=[("1", "Not positive."), ("2", "Sign slip."), ("4", "Not a root.")])

P.qa(15, "ax² + bx + c = 0 has real, distinct roots, and the product of the roots is 4 times their sum. Which pair of values of b and a is not possible?", ["b = 64, a = −3", "b = 64, a = −4", "b = −64, a = 3", "b = −64, a = −4"], "MCQ", "2", ["Algebra::Quadratic_Equations"], "Hard",
 "c/a = 4(−b/a) gives c = −4b.",
 steps(("Discriminant", p("b² − 4ac = b² + 16ab = b(b + 16a) must be positive.")),
       ("Check", p("b = 64, a = −4: 64 × 0 = 0, equal roots. The others give positive values."))) + final("Option 2"),
 why_rows=[("1", "64 × 16 > 0."), ("3", "(−64)(−16) > 0."), ("4", "(−64)(−128) > 0.")])

P.qa(16, "50 equally efficient people finish a job in 13 days working 8 hours a day. N such people finish 90% of the job in 12 days working 10 hours a day. What is N?", ["39", "40", "42", "45"], "MCQ", "1", ["Arithmetic::Time_and_Work"], "Medium",
 "Person-hours.",
 steps(("Job", p("50 × 13 × 8 = 5200 person-hours; 90% is 4680.")),
       ("N", p("4680 ÷ 120 = 39."))) + final("Option 1"),
 why_rows=SLIP("2", "3", "4"))

P.qa(17, "How many 3-digit terms of the AP 2, 5, 8, … are multiples of 10?", ["33", "31", "30", "29"], "MCQ", "3", ["Algebra::Progressions_and_Series"], "Hard",
 "Terms leave remainder 2 on division by 3.",
 steps(("Form", p("10k with 10k ≡ 2 (mod 3), so k ≡ 2 (mod 3), with 10 ≤ k ≤ 99.")),
       ("Count", p("k = 11, 14, …, 98: 30 values."))) + final("Option 3"),
 why_rows=SLIP("1", "2", "4"))

P.qa(18, "A trader has between 4000 and 4500 mangoes. Packing 10, 12 or 14 to a box leaves 3 over each time; packing 9 to a box leaves none. How many boxes does he need at 11 to a box? (The last box may hold fewer.)", ["380", "381", "382", "383"], "MCQ", "4", ["Number_System::Factors_and_Divisibility"], "Easy",
 "LCM(10, 12, 14) = 420.",
 steps(("Mangoes", p("420m + 3 in range: 4203 (m = 10), and 4 + 2 + 0 + 3 = 9, so it divides by 9.")),
       ("Boxes", p("4203 = 11 × 382 + 1: 383 boxes."))) + final("Option 4"),
 why_rows=[("1", "Too few."), ("2", "Too few."), ("3", "Leaves 1 mango out.")])

P.qa(19, "ABCD is a rectangle 56 cm long and 28 cm wide. Two equal circles, as large as possible, with centres C₁ and C₂, are drawn inside it without overlapping. A third circle, centre O, as large as possible, is drawn in the gap between them and side AB without overlapping them, as shown. Find its area in cm² (take π = 22/7)." + F.CIRC, ["77", "38.5", "84", "42"], "MCQ", "2", ["Geometry::Circles"], "Medium",
 "Big radius 14. Right triangle from O to C₂.",
 steps(("Big circles", p("Radius 56 ÷ 4 = 14.")),
       ("Small circle", p("O is above the touching point, 14 cm across from C₂. With radius r, OC₂ = 14 + r and the vertical gap is 14 − r.")),
       ("Pythagoras", p("(14 + r)² = (14 − r)² + 14², so 56r = 196 and r = 3.5.")),
       ("Area", p("22/7 × 12.25 = 38.5."))) + final("Option 2"),
 why_rows=[("1", "Doubles it."), ("3", "Wrong radius."), ("4", "Wrong radius.")])

P.qa(20, "Manisha has 128 notes of 7, 17 and 25 Sols, worth 2000 Sols in all. What is the largest possible number of 25-Sol notes?", [], "TITA", "58", ["Algebra::Linear_Equations"], "Hard",
 "Eliminate the 17-Sol notes.",
 steps(("Equations", p("x + y + z = 128 and 7x + 17y + 25z = 2000 give 10x − 8z = 176, so x = (176 + 8z)/10.")),
       ("Steps", p("z = 3, x = 20 works; z rises by 5 when x rises by 4.")),
       ("Largest", p("y = 128 − x − z ≥ 0. z = 58, x = 64, y = 6 works; z = 63 would need y < 0."))) + final("58"))

P.qa(21, "θ is an acute angle with sec θ + tan θ = 3. What is the value of 90 sin θ?", [], "TITA", "72", ["Geometry::Trigonometry"], "Medium",
 "sec²θ − tan²θ = 1.",
 steps(("Second equation", p("sec θ − tan θ = 1/3.")),
       ("Solve", p("sec θ = 5/3, tan θ = 4/3, so sin θ = tan θ ÷ sec θ = 4/5.")),
       ("Answer", p("90 × 4/5 = 72."))) + final("72"))

P.qa(22, "ABCDE is a convex pentagon whose longest side is AE. AB = 2.5 cm, BC = 3.5 cm, CD = 4 cm and DE = 5.5 cm. If AE is a whole number of cm, what is its largest possible value?", [], "TITA", "15", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "Any side is shorter than the sum of the others.",
 steps(("Bound", p("AE < 2.5 + 3.5 + 4 + 5.5 = 15.5.")),
       ("Largest", p("15 cm."))) + final("15"))
