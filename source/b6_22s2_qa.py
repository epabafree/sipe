# -*- coding: utf-8 -*-
# Batch 6 — CAT 2022 Slot 2: QA Q1–22 (exam order).
from fmt import steps, final, why, table, p
from b6_22s2 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"Working alone, the time taken by Anu, Tanu and Manu to complete any job are in the ratio \(5 : 8 : 10\). They accept a job which they can finish in \(4\) days if they all work together for \(8\) hours per day. However, Anu and Tanu work together for the first \(6\) days, working \(6\) hours \(40\) minutes per day. Then, the number of hours that Manu will take to complete the remaining job working alone is",
 [], "TITA", "6", ["Arithmetic::Time_and_Work"], "Medium",
 "Times in the ratio 5 : 8 : 10 mean rates in the ratio 1/5 : 1/8 : 1/10. Clear the fractions.",
 steps(("Rates", p(r"Multiplying \(\tfrac15 : \tfrac18 : \tfrac1{10}\) by 40 gives rates of 8, 5 and 4 units an hour.")),
       ("Size of the job", p(r"All three together do 17 units an hour for \(4 \times 8 = 32\) hours: 544 units.")),
       ("What’s left", p(r"Anu and Tanu do 13 units an hour for \(6 \times 6\tfrac23 = 40\) hours: 520 units. The remaining 24 units take Manu \(24 \div 4 = 6\) hours."))) + final(r"\(6\)"),
 shortcut="6 hours 40 minutes for 6 days is exactly 40 hours, which keeps the arithmetic clean.",
 concept=r"\[\text{work} = \text{rate} \times \text{time}, \qquad \text{rate} \propto \frac{1}{\text{time}}\]")

P.qa(2, r"Mr. Pinto invests one-fifth of his capital at \(6\%\), one-third at \(10\%\) and the remaining at \(1\%\), each rate being simple interest per annum. Then, the minimum number of years required for the cumulative interest income from these investments to equal or exceed his initial capital is",
 [], "TITA", "20", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Work out the overall yearly rate on the whole capital.",
 steps(("Yearly interest", p(r"The remaining share is \(1 - \tfrac15 - \tfrac13 = \tfrac{7}{15}\). Yearly interest as a fraction of capital:") +
         r"\[\tfrac15(6\%) + \tfrac13(10\%) + \tfrac{7}{15}(1\%) = \tfrac{18 + 50 + 7}{15}\% = 5\%\]"),
       ("Years needed", p(r"At 5% a year, simple interest reaches 100% of the capital in 20 years."))) + final(r"\(20\)"),
 shortcut="Take a capital of 1500: 300 at 6%, 500 at 10%, 700 at 1% earn 18 + 50 + 7 = 75 a year, which is 5%.",
 concept=r"\[SI = \frac{PRT}{100}\]")

P.qa(3, r"Regular polygons A and B have number of sides in the ratio \(1 : 2\) and interior angles in the ratio \(3 : 4\). Then, the number of sides of B equals",
 [], "TITA", "10", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 r"An interior angle of a regular \(n\)-gon is \(\tfrac{(n - 2)180}{n}\).",
 steps(("Setting up", p(r"Let A have \(n\) sides and B \(2n\). Then") + r"\[\frac{(n - 2)/n}{(2n - 2)/2n} = \frac34 \;\Rightarrow\; \frac{2(n - 2)}{2n - 2} = \frac34\]"),
       ("Solving", r"\[8(n - 2) = 3(2n - 2) \;\Rightarrow\; 2n = 10\]" + p(r"So A is a pentagon and B has 10 sides."))) + final(r"\(10\)"),
 shortcut="Check: a pentagon’s angle is 108° and a decagon’s is 144°; 108 : 144 = 3 : 4.",
 concept=r"\[\text{interior angle} = 180^\circ - \frac{360^\circ}{n}\]")

