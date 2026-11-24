# -*- coding: utf-8 -*-
# Simp Mock 12: DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m12 import P
import m12_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: A queue of 40 (Q1–5) ----------------
P.dilr_set(1, "Set 1 — Who can see whom in a queue", DIR,
 p("All the students of a class stand in a queue facing north (the front). Deepanjan, Indraneel, Pradeep, Pragyan and Sumanta are the five tallest, with different heights; everyone else is shorter than all five. These five split the queue into six groups, each of a different size; the smallest group has 3 students. None of the five is at either end of the queue.") +
 p("A student can see everyone in front up to and including the first student taller than him or her, but no further. A student taller than everyone in front can see the whole queue ahead.") +
 "<ol><li>Deepanjan can see the front of the queue, and exactly 8 students stand in front of him.</li>"
 "<li>The farthest person Sumanta can see is Pradeep; 15 students stand between them.</li>"
 "<li>Pradeep can see that 3 students stand between Deepanjan and Indraneel. He can see 14 students in all in front of him.</li>"
 "<li>The 9 students at the back stand in descending order of height from back to front, and the farthest each of them can see is Sumanta.</li>"
 "<li>Indraneel can see some students in front of him and nobody beyond them.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Length", p("9 behind Sumanta, Sumanta, 15, Pradeep, 14 in front: 40 students. Pradeep sees everything ahead, so he is the tallest; Pragyan is among the 15.")),
       ("Front part", p("Deepanjan has 8 ahead, Indraneel 3 away from him, Pradeep 14 ahead. Either (Pradeep) 5 (Deepanjan) 3 (Indraneel) 4 (front), or (Pradeep) 1 (Indraneel) 3 (Deepanjan) 8. A group of 1 breaks the ‘smallest is 3’ rule, so the first holds; Indraneel is shorter than Deepanjan.")),
       ("Pragyan", p("The other 14 between Sumanta and Pradeep split into two new group sizes, not 3, 4, 5 or 9: 8 + 6, in either order. Pragyan is shorter than Sumanta.")),
       ("Queue (back → front)", p("9 · Sumanta · 8 or 6 · Pragyan · 6 or 8 · Pradeep · 5 · Deepanjan · 3 · Indraneel · 4"))) +
 final("40 students; Pragyan’s spot has two options."),
 p("Total length comes from Sumanta and Pradeep; the group-size rule settles the rest."),
 p("<b>Visibility puzzles:</b> ‘can see the front’ means taller than everyone ahead; ‘farthest is X’ means X is the first taller person."))
P.dq(1, "How many students are in the queue?", [], "TITA", "40", "Hard",
 "Count around Sumanta and Pradeep.",
 steps(("Count", p("9 + 1 + 15 + 1 + 14 = 40."))) + final("40"))
P.dq(2, "Who is the tallest student?", ["Pragyan", "Sumanta", "Pradeep", "Deepanjan"], "MCQ", "3", "Hard",
 "Who sees everyone in front, with Sumanta seeing only up to him?",
 steps(("Read", p("Pradeep."))) + final("Option 3"),
 [("1", "Shorter than Sumanta."), ("2", "Stops at Pradeep."), ("4", "In front of Pradeep.")])
P.dq(3, "Which could be the number of students behind Pragyan?", ["15", "17", "18", "19"], "MCQ", "3", "Hard",
 "9 + Sumanta + 8 or 6.",
 steps(("Count", p("18 or 16."))) + final("Option 3"),
 [("1", "Not possible."), ("2", "Not possible."), ("4", "Not possible.")])
P.dq(4, "Who could be the shortest of the five?", ["Pragyan", "Indraneel", "Deepanjan", "Pragyan or Indraneel"], "MCQ", "4", "Hard",
 "Indraneel < Deepanjan < Pradeep; Pragyan < Sumanta < Pradeep.",
 steps(("Compare", p("Pragyan and Indraneel are never compared."))) + final("Option 4"),
 [("1", "Indraneel also possible."), ("2", "Pragyan also possible."), ("3", "Taller than Indraneel.")])
P.dq(5, "What is the largest possible number of students in the queue shorter than Pragyan?", [], "TITA", "37", "Hard",
 "Pragyan can be taller than Deepanjan and Indraneel.",
 steps(("Count", p("The 35 others plus Deepanjan and Indraneel: 37."))) + final("37"))

