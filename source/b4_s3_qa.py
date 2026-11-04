# -*- coding: utf-8 -*-
# Batch 4 — CAT 2023 Slot 3: QA Q1–22.
from fmt import steps, final, why, table, p
from b4_s3 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"For a real number \(x\), if \(\dfrac12\), \(\dfrac{\log_3(2^x - 9)}{\log_3 4}\) and \(\dfrac{\log_5\left(2^x + \frac{17}{2}\right)}{\log_5 4}\) are in an arithmetic progression, then the common difference is",
 M(r"\log_4\left(\dfrac32\right)", r"\log_4\left(\dfrac{23}{2}\right)", r"\log_4\left(\dfrac72\right)", r"\log_4 7"), "MCQ", "3", ["Algebra::Logarithms_and_Exponents", "Algebra::Progressions_and_Series"], "Medium",
 r"Each fraction is a change of base to \(\log_4\). Write \(\tfrac12\) as \(\log_4 2\) too.",
 steps(("Rewrite", r"\[\log_4 2,\quad \log_4(t - 9),\quad \log_4\left(t + \tfrac{17}{2}\right)\]" + p(r"where \(t = 2^x\).")),
       ("AP condition", r"\[\begin{aligned} 2\log_4(t - 9) &= \log_4 2 + \log_4\left(t + \tfrac{17}{2}\right) \\ (t - 9)^2 &= 2t + 17 \\ t^2 - 20t + 64 &= 0 \end{aligned}\]" + p(r"\(t = 16\) or \(4\); the log needs \(t > 9\), so \(t = 16\).")),
       ("Difference", r"\[d = \log_4 7 - \log_4 2 = \log_4 \tfrac72\]")) + final("Option 3"),
 shortcut=r"Middle term \(= \log_4 7\), first \(= \log_4 2\): the difference is \(\log_4 \tfrac72\) without needing the third term.",
 concept=r"\[\frac{\log_c a}{\log_c b} = \log_b a \qquad a, b, c \text{ in AP} \iff 2b = a + c\]",
 why_rows=[("1", r"Uses \(t = 4\)… but then \(t - 9 < 0\) and the log is undefined."), ("2", r"The terms are \(\log_4 2,\ \log_4 7,\ \log_4 \tfrac{49}{2}\); consecutive ones differ by \(\log_4 \tfrac72\), not this."), ("4", r"That’s the middle term, not the difference.")])

P.qa(2, r"Let \(n\) and \(m\) be two positive integers such that there are exactly \(41\) integers greater than \(8^m\) and less than \(8^n\), which can be expressed as powers of \(2\). Then, the smallest possible value of \(n + m\) is",
 M("44", "14", "16", "42"), "MCQ", "3", ["Algebra::Surds_and_Indices", "Number_System::Miscellaneous"], "Easy",
 r"Write \(8^m = 2^{3m}\) and \(8^n = 2^{3n}\). How many powers of 2 lie strictly between?",
 steps(("Count", p(r"Strictly between \(2^{3m}\) and \(2^{3n}\): \(2^{3m+1}, \dots, 2^{3n-1}\), which is \(3n - 3m - 1\) powers.")),
       ("Solve", r"\[3(n - m) - 1 = 41 \Rightarrow n - m = 14\]" + p(r"Smallest: \(m = 1\), \(n = 15\)."))) + final(r"\(n + m = 16\) — option 3"),
 shortcut="Exponents are integers between 3m and 3n, exclusive.",
 concept=r"\[\#\{k : a < k < b\} = b - a - 1\]",
 why_rows=[("1", r"Would need \(m = 15\)."), ("2", r"That’s \(n - m\), and \(m = 0\) isn’t positive."), ("4", r"Would need \(m = 14\).")])

