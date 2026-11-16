# -*- coding: utf-8 -*-
# Simp Mock 15 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_15 import P
import m25_15_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Paint bottles (Q1–5) ----------------
PAINT = p("Brands: Crimson 26, Azure 16, Emerald 28, Amber 21, Indigo 21. Types: A 30, B 20, C 62. All bottles: 112.")
P.dilr_set(1, "Set 1 — An artist’s paint bottles", DIR,
 p("An artist uses paint bottles of three types, A, B and C, from five brands: Crimson, Azure, Emerald, Amber and Indigo. The table shows how many bottles of each type each brand has.") +
 table(["Brand", "Type A", "Type B", "Type C"], [["Crimson", "7", "5", "14"], ["Azure", "4", "3", "9"], ["Emerald", "5", "2", "21"], ["Amber", "6", "4", "11"], ["Indigo", "8", "6", "7"]]),
 "DILR::DI::Data_Tabulation",
 steps(("Totals", PAINT),
       ("Worst case", p("‘To be sure of’ means planning for the unluckiest order: take everything outside the smallest group you need, then one more."))) +
 final("All questions use the totals."),
 p("For ‘to be sure’, avoid the scarcest group as long as possible."),
 p("<b>Pigeonhole worst case:</b> the answer is (everything outside the smallest needed group) + 1."))
P.dq(1, "What is the minimum number of bottles the artist must pick from the whole stack to be sure of having at least one bottle of each brand?", ["72", "93", "97", "112"], "MCQ", "3", "Easy",
 "Azure is the smallest brand (16).", steps(("Worst case", p("Pick all 96 non-Azure bottles first, then one more: 97."))) + final("Option 3"),
 [("1", "Arithmetic slip."), ("2", "That is for types."), ("4", "Every bottle.")])