P.qa(4, r"The number of distinct integer values of \(n\) satisfying \(\dfrac{4 - \log_2 n}{3 - \log_4 n} < 0\) is",
 [], "TITA", "47", ["Algebra::Logarithms_and_Exponents", "Algebra::Inequalities_and_Absolute_Value"], "Medium",
 r"Write \(\log_4 n\) as \(\tfrac12 \log_2 n\) and call \(\log_2 n = u\).",
 steps(("One variable", r"\[\frac{4 - u}{3 - u/2} = \frac{2(4 - u)}{6 - u} < 0\]"),
       ("Signs", p(r"The fraction is negative when the numerator and denominator have opposite signs, which happens for \(4 < u < 6\).")),
       ("Back to n", p(r"\(16 < n < 64\), so \(n = 17, 18, \dots, 63\): 47 values."))) + final(r"\(47\)"),
 shortcut="The fraction changes sign only at u = 4 and u = 6, so the answer is the integers strictly between 2⁴ and 2⁶.",
 concept=r"\[\log_{b^k} x = \tfrac1k \log_b x\]")

P.qa(5, r"The average of a non-decreasing sequence of \(N\) numbers \(a_1, a_2, \dots, a_N\) is \(300\). If \(a_1\) is replaced by \(6a_1\), the new average becomes \(400\). Then, the number of possible values of \(a_1\) is",
 [], "TITA", "14", ["Arithmetic::Average"], "Medium",
 r"The change in total is \(5a_1\), and it raises the average by 100.",
 steps(("Finding a₁", r"\[5a_1 = 100N \;\Rightarrow\; a_1 = 20N\]"),
       ("Limits on N", p(r"\(a_1\) is the smallest term, so it can’t exceed the average: \(20N \le 300\), so \(N \le 15\). \(N = 1\) doesn’t work, because then \(a_1\) would have to be 300 and 20 at once.")),
       ("Counting", p(r"\(N = 2, 3, \dots, 15\) each give one value of \(a_1\): 14 values."))) + final(r"\(14\)"),
 shortcut="The smallest number in a list can’t exceed the list’s average; that alone bounds N.",
 concept=r"\[\min \le \text{average} \le \max\]")

P.qa(6, r"If \(a\) and \(b\) are non-negative real numbers such that \(a + 2b = 6\), then the average of the maximum and minimum possible values of \((a + b)\) is",
 M("3.5", "4.5", "3", "4"), "MCQ", "2", ["Algebra::Linear_Equations"], "Easy",
 r"Write \(a + b\) in terms of \(b\) alone.",
 steps(("One variable", p(r"\(a + b = 6 - b\), with \(0 \le b \le 3\).")),
       ("Extremes", p(r"Largest at \(b = 0\): 6. Smallest at \(b = 3\): 3. Their average is 4.5."))) + final(r"\(4.5\), option 2"),
 concept=r"\[\text{a linear expression on an interval is extreme at its ends}\]",
 why_rows=[("1", "The range is 3 to 6."), ("3", "That is only the minimum."), ("4", "The range is 3 to 6, so the average is 4.5.")])

P.qa(7, r"The length of each side of an equilateral triangle \(ABC\) is \(3\) cm. Let \(D\) be a point on \(BC\) such that the area of triangle \(ADC\) is half the area of triangle \(ABD\). Then, the length of \(AD\), in cm, is",
 M(r"\sqrt7", r"\sqrt6", r"\sqrt8", r"\sqrt5"), "MCQ", "1", ["Geometry::Triangles"], "Easy",
 "The two triangles share the same height from A, so their areas are in the ratio of their bases.",
 steps(("Where D is", p(r"\(DC : BD = 1 : 2\), so \(BD = 2\) and \(DC = 1\).")),
       ("Length of AD", p(r"Let M be the midpoint of BC. Then \(AM = \tfrac{3\sqrt3}{2}\) and \(DM = 2 - 1.5 = 0.5\).") +
         r"\[AD^2 = \tfrac{27}{4} + \tfrac14 = 7\]")) + final(r"\(\sqrt7\), option 1"),
 shortcut=r"Cosine rule in triangle ABD: \(AD^2 = 9 + 4 - 2 \cdot 3 \cdot 2 \cos 60^\circ = 7\).",
 concept=r"\[\text{same height} \Rightarrow \text{area ratio} = \text{base ratio}\]",
 why_rows=[("2", "AD can’t be shorter than the altitude, which is about 2.6 cm."), ("3", "D would then be about 1.1 cm from the midpoint, which doesn’t split BC as 2 : 1."), ("4", "AD can’t be shorter than the altitude, which is about 2.6 cm.")])

