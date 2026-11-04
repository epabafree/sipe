# -*- coding: utf-8 -*-
# Formula (QA, DILR) and technique (VARC) reference cards for the pilot topics.
REF = []
def F(rid, section, topic, name, prompt, formula, symbols, when, trap, example, seen, kind="Formula"):
    REF.append(dict(rid=rid, kind=kind, section=section, topic=topic, name=name, prompt=prompt, formula=formula,
                    symbols=symbols, when=when, trap=trap, example=example, seen=seen))

F("QA-ALG-001", "QA", "Algebra::Equations_and_Polynomials", "Sum of squares equals zero",
  r"An equation where squares add up to \(0\) (often after moving a product term across)",
  r"\[a^2 + b^2 = 0,\ \ a, b \in \mathbb{R} \iff a = 0 \text{ and } b = 0\]",
  [(r"\(a, b\)", "any real expressions, e.g. \(x + 2y\)")],
  "When an equation mixes squares with a product like \(-4xy\), move everything to one side and complete squares.",
  "It only works for real numbers, and it gives <i>and</i>, not <i>or</i>: both squares must be zero.",
  r"\((x-3)^2 + (y+1)^2 = 0 \Rightarrow x = 3,\ y = -1\)", ["2023-S1-QA-01"])

F("QA-NUM-001", "QA", "Number_System::Factors_and_Divisibility", "Divisibility through prime powers",
  r"The least power \(n\) such that \(A\) divides \(B^n\)",
  r"\[A \mid B^n \iff n \ge \max_p \left\lceil \frac{e_p(A)}{e_p(B)} \right\rceil\]",
  [(r"\(e_p(N)\)", "the exponent of prime \(p\) in \(N\)"), (r"\(\lceil\ \rceil\)", "round up")],
  "Questions asking for the least power or least multiplier that makes one number divide another.",
  "Every prime in \(A\) must also appear in \(B\); otherwise no power works.",
  r"\(A = 2^3 \cdot 3,\ B = 2 \cdot 3^4 \Rightarrow n = \max(3, 1) = 3\)", ["2023-S1-QA-02"])

F("QA-ALG-002", "QA", "Algebra::Surds_and_Indices", "Pairing surds: difference of squares",
  r"A sum of two square roots is given and you need each root",
  r"\[(\sqrt p + \sqrt q)(\sqrt p - \sqrt q) = p - q \qquad \frac{1}{\sqrt p + \sqrt q} = \frac{\sqrt p - \sqrt q}{p - q}\]",
  [(r"\(p, q\)", "positive numbers or expressions")],
  "If you know \(\sqrt p + \sqrt q\) and \(p - q\), divide to get \(\sqrt p - \sqrt q\), then add the two equations.",
  "Rationalise carefully: the sign flips in the conjugate.",
  r"\(\sqrt{x+9} + \sqrt{x-9} = 9 \Rightarrow \sqrt{x+9} - \sqrt{x-9} = 18/9 = 2\)", ["2023-S1-QA-03", "2023-S1-QA-20"])

F("QA-ALG-003", "QA", "Algebra::Logarithms_and_Exponents", "Logarithm ↔ power",
  "Turning a log equation into an ordinary one",
  r"\[\log_b a = c \iff b^c = a \qquad \log_b a = \frac{1}{\log_a b}\]",
  [(r"\(b\)", "base: \(b > 0,\ b \ne 1\)"), (r"\(a\)", "argument: \(a > 0\)")],
  "Any log equation: rewrite it as a power, then solve as usual.",
  "Discard roots that make the base negative or \(1\), or the argument non-positive.",
  r"\(\log_x 16 = 4 \Rightarrow x^4 = 16 \Rightarrow x = 2\)", ["2023-S1-QA-04"])

F("QA-ALG-004", "QA", "Algebra::Quadratic_Equations", "Sum and product of roots",
  r"Questions about the roots \(\alpha, \beta\) of a quadratic, without solving it",
  r"\[ax^2 + bx + c = 0:\qquad \alpha + \beta = -\frac{b}{a}, \qquad \alpha\beta = \frac{c}{a}\]",
  [(r"\(a, b, c\)", "coefficients, \(a \ne 0\)"), (r"\(\alpha, \beta\)", "the two roots")],
  "Whenever a question mentions roots, their sum or product, or a quadratic built from them.",
  "For distinct real roots, check the discriminant \(b^2 - 4ac > 0\).",
  r"\(2x^2 - 6x + k:\ \alpha + \beta = 3,\ \alpha\beta = k/2\)", ["2023-S1-QA-07"])

F("QA-ARI-001", "QA", "Arithmetic::Percentages", "Successive percentage change",
  "A value goes through several percentage changes in a row",
  r"\[V_{\text{final}} = V\,(1 + r_1)(1 + r_2)\cdots \qquad \text{net change} = r_1 + r_2 + r_1 r_2\]",
  [(r"\(r_i\)", "each change as a decimal (+ for rise, − for fall)")],
  "Salary hikes, price changes, population growth over several periods.",
  "Each later percentage applies to the <i>new</i> value, not the original.",
  r"\(+20\%\) then \(+40\%\): \(1.2 \times 1.4 = 1.68 \Rightarrow +68\%\)", ["2023-S1-QA-09"])

F("QA-ARI-002", "QA", "Arithmetic::Clocks_and_Calendars", "Angle between clock hands",
  "The angle between the hands at a given time, or how long until it changes",
  r"\[\theta = \left|30H - 5.5M\right| \qquad \text{the gap changes at } 5.5^\circ \text{ per minute}\]",
  [(r"\(H\)", "hour (1–12)"), (r"\(M\)", "minutes past the hour")],
  "Any clock-angle question; for “how long until…” use the \(5.5^\circ\)/min relative speed.",
  "If \(\theta > 180^\circ\), the minor angle is \(360^\circ - \theta\).",
  r"\(8{:}48:\ |240 - 264| = 24^\circ\)", ["2023-S1-QA-10"])

