# -*- coding: utf-8 -*-
# Batch 8 — CAT 2021 Slot 1: DILR sets 1–4 (Q1–20, exam order).
from fmt import steps, final, trap, why, table, p
from b8_21s1 import P

# ---------------- Set 1: Journal papers ----------------
P.dilr_set(1, "Set 1 — Eighteen papers in four issues", "Read the following passage carefully and answer the questions that follow.",
 p("A journal plans to publish 18 research papers, written by eight authors (A, B, C, D, E, F, G, and H) in four issues of the journal scheduled in January, April, July and October. Each of the research papers was written by exactly one of the eight authors. Five papers were scheduled in each of the first two issues, while four were scheduled in each of the last two issues. Every author wrote at least one paper and at most three papers. The total number of papers written by A, D, G and H was double the total number of papers written by the other four authors. Four of the authors were from India and two each were from Japan and China. Each author belonged to exactly one of the three areas — Manufacturing, Automation and Logistics. Four of the authors were from the Logistics area and two were from the Automation area. As per the journal policy, none of the authors could have more than one paper to any issue of the journal.") +
 p("The following facts are also known.") +
 "<ol><li>F, an Indian author from the Logistics area, wrote only one paper. It was scheduled in the October issue.</li><li>A was from the Automation area and did not have a paper scheduled in the October issue.</li><li>None of the Indian authors were from the Manufacturing area and none of the Japanese or Chinese authors were from the Automation area.</li><li>A and H were from different countries, but had their papers scheduled in exactly the same issues.</li><li>C and E, both Chinese authors from different areas, had the same number of papers scheduled. Further, E had papers scheduled in consecutive issues of the Journal but C did not.</li><li>B, from the Logistics area, had a paper scheduled in the April issue of the Journal.</li><li>B and G belonged to the same country. None of their papers were scheduled in the same issue of the Journal.</li><li>D, a Japanese author from the Manufacturing area, did not have a paper scheduled in the July issue.</li><li>C and H belonged to different areas.</li></ol>",
 "DILR::LR::Analytical_Reasoning",
 steps(("Countries and areas", p("Automation authors can’t be Japanese or Chinese, so A is Indian. Indians can’t be in Manufacturing, so the four Indians are the two Automation authors and two Logistics authors; the four Japanese and Chinese authors are two Manufacturing and two Logistics.")),
       ("Placing each author", p("D is Japanese Manufacturing. C and E are Chinese in different areas, so one of them is the other Manufacturing author. H is from a different country than A, so not Indian, and not Chinese (C and E are the Chinese pair): H is Japanese, and must be Logistics. C differs from H in area, so C is Manufacturing and E is Logistics. That leaves B and G Indian (they share a country), with B in Logistics and G in Automation.") +
       table(["", "India", "Japan", "China"], [["Automation", "A, G", "", ""], ["Manufacturing", "", "D", "C"], ["Logistics", "B, F", "H", "E"]])),
       ("How many papers each", p("A, D, G and H wrote 12 papers between them, so 3 each. B, C, E and F wrote 6. F wrote 1, and C = E. C’s issues aren’t consecutive, so C has at least 2: C = E = 2 and B = 1.")),
       ("Which issues", p("A: Jan, Apr, Jul (not Oct). H: the same. D: Jan, Apr, Oct (not Jul). B: Apr only, so G avoids April: G is Jan, Jul, Oct. F: Oct. That fills Jan 4, Apr 4, Jul 3, Oct 3, and C and E add one paper to each. E must be consecutive and C not, which only works with C in Jan and Oct and E in Apr and Jul.") +
       table(["Issue", "Papers"], [["January", "A, H, D, G, C"], ["April", "A, H, D, B, E"], ["July", "A, H, G, E"], ["October", "D, G, F, C"]]))) +
 final("The schedule is unique."),
 p("The country and area rules pin down everyone before you look at the issues. Do that first; the schedule then follows almost directly."),
 p("<b>Two-way grids:</b> when every person has a country and an area, draw a small country × area grid and fill it from the negative rules (‘none of the Indians were…’)."))
