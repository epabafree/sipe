# -*- coding: utf-8 -*-
# Batch 5 — CAT 2022 Slot 1: VARC (Q1–24). DILR and QA are added by b5_22s1_dilr.py and b5_22s1_qa.py.
# Question numbers follow the order of the actual exam.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2022, 1, "ex5_22s1.json")
P.passage("P1", "Passage 1 — Copies, originals and the idea of identity", "Arts_and_Literature")
P.passage("P2", "Passage 2 — The Stoics and the two movements of emotion", "Philosophy_and_Psychology")
P.passage("P3", "Passage 3 — How stories of the Undead took shape", "Social_Science_and_History")
P.passage("P4", "Passage 4 — Critical theory of technology", "Philosophy_and_Psychology")

# ---------------- Passage 1 ----------------
P.rc(1, "P1", "Application", "2", "Medium",
 "Think about how the passage describes the way artworks were restored in the West during the 17th century. Which scenario goes against that picture?",
 steps(("What the passage says about the 17th century", ev(4, "Back in the 17th century [in the West], excavated artworks from antiquity were treated quite differently from today. They were not restored in a way that was faithful to the original. Instead, there was massive intervention in these works") +
          p("So, in that period, Western restorers felt quite free to change old works. The idea of an untouchable original came later.")),
       ("Testing the scenarios", p("A 17th-century British painter adding personal touches fits this description well. A 17th-century French artist feeling bound to stay completely true to the original runs against it, whatever his religious outlook, because the passage says that faithfulness simply wasn’t the norm then.") +
          p("The Japanese monk valuing the rebuilt shrine matches the Ise example, and the Christian scientist opposing cloning matches the last paragraph."))) +
 final("Option 2 is the one that doesn’t follow."),
 "inference",
 [("1", "This is exactly what the passage describes for the 17th-century West: free intervention in old works."),
  ("3", "The Ise shrine is treated as 1,300 years old even though it is rebuilt every 20 years, so a Japanese Buddhist monk would value the rebuilt shrine."),
  ("4", "The passage notes that Christians called for a ban on human cloning, so this scenario fits.")])

P.rc(2, "P1", "Detail_Not_True", "1", "Medium",
 "Look closely at how each building is renewed. Is the process the same kind of thing for both?",
 steps(("How each one is kept up", ev(2, "this temple complex is completely rebuilt from scratch every 20 years") +
          ev(3, "The cathedral of Freiburg Minster in southwest Germany is covered in scaffolding almost all year round … the cathedral is continually being examined for damage, and eroded stones are replaced.")),
       ("Where the similarity breaks", p("The cathedral is under constant, gradual repair. The shrine, on the other hand, is rebuilt all at once at fixed intervals. So “both are continually undergoing restoration” describes only the cathedral."))) +
 final("Option 1 does not express a real similarity."),
 "notrue",
 [("2", "A Shinto shrine and a cathedral are both places of worship, so this similarity holds."),
  ("3", "The author says the two cases are fundamentally the same operation: in time, every stone of the cathedral is replaced too."),
  ("4", "The shrine is regarded as 1,300 years old and the cathedral dates back to the Middle Ages, so both count as very old.")])

P.rc(3, "P1", "Except", "4", "Hard",
 "Three options describe things that plausibly follow from valuing the original. For one of them, the passage gives a different explanation.",
 steps(("What the passage links to cloning", ev(5, "It is probably this intellectual position that explains why Asians have far fewer scruples about cloning than Europeans … He found a great deal of support and followers among Buddhists, while Christians called for a ban on human cloning.") +
          p("The attitude to cloning is tied to religious and philosophical outlooks, Buddhist and Christian. The passage never says that the Western regard for the original is what holds Europeans back from cloning.")),
       ("The other three", p("Refusing copies in place of originals suggests a reluctance to show multiple copies. A workshop that constantly produces replacement figures gives craftsmen steady work. And the modern reluctance to intervene in ancient art is set directly against the 17th-century habit of changing old works."))) +
 final("Option 4 is the exception."),
 "except",
 [("1", "Western museums reject copies sent instead of originals, so showing several copies side by side is something they would avoid."),
  ("2", "The cathedral’s dedicated workshop is constantly producing copies, which means regular work for those craftsmen."),
  ("3", "Today’s Western practice is contrasted with the “massive intervention” of the 17th century, so valuing the original discourages such changes.")])

