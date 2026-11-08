# -*- coding: utf-8 -*-
# Simp Mock 2 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_02 import P
import m25_02_figs as F

P.qa(1, "Find the remainder when 123412341234… up to 206 digits is divided by 64.", ["8", "12", "16", "20"], "MCQ", "4", ["Number_System::Remainders"], "Medium",
 "\\(10^6\\) is divisible by 64, so only the last six digits matter.",
 steps(("Last six digits", p("206 = 4 × 51 + 2, so the number ends …1234 12. The last six digits are 123412.")),
       ("Divide", p("123412 = 64 × 1928 + 20."))) + final("20, option 4"),
 concept=r"\[2^6 \mid 10^6:\ \text{remainder mod } 64 \text{ depends on the last 6 digits}\]",
 why_rows=[("1", "Uses the wrong final digits."), ("2", "Uses the wrong final digits."), ("3", "Uses the wrong final digits.")])

P.qa(2, "The product of the digits of a three-digit positive integer ‘n’ is 10. Which of the following cannot be a factor of ‘n’?", ["19", "25", "29", "43"], "MCQ", "3", ["Number_System::Factors_and_Divisibility"], "Easy",
 "The digits must be 1, 2 and 5. List all six numbers.",
 steps(("Candidates", p("125, 152, 215, 251, 512, 521.")),
       ("Factors", p("152 = 8 × 19; 125 = 5³; 215 = 5 × 43; 251 and 521 are prime; 512 = 2⁹. None is a multiple of 29."))) + final("29, option 3"),
 why_rows=[("1", "152 = 8 × 19."), ("2", "125 = 5 × 25."), ("4", "215 = 5 × 43.")])

P.qa(3, "What is the value of (4B7)<sub>17</sub> when converted to base 13? (In base 13 and 17, A = 10, B = 11 and so on.)", ["(7AC)<sub>13</sub>", "(7AB)<sub>13</sub>", "(7CB)<sub>13</sub>", "(7BC)<sub>13</sub>"], "MCQ", "3", ["Number_System::Miscellaneous"], "Easy",
 "Go through base 10.",
 steps(("To base 10", p(r"\(4 \times 289 + 11 \times 17 + 7 = 1350\).")),
       ("To base 13", p(r"\(1350 = 7 \times 169 + 167\), and \(167 = 12 \times 13 + 11\). Digits 7, 12 (C), 11 (B)."))) + final("(7CB)<sub>13</sub>, option 3"),
 why_rows=[("1", "Digits wrong."), ("2", "Digits wrong."), ("4", "Last two digits swapped.")])

P.qa(4, "Kamal travels from her home to office at her normal speed of 50 km/hr and reaches the office on time. If she travels at 40 km/hr, she will reach the office 12 minutes late. One day, she started from her home at twice the normal speed and covered half the distance between her home and office. Then she lost 6 minutes due to a traffic jam on the road. At what speed will she then have to travel to reach the office on time?",
 ["75 km/hr", "60 km/hr", "40 km/hr", "30 km/hr"], "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Find the distance from the 12-minute difference.",
 steps(("Distance", p(r"\(\tfrac{d}{40} - \tfrac{d}{50} = \tfrac{12}{60}\) gives \(d = 40\) km; usual time 48 minutes.")),
       ("That day", p("20 km at 100 km/h: 12 minutes. Plus 6 minutes lost: 18. Left: 30 minutes for 20 km, so 40 km/h."))) + final("40 km/hr, option 3"),
 why_rows=[("1", "Not enough time left for that speed to be needed."), ("2", "Ignores the delay."), ("4", "Too slow: 20 km would take 40 minutes.")])