# ---------------- Set 2: Doctors (Q6–10) ----------------
COUNTS = table(["C", "N", "U", "O", "E"], [["80", "120", "100", "80", "60"]])
P.dilr_set(2, "Set 2 — Doctors in five specialities", DIR,
 p("A multi-speciality hospital has doctors in five categories: Cardiologists (C), Nephrologists (N), Urologists (U), Orthopaedists (O) and Endocrinologists (E). In each category, the doctors with an advanced specialisation make up a different one of the percentages 15%, 20%, 30%, 40% and 50%, in some order.") +
 p("The chart gives the number of doctors in each set of three categories taken together.") + F.DOCS,
 "DILR::DI::Graphs_and_Charts",
 steps(("Total", p("Each category appears in 6 of the 10 bars: 2640 ÷ 6 = 440 doctors.")),
       ("Each category", p("C = (C+N+U) + (C+O+E) − 440 = 300 + 220 − 440 = 80, and similarly for the rest.") + COUNTS),
       ("Specialists", p("Each count is multiplied by a different one of 15%, 20%, 30%, 40%, 50%."))) +
 final("All five counts are fixed; only the percentages move."),
 p("Pairs of complementary triples (sharing one category) give each category."),
 p("<b>Sums taken k at a time:</b> each item appears in the same number of sums, so the grand total comes first."))
P.dq(6, "What is the smallest possible number of categories with at least 10 specialists?", [], "TITA", "4", "Medium",
 "Which category could fall below 10?",
 steps(("Below 10", p("Only E at 15%: 60 × 0.15 = 9. Every other product is at least 12."))) + final("4"))
P.dq(7, "What is the largest possible number of categories with at least 50 specialists?", [], "TITA", "1", "Medium",
 "Only 50% of 100 or 120 reaches 50.",
 steps(("Check", p("120 × 0.4 = 48 falls short, and only one category gets 50%."))) + final("1"))
P.dq(8, "For how many categories can the number of doctors be determined exactly?", [], "TITA", "5", "Medium",
 "All counts come from the chart.",
 steps(("Read", p("All five."))) + final("5"))
P.dq(9, "Suppose that when the categories are ordered by number of doctors, their specialisation percentages are in the same order. What is the total number of specialists?", ["149", "141", "148", "Cannot be determined because we cannot determine the number of doctors in all five categories"], "MCQ", "1", "Medium",
 "60, 80, 80, 100, 120 with 15%, 20%, 30%, 40%, 50%.",
 steps(("Add", p("9 + 16 + 24 + 40 + 60 = 149."))) + final("Option 1"),
 [("2", "Slip."), ("3", "Slip."), ("4", "The counts are known.")])
P.dq(10, "Which set could be the numbers of specialists in the five categories, in descending order?", ["(18, 24, 24, 30, 36)", "(40, 40, 36, 16, 9)", "(12, 12, 32, 40, 60)", "More than one of the above"], "MCQ", "2", "Medium",
 "Each percentage once, each category once.",
 steps(("Option 2", p("E 60 × 15% = 9, C or O 80 × 20% = 16, N 120 × 30% = 36, U 100 × 40% = 40, O or C 80 × 50% = 40.")),
       ("Others", p("Options 1 and 3 cannot be made with each percentage used once."))) + final("Option 2"),
 [("1", "Not possible."), ("3", "Not possible."), ("4", "Only option 2.")])

# ---------------- Set 3: Barter among five tribes (Q11–15) ----------------
TRIBE = (table(["Tribe", "Br.", "Rec.", "Home"], [["Shark", "10", "12", "13"], ["Whale", "17", "13", "15"], ["Octopus", "16", "11", "14"], ["Dolphin", "—", "13", "13"], ["Turtle", "—", "13", "13"]]) +
         table(["Tribe", "T", "H", "M", "G"], [["Shark", "2", "0", "1", "1"], ["Whale", "1", "2", "1", "0"], ["Octopus", "1", "1", "1", "1"], ["Dolphin", "2", "2", "0", "0"], ["Turtle", "1", "2", "1", "0"]]))
DEALS = table(["Barter", "Units received"], [["Shark–Whale", "5 – 3"], ["Shark–Octopus", "0 – 0"], ["Shark–Dolphin", "3 – 2"], ["Shark–Turtle", "4 – 4"], ["Whale–Octopus", "5 – 5"],
                                             ["Whale–Dolphin", "2 – 4"], ["Whale–Turtle", "3 – 1"], ["Octopus–Dolphin", "4 – 3"], ["Octopus–Turtle", "2 – 5"], ["Dolphin–Turtle", "4 – 3"]])
