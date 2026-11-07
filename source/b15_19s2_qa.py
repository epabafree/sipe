# -*- coding: utf-8 -*-
# Batch 15 — CAT 2019 Slot 2: QA (33 of 34; Q3 isn't in the source).
from fmt import steps, final, trap, why, table, p
from b15_19s2 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"The average of \(30\) integers is \(5\). Among these \(30\) integers, there are exactly \(20\) which do not exceed \(5\). What is the highest possible value of the average of these \(20\) integers?",
 M("3.5", "5", "4.5", "4"), "MCQ", "3", ["Arithmetic::Average"], "Medium",
 "The other 10 are at least 6 each.",
 steps(("Bound", p(r"Total 150. The other ten add up to at least 60, so the twenty add up to at most 90.")),
       ("Average", p(r"\(90 \div 20 = 4.5\)."))) + final(r"\(4.5\), option 3"),
 why_rows=[("1", "Not the highest."), ("2", "Would need the others to be 5 too."), ("4", "Not the highest.")])

P.qa(2, r"Amal invests Rs \(12000\) at \(8\%\) interest, compounded annually, and Rs \(10000\) at \(6\%\) interest, compounded semi-annually, both investments being for one year. Bimal invests his money at \(7.5\%\) simple interest for one year. If Amal and Bimal get the same amount of interest, then the amount, in Rupees, invested by Bimal is",
 [], "TITA", "20920", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Semi-annual 6% is 3% twice.",
 steps(("Amal", p(r"\(960 + 10000(1.03^2 - 1)\) \(= 960 + 609 = 1569\).")),
       ("Bimal", p(r"\(1569 \div 0.075 = 20920\)."))) + final(r"\(20920\)"))

P.qa(4, r"How many pairs \((m, n)\) of positive integers satisfy the equation \(m^2 + 105 = n^2\)?",
 [], "TITA", "4", ["Number_System::Factors_and_Divisibility"], "Easy",
 r"\((n - m)(n + m) = 105\).",
 steps(("Factor pairs", p("1 × 105, 3 × 35, 5 × 21, 7 × 15. Each gives positive m and n.")),
       ("Count", p("4."))) + final(r"\(4\)"),
 concept=r"\[n^2 - m^2 = (n - m)(n + m)\]")

P.qa(5, r"Two ants A and B start from a point P on a circle at the same time, with A moving clock-wise and B moving anti-clockwise. They meet for the first time at 10:00 am when A has covered \(60\%\) of the track. If A returns to P at 10:12 am, then B returns to P at",
 ["10:25 am", "10:45 am", "10:18 am", "10:27 am"], "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "A covers the last 40% in 12 minutes.",
 steps(("Start", p("A takes 18 minutes for 60%, so they started at 9:42.")),
       ("B", p("B covered 40% in 18 minutes, so the remaining 60% takes 27: back at 10:27."))) + final("10:27 am, option 4"),
 why_rows=[("1", "Wrong rate."), ("2", "Wrong rate."), ("3", "Wrong rate.")])

P.qa(6, r"Let \(a_1, a_2, \dots\) be integers such that \(a_1 - a_2 + a_3 - a_4\) \(+ \dots + (-1)^{n-1}a_n = n\), for all \(n \ge 1\). Then \(a_{51} + a_{52} + \dots + a_{1023}\) equals",
 M("0", "1", "10", "-1"), "MCQ", "2", ["Algebra::Progressions_and_Series"], "Medium",
 r"Subtract the condition for \(n - 1\) from the one for \(n\).",
 steps(("Each term", p(r"\((-1)^{n-1}a_n = 1\), so odd terms are 1 and even terms −1.")),
       ("Sum", p("From 51 to 1023 there are 487 odd and 486 even terms: 1."))) + final(r"\(1\), option 2"),
 why_rows=[("1", "Pairs up all but one term."), ("3", "No basis."), ("4", "Sign error.")])