F("QA-ARI-003", "QA", "Arithmetic::Simple_and_Compound_Interest", "Compound interest, any compounding period",
  "Money compounded half-yearly or quarterly",
  r"\[A = P\left(1 + \frac{r}{100k}\right)^{kt} \qquad A_{\text{SI}} = P\left(1 + \frac{rt}{100}\right)\]",
  [(r"\(P\)", "principal"), (r"\(r\)", "annual rate in %"), (r"\(k\)", "periods per year (2 = half-yearly)"), (r"\(t\)", "years")],
  "Any interest question; when two schemes give equal amounts, cancel common factors first.",
  "Half-yearly: halve the rate <i>and</i> double the number of periods.",
  r"\(4\%\) p.a. half-yearly for \(6\) years: \((1.02)^{12}\)", ["2023-S1-QA-14"])

F("QA-GEO-001", "QA", "Geometry::Circles", "Diagonals of a cyclic quadrilateral",
  r"How the diagonals of a cyclic quadrilateral \(ABCD\) divide each other at \(E\)",
  r"\[\frac{AE}{EC} = \frac{AB \cdot AD}{CB \cdot CD} \qquad AE \cdot EC = BE \cdot ED\]",
  [(r"\(E\)", r"where diagonals \(AC\) and \(BD\) meet")],
  "Ratios of diagonal segments in a quadrilateral inscribed in a circle.",
  "Pair each segment with the two sides that meet at its vertex.",
  r"\(AB : CD = 2 : 1,\ BC : AD = 5 : 4 \Rightarrow AE : EC = 8 : 5\)", ["2023-S1-QA-17"])

F("QA-GEO-002", "QA", "Geometry::Coordinate_Geometry", "Circle from its general equation; tangents from a point",
  "Finding the centre and radius, or the distance at which tangents meet at a given angle",
  r"\[x^2 + y^2 + 2gx + 2fy + c = 0\]\[\text{centre } (-g, -f), \quad r = \sqrt{g^2 + f^2 - c}\]\[\text{tangents meet at } 2\theta:\ \ PO = \frac{r}{\sin\theta}\]",
  [(r"\(P\)", "external point"), (r"\(O\)", "centre")],
  "Coordinate questions about circles, tangents and loci.",
  "A vertical tangent touches the circle at the centre’s \(y\)-coordinate.",
  r"\(x^2 + y^2 + 4x - 6y - 3 = 0\) gives centre \((-2, 3)\) and \(r = 4\)", ["2023-S1-QA-18"])

F("QA-GEO-003", "QA", "Geometry::Triangles", "Triangles with the same height",
  "Comparing areas of triangles that share a vertex and a base line",
  r"\[\frac{[\triangle_1]}{[\triangle_2]} = \frac{\text{base}_1}{\text{base}_2} \quad \text{(same height)}\]",
  [(r"\([\ ]\)", "area")],
  "Points on one side of a triangle, with areas in a ratio or progression.",
  "Check the triangles really share the same height (same apex, bases on one line).",
  r"\([ABP] : [ABC] = BP : BC\)", ["2023-S1-QA-19"])

F("QA-ALG-005", "QA", "Algebra::Progressions_and_Series", "Linear recurrence → geometric progression",
  r"A sequence where each term is “\(r\) times the previous, plus \(d\)”",
  r"\[a_n = r\,a_{n-1} + d \;\Rightarrow\; a_n + \tfrac{d}{r-1} = \left(a_1 + \tfrac{d}{r-1}\right) r^{\,n-1}\]",
  [(r"\(r\)", "multiplier (\(r \ne 1\))"), (r"\(d\)", "amount added each step")],
  "Growth questions such as organisms, savings or populations with a fixed addition.",
  "Make sure the question asks for the \(n^{\text{th}}\) term, not the sum.",
  r"\(a_n = 2a_{n-1} + 3,\ a_1 = 2 \Rightarrow a_n = 5 \cdot 2^{n-1} - 3\)", ["2023-S1-QA-22"])

F("QA-ALG-006", "QA", "Algebra::Progressions_and_Series", "Condition for an arithmetic progression",
  "Recognising three terms in AP",
  r"\[a, b, c \text{ in AP} \iff 2b = a + c\]",
  [(r"\(b\)", "the middle term")],
  "Any “which relation holds” question; also test with a quick numeric AP.",
  "Order matters: “\(y, x, z\) in AP” means \(2x = y + z\).",
  r"\(1, 4, 7:\ 2 \times 4 = 1 + 7\) ✓", ["2023-S1-QA-20"])

F("DILR-STA-001", "DILR", "DI::Statistics_Mean_Median_Mode", "Mean, median, mode, range",
  "Data sets described only by their summary statistics",
  r"\[\text{Total} = \text{mean} \times n \qquad \text{Median} = \text{middle value (sorted)} \qquad \text{Range} = \max - \min\]",
  [("Mode", "most frequent value; bimodal = two values tie")],
  "Rating, score and marks sets: turn every mean into a total first.",
  "With 5 values, the median is the 3rd after sorting, which may differ from the 3rd as listed.",
  r"Mean \(3.4\) over \(5\) ratings ⇒ total \(17\)", ["2023-S1-DILR-11", "2023-S1-DILR-15"])

def T(rid, topic, name, prompt, steps_html, trap, example, seen):
    F(rid, "VARC", topic, name, prompt, steps_html, [], "", trap, example, seen, kind="Technique")

