# -*- coding: utf-8 -*-
# Batch 5 — CAT 2022 Slot 1: QA Q1–22 (exam order; see the README note on numbering).
from fmt import steps, final, why, table, p
from b5_22s1 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, "Pinky is standing in a queue at a ticket counter. Suppose the ratio of the number of persons standing ahead of Pinky to the number of persons standing behind her in the queue is 3 : 5. If the total number of persons in the queue is less than 300, then the maximum possible number of persons standing ahead of Pinky is",
 [], "TITA", "111", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Call the people ahead 3k and the people behind 5k. Don’t forget to count Pinky herself.",
 steps(("Setting it up", p(r"With \(3k\) people ahead and \(5k\) behind, the queue has \(3k + 5k + 1 = 8k + 1\) people, Pinky included.")),
       ("Using the limit", r"\[8k + 1 < 300 \;\Rightarrow\; k \le 37\]" + p(r"The largest choice is \(k = 37\), which puts \(3 \times 37 = 111\) people ahead of her."))) + final(r"\(111\)"),
 shortcut=r"The total must be one more than a multiple of 8. The largest such number below 300 is 297, which gives \(k = 37\).",
 concept=r"\[\text{parts in ratio } a : b \;\Rightarrow\; ak,\ bk \text{ for some whole number } k\]")

P.qa(2, r"Let \(a, b, c\) be non-zero real numbers such that \(b^2 < 4ac\), and \(f(x) = ax^2 + bx + c\). If the set \(S\) consists of all integers \(m\) such that \(f(m) < 0\), then the set \(S\) must necessarily be",
 ["either the empty set or the set of all integers", "the set of all integers", "the set of all positive integers", "the empty set"], "MCQ", "1", ["Algebra::Quadratic_Equations"], "Easy",
 r"What does \(b^2 < 4ac\) tell you about where the graph of \(f\) crosses the x-axis?",
 steps(("No real roots", p(r"\(b^2 - 4ac < 0\) means the parabola never touches the x-axis, so \(f(x)\) keeps the same sign for every real \(x\).")),
       ("Which sign?", p(r"If \(a > 0\), the parabola opens upwards and \(f(x) > 0\) everywhere, so no integer makes it negative: \(S\) is empty. If \(a < 0\), \(f(x) < 0\) everywhere, so \(S\) is every integer. We aren’t told the sign of \(a\), so both are possible."))) +
 final("Option 1"),
 shortcut=r"Try \(f(x) = x^2 + 1\) (never negative) and \(f(x) = -x^2 - 1\) (always negative). Both satisfy the condition, so the answer must allow both outcomes.",
 concept=r"\[b^2 - 4ac < 0 \;\Rightarrow\; f(x) \text{ has the sign of } a \text{ for every real } x\]",
 why_rows=[("2", r"This happens only when \(a < 0\); with \(a > 0\) the set is empty."), ("3", "The sign of f is the same for every integer, so the set can’t be just the positive ones."), ("4", r"This happens only when \(a > 0\).")])

P.qa(3, r"The average of three integers is \(13\). When a natural number \(n\) is included, the average of these four integers remains an odd integer. The minimum possible value of \(n\) is",
 M("5", "1", "3", "4"), "MCQ", "1", ["Arithmetic::Average"], "Easy",
 "The three integers add up to 39. What must the new total of four numbers look like?",
 steps(("The new total", p(r"The four numbers add up to \(39 + n\). Their average is an odd integer, so \(39 + n = 4 \times \text{odd}\), that is 4, 12, 20, 28, 36, 44, …")),
       ("The smallest n", p(r"\(n\) is a natural number, so \(39 + n \ge 40\). The first value in the list that is at least 40 is 44, which gives \(n = 5\)."))) + final(r"\(5\), option 1"),
 shortcut="Try the options from the smallest: 1, 3 and 4 give totals of 40, 42 and 43, whose averages are 10, 10.5 and 10.75. Only 5 gives 11.",
 concept=r"\[\text{average} = \frac{\text{total}}{\text{count}}\]",
 why_rows=[("2", "The total would be 40, and an average of 10 is even."), ("3", "The total would be 42, giving an average of 10.5."), ("4", "The total would be 43, giving an average of 10.75.")])

