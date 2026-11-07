# -*- coding: utf-8 -*-
# Batch 14 — CAT 2019 Slot 1: QA (32 of 34).
from fmt import steps, final, trap, why, table, p
from b14_19s1 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"Two cars travel the same distance starting at 10:00 a.m. and 11:00 a.m., respectively, on the same day. They reach their common destination at the same point of time. If the first car travelled for at least \(6\) hours, then the highest possible value of the percentage by which the speed of the second car could exceed that of the first car is",
 M("20", "30", "25", "10"), "MCQ", "1", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 r"Speeds are in the inverse ratio of the times \(t\) and \(t - 1\).",
 steps(("Ratio", p(r"\(\tfrac{v_2}{v_1} = \tfrac{t}{t - 1}\), which shrinks as \(t\) grows.")),
       ("Largest", p(r"At \(t = 6\): \(\tfrac65\), so 20% faster."))) + final(r"\(20\), option 1"),
 why_rows=[("2", "Would need t below 6."), ("3", "Would need t = 5."), ("4", "Possible, but not the highest.")])

P.qa(2, r"If \(a_1, a_2, \dots\) are in A.P., then \(\dfrac{1}{\sqrt{a_1} + \sqrt{a_2}}\) \(+ \dfrac{1}{\sqrt{a_2} + \sqrt{a_3}}\) \(+ \dots\) \(+ \dfrac{1}{\sqrt{a_n} + \sqrt{a_{n+1}}}\) is equal to",
 M(r"\dfrac{n}{\sqrt{a_1} + \sqrt{a_{n+1}}}", r"\dfrac{n - 1}{\sqrt{a_1} + \sqrt{a_{n-1}}}", r"\dfrac{n - 1}{\sqrt{a_1} + \sqrt{a_n}}", r"\dfrac{n}{\sqrt{a_1} - \sqrt{a_{n+1}}}"), "MCQ", "1", ["Algebra::Progressions_and_Series", "Algebra::Surds_and_Indices"], "Medium",
 "Rationalise each term.",
 steps(("One term", p(r"\(\dfrac{1}{\sqrt{a_k} + \sqrt{a_{k+1}}} = \dfrac{\sqrt{a_{k+1}} - \sqrt{a_k}}{d}\), where \(d\) is the common difference.")),
       ("Telescoping", p(r"The sum is \(\dfrac{\sqrt{a_{n+1}} - \sqrt{a_1}}{d}\).")),
       ("Tidy", p(r"Multiply top and bottom by \(\sqrt{a_{n+1}} + \sqrt{a_1}\): the top becomes \(a_{n+1} - a_1 = nd\), giving \(\dfrac{n}{\sqrt{a_1} + \sqrt{a_{n+1}}}\)."))) + final("Option 1"),
 concept=p("Sums of 1/(√a + √b) over an AP telescope after rationalising."),
 why_rows=[("2", "Wrong count and last term."), ("3", "Stops one term early."), ("4", "Sign error in the denominator.")])

P.qa(3, r"AB is a diameter of a circle of radius \(5\) cm. Let P and Q be two points on the circle so that the length of PB is \(6\) cm, and the length of AP is twice that of AQ. Then the length, in cm, of QB is nearest to",
 M("9.3", "7.8", "9.1", "8.5"), "MCQ", "3", ["Geometry::Circles"], "Easy",
 "Angles in a semicircle are right angles.",
 steps(("AP", p(r"\(AP = \sqrt{100 - 36} = 8\), so \(AQ = 4\).")),
       ("QB", p(r"\(\sqrt{100 - 16} = \sqrt{84} \approx 9.17\)."))) + final(r"\(9.1\), option 3"),
 why_rows=[("1", "Too long."), ("2", "Too short."), ("4", "Too short.")])

P.qa(4, r"If \((5.55)^x = (0.555)^y = 1000\), then the value of \(\tfrac1x - \tfrac1y\) is",
 M(r"\tfrac13", "3", "1", r"\tfrac25"), "MCQ", "1", ["Algebra::Logarithms_and_Exponents"], "Easy",
 "Take logs to base 10.",
 steps(("Reciprocals", p(r"\(\tfrac1x = \tfrac{\log 5.55}{3}\), \(\tfrac1y = \tfrac{\log 0.555}{3}\).")),
       ("Difference", p(r"\(\tfrac{\log 5.55 - \log 0.555}{3} = \tfrac{\log 10}{3} = \tfrac13\)."))) + final(r"\(\tfrac13\), option 1"),
 why_rows=[("2", "Upside down."), ("3", "Forgets the 3 in 1000 = 10³."), ("4", "No basis.")])

