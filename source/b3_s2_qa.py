# -*- coding: utf-8 -*-
# Batch 3 — CAT 2023 Slot 2: QA Q1–22.
from fmt import steps, final, why, table, p
from b3_s2 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"For any natural numbers \(m\), \(n\) and \(k\), such that \(k\) divides both \(m + 2n\) and \(3m + 4n\), \(k\) must be a common divisor of",
 M(r"m \text{ and } n", r"m \text{ and } 2n", r"2m \text{ and } 3n", r"2m \text{ and } n"), "MCQ", "2", ["Number_System::Factors_and_Divisibility"], "Easy",
 "If k divides two numbers, it divides any combination of them. Combine them to kill m, then to kill n.",
 steps(("Eliminate m", r"\[3(m + 2n) - (3m + 4n) = 2n \;\Rightarrow\; k \mid 2n\]"),
       ("Eliminate n", r"\[(3m + 4n) - 2(m + 2n) = m \;\Rightarrow\; k \mid m\]")) + final(r"\(k\) divides \(m\) and \(2n\) — option 2"),
 shortcut=r"Test \(m = 2, n = 1\): \(m + 2n = 4\), \(3m + 4n = 10\), so \(k = 2\) works. \(2\) doesn’t divide \(n = 1\), which rules out options 1 and 4; it doesn’t divide \(3n = 3\), which rules out option 3.",
 concept=r"\[k \mid a,\ k \mid b \;\Rightarrow\; k \mid (xa + yb) \text{ for any integers } x, y\]",
 why_rows=[("1", r"\(m = 2, n = 1, k = 2\): \(k\) doesn’t divide \(n\)."), ("3", r"Same example: \(2 \nmid 3n = 3\)."), ("4", r"Same example: \(2 \nmid n\).")])

P.qa(2, r"The sum of all possible values of \(x\) satisfying the equation \(2^{4x^2} - 2^{2x^2 + x + 16} + 2^{2x + 30} = 0\), is",
 M("3", r"\dfrac52", r"\dfrac32", r"\dfrac12"), "MCQ", "4", ["Algebra::Logarithms_and_Exponents", "Algebra::Quadratic_Equations"], "Medium",
 r"Write every term using \(a = 2^{2x^2}\) and \(b = 2^{x + 15}\).",
 steps(("Substitute", p(r"\(2^{4x^2} = a^2\), \(2^{2x + 30} = b^2\) and \(2^{2x^2 + x + 16} = 2 \cdot 2^{2x^2} \cdot 2^{x + 15} = 2ab\).") + r"\[a^2 - 2ab + b^2 = (a - b)^2 = 0 \;\Rightarrow\; a = b\]"),
       ("Equate powers", r"\[\begin{aligned} 2x^2 &= x + 15 \\ 2x^2 - x - 15 &= 0 \\ (2x + 5)(x - 3) &= 0 \end{aligned}\]" + p(r"\(x = 3\) or \(x = -\tfrac52\).")))
 + final(r"Sum \(= 3 - \tfrac52 = \tfrac12\) — option 4"),
 shortcut=r"Once you see a perfect square, you only need the sum of roots of \(2x^2 - x - 15 = 0\): \(-\tfrac{b}{a} = \tfrac12\).",
 concept=r"\[a^2 - 2ab + b^2 = (a - b)^2 \qquad \alpha + \beta = -\tfrac{b}{a}\]",
 why_rows=[("1", r"That’s one root (\(3\)), not the sum."), ("2", r"That’s the size of the other root, \(-\tfrac52\)."), ("3", r"Comes from a sign slip in factoring (roots \(3\) and \(-\tfrac32\)).")])

