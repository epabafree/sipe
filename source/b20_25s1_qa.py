# -*- coding: utf-8 -*-
# Batch 20 — CAT 2025 Slot 1: QA Q1–22 (exam order).
from fmt import steps, final, trap, why, table, p
from b20_25s1 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, "The ratio of the number of students in the morning shift and afternoon shift of a school was 13 : 9. After 21 students moved from the morning shift to the afternoon shift, this ratio became 19 : 14. Next, some new students joined the morning and afternoon shifts in the ratio 3 : 8 and then the ratio of the number of students in the morning shift and the afternoon shift became 5 : 4. The number of new students who joined is",
 M("110", "121", "88", "99"), "MCQ", "4", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "Let the shifts be 13k and 9k. The move of 21 students fixes k.",
 steps(("After the move", p(r"\(\frac{13k - 21}{9k + 21} = \frac{19}{14}\) gives \(182k - 294 = 171k + 399\), so \(k = 63\): 798 and 588 after the move.")),
       ("New students", p(r"With \(3t\) and \(8t\) joining: \(\frac{798 + 3t}{588 + 8t} = \frac54\), so \(3192 + 12t = 2940 + 40t\) and \(t = 9\). That is \(11t = 99\) new students."))) + final(r"\(99\), option 4"),
 concept=r"\[\frac{a}{b} = \frac{m}{n} \;\Rightarrow\; na = mb\]",
 why_rows=[("1", "This is 11 × 10; t is 9."), ("2", "This is 11 × 11."), ("3", "This is 11 × 8.")])

P.qa(2, r"The number of distinct integers \(n\) for which \(\log_{\frac14}\left(n^2 - 7n + 11\right) \ge 0\), is",
 M("0", "1", r"\text{Infinite}", "2"), "MCQ", "4", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "With a base below 1, a log is non-negative when its argument lies in (0, 1].",
 steps(("Condition", p(r"\(0 < n^2 - 7n + 11 \le 1\).")),
       ("Integers", p(r"\(n^2 - 7n + 11\) takes the values 11, 5, 1, −1, −1, 1, 5, 11 for \(n = 0\) to 7, and grows beyond. Only \(n = 2\) and \(n = 5\) give a value in (0, 1]. For \(n = 3, 4\) the argument is negative, so the log isn’t defined."))) +
 trap("Solving n² − 7n + 11 &lt; 1 alone gives n = 3, 4, but there the argument is negative and the log doesn’t exist.") + final(r"\(2\), option 4"),
 concept=r"\[0 < b < 1: \;\; \log_b x \ge 0 \iff 0 < x \le 1\]",
 why_rows=[("1", "n = 2 and n = 5 both work."), ("2", "There are two such integers."), ("3", "Only finitely many integers keep the argument between 0 and 1.")])

P.qa(3, r"In a circle with center \(C\) and radius \(6\sqrt2\) cm, \(PQ\) and \(SR\) are two parallel chords separated by one of the diameters. If \(\angle PQC = 45^\circ\), and the ratio of the perpendicular distance of \(PQ\) and \(SR\) from \(C\) is 3 : 2, then the area, in sq. cm, of the quadrilateral \(PQRS\) is",
 M(r"20\left(3 + \sqrt{14}\right)", r"4\left(3 + \sqrt{14}\right)", r"4\left(3\sqrt2 + \sqrt7\right)", r"20\left(3\sqrt2 + \sqrt7\right)"), "MCQ", "1", ["Geometry::Circles"], "Medium",
 "Triangle PQC is isosceles with a 45° base angle, so it is right-angled at C.",
 steps(("Chord PQ", p(r"The distance from C to PQ is \(6\sqrt2 \cos 45^\circ = 6\), and \(PQ = 2 \times 6 = 12\).")),
       ("Chord SR", p(r"Its distance is \(\frac23 \times 6 = 4\), so half of SR is \(\sqrt{72 - 16} = 2\sqrt{14}\) and \(SR = 4\sqrt{14}\).")),
       ("Area", p(r"The chords are on opposite sides of C, so the trapezium’s height is \(6 + 4 = 10\). Area \(= \frac{12 + 4\sqrt{14}}{2} \times 10 = 20(3 + \sqrt{14})\)."))) + final("Option 1"),
 concept=r"\[\text{half-chord} = \sqrt{r^2 - d^2}\]",
 why_rows=[("2", "This uses a height of 2, as if both chords were on the same side."), ("3", "Wrong half-chord and height."), ("4", "Wrong half-chord for SR.")])

