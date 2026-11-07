# -*- coding: utf-8 -*-
# Batch 9 — CAT 2021 Slot 2: DILR sets 1–4 (Q1–20, exam order).
from fmt import steps, final, trap, why, table, p
from b9_21s2 import P

# ---------------- Set 1: Orders and ship modes ----------------
P.dilr_set(1, "Set 1 — Orders and ship modes", "Read the following passage and bar chart carefully and answer the questions that follow.",
 '<p class="fig"><img src="sipe_2021S2_DILR_S1.svg" alt="Bar chart of orders by category, from booking day to dispatch day, coloured by ship mode (S = Standard, 2 = Second class, F = First class). Art: S 1–3, 2 3–4, F 4–6, 2 6–13, S 13–21. Binders: S 1–2, 2 2–4, F 4–5, 2 5–16. Paper: 2 2–4, F 4–7, 2 7–12. Phones: S 2–4, F 4–5, S 5–17. Appliances: 2 2–4, S 4–12. Bookcases: 2 3–4, F 4–6, 2 6–7. Fasteners: S 2–4, 2 4–6, S 6–8. Furnishings: 2 1–5, S 5–12. Labels: 2 2–4, S 4–12. Tables: S 2–4, 2 4–10. Chairs: S 2–3, 2 3–9. Accessories: S 1–19. Envelopes: S 3–7. Storage: 2 2–7, S 7–22."></p>' +
 p("The different bars in the diagram above provide information about different orders in various categories (Art, Binders, ….) that were booked in the first two weeks of September of a store for one client. The colour and pattern of a bar denotes the ship mode (First Class / Second Class / Standard Class). The left end point of a bar indicates the booking day of the order, while the right end point indicates the dispatch day of the order. The difference between the dispatch day and the booking day (measured in terms of the number of days) is called the processing time of the order. For the same category, an order is considered for booking only after the previous order of the same category is dispatched. No two consecutive orders of the same category had identical ship mode during this period.") +
 p("For example, there were only two orders in the furnishing category during this period. The first one was shipped in the Second Class. It was booked on Sep 1 and dispatched on Sep 5. The second order was shipped in the Standard class. It was booked on Sep 5 (although the order might have been placed before that) and dispatched on Sep 12. So, the processing times were 4 and 7 days respectively for these orders."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Reading the bars", p("Each colour change is a new order. Processing times, row by row:") +
          table(["Category", "Orders (booked → dispatched)", "Processing times"],
                [["Art", "1→3, 3→4, 4→6, 6→13, 13→21", "2, 1, 2, 7, 8"], ["Binders", "1→2, 2→4, 4→5, 5→16", "1, 2, 1, 11"], ["Paper", "2→4, 4→7, 7→12", "2, 3, 5"],
                 ["Phones", "2→4, 4→5, 5→17", "2, 1, 12"], ["Appliances", "2→4, 4→12", "2, 8"], ["Bookcases", "3→4, 4→6, 6→7", "1, 2, 1"], ["Fasteners", "2→4, 4→6, 6→8", "2, 2, 2"],
                 ["Furnishings", "1→5, 5→12", "4, 7"], ["Labels", "2→4, 4→12", "2, 8"], ["Tables", "2→4, 4→10", "2, 6"], ["Chairs", "2→3, 3→9", "1, 6"],
                 ["Accessories", "1→19", "18"], ["Envelopes", "3→7", "4"], ["Storage", "2→7, 7→22", "5, 15"]]) +
          p("35 orders in all."))) +
 final("Every question is a count or an average over this table."),
 p("Turn the chart into a list of orders once. Each question is then quick arithmetic."),
 p("<b>Gantt-style charts:</b> each segment is one item; its start, end and length are all you need. Write them down before answering anything."))
P.dq(1, "How many days between Sep 1 and Sep 14 (both inclusive) had no booking from this client considering all the above categories?", [], "TITA", "6", "Easy",
 "List the start days of every bar.",
 steps(("Booking days", p("Orders were booked on Sep 1, 2, 3, 4, 5, 6, 7 and 13.")),
       ("No bookings", p("Sep 8, 9, 10, 11, 12 and 14: 6 days."))) + final(r"\(6\)"))
