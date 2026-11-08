# -*- coding: utf-8 -*-
# Simp Mock 3 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_03 import P

P.qa(1, "A tank is connected with two inlet pipes - pipe A and pipe B. The two pipes together take ‘t’ minutes to fill the tank. Pipe A can alone fill the tank in (t + 120) minutes and pipe B can alone fill the tank in (t + 30) minutes. Find the total time (in minutes) required to fill the tank when the two pipes are operated alternately every minute.",
 ["120", "90", "80", "Cannot be determined"], "MCQ", "1", ["Arithmetic::Time_and_Work"], "Medium",
 "Together in \\(t\\), alone in \\(t + x\\) and \\(t + y\\): then \\(t^2 = xy\\).",
 steps(("Find t", p(r"\(\tfrac1{t+120} + \tfrac1{t+30} = \tfrac1t\) simplifies to \(t^2 = 120 \times 30\), so \(t = 60\). A takes 180 minutes, B 90.")),
       ("Alternating", p(r"Every 2 minutes: \(\tfrac1{180} + \tfrac1{90} = \tfrac1{60}\). After 119 minutes the tank is \(\tfrac{59}{60} + \tfrac1{180}\) full, short of 1; the 120th minute (pipe B) finishes it exactly."))) + final("120, option 1"),
 concept=r"\[\text{If together take } t, \text{ alone } t + x \text{ and } t + y:\ t = \sqrt{xy}\]",
 why_rows=[("2", "B’s time alone."), ("3", "Not a multiple of the cycle that fills it."), ("4", "t is fixed by the data.")])

P.qa(2, "The ratio of water to milk in a solution made of only milk and water was 5 : 2. After adding ‘V’ litres of pure milk to this solution, the ratio of water to milk changed to 5 : 3. Now, 20% volume of this solution is removed and 40 litres of pure water is added to the remaining solution. After this operation the final ratio of water to milk becomes 5 : 2. Find the value of ‘V’.",
 ["20", "30", "40", "50"], "MCQ", "1", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Water \\(5k\\), milk \\(2k\\). Adding milk only changes milk.",
 steps(("After the milk", p(r"\(\tfrac{5k}{2k + V} = \tfrac53\), so \(V = k\): water \(5k\), milk \(3k\).")),
       ("Remove 20%, add water", p(r"Water \(4k + 40\), milk \(2.4k\). \(\tfrac{4k + 40}{2.4k} = \tfrac52\) gives \(4k + 40 = 6k\), \(k = 20\). So \(V = 20\)."))) + final("20, option 1"),
 why_rows=[("2", "Doesn’t give 5 : 3."), ("3", "Doesn’t give 5 : 3."), ("4", "Doesn’t give 5 : 3.")])

P.qa(3, "A man invested a certain sum of money at simple interest for three years and earned a total interest of Rs. 2400. However, if he had invested the same sum at the same rate under compound interest for three years compounding annually, he would have earned a total interest of Rs. 2648. Determine the annual rate of interest (in percent).",
 ["8", "10", "12", "Cannot be determined"], "MCQ", "2", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "Simple interest is ₹800 a year. CI − SI over three years \\(= P(3r^2 + r^3)\\).",
 steps(("Set up", p(r"\(Pr = 800\). \(P(3r^2 + r^3) = 248\), i.e. \(800(3r + r^2) = 248\).")), ("Solve", p(r"\(r^2 + 3r - 0.31 = 0\): \(r = 0.1\), i.e. 10%."))) + final("10%, option 2"),
 concept=r"\[\text{CI} - \text{SI (3 years)} = P(3r^2 + r^3)\]",
 why_rows=[("1", "Gives CI − SI below 248."), ("3", "Gives CI − SI above 248."), ("4", "The two interests fix r.")])

P.qa(4, "Four friends Abhay, Bobby, Chinni, and Dhruv had agreed to share their playing marbles. Dhruv had 12.5% more marbles than Chinni, Chinni had 40% more marbles than Bobby, and Bobby had 20% more marbles than Abhay. If the four friends had an even number of marbles in total, then the minimum possible value of the total number of marbles is ________ .",
 ["1178", "1166", "1154", "1142"], "MCQ", "3", ["Arithmetic::Percentages"], "Medium",
 "Write everyone in terms of Abhay’s count \\(a\\).",
 steps(("In terms of a", p(r"Bobby \(\tfrac65a\), Chinni \(\tfrac{42}{25}a\), Dhruv \(\tfrac{189}{100}a\). All whole numbers needs \(a\) a multiple of 100.")),
       ("Total", p(r"\(a = 100k\): \(100 + 120 + 168 + 189 = 577\) per 100. 577 is odd, so \(k = 2\): 1154."))) + final("1154, option 3"),
 why_rows=[("1", "Not a multiple of 577."), ("2", "Not a multiple of 577."), ("4", "Not a multiple of 577.")])

