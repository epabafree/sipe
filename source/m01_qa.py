# -*- coding: utf-8 -*-
# Simp Mock 1: QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m01 import P

def fig(src, alt): return f'<p class="fig"><img src="{src}" alt="{alt}"></p>'

P.qa(1, r"Let ABCDEF be a regular hexagon with each side of length 1 cm. Then the value of \(\dfrac{BE}{BC}\) is:",
 [r"\(2\sqrt{3}\)", r"\(3\sqrt{2}\)", "2", "3"], "MCQ", "3", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 "BE joins opposite vertices. Into what shapes do the long diagonals cut a regular hexagon?",
 steps(("Six equilateral triangles", p("The three long diagonals of a regular hexagon meet at its centre O and cut it into six equilateral triangles, each with side equal to the hexagon’s side.")),
       ("BE", p(r"BE passes through O, so \(BE = BO + OE = 1 + 1 = 2\) cm, while \(BC = 1\) cm. The ratio is 2."))) + final("2, option 3"),
 concept=r"\[\text{Regular hexagon, side } a:\]\[\text{long diagonal} = 2a\]\[\text{short diagonal} = \sqrt{3}\,a\]",
 why_rows=[("1", r"\(2\sqrt3\) is no length here; the short diagonal is \(\sqrt3\)."), ("2", "Not a hexagon length."), ("4", "Would need BE to be three sides long.")])

P.qa(2, r"If \(x = (216)^{4+2\sqrt5}\), then which of the following equals 36?",
 [r"\(\dfrac{x^{\sqrt5}}{x^{2}}\)", r"\(\sqrt{\dfrac{x^{\sqrt5}}{x^{2}}}\)", r"\(\sqrt[3]{\dfrac{x^{\sqrt5}}{x^{2}}}\)", r"\(\sqrt[3]{\dfrac{x^{2}}{x^{\sqrt5}}}\)"],
 "MCQ", "3", ["Algebra::Surds_and_Indices"], "Hard",
 r"Write everything as a power of 6. Every option contains \(x^{\sqrt5 - 2}\) in some form.",
 steps(("Base 6", p(r"\(216 = 6^3\), so \(x = 6^{3(4+2\sqrt5)} = 6^{12+6\sqrt5}\).")),
       (r"\(x^{\sqrt5-2}\)", p(r"Exponent: \((12+6\sqrt5)(\sqrt5-2)\) \(= 12\sqrt5 - 24 + 30 - 12\sqrt5\) \(= 6\). So \(\dfrac{x^{\sqrt5}}{x^{2}} = 6^6\).")),
       ("Getting 36", p(r"\(36 = 6^2 = (6^6)^{1/3}\): the cube root of option 1’s expression."))) + final("Option 3"),
 shortcut=r"\((\sqrt5+2)(\sqrt5-2) = 1\), so \(6^{6(2+\sqrt5)}\) raised to \(\sqrt5-2\) is \(6^6\).",
 concept=r"\[(a+\sqrt b)(a-\sqrt b) = a^2 - b\]",
 why_rows=[("1", r"Equals \(6^6\)."), ("2", r"Equals \(6^3 = 216\)."), ("4", r"Equals \(6^{-2} = \tfrac{1}{36}\).")])

P.qa(3, "In a locality, over a period of 5 years, the total income of the households increased by 35% and the per capita income increased by 25% during the same time. The percentage by which the population of the locality increased during the same period is ____.",
 ["12", "10", "8", "6"], "MCQ", "3", ["Arithmetic::Percentages"], "Easy",
 "Per capita income = total income ÷ population.",
 steps(("Set up", p(r"Population factor \(= \dfrac{\text{total factor}}{\text{per-capita factor}} = \dfrac{1.35}{1.25} = 1.08\).")),
       ("Answer", p("An 8% increase."))) + final("8%, option 3"),
 concept=r"\[\text{Total} = \text{per capita} \times \text{population}\]",
 why_rows=[("1", "35 − 25 = 10, plus a guess; percentages don’t subtract."), ("2", "35 − 25: growth factors divide, they don’t subtract."), ("4", "Not the ratio of factors.")])

