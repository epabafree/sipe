# -*- coding: utf-8 -*-
# Simp Mock 1: DILR (Sets 2 and 3).
from fmt import steps, final, trap, why, table, p
from m01 import P

def fig(src, alt): return f'<p class="fig"><img src="{src}" alt="{alt}"></p>'
DIR = "Read the information below and answer the questions that follow."
NEWPIPE = ("<p><b>Additional information for this question:</b> A new pipeline connecting C1 and C2 is built. The flow through this new pipeline can move from C2 to C1 only. "
           "The pipeline operators can now send petroleum products through three different routes: A-C1-B, A-C2-B and A-C2-C1-B. Time taken to carry 10000 gallons of petroleum products from C2 to C1 is 3.5 hours, "
           "and each additional 10000 gallons sent through this pipeline increases the transportation time by 30 minutes. For example, the time taken to carry 20000 gallons of petroleum through the new pipeline is 4 hours and so on.</p>")

# ---------------- Set 2: Two pipelines (Q6–10) ----------------
SEG = table(["Stretch", "1 unit", "Each extra unit"],
            [["A → C1", "10 h", "+30 min"], ["C1 → B", "3 h", "+1 h 30 min"], ["A → C2", "3 h", "+1 h 30 min"], ["C2 → B", "10 h", "+25 min"]])
ROUTES = p("Split = units on Pipeline 1 : units on Pipeline 2. Times in hours.") + table(["Split", "Pipe 1", "Pipe 2", "Overall"],
               [["0 : 4", "—", "18.75", "18.75"], ["1 : 3", "13", "16.83", "16.83"], ["2 : 2", "15", "14.92", "15"], ["3 : 1", "17", "13", "17"], ["4 : 0", "19", "—", "19"]], hi={(2, 3)}) + \
         p("For example, 2 : 2. Pipe 1: A→C1 takes 10.5 h and C1→B 4.5 h, total 15 h. Pipe 2: A→C2 takes 4.5 h and C2→B 10 h 25 min, total 14 h 55 min. The slower one, 15 h, decides.")
P.dilr_set(2, "Set 2 — Two pipelines", DIR,
 p("City A has an oil refinery which refines crude oil into various petroleum products with an output capacity of 40000 gallons per day. It sends all its daily output through two different pipelines to city B in one shot. "
   "These two pipelines pass through two different checkpoints. Pipeline-1 passes through checkpoint C1 and pipeline-2 passes through checkpoint C2. Any pipeline carries petroleum products in integral multiples of 10000 gallons.") +
 p("Total time taken to carry 10000 gallons of petroleum products from A to C1 and C2 to B is the same, which is 10 hours. If an additional volume of output is sent through these two portions of the pipeline, each additional 10000 gallons increases the total transportation time by 30 minutes and 25 minutes from A to C1 and C2 to B respectively. "
   "For example, the time taken to carry 20000 gallons of petroleum from A to C1 is 10 hours and 30 minutes and so on. Similarly, the time taken to carry 20000 gallons of petroleum from C2 to B is 10 hours and 25 minutes and so on. This delay happens because of excess pressure in the pipeline.") +
 p("In a similar way, the total time taken to carry 10000 gallons of petroleum products from A to C2 and C1 to B are the same, which is 3 hours. If an additional volume of output is sent through these two portions of the pipeline, each additional 10000 gallons increases the transportation time by 1 hour and 30 minutes for both the portions. "
   "For example, the time taken to carry 20000 gallons of petroleum from A to C2 and C1 to B is 4 hours and 30 minutes and so on.") +
 p("The pipeline operators send petroleum products through the pipelines in such a way that the total daily produce of the refinery is sent to city B in the minimum possible over-all transportation time. Any alteration in volumes sent through the pipelines will increase the overall transportation time. "
   "No time is wasted at the two checkpoints once the flow starts. ‘Over-all transportation time’ is the total time from beginning to end to complete the total transportation.") +
 fig("sipe_SM01_DILR_S2.svg", "Routes A to C1 to B and A to C2 to B, with the time for each stretch; a dashed new pipe from C2 to C1"),
 "DILR::LR::Routes_and_Networks",
 steps(("Work in units", p("Call 10,000 gallons one unit. The refinery sends 4 units. A stretch carrying \\(n\\) units takes its first-unit time plus \\((n-1)\\) extra steps.") + SEG),
       ("Time of each route", p("Both pipelines start together, so the overall time is the slower of the two routes. A route’s time is the sum of its two stretches.") + ROUTES),
       ("The operators’ plan", p("The best split is 2 units each way: 15 hours."))) +
 final("Normal plan: 2 units on each pipeline, 15 hours overall."),
 p("Overall time = the slower route. Balance the routes: the split that makes them closest is usually best."),
 p("<b>Parallel routes finish when the slowest one does:</b> overall time is the maximum, not the sum, of the route times."))