P.qa(5, "A can alone complete a work in 36 days. A starts the work and works alone for 6 days. Then B works alone for the next 10 days. After that C works alone for the next 8 days. The remaining work is completed by A and B together in the next 6 days. On which day the work will be completed if all three work together, given that C is 300% faster than B?",
 ["9<sup>th</sup> day", "10<sup>th</sup> day", "11<sup>th</sup> day", "12<sup>th</sup> day"], "MCQ", "3", ["Arithmetic::Time_and_Work"], "Medium",
 "300% faster means 4 times as fast.",
 steps(("Rates", p(r"A does \(\tfrac1{36}\) a day. Let B do \(b\); C does \(4b\).")),
       ("The whole job", p(r"\(\tfrac{6}{36} + 10b + 32b + \tfrac{6}{36} + 6b = 1\), so \(48b = \tfrac23\), \(b = \tfrac1{72}\), C \(= \tfrac1{18}\).")),
       ("Together", p(r"\(\tfrac1{36} + \tfrac1{72} + \tfrac1{18} = \tfrac{7}{72}\) a day: \(\tfrac{72}{7} \approx 10.3\) days, so it finishes on the 11th day."))) + trap("‘300% faster’ is 4 times the speed, not 3 times.") + final("Option 3"),
 why_rows=[("1", "Too early."), ("2", "After 10 days the work is not yet complete."), ("4", "Too late.")])

P.qa(6, "Exactly four candidates contested in an election. Exactly a fifth of the registered voters did not cast their votes. All the votes cast were valid. One of the candidates received 30% of the total registered voters while the other three candidates received the remaining valid votes actually cast in the proportion 5 : 4 : 3. If the winner of the election beat the runner-up by a margin of 2222 votes, then the number of registered voters was ________.",
 ["22220", "23230", "32320", "24240"], "MCQ", "4", ["Arithmetic::Percentages"], "Medium",
 "Votes cast = 80%. The other three share 50% in 5 : 4 : 3.",
 steps(("Shares", p(r"30% to one; the others get \(\tfrac5{12}, \tfrac4{12}, \tfrac3{12}\) of 50%: about 20.8%, 16.7% and 12.5%. The winner has 30%, the runner-up \(\tfrac{25}{120}\).")),
       ("Margin", p(r"\(\tfrac{36 - 25}{120}N = 2222\), so \(N = 24240\)."))) + final("24240, option 4"),
 why_rows=[("1", "Margin would be 2036.8."), ("2", "Not divisible as needed."), ("3", "Margin would be 2962.7.")])

