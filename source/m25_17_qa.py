# -*- coding: utf-8 -*-
# Simp Mock 17 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_17 import P
import m25_17_figs as F

P.qa(1, "a and b are integers with 11a + 7b = 570. What is the least possible value of |a − b|?", ["6", "9", "4", "7"], "MCQ", "1", ["Algebra::Linear_Equations"], "Easy",
 "Find one solution, then step by (7, −11).",
 steps(("Solutions", p("(34, 28) works; all are (34 + 7k, 28 − 11k).")), ("Difference", p("a − b = 6 + 18k, smallest in size 6."))) + final("Option 1"),
 why_rows=[("2", "Not reachable."), ("3", "Not reachable."), ("4", "Not reachable.")])

P.qa(2, r"What is the minimum value of \(2^x + 2^{1 - x}\)?", ["2", r"\(2\sqrt2\)", "4", r"\(4\sqrt2\)"], "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Easy",
 "AM–GM: the product is 2.",
 steps(("AM–GM", p(r"\(2^x + 2^{1-x} \ge 2\sqrt{2^x \cdot 2^{1-x}} = 2\sqrt2\), at x = ½."))) + final("Option 2"),
 why_rows=[("1", "Ignores the product."), ("3", "Not the minimum."), ("4", "Not the minimum.")])

P.qa(3, r"a, b, c are positive integers with \((a - b - c)^2 = 2(c^2 + bc - ab - ac)\) and a + b + c < 50. How many ordered triples (a, b, c) are there?", [], "TITA", "12", ["Number_System::Miscellaneous"], "Medium",
 "Expand: it reduces to a Pythagorean relation.",
 steps(("Reduce", p(r"Expanding gives \(a^2 + b^2 = c^2\).")),
       ("Triples", p("Perimeter under 50: (3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20).")),
       ("Order", p("a and b can swap: 12."))) + final("12"))

P.qa(4, r"For integers x with |x| ≤ 5, how many satisfy \(\left|\dfrac{x^3 - 1}{x}\right| \le |x^2 - x|\)?", ["7", "6", "5", "None of these"], "MCQ", "2", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "Factor out |x − 1|.",
 steps(("Rewrite", p(r"\(|x - 1|\,|x^2 + x + 1| \le x^2|x - 1|\) (x ≠ 0).")),
       ("Cases", p(r"x = 1 works. Otherwise need \(x^2 + x + 1 \le x^2\), i.e. x ≤ −1: −5 to −1.")), ("Count", p("6."))) + final("Option 2"),
 why_rows=[("1", "Counts x = 0."), ("3", "Misses x = 1."), ("4", "6 is listed.")])

