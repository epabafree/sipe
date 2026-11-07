# -*- coding: utf-8 -*-
# Batch 14 — CAT 2019 Slot 1: VARC (20 of 34). DILR and QA: b14_19s1_dilr.py, b14_19s1_qa.py.
from fmt import steps, final, trap, ev, why, table, p
from paperlib import Paper

P = Paper(2019, 1, "ex14_19s1.json")
P.passage("P2", "Passage 2 — How Emperor Penguins stay warm", "Science_and_Technology")
P.passage("P3", "Passage 3 — Folk, fashionable and unfashionable", "Arts_and_Literature")
P.passage("P4", "Passage 4 — Who told the tale of Aladdin", "Arts_and_Literature")
P.passage("P5", "Passage 5 — Topophilia", "Social_Science_and_History")

# ---------------- Verbal ability (Q2) ----------------
P.va(2, P.summary_html(2, "Vance Packard"), P.Q["VARC"][2]["opts"], "MCQ", "1", "Summary", "Medium",
 "Packard wrote about the supraliminal, not the subliminal. Are the people aware of being persuaded?",
 steps(("What the passage says", "<ol><li>Advertisers used depth interviews to find hidden motivations.</li><li>Packard wasn’t writing about subliminal advertising.</li><li>People can be persuaded by supraliminal messages without knowing it.</li></ol>"),
       ("Choosing", p("Option 1 has supraliminal and unaware."))) +
 final("Option 1"),
 "summary",
 [("2", "Says subliminal, and builds on conscious awareness."), ("3", "Says the people are aware."), ("4", "Says subliminal, which the passage rules out.")])

# ---------------- Passage 2: Penguins ----------------
P.rc(10, "P2", "Detail", "3", "Hard",
 "Read the last paragraph. What makes ‘every bit of warmth’ count?",
 steps(("The last paragraph", ev(4, "given the Emperors’ unusually demanding breeding cycle, every bit of warmth counts … [male penguins] don’t eat anything during [the incubation period of 64 days]") +
          p("Breeding drains their heat: long treks and weeks without food.")),
       ("The others", p("Metabolism of food keeps them warm. The plumage insulates. Convection gives a little heat back."))) +
 final("Option 3"),
 "detail",
 [("1", "Metabolism maintains body heat."), ("2", "Plumage insulates the body."), ("4", "Convection brings heat back to the penguins.")])

P.rc(11, "P2", "Except", "2", "Hard",
 "The finding is that most of the plumage is colder than the air. Which option leaves that intact?",
 steps(("The finding", p("The plumage on head, chest and back is colder than the air, so it can draw heat through convection.")),
       ("Checking", p("Option 2 only changes the feet, which were already the warmest part and above the air temperature. The plumage is unaffected.")),
       ("The others", p("No convection (1), air colder than the plumage (3), and positive plumage temperatures above the air (4) would each overturn the finding."))) +
 final("Option 2"),
 "except",
 [("1", "No convection means no heat gained back."), ("3", "Air at −10 is colder than the plumage."), ("4", "Plumage warmer than the air can’t draw heat from it.")])

P.rc(12, "P2", "Purpose", "4", "Medium",
 "What is surprising about ‘keeping their outer surface below air temperature’?",
 steps(("The sentence", ev(2, "by keeping their outer surface below air temperature, the birds might paradoxically be able to draw very slight amounts of heat from the air") +
          p("Being colder on the outside helps them stay warm."))) +
 final("Option 4"),
 "purpose",
 [("1", "The plumage is kept colder, not warmer."), ("2", "Radiation loses heat; it isn’t gained."), ("3", "Describes the mechanism, not the paradox.")])

P.rc(13, "P2", "Detail", "1", "Medium",
 "‘Slightly warmer’ than what? The plumage.",
 steps(("The sentence", ev(3, "slightly warmer air comes into contact with the plumage and donates minute amounts of heat back to the penguins, then cycles away at a slightly colder temperature") +
          p("The air is warmer than the plumage; after giving up heat it is colder."))) +
 final("Option 1"),
 "detail",
 [("2", "The air isn’t warmed by the penguins."), ("3", "It is the outside air, not air in the plumage."), ("4", "Not air inside the body.")])