P.qa(4, "A container holds 200 litres of a solution of acid and water, having 30% acid by volume. Atul replaces 20% of this solution with water, then replaces 10% of the resulting solution with acid, and finally replaces 15% of the solution thus obtained, with water. The percentage of acid by volume in the final solution obtained after these three replacements, is nearest to",
 M("27", "25", "29", "23"), "MCQ", "1", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Track the acid in litres; the volume stays 200 throughout.",
 steps(p(r"Start: 60 L acid. Replace 20% with water: 48. Replace 10% with acid: \(48 \times 0.9 + 20 = 63.2\). Replace 15% with water: \(63.2 \times 0.85 = 53.72\). That is \(53.72 \div 200 \approx 26.9\%\).")) + final(r"\(27\%\), option 1"),
 concept=r"\[\text{replacing } f \text{ of a mix keeps } (1 - f) \text{ of each part, plus what is added}\]",
 why_rows=[("2", "This forgets the acid added in step 2."), ("3", "This forgets the last dilution."), ("4", "Too low: the acid added in step 2 is 20 litres.")])

P.qa(5, "Shruti travels a distance of 224 km in four parts for a total travel time of 3 hours. Her speeds in these four parts follow an arithmetic progression, and the corresponding time taken to cover these four parts follow another arithmetic progression. If she travels at a speed of 960 meters per minute for 30 minutes to cover the first part, then the distance, in meters, she travels in the fourth part is",
 M("76800", "112000", "86400", "96000"), "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Hard",
 "960 m/min is 57.6 km/h. Find the time step first.",
 steps(("Times", p(r"The four times are \(0.5\), \(0.5 + d\), \(0.5 + 2d\) and \(0.5 + 3d\) hours, adding to 3. So \(2 + 6d = 3\) and \(d = \frac16\) h: 30, 40, 50 and 60 minutes.")),
       ("Speeds", p(r"With speeds \(57.6 + ke\) km/h for \(k = 0\) to 3: \(57.6 \times 3 + e\left(\frac46 + \frac{10}{6} + 3\right) = 224\), so \(172.8 + \frac{16}{3}e = 224\) and \(e = 9.6\).")),
       ("Fourth part", p(r"Speed \(57.6 + 28.8 = 86.4\) km/h for 1 hour: 86.4 km, or 86400 m."))) + final(r"\(86400\), option 3"),
 concept=r"\[\text{distance} = \sum \text{speed}_i \times \text{time}_i\]",
 why_rows=[("1", "76.8 km/h is the third part’s speed, not the fourth."), ("2", "112 km is half the whole journey."), ("4", "96 km/h is one step beyond the fourth speed.")])

P.qa(6, r"The number of distinct pairs of integers \((x, y)\) satisfying the inequalities \(x > y \ge 3\) and \(x + y < 14\) is",
 [], "TITA", "16", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "Fix y from 3 upwards and count the x values.",
 steps(p(r"\(y = 3\): x from 4 to 10, 7 values. \(y = 4\): 5 to 9, 5 values. \(y = 5\): 6 to 8, 3 values. \(y = 6\): x = 7, 1 value. \(y = 7\): x would need to be 8 or more with \(x < 7\): none. Total 16.")) + final(r"\(16\)"),
 concept=r"\[\text{count by fixing one variable}\]")