P.dq(2, "What was the average processing time of all orders in the categories which had only one type of ship mode?", [], "TITA", "11", "Easy",
 "Which rows have bars of a single colour?",
 steps(("The categories", p("Accessories (one Standard order, 18 days) and Envelopes (one Standard order, 4 days).")),
       ("Average", p(r"\(\tfrac{18 + 4}{2} = 11\)."))) + final(r"\(11\)"))
P.dq(3, "The sequence of categories – Art, Binders, Paper and Phones – in decreasing order of average processing time of their orders in this period is:",
 ["Phones, Binders, Art, Paper", "Phones, Art, Binders, Paper", "Art, Binders, Paper, Phones", "Paper, Binders, Art, Phones"], "MCQ", "2", "Easy",
 "Average each row’s processing times.",
 steps(("Averages", p("Art 20/5 = 4. Binders 15/4 = 3.75. Paper 10/3 ≈ 3.33. Phones 15/3 = 5."))) + final("Phones, Art, Binders, Paper, option 2"),
 [("1", "Binders (3.75) is below Art (4)."), ("3", "Phones is the highest."), ("4", "Roughly the reverse.")])
P.dq(4, "Approximately what percentage of orders had a processing time of one day during the period Sep 1 to Sep 22 (both dates inclusive)?",
 ["20%", "22%", "16%", "25%"], "MCQ", "1", "Medium",
 "Count all orders, then the one-day ones.",
 steps(("Counting", p("35 orders in all. One-day orders: Art 1, Binders 2, Phones 1, Bookcases 2, Chairs 1: 7.")),
       ("Percentage", p(r"\(\tfrac{7}{35} = 20\%\)."))) + final("20%, option 1"),
 [("2", "Would need about 8 of 35 or fewer orders in all."), ("3", "Would need about 6 one-day orders."), ("4", "Would need about 9.")])

# ---------------- Set 2: Fair division ----------------
_V = [["Amar", 4, 9, 9, 3, 7, 3, 8, 7, 9, 5], ["Barat", 5, 9, 7, 5, 5, 3, 6, 8, 10, 8], ["Charles", 8, 8, 8, 3, 6, 4, 5, 8, 9, 6],
      ["Disha", 8, 8, 8, 5, 5, 3, 6, 4, 9, 8], ["Elise", 6, 8, 9, 5, 6, 5, 6, 3, 7, 10]]
OBJ = (table([""] + [f"o{k}" for k in range(1, 6)], [[r[0]] + [str(x) for x in r[1:6]] for r in _V]) +
       table([""] + [f"o{k}" for k in range(6, 11)], [[r[0]] + [str(x) for x in r[6:11]] for r in _V]))

