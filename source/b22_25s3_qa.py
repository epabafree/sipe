# -*- coding: utf-8 -*-
# Batch 22 — CAT 2025 Slot 3: QA Q1–22 (exam order).
from fmt import steps, final, trap, why, table, p
from b22_25s3 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"If \(\left(x^2 + \frac{1}{x^2}\right) = 25\) and \(x > 0\), then the value of \(\left(x^7 + \frac{1}{x^7}\right)\) is",
 M(r"44850\sqrt3", r"44853\sqrt3", r"44859\sqrt3", r"44856\sqrt3"), "MCQ", "2", ["Algebra::Equations_and_Polynomials"], "Hard",
 r"Let \(t = x + \frac1x\). Then build up the powers step by step.",
 steps(("t", p(r"\(t^2 = 25 + 2 = 27\), so \(t = 3\sqrt3\).")),
       ("Cubes", p(r"\(x^3 + \frac{1}{x^3} = t^3 - 3t\) \(= 81\sqrt3 - 9\sqrt3 = 72\sqrt3\).")),
       ("Fourth powers", p(r"\(x^4 + \frac{1}{x^4} = 25^2 - 2 = 623\).")),
       ("Seventh powers", p(r"Multiplying the cube and fourth-power sums gives the seventh-power sum plus \(x + \frac1x\). So \(x^7 + \frac{1}{x^7}\) \(= 72\sqrt3 \times 623 - 3\sqrt3\) \(= 44853\sqrt3\)."))) + final("Option 2"),
 concept=p(r"With \(s_n = x^n + x^{-n}\): \(s_a s_b = s_{a+b} + s_{a-b}\)."),
 why_rows=[("1", r"This subtracts \(6\sqrt3\) instead of \(3\sqrt3\)."), ("3", r"This adds \(3\sqrt3\) instead of subtracting."), ("4", r"This forgets to subtract \(x + \frac1x\).")])

P.qa(2, r"For real values of \(x\), the range of the function \(f(x) = \frac{2x - 3}{2x^2 + 4x - 6}\) is",
 M(r"\left(-\infty, \tfrac18\right] \cup [1, \infty)", r"\left(-\infty, \tfrac14\right] \cup [1, \infty)", r"\left(-\infty, \tfrac14\right] \cup \left[\tfrac12, \infty\right)", r"\left(-\infty, \tfrac18\right] \cup \left[\tfrac12, \infty\right)"), "MCQ", "4", ["Algebra::Functions"], "Hard",
 "Set y = f(x) and ask when the resulting quadratic in x has a real solution.",
 steps(("A quadratic in x", r"\[2yx^2 + (4y - 2)x + (3 - 6y) = 0\]"),
       ("Real roots", p(r"Discriminant: \((4y - 2)^2 - 8y(3 - 6y)\) \(= 64y^2 - 40y + 4 \ge 0\), i.e. \(16y^2 - 10y + 1 \ge 0\), so \((8y - 1)(2y - 1) \ge 0\).")),
       ("Range", p(r"\(y \le \frac18\) or \(y \ge \frac12\). (y = 0 comes from x = 1.5, and the boundary values come from x = 3 and x = 0, all allowed.)"))) + final("Option 4"),
 concept=p("To find the range of a rational function, solve y = f(x) for x and require real solutions."),
 why_rows=[("1", "The gap ends at 1/2, not 1."), ("2", "Both ends of the gap are wrong."), ("3", "The gap starts at 1/8.")])