P.dq(1, "What is the correct sequence of number of papers written by B, C, E and G, respectively?",
 ["1, 2, 2, 3", "3, 1, 1, 3", "1, 2, 2, 1", "1, 3, 3, 1"], "MCQ", "1", "Medium",
 "A, D, G and H wrote 12 papers between them.",
 steps(("From the set solution", p("G wrote 3 (as did A, D and H). B wrote 1, and C and E wrote 2 each."))) + final("1, 2, 2, 3, option 1"),
 [("2", "B wrote only 1, since C and E need 2 each."), ("3", "G is one of the authors with 3 papers."), ("4", "B + C + E would be 7, but it must be 5.")])
P.dq(2, "How many papers were written by Indian authors?", [], "TITA", "8", "Medium",
 "The Indian authors are A, B, F and G.",
 steps(("Adding", p("A 3 + B 1 + F 1 + G 3 = 8."))) + final(r"\(8\)"))
P.dq(3, "Which of the following statement(s) MUST be true?<br>Statement A: Every issue had atleast one paper by author(s) from each country.<br>Statement B: Every issue had at most two papers by author(s) from each area.",
 ["Neither of the statements", "Both the statements", "Only Statement A", "Only Statement B"], "MCQ", "3", "Medium",
 "Check the April issue for Statement B.",
 steps(("Statement A", p("India (A, B, F, G), Japan (D, H) and China (C, E) each appear in every issue. True.")),
       ("Statement B", p("April has H, B and E, three Logistics papers. False."))) + final("Only Statement A, option 3"),
 [("1", "Statement A is true."), ("2", "Statement B fails in April."), ("4", "Statement B fails in April.")])
P.dq(4, "Which of the following statements is FALSE?",
 ["Every issue had atleast one paper by author(s) from Automation area.", "Every issue had exactly one paper by a Chinese author.", "Every issue had exactly two papers by authors from Logistics area.", "Every issue had exactly two papers by Indian authors."], "MCQ", "3", "Medium",
 "Count Logistics papers (B, E, F, H) issue by issue.",
 steps(("Checking", p("Logistics papers per issue: January 1 (H), April 3 (H, B, E), July 2, October 1. So statement 3 is false. The other three hold."))) + final("Option 3"),
 [("1", "A or G is in every issue."), ("2", "C in January and October, E in April and July."), ("4", "January A, G; April A, B; July A, G; October G, F.")])
P.dq(5, "Which of the following statements is FALSE?",
 ["There were exactly two papers by authors from Manufacturing area in the July issue.", "There were exactly two papers by authors from Manufacturing area in the January issue.", "There was exactly one paper by an author from Logistics area in the October issue.", "There was exactly one paper by an author from Manufacturing area in the April issue."], "MCQ", "1", "Medium",
 "The Manufacturing authors are C and D. Is either of them in July?",
 steps(("Checking", p("July has A, H, G and E: no Manufacturing papers at all. Statement 1 is false."))) + final("Option 1"),
 [("2", "January has D and C."), ("3", "October has F only from Logistics."), ("4", "April has D only from Manufacturing.")])
P.dq(6, "Which of the following is the correct sequence of number of papers by authors from Automation, Manufacturing and Logistics areas, respectively?",
 ["6, 6, 6", "6, 5, 7", "5, 6, 7", "6, 7, 5"], "MCQ", "2", "Medium",
 "Add the papers of each area’s authors.",
 steps(("Adding", p("Automation: A 3 + G 3 = 6. Manufacturing: D 3 + C 2 = 5. Logistics: H 3 + B 1 + E 2 + F 1 = 7."))) + final("6, 5, 7, option 2"),
 [("1", "Manufacturing has only 5."), ("3", "Automation has 6."), ("4", "Swaps Manufacturing and Logistics.")])

