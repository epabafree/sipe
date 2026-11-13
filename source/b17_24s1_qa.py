# -*- coding: utf-8 -*-
# Batch 17 — CAT 2024 Slot 1: QA Q1–22 (exam order).
from fmt import steps, final, trap, why, table, p
from b17_24s1 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"When \(10^{100}\) is divided by \(7\), the remainder is", M("6", "1", "4", "3"), "MCQ", "3", ["Number_System::Remainders"], "Easy",
 r"\(10\) leaves remainder 3 when divided by 7. Powers of 3 repeat their remainders every 6 steps.",
 steps(("Reduce the base", p(r"\(10 \equiv 3 \pmod 7\), so we need the remainder of \(3^{100}\).")),
       ("The cycle", p(r"\(3^6 = 729 = 7 \times 104 + 1\), so \(3^6\) leaves 1. Since \(100 = 6 \times 16 + 4\), \(3^{100}\) leaves the same remainder as \(3^4 = 81\), which is \(81 - 77 = 4\)."))) + final(r"\(4\), option 3"),
 shortcut=r"By Fermat’s little theorem, \(a^6 \equiv 1 \pmod 7\) for any \(a\) not divisible by 7, so only \(100 \bmod 6 = 4\) matters: \(10^4 = 10000 = 7 \times 1428 + 4\).",
 concept=r"\[a \equiv b \pmod n \;\Rightarrow\; a^k \equiv b^k \pmod n\]",
 why_rows=[("1", r"6 is the remainder of \(10^3\), not \(10^{100}\)."), ("2", r"1 is the remainder only when the power is a multiple of 6."), ("4", r"3 is the remainder of \(10^1\).")])

P.qa(2, "Two places A and B are 45 kms apart and connected by a straight road. Anil goes from A to B while Sunil goes from B to A. Starting at the same time, they cross each other in exactly 1 hour 30 minutes. If Anil reaches B exactly 1 hour 15 minutes after Sunil reaches A, the speed of Anil, in km per hour, is",
 M("14", "12", "16", "18"), "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Their speeds add up to 45 ÷ 1.5. Then test the options against the time gap.",
 steps(("Combined speed", p(r"They close 45 km in 1.5 hours, so \(a + s = 30\) km/h.")),
       ("The time gap", p(r"\(\frac{45}{a} - \frac{45}{s} = 1.25\). Try \(a = 12, s = 18\): \(3.75 - 2.5 = 1.25\). It works."))) + final(r"\(12\) km/h, option 2"),
 shortcut=r"After crossing, Anil covers Sunil’s 1.5 hours of distance and Sunil covers Anil’s. Then \(\frac{1.5s}{a} - \frac{1.5a}{s} = 1.25\); with \(s = 30 - a\), \(a = 12\) fits.",
 concept=r"\[\text{time to meet} = \frac{\text{distance}}{\text{sum of speeds}}\]",
 why_rows=[("1", r"Sunil would be at 16 km/h: \(3.21 - 2.81 \approx 0.4\) h, not 1.25."), ("3", "Then Anil would be the faster one and reach first."), ("4", "Then Anil would be the faster one and reach first.")])

P.qa(3, "There are four numbers such that average of first two numbers is 1 more than the first number, average of first three numbers is 2 more than average of first two numbers, and average of first four numbers is 3 more than average of first three numbers. Then, the difference between the largest and the smallest numbers, is",
 [], "TITA", "15", ["Arithmetic::Average"], "Easy",
 "Call the first number a and write every other number in terms of a.",
 steps(("The second", p(r"\(\frac{a + b}{2} = a + 1\), so \(b = a + 2\).")),
       ("The third", p(r"The first three average \(a + 3\), so they total \(3a + 9\), and \(c = 3a + 9 - (2a + 2) = a + 7\).")),
       ("The fourth", p(r"The first four average \(a + 6\), so they total \(4a + 24\), and \(d = 4a + 24 - (3a + 9) = a + 15\).")),
       ("The difference", p(r"The numbers are \(a, a + 2, a + 7, a + 15\). Largest minus smallest is 15."))) + final(r"\(15\)"),
 shortcut="Take the first number as 0. The numbers become 0, 2, 7 and 15.",
 concept=r"\[\text{new number} = \text{new total} - \text{old total}\]")