P.qa(4, r"Let \(A\) be the largest positive integer that divides all the numbers of the form \(3^k + 4^k + 5^k\), and \(B\) be the largest positive integer that divides all the numbers of the form \(4^k + 3(4^k) + 4^{k+2}\), where \(k\) is any positive integer. Then \((A + B)\) equals",
 [], "TITA", "82", ["Number_System::Factors_and_Divisibility"], "Medium",
 r"For \(A\), try a few small values of \(k\) and look for what they share. For \(B\), take \(4^k\) out as a common factor.",
 steps(("Finding A", p(r"\(k = 1\) gives 12, \(k = 2\) gives 50, \(k = 3\) gives 216. The only common factor of 12 and 50 is 2, and every term is even (odd + even + odd), so \(A = 2\).")),
       ("Finding B", r"\[4^k + 3 \cdot 4^k + 16 \cdot 4^k = 20 \cdot 4^k\]" + p(r"The smallest of these numbers, at \(k = 1\), is 80, and every later one is a multiple of 80. So \(B = 80\).")),
       ("Adding", p(r"\(A + B = 2 + 80 = 82\)."))) + final(r"\(82\)"),
 shortcut="The largest number dividing every term of a list can’t be larger than the gcd of its first two terms, so a couple of small cases usually settle it.",
 concept=r"\[\text{largest common divisor of a family} = \gcd(\text{its members})\]")

P.qa(5, r"In a village, the ratio of number of males to females is \(5 : 4\). The ratio of number of literate males to literate females is \(2 : 3\). The ratio of the number of illiterate males to illiterate females is \(4 : 3\). If \(3600\) males in the village are literate, then the total number of females in the village is",
 [], "TITA", "43200", ["Arithmetic::Ratio_and_Proportion"], "Medium",
 r"Literate females follow from the 2 : 3 ratio. Then write males as \(5x\) and females as \(4x\).",
 steps(("Literate people", p(r"Literate males are 3600, so literate females are \(3600 \times \tfrac32 = 5400\).")),
       ("Illiterate people", p(r"With \(5x\) males and \(4x\) females, the illiterate groups are \(5x - 3600\) and \(4x - 5400\).") +
         r"\[\begin{aligned} \frac{5x - 3600}{4x - 5400} &= \frac43 \\ 15x - 10800 &= 16x - 21600 \\ x &= 10800 \end{aligned}\]"),
       ("Females", p(r"\(4x = 43200\)."))) + final(r"\(43200\)"),
 shortcut="Check: males 54,000, of whom 50,400 are illiterate; females 43,200, of whom 37,800 are illiterate. 50,400 : 37,800 is indeed 4 : 3.",
 concept=r"\[\text{split each group into parts, then use the given ratio on each part}\]")

P.qa(6, r"Let \(ABCD\) be a parallelogram such that the coordinates of its three vertices \(A, B, C\) are \((1, 1)\), \((3, 4)\) and \((-2, 8)\), respectively. Then, the coordinates of the vertex \(D\) are",
 M("(-4, 5)", "(-3, 4)", "(0, 11)", "(4, 5)"), "MCQ", "1", ["Geometry::Coordinate_Geometry"], "Easy",
 "In a parallelogram the diagonals bisect each other, so AC and BD share a midpoint.",
 steps(("Same midpoint", r"\[A + C = B + D \;\Rightarrow\; D = A + C - B\]"),
       ("Computing", r"\[D = (1 - 2 - 3,\; 1 + 8 - 4) = (-4,\, 5)\]")) + final(r"\((-4, 5)\), option 1"),
 shortcut=r"Moving from B to A is a step of \((-2, -3)\). Take the same step from C: \((-2 - 2, 8 - 3) = (-4, 5)\).",
 concept=r"\[\text{parallelogram } ABCD: \; A + C = B + D\]",
 why_rows=[("2", "BD would then have a different midpoint from AC, so the diagonals wouldn’t bisect each other."), ("3", "This point makes ABDC a parallelogram, with the vertices in a different order."), ("4", "BD would not share its midpoint with AC.")])

