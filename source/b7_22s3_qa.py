# -*- coding: utf-8 -*-
# Batch 7 — CAT 2022 Slot 3: QA Q1–22 (exam order).
from fmt import steps, final, trap, why, table, p
from b7_22s3 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"If \(c = \dfrac{16x}{y} + \dfrac{49y}{x}\) for some non-zero real numbers \(x\) and \(y\), then \(c\) cannot take the value",
 M("-60", "-50", "60", "-70"), "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 r"Put \(t = \tfrac{x}{y}\). Then \(c = 16t + \tfrac{49}{t}\), and \(t\) can be positive or negative.",
 steps(("Positive t", p(r"By AM ≥ GM, \(16t + \tfrac{49}{t} \ge 2\sqrt{16 \times 49} = 56\).")),
       ("Negative t", p(r"Replacing \(t\) by \(-t\) flips the sign, so \(c \le -56\).")),
       ("What c can’t be", p(r"\(c\) can’t lie strictly between \(-56\) and \(56\). Of the options, only \(-50\) is in that gap."))) + final(r"\(-50\), option 2"),
 shortcut=r"The product of the two terms is always \(16 \times 49\), so their sum is at least \(2\sqrt{784} = 56\) in size.",
 concept=r"\[t + \frac{k}{t} \ge 2\sqrt{k} \;(t > 0), \qquad t + \frac{k}{t} \le -2\sqrt{k} \;(t < 0)\]",
 why_rows=[("1", r"\(-60 \le -56\), so it is possible."), ("3", r"\(60 \ge 56\), so it is possible."), ("4", r"\(-70 \le -56\), so it is possible.")])

P.qa(2, r"Suppose \(k\) is any integer such that the equation \(2x^2 + kx + 5 = 0\) has no real roots and the equation \(x^2 + (k - 5)x + 1 = 0\) has two distinct real roots for \(x\). Then, the number of possible values of \(k\) is",
 M("7", "9", "8", "13"), "MCQ", "2", ["Algebra::Quadratic_Equations"], "Medium",
 "Write down both discriminant conditions, then count the integers that satisfy both.",
 steps(("No real roots", p(r"\(k^2 - 40 < 0\), so \(k^2 < 40\): \(k = -6, -5, \dots, 6\).")),
       ("Two distinct roots", p(r"\((k - 5)^2 - 4 > 0\), so \(|k - 5| > 2\): \(k < 3\) or \(k > 7\).")),
       ("Both", p(r"\(k = -6, -5, \dots, 2\): 9 values."))) + final(r"\(9\), option 2"),
 concept=r"\[b^2 - 4ac < 0: \text{ no real roots}\]\[b^2 - 4ac > 0: \text{ two distinct real roots}\]",
 why_rows=[("1", r"Leaves out a couple of values; the range is \(-6\) to \(2\)."), ("3", r"The range \(-6\) to \(2\) has 9 integers, not 8."), ("4", r"This counts all of \(-6\) to \(6\) and ignores the second condition.")])

P.qa(3, r"If \(\left(\sqrt{\tfrac{7}{5}}\right)^{3x - y} = \dfrac{875}{2401}\) and \(\left(\dfrac{4a}{b}\right)^{6x - y} = \left(\dfrac{2a}{b}\right)^{y - 6x}\), for all non-zero real values of \(a\) and \(b\), then the value of \(x + y\) is",
 [], "TITA", "14", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"Write \(\tfrac{875}{2401}\) as a power of \(\tfrac75\). For the second equation, think about what has to be true for it to hold for every \(a\) and \(b\).",
 steps(("First equation", p(r"\(875 = 7 \times 5^3\) and \(2401 = 7^4\), so \(\tfrac{875}{2401} = \tfrac{5^3}{7^3} = \left(\tfrac75\right)^{-3} = \left(\sqrt{\tfrac75}\right)^{-6}\). So \(3x - y = -6\).")),
       ("Second equation", p(r"Move everything to one side: \(\left(\tfrac{4a}{b}\right)^{6x - y}\left(\tfrac{2a}{b}\right)^{6x - y} = 1\), that is \(\left(\tfrac{8a^2}{b^2}\right)^{6x - y} = 1\). For this to hold for all \(a\) and \(b\), the exponent must be 0: \(y = 6x\).")),
       ("Solving", p(r"\(3x - 6x = -6\), so \(x = 2\), \(y = 12\), and \(x + y = 14\)."))) + final(r"\(14\)"),
 concept=r"\[m^k = 1 \text{ for every base } m \;\Rightarrow\; k = 0\]")