P.qa(8, r"The number of integers greater than \(2000\) that can be formed with the digits \(0, 1, 2, 3, 4, 5\), using each digit at most once, is",
 M("1480", "1440", "1200", "1420"), "MCQ", "2", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "Count 4-, 5- and 6-digit numbers separately. Only the 4-digit case needs care.",
 steps(("4 digits", p(r"The first digit must be 2 to 5: \(4 \times 5 \times 4 \times 3 = 240\). All of these exceed 2000, since 2000 itself repeats a digit.")),
       ("5 and 6 digits", p(r"First digit 1 to 5. Five digits: \(5 \times 5 \times 4 \times 3 \times 2 = 600\). Six digits: \(5 \times 5! = 600\).")),
       ("Total", p(r"\(240 + 600 + 600 = 1440\)."))) + final(r"\(1440\), option 2"),
 concept=r"\[\text{first digit can’t be 0; the rest are arrangements of what’s left}\]",
 why_rows=[("1", "The count is 240 + 600 + 600 = 1440."), ("3", "This leaves out the 4-digit numbers."), ("4", "The count is 240 + 600 + 600 = 1440.")])

P.qa(9, r"Let \(f(x)\) be a quadratic polynomial in \(x\) such that \(f(x) \ge 0\) for all real numbers \(x\). If \(f(2) = 0\) and \(f(4) = 6\), then \(f(-2)\) is equal to",
 M("36", "12", "24", "6"), "MCQ", "3", ["Algebra::Quadratic_Equations"], "Easy",
 r"A quadratic that is never negative and touches zero at \(x = 2\) has a double root there.",
 steps(("Its form", p(r"\(f(x) = k(x - 2)^2\). From \(f(4) = 4k = 6\), \(k = 1.5\).")),
       ("Evaluating", p(r"\(f(-2) = 1.5 \times 16 = 24\)."))) + final(r"\(24\), option 3"),
 shortcut="f(−2) is four times the distance-squared of f(4) from the root: 16/4 × 6 = 24.",
 concept=r"\[f(x) \ge 0,\ f(r) = 0 \;\Rightarrow\; f(x) = k(x - r)^2,\ k > 0\]",
 why_rows=[("1", "This uses k = 2.25."), ("2", "This uses k = 0.75."), ("4", "That is f(4), not f(−2).")])

P.qa(10, r"Manu earns ₹ \(4000\) per month and wants to save an average of ₹ \(550\) per month in a year. In the first nine months, his monthly expense was ₹ \(3500\), and he foresees that, tenth month onwards, his monthly expense will increase to ₹ \(3700\). In order to meet his yearly savings target, his monthly earnings, in rupees, from the tenth month onwards should be",
 M("4350", "4400", "4300", "4200"), "MCQ", "2", ["Arithmetic::Average"], "Easy",
 "Work out how much he still needs to save in the last three months.",
 steps(("Savings so far", p(r"Target \(550 \times 12 = 6600\). First nine months: \(9 \times 500 = 4500\).")),
       ("The last three months", p(r"He needs 2100 more, or 700 a month. With expenses of 3700 he must earn 4400."))) + final(r"₹ \(4400\), option 2"),
 concept=r"\[\text{savings} = \text{earnings} - \text{expenses}\]",
 why_rows=[("1", "This leaves him 150 short."), ("3", "This leaves him 300 short."), ("4", "This leaves him 600 short.")])

P.qa(11, r"In an election, there were four candidates and \(80\%\) of the registered voters casted their votes. One of the candidates received \(30\%\) of the casted votes while the other three candidates received the remaining casted votes in the proportion \(1 : 2 : 3\). If the winner of the election received \(2512\) votes more than the candidate with the second highest votes, then the number of registered voters was",
 M("62800", "50240", "40192", "60288"), "MCQ", "1", ["Arithmetic::Percentages"], "Easy",
 "Split the remaining 70% in the ratio 1 : 2 : 3.",
 steps(("Shares", p(r"The 70% splits into about 11.7%, 23.3% and 35%. The winner has 35% and the runner-up 30%.")),
       ("Votes cast", p(r"The 5% gap is 2512 votes, so 50,240 votes were cast.")),
       ("Registered voters", p(r"\(50240 \div 0.8 = 62800\)."))) + final(r"\(62800\), option 1"),
 concept=r"\[\text{part of a part: multiply the percentages}\]",
 why_rows=[("2", "That is the number of votes cast."), ("3", "This takes 80% of the votes cast instead of dividing."), ("4", "This uses the wrong gap between the top two.")])

