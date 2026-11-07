# -*- coding: utf-8 -*-
# Batch 16 — CAT 2018 Slot 1: QA (33 of 34; Q9 isn't in the source).
from fmt import steps, final, trap, why, table, p
from b16_18s1 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"If \(x\) is a positive quantity such that \(2^x = 3^{\log_5 2}\), then \(x\) is equal to",
 M(r"\log 8", r"1 + \log_3 \tfrac53", r"\log_5 9", r"1 + \log_5 \tfrac35"), "MCQ", "4", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Take log base 2.",
 steps(("Logs", p(r"\(x = \log_5 2 \cdot \log_2 3 = \log_5 3\).")),
       ("Match", p(r"\(\log_5 3 = \log_5 5 + \log_5 \tfrac35 = 1 + \log_5 \tfrac35\)."))) + final("Option 4"),
 concept=r"\[\log_a b \cdot \log_b c = \log_a c\]",
 why_rows=[("1", "No basis."), ("2", r"Equals \(\log_3 5\)."), ("3", r"Twice the answer.")])

P.qa(2, r"In a circle, two parallel chords on the same side of a diameter have lengths \(4\) cm and \(6\) cm. If the distance between these chords is \(1\) cm, then the radius of the circle, in cm, is",
 M(r"\sqrt{13}", r"\sqrt{14}", r"\sqrt{11}", r"\sqrt{12}"), "MCQ", "1", ["Geometry::Circles"], "Medium",
 "The shorter chord is farther from the centre.",
 steps(("Distances", p(r"\(\sqrt{r^2 - 4} - \sqrt{r^2 - 9} = 1\).")),
       ("Solve", p(r"With \(a = \sqrt{r^2 - 9}\): \(a^2 + 5 = (a + 1)^2\), so \(a = 2\) and \(r^2 = 13\)."))) + final(r"\(\sqrt{13}\), option 1"),
 why_rows=[("2", "Doesn’t fit."), ("3", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(3, r"Humans and robots can both perform a job but at different efficiencies. Fifteen humans and five robots working together take thirty days to finish the job, whereas five humans and fifteen robots working together take sixty days to finish it. How many days will fifteen humans working together (without any robot) take to finish it?",
 M("45", "36", "32", "40"), "MCQ", "3", ["Arithmetic::Time_and_Work"], "Medium",
 r"Rates \(h\) and \(r\) per day.",
 steps(("Equations", p(r"\(15h + 5r = \tfrac1{30}\), \(5h + 15r = \tfrac1{60}\).")),
       ("Solve", p(r"Tripling the second and subtracting: \(40r = \tfrac1{60}\), so \(r = \tfrac1{2400}\) and \(15h = \tfrac{75}{2400} = \tfrac1{32}\)."))) + final(r"\(32\), option 3"),
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(4, r"Let ABCD be a rectangle inscribed in a circle of radius \(13\) cm. Which one of the following pairs can represent, in cm, the possible length and breadth of ABCD?",
 ["24, 10", "25, 9", "25, 10", "24, 12"], "MCQ", "1", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "The diagonal is the diameter, 26.",
 steps(("Check", p(r"\(24^2 + 10^2 = 676 = 26^2\)."))) + final("Option 1"),
 why_rows=[("2", "706."), ("3", "725."), ("4", "720.")])

P.qa(5, r"Points E, F, G, H lie on the sides AB, BC, CD, and DA, respectively, of a square ABCD. If EFGH is also a square whose area is \(62.5\%\) of that of ABCD and CG is longer than EB, then the ratio of length of EB to that of CG is",
 M("3 : 8", "2 : 5", "4 : 9", "1 : 3"), "MCQ", "4", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "The four corner triangles are congruent, so AE = CG.",
 steps(("Equation", p(r"With side 1 and \(EB = x\): \(x^2 + (1 - x)^2 = 0.625\), so \(x = \tfrac14\) or \(\tfrac34\).")),
       ("Ratio", p(r"CG = AE is the longer, \(\tfrac34\). So \(EB : CG = 1 : 3\)."))) + final(r"\(1 : 3\), option 4"),
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("3", "Doesn’t fit.")])

P.qa(6, r"Point P lies between points A and B such that the length of BP is thrice that of AP. Car 1 starts from A and moves towards B. Simultaneously, car 2 starts from B and moves towards A. Car 2 reaches P one hour after car 1 reaches P. If the speed of car 2 is half that of car 1, then the time, in minutes, taken by car 1 in reaching P from A is",
 [], "TITA", "12", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 r"AP = \(d\), BP = \(3d\); speeds \(2v\) and \(v\).",
 steps(("Times", p(r"Car 1: \(\tfrac{d}{2v}\). Car 2: \(\tfrac{3d}{v}\), which is 6 times as long.")),
       ("One hour", p(r"5 × car 1’s time = 60 minutes, so 12."))) + final(r"\(12\)"))

P.qa(7, r"Let \(f(x) = \min(2x^2, 52 - 5x)\) where \(x\) is any positive real number. Then the maximum possible value of \(f(x)\) is",
 [], "TITA", "32", ["Algebra::Functions"], "Easy",
 "The minimum of a rising and a falling curve peaks where they cross.",
 steps(("Crossing", p(r"\(2x^2 = 52 - 5x\) at \(x = 4\).")),
       ("Value", p("32."))) + final(r"\(32\)"))

P.qa(8, r"While multiplying three real numbers, Ashok took one of the numbers as \(73\) instead of \(37\). As a result, the product went up by \(720\). Then the minimum possible value of the sum of squares of the other two numbers is",
 [], "TITA", "40", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "The other two multiply to 20.",
 steps(("Product", p(r"\(36yz = 720\), so \(yz = 20\).")),
       ("Minimum", p(r"\(y^2 + z^2 \ge 2yz = 40\), reached when \(y = z\)."))) + final(r"\(40\)"),
 concept=r"\[y^2 + z^2 \ge 2yz\]")

P.qa(10, r"Two types of tea, A and B, are mixed and then sold at Rs \(40\) per kg. The profit is \(10\%\) if A and B are mixed in the ratio \(3 : 2\), and \(5\%\) if this ratio is \(2 : 3\). The cost prices, per kg, of A and B are in the ratio",
 M("17 : 25", "18 : 25", "19 : 24", "21 : 25"), "MCQ", "3", ["Arithmetic::Mixture_and_Alligation", "Arithmetic::Profit_Loss_and_Discount"], "Medium",
 "Write the cost of each blend.",
 steps(("Blends", p(r"\(3a + 2b = 5 \times \tfrac{40}{1.1}\) and \(2a + 3b = 5 \times \tfrac{40}{1.05}\).")),
       ("Solve", p(r"\(a = \tfrac{7600}{231}\), \(b = \tfrac{9600}{231}\): 76 : 96 = 19 : 24."))) + final(r"\(19 : 24\), option 3"),
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(11, r"Given an equilateral triangle \(T_1\) with side \(24\) cm, a second triangle \(T_2\) is formed by joining the midpoints of the sides of \(T_1\). Then a third triangle \(T_3\) is formed by joining the midpoints of the sides of \(T_2\). If this process of forming triangles is continued, the sum of the areas, in sq cm, of infinitely many such triangles \(T_1, T_2, T_3, \dots\) will be",
 M(r"188\sqrt3", r"248\sqrt3", r"164\sqrt3", r"192\sqrt3"), "MCQ", "4", ["Algebra::Progressions_and_Series", "Geometry::Triangles"], "Easy",
 "Each area is a quarter of the last.",
 steps(("First", p(r"\(\tfrac{\sqrt3}{4} \times 576 = 144\sqrt3\).")),
       ("Sum", p(r"\(144\sqrt3 \times \tfrac43 = 192\sqrt3\)."))) + final(r"\(192\sqrt3\), option 4"),
 concept=r"\[a + ar + ar^2 + \dots = \frac{a}{1 - r}\]",
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("3", "Doesn’t fit.")])

P.qa(12, r"If \(\log_{12} 81 = p\), then \(3\left(\dfrac{4 - p}{4 + p}\right)\) is equal to",
 M(r"\log_4 16", r"\log_6 16", r"\log_2 8", r"\log_6 8"), "MCQ", "4", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"\(\tfrac p4 = \log_{12} 3\).",
 steps(("Rewrite", p(r"\(\dfrac{4 - p}{4 + p} = \dfrac{1 - \log_{12} 3}{1 + \log_{12} 3}\) \(= \dfrac{\log_{12} 4}{\log_{12} 36}\) \(= \log_{36} 4\).")),
       ("Times 3", p(r"\(3\log_{36} 4 = \log_{36} 64 = \log_6 8\)."))) + final(r"\(\log_6 8\), option 4"),
 why_rows=[("1", "Equals 2."), ("2", "Not equal."), ("3", "Equals 3.")])

P.qa(13, r"John borrowed Rs \(2,10,000\) from a bank at an interest rate of \(10\%\) per annum, compounded annually. The loan was repaid in two equal installments, the first after one year and the second after another year. The first installment was interest of one year plus part of the principal amount, while the second was the rest of the principal amount plus due interest thereon. Then each installment, in Rs, is",
 [], "TITA", "121000", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "The installments’ present values add to the loan.",
 steps(("Equation", p(r"\(\tfrac{x}{1.1} + \tfrac{x}{1.21} = 210000\).")),
       ("Solve", p(r"\(x \times \tfrac{2.1}{1.21} = 210000\), so \(x = 121000\)."))) + final(r"\(121000\)"))

P.qa(14, r"When they work alone, B needs \(25\%\) more time to finish a job than A does. They two finish the job in \(13\) days in the following manner: A works alone till half the job is done, then A and B work together for four days, and finally B works alone to complete the remaining \(5\%\) of the job. In how many days can B alone finish the entire job?",
 M("20", "22", "16", "18"), "MCQ", "1", ["Arithmetic::Time_and_Work"], "Medium",
 r"Let A take \(a\) days, B \(1.25a\).",
 steps(("The middle 45%", p(r"Four days together: \(4\left(\tfrac1a + \tfrac{0.8}{a}\right) = \tfrac{7.2}{a} = 0.45\), so \(a = 16\).")),
       ("Check", p("8 + 4 + 1 = 13 days. B alone: 20."))) + final(r"\(20\), option 1"),
 why_rows=[("2", "Doesn’t fit."), ("3", "That is A."), ("4", "Doesn’t fit.")])

P.qa(15, r"How many numbers with two or more digits can be formed with the digits \(1, 2, 3, 4, 5, 6, 7, 8, 9\), so that in every such number, each digit is used at most once and the digits appear in the ascending order?",
 [], "TITA", "502", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Each set of digits gives exactly one ascending number.",
 steps(("Subsets", p(r"\(2^9 - 1 - 9 = 502\) sets of two or more digits."))) + final(r"\(502\)"))

P.qa(16, r"A right circular cone, of height \(12\) ft, stands on its base which has diameter \(8\) ft. The tip of the cone is cut off with a plane which is parallel to the base and \(9\) ft from the base. With \(\pi = \tfrac{22}{7}\), the volume, in cubic ft, of the remaining part of the cone is",
 [], "TITA", "198", ["Geometry::Mensuration"], "Easy",
 "The tip is a small cone of height 3 and radius 1.",
 steps(("Volumes", p(r"\(\tfrac13\pi(16 \times 12 - 1 \times 3)\) \(= \tfrac13 \times \tfrac{22}{7} \times 189\) \(= 198\)."))) + final(r"\(198\)"))

P.qa(17, r"Raju and Lalitha originally had marbles in the ratio \(4 : 9\). Then Lalitha gave some of her marbles to Raju. As a result, the ratio of the number of marbles with Raju to that with Lalitha became \(5 : 6\). What fraction of her original number of marbles was given by Lalitha to Raju?",
 M(r"\tfrac15", r"\tfrac{6}{19}", r"\tfrac14", r"\tfrac{7}{33}"), "MCQ", "4", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "The total, 13 parts, doesn’t change.",
 steps(("Scale", p(r"Use 143 marbles: 44 and 99 before, 65 and 78 after.")),
       ("Fraction", p(r"Lalitha gave 21 of 99: \(\tfrac{7}{33}\)."))) + final(r"\(\tfrac{7}{33}\), option 4"),
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("3", "Doesn’t fit.")])

P.qa(18, r"Each of \(74\) students in a class studies at least one of the three subjects H, E and P. Ten students study all three subjects, while twenty study H and E, but not P. Every student who studies P also studies H or E or both. If the number of students studying H equals that studying E, then the number of students studying H is",
 [], "TITA", "52", ["Modern_Maths::Set_Theory"], "Medium",
 "Nobody studies P alone.",
 steps(("Regions", p(r"Only H, only E, H-and-P only, E-and-P only add to \(74 - 30 = 44\).")),
       ("Equal H and E", p(r"Only H + (H and P) = Only E + (E and P) = 22. H = 22 + 20 + 10 = 52."))) + final(r"\(52\)"))

P.qa(19, r"A wholesaler bought walnuts and peanuts, the price of walnut per kg being thrice that of peanut per kg. He then sold \(8\) kg of peanuts at a profit of \(10\%\) and \(16\) kg of walnuts at a profit of \(20\%\) to a shopkeeper. However, the shopkeeper lost \(5\) kg of walnuts and \(3\) kg of peanuts in transit. He then mixed the remaining nuts and sold the mixture at Rs \(166\) per kg, thus making an overall profit of \(25\%\). At what price, in Rs per kg, did the wholesaler buy the walnuts?",
 M("96", "98", "86", "84"), "MCQ", "1", ["Arithmetic::Profit_Loss_and_Discount"], "Medium",
 r"Let peanuts cost \(p\) per kg.",
 steps(("Shopkeeper’s cost", p(r"\(8 \times 1.1p + 16 \times 3.6p = 66.4p\).")),
       ("His sale", p(r"16 kg left, sold for \(16 \times 166 = 2656 = 1.25 \times 66.4p\), so \(p = 32\).")),
       ("Walnuts", p(r"\(3p = 96\)."))) + final(r"\(96\), option 1"),
 why_rows=[("2", "Doesn’t fit."), ("3", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(20, r"If among \(200\) students, \(105\) like pizza and \(134\) like burger, then the number of students who like only burger can possibly be",
 M("23", "26", "96", "93"), "MCQ", "4", ["Modern_Maths::Set_Theory"], "Easy",
 "Both is between 39 and 105.",
 steps(("Range", p(r"Only burger = 134 − both, so between 29 and 95."))) + final(r"\(93\), option 4"),
 why_rows=[("1", "Too few."), ("2", "Too few."), ("3", "Too many.")])

P.qa(21, r"If \(f(x + 2) = f(x) + f(x + 1)\) for all positive integers \(x\), and \(f(11) = 91\), \(f(15) = 617\), then \(f(10)\) equals",
 [], "TITA", "54", ["Algebra::Functions", "Algebra::Progressions_and_Series"], "Medium",
 r"Let \(f(12) = a\) and build up to \(f(15)\).",
 steps(("Forward", p(r"\(f(13) = 91 + a\), \(f(14) = 91 + 2a\), \(f(15) = 182 + 3a = 617\), so \(a = 145\).")),
       ("Back", p(r"\(f(10) = f(12) - f(11) = 54\)."))) + final(r"\(54\)"))

P.qa(22, r"In an apartment complex, the number of people aged \(51\) years and above is \(30\) and there are at most \(39\) people whose ages are below \(51\) years. The average age of all the people in the apartment complex is \(38\) years. What is the largest possible average age, in years, of the people whose ages are below \(51\) years?",
 M("27", "25", "26", "28"), "MCQ", "4", ["Arithmetic::Average"], "Medium",
 "Keep the older group as young as allowed (51 each).",
 steps(("Bound", p(r"With \(n\) younger people: their average \(\le \tfrac{38(30 + n) - 30 \times 51}{n} = 38 - \tfrac{390}{n}\).")),
       ("Largest", p("Biggest at n = 39: 28."))) + final(r"\(28\), option 4"),
 why_rows=[("1", "Not the largest."), ("2", "Not the largest."), ("3", "Not the largest.")])

P.qa(23, r"A trader sells \(10\) litres of a mixture of paints A and B, where the amount of B in the mixture does not exceed that of A. The cost of paint A per litre is Rs \(8\) more than that of paint B. If the trader sells the entire mixture for Rs \(264\) and makes a profit of \(10\%\), then the highest possible cost of paint B, in Rs per litre, is",
 M("16", "26", "20", "22"), "MCQ", "3", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Cost is 240. Use as little A as allowed.",
 steps(("Cost", p(r"\(x\) litres of A: \(10b + 8x = 240\), with \(x \ge 5\).")),
       ("Highest b", p(r"At \(x = 5\), \(b = 20\)."))) + final(r"\(20\), option 3"),
 why_rows=[("1", "Not the highest."), ("2", "Needs x below 5."), ("4", "Needs x below 5.")])

P.qa(24, r"In a parallelogram ABCD of area \(72\) sq cm, the sides CD and AD have lengths \(9\) cm and \(16\) cm, respectively. Let P be a point on CD such that AP is perpendicular to CD. Then the area, in sq cm, of triangle APD is",
 M(r"32\sqrt3", r"18\sqrt3", r"24\sqrt3", r"12\sqrt3"), "MCQ", "1", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "AP is the height on CD.",
 steps(("Height", p(r"\(AP = 72 \div 9 = 8\).")),
       ("PD", p(r"\(\sqrt{256 - 64} = 8\sqrt3\).")),
       ("Area", p(r"\(\tfrac12 \times 8 \times 8\sqrt3 = 32\sqrt3\)."))) + final(r"\(32\sqrt3\), option 1"),
 why_rows=[("2", "Doesn’t fit."), ("3", "Doesn’t fit."), ("4", "Doesn’t fit.")])

P.qa(25, r"If \(U^2 + (U - 2V - 1)^2 = -4V(U + V)\), then what is the value of \(U + 3V\)?",
 M("0", r"\tfrac12", r"-\tfrac14", r"\tfrac14"), "MCQ", "3", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Move everything to one side and look for squares.",
 steps(("Squares", p(r"\((U + 2V)^2 + (U - 2V - 1)^2 = 0\).")),
       ("Solve", p(r"\(U = -2V\) and \(U - 2V = 1\): \(V = -\tfrac14\), \(U = \tfrac12\). So \(U + 3V = -\tfrac14\)."))) + final(r"\(-\tfrac14\), option 3"),
 concept=r"\[a^2 + b^2 = 0 \iff a = b = 0\]",
 why_rows=[("1", "Doesn’t fit."), ("2", "That is U."), ("4", "Sign error.")])

P.qa(26, r"In a circle with center O and radius \(1\) cm, an arc AB makes an angle \(60\) degrees at O. Let R be the region bounded by the radii OA, OB and the arc AB. If C and D are two points on OA and OB, respectively, such that OC = OD and the area of triangle OCD is half that of R, then the length of OC, in cm, is",
 M(r"\left(\tfrac{\pi}{4\sqrt3}\right)^{1/2}", r"\left(\tfrac{\pi}{6}\right)^{1/2}", r"\left(\tfrac{\pi}{3\sqrt3}\right)^{1/2}", r"\left(\tfrac{\pi}{4}\right)^{1/2}"), "MCQ", "3", ["Geometry::Circles"], "Medium",
 "Triangle OCD is equilateral.",
 steps(("Areas", p(r"Sector \(= \tfrac{\pi}{6}\). Triangle \(= \tfrac{\sqrt3}{4}OC^2 = \tfrac{\pi}{12}\).")),
       ("Solve", p(r"\(OC^2 = \tfrac{\pi}{3\sqrt3}\)."))) + final("Option 3"),
 why_rows=[("1", "Off by a factor."), ("2", "Off by a factor."), ("4", "Off by a factor.")])

P.qa(27, r"The distance from A to B is \(60\) km. Partha and Narayan start from A at the same time and move towards B. Partha takes four hours more than Narayan to reach B. Moreover, Partha reaches the mid-point of A and B two hours before Narayan reaches B. The speed of Partha, in km per hour, is",
 M("6", "4", "3", "5"), "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Partha’s second half takes 4 + 2 = 6 hours.",
 steps(("Half the way", p(r"Partha covers 30 km in the last 6 hours: 5 km/h."))) + final(r"\(5\), option 4"),
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("3", "Doesn’t fit.")])

P.qa(28, r"Let \(x, y, z\) be three positive real numbers in a geometric progression such that \(x < y < z\). If \(5x\), \(16y\), and \(12z\) are in an arithmetic progression then the common ratio of the geometric progression is",
 M(r"\tfrac36", r"\tfrac16", r"\tfrac52", r"\tfrac32"), "MCQ", "3", ["Algebra::Progressions_and_Series"], "Easy",
 r"\(y = xr\), \(z = xr^2\).",
 steps(("AP condition", p(r"\(32r = 5 + 12r^2\), so \(r = \tfrac52\) or \(\tfrac16\).")),
       ("Increasing", p(r"\(r > 1\): \(\tfrac52\)."))) + final(r"\(\tfrac52\), option 3"),
 why_rows=[("1", "Doesn’t satisfy the equation."), ("2", "The other root, but decreasing."), ("4", "Doesn’t satisfy the equation.")])

P.qa(29, r"Given that \(x^{2018}y^{2017} = \tfrac12\), and \(x^{2016}y^{2019} = 8\), then value of \(x^2 + y^3\) is",
 M(r"\tfrac{31}{4}", r"\tfrac{35}{4}", r"\tfrac{37}{4}", r"\tfrac{33}{4}"), "MCQ", "4", ["Algebra::Surds_and_Indices"], "Medium",
 "Divide the two equations.",
 steps(("Ratio", p(r"\(\tfrac{y^2}{x^2} = 16\), so \(y = \pm4x\).")),
       ("Values", p(r"Either way \(x^2 = \tfrac14\) and \(y = 2\): \(\tfrac14 + 8 = \tfrac{33}{4}\)."))) + final(r"\(\tfrac{33}{4}\), option 4"),
 why_rows=[("1", "Doesn’t fit."), ("2", "Doesn’t fit."), ("3", "Doesn’t fit.")])

P.qa(30, r"A tank is fitted with pipes, some filling it and the rest draining it. All filling pipes fill at the same rate, and all draining pipes drain at the same rate. The empty tank gets completely filled in \(6\) hours when \(6\) filling and \(5\) draining pipes are on, but this time becomes \(60\) hours when \(5\) filling and \(6\) draining pipes are on. In how many hours will the empty tank get completely filled when one draining and two filling pipes are on?",
 [], "TITA", "10", ["Arithmetic::Time_and_Work"], "Medium",
 r"Rates \(f\) and \(d\).",
 steps(("Equations", p(r"\(6f - 5d = \tfrac16\), \(5f - 6d = \tfrac1{60}\). Adding and subtracting: \(f - d = \tfrac1{60}\), \(f + d = \tfrac{3}{20}\).")),
       ("Rates", p(r"\(f = \tfrac1{12}\), \(d = \tfrac1{15}\). \(2f - d = \tfrac1{10}\)."))) + final(r"\(10\)"))

P.qa(31, r"If \(\log_2(5 + \log_3 a) = 3\) and \(\log_5(4a + 12 + \log_2 b) = 3\), then \(a + b\) is equal to",
 M("59", "40", "32", "67"), "MCQ", "1", ["Algebra::Logarithms_and_Exponents"], "Easy",
 "Undo one log at a time.",
 steps(("a", p(r"\(5 + \log_3 a = 8\), so \(a = 27\).")),
       ("b", p(r"\(108 + 12 + \log_2 b = 125\), so \(b = 32\)."))) + final(r"\(59\), option 1"),
 why_rows=[("2", "Doesn’t fit."), ("3", "That is b."), ("4", "Doesn’t fit.")])

P.qa(32, r"A CAT aspirant appears for a certain number of tests. His average score increases by \(1\) if the first \(10\) tests are not considered, and decreases by \(1\) if the last \(10\) tests are not considered. If his average scores for the first \(10\) and the last \(10\) tests are \(20\) and \(30\), respectively, then the total number of tests taken by him is",
 [], "TITA", "60", ["Arithmetic::Average"], "Medium",
 r"\(n\) tests with average \(A\).",
 steps(("Equations", p(r"\(nA - 200 = (n - 10)(A + 1)\) gives \(10A - n = 190\). \(nA - 300 = (n - 10)(A - 1)\) gives \(10A + n = 310\).")),
       ("Solve", p(r"\(A = 25\), \(n = 60\)."))) + final(r"\(60\)"))

P.qa(33, r"The number of integers \(x\) such that \(0.25 \le 2^x \le 200\) and \(2^x + 2\) is perfectly divisible by either \(3\) or \(4\), is",
 [], "TITA", "5", ["Number_System::Factors_and_Divisibility"], "Easy",
 r"\(x\) runs from −2 to 7.",
 steps(("Check", p(r"\(2^x + 2\): x = 0 → 3, 1 → 4, 2 → 6, 4 → 18, 6 → 66 work. Negative x give fractions; 3, 5, 7 give 10, 34, 130."))) + final(r"\(5\)"))

P.qa(34, r"In an examination, the maximum possible score is \(N\) while the pass mark is \(45\%\) of \(N\). A candidate obtains \(36\) marks, but falls short of the pass mark by \(68\%\). Which one of the following is then correct?",
 [r"\(N \le 200\)", r"\(243 \le N \le 252\)", r"\(201 \le N \le 242\)", r"\(N \ge 253\)"], "MCQ", "2", ["Arithmetic::Percentages"], "Easy",
 "36 is 32% of the pass mark.",
 steps(("Pass mark", p(r"\(36 \div 0.32 = 112.5\).")),
       ("N", p(r"\(112.5 \div 0.45 = 250\)."))) + final("Option 2"),
 why_rows=[("1", "Too small."), ("3", "Too small."), ("4", "Too big.")])
