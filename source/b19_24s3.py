# -*- coding: utf-8 -*-
# Batch 19 — CAT 2024 Slot 3: VARC (Q1–24). DILR and QA are added by b19_24s3_dilr.py and b19_24s3_qa.py.
# Question numbers follow the order of the actual exam.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2024, 3, "ex19_24s3.json")
P.passage("P1", "Passage 1 — AI and the operating system of civilisation", "Science_and_Technology")
P.passage("P2", "Passage 2 — How a Chinese liquor brand broke the rules", "Economics_and_Management")
P.passage("P3", "Passage 3 — Should we keep Mars sterile?", "Science_and_Technology")
P.passage("P4", "Passage 4 — Language extinction and the liberal arts", "Social_Science_and_History")

# ---------------- Passage 1 ----------------
P.rc(1, "P1", "Except", "1", "Medium",
 "Three options restate dangers the author spells out. One adds a consequence he never mentions.",
 steps(("The dangers named", ev(3, "AI could even form intimate relationships with people, and use the power of intimacy to change our opinions and worldviews") +
          ev(4, "AI can create completely new ideas, completely new culture") +
          ev(2, "try to imagine the impact of AI tools that can be made to mass-produce political content, fake-news stories and scriptures for new cults")),
       ("The odd one", p("The author says AI could use intimacy to change opinions. He never says it would deepen political polarisation."))) +
 final("Option 1."),
 "except",
 [("2", "AI creating “completely new culture” is one of his main worries."),
  ("3", "Mass-produced fake news around an election, and the end of meaningful democratic conversation."),
  ("4", "He asks what happens when AI is better than humans at stories, melodies, images, laws and scriptures.")])

P.rc(2, "P1", "Inference", "3", "Easy",
 "The last paragraph is about regulation. What does the author say is at stake?",
 steps(("The author’s worry", ev(5, "Unregulated AI deployments would create social chaos, which would benefit autocrats and ruin democracies.") +
          ev(5, "When AI hacks language, it could destroy our ability to have meaningful conversations, thereby destroying democracy")),
       ("So", p("He would agree that democracy is one of the biggest casualties of unregulated AI."))) +
 final("Option 3."),
 "inference",
 [("1", "He deliberately doesn’t discuss AI’s benefits."),
  ("2", "He says the danger now comes from an unexpected direction; he doesn’t call the fear of harm unfounded."),
  ("4", "He says the school-essay worry misses the bigger picture, not that it is unfounded.")])

P.rc(3, "P1", "Except", "4", "Medium",
 "Why is language the “operating system”? Look at what the author says culture is built from.",
 steps(("The reasons", ev(2, "Language is the stuff almost all human culture is made of.") +
          ev(2, "they are cultural artefacts we created by telling stories and writing laws") +
          ev(3, "Through its mastery of language, AI could even form intimate relationships with people, and use the power of intimacy to change our opinions and worldviews.")),
       ("The odd one", p("Language is the operating system because culture, values and opinions run on it. That AI tools are built on language and can write academic content is not the reason given; the author even sets school essays aside."))) +
 final("Option 4."),
 "except",
 [("1", "Human rights and gods are cultural artefacts created through stories and writing."),
  ("2", "Almost all human culture is made of language."),
  ("3", "Language lets AI form intimate ties and so change opinions.")])

P.rc(4, "P1", "Tone", "4", "Medium",
 "The author warns, then proposes regulation. Is he panicking, puzzled, or warning?",
 steps(("The tone", ev(5, "We can still regulate the new AI tools, but we must act quickly.") +
          p("He lays out the harms of unregulated AI and calls for specific safeguards, such as requiring AI to disclose that it is an AI. That is a warning with a remedy.")),
       ("Choosing", p("“Cautionary” fits best."))) +
 final("Option 4."),
 "inference",
 [("1", "The questions are rhetorical; the closing question is a flourish, not a sign of puzzlement."),
  ("2", "He is measured and offers solutions, so “alarmist” is too strong."),
  ("3", "“Prescient” is a judgement about whether he turns out to be right, not a description of his tone.")])

