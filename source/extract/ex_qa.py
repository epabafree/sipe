# -*- coding: utf-8 -*-
# CAT 2023 Slot 1 — QA pilot items. Math in MathJax \( \) / \[ \] (rendered natively by Anki).
QA = []
def q(qno, question, options, qtype, answer, expl, why="", approach="", concept="", topic=(), diff="Medium", note="", hint=""):
    QA.append(dict(section="QA", qno=qno, set_id="", set_title="", directions="", context="",
        question=question, options=options, qtype=qtype, answer=answer, explanation=expl, why_wrong=why,
        approach=approach, concept=concept, hint=hint, topic=["QA::" + t for t in topic], difficulty=diff, source_note=note))

q(1, r"If \(x\) and \(y\) are real numbers such that \(x^2 + (x - 2y - 1)^2 = -4y(x + y)\), then the value \(x - 2y\) is",
  [r"\(1\)", r"\(2\)", r"\(-1\)", r"\(0\)"], "MCQ", "1",
  r"""<p>Move everything to one side:</p>
\[x^2 + 4xy + 4y^2 + (x - 2y - 1)^2 = 0\]
\[(x + 2y)^2 + (x - 2y - 1)^2 = 0\]
<p>A sum of two squares of real numbers is zero only if <b>both</b> are zero:</p>
\[x + 2y = 0 \quad\text{and}\quad x - 2y - 1 = 0 \;\Rightarrow\; x - 2y = 1\]
<p>(Indeed \(x = \tfrac12,\ y = -\tfrac14\) satisfies the equation.)</p>""",
  r"<p>\(2,\ -1,\ 0\) would leave \((x-2y-1)^2 \neq 0\), so the sum of squares could not be zero.</p>",
  r"<p><b>Pattern:</b> whenever an equation has squares on one side and a negative-looking product on the other, move everything across and complete squares. \(\text{(square)} + \text{(square)} = 0\) forces each square to be 0.</p>",
  r"\[a^2 + b^2 = 0,\ a,b \in \mathbb{R} \iff a = b = 0\] \[x^2 + 4xy + 4y^2 = (x+2y)^2\]",
  ["Algebra::Equations_and_Polynomials"], "Easy",
  note="Source states “x – 2y = 1” as following from “x + 2y = 0 <i>or</i> x – 2y – 1 = 0”; both must hold (“and”). Corrected in the explanation.")

q(2, r"Let \(n\) be the least positive integer such that 168 is a factor of \(1134^n\). If \(m\) is the least positive integer such that \(1134^n\) is a factor of \(168^m\), then \(m + n\) equals",
  [r"\(24\)", r"\(12\)", r"\(9\)", r"\(15\)"], "MCQ", "4",
  r"""<p>Prime-factorise both numbers:</p>
\[168 = 2^3 \cdot 3 \cdot 7, \qquad 1134 = 2 \cdot 3^4 \cdot 7\]
<p><b>Finding n:</b> \(1134^n = 2^n \cdot 3^{4n} \cdot 7^n\). For \(2^3 \mid 2^n\) we need \(n \ge 3\) (the powers of 3 and 7 are already enough), so \(n = 3\).</p>
<p><b>Finding m:</b> \(1134^3 = 2^3 \cdot 3^{12} \cdot 7^3\) must divide \(168^m = 2^{3m} \cdot 3^m \cdot 7^m\).</p>
\[3m \ge 3,\quad m \ge 12,\quad m \ge 3 \;\Rightarrow\; m = 12\]
\[m + n = 12 + 3 = 15\]""",
  r"<p>With \(n = 3\), \(m\) must be exactly 12: \(m = 11\) gives only \(3^{11}\), which misses \(3^{12}\). So \(m + n\) is 15, not \(24\), \(12\) or \(9\).</p>",
  r"<p><b>Shortcut:</b> for “least power so that A divides Bⁿ”, check each prime: \(n = \max\big\lceil \tfrac{\text{exponent in A}}{\text{exponent in B}} \big\rceil\).</p>",
  r"\[a \mid b \iff \text{every prime exponent of } a \le \text{that of } b\]",
  ["Number_System::Factors_and_Divisibility"], "Easy")

