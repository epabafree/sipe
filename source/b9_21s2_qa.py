# -*- coding: utf-8 -*-
# Batch 9 — CAT 2021 Slot 2: QA Q1–22 (exam order).
from fmt import steps, final, trap, why, table, p
from b9_21s2 import P

M = lambda *xs: [rf"\({x}\)" for x in xs]

P.qa(1, r"For all possible integers \(n\) satisfying \(2.25 \le 2 + 2^{n+2} \le 202\), the number of integer values of \(3 + 3^{n+1}\) is",
 [], "TITA", "7", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"Find the integers \(n\) first. Then ask when \(3^{n+1}\) is a whole number.",
 steps(("The range of n", p(r"\(0.25 \le 2^{n+2} \le 200\), so \(n + 2\) runs from \(-2\) to \(7\): \(n = -4, \dots, 5\).")),
       ("Integer values", p(r"\(3 + 3^{n+1}\) is an integer only when \(n + 1 \ge 0\), that is \(n = -1, 0, \dots, 5\): 7 values."))) + trap(r"There are 10 possible values of \(n\), but for \(n = -4, -3, -2\) the expression isn’t a whole number.") + final(r"\(7\)"),
 concept=r"\[a^{k} \text{ is a fraction for } k < 0 \text{ when } a > 1\]")

P.qa(2, r"Three positive integers \(x, y\) and \(z\) are in arithmetic progression. If \(y - x > 2\) and \(xyz = 5(x + y + z)\), then \(z - x\) equals",
 M("8", "12", "10", "14"), "MCQ", "4", ["Algebra::Progressions_and_Series"], "Medium",
 r"In an AP, \(x + y + z = 3y\).",
 steps(("Simplifying", p(r"\(xyz = 15y\), so \(xz = 15\).")),
       ("Cases", p(r"\(x\) and \(z\) are 1 and 15, or 3 and 5. With 3 and 5 the common difference is 1, which fails \(y - x > 2\). So \(x = 1\), \(y = 8\), \(z = 15\), and \(z - x = 14\)."))) + final(r"\(14\), option 4"),
 concept=r"\[x, y, z \text{ in AP} \Rightarrow x + z = 2y\]",
 why_rows=[("1", "Not a possible difference."), ("2", "Not a possible difference."), ("3", "Not a possible difference.")])

P.qa(3, r"For a \(4\)-digit number, the sum of its digits in the thousands, hundreds and tens places is \(14\), the sum of its digits in the hundreds, tens and units places is \(15\), and the tens place digit is \(4\) more than the units place digit. Then the highest possible \(4\)-digit number satisfying the above conditions is",
 [], "TITA", "4195", ["Number_System::Miscellaneous"], "Easy",
 r"Subtract the two sums to link the first and last digits.",
 steps(("Relations", p(r"With digits \(a, b, c, d\): \(d - a = 1\) and \(c = d + 4\). So \(d \le 5\).")),
       ("Largest", p(r"To make \(a\) largest, take \(d = 5\): \(a = 4\), \(c = 9\), and \(b = 14 - 4 - 9 = 1\). The number is 4195."))) + final(r"\(4195\)"),
 concept=p("To maximise a number, maximise the leading digit first, then the next."))

P.qa(4, r"Raj invested ₹\(10000\) in a fund. At the end of first year, he incurred a loss but his balance was more than ₹\(5000\). This balance, when invested for another year, grew and the percentage of growth in the second year was five times the percentage of loss in the first year. If the gain of Raj from the initial investment over the two year period is \(35\%\), then the percentage of loss in the first year is",
 M("10", "5", "70", "15"), "MCQ", "1", ["Arithmetic::Percentages"], "Easy",
 r"Write \((1 - r)(1 + 5r) = 1.35\).",
 steps(("Equation", p(r"\(1 + 4r - 5r^2 = 1.35\), so \(5r^2 - 4r + 0.35 = 0\), giving \(r = 0.1\) or \(r = 0.7\).")),
       ("Choosing", p("A 70% loss would leave less than ₹5000, so the loss was 10%."))) + final(r"\(10\), option 1"),
 concept=r"\[\text{successive changes: } (1 + r_1)(1 + r_2)\]",
 why_rows=[("2", r"\(0.95 \times 1.25 \approx 1.19\), not 1.35."), ("3", "Fits the equation but leaves the balance below ₹5000."), ("4", r"\(0.85 \times 1.75 \approx 1.49\).")])