T("VARC-RC-001", "RC::Technique", "EXCEPT / NOT questions in RC", "“All of the following … EXCEPT” and “Which is NOT true”",
  "<ol><li>State the passage’s main claim in one line.</li><li>Tick off the options that agree with it, each against a specific line.</li><li>The answer reverses the claim or swaps a key word (south ↔ north).</li></ol>",
  "Bold-sounding options are often near-quotes and therefore true.", "“Remapping” = re-centring on the global south ⇒ the West-origin option is the exception.", ["2023-S1-VARC-01", "2023-S1-VARC-04"])
T("VARC-RC-002", "RC::Technique", "Odd pair out", "Pairs of items; choose the pair whose relationship differs",
  "<ol><li>Label each pair: “has this feature” or “lacks this feature”.</li><li>The odd pair has the different label.</li></ol>",
  "A pair that feels negative can still be a genuine characteristic.", "Postcolonial novels : Border-crossing is a contrast; the other three are characteristics.", ["2023-S1-VARC-02"])
T("VARC-RC-003", "RC::Technique", "Weaken–EXCEPT", "“All of the following would weaken … EXCEPT”",
  "<ol><li>Write the claim, both sides if it is a contrast.</li><li>Sort the options by which side they attack.</li><li>The answer agrees with the passage.</li></ol>",
  "Options that seem off-topic may attack the less obvious side of the contrast.", "Mainstream fiction privileged white Christian travel: this restates the claim, so it doesn’t weaken it.", ["2023-S1-VARC-03"])
T("VARC-VA-001", "VA::Technique", "Missing sentence", "Place a sentence into one of four gaps",
  "<ol><li>Read the sentence <i>after</i> each gap.</li><li>Find a pronoun or “this/these” that needs the new sentence.</li><li>Match the gap number to the shuffled answer labels.</li></ol>",
  "Answer choices may be labelled “Option 2”, “Option 4”… in shuffled order.", "“They shared similarities…” needs the peoples and similarities sentence before it.", ["2023-S1-VARC-17"])
T("VARC-VA-002", "VA::Technique", "Odd sentence out", "Five sentences; four form a paragraph",
  "<ol><li>Find the opener.</li><li>Chain the sentences through linking words (“this capacity”).</li><li>The leftover is on topic but does a different job.</li></ol>",
  "Don’t pick the off-topic-looking sentence too fast; test the chain.", "A sentence about what to <i>call</i> the capacity breaks a chain about how it develops.", ["2023-S1-VARC-19"])
T("VARC-VA-003", "VA::Technique", "Para-jumble (type the order)", "Four sentences to order",
  "<ol><li>Fix a question → answer pair.</li><li>Fix a keyword hand-off (“mystery” → “unsolved”).</li><li>Place the broadest sentence first.</li></ol>",
  "A sentence starting with a pronoun (“It…”) can’t open the paragraph.", "4 → 1 → 2 → 3", ["2023-S1-VARC-21"])
T("VARC-VA-004", "VA::Technique", "Summary questions", "Choose the best summary of a short passage",
  "<ol><li>List the passage’s 2–3 points.</li><li>Eliminate contradictions and additions.</li><li>Keep the cause → effect structure.</li></ol>",
  "Specific words not in the passage (“British”) rule an option out.", "Navigation tech transformed colonialism ⇒ settlement and dominance.", ["2023-S1-VARC-23"])

# ---------------- added in batch 2 (CAT 2023 Slot 1, remaining questions) ----------------
F("QA-ALG-007", "QA", "Algebra::Inequalities_and_Absolute_Value", "Equations with |x| and x²",
  r"An equation mixing \(|x|\) with \(x^2\)",
  r"\[x^2 = |x|^2\]<p>Put \(t = |x| \ge 0\), solve for \(t\), then \(x = \pm t\).</p>",
  [(r"\(t\)", "the non-negative value \(|x|\)")],
  "Absolute-value equations or inequalities that also contain squares.",
  r"Check \(x = 0\) separately before dividing by \(|x|\), and discard negative \(t\).",
  r"\(2|x|(x^2 + 1) = 5x^2 \Rightarrow 2t^2 - 5t + 2 = 0 \Rightarrow t = 2\) (or \(\tfrac12\))", ["2023-S1-QA-05"])
F("QA-ALG-008", "QA", "Algebra::Equations_and_Polynomials", "Factor theorem, then the discriminant",
  "A cubic with one known root, and a condition on the other roots",
  r"\[p(a) = 0 \iff (x - a) \text{ is a factor of } p(x)\]\[\text{real roots of } x^2 + bx + c \iff b^2 - 4c \ge 0\]",
  [(r"\(a\)", "the known root")],
  "Cubic questions: divide out the known root and work with the quadratic left over.",
  "Match coefficients carefully; the constant term of the quadratic is often fixed by the cubic’s constant.",
  r"\(x^3 + \dots + 2 = (x + 2)(x^2 + (2r-1)x + 1)\)", ["2023-S1-QA-06"])
F("QA-ARI-004", "QA", "Arithmetic::Average", "Totals from averages, with bounds",
  "Groups with equal marks each, an average, and inequalities between them",
  r"\[\text{Total} = \text{average} \times n\]<p>Write the target in one variable, find its interval, then count the integers in it.</p>",
  [(r"\(n\)", "number of people")],
  "Average questions that ask how many values a total can take.",
  "Individual marks may be non-integers; only the asked-for quantity needs to be an integer. Check both ends of the interval.",
  r"\(4g + 6b = 240,\ b \le g \le 2b \Rightarrow 2g + 6b \in [171.4,\ 192]\)", ["2023-S1-QA-08"])
