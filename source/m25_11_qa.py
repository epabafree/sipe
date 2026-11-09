# -*- coding: utf-8 -*-
# Simp Mock 11 (2025): QA (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_11 import P
import m25_11_figs as F

P.qa(1, "Arjun invested ₹15,625 for 3 years at 20% per annum simple interest. At maturity he received ₹X, borrowed another ₹X from a friend, and invested the whole ₹2X at 20% per annum compound interest. If the total compound interest earned was ₹74,416, for how many years was the money invested?", [], "TITA", "5", ["Arithmetic::Simple_and_Compound_Interest"], "Easy",
 "X = 15,625 × 1.6.",
 steps(("X", p("25,000, so 2X = 50,000.")), ("Years", p(r"\(50000 \times 1.2^n = 124416\): \(1.2^n = 2.48832 = 1.2^5\)."))) + final("5"))

P.qa(2, r"In △ABC, AB = 100 cm, BC = \(100\sqrt3\) cm and ∠ABC = 90°. BD is perpendicular to the hypotenuse AC. Point B₁ on BC is such that DB₁ ⊥ BC. Then B₁D₁ is drawn perpendicular to DC, D₁B₂ perpendicular to BC, and so on forever, along A-D-D₁-D₂-…-C and B-B₁-B₂-…-C." + F.PERP + "Find AB + DB₁ + D₁B₂ + D₂B₃ + …", [], "TITA", "400", ["Geometry::Triangles"], "Hard",
 "∠C = 30°; each step from one vertical segment to the next multiplies by sin²60° = 3/4.",
 steps(("BD", p(r"AC = 200, so \(BD = \tfrac{100 \cdot 100\sqrt3}{200}\) \(= 50\sqrt3\).")),
       ("DB₁", p(r"In △BDC, ∠DBC = 60°: \(DB_1 = BD \sin 60^\circ = 75\). Each later vertical is \(\tfrac34\) of the one before (two 60° projections).")),
       ("Sum", p(r"\(100 + 75 + 56.25 + \dots\) \(= \dfrac{100}{1 - \tfrac34} = 400\)."))) + final("400"))

P.qa(3, r"Find a if \(\log_5\left(1 - \tfrac12\right) + \log_5\left(1 - \tfrac13\right)\) \(+ \log_5\left(1 - \tfrac14\right) + \dots\) \(+ \log_5\left(1 - \tfrac1{125}\right) + a = 0\).", [], "TITA", "3", ["Algebra::Logarithms_and_Exponents"], "Easy",
 "The product telescopes.",
 steps(("Product", p(r"\(\tfrac12 \cdot \tfrac23 \cdots \tfrac{124}{125} = \tfrac1{125}\); \(\log_5 \tfrac1{125} = -3\).")), ("a", p("3."))) + final("3"))