P.qa(7, r"Two circles, each of radius \(4\) cm, touch externally. Each of these two circles is touched externally by a third circle. If these three circles have a common tangent, then the radius of the third circle, in cm, is",
 M(r"\tfrac{1}{\sqrt2}", r"\tfrac{\pi}{3}", r"\sqrt2", "1"), "MCQ", "4", ["Geometry::Circles"], "Hard",
 "The small circle sits in the gap between the two big ones, on the same line.",
 steps(("Set-up", p(r"Centres of the big circles: \((\pm4, 4)\). Small circle centre \((0, r)\).")),
       ("Touching", p(r"\(16 + (4 - r)^2 = (4 + r)^2\), so \(16 = 16r\) and \(r = 1\)."))) + final(r"\(1\), option 4"),
 concept=r"\[\frac{1}{\sqrt{r_3}} = \frac{1}{\sqrt{r_1}} + \frac{1}{\sqrt{r_2}}\]",
 why_rows=[("1", "Too small."), ("2", "No basis."), ("3", "Too big.")])

P.qa(8, r"Let A be a real number. Then the roots of the equation \(x^2 - 4x - \log_2 A = 0\) are real and distinct if and only if",
 M(r"A > \tfrac{1}{16}", r"A < \tfrac{1}{16}", r"A < \tfrac18", r"A > \tfrac18"), "MCQ", "1", ["Algebra::Quadratic_Equations", "Algebra::Logarithms_and_Exponents"], "Easy",
 "The discriminant must be positive.",
 steps(("Discriminant", p(r"\(16 + 4\log_2 A > 0\), so \(\log_2 A > -4\) and \(A > \tfrac1{16}\)."))) + final("Option 1"),
 why_rows=[("2", "Reversed."), ("3", "Wrong bound."), ("4", "Too strict.")])

P.qa(9, r"The quadratic equation \(x^2 + bx + c = 0\) has two roots \(4a\) and \(3a\), where \(a\) is an integer. Which of the following is a possible value of \(b^2 + c\)?",
 M("3721", "361", "427", "549"), "MCQ", "4", ["Algebra::Quadratic_Equations"], "Easy",
 "Sum and product of the roots.",
 steps(("b and c", p(r"\(b = -7a\), \(c = 12a^2\), so \(b^2 + c = 61a^2\).")),
       ("Check", p(r"\(549 = 61 \times 9\), with \(a = 3\)."))) + final(r"\(549\), option 4"),
 why_rows=[("1", r"\(3721 = 61^2\), so \(a^2\) would be 61."), ("2", "Not a multiple of 61."), ("3", "61 × 7, and 7 isn’t a square.")])