P.qa(7, r"Alex invested his savings in two parts. The simple interest earned on the first part at \(15\%\) per annum for \(4\) years is the same as the simple interest earned on the second part at \(12\%\) per annum for \(3\) years. Then, the percentage of his savings invested in the first part is",
 [r"\(60\%\)", r"\(62.5\%\)", r"\(37.5\%\)", r"\(40\%\)"], "MCQ", "3", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Simple interest is principal × rate × time. Set the two interests equal.",
 steps(("Equal interest", r"\[\begin{aligned} &x \times 0.15 \times 4 = y \times 0.12 \times 3 \\ \Rightarrow\ &0.6x = 0.36y \\ \Rightarrow\ &x : y = 3 : 5 \end{aligned}\]"),
       ("As a percentage", p(r"The first part is \(\tfrac{3}{8}\) of the savings, which is \(37.5\%\)."))) + final(r"\(37.5\%\), option 3"),
 shortcut="The first part earns at 60% over its term and the second at 36%. To earn the same, the amounts must be in the inverse ratio, 36 : 60 = 3 : 5.",
 concept=r"\[SI = \frac{P \times R \times T}{100}\]",
 why_rows=[("1", "With 60% in the first part, it would earn far more interest than the second."), ("2", "That is the second part’s share, 5/8."), ("4", "With 40% in the first part, the two interests still aren’t equal.")])

P.qa(8, r"The average weight of students in a class increases by \(600\) gm when some new students join the class. If the average weight of the new students is \(3\) kg more than the average weight of the original students, then the ratio of the number of original students to the number of new students is",
 M("1 : 2", "4 : 1", "1 : 4", "3 : 1"), "MCQ", "2", ["Arithmetic::Average"], "Easy",
 "Each new student is 3 kg above the old average. That extra weight is spread over everyone, raising the average by 0.6 kg.",
 steps(("Spreading the extra weight", p(r"With \(n\) original and \(m\) new students, the new students bring \(3m\) kg above the old average. Shared among all \(n + m\) students, this raises the average by 0.6 kg.") +
         r"\[\begin{aligned} &\frac{3m}{n + m} = 0.6 \\ \Rightarrow\ &3m = 0.6n + 0.6m \\ \Rightarrow\ &2.4m = 0.6n \\ \Rightarrow\ &n : m = 4 : 1 \end{aligned}\]")) + final(r"\(4 : 1\), option 2"),
 shortcut="Alligation: the new average sits 0.6 above the old and 2.4 below the newcomers, so the numbers are in the ratio 2.4 : 0.6 = 4 : 1.",
 concept=r"\[\text{change in average} = \frac{\text{extra weight}}{\text{new total count}}\]",
 why_rows=[("1", "One old student to two new would raise the average by 2 kg."), ("3", "One old to four new would raise it by 2.4 kg."), ("4", "Three old to one new would raise it by 0.75 kg.")])

P.qa(9, r"A mixture contains lemon juice and sugar syrup in equal proportion. If a new mixture is created by adding this mixture and sugar syrup in the ratio \(1 : 3\), then the ratio of lemon juice and sugar syrup in the new mixture is",
 M("1 : 7", "1 : 6", "1 : 5", "1 : 4"), "MCQ", "1", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Take 1 litre of the mixture and add 3 litres of syrup.",
 steps(("Counting", p("One litre of the mixture has half a litre of each. Adding 3 litres of syrup gives 0.5 litres of lemon juice and 3.5 litres of syrup."))) + final(r"\(1 : 7\), option 1"),
 shortcut="Use 2 litres of mixture and 6 of syrup to avoid fractions: 1 litre lemon to 7 litres syrup.",
 concept=r"\[\text{track each ingredient separately, then compare}\]",
 why_rows=[("2", "This forgets the half litre of syrup already in the mixture."), ("3", "There are 0.5 litres of lemon juice to 3.5 of syrup, which is 1 : 7."), ("4", "There are 0.5 litres of lemon juice to 3.5 of syrup, which is 1 : 7.")])