P.rc(4, "P1", "Application", "1", "Easy",
 "Go back to the two Chinese words for a copy. Which kind of copy is considered just as valuable as the original?",
 steps(("The two kinds of copy", ev(1, "The second concept for a copy is fuzhipin . . . They are exact reproductions of the original, which, for the Chinese, are of equal value to the original.") +
          p("An exact reproduction is valued as much as the original. A copy with obvious differences, a fangzhipin, is not.")),
       ("Applying it", p("A painting identical in every respect is a fuzhipin, so a Chinese museum would not see it as less valuable. A miniature, a copy carrying a different signature, or a photograph are all visibly different from the original."))) +
 final("Option 1."),
 "inference",
 [("2", "A miniaturised version is visibly different in size, which makes it the souvenir kind of copy (fangzhipin)."),
  ("3", "Picasso’s signature makes it different from van Gogh’s original, so it is no longer an exact reproduction."),
  ("4", "A photograph is a different medium altogether, however accurate the scale.")])

# ---------------- Passage 2 ----------------
P.rc(5, "P2", "Except", "1", "Medium",
 "Read the quoted sentence slowly. It talks about allowing emotions, watching them and deciding what matters. Does it say anything about leaving the body?",
 steps(("What the sentence describes", p("Emotions are allowed to happen, since they can’t be prevented. One then watches them without acting at once, gains some distance, and decides what has value. That watching and deciding is the Stoics’ “second movement”.")),
       ("Checking the options", p("Options 2, 3 and 4 all follow from this: observing at a distance is the second movement, emotions are first received without resistance, and strong emotions can blur what is valuable.") +
          p("“Out-of-body experiences” appear nowhere. The distance in the passage is a mental stance, not a physical one."))) +
 final("Option 1 is not a possible implication."),
 "except",
 [("2", "Observing and deciding after the first reaction is exactly what the passage calls the second movement."),
  ("3", "One “allows emotions to happen”, so the first step is indeed passive."),
  ("4", "The need to step back and decide what has value suggests that, in the moment, emotions make this hard.")])

P.rc(6, "P2", "Inference", "1", "Medium",
 "In the example, Marcus is accused by an army general in front of officers, and one possible response is to keep leading. What does that tell you about his role?",
 steps(("Reading the example", ev(1, "consider what could have happened if an army general accused Marcus Aurelius of treason in front of other officers … continuing to lead the Romans in a way that Marcus Aurelius believed best benefited them") +
          p("The setting is military, and Marcus is the one leading the Romans. It is safe to infer that he was one of the leaders of the army.")),
       ("Why the others are too strong", p("The example is hypothetical (“what could have happened”), so we can’t conclude that he actually plotted revenge or actually felt humiliated. The passage also never calls him a Stoic whose philosophy survived."))) +
 final("Option 1."),
 "inference",
 [("2", "Revenge is offered only as one possible second movement in an imagined scene."),
  ("3", "Humiliation is not stated; the passage only imagines surprise and anger."),
  ("4", "It is Stoicism that survived in the Roman era, not Marcus’s personal philosophy, and the passage never labels him a Stoic.")])

P.rc(7, "P2", "Detail_Not_True", "1", "Hard",
 "This question is easier if you turn it around: you are looking for a statement that is true according to the passage, because denying it would contradict the passage.",
 steps(("Turning the question around", p("If a statement, when false, contradicts the passage, then the statement itself must agree with the passage. So we need the option that the passage supports.")),
       ("Finding it", ev(1, "people should enjoy simple pleasures, such as good conversation, friendship, food, and wine, but not be indulgent in these pursuits") +
          p("The Epicureans welcomed simple pleasures but warned against indulging in them. So “indulging in simple pleasures is not desirable” matches their view, and its opposite would contradict the passage."))) +
 final("Option 1.") + trap("Options 3 and 4 already contradict the passage as they stand, so making them false would agree with it, not contradict it."),
 "notrue",
 [("2", "The passage treats emotions as things to be “reined in and controlled”, so this statement is already false; denying it agrees with the passage."),
  ("3", "The reasoned response belongs to the second movement, not the first, so this statement is already false; denying it agrees with the passage."),
  ("4", "It was Stoicism, not Zeno himself, that survived until about AD 300, so this is already false.")])

