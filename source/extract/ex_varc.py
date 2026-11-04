# -*- coding: utf-8 -*-
# CAT 2023 Slot 1 — VARC pilot items (faithful to source; explanations rewritten/expanded)

P1_TITLE = "Passage 1 — Indian Ocean novels and the “remapping” of the world"
P1_DIRECTIONS = ("The passage below is accompanied by four questions. Based on the passage, "
                 "choose the best answer for each question.")
P1 = r"""
<p>For early postcolonial literature, the world of the novel was often the nation. Postcolonial novels were usually [concerned with] national questions. Sometimes the whole story of the novel was taken as an allegory of the nation, whether India or Tanzania. This was important for supporting anti-colonial nationalism, but could also be limiting – land-focused and inward-looking.</p>
<p>My new book “Writing Ocean Worlds” explores another kind of world of the novel: not the village or nation, but the Indian Ocean world. The book describes a set of novels in which the Indian Ocean is at the centre of the story. It focuses on the novelists Amitav Ghosh, Abdulrazak Gurnah, Lindsey Collen and Joseph Conrad [who have] centred the Indian Ocean world in the majority of their novels. . . . Their work reveals a world that is outward-looking – full of movement, border-crossing and South-South interconnection. They are all very different – from colonially inclined (Conrad) to radically anti-capitalist (Collen), but together draw on and shape a wider sense of Indian Ocean space through themes, images, metaphors and language. This has the effect of remapping the world in the reader’s mind, as centred in the interconnected global south. . . .</p>
<p>The Indian Ocean world is a term used to describe the very long-lasting connections among the coasts of East Africa, the Arab coasts, and South and East Asia. These connections were made possible by the geography of the Indian Ocean. For much of history, travel by sea was much easier than by land, which meant that port cities very far apart were often more easily connected to each other than to much closer inland cities. Historical and archaeological evidence suggests that what we now call globalisation first appeared in the Indian Ocean. This is the interconnected oceanic world referenced and produced by the novels in my book. . . .</p>
<p>For their part Ghosh, Gurnah, Collen and even Conrad reference a different set of histories and geographies than the ones most commonly found in fiction in English. Those [commonly found ones] are mostly centred in Europe or the US, assume a background of Christianity and whiteness, and mention places like Paris and New York. The novels in [my] book highlight instead a largely Islamic space, feature characters of colour and centralise the ports of Malindi, Mombasa, Aden, Java and Bombay. . . . It is a densely imagined, richly sensory image of a southern cosmopolitan culture which provides for an enlarged sense of place in the world.</p>
<p>This remapping is particularly powerful for the representation of Africa. In the fiction, sailors and travellers are not all European. . . . African, as well as Indian and Arab characters, are traders, nakhodas (dhow ship captains), runaways, villains, missionaries and activists. This does not mean that Indian Ocean Africa is romanticised. Migration is often a matter of force; travel is portrayed as abandonment rather than adventure, freedoms are kept from women and slavery is rife. What it does mean is that the African part of the Indian Ocean world plays an active role in its long, rich history and therefore in that of the wider world.</p>
"""
P1_NOTE = ("Source print reads “What does it mean is that…” in the last paragraph; restored to the "
           "original wording “What it does mean is that…”. Meaning unchanged.")

VARC = []

def rc(qno, question, options, answer, explanation, why_wrong, approach, subtype, diff):
    VARC.append(dict(section="VARC", qno=qno, set_id="2023_S1_VARC_P1", set_title=P1_TITLE,
        directions=P1_DIRECTIONS, context=P1, question=question, options=options, qtype="MCQ",
        answer=answer, explanation=explanation, why_wrong=why_wrong, approach=approach, concept="",
        hint="", topic=["VARC::RC::Literature", "Subtype::RC::" + subtype], difficulty=diff,
        source_note=P1_NOTE))

