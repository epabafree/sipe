# -*- coding: utf-8 -*-
# Simp Mock 6: DILR (20 of 20).
from fmt import steps, final, trap, why, table, p
from m06 import P

DIR = "Read the information below and answer the questions that follow."

# ---------------- Set 1: Houses on a road (Q1–5) ----------------
HOUSES = table(["Pos", "North row", "South row"], [["1", "Gupta", "Sen"], ["2", "Singh", "Bose"], ["3", "Ahuja", "Tilak"],
                                                   ["4", "Bhalla / Pathak", "Pathak / Bhalla"], ["5", "Arora", "Sharma"]])
P.dilr_set(1, "Set 1 — Ten houses facing a road", DIR,
 p("Ten families live in identical houses along a straight road, five on each side, each house directly opposite one on the other side. The families are Ahuja, Arora, Bhalla, Bose, Gupta, Pathak, Sen, Sharma, Singh and Tilak.") +
 p("Each person describes ‘left’ and ‘right’ as seen while standing at his own front gate, facing the road. So when a person talks about houses in the other row, the true directions (as seen from that row) are reversed. For example, if Tilak and Sharma live on opposite sides and Tilak says ‘three houses are to the left of Sharma’s’, then from Sharma’s side there are three houses to his right.") +
 p("‘Immediate neighbour’ means the next house in the same row. The statements:") +
 "<ol><li>Pathak: ‘The numbers of houses to my left and to my right are the same as the numbers to the left and right of Bhalla’s house, respectively. Bhalla has at least one house on each side.’</li>"
 "<li>Bose: ‘The number of houses to the left of Bhalla’s house equals the number to my right. Sen is my immediate neighbour.’</li>"
 "<li>Ahuja: ‘The number of houses to the left of Pathak’s house equals the number to the right of Singh’s house.’</li>"
 "<li>Sen: ‘Neither Pathak nor Bhalla is my immediate neighbour. The numbers of houses to my left and right are the same as the numbers to the left and right of Gupta’s house, respectively.’</li>"
 "<li>Gupta: ‘Ahuja’s house is two places to the left of mine, and Sharma’s house is two places to the left of Tilak’s. Ahuja is not Bose’s neighbour.’</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Opposite pairs", p("Number the positions 1–5 along the road. Equal counts on a speaker’s left and right are possible only for the house directly opposite, so Pathak faces Bhalla (not at an end) and Sen faces Gupta.")),
       ("Mirror positions", p("Bose’s statement means Bose’s position and Bhalla’s add up to 6; Ahuja’s statement means Singh’s and Pathak’s add up to 6. Pathak and Bhalla share a position, so Bose and Singh share one too: they face each other. Bhalla cannot be at 3 (three houses at position 3), so take Bhalla at 4 (the mirror image gives the same arrangement); Bose and Singh are at 2.")),
       ("Sen and Gupta", p("Sen is next to Bose, at 1 or 3, but not next to Pathak or Bhalla (at 4), so Sen is at 1 and Gupta faces him at 1, in Singh’s row.")),
       ("The rest", p("Ahuja is two places to Gupta’s left in Gupta’s row: position 3, so Gupta’s left points towards 5. Tilak and Sharma are in Sen’s row with Sharma two places further that way: Tilak 3, Sharma 5. Arora takes position 5 in Gupta’s row.") + HOUSES)) +
 final("Two arrangements, differing only in Pathak and Bhalla."),
 p("‘Same number on my left and right as on his’ means the two houses face each other."),
 p("<b>Facing rows:</b> fix one global direction along the road; each row’s ‘left’ points the opposite way."))
P.dq(1, "Which statement is definitely false?", ["There are two houses between Bose’s and Sharma’s.", "Tilak’s house lies between Bose’s and Pathak’s.", "Arora is Pathak’s immediate neighbour.", "Ahuja’s house lies between Arora’s and Pathak’s."], "MCQ", "4", "Medium",
 "Check each in both arrangements.",
 steps(("1", p("Bose 2, Sharma 5 in the south row: Tilak and one more between. True.")),
       ("2 and 3", p("True if Pathak is in the south row (2) or the north row (3); each can hold.")),
       ("4", p("Ahuja is at 3, Arora at 5 and Pathak at 4: Ahuja is never between them."))) + final("Option 4"),
 [("1", "Always true."), ("2", "True in one arrangement."), ("3", "True in the other.")])
P.dq(2, "If there are two houses between Sen’s and Bhalla’s, whose house is immediately to the left of Pathak’s?", ["Arora", "Ahuja", "Bose", "Sharma"], "MCQ", "1", "Medium",
 "Then Bhalla is in Sen’s row.",
 steps(("Bhalla", p("Sen 1 south, Bhalla 4 south (Bose and Tilak between). Pathak is 4 north.")),
       ("Left of Pathak", p("For the north row, left points towards position 5: Arora."))) + final("Option 1"),
 [("2", "Ahuja is on Pathak’s right."), ("3", "Other row."), ("4", "Other row.")])