P.rc(8, "P2", "Detail", "2", "Easy",
 "Look at the last few lines of the passage. Where does the passage say Stoic ideas ended up?",
 steps(("Locating it", ev(2, "the Stoic idea of developing virtue in oneself … laid the foundation for the three monotheistic religions: Judaism, Christianity, and Islam")),
       ("Reading the options", p("Stoic influence is said to run through three religions, which is what option 2 says. The other options either overstate the passage or say the opposite."))) +
 final("Option 2."),
 "detail",
 [("1", "The Epicureans were against excessive pursuits; nothing suggests they wanted to control all emotions."),
  ("3", "The passage compares Stoic ideas with Buddhism but says nothing about Stoics in India."),
  ("4", "The Stoics said money, power and excessive sexual gratification are not important, which is the opposite.")])

# ---------------- Passage 3 ----------------
P.rc(9, "P3", "Inference", "3", "Easy",
 "The sentence is figurative. What is it really saying about what early humans believed?",
 steps(("Reading the image", p("“Whispers of eerie creatures” coming out of “the primal darkness of Mankind’s earliest years” is a way of saying that, from very early on, people told of beings that were neither fully alive nor fully dead.")),
       ("Choosing", p("Option 3 states this plainly: early humanity believed in such creatures. The other options take the whispers or the darkness literally."))) +
 final("Option 3."),
 "inference",
 [("1", "The passage doesn’t say we can understand these creatures’ lives through their whispers; the whispers are a figure of speech for early stories."),
  ("2", "The creatures aren’t literally whispering that they are not dead."),
  ("4", "This reads the whispers and darkness literally and drops the key point, that they were neither alive nor dead.")])

P.rc(10, "P3", "Detail_Not_True", "2", "Hard",
 "Flip the question first. If a statement, when false, fits the passage, then the statement itself goes against the passage. You want the one statement that actually agrees with it.",
 steps(("Turning the question around", p("For three options, the statement is untrue according to the passage, so its being false is in accordance with the passage. The exception is the one statement the passage confirms.")),
       ("Checking each one", p("Option 1: humans did not stop believing; the Undead “travelled with them”. Option 3: many of the Undead did take on definite shapes. Option 4: the relationship was “very tenuous and uncertain”. All three are false according to the passage.") +
          ev(5, "From the Middle Ages and into the Age of Enlightenment, theories of the Undead continued to grow and develop.") +
          p("Option 2 agrees with this line, so it is the exception."))) +
 final("Option 2."),
 "notrue",
 [("1", "The passage says the Undead travelled with Mankind into towns and cities, so this statement is false, and its being false fits the passage."),
  ("3", "Many creatures came to have definite shapes, so this statement is false too."),
  ("4", "The passage calls the relationship tenuous and uncertain, so this is false as well.")])

P.rc(11, "P3", "Main_Idea", "4", "Easy",
 "Follow the passage from start to finish: early humans, settled communities, the link with magic, and then the Middle Ages to the Enlightenment.",
 steps(("The arc of the passage", p("It begins with vague terrors around early encampments, moves to more definite creatures as communities form, adds their connection with magic, and ends with named creatures from the Middle Ages to the Enlightenment. It is a history of how ideas about the Undead developed.")),
       ("Matching", p("Option 4 captures that whole development. Option 1 picks out one part, and options 2 and 3 drift away from the Undead."))) +
 final("Option 4."),
 "inference",
 [("1", "Magic and Shamans form only one paragraph of the passage."),
  ("2", "The passage isn’t about humans failing to understand their environment in general."),
  ("3", "The shift in human thinking is the background; the subject is the Undead.")])

P.rc(12, "P3", "Inference", "3", "Medium",
 "Who “accorded” these attributes? Keep in mind that the passage is about how people imagined the Undead.",
 steps(("Unpacking the sentence", p("People gave the Undead powers that defy nature, such as changing shape or drinking blood, to mark them as abnormal. In other words, humans imagined them as having abnormal features.")),
       ("Choosing", p("Option 3 says exactly this. The other options either garble the grammar of the sentence or talk about divine or natural attributes that the passage doesn’t mention."))) +
 final("Option 3."),
 "inference",
 [("1", "The passage doesn’t say the Undead were deified or given divine attributes."),
  ("2", "This rewords the sentence without keeping its meaning."),
  ("4", "The attributes are supernatural from the start; nothing natural is being changed.")])