P.dilr_set(2, "Set 2 — Ten objects, five bundles", "Read the following passage and table carefully and answer the questions that follow.",
 p("Ten objects o1, o2, …, o10 were distributed among Amar, Barat, Charles, Disha, and Elise. Each item went to exactly one person. Each person got exactly two of the items, and this pair of objects is called her/his bundle.") +
 p("The following table shows how each person values each object.") + OBJ +
 p("The value of any bundle by a person is the sum of that person’s values of the objects in that bundle. A person X envies another person Y if X values Y’s bundle more than X’s own bundle.") +
 p("For example, hypothetically suppose Amar’s bundle consists of o1 and o2, and Barat’s bundle consists of o3 and o4. Then Amar values his own bundle at 4 + 9 = 13 and Barat’s bundle at 9 + 3 = 12. Hence Amar does not envy Barat. On the other hand, Barat values his own bundle at 7 + 5 = 12 and Amar’s bundle at 5 + 9 = 14. Hence Barat envies Amar.") +
 p("The following facts are known about the actual distribution of the objects among the five people.") +
 "<ol><li>If someone’s value for an object is 10, then she/he received that object.</li><li>Objects o1, o2, and o3 were given to three different people.</li><li>Objects o1 and o8 were given to different people.</li><li>Three people value their own bundles at 16. No one values her/his own bundle at a number higher than 16.</li><li>Disha values her own bundle at an odd number. All others value their own bundles at an even number.</li><li>Some people who value their own bundles less than 16 envy some other people who value their own bundle at 16. No one else envies others.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("The 10s", p("Barat gets o9 and Elise gets o10. Barat’s total must be even and at most 16, so his other object is worth 6 to him: o7. Elise likewise needs a 6: o1 or o5.")),
       ("Who else is at 16", p("Amar values Barat’s bundle at 8 + 9 = 17, so if Amar were at 16 he would envy Barat, which isn’t allowed. Disha’s total is odd. So the third 16 is Charles, from two 8s. o1, o2 and o3 go to different people and o1 can’t be with o8, so Charles has o8 with o2 or o3.")),
       ("Elise’s second object", p("If Elise took o1, Amar and Disha would share the remaining o2/o3, o4, o5 and o6. Disha would need the o2/o3 (for an odd total), and Amar, with at most 10, would value her bundle at 12 or more: he would envy someone below 16. So Elise has o5.")),
       ("Amar and Disha", p("They share o1, the remaining one of o2/o3, o4 and o6, with o1 and that o2/o3 going to different people. Disha’s odd total needs o4 or o6. If Disha had o1 + o6 (11), she would value Amar’s o2/o3 + o4 at 13 and envy him. So Disha has o1 + o4 (13) and Amar has the o2/o3 + o6 (12).")),
       ("o2 or o3", p("If Charles had o2 + o8, Barat would value that bundle at 9 + 8 = 17 and envy Charles. So Charles has o3 + o8, and Amar has o2 + o6.") +
       table(["Person", "Bundle", "Own value"], [["Amar", "o2, o6", "12"], ["Barat", "o7, o9", "16"], ["Charles", "o3, o8", "16"], ["Disha", "o1, o4", "13"], ["Elise", "o5, o10", "16"]]) +
       p("Amar envies Barat and Charles; Disha envies Barat."))) +
 final("The distribution is unique."),
 p("Start from the 10s and the cap of 16. Then use ‘envy’ as a filter: any envy from someone at 16, or towards someone below 16, rules a case out."),
 p("<b>Constraints that forbid:</b> a rule like ‘no one else envies others’ is easiest to use as a test. Build each candidate and look for one forbidden envy."))
P.dq(5, "What BEST can be said about object o8?",
 ["o8 was given to Amar, Charles, or Disha.", "o8 was given to Charles or Disha.", "o8 was given to Charles.", "o8 was given to Disha."], "MCQ", "3", "Hard",
 "Who needs two 8s to reach 16?",
 steps(("From the set solution", p("Charles reaches 16 with o3 and o8."))) + final("Option 3"),
 [("1", "The distribution is fixed; only Charles has it."), ("2", "Disha has o1 and o4."), ("4", "Disha has o1 and o4.")])
P.dq(6, "Who among the following envies someone else?", ["Amar", "Charles", "Elise", "Barat"], "MCQ", "1", "Hard",
 "Only people below 16 can envy.",
 steps(("From the set solution", p("Amar (12) values Barat’s bundle at 17 and Charles’s at 16, so he envies both."))) + final("Amar, option 1"),
 [("2", "Charles is at 16, so he envies no one."), ("3", "Elise is at 16."), ("4", "Barat is at 16.")])
P.dq(7, "What is Amar’s value for his own bundle?", [], "TITA", "12", "Hard",
 "Amar can’t be at 16, because he would envy Barat.",
 steps(("From the set solution", p("Amar has o2 and o6: 9 + 3 = 12."))) + final(r"\(12\)"))
P.dq(8, "Object o4 was given to", ["Barat", "Charles", "Elise", "Disha"], "MCQ", "4", "Hard",
 "Disha’s total must be odd.",
 steps(("From the set solution", p("Disha has o1 and o4 (8 + 5 = 13)."))) + final("Disha, option 4"),
 [("1", "Barat has o7 and o9."), ("2", "Charles has o3 and o8."), ("3", "Elise has o5 and o10.")])