P.dq(2, "What is the minimum number of bottles the artist must pick to be sure of having at least one bottle of each type?", ["72", "93", "97", "112"], "MCQ", "2", "Easy",
 "Type B is the smallest (20).", steps(("Worst case", p("All 30 + 62 = 92 of types A and C, then one more: 93."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "That is for brands."), ("4", "Every bottle.")])
P.dq(3, "What is the minimum number of bottles the artist must pick to be sure of having at least one bottle of every brand–type combination?", [], "TITA", "111", "Easy",
 "The smallest cell is Emerald type B, 2 bottles.", steps(("Worst case", p("112 − 2 = 110 others first, then one more: 111."))) + final("111"))
P.dq(4, "The artist picks two different brands and one bottle from each. In how many ways can this be done? (All bottles are distinct.)", [], "TITA", "4973", "Medium",
 "Add the products of brand totals over all pairs.",
 steps(("Shortcut", p(r"\(\sum_{i<j} n_i n_j = \tfrac{(\sum n_i)^2 - \sum n_i^2}{2}\).")),
       ("Numbers", p(r"\(112^2 = 12544\); squares 676 + 256 + 784 + 441 + 441 = 2598. (12544 − 2598) ÷ 2 = 4973."))) + final("4973"))
P.dq(5, "The artist picks three bottles at random from the whole collection. What is the probability that they are of three different types?",
 [r"\(\tfrac{475}{2849}\)", r"\(\tfrac{465}{2849}\)", r"\(\tfrac{485}{2849}\)", r"\(\tfrac{455}{2849}\)"], "MCQ", "2", "Medium",
 "One bottle from each type total.",
 steps(("Favourable", p("30 × 20 × 62 = 37,200.")), ("Total", p(r"\(\binom{112}{3} = 227{,}920\).")), ("Ratio", p(r"\(\tfrac{37200}{227920} = \tfrac{465}{2849}\)."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])

# ---------------- Set 2: A courier network (Q6–9) ----------------
P.dilr_set(2, "Set 2 — Tempos and trucks on an island", DIR,
 p("A logistics company works on an island nation of 20 districts, each split into 5 sub-districts. It has a major collection centre at each district headquarters and a minor collection centre at each of the 100 sub-district headquarters. Every district headquarters is connected to every other, and the journey between any two takes exactly 4 hours. Each sub-district headquarters is connected only to its own district headquarters, 1 hour away.") +
 p("Each minor centre has exactly one tempo, which goes to its district’s major centre, delivers, collects the shipments for its minor centre, and returns the same day. Each major centre has exactly one truck dedicated to each other major centre; it goes there, delivers, collects the shipments headed back, and returns the same day.") +
 p("No time is lost anywhere, and loading and unloading take no time. Each tempo and truck makes exactly one round trip a day. Customers drop off shipments through the day; on the way back each vehicle collects everything waiting for its home centre at that moment, and anything dropped later goes the next day. Recipients collect shipments from the centres."),
 "DILR::LR::Routes_and_Networks",
 steps(("Now", p("100 tempos (2-hour round trips) and 20 × 19 = 380 trucks (8-hour round trips).")),
       ("With zones", p("Inside a zone of k districts, each major centre has a truck to each of the other k − 1. Hubs also run the stated number of trucks to each other hub.")),
       ("Longest road trip", p("Without zones: minor → major → major → minor = 1 + 4 + 1 = 6 hours. With two zones the worst case adds two 4-hour legs (to the hub, across, from the hub)."))) +
 final("Count vehicles per centre, then multiply."),
 p("Each question changes the network; recount trucks per centre and per hub."),
 p("<b>Complete networks:</b> k centres with one dedicated truck per pair per direction need k(k − 1) trucks."))
P.dq(6, "How many tempos and trucks does the company need in all?", [], "TITA", "480", "Easy",
 "One tempo per minor centre; 19 trucks per major centre.", steps(("Count", p("100 + 20 × 19 = 480."))) + final("480"))
P.dq(7, "Twenty years ago, short of funds, the company split the 20 districts into four zones of five. One district in each zone was the zone’s hub, and only hubs were connected to hubs in other zones; other districts were connected only within their zone. Besides the tempos and trucks described above, each hub ran five dedicated trucks to each other hub. How many tempos and trucks did the company have then?", [], "TITA", "240", "Medium",
 "Within-zone trucks plus hub trucks plus tempos.",
 steps(("Tempos", p("100.")), ("Within zones", p("Each zone: 5 × 4 = 20; four zones: 80.")), ("Hubs", p("4 hubs × 3 other hubs × 5 = 60.")), ("Total", p("100 + 80 + 60 = 240."))) + final("240"))
P.dq(8, "Ten years ago the company used two zones of ten districts, with one hub in each; only the hubs were connected across zones, and each hub ran ten dedicated trucks to the other hub, besides the tempos and trucks described above. A tempo uses 3 litres of diesel per running hour and a truck 5 litres. With every vehicle running daily, how many litres of diesel were needed each day?", ["8000", "8300", "8600", "9000"], "MCQ", "3", "Medium",
 "Round trips: tempo 2 hours, truck 8 hours.",
 steps(("Tempos", p("100 × 2 × 3 = 600.")), ("Zone trucks", p("2 × 10 × 9 = 180 trucks × 8 × 5 = 7200.")), ("Hub trucks", p("20 × 8 × 5 = 800.")), ("Total", p("600 + 7200 + 800 = 8600."))) + final("Option 3"),
 [("1", "Leaves out the hub trucks."), ("2", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(9, "With the two-zone network of ten years ago (as in the previous question), let T1 be the longest time a shipment might spend on the road from origin to destination, and T2 the same now, with no zones. What is T1 − T2 (in hours)?", ["7", "6", "9", "8"], "MCQ", "4", "Medium",
 "The worst case crosses zones between two non-hub districts.",
 steps(("Then", p("1 + 4 (to hub) + 4 (hub to hub) + 4 (to district) + 1 = 14.")), ("Now", p("1 + 4 + 1 = 6.")), ("Difference", p("8."))) + final("Option 4"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])

# ---------------- Set 3: A three-round championship (Q10–14) ----------------
ROUNDS = table(["Player", "Elim 1", "Elim 2", "Final"], [["A", "5 or 9", "6", "19"], ["B", "7", "14", "6 or 10"], ["C", "11", "10", "10 or 6"], ["D", "9 or 5", "5", "—"], ["E", "3", "—", "—"]])
P.dilr_set(3, "Set 3 — The Open Show Championship", DIR,
 p("Five friends, A, B, C, D and E, held a championship of three rounds, Eliminator 1, Eliminator 2 and the Final, each of 14 games. All five play Eliminator 1 and the lowest scorer is out; the remaining four play Eliminator 2 and the lowest scorer is out; the last three play the Final.") +
 p("In each round, games 1–10 are ‘Mini’ games worth 1 point to the winner, games 11–13 are ‘Major’ games worth 5 points, and game 14 is the ‘Prime’ game worth 10 points.") +
 "<ul><li>Each round’s Prime game had a different winner; C won it in Eliminator 1.</li><li>No player won more than one Major game in a round.</li><li>No player won more than 5 Mini games in a round.</li>"
 "<li>The difference between B’s and C’s points was the same in all three rounds.</li><li>The players’ points formed an arithmetic progression in exactly one round.</li><li>No one scored 0 in any round.</li>"
 "<li>A scored 6 and D scored 5 in the same round. A won the championship by winning the Final with 19 points.</li></ul>",
 "DILR::LR::Games_and_Tournaments",
 steps(("Points per round", p("10 + 3 × 5 + 10 = 35 in every round.")),
       ("Which round is the AP", p("Four terms in AP sum to 4a + 6d, which is even, and three terms to 3(a + d); neither can be 35. So the AP is Eliminator 1, with middle term 7. Difference 1 tops out at 9, below C’s 10 or more. Difference 3 (1, 4, 7, 10, 13) uses up all the Minis and leaves the 10-scorer needing two Majors. So 3, 5, 7, 9, 11, and C has 11.")),
       ("Eliminator 2", p("E (3) is out. A 6 and D 5 must be here (A can’t be 6 in the Final), so B + C = 24 with B’s Prime 10. Only B 14, C 10 keeps the rules: a gap of 4.")),
       ("Final", p("A 19 (Prime + Major + 4 Minis); B and C share 16 with a gap of 4: 10 and 6. In Eliminator 1, B has the 7 (gap 4 to C’s 11), and A, D are 5 and 9.") + ROUNDS)) +
 final("Only the A/D split in Eliminator 1 and the B/C split in the Final are open."),
 p("Each round gives out exactly 35 points; start from the AP round."),
 p("<b>Fixed totals:</b> an AP with a known sum fixes its middle term."))
P.dq(10, "Who won the three Major games in Eliminator 1?", ["A, B, C", "A, B, D", "A, C, D", "B, C, D"], "MCQ", "2", "Medium",
 "C’s 11 is Prime + 1 Mini.",
 steps(("Minis", p("C 1, E 3, B 2 (7 = 5 + 2), the 9-scorer 4 (9 = 5 + 4): all 10 Minis used, so the 5-scorer’s 5 is a Major.")),
       ("Majors", p("B, and both of A and D."))) + final("Option 2"),
 [("1", "C won no Major."), ("3", "B won one."), ("4", "C won no Major.")])
P.dq(11, "Who was eliminated in Eliminator 1?", ["D", "E", "Either D or E", "None of the above"], "MCQ", "2", "Easy",
 "Lowest score in the AP.", steps(("Out", p("E, with 3."))) + final("Option 2"),
 [("1", "D plays Eliminator 2."), ("3", "Only E."), ("4", "E is listed.")])
P.dq(12, "How many points did B score in Eliminator 2?", [], "TITA", "14", "Medium",
 "B won that round’s Prime.", steps(("B", p("A 6 and D 5 leave B + C = 24. The gap of 4 from Eliminator 1 (B 7, C 11) gives B 14, C 10."))) + final("14"))
P.dq(13, "Which statement is definitely correct?", ["A won 1 Major game and 4 Mini games in Eliminator 1.", "C won 2 Major games in Eliminator 2.", "B won 1 Major game and 2 Mini games in Eliminator 1.", "None of these"], "MCQ", "3", "Medium",
 "B’s 7 in Eliminator 1.", steps(("Check", p("7 can’t be all Minis (max 5), so 5 + 2. A may have 5 or 9; no one wins 2 Majors."))) + final("Option 3"),
 [("1", "A may have scored 5."), ("2", "Never two Majors."), ("4", "Option 3 holds.")])
P.dq(14, "What is the difference between A’s and C’s points in Eliminator 2?", [], "TITA", "4", "Easy",
 "A 6, C 10.", steps(("Difference", p("4."))) + final("4"))

# ---------------- Set 4: A cave system (Q15–18) ----------------
CHAIN = table(["Cave", "Visitors"], [["C-8 … C-5", "n, n + 1, n + 2, n + 3"], ["B-4, B-3", "2n + 1, 2n + 5"], ["C-4 = B-2", "2n + 6"], ["C-3 … C-1", "2n + 7, 2n + 8, 2n + 9"], ["A-2, A-1", "4n + 6, 8n + 30"]])
P.dilr_set(4, "Set 4 — Fourteen caves", DIR,
 p("An amusement park has an artificial cave system of 14 caves, with one entrance and eight exits, as shown. Visitors enter at the entrance, move along the paths shown, visit each cave at most once, and leave through one exit.") + F.CAVES +
 "<ul><li>More visitors went through A-1 than A-2.</li><li>B-1 had the most visitors among the four B caves, followed by B-2, B-3 and B-4, in that order.</li><li>Similarly, C-1 had the most among the eight C caves, followed by C-2, C-3, …, C-8, in that order.</li><li>At least one visitor went through each of the 14 caves.</li></ul>",
 "DILR::LR::Routes_and_Networks",
 steps(("Flows", p("Each cave’s visitors split among the caves after it: B-1 = C-1 + C-2 + C-3, B-2 = C-4, B-3 = C-5 + C-6, B-4 = C-7 + C-8, A-1 = B-1 + B-2, A-2 = B-3 + B-4.")),
       ("Smallest counts", p("With C-8 = n and every other value as small as the order allows (C-4 = B-2 must exceed B-3):") + CHAIN)) +
 final("Minimise from the bottom up; the orders force the gaps."),
 p("Write every cave in terms of the eight C caves."),
 p("<b>Flow conservation:</b> what enters a cave leaves it, so parents are sums of children."))
P.dq(15, "What is the least possible difference between the numbers of people who went through A-1 and A-2?", ["22", "24", "28", "30"], "MCQ", "3", "Medium",
 "Minimise with n = 1.", steps(("Difference", p("(8n + 30) − (4n + 6) = 4n + 24, least 28 at n = 1."))) + final("Option 3"),
 [("1", "Ignores B-2 > B-3."), ("2", "n = 0 isn’t allowed."), ("4", "Not the least.")])
P.dq(16, "If 7 visitors went through B-4, at least how many went through C-2?", ["12", "13", "14", "Cannot be determined"], "MCQ", "3", "Medium",
 "C-7 + C-8 = 7, so C-7 is 4, 5 or 6.",
 steps(("B-3", p("C-7 = 4 gives C-6 ≥ 5, C-5 ≥ 6, B-3 ≥ 11 (larger C-7 only raises it).")), ("Up the chain", p("C-4 = B-2 ≥ 12, C-3 ≥ 13, C-2 ≥ 14."))) + final("Option 3"),
 [("1", "That is B-2."), ("2", "That is C-3."), ("4", "A minimum exists.")])
P.dq(17, "The numbers through A-2, B-4, C-7 and C-8 were all primes. What is the least possible number through A-1?", ["42", "48", "53", "58"], "MCQ", "4", "Hard",
 "Smallest primes for C-8, C-7, then make A-2 prime.",
 steps(("Bottom", p("C-8 = 2, C-7 = 3, B-4 = 5. B-3 ≥ 9 (C-6 ≥ 4, C-5 ≥ 5), and A-2 = B-3 + 5 must be prime: B-3 = 12 gives 17 (C-5, C-6 = 8, 4).")),
       ("Top", p("C-4 = B-2 ≥ 13, then C-3, C-2, C-1 ≥ 14, 15, 16: B-1 = 45, A-1 = 58."))) + final("Option 4"),
 [("1", "A-2 not prime."), ("2", "A-2 not prime."), ("3", "Arithmetic slip.")])
P.dq(18, "What is the largest possible number of caves with a prime number of visitors?", ["9", "10", "11", "12"], "MCQ", "4", "Hard",
 "2 can be used only once; the B-3 group can’t be all prime.",
 steps(("Bound", p("Only one cave can hold the even prime 2, and it must be C-8 (every other cave is larger than some cave). So if C-5 and C-6 are both prime, B-3 is even; if B-1 and B-2 are both prime, A-1 is even. At least one cave in each of those two trios is not prime: at most 12.")),
       ("Example", p("C: 23, 19, 17, 13, 7, 5, 3, 2; B: 59, 13, 12, 5; A: 72, 17. Primes everywhere except B-3 and A-1: 12."))) + final("Option 4"),
 [("1", "Too few."), ("2", "Too few."), ("3", "One more is possible.")])

# ---------------- Set 5: Seminar week (Q19–22) ----------------
LAYOUT = table(["Slots", "Use"], [["1–3", "Literature"], ["4–6", "empty"], ["7–10", "Philosophy"], ["11", "empty"], ["12–16", "Mathematics"]])
ARR = ("<ul><li>Either slot 1 holds R or W and slots 2–3 hold T and V; then S is in 8 and slots 7–10 are M/N, S, N/M, P.</li>"
       "<li>Or slots 1–2 hold T and V and slot 3 holds R or W; then S is in 9 and slots 7–10 are P, M/N, S, N/M.</li>"
       "<li>Slots 12–16 are always U, O, Q, then W or R, then X.</li></ul>")
P.dilr_set(5, "Set 5 — Twelve lectures in sixteen slots", DIR,
 p("A university is scheduling 12 lecture sessions, M to X, in 16 time slots in a seminar week: five in Mathematics, three in Literature and four in Philosophy. One session per slot. Sessions of a subject must be in consecutive slots with no gap, and there must be at least one empty slot between different subjects. Slot 1 is used.") +
 "<ul><li>M and N are Philosophy sessions with exactly one session between them.</li><li>T and V are in consecutive slots, before all the Mathematics sessions.</li>"
 "<li>The slots of R, S and W, taken in that order, form an arithmetic progression (the common difference may be negative); the three are in different subjects.</li>"
 "<li>X is in slot 16.</li><li>U is in the slot just after an empty slot.</li><li>P and Q are in different subjects, and P’s subject has fewer sessions than Q’s.</li>"
 "<li>O is exactly three slots after the last Philosophy session.</li></ul>",
 "DILR::LR::Scheduling",
 steps(("Who is Mathematics", p("M, N (Philosophy), T, V (before Maths), P (its subject has fewer than another’s) and two of R, S, W are not Maths: seven sessions. So the other five, U, O, Q, X and one of R/S/W, are.")),
       ("Blocks", p("X in 16 puts Maths in 12–16, with U in 12 after an empty 11 and O in 13. O is three after Philosophy’s end, so Philosophy is 7–10, and Literature takes 1–3 with 4–6 empty.") + LAYOUT),
       ("R, S, W", p("S is the Philosophy one; R and W are slot 1 or 3 and 15. Q, the remaining Maths session, is 14.")),
       ("Arrangements", ARR)) +
 final("Subjects are fixed except for R and W."),
 p("Count the sessions that can’t be Mathematics; the rest must be."),
 p("<b>Block scheduling:</b> with fixed block sizes and a fixed number of empty slots, a couple of anchors place every block."))
P.dq(19, "Which of the following must be a Mathematics session?", ["P", "Q", "R", "T"], "MCQ", "2", "Easy",
 "The five Maths sessions include U, O, Q, X.", steps(("Q", p("Q is in slot 14."))) + final("Option 2"),
 [("1", "P is Philosophy."), ("3", "R may be Literature."), ("4", "T is Literature.")])
P.dq(20, "For how many of the 12 sessions can the slot be uniquely determined?", ["12", "10", "8", "Less than 8"], "MCQ", "4", "Medium",
 "List the fixed ones.", steps(("Fixed", p("U 12, O 13, Q 14, X 16: four. S is 8 or 9, and the rest move."))) + final("Option 4"),
 [("1", "Many alternatives."), ("2", "Too many."), ("3", "Too many.")])
P.dq(21, "For how many of the 12 sessions can the subject be uniquely determined?", ["12", "10", "9", "Less than 9"], "MCQ", "2", "Medium",
 "Only R and W swap subjects.", steps(("Count", p("12 − 2 = 10."))) + final("Option 2"),
 [("1", "R and W are open."), ("3", "Too few."), ("4", "Too few.")])
P.dq(22, "Ignoring empty slots, which of the following cannot be three consecutive sessions, in that order?", ["T, R and P", "R, P and N", "S, N and U", "P, S and M"], "MCQ", "4", "Medium",
 "P is at the edge of the Philosophy block, next to M or N.",
 steps(("Check", p("V, T, R, P (1); R, P, N, S (2); M, S, N, U (3). P is always beside M or N, never S, so (4) fails."))) + final("Option 4"),
 [("1", "R in slot 3, P in 7."), ("2", "P at 7, N at 8."), ("3", "S 8, N 9, then U.")])
