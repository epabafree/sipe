# -*- coding: utf-8 -*-
# Simp Mock 11 (2025): DILR (22 of 22).
from fmt import steps, final, trap, why, table, p
from m25_11 import P
import m25_11_figs as F

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Municipal election (Q1–5) ----------------
PCT = table(["Candidate", "Share of valid votes"], [["Amit", r"\(47\tfrac18\%\)"], ["Bibhuti", r"\(22\tfrac17\%\)"], ["Chitra", r"\(13\tfrac16\%\)"], ["Debu", r"\(10\tfrac pq\%\)"], ["Esha", r"\(7\tfrac15\%\)"]])
VOTES = table(["Candidate", "Votes"], [["Amit", "39,585"], ["Bibhuti", "18,600"], ["Chitra", "11,060"], ["Debu", "8,707"], ["Esha", "6,048"]])
P.dilr_set(1, "Set 1 — A municipal election", DIR,
 p("A small town has fewer than one lakh voters, all of whom voted in the latest municipal election. Each voter went to a polling booth, and each booth served exactly one thousand voters. Five candidates contested, and the valid votes they received together equalled the number of eligible voters. The table gives each candidate’s share of the votes.") + PCT +
 p("Here p and q are coprime natural numbers."),
 "DILR::DI::Caselets",
 steps(("Debu’s share", p(r"\(100 - 89 - \left(\tfrac18 + \tfrac17 + \tfrac16 + \tfrac15\right) = 11 - \tfrac{533}{840} = 10\tfrac{307}{840}\%\).")),
       ("Booths", p(r"With N booths, Debu gets \(1000N \times \tfrac{8707}{84000} = \tfrac{8707N}{84}\). 8707 shares no factor with 84, so N is a multiple of 84; under one lakh voters, N = 84 and there are 84,000 voters.")),
       ("Votes", VOTES)) +
 final("84 booths, 84,000 voters."),
 p("Work out Debu’s share first; whole votes then force the voter count to a multiple of 84,000."),
 p("<b>Whole-number votes:</b> a fractional percentage must give whole votes, which fixes the total."))
P.dq(1, "How many polling booths were used in the election?", ["57", "64", "72", "84"], "MCQ", "4", "Medium",
 "Debu’s votes are 8707N/84.", steps(("N", p("A multiple of 84 below 100: 84."))) + final("84, option 4"),
 [("1", "Gives fractional votes."), ("2", "Gives fractional votes."), ("3", "Gives fractional votes.")])
