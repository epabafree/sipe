# -*- coding: utf-8 -*-
# Batch 8 — CAT 2021 Slot 1: VARC (Q1–24). DILR and QA: b8_21s1_dilr.py, b8_21s1_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2021, 1, "ex8_21s1.json")
P.passage("P1", "Passage 1 — Personhood for the Classic Maya", "Social_Science_and_History")
P.passage("P2", "Passage 2 — A history of tea", "Social_Science_and_History")
P.passage("P3", "Passage 3 — Utopia and dystopia", "Philosophy_and_Psychology")
P.passage("P4", "Passage 4 — Self-control in cuttlefish", "Environment_and_Life_Science")

# ---------------- Passage 1: Maya ----------------
P.rc(1, "P1", "Weaken", "4", "Medium",
 "What is the iPhone example meant to contrast with? Look at how the phone gets its personhood.",
 steps(("What the example does", ev(1, "Does it have personhood (if at all) because it is connected to me, drawing this resource from me as an owner or source? For the Maya … the answer was no. Nonhuman persons were not tethered to specific humans") +
          p("The phone’s possible personhood depends on its owner. The author uses it to show that, for the Maya, personhood did not depend on a link to humans.")),
       ("What would undo it", p("If the Maya objects were persons because they were useful to humans, they would be just like the phone, and the contrast would fall apart. That is option 4."))) +
 final("Option 4"),
 "weaken",
 [("1", "The burner being only a person affects the point about overlapping categories, not the iPhone contrast."), ("2", "Songs with talking objects fit the passage; they don’t touch the contrast."),
  ("3", "The passage says the Maya had plenty of communicating objects, but the iPhone point is about owners, not communication.")])

P.rc(2, "P1", "Inference", "2", "Hard",
 "Before the burner, an object could be a person and still an object. What does the burner add?",
 steps(("The nonbinary idea so far", ev(3, "Entities were able to be persons while also being something else. … a person-tool is still made of stone.")),
       ("The complexity", ev(3, "the incense burner … is categorised as a person – but also as a tree.") +
          p("The burner is an object and a person, and it is also a tree. The tree is a third category, and it relates to the burner in the same way the other two do: the burner belongs to it without leaving the others. That is option 2."))) +
 final("Option 2"),
 "inference",
 [("1", "It isn’t an exception; it extends the nonbinary idea."), ("3", "The third category relates in the same way, not a different way."), ("4", "The tree is sacred, but the passage doesn’t frame this as divine versus profane.")])

P.rc(3, "P1", "Application", "4", "Hard",
 "What ‘activates’ personhood for the Maya? Find the option whose reason matches.",
 steps(("The Maya view", ev(2, "The Maya saw personhood as ‘activated’ by experiencing certain bodily needs and through participation in certain social activities.")),
       ("Matching", p("Option 4 grounds the plants’ personhood in a bodily need (nutrition) and in belonging to a community (an ecosystem), and it isn’t tied to their use to people. That is the closest match.")),
       ("Why not option 1", p("Option 1 bases the utensils’ personhood partly on their functionality. In the passage, objects keep their function alongside being persons, but function is not what makes them persons."))) +
 final("Option 4"),
 "inference",
 [("1", "Bases personhood on functionality, which the passage doesn’t."), ("2", "Bases it on usefulness for human survival, the very link the Maya rejected."),
  ("3", "Bases it on similarity to humans, which puts humans back at the centre.")])

P.rc(4, "P1", "Weaken_Except", "3", "Medium",
 "‘Democratising’ means humans are not more important persons than anything else. Which option keeps that intact?",
 steps(("The democratising idea", ev(1, "Humans are not more important persons – we are just one of many kinds of persons who inhabit this world.")),
       ("Checking each", p("Options 1 and 2 put humans at the centre: closeness to humans, or human form, makes something more of a person. Option 4 shuts some beings out of personhood. Option 3 has humans taking on the features of plants, which keeps humans and nonhumans on an equal footing."))) +
 final("Option 3"),
 "weaken",
 [("1", "Personhood would depend on closeness to humans."), ("2", "Objects would be persons only in human form."), ("4", "Excludes rivers and animals, so not everything can be a person.")])

# ---------------- Verbal ability (Q5–6) ----------------
P.va(5, P.sent_html(5), [], "TITA", "4312", "Para_Jumble", "Hard",
 "One sentence introduces the ‘two poles’. Another begins ‘From this polarity’.",
 steps(("The opener", p("Sentence 4 sets up the two poles of a literary work: the artistic (the text) and the aesthetic (the reader’s realisation).")),
       ("Following the idea", p("Sentence 3, “From this polarity”, concludes that the work lies between text and realisation. Sentence 1 explains why it is more than the text. Sentence 2 sums up: the meeting of text and reader brings the work into existence."))) +
 final("4312"),
 "pj",
 [("4", "The two poles."), ("3", "“From this polarity”: the work lies between them."), ("1", "Why the work is more than the text."), ("2", "The convergence of text and reader.")],
 why_title="Why each sentence goes where it does")