q(3, r"If \(\sqrt{5x+9} + \sqrt{5x-9} = 3\left(2 + \sqrt{2}\right)\), then \(\sqrt{10x+9}\)",
  [r"\(3\sqrt{31}\)", r"\(2\sqrt{7}\)", r"\(3\sqrt{7}\)", r"\(4\sqrt{5}\)"], "MCQ", "3",
  r"""<p>Let \(a = \sqrt{5x+9}\) and \(b = \sqrt{5x-9}\). Then</p>
\[a + b = 6 + 3\sqrt2, \qquad a^2 - b^2 = (5x+9) - (5x-9) = 18\]
\[a - b = \frac{18}{6 + 3\sqrt2} = \frac{6}{2+\sqrt2} = \frac{6(2-\sqrt2)}{2} = 6 - 3\sqrt2\]
<p>Adding: \(2a = 12 \Rightarrow a = 6\), so \(5x + 9 = 36 \Rightarrow 5x = 27\).</p>
\[\sqrt{10x + 9} = \sqrt{54 + 9} = \sqrt{63} = 3\sqrt7\]""",
  r"<p>Check: \(b = 3\sqrt2\), so \(b^2 = 18 = 5x - 9\) ✓. The other options do not equal \(\sqrt{63}\).</p>",
  r"<p><b>Shortcut:</b> match the right side as \(6 + 3\sqrt2 = \sqrt{36} + \sqrt{18}\). Then \(5x + 9 = 36\) and \(5x - 9 = 18\) both give \(5x = 27\) — done in one line.</p>",
  r"\[(\sqrt p + \sqrt q)(\sqrt p - \sqrt q) = p - q\]",
  ["Algebra::Surds_and_Indices"], "Medium",
  note="The question line ends without a verb in the source print (“then √(10x+9)”); kept as printed — read it as “equals”.")

q(4, r"If \(x\) and \(y\) are positive real numbers such that \(\log_x\left(x^2 + 12\right) = 4\) and \(3\log_y x = 1\), then \(x + y\) equals",
  [r"\(10\)", r"\(68\)", r"\(20\)", r"\(11\)"], "MCQ", "1",
  r"""\[\log_x(x^2+12) = 4 \;\Rightarrow\; x^4 = x^2 + 12 \;\Rightarrow\; (x^2 - 4)(x^2 + 3) = 0 \;\Rightarrow\; x = 2\]
\[3\log_y x = 1 \;\Rightarrow\; \log_y 2 = \tfrac13 \;\Rightarrow\; y^{1/3} = 2 \;\Rightarrow\; y = 8\]
\[x + y = 2 + 8 = 10\]""",
  r"<p>Only \(x = 2,\ y = 8\) satisfies both equations: \(\log_2 16 = 4\) ✓ and \(3\log_8 2 = 3\cdot\tfrac13 = 1\) ✓. No other pair gives \(68\), \(20\) or \(11\).</p>",
  r"<p>Treat \(x^4 = x^2 + 12\) as a quadratic in \(x^2\). The base must be positive and \(\ne 1\), so \(x = 2\) is the only valid root.</p>",
  r"\[\log_b a = c \iff b^c = a\]",
  ["Algebra::Logarithms_and_Exponents"], "Easy")

