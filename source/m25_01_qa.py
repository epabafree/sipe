# -*- coding: utf-8 -*-
# Simp Mock 1 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_01 import P
import m25_01_figs as F

P.qa(1, "Find the smallest possible four-digit number having exactly 12 distinct factors.", ["1000", "1012", "1020", "1060"], "MCQ", "2", ["Number_System::Factors_and_Divisibility"], "Medium",
 "12 = 12, 6 × 2, 4 × 3 or 3 × 2 × 2: the number is \\(p^{11}\\), \\(p^5q\\), \\(p^3q^2\\) or \\(p^2qr\\).",
 steps(("Check upward from 1000", table(["Number", "Factorised", "Factors"],
         [["1000", "\\(2^3 \\cdot 5^3\\)", "16"], ["1001", "\\(7 \\cdot 11 \\cdot 13\\)", "8"], ["1002", "\\(2 \\cdot 3 \\cdot 167\\)", "8"], ["1003", "\\(17 \\cdot 59\\)", "4"], ["1004", "\\(2^2 \\cdot 251\\)", "6"],
          ["1005", "\\(3 \\cdot 5 \\cdot 67\\)", "8"], ["1006", "\\(2 \\cdot 503\\)", "4"], ["1007", "\\(19 \\cdot 53\\)", "4"], ["1008", "\\(2^4 \\cdot 3^2 \\cdot 7\\)", "30"], ["1009", "prime", "2"],
          ["1010", "\\(2 \\cdot 5 \\cdot 101\\)", "8"], ["1011", "\\(3 \\cdot 337\\)", "4"], ["1012", "\\(2^2 \\cdot 11 \\cdot 23\\)", "12"]], hi={(12, 2)}))) + final("1012, option 2"),
 concept=r"\[n = p^a q^b r^c \Rightarrow \text{number of factors} = (a+1)(b+1)(c+1)\]",
 why_rows=[("1", "\\(2^3 5^3\\) has 16 factors."), ("3", "1020 has 12 factors, but 1012 is smaller."), ("4", "Larger than 1012.")])

P.qa(2, r"Find the absolute value of the difference between the roots of the equation \(\sqrt[3]{5+3x} + \sqrt[3]{5-3x} = \sqrt[3]{10}\).",
 [r"\(\dfrac{10}{3}\)", r"\(\dfrac{5}{3}\)", r"\(\dfrac{25}{9}\)", "9"], "MCQ", "1", ["Algebra::Surds_and_Indices"], "Medium",
 "Let \\(a\\) and \\(b\\) be the two cube roots. Then \\(a^3 + b^3 = 10\\) and \\(a + b = \\sqrt[3]{10}\\). Cube the second.",
 steps(("Cube both sides", p(r"\((a+b)^3 = a^3 + b^3 + 3ab(a+b)\): \(10 = 10 + 3ab\sqrt[3]{10}\), so \(ab = 0\).")),
       ("Roots", p(r"Either \(5 + 3x = 0\) or \(5 - 3x = 0\): \(x = \pm\tfrac53\). Both satisfy the equation. Difference \(\tfrac{10}{3}\)."))) + final(r"\(\tfrac{10}{3}\), option 1"),
 concept=r"\[(a+b)^3 = a^3 + b^3 + 3ab(a+b)\]",
 why_rows=[("2", "One root, not the difference."), ("3", "The product squared, not the difference."), ("4", "Not from these roots.")])

P.qa(3, "Towns A and B are 20 km apart. A single bus operates non-stop between the two towns, taking 25 minutes to complete each one-way trip. After completing a trip, the bus halts for 5 minutes before starting the next journey. The service begins from town A at 6:00 AM and continues throughout the day. On a particular day, Raja starts cycling from town A towards town B at 6:30 AM and rides without any breaks. His electric cycle maintains a constant speed of 5 km/hr. What is the total distance (in km) covered by the bus while travelling towards town B from the moment it first crosses Raja to the moment Raja reaches town B?",
 [r"\(176\tfrac{8}{9}\)", r"\(139\tfrac{5}{11}\)", "104", "80"], "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Hard",
 "The bus runs A→B in 0–25 min of every hour, waits, and runs B→A in 30–55 min. Raja takes 4 hours, so he reaches B at 10:30.",
 steps(("First crossing", p("At 6:30 the bus is at B. On its way back (6:30–6:55) it meets Raja, who is near A. From then on, count the bus’s A→B runs until 10:30.")),
       ("A→B runs after the crossing", p("The bus leaves A for B at 7:00, 8:00, 9:00 and 10:00, each run finishing 25 minutes later, all before 10:30. Four runs of 20 km.")),
       ("Total", p("\\(4 \\times 20 = 80\\) km."))) + trap("Only movement towards B counts. The 6:00 run ended before Raja started, and the meeting happens on a return trip.") + final("80, option 4"),
 why_rows=[("1", "Adds distance in both directions."), ("2", "Not from whole trips."), ("3", "Counts part of a trip that doesn’t happen.")])

