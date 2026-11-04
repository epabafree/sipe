# -*- coding: utf-8 -*-
# CAT 2023 Slot 1 — DILR pilot set (Q11–15): restaurant ratings
SET_ID = "2023_S1_DILR_S3"
SET_TITLE = "Set 3 — Five restaurants rate five gig workers"
DIRECTIONS = "Answer the questions based on the following information."
CONTEXT = r"""
<p>Five restaurants, coded R1, R2, R3, R4 and R5 gave integer ratings to five gig workers – Ullas, Vasu, Waman, Xavier and Yusuf, on a scale of 1 to 5.</p>
<p>The means of the ratings given by R1, R2, R3, R4 and R5 were 3.4, 2.2, 3.8, 2.8 and 3.4 respectively.</p>
<p>The summary statistics of these ratings for the five workers is given below.</p>
<div class="tbl"><table>
<tr><th></th><th>Ullas</th><th>Vasu</th><th>Waman</th><th>Xavier</th><th>Yusuf</th></tr>
<tr><td class="rh">Mean rating</td><td>2.2</td><td>3.8</td><td>3.4</td><td>3.6</td><td>2.6</td></tr>
<tr><td class="rh">Median rating</td><td>2</td><td>4</td><td>4</td><td>4</td><td>3</td></tr>
<tr><td class="rh">Modal rating</td><td>2</td><td>4</td><td>5</td><td>5</td><td>1 and 4</td></tr>
<tr><td class="rh">Range of rating*</td><td>3</td><td>3</td><td>4</td><td>4</td><td>3</td></tr>
</table></div>
<p class="small">* Range of ratings is defined as the difference between the maximum and minimum ratings awarded to a worker.</p>
<p>The following is partial information about ratings of 1 and 5 awarded by the restaurants to the workers.</p>
<p>(a) R1 awarded a rating of 5 to Waman, as did R2 to Xavier, R3 to Waman and Xavier, and R5 to Vasu.<br>
(b) R1 awarded a rating of 1 to Ullas, as did R2 to Waman and Yusuf, and R3 to Yusuf.</p>
"""
NOTE = ("Source misprints in the data table were corrected: “Model rating” → “Modal rating”. The Range row was printed "
        "as 3, 3, 5, 4, 4. That contradicts statements (a)/(b): Waman has both a 1 and a 5 but a mode of 5 and median 4, which forces a range of 4, "
        "and Yusuf’s ratings are 1, 1, 3, 4, 4. The source’s own solution uses 3, 3, 4, 4, 3, which is what is shown here. "
        "All five answers match the answer key.")

SOLUTION = r"""
<p class="step"><b>Step 1 — Convert means to totals</b> (5 ratings each).</p>
<p>Restaurant totals: R1 = 17, R2 = 11, R3 = 19, R4 = 14, R5 = 17. &nbsp;Worker totals: Ullas 11, Vasu 19, Waman 17, Xavier 18, Yusuf 13. (Both add up to 78 ✓)</p>

<p class="step"><b>Step 2 — Pin down each worker’s multiset of ratings</b></p>
<ul>
<li><b>Waman</b> has 5 (R1), 1 (R2), 5 (R3). The other two add to 17 − 11 = 6, and the median must be 4, so they are {4, 2}.</li>
<li><b>Xavier</b> has 5 (R2), 5 (R3). Range 4 ⇒ his minimum is 1. The remaining three add to 8 with median 4 ⇒ {1, 3, 4}.</li>
<li><b>Yusuf</b> has 1 (R2), 1 (R3). Bimodal 1 and 4 ⇒ two 4s; median 3 ⇒ the fifth rating is 3. Ratings {1, 1, 3, 4, 4}, total 13 ✓.</li>
<li><b>Ullas</b> has 1 (R1). Mode 2 and median 2, range 3 ⇒ maximum 4; total 11 ⇒ {1, 2, 2, 2, 4}.</li>
<li><b>Vasu</b> has 5 (R5). Range 3 ⇒ minimum 2; mode and median 4, total 19 ⇒ {2, 4, 4, 4, 5}.</li>
</ul>

<p class="step"><b>Step 3 — Use the restaurant totals</b></p>
<ul>
<li><b>R2</b>: W 1 + X 5 + Y 1 = 7 ⇒ U + V = 4. Ullas’s only 1 is from R1, so U = 2 and V = 2.</li>
<li><b>R3</b>: W 5 + X 5 + Y 1 = 11 ⇒ U + V = 8 ⇒ U = 4, V = 4 (Vasu’s only 5 is from R5).</li>
<li>So Ullas gets 2, 2 from R4 and R5, and Vasu gets 4, 4 from R1 and R4.</li>
<li><b>R1</b>: U 1 + V 4 + W 5 = 10 ⇒ X + Y = 7 ⇒ (X, Y) = (3, 4) or (4, 3).</li>
<li>If R1 gives X = 4, Y = 3: then R4 and R5 both give Yusuf 4. R4 needs W + X = 14 − 2 − 4 − 4 = 4 with W ∈ {2, 4}, X ∈ {1, 3} — impossible. So <b>X = 3, Y = 4</b>.</li>
<li><b>R4</b>: W + X + Y = 8 and <b>R5</b>: W + X + Y = 10, with W ∈ {4, 2}, X ∈ {1, 4}, Y ∈ {3, 4}. The only fit is R4: W 4, X 1, Y 3 and R5: W 2, X 4, Y 4.</li>
</ul>

<p class="step"><b>Final grid (every rating is determined)</b></p>
<div class="tbl"><table>
<tr><th></th><th>Ullas</th><th>Vasu</th><th>Waman</th><th>Xavier</th><th>Yusuf</th><th>Total</th></tr>
<tr><td class="rh">R1</td><td>1</td><td>4</td><td>5</td><td>3</td><td>4</td><td>17</td></tr>
<tr><td class="rh">R2</td><td>2</td><td>2</td><td>1</td><td>5</td><td>1</td><td>11</td></tr>
<tr><td class="rh">R3</td><td>4</td><td>4</td><td>5</td><td>5</td><td>1</td><td>19</td></tr>
<tr><td class="rh">R4</td><td>2</td><td>4</td><td>4</td><td>1</td><td>3</td><td>14</td></tr>
<tr><td class="rh">R5</td><td>2</td><td>5</td><td>2</td><td>4</td><td>4</td><td>17</td></tr>
<tr class="tot"><td class="rh">Total</td><td>11</td><td>19</td><td>17</td><td>18</td><td>13</td><td>78</td></tr>
</table></div>
"""