P.va(6, P.sent_html(6), [], "TITA", "2143", "Para_Jumble", "Easy",
 "Sentence 1 calls something ‘a popular response’. A response to what?",
 steps(("The opener", p("Sentence 2 states the problem: global warming will go well above two degrees.")),
       ("Following the trees", p("Sentence 1 gives the popular response (plant more trees), sentence 4 explains why (trees store carbon), and sentence 3 follows on: burning them releases “it”, the carbon."))) +
 final("2143"),
 "pj",
 [("2", "The problem."), ("1", "The response to it."), ("4", "Why trees help."), ("3", "“Burning them releases it”: the carbon from sentence 4.")],
 why_title="Why each sentence goes where it does")

# ---------------- Passage 2: Tea ----------------
P.rc(7, "P2", "Application", "1", "Easy",
 "The passage lists modern examples of ‘morality marketing’. Which option is like them?",
 steps(("The examples", ev(4, "morality marketing is now a commodity as well, applied to food, “fair trade” apparel and eco-tourism.")),
       ("Matching", p("Sustainably farmed food is sold as a good choice, not just a tasty one: buying it is presented as a virtue. The other options are sold on comfort, health or the experience itself."))) +
 final("Option 1"),
 "inference",
 [("2", "Pristine destinations are sold on the experience, not on doing good."), ("3", "Ergonomic design is a comfort benefit."), ("4", "Health supplements are sold on a personal benefit.")])

P.rc(8, "P2", "Except", "4", "Medium",
 "Three options are supported by the review. Which one does it never discuss?",
 steps(("What the review supports", p("Tea as patriotic in the Second World War (option 1), tea offered across the world as friendship (options 2 and 3).")),
       ("The odd one", p("The review never says when tea became Britain’s leading drink. It has nothing to support option 4."))) +
 final("Option 4"),
 "except",
 [("1", "¶2: tea service was “a social and patriotic activity”."), ("2", "¶5: the author has been offered tea in many settings."), ("3", "¶5: the offering was “friendship, community, respect”.")])

P.rc(9, "P2", "Except", "3", "Easy",
 "List the groups the second paragraph names. Which option isn’t one of them?",
 steps(("The groups", ev(2, "the temperance movement advocated for tea … industrialists soon borrowed this moral argument in advancing their case for free trade in tea … Factory owners joined in, compelled by the cause of a sober workforce")),
       ("The odd one", p("Tea drinkers lobbying for more variety appear nowhere."))) +
 final("Option 3"),
 "except",
 [("1", "Factory owners wanted a sober workforce."), ("2", "The temperance movement promoted tea over drink."), ("4", "Industrialists argued for free trade in tea.")])

P.rc(10, "P2", "Detail", "2", "Medium",
 "Read the end of the fourth paragraph: what makes tea ‘a world apart’?",
 steps(("The relevant line", ev(4, "Yet tea is, Rappaport makes clear, a world apart – an astonishing success story in which tea marketers not only succeeded in conveying a sense of moral elevation to the consumer but also arguably did advance the cause of civilisation and community.")),
       ("Choosing", p("Other morality products only claim a benefit. Tea actually delivered one. That is option 2."))) +
 final("Option 2"),
 "detail",
 [("1", "The review doesn’t contrast universal and niche appeal."), ("3", "Many groups promoted tea, but that isn’t what sets it apart."), ("4", "The government isn’t singled out.")])

# ---------------- Passage 3: Utopia ----------------
P.rc(11, "P3", "Inference", "2", "Medium",
 "The first paragraph describes Utopia as relying on ‘relentless transparency’ and ‘the curtailment of privacy’.",
 steps(("The relevant line", ev(1, "For modern readers, however, Utopia appears to rely upon relentless transparency, the repression of variety, and the curtailment of privacy. Utopia provides security")),
       ("Choosing", p("Watching every individual for the sake of their security and welfare fits all of this."))) +
 final("Option 2"),
 "inference",
 [("1", "Utopias curb the desire for public power; they don’t reward merit with it."), ("3", "Utopias repress variety, they don’t promote it."), ("4", "Utopias have many rules restraining individuality.")])