rc(1, "All of the following claims contribute to the “remapping” discussed by the passage, EXCEPT:",
   ["Indian Ocean novels have gone beyond the specifics of national concerns to explore rich regional pasts.",
    "Cosmopolitanism originated in the West and travelled to the East through globalisation.",
    "The global South, as opposed to the global North, was the first centre of globalisation.",
    "The world of early international trade and commerce was not the sole domain of white Europeans."],
   "2",
   r"""<p>The “remapping” is the shift of the reader’s mental map <b>away from a Europe/US-centred world and towards an interconnected global south</b>. Any claim that re-centres the West works <i>against</i> that remapping.</p>
<p>Option 2 says cosmopolitanism <b>originated in the West</b> and travelled East. The passage says the opposite: globalisation “first appeared in the Indian Ocean”, and the novels present “a southern cosmopolitan culture”. So option 2 does not contribute to the remapping — it is the exception.</p>""",
   r"""<ul>
<li><b>Option 1</b> contributes: the novels move beyond “the village or nation” (land-focused, inward-looking postcolonial fiction) to the wider Indian Ocean world.</li>
<li><b>Option 3</b> contributes: “what we now call globalisation first appeared in the Indian Ocean” — i.e., in the global South.</li>
<li><b>Option 4</b> contributes: in the fiction “sailors and travellers are not all European”; African, Indian and Arab characters are traders and nakhodas.</li>
</ul>""",
   r"""<p><b>EXCEPT questions:</b> first state the passage’s thesis in one line (“the world re-centred on the global south”). Then the answer is the option that <i>reverses</i> the thesis — here, the only option that puts the West at the origin.</p>""",
   "Except", "Medium")

rc(2, "On the basis of the nature of the relationship between the items in each pair below, choose the odd pair out:",
   ["Postcolonial novels : Border-crossing",
    "Indian Ocean novels : Outward-looking",
    "Indian Ocean world : Slavery",
    "Postcolonial novels : Anti-colonial nationalism"],
   "1",
   r"""<p>Three pairs link a subject to a feature the passage <b>attributes</b> to it. One pair links a subject to a feature the passage <b>denies</b> it.</p>
<p>Early postcolonial novels were “land-focused and inward-looking”. Border-crossing belongs to the <i>Indian Ocean</i> novels (“full of movement, border-crossing and South-South interconnection”). So <b>Postcolonial novels : Border-crossing</b> is a contrast pair, not a characteristic pair — it is the odd one out.</p>""",
   r"""<ul>
<li><b>Option 2</b> — characteristic pair: Indian Ocean novels reveal “a world that is outward-looking”.</li>
<li><b>Option 3</b> — characteristic pair: in the Indian Ocean world “slavery is rife”.</li>
<li><b>Option 4</b> — characteristic pair: postcolonial novels were “important for supporting anti-colonial nationalism”.</li>
</ul>""",
   r"""<p><b>Odd-pair questions:</b> label each pair’s relationship in one word (“has feature” / “lacks feature”). The odd pair is the one whose label differs.</p>""",
   "Odd_Pair", "Medium")

rc(3, "All of the following statements, if true, would weaken the passage’s claim about the relationship between mainstream English-language fiction and Indian Ocean novels EXCEPT:",
   ["Very few mainstream English-language novels have historically been set in American and European metropolitan centres.",
    "The depiction of Africa in most Indian Ocean novels is driven by an Orientalist imagination of its cultural crudeness.",
    "The depiction of Africa in most Indian Ocean novels is driven by a postcolonial nostalgia for an idyllic past.",
    "Most mainstream English-language novels have historically privileged the Christian, white, male experience of travel and adventure."],
   "4",
   r"""<p>The claim being tested is a <b>contrast</b>. Mainstream English fiction is “centred in Europe or the US” and assumes “Christianity and whiteness”. Indian Ocean novels instead present a largely Islamic space, characters of colour, and an Africa that is active and <i>not romanticised</i>.</p>
<p>Option 4 restates the passage’s description of mainstream fiction (Christian, white, travel and adventure). It <b>strengthens</b> the contrast rather than weakening it, so it is the exception.</p>""",
   r"""<ul>
<li><b>Option 1</b> weakens: it denies that mainstream fiction is centred on Western metropolitan places (“places like Paris and New York”).</li>
<li><b>Option 2</b> weakens: an Orientalist picture of African “cultural crudeness” contradicts the claim that these novels give Africa “an active role in its long, rich history”.</li>
<li><b>Option 3</b> weakens: a nostalgic, idyllic picture contradicts “This does not mean that Indian Ocean Africa is romanticised”.</li>
</ul>""",
   r"""<p><b>Weaken–EXCEPT:</b> three options will attack either side of the contrast. The answer usually <i>agrees</i> with the passage — look for the option that sounds like a paraphrase of a line in the text.</p>""",
   "Weaken_Except", "Hard")