P.dq(6, "How many units of 10000 gallons of output from refinery in city A should be sent to city B through Pipeline-1?", [], "TITA", "2", "Medium",
 "Try every split of the 4 units. The overall time is the slower pipeline.",
 steps(("Compare splits", ROUTES), ("Best", p("2 units each way gives 15 hours, the least."))) + final("2"))

P.dq(7, "An operator explores all possible combinations of pipelines using which the total daily output can be sent from city A to city B, and notes down the overall transportation times (in hours) in each case. What is the average of all such overall transportation times noted by the operator? Round-off your answer to two decimal places.",
 ["17.32", "16.93", "16.17", "14.43"], "MCQ", "1", "Medium",
 "There are five splits (0 to 4 units on Pipeline 1). Average their overall times.",
 steps(("The five times", p("From the table: 18.75, 16.83, 15, 17 and 19 hours. (16.83 is 16 h 50 min, that is \\(16\\tfrac{5}{6}\\).)")),
       ("Average", p("Sum: \\(18.75 + 16.8\\overline{3} + 15\\) \\(+\\, 17 + 19 = 86.58\\overline{3}\\). Divided by 5: \\(17.31\\overline{6} \\approx 17.32\\)."))) + final("17.32, option 1"),
 [("2", "Leaves out one of the splits."), ("3", "Too low; check the 0 : 4 and 4 : 0 cases."), ("4", "Below even the best time, 15 hours.")])

ROUTES3 = p("Split = units on A–C1–B : A–C2–B : A–C2–C1–B. Times in hours; R1–R3 are the three routes in that order.") + table(["Split", "R1", "R2", "R3", "Max"],
                [["1 : 2 : 1", "14.5", "16.42", "14", "16.42"], ["2 : 1 : 1", "16.5", "14.5", "14", "16.5"], ["1 : 1 : 2", "16", "16", "16", "16"]], hi={(2, 4)}) + \
          p("For example, 1 : 1 : 2. A→C2 carries 3 units (6 h), C2→C1 carries 2 (4 h), C1→B carries 3 (6 h), A→C1 carries 1 (10 h), C2→B carries 1 (10 h). Route 1: 10 + 6 = 16; Route 2: 6 + 10 = 16; Route 3: 6 + 4 + 6 = 16.")
P.dq(8, NEWPIPE + "<p>If at most 20000 gallons of petroleum products are to be sent through the new pipeline, how much reduction in overall transportation time (in hours) can be achieved due to availability of this newly built pipeline given that no pipeline remains unused?</p>",
 [], "TITA", "0", "Medium",
 "Every stretch must be used, and the new pipe carries 1 or 2 units. Remember that units on the new route also load A→C2 and C1→B.",
 steps(("Loads", p("Units on A–C2–C1–B travel A→C2 (shared with A–C2–B), then C2→C1, then C1→B (shared with A–C1–B). All three routes need at least 1 unit.")),
       ("Every possible split (hours)", ROUTES3),
       ("Compare", p("The best with the new pipe is 16 hours. Without it, the plan already takes 15 hours. So the new pipe gives no reduction; the operators wouldn’t use it."))) +
 trap("A shared stretch carries the units of every route through it, so its time goes up for all of them.") + final("0"))

P.dq(9, NEWPIPE + "<p>What will be the percentage change in over-all transportation time in comparison to normal operations if the new pipeline can carry any volume of output and the operators send all the output through the A-C2-C1-B route?</p>",
 ["25% more time", "25% less time", "\\(33\\tfrac{1}{3}\\)% less time", "\\(33\\tfrac{1}{3}\\)% more time"], "MCQ", "4", "Easy",
 "All 4 units go A→C2, C2→C1, C1→B. Add the three stretch times.",
 steps(("All 4 units on one route", p("A→C2: \\(3 + 3 \\times 1.5 = 7.5\\) h. C2→C1: \\(3.5 + 3 \\times 0.5 = 5\\) h. C1→B: \\(3 + 3 \\times 1.5 = 7.5\\) h. Total 20 hours.")),
       ("Compare", p("Normal operations take 15 hours. \\(\\frac{20 - 15}{15} = \\frac{1}{3}\\), so \\(33\\tfrac{1}{3}\\%\\) more time."))) + final("Option 4"),
 [("1", "\\(5/20\\): measured against the new time, not the normal one."), ("2", "The time goes up, not down."), ("3", "The time goes up, not down.")])