F("QA-ARI-005", "QA", "Arithmetic::Time_Speed_and_Distance", "Average speed",
  "Average speed over a whole trip",
  r"\[\bar v = \frac{\text{total distance}}{\text{total time}} \qquad \text{equal distances at } u, v:\ \bar v = \frac{2uv}{u + v}\]",
  [(r"\(\bar v\)", "average speed")],
  "Trips with a speed limit, stops, or several legs.",
  "Never average the speeds directly unless the <i>times</i> are equal.",
  r"\(800\) km in \(8\) h ⇒ \(100\) km/h", ["2023-S1-QA-11"])
F("QA-ARI-006", "QA", "Arithmetic::Profit_Loss_and_Discount", "Profit, loss and equal selling prices",
  "Two items sold at the same price with different profit or loss percentages",
  r"\[\text{SP} = \text{CP}\,(1 + p) \qquad \text{equal SP} \Rightarrow \text{CP}_A (1 + p_A) = \text{CP}_B (1 + p_B)\]",
  [(r"\(p\)", "profit as a decimal (negative for loss)")],
  "Comparing two items, or re-pricing them so the selling prices stay equal.",
  "Profit % is always on the cost price, not the selling price.",
  r"\(1.2A = 0.9B \Rightarrow B = \tfrac43 A\)", ["2023-S1-QA-12"])
F("QA-ARI-007", "QA", "Arithmetic::Mixture_and_Alligation", "Repeated removal and replacement",
  "A portion is taken out and replaced with another substance, several times",
  r"\[\text{original left} = V\left(1 - \frac{x}{V}\right)^{n}\]",
  [(r"\(V\)", "total volume"), (r"\(x\)", "amount removed each time"), (r"\(n\)", "number of replacements")],
  "Milk–water, coffee–cocoa, wine–water replacement questions.",
  "The same amount must be removed each time, and the total volume must stay constant.",
  r"\(\left(1 - \tfrac15\right)^2 = \tfrac{16}{25}\)", ["2023-S1-QA-13"])
F("QA-ARI-008", "QA", "Arithmetic::Time_and_Work", "Work, rates and progressions",
  "Several workers with linked rates or times",
  r"\[\text{work} = \text{rate} \times \text{time} \qquad \text{rates in HP} \iff \text{times in AP}\]",
  [("rate", "fraction of the job done per day"), ("time", "days to finish the job alone")],
  "Time-and-work questions where the rates or times form a progression.",
  "Harmonic progression in rates turns into an arithmetic progression in times, not in rates.",
  r"Times \(T, 1.5T, 2T\): \(\tfrac4T + \tfrac{9}{1.5T} + \tfrac{16}{2T} = 1 \Rightarrow T = 18\)", ["2023-S1-QA-15"])
F("QA-ARI-009", "QA", "Arithmetic::Time_Speed_and_Distance", "Two travellers meeting",
  "Two people start together from opposite ends; you know how long each takes after they meet",
  r"\[t_{\text{meet}} = \sqrt{t_1 t_2} \qquad \frac{v_1}{v_2} = \sqrt{\frac{t_2}{t_1}}\]",
  [(r"\(t_1, t_2\)", "time each takes after meeting to reach the other end")],
  "Any “after meeting, A takes … and B takes …” question.",
  "The speed ratio uses the square root of the times in reverse order.",
  r"\(t_1 = 6,\ t_2 = 24 \Rightarrow t = 12,\ v_1 : v_2 = 2 : 1\)", ["2023-S1-QA-16"])
F("QA-MOD-001", "QA", "Modern_Maths::Permutations_and_Combinations", "Counting numbers with distinct digits",
  "How many numbers in a range have no repeated digit",
  r"<p>Numbers with \(k\) digits, all different:</p>\[9 \times 9 \times 8 \times \cdots \quad (k \text{ factors})\]",
  [("first 9", "first digit can’t be 0"), ("next 9", "0 is now allowed, but not the first digit")],
  "Digit-counting questions; split the count by number of digits.",
  "Check the endpoint separately (1000 repeats 0).",
  r"\(9 + 81 + 648 = 738\) up to \(1000\)", ["2023-S1-QA-21"])

F("DILR-LR-001", "DILR", "LR::Analytical_Reasoning", "Bloc voting",
  "Groups vote together, some members are candidates, and totals are given",
  r"<ol><li>Bloc size = group size − candidates in that group.</li><li>Remove the candidates’ own votes from each total.</li><li>Match what remains to possible bloc sizes; usually only one combination works.</li></ol>",
  [], "Elections, departments, teams voting as units.", "Candidates can’t vote for themselves or for their own group’s candidates, so check both rules.",
  "13 = 9 + 4 is the only way to make 13 from the possible bloc sizes", ["2023-S1-DILR-06"], kind="Technique")
F("DILR-LR-002", "DILR", "LR::Puzzles", "Price or score formulas: build a table of possibilities",
  "Each item’s value comes from a formula with a few unknown parts",
  r"<ol><li>Compute the fixed part for each item (here, road adjacency).</li><li>List every value the item can take.</li><li>A given maximum or minimum usually matches exactly one cell, and that fixes the rest.</li></ol>",
  [], "Grid puzzles with prices, scores or points computed from neighbours.", "Remember to check every vacant item against the given maximum or minimum, not just the one you used.",
  r"Only B2 (no parking, \(3\) occupied neighbours) gives ₹24 lakhs", ["2023-S1-DILR-01"], kind="Technique")