P.qa(5, r"A and B can individually complete a piece of work in a certain integer number of days. When working at their regular efficiencies, A and B together complete one-fourth of a task in 3 days, with A being more efficient than B. If their efficiencies are increased by \(33\tfrac13\)% and 25% respectively, they can complete the task alone in \(x\) days and \(y\) days, where \(x\) and \(y\) are integers satisfying \(390 > xy > 330\). Find the time they take to complete the entire task when working together with their enhanced efficiencies.",
 [r"\(9\tfrac{3}{13}\) days", r"\(9\tfrac{9}{47}\) days", r"\(9\tfrac{27}{109}\) days", "None of these"], "MCQ", "1", ["Arithmetic::Time_and_Work"], "Hard",
 "Together they take 12 days, so \\(\\tfrac1a + \\tfrac1b = \\tfrac1{12}\\) with \\(a < b\\).",
 steps(("Integer pairs", p(r"\((a - 12)(b - 12) = 144\): (13, 156), (14, 84), (15, 60), (16, 48), (18, 36), (20, 30), (21, 28).")),
       ("Enhanced times", p(r"\(x = \tfrac34a\), \(y = \tfrac45b\), both integers, so \(a\) is a multiple of 4 and \(b\) of 5: (20, 30) only, giving \(x = 15,\ y = 24\), \(xy = 360\) ✓.")),
       ("Together", p(r"\(\tfrac1{15} + \tfrac1{24} = \tfrac{13}{120}\): \(\tfrac{120}{13} = 9\tfrac{3}{13}\) days."))) + final("Option 1"),
 concept=r"\[\frac1a + \frac1b = \frac1c \iff (a - c)(b - c) = c^2\]",
 why_rows=[("2", "From a pair that fails the integer test."), ("3", "From a pair that fails the integer test."), ("4", "Option 1 is right.")])

P.qa(6, "A person bought a new watch. The shopkeeper correctly sets the time at exactly 11:00 AM. The first time the minute and hour hands of the watch were perfectly aligned in opposite directions after it was set, the shopkeeper called the buyer: he had unintentionally doubled the speed of the minute hand during the setup. This does not affect the hour hand at all. What was the correct time when the shopkeeper called?",
 [r"\(11{:}13\tfrac{1}{23}\) AM", r"\(11{:}23\tfrac{1}{23}\) AM", r"\(11{:}33\tfrac{1}{23}\) AM", r"\(11{:}36\tfrac{1}{23}\) AM"], "MCQ", "1", ["Arithmetic::Miscellaneous"], "Hard",
 "Minute hand: 12° per minute now. Hour hand: 0.5° per minute. At 11:00 the minute hand is 30° behind… or ahead?",
 steps(("Start", p("At 11:00 the hour hand is at 330°, the minute hand at 0°: the minute hand is 30° ahead (going clockwise).")),
       ("Opposite", p(r"It gains 11.5° per minute and must be 180° ahead: \(\tfrac{150}{11.5} = \tfrac{300}{23} = 13\tfrac1{23}\) minutes."))) + trap("The clock face is a circle: 330° behind is the same as 30° ahead.") + final(r"\(11{:}13\tfrac{1}{23}\) AM, option 1"),
 why_rows=[("2", "Off by 10 minutes."), ("3", "Uses the normal speed."), ("4", "Uses the normal speed and a different gap.")])

P.qa(7, r"On a certain day in a class, which had fewer than 100 students enrolled in it, \(86\tfrac23\)% of the students were present. Among all the students enrolled in the class, 4% girls and 20% boys were absent. If all the students of the class were either boy or girl and the number of boys exceeded that of the girls by 10 then the total number of students enrolled in the class was ____.",
 [], "TITA", "60", ["Arithmetic::Percentages"], "Medium",
 "Absent = \\(\\tfrac{2}{15}\\) of the class.",
 steps(("Equation", p(r"With \(g\) girls and \(g + 10\) boys: \(0.04g + 0.2(g + 10) = \tfrac{2}{15}(2g + 10)\).")),
       ("Solve", p(r"Multiply by 75: \(3g + 15g + 150 = 20g + 100\), so \(g = 25\). Class: 25 + 35 = 60."))) + final("60"))

P.qa(8, "In a certain village, the rates of completing a task X are as follows: 25 men can complete X in 15 days, or 25 women can complete X in 20 days, or 20 children can complete X in 25 days. If 15 men, 20 women, and 10 children start working together on task X, how many days will it take them to finish the job?", [], "TITA", "10", ["Arithmetic::Time_and_Work"], "Easy",
 "One man does \\(\\tfrac1{375}\\) a day.",
 steps(("Rates", p(r"Man \(\tfrac1{375}\), woman \(\tfrac1{500}\), child \(\tfrac1{500}\).")),
       ("Team", p(r"\(\tfrac{15}{375} + \tfrac{20}{500} + \tfrac{10}{500}\) \(= 0.04 + 0.04 + 0.02 = 0.1\) a day: 10 days."))) + final("10"))