APPROACH = r"""<p><b>Set strategy:</b> mean, median, mode and range questions always start by converting every mean into a <b>total</b>. Then fix the workers with the most constraints (two known extremes plus a mode) before touching the restaurant totals. Here Yusuf, Xavier and Waman collapse almost immediately.</p>"""
CONCEPT = r"""<p>Sum = mean × n &nbsp;·&nbsp; Median of 5 values = the 3rd value when sorted &nbsp;·&nbsp; Range = max − min &nbsp;·&nbsp; Mode = most frequent value (bimodal ⇒ two values tie)</p>"""

DILR = []
def q(qno, question, options, qtype, answer, expl, why="", diff="Medium"):
    DILR.append(dict(section="DILR", qno=qno, set_id=SET_ID, set_title=SET_TITLE, directions=DIRECTIONS,
        context=CONTEXT, question=question, options=options, qtype=qtype, answer=answer,
        explanation=expl + "<hr class='soft'>" + SOLUTION, why_wrong=why, approach=APPROACH, concept=CONCEPT, hint="",
        topic=["DILR::DI::Logic_Based_DI", "DILR::DI::Statistics_Mean_Median_Mode"], difficulty=diff,
        source_note=NOTE))

q(11, "How many individual ratings cannot be determined from the above information?", [], "TITA", "0",
  r"<p><b>Answer: 0.</b> The case analysis below leaves exactly one consistent grid, so all 25 ratings are determined.</p>")
q(12, "To how many workers did R2 give a rating of 4?", [], "TITA", "0",
  r"<p><b>Answer: 0.</b> R2’s ratings are 2, 2, 1, 5, 1 — no 4s.</p>")
q(13, "What rating did R1 give to Xavier?", [], "TITA", "3",
  r"<p><b>Answer: 3.</b> R1 must give X + Y = 7. The case X = 4, Y = 3 fails at R4, so X = 3.</p>")
q(14, "What is the median of the ratings given by R3 to the five workers?", [], "TITA", "4",
  r"<p><b>Answer: 4.</b> R3’s ratings sorted: 1, 4, 4, 5, 5 → the median is 4.</p>")
q(15, "Which among the following restaurants gave its median rating to exactly one of the workers?",
  ["R2", "R3", "R4", "R5"], "MCQ", "3",
  r"<p><b>Answer: R4.</b> R4’s ratings sorted: 1, 2, 3, 4, 4 → the median is 3, and only Yusuf got a 3.</p>",
  r"""<ul>
<li><b>R2</b>: 1, 1, 2, 2, 5 → median 2, given to <i>two</i> workers (Ullas, Vasu).</li>
<li><b>R3</b>: 1, 4, 4, 5, 5 → median 4, given to two workers (Ullas, Vasu).</li>
<li><b>R5</b>: 2, 2, 4, 4, 5 → median 4, given to two workers (Xavier, Yusuf).</li>
</ul>""")
