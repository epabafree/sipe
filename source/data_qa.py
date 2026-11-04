# -*- coding: utf-8 -*-
# QA — CAT 2023 Slot 1 pilot. Question/option text reused verbatim from the extraction.
from fmt import steps, final, why, table, p

SOL = {}

SOL[1] = dict(
 hint=p(r"Move the right side across. Can \(x^2 + 4xy + 4y^2\) be written as a square?"),
 solution=steps(
  ("Bring everything to one side", r"\[\begin{aligned} x^2 + (x-2y-1)^2 &= -4xy - 4y^2 \\ x^2 + 4xy + 4y^2 + (x-2y-1)^2 &= 0 \\ (x+2y)^2 + (x-2y-1)^2 &= 0 \end{aligned}\]"),
  ("Use the sum-of-squares rule", p(r"Two real squares add up to \(0\) only if <b>both</b> are \(0\):") + r"\[x + 2y = 0 \quad\text{and}\quad x - 2y - 1 = 0\]"),
  ("Read off the answer", r"\[x - 2y = 1\]" + p(r"Check: \(x = \tfrac12,\ y = -\tfrac14\) satisfies the original equation.")),
 ) + final(r"\(x - 2y = 1\) — option 1"),
 shortcut=p(r"Seeing a “negative” product such as \(-4y(x+y)\) next to squares is a signal: move it across and complete a square."),
 concept=r"\[a^2 + b^2 = 0,\ \ a, b \in \mathbb{R} \iff a = b = 0\]\[x^2 + 4xy + 4y^2 = (x + 2y)^2\]",
 why=why([(o, r"Any value other than \(1\) leaves \((x - 2y - 1)^2 > 0\), so the sum of squares can’t be \(0\).") for o in ("2", "3", "4")]))

SOL[2] = dict(
 hint=p(r"Factorise both numbers into primes: \(168 = 2^3 \cdot 3 \cdot 7\)."),
 solution=steps(
  ("Prime-factorise", r"\[168 = 2^3 \cdot 3 \cdot 7, \qquad 1134 = 2 \cdot 3^4 \cdot 7\]"),
  ("Find n", p(r"\(1134^n = 2^n \cdot 3^{4n} \cdot 7^n\). The powers of \(3\) and \(7\) are already enough; for \(2^3\) we need \(n \ge 3\).") + r"\[n = 3\]"),
  ("Find m", p(r"\(1134^3 = 2^3 \cdot 3^{12} \cdot 7^3\) must divide \(168^m = 2^{3m} \cdot 3^m \cdot 7^m\):") +
     r"\[3m \ge 3, \qquad m \ge 12, \qquad m \ge 3 \;\Rightarrow\; m = 12\]"),
 ) + final(r"\(m + n = 12 + 3 = 15\) — option 4"),
 shortcut=p(r"For “least power so that \(A\) divides \(B^n\)”, check each prime: \(n = \max \left\lceil \dfrac{\text{exponent in } A}{\text{exponent in } B} \right\rceil\)."),
 concept=r"\[a \mid b \iff \text{each prime’s exponent in } a \le \text{its exponent in } b\]",
 why=why([("1", r"\(24\) would need \(m = 21\), but \(m = 12\) already works."), ("2", r"\(12\) is \(m\) alone; you still have to add \(n = 3\)."), ("3", r"\(9\) would need \(m = 6\), but \(168^6\) has only \(3^6\), far short of \(3^{12}\).")]))