P.qa(10, r"Amal buys \(110\) kg of syrup and \(120\) kg of juice, syrup being \(20\%\) less costly than juice, per kg. He sells \(10\) kg of syrup at \(10\%\) profit and \(20\) kg of juice at \(20\%\) profit. Mixing the remaining juice and syrup, Amal sells the mixture at ₹ \(308.32\) per kg and makes an overall profit of \(64\%\). Then, Amal’s cost price for the syrup, in rupees per kg, is",
 [], "TITA", "160", ["Arithmetic::Profit_Loss_and_Discount", "Arithmetic::Mixture_and_Alligation"], "Medium",
 r"Let juice cost \(j\) per kg, so syrup costs \(0.8j\). Write total revenue in two ways.",
 steps(("Total cost", p(r"\(110 \times 0.8j + 120j = 208j\).")),
       ("Total revenue", p(r"10 kg of syrup at \(1.1 \times 0.8j\), 20 kg of juice at \(1.2j\), and the remaining 200 kg at ₹ 308.32:") +
         r"\[8.8j + 24j + 200 \times 308.32 = 32.8j + 61664\]"),
       ("64% profit", r"\[\begin{aligned} 32.8j + 61664 &= 1.64 \times 208j = 341.12j \\ 308.32j &= 61664 \\ j &= 200 \end{aligned}\]" + p(r"So syrup costs \(0.8 \times 200 = 160\) per kg."))) + final(r"₹ \(160\)"),
 shortcut="Notice that 308.32 appears on both sides once you simplify: 341.12j − 32.8j = 308.32j, so j = 61664 ÷ 308.32 = 200.",
 concept=r"\[\text{revenue} = (1 + \text{profit \%}) \times \text{cost}\]")

P.qa(11, r"A trapezium \(ABCD\) has side \(AD\) parallel to \(BC\), \(\angle BAD = 90^\circ\), \(BC = 3\) cm and \(AD = 8\) cm. If the perimeter of this trapezium is \(36\) cm, then its area, in sq cm, is",
 [], "TITA", "66", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "AB is perpendicular to both parallel sides, so it is the height. Drop a perpendicular from C to AD to find CD.",
 steps(("The slanted side", p(r"Let the height \(AB = h\). Dropping a perpendicular from C to AD leaves a right triangle with legs \(h\) and \(8 - 3 = 5\), so \(CD = \sqrt{h^2 + 25}\).")),
       ("Using the perimeter", r"\[\begin{aligned} 3 + 8 + h + \sqrt{h^2 + 25} &= 36 \\ \sqrt{h^2 + 25} &= 25 - h \\ h^2 + 25 &= 625 - 50h + h^2 \\ h &= 12 \end{aligned}\]"),
       ("The area", r"\[\tfrac12 (3 + 8) \times 12 = 66\]")) + final(r"\(66\)"),
 shortcut="With h = 12 the slanted side is 13: the familiar 5, 12, 13 triangle. That is a good check.",
 concept=r"\[\text{trapezium area} = \tfrac12 (a + b) h\]")