q(7, r"Let \(\alpha\) and \(\beta\) be the two distinct roots of the equation \(2x^2 - 6x + k = 0\), such that \((\alpha + \beta)\) and \(\alpha\beta\) are the distinct roots of the equation \(x^2 + px + p = 0\). Then the value of \(8(k - p)\) is",
  [], "TITA", "6",
  r"""<p>From \(2x^2 - 6x + k = 0\):</p>
\[\alpha + \beta = 3, \qquad \alpha\beta = \frac{k}{2}\]
<p>So \(3\) and \(\tfrac{k}{2}\) are the roots of \(x^2 + px + p = 0\):</p>
\[3 + \frac{k}{2} = -p \quad\text{(sum)}, \qquad 3\cdot\frac{k}{2} = p \quad\text{(product)}\]
\[3 + \frac{k}{2} = -\frac{3k}{2} \;\Rightarrow\; 3 = -2k \;\Rightarrow\; k = -\frac32, \quad p = -\frac94\]
\[8(k - p) = 8\left(-\frac32 + \frac94\right) = 8 \cdot \frac34 = 6\]
<p>Check: \(2x^2 - 6x - \tfrac32\) has discriminant \(36 + 12 > 0\), so its roots are distinct ✓. The values \(3\) and \(-\tfrac34\) are distinct ✓.</p>""",
  "",
  r"<p><b>Shortcut:</b> because \(x^2 + px + p\) has its sum and product of roots in a fixed relation (sum \(= -\)product), you get \(3 + \tfrac{k}{2} = -\tfrac{3k}{2}\) at once.</p>",
  r"\[ax^2 + bx + c = 0:\quad \text{sum} = -\frac{b}{a},\quad \text{product} = \frac{c}{a}\]",
  ["Algebra::Quadratic_Equations"], "Medium",
  note="Source working swaps the values (prints k = −9/4, p = −3/2, which would give −6). Corrected: k = −3/2, p = −9/4; the final answer of 6 matches the key.")

q(9, r"The salaries of three friends Sita, Gita and Mita are initially in the ratio \(5 : 6 : 7\), respectively. In the first year, they get salary hikes of 20%, 25% and 20%, respectively. In the second year, Sita and Mita get salary hikes of 40% and 25%, respectively, and the salary of Gita becomes equal to the mean salary of the three friends. The salary hike of Gita in the second year is",
  [r"26%", r"30%", r"28%", r"25%"], "MCQ", "1",
  r"""<p>Take the initial salaries as \(5x,\ 6x,\ 7x\).</p>
<div class="tbl"><table><tr><th></th><th>Start</th><th>After year 1</th><th>After year 2</th></tr>
<tr><td class="rh">Sita</td><td>\(5x\)</td><td>\(6x\)</td><td>\(8.4x\)</td></tr>
<tr><td class="rh">Gita</td><td>\(6x\)</td><td>\(7.5x\)</td><td>\(g\)</td></tr>
<tr><td class="rh">Mita</td><td>\(7x\)</td><td>\(8.4x\)</td><td>\(10.5x\)</td></tr></table></div>
<p>Gita’s salary equals the mean of all three:</p>
\[g = \frac{8.4x + g + 10.5x}{3} \;\Rightarrow\; 2g = 18.9x \;\Rightarrow\; g = 9.45x\]
\[\text{Hike} = \frac{9.45x - 7.5x}{7.5x} \times 100\% = \frac{1.95}{7.5}\times 100\% = 26\%\]""",
  r"<p>The hike is measured from Gita’s salary after year 1 (\(7.5x\)), not her starting \(6x\). Measured correctly it is exactly 26%, so 30%, 28% and 25% are all wrong.</p>",
  r"<p><b>Shortcut:</b> if one person equals the mean of three, they also equal the mean of the <i>other two</i>: \(g = \tfrac{8.4x + 10.5x}{2} = 9.45x\).</p>",
  r"\[x = \tfrac{a+b+x}{3} \iff x = \tfrac{a+b}{2}\]",
  ["Arithmetic::Percentages"], "Easy")