P.qa(4, r"The sum of all four-digit numbers that can be formed with the distinct non-zero digits \(a, b, c\), and \(d\), with each digit appearing exactly once in every number, is \(153310 + n\), where \(n\) is a single digit natural number. Then, the value of \((a + b + c + d + n)\) is",
 [], "TITA", "31", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "In the 24 numbers, each digit appears 6 times in each place.",
 steps(("The sum", p(r"Each digit sits in each of the four places \(3! = 6\) times, so the sum is \(6 \times 1111 \times (a + b + c + d) = 6666\,S\).")),
       ("Matching", p(r"\(6666 \times 23 = 153318\), which is \(153310 + 8\). The neighbours \(6666 \times 22\) and \(6666 \times 24\) fall outside 153311 to 153319. So \(S = 23\) and \(n = 8\).")),
       ("Answer", p(r"\(S + n = 23 + 8 = 31\)."))) + final(r"\(31\)"),
 shortcut=r"\(153310 \div 6666 \approx 23\), so try \(S = 23\).",
 concept=p(r"Sum of all numbers formed by arranging \(k\) distinct digits \(= (k-1)! \times 11\ldots1 \times (\text{sum of digits})\), with \(k\) ones in the repunit."))

P.qa(5, "In September, the incomes of Kamal, Amal and Vimal are in the ratio 8 : 6 : 5. They rent a house together, and Kamal pays 15%, Amal pays 12% and Vimal pays 18% of their respective incomes to cover the total house rent in that month. In October, the house rent remains unchanged while their incomes increase by 10%, 12% and 15%, respectively. In October, the percentage of their total income that will be paid as house rent, is nearest to",
 M("13.26", "14.84", "12.75", "15.18"), "MCQ", "1", ["Arithmetic::Percentages"], "Medium",
 "Take the incomes as 800, 600 and 500 and find the rent in rupees.",
 steps(("The rent", p(r"\(0.15 \times 800 + 0.12 \times 600 + 0.18 \times 500\) \(= 120 + 72 + 90 = 282\).")),
       ("October incomes", p(r"\(880 + 672 + 575 = 2127\).")),
       ("Percentage", p(r"\(282 \div 2127 \approx 13.26\%\)."))) + final(r"\(13.26\), option 1"),
 concept=r"\[\text{percentage} = \frac{\text{part}}{\text{whole}} \times 100\]",
 why_rows=[("2", "September’s figure is 282 ÷ 1900 ≈ 14.84%; incomes rose in October."), ("3", "This is too low for a rent of 282 on 2127."), ("4", "This is higher than even September’s share.")])

P.qa(6, "An amount of Rs 10000 is deposited in bank A for a certain number of years at a simple interest of 5% per annum. On maturity, the total amount received is deposited in bank B for another 5 years at a simple interest of 6% per annum. If the interests received from bank A and bank B are in the ratio 10 : 13, then the investment period, in years, in bank A is",
 M("4", "6", "3", "5"), "MCQ", "2", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "Write both interests in terms of t, the years in bank A.",
 steps(("Bank A", p(r"Interest \(= 500t\); the amount moved to B is \(10000 + 500t\).")),
       ("Bank B", p(r"Five years at 6% is 30%: interest \(= 0.3(10000 + 500t) = 3000 + 150t\).")),
       ("The ratio", r"\[\frac{500t}{3000 + 150t} = \frac{10}{13}\]" + r"\[6500t = 30000 + 1500t \;\Rightarrow\; t = 6\]")) + final(r"\(6\) years, option 2"),
 shortcut="Check option 2: interest 3000 in A, then 30% of 13000 = 3900 in B. 3000 : 3900 = 10 : 13.",
 concept=r"\[\text{SI} = \frac{P \times R \times T}{100}\]",
 why_rows=[("1", "2000 against 3600 is 10 : 18."), ("3", "1500 against 3450 is 10 : 23."), ("4", "2500 against 3750 is 10 : 15.")])

