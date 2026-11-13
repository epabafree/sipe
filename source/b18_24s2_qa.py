# -*- coding: utf-8 -*-
# Batch 18 — CAT 2024 Slot 2: QA Q1–22 (exam order).
from fmt import steps, final, trap, why, table, p
from b18_24s2 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, "A company has 40 employees whose names are listed in a certain order. In the year 2022, the average bonus of the first 30 employees was Rs. 40000, of the last 30 employees was Rs. 60000, and of the first 10 and last 10 employees together was Rs. 50000. Next year, the average bonus of the first 10 employees increased by 100%, of the last 10 employees increased by 200% and of the remaining employees was unchanged. Then, the average bonus, in rupees, of all the 40 employees together in the year 2023 was",
 M("90000", "80000", "95000", "85000"), "MCQ", "3", ["Arithmetic::Average"], "Medium",
 "Split the 40 into three blocks: first 10, middle 20, last 10. Find each block’s total.",
 steps(("Three equations", p(r"In lakh rupees: \(F + M = 12\), \(M + L = 18\), \(F + L = 10\).")),
       ("Solve", p(r"Adding all three: \(2(F + M + L) = 40\), so the total is 20. Then \(L = 8\), \(F = 2\), \(M = 10\).")),
       ("2023", p(r"\(2 \times 2 + 10 + 8 \times 3 = 38\) lakh. The average is \(3800000 \div 40 = 95000\)."))) + final(r"\(95000\), option 3"),
 concept=r"\[\text{total} = \text{average} \times \text{count}\]",
 why_rows=[("1", "This would be 36 lakh in total."), ("2", "This would be 32 lakh: it misses part of the increases."), ("4", "This would be 34 lakh.")])

P.qa(2, r"When \(3^{333}\) is divided by \(11\), the remainder is", M("10", "1", "6", "5"), "MCQ", "4", ["Number_System::Remainders"], "Easy",
 r"Find a small power of 3 that leaves remainder 1 when divided by 11.",
 steps(p(r"\(3^5 = 243 = 11 \times 22 + 1\), so \(3^5\) leaves 1. Since \(333 = 5 \times 66 + 3\), the remainder equals that of \(3^3 = 27\), which is 5.")) + final(r"\(5\), option 4"),
 concept=r"\[a^k \equiv 1 \pmod n \;\Rightarrow\; a^{qk + r} \equiv a^r \pmod n\]",
 why_rows=[("1", "The powers of 3 leave only the remainders 3, 9, 5, 4 and 1; 10 never appears."), ("2", "1 is the remainder only when the exponent is a multiple of 5."), ("3", "6 never appears among the remainders 3, 9, 5, 4, 1.")])

P.qa(3, r"If \(m\) and \(n\) are natural numbers such that \(n > 1\), and \(m^n = 2^{25} \times 3^{40}\), then \(m - n\) equals",
 M("209937", "209947", "209942", "209932"), "MCQ", "2", ["Algebra::Surds_and_Indices"], "Medium",
 "n must divide both 25 and 40.",
 steps(("n", p(r"\(m = 2^{25/n} \times 3^{40/n}\) must be a whole number, so \(n\) divides both 25 and 40. Their only common factor above 1 is 5, so \(n = 5\).")),
       ("m", p(r"\(m = 2^5 \times 3^8 = 32 \times 6561 = 209952\).")),
       ("Answer", p(r"\(209952 - 5 = 209947\)."))) + final(r"\(209947\), option 2"),
 concept=r"\[m^n = p^a q^b \text{ with } m \text{ whole} \;\Rightarrow\; n \mid a \text{ and } n \mid b\]",
 why_rows=[("1", "This subtracts 15."), ("3", "This subtracts 10."), ("4", "This subtracts 20.")])

P.qa(4, "A vessel contained a certain amount of a solution of acid and water. When 2 litres of water was added to it, the new solution had 50% acid concentration. When 15 litres of acid was further added to this new solution, the final solution had 80% acid concentration. The ratio of water and acid in the original solution was",
 M("4 : 5", "3 : 5", "5 : 3", "5 : 4"), "MCQ", "2", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "At 50%, acid equals water. After 15 litres of acid, acid is 4 times the water.",
 steps(("After the water", p(r"Acid \(a\) = water \(w + 2\).")),
       ("After the acid", p(r"\(a + 15 = 4(w + 2) = 4a\), so \(a = 5\) and \(w = 3\).")),
       ("Ratio", p(r"Water : acid \(= 3 : 5\)."))) + final(r"\(3 : 5\), option 2"),
 concept=r"\[x\% \text{ concentration} \;\Rightarrow\; \text{acid} : \text{water} = x : (100 - x)\]",
 why_rows=[("1", "This uses the water after the 2 litres were added."), ("3", "This is acid : water, the wrong way round."), ("4", "This doesn’t satisfy either condition.")])