q(10, r"The minor angle between the hour hand and minute hand of a clock was observed at 8:48 am. The minimum duration, in minutes, after 8:48 am when this angle increase by 50% is",
  [r"\(\dfrac{24}{11}\)", r"\(\dfrac{36}{11}\)", r"\(4\)", r"\(2\)"], "MCQ", "1",
  r"""<p>At 8:48 the hour hand is at \(8 \times 30 + 48 \times 0.5 = 264^\circ\) and the minute hand at \(48 \times 6 = 288^\circ\). The minor angle is \(24^\circ\).</p>
<p>A 50% increase means the angle must reach \(36^\circ\). The minute hand is ahead and gains \(5.5^\circ\) per minute, so the angle grows at once:</p>
\[24 + 5.5t = 36 \;\Rightarrow\; t = \frac{12}{5.5} = \frac{24}{11}\ \text{minutes}\]""",
  r"<p>\(\tfrac{36}{11}\) is the time to cover \(18^\circ\) (a 75% increase); \(4\) and \(2\) are rounded guesses.</p>",
  "",
  r"\[\theta = \left|30H - 5.5M\right|, \qquad \text{relative speed} = 5.5^\circ/\text{min}\]",
  ["Arithmetic::Clocks_and_Calendars"], "Medium")

q(14, r"Anil invests ₹ 22000 for 6 years in a certain scheme with 4% interest per annum, compounded half-yearly. Sunil invests in the same scheme for 5 years, and then reinvests the entire amount received at the end of 5 years for one year at 10% simple interest. If the amounts received by both at the end of 6 years are same, then the initial investment made by Sunil, in rupees, is",
  [], "TITA", "20808",
  r"""<p>Half-yearly rate = 2%. Anil compounds for 12 half-years; Sunil compounds for 10 half-years and then earns 10% simple interest for one year.</p>
\[22000\,(1.02)^{12} = P\,(1.02)^{10} \times 1.10\]
\[P = \frac{22000 \times (1.02)^2}{1.1} = 20000 \times 1.0404 = 20808\]
<p>Sunil invested <b>₹ 20,808</b>.</p>""",
  "",
  r"<p><b>Shortcut:</b> cancel the common \((1.02)^{10}\) before computing anything — then it is a two-line calculation.</p>",
  r"\[A = P\left(1 + \frac{r}{200}\right)^{2t}\ \text{(half-yearly)}, \qquad A_{SI} = P(1 + rt)\]",
  ["Arithmetic::Simple_and_Compound_Interest"], "Easy")

q(17, r"A quadrilateral ABCD is inscribed in a circle such that \(AB : CD = 2 : 1\) and \(BC : AD = 5 : 4\). If AC and BD intersect at the point E, then \(AE : CE\) equals",
  [r"\(2 : 1\)", r"\(1 : 2\)", r"\(8 : 5\)", r"\(5 : 8\)"], "MCQ", "3",
  r"""<p class="fig"><img src="catpyq_2023S1_QA17.svg" alt="Cyclic quadrilateral ABCD with diagonals meeting at E"></p>
<p>In a cyclic quadrilateral, the diagonals create two pairs of similar triangles (angles in the same segment are equal).</p>
<p><b>△AEB ~ △DEC</b> (∠ABE = ∠DCE and ∠BAE = ∠CDE):</p>
\[\frac{AE}{DE} = \frac{BE}{CE} = \frac{AB}{DC} = 2\]
<p><b>△AED ~ △BEC</b>:</p>
\[\frac{AE}{BE} = \frac{ED}{EC} = \frac{AD}{BC} = \frac45\]
<p>Multiply the two ratios to get AE : CE:</p>
\[\frac{AE}{CE} = \frac{AE}{BE} \cdot \frac{BE}{CE} = \frac45 \times 2 = \frac85\]""",
  r"<p>\(2 : 1\) uses only the first similarity; \(5 : 8\) inverts the answer; \(1 : 2\) inverts the side ratio.</p>",
  r"<p><b>Formula to remember:</b> for a cyclic quadrilateral, \(\dfrac{AE}{EC} = \dfrac{AB \cdot AD}{CB \cdot CD} = \dfrac{2 \cdot 4}{5 \cdot 1} = \dfrac85\).</p>",
  r"\[\frac{AE}{EC} = \frac{AB\cdot AD}{CB\cdot CD}\quad\text{(cyclic quadrilateral)}\]",
  ["Geometry::Circles", "Geometry::Quadrilaterals"], "Medium")