P.qa(12, r"The largest real value of \(a\) for which the equation \(|x + a| + |x - 1| = 2\) has an infinite number of solutions of \(x\) is",
 M("2", "-1", "0", "1"), "MCQ", "4", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 r"\(|x + a| + |x - 1|\) is the sum of distances from \(x\) to \(-a\) and to \(1\). When is that sum the same for a whole stretch of x?",
 steps(("Thinking in distances", p(r"The sum of distances from \(x\) to two points is smallest, and constant, for every \(x\) between them. That constant value is the distance between the points, \(|1 + a|\).")),
       ("Infinitely many solutions", p(r"The equation holds for a whole interval exactly when \(|1 + a| = 2\), so \(a = 1\) or \(a = -3\). The larger value is 1."))) + final(r"\(1\), option 4"),
 shortcut=r"Test \(a = 1\): \(|x + 1| + |x - 1| = 2\) for every \(x\) between \(-1\) and \(1\). Then check that \(a = 2\) gives a minimum of 3, which is too big.",
 concept=r"\[|x - p| + |x - q| \ge |p - q|, \text{ with equality for all } x \text{ between } p \text{ and } q\]",
 why_rows=[("1", r"With \(a = 2\) the smallest value of the left side is 3, so there are no solutions."), ("2", r"With \(a = -1\) the two points coincide and there are just two solutions."), ("3", "With a = 0 the minimum is 1, and the equation has only two solutions.")])

P.qa(13, r"Let \(a\) and \(b\) be natural numbers. If \(a^2 + ab + a = 14\) and \(b^2 + ab + b = 28\), then \((2a + b)\) equals",
 M("8", "9", "7", "10"), "MCQ", "1", ["Algebra::Equations_and_Polynomials"], "Easy",
 "Add the two equations and look for a perfect square.",
 steps(("Adding", r"\[\begin{aligned} &a^2 + 2ab + b^2 + a + b = 42 \\ \Rightarrow\ &(a + b)^2 + (a + b) = 42 \\ \Rightarrow\ &a + b = 6 \end{aligned}\]"),
       ("Factorising each one", p(r"\(a^2 + ab + a = a(a + b + 1) = 7a = 14\), so \(a = 2\), and then \(b = 4\).")),
       ("The answer", p(r"\(2a + b = 4 + 4 = 8\)."))) + final(r"\(8\), option 1"),
 shortcut=r"Each equation factorises: \(a(a + b + 1) = 14\) and \(b(a + b + 1) = 28\), so \(b = 2a\). Then \(a(3a + 1) = 14\) gives \(a = 2\).",
 concept=r"\[a^2 + 2ab + b^2 = (a + b)^2\]",
 why_rows=[("2", r"The equations fix \(a = 2\) and \(b = 4\), so \(2a + b\) can only be 8."), ("3", r"The equations fix \(a = 2\) and \(b = 4\), so \(2a + b\) can only be 8."), ("4", r"That is \(a + 2b\), not \(2a + b\).")])

P.qa(14, r"For any natural number \(n\), suppose the sum of the first \(n\) terms of an arithmetic progression is \((n + 2n^2)\). If the \(n^{\text{th}}\) term of the progression is divisible by \(9\), then the smallest possible value of \(n\) is",
 M("8", "7", "4", "9"), "MCQ", "2", ["Algebra::Progressions_and_Series"], "Easy",
 r"The \(n\)th term is the sum of the first \(n\) terms minus the sum of the first \(n - 1\).",
 steps(("The general term", r"\[\begin{aligned} a_n &= S_n - S_{n-1} \\ &= (n + 2n^2) - \big((n - 1) + 2(n - 1)^2\big) \\ &= 4n - 1 \end{aligned}\]"),
       ("Divisible by 9", p(r"Try small \(n\): 3, 7, 11, 15, 19, 23, 27, … The first multiple of 9 is 27, at \(n = 7\)."))) + final(r"\(7\), option 2"),
 shortcut=r"\(4n - 1 \equiv 0 \pmod 9\) means \(4n \equiv 1\). Since \(4 \times 7 = 28 = 27 + 1\), \(n = 7\).",
 concept=r"\[a_n = S_n - S_{n-1}\]",
 why_rows=[("1", r"\(a_8 = 31\), not a multiple of 9."), ("3", r"\(a_4 = 15\), not a multiple of 9."), ("4", r"\(a_9 = 35\), not a multiple of 9.")])