# ---------------- Passage 4 ----------------
P.rc(13, "P4", "Detail_Not_True", "4", "Medium",
 "In the second paragraph, what role do Foucault’s prisons and Habermas’s public sphere play? Are they the source of the pattern, or examples of it?",
 steps(("What the passage says", ev(2, "everywhere [that] masses are organised – whether it be Foucault’s prisons or Habermas’s public sphere – the same pattern prevails") +
          p("The prisons and the public sphere are examples of places where the pattern shows up. The pattern itself comes from the problems of commanding a disempowered workforce.")),
       ("Where option 4 goes wrong", p("Option 4 makes the prisons and the public sphere the models that set the pattern, which reverses their role."))) +
 final("Option 4 contradicts the passage."),
 "notrue",
 [("1", "This follows the second paragraph: the problems of command gave rise to the same pattern wherever masses are organised."),
  ("2", "The passage says the trajectory marks every modern political system, “including so-called socialist systems”."),
  ("3", "Marx’s trajectory and Marcuse’s “project” are presented as part of the same line of thought.")])

P.rc(14, "P4", "Inference", "4", "Easy",
 "The third and fourth paragraphs describe technology in a particular way. What word does the author keep using?",
 steps(("The key idea", ev(3, "critical theory of technology regards technologies as an environment rather than as a collection of tools") +
          ev(4, "As an environment, technologies shape their inhabitants.")),
       ("Choosing", p("Option 4 combines both lines: technologies form the environment and shape society."))) +
 final("Option 4."),
 "inference",
 [("1", "The author proposes a less romantic conception that grants theoretical legitimacy, so this mixes up the two."),
  ("2", "The passage says nature lies where society loses control; it doesn’t say nature decides that point."),
  ("3", "The passage says laws and customs represent dimensions of human nature, not just culture.")])

P.rc(15, "P4", "Main_Idea", "2", "Medium",
 "Read the opening of the fourth paragraph. What comparison does the whole paragraph build on?",
 steps(("The paragraph’s claim", ev(4, "As an environment, technologies shape their inhabitants. In this respect, they are comparable to laws and customs. Each of these institutions can be said to represent those who live under their sway") +
          p("The point is that technology works like laws and customs: all three are institutions that represent people by favouring certain parts of human nature.")),
       ("Choosing", p("Option 2 says technology, laws and customs are alike when seen as institutions, which is the heart of the paragraph."))) +
 final("Option 2.") + trap("Option 4 sounds close, but “as effectively as” adds a comparison of effectiveness that the paragraph never makes."),
 "inference",
 [("1", "The automobile is only an example within the paragraph."),
  ("3", "The paragraph stresses that they are alike, not that they are dissimilar."),
  ("4", "“As effectively as” is not in the paragraph.")])

P.rc(16, "P4", "Except", "2", "Medium",
 "Three options can be traced to specific lines. Which one adds a cost that the passage never mentions?",
 steps(("Tracing the three", p("Option 1 matches the third paragraph on social histories of technology. Option 3 matches the first paragraph: human rights take centre stage while an authoritarian order grows in the background. Option 4 matches the fifth paragraph: representing interests doesn’t imply an eternal human nature.")),
       ("The odd one", p("Option 2 claims that technologies privilege some dimensions of human nature “at a high cost to the lived nature”. The passage never talks about such a cost."))) +
 final("Option 2."),
 "except",
 [("1", "The third paragraph says the theory builds its method on the lessons of these social histories."),
  ("3", "This is how the first paragraph describes the tradition from Marx to Habermas."),
  ("4", "The fifth paragraph opens by saying this notion of representation does not imply an eternal human nature.")])

# ---------------- Verbal ability ----------------
P.va(17, P.sent_html(17), [], "TITA", "2431", "Para_Jumble", "Medium",
 "Start with the sentence that introduces collagen in general, then look for the problem that fish skin solves.",
 steps(("A natural opening", p("Sentence 2 introduces collagen and why it matters for skin. Nothing before it is needed.")),
       ("The problem, then the answer", p("Sentence 4 explains what held back pig and cow collagen: the risk of passing on diseases. Sentence 3 then explains why fish skin avoids that problem, and sentence 1 finishes by describing what makes fish collagen such a good bandage."))) +
 final("2431"),
 "pj",
 [("2", "Introduces collagen in general."), ("4", "The problem with collagen from pigs and cows."), ("3", "Why fish skin avoids that problem."), ("1", "What makes fish collagen useful as a bandage.")],
 why_title="Why each sentence goes where it does")