P.rc(12, "P3", "Except", "3", "Medium",
 "Check option 3 against the first paragraph closely. Does it say people didn’t need restraints?",
 steps(("What the passage says", ev(1, "In More’s time, for much of the population, given the plenty and security on offer, such restraints would not have seemed overly unreasonable.") +
          p("The restraints existed; people simply found them acceptable in return for plenty and security. Option 3 turns this into “people did not need restraints”.")),
       ("The others", p("Options 1, 2 and 4 restate the third and second paragraphs."))) +
 final("Option 3"),
 "notrue",
 [("1", "¶3: thousands of intentional communities with “harmony without coercion”."), ("2", "¶2: unity and homogeneity “at the cost of individuality”."), ("4", "¶2: societies where it would be “almost impossible for man to be depraved, or wicked”.")])

P.rc(13, "P3", "Main_Idea", "1", "Hard",
 "Follow the passage paragraph by paragraph: what does Utopia offer, how is it achieved, and what is the closing example?",
 steps(("The sequence", p("¶1: Utopia provides security, at a price. ¶2: the tradition achieves it through homogeneity. ¶3: but intentional communities show harmony can be voluntary.")),
       ("Choosing", p("Option 1 follows this order. The others start or end in the wrong place, or bring in coercion, which the passage sets aside at the end."))) +
 final("Option 1"),
 "inference",
 [("2", "Dystopia isn’t the end point; the passage ends on intentional communities."), ("3", "The passage ends by saying harmony is achieved without coercion."), ("4", "Starts with a detail and puts dystopia before utopia.")])

P.rc(14, "P3", "Except", "4", "Hard",
 "How firmly does the author state that utopia and dystopia are twins?",
 steps(("The relevant line", ev(3, "it is not unreasonable to take as our starting point here the hypothesis that utopia and dystopia evidently share more in common than is often supposed. Indeed, they might be twins") +
          p("It is put forward as a hypothesis and then qualified: not all utopias produce dystopias. Option 4 states it as a fact.")),
       ("The others", p("Uniformity (option 1), a change of perspective (option 2, ¶1’s “for modern readers”), and a literary tradition (option 3) all follow from the passage."))) +
 final("Option 4"),
 "except",
 [("1", "¶2: utopian homogeneity is a familiar theme."), ("2", "¶1: to modern readers Utopia looks dystopian."), ("3", "¶2 speaks of the literary tradition after More.")])

# ---------------- Verbal ability (Q15–19) ----------------
P.va(15, P.sent_html(15), [], "TITA", "2341", "Para_Jumble", "Medium",
 "One sentence introduces the discovery. Another begins ‘However, their ability…’.",
 steps(("The opener", p("Sentence 2 introduces the discovery in zebrafish.")),
       ("Details, then limits", p("Sentence 3 says which cells were studied. Sentence 4, “However, their ability…”, adds a limit for those cells. Sentence 1 closes by saying such regeneration hasn’t been proven in other species."))) +
 final("2341"),
 "pj",
 [("2", "The discovery."), ("3", "The Mauthner cells studied."), ("4", "“However”: it depends on where the injury is."), ("1", "Other species: not yet proven.")],
 why_title="Why each sentence goes where it does")

P.va(16, P.sent_html(16), [], "TITA", "5", "Odd_One_Out", "Medium",
 "Four sentences describe what predatory journals claim and how they work. One talks about the victims.",
 steps(("The chain", p("1 → 4 → 3 → 2: predatory journals (1), what they claim (4), so they look like real journals (3), but you can publish anything if you pay (2).")),
       ("The odd one", p("Sentence 5 shifts to the researchers who are scammed. It begins with “But”, yet there is no point in the chain for it to push against."))) +
 final("5"),
 "oddone",
 [("1", "Introduces predatory journals."), ("4", "What they claim."), ("3", "So they look reputable."), ("2", "“But in truth”: the reality.")],
 why_title="How the other sentences fit")

P.va(17, P.summary_html(17, "McGurk and MacDonald"), P.Q["VARC"][17]["opts"], "MCQ", "2", "Summary", "Medium",
 "What is the McGurk effect? A good summary says what happens, not just that it is famous.",
 steps(("What the passage says", "<ol><li>A sound dubbed onto a mismatched face is heard as a different sound.</li><li>This is the McGurk effect.</li><li>It is a striking example of the senses being combined.</li></ol>"),
       ("Choosing", p("Option 2 describes the effect itself. Option 1 only says it has been replicated."))) +
 final("Option 2"),
 "summary",
 [("1", "Says the effect is replicated but not what it is."), ("3", "The passage doesn’t say integration is imperfect; it says the two are merged."), ("4", "Poor-quality audio isn’t the point; the audio was recognised well on its own.")])

P.va(18, P.summary_html(18, "Developing countries"), P.Q["VARC"][18]["opts"], "MCQ", "2", "Summary", "Medium",
 "Three points: once cheap labour, now innovating, and going global.",
 steps(("What the passage says", "<ol><li>Developing countries are now innovating in business.</li><li>Once known for cheap labour, they are climbing the value chain.</li><li>They compete at home and are going global.</li></ol>"),
       ("Choosing", p("Option 2 has all three."))) +
 final("Option 2"),
 "summary",
 [("1", "Shifts the focus to developed countries being challenged."), ("3", "Narrows innovation to production and distribution and drops going global."), ("4", "“Forced” and “domestically” misread the passage, which says they are going global.")])