P.qa(4, "A container initially holds a mixture of pink and yellow paints in the ratio 5 : 7. A certain quantity of this mixture is removed, and some amount of white paint is added to the remaining mixture. As a result, the ratio of pink, yellow, and white paints in the container becomes 10 : 14 : 11. The total volume of paint in the container after the addition of white paint is 33 litres less than the initial volume. Moreover, the quantity of pink paint removed is 121 litres less than the quantity of white paint added. The quantity (in litres) of white paint added is ________.",
 [], "TITA", "231", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "After the change: pink \\(10k\\), yellow \\(14k\\), white \\(11k\\). The paint left from the old mixture is \\(24k\\).",
 steps(("Volumes", p(r"After: \(35k\). Before: \(35k + 33\). Removed: \((35k + 33) - 24k = 11k + 33\).")),
       ("Pink removed", p(r"\(\tfrac{5}{12}(11k + 33)\). It is 121 less than the white added: \(11k - \tfrac{5}{12}(11k + 33) = 121\).")),
       ("Solve", p(r"\(132k - 55k - 165 = 1452\), so \(77k = 1617\), \(k = 21\). White added \(= 11k = 231\)."))) + final("231"))

P.qa(5, "Mr. One and Mr. Two simultaneously start from points A and B towards each other with speeds 12 kmph and 6 kmph respectively. At the same instant, Mr. Three starts from point A towards point B and Mr. Four starts from point B towards point A, both at the same speed of 24 kmph. On reaching points B and A respectively, Mr. Three and Mr. Four immediately reverse their directions and keep running between points A and B without changing their speeds. If the distance between points A and B is 36 km, the distance (in km) between Mr. Three and Mr. Four at the instant when Mr. One and Mr. Two meet for the first time is _________ .",
 ["0", "12", "18", "24"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "One and Two meet after \\(36 \\div 18 = 2\\) hours. Where are Three and Four then?",
 steps(("Time", p("2 hours.")), ("Three", p("Runs 48 km: 36 to B, then 12 back. Position 24 km from A.")),
       ("Four", p("Runs 48 km: 36 to A, then 12 back towards B. Position 12 km from A.")), ("Gap", p("24 − 12 = 12 km."))) + final("12, option 2"),
 why_rows=[("1", "They meet at 18 km after 1.5 hours, not at 2 hours."), ("3", "Half of AB."), ("4", "Three’s position, not the gap.")])

P.qa(6, "Initially, a cinema reduced its ticket price by a% and observed that (a − 5) additional seats were filled, but the total revenue remained unchanged at ₹24,000. Instead, if they had reduced the ticket price by (a + 17.5)%, though they would have filled ‘b’ more seats than the original situation, yet the total revenue would have remained unchanged at ₹24,000. If initially they reduced ₹80 per ticket, then find the value of (b − a).",
 [], "TITA", "16", ["Arithmetic::Percentages"], "Hard",
 "₹80 is a% of the price, so price \\(= \\tfrac{8000}{a}\\) and seats \\(= 24000 \\div \\text{price} = 3a\\).",
 steps(("Find a", p(r"New price \(\tfrac{8000}{a} - 80\), seats \(3a + a - 5 = 4a - 5\). Revenue: \(\left(\tfrac{8000}{a} - 80\right)(4a - 5) = 24000\). Try \(a = 20\): price 400 → 320, seats 60 → 75, \(320 \times 75 = 24000\). ✓")),
       ("Second cut", p(r"37.5% off ₹400 gives ₹250. Seats \(24000 \div 250 = 96\), which is 36 more than 60. So \(b = 36\).")),
       ("Answer", p(r"\(b - a = 36 - 20 = 16\)."))) + final("16"),
 concept=r"\[\text{price} \times \text{seats} = \text{revenue (fixed)}\]")

P.qa(7, "Anisha can do a piece of work in 20 days while working independently. Beena is twice as efficient as Chetana. While working independently, Chetana takes 10% more time as compared to Anisha for the same work. Anisha works alone for the first 10 days and then Beena works alone for another 3 days. The rest of the work has been finished by Chetana working alone. What will be the amount (in ₹) of the wage received by Chetana given that Beena received ₹3330 for the work?",
 ["2450", "2475", "2575", "2775"], "MCQ", "4", ["Arithmetic::Time_and_Work"], "Medium",
 "Wages go by share of work done.",
 steps(("Rates", p(r"Anisha \(\tfrac1{20}\); Chetana takes 22 days: \(\tfrac1{22}\); Beena \(\tfrac2{22} = \tfrac1{11}\).")),
       ("Shares", p(r"Anisha: \(10 \times \tfrac1{20} = \tfrac12\). Beena: \(\tfrac{3}{11}\). Chetana: \(1 - \tfrac12 - \tfrac3{11} = \tfrac{5}{22}\).")),
       ("Wage", p(r"Beena : Chetana \(= \tfrac{6}{22} : \tfrac{5}{22} = 6 : 5\). Chetana gets \(3330 \times \tfrac56 = 2775\)."))) + final("₹2775, option 4"),
 why_rows=[("1", "Not 5/6 of 3330."), ("2", "Uses the wrong time for Chetana."), ("3", "Not 5/6 of 3330.")])

P.qa(8, "There are 9 students present in a class. Their average weight (in kg) is an integer value between 33 and 36 (including the two values). As one more student enters the class, the new average weight (in kg) of the ten students changes from the previous average value of the nine students but remains an integer. If the weight (in kg) of the tenth student is an integer value between 41 and 43 (including the two values) then the average weight (in kg) of the original nine students is _________ .",
 ["33", "34", "35", "36"], "MCQ", "1", ["Arithmetic::Average"], "Medium",
 "New average = (9 × old + w) ÷ 10 must be a whole number.",
 steps(("Last digit", p(r"\(9A + w\) must end in 0. Try each: \(A = 33\): 297 + w, needs \(w = 43\) → total 340, average 34. ✓ \(A = 34\): 306 + w needs \(w = 44\) ✗. \(A = 35\): 315 needs 45 ✗. \(A = 36\): 324 needs 46 ✗."))) + final("33, option 1"),
 why_rows=[("2", "Needs a 44 kg student."), ("3", "Needs a 45 kg student."), ("4", "Needs a 46 kg student.")])

P.qa(9, r"A tap can fill a tank in 30 minutes less than its usual time when operating at \(\tfrac{13}{9}\) times its normal flow rate. What is the time required in minutes for the tap to fill the tank when it operates at \(\tfrac{15}{14}\) times its normal flow rate?",
 [], "TITA", "91", ["Arithmetic::Time_and_Work"], "Medium",
 "Time is inversely proportional to the flow rate.",
 steps(("Usual time", p(r"At \(\tfrac{13}{9}\) the rate, time is \(\tfrac{9}{13}T\): \(T - \tfrac{9}{13}T = 30\), so \(\tfrac{4}{13}T = 30\), \(T = 97.5\) minutes.")),
       ("New rate", p(r"\(\tfrac{14}{15} \times 97.5 = 91\) minutes."))) + final("91"))

P.qa(10, "A bank allows its customers to invest only in integral multiples of ₹100. Chandan invested ₹15000 in this bank at 10% rate of interest per annum compounding annually. At the same time, Suraj invested a sum of money in the same bank at 8% rate of interest per annum, in a simple interest scheme. What is the maximum amount of money (in ₹) that Suraj can invest so that after 3 years the maturity amount of Chandan is more than that of Suraj?",
 [], "TITA", "16100", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "Chandan’s amount: \\(15000 \\times 1.1^3\\). Suraj’s: \\(S \\times 1.24\\).",
 steps(("Chandan", p(r"\(15000 \times 1.331 = 19965\).")),
       ("Suraj", p(r"\(1.24S < 19965\), so \(S < 16100.8\). The largest multiple of 100 is 16100 (giving 19964)."))) + final("16100"))

P.qa(11, r"The remainder when \(17^{300} - 53\) is divided by 307 is _________ .", [], "TITA", "255", ["Number_System::Remainders"], "Hard",
 "307 is prime. Fermat: \\(17^{306} \\equiv 1\\). So \\(17^{300} \\equiv 17^{-6}\\).",
 steps(("Small powers", p(r"\(17^2 = 289 \equiv -18\).") + p(r"\(17^3 \equiv -18 \times 17 = -306\), and \(-306 \equiv 1 \pmod{307}\).")),
       ("The big power", p(r"\(17^{300} = (17^3)^{100} \equiv 1\).")),
       ("Subtract", p(r"\(1 - 53 = -52 \equiv 307 - 52 = 255\)."))) + final("255"),
 concept=r"\[a^{p-1} \equiv 1 \pmod p\ \ (p \text{ prime},\ p \nmid a)\]")

P.qa(12, "Which of the following equations definitely has real roots?",
 [r"\(ax^2 + bx + c = 0\), given that \(a, b, c\) are real numbers, and \(a\) is positive but \(b\) is negative.", r"\(ax^2 + bx + c = 0\), given that \(a, b, c\) are real numbers, and both \(a\) and \(b\) are positive.",
  r"\(ax^2 + bx + c = 0\), given that \(a, b, c\) are real numbers, and both \(b\) and \(c\) are negative.", r"\(ax^2 + bx + c = 0\), given that \(a, b, c\) are real numbers, and \(c\) is positive but \(a\) is negative."],
 "MCQ", "4", ["Algebra::Quadratic_Equations"], "Easy",
 "Real roots need \\(b^2 - 4ac \\ge 0\\). When is that guaranteed whatever \\(b\\) is?",
 steps(("Opposite signs of a and c", p(r"If \(a < 0 < c\), then \(-4ac > 0\), so \(b^2 - 4ac > 0\) always.")),
       ("The others fail", p(r"\(x^2 - x + 1\) (option 1), \(x^2 + x + 1\) (option 2), \(-x^2 - x - 1\) (option 3) all have negative discriminants."))) + final("Option 4"),
 why_rows=[("1", r"\(x^2 - x + 1\): no real roots."), ("2", r"\(x^2 + x + 1\): no real roots."), ("3", r"\(-x^2 - x - 1\): no real roots.")])

P.qa(13, r"Find the minimum value of the function \(f(x) = \left|-13 + 12x - 3x^2\right|\).", [], "TITA", "1", ["Algebra::Functions"], "Easy",
 "Complete the square inside.",
 steps(("Inside", p(r"\(-3x^2 + 12x - 13\) \(= -3(x-2)^2 - 1\), which is at most \(-1\). It never reaches 0.")),
       ("Absolute value", p(r"\(|{\dots}| = 3(x-2)^2 + 1 \ge 1\), equal to 1 at \(x = 2\)."))) + final("1"))

P.qa(14, r"The number of integers that satisfy the inequality \((x + 2)(x - 8) < 24\) is", ["More than 15", "14", "13", "Less than 13"], "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "Move 24 across and factorise.",
 steps(("Rearrange", p(r"\(x^2 - 6x - 40 < 0\), i.e. \((x - 10)(x + 4) < 0\), so \(-4 < x < 10\).")),
       ("Count", p("Integers −3 to 9: 13."))) + final("13, option 3"),
 why_rows=[("1", "Too many."), ("2", "Includes an endpoint."), ("4", "13 exactly.")])

P.qa(15, "Employees of an organisation are categorised into three levels: managers, supervisors, and executives. Managers are superior to the other two categories, and the executives are subordinates to the other two categories. The supervisors are subordinate to the managers but superior to the executives. An employee refers to another employee working at the same level as a ‘peer’. In one of the branch offices of this organisation, a manager said that the ratio of the number of her peers to that of her subordinates is 1 : 8. For a supervisor in this branch, the ratio of the number of superiors to that of the subordinates is 1 : 4. What can be the minimum value of the total number of employees working in that branch office?",
 ["9", "13", "17", "19"], "MCQ", "4", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "With \\(M\\) managers, \\(S\\) supervisors and \\(E\\) executives: \\((M-1) : (S+E) = 1 : 8\\) and \\(M : E = 1 : 4\\).",
 steps(("Equations", p(r"\(S + E = 8(M - 1)\) and \(E = 4M\), so \(S = 4M - 8\).")),
       ("Smallest M", p(r"\(M = 1\): the manager has no peers, ratio 0 ✗. \(M = 2\): \(S = 0\), but there is a supervisor ✗. \(M = 3\): \(S = 4,\ E = 12\).")),
       ("Total", p("3 + 4 + 12 = 19."))) + trap("A manager’s peers don’t include herself: \\(M - 1\\), not \\(M\\).") + final("19, option 4"),
 why_rows=[("1", "Can’t satisfy both ratios."), ("2", "Can’t satisfy both ratios."), ("3", "Can’t satisfy both ratios.")])

P.qa(16, r"What is the area enclosed by the region \(y = |x + 2| + 3\), line \(x = -1\), x-axis and y-axis?", ["6 sq. units", "4.5 sq. units", "9 sq. units", "8 sq. units"], "MCQ", "2", ["Geometry::Coordinate_Geometry"], "Easy",
 "Between \\(x = -1\\) and \\(x = 0\\), \\(x + 2 > 0\\), so \\(y = x + 5\\).",
 steps(("A trapezium", p(r"Heights 4 at \(x = -1\) and 5 at \(x = 0\), width 1. Area \(\tfrac{4 + 5}{2} \times 1 = 4.5\)."))) + final("4.5 sq. units, option 2"),
 why_rows=[("1", "Not this region."), ("3", "Doubles the area."), ("4", "Not this region.")])

P.qa(17, "In the diagram given below, CE bisects ∠DCB and BE bisects ∠DBA. If m∠D = 70°, m∠E = ?" + F.Q17, ["70°", "35°", "140°", "Cannot be determined"], "MCQ", "2", ["Geometry::Triangles"], "Medium",
 "∠DBA is an exterior angle of triangle DCB. Use it twice.",
 steps(("Exterior angles", p(r"In triangle DCB: \(\angle DBA = \angle D + \angle DCB\).") + p(r"In triangle ECB: \(\angle EBA = \angle E + \angle ECB\).")),
       ("Halve the first", p(r"\(\angle EBA = \tfrac12\angle DBA\) \(= \tfrac12\angle D + \tfrac12\angle DCB\) \(= \tfrac12\angle D + \angle ECB\).") + p(r"So \(\angle E = \tfrac12\angle D = 35^\circ\)."))) + final("35°, option 2"),
 concept=r"\[\text{Internal bisector at } C\]\[\text{meets external bisector at } B:\]\[\angle E = \tfrac12 \angle D\]",
 why_rows=[("1", "Forgets the halving."), ("3", "Doubles instead of halving."), ("4", "It is fixed at 35°.")])

P.qa(18, "In triangle ABC (shown below) AP = 8 cm, BC = 9 cm, BE = 2 × AE, and AC = 3 × AD. Find the area (in cm²) of the quadrilateral ADOE." + F.Q18, ["16", "6", "6.4", "9"], "MCQ", "2", ["Geometry::Triangles"], "Hard",
 "Area of ABC is 36. E and D each cut a third of their sides from A. Use mass points (or symmetry) to find where O sits on BD.",
 steps(("Area of ABC", p(r"\(\tfrac12 \times 9 \times 8 = 36\).")),
       ("Where O is", p(r"AE : EB = 1 : 2 and AD : DC = 1 : 2. Put mass 2 at A, 1 at B, 1 at C. Then E has mass 3 and D has mass 3, and O on BD has BO : OD = 3 : 1, likewise CO : OE = 3 : 1.")),
       ("Pieces", p(r"Triangle ABD = \(\tfrac13 \times 36 = 12\). Triangle AOD = \(\tfrac14\) of ABD = 3 (O is a quarter of the way from D to B). By symmetry triangle AOE = 3. ADOE = 6."))) + final("6, option 2"),
 concept=r"\[\text{Triangles with the same height: area} \propto \text{base}\]",
 why_rows=[("1", "Not this region."), ("3", "Wrong ratio on BD."), ("4", "Wrong ratio on BD.")])

P.qa(19, r"Area of ΔABC, an equilateral triangle, is \(36\sqrt3\) sq. cm. D is the midpoint of side BC. The tangent drawn to the circumcircle of ΔABC at point C intersects extended AD at point P. Find the length (in cm) of line segment PC.",
 ["12", "10", r"\(6\sqrt3\)", r"\(4\sqrt3\)"], "MCQ", "1", ["Geometry::Circles"], "Medium",
 "AD passes through the centre O. The tangent at C is perpendicular to OC.",
 steps(("Side and radius", p(r"\(\tfrac{\sqrt3}{4}a^2 = 36\sqrt3\) gives \(a = 12\); circumradius \(R = \tfrac{a}{\sqrt3} = 4\sqrt3\).")),
       ("Right triangle OCP", p(r"Angle COD = 60° (half of the 120° that side BC subtends at the centre), so in triangle OCP, right-angled at C: \(PC = OC \tan 60^\circ = 4\sqrt3 \times \sqrt3 = 12\)."))) + final("12, option 1"),
 why_rows=[("2", "Not from these lengths."), ("3", "The altitude, not PC."), ("4", "The circumradius.")])

P.qa(20, "50 tourist places are shortlisted in the state. They are beaches or religious places or hill stations. Among them, 15 are only hill stations and 10 are only religious places. 6 are hill stations as well as religious places. 2 are classified as hill stations as well as beaches but not religious places. 2 places known for their religious importance also have beaches, but not classified as hill stations. 20 are classified as beaches. If one must select either only a beach or a hill station which is also a religious place but does not have a beach, how many options does he have?",
 ["20", "19", "21", "None of these"], "MCQ", "1", ["Modern_Maths::Set_Theory"], "Medium",
 "Let \\(y\\) be the places that are all three, and \\(x\\) the beaches only. The 6 includes the \\(y\\).",
 steps(("Total", p(r"15 + 10 + 6 + 2 + 2 + \(x = 50\), so \(x = 15\) (the 6 counts every hill-and-religious place, all-three included).")),
       ("Beaches", p(r"\(x + 2 + 2 + y = 20\): \(y = 1\).")),
       ("Count", p(r"Only beaches: 15. Hill and religious without beach: \(6 - 1 = 5\). Total 20."))) + final("20, option 1"),
 why_rows=[("2", "Counts the all-three place in."), ("3", "Off by one."), ("4", "20 is listed.")])

P.qa(21, r"It is given that \(f(x) = \dfrac{(\log_2 x) - 7}{(\log_2 x) - 11}\), where \(x\) is an integer. Find the number of integer values of \(x\) for which \(f(x)\) is negative.",
 ["1916", "1918", "1919", "1920"], "MCQ", "3", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "A fraction is negative when the top and bottom have opposite signs.",
 steps(("Signs", p(r"\(7 < \log_2 x < 11\), i.e. \(128 < x < 2048\).")), ("Count", p(r"\(2047 - 129 + 1 = 1919\)."))) + final("1919, option 3"),
 why_rows=[("1", "Off by a few."), ("2", "Excludes one too many."), ("4", "Includes an endpoint.")])

P.qa(22, "In a 7 × 7 grid with each cell having unit square area, how many rectangles (which are not squares) can be formed using the edges of the squares in the grid?", ["350", "644", "784", "700"], "MCQ", "2", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "All rectangles minus squares.",
 steps(("All rectangles", p(r"Choose 2 of 8 vertical and 2 of 8 horizontal lines: \(\binom82^2 = 28^2 = 784\).")),
       ("Squares", p(r"\(1^2 + 2^2 + \dots + 7^2 = 140\).")), ("Answer", p("784 − 140 = 644."))) + final("644, option 2"),
 concept=r"\[n \times n \text{ grid: } \binom{n+1}{2}^2 \text{ rectangles},\ \sum_{k=1}^{n} k^2 \text{ squares}\]",
 why_rows=[("1", "Not rectangles minus squares."), ("3", "Includes the squares."), ("4", "Subtracts too few squares.")])