P.qa(9, "A student gets an aggregate of 50% marks in five subjects in the ratio 10 : 9 : 8 : 7 : 6. Each of the five marks received by the student is a natural number. The maximum marks for each subject is the same and it is a natural number. What can be the maximum value of the maximum marks in each subject given that it is not more than 500?", [], "TITA", "496", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "Marks \\(10k, 9k, \\dots\\) total \\(40k\\), which is half of \\(5M\\).",
 steps(("Link", p(r"\(40k = 2.5M\), so \(M = 16k\).")), ("Largest", p(r"\(16k \le 500\): \(k = 31\), \(M = 496\)."))) + final("496"))

P.qa(10, "A partially filled container initially holds pure grape juice. Five litres of the juice is replaced with water, followed by a second replacement of six litres of the mixture with water. Three litres of pure grape juice is added further to achieve a 50% concentration of grape juice in the mixture. Determine the initial volume (in litres) of pure grape juice in the container.", ["25", "20", "17", "15"], "MCQ", "4", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "After the two replacements, juice = \\(\\tfrac{(V-5)(V-6)}{V}\\).",
 steps(("Equation", p(r"\(\tfrac{(V-5)(V-6)}{V} + 3 = \tfrac{V + 3}{2}\).")),
       ("Test", p(r"\(V = 15\): \(\tfrac{10 \times 9}{15} + 3 = 9\) and \(\tfrac{18}{2} = 9\). ✓"))) + final("15, option 4"),
 why_rows=[("1", "Gives 19.2 + 3 against 14."), ("2", "Gives 10.5 + 3 against 11.5."), ("3", "Gives about 8.5 + 3 against 10.")])

P.qa(11, "Chahat alone started a business on 1 January 2024 by investing certain capital. Nisha joined the business on 1 January 2025, while Chahat withdrew half of her capital exactly halfway in 2025. The total profits earned by the business in 2024 and 2025 were the same. Chahat’s profit share from the business in 2025 was only 60% of that in 2024. Chahat kept her investment unchanged in 2026. By what percentage should Nisha increase her investment at the beginning of 2026 so that Nisha can claim half of the profit earned in 2026?",
 ["200%", "100%", "50%", "0%"], "MCQ", "4", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "Chahat’s 2025 share was 60% of the whole profit.",
 steps(("2025 shares", p(r"Chahat: \(C\) for half a year and \(\tfrac C2\) for half: \(0.75C\). Nisha: \(N\). \(\tfrac{0.75C}{0.75C + N} = 0.6\), so \(N = 0.5C\).")),
       ("2026", p(r"Chahat has \(\tfrac C2\) all year; Nisha has \(\tfrac C2\). They are already equal."))) + final("0%, option 4"),
 why_rows=[("1", "No increase is needed."), ("2", "Compares with Chahat’s original capital."), ("3", "No increase is needed.")])

P.qa(12, r"If all the roots of the equation \(x^4 + 2x^3 - 960x^2 - 1922x - 961 = 0\) are integers then the sum of the squares of the distinct roots, taken only once, is ____.", ["962", "1922", "1923", "1924"], "MCQ", "3", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Try \\(x = -1\\). Note 961 = 31².",
 steps(("Factor", p(r"\(x = -1\) works. In fact the polynomial factorises as") + r"\[(x+1)^2(x^2 - 961)\]"),
       ("Roots", p(r"−1 (twice), 31, −31. Distinct squares: 1 + 961 + 961 = 1923."))) + final("1923, option 3"),
 why_rows=[("1", "Counts ±31 once."), ("2", "Leaves out −1."), ("4", "Counts −1 twice.")])

P.qa(13, r"Given \(f(x) = x^2 + 3x + k\) and \(g(x) = x^2 + x + 1\) for all real \(x\). Find the value of \(k\) if \(f(1) - g(2) + f(3) - g(4)\) \(+ \dots + f(19) - g(20) = 20\).", ["6", "5", "4", "3"], "MCQ", "2", ["Algebra::Functions"], "Medium",
 "Work out one pair \\(f(2m-1) - g(2m)\\).",
 steps(("One pair", p(r"\(f(2m-1) = 4m^2 + 2m - 2 + k\)") + p(r"\(g(2m) = 4m^2 + 2m + 1\)") + p(r"Difference: \(k - 3\).")),
       ("Ten pairs", p(r"\(10(k - 3) = 20\), so \(k = 5\)."))) + final("5, option 2"),
 why_rows=[("1", "Gives 30."), ("3", "Gives 10."), ("4", "Gives 0.")])