P.qa(7, r"If the equations \(x^2 + mx + 9 = 0\), \(x^2 + nx + 17 = 0\) and \(x^2 + (m + n)x + 35 = 0\) have a common negative root, then the value of \((2m + 3n)\) is",
 [], "TITA", "38", ["Algebra::Quadratic_Equations"], "Medium",
 "Add the first two equations at the common root and compare with the third.",
 steps(("Combine", p(r"At the common root \(r\): adding the first two gives \(2r^2 + (m + n)r + 26 = 0\). The third says \(r^2 + (m + n)r + 35 = 0\). Subtracting, \(r^2 - 9 = 0\), so \(r = -3\).")),
       ("m and n", p(r"\(9 - 3m + 9 = 0 \Rightarrow m = 6\). \(9 - 3n + 17 = 0 \Rightarrow n = \frac{26}{3}\).")),
       ("Answer", p(r"\(2m + 3n = 12 + 26 = 38\)."))) + final(r"\(38\)"),
 concept=p("A common root satisfies every equation, so the equations can be added or subtracted at that root."))

P.qa(8, r"If \(x\) is a positive real number such that \(4\log_{10} x + 4\log_{100} x + 8\log_{1000} x = 13\), then the greatest integer not exceeding \(x\), is",
 [], "TITA", "31", ["Algebra::Logarithms_and_Exponents"], "Easy",
 r"Change every log to base 10: \(\log_{100} x = \frac12 \log x\).",
 steps(("One base", r"\[4L + 4 \cdot \tfrac{L}{2} + 8 \cdot \tfrac{L}{3} = 13 \;\Rightarrow\; \tfrac{26}{3}L = 13 \;\Rightarrow\; L = \tfrac32\]" + p(r"where \(L = \log_{10} x\).")),
       ("x", p(r"\(x = 10^{1.5} = 10\sqrt{10} \approx 31.62\). The greatest integer not exceeding it is 31."))) + final(r"\(31\)"),
 concept=r"\[\log_{b^k} x = \frac{1}{k}\log_b x\]")

P.qa(9, r"Let \(x, y\), and \(z\) be real numbers satisfying<br>\(4(x^2 + y^2 + z^2) = a\)<br>\(4(x - y - z) = 3 + a\)<br>Then \(a\) equals",
 M(r"1\tfrac13", "3", "1", "4"), "MCQ", "2", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Subtract the second equation from the first and look for perfect squares.",
 steps(("Subtract", r"\[4x^2 + 4y^2 + 4z^2 - 4x + 4y + 4z = -3\]"),
       ("Complete the squares", r"\[(2x - 1)^2 + (2y + 1)^2 + (2z + 1)^2 = 0\]" + p(r"A sum of squares is zero only if each is zero: \(x = \frac12\), \(y = z = -\frac12\).")),
       ("a", p(r"\(a = 4 \times \frac34 = 3\)."))) + final(r"\(3\), option 2"),
 concept=r"\[p^2 + q^2 + r^2 = 0 \text{ (real numbers)} \;\Rightarrow\; p = q = r = 0\]",
 why_rows=[("1", "This isn’t forced by the equations."), ("3", "With a = 1, the squares would have to add to a negative number."), ("4", "The squares would add to −1, which is impossible.")])