P.qa(3, "For a 4-digit number (greater than 1000), sum of the digits in the thousands, hundreds, and tens places is 15. Sum of the digits in the hundreds, tens, and units places is 16. Also, the digit in the tens place is 6 more than the digit in the units place. The difference between the largest and smallest possible value of the number is",
 M("811", "4078", "735", "3289"), "MCQ", "1", ["Number_System::Miscellaneous"], "Medium",
 "Subtract the two sums: the units digit is one more than the thousands digit.",
 steps(("Relations", p(r"With digits \(a, b, c, d\): \(d = a + 1\), \(c = d + 6 = a + 7\), and \(b = 15 - a - c = 8 - 2a\).")),
       ("Possibilities", p(r"\(c \le 9\) gives \(a \le 2\). \(a = 1\): 1682. \(a = 2\): 2493.")),
       ("Difference", p(r"\(2493 - 1682 = 811\)."))) + final(r"\(811\), option 1"),
 concept=r"\[\text{express every digit in terms of one}\]",
 why_rows=[("2", "Only two numbers are possible, 1682 and 2493."), ("3", "This doesn’t match 2493 − 1682."), ("4", "This doesn’t match 2493 − 1682.")])

P.qa(4, "Teams A, B, and C consist of five, eight, and ten members, respectively, such that every member within a team is equally productive. Working separately, teams A, B, and C can complete a certain job in 40 hours, 50 hours, and 4 hours, respectively. Two members from team A, three members from team B, and one member from team C together start the job, and the member from team C leaves after 23 hours. The number of additional member(s) from team B, that would be required to replace the member from team C, to finish the job in the next one hour, is",
 M("2", "4", "1", "3"), "MCQ", "1", ["Arithmetic::Time_and_Work"], "Medium",
 "Use 400 units of work: an A member does 2 an hour, a B member 1, a C member 10.",
 steps(("Rates", p(r"Team A: 400 ÷ 40 = 10 an hour, 2 per member. Team B: 8 an hour, 1 per member. Team C: 100 an hour, 10 per member.")),
       ("23 hours", p(r"\(2 \times 2 + 3 \times 1 + 10 = 17\) an hour, so \(17 \times 23 = 391\). 9 units are left.")),
       ("The last hour", p(r"Without C, the group does 7 an hour, so 2 more B members are needed."))) + final(r"\(2\), option 1"),
 concept=r"\[\text{take total work as a common multiple of the times}\]",
 why_rows=[("2", "4 extra would finish in well under an hour."), ("3", "One extra gives only 8 of the 9 units."), ("4", "Two are enough.")])

P.qa(5, "The average salary of 5 managers and 25 engineers in a company is 60000 rupees. If each of the managers received 20% salary increase while the salary of the engineers remained unchanged, the average salary of all 30 employees would have increased by 5%. The average salary, in rupees, of the engineers is",
 M("50000", "45000", "40000", "54000"), "MCQ", "4", ["Arithmetic::Average"], "Easy",
 "The managers’ raise is 5% of the whole payroll.",
 steps(p(r"Total payroll 1,800,000. 5% of it is 90,000, which is 20% of the managers’ total, so managers earn 450,000. Engineers: \(1350000 \div 25 = 54000\).")) + final(r"\(54000\), option 4"),
 concept=r"\[\text{total} = \text{average} \times \text{count}\]",
 why_rows=[("1", "This doesn’t use the 5% condition."), ("2", "This is the managers’ total divided by 10."), ("3", "Too low for the given payroll.")])

P.qa(6, "The monthly sales of a product from January to April were 120, 135, 150 and 165 units, respectively. The cost price of the product was Rs. 240 per unit, and a fixed marked price was used for the product in all the four months. Discounts of 20%, 10% and 5% were given on the marked price per unit in January, February and March, respectively, while no discounts were given in April. If the total profit from January to April was Rs. 138825, then the marked price per unit, in rupees, was",
 M("525", "515", "520", "510"), "MCQ", "1", ["Arithmetic::Profit_Loss_and_Discount"], "Medium",
 "Revenue = M × (effective units), cost = 240 × 570.",
 steps(p(r"Each month’s revenue is M times the units times (1 − discount). Effective units: \(96 + 121.5 + 142.5 + 165 = 525\). Cost \(240 \times 570 = 136800\). So \(525M = 275625\) and \(M = 525\).")) + final(r"\(525\), option 1"),
 concept=r"\[\text{profit} = \text{revenue} - \text{cost}\]",
 why_rows=[("2", "Profit would be 133575."), ("3", "Profit would be 136200."), ("4", "Profit would be 130950.")])