P.dq(3, "Whose house is two places to the left of the house opposite Singh’s?", ["Bhalla", "Pathak", "Sharma", "There is no such house"], "MCQ", "4", "Medium",
 "Opposite Singh is Bose.",
 steps(("Bose", p("Bose is at position 2 of the south row; for that row left points towards position 1, and there is only one house (Sen) that way."))) + final("Option 4"),
 [("1", "Not two places left of Bose."), ("2", "Not two places left of Bose."), ("3", "Sharma is on Bose’s right.")])
P.dq(4, "Gupta visits Bose, Pathak, Ahuja and Sharma in order of increasing distance from his house. Whom does he visit last?", ["Ahuja", "Pathak", "Sharma", "Bose"], "MCQ", "3", "Medium",
 "Gupta is at one end.",
 steps(("Distances", p("Gupta at 1 north; Bose at 2, Ahuja at 3, Pathak at 4, Sharma at 5 (south). Sharma is farthest."))) + final("Option 3"),
 [("1", "Position 3."), ("2", "Position 4."), ("4", "Position 2.")])
P.dq(5, "Which statement is definitely correct if made by Arora (left and right as seen from his own gate)?", ["Tilak’s house is two places to the left of Sharma’s.", "Gupta’s house is four places to the right of mine.", "Bose’s house is three places to the left of Sharma’s.", "Gupta’s house is at the extreme left end of the road."], "MCQ", "2", "Medium",
 "Arora is at position 5 of the north row; his left points towards 5, his right towards 1.",
 steps(("Option 2", p("Gupta is at 1, four places to Arora’s right.")),
       ("Others", p("Tilak (3) and Bose (2) are to the right of Sharma (5) in Arora’s terms, and Gupta is at Arora’s right end."))) + final("Option 2"),
 [("1", "Tilak is on Sharma’s right for Arora."), ("3", "Bose is on Sharma’s right for Arora."), ("4", "Right end, not left.")])

# ---------------- Set 2: A garment store's stock (Q6–10) ----------------
STOCK = (p("Women (3350):") + table(["", "Cotton", "Synth.", "Leather"], [["Dom.", "750", "600", "600"], ["Imp.", "600", "400", "400"]]) +
         p("Men (1650):") + table(["", "Cotton", "Synth.", "Leather"], [["Dom.", "400", "250", "200"], ["Imp.", "250", "350", "200"]]))
P.dilr_set(2, "Set 2 — Stock-taking in a garment store", DIR,
 p("Mrs Kapdawala owns a ready-made garment store in Pune. The first floor sells only women’s clothing and the second floor only men’s. Every item is cotton, synthetic or leather, and is either domestic or imported. A stock check on 31 March counted 5000 items.") +
 "<ol><li>44% of all items were imported, and 33% were men’s clothing.</li>"
 "<li>Non-leather items were 72% of the total, and 55 5/9 % of the non-leather items were cotton.</li>"
 "<li>42.5% of the cotton items and 46 7/8 % of the synthetic items were imported.</li>"
 "<li>Among women’s clothing, domestic leather items outnumbered imported leather items by half the number of men’s leather items. Half of the men’s leather items were domestic.</li>"
 "<li>There were 750 domestic cotton items for women. The number of men’s cotton items was 100 less than that.</li>"
 "<li>Women’s domestic items totalled 1950.</li></ol>",
 "DILR::DI::Caselets",
 steps(("Totals", p("Men 1650, women 3350. Imported 2200, domestic 2800. Women: 1950 domestic, 1400 imported. Men: 850 domestic, 800 imported.")),
       ("Materials", p("Leather 1400. Cotton 2000 (850 imported, 1150 domestic). Synthetic 1600 (750 imported, 850 domestic).")),
       ("Cotton", p("Men’s cotton 650: domestic 1150 − 750 = 400, imported 250. Women’s imported cotton 600.")),
       ("Leather", p("Let men’s leather be b domestic and b imported. Men’s imported: 250 + synthetic + b = 800; women’s figures then give women’s domestic leather 800 − b and imported 600 − b. Fact 4: (800 − b) − (600 − b) = b, so b = 200.") + STOCK)) +
 final("All twelve cells are fixed."),
 p("Fix the totals by gender, source and material first; the leather rule closes the system."),
 p("<b>Three-way tables:</b> split one dimension at a time and check each row and column total."))
P.dq(6, "Men’s domestic leather items cost ₹2450 each on average. What is their total cost price (in ₹)?", [], "TITA", "490000", "Medium",
 "There are 200 of them.",
 steps(("Cost", p("200 × 2450 = 4,90,000."))) + final("490000"))