rc(4, "Which one of the following statements is not true about migration in the Indian Ocean world?",
   ["Migration in the Indian Ocean world was an ambivalent experience.",
    "Geographical location rather than geographical proximity determined the choice of destination for migrants.",
    "The Indian Ocean world’s migration networks connected the global north with the global south.",
    "The Indian Ocean world’s migration networks were shaped by religious and commercial histories of the region."],
   "3",
   r"""<p>The passage describes the Indian Ocean world as linking “the coasts of East Africa, the Arab coasts, and South and East Asia”. It calls this a world of “<b>South-South</b> interconnection”, “centred in the interconnected global south”. Nothing suggests its networks joined the global <i>north</i> to the south. So option 3 is <b>not true</b>.</p>""",
   r"""<ul>
<li><b>Option 1</b> is true: migration is “often a matter of force” and travel “portrayed as abandonment rather than adventure”, yet the region’s history is “long, rich” — a mixed, ambivalent picture.</li>
<li><b>Option 2</b> is true: “port cities very far apart were often more easily connected to each other than to much closer inland cities” — position on the sea mattered more than nearness.</li>
<li><b>Option 4</b> is true: the space is “largely Islamic”, and the characters are traders and nakhodas — religious and commercial histories shape the networks.</li>
</ul>""",
   r"""<p><b>“Not true” questions:</b> look for options that swap a key term for its opposite. Here “South-South” has become “north–south”.</p>""",
   "Detail_Not_True", "Medium")

# ---------------- Verbal ability ----------------
def va(qno, question, options, qtype, answer, explanation, why_wrong, approach, sub, diff, note=""):
    VARC.append(dict(section="VARC", qno=qno, set_id="", set_title="", directions="", context="",
        question=question, options=options, qtype=qtype, answer=answer, explanation=explanation,
        why_wrong=why_wrong, approach=approach, concept="", hint="", topic=["VARC::VA::" + sub],
        difficulty=diff, source_note=note))