P.qa(4, r"Consider six distinct natural numbers such that the average of the two smallest numbers is \(14\), and the average of the two largest numbers is \(28\). Then, the maximum possible value of the average of these six numbers is",
 M("22.5", "23", "23.5", "24"), "MCQ", "1", ["Arithmetic::Average"], "Medium",
 "The two middle numbers must be smaller than the second-largest. Make the second-largest as big as you can.",
 steps(("The fixed sums", p("The two smallest add to 28 and the two largest add to 56.")),
       ("The largest two", p("They are distinct and add to 56, so the smaller of them is at most 27 (27 and 29).")),
       ("The middle two", p("They must be distinct and below 27, so at most 26 and 25, which add to 51.")),
       ("Average", p(r"\(\tfrac{28 + 51 + 56}{6} = \tfrac{135}{6} = 22.5\)."))) + final(r"\(22.5\), option 1"),
 shortcut="Only the middle pair can change. Push it as high as the fifth number allows.",
 concept=p("To maximise a sum of ordered numbers, push each free value up to the largest it can be."),
 why_rows=[("2", "Would need the middle pair to add to 54, which forces a value of 27 or more."), ("3", "Not possible for the same reason."), ("4", "Not possible for the same reason.")])

P.qa(5, r"Suppose the medians \(BD\) and \(CE\) of a triangle \(ABC\) intersect at a point \(O\). If the area of triangle \(ABC\) is \(108\) sq. cm., then, the area of the triangle \(EOD\), in sq. cm., is",
 [], "TITA", "9", ["Geometry::Triangles"], "Easy",
 r"\(DE\) joins two midpoints, so it is parallel to \(BC\) and half its length.",
 steps(("Triangle BOC", p(r"O is the centroid. Triangle BOC has a third of the area of ABC: 36.")),
       ("Similar triangles", p(r"\(DE \parallel BC\) and \(DE = \tfrac12 BC\), so triangle EOD is similar to triangle COB with ratio \(1 : 2\). Its area is \(\tfrac14 \times 36 = 9\)."))) + final(r"\(9\)"),
 shortcut=r"Triangle EOD is always \(\tfrac{1}{12}\) of triangle ABC.",
 concept=r"\[\text{area}(BOC) = \tfrac13\,\text{area}(ABC), \qquad \text{area}(EOD) = \tfrac{1}{12}\,\text{area}(ABC)\]")

P.qa(6, r"If \(3 + 2\sqrt2\) is a root of the equation \(ax^2 + bx + c = 0\), and \(4 + 2\sqrt3\) is a root of the equation \(ay^2 + my + n = 0\), where \(a, b, c, m\) and \(n\) are integers, then the value of \(\left(\dfrac{b}{m} + \dfrac{c - 2b}{n}\right)\) is",
 M("0", "3", "4", "1"), "MCQ", "3", ["Algebra::Quadratic_Equations", "Algebra::Surds_and_Indices"], "Medium",
 "With integer coefficients, irrational roots come in conjugate pairs.",
 steps(("First equation", p(r"The roots are \(3 \pm 2\sqrt2\): sum 6, product 1. So \(b = -6a\) and \(c = a\).")),
       ("Second equation", p(r"The roots are \(4 \pm 2\sqrt3\): sum 8, product \(16 - 12 = 4\). So \(m = -8a\) and \(n = 4a\).")),
       ("The value", r"\[\frac{-6a}{-8a} + \frac{a + 12a}{4a} = \frac34 + \frac{13}{4} = 4\]")) + final(r"\(4\), option 3"),
 concept=r"\[\text{integer coefficients: } p + \sqrt{q} \text{ a root} \Rightarrow p - \sqrt{q} \text{ a root}\]",
 why_rows=[("1", r"The two parts are \(\tfrac34\) and \(\tfrac{13}{4}\); they don’t cancel."), ("2", r"\(\tfrac34 + \tfrac{13}{4} = 4\), not 3."), ("4", r"\(\tfrac34 + \tfrac{13}{4} = 4\), not 1.")])