# ---------------- Set 2: Smoothies ----------------
T1 = table(["Finished product", "Raw materials required"],
           [["Mango smoothie", "Mango, Milk"], ["Apple smoothie", "Apple, Milk"], ["Banana smoothie", "Banana, Milk"],
            ["Mixed fruit smoothie", "Mango, Apple, Banana, Milk"], ["Fruit salad", "Mango, Apple, Banana"]])
T2 = table(["Business Hour", "Ganga", "Kaveri", "Narmada"],
           [["Hour 1", "23", "19", "31"], ["Hour 2", "21", "22", "21"], ["Hour 3", "29", "30", "23"], ["Hour 4 (last hour)", "30", "27", "22"]])
P.dilr_set(2, "Set 2 — Smoothies and fruit salad", "Read the following passage and tables carefully and answer the questions that follow.",
 p("Ganga, Kaveri, and Narmada are three women who buy four raw materials (Mango, Apple, Banana and Milk) and sell five finished products (Mango smoothie, Apple smoothie, Banana smoothie, Mixed fruit smoothie and Fruit salad). Table-1 gives information about the raw materials required to produce the five finished products. One unit of a finished product requires one unit of each of the raw materials mentioned in the second column of the table.") +
 p("<b>Table-1</b>") + T1 +
 p("One unit of milk, mango, apple, and banana cost ₹5, ₹3, ₹2, and ₹1 respectively. Each unit of a finished product is sold for a profit equal to two times the number of raw materials used to make that product. For example, apple smoothie is made with two raw materials (apple and milk) and will be sold for a profit of ₹4 per unit. Leftover raw materials are sold during the last business hour of the day for a loss of ₹1 per unit.") +
 p("The amount in rupees, received from sales (revenue) for each woman in each of the four business hours of the day is given in Table-2.") +
 p("<b>Table-2</b>") + T2 +
 p("The following additional facts are known.") +
 "<ol><li>No one except possibly Ganga sold any Mango smoothie.</li><li>Each woman sold either zero or one unit of any single finished product in any hour.</li><li>Each woman had exactly one unit each of two different raw materials as leftovers.</li><li>No one had any banana leftover.</li></ol>",
 "DILR::DI::Data_Tabulation",
 steps(("Prices", table(["Product", "Cost", "Profit", "Price"],
          [["Mango smoothie", "8", "4", "12"], ["Apple smoothie", "7", "4", "11"], ["Banana smoothie", "6", "4", "10"], ["Mixed fruit smoothie", "11", "8", "19"], ["Fruit salad", "6", "6", "12"]]) +
          p("Leftovers sell at cost − 1: milk 4, mango 2, apple 1. Each woman’s leftover pair is milk + mango (6), milk + apple (5) or mango + apple (3).")),
       ("Kaveri and Narmada", p("Without mango smoothie they choose from 10, 11, 12 and 19, at most one of each per hour. Kaveri: 19 = mixed; 22 = banana + salad; 30 = apple + mixed; 27 is 21 + 6 (banana + apple, leftovers milk + mango) or 22 + 5 (banana + salad, leftovers milk + apple). Narmada: 31 = salad + mixed; 21 = apple + banana; 23 = apple + salad; 22 can only be 19 + 3, mixed with mango + apple left over.")),
       ("Ganga", p("23 = apple + (mango smoothie or salad); 21 = apple + banana; 29 = banana + mixed; 30 can only be 24 + 6, mango smoothie + salad with milk + mango left over."))) +
 final("Everything is fixed except Ganga’s first hour and Kaveri’s last hour."),
 p("Work out each product’s selling price first. After that, every hourly figure is a small subset-sum puzzle with very few answers."),
 p("<b>Subset sums:</b> when revenues come from a short price list with at most one of each item, list the possible sums once and match each figure against them."))