P.qa(5, r"The number of ways of distributing \(15\) identical balloons, \(6\) identical pencils and \(3\) identical erasers among \(3\) children, such that each child gets at least four balloons and one pencil, is",
 [], "TITA", "1000", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "Hand out the minimums first, then share what is left freely.",
 steps(("Balloons", p(r"After 4 each, 3 are left: \(\binom{5}{2} = 10\) ways.")),
       ("Pencils", p(r"After 1 each, 3 are left: 10 ways.")),
       ("Erasers", p(r"3 with no minimum: 10 ways.")),
       ("Together", p(r"\(10 \times 10 \times 10 = 1000\)."))) + final(r"\(1000\)"),
 concept=r"\[n \text{ identical items among } r \text{ people: } \binom{n + r - 1}{r - 1}\]")

P.qa(6, r"Two trains A and B were moving in opposite directions, their speeds being in the ratio \(5 : 3\). The front end of A crossed the rear end of B \(46\) seconds after the front ends of the trains had crossed each other. It took another \(69\) seconds for the rear ends of the trains to cross each other. The ratio of length of train A to that of train B is",
 M("2 : 3", "5 : 3", "2 : 1", "3 : 2"), "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Watch the meeting point move along each train at the relative speed.",
 steps(("First 46 seconds", p("From fronts meeting to A’s front reaching B’s rear, the relative motion covers B’s full length.")),
       ("Next 69 seconds", p("From then until the rear ends meet, it covers A’s full length.")),
       ("Ratio", p("At the same relative speed, the lengths are in the ratio of the times: A : B = 69 : 46 = 3 : 2."))) + trap("The 5 : 3 speed ratio isn’t needed; both stretches happen at the same relative speed.") + final(r"\(3 : 2\), option 4"),
 concept=r"\[\text{same speed} \Rightarrow \text{distance} \propto \text{time}\]",
 why_rows=[("1", "Inverts the ratio."), ("2", "The speed ratio, not the length ratio."), ("3", "Not 69 : 46.")])

P.qa(7, r"Suppose one of the roots of the equation \(ax^2 - bx + c = 0\) is \(2 + \sqrt3\), where \(a, b\) and \(c\) are rational numbers and \(a \ne 0\). If \(b = c^3\), then \(|a|\) equals",
 M("3", "1", "4", "2"), "MCQ", "4", ["Algebra::Quadratic_Equations"], "Easy",
 "The other root is the conjugate.",
 steps(("Sum and product", p(r"Roots \(2 \pm \sqrt3\): sum \(\tfrac{b}{a} = 4\), product \(\tfrac{c}{a} = 1\). So \(b = 4a\), \(c = a\).")),
       ("Using b = c³", p(r"\(4a = a^3\), so \(a^2 = 4\) and \(|a| = 2\)."))) + final(r"\(2\), option 4"),
 concept=r"\[\text{rational coefficients: } p + \sqrt q \text{ a root} \Rightarrow p - \sqrt q \text{ a root}\]",
 why_rows=[("1", r"\(a^2 = 4\), not 9."), ("2", r"\(a^2 = 4\), not 1."), ("3", "That is b/a, the sum of the roots.")])