P.qa(15, r"In a class of \(100\) students, \(73\) like coffee, \(80\) like tea and \(52\) like lemonade. It may be possible that some students do not like any of these three drinks. Then, the difference between the maximum and minimum possible number of students who like all the three drinks is",
 M("48", "52", "53", "47"), "MCQ", "4", ["Modern_Maths::Set_Theory"], "Hard",
 "Find the largest and the smallest possible overlap separately. For the smallest, try to spread the likes so that as few students as possible like all three.",
 steps(("The largest overlap", p("No more than 52 students can like all three, because only 52 like lemonade. And it can happen: at least 53 like both coffee and tea, and the 52 lemonade lovers can all be among them.")),
       ("The smallest overlap", p(r"There are \(73 + 80 + 52 = 205\) likes in all, shared among at most 100 students. If \(x_1, x_2, x_3\) students like exactly one, two and three drinks:") +
         r"\[x_1 + 2x_2 + 3x_3 = 205, \qquad x_1 + x_2 + x_3 \le 100\]" +
         p(r"Subtracting twice the second from the first gives \(x_3 - x_1 \ge 5\), so \(x_3 \ge 5\). Five is possible with \(x_1 = 0\), \(x_2 = 95\), \(x_3 = 5\).")),
       ("The difference", p(r"\(52 - 5 = 47\)."))) + final(r"\(47\), option 4"),
 shortcut="For the minimum, imagine every student liking at least two drinks: 100 students then account for 200 likes, and the 5 extra likes must come from students who like all three.",
 concept=r"\[\text{total likes} = x_1 + 2x_2 + 3x_3\]",
 why_rows=[("1", "This uses 4 as the minimum instead of 5."), ("2", "That is only the maximum."), ("3", "The largest possible overlap is 52 and the smallest is 5, so the gap can’t be 53.")])

P.qa(16, r"Trains A and B start travelling at the same time towards each other with constant speeds from stations X and Y, respectively. Train A reaches station Y in \(10\) minutes while train B takes \(9\) minutes to reach station X after meeting train A. Then, the total time taken, in minutes, by train B to travel from station Y to station X is",
 M("12", "6", "15", "10"), "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 r"Let them meet after \(t\) minutes. After meeting, B covers what A covered before meeting.",
 steps(("Setting up", p(r"A covers the whole distance \(D\) in 10 minutes, so its speed is \(\tfrac{D}{10}\). In \(t\) minutes A covers \(\tfrac{Dt}{10}\), and B covers that same stretch in 9 minutes after meeting, so B’s speed is \(\tfrac{Dt}{90}\).")),
       ("Meeting", p(r"Before meeting, B covers the rest of the distance:") + r"\[\begin{aligned} &\frac{Dt}{90} \cdot t = D - \frac{Dt}{10} \\ \Rightarrow\ &t^2 + 9t - 90 = 0 \\ \Rightarrow\ &t = 6 \end{aligned}\]"),
       ("B’s total time", p(r"\(6 + 9 = 15\) minutes."))) + final(r"\(15\), option 3"),
 shortcut="Check the answer: B takes 15 minutes and A takes 10, so their speeds are in the ratio 2 : 3. They meet after 6 minutes, when A has gone 3/5 of the way, and B needs 9 more minutes for that 3/5.",
 concept=r"\[\text{same distance} \Rightarrow \text{time} \propto \frac{1}{\text{speed}}\]",
 why_rows=[("1", "This doesn’t satisfy the 9 minutes after meeting."), ("2", "That is the meeting time, not B’s whole journey."), ("4", "That is A’s time.")])