P.qa(5, "Buildings A, B and C stand on a straight line, with B between A and C, and have different heights. The angle of elevation of the top of C is the same, α, from the foot of A and from the top of B. The angle of elevation of the top of A is the same, β, from the foot of C and from the top of B. A and B are 100 m and 80 m tall, and their feet are 100 m apart. Find sec²α + sec²β. (Ignore the buildings’ widths.)",
 [r"\(\tfrac{67}{25}\)", r"\(\tfrac{71}{25}\)", r"\(\tfrac{41}{16}\)", r"\(\tfrac{43}{16}\)"], "MCQ", "1", ["Geometry::Trigonometry"], "Hard",
 "Equal angles mean the top of B lies on both sight lines.",
 steps(("Picture", F.TOWERS),
       ("Distance BC", p(r"Line from the foot of C to the top of A passes the top of B: \(\tfrac{80}{100} = \tfrac{x}{100 + x}\), so x = 400.")),
       ("Height of C", p(r"Two crossing lines: \(\tfrac1{100} + \tfrac1y = \tfrac1{80}\), y = 400.")),
       ("Angles", p(r"\(\tan\alpha = \tfrac{400}{500} = \tfrac45\), \(\tan\beta = \tfrac{100}{500} = \tfrac15\); \(\sec^2\alpha + \sec^2\beta = 2 + \tfrac{16}{25} + \tfrac1{25} = \tfrac{67}{25}\)."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(6, r"A right circular cone has base radius 4 cm and height 8 cm. A smaller cone is cut off its tip by a cut parallel to the base, at half the height. What is the volume of the remaining part? (Take \(\pi = \tfrac{22}{7}\).)",
 [r"\(\tfrac{352}{3}\) cm³", r"\(\tfrac{256}{3}\) cm³", r"\(\tfrac{512}{3}\) cm³", r"\(\tfrac{192}{3}\) cm³"], "MCQ", "1", ["Geometry::Mensuration"], "Easy",
 "The small cone is ⅛ of the big one.",
 steps(("Big cone", p(r"\(\tfrac13 \cdot \tfrac{22}{7} \cdot 16 \cdot 8 = \tfrac{2816}{21}\).")), ("Remaining", p(r"\(\tfrac78 \times \tfrac{2816}{21} = \tfrac{352}{3}\)."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(7, "A toy maker glues 480 identical wooden cubes of edge 2 cm into a solid cuboid whose three dimensions (in cm) are consecutive multiples of 4. What is the ratio of the cuboid’s body diagonal to its shortest face diagonal?", [r"\(\sqrt3 : 1\)", r"\(\sqrt5 : 2\)", r"\(2 : \sqrt3\)", r"\(\sqrt2 : 1\)"], "MCQ", "4", ["Geometry::Mensuration"], "Medium",
 "Volume 480 × 8 = 3840 = 64x(x + 1)(x + 2).",
 steps(("Size", p("x(x + 1)(x + 2) = 60, x = 3: 12 × 16 × 20.")),
       ("Diagonals", p(r"Body \(\sqrt{144 + 256 + 400} = 20\sqrt2\); shortest face \(\sqrt{144 + 256} = 20\). Ratio \(\sqrt2 : 1\)."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(8, "In △ABC, AB ⊥ BC and BD ⊥ AC with D on AC. AB, BC, AC and CD are whole numbers of centimetres, and BD = 12 cm. Find the perimeter of △ABC (in cm).", [], "TITA", "60", ["Geometry::Triangles"], "Medium",
 "AD × DC = BD² = 144.",
 steps(("Split", p(r"AD and DC multiply to 144, and \(AD^2 + 144\), \(DC^2 + 144\) must be squares: 9 and 16.")),
       ("Sides", p("AB = 15, BC = 20, AC = 25: perimeter 60."))) + final("60"))

P.qa(9, "Inlet pipes P1 and P2 fill an empty tank alone in 35 and 45 hours. When both are open together, each pipe’s rate drops by p%, and together they fill the tank in 21 hours. Find p.", [r"\(6\tfrac23\)", r"\(6\tfrac14\)", r"\(6\tfrac19\)", r"\(6\tfrac1{11}\)"], "MCQ", "2", ["Arithmetic::Time_and_Work"], "Easy",
 "Tank 315 units: rates 9 and 7.",
 steps(("Equation", p(r"\(16(1 - \tfrac{p}{100}) \times 21 = 315\), so \(1 - \tfrac{p}{100} = \tfrac{15}{16}\).")), ("p", p(r"\(6\tfrac14\)."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(10, r"Trains A and B run on parallel tracks. A is twice as long as B, and their lengths differ by 400 m. The slower train’s speed is \(\tfrac5{11}\) of the faster one’s. A takes 50 seconds longer to pass B completely when they run in the same direction than when they run in opposite directions. What is the slower train’s speed?", ["99 km/h", "72 km/h", "60 km/h", "45 km/h"], "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Lengths 800 and 400: 1200 m to clear.",
 steps(("Speeds", p(r"Let the speeds be 11k and 5k m/s: \(\tfrac{1200}{6k} - \tfrac{1200}{16k} = 50\), so \(\tfrac{125}{k} = 50\), k = 2.5.")), ("Slower", p("12.5 m/s = 45 km/h."))) + final("Option 4"),
 why_rows=[("1", "The faster train."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(11, "In a school election, 15,000 students voted for Ravi or Kiran, and Ravi won. Had 25% of Kiran’s voters voted for Ravi instead, Ravi’s winning margin would have doubled. How many voted for Kiran?", ["7300", "6900", "6300", "6000"], "MCQ", "4", ["Arithmetic::Percentages"], "Easy",
 "Moving v votes changes the margin by 2v.",
 steps(("Equation", p("Kiran K: margin 15000 − 2K; moving K/4 adds K/2, which must equal the margin: K/2 = 15000 − 2K.")), ("K", p("K = 6000."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(12, "A bottle is partly filled with pure grape juice. Five litres are taken out and replaced with water, and this is done twice more. Then 5 more litres of pure juice fill the bottle to the brim. The juice-to-water ratio is now 5 : 7. What is the bottle’s capacity (in litres)?", ["10", "12", "15", "18"], "MCQ", "3", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "Let the starting juice be V litres; capacity V + 5.",
 steps(("After three swaps", p(r"Juice \(V\left(1 - \tfrac5V\right)^3\).")),
       ("Check V = 10", p(r"\(10 \times \tfrac18 = 1.25\), plus 5 = 6.25 of 15 litres, and \(\tfrac{5}{12} \times 15 = 6.25\). ✓"))) + final("Option 3"),
 why_rows=[("1", "That is V."), ("2", "Ratio fails."), ("4", "Ratio fails.")])

P.qa(13, "Ravi, Sameer and Karan can paint a wall alone in 9, 18 and 3 days. They start together. At some point Karan stops; from then Ravi and Sameer could have finished in 3 days. After Ravi and Sameer work together for a while, Ravi stops, and Sameer finishes the rest in 3 days. How many days does the painting take in all?", ["8 days", "7 days", "5 days", "6 days"], "MCQ", "4", ["Arithmetic::Time_and_Work"], "Medium",
 "Wall = 18 units; rates 2, 1 and 6.",
 steps(("After Karan", p("Ravi and Sameer’s 3 days = 9 units left. Sameer’s last 3 units leave 6 for the pair: 2 days.")),
       ("All three", p("First 9 units at 9 a day: 1 day.")), ("Total", p("1 + 2 + 3 = 6."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(14, "A quarter of a school’s scholarship holders are rural students and the rest urban. Rural students get 20% of the total scholarship money. What is the ratio of the average scholarship of an urban student to that of a rural student?", ["4 : 5", "3 : 4", "4 : 3", "5 : 6"], "MCQ", "3", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Averages: 20/25 and 80/75.",
 steps(("Ratio", p(r"\(\tfrac{80}{75} : \tfrac{20}{25} = \tfrac{16}{15} : \tfrac45 = 4 : 3\)."))) + final("Option 3"),
 why_rows=[("1", "Inverted."), ("2", "Inverted."), ("4", "Arithmetic slip.")])

P.qa(15, r"Gopal and Tarun start running at the same time from the two ends of a 15 km road towards the opposite ends, at different steady speeds. They meet after 45 minutes, and Gopal reaches his end \(18\tfrac2{11}\) minutes before Tarun reaches his. What is Tarun’s speed (in km/h)?", ["8", "8.5", "9", "9.5"], "MCQ", "3", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Speeds add to 20 km/h.",
 steps(("Equation", p(r"\(\tfrac{15}{t} - \tfrac{15}{20 - t} = \tfrac{10}{33}\) hour.")), ("Check", p(r"t = 9, g = 11: \(\tfrac{15}{9} - \tfrac{15}{11} = \tfrac{30}{99} = \tfrac{10}{33}\). ✓"))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(16, "The wheels of bicycles P and Q have radii 24 cm and 36 cm. Over a certain distance each wheel of P makes 6250 more revolutions than each wheel of Q. If Q covers the distance in 45 minutes, what is its speed (in km/h)?", ["12π", "14π", "16π", "18π"], "MCQ", "1", ["Geometry::Circles"], "Easy",
 "Revolutions are in the ratio 3 : 2.",
 steps(("Q’s revolutions", p("2 × 6250 = 12,500.")), ("Distance", p("12,500 × 2π × 0.36 m = 9000π m = 9π km.")), ("Speed", p("9π ÷ 0.75 = 12π."))) + final("Option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(17, r"Find \(2^{\log_3 5} + 3^{\log_5 7} + 5^{\log_7 11} + 7^{\log_{11} 13}\) \(- 5^{\log_3 2} - 7^{\log_5 3} - 11^{\log_7 5} - 13^{\log_{11} 7}\).", [], "TITA", "0", ["Algebra::Logarithms_and_Exponents"], "Medium",
 r"\(a^{\log_b c} = c^{\log_b a}\).",
 steps(("Swap", p(r"\(2^{\log_3 5} = 5^{\log_3 2}\), \(3^{\log_5 7} = 7^{\log_5 3}\), \(5^{\log_7 11} = 11^{\log_7 5}\), \(7^{\log_{11} 13} = 13^{\log_{11} 7}\).")),
       ("Cancel", p("Each positive term cancels a negative one: 0."))) + final("0"))

P.qa(18, "A two-digit number xy (that is, 10x + y) has exactly three positive divisors. How many positive divisors does the four-digit number xyxy have?", [], "TITA", "6", ["Number_System::Factors_and_Divisibility"], "Easy",
 "xyxy = 101 × xy.",
 steps(("xy", p(r"Three divisors means \(p^2\): 25 or 49.")), ("xyxy", p(r"\(101 \times p^2\): (1 + 1)(2 + 1) = 6 divisors."))) + final("6"))

P.qa(19, r"p and q are rational numbers with \(\sqrt{17 + 12\sqrt2} = p + q\sqrt2\). Find p + q.", [], "TITA", "5", ["Algebra::Surds_and_Indices"], "Easy",
 r"\((p + q\sqrt2)^2 = p^2 + 2q^2 + 2pq\sqrt2\).",
 steps(("Match", p(r"\(p^2 + 2q^2 = 17\), pq = 6: p = 3, q = 2, since \((3 + 2\sqrt2)^2 = 17 + 12\sqrt2\).")), ("Sum", p("5."))) + final("5"))

P.qa(20, r"f(x) is the remainder when \(x^{20}\) is divided by 5. Find f(1) + f(2) + … + f(100).", ["75", "80", "100", "140"], "MCQ", "2", ["Number_System::Remainders"], "Easy",
 "Fermat: x⁴ ≡ 1 (mod 5) unless 5 divides x.",
 steps(("Values", p("f(x) = 1 for the 80 numbers not divisible by 5, and 0 for the other 20.")), ("Sum", p("80."))) + final("Option 2"),
 why_rows=[("1", "Arithmetic slip."), ("3", "Counts every x."), ("4", "Arithmetic slip.")])

P.qa(21, r"Find the real number n with \(10^n + 100^n + 1000^n = 14\).", [r"\(\log_{10}\tfrac32\)", r"\(\log_{10}5\)", r"\(\log_{10}3\)", r"\(\log_{10}2\)"], "MCQ", "4", ["Algebra::Logarithms_and_Exponents"], "Easy",
 r"Let \(x = 10^n\): \(x + x^2 + x^3 = 14\).",
 steps(("Root", p("x = 2 works, and the left side is increasing for x > 0, so it’s the only one.")), ("n", p(r"\(n = \log_{10}2\)."))) + final("Option 4"),
 why_rows=[("1", "x = 1.5 gives 6.5."), ("2", "x = 5 is far too big."), ("3", "x = 3 gives 39.")])

P.qa(22, "A teacher divides 10 students into two groups of at least 2 each, with Alfred and Wilfred in different groups. In how many ways can she do it?", ["511", "255", "254", "510"], "MCQ", "3", ["Modern_Maths::Permutations_and_Combinations"], "Easy",
 "Place the other 8 with Alfred or Wilfred.",
 steps(("Assign", p(r"\(2^8 = 256\) ways, less the 2 that leave someone alone: 254."))) + final("Option 3"),
 why_rows=[("1", "Ignores the size rule and the split."), ("2", "Allows a group of one."), ("4", "Double counts.")])