P.dq(7, "What BEST can be concluded about the number of units of fruit salad sold in the first hour?",
 ["Exactly 1", "Either 0 or 1 or 2", "Either 1 or 2", "Exactly 2"], "MCQ", "3", "Medium",
 "Kaveri’s 19 is a mixed fruit smoothie. Ganga’s 23 has two possibilities.",
 steps(("First hour", p("Narmada sold one salad (12 + 19). Kaveri sold none. Ganga sold an apple smoothie with either a mango smoothie or a salad. So 1 or 2."))) + final("Either 1 or 2, option 3"),
 [("1", "Ganga may also have sold one."), ("2", "Narmada certainly sold one, so 0 is impossible."), ("4", "Ganga may have sold a mango smoothie instead.")])
P.dq(8, "Which of the following is NECESSARILY true?",
 ["Ganga did not sell any leftover apples", "Kaveri sold one unit of leftover mangoes", "Narmada sold one unit of leftover milk", "Ganga did not sell any leftover mangoes"], "MCQ", "1", "Medium",
 "Ganga’s last hour fixes her leftovers.",
 steps(("From the set solution", p("Ganga’s leftovers are milk and mango, so she had no leftover apple."))) + final("Option 1"),
 [("2", "Kaveri may have had milk and apple instead."), ("3", "Narmada’s leftovers are mango and apple."), ("4", "Ganga did sell a leftover mango.")])
P.dq(9, "What BEST can be concluded about the total number of units of milk the three women had in the beginning?",
 ["Either 18 or 19 units", "Either 17 or 18 or 19 units", "Either 18 or 19 or 20 units", "Either 19 or 20 units"], "MCQ", "3", "Hard",
 "Milk goes into every smoothie, but not the salad. Add any leftover milk.",
 steps(("Ganga", p("Hour 1: 1 or 2; hour 2: 2; hour 3: 2; hour 4: 1; leftover 1. Total 7 or 8.")),
       ("Kaveri", p("Hours 1–3: 1 + 1 + 2. Hour 4 is either banana + apple with milk left over (3) or banana + salad with milk left over (2). Total 7 or 6.")),
       ("Narmada", p("1 + 2 + 1 + 1, no leftover milk: 5.")),
       ("Together", p("Between 6 + 5 + 7 = 18 and 7 + 5 + 8 = 20, and all three values can occur."))) + final("18, 19 or 20, option 3"),
 [("1", "Leaves out 20, which happens when both open choices add milk."), ("2", "17 is below the minimum."), ("4", "Leaves out 18.")])
P.dq(10, "If it is known that three leftover units of mangoes were sold during the last business hour of the day, how many apple smoothies were sold during the day?", [], "TITA", "6", "Medium",
 "Ganga and Narmada each have a leftover mango. The third must be Kaveri’s.",
 steps(("Kaveri’s last hour", p("Kaveri’s leftovers are milk + mango, so her last hour is banana + apple.")),
       ("Counting apple smoothies", p("Ganga 2 (hours 1 and 2), Kaveri 2 (hours 3 and 4), Narmada 2 (hours 2 and 3): 6."))) + final(r"\(6\)"))

# ---------------- Set 3: Friends, acquaintances, strangers ----------------
REL = table(["", "No. of Friends", "No. of Acquaintances", "No. of Strangers"],
            [["Amudha", "", "1", "4"], ["Bharatan", "", "", ""], ["Chandran", "", "1", ""], ["Dhinesh", "", "", "2"],
             ["Ezhil", "", "", "1"], ["Fani", "1", "", ""], ["Gowtham", "", "3", "2"]])
