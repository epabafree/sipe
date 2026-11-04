# -*- coding: utf-8 -*-
# DILR — CAT 2023 Slot 1, Set 3 (Q11–15). Context reused from the extraction (corrected table).
from fmt import steps, final, why, table, p


SET_SOLUTION = steps(
 ("Turn every mean into a total", p(r"Each restaurant and each worker has \(5\) ratings, so \(\text{total} = 5 \times \text{mean}\).") +
   table(["Restaurant", "R1", "R2", "R3", "R4", "R5"], [["Mean", "3.4", "2.2", "3.8", "2.8", "3.4"], ["Total", "17", "11", "19", "14", "17"]]) +
   table(["Worker", "Ullas", "Vasu", "Waman", "Xavier", "Yusuf"], [["Mean", "2.2", "3.8", "3.4", "3.6", "2.6"], ["Total", "11", "19", "17", "18", "13"]]) +
   p(r"Both rows of totals add up to \(78\) ✓")),
 ("Pin down each worker’s five ratings", p("Use the known 1s and 5s with each worker’s median, mode and range.") +
   table(["Worker", "Known", "Reasoning", "Ratings"], [
     ["Waman", r"\(5, 1, 5\)", r"other two sum to \(17 - 11 = 6\); median \(4\) ⇒ \(4\) and \(2\)", r"\(\{1, 2, 4, 5, 5\}\)"],
     ["Xavier", r"\(5, 5\)", r"range \(4\) ⇒ min \(1\); other three sum to \(8\), median \(4\)", r"\(\{1, 3, 4, 5, 5\}\)"],
     ["Yusuf", r"\(1, 1\)", r"modes \(1\) and \(4\) ⇒ two 4s; median \(3\)", r"\(\{1, 1, 3, 4, 4\}\)"],
     ["Ullas", r"\(1\)", r"mode and median \(2\); max \(= 1 + 3 = 4\); total \(11\)", r"\(\{1, 2, 2, 2, 4\}\)"],
     ["Vasu", r"\(5\)", r"min \(= 5 - 3 = 2\); mode and median \(4\); total \(19\)", r"\(\{2, 4, 4, 4, 5\}\)"],
   ])),
 ("Use R2 and R3", p(r"<b>R2:</b> Waman \(1\) + Xavier \(5\) + Yusuf \(1\) \(= 7\), so Ullas + Vasu \(= 11 - 7 = 4\). Ullas’s only \(1\) came from R1, so both are \(2\).") +
   p(r"<b>R3:</b> \(5 + 5 + 1 = 11\), so Ullas + Vasu \(= 19 - 11 = 8\). Vasu’s only \(5\) came from R5, so both are \(4\).") +
   p(r"That leaves Ullas \(2, 2\) for R4 and R5, and Vasu \(4, 4\) for R1 and R4.")),
 ("Settle R1 by testing both cases", p(r"R1 already has Ullas \(1\), Vasu \(4\), Waman \(5\), so Xavier + Yusuf \(= 17 - 10 = 7\): either \((3, 4)\) or \((4, 3)\).") +
   p(r"If Xavier \(= 4\) and Yusuf \(= 3\), Yusuf’s R4 and R5 are both \(4\). R4 then needs Waman + Xavier \(= 14 - 2 - 4 - 4 = 4\) with Waman \(\in \{2, 4\}\) and Xavier \(\in \{1, 3\}\). No pair works.") +
   p(r"So <b>Xavier \(= 3\) and Yusuf \(= 4\)</b> at R1.")),
 ("Finish R4 and R5", p(r"R4 needs Waman + Xavier + Yusuf \(= 14 - 6 = 8\); R5 needs \(17 - 7 = 10\). With Waman \(\in \{4, 2\}\), Xavier \(\in \{1, 4\}\), Yusuf \(\in \{3, 4\}\), the only fit is R4 \(= (4, 1, 3)\) and R5 \(= (2, 4, 4)\).")),
) + table(["", "Ullas", "Vasu", "Waman", "Xavier", "Yusuf", "Total"], [
     ["R1", "1", "4", "5", "3", "4", "17"], ["R2", "2", "2", "1", "5", "1", "11"], ["R3", "4", "4", "5", "5", "1", "19"],
     ["R4", "2", "4", "4", "1", "3", "14"], ["R5", "2", "5", "2", "4", "4", "17"], ["Total", "11", "19", "17", "18", "13", "78"]]) \
  + final("All 25 ratings are fixed: there is exactly one possible grid.")