P.qa(5, r"The income of Amala is \(20\%\) more than that of Bimala and \(20\%\) less than that of Kamala. If Kamala’s income goes down by \(4\%\) and Bimala’s goes up by \(10\%\), then the percentage by which Kamala’s income would exceed Bimala’s is nearest to",
 M("31", "29", "28", "32"), "MCQ", "1", ["Arithmetic::Percentages"], "Easy",
 "Take Bimala’s income as 100.",
 steps(("Incomes", p("Bimala 100, Amala 120, Kamala 150.")),
       ("After", p(r"Kamala 144, Bimala 110. \(\tfrac{144}{110} \approx 1.309\)."))) + final(r"\(31\), option 1"),
 why_rows=[("2", "Too low."), ("3", "Too low."), ("4", "Too high.")])

P.qa(6, r"The wheels of bicycles A and B have radii \(30\) cm and \(40\) cm, respectively. While traveling a certain distance, each wheel of A required \(5000\) more revolutions than each wheel of B. If bicycle B traveled this distance in \(45\) minutes, then its speed, in km per hour, was",
 M(r"18\pi", r"14\pi", r"16\pi", r"12\pi"), "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance", "Geometry::Mensuration"], "Medium",
 r"Circumferences \(60\pi\) and \(80\pi\) cm.",
 steps(("Distance", p(r"\(\tfrac{D}{60\pi} - \tfrac{D}{80\pi} = 5000\), so \(D = 1200000\pi\) cm \(= 12\pi\) km.")),
       ("Speed", p(r"\(12\pi \div 0.75 = 16\pi\)."))) + final(r"\(16\pi\), option 3"),
 why_rows=[("1", "Wrong distance."), ("2", "Wrong distance."), ("4", "Uses 1 hour.")])

P.qa(7, r"The product of the distinct roots of \(|x^2 - x - 6| = x + 2\) is",
 M("-16", "-4", "-24", "-8"), "MCQ", "1", ["Algebra::Inequalities_and_Absolute_Value", "Algebra::Quadratic_Equations"], "Medium",
 r"\(x^2 - x - 6 = (x - 3)(x + 2)\). Split by sign.",
 steps(("Outside (−2, 3)", p(r"\(x^2 - 2x - 8 = 0\): \(x = 4\) or \(-2\).")),
       ("Inside", p(r"\(-(x^2 - x - 6) = x + 2\) gives \(x^2 = 4\): \(x = 2\).")),
       ("Product", p(r"\(4 \times (-2) \times 2 = -16\)."))) + final(r"\(-16\), option 1"),
 why_rows=[("2", "Misses x = 4."), ("3", "Wrong roots."), ("4", "Misses x = 2.")])

P.qa(9, r"If the population of a town is \(p\) in the beginning of any year then it becomes \(3 + 2p\) in the beginning of the next year. If the population in the beginning of \(2019\) is \(1000\), then the population in the beginning of \(2034\) will be",
 M(r"(1003)^{15} + 6", r"(997)^{15} - 3", r"(997)2^{14} + 3", r"(1003)2^{15} - 3"), "MCQ", "4", ["Algebra::Progressions_and_Series"], "Medium",
 r"Look at \(p + 3\).",
 steps(("Doubling", p(r"\(p + 3\) doubles each year: \(1003 \to 2 \times 1003\), and so on.")),
       ("15 years", p(r"\(1003 \times 2^{15} - 3\)."))) + final("Option 4"),
 concept=p("For p → ap + b, shift by b/(a − 1); the shifted value grows geometrically."),
 why_rows=[("1", "Powers of the wrong number."), ("2", "Wrong shift."), ("3", "Wrong shift and power.")])

P.qa(10, r"Consider a function \(f\) satisfying \(f(x + y) = f(x)f(y)\) where \(x, y\) are positive integers, and \(f(1) = 2\). If \(f(a + 1) + f(a + 2)\) \(+ \dots + f(a + n)\) \(= 16(2^n - 1)\) then \(a\) is equal to",
 [], "TITA", "3", ["Algebra::Functions", "Algebra::Progressions_and_Series"], "Easy",
 r"\(f(n) = 2^n\).",
 steps(("Sum", p(r"\(2^{a+1} + \dots + 2^{a+n} = 2^{a+1}(2^n - 1)\).")),
       ("Match", p(r"\(2^{a+1} = 16\), so \(a = 3\)."))) + final(r"\(3\)"))