P.qa(7, r"Let \(3 \le x \le 6\) and \([x^2] = [x]^2\), where \([x]\) is the greatest integer not exceeding \(x\). If set \(S\) represents all feasible values of \(x\), then a possible subset of \(S\) is",
 [r"\(\left(4, \sqrt{18}\right) \cup \left[5, \sqrt{27}\right) \cup \{6\}\)", r"\(\left[3, \sqrt{10}\right] \cup \left[4, \sqrt{17}\right] \cup \{6\}\)", r"\(\left(3, \sqrt{10}\right) \cup \left[5, \sqrt{26}\right) \cup \{6\}\)", r"\(\left[3, \sqrt{10}\right] \cup \left[5, \sqrt{26}\right]\)"],
 "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 r"On \([n, n+1)\), the condition is \(n^2 \le x^2 < n^2 + 1\).",
 steps(("Find S", p(r"\(S = [3, \sqrt{10}) \cup [4, \sqrt{17})\) \(\cup\, [5, \sqrt{26}) \cup \{6\}\).")),
       ("Check the options", p(r"Option 3 lies entirely inside S. Options 2 and 4 include \(\sqrt{10}\) (and \(\sqrt{17}\) or \(\sqrt{26}\)), where \([x^2]\) jumps. Option 1 includes values above \(\sqrt{17}\) and above \(\sqrt{26}\)."))) + final("Option 3"),
 concept=r"\[[x] = n \text{ on } [n, n+1)\]",
 why_rows=[("1", r"\(\sqrt{17} < x < \sqrt{18}\) is not in S."), ("2", r"\(x = \sqrt{10}\) gives \([x^2] = 10 \ne 9\)."), ("4", r"\(x = \sqrt{10}\) is not in S.")])

P.qa(8, "Kamala divided her investment of Rs 100000 between stocks, bonds, and gold. Her investment in bonds was 25% of her investment in gold. With annual returns of 10%, 6%, 8% on stocks, bonds, and gold, respectively, she gained a total amount of Rs 8200 in one year. The amount, in rupees, that she gained from the bonds, was",
 [], "TITA", "900", ["Arithmetic::Percentages"], "Easy",
 "Let gold be G; bonds are G/4 and stocks are the rest.",
 steps(p(r"Stocks are \(100000 - 1.25G\). The gain is \(0.1(100000 - 1.25G)\) \(+ 0.06(0.25G) + 0.08G\) \(= 10000 - 0.03G = 8200\), so \(G = 60000\), bonds 15000, and the gain from bonds \(0.06 \times 15000 = 900\).")) + final(r"\(900\)"),
 concept=r"\[\text{return} = \text{rate} \times \text{amount}\]")

P.qa(9, "At a certain simple rate of interest, a given sum amounts to Rs.13920 in 3 years, and to Rs 18960 in 6 years and 6 months. If the same given sum had been invested for 2 years at the same rate as before but with interest compounded every 6 months, then the total interest earned, in rupees, would have been nearest to",
 M("3221", "3180", "3150", "3096"), "MCQ", "1", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "3.5 years of simple interest add 5040.",
 steps(("Rate and principal", p(r"Yearly interest \(= 5040 \div 3.5 = 1440\). Principal \(= 13920 - 3 \times 1440 = 9600\), rate \(1440 \div 9600 = 15\%\).")),
       ("Half-yearly compounding", p(r"7.5% per half-year for 4 half-years: \(9600(1.075^4 - 1)\) \(\approx 9600 \times 0.3355 \approx 3221\)."))) + final(r"\(3221\), option 1"),
 concept=r"\[CI = P\left[(1 + r)^n - 1\right]\]",
 why_rows=[("2", "Slightly low: 1.075⁴ is about 1.3355."), ("3", "This is close to yearly compounding."), ("4", "This is 2 years of simple interest plus a little.")])