P.qa(17, r"Ankita buys \(4\) kg cashews, \(14\) kg peanuts and \(6\) kg almonds when the cost of \(7\) kg cashews is the same as that of \(30\) kg peanuts or \(9\) kg almonds. She mixes all the three nuts and marks a price for the mixture in order to make a profit of ₹ \(1752\). She sells \(4\) kg of the mixture at this marked price and the remaining at a \(20\%\) discount on the marked price, thus making a total profit of ₹ \(744\). Then, the amount, in rupees, that she had spent in buying almonds is",
 M("2520", "1176", "1680", "1440"), "MCQ", "3", ["Arithmetic::Profit_Loss_and_Discount"], "Medium",
 "Start with the two profit figures. Selling 20 kg at a discount instead of full price cost her the difference.",
 steps(("The marked price", p(r"With marked price \(M\) per kg, full-price sales of all 24 kg would earn 1752 profit. Selling 20 kg at 20% off lost \(20 \times 0.2M = 4M\), and the profit fell to 744.") +
         r"\[4M = 1752 - 744 = 1008 \;\Rightarrow\; M = 252\]"),
       ("Total cost", p(r"\(24 \times 252 - 1752 = 4296\).")),
       ("Splitting the cost", p(r"Let \(7c = 30p = 9a = 630k\), so cashews cost \(90k\), peanuts \(21k\) and almonds \(70k\) per kg. Then the total cost is") + r"\[4(90k) + 14(21k) + 6(70k) = 1074k = 4296\]" + p(r"so \(k = 4\), and almonds cost \(6 \times 70 \times 4 = 1680\)."))) +
 final(r"₹ \(1680\), option 3"),
 shortcut="Almonds make up 420 of every 1074 rupees spent. 4296 × 420/1074 = 1680.",
 concept=r"\[\text{profit} = \text{revenue} - \text{cost}\]",
 why_rows=[("1", "That would be the cost of 9 kg of almonds, not 6."), ("2", "That is what she spent on peanuts."), ("4", "That is what she spent on cashews.")])

P.qa(18, r"For natural numbers \(x\), \(y\), and \(z\), if \(xy + yz = 19\) and \(yz + xz = 51\), then the minimum possible value of \(xyz\) is",
 [], "TITA", "34", ["Number_System::Factors_and_Divisibility", "Algebra::Equations_and_Polynomials"], "Medium",
 "Factorise both equations. 19 is prime, which narrows things down a lot.",
 steps(("The first equation", p(r"\(y(x + z) = 19\). Since 19 is prime and \(x + z \ge 2\), \(y = 1\) and \(x + z = 19\).")),
       ("The second equation", p(r"\(z(x + y) = z(x + 1) = 51 = 3 \times 17\). With \(x + z = 19\), the pairs that work are \(z = 3, x = 16\) and \(z = 17, x = 2\).")),
       ("The products", p(r"\(16 \times 1 \times 3 = 48\) and \(2 \times 1 \times 17 = 34\). The smaller is 34."))) + final(r"\(34\)"),
 shortcut="Once y = 1, just list the factor pairs of 51 and keep the ones where x + z = 19.",
 concept=r"\[\text{prime product } pq \Rightarrow \text{one factor is } 1\]")