P.dilr_set(3, "Set 3 — Friends, acquaintances and strangers", "Read the following passage and table carefully and answer the questions that follow.",
 p("Amudha, Bharatan, Chandran, Dhinesh, Ezhil, Fani and Gowtham are seven people in a town. Any pair of them could either be strangers, acquaintances, or friends. All relationships are mutual. For example, if Amudha is a friend of Bharatan, then Bharatan is also a friend of Amudha. Similarly, if Amudha is a stranger to Bharatan, then Bharatan is also a stranger to Amudha. Partial information about the number of friends, acquaintances, and strangers of each of these people among them is given in the table below.") +
 REL + p("The following additional facts are also known.") +
 "<ol><li>Amudha, Bharatan, and Chandran are mutual strangers.</li><li>Amudha, Dhinesh, and Fani are Ezhil’s friends.</li><li>Chandran and Gowtham are friends.</li><li>Every friend of Amudha is an acquaintance of Bharatan, and every acquaintance of Bharatan is a friend of Amudha.</li><li>Every friend of Bharatan is an acquaintance of Amudha, and every acquaintance of Amudha is a friend of Bharatan.</li></ol>",
 "DILR::LR::Puzzles",
 steps(("Amudha and Bharatan", p("Everyone has 6 relationships. Amudha has 1 acquaintance and 4 strangers, so exactly 1 friend: Ezhil. By fact 4, Bharatan’s only acquaintance is Ezhil. By fact 5, Bharatan’s friends are exactly Amudha’s one acquaintance.")),
       ("Who that is", p("Fani’s only friend is Ezhil and Gowtham’s only friend is Chandran (he has 3 + 2 others), so Bharatan’s friend can’t be either of them. It is Dhinesh. So Amudha’s acquaintance is Dhinesh, and Amudha and Bharatan are strangers to Fani and Gowtham.")),
       ("Gowtham, Ezhil, Dhinesh", p("Gowtham’s two strangers are Amudha and Bharatan, so Dhinesh, Ezhil and Fani are his acquaintances. Ezhil has one stranger, and it must be Chandran. Dhinesh has 2 strangers; his other four relationships are already known, so Chandran and Fani are his strangers. Chandran’s single acquaintance is then Fani.") +
       table(["", "Am", "Bh", "Ch", "Dh", "Ez", "Fa", "Go"],
             [["Amudha", "–", "S", "S", "A", "F", "S", "S"], ["Bharatan", "S", "–", "S", "F", "A", "S", "S"], ["Chandran", "S", "S", "–", "S", "S", "A", "F"],
              ["Dhinesh", "A", "F", "S", "–", "F", "S", "A"], ["Ezhil", "F", "A", "S", "F", "–", "F", "A"], ["Fani", "S", "S", "A", "S", "F", "–", "A"],
              ["Gowtham", "S", "S", "F", "A", "A", "A", "–"]]) + p("F = friend, A = acquaintance, S = stranger."))) +
 final("The whole table is fixed."),
 p("Use facts 4 and 5 to tie Bharatan’s relationships to Amudha’s, then look for people with only one friend: they rule out most choices."),
 p("<b>Rows add up:</b> in a relationship table, each row has a fixed total (here 6). A row with two known counts gives you the third."))
P.dq(11, "Who are Gowtham’s acquaintances?",
 ["Dhinesh, Ezhil and Fani", "Amudha, Dhinesh and Fani", "Amudha, Bharatan and Fani", "Bharatan, Dhinesh and Ezhil"], "MCQ", "1", "Hard",
 "Gowtham has 1 friend, 3 acquaintances and 2 strangers.",
 steps(("From the set solution", p("His strangers are Amudha and Bharatan and his friend is Chandran, so his acquaintances are Dhinesh, Ezhil and Fani."))) + final("Option 1"),
 [("2", "Amudha is a stranger to him."), ("3", "Amudha and Bharatan are strangers to him."), ("4", "Bharatan is a stranger to him.")])
P.dq(12, "Which of these pairs share the same type of relationship?",
 ["(Chandran, Ezhil) and (Dhinesh, Gowtham)", "(Bharatan, Chandran) and (Dhinesh, Ezhil)", "(Bharatan, Ezhil) and (Fani, Gowtham)", "(Amudha, Gowtham) and (Ezhil, Fani)"], "MCQ", "3", "Hard",
 "Look each pair up in the final table.",
 steps(("Checking", p("Bharatan–Ezhil and Fani–Gowtham are both acquaintances."))) + final("Option 3"),
 [("1", "Strangers and acquaintances."), ("2", "Strangers and friends."), ("4", "Strangers and friends.")])