P.qa(10, r"In the XY-plane, the area, in sq. units, of the region defined by the inequalities \(y \ge x + 4\) and \(-4 \le x^2 + y^2 + 4(x - y) \le 0\) is",
 M(r"3\pi", r"2\pi", r"\pi", r"4\pi"), "MCQ", "2", ["Geometry::Coordinate_Geometry"], "Medium",
 "Complete the squares to find the circles, then check where the line passes.",
 steps(("The circles", p(r"\(x^2 + 4x + y^2 - 4y\) \(= (x + 2)^2 + (y - 2)^2 - 8\). So the second condition is \(4 \le (x + 2)^2 + (y - 2)^2 \le 8\): a ring around \((-2, 2)\) between radii 2 and \(2\sqrt2\).")),
       ("The ring’s area", p(r"\(\pi(8 - 4) = 4\pi\).")),
       ("The line", p(r"\(y = x + 4\) passes through \((-2, 2)\), the centre, so it cuts the ring exactly in half. The region above it has area \(2\pi\)."))) + final(r"\(2\pi\), option 2"),
 concept=p(r"The circle \(x^2 + y^2 + 2gx + 2fy + c = 0\) has centre \((-g, -f)\) and radius \(\sqrt{g^2 + f^2 - c}\)."),
 why_rows=[("1", r"Half the ring is \(2\pi\)."), ("3", "The line divides the ring in half, not into quarters."), ("4", r"\(4\pi\) is the whole ring; the line keeps only half.")])

P.qa(11, "A glass is filled with milk. Two-thirds of its content is poured out and replaced with water. If this process of pouring out two-thirds the content and replacing with water is repeated three more times, then the final ratio of milk to water in the glass, is",
 M("1 : 26", "1 : 80", "1 : 27", "1 : 81"), "MCQ", "2", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "Each time, one-third of the milk stays. How many times does this happen in all?",
 steps(p(r"After four rounds, the milk left is \(\left(\frac13\right)^4 = \frac{1}{81}\) of the glass. Water is \(\frac{80}{81}\), so the ratio is \(1 : 80\).")) + trap("“Repeated three more times” means four rounds in all.") + final(r"\(1 : 80\), option 2"),
 concept=r"\[\text{fraction left after } n \text{ replacements} = \left(1 - \frac{\text{removed}}{\text{total}}\right)^n\]",
 why_rows=[("1", "This is the answer after three rounds."), ("3", "1/27 is the milk fraction after three rounds, not a ratio."), ("4", "This compares milk with the whole glass, not with the water.")])

P.qa(12, r"Consider two sets \(A = \{2, 3, 5, 7, 11, 13\}\) and \(B = \{1, 8, 27\}\). Let \(f\) be a function from \(A\) to \(B\) such that for every element \(b\) in \(B\), there is at least one element \(a\) in \(A\) such that \(f(a) = b\). Then, the total number of such functions \(f\) is",
 M("667", "540", "537", "665"), "MCQ", "2", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "Count all functions, then remove those that miss one or more values of B.",
 steps(("All functions", p(r"\(3^6 = 729\).")),
       ("Missing at least one value", p(r"Missing a chosen value: \(2^6 = 64\) each, for 3 values: 192. Missing two values: 1 function each, for 3 pairs: 3, which were taken away twice.")),
       ("Onto functions", r"\[729 - 192 + 3 = 540\]")) + final(r"\(540\), option 2"),
 concept=r"\[\text{onto functions from } n \text{ to } 3 \text{ elements} = 3^n - 3 \cdot 2^n + 3\]",
 why_rows=[("1", "Too many: 192 of the 729 functions miss a value, and only 3 are counted back."), ("3", "This forgets to add back the three constant functions."), ("4", "Too many: the functions that miss a value haven’t all been removed.")])