P.qa(8, r"From a container filled with milk, \(9\) litres of milk are drawn and replaced with water. Next, from the same container, \(9\) litres are drawn and again replaced with water. If the volumes of milk and water in the container are now in the ratio of \(16 : 9\), then the capacity of the container, in litres, is",
 [], "TITA", "45", ["Arithmetic::Mixture_and_Alligation"], "Easy",
 "After two replacements the milk fraction is (1 − 9/V)².",
 steps(("Milk fraction", p(r"Milk is \(\tfrac{16}{25}\) of the container, so \(\left(1 - \tfrac{9}{V}\right)^2 = \tfrac{16}{25}\).")),
       ("Solving", p(r"\(1 - \tfrac9V = \tfrac45\), so \(V = 45\)."))) + final(r"\(45\)"),
 concept=r"\[\text{after } n \text{ replacements: } \text{milk} = V\left(1 - \frac{x}{V}\right)^n\]")

P.qa(9, r"If a rhombus has area \(12\) sq cm and side length \(5\) cm, then the length, in cm, of its longer diagonal is",
 M(r"\dfrac{\sqrt{37} + \sqrt{13}}{2}", r"\sqrt{37} + \sqrt{13}", r"\dfrac{\sqrt{13} + \sqrt{12}}{2}", r"\sqrt{13} + \sqrt{12}"), "MCQ", "2", ["Geometry::Polygons_and_Quadrilaterals"], "Medium",
 r"With diagonals \(p, q\): \(pq = 24\) and \(p^2 + q^2 = 100\).",
 steps(("Sum and difference", p(r"\((p + q)^2 = 100 + 48 = 148\), so \(p + q = 2\sqrt{37}\). \((p - q)^2 = 100 - 48 = 52\), so \(p - q = 2\sqrt{13}\).")),
       ("Longer diagonal", p(r"\(p = \sqrt{37} + \sqrt{13}\)."))) + final(r"\(\sqrt{37} + \sqrt{13}\), option 2"),
 concept=r"\[\text{rhombus: area} = \tfrac12 pq, \qquad p^2 + q^2 = 4a^2\]",
 why_rows=[("1", "Half the longer diagonal."), ("3", "Not a diagonal of this rhombus."), ("4", "Not a diagonal of this rhombus.")])

P.qa(10, r"If \(\log_2\left[3 + \log_3\{4 + \log_4(x - 1)\}\right] - 2 = 0\), then \(4x\) equals",
 [], "TITA", "5", ["Algebra::Logarithms_and_Exponents"], "Easy",
 "Peel the logarithms off from the outside in.",
 steps(("Outside in", p(r"\(3 + \log_3\{\ldots\} = 4\), so \(\log_3\{\ldots\} = 1\), so \(4 + \log_4(x - 1) = 3\), so \(\log_4(x - 1) = -1\).")),
       ("Solving", p(r"\(x - 1 = \tfrac14\), \(x = \tfrac54\), \(4x = 5\)."))) + final(r"\(5\)"),
 concept=r"\[\log_b y = k \iff y = b^k\]")

P.qa(11, r"The sides \(AB\) and \(CD\) of a trapezium \(ABCD\) are parallel, with \(AB\) being the smaller side. \(P\) is the midpoint of \(CD\) and \(ABPD\) is a parallelogram. If the difference between the areas of the parallelogram \(ABPD\) and the triangle \(BPC\) is \(10\) sq cm, then the area, in sq cm, of the trapezium \(ABCD\) is",
 M("40", "30", "25", "20"), "MCQ", "2", ["Geometry::Polygons_and_Quadrilaterals"], "Easy",
 r"\(ABPD\) is a parallelogram, so \(DP = AB\), and \(PC = DP\).",
 steps(("Areas", p(r"With \(AB = a\) and height \(h\): parallelogram \(ah\), triangle \(BPC\) \(\tfrac12 ah\). The difference is \(\tfrac12 ah = 10\), so \(ah = 20\).")),
       ("Trapezium", p(r"Parallel sides \(a\) and \(2a\): area \(\tfrac32 ah = 30\)."))) + final(r"\(30\), option 2"),
 concept=r"\[\text{trapezium} = \tfrac12(\text{sum of parallel sides}) \times h\]",
 why_rows=[("1", r"That would be \(2ah\)."), ("3", "Not a multiple of 10 that fits."), ("4", "That is the parallelogram alone.")])