P.dq(9, "Object o5 was given to", ["Disha", "Elise", "Charles", "Amar"], "MCQ", "2", "Hard",
 "Elise’s second object is worth 6 to her.",
 steps(("From the set solution", p("Elise has o5 and o10."))) + final("Elise, option 2"),
 [("1", "Disha has o1 and o4."), ("3", "Charles has o3 and o8."), ("4", "Amar has o2 and o6.")])
P.dq(10, "What BEST can be said about the distribution of object o1?",
 ["o1 was given to Charles or Disha.", "o1 was given to Charles, Disha, or Elise.", "o1 was given to Charles.", "o1 was given to Disha."], "MCQ", "4", "Hard",
 "o1 can’t be with o8, and Elise ends up with o5.",
 steps(("From the set solution", p("Disha has o1 and o4."))) + final("Disha, option 4"),
 [("1", "Charles has o3 and o8."), ("2", "Only Disha is possible."), ("3", "Charles has o8, which can’t go with o1.")])

# ---------------- Set 3: Chango ----------------
P.dilr_set(3, "Set 3 — The Chango championship", "Read the following passage carefully and answer the questions that follow.",
 p("The game of Chango is a game where two people play against each other; one of them wins and the other loses, i.e., there are no drawn Chango games. 12 players participated in a Chango championship. They were divided into four groups: Group A consisted of Aruna, Azul, and Arif; Group B consisted of Brinda, Brij, and Biju; Group C consisted of Chitra, Chetan, and Chhavi; and Group D consisted of Dipen, Donna, and Deb.") +
 p("Players within each group had a distinct rank going into the championship. The players have NOT been listed necessarily according to their ranks. In the group stage of the game, the second and third ranked players play against each other, and the winner of that game plays against the first ranked player of the group. The winner of this second game is considered as the winner of the group and enters a semi-final.") +
 p("The winners from Groups A and B play against each other in one semi-final, while the winners from Groups C and D play against each other in the other semi-final. The winners of the two semi-finals play against each other in the final to decide the winner of the championship.") +
 p("It is known that:") +
 "<ol><li>Chitra did not win the championship.</li><li>Aruna did not play against Arif. Brij did not play against Brinda.</li><li>Aruna, Biju, Chitra, and Dipen played three games each, Azul and Chetan played two games each, and the remaining players played one game each.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("How many games each", p("A first-ranked player plays 1 group game; a group winner from the 2nd/3rd pair plays 2. Then the semi-final, and the final for semi-final winners. So 3 games means either ‘first-ranked, reached the final’ or ‘2nd/3rd, won the group, lost the semi-final’.")),
       ("Groups B and D", p("Biju and Dipen have 3 games while their group-mates have 1 each. They played both group games (so they were 2nd/3rd), won their groups and lost the semi-finals.")),
       ("Groups A and C", p("If Aruna were 2nd/3rd, she would play both group-mates, including Arif, which fact 2 rules out. So Aruna was first-ranked: Azul beat Arif, lost to Aruna, and Aruna reached the final. Group C works the same way: if Chitra were 2nd/3rd, Chetan could only have 1 game. So Chitra was first-ranked, Chetan beat Chhavi and lost to Chitra, and Chitra reached the final.")),
       ("The knockouts", p("Semi-finals: Aruna beat Biju, Chitra beat Dipen. Chitra didn’t win the championship, so Aruna won the final."))) +
 final("Champion: Aruna."),
 p("Use the game counts. Three games can only happen in two ways, and fact 2 picks between them for each group."),
 p("<b>Counting games:</b> in a knockout, the number of games a player plays tells you how far they went. Translate each count into a path before anything else."))
P.dq(11, "Who among the following was DEFINITELY NOT ranked first in his/her group?", ["Dipen", "Aruna", "Chitra", "Brij"], "MCQ", "1", "Medium",
 "A player who played both group games can’t be first-ranked.",
 steps(("From the set solution", p("Dipen played both group games, so he was ranked second or third."))) + final("Dipen, option 1"),
 [("2", "Aruna was ranked first."), ("3", "Chitra was ranked first."), ("4", "Brij could have been ranked first.")])