P.qa(13, "The surface area of a closed rectangular box, which is inscribed in a sphere, is 846 sq cm, and the sum of the lengths of all its edges is 144 cm. The volume, in cubic cm, of the sphere is",
 M(r"1125\pi\sqrt2", r"750\pi\sqrt2", r"1125\pi", r"750\pi"), "MCQ", "1", ["Geometry::Mensuration"], "Medium",
 "The sphere’s diameter is the box’s space diagonal. Find it from the edge sum and the surface area.",
 steps(("The two facts", p(r"\(4(l + b + h) = 144\), so \(l + b + h = 36\). \(2(lb + bh + hl) = 846\).")),
       ("The diagonal", r"\[l^2 + b^2 + h^2 = 36^2 - 846 = 1296 - 846 = 450\]" + p(r"So the diagonal is \(\sqrt{450} = 15\sqrt2\) and the radius is \(\frac{15\sqrt2}{2}\).")),
       ("The volume", r"\[\tfrac43 \pi \left(\tfrac{15\sqrt2}{2}\right)^3 = \tfrac43 \pi \cdot \tfrac{3375 \cdot 2\sqrt2}{8} = 1125\sqrt2\,\pi\]")) + final(r"\(1125\pi\sqrt2\), option 1"),
 concept=r"\[(l + b + h)^2 = l^2 + b^2 + h^2 + 2(lb + bh + hl)\]",
 why_rows=[("2", "This uses a smaller radius than the diagonal gives."), ("3", r"This drops the \(\sqrt2\) from the radius cubed."), ("4", r"This is wrong in both the factor and the \(\sqrt2\).")])

P.qa(14, "The selling price of a product is fixed to ensure 40% profit. If the product had cost 40% less and had been sold for 5 rupees less, then the resulting profit would have been 50%. The original selling price, in rupees, of the product is",
 M("10", "15", "20", "14"), "MCQ", "4", ["Arithmetic::Profit_Loss_and_Discount"], "Easy",
 "Let the cost be c. Write both selling prices in terms of c.",
 steps(p(r"Original selling price \(= 1.4c\). New cost \(0.6c\), new selling price \(1.5 \times 0.6c = 0.9c\). This is 5 less: \(1.4c - 0.9c = 5\), so \(c = 10\) and the selling price is 14.")) + final(r"\(14\), option 4"),
 concept=r"\[\text{SP} = \text{CP} \times (1 + \text{profit\%})\]",
 why_rows=[("1", "10 is the cost price."), ("2", "With a selling price of 15, the cost is about 10.71 and the two prices differ by about 5.36, not 5."), ("3", "With SP 20, the cost would be about 14.3 and the second condition fails.")])

P.qa(15, "A shop wants to sell a certain quantity (in kg) of grains. It sells half the quantity and an additional 3 kg of these grains to the first customer. Then, it sells half of the remaining quantity and an additional 3 kg of these grains to the second customer. Finally, when the shop sells half of the remaining quantity and an additional 3 kg of these grains to the third customer, there are no grains left. The initial quantity, in kg, of grains is",
 M("42", "18", "36", "50"), "MCQ", "1", ["Arithmetic::Miscellaneous"], "Easy",
 "Work backwards. Before each sale, add 3 and double.",
 steps(p(r"Before the third sale: \((0 + 3) \times 2 = 6\). Before the second: \((6 + 3) \times 2 = 18\). Before the first: \((18 + 3) \times 2 = 42\).")) + final(r"\(42\) kg, option 1"),
 concept=r"\[\text{left} = \tfrac{x}{2} - 3 \;\Rightarrow\; x = 2(\text{left} + 3)\]",
 why_rows=[("2", "18 kg is what remained after the first customer."), ("3", "Halving 36 and taking 3 leaves 15, which doesn’t work out."), ("4", "50 leaves 22, then 8, then 1 kg, not zero.")])

