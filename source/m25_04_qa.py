# -*- coding: utf-8 -*-
# Simp Mock 4 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_04 import P

P.qa(1, r"Let \(f(n, k)\) be defined for all non-negative integers \(n\) and \(k\) as \(\dfrac{n!}{(k!)!}\). What is the largest possible value of \(n\) such that \(f(n, 6)\) is not an integer?", ["121", "359", "719", "720"], "MCQ", "3", ["Number_System::Factorials"], "Easy",
 "\\((6!)! = 720!\\).",
 steps(("When it divides", p(r"\(720!\) divides \(n!\) exactly when \(n \ge 720\). The largest \(n\) that fails is 719."))) + final("719, option 3"),
 why_rows=[("1", "Not the largest."), ("2", "Not the largest."), ("4", r"\(720!/720! = 1\), an integer.")])

P.qa(2, r"Find the value of \(\dfrac1{x^2} + \dfrac1{y^2}\) given that \(x = A + \sqrt{(A+1)(A-1)}\) and \(x = y^{-1}\).", [r"\(4A^2 - 1\)", r"\(4A^2 - 2\)", r"\(2A^2 - 1\)", r"\(2(A^2 - 1)\)"], "MCQ", "2", ["Algebra::Surds_and_Indices"], "Medium",
 "\\(\\tfrac1x = A - \\sqrt{A^2 - 1}\\): rationalise.",
 steps(("y", p(r"\(y = \tfrac1x = A - \sqrt{A^2 - 1}\), so \(\tfrac1{x^2} + \tfrac1{y^2} = y^2 + x^2\).")),
       ("Sum of squares", p(r"\(x + y = 2A\), \(xy = 1\): \(x^2 + y^2 = 4A^2 - 2\)."))) + final("Option 2"),
 why_rows=[("1", "Uses 2xy = 1."), ("3", "Halves the square."), ("4", "Halves the square.")])

P.qa(3, "Two people started walking simultaneously from the same point towards south and east respectively with their individual constant speeds. The shortest distance between them after the first 15 minutes was 2190 metres. They did not stop anywhere in the first 15 minutes. Find the sum of the distances covered (in metres) by both in these 15 minutes, if the speed of the eastbound walker was \\(\\tfrac{7}{48}\\) times more than the speed of the southbound walker.",
 ["2200", "2980", "3090", "3300"], "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "\\(\\tfrac7{48}\\) times more means \\(\\tfrac{55}{48}\\) of the other’s speed. 48-55-73 is a Pythagorean triple.",
 steps(("Distances", p(r"South \(48k\), east \(55k\), straight-line gap \(73k = 2190\), so \(k = 30\).")), ("Sum", p("(48 + 55) × 30 = 3090 m."))) + trap("‘7/48 times more’ adds to the original: 1 + 7/48 = 55/48.") + final("3090, option 3"),
 why_rows=[("1", "Uses the wrong ratio."), ("2", "Uses the wrong ratio."), ("4", "Uses the wrong ratio.")])

P.qa(4, "A mixture has only three ingredients, namely, milk, water and honey in the ratio (by weight) 7 : 8 : 9. If we add ‘m’ grams of milk and ‘h’ grams of honey to the mixture, the ratio (by weight) of milk, water and honey becomes 11 : 10 : 13. If the value of (m + h) is 48 gm, find the original weight (in gm) of the mixture.", ["320", "360", "400", "420"], "MCQ", "2", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "Water doesn’t change: 8 parts before equal 10 parts after.",
 steps(("Same scale", p(r"Before: \(7k, 8k, 9k\). After, with water \(8k\): milk \(8.8k\), honey \(10.4k\).")),
       ("Added", p(r"\(m + h = 1.8k + 1.4k = 3.2k = 48\), so \(k = 15\). Original: \(24k = 360\) g."))) + final("360, option 2"),
 why_rows=[("1", "Wrong k."), ("3", "Wrong k."), ("4", "Wrong k.")])