P.qa(3, r"For some real numbers \(a\) and \(b\), the system of equations \(x + y = 4\) and \((a + 5)x + (b^2 - 15)y = 8b\) has infinitely many solutions for \(x\) and \(y\). Then, the maximum possible value of \(ab\) is",
 M("33", "55", "15", "25"), "MCQ", "1", ["Algebra::Linear_Equations"], "Medium",
 "Infinitely many solutions: the second equation must be a multiple of the first.",
 steps(("Proportional coefficients", r"\[\frac{a + 5}{1} = \frac{b^2 - 15}{1} = \frac{8b}{4} = 2b\]"),
       ("Solve for b", r"\[b^2 - 2b - 15 = 0 \Rightarrow b = 5 \text{ or } -3\]"),
       ("ab", p(r"\(a = 2b - 5\): \(b = 5 \Rightarrow a = 5,\ ab = 25\); \(b = -3 \Rightarrow a = -11,\ ab = 33\)."))) + final(r"\(33\) — option 1"),
 shortcut=r"Don’t forget the negative root: \(b = -3\) gives the larger product.",
 concept=r"\[a_1x + b_1y = c_1,\ a_2x + b_2y = c_2 \text{ coincide} \iff \frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}\]",
 why_rows=[("2", r"Not possible: \(ab\) is \(25\) or \(33\)."), ("3", r"Not possible: \(ab\) is \(25\) or \(33\)."), ("4", r"That’s the \(b = 5\) case; \(b = -3\) gives more.")])

P.qa(4, r"If \(x\) is a positive real number such that \(x^8 + \left(\dfrac1x\right)^8 = 47\), then the value of \(x^9 + \left(\dfrac1x\right)^9\) is",
 M(r"34\sqrt5", r"40\sqrt5", r"30\sqrt5", r"36\sqrt5"), "MCQ", "1", ["Algebra::Surds_and_Indices"], "Medium",
 r"Step down: \(x^8 + x^{-8} = (x^4 + x^{-4})^2 - 2\).",
 steps(("Step down", r"\[x^4 + x^{-4} = 7,\quad x^2 + x^{-2} = 3,\quad x + x^{-1} = \sqrt5\]"),
       ("Cube", r"\[x^3 + x^{-3} = (\sqrt5)^3 - 3\sqrt5 = 2\sqrt5\]"),
       ("Cube again", r"\[x^9 + x^{-9} = (2\sqrt5)^3 - 3(2\sqrt5) = 40\sqrt5 - 6\sqrt5 = 34\sqrt5\]")) + final(r"\(34\sqrt5\) — option 1"),
 shortcut=r"Use \(a^3 + a^{-3} = s^3 - 3s\) twice: \(9 = 3 \times 3\).",
 concept=r"\[\left(t + \tfrac1t\right)^2 = t^2 + \tfrac1{t^2} + 2 \qquad t^3 + \tfrac1{t^3} = s^3 - 3s \;\left(s = t + \tfrac1t\right)\]",
 why_rows=[("2", r"That’s \((2\sqrt5)^3\) alone: it forgets the \(-3s\) term."), ("3", r"Not what the identity gives: \(40\sqrt5 - 6\sqrt5\)."), ("4", r"Not what the identity gives: \(40\sqrt5 - 6\sqrt5\).")])

P.qa(5, r"A quadratic equation \(x^2 + bx + c = 0\) has two real roots. If the difference between the reciprocals of the roots is \(\dfrac13\), and the sum of the reciprocals of the squares of the roots is \(\dfrac59\), then the largest possible value of \((b + c)\) is",
 [], "TITA", "9", ["Algebra::Quadratic_Equations"], "Medium",
 r"Let \(p = \tfrac1\alpha\), \(q = \tfrac1\beta\). You know \(p - q\) and \(p^2 + q^2\); find \(pq\) and \(p + q\).",
 steps(("Product", r"\[2pq = (p^2 + q^2) - (p - q)^2 = \tfrac59 - \tfrac19 = \tfrac49 \Rightarrow pq = \tfrac29\]"),
       ("Sum", r"\[(p + q)^2 = \tfrac59 + \tfrac49 = 1 \Rightarrow p + q = \pm 1\]"),
       ("Back to b, c", p(r"\(pq = \tfrac{1}{c} \Rightarrow c = \tfrac92\). \(p + q = -\tfrac{b}{c} = \pm 1 \Rightarrow b = \mp \tfrac92\).") + r"\[b + c = 0 \;\text{ or }\; 9\]")) + final(r"\(9\)"),
 shortcut=r"Reciprocal roots are the roots of \(cx^2 + bx + 1 = 0\): sum \(-\tfrac bc\), product \(\tfrac1c\).",
 concept=r"\[\frac1\alpha + \frac1\beta = -\frac bc \qquad \frac1{\alpha\beta} = \frac1c\]")