P.qa(12, r"On day one, there are \(100\) particles in a laboratory experiment. On day \(n\), where \(n \ge 2\), one out of every \(n\) particles produces another particle. If the total number of particles in the laboratory experiment increases to \(1000\) on day \(m\), then \(m\) equals",
 M("19", "17", "16", "18"), "MCQ", "1", ["Algebra::Progressions_and_Series"], "Medium",
 r"On day \(n\) the count is multiplied by \(1 + \tfrac1n = \tfrac{n + 1}{n}\).",
 steps(("A telescoping product", r"\[100 \times \frac32 \times \frac43 \times \cdots \times \frac{m + 1}{m} = 100 \times \frac{m + 1}{2}\]"),
       ("Solving", p(r"\(50(m + 1) = 1000\), so \(m = 19\)."))) + final(r"\(19\), option 1"),
 shortcut="Day 2 gives 150, day 3 gives 200: the count goes up by 50 a day, so it reaches 1000 on day 19.",
 concept=r"\[\prod_{n=2}^{m} \frac{n + 1}{n} = \frac{m + 1}{2}\]",
 why_rows=[("2", "Day 17 has 900 particles."), ("3", "Day 16 has 850."), ("4", "Day 18 has 950.")])

P.qa(13, r"There are two containers of the same volume; the first container half-filled with sugar syrup and the second container half-filled with milk. Half the content of the first container is transferred to the second container, and then the half of this mixture is transferred back to the first container. Next, half the content of the first container is transferred back to the second container. Then, the ratio of sugar syrup and milk in the second container is",
 M("6 : 5", "5 : 6", "4 : 5", "5 : 4"), "MCQ", "2", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Use 8 units of syrup and 8 of milk, and track both liquids through each step.",
 steps(("Step 1", p("Half the syrup moves across. First: 4 syrup. Second: 4 syrup, 8 milk.")),
       ("Step 2", p("Half the second container (2 syrup, 4 milk) goes back. First: 6 syrup, 4 milk. Second: 2 syrup, 4 milk.")),
       ("Step 3", p("Half the first container (3 syrup, 2 milk) moves across. Second: 5 syrup, 6 milk."))) + final(r"\(5 : 6\), option 2"),
 concept=r"\[\text{moving half a mixture moves half of each part}\]",
 why_rows=[("1", "This is the ratio the wrong way round."), ("3", "The second container ends with 5 parts syrup and 6 parts milk."), ("4", "The second container ends with 5 parts syrup and 6 parts milk.")])

P.qa(14, r"Five students, including Amit, appear for an examination in which possible marks are integers between \(0\) and \(50\), both inclusive. The average marks for all the students is \(38\) and exactly three students got more than \(32\). If no two students got the same marks and Amit got the least marks among the five students, then the difference between the highest and lowest possible marks of Amit is",
 M("22", "20", "21", "24"), "MCQ", "2", ["Arithmetic::Average"], "Hard",
 "The total is 190. Two students, Amit and one other, have 32 or less.",
 steps(("Amit’s highest", p("The two lower students can share at most 32 + 31 = 63, so the top three need at least 127, which is possible (say 41, 42, 44). With the other student at 32, Amit gets 190 − 127 − 32 = 31.")),
       ("Amit’s lowest", p("Make the top three as large as possible: 50 + 49 + 48 = 147. The other student takes 32, leaving Amit 190 − 147 − 32 = 11.")),
       ("The difference", p("31 − 11 = 20."))) + final(r"\(20\), option 2"),
 concept=r"\[\text{to push one value to an extreme, push the others the opposite way}\]",
 why_rows=[("1", "Amit’s marks range from 11 to 31, a difference of 20."), ("3", "Amit’s marks range from 11 to 31, a difference of 20."), ("4", "Amit’s marks range from 11 to 31, a difference of 20.")])