va(17, r"""<p>There is a sentence that is missing in the paragraph below. Look at the paragraph and decide where (option 1, 2, 3, or 4) the following sentence would best fit.</p>
<p class="quote"><b>Sentence:</b> The discovery helps to explain archeological similarities between the Paleolithic peoples of China, Japan, and the Americas.</p>
<p class="quote"><b>Paragraph:</b> The researchers also uncovered an unexpected genetic link between Native Americans and Japanese people. ___(1)___. During the deglaciation period, another group branched out from Northern coastal China and travelled to Japan. ___(2)___. “We were surprised to find that this ancestral source also contributed to the Japanese gene pool, especially the indigenous Ainus,” says Li. ___(3)___. They shared similarities in how they crafted stemmed projectile points for arrowheads and spears. ___(4)___. “This suggests that the Pleistocene connection among America, China, and Japan was not confined to culture but also to genetics,” says senior author Qing-Peng Kong, an evolutionary geneticist at the Chinese Academy of Sciences.</p>""",
   ["Option 2", "Option 4", "Option 3", "Option 1"], "MCQ", "3",
   r"""<p>The sentence fits in <b>blank (3)</b>, which is answer choice <b>3</b> (“Option 3”).</p>
<p>Before blank (3), Li reports the <b>genetic</b> finding: an ancestral source contributed to the Japanese gene pool. The inserted sentence says this <i>discovery</i> explains <b>archaeological similarities</b>. The next sentence — “<b>They</b> shared similarities in how they crafted stemmed projectile points” — gives an example of those similarities. “They” needs a plural antecedent, and “the Paleolithic peoples of China, Japan, and the Americas” supplies it.</p>""",
   r"""<ul>
<li><b>Blank (1)</b>: we have not yet heard the details of the discovery, so “the discovery helps to explain…” is premature, and “They shared…” would lose its referent.</li>
<li><b>Blank (2)</b>: it breaks the narrative of migration and Li’s comment on it.</li>
<li><b>Blank (4)</b>: the stemmed-points sentence would then refer back to nothing, and Kong’s closing quote (culture <i>and</i> genetics) already sums up.</li>
</ul>
<p class="warn">Watch the trap: the answer choices are shuffled labels. Choice 3 happens to say “Option 3”, but choice 1 says “Option 2”.</p>""",
   r"""<p><b>Look for a hook:</b> the sentence after the gap often contains a pronoun (“They”) that only the inserted sentence can explain.</p>""",
   "Missing_Sentence", "Easy")

va(19, r"""<p>Five jumbled up sentences (labelled 1, 2, 3, 4 and 5), related to a topic, are given below. Four of them can be put together to form a coherent paragraph. Identify the odd sentence and key in the number of that sentence as your answer.</p>
<ol class="sent">
<li>Having an appreciation for the workings of another person’s mind is considered a prerequisite for natural language acquisition, strategic social interaction, reflexive thought, and moral judgment.</li>
<li>It is a ‘theory of mind’ though some scholars prefer to call it ‘mentalising’ or ‘mindreading’, which is important for the development of one’s cognitive abilities.</li>
<li>Though we must speculate about its evolutionary origin, we do have indications that the capacity evolved sometime in the last few million years.</li>
<li>This capacity develops from early beginnings in the first year of life to the adult’s fast and often effortless understanding of others’ thoughts, feelings, and intentions.</li>
<li>One of the most fascinating human capacities is the ability to perceive and interpret other people’s behaviour in terms of their mental states.</li>
</ol>""",
   [], "TITA", "2",
   r"""<p><b>Odd sentence: 2.</b> &nbsp;Coherent order: <b>5 → 1 → 4 → 3</b>.</p>
<ul>
<li><b>5</b> introduces the topic: the capacity to interpret behaviour in terms of mental states.</li>
<li><b>1</b> says why it matters: it is a prerequisite for language, social interaction, reflexive thought and moral judgment.</li>
<li><b>4</b> describes how “this capacity” <i>develops</i> in an individual, from infancy to adulthood.</li>
<li><b>3</b> widens to how “the capacity” <i>evolved</i> in the species, over millions of years.</li>
</ul>
<p>Sentence 2 is about <b>terminology</b> — what to call the capacity (“theory of mind”, “mentalising”, “mindreading”). It also restates a benefit that sentence 1 already covers more precisely. Its opening “It is…” has no clean place in the chain 5-1-4-3: inserted anywhere, it interrupts the progression from capacity, to importance, to individual development, to evolutionary origin.</p>""",
   "", r"""<p><b>Odd-one-out:</b> build the strongest chain first, using demonstratives (“This capacity”, “the capacity”). The sentence that does a different <i>job</i> — here, naming the concept — is the odd one.</p>""",
   "Odd_One_Out", "Medium")

