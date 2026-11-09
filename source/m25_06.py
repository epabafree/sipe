# -*- coding: utf-8 -*-
# Simp Mock 6 (2025): VARC (24 of 24). DILR and QA: m25_06_dilr.py, m25_06_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Mock

P = Mock(6, "sm25_06.json", series=2025)
P.passage("V1", "Passage 1 — The fruit-bat migration", "Environment_and_Life_Science")
P.passage("V2", "Passage 2 — Thinking at the scale of the planet", "Philosophy_and_Psychology")
P.passage("V3", "Passage 3 — From chatbots to AI agents", "Science_and_Technology")
P.passage("V4", "Passage 4 — A hybrid cartoon remake", "Arts_and_Literature")

# ---------------- Passage 1 (Q1–4) ----------------
P.rc(1, "V1", "Inference", "3", "Easy",
 "What do scientists believe the migration is tied to?",
 steps(("The line", ev(2, "While their migration is believed to be tied to food availability") +
          p("The bats feast on local fruits such as waterberries and mangoes. Food is the most plausible reason given."))) + final("Option 3"),
 "inference", [("1", "The swamp is a safe haven once there, not the stated reason for coming."), ("2", "Same: a benefit of the roost, not the driver."), ("4", "Seed dispersal is an effect of feeding, not a goal.")])
P.rc(2, "V1", "Inference_Except", "4", "Medium",
 "List what the passage says scientists struggle with. Do we know where the bats go?",
 steps(("The challenges", p("Tracking: ‘GPS tags have yet to last a full year’ (option 1). Reasons: ‘scientists remain puzzled about the exact reasons for their seasonal congregation’ (option 2). Numbers: guides say 10–12 million, studies about one million (option 3).")),
       ("The odd one", ev(3, "Studies reveal their dispersal into Congo, Malawi, and even South Sudan after leaving the park") +
          p("Where they go is partly known; unpredictable routes are not named as a challenge."))) + final("Option 4"),
 "except", [("1", "Stated: GPS tags fail."), ("2", "Stated: reasons unclear."), ("3", "Implied: estimates differ tenfold.")])
P.rc(3, "V1", "Detail", "4", "Hard",
 "What is the event, and what makes it ‘profound’? Read the opening of the passage.",
 steps(("The line", ev(4, "Witnessing millions of bats rise together is a profound biological event that underscores their ecological significance") +
          p("The event is profound because of its sheer scale: millions rising together. The opening establishes that scale: ‘The world’s largest mammal migration’.")),
       ("Why not 1", p("Ecological significance is what the event underscores, a consequence; it isn’t why the event itself is profound."))) +
 trap("Option 1 echoes the second half of the sentence; the question asks what makes the event profound.") + final("Option 4"),
 "detail", [("1", "What the event underscores, not why it’s profound."), ("2", "Bats are mammals, not birds."), ("3", "Distance is mentioned but isn’t the point of the sentence.")])
P.rc(4, "V1", "Inference_Except", "3", "Medium",
 "Which option isn’t a reason for the puzzle, and isn’t even true?",
 steps(("The reasons", p("GPS tags don’t last a year (1); the bats spread over a wide area after leaving (2); what triggers the timing is unclear (4).")),
       ("The odd one", ev(3, "which typically prefer tall trees or urban environments") +
          p("Option 3 reverses the passage, and roost preference isn’t why scientists are puzzled."))) + final("Option 3"),
 "except", [("1", "A stated reason."), ("2", "A stated reason."), ("4", "Implied by ‘remain puzzled’.")])

P.va(5, P.summary_html(5, "The largest and"), P.Q["VARC"][5]["opts"], "MCQ", "4", "Summary", "Medium",
 "Three parts: a prominent sight, a source of myth and science, and an origin still uncertain.",
 steps(("Choosing", p("Option 4 has the Moon’s prominence, myths and exploration, and the open question of its origin."))) + final("Option 4"),
 "summary", [("1", "‘Unsolved mystery’ is too broad: only its origin is unknown."), ("2", "‘Immense influence’ is added; leaves out the myths."), ("3", "Puts weight on further exploration; the origin becomes a side note.")])