P.qa(4, "Time taken by 7 men and 8 robots to complete a job working together is 70% less than the same job done by 3 men and 2 robots. If 6 robots finish a job in 4 days, then the number of days required by a group of three men to finish the same job is ____.",
 [], "TITA", "18", ["Arithmetic::Time_and_Work"], "Medium",
 "70% less time means the bigger team works \\(\\tfrac{10}{3}\\) times as fast.",
 steps(("Rates", p(r"Let a man do \(m\) and a robot \(r\) per day. Time is 30% of the other, so the rate is \(\tfrac{1}{0.3}\) times: \(0.3(7m + 8r) = 3m + 2r\), i.e. \(2.1m + 2.4r = 3m + 2r\), so \(0.4r = 0.9m\), \(r = \tfrac{9}{4}m\).")),
       ("The job", p(r"6 robots × 4 days = \(24r = 54m\) man-days.")),
       ("Three men", p(r"\(54 \div 3 = 18\) days."))) + trap("70% less time is not 70% more speed: time × 0.3 means rate ÷ 0.3.") + final("18"),
 concept=r"\[\text{Work} = \text{rate} \times \text{time}\]")

P.qa(5, "A salesman’s annual target is to sell 100 water purifiers. In the first two quarters of the year, he could sell only 5 water purifiers per month. In the third quarter, his monthly sales average increased by 20% in comparison to the first two quarters’ monthly sales average. How many water purifiers will he have to sell in the last quarter of the year if his annual target has been reduced by 10%?",
 ["14", "28", "42", "52"], "MCQ", "3", ["Arithmetic::Percentages"], "Easy",
 "Count what has been sold in nine months, then compare with the new target.",
 steps(("Sold so far", p("First six months: \\(6 \\times 5 = 30\\). Third quarter: 6 a month for 3 months = 18. Total 48.")),
       ("Target", p("Reduced target: 90. Still to sell: \\(90 - 48 = 42\\)."))) + final("42, option 3"),
 why_rows=[("1", "Not what’s left."), ("2", "Uses only one quarter’s sales."), ("4", "Uses the original target of 100.")])

P.qa(6, "There are 100 MCQ questions to be answered in an examination. Correct answer fetches you 2 marks but the wrong answer penalises you by deducting 1 mark. One mark is awarded for each unattempted question. What is the highest total marks that can be achieved by two students, each with a different number of correct answers?",
 [], "TITA", "197", ["Algebra::Linear_Equations"], "Medium",
 "Find the highest score that can be reached in two different ways (different numbers of correct answers).",
 steps(("Score formula", p(r"With \(c\) correct, \(w\) wrong and \(100 - c - w\) unattempted: score \(= 2c - w + (100 - c - w)\) \(= 100 + c - 2w\).")),
       ("Go down from the top", table(["Score", "Ways (c, w)"], [["200", "(100, 0)"], ["199", "(99, 0)"], ["198", "(98, 0)"], ["197", "(97, 0) and (99, 1)"]], hi={(3, 1)}) +
          p("Each extra wrong answer must be paid for with two more correct ones, and \\(c + w \\le 100\\). 197 is the first score with two ways."))) + final("197"),
 concept=r"\[\text{score} = 100 + c - 2w\]\[c + w \le 100\]")

P.qa(7, r"Let \(a\) and \(b\) be two real numbers. If 2 and −2 are roots of \(ax^3 + bx^2 - 7x + 8 = 0\), then \(b\) equals",
 ["2", r"\(\dfrac{7}{4}\)", r"\(\dfrac{\sqrt7}{2}\)", "−2"], "MCQ", "4", ["Algebra::Equations_and_Polynomials"], "Medium",
 "Substitute both roots and add the two equations: the \\(a\\) terms cancel.",
 steps(("Substitute", p(r"\(x = 2\): \(8a + 4b - 14 + 8 = 0\). \(x = -2\): \(-8a + 4b + 14 + 8 = 0\).")),
       ("Add", p(r"\(8b + 16 = 0\), so \(b = -2\). (Then \(a = \tfrac{7}{4}\).)"))) + final("−2, option 4"),
 why_rows=[("1", "Sign slip."), ("2", r"That is \(a\), not \(b\)."), ("3", "Doesn’t come out of the equations.")])