P.qa(15, r"Two ships meet mid-ocean, and then, one ship goes south and the other ship goes west, both travelling at constant speeds. Two hours later, they are \(60\) km apart. If the speed of one of the ships is \(6\) km per hour more than the other one, then the speed, in km per hour, of the slower ship is",
 M("24", "18", "20", "12"), "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance", "Geometry::Triangles"], "Easy",
 "South and west are at right angles, so use Pythagoras.",
 steps(("After two hours", r"\[(2v)^2 + (2v + 12)^2 = 60^2 \;\Rightarrow\; v^2 + 6v - 432 = 0\]"),
       ("Solving", p(r"\((v + 24)(v - 18) = 0\), so \(v = 18\)."))) + final(r"\(18\), option 2"),
 shortcut="After two hours the distances are 36 and 48, a 3-4-5 triangle scaled by 12.",
 concept=r"\[a^2 + b^2 = c^2\]",
 why_rows=[("1", "That is the faster ship."), ("3", "40 and 52 don’t give 60."), ("4", "24 and 36 don’t give 60.")])

P.qa(16, r"For some natural number \(n\), assume that \((15{,}000)!\) is divisible by \((n!)!\). The largest possible value of \(n\) is",
 M("5", "4", "6", "7"), "MCQ", "4", ["Number_System::Factorials"], "Easy",
 r"\(a!\) divides \(b!\) exactly when \(a \le b\).",
 steps(("The condition", p(r"We need \(n! \le 15000\).")),
       ("Checking", p(r"\(7! = 5040\) works, \(8! = 40320\) is too big."))) + final(r"\(7\), option 4"),
 concept=r"\[a \le b \Rightarrow a! \mid b!\]",
 why_rows=[("1", "Works, but isn’t the largest."), ("2", "Works, but isn’t the largest."), ("3", "Works, but 7 also works.")])

P.qa(17, r"Suppose for all integers \(x\), there are two functions \(f\) and \(g\) such that \(f(x) + f(x - 1) - 1 = 0\) and \(g(x) = x^2\). If \(f(x^2 - x) = 5\), then the value of the sum \(f(g(5)) + g(f(5))\) is",
 [], "TITA", "12", ["Algebra::Functions"], "Medium",
 r"\(f(x) = 1 - f(x - 1)\), so \(f\) takes one value at even numbers and another at odd numbers.",
 steps(("Even and odd", p(r"\(x^2 - x = x(x - 1)\) is always even, so \(f(\text{even}) = 5\) and \(f(\text{odd}) = 1 - 5 = -4\).")),
       ("Evaluating", p(r"\(f(g(5)) = f(25) = -4\). \(g(f(5)) = (-4)^2 = 16\). The sum is 12."))) + final(r"\(12\)"),
 concept=r"\[f(x) + f(x - 1) = c \;\Rightarrow\; f \text{ alternates between two values}\]")

P.qa(18, r"In triangle \(ABC\), altitudes \(AD\) and \(BE\) are drawn to the corresponding bases. If \(\angle BAC = 45^\circ\) and \(\angle ABC = \theta\), then \(\dfrac{AD}{BE}\) equals",
 M(r"\sqrt2 \cos\theta", "1", r"\sqrt2 \sin\theta", r"\dfrac{\sin\theta + \cos\theta}{\sqrt2}"), "MCQ", "3", ["Geometry::Triangles", "Geometry::Trigonometry"], "Easy",
 "Write both altitudes in terms of side AB.",
 steps(("The altitudes", p(r"In triangle ABD, \(AD = AB \sin\theta\). In triangle ABE, \(BE = AB \sin 45^\circ = \tfrac{AB}{\sqrt2}\).")),
       ("The ratio", r"\[\frac{AD}{BE} = \sqrt2 \sin\theta\]")) + final("Option 3"),
 concept=r"\[\text{altitude from } A = AB \sin B\]",
 why_rows=[("1", "Uses cosine where sine is needed."), ("2", r"Only true when \(\theta = 45^\circ\)."), ("4", "Not what the two altitudes give.")])

P.qa(19, r"The number of integer solutions of the equation \(\left(x^2 - 10\right)^{\left(x^2 - 3x - 10\right)} = 1\) is",
 [], "TITA", "4", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "A power equals 1 in three ways: the base is 1, the exponent is 0 (with a non-zero base), or the base is −1 with an even exponent.",
 steps(("Base 1", p(r"\(x^2 = 11\): no integer solutions.")),
       ("Exponent 0", p(r"\(x^2 - 3x - 10 = (x - 5)(x + 2) = 0\): \(x = 5\) or \(-2\). The bases, 15 and −6, are non-zero.")),
       ("Base −1", p(r"\(x^2 = 9\): \(x = 3\) gives exponent −10 and \(x = -3\) gives 8, both even, so both work."))) + final(r"\(4\)"),
 concept=r"\[a^b = 1 \iff a = 1,\ \text{or } b = 0,\ a \ne 0,\ \text{or } a = -1,\ b \text{ even}\]")