P.va(5, P.summ(5), P.Q["VARC"][5]["opts"], "MCQ", "2", "Summary", "Medium",
 "The passage sets up a clash, then says “however”. What does the second strand of Marxism see in lyric poetry?",
 steps(("What the passage says", "<ol><li>Lyric poetry is personal, while Marxism seeks social change, so they seem incompatible.</li><li>But one strand of Marxism finds in lyric poetry ways of seeing that resist a repressive reality.</li><li>So poetry can be implicitly critical and utopian.</li></ol>"),
       ("Choosing", p("Option 2 keeps the apparent mismatch and the possibility of poetry as resistance."))) +
 final("Option 2."),
 "summary",
 [("1", "The passage doesn’t say one strand of Marxism sees no merit in lyric poetry."),
  ("3", "“Unless the difference is resolved” is not in the passage, and “utopian” is used positively there."),
  ("4", "The passage doesn’t say Marxism ignores poetry’s merits.")])

P.va(6, P.ms(6), ["Option 3", "Option 4", "Option 1", "Option 2"], "MCQ", "1", "Missing_Sentence", "Hard",
 "The sentence lists costs employees “haven’t incurred for nearly two years”. Which sentence picks up from that?",
 steps(("The link", p("After blank (3) comes: “This is especially jarring for workers who were able to save during remote work, when these expenditures weren’t a factor.” “These expenditures” are the transport, lunches and childcare in the missing sentence. So the sentence belongs at blank (3).")),
       ("What comes before", p("Just before blank (3), the paragraph says wages haven’t kept up with inflation. “This reality”, rising costs and flat wages, follows naturally.")),
       ("Reading the options", p("Blank (3) is listed first, so the answer is option 1."))) +
 final("Blank (3), which is option 1."),
 "missing",
 [("2", "Blank (4) is after “This is especially jarring…”, which needs the list of costs before it."),
  ("3", "At blank (1) there is no “reality” yet for the sentence to refer to."),
  ("4", "At blank (2) the paragraph hasn’t yet mentioned wages, so “this reality” would be incomplete.")])

P.va(7, P.ms(7), ["Option 1", "Option 2", "Option 3", "Option 4"], "MCQ", "3", "Missing_Sentence", "Medium",
 "The sentence steps back from the picture to its date, place and meaning. Where does the paragraph finish describing the image?",
 steps(("The description", p("Blanks (1) and (2) sit inside the description of the photo: the smoke, the faces, the soldiers following behind.")),
       ("The fit", p("After the soldiers, the paragraph turns to the picture’s title. The missing sentence, which says when and where the picture was taken and what it captured, bridges the two at blank (3)."))) +
 final("Blank (3), which is option 3."),
 "missing",
 [("1", "Blank (1) interrupts the move from “defining image” straight into what the image shows."),
  ("2", "Blank (2) splits the description of the children from the soldiers behind them."),
  ("4", "Blank (4) is after the title and nickname; the date and place would come too late.")])

# ---------------- Passage 2 ----------------
P.rc(8, "P2", "Inference", "3", "Hard",
 "Look at the third success factor and the biggest long-run risk. Both are about age.",
 steps(("A reason for success", ev(5, "Third, Moutai looks beyond affluent millennials and digital natives. The elderly and the middle-aged, it found, can be just as lucrative.")),
       ("A threat", ev(7, "In the long run, its biggest risk may be millennials. As they grow older, health concerns, work-life balance and the desire for more wholesome pursuits than binge-drinking may curb the “Ganbei!” toasting culture") +
          p("Its reliance on older drinkers works now, but as the younger generation ages it may not take up the same habits."))) +
 final("Option 3."),
 "inference",
 [("1", "Serving the rich is a strength; the passage doesn’t present it as a risk."),
  ("2", "The toasting culture is a source of demand, but it isn’t one of the three success factors."),
  ("4", "Government meddling is a risk, but it isn’t a reason for success.")])

P.rc(9, "P2", "Purpose", "3", "Medium",
 "Why would a Western business writer call nationalism, elitism and ageism “unholy”?",
 steps(("The setting", ev(2, "It does this while disregarding every Western marketing mantra.") +
          ev(6, "Moutai has succeeded thanks to nationalism, elitism and ageism, in other words—not in spite of this unholy trinity.")),
       ("So", p("The three are “unholy” from the Western point of view: they go against everything Western marketing preaches, yet they work."))) +
 final("Option 3."),
 "purpose",
 [("1", "Nationalism is only one of the three."),
  ("2", "The risks come afterwards and are different: the government and millennials."),
  ("4", "The phrase isn’t about liquor marketing being unholy in general.")])

