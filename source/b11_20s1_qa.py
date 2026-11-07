# -*- coding: utf-8 -*-
# Batch 11 — CAT 2020 Slot 1: QA (25 of 26; Q10 isn't in the source).
from fmt import steps, final, trap, why, table, p
from b11_20s1 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"If \(y\) is a negative number such that \(2^{y^2 \log_3 5} = 5^{\log_2 3}\), then \(y\) equals",
 M(r"\log_2\left(\tfrac13\right)", r"-\log_2\left(\tfrac15\right)", r"-\log_2\left(\tfrac13\right)", r"\log_2\left(\tfrac15\right)"), "MCQ", "1", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Take log base 2 of both sides.",
 steps(("Logs", p(r"\(y^2 \log_3 5 = \log_2 3 \cdot \log_2 5\), so \(y^2\) \(= \log_2 3 \cdot \dfrac{\log_2 5}{\log_3 5}\) \(= \log_2 3 \cdot \log_2 3\).")),
       ("Sign", p(r"\(y = -\log_2 3 = \log_2\tfrac13\), since \(y\) is negative."))) + final(r"\(\log_2\tfrac13\), option 1"),
 concept=r"\[\frac{\log_b x}{\log_c x} = \log_b c\]",
 why_rows=[("2", r"Equals \(\log_2 5\), positive."), ("3", r"Equals \(\log_2 3\), positive."), ("4", r"\(-\log_2 5\), the wrong number.")])

P.qa(2, r"A gentleman decided to treat a few children in the following manner. He gives half of his total stock of toffees and one extra to the first child, and then the half of the remaining stock along with one extra to the second and continues giving away in this fashion. His total stock exhausts after he takes care of \(5\) children. How many toffees were there in his stock initially?",
 [], "TITA", "62", ["Arithmetic::Miscellaneous"], "Easy",
 "Work backwards from the last child.",
 steps(("Backwards", p(r"Before a child, the stock \(s\) satisfies \(s - (\tfrac s2 + 1) = \text{what is left}\), so \(s = 2(\text{left} + 1)\).")),
       ("Five children", p("Left after the fifth: 0. Before: 2, 6, 14, 30, 62."))) + final(r"\(62\)"),
 concept=p("For ‘give half plus one’ processes, reverse each step: double what remains and add 2."))

P.qa(3, r"How many \(3\)-digit numbers are there, for which the product of their digits is more than \(2\) but less than \(7\)?",
 [], "TITA", "21", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "The product is 3, 4, 5 or 6. List the digit sets.",
 steps(("Digit sets", p("{1, 1, 3}, {1, 1, 4}, {1, 2, 2}, {1, 1, 5}, {1, 1, 6}, {1, 2, 3}.")),
       ("Arrangements", p("Each set with a repeated digit gives 3 numbers; {1, 2, 3} gives 6. Total 5 × 3 + 6 = 21."))) + final(r"\(21\)"),
 concept=r"\[\text{arrangements with a repeat: } \frac{3!}{2!} = 3\]")

P.qa(4, r"The number of real-valued solutions of the equation \(2^x + 2^{-x} = 2 - (x - 2)^2\) is",
 ["infinite", "0", "2", "1"], "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Compare the smallest value of the left side with the largest of the right.",
 steps(("Bounds", p(r"\(2^x + 2^{-x} \ge 2\), with equality only at \(x = 0\). \(2 - (x - 2)^2 \le 2\), with equality only at \(x = 2\).")),
       ("No overlap", p("Both sides would have to equal 2 at the same x, which can’t happen."))) + final("0, option 2"),
 concept=r"\[a + \frac1a \ge 2 \quad (a > 0)\]",
 why_rows=[("1", "There are none."), ("3", "There are none."), ("4", "There are none.")])