P.qa(8, r"The perimeter of a rectangle is larger than that of an equilateral triangle by 88 cm. The numerical value of the area of the rectangle in sq. cm is equal to the square of the numerical value of the area of the equilateral triangle expressed in the same unit. The length of the rectangle is \(33\tfrac{1}{3}\)% more than the breadth of the rectangle. The length of the diagonal of the rectangle, in cm, is ____.",
 ["40", "45", "50", "55"], "MCQ", "1", ["Geometry::Triangles"], "Hard",
 "Length : breadth = 4 : 3, so call them \\(4k\\) and \\(3k\\). The diagonal is \\(5k\\).",
 steps(("Areas", p(r"Rectangle: \(12k^2\). Triangle of side \(a\): \(\tfrac{\sqrt3}{4}a^2\), squared \(\tfrac{3}{16}a^4\). So \(\tfrac{3}{16}a^4 = 12k^2\), \(a^4 = 64k^2\), \(a^2 = 8k\).")),
       ("Perimeters", p(r"\(14k = 3a + 88\). With \(k = \tfrac{a^2}{8}\): \(7a^2 = 12a + 352\), so \((a - 8)(7a + 44) = 0\) and \(a = 8\), \(k = 8\).")),
       ("Diagonal", p(r"\(5k = 40\) cm."))) + final("40, option 1"),
 concept=r"\[\text{Equilateral triangle: area} = \tfrac{\sqrt3}{4}a^2\]",
 why_rows=[("2", "Not a multiple of 5k with k = 8."), ("3", "Would need k = 10."), ("4", "Would need k = 11.")])

P.qa(9, r"Find the sum of \(5 \times 9 + 9 \times 13\) \(+\, 13 \times 17 + \dots + 97 \times 101\).",
 ["85720", "87520", "82570", "85270"], "MCQ", "1", ["Algebra::Progressions_and_Series"], "Medium",
 "Each term is \\((4n+1)(4n+5)\\). How many terms are there?",
 steps(("General term", p(r"\(T_n = (4n+1)(4n+5)\) \(= 16n^2 + 24n + 5\), for \(n = 1\) to \(24\) (since \(4 \times 24 + 1 = 97\)).")),
       ("Sum", p(r"\(16 \cdot \tfrac{24 \cdot 25 \cdot 49}{6} + 24 \cdot \tfrac{24 \cdot 25}{2} + 5 \cdot 24\)") + p(r"\(= 78400 + 7200 + 120 = 85720\)."))) + final("85720, option 1"),
 shortcut=r"Write each product as \((m-2)(m+2) = m^2 - 4\) with \(m = 7, 11, \dots, 99\); the last digit of the sum must be 0, which leaves options 1 and 2.",
 concept=r"\[\sum_{n=1}^{N} n^2 = \frac{N(N+1)(2N+1)}{6}\]\[\sum_{n=1}^{N} n = \frac{N(N+1)}{2}\]",
 why_rows=[("2", "Digits of 85720 swapped."), ("3", "Digits swapped."), ("4", "Digits swapped.")])

P.qa(10, r"If \(x\) is a natural number and \(\log_x \tfrac{1}{2} = -\tfrac{1}{2}\), then the value of \(x\) is ____.",
 [], "TITA", "4", ["Algebra::Logarithms_and_Exponents"], "Medium",
 "Turn the log into a power.",
 steps(("Rewrite", p(r"\(x^{-1/2} = \tfrac{1}{2}\), so \(\sqrt{x} = 2\) and \(x = 4\)."))) + final("4"),
 concept=r"\[\log_b a = c \iff b^c = a\]")

P.qa(11, "17 glass balls of distinct colours and distinct weights have been arranged in a row. The weight of the red ball is 17 kg. The average weight of all balls other than the green one is 8.5625 kg. The average weight of all the balls is 500 gm more than the average weight of 16 balls other than the red one. The weight of the green ball, in kg, is ____.",
 [], "TITA", "16", ["Arithmetic::Average"], "Medium",
 "Let the 15 balls other than red and green weigh \\(W\\) in all.",
 steps(("Without green", p(r"16 balls average 8.5625: total \(137\) kg, so \(W = 137 - 17 = 120\).")),
       ("The 0.5 kg gap", p(r"\(\dfrac{137 + G}{17} - \dfrac{120 + G}{16} = \dfrac12\). Try a nice value: if \(120 + G = 136\), the averages are \(\tfrac{153}{17} = 9\) and \(\tfrac{136}{16} = 8.5\), a gap of 0.5. So \(G = 16\).")),
       ("Algebra check", p(r"Multiply by 272: \(16(137+G) - 17(120+G) = 136\), so \(2192 - 2040 - G = 136\), \(G = 16\)."))) + final("16"))