P.qa(20, r"Let \(r\) and \(c\) be real numbers. If \(r\) and \(-r\) are roots of \(5x^3 + cx^2 - 10x + 9 = 0\), then \(c\) equals",
 M("4", "-4", r"-\dfrac92", r"\dfrac92"), "MCQ", "3", ["Algebra::Equations_and_Polynomials"], "Medium",
 r"Substitute \(r\) and \(-r\), then add and subtract the two equations.",
 steps(("Two equations", r"\[5r^3 + cr^2 - 10r + 9 = 0 \qquad -5r^3 + cr^2 + 10r + 9 = 0\]"),
       ("Subtracting", p(r"\(10r^3 - 20r = 0\), so \(r^2 = 2\).")),
       ("Adding", p(r"\(2cr^2 + 18 = 0\), so \(c = -\tfrac{9}{r^2} = -\tfrac92\)."))) + final("Option 3"),
 shortcut=r"Product of roots: \(-r^2 \cdot s = -\tfrac95\); sum of pairwise products: \(-r^2 = -2\). So \(s = \tfrac{9}{10}\) and \(c = -5s = -\tfrac92\).",
 concept=r"\[\text{for } ax^3 + bx^2 + cx + d:\ \textstyle\sum \alpha = -\tfrac ba,\ \sum \alpha\beta = \tfrac ca,\ \alpha\beta\gamma = -\tfrac da\]",
 why_rows=[("1", r"Not what the equations give."), ("2", r"Not what the equations give."), ("4", "Sign error.")])

P.qa(21, r"Consider the arithmetic progression \(3, 7, 11, \dots\) and let \(A_n\) denote the sum of the first \(n\) terms of this progression. Then, the value of \(\dfrac{1}{25}\displaystyle\sum_{n=1}^{25} A_n\) is",
 M("442", "404", "455", "415"), "MCQ", "3", ["Algebra::Progressions_and_Series"], "Medium",
 r"First find \(A_n\) as a formula in \(n\).",
 steps(("The sum of n terms", r"\[A_n = \frac n2 \big(6 + 4(n - 1)\big) = 2n^2 + n\]"),
       ("Summing", r"\[\begin{aligned} \sum_{n=1}^{25} A_n &= 2 \cdot \frac{25 \cdot 26 \cdot 51}{6} + \frac{25 \cdot 26}{2} \\ &= 11050 + 325 = 11375 \end{aligned}\]"),
       ("Dividing", p(r"\(11375 \div 25 = 455\)."))) + final(r"\(455\), option 3"),
 concept=r"\[\sum_{k=1}^n k = \frac{n(n + 1)}{2} \qquad \sum_{k=1}^n k^2 = \frac{n(n + 1)(2n + 1)}{6}\]",
 why_rows=[("1", "Not the value of the sum."), ("2", "Not the value of the sum."), ("4", "Not the value of the sum.")])

P.qa(22, r"In an examination, there were \(75\) questions. \(3\) marks were awarded for each correct answer, \(1\) mark was deducted for each wrong answer and \(1\) mark was awarded for each unattempted question. Rayan scored a total of \(97\) marks in the examination. If the number of unattempted questions was higher than the number of attempted questions, then the maximum number of correct answers that Rayan could have given in the examination is",
 [], "TITA", "24", ["Arithmetic::Miscellaneous"], "Medium",
 r"Use \(c\), \(w\) and \(u\) for correct, wrong and unattempted, and remove \(u\).",
 steps(("Two equations", r"\[c + w + u = 75 \qquad 3c - w + u = 97\]" + p(r"Subtracting: \(2c - 2w = 22\), so \(w = c - 11\) and \(u = 86 - 2c\).")),
       ("The condition", p(r"\(u > c + w\) means \(86 - 2c > 2c - 11\), so \(c < 24.25\).")),
       ("Checking 24", p(r"\(c = 24\), \(w = 13\), \(u = 38\): 38 unattempted against 37 attempted, and \(72 - 13 + 38 = 97\)."))) + final(r"\(24\)"),
 concept=r"\[\text{eliminate a variable, then apply the inequality}\]")