q(18, r"Let C be the circle \(x^2 + y^2 + 4x - 6y - 3 = 0\) and L be the locus of the point of intersection of a pair of tangents to C with the angle between the two tangents equal to \(60^\circ\). Then, the point at which L touches the line \(x = 6\) is",
  [r"\((6, 6)\)", r"\((6, 4)\)", r"\((6, 8)\)", r"\((6, 3)\)"], "MCQ", "4",
  r"""<p>Complete the squares:</p>
\[(x+2)^2 + (y-3)^2 = 16 \;\Rightarrow\; \text{centre } O(-2, 3),\ r = 4\]
<p>From an external point P, the two tangents make \(30^\circ\) each with PO, so</p>
\[\sin 30^\circ = \frac{r}{PO} \;\Rightarrow\; PO = 2r = 8\]
<p>The locus L is the circle \((x+2)^2 + (y-3)^2 = 64\). It touches the vertical line \(x = 6\) where \(x + 2 = 8\) and \(y\) equals the centre’s \(y\):</p>
\[\text{Point of contact} = (6,\ 3)\]""",
  r"<p>Any other point on \(x = 6\), e.g. \((6, 6)\), is at distance \(\sqrt{64 + 9} > 8\) from the centre, so it is not on L.</p>",
  r"<p><b>Shortcut:</b> a vertical tangent to a circle always touches it at the centre’s y-coordinate — so the answer must be \((6, 3)\) once you know the centre.</p>",
  r"\[\text{Angle between tangents } 2\theta \Rightarrow PO = \frac{r}{\sin\theta}\]",
  ["Geometry::Coordinate_Geometry", "Geometry::Circles"], "Medium")

q(19, r"In a right-angled triangle \(\triangle ABC\), the altitude AB is 5 cm, and the base BC is 12 cm. P and Q are two points on BC such that the areas of \(\triangle ABP\), \(\triangle ABQ\) and \(\triangle ABC\) are in arithmetic progression. If the area of \(\triangle ABC\) is 1.5 times the area of \(\triangle ABP\), the length of PQ, in cm, is",
  [], "TITA", "2",
  r"""<p class="fig"><img src="catpyq_2023S1_QA19.svg" alt="Right triangle ABC with right angle at B and points P, Q on BC"></p>
<p>All three triangles have the same height AB = 5, so their areas are proportional to their bases on BC.</p>
\[[ABC] = \tfrac12 \cdot 5 \cdot 12 = 30, \qquad [ABP] = \frac{30}{1.5} = 20\]
<p>AP of areas: \(20,\ [ABQ],\ 30 \Rightarrow [ABQ] = 25\).</p>
\[\tfrac12 \cdot 5 \cdot BP = 20 \Rightarrow BP = 8, \qquad \tfrac12 \cdot 5 \cdot BQ = 25 \Rightarrow BQ = 10\]
\[PQ = BQ - BP = 10 - 8 = 2\ \text{cm}\]""",
  "",
  r"<p><b>Shortcut:</b> same height ⇒ the bases form the same AP as the areas: \(BP, BQ, 12\) are in AP and \(BP = 12/1.5 = 8\), so \(BQ = 10\) and \(PQ = 2\).</p>",
  r"\[\text{Area} = \tfrac12 \times \text{base} \times \text{height}\]",
  ["Geometry::Triangles"], "Medium")