SHORTCUT = p("Start with the workers who have the most constraints, here two known extremes plus a mode (Yusuf, Xavier, Waman). They settle almost at once, and the restaurant totals finish the job.")
CONCEPT = r"\[\text{Total} = \text{mean} \times n \qquad \text{Median of 5} = 3^{\text{rd}} \text{ value when sorted}\]\[\text{Range} = \max - \min \qquad \text{Bimodal} \Rightarrow \text{two values tie for most frequent}\]"

SOL = {
 11: dict(hint=p(r"Convert each mean to a total first: R1 \(= 3.4 \times 5 = 17\), and so on."),
          solution=steps(("Solve the set", p("Work through the whole set (open “Solve the whole set” below).")),
                         ("Count the unknowns", p("Exactly one grid satisfies every condition, so no rating is left open."))) + final(r"\(0\)")),
 12: dict(hint=p("You need R2’s full row. R2’s known ratings plus its total of 11 settle it quickly."),
          solution=steps(("Find R2’s row", p(r"Waman \(1\), Xavier \(5\), Yusuf \(1\); then Ullas + Vasu \(= 4\), and both must be \(2\).")),
                         ("Count the 4s", table(["", "Ullas", "Vasu", "Waman", "Xavier", "Yusuf"], [["R2", "2", "2", "1", "5", "1"]]) + p("There are no 4s in the row."))) + final(r"\(0\)")),
 13: dict(hint=p(r"At R1, Xavier + Yusuf must add to \(7\). Test both ways of splitting it."),
          solution=steps(("Set up R1", p(r"R1 \(= 17\); Ullas \(1\) + Vasu \(4\) + Waman \(5\) \(= 10\), so Xavier + Yusuf \(= 7\).")),
                         ("Test the cases", p(r"\((4, 3)\) fails at R4: no allowed Waman + Xavier makes \(4\). So Xavier \(= 3\)."))) + final(r"\(3\)")),
 14: dict(hint=p("Find R3’s five ratings, sort them, and take the middle one."),
          solution=steps(("R3’s ratings", table(["", "Ullas", "Vasu", "Waman", "Xavier", "Yusuf"], [["R3", "4", "4", "5", "5", "1"]])),
                         ("Sort and take the middle", r"\[1,\ 4,\ \boxed{4},\ 5,\ 5\]")) + final(r"\(4\)")),
 15: dict(hint=p("Write each restaurant’s ratings in sorted order and count how many workers received the median value."),
          solution=steps(("Sort each restaurant’s ratings", table(["Restaurant", "Sorted ratings", "Median", "Workers given the median"], [
                              ["R2", "1, 1, 2, 2, 5", "2", "2 (Ullas, Vasu)"], ["R3", "1, 4, 4, 5, 5", "4", "2 (Ullas, Vasu)"],
                              ["R4", "1, 2, 3, 4, 4", "3", "1 (Yusuf)"], ["R5", "2, 2, 4, 4, 5", "4", "2 (Xavier, Yusuf)"]], hi={(2, 3)}))) + final("R4 (choice 3)"),
          why=why([("1", r"R2’s median \(2\) went to two workers."), ("2", r"R3’s median \(4\) went to two workers."), ("4", r"R5’s median \(4\) went to two workers.")])),
}