P.qa(11, r"Amala, Bina, and Gouri invest money in the ratio \(3 : 4 : 5\) in fixed deposits having respective annual interest rates in the ratio \(6 : 5 : 4\). What is their total interest income (in Rs) after a year, if Bina’s interest income exceeds Amala’s by Rs \(250\)?",
 M("6350", "6000", "7000", "7250"), "MCQ", "4", ["Arithmetic::Simple_and_Compound_Interest", "Arithmetic::Ratio_and_Proportion"], "Easy",
 "Multiply the two ratios.",
 steps(("Interest ratio", p("18 : 20 : 20.")),
       ("Scale", p("2 parts = 250, so a part is 125 and the total, 58 parts, is 7250."))) + final(r"\(7250\), option 4"),
 why_rows=[("1", "Not 58 parts."), ("2", "Not 58 parts."), ("3", "Not 58 parts.")])

P.qa(12, r"For any positive integer \(n\), let \(f(n) = n(n + 1)\) if \(n\) is even, and \(f(n) = n + 3\) if \(n\) is odd. If \(m\) is a positive integer such that \(8f(m + 1) - f(m) = 2\), then \(m\) equals",
 [], "TITA", "10", ["Algebra::Functions"], "Medium",
 "Try m even and m odd separately.",
 steps(("m odd", p(r"\(8(m + 1)(m + 2) - (m + 3) = 2\) has no positive solution.")),
       ("m even", p(r"\(8(m + 4) - m(m + 1) = 2\) gives \(m^2 - 7m - 30 = 0\), so \(m = 10\).")),
       ("Check", p(r"\(8 \times 14 - 110 = 2\)."))) + final(r"\(10\)"))