P.qa(10, "A cafeteria offers 5 types of sandwiches. Moreover, for each type of sandwich, a customer can choose one of 4 breads and opt for either small or large sized sandwich. Optionally, the customer may also add up to 2 out of 6 available sauces. The number of different ways in which an order can be placed for a sandwich, is",
 M("840", "800", "880", "600"), "MCQ", "3", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Sauces: none, one, or two different ones.",
 steps(p(r"\(5 \times 4 \times 2 = 40\) base choices. Sauces: \(1 + 6 + 15 = 22\). Total \(40 \times 22 = 880\).")) + final(r"\(880\), option 3"),
 concept=r"\[\text{independent choices multiply}\]",
 why_rows=[("1", "This counts 21 sauce options, missing one."), ("2", "This counts 20 sauce options."), ("4", "This counts 15: only pairs of sauces.")])

P.qa(11, "Arun, Varun and Tarun, if working alone, can complete a task in 24, 21, and 15 days, respectively. They charge Rs 2160, Rs 2400, and Rs 2160 per day, respectively, even if they are employed for a partial day. On any given day, any of the workers may or may not be employed to work. If the task needs to be completed in 10 days or less, then the minimum possible amount, in rupees, required to be paid for the entire task is",
 M("47040", "38880", "34400", "38400"), "MCQ", "4", ["Arithmetic::Time_and_Work"], "Medium",
 "Work out each person’s cost for the whole task. Use the cheapest as much as the deadline allows.",
 steps(("Cost per whole task", p("Arun 24 × 2160 = 51840, Varun 21 × 2400 = 50400, Tarun 15 × 2160 = 32400. Tarun is cheapest.")),
       ("Tarun for 10 days", p(r"He does \(\frac{10}{15} = \frac23\) for 21600.")),
       ("The last third", p(r"Varun is next cheapest: \(\frac13\) takes him exactly 7 days, 16800. Total 38400."))) + final(r"\(38400\), option 4"),
 concept=r"\[\text{cost per task} = \text{days alone} \times \text{daily wage}\]",
 why_rows=[("1", "This uses Arun or Varun for far more of the work."), ("2", "This gives the last third to Arun (8 days, 17280)."), ("3", "Tarun alone can’t finish within 10 days, so this is too low.")])

P.qa(12, r"The number of non-negative integer values of \(k\) for which the quadratic equation \(x^2 - 5x + k = 0\) has only integer roots, is",
 [], "TITA", "3", ["Algebra::Quadratic_Equations"], "Easy",
 "The roots add to 5 and multiply to k, which must be non-negative.",
 steps(p(r"Integer pairs adding to 5 with a non-negative product: (0, 5), (1, 4), (2, 3), giving \(k = 0, 4, 6\).")) + final(r"\(3\)"),
 concept=r"\[x^2 - sx + p = 0 \text{ has roots adding to } s \text{ and multiplying to } p\]")

P.qa(13, r"The \((x, y)\) coordinates of vertices P, Q and R of a parallelogram PQRS are \((-3, -2)\), \((1, -5)\) and \((9, 1)\), respectively. If the diagonal SQ intersects the x-axis at \((a, 0)\), then the value of \(a\) is",
 M(r"\tfrac{10}{3}", r"\tfrac{29}{9}", r"\tfrac{13}{4}", r"\tfrac{27}{7}"), "MCQ", "2", ["Geometry::Coordinate_Geometry"], "Easy",
 "S = P + R − Q.",
 steps(("S", p(r"\(S = P + R - Q\) \(= (5, 4)\).")),
       ("Line SQ", p(r"From \(Q(1, -5)\) to \(S(5, 4)\): \(y = 0\) is \(\frac59\) of the way up, so \(x = 1 + \frac59 \times 4 = \frac{29}{9}\)."))) + final(r"\(\tfrac{29}{9}\), option 2"),
 concept=r"\[\text{parallelogram: } P + R = Q + S\]",
 why_rows=[("1", "This uses the wrong fourth vertex."), ("3", "This uses the wrong fourth vertex."), ("4", "This uses the wrong fourth vertex.")])