P.dq(2, "How many votes did Debu receive?", ["8077", "8707", "8817", "8897"], "MCQ", "2", "Easy",
 "8707 × 84 ÷ 84.", steps(("Debu", p("8,707."))) + final("Option 2"),
 [("1", "Digits swapped."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(3, "What is the difference between the highest and lowest numbers of votes received by a candidate?", ["33537", "31779", "30535", "29974"], "MCQ", "1", "Easy",
 "Amit minus Esha.", steps(("Difference", p("39,585 − 6,048 = 33,537."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(4, "What is the median number of votes received by the candidates other than Esha?", ["12428", "14432", "14630", "14830"], "MCQ", "4", "Easy",
 "Four values: the average of the middle two.", steps(("Median", p("(18,600 + 11,060) ÷ 2 = 14,830."))) + final("Option 4"),
 [("1", "Arithmetic slip."), ("2", "Arithmetic slip."), ("3", "Arithmetic slip.")])
P.dq(5, "The number of voters would exceed one lakh if it grew by x%. What is the smallest natural number x?", [], "TITA", "20", "Easy",
 "84,000 × (1 + x/100) > 1,00,000.", steps(("x", p(r"\(x > 19.05\): smallest natural number 20."))) + final("20"))

# ---------------- Set 2: Pets in six houses (Q6–9) ----------------
CASES = ("<ul><li><b>Case 1</b>: 1W parakeet, turtle · 2W dog, hamster · 3W duck, sheep</li><li><b>Case 2</b>: 1W parakeet, turtle · 2W dog, duck · 3W hamster, sheep</li>"
         "<li><b>Case 3</b>: 1W parakeet, sheep · 2W dog, hamster · 3W duck, turtle</li><li><b>Case 4</b>: 1W parakeet, sheep · 2W dog, duck · 3W hamster, turtle</li></ul>")
P.dilr_set(2, "Set 2 — Pets on both sides of the road", DIR,
 p("A colony has six houses in two rows on either side of a road. Houses 1E, 2E and 3E face east; houses 1W, 2W and 3W face west. Each east house directly faces the matching west house (1E faces 1W, and so on), and 2E lies between 1E and 3E.") +
 p("Each house has two pets of different types, and no two houses have the same combination. The colony has seven types of pet: chinchilla, hamster, dog, parakeet, duck, turtle and sheep, all of them present.") +
 "<ul><li>The six pets in the west houses are all of different types; this is not true of the east houses.</li><li>Dogs live in three houses and parakeets in two.</li><li>House 3E has a duck and a hamster. There is one more hamster and one more duck in the colony.</li><li>Exactly two pairs of facing houses share one common pet type. One such pair is 2E and 2W, which both have a dog.</li><li>No west house has a chinchilla. Among the west houses, the turtle, the sheep and the dog are in three separate houses.</li></ul>",
 "DILR::LR::Puzzles",
 steps(("East houses", p("The west has only one dog (all its pets differ), so the other two dogs are in 1E and 2E. The chinchilla must be in 1E or 2E too. The west’s six different pets are turtle, sheep, dog and one each of hamster, parakeet and duck; so the second parakeet is in 1E or 2E. East: (dog, chinchilla), (dog, parakeet), (duck, hamster).")),
       ("Which is which", p("2W has a dog and a second pet. If 1E had the parakeet, 2W couldn’t (that would repeat 1E’s combination), and then either 1W shares the parakeet and 3W a duck or hamster (three sharing pairs), or neither shares (one pair). So 1E = dog + chinchilla, 2E = dog + parakeet.")),
       ("West houses", p("2W can’t have the parakeet (it would copy 2E), so it has a hamster or duck. For exactly one more sharing pair, 1W takes the parakeet and 3W the other of hamster and duck. Turtle and sheep split between 1W and 3W.")),
       ("Four cases", CASES)) +
 final("The east houses are fixed; four arrangements remain for the west."),
 p("Count the dogs first: the west can hold only one."),
 p("<b>Pair-sharing clues:</b> count how many facing pairs each placement would make share."))
P.dq(6, "For how many of the six houses can both pets be determined uniquely?", [], "TITA", "3", "Medium",
 "The east side is fixed.", steps(("Count", p("1E, 2E and 3E."))) + final("3"))
P.dq(7, "Which pet is definitely in house 1W?", ["Sheep", "Turtle", "Duck", "Parakeet"], "MCQ", "4", "Easy",
 "In every case 1W has the parakeet.", steps(("1W", p("Parakeet, with a turtle or a sheep."))) + final("Option 4"),
 [("1", "Only in cases 3 and 4."), ("2", "Only in cases 1 and 2."), ("3", "Never in 1W.")])
P.dq(8, "If a duck lives next door to a turtle (adjacent houses on the same side of the road), which of the following is true?", ["Dogs are in 1E and 1W.", "Hamsters are in 2E and 3W.", "Parakeets are in 1E and 2W.", "Ducks are in 3E and 2W."], "MCQ", "4", "Medium",
 "The turtle is in 1W or 3W; its west neighbour must have the duck.",
 steps(("Cases", p("Turtle in 1W needs the duck in 2W (case 2). Turtle in 3W needs the duck in 2W (case 4). Either way the ducks are in 3E and 2W."))) + final("Option 4"),
 [("1", "1W never has a dog."), ("2", "2E has no hamster."), ("3", "1E has no parakeet.")])
P.dq(9, "If the two hamsters are not in houses facing each other, how many arrangements are possible?", [], "TITA", "2", "Easy",
 "3E has a hamster; 3W must not.", steps(("Cases", p("Cases 1 and 3."))) + final("2"))

# ---------------- Set 3: Two warehouses (Q10–13) ----------------
FLOW = table(["Mo.", "A closing", "Transfer"], [["Oct", "300 → 300", "—"], ["Nov", "50 → 350", "300 B→A"], ["Dec", "500 → 500", "—"], ["Jan", "550 → 450", "100 A→B"], ["Feb", "−50 → 150", "200 B→A"], ["Mar", "100 → 0", "100 A→B"]])
P.dilr_set(3, "Set 3 — Two warehouses", DIR,
 p("A large water-tank retailer has two warehouses, A (north of the city) and B (south). Each buys stock from manufacturers only on the first day of each month, based on that month’s sales projection: monthly sales projection = opening stock + purchase. A month’s closing stock is the next month’s opening stock. The graphs give each warehouse’s opening stock, purchase and sales (in tanks) for October 2024 to March 2025. No tanks were defective or damaged. At the end of 31 March 2025 both warehouses had sold out completely.") +
 p("<b>Warehouse A</b>") + F.WA + p("<b>Warehouse B</b>") + F.WB +
 "<ul><li>Tanks may be transferred between the warehouses, at most once a month.</li><li>A transfer is judged ‘bad’ if the receiving warehouse could have met that month’s sales without it.</li><li>The projection team gets a special incentive in a month if the city’s actual sales lie within ±20% of the city’s monthly sales projection.</li></ul>",
 "DILR::DI::Graphs_and_Charts",
 steps(("Transfers at A", p("Opening + purchase − sales gives the expected closing stock; the gap to the actual closing (next month’s opening; 0 in March) is the transfer. Expected → actual:") + FLOW),
       ("Check with B", p("B’s figures balance with the same transfers: for example November 50 + 1000 − 650 − 300 = 100, December’s opening.")),
       ("City projections", p("Sales as a share of projection: Oct 1950/2300 ≈ 84.8%; Nov 1750/2200 ≈ 79.5%; Dec 1150/1900 ≈ 60.5%; Jan 1550/2050 ≈ 75.6%; Feb 1950/2200 ≈ 88.6%; Mar 1800/1800 = 100%."))) +
 final("Transfers in November, January, February and March."),
 p("Expected closing = opening + purchase − sales; compare with the next opening."),
 p("<b>Stock flow:</b> any unexplained gain or loss in stock is a transfer."))
P.dq(10, "How many times in these six months did an inter-warehouse transfer take place?", [], "TITA", "4", "Medium",
 "Compare A’s expected and actual closing.", steps(("Count", p("November, January, February, March."))) + final("4"))
P.dq(11, "How many times in these six months did a transfer turn out to be ‘bad’?", [], "TITA", "1", "Medium",
 "Could the receiver have met its sales alone?",
 steps(("Check", p("Nov: A had 300 + 850 = 1150 ≥ 1100, so bad. Jan: B had 1050 < 1100. Feb: A had 1250 < 1300. Mar: B had 700 < 800."))) + final("1"))
P.dq(12, "How many times in these six months did the projection team earn the special incentive?", ["1", "2", "3", "4"], "MCQ", "3", "Medium",
 "City sales within 80–120% of city projection.", steps(("Months", p("October, February, March."))) + final("3, option 3"),
 [("1", "Misses two."), ("2", "Misses March (100%)."), ("4", "November is 79.5%.")])
P.dq(13, "In how many of these months was Warehouse A’s closing stock less than 50% of its sales?", ["0", "2", "3", "4"], "MCQ", "4", "Easy",
 "Closing ÷ sales for A.", steps(("Months", p("Oct 300/950, Nov 350/1100, Feb 150/1300, Mar 0/1000: four. December and January are above half."))) + final("4, option 4"),
 [("1", "Several are below."), ("2", "Misses two."), ("3", "Misses March.")])

# ---------------- Set 4: Interhouse chess (Q14–17) ----------------
CH = table(["Case", "A v P", "A v R", "S, T beat"], [["1A", "A", "R", "B, C"], ["1B", "A", "R", "C, B"], ["2A", "P", "A", "B, C"], ["2B", "P", "A", "C, B"]])
P.dilr_set(4, "Set 4 — Interhouse chess", DIR,
 p("In a school’s annual interhouse rapid-chess competition, four students of Water House and four of Earth House reached the final round, where each Water House student played one match against each Earth House student. Matches won — Water House: Anushka 3, Bidisha 2, Chandrakant 1, Divya 2. Earth House: Priyanka 2, Rimjhim 3, Saloni 2, Tina 1.") +
 p("Anushka beat Tina, Bidisha beat Priyanka, Chandrakant lost to Rimjhim, and Saloni beat Divya. Every match had a winner."),
 "DILR::LR::Games_and_Tournaments",
 steps(("Totals", p("16 matches; Water House won 8 and Earth House 8.")),
       ("Branch on Anushka v Priyanka", p("If Anushka won: Priyanka beat Chandrakant and Divya; Divya beat Rimjhim and Tina; Rimjhim beat Anushka, Bidisha and Chandrakant; Anushka beat Saloni. If Priyanka won: Anushka beat Rimjhim and Saloni; Rimjhim beat Bidisha, Chandrakant and Divya; Divya beat Priyanka and Tina; Priyanka beat Chandrakant.")),
       ("Saloni and Tina", p("Saloni’s other win and Tina’s single win split Bidisha and Chandrakant either way.")),
       ("Cases", CH + p("Initials: A Anushka, B Bidisha, C Chandrakant, P Priyanka, R Rimjhim, S Saloni, T Tina. Divya beats Tina in every case."))) +
 final("Four possible result tables."),
 p("Anushka’s result against Priyanka decides most of the table."),
 p("<b>Round-robin tables:</b> fill rows and columns to their win totals; branch on the least-constrained match."))
P.dq(14, "Which two players won their matches against Priyanka?<br>(i) Anushka and Bidisha<br>(ii) Bidisha and Divya<br>(iii) Chandrakant and Bidisha", ["(i) or (iii)", "(ii) or (iii)", "(i) or (ii)", "Only (ii)"], "MCQ", "3", "Medium",
 "Bidisha always; the other is Anushka or Divya.", steps(("Cases", p("Case 1: Anushka and Bidisha. Case 2: Bidisha and Divya."))) + final("Option 3"),
 [("1", "Chandrakant never beats Priyanka."), ("2", "Same."), ("4", "(i) is also possible.")])
P.dq(15, "Which of the following is definitely true?", ["Tina won against Bidisha.", "Chandrakant won against Saloni.", "Anushka won against Priyanka.", "Divya won against Tina."], "MCQ", "4", "Medium",
 "Which result is the same in all cases?", steps(("Fixed", p("Divya beats Tina in every case."))) + final("Option 4"),
 [("1", "Only in some cases."), ("2", "Only in some cases."), ("3", "Only in case 1.")])
P.dq(16, "If Anushka won against Rimjhim, for how many matches can the result not be determined?", [], "TITA", "4", "Medium",
 "That is case 2.", steps(("Open", p("Saloni v Bidisha, Saloni v Chandrakant, Tina v Bidisha, Tina v Chandrakant."))) + final("4"))
P.dq(17, "If Tina won against Chandrakant, for how many matches can the result be determined?", [], "TITA", "12", "Medium",
 "Then Saloni beat Bidisha; cases 1A and 2A remain.", steps(("Open", p("Anushka v Priyanka, Anushka v Rimjhim, Divya v Priyanka, Divya v Rimjhim are open: 16 − 4 = 12 fixed."))) + final("12"))

# ---------------- Set 5: Car hire between cities (Q18–22) ----------------
P.dilr_set(5, "Set 5 — Car hire between cities", DIR,
 p("Mr Bhave handles sales and distribution for a food-products company in seven cities, A, J, M, N, P, R and S, connected by the roads shown (lengths in km).") + F.ROADS +
 p("By company policy he may travel only in cars hired from Swift Cabs or Highway Cars:") +
 "<ul><li>Swift Cabs charges ₹14 per km for the first 100 km and ₹8 per km after that, for each car hired.</li><li>Highway Cars charges ₹12 per km for the first 200 km and ₹6 per km after that, for each car hired.</li><li>If he visits clients in a city, he must hire a new car (from either agency) for the next stretch.</li><li>If he only passes through a city without visiting clients, he can keep the same car.</li></ul>",
 "DILR::LR::Routes_and_Networks",
 steps(("Costs", p(r"Swift for d km: 14d up to 100, then 1400 + 8(d − 100). Highway: 12d up to 200, then 2400 + 6(d − 200).")),
       ("Rule", p("Each client visit ends a hire, so price each stretch between visits separately."))) +
 final("Price each hired stretch with the right tariff."),
 p("Split the trip at client visits; each stretch is a separate hire."),
 p("<b>Tiered tariffs:</b> long stretches favour the cheaper later rate."))
P.dq(18, "Mr Bhave is in city P. He must visit clients in A and S and return to P, without passing through M (flooded). What is his least cost if every stretch uses the same agency?", ["Rs. 11880", "Rs. 12500", "Rs. 13000", "Rs. 13840"], "MCQ", "1", "Hard",
 "P → A (visit) → S (visit) → P, via J both ways.",
 steps(("Stretches", p("P–J–A 520 km, A–S 180 km, S–A–J–P 700 km (passing A without a visit).")),
       ("Highway Cars", p("4,320 + 2,160 + 5,400 = 11,880. Swift Cabs: 4,760 + 2,040 + 6,200 = 13,000."))) + final("Option 1"),
 [("2", "Not a route total."), ("3", "Swift Cabs."), ("4", "Uses a longer route.")])
P.dq(19, "What is the shortest distance at which the two agencies charge the same?", ["120 km", "150 km", "250 km", "350 km"], "MCQ", "2", "Easy",
 "Between 100 and 200 km: 1400 + 8(d − 100) = 12d.", steps(("Solve", p("600 = 4d: d = 150."))) + final("Option 2"),
 [("1", "Costs differ."), ("3", "Costs differ."), ("4", "Costs differ.")])
P.dq(20, "Mr Bhave travels from A to M, visiting clients in every city on the way, using only one agency. Which combination is cheapest?", ["Swift Cabs, route A-J-P-M", "Swift Cabs, route A-N-R-M", "Highway Cars, route A-J-P-M", "Highway Cars, route A-N-R-M"], "MCQ", "4", "Medium",
 "Price each road separately.",
 steps(("Costs", table(["Route", "Swift", "Highway"], [["A-J-P-M", "7,960", "7,920"], ["A-N-R-M", "6,200", "6,180"]], hi={(1, 2)}))) + final("Option 4"),
 [("1", "7,960."), ("2", "6,200."), ("3", "7,920.")])
P.dq(21, "Mr Bhave travels from M to S with no client visits on the way. What is the least cost of the journey?", ["Rs. 7080", "Rs. 6900", "Rs. 6300", "Rs. 5580"], "MCQ", "4", "Medium",
 "One car; take the shortest route.",
 steps(("Route", p("M–R–N–A–S: 730 km, the shortest.")), ("Cost", p("Highway Cars: 2,400 + 530 × 6 = 5,580 (Swift: 6,440)."))) + final("Option 4"),
 [("1", "A longer route."), ("2", "A longer route."), ("3", "Arithmetic slip.")])
P.dq(22, "Considering both agencies, what is the difference between the highest and lowest cost of travelling a single road between two directly connected cities?", ["Rs. 2460", "Rs. 2600", "Rs. 2740", "Rs. 2850"], "MCQ", "2", "Easy",
 "Longest road P–J (370 km); shortest J–N (80 km).",
 steps(("Highest", p("P–J by Swift: 1,400 + 270 × 8 = 3,560.")), ("Lowest", p("J–N by Highway: 960.")), ("Difference", p("2,600."))) + final("Option 2"),
 [("1", "Uses Highway Cars for P–J."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