P.rc(10, "P2", "Vocabulary", "1", "Easy",
 "Is the writer really comparing a drink with gunpowder?",
 steps(p("A hangover-proof liquor would be a wonderful invention, so the writer jokingly ranks it with one of China’s great inventions. The comparison is figurative, not literal.")) +
 final("Option 1."),
 "detail",
 [("2", "No one literally thinks liquor rivals gunpowder."),
  ("3", "“Substantive” means real or factual, which this joke isn’t."),
  ("4", "“Synonymical” would mean the two words mean the same thing.")])

P.rc(11, "P2", "Except", "4", "Medium",
 "What does the passage say about the middle-class market?",
 steps(("The middle class", ev(4, "Markets are littered with the corpses of firms that could not compete in the cut-throat battle for Chinese middle-class wallets.") +
          p("The passage presents the middle class as a market where firms fail, not one where money is easily made.")),
       ("The others", ev(4, "still less crowded with prestige brands than advanced economies") +
          ev(6, "It appears to want prices to remain stable."))) +
 final("Option 4."),
 "except",
 [("1", "The battle for middle-class wallets is “cut-throat”."),
  ("2", "The premium market is less crowded with prestige brands."),
  ("3", "The government, as the largest shareholder, wants to keep prices stable.")])

P.va(12, P.summ(12), P.Q["VARC"][12]["opts"], "MCQ", "4", "Summary", "Hard",
 "The passage says the tradwife both exposes the artifice of modern life and outrages people by taking it literally. Which option keeps both?",
 steps(("What the passage says", "<ol><li>The tradwife takes the fantasy of a storybook past literally.</li><li>In doing so she shows how much of our lives is artifice and playacting.</li><li>She outrages people and leaves them feeling cheated, which challenges current norms.</li></ol>"),
       ("Choosing", p("Option 4 keeps the dress and traditional roles, the light they throw on the superficiality of modern life, and the challenge to current norms."))) +
 final("Option 4."),
 "summary",
 [("1", "The passage doesn’t say she critiques society’s ideals; she beats us at our own game."),
  ("2", "It leaves out the outrage and the challenge she poses."),
  ("3", "“Mocks societal norms” attributes an intention the passage doesn’t give her.")])

P.va(13, P.ms(13), ["Option 4", "Option 1", "Option 3", "Option 2"], "MCQ", "1", "Missing_Sentence", "Medium",
 "The sentence is about people leaving their homes. Which sentence talks about going back?",
 steps(("The link", p("The last sentence reads: “Some, like the pastoralists, may never be able to go back as their livelihoods have been irreversibly wiped out.” “Go back” needs the displacement in the missing sentence. So it goes at blank (4), right after the farmers and pastoralists lose their livelihoods.")),
       ("Reading the options", p("Blank (4) is listed first, so the answer is option 1."))) +
 final("Blank (4), which is option 1."),
 "missing",
 [("2", "Blank (1) is between the drought and the failed rainy seasons; displacement would come too early."),
  ("3", "Blank (3) sits between “far-reaching damage” and its examples."),
  ("4", "Blank (2) is between food insecurity and deaths, and nothing nearby mentions going back.")])

P.va(14, P.sents(14), [], "TITA", "2", "Odd_One_Out", "Medium",
 "Sentence 3 begins “This was true even though the latter…”. Which sentence mentions two groups, so that “the latter” makes sense?",
 steps(("The chain", p("Sentence 1 says forecasting doesn’t need expertise. Sentence 5 says non-experts’ aggregated forecasts beat experts’. Sentence 4 gives the study: forecasters beat the US intelligence community. Sentence 3 adds that this was true even though “the latter”, the intelligence community, had classified information.")),
       ("The extra sentence", p("Sentence 2 is about why the idea interested the intelligence community and links forecasting to modelling the world. It doesn’t fit the point about non-experts beating experts."))) +
 final(r"\(2\)"),
 "oddone",
 [("1", "Forecasting needs no special expertise."), ("5", "Non-experts beat experts."), ("4", "The study that shows it."), ("3", "“The latter” is the intelligence community in sentence 4.")],
 why_title="How the other sentences fit")