F("DILR-DI-001", "DILR", "DI::Caselets", "Queues and counters",
  "Applicants arrive in slots and are served at counters with fixed times",
  r"\[\text{capacity per slot} = c \times \frac{\text{slot length}}{t}\]",
  [(r"\(c\)", "number of counters"), (r"\(t\)", "time per application")],
  "Scheduling and queue caselets: if capacity exceeds arrivals, no backlog builds and only the last slot matters.",
  "Late arrivals join the queue when they arrive, not at their scheduled time.",
  r"\(4 \times 15/10 = 6 > 5\) US applications per slot", ["2023-S1-DILR-20"])

T("VARC-RC-004", "RC", "Purpose of an example or reference", "“The author mentions X to…”",
  "<ol><li>Reread the sentences just before and after X.</li><li>Name the claim being supported there.</li><li>Pick the option describing that claim, not the topic in general.</li></ol>",
  "Options often describe the example accurately but miss <i>why</i> it is there.", "Hadza example ⇒ foraging was a choice", ["2023-S1-VARC-05", "2023-S1-VARC-06", "2023-S1-VARC-14"])
T("VARC-RC-005", "RC", "Detail questions", "Questions about what a specific part of the passage says",
  "<ol><li>Find the exact lines.</li><li>Paraphrase them in your own words.</li><li>Match; reject options that exaggerate, invert, or import ideas.</li></ol>",
  "A familiar word from the passage in a wrong option is a common trap.", "“does not thematise them as heavily” ⇒ cursory treatment", ["2023-S1-VARC-07", "2023-S1-VARC-10"])
T("VARC-RC-006", "RC", "Main goal and inference", "What the author mainly wants, or what can be inferred",
  "<ol><li>State the passage’s main claim in one line.</li><li>An inference must follow from the text, not just sound reasonable.</li><li>Watch quantifiers: most, all, never, only.</li></ol>",
  "Value-laden words (“degenerated”, “most”) usually go beyond the text.", "“holds a mirror to an acquisitive society”", ["2023-S1-VARC-08", "2023-S1-VARC-15"])
T("VARC-RC-007", "RC", "Weaken questions", "“Which, if true, would weaken the author’s claims?”",
  "<ol><li>Pin down the claim, often the conclusion.</li><li>The answer attacks the claim directly.</li><li>Options that restate facts or misstate minor details don’t weaken anything.</li></ol>",
  "An option can be factually wrong and still not weaken the argument.", "Wolf attacks on tourists undercut the tourism upside", ["2023-S1-VARC-12"])

# ---------------- added with CAT 2023 Slots 2 and 3 ----------------
F("QA-NUM-002", "QA", "Number_System::Factors_and_Divisibility", "Counting factors",
  r"How many factors a number has, or the smallest number with a given count",
  r"\[N = p^a q^b r^c\]\[\text{factors} = (a+1)(b+1)(c+1)\]",
  [(r"\(p, q, r\)", "distinct primes"), (r"\(a, b, c\)", "their exponents")],
  "“Exactly k factors” questions: factorise k to list the possible shapes, then try the smallest primes.",
  "“Factors other than 1 and itself” means subtract 2 from the total before matching shapes.",
  r"\(15 = 5 \times 3 \Rightarrow p^4 q^2\): \(2^4 \cdot 3^2 = 144\)", ["2023-S2-QA-06", "2023-S3-QA-07"])
F("QA-ALG-009", "QA", "Algebra::Inequalities_and_Absolute_Value", "AM ≥ GM for a minimum",
  r"The least value of a sum like \(\tfrac{A}{y} + By\) with \(y > 0\)",
  r"\[\frac{a + b}{2} \ge \sqrt{ab} \qquad \frac{A}{y} + By \ge 2\sqrt{AB}\]",
  [(r"\(a, b\)", "positive quantities whose product is constant")],
  "Whenever two positive terms multiply to a constant, their sum is smallest when they are equal.",
  "Only for positive terms, and the minimum is reached only if equality is actually possible.",
  r"\(\tfrac1y + 9y \ge 2\sqrt9 = 6\), at \(y = \tfrac13\)", ["2023-S2-QA-05"])
F("QA-ALG-010", "QA", "Algebra::Equations_and_Polynomials", "Cube identities",
  r"Sums or differences of cubes, or powers of \(t + \tfrac1t\)",
  r"\[a^3 - b^3 = (a - b)(a^2 + ab + b^2)\]\[t^3 + \tfrac1{t^3} = s^3 - 3s,\quad s = t + \tfrac1t\]",
  [(r"\(s\)", r"\(t + \tfrac1t\)")],
  r"Given \(p^2 + q^2\) and \(pq\), or \(t^n + t^{-n}\) for some \(n\), step up or down with these identities.",
  r"Taking a square root gives \(\pm\); check which sign is allowed.",
  r"\(t + \tfrac1t = \sqrt5 \Rightarrow t^3 + \tfrac1{t^3} = 5\sqrt5 - 3\sqrt5 = 2\sqrt5\)", ["2023-S2-QA-20", "2023-S3-QA-04"])
F("QA-ALG-011", "QA", "Algebra::Logarithms_and_Exponents", "Change of base",
  r"Fractions of logs, or logs with surd bases",
  r"\[\frac{\log_c a}{\log_c b} = \log_b a \qquad \log_{b^k} a = \tfrac1k \log_b a\]",
  [(r"\(c\)", "any valid base")],
  "Turn every term into the same base before comparing or adding.",
  "The argument of every log must stay positive; reject roots that break this.",
  r"\(\dfrac{\log_x 25}{\log_x 0.008} = \log_{5^{-3}} 5^2 = -\tfrac23\)", ["2023-S2-QA-07", "2023-S3-QA-01"])