P.qa(16, r"If \((a + b\sqrt n)\) is the positive square root of \((29 - 12\sqrt5)\), where \(a\) and \(b\) are integers, and \(n\) is a natural number, then the maximum possible value of \((a + b + n)\) is",
 M("4", "18", "6", "22"), "MCQ", "2", ["Algebra::Surds_and_Indices"], "Medium",
 r"Find the square root first. Then remember that \(2\sqrt5\) can also be written as \(\sqrt{20}\).",
 steps(("The square root", p(r"\((2\sqrt5 - 3)^2 = 20 + 9 - 12\sqrt5\). Since \(2\sqrt5 \approx 4.47 > 3\), the positive root is \(-3 + 2\sqrt5\).")),
       ("Ways to write it", p(r"\(a = -3\) and \(b\sqrt n = 2\sqrt5\). With \(b = 2, n = 5\): sum 4. With \(b = 1, n = 20\): sum \(-3 + 1 + 20 = 18\). No other whole-number pair works.")),
       ("Maximum", p("18."))) + trap(r"\(3 - 2\sqrt5\) also squares to \(29 - 12\sqrt5\), but it is negative.") + final(r"\(18\), option 2"),
 concept=r"\[\sqrt{x - 2\sqrt{y}} = \sqrt{p} - \sqrt{q} \text{ when } p + q = x,\ pq = y,\ p > q\]",
 why_rows=[("1", r"This is \(b = 2, n = 5\); writing \(2\sqrt5\) as \(\sqrt{20}\) gives more."), ("3", r"This takes \(a = 3\), whose root is negative."), ("4", r"This would need \(a = 3\), which gives the negative root.")])

P.qa(17, "ABCD is a rectangle with sides AB = 56 cm and BC = 45 cm, and E is the midpoint of side CD. Then, the length, in cm, of radius of incircle of △ADE is",
 [], "TITA", "10", ["Geometry::Triangles"], "Easy",
 "Triangle ADE has a right angle at D. Find the hypotenuse.",
 steps(("The sides", p(r"AD = 45, DE = 28 (half of 56), and \(AE = \sqrt{45^2 + 28^2} = \sqrt{2809} = 53\).")),
       ("Inradius", p(r"For a right triangle, \(r = \frac{45 + 28 - 53}{2} = 10\)."))) + final(r"\(10\) cm"),
 concept=r"\[\text{right triangle: } r = \frac{\text{leg}_1 + \text{leg}_2 - \text{hypotenuse}}{2}\]")

P.qa(18, "A fruit seller has a total of 187 fruits consisting of apples, mangoes and oranges. The number of apples and mangoes are in the ratio 5 : 2. After she sells 75 apples, 26 mangoes and half of the oranges, the ratio of number of unsold apples to number of unsold oranges becomes 3 : 2. The total number of unsold fruits is",
 [], "TITA", "66", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Let the apples be 5k and the mangoes 2k. The oranges are what is left of 187.",
 steps(("Set up", p(r"Oranges \(= 187 - 7k\). After the sales: apples \(5k - 75\), oranges \(\frac{187 - 7k}{2}\).")),
       ("The ratio", r"\[\frac{5k - 75}{(187 - 7k)/2} = \frac32\]" + r"\[20k - 300 = 561 - 21k \;\Rightarrow\; k = 21\]"),
       ("Unsold", p(r"Apples \(105 - 75 = 30\), mangoes \(42 - 26 = 16\), oranges \(40 \div 2 = 20\). Total 66."))) + final(r"\(66\)"),
 concept=r"\[a : b = m : n \;\Rightarrow\; a = mk,\ b = nk\]")

P.qa(19, r"The sum of all real values of \(k\) for which \(\left(\frac18\right)^k \times \left(\frac{1}{32768}\right)^{\frac13} = \frac18 \times \left(\frac{1}{32768}\right)^{\frac1k}\), is",
 M(r"-\tfrac43", r"-\tfrac23", r"\tfrac43", r"\tfrac23"), "MCQ", "2", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"\(32768 = 2^{15} = 8^5\). Write everything as a power of 8.",
 steps(("One base", r"\[8^{-k} \cdot 8^{-5/3} = 8^{-1} \cdot 8^{-5/k}\]"),
       ("Equate exponents", r"\[k + \tfrac53 = 1 + \tfrac5k \;\Rightarrow\; 3k^2 + 2k - 15 = 0\]"),
       ("Sum of roots", p(r"The discriminant \(4 + 180\) is positive, so both roots are real and non-zero. Their sum is \(-\frac23\)."))) + final(r"\(-\tfrac23\), option 2"),
 concept=r"\[ax^2 + bx + c = 0 \;\Rightarrow\; \text{sum of roots} = -\tfrac{b}{a}\]",
 why_rows=[("1", "This doubles the sum."), ("3", "Wrong sign and doubled."), ("4", "Wrong sign.")])