P.va(6, P.missing_html(6), P.Q["VARC"][6]["opts"], "MCQ", "3", "Missing_Sentence", "Medium",
 "‘Activists blame … authorities deny’: what comes just before it, and what comes after?",
 steps(("Find the spot", p("Blank 3 follows the local allegations and the alarming 2024 tests. The sentence names who blames whom; after it, a villager describes the effects, and officials’ dismissal picks up the ‘authorities deny’ thread.")),
       ("Match the label", p("Blank 3 is choice 3, labelled ‘Option 3’."))) + final("Choice 3 (“Option 3”)"),
 "missing", [("1", "“Option 1”: the pollution hasn’t been described yet."), ("2", "“Option 2”: the allegations and tests haven’t come yet."), ("4", "“Option 4”: after the closing line.")])

# ---------------- Passage 2 (Q7–10) ----------------
P.rc(7, "V2", "Main_Idea", "3", "Medium",
 "Which idea runs through the whole passage, from Spivak to the closing sentence?",
 steps(("The thread", ev(1, "she proposed an approach rooted in humility, recognizing Earth’s vastness and complexity without attempting to dominate it") +
          ev(3, "The planetary perspective forces us to confront our interconnectedness with Earth and beyond") +
          p("Humility, interconnectedness and an Earth that is ‘alive and self-regulating’."))) + final("Option 3"),
 "inference", [("1", "Technology is one strand, not the aim."), ("2", "‘Replacement’ is too strong; the local still matters (China)."), ("4", "Space is one part of the discussion.")])
P.rc(8, "V2", "Inference", "1", "Hard",
 "What has changed since Spivak said no to domination?",
 steps(("The line", ev(2, "These proposals suggest humanity now has the tools to manage Earth’s systems in ways that could ensure survival") +
          p("Proposals such as geoengineering and planetary governance accept the power to manage the Earth, the very thing Spivak rejected. Humanity is no longer opposed to using such tools.")),
       ("Why not 3", p("‘Replaced’ is too strong: these are proposals by some thinkers, not a full shift away from humility."))) + final("Option 1"),
 "inference", [("2", "‘Fully endorses’ overstates ‘some advocate’."), ("3", "‘Replaced’ goes too far."), ("4", "The opposite: these proposals embrace power.")])
P.rc(9, "V2", "Purpose", "2", "Medium",
 "What does the sentence after the China example say?",
 steps(("The line", ev(2, "This interplay between the local and planetary shows solutions must consider both scales") +
          p("China’s shift was driven by local smog yet serves a planetary goal. The point is the link between scales."))) + final("Option 2"),
 "purpose", [("1", "Close, but the conclusion is about both scales together."), ("3", "Global cooperation isn’t the point."), ("4", "The two visions are Musk’s and Bezos’s.")])
P.rc(10, "V2", "Inference_Except", "4", "Medium",
 "Do Musk and Bezos agree?",
 steps(("The line", ev(3, "Musk’s vision is survivalist, preparing for the worst, while Bezos’s is expansionist") +
          p("Their views are ‘contrasting’. Musk treats Mars as a backup; Bezos keeps Earth pristine and makes space an industrial hinterland. They don’t converge on anything."))) + final("Option 4"),
 "except", [("1", "Survival and expansion: stated."), ("2", "Distinct approaches: stated."), ("3", "Inferable from Bezos’s industrial hinterland.")])

P.va(11, P.missing_html(11), P.Q["VARC"][11]["opts"], "MCQ", "1", "Missing_Sentence", "Medium",
 "A general remark about celebrities should come right before a specific celebrity example.",
 steps(("Find the spot", p("Blank 3 follows the runway shows; next comes the oversized bag that ‘has become a celebrity favorite’, carried by named stars. The sentence introduces that.")),
       ("Match the label", p("Blank 3 is choice 1, labelled ‘Option 3’."))) + final("Choice 1 (“Option 3”)"),
 "missing", [("2", "“Option 2”: designers, not celebrities, are the topic there."), ("3", "“Option 1”: no celebrity yet."), ("4", "“Option 4”: after the example, too late.")])