F("QA-ALG-012", "QA", "Algebra::Progressions_and_Series", "Common terms of two APs",
  "Numbers that belong to two arithmetic progressions at once",
  r"\[d_{\text{common}} = \operatorname{lcm}(d_1, d_2)\]",
  [(r"\(d_1, d_2\)", "the two common differences")],
  "Find the first common term by remainders, then step by the LCM within the overlapping range.",
  "Stay inside both ranges: each sequence may stop at a different place.",
  r"\(6n + 7\) and \(7n + 8\): both \(\equiv 1 \pmod{42}\) ⇒ largest 3-digit \(967\)", ["2023-S2-QA-22", "2023-S3-QA-21"])
F("QA-ALG-013", "QA", "Algebra::Linear_Equations", "Two linear equations: how many solutions",
  "Conditions for one, none, or infinitely many solutions",
  r"\[\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2} \Rightarrow \infty \qquad \frac{a_1}{a_2} = \frac{b_1}{b_2} \ne \frac{c_1}{c_2} \Rightarrow \text{none}\]",
  [(r"\(a_i x + b_i y = c_i\)", "the two equations")],
  "Infinitely many solutions means the two lines are the same line.",
  "Solve the resulting quadratic fully; the negative root often gives the extreme answer.",
  r"\(\tfrac{a+5}{1} = \tfrac{b^2-15}{1} = \tfrac{8b}{4}\)", ["2023-S3-QA-03"])
F("QA-ALG-014", "QA", "Algebra::Functions", "Functions of combined inputs",
  r"\(f(\text{expression}_1, \text{expression}_2)\) is given; find \(f\) itself",
  r"\[\text{find } \alpha, \beta \text{ with } \alpha u + \beta v = \text{the right-hand side}\]",
  [(r"\(u, v\)", "the two input expressions")],
  "Linear inputs: combine them to cancel one variable, then read off the formula.",
  "Check the combination on the original before substituting.",
  r"\(u = 3x + 2y,\ v = 2x - 5y \Rightarrow 5u + 2v = 19x\)", ["2023-S3-QA-22"])
F("QA-ALG-015", "QA", "Algebra::Progressions_and_Series", "Infinite geometric series",
  "Sums that go on forever with a constant ratio",
  r"\[a + ar + ar^2 + \dots = \frac{a}{1 - r}\quad (|r| < 1)\]",
  [(r"\(r\)", "common ratio")],
  "Nested sums: write each bracket as a finite GP, or swap the order of summation.",
  r"Only valid for \(|r| < 1\).",
  r"\(\sum_{k\ge0} 4^{-k} = \tfrac43\)", ["2023-S3-QA-20"])
F("QA-ARI-010", "QA", "Arithmetic::Time_Speed_and_Distance", "Boats and streams",
  "A boat going up and down a river",
  r"\[\text{down} = b + r \qquad \text{up} = b - r \qquad b = \tfrac{\text{down} + \text{up}}{2},\ r = \tfrac{\text{down} - \text{up}}{2}\]",
  [(r"\(b\)", "boat speed in still water"), (r"\(r\)", "river speed")],
  "Pick the distance as the LCM of the times to get whole-number speeds.",
  "Check which direction is downstream before writing the equation.",
  r"\(12\) km in \(2\) h down and \(3\) h up ⇒ \(b = 5,\ r = 1\)", ["2023-S3-QA-09"])
F("QA-ARI-011", "QA", "Arithmetic::Time_and_Work", "Pipes and cisterns",
  "Fill pipes and drain pipes working together",
  r"\[\text{net rate} = \sum \frac{1}{t_{\text{fill}}} - \sum \frac{1}{t_{\text{drain}}}\]",
  [(r"\(t\)", "time for one pipe alone")],
  "Write one equation per scenario in terms of rates, then eliminate.",
  "Use given limits (like “less than five hours”) to pick between roots.",
  r"\(\tfrac13 - \tfrac12 + \tfrac23 = \tfrac12\) ⇒ tank full in 2 h", ["2023-S2-QA-08"])
F("QA-ARI-012", "QA", "Arithmetic::Ratio_and_Proportion", "Direct and square proportion",
  "Price or value that varies with a power of size",
  r"\[P = k w^n\]<p>For a fixed total weight, \(\sum w^2\) is smallest when the parts are as equal as possible, and largest when they are as uneven as possible.</p>",
  [(r"\(k\)", "constant of proportionality")],
  "Breaking an object into parts: compare the extremes of the sum of squares.",
  "Parts must respect the conditions (distinct, whole numbers).",
  r"\(18 = 3 + 4 + 5 + 6\) (min \(\sum w^2 = 86\)) vs \(1 + 2 + 3 + 12\) (max \(158\))", ["2023-S2-QA-12"])
F("QA-ARI-013", "QA", "Arithmetic::Profit_Loss_and_Discount", "False measures and discounts",
  "A trader gets extra on buying, gives less on selling, and offers a discount",
  r"\[\begin{aligned} 1 + \text{profit} = {} & \frac{\text{received}}{\text{paid for}} \times \frac{\text{charged for}}{\text{given}} \\ & \times \frac{SP}{CP} \times (1 - d) \end{aligned}\]",
  [(r"\(d\)", "discount as a decimal")],
  "Multiply all the factors; every cheat and discount is one ratio.",
  "Keep each ratio the right way up: getting extra helps him, giving less helps him.",
  r"\(\tfrac{105}{100} \times \tfrac{100}{95} \times 1.1 \times 0.95 = 1.155\)", ["2023-S3-QA-08"])
F("QA-GEO-004", "QA", "Geometry::Polygons_and_Quadrilaterals", "Regular polygons",
  "Angles and diagonals of an n-sided regular polygon",
  r"\[\text{exterior} = \frac{360^\circ}{n} \qquad \text{interior} = 180^\circ - \text{exterior} \qquad \text{diagonals} = \frac{n(n - 3)}{2}\]",
  [(r"\(n\)", "number of sides")],
  "Any question that gives an angle relation in a regular polygon.",
  "Interior and exterior angles add to 180°, not 360°.",
  r"\(I - E = 120^\circ \Rightarrow E = 30^\circ,\ n = 12,\ 54\) diagonals", ["2023-S3-QA-19"])