P.qa(5, "The average height of a group of people increases by 0.375 inches when a few more people join them. If the average height of the new people is 3 inches more than that of the original group, then the ratio of the number of people present originally to those who joined later is ____.", ["7 : 1", "11 : 5", "5 : 1", "13 : 2"], "MCQ", "1", ["Arithmetic::Average"], "Easy",
 "The newcomers’ extra height is shared by everyone.",
 steps(("Balance", p(r"\(m\) newcomers each 3 inches above the old average: \(3m = 0.375(n + m)\), so \(2.625m = 0.375n\), \(n : m = 7 : 1\)."))) + final("7 : 1, option 1"),
 why_rows=[("2", "Not from the equation."), ("3", "Ignores the newcomers in the new average."), ("4", "Not from the equation.")])

P.qa(6, "How many times do the three hands (i.e. the hour, minute, and seconds) of a normal functional watch coincide in a duration of 24 hours?", ["1", "2", "22", "23"], "MCQ", "2", ["Arithmetic::Miscellaneous"], "Medium",
 "Hour and minute hands meet 22 times a day; at how many of those is the second hand there too?",
 steps(("Hour and minute", p(r"They meet every \(\tfrac{720}{11}\) minutes, i.e. at \(65\tfrac5{11}\)-minute intervals.")),
       ("Second hand", p(r"At those meetings the time has a fraction of \(\tfrac{1}{11}\) of a minute in it, so the second hand points elsewhere, except at 12:00. Twice a day."))) + final("2, option 2"),
 why_rows=[("1", "12:00 happens twice in 24 hours."), ("3", "Hour and minute hands only."), ("4", "Not a meeting count.")])

P.qa(7, "A shopkeeper buys the following dried fruits: 7 kg of apricots, 13 kg of blackberries and 8 kg of cherries. The cost prices are such that the price of 9 kg of apricots is the same as that of 24 kg of blackberries or that of 16 kg of cherries. She mixes the fruits thoroughly and sets a price P per kg for the mixture so that she would make a profit of Rs 90. However, during the festive season she is able to sell 21 kg at 20% above P (and the rest at P) and consequently makes a profit of Rs. 300. How much did she spend (in Rs.) on buying blackberries?", [], "TITA", "390", ["Arithmetic::Profit_and_Loss"], "Hard",
 "The extra ₹210 profit comes from selling 21 kg at 20% more.",
 steps(("Find P", p(r"\(21 \times 0.2P = 210\), so \(P = 50\). Revenue at P: 28 × 50 = 1400, cost 1310.")),
       ("Prices", p(r"Per kg, apricots : blackberries : cherries \(= 48 : 18 : 27\) (from \(9a = 24b = 16c\)). Cost \(= 7(48) + 13(18) + 8(27) = 786\) units = ₹1310, so 1 unit = ₹\(\tfrac53\).")),
       ("Blackberries", p(r"\(13 \times 18 \times \tfrac53 = 390\)."))) + final("390"))

P.qa(8, "If a person invests Rs. 10000 in a bank with r% interest per annum in a simple interest scheme (s)he will get the amount Rs. 36000 after 10 years. Another person invests Rs. 50000 in the same bank in a compound interest scheme with r% rate of interest per annum compounding annually, wherein the duration has to be a whole number of years. What is the minimum investment period (in years) needed to earn at least Rs. 50000 as interest?", [], "TITA", "3", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "Find r first, then double the money.",
 steps(("Rate", p("₹26,000 interest over 10 years on ₹10,000: 26% a year.")), ("Doubling", p(r"\(1.26^2 = 1.5876\), \(1.26^3 = 2.000376 \ge 2\). Three years."))) + final("3"))

P.qa(9, "Working alone, A and B can finish a job in 42 minutes and 48 minutes respectively. If A and B take the help of a helper C and they finish the entire job working together, they earn Rs. 480 in total out of which C receives his share of Rs. 30. The time (in minutes) in which the job is finished by all three of them together is ________ .", ["18", "21", "24", "28"], "MCQ", "2", ["Arithmetic::Time_and_Work"], "Medium",
 "C’s share is \\(\\tfrac{30}{480} = \\tfrac1{16}\\) of the work.",
 steps(("A and B do the rest", p(r"\(\tfrac{15}{16}\) of the job at \(\tfrac1{42} + \tfrac1{48} = \tfrac{15}{336}\) per minute.")), ("Time", p(r"\(\tfrac{15}{16} \div \tfrac{15}{336} = 21\) minutes."))) + final("21, option 2"),
 why_rows=[("1", "Too short."), ("3", "Too long."), ("4", "Too long.")])