# ---------------- Passage 3: Folk ----------------
P.rc(15, "P3", "Inference", "1", "Medium",
 "The author calls folk ‘contested territory’ and ‘constant transformation’.",
 steps(("The author’s view", p("Folk is contested, plural, always changing, and tense with newness.")),
       ("The odd one", p("‘Unusual poise and homogeneity’ goes against all of that."))) +
 final("Option 1"),
 "inference",
 [("2", "Matches Sharp’s view of singers changing songs."), ("3", "Matches the past-and-present tension."), ("4", "Folk is ‘hip again’.")])

P.rc(16, "P3", "Purpose", "3", "Medium",
 "Radical Morris, now on genteel sofas.",
 steps(("The sentence", ev(2, "Just as the effusive floral prints of the radical William Morris now cover genteel sofas, so the revolutionary intentions of many folk historians and revivalists have led to music that is commonly regarded as parochial and conservative") +
          p("Radical once, conformist now."))) +
 final("Option 3"),
 "purpose",
 [("1", "The point is the change, not popularity."), ("2", "Influence comes up later, separately."), ("4", "The direction is reversed.")])

P.rc(17, "P3", "Inference", "2", "Hard",
 "What comes just before the phrase?",
 steps(("The context", ev(1, "an anticapitalist conservationism … that solaced itself with the vision of a preindustrial golden age. In Britain, folk may often appear a cosy, fossilised form") +
          p("The cosiness comes from looking back to a pre-industrial past.")),
       ("Not the others", p("Option 3 is what lies underneath, ‘when you look more closely’. It explains why folk is contested, not why it looks cosy."))) +
 final("Option 2"),
 "inference",
 [("1", "The shabby chic line comes later, about folk being hip."), ("3", "Explains the contest, not the cosy look."), ("4", "Debates are why it isn’t really cosy.")])

P.rc(18, "P3", "Except", "1", "Medium",
 "Is rock music said to be necessary for electrification?",
 steps(("The line", ev(3, "Electrification, however, comes in many forms") +
          p("The passage says the opposite of option 1: electrification came from many sources."))) +
 final("Option 1"),
 "except",
 [("2", "Purists were suspicious."), ("3", "Folk kept changing, as Sharp said."), ("4", "Lyrical freedom and the 60s.")])

P.rc(19, "P3", "Except", "2", "Medium",
 "Which option is about how folk is seen, not where its diversity comes from?",
 steps(("The causes", p("Heathen dark-age traces, oral transmission and obscure ancient origins all open folk up to variety.")),
       ("The odd one", p("Being fashionable and unfashionable at once describes its status. It doesn’t make it diverse."))) +
 final("Option 2"),
 "except",
 [("1", "“A whiff of Britain’s heathen dark ages”."), ("3", "Oral transmission keeps songs changing."), ("4", "Obscure origins open up space for fancies.")])

# ---------------- Passage 4: Aladdin ----------------
P.rc(22, "P4", "Except", "1", "Hard",
 "Evidence that the character is Diyab, not that Diyab told the story.",
 steps(("The evidence", p("Diyab’s hard upbringing, his wonder at Versailles, and his position between East and West all make him look like Aladdin.")),
       ("The odd one", p("Telling Galland the story shows where the story came from. It says nothing about the character being him."))) +
 final("Option 1"),
 "except",
 [("2", "Rags to riches, like Aladdin."), ("3", "The palace descriptions match."), ("4", "“The overlapping world of East and West”.")])

P.rc(23, "P4", "Main_Idea", "1", "Medium",
 "‘Its narrative drama isn’t the only reason’. What else?",
 steps(("The line", ev(4, "a story about Middle Easterners coming to Paris and that speaks to our world today") +
          p("Diyab’s experience as a traveller still resonates."))) +
 final("Option 1"),
 "inference",
 [("2", "The drama is ‘not the only reason’."), ("3", "History is part of it, but the point is today."), ("4", "Orientalism is the old theory.")])