P.dq(13, "Who is an acquaintance of Amudha?", ["Ezhil", "Gowtham", "Dhinesh", "Fani"], "MCQ", "3", "Hard",
 "Bharatan’s friend is Amudha’s acquaintance.",
 steps(("From the set solution", p("Amudha’s one acquaintance is Dhinesh."))) + final("Dhinesh, option 3"),
 [("1", "Ezhil is her friend."), ("2", "Gowtham is a stranger."), ("4", "Fani is a stranger.")])
P.dq(14, "Who is an acquaintance of Chandran?", ["Bharatan", "Dhinesh", "Ezhil", "Fani"], "MCQ", "4", "Hard",
 "Chandran has exactly one acquaintance.",
 steps(("From the set solution", p("Dhinesh and Ezhil are strangers to Chandran, so his acquaintance is Fani."))) + final("Fani, option 4"),
 [("1", "Bharatan is a stranger (fact 1)."), ("2", "Dhinesh is a stranger."), ("3", "Ezhil is a stranger.")])
P.dq(15, "How many friends does Ezhil have?", [], "TITA", "3", "Hard",
 "Fact 2 gives three. Can there be more?",
 steps(("From the set solution", p("Ezhil’s friends are Amudha, Dhinesh and Fani. Bharatan and Gowtham are acquaintances and Chandran a stranger."))) + final(r"\(3\)"))
P.dq(16, "How many people are either a friend or a friend-of-a-friend of Ezhil?", [], "TITA", "4", "Hard",
 "List Ezhil’s friends, then their friends. Don’t count Ezhil.",
 steps(("Counting", p("Friends: Amudha, Dhinesh, Fani. Their other friends: Amudha has none, Dhinesh has Bharatan, Fani has none. So 4 people: Amudha, Dhinesh, Fani and Bharatan."))) +
 trap("Ezhil is a friend of each of his friends, but he isn’t counted.") + final(r"\(4\)"))

# ---------------- Set 4: Sales chart ----------------
P.dilr_set(4, "Set 4 — Sales by sub-category", "Read the following passage and bar chart carefully and answer the questions that follow.",
 '<p class="fig"><img src="sipe_2021S1_DILR_S4.svg" alt="Horizontal bar chart of 2020 sales (bars) and 2019 sales (vertical marks), in ₹ million, approximately: Bookcases 2.2 / 1.9, Chairs 7.0 / 6.1, Furnishings 2.1 / 2.05, Tables 4.5 / 4.4, Binders 5.3 / 3.6, Art 0.6 / 0.45, Appliances 3.1 / 1.9, Envelopes 0.2 / 0.35, Fasteners 0.1 / 0.1, Labels 0.3 / 0.2, Paper 2.0 / 1.5, Storage 5.1 / 5.1, Suppliers 1.2 / 1.05, Accessories 4.4 / 3.1, Copiers 4.6 / 3.6, Machines 4.1 / 4.1, Phones 7.7 / 5.8."></p>' +
 p("The horizontal bars in the above diagram represent 2020 aggregate sales (in ₹ million) of a company for the different subcategories of its products. The top four product subcategories (Bookcases, Chairs, Furnishings, Tables) belong to furniture product category; the bottom four product subcategories (Accessories, Copiers, Machines, Phones) belong to the technology product category while all other product subcategories belong to the office supply product category. For each of the product subcategories, there is a vertical line indicating the sales of the corresponding subcategory in 2019."),
 "DILR::DI::Graphs_and_Charts",
 steps(("Reading the chart", p("Approximate values (2020 / 2019), in ₹ million:") +
          table(["Category", "Sub-category", "2020", "2019"],
                [["Furniture", "Bookcases", "2.2", "1.9"], ["", "Chairs", "7.0", "6.1"], ["", "Furnishings", "2.1", "2.05"], ["", "Tables", "4.5", "4.4"],
                 ["Office supply", "Binders", "5.3", "3.6"], ["", "Art", "0.6", "0.45"], ["", "Appliances", "3.1", "1.9"], ["", "Envelopes", "0.2", "0.35"],
                 ["", "Fasteners", "0.1", "0.1"], ["", "Labels", "0.3", "0.2"], ["", "Paper", "2.0", "1.5"], ["", "Storage", "5.1", "5.1*"], ["", "Suppliers", "1.2", "1.05"],
                 ["Technology", "Accessories", "4.4", "3.1"], ["", "Copiers", "4.6", "3.6"], ["", "Machines", "4.1", "4.1"], ["", "Phones", "7.7", "5.8"]]) +
          p("* Storage has no separate 2019 mark; it is taken as level with the 2020 bar."))) +
 final("Readings to about 0.05 are enough; the options are far apart."),
 p("Read only what each question needs. The options are spread out, so rough readings are fine."),
 p("<b>Bars with markers:</b> the bar and the marker on the same row give the change directly. A marker inside the bar means sales went up."))