P.qa(13, r"The product of two positive numbers is \(616\). If the ratio of the difference of their cubes to the cube of their difference is \(157 : 3\), then the sum of the two numbers is",
 M("58", "85", "50", "95"), "MCQ", "3", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Cancel one factor of (a − b).",
 steps(("Simplify", p(r"\(\dfrac{a^2 + ab + b^2}{(a - b)^2} = \dfrac{157}{3}\). With \(d = (a - b)^2\), the top is \(d + 3 \times 616\).")),
       ("Solve", p(r"\(3d + 5544 = 157d\), so \(d = 36\).")),
       ("Sum", p(r"\((a + b)^2 = 36 + 4 \times 616 = 2500\), so \(a + b = 50\)."))) + final(r"\(50\), option 3"),
 concept=r"\[(a + b)^2 = (a - b)^2 + 4ab\]",
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(14, r"One can use three different transports which move at \(10\), \(20\), and \(30\) kmph, respectively. To reach from A to B, Amal took each mode of transport \(\tfrac13\) of his total journey time, while Bimal took each mode of transport \(\tfrac13\) of the total distance. The percentage by which Bimal’s travel time exceeds Amal’s travel time is nearest to",
 M("22", "20", "19", "21"), "MCQ", "1", ["Arithmetic::Time_Speed_and_Distance", "Arithmetic::Average"], "Medium",
 "Equal times: arithmetic mean. Equal distances: harmonic mean.",
 steps(("Average speeds", p(r"Amal 20. Bimal \(\dfrac{3}{\tfrac1{10} + \tfrac1{20} + \tfrac1{30}} = \tfrac{180}{11}\).")),
       ("Ratio", p(r"\(20 \div \tfrac{180}{11} = \tfrac{11}{9} \approx 1.222\)."))) + final(r"\(22\), option 1"),
 why_rows=[("2", "Too low."), ("3", "Too low."), ("4", "Too low.")])

P.qa(15, r"Meena scores \(40\%\) in an examination and after review, even though her score is increased by \(50\%\), she fails by \(35\) marks. If her post-review score is increased by \(20\%\), she will have \(7\) marks more than the passing score. The percentage score needed for passing the examination is",
 M("60", "80", "70", "75"), "MCQ", "3", ["Arithmetic::Percentages"], "Medium",
 "Her post-review score is 60% of the total.",
 steps(("Equations", p(r"Pass mark \(= 0.6M + 35 = 0.72M - 7\), so \(M = 350\).")),
       ("Pass", p(r"\(245\) out of 350: 70%."))) + final(r"\(70\), option 3"),
 why_rows=[("1", "Her post-review score."), ("2", "Too high."), ("4", "Too high.")])

P.qa(16, r"A person invested a total amount of Rs \(15\) lakh. A part of it was invested in a fixed deposit earning \(6\%\) annual interest, and the remaining amount was invested in two other deposits in the ratio \(2 : 1\), earning annual interest at the rates of \(4\%\) and \(3\%\), respectively. If the total annual interest income is Rs \(76000\), then the amount (in Rs lakh) invested in the fixed deposit was",
 [], "TITA", "9", ["Arithmetic::Simple_and_Compound_Interest", "Arithmetic::Mixture_and_Alligation"], "Medium",
 r"The other two deposits earn \(\tfrac{2(4) + 1(3)}{3} = \tfrac{11}{3}\%\) together.",
 steps(("Equation", p(r"With \(x\) lakh in the FD: \(0.06x + \tfrac{11}{300}(15 - x) = 0.76\).")),
       ("Solve", p(r"\(18x + 165 - 11x = 228\), so \(x = 9\)."))) + final(r"\(9\)"))

P.qa(17, r"A club has \(256\) members of whom \(144\) can play football, \(123\) can play tennis, and \(132\) can play cricket. Moreover, \(58\) members can play both football and tennis, \(25\) can play both cricket and tennis, while \(63\) can play both football and cricket. If every member can play at least one game, then the number of members who can play only tennis is",
 M("38", "32", "45", "43"), "MCQ", "4", ["Modern_Maths::Set_Theory"], "Medium",
 "Find how many play all three first.",
 steps(("All three", p(r"\(256 = 399 - 146 + t\), so \(t = 3\).")),
       ("Only tennis", p(r"\(123 - 58 - 25 + 3 = 43\)."))) + final(r"\(43\), option 4"),
 concept=r"\[|A \cup B \cup C| = \sum|A| - \sum|A \cap B| + |A \cap B \cap C|\]",
 why_rows=[("1", "Forgets to add back the 3."), ("2", "Wrong pairs."), ("3", "Wrong pairs.")])

P.qa(18, r"If \(a_1 + a_2 + a_3 + \dots + a_n = 3(2^{n+1} - 2)\), for every \(n \ge 1\), then \(a_{11}\) equals",
 [], "TITA", "6144", ["Algebra::Progressions_and_Series"], "Easy",
 r"\(a_{11} = S_{11} - S_{10}\).",
 steps(("Difference", p(r"\(3(2^{12} - 2^{11}) = 3 \times 2048 = 6144\)."))) + final(r"\(6144\)"))

P.qa(19, r"The number of the real roots of the equation \(2\cos(x(x + 1)) = 2^x + 2^{-x}\) is",
 ["2", "1", "Infinite", "0"], "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value", "Geometry::Trigonometry"], "Medium",
 "Compare the largest value of the left side with the smallest of the right.",
 steps(("Bounds", p(r"Left \(\le 2\). Right \(\ge 2\), with equality only at \(x = 0\).")),
       ("Check x = 0", p(r"\(2\cos 0 = 2 = 2^0 + 2^0\). One root."))) + trap("Don’t stop at ‘both sides can only meet at 2’. Check whether they actually do.") + final(r"\(1\), option 2"),
 concept=r"\[a + \frac1a \ge 2 \quad (a > 0)\]",
 why_rows=[("1", "Only x = 0 works."), ("3", "Only x = 0 works."), ("4", "x = 0 is a root.")])

P.qa(21, r"In a class, \(60\%\) of the students are girls and the rest are boys. There are \(30\) more girls than boys. If \(68\%\) of the students, including \(30\) boys, pass an examination, the percentage of the girls who do not pass is",
 [], "TITA", "20", ["Arithmetic::Percentages"], "Easy",
 "20% of the class is 30 students.",
 steps(("Class", p("150 students: 90 girls, 60 boys.")),
       ("Girls who fail", p(r"102 pass, 72 of them girls. \(\tfrac{18}{90} = 20\%\)."))) + final(r"\(20\)"))

P.qa(22, r"In a circle of radius \(11\) cm, CD is a diameter and AB is a chord of length \(20.5\) cm. If AB and CD intersect at a point E inside the circle and CE has length \(7\) cm, then the difference of the lengths of BE and AE, in cm, is",
 M("2.5", "1.5", "3.5", "0.5"), "MCQ", "4", ["Geometry::Circles"], "Medium",
 "Intersecting chords: AE × EB = CE × ED.",
 steps(("Products", p(r"\(AE \cdot EB = 7 \times 15 = 105\), with \(AE + EB = 20.5\).")),
       ("Solve", p(r"10 and 10.5: a difference of 0.5."))) + final(r"\(0.5\), option 4"),
 concept=r"\[AE \cdot EB = CE \cdot ED\]",
 why_rows=[("1", "Doesn’t satisfy the product."), ("2", "Doesn’t satisfy the product."), ("3", "Doesn’t satisfy the product.")])