P.qa(5, r"How many distinct positive integer-valued solutions exist to the equation \((x^2 - 7x + 11)^{(x^2 - 13x + 42)} = 1\)?",
 M("2", "4", "8", "6"), "MCQ", "4", ["Algebra::Logarithms_and_Exponents", "Algebra::Quadratic_Equations"], "Medium",
 "A power equals 1 in three ways.",
 steps(("Exponent 0", p(r"\(x^2 - 13x + 42 = 0\): \(x = 6, 7\).")),
       ("Base 1", p(r"\(x^2 - 7x + 11 = 1\): \(x = 2, 5\).")),
       ("Base −1, even exponent", p(r"\(x^2 - 7x + 11 = -1\): \(x = 3, 4\). The exponents are 12 and 6, both even, so both work.")),
       ("Total", p("6 solutions."))) + trap("Check the exponent is even when the base is −1.") + final(r"\(6\), option 4"),
 concept=r"\[a^b = 1 \iff b = 0 \;(a \ne 0),\; a = 1,\; \text{or } a = -1 \text{ with } b \text{ even}\]",
 why_rows=[("1", "Only the exponent-zero case."), ("2", "Leaves out the base −1 case."), ("3", "Counts extra values.")])

P.qa(6, r"A solid right circular cone of height \(27\) cm is cut into two pieces along a plane parallel to its base at a height of \(18\) cm from the base. If the difference in volume of the two pieces is \(225\) cc, the volume, in cc, of the original cone is",
 M("264", "256", "232", "243"), "MCQ", "4", ["Geometry::Mensuration"], "Easy",
 "The top piece is a small cone of height 9, a third of the original.",
 steps(("Small cone", p(r"Scale \(\tfrac13\), so volume \(\tfrac{1}{27}V\). The frustum is \(\tfrac{26}{27}V\).")),
       ("Difference", p(r"\(\tfrac{25}{27}V = 225\), so \(V = 243\)."))) + final(r"\(243\), option 4"),
 concept=r"\[\text{similar solids: volume ratio} = (\text{scale})^3\]",
 why_rows=[("1", "Not a multiple of 27."), ("2", "Not a multiple of 27."), ("3", "Not a multiple of 27.")])

P.qa(7, r"The area of the region satisfying the inequalities \(|x| - y \le 1\), \(y \ge 0\) and \(y \le 1\) is",
 [], "TITA", "3", ["Geometry::Coordinate_Geometry"], "Easy",
 r"At height \(y\), the region runs from \(x = -(y + 1)\) to \(y + 1\).",
 steps(("The shape", p(r"A trapezium with parallel sides 2 (at \(y = 0\)) and 4 (at \(y = 1\)), height 1.")),
       ("Area", p(r"\(\tfrac12(2 + 4) \times 1 = 3\)."))) + final(r"\(3\)"),
 concept=r"\[\text{trapezium} = \tfrac12(a + b)h\]")

P.qa(8, r"On a rectangular metal sheet of area \(135\) sq inch, a circle is painted such that the circle touches two opposite sides. If the area of the sheet left unpainted is two-thirds of the painted area then the perimeter of the rectangle in inches is",
 M(r"5\sqrt\pi\left(3 + \tfrac{9}{\pi}\right)", r"3\sqrt\pi\left(5 + \tfrac{12}{\pi}\right)", r"4\sqrt\pi\left(3 + \tfrac{9}{\pi}\right)", r"3\sqrt\pi\left(\tfrac52 + \tfrac{6}{\pi}\right)"), "MCQ", "2", ["Geometry::Circles", "Geometry::Mensuration"], "Medium",
 "Painted + unpainted = 135, with unpainted two-thirds of painted.",
 steps(("The circle", p(r"Painted area is \(\tfrac35 \times 135 = 81\), so \(r = \tfrac{9}{\sqrt\pi}\) and the width is \(\tfrac{18}{\sqrt\pi}\).")),
       ("Length", p(r"\(\tfrac{135}{18/\sqrt\pi} = 7.5\sqrt\pi\).")),
       ("Perimeter", p(r"\(2\left(\tfrac{18}{\sqrt\pi} + 7.5\sqrt\pi\right)\) \(= 15\sqrt\pi + \tfrac{36}{\sqrt\pi}\) \(= 3\sqrt\pi\left(5 + \tfrac{12}{\pi}\right)\)."))) +
 final(r"Option 2"),
 concept=r"\[\text{circle touching two opposite sides: diameter} = \text{width}\]",
 why_rows=[("1", r"Expands to \(15\sqrt\pi + 45/\sqrt\pi\)."), ("3", r"Expands to \(12\sqrt\pi + 36/\sqrt\pi\)."), ("4", "Half the perimeter.")])