P.qa(12, r"If for any natural number \(n\), \(F_n(x) = f(f(\dots f(x)))\) (\(f\) applied \(n\) times), where \(f(x) = 5 + 3x\) for any real \(x\), then \(F_{10}(10)\) is ____.",
 ["738110", "783110", "713180", "711380"], "MCQ", "1", ["Algebra::Functions"], "Hard",
 r"Shift by the fixed point: \(f(x) + \tfrac52 = 3\left(x + \tfrac52\right)\).",
 steps(("Fixed point", p(r"\(x = 5 + 3x\) gives \(x = -\tfrac52\). So \(f(x) + \tfrac52 = 3\left(x + \tfrac52\right)\): adding \(\tfrac52\) turns \(f\) into multiplication by 3.")),
       ("Ten times", p(r"\(F_{10}(10) + \tfrac52 = 3^{10}\left(10 + \tfrac52\right)\) \(= 59049 \times 12.5 = 738112.5\).") + p(r"So \(F_{10}(10) = 738110\)."))) + final("738110, option 1"),
 shortcut="Last digit: f(x) ends in 5 + 3 × (last digit). 10 → 35 → 110 → 335 → … the values end 0, 5, 0, 5…; the 10th ends in 0. Then 3¹⁰ × 12.5 ≈ 738 thousand.",
 concept=r"\[f(x) = ax + b,\ \ p = \frac{b}{1-a}\]\[\Rightarrow f^{(n)}(x) = a^n(x - p) + p\]",
 why_rows=[("2", "Digits swapped."), ("3", "Digits swapped."), ("4", "Digits swapped.")])

P.qa(13, r"For some natural number \(n\), assume that \(N!\) is divisible by \((n!)!\) (where \(N\) is also a natural number). Which of the following statements is definitely correct?",
 [r"\(n! > N\)", r"\(n \le N\) and \(n! \le N\)", r"\(n < N\) and \(n! \le N\)", r"\(N\) is divisible by \(n\)"], "MCQ", "2", ["Number_System::Factorials"], "Medium",
 r"When does \(k!\) divide \(N!\)?",
 steps(("The rule", p(r"For natural numbers, \(k!\) divides \(N!\) exactly when \(k \le N\). Here \(k = n!\), so \(n! \le N\). Also \(n \le n!\), so \(n \le N\). Option 2 always holds.")),
       ("Test the others", p(r"\(n = N = 2\): \((2!)! = 2\) divides \(2!\), but \(n < N\) fails, so option 3 can fail. \(n = 3, N = 7\): \(6!\) divides \(7!\), but 3 doesn’t divide 7, so option 4 can fail."))) + final("Option 2"),
 why_rows=[("1", r"The opposite of what is forced."), ("3", r"Fails for \(n = N = 2\)."), ("4", r"Fails for \(n = 3,\ N = 7\).")])

P.qa(14, r"How many distinct positive integer-valued solutions exist to the equation \((x^2 - 5x + 5)^{\,x^2 + 3x + 4} = 1\)?",
 [], "TITA", "4", ["Algebra::Quadratic_Equations"], "Hard",
 "\\(a^b = 1\\) when \\(b = 0\\) (with \\(a \\ne 0\\)), when \\(a = 1\\), or when \\(a = -1\\) and \\(b\\) is even.",
 steps(("Exponent 0?", p(r"\(x^2 + 3x + 4\) has discriminant \(9 - 16 < 0\): never zero.")),
       ("Base 1", p(r"\(x^2 - 5x + 5 = 1\): \((x-1)(x-4) = 0\), so \(x = 1, 4\).")),
       ("Base −1, even exponent", p(r"\(x^2 - 5x + 5 = -1\): \((x-2)(x-3) = 0\), so \(x = 2, 3\). The exponent \(x(x+3) + 4\) is always even, since one of \(x, x+3\) is even. Both work."))) + trap("Base −1 counts only when the exponent is even; check it, don’t assume it.") + final("4"),
 concept=r"\[a^b = 1 \iff b = 0\ (a \ne 0),\ \text{or } a = 1,\ \text{or } a = -1 \text{ with } b \text{ even}\]")