P.qa(7, r"A group of \(N\) people worked on a project. They finished \(35\%\) of the project by working \(7\) hours a day for \(10\) days. Thereafter, \(10\) people left the group and the remaining people finished the rest of the project in \(14\) days by working \(10\) hours a day. Then, the value of \(N\) is",
 M("150", "36", "140", "23"), "MCQ", "3", ["Arithmetic::Time_and_Work"], "Easy",
 "Work done is people × hours. Compare work per percent in the two phases.",
 steps(("Two phases", p(r"First phase: \(70N\) person-hours for 35%. Second phase: \(140(N - 10)\) person-hours for 65%.")),
       ("Equal rates", r"\[\frac{70N}{35} = \frac{140(N - 10)}{65}\]\[2N = \frac{28(N - 10)}{13} \;\Rightarrow\; 26N = 28N - 280\]" + p(r"So \(N = 140\)."))) + final(r"\(140\), option 3"),
 concept=r"\[\frac{M_1 H_1}{W_1} = \frac{M_2 H_2}{W_2}\]",
 why_rows=[("1", "Doesn’t balance the two phases."), ("2", "Too small; 10 leaving would change the rate far more."), ("4", "Too small, for the same reason.")])

P.qa(8, r"A glass contains \(500\) cc of milk and a cup contains \(500\) cc of water. From the glass, \(150\) cc of milk is transferred to the cup and mixed thoroughly. Next, \(150\) cc of this mixture is transferred from the cup to the glass. Now, the amount of water in the glass and the amount of milk in the cup are in the ratio",
 M("1 : 1", "10 : 3", "10 : 13", "3 : 10"), "MCQ", "1", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Each container ends with 500 cc. Whatever water left the cup had to be replaced by milk.",
 steps(("Volumes", p("After both transfers, the glass and the cup each hold 500 cc again.")),
       ("The swap", p("The cup lost some water to the glass. Since its volume is back to 500, it must have gained exactly that much milk. So the two amounts are equal."))) +
 final(r"\(1 : 1\), option 1"),
 shortcut=r"Check by numbers: the cup sends back \(\tfrac{150 \times 500}{650} = \tfrac{1500}{13}\) cc of water, and keeps \(150 - \tfrac{450}{13} = \tfrac{1500}{13}\) cc of milk.",
 concept=p("If both containers end with the volumes they started with, each has gained exactly as much of the other liquid as it lost of its own."),
 why_rows=[("2", "Compares water in the glass with milk sent back, not milk kept."), ("3", "Compares the water in the glass with all 150 cc of milk first moved, not the milk left in the cup."), ("4", "Option 2 turned upside down.")])