P.dq(10, "<p><b>Additional information for this question:</b> Some improvements have been proposed to the new pipeline connecting C1 and C2 (as mentioned in the previous questions) so that now the time to carry 10000 gallons of petroleum products from C2 to C1 has been reduced to 2.5 hours, and the excess load of every 10000 gallons will increase the transportation time by 30 minutes.</p>"
 "<p>The flow through this new pipeline will continue from C2 to C1 only. The pipeline operators can now send petroleum products through three different routes. They are A-C1-B, A-C2-B, and A-C2-C1-B.</p>"
 "<p>What will be the reduction in overall transportation times (in hours) to carry 40000 gallons of oil from city A to city B, if exactly 10000 gallons are sent through the new pipeline?</p>",
 ["3 hours", "2.5 hours", "2 hours or less", "Reduction in transportation time from C2 to C1 will not affect the overall transportation time."], "MCQ", "4", "Medium",
 "With 1 unit on the new pipe, which route is the slowest? Does the new pipe’s time even matter?",
 steps(("Splits with 1 unit on the new pipe", p("Split = units on A–C1–B : A–C2–B, with 1 unit on A–C2–C1–B. Times in hours; R1–R3 are the three routes in that order.") + table(["Split", "R1", "R2", "R3", "Max"],
           [["1 : 2", "14.5", "16.42", "13", "16.42"], ["2 : 1", "16.5", "14.5", "13", "16.5"], ["3 : 0", "18.5", "—", "13", "18.5"], ["0 : 3", "—", "18.33", "13", "18.33"]])),
       ("What decides the time", p("In every split the new route is the fastest, so the overall time is set by the other routes. Making C2→C1 quicker changes nothing, and every split is still slower than the normal 15 hours."))) +
 final("Option 4"),
 [("1", "No split beats 15 hours."), ("2", "No split beats 15 hours."), ("3", "There is no reduction at all.")])

# ---------------- Set 3: Fruit purchases (Q11–15) ----------------
COMBOS = table(["Pair (2 kg each)", "₹"],
               [["Apple + Banana", "300"], ["Apple + Orange", "360"], ["Apple + Mango", "500"], ["Apple + Watermelon", "280"], ["Banana + Orange", "260"],
                ["Banana + Mango", "400"], ["Banana + Watermelon", "180"], ["Orange + Mango", "460"], ["Orange + Watermelon", "240"], ["Mango + Watermelon", "380"]])
FINAL = table(["Pair", "₹", "Who"],
              [["Apple + Mango", "500", "B, F, G"], ["Orange + Mango", "460", "B, F, G"], ["Banana + Mango", "400", "B, F, G"],
               ["Mango + W.melon", "380", "Jatin"], ["Apple + Orange", "360", "Chandani"], ["Apple + Banana", "300", "Enaya"], ["Apple + W.melon", "280", "Indu"],
               ["Banana + Orange", "260", "A, D, H"], ["Orange + W.melon", "240", "A, D, H"], ["Banana + W.melon", "180", "A, D, H"]])