P.qa(5, r"If \(\left(x + 6\sqrt2\right)^{\frac12} - \left(x - 6\sqrt2\right)^{\frac12} = 2\sqrt2\), then \(x\) equals",
 [], "TITA", "11", ["Algebra::Surds_and_Indices"], "Medium",
 "Call the two square roots u and v. You know u − v; find u + v from u² − v².",
 steps(("u + v", p(r"\(u^2 - v^2 = 12\sqrt2\) and \(u - v = 2\sqrt2\), so \(u + v = 6\).")),
       ("u", p(r"\(u = 3 + \sqrt2\), so \(u^2 = 11 + 6\sqrt2 = x + 6\sqrt2\).")),
       ("x", p(r"\(x = 11\)."))) + final(r"\(11\)"),
 shortcut=r"\(11 + 6\sqrt2 = (3 + \sqrt2)^2\) and \(11 - 6\sqrt2 = (3 - \sqrt2)^2\). The difference of the roots is \(2\sqrt2\).",
 concept=r"\[u^2 - v^2 = (u - v)(u + v)\]")

P.qa(6, "Anil invests Rs 22000 for 6 years in a scheme with 4% interest per annum, compounded half-yearly. Separately, Sunil invests a certain amount in the same scheme for 5 years, and then reinvests the entire amount he receives at the end of 5 years, for one year at 10% simple interest. If the amounts received by both at the end of 6 years are equal, then the initial investment, in rupees, made by Sunil is",
 M("20860", "20808", "20480", "20640"), "MCQ", "2", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "Both grow at 2% per half-year for 5 years. Compare only the last year.",
 steps(("The common part", p(r"Over 5 years both amounts are multiplied by \(1.02^{10}\).")),
       ("The last year", p(r"Anil: two more half-years, \(\times 1.02^2 = 1.0404\). Sunil: \(\times 1.1\).")),
       ("Sunil’s amount", r"\[S = \frac{22000 \times 1.0404}{1.1} = 20000 \times 1.0404 = 20808\]")) + final(r"\(20808\), option 2"),
 concept=r"\[\text{half-yearly at } r\% \text{ a year} \;\Rightarrow\; \times\left(1 + \tfrac{r}{200}\right) \text{ every six months}\]",
 why_rows=[("1", "This is a little too large to match."), ("3", "This uses 2.4% growth instead of 4.04% in the last year."), ("4", "This uses 3.2% for the last year.")])

P.qa(7, "Amal and Vimal together can complete a task in 150 days, while Vimal and Sunil together can complete the same task in 100 days. Amal starts working on the task and works for 75 days, then Vimal takes over and works for 135 days. Finally, Sunil takes over and completes the remaining task in 45 days. If Amal had started the task alone and worked on all days, Vimal had worked on every second day, and Sunil had worked on every third day, then the number of days required to complete the task would have been",
 [], "TITA", "139", ["Arithmetic::Time_and_Work"], "Hard",
 "Split 75A + 135V + 45S into 75(A + V) + 45(V + S) + something.",
 steps(("Vimal’s rate", p(r"\(75A + 135V + 45S\) \(= 75(A + V) + 45(V + S) + 15V\) \(= \frac{75}{150} + \frac{45}{100} + 15V = 1\), so \(15V = \frac{1}{20}\) and \(V = \frac{1}{300}\).")),
       ("The others", p(r"\(A = \frac{1}{150} - \frac{1}{300} = \frac{1}{300}\) and \(S = \frac{1}{100} - \frac{1}{300} = \frac{2}{300}\). Take the task as 300 units: Amal 1, Vimal 1, Sunil 2 a day.")),
       ("Six-day cycles", p("In 6 days: Amal 6, Vimal 3 (days 2, 4, 6), Sunil 4 (days 3, 6). That is 13 units. 23 cycles (138 days) do 299 units.")),
       ("The last day", p("On day 139 only Amal works (139 is neither even nor a multiple of 3), and his 1 unit finishes the task."))) + final(r"\(139\)"),
 concept=r"\[\text{work} = \text{rate} \times \text{days}\]")