# ---------------- Passage 3 (Q12–15) ----------------
P.rc(12, "V3", "Main_Idea", "4", "Medium",
 "The passage covers product launches, their hiccups, the agentic push, and its hurdles and promise.",
 steps(("The arc", ev(2, "While researchers aim for new intelligence frontiers, developers are under pressure to release tools that demonstrate market value") +
          p("From research to products, with problems and hopes on both sides: option 4."))) + final("Option 4"),
 "inference", [("1", "The passage doesn’t say development is slow."), ("2", "Rivalry is a backdrop, not the theme."), ("3", "Leaves out the opportunities and the product focus.")])
P.rc(13, "V3", "Inference", "1", "Easy",
 "A hammer looking for a nail is a tool hunting for a use.",
 steps(("Meaning", ev(2, "Usually, products are designed around consumer needs") +
          p("The usual rule is to start from the need, not from the technology."))) + final("Option 1"),
 "inference", [("2", "That is Weil’s next point, not what the saying means."), ("3", "Not what the saying says."), ("4", "The reverse.")])
P.rc(14, "V3", "Application", "3", "Easy",
 "Agentic AI takes actions on a user’s behalf.",
 steps(("The definition", ev(1, "These tools are “agentic AI,” capable of taking actions on a user’s behalf") +
          p("Filing a tax return with documents is doing a task end to end, ‘from chatting to doing’."))) + final("Option 3"),
 "inference", [("1", "Gives instructions; the user still does the work."), ("2", "Generating content, not acting."), ("4", "Prediction, not action.")])
P.rc(15, "V3", "Weaken", "1", "Hard",
 "Which barrier does the passage put first, as the reason agents are harder to build at all?",
 steps(("The claim", ev(4, "Agents require data on task performance, including sequences and reasoning, which can be hard to collect") +
          p("This is the first and foundational hurdle: without task data, agents can’t be built. Trust, privacy and cost come after a working agent exists.")),
       ("The weakener", p("If such data is easy to access and integrate, the root difficulty that makes agents harder than chatbots falls away."))) +
 trap("Options 2–4 each remove a later hurdle (privacy, cost, trust); the passage itself already hints cost may be absorbed. Option 1 removes the one that blocks building.") + final("Option 1"),
 "weaken", [("2", "Removes a later adoption hurdle only."), ("3", "The passage already allows for this (subsidies, users paying)."), ("4", "Removes the trust hurdle, but agents still need data to exist.")])

P.va(16, P.summary_html(16, "The concept of"), P.Q["VARC"][16]["opts"], "MCQ", "1", "Summary", "Hard",
 "The concept, its critique of Western modernity, and why it is controversial.",
 steps(("Choosing", p("Option 1 keeps the critique and the controversy from its wartime ties, without adding claims."))) +
 trap("Option 4 says the idea was ‘largely avoided’ in postwar discourse; the passage says it persisted in the School’s own postwar work.") + final("Option 1"),
 "summary", [("2", "Leaves out the controversy."), ("3", "‘Selective revival’ is a detail; misses why it is controversial."), ("4", "‘Largely avoided’ contradicts its persistence.")])
P.va(17, P.sent_html(17), [], "TITA", "2", "Odd_One_Out", "Medium",
 "Four sentences describe what Enlightenment thinkers believed and what followed. One jumps to today.",
 steps(("The chain", p("4 → 1 → 5 → 3: thinkers valued reason and science (4); social sciences could improve life (1); law and truth were essential to progress (5); the Industrial Revolution showed the effect (3).")),
       ("The odd one", p("Sentence 2 is about modern populist debates, outside the historical account."))) + final("2"),
 "oddone", [("1", "Their belief in social science."), ("3", "The outcome."), ("4", "The opening."), ("5", "Another core value.")], why_title="How the other sentences fit")

