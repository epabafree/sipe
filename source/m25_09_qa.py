# -*- coding: utf-8 -*-
# Simp Mock 9 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_09 import P
import m25_09_figs as F

P.qa(1, r"The equation \(x^2 - kx - 5 = 0\) has two real and distinct roots, both in the interval [−1, 8]. The value of k lies in the interval:",
 [r"\(\left[4, \tfrac{59}8\right]\)", "[−5, 6)", r"\(\left(-2, \tfrac{59}8\right)\)", "[8, ∞)"], "MCQ", "1", ["Algebra::Quadratic_Equations"], "Medium",
 "f(−1) ≥ 0 and f(8) ≥ 0, since the parabola opens upward.",
 steps(("f(−1)", p(r"\(1 + k - 5 \ge 0\): \(k \ge 4\).")),
       ("f(8)", p(r"\(64 - 8k - 5 \ge 0\): \(k \le \tfrac{59}8\).")),
       ("Others", p(r"The discriminant \(k^2 + 20 > 0\) always, and the vertex \(\tfrac k2\) lies between −1 and 8."))) + final("Option 1"),
 why_rows=[("2", "Ignores the end conditions."), ("3", "Lower end wrong."), ("4", "Above 59/8 the root passes 8.")])

P.qa(2, "Three trains of equal length start at the same moment from the same point, side by side, in the same direction on parallel tracks, each at a different constant speed. Exactly 60 seconds after starting, the fastest train finishes passing the second-fastest at the same moment as the second-fastest finishes passing the slowest. If only the fastest and slowest trains were running, how long would the fastest take to pass the slowest completely from behind (from its front reaching the slowest train’s rear to its rear clearing the slowest train’s front)?",
 ["15 seconds", "30 seconds", "45 seconds", "60 seconds"], "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Starting level, ‘finishing passing’ means gaining one train length.",
 steps(("Speeds", p(r"Speeds x < y < z, length L: \(\tfrac L{z - y} = \tfrac L{y - x} = 60\), so \(z - x = 2(y - x) = \tfrac L{30}\).")),
       ("From behind", p(r"Gaining two lengths: \(\tfrac{2L}{z - x} = 60\) seconds."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Uses one length."), ("3", "Arithmetic slip.")])

P.qa(3, "A shop sold 300 ice creams of 4 different flavours to 90 customers in a day. Each customer bought at least 2 different flavours, and no customer bought two or more ice creams of the same flavour. What is the largest possible number of customers who bought exactly three ice creams?",
 ["40", "50", "60", "80"], "MCQ", "3", ["Arithmetic::Miscellaneous"], "Easy",
 "Each customer buys 2, 3 or 4.",
 steps(("Equations", p(r"\(a + b + c = 90\), \(2a + 3b + 4c = 300\): \(b + 2c = 120\).")),
       ("Maximum b", p("b = 120 − 2c and b ≤ 90 − c give c ≥ 30; c = 30, a = 0: b = 60."))) + final("60, option 3"),
 why_rows=[("1", "Not the maximum."), ("2", "Not the maximum."), ("4", "Too many ice creams needed.")])

P.qa(4, "A milk vendor sells a mixture of milk and water in the ratio 5 : 2 at the cost price of pure milk. Later he adds more water (which costs nothing) so that the ratio becomes 5 : 3, keeping the selling price per litre the same. By what percentage has his profit percentage increased?",
 ["20%", "50%", "60%", "40%"], "MCQ", "2", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Profit % = water ÷ milk.",
 steps(("Before and after", p("2/5 = 40%; 3/5 = 60%.")), ("Increase", p("From 40 to 60 is a 50% increase."))) + final("Option 2"),
 why_rows=[("1", "Percentage points."), ("3", "The new profit."), ("4", "The old profit.")])

P.qa(5, "Vishwanath dug a well of diameter 6 m to a depth of 5 m. The earth removed was heaped into a cone of height 9 m on the ground nearby. What is the ratio of the radius of the cone’s base to the radius of the well?",
 [r"\(5\sqrt3\)", r"\(\dfrac5{3\sqrt3}\)", r"\(\sqrt{\dfrac53}\)", r"\(\dfrac5{\sqrt3}\)"], "MCQ", "3", ["Geometry::Mensuration"], "Easy",
 "Equal volumes.",
 steps(("Volumes", p(r"\(\pi \cdot 9 \cdot 5 = \tfrac13 \pi r^2 \cdot 9\): \(r^2 = 15\).")),
       ("Ratio", p(r"\(\tfrac{\sqrt{15}}3 = \sqrt{\tfrac53}\)."))) + final("Option 3"),
 why_rows=[("1", "Not a ratio of radii."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(6, "P and Q together can complete a job in 80 hours, Q and R in 120 hours, and P and R in 100 hours. How long will P, Q and R take together?",
 ["More than 63.75 but less than 64 hours", "More than 64 but less than 64.25 hours", "More than 64.25 but less than 64.75 hours", "More than 64.75 hours"], "MCQ", "4", ["Arithmetic::Time_and_Work"], "Easy",
 "Add the three pair rates.",
 steps(("Twice the total", p(r"\(\tfrac1{80} + \tfrac1{120} + \tfrac1{100} = \tfrac{37}{1200}\).")),
       ("Time", p(r"\(\tfrac{2400}{37} \approx 64.86\) hours."))) + final("Option 4"),
 why_rows=[("1", "Too small."), ("2", "Too small."), ("3", "Too small.")])

P.qa(7, r"If \(\sqrt{15 + 4\sqrt{11}} - \sqrt{15 - 4\sqrt{11}} = k\), then k is a/an ________ .", ["Natural number", "Negative integer", "Irrational number", "Cannot be determined"], "MCQ", "1", ["Algebra::Surds_and_Indices"], "Easy",
 "\\(15 + 4\\sqrt{11} = (\\sqrt{11} + 2)^2\\).",
 steps(("Roots", p(r"\((\sqrt{11} + 2) - (\sqrt{11} - 2) = 4\)."))) + final("Natural number, option 1"),
 why_rows=[("2", "It’s positive."), ("3", "The surds cancel."), ("4", "It’s 4.")])

P.qa(8, "Three distinct numbers a, b and c are in geometric progression (in that order), and their sum is 252. The numbers 8a, 6b and 4c are in arithmetic progression (in that order). Find a² + b² + c².", [], "TITA", "27216", ["Algebra::Progressions_and_Series"], "Medium",
 "12b = 8a + 4c with b = ar, c = ar².",
 steps(("Ratio", p(r"\(3r = 2 + r^2\): r = 1 or 2; distinct numbers, so r = 2.")),
       ("Values", p(r"\(7a = 252\): 36, 72, 144. Squares: 1296 + 5184 + 20736 = 27216."))) + final("27216"))

P.qa(9, "The vertices of a triangle are (4, 3), (12, 3) and (4, 9). What is the circumradius of the triangle (in units)?", [], "TITA", "5", ["Geometry::Coordinate_Geometry"], "Easy",
 "It is right-angled at (4, 3).",
 steps(("Hypotenuse", p(r"Legs 8 and 6, hypotenuse 10; the circumradius is half of it: 5."))) + final("5"))

P.qa(10, "At a school function, children took part in games with their parents: 360 participants in all. Male participants (fathers and boys) outnumbered female participants (mothers and girls) by 25%, and 60% of the children were boys. Find the number of mothers as a percentage of the number of fathers, assuming every participant is either a child or a parent.",
 ["75%", "87.5%", "92.5%", "Cannot be determined"], "MCQ", "4", ["Arithmetic::Percentages"], "Medium",
 "Males 200, females 160. How many children?",
 steps(("Unknown", p("Boys = 3x, girls = 2x: fathers = 200 − 3x, mothers = 160 − 2x. The ratio changes with x (for example x = 20 gives 120/140; x = 40 gives 80/80)."))) + final("Option 4"),
 why_rows=[("1", "Assumes a value of x."), ("2", "Assumes a value of x."), ("3", "Assumes a value of x.")])

P.qa(11, r"a, b, c and d are real numbers, and \(\big|(a + b) - |c + d|\big|\) is greater than \(\big||a + b| - (c + d)\big|\). Which of the following is definitely true?",
 [r"\(a + b > 0\)", r"\(|c + d| > (c + d)\)", r"\(c + d < 0\)", r"\(|a + b| > (a + b)\)"], "MCQ", "4", ["Algebra::Inequalities_and_Absolute_Value"], "Hard",
 "Let x = a + b, y = c + d, and try the sign cases.",
 steps(("x ≥ 0", p(r"If y ≥ 0 the two sides are equal. If y < 0: left \(|x + y| \le x - y\) = right. The inequality fails.")),
       ("x < 0", p(r"Then the left side is \(|x| + |y|\); the right side \(\big||x| - y\big|\) is smaller only when y > 0.")),
       ("So", p(r"a + b < 0 and c + d > 0: \(|a + b| > (a + b)\)."))) + final("Option 4"),
 why_rows=[("1", "a + b must be negative."), ("2", "c + d is positive, so |c + d| = c + d."), ("3", "c + d is positive.")])

P.qa(12, "The HCF and LCM of two distinct positive integers are 24 and 288. Find the sum of all possible values of the smaller integer.", [], "TITA", "96", ["Number_System::Factors_and_Divisibility"], "Easy",
 "Write them as 24m and 24n with m, n coprime and mn = 12.",
 steps(("Pairs", p("(1, 12) and (3, 4): smaller numbers 24 and 72. Sum 96."))) + final("96"))

P.qa(13, "Mohan, Naman and Pawan are partners. Mohan and Naman started the business at the beginning of the year with ₹35,000 and ₹56,000. Mohan was also the manager and received 10% of the total profit as commission. Pawan joined five months later with some capital. The first year’s profit was ₹1,50,000, of which Mohan received ₹60,000 in all. At the start of the second year Naman withdrew half his capital, Pawan added ₹25,000, and Mohan kept his capital unchanged and again received 10% of the profit as commission. The second year’s profit was ₹1,60,000. How much did Mohan earn from the business in the second year?",
 ["₹56,000", "₹58,000", "₹61,000", "₹63,000"], "MCQ", "3", ["Arithmetic::Ratio_and_Proportion"], "Hard",
 "Year 1 fixes Pawan’s capital.",
 steps(("Pawan’s capital", p(r"Mohan’s share after commission: 45,000 of 1,35,000, one-third. \(\tfrac{35 \times 12}{35 \times 12 + 56 \times 12 + 7x} = \tfrac13\) (thousands) gives x = 24.")),
       ("Year 2", p("Capitals 35, 28, 49: ratio 5 : 4 : 7. After the 16,000 commission, Mohan gets 5/16 of 1,44,000 = 45,000.")),
       ("Total", p("45,000 + 16,000 = 61,000."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(14, "In △ABC, BC is the longest side and is less than 50 cm, and AC + BC = 2 × AB. CD is the perpendicular from C to AB, and AB + CD = 2 × AC. All three sides are whole numbers of centimetres, and CD + 3 = BC (in cm). Find the perimeter of △ABC (in cm).", [], "TITA", "42", ["Geometry::Triangles"], "Hard",
 "The conditions make CD, AC, AB, BC consecutive integers.",
 steps(("Order", p("CD < AC < AB < BC with BC = CD + 3: CD = x, AC = x + 1, AB = x + 2, BC = x + 3.")),
       ("Pythagoras", p(r"\(BD = \sqrt{(x + 3)^2 - x^2}\), \(AD = \sqrt{(x + 1)^2 - x^2}\), and BD + AD = x + 2. x = 12 gives 9 + 5 = 14. ✓")),
       ("Perimeter", p("13 + 14 + 15 = 42."))) + final("42"))

P.qa(15, "Raju has three identical red balls, three identical blue balls, and a cube whose six faces are painted in six different colours. He picks three of the balls and arranges them in a row from left to right, then places the cube to the right of the rightmost ball. Two arrangements are different if the ball sequence differs or a different face of the cube points upward. How many distinct arrangements can he form?",
 ["48", "8", "192", "32"], "MCQ", "1", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Ball sequences × choices of top face.",
 steps(("Count", p(r"\(2^3 = 8\) ball sequences, 6 faces up: 48."))) + final("Option 1"),
 why_rows=[("2", "Ignores the cube."), ("3", "Counts full orientations."), ("4", "Arithmetic slip.")])

P.qa(16, "A clothes shop gives 20% off the marked price of shirts and 10% off the marked price of trousers. Every shirt has the same cost price, a multiple of ₹100, and the same is true of every trouser. Shirts are marked 50% above cost and trousers 40% above cost. Jignesh bought one shirt and one trouser for ₹990. How much did he pay for the shirt (in ₹)?", [], "TITA", "360", ["Arithmetic::Profit_and_Loss"], "Medium",
 "Cost prices 100S and 100T.",
 steps(("Selling prices", p(r"Shirt \(100S \times 1.5 \times 0.8 = 120S\); trouser \(100T \times 1.4 \times 0.9 = 126T\).")),
       ("Solve", p(r"\(120S + 126T = 990\): 126T must end in 0, so T = 5 (630) and the shirt is 360."))) + final("360"))

P.qa(17, r"Treating the roots algebraically (they need not be real), find the minimum value, over real a, of the sum of the squares of the roots of \(x^2 + (2a + 1)x + 3a = 0\).",
 [r"\(\tfrac14\)", r"\(\tfrac34\)", r"\(-\tfrac14\)", r"\(\tfrac32\)"], "MCQ", "2", ["Algebra::Quadratic_Equations"], "Medium",
 "\\(p^2 + q^2 = (p + q)^2 - 2pq\\).",
 steps(("Expression", p(r"\((2a + 1)^2 - 6a = 4a^2 - 2a + 1\).")),
       ("Minimum", p(r"At \(a = \tfrac14\): \(\tfrac14 - \tfrac12 + 1 = \tfrac34\)."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Not the minimum.")])

P.qa(18, "25 litres of water are added to 15 litres of orange squash. Then 20% of the mixture is replaced with orange squash. Finally, water is added to fill the container to the brim. If water and squash are then in the ratio 2 : 1, what is the container’s capacity (in litres)?", [], "TITA", "60", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Track the squash.",
 steps(("Squash", p("8 litres removed (3 squash, 5 water), 8 squash added: 15 − 3 + 8 = 20.")),
       ("Capacity", p("Water 40, total 60."))) + final("60"))

P.qa(19, "In a game between Akarsh and Utkarsh, Akarsh begins by naming a natural number from 2 to 9. Utkarsh then doubles it, and Akarsh adds 10 to the result. They continue this way: Utkarsh always doubles the last number, and Akarsh always adds 10. The first player to say a number of 100 or more loses. How many starting numbers from 2 to 9 should Akarsh avoid if he wants to win?", [], "TITA", "1", ["Arithmetic::Miscellaneous"], "Easy",
 "Every move is forced; just play each start.",
 steps(("Play", p("Start 4: 4, 8, 18, 36, 46, 92, 102, and Akarsh says 102. Every other start has Utkarsh doubling past 100 first (for 5: 5, 10, 20, 40, 50, 100)."))) + final("1"))

P.qa(20, "Usha took exams in Physics, Chemistry, Mathematics and Biology, each out of 100. She scored 12 more in Mathematics and 10 less in Biology than her average over the four subjects. She scored 73 in Physics and 89 in Chemistry. What was her highest score?", ["92", "94", "98", "90"], "MCQ", "2", ["Arithmetic::Average"], "Easy",
 "Let the average be A.",
 steps(("Average", p(r"\(4A = 73 + 89 + (A + 12) + (A - 10)\): A = 82.")), ("Scores", p("Maths 94, Biology 72; highest 94."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(21, "In the diagram, AB is a chord of a circle with centre O, and ABCD is a rectangle with AB : AC = 1 : √5. The ratio of the area of the circle to that of the rectangle is 11 : 7." + F.RECT + "Find the ratio of the shaded area (the region common to the circle and the rectangle) to the unshaded area of the rectangle. (Take π = 22/7.)",
 [r"\((44 - 21\sqrt3) : 168\)", r"\((44 - 21\sqrt3) : (124 - 21\sqrt3)\)", r"\((44 - 21\sqrt3) : (124 + 21\sqrt3)\)", r"\((44 + 21\sqrt3) : (124 + 21\sqrt3)\)"], "MCQ", "3", ["Geometry::Circles"], "Hard",
 "AC is the diagonal, so BC = 2 AB.",
 steps(("Sizes", p(r"AB = s, BC = 2s, rectangle \(2s^2\). \(\tfrac{22}7 r^2 : 2s^2 = 11 : 7\) gives r = s, so chord AB subtends 60°.")),
       ("Segment", p(r"\(s^2\left(\tfrac{11}{21} - \tfrac{\sqrt3}4\right) = \tfrac{(44 - 21\sqrt3)\,s^2}{84}\).")),
       ("Ratio", p(r"Unshaded: \(2s^2\) minus that \(= \tfrac{(124 + 21\sqrt3)\,s^2}{84}\)."))) + final("Option 3"),
 why_rows=[("1", "Uses the whole rectangle."), ("2", "Sign slip."), ("4", "Sign slip.")])

P.qa(22, r"Let \(u = \sqrt{5\sqrt{5\sqrt5}}\) and \(v = \sqrt{11\sqrt{11\sqrt{11\sqrt{11}}}}\). If \(\log_2(\log_5 u) = \log_2 a - 3\) and \(\log_2(\log_{11} v) = \log_2 b - 4\), then a − b is:", ["6", "−7", "−8", "7"], "MCQ", "3", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Work out each nested radical’s exponent.",
 steps(("First", p(r"\(\sqrt{5\sqrt{5\sqrt5}} = 5^{7/8}\); \(\log_2\tfrac78 = \log_2 7 - 3\), so a = 7.")),
       ("Second", p(r"The 11-radical is \(11^{15/16}\); \(\log_2\tfrac{15}{16} = \log_2 15 - 4\), so b = 15.")),
       ("Difference", p("7 − 15 = −8."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Off by one."), ("4", "Sign slip.")])