P.qa(10, "A tank is connected with (2 + n) inlet pipes and 2 outlet pipes (n is a natural number). If only the inlet pipes are operational the empty tank becomes full in ‘6n’ minutes. If only the outlet pipes are operational the full tank becomes empty in ‘54n’ minutes. Find the time (in seconds) required to fill the empty tank when all the pipes are operational, given that the ratio of the capacities of each outlet pipe to that of each inlet pipe is 1 : 6.", [], "TITA", "405", ["Arithmetic::Time_and_Work"], "Hard",
 "Let each inlet do \\(i\\) per minute; each outlet does \\(\\tfrac i6\\).",
 steps(("Two equations", p(r"\((n + 2)i = \tfrac1{6n}\) and \(2 \times \tfrac i6 = \tfrac1{54n}\), so \(i = \tfrac1{18n}\). Then \(\tfrac{n+2}{18n} = \tfrac1{6n}\): \(n = 1\).")),
       ("All pipes", p(r"Inlets \(3 \times \tfrac1{18} = \tfrac16\), outlets \(\tfrac1{54}\). Net \(\tfrac{8}{54}\): 6.75 minutes = 405 seconds."))) + final("405"))

P.qa(11, r"Let \(a, b, c\) be non-zero real numbers such that \(b^2 < 4ac\), and \(f(x) = ax^2 + bx + c\). If the set \(S\) consists of all integers \(m\) such that \(m \times f(m) > 0\), then the set \(S\) must necessarily be ____.", ["the set of all positive integers", "the set of all negative integers", "the set of all positive integers and the set of all negative integers", "either the set of all positive integers or the set of all negative integers, but not both"], "MCQ", "4", ["Algebra::Quadratic_Equations"], "Medium",
 "With a negative discriminant, \\(f\\) never changes sign.",
 steps(("Sign of f", p(r"\(f(m)\) always has the sign of \(a\) (and of \(c\)). \(m f(m) > 0\) needs \(m\) with that same sign, and \(m = 0\) never works.")), ("So", p("All positive integers if \\(a > 0\\), all negative integers if \\(a < 0\\)."))) + final("Option 4"),
 why_rows=[("1", "Only when a > 0."), ("2", "Only when a < 0."), ("3", "Never both.")])

P.qa(12, r"If \(a, b\) and \(c\) are the roots of the equation \(x^3 - 6x^2 + 18x - 11 = 0\) then the value of \(\dfrac{a^2}{b^2 + c^2} + \dfrac{b^2}{c^2 + a^2} + \dfrac{c^2}{a^2 + b^2}\) is", ["6", "−4", "3", "−3"], "MCQ", "4", ["Algebra::Equations_and_Polynomials"], "Hard",
 "Find \\(a^2 + b^2 + c^2\\).",
 steps(("Sum of squares", p(r"\(a^2 + b^2 + c^2 = 6^2 - 2 \times 18 = 0\). So \(b^2 + c^2 = -a^2\), and so on.")), ("Each term", p(r"Each fraction is \(-1\): total \(-3\). (Two roots are complex, which is why the squares can sum to 0.)"))) + final("−3, option 4"),
 why_rows=[("1", "Not from these sums."), ("2", "Not from these sums."), ("3", "Sign error.")])

P.qa(13, r"The maximum possible value of \(\displaystyle\sum_{n=1}^{100} \frac{n x^n}{1 + x^{2n}}\) for real \(x\) is ____.", ["2500", "2525", "4545", "5000"], "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "\\(\\tfrac{t}{1 + t^2} \\le \\tfrac12\\).",
 steps(("Each term", p(r"With \(t = x^n\), \(\tfrac{t}{1 + t^2} \le \tfrac12\), equality at \(t = 1\). All terms are at their best together when \(x = 1\).")), ("Sum", p(r"\(\tfrac12(1 + 2 + \dots + 100) = 2525\)."))) + final("2525, option 2"),
 why_rows=[("1", "Not half of 5050."), ("3", "Not half of 5050."), ("4", "Forgets the ½.")])