# ---------------- Passage 4 (Q18–21) ----------------
P.rc(18, "V4", "Inference", "3", "Medium",
 "Why is the hybrid approach a problem for this film in particular?",
 steps(("The reason", ev(3, "But those succeeded because humans interacted with animals, not blob-headed babies") +
          p("Hybrids can work; the trouble is Rugrats’ deliberately strange character designs next to real people."))) + final("Option 3"),
 "inference", [("1", "The author cites successful hybrids."), ("2", "The author says the balance likely ‘won’t matter’."), ("4", "Not inherently flawed: Paddington succeeded.")])
P.rc(19, "V4", "Inference", "2", "Hard",
 "Why did the all-CGI reboot work, and why did Paddington work?",
 steps(("The lines", ev(2, "The uniformly weird aesthetic allowed viewers to quickly adjust") +
          p("And the successful hybrids paired humans with animals that fit their world. Success depends on the animated and real elements sitting together comfortably.")),
       ("Why not 4", p("The author doesn’t say hybrids generally alienate audiences; the worry is specific to Rugrats."))) + final("Option 2"),
 "inference", [("1", "Hybrids aren’t ‘inherently flawed’."), ("3", "Popularity for exploring interactions isn’t argued."), ("4", "Too general; the problem is Rugrats’ designs.")])
P.rc(20, "V4", "Purpose", "4", "Medium",
 "The examples are followed by ‘But those succeeded because…’.",
 steps(("The contrast", ev(3, "But those succeeded because humans interacted with animals") +
          p("The successful hybrids set up a comparison with Rugrats, whose babies are ‘blob-headed’."))) + final("Option 4"),
 "purpose", [("1", "True of the examples, but they serve the comparison."), ("2", "Not a general account of challenges."), ("3", "Not argued.")])
P.rc(21, "V4", "Tone", "3", "Easy",
 "Look at the comparisons: square watermelons, Windows screensavers, the Brundlefly teleporter.",
 steps(("The tone", ev(4, "This combination could provoke that story—and you know what? I’d watch it") +
          p("Exaggerated images and a joking ending: humorous and ironic."))) + final("Option 3"),
 "inference", [("1", "Far from neutral."), ("2", "Critical, yes, but the dominant note is comic."), ("4", "No nostalgia; the author mocks the original’s looks too.")])

P.va(22, P.summary_html(22, "The Bugis ethnic"), P.Q["VARC"][22]["opts"], "MCQ", "1", "Summary", "Medium",
 "Three genders beyond the binary, each with a defined social or spiritual role.",
 steps(("Choosing", p("Option 1 has the three genders and their distinct roles."))) + final("Option 1"),
 "summary", [("2", "Bissu is a gender, not only a symbol."), ("3", "‘Spiritual duality’ is added."), ("4", "‘Fluidity’ is added; the roles are defined.")])
P.va(23, P.sent_html(23), [], "TITA", "4", "Odd_One_Out", "Medium",
 "Four sentences argue for rethinking economic frameworks around production. One is about trade policy.",
 steps(("The chain", p("1 → 2 → 5 → 3: monopoly of ideas shapes how problems are framed (1); equilibrium theories are outdated (2); rethinking means dropping comfortable ideas (5); economists must centre production (3).")),
       ("The odd one", p("Sentence 4, on trade liberalisation and domestic production, is a policy point outside the argument about ideas."))) + final("4"),
 "oddone", [("1", "The framing."), ("2", "What’s outdated."), ("3", "The proposal."), ("5", "What rethinking needs.")], why_title="How the other sentences fit")
P.va(24, P.missing_html(24), P.Q["VARC"][24]["opts"], "MCQ", "4", "Missing_Sentence", "Medium",
 "‘This skepticism’ needs skepticism just before it, about interests.",
 steps(("Find the spot", p("Blank 3 follows ‘The public often questions whether scientific discoveries are … influenced by financial and political interests.’ The sentence explains what fuels that doubt.")),
       ("Match the label", p("Blank 3 is choice 4, labelled ‘Option 3’."))) + final("Choice 4 (“Option 3”)"),
 "missing", [("1", "“Option 1”: no skepticism described yet."), ("2", "“Option 2”: misconduct, not interests."), ("3", "“Option 4”: after the remedy.")])