q(20, r"""For some positive and distinct real numbers \(x\), \(y\) and \(z\), if \(\dfrac{1}{\sqrt{y}+\sqrt{z}}\) is the arithmetic mean of \(\dfrac{1}{\sqrt{x}+\sqrt{z}}\) and \(\dfrac{1}{\sqrt{x}+\sqrt{y}}\), then the relationship which will always hold true, is""",
  [r"\(x\), \(y\) and \(z\) are in arithmetic progression",
   r"\(\sqrt{x}\), \(\sqrt{y}\) and \(\sqrt{z}\) are in arithmetic progression",
   r"\(y\), \(x\) and \(z\) are in arithmetic progression",
   r"\(\sqrt{x}\), \(\sqrt{z}\) and \(\sqrt{y}\) are in arithmetic progression"], "MCQ", "3",
  r"""<p>Write \(a = \sqrt x,\ b = \sqrt y,\ c = \sqrt z\). The condition is</p>
\[\frac{2}{b + c} = \frac{1}{a + c} + \frac{1}{a + b} = \frac{2a + b + c}{(a+c)(a+b)}\]
\[2(a+c)(a+b) = (b+c)(2a+b+c)\]
\[2a^2 + 2ab + 2ac + 2bc = 2ab + 2ac + b^2 + 2bc + c^2\]
\[2a^2 = b^2 + c^2 \;\Rightarrow\; 2x = y + z\]
<p>So \(x\) is the arithmetic mean of \(y\) and \(z\): <b>\(y, x, z\) are in AP</b>.</p>
<p>Check with numbers: \(y = 1, x = 4, z = 7\). LHS \(= \tfrac{1}{1+\sqrt7} \approx 0.2743\); RHS \(= \tfrac12\left(\tfrac{1}{2+\sqrt7} + \tfrac13\right) \approx 0.2743\) ✓.</p>""",
  r"<p>Options 1, 2 and 4 each need a different middle term or the square roots in AP. The algebra gives \(2x = y + z\) only, and the example \(y=1, x=4, z=7\) satisfies the condition while breaking options 1, 2 and 4.</p>",
  r"<p><b>Shortcut (rationalise):</b> \(\tfrac{1}{\sqrt p + \sqrt q} = \tfrac{\sqrt p - \sqrt q}{p - q}\). Or just test a simple AP such as \(y, x, z = 1, 4, 7\) in each option — only option 3 survives.</p>",
  r"\[a, b, c \text{ in AP} \iff 2b = a + c\]",
  ["Algebra::Progressions_and_Series", "Algebra::Surds_and_Indices"], "Hard")

q(22, r"A lab experiment measures the number of organisms at 8 am every day. Starting with 2 organisms on the first day, the number of organisms on any day is equal to 3 more than twice the number on the previous day. If the number of organisms on the \(n^{\text{th}}\) day exceeds one million, then the lowest possible value of \(n\) is",
  [], "TITA", "19",
  r"""<p>The rule is \(a_1 = 2,\ a_n = 2a_{n-1} + 3\). Add 3 to both sides:</p>
\[a_n + 3 = 2(a_{n-1} + 3) \;\Rightarrow\; a_n + 3 = 5 \cdot 2^{n-1} \;\Rightarrow\; a_n = 5\cdot 2^{n-1} - 3\]
<p>(Check: 2, 7, 17, 37, … ✓)</p>
\[5 \cdot 2^{n-1} - 3 > 10^6 \;\Rightarrow\; 2^{n-1} > 200000.6\]
<p>\(2^{17} = 131072\) is too small and \(2^{18} = 262144\) works, so \(n - 1 = 18\), giving \(n = 19\).</p>
<p>\(a_{18} = 655357\) (below a million), \(a_{19} = 1310717\) (above) ✓.</p>""",
  "",
  r"<p><b>Pattern:</b> for \(a_n = r\,a_{n-1} + d\), add \(\tfrac{d}{r-1}\) to turn it into a GP. Here \(\tfrac{3}{2-1} = 3\).</p>",
  r"\[a_n = r a_{n-1} + d \Rightarrow a_n + \tfrac{d}{r-1} = \left(a_1 + \tfrac{d}{r-1}\right) r^{n-1}\]",
  ["Algebra::Progressions_and_Series"], "Medium",
  note="Source working sets up a running sum S = 2 + 7 + 17 + … instead of the nth-day count; it reaches the right answer (19) by an unclear route. The explanation has been rewritten.")
