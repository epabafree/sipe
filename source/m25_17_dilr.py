# -*- coding: utf-8 -*-
# Simp Mock 17 (2025): DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m25_17 import P
import m25_17_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Shirt outlets (Q1–4) ----------------
CPS = ("<ul>" + "".join(f"<li>Path {k}: {v}</li>" for k, v in enumerate(["100, 130, 160, 180, 200", "100, 130, 150, 180, 200", "100, 130, 150, 170, 200",
       "100, 120, 150, 180, 200", "100, 120, 150, 170, 200", "100, 120, 140, 170, 200"], 1)) + "</ul>")
P.dilr_set(1, "Set 1 — Three shirt outlets", DIR,
 p("A garment company makes one kind of shirt and sells it through three outlets in the city: Awesome, Credible and Horizon. In any month the cost price of a shirt is the same at all three outlets. It was $100 in March and rose each month by either $20 or $30, reaching $200 in July.") +
 p("Percentage profit = (selling price − cost price) ÷ cost price × 100. The chart shows the percentage profit at each outlet from March to July.") + F.PCT,
 "DILR::DI::Graphs_and_Charts",
 steps(("Cost paths", p("Four rises adding to $100 must be two of $20 and two of $30: six orders.") + CPS),
       ("Selling price", p("Selling price = cost price × (1 + profit % ÷ 100), read month by month from the chart."))) +
 final("Each question picks the cost path that suits it, or the one its data forces."),
 p("List the six possible cost paths first."),
 p("<b>Fixed endpoints:</b> rises of 20 or 30 adding to 100 must be two of each."))
P.dq(1, "What is the largest possible rise (in $) in the selling price of a shirt at Credible from April to May?", [], "TITA", "49", "Medium",
 "Credible: 10% in April, 20% in May.",
 steps(("Best path", p("Make May’s cost as high as possible: path 1, April 130, May 160.")), ("Rise", p("1.2 × 160 − 1.1 × 130 = 192 − 143 = 49."))) + final("49"))