P.qa(9, r"Nitu has an initial capital of ₹\(20,000\). Out of this, she invests ₹\(8,000\) at \(5.5\%\) in bank A, ₹\(5,000\) at \(5.6\%\) in bank B and the remaining amount at \(x\%\) in bank C; each rate being simple interest per annum. Her combined annual interest income from these investments is equal to \(5\%\) of the initial capital. If she had invested her entire initial capital in bank C alone, then her annual interest income, in rupees, would have been",
 M("900", "800", "1000", "700"), "MCQ", "2", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Work out the yearly interest from banks A and B, and what is left for bank C.",
 steps(("A and B", p("₹8,000 at 5.5% gives ₹440; ₹5,000 at 5.6% gives ₹280. Together ₹720.")),
       ("Bank C", p(r"The total should be 5% of ₹20,000, which is ₹1,000. So ₹7,000 in bank C earns ₹280, and \(x = 4\).")),
       ("All in C", p("4% of ₹20,000 is ₹800."))) + final(r"\(800\), option 2"),
 concept=r"\[SI = \frac{PRT}{100}\]",
 why_rows=[("1", "That would need a rate of 4.5%."), ("3", "That is the income from the actual split."), ("4", "That would need a rate of 3.5%.")])

P.qa(10, r"Two cars travel from different locations at constant speeds. To meet each other after starting at the same time, they take \(1.5\) hours if they travel towards each other, but \(10.5\) hours if they travel in the same direction. If the speed of the slower car is \(60\) km/hr, then the distance travelled, in km, by the slower car when it meets the other car while travelling towards each other, is",
 M("100", "90", "150", "120"), "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "The slower car’s distance is just 60 × 1.5. The rest of the information isn’t needed.",
 steps(("Reading the question", p(r"When they travel towards each other they meet after 1.5 hours. The slower car covers \(60 \times 1.5 = 90\) km.")),
       ("Checking it’s consistent", p(r"With faster speed \(u\): \(1.5(u + 60) = 10.5(u - 60)\) gives \(u = 80\). That only confirms the setup."))) + final(r"\(90\), option 2"),
 concept=r"\[\text{towards: } \frac{D}{u + v}, \qquad \text{same direction: } \frac{D}{u - v}\]",
 why_rows=[("1", "Not 60 × 1.5."), ("3", "Not 60 × 1.5."), ("4", "That is the faster car’s distance.")])

P.qa(11, r"The arithmetic mean of all the distinct numbers that can be obtained by rearranging the digits in \(1421\), including itself, is",
 M("2442", "3333", "2592", "2222"), "MCQ", "4", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "Each place value sees the same mix of digits. Find the average digit in one place.",
 steps(("How many numbers", p(r"The digits 1, 1, 2, 4 give \(\tfrac{4!}{2!} = 12\) distinct numbers.")),
       ("One place", p(r"In any one position, 1 appears 6 times, 2 appears 3 times and 4 appears 3 times. The average digit there is \(\tfrac{6 + 6 + 12}{12} = 2\).")),
       ("The mean", p("Every position averages 2, so the mean is 2222."))) + final(r"\(2222\), option 4"),
 shortcut="The average digit is (1 + 1 + 2 + 4) ÷ 4 = 2, and every position averages to it.",
 concept=r"\[\text{mean of all arrangements} = \bar{d} \times 111\ldots1\]",
 why_rows=[("1", "Not the average of these numbers."), ("2", "That would need an average digit of 3."), ("3", "Not the average of these numbers.")])

P.qa(12, r"The lengths of all four sides of a quadrilateral are integer valued. If three of its sides are of length \(1\) cm, \(2\) cm and \(4\) cm, then the total number of possible lengths of the fourth side is",
 M("5", "4", "3", "6"), "MCQ", "1", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "Every side of a quadrilateral is shorter than the sum of the other three.",
 steps(("Upper limit", p(r"\(x < 1 + 2 + 4 = 7\).")),
       ("Lower limit", p(r"The 4 cm side must also be shorter than the rest: \(4 < 1 + 2 + x\), so \(x > 1\).")),
       ("Counting", p(r"\(x = 2, 3, 4, 5, 6\): 5 lengths."))) + trap("The lower limit comes from the 4 cm side, not from the new one.") + final(r"\(5\), option 1"),
 concept=r"\[\text{each side} < \text{sum of the other three}\]",
 why_rows=[("2", "Leaves out one value, usually 2 or 6."), ("3", "Too few."), ("4", "Includes 1, which fails the 4 cm condition.")])