P.qa(6, r"Let \(n\) be any natural number such that \(5^{n-1} < 3^{n+1}\). Then, the least integer value of \(m\) that satisfies \(3^{n+1} < 2^{n+m}\) for each such \(n\), is",
 [], "TITA", "5", ["Algebra::Logarithms_and_Exponents", "Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "List the n that work first; there are only a few.",
 steps(("Which n", table(["n", "1", "2", "3", "4", "5", "6"], [[r"\(5^{n-1}\)", "1", "5", "25", "125", "625", "3125"], [r"\(3^{n+1}\)", "9", "27", "81", "243", "729", "2187"]]) +
          p(r"Works for \(n = 1\) to \(5\); from \(6\) on, \(5^{n-1}\) wins.")),
       ("Hardest case n = 5", r"\[729 < 2^{5 + m} \Rightarrow 5 + m \ge 10 \Rightarrow m \ge 5\]" + p(r"\(m = 5\) also works for \(n = 1\)–\(4\) (\(9 < 64\), \(27 < 128\), \(81 < 256\), \(243 < 512\))."))) + final(r"\(5\)"),
 shortcut=r"The largest valid \(n\) is the binding one: \(2^{10} = 1024 > 729\), \(2^9 = 512 < 729\).",
 concept=r"\[2^{10} = 1024,\ 3^6 = 729,\ 5^5 = 3125\]")

P.qa(7, r"The sum of the first two natural numbers, each having \(15\) factors (including \(1\) and the number itself), is",
 [], "TITA", "468", ["Number_System::Factors_and_Divisibility"], "Easy",
 r"\(15 = 15 \times 1 = 5 \times 3\). Which prime shapes give that?",
 steps(("Shapes", p(r"\(p^{14}\) or \(p^4 q^2\).")),
       ("Smallest", p(r"\(2^4 \cdot 3^2 = 144\), \(2^2 \cdot 3^4 = 324\), then \(2^4 \cdot 5^2 = 400\); \(2^{14}\) is far bigger."))) + final(r"\(144 + 324 = 468\)"),
 shortcut="Put the bigger exponent on the smaller prime for the smallest number; swap them for the next.",
 concept=r"\[N = p^a q^b \Rightarrow (a + 1)(b + 1) \text{ factors}\]")

P.qa(8, r"A merchant purchases a cloth at a rate of ₹ \(100\) per metre and receives \(5\) cm length of cloth free for every \(100\) cm length of cloth purchased by him. He sells the same cloth at a rate of ₹ \(110\) per metre but cheats his customers by giving \(95\) cm length of cloth for every \(100\) cm length of cloth purchased by the customers. If the merchant provides a \(5\%\) discount, the resulting profit earned by him is",
 [r"\(9.7\%\)", r"\(15.5\%\)", r"\(4.2\%\)", r"\(16\%\)"], "MCQ", "2", ["Arithmetic::Profit_Loss_and_Discount"], "Medium",
 "Compare the price per cm he pays with the price per cm he actually receives.",
 steps(("Cost", p(r"₹\(100\) buys \(105\) cm, so \(\tfrac{100}{105}\) per cm.")),
       ("Revenue", p(r"Customer pays \(110 \times 0.95 = 104.5\) for what is really \(95\) cm, so \(1.1\) per cm.")),
       ("Profit", r"\[\frac{1.1}{100/105} - 1 = 1.155 - 1 = 15.5\%\]")) + final(r"\(15.5\%\) — option 2"),
 shortcut=r"Multiply the factors: \(\tfrac{105}{100} \times \tfrac{100}{95} \times 1.10 \times 0.95 = 1.155\).",
 concept=r"\[\text{profit factor} = \frac{\text{SP per unit actually given}}{\text{CP per unit actually received}}\]",
 why_rows=[("1", r"Ignores the short measure (95 cm for 100): \(1.05 \times 1.045 = 1.097\)."), ("3", r"Doesn’t match \(1.05 \times \tfrac{100}{95} \times 1.045 = 1.155\)."), ("4", r"Close, but the product is \(1.155\), not \(1.16\).")])

P.qa(9, r"A boat takes \(2\) hours to travel downstream a river from part A to part B, and \(3\) hours to return to part A. Another boat takes a total of \(6\) hours to travel from part B to part A and return to part B. If the speeds of the boats and the river are constant, then the time, in hours, taken by the slower boat to travel from part A to part B is",
 M(r"3(3 + \sqrt5)", r"3(3 - \sqrt5)", r"3(\sqrt5 - 1)", r"12(\sqrt5 - 2)"), "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Hard",
 r"Take the distance \(AB = 12\) (the LCM of 2 and 3) to get clean speeds.",
 steps(("First boat", p(r"Down \(12/2 = 6\), up \(12/3 = 4\): boat \(5\), river \(1\).")),
       ("Second boat", r"\[\begin{aligned} \frac{12}{v - 1} + \frac{12}{v + 1} &= 6 \\ v^2 - 4v - 1 &= 0 \\ v &= 2 + \sqrt5 \approx 4.24 \end{aligned}\]" + p(r"This is the slower boat (\(4.24 < 5\)).")),
       ("A to B (downstream)", r"\[\frac{12}{3 + \sqrt5} = \frac{12(3 - \sqrt5)}{4} = 3(3 - \sqrt5)\]")) + final("Option 2"),
 shortcut=r"Downstream for the slower boat must take more than \(2\) h (the faster boat’s time) but well under \(3\) h: \(3(3 - \sqrt5) \approx 2.29\).",
 concept=r"\[\text{downstream} = v + r \qquad \text{upstream} = v - r\]",
 why_rows=[("1", r"\(\approx 15.7\) h: far too slow for a downstream trip."), ("3", r"\(\approx 3.7\) h: that is roughly the upstream time."), ("4", r"\(\approx 2.8\) h: doesn’t satisfy the 6-hour round trip.")])

P.qa(10, r"There are three persons A, B and C in a room. If a person D joins the room, the average weight of the persons in the room reduces by \(x\) kg. Instead of D, if person E joins the room, the average weight of the persons in the room increases by \(2x\) kg. If the weight of E is \(12\) kg more than that of D, then the value of \(x\) is",
 M("2", "1", "1.5", "0.5"), "MCQ", "2", ["Arithmetic::Average"], "Easy",
 "Both new averages are over four people. Subtract them.",
 steps(("Subtract", r"\[\frac{S + E}{4} - \frac{S + D}{4} = 2x - (-x) = 3x\]"),
       ("Solve", r"\[\frac{12}{4} = 3x \Rightarrow x = 1\]")) + final(r"\(1\) — option 2"),
 shortcut="Swapping D for E changes the four-person total by 12, so the average by 3 = x + 2x.",
 concept=r"\[\Delta(\text{average}) = \frac{\Delta(\text{total})}{\text{count}}\]",
 why_rows=[("1", r"Would need E − D \(= 4 \times 6 = 24\) kg."), ("3", r"Would need E − D \(= 18\) kg."), ("4", r"Would need E − D \(= 6\) kg.")])

P.qa(11, r"The population of a town in 2020 was \(1{,}00{,}000\). The population decreased by \(y\%\) from the year 2020 to 2021, and increased by \(x\%\) from the year 2021 to 2022, where \(x\) and \(y\) are two natural numbers. If population in 2022 was greater than the population in 2020 and the difference between \(x\) and \(y\) is \(10\), then the lowest possible population of the town in 2021 was",
 M("73{,}000", "75{,}000", "74{,}000", "72{,}000"), "MCQ", "1", ["Arithmetic::Percentages"], "Medium",
 r"For a net rise, \(x > y\), so \(x = y + 10\). The lowest 2021 population needs the largest \(y\).",
 steps(("Condition", r"\[\begin{aligned} (100 - y)(110 + y) &> 10000 \\ y^2 + 10y - 1000 &< 0 \end{aligned}\]"),
       ("Largest y", p(r"\(y = 27\): \(73 \times 137 = 10001 > 10000\) ✓. \(y = 28\): \(72 \times 138 = 9936\) ✗."))) + final(r"\(1{,}00{,}000 \times 0.73 = 73{,}000\) — option 1"),
 shortcut="Test from the smallest option up: 72,000 fails (72 × 138 < 10,000), 73,000 passes.",
 concept=r"\[\text{net change} = \left(1 - \tfrac{y}{100}\right)\left(1 + \tfrac{x}{100}\right)\]",
 why_rows=[("2", "Possible, but not the lowest."), ("3", "Possible, but not the lowest."), ("4", r"\(72 \times 138 = 9936 < 10000\): the 2022 population would fall.")])

P.qa(12, r"Anil mixes cocoa with sugar in the ratio \(3 : 2\) to prepare mixture A, and coffee with sugar in the ratio \(7 : 3\) to prepare mixture B. He combines mixtures A and B in the ratio \(2 : 3\) to make a new mixture C. If he mixes C with an equal amount of milk to make a drink, then the percentage of sugar in this drink will be",
 M("24", "16", "17", "21"), "MCQ", "3", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Sugar is 2/5 of A and 3/10 of B.",
 steps(("Sugar in C", r"\[\tfrac25 \cdot \tfrac25 + \tfrac35 \cdot \tfrac3{10} = \tfrac{4}{25} + \tfrac{9}{50} = \tfrac{17}{50} = 34\%\]"),
       ("Add milk", p(r"Equal milk halves it: \(17\%\)."))) + final(r"\(17\%\) — option 3"),
 shortcut="Take 50 units of C: 20 of A (8 sugar) + 30 of B (9 sugar) = 17 sugar in 100 units of drink.",
 concept=r"\[\text{blend} = \sum \text{share} \times \text{concentration}\]",
 why_rows=[("1", r"Would need \(48\%\) sugar in C; it has \(34\%\)."), ("2", r"Would need \(32\%\) sugar in C."), ("4", r"Would need \(42\%\) sugar in C.")])

P.qa(13, r"Rahul, Rakshita and Gurmeet, working together, would have taken more than \(7\) days to finish a job. On the other hand, Rahul and Gurmeet, working together would have taken less than \(15\) days to finish the job. However, they all worked together for \(6\) days, followed by Rakshita, who worked alone for \(3\) more days to finish the job. If Rakshita had worked alone on the job then the number of days she would have taken to finish the job, cannot be",
 M("20", "21", "16", "17"), "MCQ", "2", ["Arithmetic::Time_and_Work"], "Medium",
 r"Let Rakshita’s rate be \(k\) and all three together \(T\). Use \(6T + 3k = 1\) with both inequalities.",
 steps(("Together", r"\[T = \frac{1 - 3k}{6} < \frac17 \Rightarrow k > \frac1{21}\]"),
       ("Rahul + Gurmeet", r"\[T - k = \frac{1 - 9k}{6} > \frac1{15} \Rightarrow k < \frac1{15}\]"),
       ("Range", p(r"Her time \(\tfrac1k\) is strictly between \(15\) and \(21\) days."))) + final(r"\(21\) — option 2"),
 shortcut="Both bounds are strict (“more than”, “less than”), so the endpoint 21 is excluded.",
 concept=r"\[\text{rate} = \frac1{\text{days}} \qquad \text{work} = \text{rate} \times \text{time}\]",
 why_rows=[("1", "Inside the range 15–21."), ("3", "Inside the range."), ("4", "Inside the range.")])

P.qa(14, r"The number of coins collected per week by two coin-collectors A and B are in the ratio \(3 : 4\). If the total number of coins collected by A in \(5\) weeks is a multiple of \(7\), and the total number of coins collected by B in \(3\) weeks is a multiple of \(24\), then the minimum possible number of coins collected by A in one week is",
 [], "TITA", "42", ["Arithmetic::Ratio_and_Proportion", "Number_System::Factors_and_Divisibility"], "Easy",
 r"Let A collect \(3k\) and B \(4k\) a week.",
 steps(("Conditions", p(r"\(15k\) a multiple of \(7\) ⇒ \(7 \mid k\). \(12k\) a multiple of \(24\) ⇒ \(k\) even.")),
       ("Smallest", p(r"\(k = 14\), so A collects \(3 \times 14 = 42\)."))) + final(r"\(42\)"),
 shortcut=r"\(k\) must be a multiple of \(\operatorname{lcm}(7, 2) = 14\).",
 concept=r"\[a \mid bk,\ \gcd(a, b) = 1 \Rightarrow a \mid k\]")

P.qa(15, r"Gautam and Suhani, working together, can finish a job in \(20\) days. If Gautam does only \(60\%\) of his usual work on a day, Suhani must do \(150\%\) of her usual work on that day to exactly make up for it. Then, the number of days required by the faster worker to complete the job working alone is",
 [], "TITA", "36", ["Arithmetic::Time_and_Work"], "Easy",
 "The 40% Gautam drops equals the extra 50% Suhani adds.",
 steps(("Ratio", r"\[0.4G = 0.5S \Rightarrow G : S = 5 : 4\]"),
       ("Faster = Gautam", r"\[G = \tfrac59 \times \tfrac1{20} = \tfrac1{36}\]")) + final(r"\(36\) days"),
 shortcut="Together 9 units a day for 20 days = 180 units; Gautam does 5 a day ⇒ 36 days.",
 concept=r"\[\text{time} = \frac{\text{total work}}{\text{rate}}\]")

P.qa(16, r"A fruit seller has a stock of mangoes, bananas and apples with at least one fruit of each type. At the beginning of a day, the number of mangoes make up \(40\%\) of his stock. That day, he sells half of the mangoes, \(96\) bananas and \(40\%\) of the apples. At the end of the day, he ends up selling \(50\%\) of the fruits. The smallest possible total number of fruits in the stock at the beginning of the day is",
 [], "TITA", "340", ["Arithmetic::Percentages", "Number_System::Miscellaneous"], "Hard",
 r"Let the stock be \(N\) and apples \(a\). Write the “sold half” condition, then use whole-number constraints.",
 steps(("Apples", r"\[0.2N + 96 + 0.4a = 0.5N \Rightarrow a = 0.75N - 240\]"),
       ("Limits", p(r"\(a \ge 1\) ⇒ \(N > 320\). Bananas \(= 0.6N - a = 240 - 0.15N \ge 96\) ⇒ \(N \le 960\).")),
       ("Whole numbers", p(r"Half the mangoes \(0.2N\), \(0.15N\) and \(0.75N\) must be integers, so \(N\) is a multiple of \(20\). Smallest above \(320\): \(340\).")),
       ("Check 340", p(r"Mangoes \(136\), apples \(15\), bananas \(189\). Sold \(68 + 96 + 6 = 170 = 50\%\) ✓"))) + final(r"\(340\)"),
 shortcut="N = 320 gives zero apples, so step to the next multiple of 20.",
 concept=r"\[\text{fractions of a count must be whole numbers}\]")

P.qa(17, r"Let \(\triangle ABC\) be an isosceles triangle such that \(AB\) and \(AC\) are of equal length. \(AD\) is the altitude from \(A\) on \(BC\) and \(BE\) is the altitude from \(B\) on \(AC\). If \(AD\) and \(BE\) intersect at \(O\) such that \(\angle AOB = 105^\circ\), then \(\dfrac{AD}{BE}\) is",
 M(r"2\cos 15^\circ", r"\sin 15^\circ", r"2\sin 15^\circ", r"\cos 15^\circ"), "MCQ", "1", ["Geometry::Triangles", "Geometry::Trigonometry"], "Medium",
 r"\(\angle AOE = 180^\circ - 105^\circ\). Triangle \(AOE\) has a right angle at \(E\).",
 steps(("Apex angle", p(r"\(\angle AOE = 75^\circ\), so \(\angle OAE = 15^\circ\). \(AD\) bisects \(\angle A\), so \(\angle A = 30^\circ\).")),
       ("Lengths", r"\[AD = AB\cos 15^\circ\]\[BE = AB\sin 30^\circ = \tfrac{AB}{2}\]"),
       ("Ratio", r"\[\frac{AD}{BE} = 2\cos 15^\circ\]")) + final("Option 1"),
 shortcut=r"The ratio is about \(1.93\): only \(2\cos 15^\circ\) is bigger than 1 by that much.",
 concept=p("In an isosceles triangle, the altitude to the base also bisects the apex angle.") + r"\[\text{altitude from } B = AB\sin A\]",
 why_rows=[("2", r"\(\approx 0.26\): less than 1, but \(AD\) is clearly longer than \(BE\)."), ("3", r"\(\approx 0.52\): uses sine for \(AD\)."), ("4", r"Forgets that \(BE = \tfrac{AB}{2}\).")])

P.qa(18, r"A rectangle with the largest possible area is drawn inside a semicircle of radius \(2\) cm. Then, the ratio of the lengths of the largest to the smallest side of this rectangle is",
 M("1 : 1", "2 : 1", r"\sqrt5 : 1", r"\sqrt2 : 1"), "MCQ", "2", ["Geometry::Circles", "Geometry::Polygons_and_Quadrilaterals"], "Easy",
 r"Put the rectangle’s base on the diameter: base \(2x\), height \(y\), with \(x^2 + y^2 = r^2\).",
 steps(("Maximise", p(r"Area \(2xy\) is largest when \(x = y\) (for fixed \(x^2 + y^2\)).")),
       ("Sides", p(r"Base \(2x\), height \(y = x\): ratio \(2 : 1\)."))) + final(r"\(2 : 1\) — option 2"),
 shortcut="Reflect the semicircle into a full circle: the best rectangle becomes a square made of two halves, so each half is 2 : 1.",
 concept=r"\[x^2 + y^2 = r^2 \Rightarrow xy \le \tfrac{r^2}{2}\ (\text{equal when } x = y)\]",
 why_rows=[("1", r"Area \(3.2\), less than the maximum \(4\)."), ("3", r"Area \(\approx 3.98\), just under \(4\)."), ("4", r"Area \(\approx 3.77\), less than \(4\).")])

P.qa(19, r"In a regular polygon, any interior angle exceeds the exterior angle by \(120\) degrees. Then, the number of diagonals of this polygon is",
 [], "TITA", "54", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "Interior + exterior = 180°.",
 steps(("Angles", r"\[\begin{aligned} I - E = 120,\ I + E &= 180 \\ E &= 30^\circ \\ n &= \tfrac{360}{30} = 12 \end{aligned}\]"),
       ("Diagonals", r"\[\frac{12 \times 9}{2} = 54\]")) + final(r"\(54\)"),
 shortcut="Exterior angle 30° ⇒ a 12-gon.",
 concept=r"\[\text{exterior angle} = \frac{360^\circ}{n} \qquad \text{diagonals} = \frac{n(n - 3)}{2}\]")

P.qa(20, r"<p>The value of</p>\[\begin{aligned} &1 + \left(1 + \frac13\right)\frac14 + \left(1 + \frac13 + \frac19\right)\frac1{16} \\ &+ \left(1 + \frac13 + \frac19 + \frac1{27}\right)\frac1{64} + \cdots \end{aligned}\]<p>is</p>",
 M(r"\dfrac{15}{8}", r"\dfrac{15}{13}", r"\dfrac{16}{11}", r"\dfrac{27}{12}"), "MCQ", "3", ["Algebra::Progressions_and_Series"], "Hard",
 r"The \(k\)-th bracket is a GP sum: \(1 + \tfrac13 + \dots + \tfrac1{3^k} = \tfrac32\left(1 - \tfrac1{3^{k+1}}\right)\).",
 steps(("General term", r"\[S = \sum_{k \ge 0} \tfrac32\left(1 - \tfrac{1}{3^{k+1}}\right)\frac1{4^k}\]"),
       ("Split", r"\[S = \tfrac32\left[\sum \frac1{4^k} - \tfrac13\sum \frac1{12^k}\right] = \tfrac32\left[\tfrac43 - \tfrac13 \cdot \tfrac{12}{11}\right]\]"),
       ("Simplify", r"\[S = \tfrac32 \cdot \tfrac{32}{33} = \tfrac{16}{11}\]")) + final("Option 3"),
 shortcut=p(r"Swap the order of summation. The \(1\) in every bracket pairs with all of \(1, \tfrac14, \tfrac1{16}, \dots\) (sum \(\tfrac43\)); each \(\tfrac1{3^j}\) pairs with \(\tfrac1{4^j}, \tfrac1{4^{j+1}}, \dots\) (sum \(\tfrac43 \cdot \tfrac1{12^j}\)).") + r"\[S = \tfrac43\left(1 + \tfrac1{12} + \tfrac1{144} + \cdots\right) = \tfrac43 \cdot \tfrac{12}{11} = \tfrac{16}{11}\]",
 concept=r"\[a + ar + ar^2 + \dots = \frac{a}{1 - r}\ (|r| < 1)\]",
 why_rows=[("1", r"\(1.875\): too big; the first few terms already settle near \(1.45\)."), ("2", r"\(\approx 1.15\): smaller than the first two terms (\(1 + \tfrac13 = 1.33\))."), ("4", r"\(2.25\): far too big.")])

P.qa(21, r"Let \(a_n = 46 + 8n\) and \(b_n = 98 + 4n\) be two sequences for natural numbers \(n \le 100\). Then, the sum of all terms common to both the sequences is",
 M("14602", "14798", "15000", "14900"), "MCQ", "4", ["Algebra::Progressions_and_Series"], "Medium",
 r"\(a_n\) runs \(54, 62, \dots, 846\) and \(b_n\) runs \(102, 106, \dots, 498\). Common terms step by \(8\).",
 steps(("First and last", p(r"\(a_n \equiv 6 \pmod 8\). In \(b_n\)’s range, the first such number is \(102\) and the last is \(494\).")),
       ("Count and sum", r"\[\frac{494 - 102}{8} + 1 = 50 \text{ terms}\]\[\frac{50(102 + 494)}{2} = 14900\]")) + final(r"\(14900\) — option 4"),
 shortcut="Common terms of APs with differences 8 and 4 form an AP with difference 8, inside the overlap of the ranges.",
 concept=r"\[S = \frac{n}{2}(\text{first} + \text{last})\]",
 why_rows=[("1", "Not the sum of the 50 common terms (102 to 494)."), ("2", "14900 − 102: drops the first common term."), ("3", "Not the sum of the 50 common terms.")])

P.qa(22, r"Suppose \(f(x, y)\) is a real-valued function such that \(f(3x + 2y,\ 2x - 5y) = 19x\), for all real numbers \(x\) and \(y\). The value of \(x\) for which \(f(x, 2x) = 27\), is",
 [], "TITA", "3", ["Algebra::Functions"], "Medium",
 r"Let \(u = 3x + 2y\), \(v = 2x - 5y\). Find a combination of \(u\) and \(v\) that equals \(19x\).",
 steps(("Eliminate y", r"\[5u + 2v = 15x + 10y + 4x - 10y = 19x\]" + p(r"So \(f(u, v) = 5u + 2v\).")),
       ("Solve", r"\[f(x, 2x) = 5x + 4x = 9x = 27 \Rightarrow x = 3\]")) + final(r"\(3\)"),
 shortcut="Multiply to cancel y: 5 × (2y) and 2 × (−5y).",
 concept=p(r"Write the right-hand side in terms of the inputs \((u, v)\), then substitute."))