P.dq(12, "Which of the following pairs must have played against each other in the championship?", ["Deb, Donna", "Azul, Biju", "Donna, Chetan", "Chitra, Dipen"], "MCQ", "4", "Medium",
 "The group C and D winners meet in a semi-final.",
 steps(("From the set solution", p("Chitra and Dipen met in the semi-final."))) + final("Option 4"),
 [("1", "Dipen played both of them; they didn’t play each other."), ("2", "Azul lost in the group stage."), ("3", "They were in different groups and both lost early.")])
P.dq(13, "Who won the championship?", ["Chitra", "Brij", "Aruna", "Cannot be determined"], "MCQ", "3", "Medium",
 "Who were the two finalists?",
 steps(("From the set solution", p("Aruna and Chitra reached the final, and Chitra didn’t win."))) + final("Aruna, option 3"),
 [("1", "Fact 1 rules her out."), ("2", "Brij played only one game."), ("4", "It can be determined.")])
P.dq(14, "Who among the following did NOT play against Chitra in the championship?", ["Aruna", "Biju", "Dipen", "Chetan"], "MCQ", "2", "Medium",
 "List Chitra’s three opponents.",
 steps(("From the set solution", p("Chitra played Chetan (group), Dipen (semi-final) and Aruna (final). She never played Biju."))) + final("Biju, option 2"),
 [("1", "They met in the final."), ("3", "They met in the semi-final."), ("4", "They met in the group.")])

# ---------------- Set 4: Ravi's ratings ----------------
P.dilr_set(4, "Set 4 — Ratings, bonuses and tips", "Read the following passage carefully and answer the questions that follow.",
 p("Ravi works in an online food-delivery company. After each delivery, customers rate Ravi on each of four parameters – Behaviour, Packaging, Hygiene and Timeliness, on a scale from 1 to 9. If the total of the four rating points is 25 or more, then Ravi gets a bonus of ₹20 for that delivery. Additionally, a customer may or may not give Ravi a tip. If the customer gives a tip, it is either ₹30 or ₹50.") +
 p("One day, Ravi made four deliveries - one to each of Atal, Bihari, Chirag and Deepak, and received a total of ₹120 in bonus and tips. He did not get both a bonus and a tip from the same customer.") +
 p("The following additional facts are also known.") +
 "<ol><li>In Timeliness, Ravi received a total of 21 points, and three of the customers gave him the same rating points in this parameter. Atal gave higher rating points than Bihari and Chirag in this parameter.</li><li>Ravi received distinct rating points in Packaging from the four customers adding up to 29 points. Similarly, Ravi received distinct rating points in Hygiene from the four customers adding up to 26 points.</li><li>Chirag gave the same rating points for Packaging and Hygiene.</li><li>Among the four customers, Bihari gave the highest rating points in Packaging, and Chirag gave the highest rating points in Hygiene.</li><li>Everyone rated Ravi between 5 and 7 in Behaviour. Unique maximum and minimum ratings in this parameter were given by Atal and Deepak respectively.</li><li>If the customers are ranked based on ratings given by them in individual parameters, then Atal’s rank based on Packaging is the same as that based on Hygiene. This is also true for Deepak.</li></ol>",
 "DILR::LR::Mathematical_Reasoning",
 steps(("Behaviour and Timeliness", p("Behaviour: Atal 7, Bihari 6, Chirag 6, Deepak 5. In Timeliness, Atal beats Bihari and Chirag, so the three equal ratings are Bihari, Chirag and Deepak (t each) and Atal has 21 − 3t > t: either t = 4 with Atal 9, or t = 5 with Atal 6.")),
       ("Packaging and Hygiene", p("Four distinct Hygiene ratings add to 26, so the highest is at least 8. Chirag’s Hygiene is the top Hygiene rating and equals his Packaging, which is below Bihari’s: so Chirag has 8 in both and Bihari 9 in Packaging. Hygiene is then 8, 7, 6, 5, and Atal and Deepak share 12 in Packaging: 7 and 5.")),
       ("Ranks", p("In Packaging, Atal and Deepak hold ranks 3 and 4, so they hold the same ranks in Hygiene: Bihari has 7 there, and Atal and Deepak have 6 and 5 in the same order as their Packaging.")),
       ("The money", p("₹120 can be 4 tips of ₹30, 1 bonus + two ₹50 tips, or 2 bonuses + ₹50 + ₹30. Bihari and Chirag both total 22 + t. If t = 4 they have 26 each and, whatever the case, Atal also reaches 26 or more: three bonuses, which is impossible. So t = 5, Atal’s Timeliness is 6, Bihari and Chirag have 27 (two bonuses), and Atal and Deepak must stay below 25. That needs Atal at 5 and 5 in Packaging and Hygiene, and Deepak at 7 and 6.") +
       table(["", "Behaviour", "Packaging", "Hygiene", "Timeliness", "Total"],
             [["Atal", "7", "5", "5", "6", "23"], ["Bihari", "6", "9", "7", "5", "27"], ["Chirag", "6", "8", "8", "5", "27"], ["Deepak", "5", "7", "6", "5", "23"]]) +
       p("Bonuses from Bihari and Chirag; tips of ₹50 and ₹30 from Atal and Deepak, in some order."))) +
 final("All ratings are fixed; only who gave which tip is open."),
 p("The Hygiene total of 26 forces a top rating of at least 8. That pins Chirag and Bihari, and the money condition settles the rest."),
 p("<b>Sums of distinct values:</b> a fixed total for distinct numbers puts a floor under the largest one. Check that floor early."))