F("QA-GEO-005", "QA", "Geometry::Circles", "Angle in a semicircle",
  "A triangle drawn on a diameter",
  r"\[\text{angle in a semicircle} = 90^\circ \qquad \text{legs } ak, bk:\ k^2(a^2 + b^2) = (2r)^2\]",
  [(r"\(r\)", "radius")],
  "A side of the triangle is a diameter: it’s right-angled, and the diameter is the hypotenuse.",
  "The hypotenuse is \(2r\), not \(r\).",
  r"Legs in ratio \(1 : 1\) on radius \(r\): area \(r^2\)", ["2023-S2-QA-17"])
F("QA-GEO-006", "QA", "Geometry::Trigonometry", "Altitudes and angles in triangles",
  "Ratios of altitudes, or angles at the orthocentre",
  r"\[h_B = AB\sin A \qquad h_{\text{base}} = AB\cos\tfrac{A}{2}\]",
  [(r"\(h_B\)", "altitude from \\(B\\)"), (r"\(h_{\text{base}}\)", "altitude to the base of an isosceles triangle"), (r"\(A\)", "apex angle")],
  "Find one angle from the given angle at the orthocentre, then express each altitude with sine or cosine.",
  "The angle at the orthocentre and the angle you need are often supplementary.",
  r"\(\angle A = 30^\circ \Rightarrow AD/BE = 2\cos 15^\circ\)", ["2023-S3-QA-17"])
F("DILR-LR-003", "DILR", "LR::Routes_and_Networks", "Timed routes on a map",
  "Teams moving along streets, one street per time step",
  r"<ol><li>Write a position grid: teams × time steps.</li><li>Fill fixed positions from the clues.</li><li>Use “one team per street at a time” to rule out the remaining moves.</li></ol>",
  [], "Patrol, delivery or travel puzzles on a small graph with fixed crossing times.",
  "A team must move every step if it patrols “continuously”; it can’t wait at a station.",
  r"Team 4 limited to A, C, E ⇒ it alternates A ↔ C/E", ["2023-S3-DILR-06", "2023-S3-DILR-07", "2023-S3-DILR-08", "2023-S3-DILR-09", "2023-S3-DILR-10"], kind="Technique")
F("DILR-LR-004", "DILR", "LR::Mathematical_Reasoning", "Rise-then-fall sequences",
  "Yearly amounts that start and end at fixed values, rise to a peak, then fall",
  r"<ol><li>Subtract the fixed ends from the total.</li><li>List every rise-then-fall pattern with allowed steps that makes the remainder.</li><li>Firms with one pattern are certain; use them first.</li></ol>",
  [], "Funding, production or score sequences with step-size rules.", "“No two equal consecutive years” rules out flat peaks.",
  r"5 years, total 10, ends 1 ⇒ middle \(2, 4, 2\) only", ["2023-S2-DILR-01", "2023-S2-DILR-02", "2023-S2-DILR-03", "2023-S2-DILR-04", "2023-S2-DILR-05"], kind="Technique")
F("DILR-DI-002", "DILR", "DI::Data_Tabulation", "Chains of 2-day averages",
  "Averages of consecutive days are given",
  r"\[T_1 + T_2 = 2A_2,\quad T_2 + T_3 = 2A_3,\ \dots\]",
  [(r"\(A_k\)", "average of days \(k - 1\) and \(k\)")],
  "One extra equality (two days equal) fixes every daily total.",
  "Averages can be non-integers; double them first.",
  r"\(T_3 = T_4\) and \(T_3 + T_4 = 32\) ⇒ \(16\) each", ["2023-S2-DILR-11", "2023-S2-DILR-12", "2023-S2-DILR-13", "2023-S2-DILR-14", "2023-S2-DILR-15"])
F("DILR-LR-005", "DILR", "LR::Puzzles", "Grids with equal row and column totals",
  "Cells hold distinct values 1–9 and rows/columns have equal sums",
  r"\[\text{each line sum} = \frac{1 + 2 + \dots + 9}{3} = 15\]",
  [], "3 × 3 grids with distinct integer averages and equal row and column totals.",
  "Distinct integers between 1 and 9 in nine cells must be exactly 1 to 9.",
  r"Col 1 averages \(4, 8\) ⇒ third \(= 3\)", ["2023-S2-DILR-16", "2023-S2-DILR-17", "2023-S2-DILR-18", "2023-S2-DILR-19", "2023-S2-DILR-20"])
F("DILR-DI-003", "DILR", "DI::Data_Tabulation", "Two-way tables from percentages",
  "Items split two ways (variant × type) with percentage clues",
  r"<ol><li>Fill the 2 × 2 grid of city totals first (variant × type).</li><li>Then go dealer by dealer, subtracting.</li></ol>",
  [], "Sales or survey sets where each item has two attributes.",
  "A percentage of a sub-group (e.g. of Inverter ACs) is not a percentage of the total.",
  r"Split Inverter \(36 = 80\%\) of Inverter ⇒ Inverter \(= 45\)", ["2023-S3-DILR-16", "2023-S3-DILR-17", "2023-S3-DILR-18", "2023-S3-DILR-19", "2023-S3-DILR-20"])