P.qa(15, r"Let \(a_1, a_2, a_3, \dots, a_{10}\) be a sequence of ten consecutive natural numbers. Consider a new sequence of ten consecutive even numbers having \(2a_{10} - 2\) as the last term of the sequence. If the sum of the numbers in the new sequence is 210, then the average of the numbers of the original sequence without \(a_{10}\) is ____.",
 ["10.5", "11.0", "11.5", "12.0"], "MCQ", "2", ["Algebra::Progressions_and_Series"], "Easy",
 "The new sequence is \\(2a_{10} - 20, \\dots, 2a_{10} - 2\\).",
 steps(("Sum", p(r"\(10 \times 2a_{10} - 2(1 + 2 + \dots + 10)\) \(= 20a_{10} - 110 = 210\), so \(a_{10} = 16\).")),
       ("Original", p("7, 8, …, 16. Without 16: 7 to 15, average 11."))) + final("11.0, option 2"),
 why_rows=[("1", "Average of 6 to 15."), ("3", "Average of all ten, 7 to 16."), ("4", "Average of 8 to 16.")])

P.qa(16, "In the given figure, O and N are the centres of outer and inner circles respectively. Chord PQ is parallel to the common tangent to both the given circles. PQ = 12 units. Find the radius of the larger circle." +
 fig("sipe_SM01_QA_16.svg", "Large circle with centre O; a smaller circle inside touching it at the bottom and passing through O; chord PQ of the large circle through N, parallel to the tangent at the bottom"),
 [r"\(4\sqrt3\) units", r"\(6\sqrt3\) units", "8 units", "None of these"], "MCQ", "1", ["Geometry::Circles"], "Medium",
 "The small circle runs from the touching point up to O, so its diameter is the big circle’s radius.",
 steps(("Distances", p(r"Let the big radius be \(R\). The small circle’s diameter is \(R\), so \(ON = \tfrac{R}{2}\). PQ passes through N, and ON is perpendicular to PQ, so N is the midpoint: \(PN = 6\).")),
       ("Pythagoras in OPN", p(r"\(R^2 = 6^2 + \left(\tfrac R2\right)^2\), so \(\tfrac34R^2 = 36\), \(R^2 = 48\), \(R = 4\sqrt3\)."))) + final(r"\(4\sqrt3\) units, option 1"),
 concept=r"\[\text{Half-chord}^2 + \text{distance from centre}^2 = R^2\]",
 why_rows=[("2", r"Would need \(PN = 9\)."), ("3", "Would make PN = \\(\\sqrt{48}\\), not 6."), ("4", "Option 1 is right.")])

P.qa(17, "On a triangle ABC, a circle with diameter BC is drawn, intersecting AB and AC at points P and Q, respectively. If the lengths of AP, BP, BQ and PC are x cm, 39 cm, 60 cm, and 52 cm respectively, then the length of AQ, in cm, is ____.",
 [r"\(\dfrac{13x+132}{15}\)", r"\(\dfrac{13x+140}{15}\)", r"\(\dfrac{15x+132}{13}\)", r"\(\dfrac{15x+140}{13}\)"], "MCQ", "1", ["Geometry::Triangles"], "Medium",
 "Angles in a semicircle: \\(\\angle BPC = \\angle BQC = 90^\\circ\\). So PC and BQ are altitudes.",
 steps(("Lengths", p(r"In right triangle BPC: \(BC = \sqrt{39^2 + 52^2} = 65\). In right triangle BQC: \(QC = \sqrt{65^2 - 60^2} = 25\).")),
       ("Area two ways", p(r"\(AB \cdot PC = AC \cdot BQ\): \((x + 39) \times 52 = (AQ + 25) \times 60\). Divide by 4: \(13x + 507 = 15\,AQ + 375\), so \(AQ = \dfrac{13x + 132}{15}\)."))) + final("Option 1"),
 concept=r"\[\text{Area} = \tfrac12 \times \text{base} \times \text{altitude, for any side}\]",
 why_rows=[("2", "Arithmetic slip in 507 − 375."), ("3", "Ratio upside down."), ("4", "Ratio upside down.")])

P.qa(18, r"Find the largest natural number which will definitely divide \(4^n - 3n - 1\) where \(n\) is a natural number greater than 1.",
 [], "TITA", "9", ["Number_System::Factors_and_Divisibility"], "Medium",
 "Expand \\((1+3)^n\\).",
 steps(("Binomial", p(r"\(4^n = (1+3)^n\) \(= 1 + 3n + \binom n2 3^2 + \dots\), so \(4^n - 3n - 1\) is a multiple of 9.")),
       ("Can it be more?", p(r"\(n = 2\) gives \(16 - 7 = 9\). So nothing larger than 9 divides every value."))) + final("9"),
 concept=r"\[(1+x)^n = 1 + nx + \tbinom n2 x^2 + \cdots\]")