P.dq(7, "Men’s cotton items cost ₹1300 each on average and women’s ₹775. What is the difference between the total cost prices of men’s and women’s cotton items (in ₹)?", [], "TITA", "201250", "Medium",
 "Men 650, women 1350.",
 steps(("Totals", p("650 × 1300 = 8,45,000; 1350 × 775 = 10,46,250.")),
       ("Difference", p("2,01,250."))) + final("201250"))
P.dq(8, "What is the ratio of imported men’s items to all men’s items?", ["16 : 33", "16 : 35", "17 : 33", "20 : 43"], "MCQ", "1", "Easy",
 "800 of 1650.",
 steps(("Ratio", p("800 : 1650 = 16 : 33."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "Arithmetic slip.")])
P.dq(9, "The items are split into 12 categories by material, source and gender. Which of these four categories has the fewest items?", ["Cotton–Imported–Women", "Synthetic–Domestic–Women", "Leather–Domestic–Women", "Synthetic–Imported–Women"], "MCQ", "4", "Medium",
 "Read the women’s table.",
 steps(("Values", p("600, 600, 600 and 400."))) + final("Option 4"),
 [("1", "600."), ("2", "600."), ("3", "600.")])
P.dq(10, "How many non-cotton (synthetic or leather) items are domestic?", [], "TITA", "1650", "Easy",
 "Add four cells.",
 steps(("Sum", p("Women 600 + 600; men 250 + 200: 1650."))) + final("1650"))

# ---------------- Set 3: A betting game (Q11–15) ----------------
MONEY = "<ul><li>After round 1: Mohan ₹130, the others ₹90.</li><li>After round 4: everyone ₹100 (one win each).</li><li>After round 10: Tarun ₹160, Mohan ₹120, the others ₹80 and ₹40.</li></ul>"
P.dilr_set(3, "Set 3 — A four-player betting game", DIR,
 p("Four friends — Vinod, Jatin, Mohan and Tarun — play a card game. In each round each player gets one card from four cards numbered 1 to 4 and bets ₹10 on it; the highest card wins all the money bet in that round. For the first ten rounds the bet is fixed at ₹10. In round 11 each player must bet the smallest amount any player then has.") +
 "<ol><li>No player won two rounds in a row.</li><li>After round 4, at least three players had equal amounts.</li>"
 "<li>Over rounds 1–10, the players won different numbers of rounds.</li><li>Each started with ₹100.</li>"
 "<li>Tarun won the most rounds in rounds 1–10.</li><li>Mohan never had less than ₹100 at any point.</li><li>Each player won at least one round.</li></ol>",
 "DILR::LR::Games_and_Tournaments",
 steps(("Wins", p("Different counts adding to 10, each at least 1: 1, 2, 3 and 4. Tarun has 4. A round’s winner gains ₹30 and the others lose ₹10.")),
       ("First four rounds", p("To leave at least three players level after round 4, each player must win exactly one of rounds 1–4; everyone then has ₹100.")),
       ("Mohan", p("He must win round 1 (else he drops to 90) and, being level at 100 after round 4, he must win round 5 too.")),
       ("Tarun", p("Four wins without consecutive rounds, one in rounds 1–4 and none in round 5: rounds 6, 8 and 10 plus his earlier one. Mohan wins once more, in round 7 or 9; the 1-win player has only his round in 1–4.") + MONEY)) +
 final("Final amounts after round 10: ₹160, ₹120, ₹80 and ₹40."),
 p("Count wins first: distinct counts adding to 10 must be 1, 2, 3, 4."),
 p("<b>Money after k rounds:</b> 100 + 30 × wins − 10 × losses."))
P.dq(11, "How much did Jatin have after round 4?", ["₹80", "₹100", "₹120", "₹110"], "MCQ", "2", "Medium",
 "Everyone wins one of the first four rounds.",
 steps(("Round 4", p("All four have ₹100."))) + final("Option 2"),
 [("1", "No one is below 100 then."), ("3", "No one is above 100 then."), ("4", "Not possible.")])
P.dq(12, "How much must each player bet in round 11?", ["₹40", "₹50", "Either ₹40 or ₹50", "₹60"], "MCQ", "1", "Medium",
 "The 1-win player has the least.",
 steps(("Least", p("100 + 30 − 90 = ₹40."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "It is fixed."), ("4", "Arithmetic slip.")])
P.dq(13, "After 10 rounds, which of these could be one player’s amount?", ["₹150", "₹130", "₹160", "₹180"], "MCQ", "3", "Easy",
 "The four amounts are 40, 80, 120, 160.",
 steps(("Amounts", p("1 win: 40; 2 wins: 80; 3 wins: 120; 4 wins: 160."))) + final("Option 3"),
 [("1", "Not one of the four."), ("2", "Not one of the four."), ("4", "Not one of the four.")])
P.dq(14, "How much did Tarun have after round 8?", ["₹110", "₹120", "₹130", "₹140"], "MCQ", "4", "Medium",
 "He won once in rounds 1–4, then rounds 6 and 8.",
 steps(("Rounds 5–8", p("₹100 after round 4; lost 5 (90), won 6 (120), lost 7 (110), won 8 (140)."))) + final("Option 4"),
 [("1", "After round 7."), ("2", "After round 6."), ("3", "Arithmetic slip.")])
P.dq(15, "How much did Mohan have after round 7?", ["₹120 or ₹130", "₹110 or ₹150", "₹120 or ₹150", "₹100 or ₹140"], "MCQ", "2", "Medium",
 "Did he win round 7 or round 9?",
 steps(("After round 6", p("100 + 30 (round 5) − 10 (round 6) = 120.")),
       ("Round 7", p("Win: 150. Lose (then he wins round 9): 110."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "120 is after round 6."), ("4", "Arithmetic slip.")])

# ---------------- Set 4: Clean-up bots (Q16–20) ----------------
BOTS = p("Bots cloned from each section:") + table(["Section", "Day 2", "Day 3"], [["Science", "1", "4"], ["Languages", "4", "8"], ["History", "5", "1"], ["Economics", "1", "3"]])
P.dilr_set(4, "Set 4 — Clean-up bots in four sections", DIR,
 p("An online encyclopaedia, written and edited by volunteers, has been filling up with irrelevant material. Rajesh, a volunteer, writes programs called ‘bots’ to remove it automatically from four sections: Science, Languages, History and Economics.") +
 p("On day 1 he used 10, 20, 30 and 40 bots in Science, Languages, History and Economics respectively.") +
 p("At the start of day 2 he ‘cloned’ some bots from their own section to each of the other three sections, so each cloned bot then worked in all four sections. After cloning, the four sections had 20, 27, 36 and 50 bots.") +
 p("At the start of day 3 he first deleted, from their original section only, the bots that had been cloned on day 2. Then he cloned some bots from one section to the other three, as before. After that the sections had 31, 31, 46 and 62 bots."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("Day 2", p("Let a, b, c, d bots be cloned from Science, Languages, History, Economics. Each section gains the clones of the other three: b + c + d = 10, a + c + d = 7, a + b + d = 6, a + b + c = 10. Adding: a + b + c + d = 11, so a = 1, b = 4, c = 5, d = 1.")),
       ("Day 3 start", p("Deleting the originals of day 2’s clones: 20 − 1 = 19, 27 − 4 = 23, 36 − 5 = 31, 50 − 1 = 49.")),
       ("Day 3 clones", p("Gains 12, 8, 15, 13. Each equals the sum of the other three sections’ clones; total 48 ÷ 3 = 16, so 4, 8, 1, 3.") + BOTS)) +
 final("Both days are fixed."),
 p("Each section gains the clones of the other three: add all four equations and divide by 3."),
 p("<b>Leave-one-out sums:</b> if each equation omits one unknown, the total of the unknowns is the equation total ÷ (n − 1)."))
P.dq(16, "For how many of the four sections can the number of bots cloned on both day 2 and day 3 be found?", [], "TITA", "4", "Easy",
 "Both systems have unique solutions.",
 steps(("All", p("Day 2: 1, 4, 5, 1. Day 3: 4, 8, 1, 3."))) + final("4"))
P.dq(17, "How many History bots were deleted on day 3?", [], "TITA", "5", "Easy",
 "The History bots cloned on day 2.",
 steps(("History", p("c = 5."))) + final("5"))
P.dq(18, "How many copies of cloned bots were created on day 2?", ["33", "30", "36", "Cannot be determined"], "MCQ", "1", "Easy",
 "Each cloned bot gets three copies.",
 steps(("Copies", p("11 bots × 3 = 33."))) + final("Option 1"),
 [("2", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "It is fixed.")])
P.dq(19, "How many copies of cloned bots were created on day 3?", ["81", "48", "42", "Cannot be determined"], "MCQ", "2", "Easy",
 "16 bots, three copies each.",
 steps(("Copies", p("16 × 3 = 48."))) + final("Option 2"),
 [("1", "Arithmetic slip."), ("3", "Arithmetic slip."), ("4", "It is fixed.")])
P.dq(20, "What is the ratio of Languages bots cloned on day 2 to those cloned on day 3?", ["2 : 1", "1 : 2", "2 : 3", "Cannot be determined"], "MCQ", "2", "Easy",
 "4 and 8.",
 steps(("Ratio", p("4 : 8 = 1 : 2."))) + final("Option 2"),
 [("1", "Upside down."), ("3", "Arithmetic slip."), ("4", "It is fixed.")])