P.va(15, P.sents(15), [], "TITA", "1", "Odd_One_Out", "Medium",
 "Four sentences tell a story of development before birth. One describes the anatomy of a synapse instead.",
 steps(("The chain", p("Sentence 4 says connections between eyes and brain form before birth. Sentence 2 calls this a “fetal warm-up act” and says it matters. Sentence 5 describes this rehearsal: synapses are made in excess and later pruned. Sentence 3 discusses why the pruning happens.")),
       ("The extra sentence", p("Sentence 1 explains how a neuron forms a synapse at the end of its axon. It is a technical aside, not part of the developmental story."))) +
 final(r"\(1\)"),
 "oddone",
 [("4", "Connections form before birth."), ("2", "“This fetal warm-up act”."), ("5", "“This rehearsal period”: synapses made in excess."), ("3", "“This paring back”: why they are pruned.")],
 why_title="How the other sentences fit")

# ---------------- Passage 3 ----------------
P.rc(16, "P3", "Except", "2", "Medium",
 "Go through the author’s reasons for dismissing contamination concerns. Which option is never claimed?",
 steps(("The reasons given", ev(1, "robotic exploration reveals a bleak, rusted landscape, lacking oxygen and flooded with radiation ready to sterilize any Earthly microbes") +
          ev(1, "many international competitors will ignore the demands of these protection extremists in any case") +
          ev(1, "NASA’s previous human exploration efforts made no serious attempt at sterility, with little notice.")),
       ("The one not given", p("The author never says probes used on the moon had little effect on its environment. He says the moon would kill nearly anything, and that Apollo left litter."))) +
 final("Option 2."),
 "except",
 [("1", "Mars looks lifeless and would sterilize microbes, so contamination is a moot point."),
  ("3", "China grew a seed on the moon with no protest; competitors will ignore such demands."),
  ("4", "Apollo left bacteria-infested litter, including bags of faeces.")])

P.rc(17, "P3", "Tone", "2", "Easy",
 "How does the author describe the people who want to keep space sterile?",
 steps(("The words", ev(1, "NASA incurs great expense sterilizing robotic probes in order to prevent the contamination of entirely theoretical biospheres") +
          p("“Entirely theoretical”, “purely speculative Martian fungi” and “protection extremists” show he doubts the value of these efforts.")),
       ("Choosing", p("He is sceptical of excessive sterilisation where life hasn’t been shown to exist."))) +
 final("Option 2."),
 "inference",
 [("1", "He criticises the expense; he doesn’t approve of it."),
  ("3", "He objects to the elitism, so he isn’t indifferent."),
  ("4", "He takes a clear position, so “equivocal” doesn’t fit.")])

P.rc(18, "P3", "Inference", "3", "Medium",
 "China’s own scientists didn’t protest; the space community was outraged at the Israeli case. What does the contrast show?",
 steps(("The two reactions", ev(1, "China recently sent a terrarium to the moon and germinated a plant seed—with, unsurprisingly, no protest from its own scientific community.") +
          ev(1, "a firestorm was unleashed within the space community")),
       ("So", p("Scientific communities in different places react differently to the same kind of issue: their sensitivity to biosphere protection varies."))) +
 final("Option 3."),
 "inference",
 [("1", "The passage doesn’t compare the harm from animals and plants."),
  ("2", "The author doesn’t suggest bias against particular countries."),
  ("4", "The point is the varying reactions, not that China’s approach is reasonable.")])

P.rc(19, "P3", "Except", "4", "Medium",
 "Three options match the author’s views. Which one would he push back against?",
 steps(("His view", ev(1, "The upsides from human exploration and development of Mars clearly outweigh the welfare of purely speculative Martian fungi.") +
          p("He wants exploration to go ahead now, without waiting until life has been ruled out.")),
       ("The others", ev(1, "A reasonable compromise is to continue on the course laid out by the U.S. government and the National Research Council, which proposed a system of zones on Mars"))) +
 final("Option 4."),
 "except",
 [("1", "He calls the zoning plan a reasonable compromise."),
  ("2", "He notes Apollo made no serious attempt at sterility, with little notice."),
  ("3", "He says full clean-up would destroy NASA’s human exploration budget.")])