P.va(18, P.summary_html(18, "All that we think"), P.Q["VARC"][18]["opts"], "MCQ", "4", "Summary", "Medium",
 "The passage builds up to one specific claim about animate and inanimate things. Which option keeps that claim without adding to it?",
 steps(("What the passage says", "<ol><li>Our usual picture of how life hangs together is limited.</li><li>At the quantum level, the line between animate and inanimate can’t be drawn.</li><li>The universe has a pattern beyond what our minds can grasp.</li></ol>"),
       ("Choosing", p("Option 4 keeps the central point: the distinction between animate and inanimate disappears at the scale of quantum mechanics."))) +
 final("Option 4."),
 "summary",
 [("1", "“Astigmatic view” and “erroneous assumptions” stretch the passage’s gentler point about our limited vision."),
  ("2", "Calling the inanimate world “sentient and cognizant” goes much further than the passage."),
  ("3", "The response to stimuli is one supporting detail, not the main point.")])

P.va(19, P.summary_html(19, "It’s not that modern historians"), P.Q["VARC"][19]["opts"], "MCQ", "1", "Summary", "Medium",
 "The passage contrasts an old story about Ethiopia with what recent research shows. A good summary keeps both sides.",
 steps(("What the passage says", "<ol><li>The traditional story made Ethiopia weak and dependent on European help.</li><li>That story came from a selective reading of the sources.</li><li>Recent research shows Ethiopia sending out its own missions of diplomacy, faith and commerce.</li></ol>"),
       ("Choosing", p("Option 1 keeps the selective use of texts, the old picture of weakness, and the newer picture of a well-connected, outward-looking Ethiopia."))) +
 final("Option 1."),
 "summary",
 [("2", "The passage is about Ethiopia’s links with Europe, not commercial ties with its neighbours."),
  ("3", "It is modern scholars, not the medieval sources themselves, who put the story together the wrong way."),
  ("4", "The passage doesn’t say these links were invaluable in setting up military and trade ties.")])

P.va(20, P.sent_html(20), [], "TITA", "3214", "Para_Jumble", "Medium",
 "One sentence introduces the creative industry and its growth. Another begins “In fact”, and another begins “It is for this reason”. Let those phrases guide you.",
 steps(("The opener", p("Sentence 3 introduces the topic: the creative industry is growing faster than the world economy.")),
       ("Building on it", p("Sentence 2 begins “In fact” and adds that the creative element would be even larger if other industries were counted. Sentence 1 then explains why creativity matters so much: it is one of the few lasting competitive advantages.")),
       ("The consequence", p("Sentence 4, “It is for this reason”, follows from sentence 1 and closes with what this means for trade and intellectual property."))) +
 final("3214"),
 "pj",
 [("3", "Introduces the creative industry."), ("2", "“In fact” adds to the size of the creative element."), ("1", "Why creativity gives an edge."), ("4", "“For this reason” draws the consequence.")],
 why_title="Why each sentence goes where it does")

P.va(21, P.summary_html(21, "Petitioning is an expeditious"), P.Q["VARC"][21]["opts"], "MCQ", "2", "Summary", "Medium",
 "Notice what the passage does with elections. Does it want to replace them, or does it show what petitions add?",
 steps(("What the passage says", "<ol><li>Petitions let citizens bring issues straight to government and shape agendas.</li><li>Elections are limited: few candidates, no specific policy choices, and they happen only now and then.</li><li>So petitions keep the people’s voice heard between elections.</li></ol>"),
       ("Choosing", p("Option 2 captures this balance: petitioning supports democracy by adding ongoing engagement to the electoral process."))) +
 final("Option 2."),
 "summary",
 [("1", "Calling petitions an ideal form of representative democracy overstates the passage."),
  ("3", "The passage doesn’t suggest relying on petitions instead of elections."),
  ("4", "Nothing in the passage says citizens are becoming less inclined to petition.")])

P.va(22, P.sent_html(22), [], "TITA", "2143", "Para_Jumble", "Hard",
 "Look for the general statement about shorter commutes, then pair up the two sentences about how leaders and workers read the link between commuting and productivity.",
 steps(("The opener", p("Sentence 2 makes the general claim: shorter commutes support innovation.")),
       ("Two views", p("Sentence 1 shows company leaders acting on this when choosing where to put offices. Sentence 4 then gives another reading of the same link, as support for working from home.")),
       ("The caution", p("Sentence 3 begins “This is not always the case”, which answers the work-from-home view in sentence 4: remote work doesn’t automatically help, because office conversations matter too."))) +
 final("2143"),
 "pj",
 [("2", "The general claim."), ("1", "Leaders acting on it."), ("4", "Another reading: support for working from home."), ("3", "“This is not always the case” answers sentence 4.")],
 why_title="Why each sentence goes where it does")