P.qa(8, "A bus starts at 9 am and follows a fixed route every day. One day, it traveled at a constant speed of 60 km per hour and reached its destination 3.5 hours later than its scheduled arrival time. Next day, it traveled two-thirds of its route in one-third of its total scheduled travel time, and the remaining part of the route at 40 km per hour to reach just on time. The scheduled arrival time of the bus is",
 M(r"\text{10:30 pm}", r"\text{7:00 pm}", r"\text{7:30 pm}", r"\text{9:00 pm}"), "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Call the route D and the scheduled time T. The second day gives a link between them.",
 steps(("Second day", p(r"The last third of the route, \(\frac{D}{3}\), takes the remaining \(\frac{2T}{3}\) at 40 km/h: \(\frac{D}{120} = \frac{2T}{3}\), so \(D = 80T\).")),
       ("First day", p(r"\(\frac{80T}{60} = T + 3.5\), so \(\frac{T}{3} = 3.5\) and \(T = 10.5\) hours.")),
       ("Arrival", p("9 am plus 10.5 hours is 7:30 pm."))) + final("7:30 pm, option 3"),
 concept=r"\[\text{time} = \frac{\text{distance}}{\text{speed}}\]",
 why_rows=[("1", "10:30 pm would mean a scheduled trip of 13.5 hours, which fails the second condition."), ("2", "This needs T = 10 hours, which doesn’t satisfy both days."), ("4", "This needs T = 12 hours.")])

P.qa(9, r"A function \(f\) maps the set of natural numbers to whole numbers, such that \(f(xy) = f(x)f(y) + f(x) + f(y)\) for all \(x, y\) and \(f(p) = 1\) for every prime number \(p\). Then, the value of \(f(160000)\) is",
 M("8191", "2047", "4095", "1023"), "MCQ", "3", ["Algebra::Functions"], "Medium",
 r"Add 1 to both sides. What does \(f + 1\) do to products?",
 steps(("A neater function", p(r"\(f(xy) + 1 = (f(x) + 1)(f(y) + 1)\). So \(g = f + 1\) is multiplicative, with \(g(p) = 2\) for every prime.")),
       ("Apply it", p(r"\(160000 = 2^8 \times 5^4\), a product of 12 primes, so \(g = 2^{12} = 4096\) and \(f = 4095\)."))) + final(r"\(4095\), option 3"),
 concept=r"\[ab + a + b + 1 = (a + 1)(b + 1)\]",
 why_rows=[("1", r"This counts 13 prime factors."), ("2", "This counts 11 prime factors."), ("4", "This counts 10 prime factors.")])

P.qa(10, r"The sum of the infinite series \(\frac15\left(\frac15 - \frac17\right)\) \(+ \left(\frac15\right)^2\left(\left(\frac15\right)^2 - \left(\frac17\right)^2\right)\) \(+ \left(\frac15\right)^3\left(\left(\frac15\right)^3 - \left(\frac17\right)^3\right) + \cdots\) is equal to",
 M(r"\tfrac{5}{408}", r"\tfrac{7}{816}", r"\tfrac{7}{408}", r"\tfrac{5}{816}"), "MCQ", "1", ["Algebra::Progressions_and_Series"], "Medium",
 r"Multiply out each term. You get \(\left(\frac{1}{25}\right)^n - \left(\frac{1}{35}\right)^n\).",
 steps(("Two series", p(r"The sum is \(\sum \left(\frac{1}{25}\right)^n - \sum \left(\frac{1}{35}\right)^n\).")),
       ("Each one", p(r"\(\frac{1/25}{1 - 1/25} = \frac{1}{24}\) and \(\frac{1/35}{1 - 1/35} = \frac{1}{34}\).")),
       ("Difference", p(r"\(\frac{1}{24} - \frac{1}{34} = \frac{10}{816} = \frac{5}{408}\)."))) + final(r"\(\tfrac{5}{408}\), option 1"),
 concept=r"\[a + ar + ar^2 + \cdots = \frac{a}{1 - r}, \quad |r| < 1\]",
 why_rows=[("2", "The numerator should be 10, which simplifies to 5/408."), ("3", "The numerator is wrong."), ("4", "This is half the correct sum.")])