P.qa(7, "In a class of 150 students, 75 students chose physics, 111 students chose mathematics and 40 students chose chemistry. All students chose at least one of the three subjects and at least one student chose all three subjects. The number of students who chose both physics and chemistry is equal to the number of students who chose both chemistry and mathematics, and this is half the number of students who chose both physics and mathematics. The maximum possible number of students who chose physics but not mathematics, is",
 M("35", "30", "40", "55"), "MCQ", "1", ["Modern_Maths::Set_Theory"], "Hard",
 r"Let \(|P \cap C| = |M \cap C| = u\), \(|P \cap M| = 2u\) and the triple overlap be t.",
 steps(("Inclusion–exclusion", p(r"\(150 = 226 - 4u + t\), so \(4u = 76 + t\).")),
       ("Physics but not maths", p(r"\(75 - |P \cap M| = 75 - 2u\). To maximise it, make u as small as possible.")),
       ("Smallest u", p(r"t is at least 1 and \(76 + t\) must be divisible by 4, so t = 4 and u = 20. Check: chemistry only \(40 - 40 + 4 = 4\), physics only 19, maths only 55, all non-negative. The answer is \(75 - 40 = 35\)."))) + final(r"\(35\), option 1"),
 concept=r"\[|A \cup B \cup C| = \sum|A| - \sum|A \cap B| + |A \cap B \cap C|\]",
 why_rows=[("2", "This uses u = 22.5, not a whole number."), ("3", "This needs u = 17.5."), ("4", "55 is the number who chose only maths.")])

P.qa(8, r"If \(f(x) = (x^2 + 3x)(x^2 + 3x + 2)\), then the sum of all real roots of the equation \(\sqrt{f(x) + 1} = 9701\), is",
 M("-3", "3", "6", "-6"), "MCQ", "1", ["Algebra::Quadratic_Equations"], "Medium",
 r"With \(y = x^2 + 3x\), \(f + 1 = (y + 1)^2\).",
 steps(("Simplify", p(r"\(\sqrt{(y + 1)^2} = |y + 1| = 9701\), so \(y = 9700\) or \(y = -9702\).")),
       ("Real roots", p(r"\(x^2 + 3x = 9700\) has two real roots adding to −3. \(x^2 + 3x = -9702\) has a negative discriminant, so no real roots."))) + final(r"\(-3\), option 1"),
 concept=r"\[y(y + 2) + 1 = (y + 1)^2\]",
 why_rows=[("2", "Wrong sign."), ("3", "Wrong sign and doubled."), ("4", "Counts −3 twice, but the second quadratic has no real roots.")])

P.qa(9, "Rahul starts on his journey at 5 pm at a constant speed so that he reaches his destination at 11 pm the same day. However, on his way, he stops for 20 minutes, and after that, increases his speed by 3 km per hour to reach on time. If he had stopped for 10 minutes more, he would have had to increase his speed by 5 km per hour to reach on time. His initial speed, in km per hour, was",
 M("12", "20", "18", "15"), "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Let the remaining time after the stop point be T at speed v. The remaining distance is vT either way.",
 steps(("Two equations", p(r"\(vT = (v + 3)(T - \frac13)\) and \(vT = (v + 5)(T - \frac12)\).")),
       ("Solve", p(r"The first gives \(3T = \frac{v + 3}{3}\), so \(T = \frac{v + 3}{9}\). The second gives \(5T = \frac{v + 5}{2}\), so \(T = \frac{v + 5}{10}\). Equating: \(10v + 30 = 9v + 45\), so \(v = 15\)."))) + final(r"\(15\) km/h, option 4"),
 concept=r"\[\text{same distance: } v_1 t_1 = v_2 t_2\]",
 why_rows=[("1", r"Gives T = 5/3 from one equation and 1.7 from the other."), ("2", "The two equations disagree."), ("3", "The two equations disagree.")])