SOL[3] = dict(
 hint=p(r"Call the two roots \(a\) and \(b\). You know \(a + b\), and \(a^2 - b^2\) is easy to compute."),
 solution=steps(
  ("Name the roots", p(r"Let \(a = \sqrt{5x+9}\) and \(b = \sqrt{5x-9}\).") + r"\[a + b = 6 + 3\sqrt2\]\[a^2 - b^2 = (5x+9) - (5x-9) = 18\]"),
  ("Find a − b", r"\[\begin{aligned} a - b &= \frac{18}{6 + 3\sqrt2} = \frac{6}{2 + \sqrt2} \\ &= \frac{6(2 - \sqrt2)}{2} = 6 - 3\sqrt2 \end{aligned}\]"),
  ("Solve for x", p(r"Adding the two equations: \(2a = 12\), so \(a = 6\).") + r"\[5x + 9 = 36 \;\Rightarrow\; 5x = 27 \;\Rightarrow\; 10x = 54\]"),
  ("Evaluate", r"\[\sqrt{10x + 9} = \sqrt{63} = 3\sqrt7\]"),
 ) + final(r"\(3\sqrt7\) — option 3"),
 shortcut=p(r"Read the right side as \(6 + 3\sqrt2 = \sqrt{36} + \sqrt{18}\). Then \(5x + 9 = 36\) and \(5x - 9 = 18\) both give \(5x = 27\), in one line."),
 concept=r"\[(\sqrt p + \sqrt q)(\sqrt p - \sqrt q) = p - q\]",
 why=why([("1", r"\(3\sqrt{31} = \sqrt{279}\), not \(\sqrt{63}\)."), ("2", r"\(2\sqrt7 = \sqrt{28}\), not \(\sqrt{63}\)."), ("4", r"\(4\sqrt5 = \sqrt{80}\), not \(\sqrt{63}\).")]))

SOL[4] = dict(
 hint=p(r"Rewrite \(\log_x(x^2+12) = 4\) without logs: \(x^4 = x^2 + 12\)."),
 solution=steps(
  ("Remove the first log", r"\[x^4 = x^2 + 12 \;\Rightarrow\; (x^2 - 4)(x^2 + 3) = 0 \;\Rightarrow\; x = 2\]" + p(r"The base must be positive and not \(1\), so \(x = 2\) is the only option.")),
  ("Remove the second log", r"\[3\log_y 2 = 1 \;\Rightarrow\; \log_y 2 = \tfrac13 \;\Rightarrow\; y^{1/3} = 2 \;\Rightarrow\; y = 8\]"),
 ) + final(r"\(x + y = 2 + 8 = 10\) — option 1"),
 shortcut=p(r"Treat \(x^4 = x^2 + 12\) as a quadratic in \(x^2\): two numbers that multiply to \(-12\) and differ by \(1\) are \(4\) and \(-3\)."),
 concept=r"\[\log_b a = c \iff b^c = a\]",
 why=why([(o, r"Only \(x = 2,\ y = 8\) satisfies both equations: \(\log_2 16 = 4\) ✓ and \(3\log_8 2 = 1\) ✓.") for o in ("2", "3", "4")]))

SOL[7] = dict(
 hint=p(r"From \(2x^2 - 6x + k = 0\): \(\alpha + \beta = 3\) and \(\alpha\beta = \tfrac{k}{2}\). These two numbers are the roots of the second equation."),
 solution=steps(
  ("Sum and product of the first equation", r"\[\alpha + \beta = 3, \qquad \alpha\beta = \frac{k}{2}\]"),
  ("Apply the second equation", p(r"\(3\) and \(\tfrac{k}{2}\) are the roots of \(x^2 + px + p = 0\):") +
     r"\[\begin{aligned} 3 + \frac{k}{2} &= -p && \text{(sum)} \\ 3 \cdot \frac{k}{2} &= p && \text{(product)} \end{aligned}\]"),
  ("Solve", r"\[\begin{aligned} 3 + \frac{k}{2} &= -\frac{3k}{2} \\ 3 &= -2k \\ k &= -\frac32, \quad p = -\frac94 \end{aligned}\]"),
  ("Evaluate", r"\[8(k - p) = 8\left(-\frac32 + \frac94\right) = 8 \cdot \frac34 = 6\]" +
     p(r"Check: the discriminant of \(2x^2 - 6x - \tfrac32\) is \(36 + 12 > 0\), so the roots are distinct ✓.")),
 ) + final(r"\(6\)"),
 shortcut=p(r"In \(x^2 + px + p\), sum \(= -\)product, so \(3 + \tfrac{k}{2} = -\tfrac{3k}{2}\) straight away."),
 concept=r"\[ax^2 + bx + c = 0:\qquad \text{sum} = -\frac{b}{a}, \qquad \text{product} = \frac{c}{a}\]")