P.dilr_set(3, "Set 3 — A barter market of five tribes", DIR,
 p("Five island tribes — Shark, Whale, Octopus, Dolphin and Turtle — meet at a weekly barter market. Each tribe makes one product of its own and trades with every other tribe exactly once, as a group, offering only its own product.") +
 "<ul><li><b>TEKKA</b>: the stronger tribe receives more units than it gives. Its strength is (units received) ÷ (units given) by the stronger tribe. The weaker tribe calls it a <b>HARAN</b>.</li>"
 "<li><b>MITO</b>: equal units are exchanged.</li><li><b>GOSA</b>: no exchange. Units given or received are zero only in a GOSA.</li>"
 "<li>Goods not bartered are taken back home.</li></ul>" +
 p("For one market day: Br. = units brought, Rec. = units received, Home = units taken home (received plus unbartered); T, H, M, G = number of TEKKAs, HARANs, MITOs and GOSAs.") + TRIBE +
 "<ol><li>The Dolphins brought one unit less than the Turtles.</li>"
 "<li>The Sharks and Turtles had a MITO with 8 units exchanged in all. All MITOs together exchanged 18 units.</li>"
 "<li>The units the Dolphins and Whales received from the Sharks were both prime, the Whales receiving more. The Sharks’ TEKKA over the Whales was stronger than their TEKKA over the Dolphins.</li>"
 "<li>The Whales received from the Turtles as many units as the Sharks received from the Dolphins.</li>"
 "<li>The Whales’ only TEKKA was the strongest of the day, and the only one of that strength.</li>"
 "<li>The second-strongest TEKKA was the Turtles’ over the Octopus; it was above 2 and the only one of that strength.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Goods", p("Everything brought goes home with someone: 13 + 15 + 14 + 13 + 13 = 68 brought. Dolphins and Turtles brought 68 − 43 = 25: 12 and 13.")),
       ("MITOs and GOSA", p("Shark–Octopus is the only GOSA (each has one). MITOs: Shark–Turtle 4–4, and the other (10 units) Whale–Octopus 5–5.")),
       ("Sharks", p("Their TEKKAs are over the Whales and Dolphins, who receive primes 3 and 2. Receipts give Sharks 5 from the Whales and 3 from the Dolphins.")),
       ("Whales", p("Whales got 3 from the Turtles. Their one TEKKA, the day’s strongest, is over the Turtles: 3 – 1 (strength 3). They take 2 from the Dolphins and give 4.")),
       ("Octopus", p("The Turtles’ TEKKA over the Octopus is between 2 and 3: 5 – 2. Octopus–Dolphin is then 4 – 3, and Dolphin–Turtle 4 – 3.")),
       ("All barters", DEALS)) +
 final("Every barter is fixed."),
 p("Use the goods totals first, then the unique MITOs and GOSA, then the strongest TEKKAs."),
 p("<b>Pairwise exchange puzzles:</b> conservation (brought = taken home in total) often gives the first missing numbers."))
P.dq(11, "With which two tribes did the Dolphins have a TEKKA?", ["Turtles and Whales", "Turtles and Octopus", "Whales and Octopus", "Cannot be determined"], "MCQ", "1", "Hard",
 "Where did the Dolphins receive more?",
 steps(("Read", p("Whale 4 – 2 and Turtle 4 – 3 in the Dolphins’ favour."))) + final("Option 1"),
 [("2", "Octopus beat them."), ("3", "Octopus beat them."), ("4", "Fixed.")])
P.dq(12, "In how many TEKKAs did the stronger tribe receive exactly 1 unit more than it gave?", ["2", "3", "4", "5"], "MCQ", "2", "Hard",
 "List the TEKKAs.",
 steps(("Count", p("Shark–Dolphin 3–2, Octopus–Dolphin 4–3, Dolphin–Turtle 4–3: 3."))) + final("Option 2"),
 [("1", "Misses one."), ("3", "Too many."), ("4", "Too many.")])