P.dq(2, "In June the numbers of shirts sold at Awesome, Credible and Horizon were in the ratio 3 : 5 : 4. What was the highest possible average selling price per shirt across the three outlets in June?", ["$198.75", "$195.75", "$189.75", "$185.75"], "MCQ", "1", "Medium",
 "June cost at most $180.",
 steps(("Prices", p("Awesome 1.2 × 180 = 216, Credible 1.05 × 180 = 189, Horizon 1.1 × 180 = 198.")), ("Average", p("(3 × 216 + 5 × 189 + 4 × 198) ÷ 12 = 198.75."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Uses June’s lower cost.")])
P.dq(3, "In May, Horizon made a total profit of $3,297, selling 157 shirts. If it sold 157 shirts every month, what was its average selling price per shirt over the five months?", ["$187.6", "$178.6", "$172.8", "$167.8"], "MCQ", "4", "Medium",
 "Profit per shirt in May: 3297 ÷ 157 = 21.",
 steps(("May cost", p("21 is 15% of 140, so the path is 100, 120, 140, 170, 200.")), ("Prices", p("125, 126, 161, 187, 240; average 839 ÷ 5 = 167.8."))) + final("Option 4"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])
P.dq(4, "At Awesome, with the same number of shirts sold each month, what is the difference between the highest and lowest possible average selling price per shirt over the five months?", ["$8.9", "$9.1", "$9.3", "$9.6"], "MCQ", "2", "Hard",
 "Only the April, May and June costs vary.",
 steps(("Lowest", p("Path 6: 110, 138, 154, 204, 210; average 163.2.")), ("Highest", p("Path 1: 110, 149.5, 176, 216, 210; average 172.3.")), ("Difference", p("9.1."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

# ---------------- Set 2: AI workshop (Q5–10) ----------------
GRID = table(["Year", "Ch", "Ge", "Fr", "All"], [["1st", "0", "5", "5", "10"], ["2nd", "1", "3", "5", "9"], ["3rd", "3", "2", "6", "11"], ["4th", "4", "0", "6", "10"], ["All", "8", "10", "22", "40"]])
P.dilr_set(2, "Set 2 — Languages at an AI workshop", DIR,
 p("An engineering college ran an optional AI workshop for its students, all on four-year degrees. Every student of the college takes exactly one foreign language, Chinese, French or German, from the first year and can’t change it. Fewer than 100 students attended the workshop, and none of them ever failed or took a break. The facts below are about the workshop participants only.") +
 "<ul><li>Among Chinese learners, fourth-years are the most numerous, then third, second and first years, in that order.</li><li>Half of the Chinese learners are fourth-years; of the rest, 75% are third-years.</li>"
 "<li>Among German learners, first-years are the most numerous, then second and then third years; no fourth-year takes German.</li><li>Half of the first-years take German.</li>"
 "<li>French learners outnumber the other two languages together by two-ninths of that number.</li><li>First- and second-year French learners total 10, and third- and fourth-year French learners are equal in number.</li>"
 "<li>First- and fourth-years are equal in number, and one-fourth of the participants are first-years. There are 2 more third-years than second-years.</li>"
 "<li>Among third-years, French has the most students, then Chinese, then German; the same holds for fourth-years.</li></ul>",
 "DILR::DI::Caselets",
 steps(("Size", p("French : others = 11 : 9, so the total is a multiple of 20, and a quarter of it are first-years. Years 1 and 4 are T/4 each and years 2, 3 share T/2 with a gap of 2, so T/4 is even: T = 40 or 80.")),
       ("Chinese", p("C4 = C1 + C2 + C3 and C3 = 3(C1 + C2). With T = 80, French needs 44 with third = fourth = 17, leaving C4 = 3, not a multiple of 4. So T = 40, with Chinese 0, 1, 3, 4.")),
       ("Fill in", GRID)) +
 final("Ch Chinese, Ge German, Fr French. Every cell is fixed."),
 p("The 11 : 9 split and the quarter of first-years make the total a multiple of 20."),
 p("<b>Ratio chains:</b> ‘half are fourth-years; 75% of the rest are third-years’ fixes the shape of the Chinese column."))
P.dq(5, "How many students took part in the workshop?", [], "TITA", "40", "Medium",
 "Multiple of 20, under 100, and T/4 even.", steps(("Total", p("40 (80 fails on the Chinese numbers)."))) + final("40"))
P.dq(6, "What percentage of the participants learn French?", [], "TITA", "55", "Easy",
 "22 of 40.", steps(("Share", p("22 ÷ 40 = 55%."))) + final("55"))
P.dq(7, "Find the odd one out.", ["Number of first-year students learning French", "Number of third-year students learning Chinese", "Number of third-year students learning German", "Number of third-year students learning French"], "MCQ", "4", "Medium",
 "The values are 5, 3, 2 and 6.", steps(("Odd one", p("5, 3 and 2 are prime; 6 is not."))) + final("Option 4"),
 [("1", "5 is prime."), ("2", "3 is prime."), ("3", "2 is prime.")])
P.dq(8, "How many second- and third-year participants learn French?", ["16", "12", "11", "Cannot be determined"], "MCQ", "3", "Easy",
 "5 + 6.", steps(("Count", p("11."))) + final("Option 3"),
 [("1", "Arithmetic slip."), ("2", "Third and fourth years."), ("4", "Fixed.")])
P.dq(9, "The college now lets first- and second-year students take more than one language. At most how many participants could now be taking exactly two languages?", ["19", "18", "17", "16"], "MCQ", "1", "Easy",
 "Only first- and second-years can add one.", steps(("Count", p("10 first-years + 9 second-years = 19."))) + final("Option 1"),
 [("2", "Leaves one out."), ("3", "Leaves two out."), ("4", "Leaves three out.")])
P.dq(10, "What percentage of the participants learning German are second-years?", ["50", "30", "20", "10"], "MCQ", "2", "Easy",
 "3 of 10.", steps(("Share", p("30%."))) + final("Option 2"),
 [("1", "First-years."), ("3", "Third-years."), ("4", "Arithmetic slip.")])

# ---------------- Set 3: A five-team round robin (Q11–14) ----------------
RES = table(["Match", "Result"], [["A–B, A–C", "A won"], ["B–C, C–E", "draw"], ["B–E, B–G", "B won"], ["C–G", "C won"], ["A–E, A–G, E–G", "two ways"]])
P.dilr_set(3, "Set 3 — A five-team football tournament", DIR,
 p("Five national teams, Argentina, Brazil, Chile, Ecuador and Guyana, played a football tournament in which each team played every other team once. A win earned 3 points and a loss 0; a draw earned each team 1 point. The teams finished with different points totals, in the order listed (Argentina highest, Guyana lowest).") +
 "<ul><li>Exactly two matches were drawn.</li><li>Argentina finished with 9 points.</li><li>Every team won at least one match.</li><li>Argentina beat both Brazil and Chile.</li></ul>",
 "DILR::LR::Games_and_Tournaments",
 steps(("Totals", p("10 matches: 8 results (24 points) and 2 draws (4 points), so 28 points. Distinct totals below 9, with Guyana at least 3: 9, 7, 5, 4, 3 is the only way.")),
       ("Draws", p("Chile’s 5 (one win, two draws) and Ecuador’s 4 (one win, one draw) and Brazil’s 7 (two wins, one draw) account for the two draws: Chile drew with Brazil and Ecuador.")),
       ("Results", p("Argentina’s 9 is three wins and a loss. Either Argentina beat Ecuador, Guyana beat Argentina and Ecuador beat Guyana, or the other way round.") + RES)) +
 final("Seven results are fixed; three come in two versions."),
 p("Total points are fixed by the number of draws."),
 p("<b>Points totals:</b> 3 × results + 2 × draws gives the whole pool."))
P.dq(11, "How many points did Brazil score?", [], "TITA", "7", "Easy", "9, 7, 5, 4, 3.", steps(("Brazil", p("7."))) + final("7"))
P.dq(12, "For how many matches can the result (a draw, or which team won) be determined uniquely?", [], "TITA", "7", "Medium",
 "Only the A–E, A–G, E–G triangle is open.", steps(("Count", p("10 − 3 = 7."))) + final("7"))
P.dq(13, "What was the result of Ecuador vs Guyana?", ["Ecuador won.", "Guyana won.", "It was a draw.", "Cannot be determined."], "MCQ", "4", "Easy",
 "It’s in the open triangle.", steps(("Either", p("Ecuador wins in one case, Guyana in the other."))) + final("Option 4"),
 [("1", "Only in one case."), ("2", "Only in one case."), ("3", "Both draws are known.")])
P.dq(14, "For how many teams can the results of all their matches be determined uniquely?", ["5", "4", "3", "2"], "MCQ", "4", "Medium",
 "Which teams avoid the open triangle?", steps(("Teams", p("Brazil and Chile."))) + final("Option 4"),
 [("1", "A, E, G are open."), ("2", "Too many."), ("3", "Too many.")])

# ---------------- Set 4: Five students’ scores (Q15–20) ----------------
P.dilr_set(4, "Set 4 — Five scores around a table", DIR,
 p("A physics tutor gave a 30-question multiple-choice test to five students, Ayushi, Baibhab, Harjas, Khushi and Pranav, seated round a circular table facing the centre. Each correct answer earns 1 mark, with no negative marking.") +
 "<ul><li>The five scores are distinct and lie between 35% and 90% of the maximum.</li><li>Exactly three students scored 70% or more; the other two scored 50% or less.</li>"
 "<li>Going clockwise from the top scorer, the scores keep decreasing.</li><li>Starting from any student other than the lowest scorer, the three scores at that seat and the next two clockwise add up to a prime.</li>"
 "<li>Khushi sits next to neither Ayushi nor Harjas.</li><li>Pranav scored the most, 2 more than Harjas.</li><li>Ayushi’s and Baibhab’s scores add up to an even number.</li></ul>",
 "DILR::LR::Puzzles",
 steps(("Seating", p("Clockwise: Pranav, Harjas, then the order must keep Khushi away from Harjas and Ayushi: Pranav, Harjas, Ayushi, Baibhab, Khushi. Khushi scored least.")),
       ("Ranges", p("High scorers 21–27, low scorers 11–15. Pranav and Harjas are P and P − 2.")),
       ("Primes", p("Testing the top three against the prime sums leaves Pranav 27, Harjas 25, Ayushi 21; Ayushi + Baibhab even makes Baibhab 13 or 15, and the sums force Baibhab 15, Khushi 11.")),
       ("Check", p("27 + 25 + 21 = 73, 25 + 21 + 15 = 61, 21 + 15 + 11 = 47, 15 + 11 + 27 = 53: all prime."))) +
 final("Scores: Pranav 27, Harjas 25, Ayushi 21, Baibhab 15, Khushi 11."),
 p("Seat the students first; the clockwise order then matches the score order."),
 p("<b>Prime sums:</b> parity kills most candidates fast; only odd totals can be prime."))
P.dq(15, "How many of the five scores are prime?", ["0", "1", "2", "3"], "MCQ", "2", "Easy",
 "27, 25, 21, 15, 11.", steps(("Primes", p("Only 11."))) + final("Option 2"),
 [("1", "11 is prime."), ("3", "Only one."), ("4", "Only one.")])
P.dq(16, "What is the largest difference between the scores of two students sitting next to each other?", [], "TITA", "16", "Easy",
 "Pranav sits next to Khushi.", steps(("Difference", p("27 − 11 = 16."))) + final("16"))
P.dq(17, "For how many students can the score be determined uniquely?", [], "TITA", "5", "Medium",
 "The solution is unique.", steps(("Count", p("All five."))) + final("5"))
P.dq(18, r"Suppose each student attempted only the questions they got right, and the tutor deducts \(\tfrac13\) mark for each unattempted question. For how many students is the new score a whole number?", ["0", "1", "2", "3"], "MCQ", "4", "Medium",
 r"New score \(= c - \tfrac{30 - c}{3}\).",
 steps(("Condition", p("Whole only when c is a multiple of 3: 27, 21, 15.")), ("Count", p("Pranav, Ayushi, Baibhab: 3."))) + final("Option 4"),
 [("1", "Some are whole."), ("2", "Three are."), ("3", "Three are.")])
P.dq(19, "Suppose every student attempted every question, and the tutor re-marks the papers with −1 for each wrong answer. What is the average of the five new scores?", ["8.4", "9.6", "10", "10.8"], "MCQ", "2", "Easy",
 "New score = c − (30 − c) = 2c − 30.",
 steps(("New scores", p("24, 20, 12, 0, −8; total 48.")), ("Average", p("9.6."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(20, "With the −1 penalty of the previous question, three students in consecutive seats are chosen at random and their new scores added. What is the probability that the sum is a perfect square?", [r"\(\tfrac12\)", r"\(\tfrac34\)", r"\(\tfrac35\)", r"\(\tfrac25\)"], "MCQ", "3", "Medium",
 "Five blocks of three neighbours.",
 steps(("Sums", p("Clockwise from Pranav: 56, 32, 4, 16, 36. Squares: 4, 16, 36.")), ("Probability", p("3 of 5."))) + final("Option 3"),
 [("1", "Wrong count."), ("2", "Wrong count."), ("4", "Counts the non-squares.")])