P.qa(12, r"For all real values of \(x\), the range of the function \(f(x) = \dfrac{x^2 + 2x + 4}{2x^2 + 4x + 9}\) is",
 M(r"\left[\tfrac37, \tfrac89\right)", r"\left(\tfrac37, \tfrac12\right)", r"\left[\tfrac37, \tfrac12\right)", r"\left[\tfrac49, \tfrac89\right]"), "MCQ", "3", ["Algebra::Functions"], "Medium",
 r"Complete the square: put \(t = (x + 1)^2 \ge 0\).",
 steps(("Rewriting", p(r"\(f = \dfrac{t + 3}{2t + 7}\), with \(t \ge 0\).")),
       ("Range", p(r"At \(t = 0\), \(f = \tfrac37\). As \(t\) grows, \(f\) increases towards \(\tfrac12\) but never reaches it."))) + final(r"\(\left[\tfrac37, \tfrac12\right)\), option 3"),
 concept=r"\[\frac{t + p}{2t + q} \to \frac12 \text{ as } t \to \infty\]",
 why_rows=[("1", r"The upper limit is \(\tfrac12\)."), ("2", r"\(\tfrac37\) is reached at \(x = -1\)."), ("4", r"The lower limit is \(\tfrac37\).")])

P.qa(13, r"For a sequence of real numbers \(x_1, x_2, \ldots, x_n\), if \(x_1 - x_2 + x_3 - \ldots\) \(+\, (-1)^{n+1}x_n = n^2 + 2n\) for all natural numbers \(n\), then the sum \(x_{49} + x_{50}\) equals",
 M("-2", "2", "-200", "200"), "MCQ", "1", ["Algebra::Progressions_and_Series"], "Medium",
 r"Let \(S_n = n^2 + 2n\). Then \(x_{49} = S_{49} - S_{48}\) and \(x_{50} = S_{49} - S_{50}\).",
 steps(("The values", p(r"\(S_{48} = 2400\), \(S_{49} = 2499\), \(S_{50} = 2600\). So \(x_{49} = 99\) and \(x_{50} = -101\).")),
       ("Sum", p(r"\(99 - 101 = -2\)."))) + trap(r"\(x_{50}\) enters the sum with a minus sign, so \(x_{50} = S_{49} - S_{50}\), not \(S_{50} - S_{49}\).") + final(r"\(-2\), option 1"),
 concept=r"\[S_n - S_{n-1} = (-1)^{n+1}x_n\]",
 why_rows=[("2", "Sign error on x₅₀."), ("3", "Not the sum of these two terms."), ("4", "Not the sum of these two terms.")])

P.qa(14, r"For a real number \(x\) the condition \(|3x - 20| + |3x - 40| = 20\) necessarily holds if",
 M("9 < x < 14", "6 < x < 11", "10 < x < 15", "7 < x < 12"), "MCQ", "4", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 r"\(|u - 20| + |u - 40| = 20\) exactly when \(u\) lies between 20 and 40.",
 steps(("The set", p(r"\(20 \le 3x \le 40\), so \(\tfrac{20}{3} \le x \le \tfrac{40}{3}\), roughly 6.67 to 13.33.")),
       ("Necessarily", p("The condition must hold for every x in the option, so the option must lie inside this range. Only 7 < x < 12 does."))) + final(r"\(7 < x < 12\), option 4"),
 concept=r"\[|u - a| + |u - b| = b - a \iff a \le u \le b\]",
 why_rows=[("1", "Goes past 13.33."), ("2", "Starts below 6.67."), ("3", "Goes past 13.33.")])