va(21, r"""<p>The four sentences (labelled 1, 2, 3 and 4) given below, when properly sequenced, would yield a coherent paragraph. Decide on the proper sequencing of the order of the sentences and key in the sequence of the four numbers as your answer.</p>
<ol class="sent">
<li>What precisely are the “unusual elements” that make a particular case so attractive to a certain kind of audience?</li>
<li>It might be a particularly savage or unfathomable level of depravity, very often it has something to do with the precise amount of mystery involved.</li>
<li>Unsolved, and perhaps unsolvable cases offer something that “ordinary” murder does not.</li>
<li>Why are some crimes destined for perpetual re-examination and others locked into permanent obscurity?</li>
</ol>""",
   [], "TITA", "4123",
   r"""<p><b>Answer: 4123</b></p>
<ul>
<li><b>4</b> opens with the broad question: why are some crimes re-examined forever while others are forgotten?</li>
<li><b>1</b> narrows it: what <i>precisely</i> are the “unusual elements” that make a case attractive?</li>
<li><b>2</b> answers sentence 1: “<b>It</b> might be” savage depravity, but very often it is “the precise amount of <b>mystery</b>”.</li>
<li><b>3</b> develops “mystery”: unsolved, perhaps unsolvable, cases offer something “ordinary” murder does not.</li>
</ul>
<p>The pairs that lock the order are <b>1→2</b> (question → “It might be…”) and <b>2→3</b> (“mystery” → “unsolved cases”). Sentence 4 is the most general, so it goes first.</p>""",
   "", r"""<p><b>Para-jumbles:</b> find a question–answer pair (1→2) and a keyword hand-off (“mystery” → “unsolved”). Two fixed links leave very few possible orders.</p>""",
   "Para_Jumble", "Medium",
   note="The source explanation describes the sentences in a different order from its own key (4123); the explanation has been rewritten to match the key.")

va(23, r"""<p>The passage given below is followed by four alternate summaries. Choose the option that best captures the essence of the passage.</p>
<p class="quote">Colonialism is not a modern phenomenon. World history is full of examples of one society gradually expanding by incorporating adjacent territory and settling its people on newly conquered territory. In the sixteenth century, colonialism changed decisively because of technological developments in navigation that began to connect more remote parts of the world. The modern European colonial project emerged when it became possible to move large numbers of people across the ocean and to maintain political control in spite of geographical dispersion. The term colonialism is used to describe the process of European settlement, violent dispossession and political domination over the rest of the world, including the Americas, Australia, and parts of Africa and Asia.</p>""",
   ["As a result of developments in navigation technology, European colonialism, led to the displacement of indigenous populations and global political changes in the 16th century.",
    "Colonialism, conceptualized in the 16th century, allowed colonizers to expand their territories, establish settlements, and exercise political power.",
    "Technological advancements in navigation in the 16th century, transformed colonialism, enabling Europeans to establish settlements and exert political dominance over distant regions.",
    "Colonialism surged in the 16th century due to advancements in navigation, enabling British settlements abroad and global dominance."],
   "MCQ", "3",
   r"""<p>The passage makes three points:</p>
<ol>
<li>colonialism is old, not modern;</li>
<li>in the 16th century it <b>changed decisively</b> because navigation technology connected remote regions;</li>
<li>this let Europeans <b>settle</b> people overseas and keep <b>political control</b> despite the distances.</li>
</ol>
<p>Option 3 keeps all of this: technology <i>transformed</i> an existing practice, and enabled European settlement and dominance over <i>distant</i> regions.</p>""",
   r"""<ul>
<li><b>Option 1</b> makes displacement and global political change the main point, and drops the idea that colonialism was <i>transformed</i> rather than begun.</li>
<li><b>Option 2</b> says colonialism was “conceptualized in the 16th century”, contradicting “Colonialism is not a modern phenomenon”.</li>
<li><b>Option 4</b> narrows “European” to “British”, which the passage never says.</li>
</ul>""",
   r"""<p><b>Summary questions:</b> eliminate options that contradict the text (2) or add something new (4, “British”). Then choose the option that keeps the passage’s <i>cause → effect</i> spine.</p>""",
   "Summary", "Easy")