P.qa(3, r"Any non-zero real numbers \(x, y\) such that \(y \ne 3\) and \(\dfrac{x}{y} < \dfrac{x + 3}{y - 3}\), will satisfy the condition",
 [r"If \(y > 10\), then \(-x > y\)", r"\(\dfrac{x}{y} < \dfrac{y}{x}\)", r"If \(x < 0\), then \(-x < y\)", r"If \(y < 0\), then \(-x < y\)"], "MCQ", "4", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Move everything to one side and combine into a single fraction.",
 steps(("One fraction", r"\[\frac{x + 3}{y - 3} - \frac{x}{y} = \frac{y(x + 3) - x(y - 3)}{y(y - 3)} = \frac{3(x + y)}{y(y - 3)} > 0\]"),
       ("Case y < 0", p(r"Then \(y - 3 < 0\) too, so \(y(y - 3) > 0\). The numerator must be positive: \(x + y > 0\), i.e. \(-x < y\)."))) + final("Option 4"),
 shortcut=r"The condition boils down to “\(x + y\) and \(y(y - 3)\) have the same sign”. Check each option’s case against that.",
 concept=r"\[\frac{A}{B} > 0 \iff A, B \text{ have the same sign}\]",
 why_rows=[("1", r"For \(y > 10\), \(y(y - 3) > 0\), so \(x + y > 0\): \(-x < y\), the opposite."), ("2", r"\(x = y = 4\) satisfies the condition, but \(\tfrac{x}{y} = \tfrac{y}{x}\)."), ("3", r"\(x = -2, y = 1\) satisfies it (\(0 < y < 3\) needs \(x + y < 0\)), yet \(-x = 2 > y\).")])

P.qa(4, r"Let \(a, b, m\) and \(n\) be natural numbers such that \(a > 1\) and \(b > 1\). If \(a^m b^n = 144^{145}\), then the largest possible value of \(n - m\) is",
 M("579", "580", "289", "290"), "MCQ", "1", ["Number_System::Factors_and_Divisibility", "Algebra::Surds_and_Indices"], "Medium",
 r"Factorise \(144^{145}\) into primes. Make \(n\) as large as possible and \(m\) as small as possible.",
 steps(("Prime form", r"\[144^{145} = (2^4 \cdot 3^2)^{145} = 2^{580} \cdot 3^{290}\]"),
       ("Largest n", p(r"\(b > 1\) contains some prime, so \(n \le 580\). \(n = 580\) needs \(b = 2\).")),
       ("Smallest m", p(r"Then \(a^m = 3^{290}\); take \(m = 1\), \(a = 3^{290}\)."))) + final(r"\(n - m = 580 - 1 = 579\) — option 1"),
 shortcut=r"Give \(b\) the prime with the biggest exponent (\(2^{580}\)) and dump everything else into \(a\) with \(m = 1\).",
 concept=r"\[b^n \mid p_1^{e_1} p_2^{e_2} \;\Rightarrow\; n \le \max(e_1, e_2)\]",
 why_rows=[("2", r"Needs \(m = 0\), but \(m\) is a natural number."), ("3", r"Uses \(3^{290}\) for \(b\); \(2^{580}\) gives more."), ("4", r"Same mistake, and it ignores \(m \ge 1\).")])