SOL[9] = dict(
 hint=p(r"Use \(5x, 6x, 7x\) and apply each year’s hikes. If Gita equals the mean of all three, she also equals the mean of the other two."),
 solution=steps(
  ("Track the salaries", table(["", "Start", "After year 1", "After year 2"], [
      ["Sita", r"\(5x\)", r"\(6x\)", r"\(8.4x\)"], ["Gita", r"\(6x\)", r"\(7.5x\)", r"\(g\)"], ["Mita", r"\(7x\)", r"\(8.4x\)", r"\(10.5x\)"]])),
  ("Use the mean condition", r"\[g = \frac{8.4x + g + 10.5x}{3} \;\Rightarrow\; 2g = 18.9x \;\Rightarrow\; g = 9.45x\]"),
  ("Compute the hike", r"\[\frac{9.45x - 7.5x}{7.5x} \times 100\% = \frac{1.95}{7.5} \times 100\% = 26\%\]"),
 ) + final(r"\(26\%\) — option 1"),
 shortcut=p(r"If one value equals the mean of three, it equals the mean of the other two: \(g = \tfrac{8.4x + 10.5x}{2} = 9.45x\)."),
 concept=r"\[x = \frac{a + b + x}{3} \iff x = \frac{a + b}{2}\]",
 why=why([(o, r"The hike is measured from Gita’s year-1 salary \(7.5x\), and comes to exactly \(26\%\).") for o in ("2", "3", "4")]))

SOL[10] = dict(
 hint=p(r"At 8:48 the angle is \(24^\circ\). It must grow to \(36^\circ\), and the gap changes by \(5.5^\circ\) every minute."),
 solution=steps(
  ("Angle at 8:48", r"\[\text{hour hand} = 8 \times 30 + 48 \times 0.5 = 264^\circ\]\[\text{minute hand} = 48 \times 6 = 288^\circ\]" + p(r"Minor angle \(= 24^\circ\).")),
  ("Target angle", p(r"A \(50\%\) increase: \(24 \times 1.5 = 36^\circ\).")),
  ("Time needed", p(r"The minute hand is ahead and gains \(5.5^\circ\) per minute, so the angle grows immediately:") +
     r"\[24 + 5.5t = 36 \;\Rightarrow\; t = \frac{12}{5.5} = \frac{24}{11}\ \text{min}\]"),
 ) + final(r"\(\dfrac{24}{11}\) minutes — option 1"),
 concept=r"\[\theta = \left|30H - 5.5M\right|, \qquad \text{relative speed} = 5.5^\circ/\text{min}\]",
 why=why([("2", r"\(\tfrac{36}{11}\) min adds \(18^\circ\): a \(75\%\) increase."), ("3", r"\(4\) min adds \(22^\circ\)."), ("4", r"\(2\) min adds \(11^\circ\): only \(35^\circ\).")]))

SOL[14] = dict(
 hint=p(r"Write both final amounts with the half-yearly rate \(2\%\) and set them equal; most of the powers cancel."),
 solution=steps(
  ("Set up both amounts", p(r"Half-yearly rate \(= 2\%\). Anil compounds for \(12\) half-years. Sunil compounds for \(10\) half-years, then earns \(10\%\) simple interest for one year.") +
     r"\[22000\,(1.02)^{12} = P\,(1.02)^{10} \times 1.1\]"),
  ("Cancel and solve", r"\[P = \frac{22000 \times (1.02)^2}{1.1} = 20000 \times 1.0404 = 20808\]"),
 ) + final(r"\(₹\,20{,}808\)"),
 shortcut=p(r"Cancel the shared \((1.02)^{10}\) before computing anything."),
 concept=r"\[A = P\left(1 + \frac{r}{200}\right)^{2t}\ \text{(half-yearly)}, \qquad A = P(1 + rt)\ \text{(simple interest)}\]")