P.qa(19, "A man invests 20% of his total savings at 8.2% in scheme-A, 30% of the remaining savings at 3.5% in scheme-B, 50% of the remaining savings at 3% in scheme-C, 25% of the remaining savings at 12% in scheme-D, and the remaining savings at 4% in scheme-E, each rate being simple interest per annum. What is the overall annual return (in percentage) the man earns?",
 [], "TITA", "5", ["Arithmetic::Simple_and_Compound_Interest"], "Medium",
 "Start with 100 and track what is left after each scheme.",
 steps(("Scheme by scheme", p("A takes 20, leaving 80; B takes 30% of 80 = 24, leaving 56; C takes half, 28, leaving 28; D takes a quarter, 7; E gets the last 21.") + table(["Scheme", "Amount", "Rate", "Interest"],
           [["A", "20", "8.2%", "1.64"], ["B", "24", "3.5%", "0.84"], ["C", "28", "3%", "0.84"], ["D", "7", "12%", "0.84"], ["E", "21", "4%", "0.84"]])),
       ("Total", p("1.64 + 4 × 0.84 = 5 on 100: 5%."))) + final("5"))

P.qa(20, "Two runners start running simultaneously from two opposite ends of a straight path towards each other. After crossing each other, the first and second runners reach their destinations in four and nine minutes, respectively. The ratio of speeds of the first runner to that of the second is ____.",
 ["2 : 3", "3 : 2", "1 : 3", "3 : 1"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "After meeting, each covers the stretch the other ran before meeting.",
 steps(("The rule", p(r"If they meet after \(t\) minutes, the first runner’s remaining stretch (4 min at \(u\)) was covered by the second in \(t\) minutes: \(4u = tv\). Likewise \(9v = tu\). Dividing: \(\tfrac{u^2}{v^2} = \tfrac94\).")),
       ("Ratio", p(r"\(u : v = 3 : 2\) (and they meet after \(t = 6\) minutes)."))) + final("3 : 2, option 2"),
 concept=r"\[\frac{u}{v} = \sqrt{\frac{t_2}{t_1}}\quad(t_1, t_2 = \text{times taken after meeting})\]",
 why_rows=[("1", "Upside down: the first runner finishes sooner, so is faster."), ("3", "Not the square root."), ("4", "Not the square root.")])

P.qa(21, "If a 3-digit number has at least one ‘4’ and at least one ‘5’ as digits then, the number of such 3-digit numbers greater than 100, wherein the place value of each 5 is larger than the place value of each 4, equals ____.",
 [], "TITA", "25", ["Modern_Maths::Permutations_and_Combinations"], "Hard",
 "Every 5 must sit to the left of every 4. List where the 5 and the 4 can go.",
 steps(("One 5 and one 4", table(["Pattern", "Third digit", "Count"],
           [["5 4 _", "not 4 or 5", "8"], ["5 _ 4", "not 4 or 5", "8"], ["_ 5 4", "1–9, not 4 or 5", "7"]])),
       ("Repeated digits", p("554 and 544 also work. (545, 454 and others put a 4 left of a 5.)")),
       ("Total", p("8 + 8 + 7 + 2 = 25."))) + trap("The third digit can’t be 4 or 5 in these patterns; those cases are counted separately.") + final("25"))

P.qa(22, "A pitcher is filled with corn syrup and a second pitcher is filled with pure water. Half of the corn syrup and half of the pure water are poured into a large glass bowl. Next, one-third of the remaining corn syrup from the first pitcher and half of the remaining pure water from the second pitcher is again poured into the glass bowl. Now, the volumes of corn syrup and pure water left in the two pitchers are the same. Then the ratio of corn syrup and pure water in the large glass bowl is ____.",
 ["1 : 1", "3 : 2", "2 : 3", "8 : 3"], "MCQ", "3", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Track what is left: syrup keeps \\(\\tfrac12 \\times \\tfrac23\\), water keeps \\(\\tfrac12 \\times \\tfrac12\\).",
 steps(("What’s left", p(r"Syrup \(S\): \(\tfrac13 S\) left. Water \(W\): \(\tfrac14 W\) left. Equal: \(\tfrac S3 = \tfrac W4\), so \(S = 3k,\ W = 4k\).")),
       ("In the bowl", p(r"Syrup \(3k - k = 2k\), water \(4k - k = 3k\). Ratio \(2 : 3\)."))) + final("2 : 3, option 3"),
 why_rows=[("1", "Ignores the different fractions poured."), ("2", "Upside down."), ("4", "Not what is in the bowl.")])