P.qa(14, r"If the polynomial \(x^6 + 2x^5 - 3x^4 + kx^3 - 5x^2 + 6x - 7\) is divided by \((x - 2)\), we get the remainder 97. The value of \(k\) is ____.", [], "TITA", "4", ["Algebra::Equations_and_Polynomials"], "Easy",
 "Remainder theorem: put \\(x = 2\\).",
 steps(("Evaluate", p(r"\(64 + 64 - 48 + 8k - 20 + 12 - 7\) \(= 65 + 8k = 97\), so \(k = 4\)."))) + final("4"))

P.qa(15, r"In the expansion of \((x + y)^n\), the coefficient of the third term is the arithmetic mean of the coefficients of the second and the fourth terms. Find the total number of terms present in the expansion.", [], "TITA", "8", ["Algebra::Progressions_and_Series"], "Medium",
 "\\(2\\binom n2 = \\binom n1 + \\binom n3\\).",
 steps(("Equation", p(r"\(n(n-1) = n + \tfrac{n(n-1)(n-2)}{6}\). Divide by \(n\): \(6n - 12 = n^2 - 3n + 2\), \(n^2 - 9n + 14 = 0\), \(n = 7\) (n = 2 has no fourth term).")), ("Terms", p("n + 1 = 8."))) + final("8"))

P.qa(16, "Let ABCD be a parallelogram such that the coordinates of its three vertices A, B, C are (1, 2), (3, −4) and (−5, 6), respectively. Then, the coordinates of the vertex D are ________ .", ["(−7, 12)", "(3, 4)", "(−3, 12)", "(−7, 4)"], "MCQ", "1", ["Geometry::Coordinate_Geometry"], "Easy",
 "Diagonals bisect each other: A + C = B + D.",
 steps(("D", p("D = A + C − B = (1 − 5 − 3, 2 + 6 + 4) = (−7, 12)."))) + final("Option 1"),
 why_rows=[("2", "Uses B + C − A."), ("3", "Sign slip."), ("4", "Sign slip.")])

P.qa(17, "In ΔBDC, BD = 18 and BC = 24. A is a point on side BD extended such that B-D-A, and CD = 12. If ∠BCD = ∠BAC, the area of ΔACD in square units is ____.", ["Less than 75", "Between 75 and 85", "More than 85", "More information is needed to answer this question"], "MCQ", "2", ["Geometry::Triangles"], "Hard",
 "Triangles BCD and BAC share angle B and have one more equal angle.",
 steps(("Similar triangles", p(r"\(\tfrac{BC}{BA} = \tfrac{BD}{BC}\): \(BA = \tfrac{24^2}{18} = 32\), so \(DA = 14\). Also \(\tfrac{CD}{AC} = \tfrac{BC}{BA}\): \(AC = 16\).")),
       ("Heron", p(r"Sides 12, 14, 16, \(s = 21\): area \(= \sqrt{21 \times 9 \times 7 \times 5} = \sqrt{6615} \approx 81.3\)."))) + final("Option 2"),
 why_rows=[("1", "81.3 is more."), ("3", "81.3 is less."), ("4", "Similarity gives every side.")])

P.qa(18, "S1 is a square inscribed in circle C1. A circle C2 is inscribed in S1. H1 is a regular hexagon with side equal to the radius of C2. C3 is a circle inscribed in H1. Find the ratio of the radius of C1 to the radius of C3.", [r"\(\sqrt6 : 4\)", r"\(2\sqrt6 : 3\)", r"\(2 : \sqrt3\)", "None of these"], "MCQ", "2", ["Geometry::Mensuration"], "Medium",
 "Follow one length through each shape.",
 steps(("Chain", p(r"C1 radius \(R\). Square side \(R\sqrt2\). C2 radius \(\tfrac{R\sqrt2}{2}\) = hexagon side. Hexagon inradius \(= \tfrac{\sqrt3}{2} \times \tfrac{R\sqrt2}{2} = \tfrac{R\sqrt6}{4}\).")),
       ("Ratio", p(r"\(R : \tfrac{R\sqrt6}{4} = 4 : \sqrt6 = 2\sqrt6 : 3\)."))) + final("Option 2"),
 why_rows=[("1", "Upside down."), ("3", "Skips the square."), ("4", "Option 2 is right.")])