MS23 = ('<p>There is a sentence that is missing in the paragraph given below. Look at the paragraph and decide in which blank (option 1, 2, 3, or 4) the following sentence would best fit.</p>'
        '<p class="quote"><b>Sentence:</b> Having made citizens more and less knowledgeable than their predecessors, the Internet has proved to be both a blessing and a curse.</p>'
        '<p class="quote"><b>Paragraph:</b> Never before has a population, nearly all of whom has enjoyed at a least a secondary school education, been exposed to so much information, whether in newspapers and magazines or through YouTube, Google, and Facebook. ___(1)___. Yet, it is not clear that people today are more knowledgeable than their barely literate predecessors. Contemporary advances in technology offered more serious and inquisitive students access to realms of knowledge previously unimaginable and unavailable. ___(2)___. But such readily available knowledge leads many more students away from serious study, the reading of actual texts, and toward an inability to write effectively and grammatically. ___(3)___. It has let people choose sources that reinforce their opinions rather than encouraging them to question inherited beliefs. ___(4)___.</p>')
P.va(23, MS23, ["Option 1", "Option 2", "Option 3", "Option 4"], "MCQ", "4", "Missing_Sentence", "Medium",
 "The sentence sums up a two-sided effect: more knowledgeable and less knowledgeable. Where has the paragraph finished laying out both sides?",
 steps(("What the sentence does", p("It is a summing-up. It needs both the good and the bad effects of the Internet to have been described already.")),
       ("Following the paragraph", p("The paragraph moves from more information, to doubts, to new access for serious students (the blessing), to distraction and poor writing, and finally to people choosing sources that confirm their views (the curse). Only after all of this can the sentence pull the two sides together, so it belongs at the end, in blank (4).")),
       ("The other blanks", p("Placed at (1), (2) or (3), the sentence would come before one side of the argument has been made, and it would interrupt the flow of the points."))) +
 final("Option 4."),
 "missing",
 [("1", "At this point only the flood of information has been mentioned; neither the blessing nor the curse has been shown yet."),
  ("2", "The curse hasn’t been described yet, so the sentence can’t sum up both sides here."),
  ("3", "“It has let people choose sources…” still continues the list of harms, so the summing-up would come too early.")])

MS24 = ('<p>There is a sentence that is missing in the paragraph given below. Look at the paragraph and decide in which blank (option 1, 2, 3, or 4) the following sentence would best fit.</p>'
        '<p class="quote"><b>Sentence:</b> Easing the anxiety and pressure of having a “big day” is part of the appeal for many couples who marry in secret.</p>'
        '<p class="quote"><b>Paragraph:</b> Wedding season is upon us and – after two years of Covid chaos that saw nuptials scaled back – you may think the temptation would be to go all out. ___(1)___. But instead of expanding the guest list, many couples are opting to have entirely secret ceremonies. With Covid case numbers remaining high and the cost of living crisis meaning that many couples are feeling the pinch, it’s no wonder that some are less than eager to send out invites. ___(2)___. Plus, it can’t hurt that in celebrity circles getting married in secret is all the rage. ___(3)___. “I would definitely say that secret weddings are becoming more common,” says Landis Bejar, the founder of a therapy practice, which specialises in helping brides and grooms manage wedding stress. “People are looking for ways to get out of the spotlight and avoid the pomp and circumstance of weddings. ___(4)___. They just want to get to the part where they are married.”</p>')
P.va(24, MS24, ["Option 1", "Option 2", "Option 3", "Option 4"], "MCQ", "2", "Missing_Sentence", "Medium",
 "The sentence gives one more reason for marrying in secret. Look for where the paragraph is listing reasons, and notice the word “Plus”.",
 steps(("What the sentence does", p("It offers a reason couples choose secret weddings: less anxiety and pressure.")),
       ("Finding the list of reasons", p("After blank (2) comes “Plus, it can’t hurt that…”. “Plus” adds another reason to one just given. Before the blank we already have Covid and the cost of living. Placing the sentence in blank (2) gives a third reason, and “Plus” then adds the celebrity trend.")),
       ("The other blanks", p("Blank (1) sits between “go all out” and “But instead”, which belong together. Blanks (3) and (4) fall inside the therapist’s comments, where the sentence would interrupt the quotation."))) +
 final("Option 2."),
 "missing",
 [("1", "“You may think the temptation would be to go all out” is answered directly by “But instead…”, so nothing should come between them."),
  ("3", "This is where the therapist is introduced, and the sentence would break that introduction."),
  ("4", "This falls inside a direct quotation, so the sentence can’t go there.")])