P.qa(15, r"Anil can paint a house in \(60\) days while Bimal can paint it in \(84\) days. Anil starts painting and after \(10\) days, Bimal and Charu join him. Together, they complete the painting in \(14\) more days. If they are paid a total of ₹\(21000\) for the job, then the share of Charu, in ₹, proportionate to the work done by him, is",
 M("9100", "9150", "9000", "9200"), "MCQ", "1", ["Arithmetic::Time_and_Work"], "Easy",
 "Take the job as 420 units.",
 steps(("Rates", p("Anil 7, Bimal 5 units a day.")),
       ("Charu’s rate", p(r"Anil’s first 10 days: 70. The remaining 350 take 14 days, so all three do 25 a day and Charu 13.")),
       ("Charu’s share", p(r"He did \(14 \times 13 = 182\) units: \(\tfrac{182}{420} \times 21000 = 9100\)."))) + final(r"\(9100\), option 1"),
 concept=r"\[\text{pay} \propto \text{work done}\]",
 why_rows=[("2", "Not 182/420 of 21000."), ("3", "Not 182/420 of 21000."), ("4", "Not 182/420 of 21000.")])

P.qa(16, r"A box has \(450\) balls, each either white or black, there being as many metallic white balls as metallic black balls. If \(40\%\) of the white balls and \(50\%\) of the black balls are metallic, then the number of non-metallic balls in the box is",
 [], "TITA", "250", ["Arithmetic::Percentages"], "Easy",
 r"\(0.4W = 0.5B\).",
 steps(("Counts", p(r"\(W = 1.25B\), so \(2.25B = 450\): \(B = 200\), \(W = 250\).")),
       ("Non-metallic", p(r"\(0.6 \times 250 = 150\) white and \(0.5 \times 200 = 100\) black: 250 in all."))) + final(r"\(250\)"),
 concept=p("Turn an ‘equal parts’ condition into a ratio first."))

P.qa(17, r"In a football tournament, a player has played a certain number of matches and \(10\) more matches are to be played. If he scores a total of one goal over the next \(10\) matches, his overall average will be \(0.15\) goals per match. On the other hand, if he scores a total of two goals over the next \(10\) matches, his overall average will be \(0.2\) goals per match. The number of matches he has played is",
 [], "TITA", "10", ["Arithmetic::Average"], "Easy",
 "One extra goal raises the average by 0.05.",
 steps(("Total matches", p(r"\(\tfrac{1}{N} = 0.05\), so there are 20 matches in all.")),
       ("Played so far", p(r"\(20 - 10 = 10\)."))) + final(r"\(10\)"),
 concept=r"\[\text{change in average} = \frac{\text{change in total}}{\text{count}}\]")

P.qa(18, r"A person buys tea of three different qualities at ₹\(800\), ₹\(500\), and ₹\(300\) per kg, respectively, and the amounts bought are in the proportion \(2 : 3 : 5\). She mixes all the tea and sells one-sixth of the mixture at ₹\(700\) per kg. The price, in ₹ per kg, at which she should sell the remaining tea, to make an overall profit of \(50\%\), is",
 M("688", "692", "653", "675"), "MCQ", "1", ["Arithmetic::Profit_Loss_and_Discount", "Arithmetic::Mixture_and_Alligation"], "Easy",
 "Find the cost per kg of the mixture, then the average selling price needed.",
 steps(("Cost", p(r"For 10 kg: \(1600 + 1500 + 1500 = 4600\), so ₹460 per kg.")),
       ("Target", p("A 50% profit needs an average price of ₹690.")),
       ("Remaining tea", p(r"\(\tfrac{700 + 5p}{6} = 690\), so \(p = 688\)."))) + final(r"\(688\), option 1"),
 concept=r"\[\text{average price} = \text{weighted mean of the prices}\]",
 why_rows=[("2", "Too high."), ("3", "Too low."), ("4", "Too low.")])