P.qa(5, r"Let \(k\) be the largest integer such that the equation \((x - 1)^2 + 2kx + 11 = 0\) has no real roots. If \(y\) is a positive real number, then the least possible value of \(\dfrac{k}{4y} + 9y\) is",
 [], "TITA", "6", ["Algebra::Quadratic_Equations", "Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Expand to a standard quadratic and make its discriminant negative. Then use AM ≥ GM.",
 steps(("Expand", r"\[x^2 + (2k - 2)x + 12 = 0\]"),
       ("No real roots", r"\[\begin{aligned} (2k - 2)^2 - 48 &< 0 \\ (k - 1)^2 &< 12 \\ k - 1 &< 2\sqrt3 \approx 3.46 \end{aligned}\]" + p(r"Largest integer \(k = 4\).")),
       ("AM ≥ GM", r"\[\frac{4}{4y} + 9y = \frac1y + 9y \ge 2\sqrt{\frac1y \cdot 9y} = 6\]" + p(r"Equality at \(y = \tfrac13\)."))) + final(r"\(6\)"),
 shortcut=r"For \(\tfrac{A}{y} + By\) (\(y > 0\)) the minimum is always \(2\sqrt{AB}\).",
 concept=r"\[\frac{A}{y} + By \ge 2\sqrt{AB} \quad (y > 0) \qquad \text{no real roots} \iff b^2 - 4ac < 0\]")

P.qa(6, r"The number of positive integers less than \(50\), having exactly two distinct factors other than \(1\) and itself, is",
 [], "TITA", "15", ["Number_System::Factors_and_Divisibility"], "Easy",
 r"Exactly four factors in total. Which prime shapes give that?",
 steps(("Shapes", p(r"Four factors means \(N = p^3\) or \(N = pq\) (distinct primes).")),
       ("p³", p(r"\(8, 27\): \(2\) numbers.")),
       ("pq < 50", p(r"\(2 \times\) \(\{3, 5, 7, 11, 13, 17, 19, 23\}\): \(8\). \(3 \times \{5, 7, 11, 13\}\): \(4\). \(5 \times 7\): \(1\). Total \(13\).")))
 + final(r"\(2 + 13 = 15\)"),
 shortcut="Don’t forget the cubes 8 and 27; most slips come from counting only pq.",
 concept=r"\[N = p^a q^b \;\Rightarrow\; \text{number of factors} = (a + 1)(b + 1)\]")

P.qa(7, r"For some positive real number \(x\), if \(\log_{\sqrt3} x + \dfrac{\log_x 25}{\log_x 0.008} = \dfrac{16}{3}\), then the value of \(\log_3 (3x^2)\) is",
 [], "TITA", "7", ["Algebra::Logarithms_and_Exponents"], "Easy",
 r"The fraction is a change of base: \(\tfrac{\log_x 25}{\log_x 0.008} = \log_{0.008} 25\).",
 steps(("Simplify the fraction", p(r"\(25 = 5^2\) and \(0.008 = 5^{-3}\), so the fraction is \(\tfrac{2}{-3} = -\tfrac23\).")),
       ("Solve", r"\[\begin{aligned} 2\log_3 x - \tfrac23 &= \tfrac{16}{3} \\ \log_3 x &= 3 \end{aligned}\]"),
       ("Target", r"\[\log_3(3x^2) = 1 + 2\log_3 x = 7\]")) + final(r"\(7\)"),
 shortcut=r"You never need \(x = 27\) itself; \(\log_3 x = 3\) is enough.",
 concept=r"\[\log_{\sqrt a} x = 2\log_a x \qquad \frac{\log_c A}{\log_c B} = \log_B A \qquad \log(ab^2) = \log a + 2\log b\]")

P.qa(8, "Pipes A and C are fill pipes while Pipe B is a drain pipe of a tank. Pipe B empties the full tank in one hour less than the time taken by Pipe A to fill the empty tank. When pipes A, B and C are turned on together, the empty tank is filled in two hours. If pipes B and C are turned on together when the tank is empty and Pipe B is turned off after one hour, then Pipe C takes another one hour and 15 minutes to fill the remaining tank. If Pipe A can fill the empty tank in less than five hours, then the time taken, in minutes, by Pipe C to fill the empty tank is",
 M("60", "90", "75", "120"), "MCQ", "2", ["Arithmetic::Time_and_Work"], "Hard",
 r"Let A take \(a\) hours (B takes \(a - 1\)) and C take \(c\) hours. Write the two scenarios as equations in rates.",
 steps(("Equations", r"\[\begin{aligned} \tfrac1a - \tfrac{1}{a-1} + \tfrac1c &= \tfrac12 \\ \left(\tfrac1c - \tfrac{1}{a-1}\right) + \tfrac{1.25}{c} &= 1 \end{aligned}\]"),
       ("Eliminate c", p(r"From the first, \(\tfrac1c = \tfrac12 - \tfrac1a + \tfrac{1}{a-1}\). Substitute into \(\tfrac{2.25}{c} - \tfrac{1}{a-1} = 1\):") +
        r"\[\begin{aligned} \tfrac{2.25}{a} - \tfrac{1.25}{a - 1} &= \tfrac18 \\ a^2 - 9a + 18 &= 0 \\ a &= 3 \text{ or } 6 \end{aligned}\]"),
       ("Use a < 5", r"\[a = 3:\quad \tfrac1c = \tfrac12 - \tfrac13 + \tfrac12 = \tfrac23 \;\Rightarrow\; c = 1.5 \text{ h}\]")) + final(r"\(90\) minutes — option 2"),
 shortcut=r"Test the options: \(c = 1.5\) h gives rate \(\tfrac23\); the second scenario needs \(\tfrac{2.25}{1.5} - \tfrac{1}{a-1} = 1\), so \(a = 3\), and then the first equation checks out: \(\tfrac13 - \tfrac12 + \tfrac23 = \tfrac12\) ✓.",
 concept=r"\[\text{rate} = \frac{1}{\text{time}} \qquad \text{work} = \sum \text{rate} \times \text{time} \;(\text{drain} < 0)\]",
 why_rows=[("1", r"\(c = 1\): \(2.25 - \tfrac{1}{a - 1} = 1\) gives \(a = 1.8\), so B would take \(0.8\) h and the first scenario fails."), ("3", r"\(c = 1.25\): gives \(a = 2.25\), which fails the first equation."), ("4", r"\(c = 2\): gives \(a = 9\), above the 5-hour limit.")])

P.qa(9, r"Anil borrows ₹ 2 lakhs at an interest rate of \(8\%\) per annum, compounded half-yearly. He repays ₹ \(10{,}320\) at the end of the first year and closes the loan by paying the outstanding amount at the end of the third year. Then, the total interest, in rupees, paid over the three years is nearest to",
 M("40{,}991", "45{,}311", "33{,}130", "51{,}311"), "MCQ", "4", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 r"Half-yearly at 8% p.a. means 4% every six months. Work out the balance at the end of year 1, subtract the repayment, then grow it for two more years.",
 steps(("End of year 1", r"\[200000 \times 1.04^2 = 216320\]" + p(r"After paying \(10{,}320\): \(206{,}000\).")),
       ("End of year 3", r"\[206000 \times 1.04^4 = 206000 \times 1.16986 \approx 240991\]"),
       ("Interest", r"\[(10320 + 240991) - 200000 = 51311\]")) + final(r"≈ ₹\(51{,}311\) — option 4"),
 shortcut=r"The repayment of \(10{,}320\) is exactly the year-1 interest \(16{,}320\) minus \(6{,}000\); a round \(206{,}000\) remains, which is the cue you’re on track.",
 concept=r"\[A = P\left(1 + \frac{r}{2 \cdot 100}\right)^{2t} \;\text{(half-yearly)}\]",
 why_rows=[("1", "Forgets the ₹10,320 paid at the end of year 1: 2,40,991 − 2,00,000."), ("2", "Not reachable with 4% per half-year; recheck the compounding."), ("3", "Too small: the 2,06,000 balance alone earns about ₹35,000 in years 2–3.")])

P.qa(10, "Ravi is driving at a speed of 40 km/h on a road. Vijay is 54 metres behind Ravi and driving in the same direction as Ravi. Ashok is driving along the same road from the opposite direction at a speed of 50 km/h and is 225 metres away from Ravi. The speed, in km/h, at which Vijay should drive so that all the three cross each other at the same time, is",
 M("67.2", "58.8", "61.6", "64.4"), "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "First find when Ravi and Ashok meet. Vijay must reach the same point at the same moment.",
 steps(("Ravi meets Ashok", r"\[t = \frac{225 \text{ m}}{(40 + 50) \text{ km/h}} = \frac{225}{25 \text{ m/s}} = 9 \text{ s}\]"),
       ("Distance for Vijay", p(r"Ravi covers \(\tfrac{100}{9} \times 9 = 100\) m, so Vijay covers \(54 + 100 = 154\) m in \(9\) s.")),
       ("Speed", r"\[\frac{154}{9} \text{ m/s} \times \frac{18}{5} = 61.6 \text{ km/h}\]")) + final(r"\(61.6\) km/h — option 3"),
 shortcut=r"Relative to Ravi, Vijay must close \(54\) m in \(9\) s: \(6\) m/s \(= 21.6\) km/h faster than Ravi, so \(40 + 21.6 = 61.6\).",
 concept=r"\[\text{1 m/s} = 3.6 \text{ km/h} \qquad t = \frac{\text{gap}}{\text{relative speed}}\]",
 why_rows=[("1", r"In \(9\) s Vijay would cover \(168\) m, \(14\) m too far."), ("2", r"Covers \(147\) m, \(7\) m short."), ("4", r"Covers \(161\) m, \(7\) m too far.")])

P.qa(11, r"Minu purchases a pair of sunglasses at ₹ \(1{,}000\) and sells to Kanu at \(20\%\) profit. Then, Kanu sells it back to Minu at \(20\%\) loss. Finally, Minu sells the same pair of sunglasses to Tanu. If the total profit made by Minu from all her transactions is ₹ \(500\), then the percentage of profit made by Minu when she sold the pair of sunglasses to Tanu is",
 [r"\(26\%\)", r"\(31.25\%\)", r"\(52\%\)", r"\(35.42\%\)"], "MCQ", "2", ["Arithmetic::Profit_Loss_and_Discount"], "Easy",
 "Track the cash: what Minu paid and received at each step.",
 steps(("Prices", p(r"Minu → Kanu: \(1200\). Kanu → Minu: \(1200 \times 0.8 = 960\).")),
       ("Final sale", r"\[-1000 + 1200 - 960 + S = 500 \;\Rightarrow\; S = 1260\]"),
       ("Profit % on that sale", r"\[\frac{1260 - 960}{960} \times 100 = 31.25\%\]")) + final(r"\(31.25\%\) — option 2"),
 shortcut="The last sale’s profit % is on Minu’s second cost price (960), not the original 1000.",
 concept=r"\[\text{Profit \%} = \frac{SP - CP}{CP} \times 100\]",
 why_rows=[("1", r"Sale at \(1209.60\): total profit only \(449.60\)."), ("3", r"Sale at \(1459.20\): total profit \(699.20\)."), ("4", r"Sale at \(1300\): total profit \(540\); it is \(30\%\) on 1000, mixed bases.")])

P.qa(12, r"The price of a precious stone is directly proportional to the square of its weight. Sita has a precious stone weighing \(18\) units. If she breaks it into four pieces with each piece having distinct integer weight, then the difference between the highest and lowest possible values of the total price of the four pieces will be \(2{,}88{,}000\). Then, the price of the original precious stone is",
 M("9{,}72{,}000", "12{,}96{,}000", "19{,}44{,}000", "16{,}20{,}000"), "MCQ", "2", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 "Price = k × weight². Sum of squares is largest when the pieces are as uneven as possible and smallest when they’re as even as possible.",
 steps(("Extremes", p(r"Most uneven: \(1, 2, 3, 12\): \(1 + 4 + 9 + 144 = 158\). Most even: \(3, 4, 5, 6\): \(9 + 16 + 25 + 36 = 86\).")),
       ("Find k", r"\[k(158 - 86) = 288000 \;\Rightarrow\; k = 4000\]"),
       ("Original", r"\[4000 \times 18^2 = 12{,}96{,}000\]")) + final(r"₹\(12{,}96{,}000\) — option 2"),
 shortcut=r"For a fixed sum, \(\sum w^2\) grows as the parts spread out.",
 concept=r"\[P = k w^2 \qquad \text{fixed } \textstyle\sum w \Rightarrow \sum w^2 \text{ min when parts are equal}\]",
 why_rows=[("1", r"Means \(k = 3000\): the gap would be \(72 \times 3000 = 2{,}16{,}000\)."), ("3", r"Means \(k = 6000\): gap \(4{,}32{,}000\)."), ("4", r"Means \(k = 5000\): gap \(3{,}60{,}000\).")])

P.qa(13, r"In a company, \(20\%\) of the employees work in the manufacturing department. If the total salary obtained by all the manufacturing employees is one-sixth of the total salary obtained by all the employees in the company, then the ratio of the average salary obtained by the manufacturing employees to the average salary obtained by the non-manufacturing employees is",
 M("4 : 5", "6 : 5", "5 : 6", "5 : 4"), "MCQ", "1", ["Arithmetic::Average", "Arithmetic::Ratio_and_Proportion"], "Easy",
 "Average = share of salary ÷ share of people.",
 steps(("Averages", r"\[\text{Mfg: } \frac{1/6}{1/5} = \frac56\]\[\text{Non-mfg: } \frac{5/6}{4/5} = \frac{25}{24}\]"),
       ("Ratio", r"\[\frac56 : \frac{25}{24} = 20 : 25 = 4 : 5\]")) + final(r"\(4 : 5\) — option 1"),
 shortcut="Take 10 employees and ₹60: 2 earn ₹10 (avg 5), 8 earn ₹50 (avg 6.25). 5 : 6.25 = 4 : 5.",
 concept=r"\[\text{average} = \frac{\text{total}}{\text{count}}\]",
 why_rows=[("2", "Inverse of 5 : 6, and neither is right."), ("3", r"Compares with the company average \((\tfrac56 : 1)\), not the non-manufacturing average."), ("4", "Inverted: manufacturing staff earn less on average.")])

P.qa(14, r"A container has \(40\) litres of milk. Then, \(4\) litres are removed from the container and replaced with \(4\) litres of water. This process of replacing \(4\) litres of the liquid in the container with an equal volume of water is continued repeatedly. The smallest number of times of doing this process, after which the volume of milk in the container becomes less than that of water, is",
 [], "TITA", "7", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Each step keeps 9/10 of the milk. When does milk fall below half?",
 steps(("Condition", r"\[40\left(\tfrac{9}{10}\right)^n < 20 \iff 0.9^n < 0.5\]"),
       ("Powers", p(r"\(0.9^6 \approx 0.531\), \(0.9^7 \approx 0.478\)."))) + final(r"\(7\)"),
 shortcut=r"\(0.9^2 = 0.81\), \(0.9^4 \approx 0.656\), \(0.9^6 \approx 0.531\): just above half, so one more step.",
 concept=r"\[\text{milk left} = V\left(1 - \frac{x}{V}\right)^n\]")

P.qa(15, r"If a certain amount of money is divided equally among \(n\) persons, each one receives ₹ \(352\). However, if two persons receive ₹ \(506\) each and the remaining amount is divided equally among the other persons, each of them receive less than or equal to ₹ \(330\). Then, the maximum possible value of \(n\) is",
 [], "TITA", "16", ["Arithmetic::Average"], "Easy",
 r"Total \(= 352n\). Write the per-person share of the others and apply \(\le 330\).",
 steps(("Inequality", r"\[\begin{aligned} \frac{352n - 1012}{n - 2} &\le 330 \\ 352n - 1012 &\le 330n - 660 \\ 22n &\le 352 \end{aligned}\]")) + final(r"\(n \le 16\): maximum \(16\)"),
 shortcut=r"The two people take \(2 \times 154 = 308\) extra; the other \(n - 2\) lose at least \(22\) each: \(22(n - 2) \le 308\) ⇒ \(n \le 16\).",
 concept=p("The extra paid to some people equals the shortfall spread over everyone else."))

P.qa(16, r"Jayant bought a certain number of white shirts at the rate of ₹ \(1{,}000\) per piece and a certain number of blue shirts at the rate of ₹ \(1{,}125\) per piece. For each shirt, he then set a fixed market price which was \(25\%\) higher than the average cost of all the shirts. He sold all the shirts at a discount of \(10\%\) and made a total profit of ₹ \(51{,}000\). If he bought both colours of shirts, then the maximum possible total number of shirts that he could have bought is",
 [], "TITA", "407", ["Arithmetic::Profit_Loss_and_Discount", "Number_System::Miscellaneous"], "Hard",
 r"Selling price is \(1.25 \times 0.9 = 1.125\) times average cost, so profit is \(12.5\%\) of the total cost.",
 steps(("Total cost", r"\[0.125 \times \text{cost} = 51000 \;\Rightarrow\; \text{cost} = 408000\]"),
       ("Equation", r"\[1000w + 1125b = 408000 \;\Rightarrow\; 8w + 9b = 3264\]"),
       ("Maximise w + b", p(r"Use as many cheap shirts as possible, so keep \(b\) small. \(3264\) is a multiple of \(8\), so \(8 \mid 9b\), so \(b\) is a multiple of \(8\). Smallest \(b = 8\): \(8w = 3192\), \(w = 399\).")))
 + final(r"\(399 + 8 = 407\)"),
 shortcut=r"\(w + b = 408 - \tfrac{b}{8}\) (from \(8(w + b) = 3264 - b\)); smallest valid \(b = 8\) gives \(407\).",
 concept=p(r"For \(ax + by = c\) in whole numbers, fix one variable by divisibility, then optimise."))

P.qa(17, r"A triangle is drawn with its vertices on the circle \(C\) such that one of its sides is a diameter of \(C\) and the other two sides have their lengths in the ratio \(a : b\). If the radius of the circle is \(r\), then the area of the triangle is",
 M(r"\dfrac{2abr^2}{a^2 + b^2}", r"\dfrac{4abr^2}{a^2 + b^2}", r"\dfrac{abr^2}{a^2 + b^2}", r"\dfrac{abr^2}{2(a^2 + b^2)}"), "MCQ", "1", ["Geometry::Circles", "Geometry::Triangles"], "Easy",
 "An angle in a semicircle is 90°. Let the legs be ak and bk.",
 steps(("Right triangle", r"\[(ak)^2 + (bk)^2 = (2r)^2 \;\Rightarrow\; k^2 = \frac{4r^2}{a^2 + b^2}\]"),
       ("Area", r"\[\tfrac12 (ak)(bk) = \tfrac12 ab \cdot \frac{4r^2}{a^2 + b^2} = \frac{2abr^2}{a^2 + b^2}\]")) + final("Option 1"),
 shortcut=r"Test \(a = b = 1\): an isosceles right triangle on diameter \(2r\) has area \(r^2\). Only option 1 gives \(r^2\).",
 concept=r"\[\text{angle in a semicircle} = 90^\circ \qquad \text{area} = \tfrac12 \times \text{leg}_1 \times \text{leg}_2\]",
 why_rows=[("2", r"Forgets the \(\tfrac12\): gives \(2r^2\) at \(a = b\)."), ("3", r"Gives \(\tfrac{r^2}{2}\) at \(a = b\); treats the radius as the hypotenuse."), ("4", r"Gives \(\tfrac{r^2}{4}\) at \(a = b\).")])

P.qa(18, r"In a rectangle \(ABCD\), \(AB = 9\) cm and \(BC = 6\) cm. \(P\) and \(Q\) are two points on \(BC\) such that the areas of the figures \(ABP\), \(APQ\), and \(AQCD\) are in geometric progression. If the area of the figure \(AQCD\) is four times the area of triangle \(ABP\), then \(BP : PQ : QC\) is",
 M("2 : 4 : 1", "1 : 2 : 4", "1 : 1 : 2", "1 : 2 : 1"), "MCQ", "1", ["Geometry::Polygons_and_Quadrilaterals", "Algebra::Progressions_and_Series"], "Medium",
 "Three terms in GP with the third four times the first means ratio 2. All three areas add up to the rectangle.",
 steps(("Areas", r"\[x + 2x + 4x = 9 \times 6 = 54 \;\Rightarrow\; x = \tfrac{54}{7}\]"),
       ("Lengths", p(r"Triangles \(ABP\) and \(APQ\) both have height \(AB = 9\): \(BP = \tfrac{2x}{9} = \tfrac{12}{7}\), \(PQ = \tfrac{2(2x)}{9} = \tfrac{24}{7}\), \(QC = 6 - \tfrac{36}{7} = \tfrac67\).")))
 + final(r"\(12 : 24 : 6 = 2 : 4 : 1\) — option 1"),
 shortcut=r"\(BP : PQ = 1 : 2\) straight from the area ratio (same height). Only options 1 and 2 have that; \(QC = 6 - BQ\) decides.",
 concept=r"\[\text{same height} \Rightarrow \text{area ratio} = \text{base ratio}\]",
 why_rows=[("2", r"\(QC\) would be \(4 \times BP\), making the total length too big."), ("3", r"\(BP : PQ\) must be \(1 : 2\)."), ("4", "Gets BP : PQ right but QC wrong.")])

P.qa(19, r"The area of the quadrilateral bounded by the \(Y\)-axis, the line \(x = 5\), and the lines \(|x - y| - |x - 5| = 2\), is",
 [], "TITA", "45", ["Geometry::Coordinate_Geometry", "Algebra::Inequalities_and_Absolute_Value"], "Medium",
 r"Between \(x = 0\) and \(x = 5\), \(|x - 5| = 5 - x\).",
 steps(("Remove one modulus", r"\[|x - y| = 7 - x \;\Rightarrow\; y = 7 \;\text{ or }\; y = 2x - 7\]"),
       ("Corners", p(r"At \(x = 0\): \(y = 7\) and \(y = -7\). At \(x = 5\): \(y = 7\) and \(y = 3\).")),
       ("Trapezium", r"\[\tfrac12 (14 + 4) \times 5 = 45\]")) + final(r"\(45\)"),
 shortcut="Parallel sides are the vertical lines x = 0 and x = 5; their lengths 14 and 4 come straight from the two lines.",
 concept=r"\[\text{trapezium area} = \tfrac12 (a + b) h\]")

P.qa(20, r"If \(p^2 + q^2 - 29 = 2pq - 20 = 52 - 2pq\), then the difference between the maximum and minimum possible value of \((p^3 - q^3)\) is",
 M("243", "378", "189", "486"), "MCQ", "2", ["Algebra::Equations_and_Polynomials"], "Medium",
 "The last equality gives pq at once.",
 steps(("pq and p² + q²", r"\[2pq - 20 = 52 - 2pq \Rightarrow pq = 18\]\[p^2 + q^2 = (2pq - 20) + 29 = 45\]"),
       ("p − q", r"\[(p - q)^2 = 45 - 36 = 9 \Rightarrow p - q = \pm 3\]"),
       ("Cube difference", r"\[p^3 - q^3 = (p - q)(p^2 + pq + q^2) = \pm 3 \times 63 = \pm 189\]")) + final(r"\(189 - (-189) = 378\) — option 2"),
 shortcut=r"\(p^2 + pq + q^2 = 63\) is fixed; only the sign of \(p - q\) changes.",
 concept=r"\[a^3 - b^3 = (a - b)(a^2 + ab + b^2)\]",
 why_rows=[("1", r"\(p^3 - q^3\) only takes \(\pm 189\)."), ("3", "That’s the maximum, not the difference."), ("4", r"\(p^3 - q^3\) only takes \(\pm 189\).")])

P.qa(21, r"Let both the series \(a_1, a_2, a_3, \dots\) and \(b_1, b_2, b_3, \dots\) be in arithmetic progression such that the common differences of both the series are prime numbers. If \(a_5 = b_9\), \(a_{19} = b_{19}\) and \(b_2 = 0\), then \(a_{11}\) equals",
 M("86", "84", "79", "83"), "MCQ", "3", ["Algebra::Progressions_and_Series"], "Medium",
 r"Subtract the two equalities: \(a_{19} - a_5\) equals \(b_{19} - b_9\).",
 steps(("Differences", r"\[14d_a = 10d_b \Rightarrow 7d_a = 5d_b \Rightarrow d_a = 5,\ d_b = 7\]"),
       ("Anchor", p(r"\(b_2 = 0\) ⇒ \(b_{19} = 17 \times 7 = 119 = a_{19}\).")),
       ("a₁₁", r"\[a_{11} = a_{19} - 8 \times 5 = 79\]")) + final(r"\(79\) — option 3"),
 shortcut=r"Two primes with \(7d_a = 5d_b\): it must be \(5\) and \(7\).",
 concept=r"\[a_n = a_1 + (n - 1)d \qquad a_m - a_k = (m - k)d\]",
 why_rows=[("1", r"Not a term: \(a_n = 29 + 5(n - 1)\) ends in 4 or 9."), ("2", r"That’s \(a_{12}\)."), ("4", "Not a term of the sequence.")])

P.qa(22, r"Let \(a_n\) and \(b_n\) be two sequences such that \(a_n = 13 + 6(n - 1)\) and \(b_n = 15 + 7(n - 1)\) for all natural numbers \(n\). Then, the largest three digit integer that is common to both these sequences, is",
 [], "TITA", "967", ["Algebra::Progressions_and_Series", "Number_System::Remainders"], "Easy",
 "Common terms form an AP with difference lcm(6, 7) = 42.",
 steps(("Remainders", p(r"\(a_n \equiv 1 \pmod 6\) and \(b_n \equiv 1 \pmod 7\), so common terms are \(\equiv 1 \pmod{42}\): \(43, 85, \dots\)")),
       ("Largest 3-digit", r"\[42k + 1 \le 999 \Rightarrow k = 23 \Rightarrow 967\]")) + final(r"\(967\)"),
 shortcut="Both sequences are “1 more than a multiple”, so look at 1 more than multiples of 42.",
 concept=p(r"Common terms of two APs form an AP whose difference is \(\operatorname{lcm}(d_1, d_2)\)."))