P.qa(7, "A person can cover a distance of 900 km by car at a speed of 45 kmph and the same distance by train at a speed of 60 kmph. If part of the total distance is covered by train and the rest by car, the total time taken for the entire journey is 18 hours. What is the ratio of the time spent traveling by car to the time spent traveling by train?",
 ["1 : 3", "2 : 1", "2 : 3", "3 : 4"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Let the car time be \\(c\\) hours.",
 steps(("Equation", p(r"\(45c + 60(18 - c) = 900\): \(1080 - 15c = 900\), \(c = 12\). Train 6 hours.")), ("Ratio", p("12 : 6 = 2 : 1."))) + final("2 : 1, option 2"),
 why_rows=[("1", "Not 12 : 6."), ("3", "Not 12 : 6."), ("4", "Not 12 : 6.")])

P.qa(8, "A dairy farm sells milk to milkmen who sell it to individual customers. Each milkman purchases 30 litres of milk at a fixed price per litre and the farm gives an additional volume of ‘x’ litres of milk free of cost. A milkman sells milk at 12.5% markup over the fixed price per litre he paid the farm (the markup has been calculated without including the free milk he received). After selling the entire milk, the milkman earns a net profit of 20%. Find the value of ‘x’.",
 [], "TITA", "2", ["Arithmetic::Profit_and_Loss"], "Easy",
 "Cost 30 units; he sells \\(30 + x\\) litres at 1.125.",
 steps(("Equation", p(r"\(1.125(30 + x) = 1.2 \times 30 = 36\), so \(30 + x = 32\), \(x = 2\)."))) + final("2"))

P.qa(9, r"If \(\alpha\) and \(-\alpha\) are real roots of \(2x^3 + kx^2 - 36x + 126 = 0\), then \(k\) equals ____.", [r"\(\tfrac72\)", r"\(-\tfrac72\)", "−7", "7"], "MCQ", "3", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Call the third root \\(\\beta\\). Use the sum of pairwise products first.",
 steps(("Pairwise products", p(r"\(\alpha(-\alpha) + \alpha\beta - \alpha\beta = -\alpha^2 = \tfrac{-36}{2}\), so \(\alpha^2 = 18\).")),
       ("Product", p(r"\(\alpha(-\alpha)\beta = -\tfrac{126}{2}\): \(18\beta = 63\), \(\beta = 3.5\).")),
       ("Sum", p(r"\(\alpha - \alpha + \beta = -\tfrac k2\): \(k = -7\)."))) + final("−7, option 3"),
 concept=r"\[ax^3 + bx^2 + cx + d:\ \sum r = -\tfrac ba,\ \sum r_ir_j = \tfrac ca,\ \prod r = -\tfrac da\]",
 why_rows=[("1", "That is β, with the wrong sign handling."), ("2", "That is −β."), ("4", "Sign slip.")])

P.qa(10, r"For how many natural values of \(n\) does the inequality \(|n - 20| \le |n - 80| \le |n - 10|\) hold?", ["4", "6", "8", "10"], "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "\\(|n - a| \\le |n - b|\\) means \\(n\\) is at least as close to \\(a\\) as to \\(b\\).",
 steps(("First part", p(r"Closer to 20 than to 80: \(n \le 50\).")), ("Second part", p(r"Closer to 80 than to 10: \(n \ge 45\).")), ("Count", p("45 to 50: 6 values."))) + final("6, option 2"),
 why_rows=[("1", "Endpoints dropped."), ("3", "Endpoints mis-set."), ("4", "Endpoints mis-set.")])

P.qa(11, r"ABC25 is a five-digit perfect square natural number (A, B and C are digits). What is the sum of all the pairs of real roots for all the possible quadratic equations of the form \(x^2 + x - \text{ABC} = 0\)?", ["−21", "−22", "−17", "21"], "MCQ", "2", ["Number_System::Miscellaneous"], "Medium",
 "A square ending in 25 is \\((10m + 5)^2 = 100m(m + 1) + 25\\).",
 steps(("ABC", p(r"ABC \(= m(m + 1)\), and it has three digits: \(m = 10\) to \(31\), 22 values.")),
       ("Each equation", p(r"\(x^2 + x - m(m+1)\) \(= (x - m)(x + m + 1)\): roots add to −1. 22 equations: −22."))) + final("−22, option 2"),
 why_rows=[("1", "Misses one value of m."), ("3", "Misses values."), ("4", "Sign wrong.")])

P.qa(12, r"The minimum possible value of \(\dfrac{x^2 + 8x + 17}{x + 4}\), for \(x > -4\), is ____.", ["1", "−1", "2", "−2"], "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "Write the top as \\((x + 4)^2 + 1\\).",
 steps(("Rewrite", p(r"\(\dfrac{(x+4)^2 + 1}{x + 4} = (x + 4) + \dfrac1{x + 4} \ge 2\), equal when \(x = -3\)."))) + final("2, option 3"),
 concept=r"\[t + \tfrac1t \ge 2 \ \ (t > 0)\]", why_rows=[("1", "Below the AM–GM bound."), ("2", "Only for x < −4."), ("4", "Only for x < −4.")])

P.qa(13, r"The sum of the coefficients of the expansion of \(x(x + 1)(x + 2)(x + 3)(x + 4)(x + 5)\dots\) up to \(n\) terms is ____.", [r"\(n!\)", r"\(n^2\)", r"\(\tfrac{n(n+1)}{2}\)", r"\(\tfrac{n(n+1)(2n+1)}{6}\)"], "MCQ", "1", ["Algebra::Equations_and_Polynomials"], "Easy",
 "Sum of coefficients = the value at \\(x = 1\\).",
 steps(("Put x = 1", p(r"\(1 \cdot 2 \cdot 3 \cdots n = n!\)."))) + final(r"\(n!\), option 1"), why_rows=[("2", "Not a product."), ("3", "A sum, not a product."), ("4", "Sum of squares.")])

P.qa(14, r"The line \(\ell: ax + by + c = 0\) (\(a, b, c\) non-zero real numbers and \(\tfrac ab\) negative) and the two axes of a Cartesian plane form an isosceles triangle. If we reflect the triangle on its base (the side other than the two equal sides) we get one more triangle congruent to the original triangle. The coordinates of one of the vertices of this new triangle is \((h, k)\) where neither \(h\) nor \(k\) is zero. What will be the value of \((h + k)\)?",
 ["−1", "0", "1", "Cannot be determined"], "MCQ", "2", ["Geometry::Coordinate_Geometry"], "Medium",
 "\\(\\tfrac ab < 0\\) makes the slope positive: the line cuts the axes at \\((p, 0)\\) and \\((0, -p)\\) or the mirror case.",
 steps(("The triangle", p(r"Equal legs on the axes: vertices \((0, 0), (p, 0), (0, -p)\). The base is the line \(x - y = p\).")),
       ("Reflect the origin", p(r"The reflection of \((0, 0)\) in \(x - y = p\) is \((p, -p)\). So \(h + k = 0\). The other case gives \((-p, p)\), also 0."))) + final("0, option 2"),
 why_rows=[("1", "Not from the reflection."), ("3", "Not from the reflection."), ("4", "Always 0.")])

P.qa(15, "In a triangle ABC, AC = 6 cm. A circle drawn with AC as diameter passes through B. Another circle drawn with center at B passes through A and C. Then the area (in sq. cm) of the overlapping region between the two circles is ____.", ["9π", "9(π − 1)", "9(2π − 1)", "18(π − 1)"], "MCQ", "2", ["Geometry::Circles"], "Hard",
 "∠B = 90° (angle in a semicircle) and BA = BC, so BA = \\(3\\sqrt2\\).",
 steps(("The pieces", p(r"The overlap is the half of the small circle on B’s side of AC (area \(\tfrac92\pi\)) plus the part of the big circle beyond AC.")),
       ("Big circle’s segment", p(r"Radius \(3\sqrt2\), angle ABC = 90°: segment = quarter circle − triangle \(= \tfrac{18\pi}{4} - 9\).")),
       ("Total", p(r"\(\tfrac92\pi + \tfrac92\pi - 9 = 9(\pi - 1)\)."))) + final("Option 2"),
 why_rows=[("1", "Forgets to subtract the triangle."), ("3", "Double-counts."), ("4", "Doubles the answer.")])

P.qa(16, r"If \(\cos x - \sin x = \sqrt3 \sin x\), the value of \(\tfrac12\cos x + \sin x\) is ____.", [r"\(\sqrt3\cos x\)", r"\(\tfrac{\sqrt3}{2}\cos x\)", r"\(\tfrac{\sqrt3}{2}\sin x\)", r"\(\sqrt3\sin x\)"], "MCQ", "2", ["Geometry::Trigonometry"], "Medium",
 "Write \\(\\sin x\\) in terms of \\(\\cos x\\).",
 steps(("sin x", p(r"\(\cos x = (1 + \sqrt3)\sin x\), so \(\sin x = \tfrac{\cos x}{1 + \sqrt3} = \tfrac{\sqrt3 - 1}{2}\cos x\).")),
       ("The expression", p(r"\(\tfrac12\cos x + \tfrac{\sqrt3 - 1}{2}\cos x = \tfrac{\sqrt3}{2}\cos x\)."))) + final("Option 2"),
 why_rows=[("1", "Twice the value."), ("3", "Mixes sin and cos."), ("4", "Mixes sin and cos.")])

P.qa(17, "∆ABC is a right-angled triangle such that AB ⊥ BC. Point D is located on AC such that BD ⊥ AC. The lengths of AB, BC, CA and BD are integers if expressed in centimetres. What can be the smallest value of the perimeter (in cm) of ∆ABC?", [], "TITA", "60", ["Geometry::Triangles"], "Medium",
 "BD = AB × BC ÷ AC must be a whole number.",
 steps(("Pythagorean triples", p(r"3-4-5 scaled by \(k\): BD \(= \tfrac{12k}{5}\), whole only when \(k\) is a multiple of 5. 15-20-25 gives BD = 12, perimeter 60. (Other primitive triples give larger perimeters.)"))) + final("60"))

P.qa(18, "If the second term of an infinite geometric progression is 25 and the sum of all the terms of the series is positive, then the smallest possible value of the sum of the geometric progression is ________ .", ["40", "50", "80", "100"], "MCQ", "4", ["Algebra::Progressions_and_Series"], "Medium",
 "\\(S = \\tfrac{a}{1 - r} = \\tfrac{25}{r(1 - r)}\\).",
 steps(("Minimise", p(r"\(S > 0\) needs \(0 < r < 1\). \(r(1 - r) \le \tfrac14\), so \(S \ge 100\), at \(r = \tfrac12\)."))) + final("100, option 4"), why_rows=[("1", "Below the minimum."), ("2", "Below the minimum."), ("3", "Below the minimum.")])

P.qa(19, "How many three-digit natural numbers exist such that they are divisible by both 3 and 4 with no repetition of digits?", ["56", "57", "58", "59"], "MCQ", "2", ["Number_System::Factors_and_Divisibility"], "Hard",
 "Multiples of 12 from 108 to 996 are 75; remove those with a repeated digit.",
 steps(("All multiples of 12", p("From 108 = 12 × 9 to 996 = 12 × 83: 75 numbers.")),
       ("Remove repeated digits", p("Going through them, 18 have a repeated digit: 144, 228, 252, 288, 300, 336, 444, 552, 588, 600, 636, 660, 696, 744, 828, 888, 900, 996.")),
       ("Count", p("75 − 18 = 57."))) + final("57, option 2"),
 why_rows=[("1", "Off by one."), ("3", "Off by one."), ("4", "Off by two.")])

P.qa(20, r"The number of integer solutions of the equation \((x^2 - 50)^{x^2 + 5x - 50} = 1\) is ____.", [], "TITA", "4", ["Algebra::Quadratic_Equations"], "Hard",
 "\\(a^b = 1\\) when \\(b = 0\\) (with \\(a \\ne 0\\)), \\(a = 1\\), or \\(a = -1\\) with \\(b\\) even.",
 steps(("Exponent 0", p(r"\(x^2 + 5x - 50 = 0\): \(x = 5\) or \(-10\). Bases −25 and 50, both non-zero. ✓")),
       ("Base 1", p(r"\(x^2 = 51\): no integer.")),
       ("Base −1", p(r"\(x^2 = 49\): \(x = \pm7\). Exponents \(49 + 35 - 50 = 34\) and \(49 - 35 - 50 = -36\), both even. ✓"))) + final("4"))

P.qa(21, "ABCD is a four-digit number where all the digits are distinct and non-zero. If we select any two consecutive digits and any permutation thereof, each of the two-digit numbers so formed are prime numbers. How many values of ABCD exist?", [], "TITA", "4", ["Number_System::Factors_and_Divisibility"], "Hard",
 "Both orders of each adjacent pair must be prime, so digits are odd and not 5.",
 steps(("Pairs that work both ways", p("From 1, 3, 7, 9: 13/31, 17/71, 37/73, 79/97. (19/91 fails: 91 = 7 × 13; 39/93 fails.)")),
       ("Chains of four", p("Joining these pairs: 1-3-7-9 and 3-1-7-9, and their reverses 9-7-3-1, 9-7-1-3. Four numbers: 1379, 3179, 9731, 9713."))) + final("4"))

P.qa(22, "Two trains, whose lengths are in the ratio 5 : 3, are traveling on parallel tracks. The difference in their speeds is 72 km/hr. They take 20 seconds to cross each other when traveling in opposite directions and 50 seconds when traveling in the same direction. How much more time (in seconds) will the slower train take in comparison to the faster train to cross a 180 metres long bridge given that the length of the slower train is less than that of the faster train?",
 [], "TITA", "14", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "72 km/h = 20 m/s. Same direction: total length ÷ 20 = 50 s.",
 steps(("Lengths", p("Total length 20 × 50 = 1000 m: 625 and 375.")), ("Speeds", p("Sum = 1000 ÷ 20 = 50 m/s; difference 20: 35 and 15 m/s.")),
       ("Bridge", p("Slower (375 m at 15): 555 ÷ 15 = 37 s. Faster (625 m at 35): 805 ÷ 35 = 23 s. Difference 14 s."))) + final("14"))