P.qa(14, r"If \(a\) and \(b\) are the roots of the equation \(x^2 + x - 5 = 0\) then the value of \(a^4 + b^4\) is ____.", ["91", "146", "71", "81"], "MCQ", "3", ["Algebra::Quadratic_Equations"], "Easy",
 "\\(a + b = -1\\), \\(ab = -5\\).",
 steps(("Squares", p(r"\(a^2 + b^2 = 1 + 10 = 11\).")), ("Fourth powers", p(r"\(a^4 + b^4 = 11^2 - 2 \times 25 = 71\)."))) + final("71, option 3"),
 concept=r"\[a^4 + b^4 = (a^2 + b^2)^2 - 2a^2b^2\]",
 why_rows=[("1", "Forgets to subtract."), ("2", "Wrong."), ("4", "Uses 2ab instead of 2a²b².")])

P.qa(15, r"It is given that \(a_1, a_2, a_3, \dots, a_{100}\) are distinct positive integers. The largest positive integer that will definitely be less than the value of \(\left(\dfrac{a_1}{a_2} + \dfrac{a_2}{a_3} + \dots + \dfrac{a_{99}}{a_{100}} + \dfrac{a_{100}}{a_1}\right)\) is ____.", [], "TITA", "100", ["Algebra::Inequalities_and_Absolute_Value"], "Hard",
 "The 100 fractions multiply to 1. AM–GM.",
 steps(("AM–GM", p(r"The sum is at least \(100 \times \sqrt[100]{1} = 100\), with equality only if every fraction is 1, impossible for distinct numbers. So the sum is more than 100.")),
       ("Can it be close?", p(r"With \(a_i = N + i\) for huge \(N\), every fraction is almost 1 and the sum is just over 100. So nothing bigger than 100 is guaranteed."))) + final("100"))

P.qa(16, r"If \(a\) and \(b\) are two distinct integers and \(a^2 - b = b^2 - a = 1\), then the value of \(a^3 + b^3\) is ____.", ["−1", "0", "1", "2"], "MCQ", "1", ["Algebra::Linear_Equations"], "Medium",
 "Subtract the two equations.",
 steps(("Subtract", p(r"\(a^2 - b^2 + a - b = 0\): \((a - b)(a + b + 1) = 0\), so \(a + b = -1\).")),
       ("Add", p(r"\(a^2 + b^2 - (a + b) = 2\), so \(a^2 + b^2 = 1\) and \(ab = 0\). (The numbers are 0 and −1.)")),
       ("Cube sum", p(r"\((a+b)^3 - 3ab(a+b) = -1\)."))) + final("−1, option 1"),
 why_rows=[("2", "Sign slip."), ("3", "Sign slip."), ("4", "Not from 0 and −1.")])

P.qa(17, "Which of the following represents a line such that every point on it is equidistant from lines x = 2 and y = 4?", ["x − y = 2", "x − y = −2", "x + y = −6", "x + y = −2"], "MCQ", "2", ["Geometry::Coordinate_Geometry"], "Easy",
 "\\(|x - 2| = |y - 4|\\).",
 steps(("Two lines", p(r"\(y - 4 = x - 2\), i.e. \(x - y = -2\); or \(y - 4 = -(x - 2)\), i.e. \(x + y = 6\).")), ("Match", p("Option 2."))) + final("Option 2"),
 why_rows=[("1", "Sign error."), ("3", "The bisector is x + y = 6."), ("4", "The bisector is x + y = 6.")])

P.qa(18, "A semicircle has been inscribed in equilateral triangle ABC of side 10 units, such that the diameter of the semicircle lies on side BC of the triangle as shown below. Point O is the midpoint of side BC. The diameter of the semicircle is ____ units." + F.SEMI_FIG,
 ["More than 8 but less than 8.25", "More than 8.25 but less than 8.5", "More than 8.5 but less than 8.75", "More than 8.75"], "MCQ", "3", ["Geometry::Circles"], "Medium",
 "The radius is the distance from O to side AB.",
 steps(("Radius", p(r"OB = 5, and the angle at B is 60°, so the distance from O to AB is \(5 \sin 60^\circ = \tfrac{5\sqrt3}{2} \approx 4.33\).")),
       ("Diameter", p(r"\(5\sqrt3 \approx 8.66\)."))) + final("Option 3"),
 why_rows=[("1", "Too small."), ("2", "Too small."), ("4", "Too large.")])