P.qa(19, r"Consider the pair of equations: \(x^2 - xy - x = 22\) and \(y^2 - xy + y = 34\). If \(x > y\), then \(x - y\) equals",
 M("7", "4", "6", "8"), "MCQ", "4", ["Algebra::Quadratic_Equations"], "Easy",
 "Add the two equations.",
 steps(("Adding", p(r"\(x^2 - 2xy + y^2 - x + y = 56\), that is \((x - y)^2 - (x - y) - 56 = 0\).")),
       ("Solving", p(r"\(x - y = 8\) or \(-7\). Since \(x > y\), it is 8."))) + final(r"\(8\), option 4"),
 concept=p("When two equations look alike, add or subtract them to get a perfect square."),
 why_rows=[("1", "The other root has the wrong sign: x − y = −7."), ("2", "Not a root."), ("3", "Not a root.")])

P.qa(20, r"Let \(D\) and \(E\) be points on sides \(AB\) and \(AC\), respectively, of a triangle \(ABC\), such that \(AD : BD = 2 : 1\) and \(AE : CE = 2 : 3\). If the area of the triangle \(ADE\) is \(8\) sq cm, then the area of the triangle \(ABC\), in sq cm, is",
 [], "TITA", "30", ["Geometry::Triangles"], "Easy",
 "Triangles sharing an angle have areas in the ratio of the products of the sides around it.",
 steps(("Ratio", p(r"\(\dfrac{[ADE]}{[ABC]} = \dfrac23 \times \dfrac25 = \dfrac{4}{15}\).")),
       ("Area", p(r"\([ABC] = 8 \times \tfrac{15}{4} = 30\)."))) + final(r"\(30\)"),
 concept=r"\[\frac{[ADE]}{[ABC]} = \frac{AD}{AB} \cdot \frac{AE}{AC}\]")

P.qa(21, r"Anil, Bobby and Chintu jointly invest in a business and agree to share the overall profit in proportion to their investments. Anil’s share of investment is \(70\%\). His share of profit decreases by ₹\(420\) if the overall profit goes down from \(18\%\) to \(15\%\). Chintu’s share of profit increases by ₹\(80\) if the overall profit goes up from \(15\%\) to \(17\%\). The amount, in ₹, invested by Bobby is",
 M("2200", "2400", "1800", "2000"), "MCQ", "4", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "A change of a few percentage points in profit is that many percent of the investment.",
 steps(("Anil", p(r"3% of Anil’s investment is ₹420, so he invested ₹14,000, which is 70% of ₹20,000.")),
       ("Chintu", p(r"2% of Chintu’s investment is ₹80, so he invested ₹4,000.")),
       ("Bobby", p(r"\(20000 - 14000 - 4000 = 2000\)."))) + final(r"\(2000\), option 4"),
 concept=p("Profit shared in proportion to investment means each person’s profit is the same percentage of what they put in."),
 why_rows=[("1", "Doesn’t add up to ₹20,000."), ("2", "Doesn’t add up to ₹20,000."), ("3", "Doesn’t add up to ₹20,000.")])

P.qa(22, r"Two pipes A and B are attached to an empty water tank. Pipe A fills the tank while pipe B drains it. If pipe A is opened at \(2\) pm and pipe B is opened at \(3\) pm, then the tank becomes full at \(10\) pm. Instead, if pipe A is opened at \(2\) pm and pipe B is opened at \(4\) pm, then the tank becomes full at \(6\) pm. If pipe B is not opened at all, then the time, in minutes, taken to fill the tank is",
 M("264", "140", "120", "144"), "MCQ", "4", ["Arithmetic::Time_and_Work"], "Medium",
 "Write both cases as (hours of A) × a − (hours of B) × b = full tank.",
 steps(("Equations", p(r"\(8a - 7b = 4a - 2b\), so \(4a = 5b\) and \(b = 0.8a\).")),
       ("The tank", p(r"\(4a - 1.6a = 2.4a\), so A alone takes 2.4 hours = 144 minutes."))) + final(r"\(144\), option 4"),
 concept=r"\[\text{net work} = (\text{fill rate} \times \text{hours}) - (\text{drain rate} \times \text{hours})\]",
 why_rows=[("1", "Not 2.4 hours."), ("2", "Not 2.4 hours."), ("3", "Two hours; ignores the drain’s effect.")])