P.dq(13, "In how many barters was the total number of units exchanged a non-zero even number?", ["3", "4", "5", "6"], "MCQ", "3", "Hard",
 "Add each pair.",
 steps(("Count", p("Shark–Whale 8, Shark–Turtle 8, Whale–Octopus 10, Whale–Dolphin 6, Whale–Turtle 4: 5."))) + final("Option 3"),
 [("1", "Too few."), ("2", "Too few."), ("4", "Too many.")])
P.dq(14, "The ‘barter imbalance’ of a barter is the absolute difference between the units the two sides received. Which tribe has the largest sum of its four imbalances?", ["Turtle", "Whale", "Dolphin", "More than one tribe"], "MCQ", "4", "Hard",
 "Add the gaps per tribe.",
 steps(("Sums", p("Shark 3, Whale 6, Octopus 4, Dolphin 5, Turtle 6."))) + final("Option 4"),
 [("1", "Ties with Whale."), ("2", "Ties with Turtle."), ("3", "5 only.")])
P.dq(15, "How many units did the Dolphins receive from the Octopus?", [], "TITA", "3", "Hard",
 "Octopus–Dolphin 4 – 3.",
 steps(("Read", p("3."))) + final("3"))

# ---------------- Set 4: A café’s servings (Q16–20) ----------------
CAFE = table(["", "Red", "Blue"], [["Arabica bakery", "95", "5"], ["Arabica beverage", "25", "5"], ["Robusta bakery", "35", "15"], ["Robusta beverage", "15", "10"]])
P.dilr_set(4, "Set 4 — A café’s 205 servings", DIR,
 p("A café offers 205 different servings: 130 use Arabica coffee and 75 Robusta. Each serving is either a bakery product or a beverage, and is packed in a red or a blue container.") +
 "<ol><li>35 servings are in blue containers.</li>"
 "<li>Arabica servings in blue containers equal Robusta beverages in blue containers.</li>"
 "<li>Robusta servings in blue containers equal Arabica beverages in red containers. This number equals the number of Robusta beverages, which is half the number of Robusta bakery products.</li>"
 "<li>Robusta bakery products in red containers are 65 fewer than Arabica bakery products.</li></ol>",
 "DILR::DI::Caselets",
 steps(("Robusta", p("Let Robusta beverages = x; Robusta bakery = 2x; 3x = 75, x = 25.")),
       ("Blue", p("Robusta blue = Arabica beverages in red = 25. So Arabica blue = 35 − 25 = 10 = Robusta beverages in blue; Robusta bakery blue = 15.")),
       ("The rest", p("Robusta bakery red = 50 − 15 = 35, so Arabica bakery = 100 and Arabica beverages = 30.") + CAFE)) +
 final("Every cell is fixed."),
 p("Start with the chain in clue 3; it pins Robusta first."),
 p("<b>Three-way splits:</b> chains of ‘equals’ reduce many cells to one unknown."))
P.dq(16, "How many Arabica servings are in blue containers?", ["10", "5", "15", "20"], "MCQ", "1", "Medium",
 "5 + 5.",
 steps(("Read", p("10."))) + final("Option 1"),
 [("2", "Bakery only."), ("3", "Robusta bakery blue."), ("4", "Bakery blue.")])
P.dq(17, "What is the difference between Arabica and Robusta bakery products?", ["55", "5", "65", "50"], "MCQ", "4", "Medium",
 "100 and 50.",
 steps(("Difference", p("50."))) + final("Option 4"),
 [("1", "Slip."), ("2", "Slip."), ("3", "Clue 4’s number.")])
P.dq(18, "How many bakery products are in blue containers?", ["10", "15", "20", "25"], "MCQ", "3", "Medium",
 "5 + 15.",
 steps(("Read", p("20."))) + final("Option 3"),
 [("1", "Slip."), ("2", "Robusta only."), ("4", "Slip.")])
P.dq(19, "What percentage of Robusta servings are in red containers?", ["25%", "33%", "50%", "None of these"], "MCQ", "4", "Medium",
 "50 of 75.",
 steps(("Percent", p("66⅔%."))) + final("Option 4"),
 [("1", "No."), ("2", "That is blue."), ("3", "No.")])
P.dq(20, "What is the ratio of beverages to all servings?", ["10 : 41", "11 : 41", "15 : 41", "30 : 41"], "MCQ", "2", "Medium",
 "55 beverages.",
 steps(("Ratio", p("55 : 205 = 11 : 41."))) + final("Option 2"),
 [("1", "Slip."), ("3", "Slip."), ("4", "Slip.")])