P.qa(13, r"The average of all \(3\)-digit terms in the arithmetic progression \(38, 55, 72, \ldots\), is",
 [], "TITA", "548", ["Algebra::Progressions_and_Series"], "Easy",
 "Find the first and last 3-digit terms. In an AP, the average is the average of those two.",
 steps(("First 3-digit term", p(r"Terms are \(38 + 17k\). The first above 100 is \(38 + 68 = 106\).")),
       ("Last 3-digit term", p(r"\(38 + 17 \times 56 = 990\); the next is 1007.")),
       ("Average", p(r"\(\tfrac{106 + 990}{2} = 548\)."))) + final(r"\(548\)"),
 concept=r"\[\text{average of an AP} = \frac{\text{first} + \text{last}}{2}\]")

P.qa(14, r"In an examination, the average marks of students in sections A and B are \(32\) and \(60\), respectively. The number of students in section A is \(10\) less than that in section B. If the average marks of all the students across both the sections combined is an integer, then the difference between the maximum and minimum possible number of students in section A is",
 [], "TITA", "63", ["Arithmetic::Average", "Number_System::Factors_and_Divisibility"], "Medium",
 r"Let A have \(a\) students. Write the combined average as a whole number plus a fraction.",
 steps(("Combined average", r"\[\frac{32a + 60(a + 10)}{2a + 10} = \frac{46a + 300}{a + 5} = 46 + \frac{70}{a + 5}\]"),
       ("When it’s an integer", p(r"\(a + 5\) must divide 70 and be at least 6: 7, 10, 14, 35 or 70. So \(a = 2, 5, 9, 30, 65\).")),
       ("Difference", p(r"\(65 - 2 = 63\)."))) + final(r"\(63\)"),
 concept=r"\[\frac{pa + q}{a + r} = p + \frac{q - pr}{a + r}\]")

P.qa(15, r"Let \(r\) be a real number and \(f(x) = \begin{cases} 2x - r & \text{if } x \ge r \\ r & \text{if } x < r \end{cases}\). Then, the equation \(f(x) = f(f(x))\) holds for all real",
 M(r"x \le r", "x > r", r"x \ge r", r"x \ne r"), "MCQ", "1", ["Algebra::Functions"], "Medium",
 r"Treat \(x < r\) and \(x \ge r\) separately.",
 steps(("x < r", p(r"\(f(x) = r\), and \(f(r) = 2r - r = r\). So \(f(f(x)) = f(x)\) for every \(x < r\).")),
       ("x ≥ r", p(r"\(f(x) = 2x - r \ge r\), so \(f(f(x)) = 2(2x - r) - r = 4x - 3r\). This equals \(2x - r\) only when \(x = r\).")),
       ("Together", p(r"It holds for \(x < r\) and for \(x = r\): that is, \(x \le r\)."))) + final(r"\(x \le r\), option 1"),
 concept=p("For a piecewise function, check each piece and the boundary point."),
 why_rows=[("2", r"For \(x > r\), \(f(f(x)) = 4x - 3r \ne 2x - r\)."), ("3", r"Only \(x = r\) works on this side."), ("4", r"It fails for every \(x > r\), and does hold at \(x = r\).")])

P.qa(16, r"In a triangle \(ABC\), \(AB = AC = 8\) cm. A circle drawn with \(BC\) as diameter passes through \(A\). Another circle drawn with centre at \(A\) passes through \(B\) and \(C\). Then the area, in sq. cm, of the overlapping region between the two circles is",
 M(r"16(\pi - 1)", r"32\pi", r"32(\pi - 1)", r"16\pi"), "MCQ", "3", ["Geometry::Circles"], "Medium",
 "A lies on the circle with diameter BC, so the angle at A is 90°. The two circles meet at B and C.",
 steps(("The shape", p(r"\(BC = 8\sqrt2\), so the first circle has radius \(4\sqrt2\). The second circle has radius 8 and centre A. The overlap is cut by chord BC into two pieces.")),
       ("On A’s side of BC", p(r"The half of the first circle on A’s side lies inside the second circle: \(\tfrac12 \pi (4\sqrt2)^2 = 16\pi\).")),
       ("On the far side of BC", p(r"The segment of the second circle beyond BC lies inside the first circle. It is a quarter circle minus triangle ABC: \(\tfrac14 \pi (8)^2 - \tfrac12 (8)(8) = 16\pi - 32\).")),
       ("Total", p(r"\(16\pi + 16\pi - 32 = 32(\pi - 1)\)."))) + final(r"\(32(\pi - 1)\), option 3"),
 concept=r"\[\text{segment} = \text{sector} - \text{triangle}\]",
 why_rows=[("1", "Half the correct area."), ("2", "Leaves out the triangle that has to be subtracted."), ("4", "Only the semicircle on A’s side.")])