P.dq(17, "The total sales (in ₹ million) in 2019 from products in office supplies category is closest to",
 ["13.5", "12.5", "18.0", "16.5"], "MCQ", "1", "Medium",
 "Add the 2019 markers for the nine middle rows.",
 steps(("Adding", p("3.6 + 0.45 + 1.9 + 0.35 + 0.1 + 0.2 + 1.5 + 5.1 + 1.05 ≈ 14.3. Of the options, 13.5 is closest."))) + final("13.5, option 1"),
 [("2", "Further from 14.3 than 13.5."), ("3", "Much too high."), ("4", "Further away than 13.5.")])
P.dq(18, "The percentage increase in sales in Furniture category from 2019 to 2020 is closest to",
 ["1%", "25%", "20%", "8%"], "MCQ", "4", "Medium",
 "Add the four furniture rows for each year.",
 steps(("Totals", p("2019: 1.9 + 6.1 + 2.05 + 4.4 ≈ 14.4. 2020: 2.2 + 7.0 + 2.1 + 4.5 ≈ 15.8.")),
       ("Increase", p("1.4 / 14.4 ≈ 10%, so 8% is the closest option."))) + final("8%, option 4"),
 [("1", "Too small; Chairs alone rose by about 0.9."), ("2", "That’s about Phones’ rise, not furniture’s."), ("3", "Twice the actual rise.")])
P.dq(19, "How many subcategories had sales of ₹4 million or more in 2019 and registered an increase in sales in excess of 25% in 2020?", [], "TITA", "1", "Medium",
 "First list the rows whose 2019 marker is at 4 or beyond.",
 steps(("2019 sales of 4 or more", p("Chairs (6.1), Tables (4.4), Storage (5.1), Machines (4.1), Phones (5.8).")),
       ("Increase over 25%", p("Chairs about 15%, Tables 3%, Storage and Machines about 0, Phones about 32%. Only Phones."))) + final(r"\(1\)"))
P.dq(20, "The improvement index for a category is the maximum percentage increase in sales from 2019 to 2020 among any of its subcategories. The correct order of categories in increasing order of this improvement index is",
 ["furniture, technology, office supply", "office supply, furniture, technology", "technology, furniture, office supply", "office supply, technology, furniture"], "MCQ", "1", "Medium",
 "Find the biggest percentage rise within each category.",
 steps(("Each category", p("Furniture: Chairs or Bookcases, about 15%. Technology: Accessories, 3.1 → 4.4, about 42%. Office supply: Appliances, 1.9 → 3.1, about 60%.")),
       ("Order", p("Furniture < technology < office supply."))) + final("Option 1"),
 [("2", "Office supply has the largest index."), ("3", "Technology is above furniture."), ("4", "Office supply is the largest, not the smallest.")])