P.va(19, P.sent_html(19), [], "TITA", "4", "Odd_One_Out", "Hard",
 "Four sentences are about laws for commercial activity in space. One is about a political quarrel.",
 steps(("The chain", p("1 → 5 → 2 → 3: the legal status of space resources is unclear (1), the issue is commercial activity (5), space law is state-centric and unsuited to commerce (2), and national laws so far are only first steps (3).")),
       ("The odd one", p("Sentence 4 reports critics condemning the US. It moves from the legal gap to an international dispute, and nothing else in the paragraph picks it up."))) +
 final("4"),
 "oddone",
 [("1", "The unclear legal status."), ("5", "At issue: commercial activity."), ("2", "Why space law doesn’t suit it."), ("3", "National laws as first steps.")],
 why_title="How the other sentences fit")

# ---------------- Passage 4: Cuttlefish ----------------
P.rc(20, "P4", "Except", "4", "Medium",
 "Compare the two tests point by point. Which supposed difference isn’t in the passage?",
 steps(("The differences", p("The original test lasted 15 minutes; the cuttlefish waited at most 130 seconds. Children versus cuttlefish. Words versus trained symbols.")),
       ("The odd one", p("The cuttlefish test didn’t look at survival advantages. Option 4 invents that."))) +
 final("Option 4"),
 "except",
 [("1", "15 minutes against at most 130 seconds."), ("2", "Children against cuttlefish."), ("3", "The cuttlefish had to be trained to read shapes.")])

P.rc(21, "P4", "Inference", "4", "Hard",
 "The last paragraph notes that animals with self-control usually have long, social lives. Cuttlefish don’t.",
 steps(("The open question", ev(3, "Not every species can use self-control, but most of the animals that can share another trait in common: long, social lives. Cuttlefish, on the other hand, are solitary creatures")),
       ("What complements it", p("If cuttlefish did live in sociable groups, they would fit the pattern the passage describes, and the findings would sit comfortably with what is known of other species."))) +
 final("Option 4"),
 "inference",
 [("1", "If they couldn’t tell shapes apart, the experiment wouldn’t work."), ("2", "If they liked both foods equally, waiting wouldn’t show self-control."), ("3", "The passage already reports waits of up to 130 seconds; this adds nothing.")])

P.rc(22, "P4", "Except", "2", "Easy",
 "Which option goes much further than the passage, which leaves the role of social life as an open question?",
 steps(("The relevant line", ev(3, "“We don’t know if living in a social group is important for complex cognition unless we also show those abilities are lacking in less social species”") +
          p("The passage treats the link as unknown. Option 2 states that intelligence is impossible without sociability.")),
       ("The others", p("Distracting themselves (option 1), food preferences (option 3) and self-control like children’s (option 4) all follow."))) +
 final("Option 2"),
 "except",
 [("1", "They turned away from the prawn “as if to distract themselves”."), ("3", "They preferred live shrimp to raw prawn."), ("4", "They waited, as in the children’s test.")])

P.rc(23, "P4", "Application", "2", "Medium",
 "Self-control means passing up a food you can have now for a preferred food later.",
 steps(("The setup", p("Live grass shrimp is the favourite; raw prawn is so-so; Asian shore crab is nearly unacceptable. A triangle means delayed; a square means never.")),
       ("Choosing", p("In option 2, prawns and crabs are available now and the favourite shrimp comes after a minute. Waiting for the shrimp shows self-control."))) +
 final("Option 2"),
 "inference",
 [("1", "A square means never, so taking the prawn is the sensible choice."), ("3", "The delayed food is crab, which they hardly eat; waiting for it isn’t self-control."), ("4", "The favourite food is available now, so there is nothing to wait for.")])

# ---------------- Verbal ability (Q24) ----------------
P.va(24, P.summary_html(24, "Foreign peacekeepers"), P.Q["VARC"][24]["opts"], "MCQ", "1", "Summary", "Medium",
 "The passage partly excuses the peacekeepers’ distance, then proposes working with communities.",
 steps(("What the passage says", "<ol><li>Peacekeepers live apart from locals.</li><li>This is partly justified, but they are resented.</li><li>Working closely with communities would be better.</li></ol>"),
       ("Choosing", p("Option 1 keeps all three, including the point that the distance has some justification."))) +
 final("Option 1"),
 "summary",
 [("2", "Says the anger is justified, which the passage doesn’t."), ("3", "The passage wants foreign peacekeepers to work with locals, not be replaced by them."), ("4", "Leaves out the proposed solution.")])