P.qa(17, r"A school has less than \(5000\) students and if the students are divided equally into teams of either \(9\) or \(10\) or \(12\) or \(25\) each, exactly \(4\) are always left out. However, if they are divided into teams of \(11\) each, no one is left out. The maximum number of teams of \(12\) each that can be formed out of the students in the school is",
 [], "TITA", "150", ["Number_System::Remainders"], "Medium",
 "The number of students is 4 more than a multiple of LCM(9, 10, 12, 25).",
 steps(("The form", p(r"LCM(9, 10, 12, 25) = 900, so the number is \(900k + 4\): 904, 1804, 2704, 3604 or 4504.")),
       ("Divisible by 11", p(r"Only \(1804 = 11 \times 164\) works.")),
       ("Teams of 12", p(r"\(1804 = 12 \times 150 + 4\), so 150 teams."))) + final(r"\(150\)"),
 shortcut=r"\(900 \equiv 9 \pmod{11}\), so \(900k + 4 \equiv 9k + 4\). This is 0 when \(k = 2\).",
 concept=r"\[N \equiv r \pmod{a}, \pmod{b}, \ldots \;\Rightarrow\; N = \text{LCM}(a, b, \ldots)\,k + r\]")

P.qa(18, r"The minimum possible value of \(\dfrac{x^2 - 6x + 10}{3 - x}\), for \(x < 3\), is",
 M("-2", "2", r"\tfrac12", r"-\tfrac12"), "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 r"Put \(t = 3 - x\), which is positive.",
 steps(("Rewriting", p(r"\(x^2 - 6x + 10 = (x - 3)^2 + 1 = t^2 + 1\). So the expression is \(\tfrac{t^2 + 1}{t} = t + \tfrac1t\).")),
       ("Minimum", p(r"For \(t > 0\), \(t + \tfrac1t \ge 2\), with equality at \(t = 1\) (\(x = 2\))."))) + final(r"\(2\), option 2"),
 concept=r"\[t + \frac1t \ge 2 \quad (t > 0)\]",
 why_rows=[("1", r"The expression is positive for \(x < 3\)."), ("3", r"Less than the minimum of \(t + \tfrac1t\)."), ("4", "The expression is positive.")])

P.qa(19, r"A donation box can receive only cheques of ₹\(100\), ₹\(250\), and ₹\(500\). On one good day, the donation box was found to contain exactly \(100\) cheques amounting to a total sum of ₹\(15250\). Then, the maximum possible number of cheques of ₹\(500\) that the donation box may have contained, is",
 [], "TITA", "12", ["Algebra::Linear_Equations"], "Medium",
 "Use the count of cheques to remove one variable.",
 steps(("Equations", p(r"With \(a, b, c\) cheques of ₹100, ₹250, ₹500: \(a + b + c = 100\) and \(2a + 5b + 10c = 305\).")),
       ("Removing a", p(r"Subtract twice the first: \(3b + 8c = 105\). So \(c\) must be a multiple of 3, and \(8c \le 105\).")),
       ("Largest c", p(r"\(c = 12\) gives \(b = 3\) and \(a = 85\), which all work."))) + final(r"\(12\)"),
 concept=p("For an equation like px + qy = n in whole numbers, use remainders to see which values are allowed."))