F("DILR-LR-006", "DILR", "LR::Mathematical_Reasoning", "Weighted aggregate scores",
  "An aggregate is a weighted average of two components",
  r"\[\text{agg} = wT + (1 - w)P \qquad \text{agg}_1 - \text{agg}_2 = w\Delta T + (1 - w)\Delta P\]",
  [(r"\(w\)", "weight of the test")],
  "A given gap between two people’s aggregates is linear in \(w\): solve it directly.",
  "Weights are positive and add to 1; reject cases that give an impossible component score.",
  r"\(40 - 60w = 4 \Rightarrow w = 0.6\)", ["2023-S3-DILR-11", "2023-S3-DILR-12", "2023-S3-DILR-13", "2023-S3-DILR-14", "2023-S3-DILR-15"])


# ---------------- added with CAT 2022 Slot 1 ----------------
F("QA-MOD-002", "QA", "Modern_Maths::Set_Theory", "Overlaps of three sets",
  "How many people can like all three things, at most and at least",
  r"\[x_1 + 2x_2 + 3x_3 = n(A) + n(B) + n(C)\]\[x_1 + x_2 + x_3 \le \text{total}\]",
  [(r"\(x_k\)", "people in exactly \(k\) of the sets")],
  "Questions asking for the largest or smallest possible overlap of three groups.",
  "The largest overlap can’t exceed the smallest set. For the smallest, push as many people as possible into exactly two sets.",
  r"\(73 + 80 + 52 = 205\) likes among 100 students: at least 5 like all three", ["2022-S1-QA-15"])
F("QA-ALG-016", "QA", "Algebra::Inequalities_and_Absolute_Value", "Absolute values as distances",
  r"Sums like \(|x - p| + |x - q|\)",
  r"\[|x - p| + |x - q| \ge |p - q|\]",
  [(r"\(p, q\)", "two points on the number line")],
  "Read each term as a distance on the number line. The sum is constant, and smallest, for every x between the two points.",
  r"Write \(|x + a|\) as \(|x - (-a)|\) before reading off the point.",
  r"\(|x + 1| + |x - 1| = 2\) for every \(x\) from \(-1\) to \(1\)", ["2022-S1-QA-12", "2022-S1-QA-21"])
F("QA-ALG-017", "QA", "Algebra::Functions", "The greatest integer function",
  r"Sums or equations involving \([x]\)",
  r"\[[x] = k \iff k \le x < k + 1\]",
  [(r"\([x]\)", "the largest integer not more than \(x\)")],
  "Find the values of n where the expression crosses a whole number; the function is constant between them.",
  r"For negative numbers, \([-1.2] = -2\), not \(-1\).",
  r"\(\left[\tfrac{n + 5}{25}\right] = 1\) for \(n = 20\) to \(44\)", ["2022-S1-QA-20"])
F("QA-MOD-003", "QA", "Modern_Maths::Permutations_and_Combinations", "Sharing identical things",
  "Identical objects given to different people",
  r"\[\#\{y_1 + \dots + y_k = n,\ y_i \ge 1\} = \binom{n - 1}{k - 1} \qquad \#\{y_i \ge 0\} = \binom{n + k - 1}{k - 1}\]",
  [(r"\(n\)", "number of identical objects"), (r"\(k\)", "number of people")],
  "Any “in how many ways can n identical things be shared” question. Conditions like “even numbers only” become a substitution first.",
  "Check whether each person must get at least one; the two formulas differ.",
  r"20 balloons, even amounts, at least 2 each: \(\binom{9}{3} = 84\)", ["2022-S1-QA-22"])

for r in REF:
    extra = {"VARC-RC-001": ["2023-S1-VARC-09", "2023-S1-VARC-11", "2023-S1-VARC-13", "2023-S1-VARC-16"], "VARC-VA-001": ["2023-S1-VARC-18"],
             "VARC-VA-002": ["2023-S1-VARC-20"], "VARC-VA-003": ["2023-S1-VARC-22"], "VARC-VA-004": ["2023-S1-VARC-24"],
             "QA-ALG-004": ["2023-S1-QA-06", "2023-S2-QA-02", "2023-S3-QA-05"], "DILR-STA-001": ["2023-S3-DILR-01", "2023-S3-DILR-04"],
             "QA-ARI-001": ["2023-S3-QA-11"], "QA-ARI-003": ["2023-S2-QA-09"], "QA-ARI-004": ["2023-S2-QA-13", "2023-S2-QA-15", "2023-S3-QA-10"],
             "QA-ARI-007": ["2023-S2-QA-14"], "QA-ARI-009": ["2023-S2-QA-10"], "QA-ARI-008": ["2023-S3-QA-13", "2023-S3-QA-15"],
             "QA-ALG-007": ["2023-S2-QA-19"], "QA-GEO-003": ["2023-S2-QA-18"], "QA-NUM-001": ["2023-S2-QA-04"],
             "DILR-LR-002": ["2023-S2-DILR-06", "2022-S1-DILR-06"], "QA-ALG-004": ["2023-S1-QA-06", "2023-S2-QA-02", "2023-S3-QA-05", "2022-S1-QA-02"],
             "DILR-LR-003": ["2022-S1-DILR-01", "2022-S1-DILR-02", "2022-S1-DILR-03", "2022-S1-DILR-04", "2022-S1-DILR-05"],
             "QA-ARI-004": ["2023-S2-QA-13", "2023-S2-QA-15", "2023-S3-QA-10", "2022-S1-QA-03", "2022-S1-QA-08"], "QA-ARI-012": ["2022-S1-QA-05"],
             "QA-ALG-012": ["2022-S1-QA-14"], "QA-NUM-001": ["2023-S2-QA-04", "2022-S1-QA-04"], "QA-ARI-013": ["2022-S1-QA-17"],
             "DILR-LR-006": ["2022-S1-DILR-16"]}.get(r["rid"], [])
    r["seen"] += [x for x in extra if x not in r["seen"]]