P.qa(11, "A fruit seller has a stock of mangoes, bananas and apples with at least one fruit of each type. At the beginning of a day, the number of mangoes make up 40% of his stock. That day, he sells half of the mangoes, 96 bananas and 40% of the apples. At the end of the day, he ends up selling 50% of the fruits. The smallest possible total number of fruits in the stock at the beginning of the day is",
 [], "TITA", "340", ["Arithmetic::Percentages"], "Hard",
 "Write the apples in terms of the total, then use the whole-number conditions.",
 steps(("Apples", p(r"Sold: \(0.2T + 96 + 0.4A = 0.5T\), so \(A = 0.75T - 240\).")),
       ("Conditions", p(r"Half the mangoes, \(0.2T\), must be whole, so \(T\) is a multiple of 5. \(0.75T\) must be whole, so \(T\) is a multiple of 4. So \(T\) is a multiple of 20. We also need \(A \ge 1\), so \(T > 320\); and 40% of the apples must be whole.")),
       ("Smallest", p(r"\(T = 340\): \(A = 15\) (40% is 6), mangoes 136, bananas \(340 - 136 - 15 = 189\), which is enough to sell 96. It works."))) +
 trap(r"\(T = 320\) gives no apples at all, but there must be at least one of each fruit.") + final(r"\(340\)"),
 concept=p("Every count of fruit, sold or left, has to be a whole number."))

P.qa(12, "Bina incurs 19% loss when she sells a product at Rs. 4860 to Shyam, who in turn sells this product to Hari. If Bina would have sold this product to Shyam at the purchase price of Hari, she would have obtained 17% profit. Then, the profit, in rupees, made by Shyam is",
 [], "TITA", "2160", ["Arithmetic::Profit_Loss_and_Discount"], "Easy",
 "Find Bina’s cost first. Hari paid 117% of it.",
 steps(p(r"Bina’s cost: \(4860 \div 0.81 = 6000\). Hari paid \(1.17 \times 6000 = 7020\). Shyam bought at 4860, so his profit is \(7020 - 4860 = 2160\).")) + final(r"\(2160\)"),
 concept=r"\[\text{SP} = \text{CP}(1 \pm \text{rate})\]")

P.qa(13, r"Three circles of equal radii touch (but not cross) each other externally. Two other circles, \(X\) and \(Y\), are drawn such that both touch (but not cross) each of the three previous circles. If the radius of \(X\) is more than that of \(Y\), the ratio of the radii of \(X\) and \(Y\) is",
 M(r"4 + 2\sqrt3 : 1", r"7 + 4\sqrt3 : 1", r"2 + \sqrt3 : 1", r"4 + \sqrt3 : 1"), "MCQ", "2", ["Geometry::Circles"], "Medium",
 "The centres form an equilateral triangle. X wraps around all three; Y sits in the gap between them.",
 steps(("The centres", p(r"With radius \(r\), the centres form an equilateral triangle of side \(2r\), whose centre is at distance \(R = \frac{2r}{\sqrt3}\) from each.")),
       ("The two circles", p(r"The small circle Y has radius \(R - r\); the large circle X, which encloses all three, has radius \(R + r\).")),
       ("Ratio", r"\[\frac{R + r}{R - r} = \frac{2 + \sqrt3}{2 - \sqrt3} = (2 + \sqrt3)^2 = 7 + 4\sqrt3\]")) + final(r"\(7 + 4\sqrt3 : 1\), option 2"),
 concept=r"\[\text{circumradius of an equilateral triangle of side } a = \frac{a}{\sqrt3}\]",
 why_rows=[("1", r"This is \((2 + \sqrt3)^2\) worked out wrongly."), ("3", r"This forgets to rationalise: it is only \(\sqrt{\text{ratio}}\)."), ("4", "This doesn’t come from the geometry.")])

P.qa(14, r"If \(x\) and \(y\) satisfy the equations \(|x| + x + y = 15\) and \(x + |y| - y = 20\), then \((x - y)\) equals",
 M("20", "10", "15", "5"), "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "Test the signs. If x were negative, what would the first equation say?",
 steps(("Signs", p(r"If \(x < 0\), the first equation gives \(y = 15\), and then the second gives \(x = 20\): a contradiction. So \(x \ge 0\). If \(y \ge 0\), the second gives \(x = 20\) and then \(y = -25\): a contradiction. So \(y < 0\).")),
       ("Solve", p(r"\(2x + y = 15\) and \(x - 2y = 20\) give \(x = 10\), \(y = -5\). So \(x - y = 15\)."))) + final(r"\(15\), option 3"),
 concept=r"\[|x| = x \text{ if } x \ge 0, \quad |x| = -x \text{ if } x < 0\]",
 why_rows=[("1", "That is the value of 2x."), ("2", "That is x alone."), ("4", "That is x + y.")])