P.qa(20, r"Moody takes \(30\) seconds to finish riding an escalator if he walks on it at his normal speed in the same direction. He takes \(20\) seconds to finish riding the escalator if he walks at twice his normal speed in the same direction. If Moody decides to stand still on the escalator, then the time, in seconds, needed to finish riding the escalator is",
 [], "TITA", "60", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Let the escalator have length L. Write his speed plus the escalator’s speed in each case.",
 steps(("Two speeds", p(r"\(m + e = \tfrac{L}{30}\) and \(2m + e = \tfrac{L}{20}\).")),
       ("Subtracting", p(r"\(m = \tfrac{L}{20} - \tfrac{L}{30} = \tfrac{L}{60}\), so \(e = \tfrac{L}{30} - \tfrac{L}{60} = \tfrac{L}{60}\).")),
       ("Standing still", p(r"At speed \(\tfrac{L}{60}\) the ride takes 60 seconds."))) + final(r"\(60\)"),
 concept=r"\[\text{speed on an escalator} = \text{walking speed} + \text{escalator speed}\]")

P.qa(21, r"Two ships are approaching a port along straight routes at constant speeds. Initially, the two ships and the port formed an equilateral triangle with sides of length \(24\) km. When the slower ship travelled \(8\) km, the triangle formed by the new positions of the two ships and the port became right-angled. When the faster ship reaches the port, the distance, in km, between the other ship and the port will be",
 M("4", "6", "12", "8"), "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance", "Geometry::Triangles"], "Hard",
 "The angle at the port stays 60°. So the right angle must be at one of the ships.",
 steps(("Where the right angle is", p("The slower ship is now 16 km from the port. If the right angle were at the slower ship, the faster one would be 16 ÷ cos 60° = 32 km away, more than it started with. So the right angle is at the faster ship, which is 16 × cos 60° = 8 km from the port.")),
       ("Speeds", p("In the same time the slower ship went 8 km and the faster ship 16 km, so the faster ship is twice as fast.")),
       ("The rest", p("The faster ship has 8 km left. In that time the slower ship covers 4 km, leaving it 16 − 4 = 12 km from the port."))) +
 final(r"\(12\), option 3"),
 concept=p(r"In a right triangle with a \(60^\circ\) angle, the side next to that angle is half the hypotenuse."),
 why_rows=[("1", "That is how far the slower ship moves, not where it ends up."), ("2", "Uses the wrong speed ratio."), ("4", "That is the faster ship’s distance at the right-angle moment.")])

P.qa(22, r"Bob can finish a job in \(40\) days, if he works alone. Alex is twice as fast as Bob and thrice as fast as Cole in the same job. Suppose Alex and Bob work together on the first day, Bob and Cole work together on the second day, Cole and Alex work together on the third day, and then, they continue the work by repeating this three-day roster, with Alex and Bob working together on the fourth day, and so on. Then, the total number of days Alex would have worked when the job gets finished, is",
 [], "TITA", "11", ["Arithmetic::Time_and_Work"], "Medium",
 "Take the job as 120 units. Find each person’s daily output.",
 steps(("Rates", p("Bob takes 40 days, Alex 20 and Cole 60. Out of 120 units, they do 3, 6 and 2 a day.")),
       ("One cycle", p("Alex + Bob 9, Bob + Cole 5, Cole + Alex 8: 22 units in 3 days, with Alex working 2 of them.")),
       ("Finishing", p("Five cycles (15 days) give 110 units, with Alex working 10 days. Day 16 (Alex + Bob) brings it to 119, and day 17 (Bob + Cole) finishes it. Alex worked 11 days."))) + trap("Count Alex’s days, not the total days. The job takes 17 days, but Alex works on only 11 of them.") + final(r"\(11\)"),
 concept=p("Take the whole job as the LCM of the individual times, so every rate is a whole number."))