SOL[17] = dict(
 hint=p("The diagonals of a cyclic quadrilateral create two pairs of similar triangles. Use both."),
 solution=steps(
  ("Draw it", '<p class="fig"><img src="sipe_2023S1_QA17.svg" alt="Cyclic quadrilateral ABCD with diagonals meeting at E"></p>'),
  ("First similar pair", p(r"\(\triangle AEB \sim \triangle DEC\) (angles in the same segment):") + r"\[\frac{AE}{DE} = \frac{BE}{CE} = \frac{AB}{DC} = 2\]"),
  ("Second similar pair", p(r"\(\triangle AED \sim \triangle BEC\):") + r"\[\frac{AE}{BE} = \frac{ED}{EC} = \frac{AD}{BC} = \frac45\]"),
  ("Chain the ratios", r"\[\frac{AE}{CE} = \frac{AE}{BE} \cdot \frac{BE}{CE} = \frac45 \times 2 = \frac85\]"),
 ) + final(r"\(AE : CE = 8 : 5\) — option 3"),
 shortcut=p(r"Remember the result directly: \(\dfrac{AE}{EC} = \dfrac{AB \cdot AD}{CB \cdot CD} = \dfrac{2 \cdot 4}{5 \cdot 1} = \dfrac85\)."),
 concept=r"\[\frac{AE}{EC} = \frac{AB \cdot AD}{CB \cdot CD}\quad\text{(cyclic quadrilateral, diagonals meet at } E)\]",
 why=why([("1", r"\(2 : 1\) uses only the first similar pair."), ("2", r"\(1 : 2\) inverts the side ratio \(AB : CD\)."), ("4", r"\(5 : 8\) is the answer upside down.")]))

SOL[18] = dict(
 hint=p("Find the circle’s centre and radius. Then work out how far a point must be from the centre for its two tangents to meet at 60°."),
 solution=steps(
  ("Centre and radius", r"\[(x+2)^2 + (y-3)^2 = 16 \;\Rightarrow\; O(-2,\,3),\quad r = 4\]"),
  ("Distance of the intersection point", p(r"Each tangent makes \(30^\circ\) with \(PO\):") + r"\[\sin 30^\circ = \frac{r}{PO} \;\Rightarrow\; PO = 2r = 8\]"),
  ("The locus and its contact point", p(r"L is the circle \((x+2)^2 + (y-3)^2 = 64\). A vertical line touches it at the centre’s height, where \(x + 2 = 8\):") + r"\[(6,\ 3)\]"),
 ) + final(r"\((6, 3)\) — option 4"),
 shortcut=p(r"A vertical tangent always touches a circle at the centre’s \(y\)-coordinate. Once you know the centre is \((-2, 3)\), the answer must be \((6, 3)\)."),
 concept=r"\[\text{Angle between tangents} = 2\theta \;\Rightarrow\; PO = \frac{r}{\sin\theta}\]",
 why=why([(o, rf"\({pt}\) is at distance \(\sqrt{{64 + {d}}} > 8\) from the centre, so it isn’t on L.") for o, pt, d in (("1", "(6, 6)", "9"), ("2", "(6, 4)", "1"), ("3", "(6, 8)", "25"))]))

SOL[19] = dict(
 hint=p(r"All three triangles share the height \(AB = 5\), so their areas are proportional to their bases on \(BC\)."),
 solution=steps(
  ("Draw it", '<p class="fig"><img src="sipe_2023S1_QA19.svg" alt="Right triangle ABC with points P and Q on BC"></p>'),
  ("Areas", r"\[[ABC] = \tfrac12 \cdot 5 \cdot 12 = 30\]\[[ABP] = \frac{30}{1.5} = 20\]" + p(r"AP: \(20,\ [ABQ],\ 30\) ⇒ \([ABQ] = 25\).")),
  ("Bases", r"\[\tfrac12 \cdot 5 \cdot BP = 20 \;\Rightarrow\; BP = 8\]\[\tfrac12 \cdot 5 \cdot BQ = 25 \;\Rightarrow\; BQ = 10\]"),
 ) + final(r"\(PQ = 10 - 8 = 2\) cm"),
 shortcut=p(r"Same height ⇒ the bases form the same AP as the areas: \(BP = 12 / 1.5 = 8\), so \(8, BQ, 12\) gives \(BQ = 10\)."),
 concept=r"\[\text{Area} = \tfrac12 \times \text{base} \times \text{height}; \quad \text{same height} \Rightarrow \text{area} \propto \text{base}\]")