P.dilr_set(3, "Set 3 — The fruit committee", DIR,
 p("The mess committee of a college consists of ten members namely, Ajay, Bindu, Chandani, Deepti, Enaya, Farzana, Garvit, Harshita, Indu and Jatin. Every Sunday they go to the local fruit market and buy 40 kg of fruits. "
   "On a particular Sunday they all collectively bought five types of fruits, namely Apple, Banana, Orange, Mango and Watermelon. Each member of the committee bought a total of 4 kg of fruits of two types. No one bought more than 2 kg of any one type of fruit. Also no two members bought the same combination of fruits.") +
 p("The prices of Apple, Banana, Orange, Mango and Watermelon were ₹100, ₹50, ₹80, ₹150 and ₹40 per kg in the given order. It is known that Indu bought Watermelons, Enaya bought Bananas and Jatin bought Mangoes. "
   "Also the sum of the amounts spent by Bindu, Farzana and Garvit was ₹1360 and the sum of the amounts spent by Ajay, Deepti and Harshita was ₹680."),
 "DILR::LR::Mathematical_Reasoning",
 steps(("Every member buys 2 kg of each of two fruits", p("4 kg of two types, at most 2 kg of a type, means exactly 2 kg + 2 kg. Five fruits make \\(\\binom{5}{2} = 10\\) pairs, and ten members buy different pairs, so every pair is bought once.") + COMBOS),
       ("₹1360 from three pairs", p("The three dearest pairs are 500 + 460 + 400 = 1360, and no other three pairs add to 1360. So Bindu, Farzana and Garvit bought the three mango pairs with apple, orange and banana.")),
       ("₹680 from three pairs", p("The three cheapest pairs are 180 + 240 + 260 = 680, again the only way. So Ajay, Deepti and Harshita bought Banana + Watermelon, Orange + Watermelon and Banana + Orange.")),
       ("The other four", p("Pairs left: Apple + Banana, Apple + Orange, Apple + Watermelon, Mango + Watermelon. Jatin bought mangoes: Mango + Watermelon. Enaya bought bananas: Apple + Banana. Indu bought watermelons: Apple + Watermelon. Chandani gets Apple + Orange.") + FINAL + p("B, F, G = Bindu, Farzana, Garvit; A, D, H = Ajay, Deepti, Harshita; W.melon = Watermelon. Within each of these groups the order is not known."))) +
 final("Six members are fixed; within the two groups of three, only the sets of pairs are known."),
 p("Totals equal to the largest or smallest possible sum fix the group at once: check the three dearest and three cheapest pairs first."),
 p("<b>Extreme sums pin down a choice:</b> if a total equals the largest (or smallest) possible sum, there is only one way to make it."))

P.dq(11, "Find the sum of the amounts spent (in ₹) by Jatin, Enaya and Indu.", [], "TITA", "960", "Hard",
 "Fix the two groups of three first; then each of Jatin, Enaya and Indu has only one pair left.",
 steps(("Their pairs", p("Jatin: Mango + Watermelon, ₹380. Enaya: Apple + Banana, ₹300. Indu: Apple + Watermelon, ₹280.")),
       ("Sum", p("\\(380 + 300 + 280 = 960\\)."))) + final("960"))
P.dq(12, "Who bought the combination Oranges and Apples?", ["Chandani", "Ajay", "Garvit", "Deepti"], "MCQ", "1", "Hard",
 "After the two groups of three and the three given clues, one pair and one member are left.",
 steps(("What’s left", p("Pairs left after the groups: Apple + Banana, Apple + Orange, Apple + Watermelon, Mango + Watermelon. Jatin, Enaya and Indu take three of them; Chandani gets Apple + Orange."))) + final("Option 1"),
 [("2", "Ajay is in the ₹680 group: no apples."), ("3", "Garvit is in the ₹1360 group: a mango pair."), ("4", "Deepti is in the ₹680 group: no apples.")])
P.dq(13, "How many members spent more money than Chandani?", [], "TITA", "4", "Hard",
 "Chandani spent ₹360. Count the pairs that cost more.",
 steps(("Above ₹360", p("Apple + Mango 500, Orange + Mango 460, Banana + Mango 400 and Mango + Watermelon 380. Four members."))) + final("4"))
P.dq(14, "Find the amount spent by Ajay (in ₹), if he did not buy watermelons.", [], "TITA", "260", "Hard",
 "Ajay is in the ₹680 group. Which of its pairs has no watermelon?",
 steps(("The ₹680 group", p("Banana + Watermelon, Orange + Watermelon, Banana + Orange. Without watermelon, Ajay bought Banana + Orange: \\(2 \\times 50 + 2 \\times 80 = 260\\)."))) + final("260"))
P.dq(15, "Who among the following did not buy Mangoes?", ["Bindu", "Farzana", "Jatin", "Harshita"], "MCQ", "4", "Hard",
 "Which group has no mango pairs?",
 steps(("Mango buyers", p("Bindu, Farzana and Garvit (all three mango pairs with apple, banana, orange) and Jatin (Mango + Watermelon). Harshita is in the ₹680 group, which has no mangoes."))) + final("Option 4"),
 [("1", "The ₹1360 group all bought mangoes."), ("2", "The ₹1360 group all bought mangoes."), ("3", "Given: Jatin bought mangoes.")])