P.qa(19, r"The lengths (in cm) of the two smaller sides of a right angled triangle are \(3\sin\theta\) and \(5\cos\theta\), where \(\theta\) is an acute angle. If the length of the hypotenuse is \(\sqrt{17}\) cm then the value (in degree) of \(\theta\) is ____.", [], "TITA", "45", ["Geometry::Triangles"], "Easy",
 "Pythagoras, then replace \\(\\sin^2\\) with \\(1 - \\cos^2\\).",
 steps(("Equation", p(r"\(9\sin^2\theta + 25\cos^2\theta = 17\), so \(9 + 16\cos^2\theta = 17\), \(\cos^2\theta = \tfrac12\).")), ("Angle", p("θ = 45°."))) + final("45"))

P.qa(20, r"An equilateral triangle has sides of length \(20\sqrt3\) cm. A circle of diameter 15 cm is drawn inside the triangle such that the base of the triangle is tangent to it and one diameter of the circle lies on the line segment joining the midpoint of the base with the opposite vertex. A second circle drawn with half the diameter of the first circle touches the first circle externally and one of its diameters lies along the same line segment. This process (every subsequent circle with half the diameter of the previous circle and touching the previous circle externally in exactly one point) continues as long as the diameters of all the circles drawn fit within the same line segment joining the midpoint of the base with the opposite vertex. Find the ratio of the area of the triangle to the sum of the areas of all such circles.",
 [r"\(4\sqrt3 : \pi\)", r"\(2\sqrt3 : \pi\)", r"\(6\sqrt3 : \pi\)", r"\(3\sqrt3 : \pi\)"], "MCQ", "1", ["Geometry::Circles"], "Medium",
 "The height is 30; the diameters 15, 7.5, 3.75, … add up to exactly 30, so every circle fits.",
 steps(("Triangle", p(r"Height \(= \tfrac{\sqrt3}{2} \times 20\sqrt3 = 30\). Area \(= \tfrac{\sqrt3}{4} \times 1200 = 300\sqrt3\).")),
       ("Circles", p(r"Areas \(\tfrac\pi4(15^2 + 7.5^2 + \dots)\) \(= \tfrac\pi4 \times \dfrac{225}{1 - \tfrac14}\) \(= 75\pi\).")),
       ("Ratio", p(r"\(300\sqrt3 : 75\pi = 4\sqrt3 : \pi\)."))) + final("Option 1"),
 concept=r"\[a + ar + ar^2 + \dots = \frac{a}{1 - r}\ \ (|r| < 1)\]",
 why_rows=[("2", "Halves the ratio."), ("3", "Wrong sum of areas."), ("4", "Wrong sum of areas.")])

P.qa(21, r"An arithmetic progression contains an even number of terms. The sum of all terms in odd numbered positions is \(117\tfrac12\) and the sum of all terms in even numbered positions is 125. Find the number of terms in the arithmetic progression if the last term exceeds the first term by \(14\tfrac14\).", [], "TITA", "20", ["Algebra::Progressions_and_Series"], "Medium",
 "With \\(2n\\) terms, each even-position term is \\(d\\) more than the odd one before it.",
 steps(("Two equations", p(r"Even sum − odd sum \(= nd = 7.5\). Last − first \(= (2n - 1)d = 14.25\).")),
       ("Solve", p(r"\(2nd - d = 14.25\) gives \(15 - d = 14.25\), \(d = 0.75\), \(n = 10\): 20 terms."))) + final("20"))

P.qa(22, "There are ‘m’ parallel lines in a plane. There is another set of ‘n’ parallel lines in the same plane such that the two sets of parallel lines intersect in a total of 72 distinct points. What can be the maximum number of parallelograms that can be drawn using these lines?", [], "TITA", "1008", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "\\(mn = 72\\); parallelograms \\(= \\binom m2\\binom n2\\).",
 steps(("Try the factor pairs", table(["m × n", "Parallelograms"], [["8 × 9", "28 × 36 = 1008"], ["6 × 12", "15 × 66 = 990"], ["4 × 18", "6 × 153 = 918"], ["3 × 24", "3 × 276 = 828"]], hi={(0, 1)}))) + final("1008"),
 concept=r"\[\text{Parallelograms} = \binom m2 \binom n2\]")