P.rc(24, "P4", "Except", "3", "Medium",
 "Which option was used for the old view of where Aladdin came from?",
 steps(("The claim", p("Diyab is behind Aladdin: his travelogue, Galland’s diary, the Versailles descriptions.")),
       ("The odd one", p("French fairy tales were the earlier scholars’ explanation. They don’t support the new claim."))) +
 final("Option 3"),
 "except",
 [("1", "Diyab’s narrative skill supports him."), ("2", "Galland’s diary names him."), ("4", "The Versailles descriptions match.")])

P.rc(25, "P4", "Inference", "1", "Medium",
 "Where does the story come from, according to Horta?",
 steps(("The view", p("Diyab based it on his own life and told it to Galland, who put it in his Arabian Nights."))) +
 final("Option 1"),
 "inference",
 [("2", "Galland heard it; he didn’t take it from the travelogue."), ("3", "No manuscript predates Galland’s."), ("4", "Same problem with the manuscript.")])

P.rc(26, "P4", "Weaken", "3", "Hard",
 "The ‘script’ is flipped because Diyab’s view of France appears in the story. What breaks that link?",
 steps(("The inversion", p("Not a Frenchman imagining the East, but an Easterner encountering France. The evidence is that Diyab’s Versailles matches Aladdin’s palace.")),
       ("Breaking it", p("If the two descriptions didn’t resemble each other, nothing would tie the story to Diyab’s experience of France."))) +
 final("Option 3"),
 "weaken",
 [("1", "Bordeaux is still France."), ("2", "That removes the old theory, which helps the inversion."), ("4", "That would support Diyab’s role.")])

# ---------------- Passage 5: Topophilia ----------------
P.rc(29, "P5", "Purpose", "3", "Easy",
 "Read the sentence about upscale developments.",
 steps(("The line", ev(4, "casting themselves in a superior social position and by reinforcing class and racial differences") +
          p("An example of a darker topophilia: exclusivism."))) +
 final("Option 3"),
 "purpose",
 [("1", "They reinforce exclusion."), ("2", "Nationalist projects are a separate example."), ("4", "Nothing sensitive about it.")])

P.rc(30, "P5", "Application", "2", "Medium",
 "Topophilia is an affective bond with a place.",
 steps(("Choosing", p("Calling a land ‘motherland’ or ‘fatherland’ is an emotional bond with it."))) +
 final("Option 2"),
 "inference",
 [("1", "Topography isn’t the same as topophilia."), ("3", "Not supported."), ("4", "About language, not place.")])

P.rc(31, "P5", "Inference", "4", "Medium",
 "Why would it be hard to design for and impossible to quantify?",
 steps(("The reason", p("Responses vary by person in intensity, subtlety and mode, and aesthetic ones fade. They are subjective, so design can’t capture them."))) +
 final("Option 4"),
 "inference",
 [("1", "New urbanism is said to disappoint."), ("2", "The passage doesn’t say architects can’t be topophilic."), ("3", "Philosophers interpret it; they don’t design for it.")])

P.rc(32, "P5", "Vocabulary", "1", "Easy",
 "The last sentence defines it.",
 steps(("The line", ev(4, "a sense of dread or anxiety—or topophobia") +
          p("Dread towards places."))) +
 final("Option 1"),
 "detail",
 [("2", "Not about studying topography."), ("3", "Not fear of people."), ("4", "Non-citizens aren’t mentioned.")])

P.rc(33, "P5", "Inference", "4", "Medium",
 "Which option repeats what the passage says?",
 steps(("The line", ev(4, "Topophilia connotes a positive relationship, but it often is useful to explore the darker affiliations … Patriotism") +
          p("Patriotism is presented as a darker form of topophilia."))) +
 final("Option 4"),
 "inference",
 [("1", "New urbanism is ‘bound to disappoint’."), ("2", "Ties ‘vary greatly’."), ("3", "Tactile response is only a third kind.")])