P.qa(9, r"A circle is inscribed in a rhombus with diagonals \(12\) cm and \(16\) cm. The ratio of the area of circle to the area of rhombus is",
 M(r"\tfrac{3\pi}{25}", r"\tfrac{2\pi}{15}", r"\tfrac{6\pi}{25}", r"\tfrac{5\pi}{18}"), "MCQ", "3", ["Geometry::Circles", "Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "The rhombus’s area is half its perimeter times the inradius.",
 steps(("Side and area", p("Side 10 (half-diagonals 6 and 8), area 96.")),
       ("Inradius", p(r"\(96 = \tfrac12 \times 40 \times r\), so \(r = 4.8\).")),
       ("Ratio", p(r"\(\tfrac{\pi \times 23.04}{96}\) \(= 0.24\pi\) \(= \tfrac{6\pi}{25}\)."))) + final(r"\(\tfrac{6\pi}{25}\), option 3"),
 concept=r"\[\text{area} = \tfrac12 \times \text{perimeter} \times r\]",
 why_rows=[("1", "Half the ratio."), ("2", "Not 0.24π."), ("4", "Not 0.24π.")])

P.qa(11, r"A straight road connects points A and B. Car 1 travels from A to B and Car 2 travels from B to A, both leaving at the same time. After meeting each other, they take \(45\) minutes and \(20\) minutes, respectively, to complete their journeys. If Car 1 travels at the speed of \(60\) km/hr, then the speed of Car 2, in km/hr, is",
 M("90", "70", "100", "80"), "MCQ", "1", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "After meeting, each car covers what the other covered before.",
 steps(("Speed ratio", p(r"\(\dfrac{v_1}{v_2}\) \(= \sqrt{\dfrac{t_2}{t_1}}\) \(= \sqrt{\dfrac{20}{45}}\) \(= \dfrac23\).")),
       ("Car 2", p(r"\(60 \times \tfrac32 = 90\)."))) + final(r"\(90\), option 1"),
 concept=r"\[\frac{v_1}{v_2} = \sqrt{\frac{t_2}{t_1}}\]",
 why_rows=[("2", "Not 1.5 × 60."), ("3", "Not 1.5 × 60."), ("4", "Not 1.5 × 60.")])

P.qa(12, r"A person spent ₹\(50000\) to purchase a desktop computer and a laptop computer. He sold the desktop at \(20\%\) profit and the laptop at \(10\%\) loss. If overall he made a \(2\%\) profit then the purchase price, in rupees, of the desktop is",
 [], "TITA", "20000", ["Arithmetic::Profit_Loss_and_Discount", "Arithmetic::Mixture_and_Alligation"], "Easy",
 "Alligation: +20% and −10% averaging to +2%.",
 steps(("Ratio", p(r"Desktop : laptop \(= (2 + 10) : (20 - 2)\) \(= 12 : 18 = 2 : 3\).")),
       ("Desktop", p(r"\(\tfrac25 \times 50000 = 20000\)."))) + final(r"\(20000\)"),
 concept=r"\[\frac{q_1}{q_2} = \frac{c_2 - c}{c - c_1}\]")

P.qa(13, r"A solution, of volume \(40\) litres, has dye and water in the proportion \(2 : 3\). Water is added to the solution to change this proportion to \(2 : 5\). If one-fourths of this diluted solution is taken out, how many litres of dye must be added to the remaining solution to bring the proportion back to \(2 : 3\)?",
 [], "TITA", "8", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Track dye and water separately.",
 steps(("Diluting", p("16 dye, 24 water; water rises to 40. Total 56.")),
       ("Removing a quarter", p("12 dye and 30 water remain.")),
       ("Back to 2 : 3", p("30 water needs 20 dye: add 8."))) + final(r"\(8\)"),
 concept=p("Water is the quantity that stays fixed when dye is added, so build the target ratio around it."))

P.qa(14, r"If \(x = (4096)^{7 + 4\sqrt3}\), then which of the following equals \(64\)?",
 M(r"\dfrac{x^{7/2}}{x^{2\sqrt3}}", r"\dfrac{x^7}{x^{2\sqrt3}}", r"\dfrac{x^7}{x^{4\sqrt3}}", r"\dfrac{x^{7/2}}{x^{4/\sqrt3}}"), "MCQ", "1", ["Algebra::Logarithms_and_Exponents", "Algebra::Surds_and_Indices"], "Medium",
 r"\(64 = 4096^{1/2}\), and \((7 + 4\sqrt3)(7 - 4\sqrt3) = 1\).",
 steps(("What we need", p(r"\(64 = 4096^{1/2}\), so we need \(x^k\) with \(k(7 + 4\sqrt3) = \tfrac12\), that is \(k\) \(= \tfrac12(7 - 4\sqrt3)\) \(= \tfrac72 - 2\sqrt3\).")),
       ("Matching", p(r"\(\dfrac{x^{7/2}}{x^{2\sqrt3}}\) \(= x^{7/2 - 2\sqrt3}\)."))) + final("Option 1"),
 concept=r"\[(a + \sqrt b)(a - \sqrt b) = a^2 - b\]",
 why_rows=[("2", "The exponent doesn’t simplify to a half."), ("3", "Gives 4096¹ = 4096, not 64."), ("4", "The exponent doesn’t simplify.")])

P.qa(15, r"An alloy is prepared by mixing three metals A, B and C in the proportion \(3 : 4 : 7\) by volume. Weights of the same volume of the metals A, B and C are in the ratio \(5 : 2 : 6\). In \(130\) kg of the alloy, the weight, in kg, of the metal C is",
 M("84", "70", "48", "96"), "MCQ", "1", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Weight = volume × density.",
 steps(("Weights", p(r"\(3 \times 5 : 4 \times 2 : 7 \times 6\) \(= 15 : 8 : 42\), total 65.")),
       ("C", p(r"\(\tfrac{42}{65} \times 130 = 84\)."))) + final(r"\(84\), option 1"),
 concept=r"\[\text{weight} = \text{volume} \times \text{density}\]",
 why_rows=[("2", "Uses volumes alone."), ("3", "Not 42/65 of 130."), ("4", "Not 42/65 of 130.")])

P.qa(16, r"The number of distinct real roots of the equation \(\left(x + \dfrac1x\right)^2 - 3\left(x + \dfrac1x\right) + 2 = 0\) equals",
 [], "TITA", "1", ["Algebra::Quadratic_Equations"], "Easy",
 r"Put \(t = x + \tfrac1x\). For real \(x\), \(|t| \ge 2\).",
 steps(("Solving for t", p(r"\(t^2 - 3t + 2 = 0\): \(t = 1\) or \(2\).")),
       ("Back to x", p(r"\(t = 1\) is impossible for real \(x\). \(t = 2\) gives \(x = 1\). One root."))) + final(r"\(1\)"),
 concept=r"\[x + \frac1x \ge 2 \text{ or } \le -2 \text{ for real } x\]")

P.qa(17, r"If \(2\log_4 5 = (\log_4 y)(\log_6 \sqrt5)\), then \(y\) equals",
 [], "TITA", "1296", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Write everything with common logs.",
 steps(("Rewriting", p(r"\(\dfrac{2\log 5}{\log 4}\) \(= \dfrac{\log y}{\log 4} \cdot \dfrac{\tfrac12\log 5}{\log 6}\).")),
       ("Solving", p(r"\(2 = \dfrac{\log y}{2\log 6}\), so \(\log y = 4\log 6\) and \(y = 6^4 = 1296\)."))) + final(r"\(1296\)"),
 concept=r"\[\log_b x = \frac{\log x}{\log b}\]")

P.qa(18, r"Leaving home at the same time, Amal reaches office at \(10{:}15\) am if he travels at \(8\) km/hr, and at \(9{:}40\) am if he travels at \(15\) km/hr. Leaving home at \(9{:}10\) am, at what speed, in km/hr, must he travel so as to reach office exactly at \(10\) am?",
 M("14", "12", "13", "11"), "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "The two times differ by 35 minutes.",
 steps(("Distance", p(r"\(\tfrac d8 - \tfrac d{15} = \tfrac{35}{60}\), so \(d = 10\) km.")),
       ("Speed", p("He needs 10 km in 50 minutes: 12 km/hr."))) + final(r"\(12\), option 2"),
 concept=r"\[\frac{d}{v_1} - \frac{d}{v_2} = \text{time difference}\]",
 why_rows=[("1", "Too fast."), ("3", "Too fast."), ("4", "Too slow.")])

P.qa(19, r"A train travelled at one-thirds of its usual speed, and hence reached the destination \(30\) minutes after the scheduled time. On its return journey, the train initially travelled at its usual speed for \(5\) minutes but then stopped for \(4\) minutes for an emergency. The percentage by which the train must now increase its usual speed so as to reach the destination at the scheduled time, is nearest to",
 M("58", "67", "50", "61"), "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Find the usual journey time first.",
 steps(("Usual time", p(r"\(3T = T + 30\), so \(T = 15\) minutes.")),
       ("Return", p("After 5 minutes it has covered a third of the way; the stop uses 4 more. The other two-thirds (normally 10 minutes) must take 6.")),
       ("Increase", p(r"Speed must be \(\tfrac{10}{6}\) times usual: about 67% more."))) + final(r"\(67\), option 2"),
 concept=r"\[\text{speed} \propto \frac{1}{\text{time}} \text{ for a fixed distance}\]",
 why_rows=[("1", "Not 10/6."), ("3", "Not 10/6."), ("4", "Not 10/6.")])

P.qa(20, r"The mean of all \(4\)-digit even natural numbers of the form ‘\(aabb\)’, where \(a > 0\), is",
 M("4864", "5050", "5544", "4466"), "MCQ", "3", ["Number_System::Miscellaneous"], "Easy",
 r"\(\overline{aabb} = 1100a + 11b\), with \(b\) even.",
 steps(("Averages", p(r"\(a\) averages 5 (1 to 9); \(b\) averages 4 (0, 2, 4, 6, 8).")),
       ("Mean", p(r"\(1100 \times 5 + 11 \times 4 = 5544\)."))) + final(r"\(5544\), option 3"),
 concept=p("The mean of a linear expression is the expression evaluated at the means."),
 why_rows=[("1", "Not 5500 + 44."), ("2", "Not 5500 + 44."), ("4", "Digits reversed.")])

P.qa(21, r"Two persons are walking beside a railway track at respective speeds of \(2\) and \(4\) km per hour in the same direction. A train came from behind them and crossed them in \(90\) and \(100\) seconds, respectively. The time, in seconds, taken by the train to cross an electric post is nearest to",
 M("78", "87", "75", "82"), "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "The train’s length is the same in both crossings.",
 steps(("Speed", p(r"\((v - 2) \times 90 = (v - 4) \times 100\), so \(v = 22\) km/hr.")),
       ("Length", p(r"\(20 \times \tfrac{90}{3600} = 0.5\) km.")),
       ("Post", p(r"\(\tfrac{0.5}{22}\) hours ≈ 81.8 seconds."))) + final(r"\(82\), option 4"),
 concept=r"\[\text{same direction: relative speed} = v_{\text{train}} - v_{\text{person}}\]",
 why_rows=[("1", "Too short."), ("2", "Too long."), ("3", "Too short.")])

P.qa(22, r"If \(a, b\) and \(c\) are positive integers such that \(ab = 432\), \(bc = 96\) and \(c < 9\), then the smallest possible value of \(a + b + c\) is",
 M("46", "56", "49", "59"), "MCQ", "1", ["Number_System::Factors_and_Divisibility"], "Easy",
 r"\(b\) divides both 432 and 96, and \(c = \tfrac{96}{b} < 9\).",
 steps(("Possible b", p(r"\(b\) divides 48 and \(b > 10\): 12, 16, 24 or 48.")),
       ("Sums", p("b = 12: 36 + 12 + 8 = 56. b = 16: 27 + 16 + 6 = 49. b = 24: 18 + 24 + 4 = 46. b = 48: 9 + 48 + 2 = 59."))) + final(r"\(46\), option 1"),
 concept=p("List the cases allowed by divisibility and compare."),
 why_rows=[("2", "b = 12."), ("3", "b = 16."), ("4", "b = 48.")])

P.qa(23, r"In a group of people, \(28\%\) of the members are young while the rest are old. If \(65\%\) of the members are literates, and \(25\%\) of the literates are young, then the percentage of old people among the illiterates is nearest to",
 M("59", "55", "62", "66"), "MCQ", "4", ["Arithmetic::Percentages"], "Easy",
 "Take 100 people and fill a 2 × 2 table.",
 steps(("Table", p("Literate 65: young 16.25, old 48.75. Illiterate 35: young 11.75, old 23.25.")),
       ("Percentage", p(r"\(\tfrac{23.25}{35} \approx 66\%\)."))) + final(r"\(66\), option 4"),
 concept=p("A two-way table keeps overlapping percentages straight."),
 why_rows=[("1", "Too low."), ("2", "Too low."), ("3", "Too low.")])

P.qa(24, r"Veeru invested ₹\(10000\) at \(5\%\) simple annual interest, and exactly after two years, Joy invested ₹\(8000\) at \(10\%\) simple annual interest. How many years after Veeru’s investment, will their balances, i.e., principal plus accumulated interest, be equal?",
 [], "TITA", "12", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Compare balances when Joy starts, then the yearly gain.",
 steps(("At year 2", p("Veeru has ₹11,000; Joy starts with ₹8,000. Gap ₹3,000.")),
       ("Closing the gap", p(r"Joy gains ₹800 a year, Veeru ₹500: ₹300 a year closes the gap in 10 years, which is 12 years after Veeru’s start."))) + final(r"\(12\)"),
 concept=r"\[\text{simple interest grows by a fixed amount each year}\]")

P.qa(25, r"If \(f(5 + x) = f(5 - x)\) for every real \(x\), and \(f(x) = 0\) has four distinct real roots, then the sum of these roots is",
 M("40", "10", "20", "0"), "MCQ", "3", ["Algebra::Functions"], "Easy",
 r"The graph is symmetric about \(x = 5\).",
 steps(("Pairs", p(r"Roots come in pairs \(5 + a\) and \(5 - a\), each pair adding to 10.")),
       ("Sum", p("Two pairs: 20."))) + final(r"\(20\), option 3"),
 concept=r"\[f(a + x) = f(a - x) \Rightarrow \text{symmetric about } x = a\]",
 why_rows=[("1", "Four times 10."), ("2", "One pair only."), ("4", "Symmetry about 0, not 5.")])

P.qa(26, r"Let A, B and C be three positive integers such that the sum of A and the mean of B and C is \(5\). In addition, the sum of B and the mean of A and C is \(7\). Then the sum of A and B is",
 M("6", "7", "5", "4"), "MCQ", "1", ["Algebra::Linear_Equations"], "Easy",
 r"\(2A + B + C = 10\) and \(A + 2B + C = 14\).",
 steps(("Subtracting", p(r"\(B - A = 4\).")),
       ("Positive integers", p(r"A = 1, B = 5 gives C = 3, which works. A = 2, B = 6 gives C = 0, not allowed. So A + B = 6."))) + final(r"\(6\), option 1"),
 concept=p("With fewer equations than unknowns, the integer condition picks the answer."),
 why_rows=[("2", "Not possible with positive integers."), ("3", "Not possible."), ("4", "Not possible.")])