P.qa(19, r"All the vertices of a rectangle lie on a circle of radius \(R\). If the perimeter of the rectangle is \(P\), then the area of the rectangle is",
 M(r"\dfrac{P^2}{16} - R^2", r"\dfrac{P^2}{8} - 2R^2", r"\dfrac{P^2}{2} - 2PR", r"\dfrac{P^2}{8} - \dfrac{R^2}{2}"), "MCQ", "2", ["Geometry::Circles", "Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "The diagonal of the rectangle is a diameter of the circle.",
 steps(("Two facts", r"\[a + b = \frac{P}{2} \qquad a^2 + b^2 = (2R)^2 = 4R^2\]"),
       ("The area", r"\[ab = \frac{(a + b)^2 - (a^2 + b^2)}{2} = \frac{P^2/4 - 4R^2}{2} = \frac{P^2}{8} - 2R^2\]")) + final("Option 2"),
 shortcut=r"Test a square of side \(\sqrt2\) in a circle of radius 1: \(P = 4\sqrt2\), area 2. Option 2 gives \(32/8 - 2 = 2\).",
 concept=r"\[2ab = (a + b)^2 - (a^2 + b^2)\]",
 why_rows=[("1", "For the test square this gives 1, not 2."), ("3", "For the test square this gives about 4.7."), ("4", "For the test square this gives 3.5.")])

P.qa(20, r"For any real number \(x\), let \([x]\) be the largest integer less than or equal to \(x\). If \(\displaystyle\sum_{n=1}^{N} \left[\frac15 + \frac{n}{25}\right] = 25\), then \(N\) is",
 [], "TITA", "44", ["Algebra::Functions"], "Medium",
 r"Work out when \(\tfrac15 + \tfrac{n}{25}\) first reaches 1, and when it reaches 2.",
 steps(("Where the terms change", p(r"\(\tfrac15 + \tfrac{n}{25} = \tfrac{5 + n}{25}\). This is below 1 for \(n \le 19\), so those terms are 0. It is from 1 up to just below 2 for \(n = 20\) to \(44\), so those terms are 1.")),
       ("Adding up", p(r"From \(n = 20\) onwards each term adds 1. To reach 25 we need 25 such terms, that is \(n = 20\) to \(n = 44\)."))) + final(r"\(44\)"),
 shortcut="Write the term as [(n + 5)/25]. It is 0 until n + 5 reaches 25, then 1 until n + 5 reaches 50.",
 concept=r"\[[x] = k \iff k \le x < k + 1\]")

P.qa(21, r"<p>Let \(0 \le a \le x \le 100\) and</p>\[f(x) = |x - a| + |x - 100| + |x - a - 50|.\]<p>Then, the maximum value of \(f(x)\) becomes \(100\) when \(a\) is equal to</p>",
 M("0", "25", "100", "50"), "MCQ", "4", ["Algebra::Inequalities_and_Absolute_Value"], "Hard",
 r"A sum of absolute values is largest at one of the ends of the allowed range, here \(x = a\) or \(x = 100\).",
 steps(("At the two ends", p(r"At \(x = a\): \(0 + (100 - a) + 50 = 150 - a\). At \(x = 100\): \((100 - a) + 0 + |50 - a|\), which is \(150 - 2a\) when \(a \le 50\) and 50 when \(a \ge 50\).")),
       ("Setting the maximum to 100", p(r"The larger of these is \(150 - a\). It equals 100 when \(a = 50\), and then the value at \(x = 100\) is 50, which is smaller, so the maximum really is 100."))) + final(r"\(50\), option 4"),
 shortcut="Try the options: a = 50 gives values 100 and 50 at the two ends, so the maximum is 100.",
 concept=p(r"A sum of terms like \(|x - c|\) bends upwards, so on an interval its largest value is always at one of the ends."),
 why_rows=[("1", "With a = 0 the maximum is 150."), ("2", "With a = 25 the maximum is 125."), ("3", r"With \(a = 100\), \(x\) must be 100 and \(f = 50\).")])

P.qa(22, r"The number of ways of distributing \(20\) identical balloons among \(4\) children such that each child gets some balloons but no child gets an odd number of balloons is",
 [], "TITA", "84", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 r"Every child gets an even number, at least 2. Write each child’s share as \(2y\).",
 steps(("Halving", p(r"If child \(i\) gets \(2y_i\) balloons with \(y_i \ge 1\), then \(y_1 + y_2 + y_3 + y_4 = 10\).")),
       ("Counting", p(r"The number of ways to write 10 as a sum of four positive whole numbers is \(\binom{9}{3} = 84\)."))) + final(r"\(84\)"),
 shortcut="Think of giving the balloons out in pairs: 10 identical pairs among 4 children, each getting at least one pair.",
 concept=r"\[\#\{y_1 + \dots + y_k = n,\ y_i \ge 1\} = \binom{n - 1}{k - 1}\]")