P.qa(19, "The thickness of a 36 cm long hollow pipe is 1 cm. The ratio of the cost of painting the inner curved surface area to the cost of painting its outer curved surface area is 13 : 14. If this pipe is melted to form a solid sphere, what will be the surface area (in sq. cm) of the sphere?", ["296π", "312π", "324π", "332π"], "MCQ", "3", ["Geometry::Mensuration"], "Medium",
 "Curved areas are in the ratio of the radii.",
 steps(("Radii", p("Inner 13, outer 14.")), ("Volume", p(r"\(\pi(14^2 - 13^2) \times 36 = 972\pi = \tfrac43\pi r^3\), so \(r^3 = 729\), \(r = 9\).")), ("Surface", p(r"\(4\pi \times 81 = 324\pi\)."))) + final("324π, option 3"),
 why_rows=[("1", "Wrong radius."), ("2", "Wrong radius."), ("4", "Wrong radius.")])

P.qa(20, "In trapezium ABCD, AB ∥ CD and ∠ADC + ∠BCD = 238°. Line segment AB is extended in both directions so that P-A-B-Q. Suppose that AR is the angle bisector of ∠DAP and BS is that of ∠CBQ, and that RA and SB, extended, intersect at point O. Find the value (in degrees) of ∠AOB.", [], "TITA", "61", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "Co-interior angles: ∠DAB + ∠CBA = 360° − 238°.",
 steps(("Angles at A and B", p(r"\(\angle DAB + \angle CBA = 122^\circ\). The exterior angles \(\angle DAP\) and \(\angle CBQ\) add to \(360^\circ - 122^\circ = 238^\circ\); their halves add to 119°.")),
       ("Triangle AOB", p(r"Ray AO is RA extended past A, so \(\angle OAB = \angle RAP = \tfrac12\angle DAP\) (vertically opposite). Likewise \(\angle OBA = \tfrac12\angle CBQ\). These add to 119°, so \(\angle AOB = 61^\circ\)."))) + final("61"))

P.qa(21, "A machine has 6 bolts, each of which must be fitted with a corresponding nut to stay secure. Bolts and nuts can be installed in any sequence, with the condition that a nut can only be fitted after its corresponding bolt is fixed in place. Given that all bolts and nuts are distinct, in how many ways can the 6 bolts and their corresponding 6 nuts be fitted?", [r"\(\tfrac{12!}{2}\)", r"\(\tfrac{12!}{2^6}\)", r"\((6!)^2\)", r"\(2^6 \times 6!\)"], "MCQ", "2", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "Order all 12 items freely, then keep only orders where each bolt comes before its nut.",
 steps(("Count", p(r"12! orders in all. For each bolt–nut pair, exactly half have the bolt first, independently: \(\tfrac{12!}{2^6}\)."))) + final("Option 2"),
 why_rows=[("1", "Applies the condition to one pair only."), ("3", "Treats bolts and nuts as two separate blocks."), ("4", "Not the count.")])

P.qa(22, "For any natural number n, suppose the sum of the first n terms of a sequence is (n² + 3n + 2). If the n<sup>th</sup> term of the sequence is divisible by 7, then the smallest possible value of n is ____.", ["4", "5", "6", "7"], "MCQ", "3", ["Algebra::Progressions_and_Series"], "Easy",
 "\\(a_n = S_n - S_{n-1}\\) for \\(n \\ge 2\\).",
 steps(("Terms", p(r"\(a_1 = 6\); for \(n \ge 2\), \(a_n = 2n + 2\).")), ("Divisible by 7", p(r"\(2n + 2 = 14\) gives \(n = 6\)."))) + final("6, option 3"),
 why_rows=[("1", "a₄ = 10."), ("2", "a₅ = 12."), ("4", "a₇ = 16.")])