P.qa(10, r"The base of a regular pyramid is a square and each of the other four sides is an equilateral triangle, length of each side being \(20\) cm. The vertical height of the pyramid, in cm, is",
 M("12", r"10\sqrt2", r"8\sqrt3", r"5\sqrt5"), "MCQ", "2", ["Geometry::Mensuration"], "Easy",
 "The apex is above the centre of the square.",
 steps(("Half-diagonal", p(r"\(10\sqrt2\).")),
       ("Height", p(r"\(\sqrt{400 - 200} = 10\sqrt2\)."))) + final(r"\(10\sqrt2\), option 2"),
 why_rows=[("1", "Too short."), ("3", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(11, r"Let ABC be a right-angled triangle with hypotenuse BC of length \(20\) cm. If AP is perpendicular on BC, then the maximum possible length of AP, in cm, is",
 M("10", "5", r"8\sqrt2", r"6\sqrt2"), "MCQ", "1", ["Geometry::Triangles"], "Easy",
 "A lies on the circle with BC as diameter.",
 steps(("Largest height", p("The highest point of that circle is a radius, 10, above BC."))) + final(r"\(10\), option 1"),
 why_rows=[("2", "Half the maximum."), ("3", "More than the radius."), ("4", "Less than the maximum.")])

P.qa(12, r"If \(x\) is a real number, then \(\sqrt{\log_e \dfrac{4x - x^2}{3}}\) is a real number if and only if",
 M(r"1 \le x \le 3", r"1 \le x \le 2", r"-1 \le x \le 3", r"-3 \le x \le 3"), "MCQ", "1", ["Algebra::Logarithms_and_Exponents", "Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "The log must be at least 0.",
 steps(("Condition", p(r"\(\tfrac{4x - x^2}{3} \ge 1\), so \(x^2 - 4x + 3 \le 0\): \(1 \le x \le 3\)."))) + final("Option 1"),
 why_rows=[("2", "Too narrow."), ("3", "Includes values where the log is negative."), ("4", "Too wide.")])

P.qa(13, r"If \(5^x - 3^y = 13438\) and \(5^{x-1} + 3^{y+1} = 9686\), then \(x + y\) equals",
 [], "TITA", "13", ["Algebra::Surds_and_Indices"], "Medium",
 r"Let \(a = 5^x\), \(b = 3^y\).",
 steps(("Equations", p(r"\(a - b = 13438\) and \(a + 15b = 48430\), so \(16b = 34992\).")),
       ("Values", p(r"\(b = 2187 = 3^7\), \(a = 15625 = 5^6\). So \(x + y = 13\)."))) + final(r"\(13\)"))

P.qa(14, r"The strength of a salt solution is \(p\%\) if \(100\) ml of the solution contains \(p\) grams of salt. Each of three vessels A, B, C contains \(500\) ml of salt solution of strengths \(10\%\), \(22\%\), and \(32\%\), respectively. Now, \(100\) ml of the solution in vessel A is transferred to vessel B. Then, \(100\) ml of the solution in vessel B is transferred to vessel C. Finally, \(100\) ml of the solution in vessel C is transferred to vessel A. The strength, in percentage, of the resulting solution in vessel A is",
 M("15", "13", "12", "14"), "MCQ", "4", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Track grams of salt.",
 steps(("B", p("110 + 10 = 120 g in 600 ml: 20%.")),
       ("C", p("160 + 20 = 180 g in 600 ml: 30%.")),
       ("A", p("40 + 30 = 70 g in 500 ml: 14%."))) + final(r"\(14\), option 4"),
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("3", "Doesn’t fit.")])

P.qa(15, r"A cyclist leaves A at 10 a.m. and reaches B at 11 a.m. Starting from 10:01 a.m., every minute a motorcycle leaves A and moves towards B. Forty-five such motorcycles reach B by 11 a.m. All motorcycles have the same speed. If the cyclist had doubled his speed, how many motorcycles would have reached B by the time the cyclist reached B?",
 M("22", "23", "15", "20"), "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "How long does one motorcycle take?",
 steps(("Motorcycle time", p("The 45th left at 10:45 and arrived by 11:00: 15 minutes.")),
       ("Faster cyclist", p("He reaches at 10:30. Motorcycles leaving by 10:15 arrive by then: 15."))) + final(r"\(15\), option 3"),
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(16, r"A man makes complete use of \(405\) cc of iron, \(783\) cc of aluminium, and \(351\) cc of copper to make a number of solid right circular cylinders of each type of metal. These cylinders have the same volume and each of these has radius \(3\) cm. If the total number of cylinders is to be kept at a minimum, then the total surface area of all these cylinders, in sq cm, is",
 M(r"1026(1 + \pi)", r"8464\pi", r"928\pi", r"1044(4 + \pi)"), "MCQ", "1", ["Geometry::Mensuration", "Number_System::Factors_and_Divisibility"], "Hard",
 "Largest common volume: the HCF.",
 steps(("Volume", p(r"HCF of 405, 783, 351 is 27, giving 15 + 29 + 13 = 57 cylinders.")),
       ("One cylinder", p(r"\(9\pi h = 27\), so \(h = \tfrac3\pi\). Surface \(18\pi + 6\pi \cdot \tfrac3\pi = 18(\pi + 1)\).")),
       ("Total", p(r"\(57 \times 18(1 + \pi) = 1026(1 + \pi)\)."))) + final("Option 1"),
 why_rows=[("2", "Wrong surface formula."), ("3", "Wrong surface formula."), ("4", "Wrong count.")])

P.qa(17, r"The real root of the equation \(2^{6x} + 2^{3x+2} - 21 = 0\) is",
 M(r"\log_2 9", r"\tfrac{\log_2 3}{3}", r"\log_3 27", r"\log_2 \tfrac73"), "MCQ", "2", ["Algebra::Logarithms_and_Exponents", "Algebra::Quadratic_Equations"], "Easy",
 r"Let \(t = 2^{3x}\).",
 steps(("Quadratic", p(r"\(t^2 + 4t - 21 = 0\), so \(t = 3\) (t is positive).")),
       ("x", p(r"\(3x = \log_2 3\)."))) + final("Option 2"),
 why_rows=[("1", "Too large."), ("3", "Equals 3."), ("4", "Not a root.")])

P.qa(18, r"How many factors of \(2^4 \times 3^5 \times 10^4\) are perfect squares which are greater than \(1\)?",
 [], "TITA", "44", ["Number_System::Factors_and_Divisibility"], "Easy",
 r"The number is \(2^8 \times 3^5 \times 5^4\).",
 steps(("Even exponents", p(r"5 choices for 2, 3 for 3, 3 for 5: 45 square factors.")),
       ("Exclude 1", p("44."))) + final(r"\(44\)"))

P.qa(19, r"In a six-digit number, the sixth, that is, the rightmost, digit is the sum of the first three digits, the fifth digit is the sum of first two digits, the third digit is equal to the first digit, the second digit is twice the first digit and the fourth digit is the sum of fifth and sixth digits. Then, the largest possible value of the fourth digit is",
 [], "TITA", "7", ["Number_System::Miscellaneous"], "Easy",
 r"Write every digit in terms of the first, \(d\).",
 steps(("Digits", p(r"\(d, 2d, d, 7d, 3d, 4d\).")),
       ("Largest", p(r"\(7d \le 9\) forces \(d = 1\): 121734. The fourth digit is 7."))) + final(r"\(7\)"))

P.qa(20, r"John jogs on track A at \(6\) kmph and Mary jogs on track B at \(7.5\) kmph. The total length of tracks A and B is \(325\) metres. While John makes \(9\) rounds of track A, Mary makes \(5\) rounds of track B. In how many seconds will Mary make one round of track A?",
 [], "TITA", "48", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Same time for both: distance ÷ speed.",
 steps(("Lengths", p(r"\(\tfrac{9A}{6} = \tfrac{5B}{7.5}\), so \(B = 2.25A\) and \(A = 100\) m.")),
       ("Time", p(r"7.5 kmph is \(\tfrac{25}{12}\) m/s, so 100 m takes 48 s."))) + final(r"\(48\)"))

P.qa(21, r"In 2010, a library contained a total of \(11500\) books in two categories – fiction and nonfiction. In 2015, the library contained a total of \(12760\) books in these two categories. During this period, there was \(10\%\) increase in the fiction category while there was \(12\%\) increase in the nonfiction category. How many fiction books were in the library in 2015?",
 M("6160", "6600", "6000", "5500"), "MCQ", "2", ["Arithmetic::Percentages"], "Easy",
 "If both grew 10%, there would be 12650.",
 steps(("Nonfiction", p(r"The extra 110 is 2% of nonfiction, so 5500; fiction 6000.")),
       ("2015", p(r"\(6000 \times 1.1 = 6600\)."))) + final(r"\(6600\), option 2"),
 why_rows=[("1", "Nonfiction’s growth."), ("3", "The 2010 figure."), ("4", "Nonfiction in 2010.")])

P.qa(22, r"John gets Rs \(57\) per hour of regular work and Rs \(114\) per hour of overtime work. He works altogether \(172\) hours and his income from overtime hours is \(15\%\) of his income from regular hours. Then, for how many hours did he work overtime?",
 [], "TITA", "12", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Overtime pays twice as much an hour.",
 steps(("Hours", p(r"\(114o = 0.15 \times 57r\), so \(r = \tfrac{40}{3}o\). With \(r + o = 172\): \(o = 12\)."))) + final(r"\(12\)"))

P.qa(23, r"If \((2n + 1) + (2n + 3)\) \(+ (2n + 5) + \dots\) \(+ (2n + 47) = 5280\), then what is the value of \(1 + 2 + 3 + \dots + n\)?",
 [], "TITA", "4851", ["Algebra::Progressions_and_Series"], "Easy",
 "24 terms.",
 steps(("Sum", p(r"\(48n + (1 + 3 + \dots + 47)\) \(= 48n + 576 = 5280\), so \(n = 98\).")),
       ("Answer", p(r"\(\tfrac{98 \times 99}{2} = 4851\)."))) + final(r"\(4851\)"))

P.qa(24, r"A shopkeeper sells two tables, each procured at cost price \(p\), to Amal and Asim at a profit of \(20\%\) and at a loss of \(20\%\), respectively. Amal sells his table to Bimal at a profit of \(30\%\), while Asim sells his table to Barun at a loss of \(30\%\). If the amounts paid by Bimal and Barun are \(x\) and \(y\), respectively, then \(\tfrac{x - y}{p}\) equals",
 M("1", "1.2", "0.50", "0.7"), "MCQ", "1", ["Arithmetic::Profit_Loss_and_Discount"], "Easy",
 "Chain the percentages.",
 steps(("Prices", p(r"\(x = 1.2 \times 1.3p = 1.56p\), \(y = 0.8 \times 0.7p = 0.56p\).")),
       ("Ratio", p("1."))) + final(r"\(1\), option 1"),
 why_rows=[("2", "Doesn’t fit."), ("3", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(25, r"In a triangle ABC, medians AD and BE are perpendicular to each other, and have lengths \(12\) cm and \(9\) cm, respectively. Then, the area of triangle ABC, in sq cm, is",
 M("78", "80", "72", "68"), "MCQ", "3", ["Geometry::Triangles"], "Medium",
 "Quadrilateral ABDE has perpendicular diagonals.",
 steps(("Area of ABDE", p(r"\(\tfrac12 \times 12 \times 9 = 54\).")),
       ("Whole triangle", p(r"ABDE is \(\tfrac34\) of ABC (the cut-off triangle CDE is a quarter), so ABC is 72."))) + final(r"\(72\), option 3"),
 concept=r"\[\text{Area} = \tfrac43 \times \tfrac12 \, m_1 m_2 \text{ when two medians are perpendicular}\]",
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(26, r"The number of common terms in the two sequences: \(15, 19, 23, 27, \dots, 415\) and \(14, 19, 24, 29, \dots, 464\) is",
 M("21", "20", "18", "19"), "MCQ", "2", ["Algebra::Progressions_and_Series"], "Medium",
 "The first common term is 19; then every 20.",
 steps(("Common terms", p(r"\(19, 39, 59, \dots\), up to 415.")),
       ("Count", p(r"\(19 + 20k \le 415\) gives \(k = 0\) to \(19\): 20 terms. The last is 399."))) + final(r"\(20\), option 2"),
 trap("Count from k = 0."),
 concept=p("Common terms of two APs form an AP whose difference is the LCM of the two differences."),
 why_rows=[("1", "One too many."), ("3", "Two too few."), ("4", "Misses the first or last.")])

P.qa(27, r"Let \(a, b, x, y\) be real numbers such that \(a^2 + b^2 = 81\), \(x^2 + y^2 = 121\), and \(ax + by = 99\). If \(k = ay - bx\), then",
 M(r"0 < k \le \tfrac{5}{13}", r"k > \tfrac{5}{13}", r"k = \tfrac{5}{13}", "k = 0"), "MCQ", "4", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Use the identity for (a² + b²)(x² + y²).",
 steps(("Identity", p(r"\((a^2 + b^2)(x^2 + y^2)\) \(= (ax + by)^2 + (ay - bx)^2\).")),
       ("Numbers", p(r"\(9801 = 9801 + k^2\), so \(k = 0\)."))) + final(r"\(k = 0\), option 4"),
 why_rows=[("1", "k² is zero."), ("2", "k² is zero."), ("3", "k² is zero.")])

P.qa(28, r"Mukesh purchased \(10\) bicycles in 2017, all at the same price. He sold six of these at a profit of \(25\%\) and the remaining four at a loss of \(25\%\). If he made a total profit of Rs \(2000\), then his purchase price of a bicycle, in Rupees, was",
 M("6000", "8000", "4000", "2000"), "MCQ", "3", ["Arithmetic::Profit_Loss_and_Discount"], "Easy",
 "Net gain is 6 × 25% − 4 × 25% of one bicycle.",
 steps(("Profit", p(r"\(0.5p = 2000\), so \(p = 4000\)."))) + final(r"\(4000\), option 3"),
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(29, r"In an examination, the score of A was \(10\%\) less than that of B, the score of B was \(25\%\) more than that of C, and the score of C was \(20\%\) less than that of D. If A scored \(72\), then the score of D was",
 [], "TITA", "80", ["Arithmetic::Percentages"], "Easy",
 "Chain the multipliers.",
 steps(("Chain", p(r"\(A = 0.9 \times 1.25 \times 0.8 D = 0.9D\), so \(D = 80\)."))) + final(r"\(80\)"))

P.qa(30, r"The salaries of Ramesh, Ganesh and Rajesh were in the ratio \(6 : 5 : 7\) in 2010, and in the ratio \(3 : 4 : 3\) in 2015. If Ramesh’s salary increased by \(25\%\) during 2010-2015, then the percentage increase in Rajesh’s salary during this period is closest to",
 M("10", "7", "9", "8"), "MCQ", "2", ["Arithmetic::Ratio_and_Proportion", "Arithmetic::Percentages"], "Easy",
 "Fix Ramesh: 6 becomes 7.5.",
 steps(("2015", p("Ramesh 7.5 = 3 parts, so a part is 2.5 and Rajesh is 7.5.")),
       ("Rajesh", p(r"7 to 7.5 is about 7.1%."))) + final(r"\(7\), option 2"),
 why_rows=[("1", "Too high."), ("3", "Too high."), ("4", "Too high.")])

P.qa(31, r"Let A and B be two regular polygons having \(a\) and \(b\) sides, respectively. If \(b = 2a\) and each interior angle of B is \(\tfrac32\) times each interior angle of A, then each interior angle, in degrees, of a regular polygon with \(a + b\) sides is",
 [], "TITA", "150", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 r"Interior angle of an n-gon: \(180 - \tfrac{360}{n}\).",
 steps(("Equation", p(r"\(180 - \tfrac{180}{a} = \tfrac32\left(180 - \tfrac{360}{a}\right)\), so \(a = 4\), \(b = 8\).")),
       ("12-gon", p(r"\(180 - 30 = 150\)."))) + final(r"\(150\)"))

P.qa(32, r"Let \(f\) be a function such that \(f(mn) = f(m)f(n)\) for every positive integers \(m\) and \(n\). If \(f(1)\), \(f(2)\) and \(f(3)\) are positive integers, \(f(1) < f(2)\), and \(f(24) = 54\), then \(f(18)\) equals",
 [], "TITA", "12", ["Algebra::Functions"], "Medium",
 r"\(f(24) = f(2)^3 f(3)\).",
 steps(("Values", p(r"\(54 = 27 \times 2\), so \(f(2) = 3\), \(f(3) = 2\).")),
       ("f(18)", p(r"\(f(2)f(3)^2 = 12\)."))) + final(r"\(12\)"))

P.qa(33, r"Anil alone can do a job in \(20\) days while Sunil alone can do it in \(40\) days. Anil starts the job, and after \(3\) days, Sunil joins him. Again, after a few more days, Bimal joins them and they together finish the job. If Bimal has done \(10\%\) of the job, then in how many days was the job done?",
 M("12", "13", "15", "14"), "MCQ", "2", ["Arithmetic::Time_and_Work"], "Medium",
 "Anil and Sunil do 90% between them.",
 steps(("Equation", p(r"Over \(T\) days: \(\tfrac{T}{20} + \tfrac{T - 3}{40} = 0.9\), so \(3T - 3 = 36\) and \(T = 13\)."))) + final(r"\(13\), option 2"),
 why_rows=[("1", "Doesn’t fit."), ("3", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(34, r"In an examination, Rama’s score was one-twelfth of the sum of the scores of Mohan and Anjali. After a review, the score of each of them increased by \(6\). The revised scores of Anjali, Mohan, and Rama were in the ratio \(11 : 10 : 3\). Then Anjali’s score exceeded Rama’s score by",
 M("26", "32", "35", "24"), "MCQ", "2", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "Revised scores 11k, 10k, 3k.",
 steps(("Equation", p(r"\(3k - 6 = \tfrac{(11k - 6) + (10k - 6)}{12}\), so \(k = 4\).")),
       ("Difference", p(r"44 − 12 = 32 (the same before and after the review)."))) + final(r"\(32\), option 2"),
 why_rows=[("1", "Doesn’t fit."), ("3", "Doesn’t fit."), ("4", "Doesn’t fit.")])