P.qa(14, "In a 3-digit number N, the digits are non-zero and distinct such that none of the digits is a perfect square, and only one of the digits is a prime number. Then, the number of factors of the minimum possible value of N is",
 [], "TITA", "6", ["Number_System::Factors_and_Divisibility"], "Medium",
 "Allowed digits: 2, 3, 5, 6, 7, 8 (1, 4 and 9 are squares). Exactly one prime.",
 steps(("Smallest N", p("The smallest start is 2, a prime, so the other two digits must be non-prime: 6 and 8. N = 268.")),
       ("Factors", p(r"\(268 = 2^2 \times 67\), so it has \(3 \times 2 = 6\) factors."))) + final(r"\(6\)"),
 concept=r"\[N = p^a q^b \;\Rightarrow\; (a+1)(b+1) \text{ factors}\]")

P.qa(15, "Stocks A, B and C are priced at rupees 120, 90 and 150 per share, respectively. A trader holds a portfolio consisting of 10 shares of stock A, and 20 shares of stocks B and C put together. If the total value of her portfolio is rupees 3300, then the number of shares of stock B that she holds, is",
 [], "TITA", "15", ["Algebra::Linear_Equations"], "Easy",
 "A is worth 1200, so B and C are worth 2100.",
 steps(p(r"\(90b + 150(20 - b) = 2100\), so \(3000 - 60b = 2100\) and \(b = 15\).")) + final(r"\(15\)"),
 concept=r"\[\text{value} = \text{price} \times \text{quantity}\]")

P.qa(16, r"If \(a - 6b + 6c = 4\) and \(6a + 3b - 3c = 50\), where \(a, b\) and \(c\) are real numbers, the value of \(2a + 3b - 3c\) is",
 M("18", "15", "20", "14"), "MCQ", "1", ["Algebra::Linear_Equations"], "Easy",
 "b and c always appear as b − c. Call it u.",
 steps(p(r"\(a - 6u = 4\) and \(6a + 3u = 50\). Doubling the second and adding: \(13a = 104\), so \(a = 8\) and \(u = \frac23\). Then \(2a + 3u = 16 + 2 = 18\).")) + final(r"\(18\), option 1"),
 concept=r"\[\text{treat a repeated combination as one unknown}\]",
 why_rows=[("2", "Check: 2a = 16 already, plus 2."), ("3", "This uses u = 4/3."), ("4", "This subtracts instead of adding 3u.")])

P.qa(17, r"A value of \(c\) for which the minimum value of \(f(x) = x^2 - 4cx + 8c\) is greater than the maximum value of \(g(x) = -x^2 + 3cx - 2c\), is",
 M("-2", r"-\tfrac12", "2", r"\tfrac12"), "MCQ", "4", ["Algebra::Quadratic_Equations"], "Medium",
 "Find both extreme values by completing the square.",
 steps(("Extremes", p(r"\(f_{\min} = 8c - 4c^2\) (at \(x = 2c\)); \(g_{\max} = \frac94 c^2 - 2c\) (at \(x = \frac32 c\)).")),
       ("Condition", p(r"\(8c - 4c^2 > \frac94c^2 - 2c\) gives \(\frac{25}{4}c^2 < 10c\), so \(0 < c < 1.6\). Of the options, only \(\frac12\) works."))) + final(r"\(\tfrac12\), option 4"),
 concept=r"\[ax^2 + bx + c \text{ has its extreme value } c - \frac{b^2}{4a}\]",
 why_rows=[("1", "c must be positive."), ("2", "c must be positive."), ("3", "2 is above 1.6.")])

P.qa(18, "In a class, there were more than 10 boys and a certain number of girls. After 40% of the girls and 60% of the boys left the class, the remaining number of girls was 8 more than the remaining number of boys. Then, the minimum possible number of students initially in the class was",
 [], "TITA", "55", ["Arithmetic::Percentages"], "Medium",
 "0.6G − 0.4B = 8, with both B and G multiples of 5.",
 steps(p(r"\(3G - 2B = 40\). B must be a multiple of 5 above 10: try 15, giving \(3G = 70\), not whole. Try 20: \(G = \frac{80}{3}\), no. Try 25: \(G = 30\), a multiple of 5. Total 55.")) + final(r"\(55\)"),
 concept=r"\[\text{percentages of people must give whole numbers}\]")