# ---------------- Passage 4 ----------------
P.rc(20, "P4", "Except", "3", "Hard",
 "The passage names two causes of language loss in North America. Which option has nothing to do with either?",
 steps(("The causes", ev(1, "the physical annihilation of communities of native speakers of a language is all too often the cause of language extinction") +
          ev(1, "the removal of native children from their communities to federal boarding schools where native languages and cultural practices were prohibited") +
          ev(2, "young people see education, jobs, culture and technology associated with the dominant language and focus their attention on that language")),
       ("The odd one", p("Fewer killings, no boarding schools, or less success in assimilating locals could each explain better survival. Jobs in the colonial administration would do the opposite: they would tie people to the dominant language."))) +
 final("Option 3."),
 "except",
 [("1", "Children staying with their families avoids the boarding-school effect."),
  ("2", "Failing to mainstream locals keeps the dominant language from taking over."),
  ("4", "Fewer killings means more speakers survive.")])

P.rc(21, "P4", "Weaken", "2", "Hard",
 "The passage wants students to learn languages to appreciate other cultures and support endangered languages. Which scenario cuts against that?",
 steps(("The central idea", ev(4, "When students study languages other than their own, they are sensitized to the existence of different cultural perspectives and practices.") +
          ev(2, "The largest language \"killers\" are English, Spanish, Portuguese, French, Russian, Hindi, and Chinese")),
       ("The undermining scenario", p("If a liberal arts education meant learning two of the most widely spoken languages, it would push students towards the dominant “killer” languages, which is the opposite of what the passage hopes for."))) +
 final("Option 2."),
 "weaken",
 [("1", "The passage already says most students won’t pursue linguistics."),
  ("3", "Even if schools preserve a language for only a generation, preservation still works for a while."),
  ("4", "Recording a language freezing it in time doesn’t touch the argument for education.")])

P.rc(22, "P4", "Application", "2", "Medium",
 "The loss the passage describes is knowledge, worldview and culture. Which option describes a different kind of loss?",
 steps(("The loss", ev(2, "When we lose a language, we lose the worldview, culture and knowledge of the people who spoke it, constituting a loss to all humanity.")),
       ("The odd one", p("Losing a name from a government list of tribes is an administrative change, not a loss of knowledge or worldview."))) +
 final("Option 2."),
 "inference",
 [("1", "Words for snow carry knowledge of the environment."),
  ("3", "A word for a particular loss carries a concept and an emotion."),
  ("4", "Words for the ocean’s moods carry knowledge of nature that is lost with the language.")])

P.rc(23, "P4", "Except", "2", "Medium",
 "List what the passage says such students will be able to do. Which option is something only a few will do, if anyone?",
 steps(("The benefits", ev(4, "students are more likely to be able to articulate insights into their own cultural biases, be more empathetic to individuals of other cultures, communicate successfully across linguistic and cultural differences")),
       ("The odd one", p("Schools teaching endangered languages were set up by Navajo, Cree and Inuit communities. The passage never says students will establish such schools."))) +
 final("Option 2."),
 "except",
 [("1", "They gain insight into their own cultural biases."),
  ("3", "They communicate successfully across linguistic and cultural differences."),
  ("4", "They study languages other than their own.")])

P.va(24, P.summ(24), P.Q["VARC"][24]["opts"], "MCQ", "3", "Summary", "Medium",
 "The passage ends with a question. Does it answer it?",
 steps(("What the passage says", "<ol><li>We can now engineer crops and microbes.</li><li>Regulation is outdated and not flexible enough.</li><li>It is an open question whether regulation can ever keep up with unpredictable living things.</li></ol>"),
       ("Choosing", p("Option 3 keeps both the problem (outdated regulation) and the doubt (whether a flexible enough framework is possible)."))) +
 final("Option 3."),
 "summary",
 [("1", "“Impossible” is too strong; the passage only raises the question."),
  ("2", "The passage doesn’t call for a new framework; it doubts whether one can keep up."),
  ("4", "Scientists shaping regulation isn’t mentioned.")])