P.qa(15, r"The roots \(\alpha, \beta\) of the equation \(3x^2 + \lambda x - 1 = 0\), satisfy \(\frac{1}{\alpha^2} + \frac{1}{\beta^2} = 15\). The value of \((\alpha^3 + \beta^3)^2\), is",
 M("16", "4", "1", "9"), "MCQ", "2", ["Algebra::Quadratic_Equations"], "Medium",
 r"Write everything in terms of \(s = \alpha + \beta = -\frac{\lambda}{3}\) and \(p = \alpha\beta = -\frac13\).",
 steps(("Find s", p(r"\(\frac{1}{\alpha^2} + \frac{1}{\beta^2} = \frac{s^2 - 2p}{p^2}\) \(= 9\left(s^2 + \frac23\right) = 15\), so \(s^2 = 1\).")),
       ("The cubes", p(r"\(\alpha^3 + \beta^3 = s^3 - 3ps\) \(= s^3 + s = s(s^2 + 1) = \pm 2\). Squared, that is 4."))) + final(r"\(4\), option 2"),
 concept=r"\[\alpha^3 + \beta^3 = (\alpha + \beta)^3 - 3\alpha\beta(\alpha + \beta)\]",
 why_rows=[("1", "This squares 4 instead of 2."), ("3", r"This uses \(s^3\) alone and forgets \(-3ps\)."), ("4", "This doesn’t follow from s² = 1.")])

P.qa(16, r"All the values of \(x\) satisfying the inequality \(\frac{1}{x + 5} \le \frac{1}{2x - 3}\) are",
 [r"\(-5 < x < \frac32\) or \(\frac32 < x \le 8\)", r"\(-5 < x < \frac32\) or \(x > \frac32\)", r"\(x < -5\) or \(x > \frac32\)", r"\(x < -5\) or \(\frac32 < x \le 8\)"], "MCQ", "4", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Don’t cross-multiply. Bring everything to one side and check signs on a number line.",
 steps(("One fraction", r"\[\frac{1}{2x - 3} - \frac{1}{x + 5} = \frac{8 - x}{(2x - 3)(x + 5)} \ge 0\]"),
       ("Sign chart", p(r"The critical points are \(-5\), \(\frac32\) and 8. Testing each interval: positive for \(x < -5\), negative between \(-5\) and \(\frac32\), positive between \(\frac32\) and 8 (zero at 8), negative beyond 8.")),
       ("Answer", p(r"\(x < -5\) or \(\frac32 < x \le 8\)."))) + final("Option 4"),
 concept=r"\[\text{for } \tfrac{N}{D} \ge 0, \text{ check the sign of } N \text{ and } D \text{ on each interval}\]",
 why_rows=[("1", r"Between −5 and 3/2 the expression is negative."), ("2", "This ignores the upper limit of 8 and includes a negative interval."), ("3", "Values above 8 make the left side larger.")])

P.qa(17, "When Rajesh's age was same as the present age of Garima, the ratio of their ages was 3 : 2. When Garima’s age becomes the same as the present age of Rajesh, the ratio of the ages of Rajesh and Garima will become",
 M("2 : 1", "5 : 4", "4 : 3", "3 : 2"), "MCQ", "2", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Let the age gap be d. The earlier ratio pins down Garima’s age.",
 steps(("Earlier", p(r"d years ago Rajesh was Garima’s present age \(G\), and Garima was \(G - d\). \(G : (G - d) = 3 : 2\) gives \(G = 3d\), so Rajesh is \(4d\).")),
       ("Later", p(r"In d years Garima will be \(4d\) and Rajesh \(5d\): \(5 : 4\)."))) + final(r"\(5 : 4\), option 2"),
 concept=r"\[\text{the difference between two ages never changes}\]",
 why_rows=[("1", "Their ages never get as far apart as 2 : 1."), ("3", "4 : 3 is the present ratio."), ("4", "3 : 2 is the earlier ratio.")])