P.qa(19, r"In the set of consecutive odd numbers \(\{1, 3, 5, \ldots, 57\}\), there is a number \(k\) such that the sum of all the elements less than \(k\) is equal to the sum of all the elements greater than \(k\). Then, \(k\) equals.",
 M("43", "37", "39", "41"), "MCQ", "4", ["Algebra::Progressions_and_Series"], "Medium",
 r"If k is the \(m\)th odd number, the sum of the odd numbers below it is \((m-1)^2\) and up to it is \(m^2\).",
 steps(("The set", p(r"29 terms, summing to \(29^2 = 841\).")),
       ("The condition", p(r"Below k: \((m-1)^2\). Above k: \(841 - m^2\). Setting them equal: \(2m^2 - 2m + 1 = 841\), so \(m^2 - m = 420\) and \(m = 21\).")),
       ("k", p(r"The 21st odd number is 41. Check: below 400, above \(841 - 441 = 400\)."))) + final(r"\(41\), option 4"),
 concept=r"\[1 + 3 + \cdots + (2n - 1) = n^2\]",
 why_rows=[("1", "Below 43 sums to 441, above it to 357."), ("2", "Below 37 sums to 324, above it to 480."), ("3", "Below 39 sums to 361, above it to 441.")])

P.qa(20, "A shopkeeper offers a discount of 22% on the marked price of each chair, and gives 13 chairs to a customer for the discounted price of 12 chairs to earn a profit of 26% on the transaction. If the cost price of each chair is Rs 100, then the marked price, in rupees, of each chair is",
 [], "TITA", "175", ["Arithmetic::Profit_Loss_and_Discount"], "Easy",
 "Revenue is 12 discounted prices; cost is 13 chairs.",
 steps(p(r"\(12 \times 0.78M = 1.26 \times 1300 = 1638\), so \(M = \frac{1638}{9.36} = 175\).")) + final(r"\(175\)"),
 concept=r"\[\text{revenue} = (1 + \text{profit\%}) \times \text{cost}\]")

P.qa(21, "If the length of a side of a rhombus is 36 cm and the area of the rhombus is 396 sq. cm, then the absolute value of the difference between the lengths, in cm, of the diagonals of the rhombus is",
 [], "TITA", "60", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 r"\(d_1 d_2 = 2 \times \text{area}\) and \(d_1^2 + d_2^2 = 4 \times \text{side}^2\).",
 steps(p(r"\(d_1 d_2 = 792\) and \(d_1^2 + d_2^2 = 5184\). So \((d_1 - d_2)^2 = 5184 - 1584 = 3600\), and the difference is 60.")) + final(r"\(60\)"),
 concept=r"\[(d_1 - d_2)^2 = d_1^2 + d_2^2 - 2d_1d_2\]")

P.qa(22, r"For any natural number \(k\), let \(a_k = 3^k\). The smallest natural number \(m\) for which \((a_1)^1 \times (a_2)^2 \times \cdots \times (a_{20})^{20}\) \(< a_{21} \times a_{22} \times \cdots \times a_{20+m}\), is",
 M("57", "56", "59", "58"), "MCQ", "4", ["Algebra::Progressions_and_Series"], "Medium",
 "Compare powers of 3: the left exponent is 1² + 2² + … + 20².",
 steps(("Exponents", p(r"Left: \(\sum_{k=1}^{20} k^2 = \frac{20 \cdot 21 \cdot 41}{6} = 2870\). Right: \(21 + 22 + \cdots + (20 + m)\) \(= 20m + \frac{m(m+1)}{2}\).")),
       ("Smallest m", p(r"\(m = 57\): \(1140 + 1653 = 2793\), not enough. \(m = 58\): \(1160 + 1711 = 2871 > 2870\)."))) + final(r"\(58\), option 4"),
 concept=r"\[1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}\]",
 why_rows=[("1", "2793 is still below 2870."), ("2", "Even smaller."), ("3", "58 already works.")])