SOL[20] = dict(
 hint=p(r"Substitute \(a = \sqrt x,\ b = \sqrt y,\ c = \sqrt z\), combine the two fractions on the right, and cross-multiply."),
 solution=steps(
  ("Substitute", p(r"Let \(a = \sqrt x,\ b = \sqrt y,\ c = \sqrt z\). The condition is") + r"\[\frac{2}{b + c} = \frac{1}{a + c} + \frac{1}{a + b} = \frac{2a + b + c}{(a+c)(a+b)}\]"),
  ("Cross-multiply and simplify", r"\[\begin{aligned} 2(a+c)(a+b) &= (b+c)(2a+b+c) \\ 2a^2 + 2ab + 2ac + 2bc &= 2ab + 2ac + b^2 + 2bc + c^2 \\ 2a^2 &= b^2 + c^2 \end{aligned}\]"),
  ("Translate back", r"\[2x = y + z\]" + p(r"So \(x\) is the arithmetic mean of \(y\) and \(z\).")),
  ("Check with numbers", p(r"\(y = 1,\ x = 4,\ z = 7\): left side \(\approx 0.2743\), right side \(\approx 0.2743\) ✓")),
 ) + final(r"\(y, x, z\) are in AP — option 3"),
 shortcut=p(r"Test a simple AP such as \(y, x, z = 1, 4, 7\) against each option. Only option 3 fits it, and it satisfies the condition."),
 concept=r"\[a, b, c \text{ in AP} \iff 2b = a + c\]",
 why=why([("1", r"Needs \(2y = x + z\); the example \(1, 4, 7\) breaks it."), ("2", r"Needs \(2\sqrt y = \sqrt x + \sqrt z\); \(2 \ne 2 + \sqrt7\) in the example."), ("4", r"Needs \(2\sqrt z = \sqrt x + \sqrt y\); \(2\sqrt7 \ne 3\) in the example.")]))

SOL[22] = dict(
 hint=p(r"Write the rule as \(a_n = 2a_{n-1} + 3\). Adding \(3\) to both sides turns it into a doubling sequence."),
 solution=steps(
  ("Write the rule", r"\[a_1 = 2, \qquad a_n = 2a_{n-1} + 3\]"),
  ("Turn it into a GP", r"\[\begin{aligned} a_n + 3 &= 2(a_{n-1} + 3) \\ a_n + 3 &= 5 \cdot 2^{n-1} \\ a_n &= 5 \cdot 2^{n-1} - 3 \end{aligned}\]" + p(r"Check: \(2, 7, 17, 37, \dots\) ✓")),
  ("Solve the inequality", r"\[5 \cdot 2^{n-1} - 3 > 10^6 \;\Rightarrow\; 2^{n-1} > 200000.6\]" +
     p(r"\(2^{17} = 131072\) is too small and \(2^{18} = 262144\) is enough, so \(n - 1 = 18\).")),
  ("Confirm", p(r"\(a_{18} = 655357 < 10^6\) and \(a_{19} = 1310717 > 10^6\) ✓")),
 ) + final(r"\(n = 19\)"),
 shortcut=p(r"For \(a_n = r\,a_{n-1} + d\), add \(\tfrac{d}{r-1}\) to both sides and you get a GP. Here that’s \(\tfrac{3}{1} = 3\)."),
 concept=r"\[a_n = r\,a_{n-1} + d \;\Rightarrow\; a_n + \tfrac{d}{r-1} = \left(a_1 + \tfrac{d}{r-1}\right) r^{\,n-1}\]")