P.qa(18, "P, Q, R and S are four towns. One can travel between P and Q along 3 direct paths, between Q and S along 4 direct paths, and between P and R along 4 direct paths. There is no direct path between P and S, while there are few direct paths between Q and R, and between R and S. One can travel from P to S either via Q, or via R, or via Q followed by R, respectively, in exactly 62 possible ways. One can also travel from Q to R either directly, or via P, or via S, in exactly 27 possible ways. Then, the number of direct paths between Q and R is",
 [], "TITA", "7", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "Let x be the Q–R paths and y the R–S paths. Write the two counts.",
 steps(("P to S", p(r"Via Q: \(3 \times 4 = 12\). Via R: \(4y\). Via Q then R: \(3xy\). So \(4y + 3xy = 50\).")),
       ("Q to R", p(r"Directly \(x\), via P \(3 \times 4 = 12\), via S \(4y\). So \(x + 4y = 15\).")),
       ("Solve", p(r"Put \(x = 15 - 4y\): \(4y + 3y(15 - 4y) = 50\), so \(12y^2 - 49y + 50 = 0\), giving \(y = 2\) (the other root isn’t whole). Then \(x = 7\)."))) + final(r"\(7\)"),
 concept=r"\[\text{ways along a route} = \text{product of the choices on each leg}\]")

P.qa(19, "The coordinates of the three vertices of a triangle are: (1, 2), (7, 2), and (1, 10). Then the radius of the in circle of the triangle is",
 [], "TITA", "2", ["Geometry::Coordinate_Geometry"], "Easy",
 "The triangle has a right angle at (1, 2).",
 steps(p(r"The legs are 6 and 8, so the hypotenuse is 10. For a right triangle, \(r = \frac{6 + 8 - 10}{2} = 2\).")) + final(r"\(2\)"),
 concept=r"\[r = \frac{\text{area}}{\text{semi-perimeter}} = \frac{24}{12} = 2\]")

P.qa(20, r"If \(a, b\) and \(c\) are positive real numbers such that \(a > 10 \ge b \ge c\) and \(\frac{\log_8 (a + b)}{\log_2 c} + \frac{\log_{27} (a - b)}{\log_3 c} = \frac23\), then the greatest possible integer value of \(a\) is",
 [], "TITA", "14", ["Algebra::Logarithms_and_Exponents"], "Hard",
 r"\(\log_8 = \frac13 \log_2\) and \(\log_{27} = \frac13 \log_3\). Each fraction becomes a log to base c.",
 steps(("Simplify", p(r"\(\frac{\log_8 (a + b)}{\log_2 c} = \frac13 \log_c (a + b)\), and likewise \(\frac13 \log_c (a - b)\).")),
       ("Combine", p(r"\(\frac13 \log_c (a^2 - b^2) = \frac23\), so \(a^2 - b^2 = c^2\), that is \(a^2 = b^2 + c^2\).")),
       ("Largest a", p(r"With \(b, c \le 10\), \(a^2 \le 200\), so \(a \le 14.14\). The greatest integer is 14 (for example \(b = 10\), \(c = \sqrt{96}\))."))) + final(r"\(14\)"),
 concept=r"\[\frac{\log_k x}{\log_k c} = \log_c x\]")

P.qa(21, r"If \(x\) and \(y\) are real numbers such that \(4x^2 + 4y^2 - 4xy - 6y + 3 = 0\), then the value of \((4x + 5y)\) is",
 [], "TITA", "7", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Rewrite the left side as a sum of two squares.",
 steps(("Squares", r"\[(2x - y)^2 + 3(y - 1)^2 = 0\]"),
       ("Solve", p(r"Both squares are zero: \(y = 1\) and \(x = \frac12\). So \(4x + 5y = 2 + 5 = 7\)."))) + final(r"\(7\)"),
 concept=r"\[A^2 + B^2 = 0 \text{ (real numbers)} \;\Rightarrow\; A = B = 0\]")

P.qa(22, "ABCD is a trapezium in which AB is parallel to CD. The sides AD and BC when extended, intersect at point E. If AB = 2 cm, CD = 1 cm, and perimeter of ABCD is 6 cm, then the perimeter, in cm, of ∆AEB is",
 M("8", "10", "9", "7"), "MCQ", "1", ["Geometry::Triangles"], "Medium",
 "CD is half of AB, so triangle ECD is half the size of triangle EAB.",
 steps(("Similar triangles", p(r"\(\triangle ECD \sim \triangle EAB\) with ratio \(1 : 2\), so D and C are the midpoints of EA and EB. Hence \(EA = 2AD\) and \(EB = 2BC\).")),
       ("The sides", p(r"\(AD + BC = 6 - 2 - 1 = 3\), so \(EA + EB = 6\).")),
       ("Perimeter", p(r"\(6 + AB = 6 + 2 = 8\)."))) + final(r"\(8\), option 1"),
 concept=r"\[\text{a line parallel to one side cuts the other two sides in the same ratio}\]",
 why_rows=[("2", "This adds CD as well."), ("3", "This adds only half of the extra sides."), ("4", "This leaves out part of the sides.")])