P.qa(20, r"Suppose \(x_1, x_2, x_3, \ldots, x_{100}\) are in arithmetic progression such that \(x_5 = -4\) and \(2x_6 + 2x_9 = x_{11} + x_{13}\). Then, \(x_{100}\) equals",
 M("204", "-194", "206", "-196"), "MCQ", "2", ["Algebra::Progressions_and_Series"], "Easy",
 "Write each term as a + (n − 1)d.",
 steps(("The condition", r"\[2(a + 5d) + 2(a + 8d)\]" + r"\[= (a + 10d) + (a + 12d)\]" + p(r"So \(4a + 26d = 2a + 22d\), which gives \(a = -2d\).")),
       ("Using x₅", p(r"\(a + 4d = 2d = -4\), so \(d = -2\) and \(a = 4\).")),
       ("x₁₀₀", p(r"\(4 + 99 \times (-2) = -194\)."))) + final(r"\(-194\), option 2"),
 concept=r"\[x_n = a + (n - 1)d\]",
 why_rows=[("1", "Wrong sign: the terms are falling."), ("3", "Wrong sign, and one step off."), ("4", r"This uses \(100d\) instead of \(99d\).")])

P.qa(21, "Renu would take 15 days working 4 hours per day to complete a certain task whereas Seema would take 8 days working 5 hours per day to complete the same task. They decide to work together to complete this task. Seema agrees to work for double the number of hours per day as Renu, while Renu agrees to work for double the number of days as Seema. If Renu works 2 hours per day, then the number of days Seema will work, is",
 [], "TITA", "6", ["Arithmetic::Time_and_Work"], "Medium",
 "Turn both into hourly rates: Renu needs 60 hours, Seema 40.",
 steps(("Rates", p(r"Renu does \(\frac{1}{60}\) of the task per hour, Seema \(\frac{1}{40}\).")),
       ("The plan", p(r"Seema works \(d\) days at 4 hours; Renu works \(2d\) days at 2 hours.")),
       ("Solve", r"\[\frac{4d}{60} + \frac{4d}{40} = 1 \;\Rightarrow\; \frac{d}{15} + \frac{d}{10} = \frac{d}{6} = 1 \;\Rightarrow\; d = 6\]")) + final(r"\(6\)"),
 concept=r"\[\text{work} = \text{rate} \times \text{hours}\]")

P.qa(22, r"For any natural number \(n\), let \(a_n\) be the largest integer not exceeding \(\sqrt n\). Then the value of \(a_1 + a_2 + \cdots + a_{50}\) is",
 [], "TITA", "217", ["Algebra::Progressions_and_Series"], "Medium",
 r"\(a_n = k\) for \(n\) from \(k^2\) up to \((k+1)^2 - 1\): that is \(2k + 1\) values of \(n\).",
 steps(("Blocks", table(["Value", "n (count)", "Sum"], [["1", "1–3 (3)", "3"], ["2", "4–8 (5)", "10"], ["3", "9–15 (7)", "21"], ["4", "16–24 (9)", "36"], ["5", "25–35 (11)", "55"], ["6", "36–48 (13)", "78"], ["7", "49–50 (2)", "14"]])),
       ("Total", p(r"\(3 + 10 + 21 + 36 + 55 + 78 + 14\) \(= 217\)."))) + final(r"\(217\)"),
 concept=r"\[\lfloor \sqrt n \rfloor = k \text{ for } k^2 \le n < (k+1)^2\]")