P.dq(15, "What was the minimum rating that Ravi received from any customer in any parameter?", [], "TITA", "5", "Hard",
 "Look across the final table.",
 steps(("From the set solution", p("The lowest rating anywhere is 5."))) + final(r"\(5\)"))
P.dq(16, "The COMPLETE list of customers who gave the maximum total rating points to Ravi is", ["Bihari and Chirag", "Atal and Bihari", "Bihari", "Atal"], "MCQ", "1", "Hard",
 "Compare the four totals.",
 steps(("From the set solution", p("Bihari and Chirag both gave 27; Atal and Deepak gave 23."))) + final("Option 1"),
 [("2", "Atal gave 23."), ("3", "Chirag also gave 27."), ("4", "Atal gave 23.")])
P.dq(17, "What rating did Atal give on Timeliness?", [], "TITA", "6", "Hard",
 "The three equal Timeliness ratings are 5.",
 steps(("From the set solution", p(r"\(21 - 3 \times 5 = 6\)."))) + final(r"\(6\)"))
P.dq(18, "What BEST can be concluded about the tip amount given by Deepak?", ["Either ₹30 or ₹50", "₹30", "Either ₹0 or ₹30 or ₹50", "₹50"], "MCQ", "1", "Hard",
 "Two bonuses leave ₹80 in tips from two customers.",
 steps(("From the set solution", p("Atal and Deepak gave ₹50 and ₹30 between them. Either could have given either amount."))) + final("Option 1"),
 [("2", "Could be ₹50."), ("3", "He must have tipped; ₹80 needs both of them."), ("4", "Could be ₹30.")])
P.dq(19, "In which parameter did Atal give the maximum rating points to Ravi?", ["Packaging", "Hygiene", "Timeliness", "Behaviour"], "MCQ", "4", "Hard",
 "Atal’s row: 7, 5, 5, 6.",
 steps(("From the set solution", p("Behaviour, with 7."))) + final("Behaviour, option 4"),
 [("1", "5."), ("2", "5."), ("3", "6.")])
P.dq(20, "What rating did Deepak give on Packaging?", ["8", "5", "6", "7"], "MCQ", "4", "Hard",
 "Atal and Deepak share 12 in Packaging.",
 steps(("From the set solution", p("Deepak gave 7, Atal 5."))) + final("7, option 4"),
 [("1", "Chirag gave 8."), ("2", "Atal gave 5."), ("3", "6 is Deepak’s Hygiene rating.")])