P.qa(10, "Ankita walks from A to C through B, and runs back through the same route at a speed that is 40% more than her walking speed. She takes exactly 3 hours 30 minutes to walk from B to C as well as to run from B to A. The total time, in minutes, she would take to walk from A to B and run from B to C, is",
 [], "TITA", "444", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Running is 1.4 times as fast, so running takes 1/1.4 of the walking time.",
 steps(p(r"Running B→A takes 210 minutes, so walking A→B takes \(210 \times 1.4 = 294\). Walking B→C takes 210, so running it takes \(210 \div 1.4 = 150\). Total \(294 + 150 = 444\).")) + final(r"\(444\)"),
 concept=r"\[\text{time} \propto \frac{1}{\text{speed}}\]")

P.qa(11, r"The sum of all the digits of the number \((10^{50} + 10^{25} - 123)\), is",
 M("324", "255", "212", "221"), "MCQ", "4", ["Number_System::Miscellaneous"], "Medium",
 r"Work out \(10^{25} - 123\) first.",
 steps(p(r"\(10^{25} - 123\) is 22 nines followed by 877: digit sum \(22 \times 9 + 8 + 7 + 7 = 220\). Adding \(10^{50}\) puts a 1 far to the left without overlapping. Total \(221\).")) + final(r"\(221\), option 4"),
 concept=r"\[10^n - k \text{ for small } k: \text{ a run of 9s followed by } 10^m - k\]",
 why_rows=[("1", "This counts too many nines."), ("2", "This counts too many nines."), ("3", "This drops some nines.")])

P.qa(12, "A triangle ABC is formed with AB = AC = 50 cm and BC = 80 cm. Then, the sum of the lengths, in cm, of all three altitudes of the triangle ABC is",
 [], "TITA", "126", ["Geometry::Triangles"], "Easy",
 "The altitude to BC is easy; use the area for the other two.",
 steps(p(r"Altitude to BC: \(\sqrt{50^2 - 40^2} = 30\), area \(= \frac12 \times 80 \times 30 = 1200\). Altitudes to AB and AC: \(\frac{2 \times 1200}{50} = 48\) each. Sum \(30 + 48 + 48 = 126\).")) + final(r"\(126\)"),
 concept=r"\[\text{altitude} = \frac{2 \times \text{area}}{\text{base}}\]")

P.qa(13, "Vessels A and B contain 60 litres of alcohol and 60 litres of water, respectively. A certain volume is taken out from A and poured into B. After stirring, the same volume is taken out from B and poured into A. If the resultant ratio of alcohol and water in A is 15 : 4, then the volume, in litres, initially taken out from A is",
 [], "TITA", "16", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "After the swap, A holds 60 litres again; 4/19 of it is water.",
 steps(p(r"The water in A is the water brought back: \(v \times \frac{60}{60 + v}\). It must be \(\frac{4}{19} \times 60\). So \(\frac{60v}{60 + v} = \frac{240}{19}\), giving \(1140v = 240(60 + v)\) and \(v = 16\).")) + final(r"\(16\)"),
 concept=r"\[\text{a stirred mixture keeps its proportions when part is removed}\]")

P.qa(14, "In an arithmetic progression, if the sum of fourth, seventh and tenth terms is 99, and the sum of the first fourteen terms is 497, then the sum of first five terms is",
 [], "TITA", "65", ["Algebra::Progressions_and_Series"], "Easy",
 "The three terms average to the seventh term.",
 steps(p(r"\(3(a + 6d) = 99\), so \(a + 6d = 33\). \(7(2a + 13d) = 497\), so \(2a + 13d = 71\). Then \(d = 5\), \(a = 3\), and \(S_5 = \frac52(6 + 20) = 65\).")) + final(r"\(65\)"),
 concept=r"\[S_n = \frac n2\left(2a + (n - 1)d\right)\]")