P.qa(23, r"On selling a pen at \(5\%\) loss and a book at \(15\%\) gain, Karim gains Rs \(7\). If he sells the pen at \(5\%\) gain and the book at \(10\%\) gain, he gains Rs \(13\). What is the cost price of the book in Rupees?",
 M("95", "85", "80", "100"), "MCQ", "3", ["Arithmetic::Profit_Loss_and_Discount", "Algebra::Linear_Equations"], "Easy",
 "Add the two equations; the pen cancels.",
 steps(("Add", p(r"\(0.25b = 20\), so \(b = 80\)."))) + final(r"\(80\), option 3"),
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(24, r"A chemist mixes two liquids 1 and 2. One litre of liquid 1 weighs \(1\) kg and one litre of liquid 2 weighs \(800\) gm. If half litre of the mixture weighs \(480\) gm, then the percentage of liquid 1 in the mixture, in terms of volume, is",
 M("80", "70", "85", "75"), "MCQ", "1", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "A litre of mixture weighs 960 g.",
 steps(("Alligation", p(r"\(x + 0.8(1 - x) = 0.96\), so \(x = 0.8\)."))) + final(r"\(80\), option 1"),
 why_rows=[("2", "Too little."), ("3", "Too much."), ("4", "Too little.")])

P.qa(25, r"Ramesh and Gautam are among \(22\) students who write an examination. Ramesh scores \(82.5\). The average score of the \(21\) students other than Gautam is \(62\). The average score of all the \(22\) students is one more than the average score of the \(21\) students other than Ramesh. The score of Gautam is",
 M("53", "51", "48", "49"), "MCQ", "2", ["Arithmetic::Average"], "Medium",
 r"Let the total be \(T\).",
 steps(("Ramesh", p(r"\(\tfrac{T}{22} = \tfrac{T - 82.5}{21} + 1\) gives \(T = 1353\).")),
       ("Gautam", p(r"\(1353 - 21 \times 62 = 51\)."))) + final(r"\(51\), option 2"),
 why_rows=[("1", "Doesn’t fit."), ("3", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(26, r"If \(m\) and \(n\) are integers such that \((\sqrt2)^{19}\, 3^4\, 4^2\, 9^m\, 8^n = 3^n\, 16^m\, \sqrt[4]{64}\) then \(m\) is",
 M("-20", "-24", "-12", "-16"), "MCQ", "3", ["Algebra::Surds_and_Indices"], "Medium",
 "Match the powers of 2 and of 3 separately.",
 steps(("Powers of 3", p(r"\(4 + 2m = n\).")),
       ("Powers of 2", p(r"\(\tfrac{19}{2} + 4 + 3n = 4m + \tfrac32\), so \(3n - 4m = -12\).")),
       ("Solve", p(r"\(12 + 6m - 4m = -12\), so \(m = -12\)."))) + final(r"\(-12\), option 3"),
 why_rows=[("1", "Doesn’t balance."), ("2", "Doesn’t balance."), ("4", "Doesn’t balance.")])

P.qa(27, r"Three men and eight machines can finish a job in half the time taken by three machines and eight men to finish the same job. If two machines can finish the job in \(13\) days, then how many men can finish the job in \(13\) days?",
 [], "TITA", "13", ["Arithmetic::Time_and_Work"], "Medium",
 "Compare the rates of a man and a machine.",
 steps(("Rates", p(r"\(3m + 8M = 2(3M + 8m)\), so \(M = 6.5m\).")),
       ("Men", p(r"Two machines = 13 men."))) + final(r"\(13\)"))

P.qa(28, r"Corners are cut off from an equilateral triangle T to produce a regular hexagon H. Then, the ratio of the area of H to the area of T is",
 M("2 : 3", "4 : 5", "5 : 6", "3 : 4"), "MCQ", "1", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "Cut each side into three equal parts.",
 steps(("Small triangles", p("T is 9 small equilateral triangles; the 3 corners removed leave 6.")),
       ("Ratio", p("6 : 9 = 2 : 3."))) + final(r"\(2 : 3\), option 1"),
 why_rows=[("2", "Wrong count."), ("3", "Wrong count."), ("4", "Wrong count.")])

P.qa(29, r"Let \(x\) and \(y\) be positive real numbers such that \(\log_5(x + y) + \log_5(x - y) = 3\), and \(\log_2 y - \log_2 x = 1 - \log_2 3\). Then \(xy\) equals",
 M("150", "25", "100", "250"), "MCQ", "1", ["Algebra::Logarithms_and_Exponents"], "Easy",
 "Turn both into plain equations.",
 steps(("Equations", p(r"\(x^2 - y^2 = 125\) and \(\tfrac yx = \tfrac23\).")),
       ("Solve", p(r"\(\tfrac59 x^2 = 125\): \(x = 15\), \(y = 10\), \(xy = 150\)."))) + final(r"\(150\), option 1"),
 why_rows=[("2", "Doesn’t fit."), ("3", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(30, r"Let S be the set of all points \((x, y)\) in the x-y plane such that \(|x| + |y| \le 2\) and \(|x| \ge 1\). Then, the area, in square units, of the region represented by S equals",
 [], "TITA", "2", ["Geometry::Coordinate_Geometry"], "Easy",
 "The square |x| + |y| ≤ 2 minus a middle strip.",
 steps(("Pieces", p(r"For \(1 \le x \le 2\), a triangle with base 2 and height 1: area 1. The same on the left.")),
       ("Total", p("2."))) + final(r"\(2\)"))

P.qa(31, r"With rectangular axes of co-ordinates, the number of paths from \((1, 1)\) to \((8, 10)\) via \((4, 6)\), where each step from any point \((x, y)\) is either to \((x, y + 1)\) or to \((x + 1, y)\), is",
 [], "TITA", "3920", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Count each leg as an arrangement of R and U steps.",
 steps(("First leg", p(r"3 right, 5 up: \(\binom83 = 56\).")),
       ("Second leg", p(r"4 right, 4 up: \(\binom84 = 70\).")),
       ("Total", p(r"\(56 \times 70 = 3920\)."))) + final(r"\(3920\)"))

P.qa(32, r"If the rectangular faces of a brick have their diagonals in the ratio \(3 : 2\sqrt3 : \sqrt{15}\), then the ratio of the length of the shortest edge of the brick to that of its longest edge is",
 M(r"\sqrt3 : 2", r"1 : \sqrt3", r"2 : \sqrt5", r"\sqrt2 : \sqrt3"), "MCQ", "2", ["Geometry::Mensuration"], "Medium",
 "Square the diagonals.",
 steps(("Squares", p(r"\(a^2 + b^2 = 9\), \(a^2 + c^2 = 12\), \(b^2 + c^2 = 15\). Total \(a^2 + b^2 + c^2 = 18\).")),
       ("Edges", p(r"\(a^2 = 3\), \(b^2 = 6\), \(c^2 = 9\). Ratio \(\sqrt3 : 3 = 1 : \sqrt3\)."))) + final(r"\(1 : \sqrt3\), option 2"),
 why_rows=[("1", "Not shortest to longest."), ("3", "Doesn’t fit."), ("4", "Shortest to middle.")])

P.qa(33, r"The number of solutions to the equation \(|x|(6x^2 + 1) = 5x^2\) is",
 [], "TITA", "5", ["Algebra::Inequalities_and_Absolute_Value", "Algebra::Equations_and_Polynomials"], "Medium",
 r"Take \(x \ge 0\) first, then use symmetry.",
 steps(("x ≥ 0", p(r"\(x(6x^2 - 5x + 1) = 0\): \(x = 0, \tfrac12, \tfrac13\).")),
       ("x < 0", p(r"By symmetry, \(-\tfrac12, -\tfrac13\).")),
       ("Total", p("5."))) + final(r"\(5\)"))

P.qa(34, r"Let T be the triangle formed by the straight line \(3x + 5y - 45 = 0\) and the co-ordinate axes. Let the circumcircle of T have radius of length L, measured in the same unit as the coordinate axes. Then, the integer closest to L is",
 [], "TITA", "9", ["Geometry::Coordinate_Geometry", "Geometry::Circles"], "Easy",
 "A right triangle’s circumradius is half the hypotenuse.",
 steps(("Vertices", p(r"\((0, 0)\), \((15, 0)\), \((0, 9)\).")),
       ("Radius", p(r"\(\tfrac12\sqrt{225 + 81} = \tfrac12\sqrt{306} \approx 8.75\)."))) + final(r"\(9\)"))