P.qa(4, "A train approaches a tunnel PQ. A rabbit sits inside the tunnel, two-fifths of its length from the entrance P. When the train whistles, the rabbit starts running. If it runs toward P, the train catches it exactly at P; if it runs toward the exit Q, the train catches it exactly at Q. What is the ratio of the train’s speed to the rabbit’s?",
 ["3 : 1", "3 : 2", "5 : 3", "None of these"], "MCQ", "4", ["Arithmetic::Time_Speed_and_Distance"], "Medium",
 "Compare the two cases: the extra tunnel length takes the train as long as the extra 0.2 of it takes the rabbit.",
 steps(("Difference", p(r"Running to Q instead of P, the rabbit covers 0.6L instead of 0.4L (0.2L more) while the train covers L more. So the train is 5 times as fast.")),
       ("Answer", p("5 : 1, not listed."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Ratio of the rabbit’s two runs.")])

P.qa(5, "How many numbers from 1 to 1000 (inclusive) are multiples of some perfect cube greater than 1?", ["167", "168", "182", "194"], "MCQ", "1", ["Number_System::Factors_and_Divisibility"], "Medium",
 "Use prime cubes with inclusion–exclusion.",
 steps(("Single", p("8: 125; 27: 37; 125: 8; 343: 2. Total 172.")),
       ("Overlaps", p("216: 4; 1000: 1. 172 − 5 = 167."))) + final("Option 1"),
 why_rows=[("2", "Off by one."), ("3", "Overcounts."), ("4", "Counts composite cubes separately.")])

P.qa(6, r"For which values of k is \(\dfrac{2x^2 - kx + 9}{x^2 + 4x + 5} > 1\) for every real x?", ["0 < k < 8", "−10 < k < 6", "−8 < k < 0", "−8 < k < 8"], "MCQ", "3", ["Algebra::Inequalities_and_Absolute_Value"], "Medium",
 "The denominator is always positive.",
 steps(("Rearrange", p(r"\(x^2 - (k + 4)x + 4 > 0\) for all x.")), ("Discriminant", p(r"\((k + 4)^2 < 16\): \(-8 < k < 0\)."))) + final("Option 3"),
 why_rows=[("1", "Sign slip."), ("2", "Arithmetic slip."), ("4", "Too wide.")])

P.qa(7, "Manohar bought 50 kg of sugar from a wholesaler for ₹4,600. The wholesaler’s faulty scale showed 1150 g when the actual weight was 1 kg. How much did Manohar lose (in ₹) on this purchase?", [], "TITA", "600", ["Arithmetic::Profit_and_Loss"], "Easy",
 "He actually received 50 ÷ 1.15 kg.",
 steps(("Loss", p(r"\(4600 \times \left(1 - \tfrac1{1.15}\right)\) \(= 4600 \times \tfrac{0.15}{1.15} = 600\)."))) + final("600"))

P.qa(8, "Students are asked to add any 7 distinct positive odd numbers less than 700. How many different sums are possible?", ["2401", "2402", "2501", "2502"], "MCQ", "2", ["Number_System::Miscellaneous"], "Medium",
 "Every odd value between the smallest and largest sum is reachable.",
 steps(("Range", p("Smallest 1 + 3 + … + 13 = 49; largest 687 + … + 699 = 4851. All odd.")),
       ("Count", p(r"\(\tfrac{4851 - 49}2 + 1 = 2402\)."))) + final("Option 2"),
 why_rows=[("1", "Off by one."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(9, "How many trailing zeros does 2000! have when written in base 16?", ["130", "498", "334", "247"], "MCQ", "2", ["Number_System::Factorials"], "Medium",
 "16 = 2⁴: count factors of 2.",
 steps(("Twos", p("1000 + 500 + 250 + 125 + 62 + 31 + 15 + 7 + 3 + 1 = 1994.")), ("Zeros", p(r"\(\lfloor 1994 / 4 \rfloor = 498\)."))) + final("Option 2"),
 why_rows=[("1", "Not the power of 2."), ("3", "Uses 2000 ÷ 6."), ("4", "Uses fives.")])

P.qa(10, F.SQ + p("ABCD is a square and the largest circle passes through its vertices. Each of the four equal smaller circles touches both diagonals AC and BD and one side of the square. The smallest circle touches all four of them. Find the ratio of the area of the largest circle to that of the smallest."),
 [r"\(2(17 + 12\sqrt2) : 1\)", r"\(2(17 - 12\sqrt2) : 1\)", r"\((17 + 12\sqrt2) : 2\)", r"\(4 : (17 - 12\sqrt2)\)"], "MCQ", "1", ["Geometry::Circles"], "Hard",
 "Each small circle is the incircle of a right isosceles triangle formed by two half-diagonals and a side.",
 steps(("Sizes", p(r"Side 2s: big radius \(s\sqrt2\). Incircle of the triangle with legs \(s\sqrt2\) and hypotenuse 2s: \(r = s(\sqrt2 - 1)\), centred \(r\sqrt2\) from the middle.")),
       ("Smallest", p(r"\(r\sqrt2 - r = s(\sqrt2 - 1)^2\).")),
       ("Ratio", p(r"\(\dfrac{2s^2}{s^2(\sqrt2 - 1)^4} = 2(\sqrt2 + 1)^4\) \(= 2(17 + 12\sqrt2)\)."))) + final("Option 1"),
 why_rows=[("2", "Inverts the surd."), ("3", "Off by a factor of 4."), ("4", "Inverts the ratio.")])

P.qa(11, r"What is the remainder when \((13^7 + 14^7)^7\) is divided by 56?", ["13", "27", "1", "55"], "MCQ", "1", ["Number_System::Remainders"], "Medium",
 "56 = 8 × 7.",
 steps(("Inside", p(r"Mod 8: \(5^7 + 6^7 \equiv 5 + 0\). Mod 7: \((-1)^7 + 0 = -1 \equiv 6\). So the inside ≡ 13 (mod 56).")),
       ("Power", p(r"\(13^7\): mod 8 it is 5, mod 7 it is \((-1)^7 \equiv 6\): again 13."))) + final("13, option 1"),
 why_rows=[("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Treats it as −1.")])

P.qa(12, "A photographer has M different photos. She can choose at least two of them for a montage in 32,752 ways. In how many ways can she choose at least five?", ["30657", "30467", "30287", "30827"], "MCQ", "4", ["Modern_Maths::Permutations_and_Combinations"], "Medium",
 "\\(2^M - M - 1 = 32752\\).",
 steps(("M", p(r"\(2^{15} - 16 = 32752\): M = 15.")),
       ("At least five", p(r"\(32768 - (1 + 15 + 105 + 455 + 1365)\) \(= 30827\)."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(13, "Abhishek and Abhimanyu are 1000 m apart. Walking toward each other, they meet in a minutes. If Abhimanyu walks away from Abhishek while Abhishek walks after him, they meet in b minutes. If a : b = 1 : 5, find the ratio of Abhishek’s speed to Abhimanyu’s.", ["5 : 1", "3 : 2", "4 : 3", "2 : 1"], "MCQ", "2", ["Arithmetic::Time_Speed_and_Distance"], "Easy",
 "Closing speeds x + y and x − y.",
 steps(("Ratio", p(r"\(x + y = 5(x - y)\): \(4x = 6y\), x : y = 3 : 2."))) + final("Option 2"),
 why_rows=[("1", "Uses a : b directly."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

P.qa(14, "Two parts of an 80% milk solution are mixed with five parts of an m% milk solution to make an N% solution, where N is an integer with 80 < N ≤ 90. How many integer values can m take?", ["13", "9", "5", "2"], "MCQ", "4", ["Arithmetic::Mixture_and_Alligation"], "Medium",
 "\\(N = \\tfrac{160 + 5m}7\\).",
 steps(("Range", p(r"\(80 < N \le 90\) gives \(80 < m \le 94\).")),
       ("Integer N", p(r"\(160 + 5m \equiv 0 \pmod 7\): \(m \equiv 3 \pmod 7\): 87 and 94."))) + final("2, option 4"),
 why_rows=[("1", "Ignores the integer N."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

P.qa(15, "In a group of 85 students, 8 like neither Mathematics nor English, and 20% like both. If 10 fewer students like only English than like only Mathematics, how many like Mathematics?", [], "TITA", "52", ["Modern_Maths::Set_Theory"], "Easy",
 "77 like at least one; 17 like both.",
 steps(("Only", p("Only M + only E = 60, with a difference of 10: 35 and 25.")), ("Mathematics", p("35 + 17 = 52."))) + final("52"))

P.qa(16, r"How many pairs of integers (a, b) satisfy \(a^2 - b^2 = 2400\) with a > b > 1?", ["9", "10", "11", "12"], "MCQ", "3", ["Number_System::Factors_and_Divisibility"], "Medium",
 "a − b and a + b are both even.",
 steps(("Factor", p(r"a − b = 2u, a + b = 2v with uv = 600 and u < v: 12 pairs (600 has 24 divisors).")),
       ("b > 1", p(r"b = v − u; (24, 25) gives b = 1. Remove it: 11."))) + final("11, option 3"),
 why_rows=[("1", "Removes too many."), ("2", "Removes too many."), ("4", "Keeps b = 1.")])

P.qa(17, r"If the product of the roots of \((p + 2)x^2 + (2p - 1)x + (4p + 3) = 0\) is 3, what is the square of the sum of the roots?", [], "TITA", "1", ["Algebra::Quadratic_Equations"], "Easy",
 "Product = (4p + 3)/(p + 2).",
 steps(("p", p(r"\(4p + 3 = 3p + 6\): p = 3.")), ("Sum", p(r"\(-\tfrac{2p - 1}{p + 2} = -1\); square 1."))) + final("1"))

P.qa(18, "A solid hemisphere of radius 7 cm is scooped out of a solid hemisphere of radius 14 cm, with the flat face of the small one lying on the flat face of the large one. Find the total surface area of what remains. (Take π = 22/7.)", ["824 sq. cm", "1386 sq. cm", "2002 sq. cm", "2310 sq. cm"], "MCQ", "3", ["Geometry::Mensuration"], "Medium",
 "Outer dome + flat ring + inner dome.",
 steps(("Parts", p(r"\(2\pi \cdot 196 + \pi(196 - 49)\) \(+ 2\pi \cdot 49 = 637\pi\).")), ("Value", p("637 × 22/7 = 2002."))) + final("Option 3"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Leaves out the inner dome."), ("4", "Doesn’t remove the small disc.")])

P.qa(19, "A hotel pool can be filled by inlet A alone in 18 hours or by inlet B alone in 24 hours. Both are opened together. When the pool is half full, a fault cuts the flow through both by 25%. How long (in hours) does it take to fill the pool completely?", [], "TITA", "12", ["Arithmetic::Time_and_Work"], "Easy",
 "Together: 7/72 per hour.",
 steps(("First half", p(r"\(\tfrac12 \div \tfrac7{72} = \tfrac{36}7\) h.")), ("Second half", p(r"At 3/4 the rate: \(\tfrac{48}7\) h. Total \(\tfrac{84}7 = 12\)."))) + final("12"))

P.qa(20, "Lines m and n cross lines p and q as shown, and ∠MKR = 130°. Angles w, z and ℓ are marked in the figure." + F.LINES + "If the bisectors of ∠ABC and ∠XYZ are parallel, which statement is NOT correct?",
 ["∠w = 230°", "∠ℓ + ∠ABC = 130°", "line p ∥ line q", "None of these"], "MCQ", "1", ["Geometry::Triangles"], "Hard",
 "Parallel bisectors mean ∠ABC = ∠XYZ, which makes p ∥ q.",
 steps(("p ∥ q", p("Equal angles ABC and XYZ on line m are alternate angles: p ∥ q.")),
       ("ℓ + ∠ABC", p("In △MYK the exterior angle at K is 130° = ∠KMY + ∠KYM. ∠KMY = ℓ (vertically opposite) and ∠KYM = ∠ABC (corresponding). True.")),
       ("w", p("z = 180° − 130° = 50° (p ∥ q), so the reflex angle w = 310°, not 230°."))) + final("Option 1"),
 why_rows=[("2", "True."), ("3", "True."), ("4", "Option 1 is wrong.")])

P.qa(21, "Ravi, Sohan and Tanmay have money in the ratio 3 : 7 : 13. The difference between Tanmay’s and Sohan’s amounts is a multiple of both 6 and 10. If the three together have less than ₹5,000, what is the largest possible total (in ₹)?", [], "TITA", "4945", ["Arithmetic::Ratio_and_Proportion"], "Easy",
 "Difference 6k must be a multiple of 30.",
 steps(("k", p(r"k a multiple of 5; 23k < 5000 gives k ≤ 217: k = 215.")), ("Total", p("23 × 215 = 4945."))) + final("4945"))

P.qa(22, F.TRAP + p("KLMN is an isosceles trapezium and △LMP is equilateral, with P on KN. Q and S are the points where the diagonals of KLMP and of LMPN cross, and R is where KM and LN cross. Find area(KQSN) : area(PQRS)."), ["9 : 2", r"\(5\sqrt3 : 4\)", "15 : 2", "15 : 4"], "MCQ", "4", ["Geometry::Polygons_and_Quadrilaterals"], "Hard",
 "KLMP and LMNP are parallelograms, so KN = 2 LM.",
 steps(("Coordinates", p(r"LM = 2, P(0, 0), L(−1, √3), M(1, √3), K(−2, 0), N(2, 0). Q, S are the midpoints of LP and MP: (∓½, √3/2). R = (0, 2√3/3).")),
       ("Areas", p(r"KQSN: trapezium with bases 4 and 1, height √3/2: \(\tfrac{5\sqrt3}4\). PQRS: kite with diagonals 2√3/3 and 1: \(\tfrac{\sqrt3}3\).")),
       ("Ratio", p("15 : 4."))) + final("Option 4"),
 why_rows=[("1", "Arithmetic slip."), ("2", "Leaves in a surd."), ("3", "Halves PQRS twice.")])