P.qa(15, "Let p, q and r be three natural numbers such that their sum is 900, and r is a perfect square whose value lies between 150 and 500. If p is not less than 0.3q and not more than 0.7q, then the sum of the maximum and minimum possible values of p is",
 [], "TITA", "397", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "p is largest when r is smallest and p = 0.7q; smallest when r is largest and p = 0.3q.",
 steps(("Maximum", p(r"r = 169: \(p + q = 731\). \(p \le 0.7q\) gives \(1.7p \le 0.7 \times 731\), so \(p \le 301\) (with q = 430).")),
       ("Minimum", p(r"r = 484: \(p + q = 416\). \(p \ge 0.3q\) gives \(1.3p \ge 0.3 \times 416\), so \(p \ge 96\) (with q = 320).")),
       ("Sum", p(r"\(301 + 96 = 397\)."))) + final(r"\(397\)"),
 concept=r"\[p \le kq,\; p + q = S \;\Rightarrow\; p \le \frac{kS}{1 + k}\]")

P.qa(16, "The ratio of the number of coins in boxes A and B was 17:7. After 108 coins were shifted from box A to box B, this ratio became 37:20. The number of coins that needs to be shifted further from A to B, to make this ratio 1:1, is",
 [], "TITA", "272", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Let the boxes have 17k and 7k coins.",
 steps(p(r"\(20(17k - 108) = 37(7k + 108)\) gives \(81k = 6156\), so \(k = 76\). Now A has \(1292 - 108 = 1184\) and B \(532 + 108 = 640\). Equal shares are 912 each, so 272 more must move.")) + final(r"\(272\)"),
 concept=r"\[\text{the total stays the same when coins move between boxes}\]")

P.qa(17, "The rate of water flow through three pipes A, B and C are in the ratio 4 : 9 : 36. An empty tank can be filled up completely by pipe A in 15 hours. If all the three pipes are used simultaneously to fill up this empty tank, the time, in minutes, required to fill up the entire tank completely is nearest to",
 M("71", "78", "73", "76"), "MCQ", "3", ["Arithmetic::Time_and_Work"], "Easy",
 "The three together flow at 49/4 of A’s rate.",
 steps(p(r"\(15 \times \frac{4}{49}\) hours \(= \frac{3600}{49} \approx 73.5\) minutes, nearest to 73.")) + final(r"\(73\), option 3"),
 concept=r"\[\text{time} \propto \frac{1}{\text{rate}}\]",
 why_rows=[("1", "Too short."), ("2", "Too long."), ("4", "Too long.")])

P.qa(18, "ABCD is a trapezium in which AB is parallel to DC, AD is perpendicular to AB, and AB = 3DC. If a circle inscribed in the trapezium touching all the sides has a radius of 3 cm, then the area, in sq. cm, of the trapezium is",
 M(r"30\sqrt3", "54", "48", r"36\sqrt2"), "MCQ", "3", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 "The height is the diameter, 6. A circle fits only if the sums of opposite sides are equal.",
 steps(("Set up", p(r"Let DC = x, AB = 3x, AD = 6. BC has horizontal run 2x and height 6, so \(BC = \sqrt{4x^2 + 36}\).")),
       ("Tangential condition", p(r"\(AB + DC = AD + BC\): \(4x = 6 + \sqrt{4x^2 + 36}\). Squaring \((4x - 6)^2 = 4x^2 + 36\) gives \(12x^2 = 48x\), so \(x = 4\).")),
       ("Area", p(r"\(\frac{12 + 4}{2} \times 6 = 48\)."))) + final(r"\(48\), option 3"),
 concept=r"\[\text{a quadrilateral has an incircle} \iff AB + CD = AD + BC\]",
 why_rows=[("1", "The area comes out as a whole number."), ("2", "This uses parallel sides adding to 18."), ("4", "The area comes out as a whole number.")])

P.qa(19, r"In \(\triangle ABC\), AB = AC = 12 cm and D is a point on side BC such that AD = 8 cm. If AD is extended to a point E such that \(\angle ACB = \angle AEB\), then the length, in cm, of AE is",
 M("16", "18", "20", "14"), "MCQ", "2", ["Geometry::Triangles"], "Medium",
 r"\(\angle ABC = \angle ACB = \angle AEB\). Look for similar triangles sharing angle A.",
 steps(p(r"Triangles ABD and AEB share angle A, and \(\angle ABD = \angle AEB\). So they are similar: \(\frac{AB}{AE} = \frac{AD}{AB}\), giving \(AE = \frac{144}{8} = 18\).")) + final(r"\(18\), option 2"),
 concept=r"\[AB^2 = AD \cdot AE\]",
 why_rows=[("1", "This doubles AD."), ("3", "This doesn’t match AB²/AD."), ("4", "This doesn’t match AB²/AD.")])

P.qa(20, r"If \(12^{12x} \times 4^{24x + 12} \times 5^{2y}\) \(= 8^{4z} \times 20^{12x} \times 243^{3x - 6}\), where \(x, y\) and \(z\) are natural numbers, then \(x + y + z\) equals",
 [], "TITA", "112", ["Algebra::Surds_and_Indices"], "Medium",
 "Write both sides as powers of 2, 3 and 5, and match exponents.",
 steps(("Prime powers", p(r"Left: \(2^{24x} 3^{12x} \cdot 2^{48x + 24} \cdot 5^{2y}\). Right: \(2^{12z} \cdot 2^{24x} 5^{12x} \cdot 3^{15x - 30}\).")),
       ("Match", p(r"3: \(12x = 15x - 30\), so x = 10. 5: \(2y = 12x\), so y = 60. 2: \(72x + 24 = 12z + 24x\), so \(z = 4x + 2 = 42\).")),
       ("Sum", p(r"\(10 + 60 + 42 = 112\)."))) + final(r"\(112\)"),
 concept=r"\[\text{equal numbers have equal prime-power exponents}\]")

P.qa(21, "In a school with 1500 students, each student chooses any one of the streams out of science, arts, and commerce, by paying a fee of Rs 1100, Rs 1000, and Rs 800, respectively. The total fee paid by all the students is Rs 15,50,000. If the number of science students is not more than the number of arts students, then the maximum possible number of science students in the school is",
 [], "TITA", "700", ["Algebra::Linear_Equations"], "Medium",
 "Subtract 800 per student from the total.",
 steps(p(r"Subtracting 800 for every student leaves 350000: \(300s + 200a = 350000\), so \(3s + 2a = 3500\). With \(s \le a\): \(5s \le 3500\), so \(s \le 700\). s = 700 gives a = 700 and c = 100, which works.")) + final(r"\(700\)"),
 concept=r"\[\text{subtract the smallest fee to simplify}\]")

P.qa(22, r"The sum of all possible real values of \(x\) for which \(\log_{x-3}(x^2 - 9) = \log_{x-3}(x + 1) + 2\), is",
 M("-3", r"\sqrt{33}", r"\tfrac{3 + \sqrt{33}}{2}", "3"), "MCQ", "3", ["Algebra::Logarithms_and_Exponents"], "Hard",
 r"Write 2 as \(\log_{x-3}(x - 3)^2\) and watch the base: it must be positive and not 1.",
 steps(("Equation", p(r"\(x^2 - 9 = (x + 1)(x - 3)^2\). Dividing by \(x - 3\): \(x + 3 = (x + 1)(x - 3)\), so \(x^2 - 3x - 6 = 0\) and \(x = \frac{3 \pm \sqrt{33}}{2}\).")),
       ("Valid values", p(r"The base \(x - 3\) must be positive, so \(x > 3\). Only \(\frac{3 + \sqrt{33}}{2} \approx 4.37\) qualifies (and it isn’t 4, where the base would be 1)."))) + final("Option 3"),
 concept=r"\[\log_b \text{ needs } b > 0,\ b \ne 1, \text{ and a positive argument}\]",
 why_rows=[("1", "Negative values make the base negative."), ("2", r"\(\sqrt{33}\) isn’t a root."), ("4", "3 is the sum of both roots, but one of them is invalid.")])
