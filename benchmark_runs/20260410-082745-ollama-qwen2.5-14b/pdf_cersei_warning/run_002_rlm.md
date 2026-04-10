# pdf_cersei_warning - RLM run 002

- Script: `rlm-test/test_pdf_cersei_warning.py`
- Exit code: `0`
- Rate limit encountered: `no`
- Fatal rate-limit failure: `no`

## Terminal Output

```text
No cooldown configured for this backend.

╭─ ◆ RLM ━ Recursive Language Model ───────────────────────────────────────────╮
│                                                                              │
│    Backend                 openai            Environment            local    │
│    Model                   qwen2.5:14b       Max Iterations         5        │
│    Max Depth               3                                                 │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

────────────────────────────────  Iteration 1  ─────────────────────────────────
╭─ ◇ LLM Response  (89.90s) ───────────────────────────────────────────────────╮
│ ```repl                                                                      │
│ start = context.find("Cersei")                                               │
│ end = context.rfind("Ned", start) + len("Ned")  # Find last occurrence of    │
│ Ned within found Cersei range                                                │
│                                                                              │
│ if "warning" in context[start:end].lower():                                  │
│     warning_range_start = context.lower().rfind("warning", start, end)       │
│ else:                                                                        │
│     # If explicit word 'warning' missing, look for veiled tone indicators    │
│ like threat or caution                                                       │
│     warn_indicators = ["caution", "threaten", "danger"]                      │
│     for indicator in warn_indicators:                                        │
│         if indicator in context[start:end].lower():                          │
│             warning_range_start = context.lower().rfind(indicator, start,    │
│ end)                                                                         │
│             break                                                            │
│                                                                              │
│ warning_quote_end = context.find("\n", warning_range_start)                  │
│                                                                              │
│ final_quote_variable = context[warning_range_start:warning_quote_end]        │
│ print(final_quote_variable)                                                  │
│ ```                                                                          │
│                                                                              │
│ ~73 words                                                                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ ▸ Code Execution  (0.072s) ─────────────────────────────────────────────────╮
│ Code:                                                                        │
│ start = context.find("Cersei")                                               │
│ end = context.rfind("Ned", start) + len("Ned")  # Find last occurrence of    │
│ Ned within found Cersei range                                                │
│                                                                              │
│ if "warning" in context[start:end].lower():                                  │
│     warning_range_start = context.lower().rfind("warning", start, end)       │
│ else:                                                                        │
│     # If explicit word 'warning' missing, look for veiled tone indicators    │
│ like threat or caution                                                       │
│     warn_indicators = ["caution", "threaten", "danger"]                      │
│     for indicator in warn_indicators:                                        │
│         if indicator in context[start:end].lower():                          │
│             warning_range_start = context.lower().rfind(indicator, start,    │
│ end)                                                                         │
│             break                                                            │
│                                                                              │
│ warning_quote_end = context.find("\n", warning_range_start)                  │
│                                                                              │
│ final_quote_variable = context[warning_range_start:warning_quote_end]        │
│ print(final_quote_variable)                                                  │
│                                                                              │
│ Output:                                                                      │
│ warning?”                                                                    │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
────────────────────────────────  Iteration 2  ─────────────────────────────────
╭─ ◇ LLM Response  (102.51s) ──────────────────────────────────────────────────╮
│ The code seems to have missed slicing the context correctly up until `\n`.   │
│ Let's correct that:                                                          │
│ ```repl                                                                      │
│ start = context.find("Cersei")                                               │
│ end = context.rfind("Ned", start) + len("Ned")  # Find last occurrence of    │
│ Ned within found Cersei range                                                │
│                                                                              │
│ if "warning" in context[start:end].lower():                                  │
│     warning_range_start = context.lower().rfind("warning", start, end)       │
│ else:                                                                        │
│     warn_indicators = ["caution", "threaten", "danger"]                      │
│     for indicator in warn_indicators:                                        │
│         if indicator in context[start:end].lower():                          │
│             warning_range_start = context.lower().rfind(indicator, start,    │
│ end)                                                                         │
│             break                                                            │
│                                                                              │
│ # Correcting to find the proper closing of the quote                         │
│ warning_quote_end = context.find("\n\n", warning_range_start)  # Find double │
│ newline for correct close                                                    │
│                                                                              │
│ final_quote_variable = context[warning_range_start:warning_quote_end]        │
│ print(final_quote_variable)                                                  │
│ ```                                                                          │
│                                                                              │
│ ~91 words                                                                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ ▸ Code Execution  (0.043s) ─────────────────────────────────────────────────╮
│ Code:                                                                        │
│ start = context.find("Cersei")                                               │
│ end = context.rfind("Ned", start) + len("Ned")  # Find last occurrence of    │
│ Ned within found Cersei range                                                │
│                                                                              │
│ if "warning" in context[start:end].lower():                                  │
│     warning_range_start = context.lower().rfind("warning", start, end)       │
│ else:                                                                        │
│     warn_indicators = ["caution", "threaten", "danger"]                      │
│     for indicator in warn_indicators:                                        │
│         if indicator in context[start:end].lower():                          │
│             warning_range_start = context.lower().rfind(indicator, start,    │
│ end)                                                                         │
│             break                                                            │
│                                                                              │
│ # Correcting to find the proper closing of the quote                         │
│ warning_quote_end = context.find("\n\n", warning_range_start)  # Find double │
│ newline for correct close                                                    │
│                                                                              │
│ final_quote_variable = context[warning_range_start:warning_quote_end]        │
│ print(final_quote_variable)                                                  │
│                                                                              │
│ Output:                                                                      │
│ warning?”                                                                    │
│ The bloodstained messenger shook his head. “Our outriders had been           │
│ vanishing. Marq                                                              │
│ Piper’s work, we thought. The ones who did come back had seen nothing.”      │
│ “A man who sees nothing has no use for his eyes,” the Mountain declared.     │
│ “Cut them out                                                                │
│ and give them to your next outrider. Tell him you hope that four eyes might  │
│ see better                                                                   │
│ than two . . . and if not, the man after him will have six.”                 │
│ Lord Tywin Lannister turned his face to study Ser Gregor. Tyrion saw a       │
│ glimmer of gold                                                              │
│ as the light shone off his father’s pupils, but he could not have said       │
│ whether the look was                                                         │
│ one of approval or disgust. Lord Tywin was oft quiet in council, preferring  │
│ to listen                                                                    │
│ before he spoke, a habit Tyrion himself tried to emulate. Yet this silence   │
│ was                                                                          │
│ uncharacteristic even for him, and his wine was untouched.                   │
│ “You said they came at night,” Ser Kevan prompted.                           │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
────────────────────────────────  Iteration 3  ─────────────────────────────────
╭─ ◇ LLM Response  (124.29s) ──────────────────────────────────────────────────╮
│ It seems that the code did not precisely capture the moment where Cersei     │
│ gives a veiled warning to Ned. I need to refine my search:                   │
│                                                                              │
│ 1. Look for dialogue exchanges between Cersei and Ned specifically.          │
│ 2. Identify any line from Cersei directed at Ned where she hints or implies  │
│ something ominous, which might be a subtle warning in nature.                │
│                                                                              │
│ Re-running more refined searches for the exact interaction.                  │
│                                                                              │
│ ```repl                                                                      │
│ # Find Cersei's dialog in context                                            │
│                                                                              │
│ start = context.find('Cersei')                                               │
│ end = context.find('Ned', start + len("Cersei"))  # Find next "Ned" after    │
│ found "Cersei"                                                               │
│ if end == -1:                                                                │
│     # If Ned not found, look for last occurrence within large range from     │
│ Cersei                                                                       │
│     end = context.rfind('Ned')                                               │
│                                                                              │
│ cersei_quotes = []                                                           │
│ quote_start = start                                                          │
│                                                                              │
│ while quote_start != -1 and end > quote_start:                               │
│     next_cersei = context.find('Cersei', quote_start + len("Cersei"))  #     │
│ Look for Cersei dialogues sequentially                                       │
│     if next_cersei == -1:                                                    │
│         break                                                                │
│                                                                              │
│     cersei_text = context[quote_start:next_cersei].strip()                   │
│                                                                              │
│     # Filter for sentences directly addressing Ned or using tone words       │
│     warning_indicators = ["warning", "caution", "threaten"]                  │
│     for word in warning_indicators:                                          │
│         if word in cersei_text.lower():                                      │
│             final_quote_variable = context[quote_start+6 : next_cersei]  #   │
│ Trim to actual quote                                                         │
│             print(final_quote_variable)                                      │
│                                                                              │
│     quote_start = next_cersei + len("Cersei")                                │
│ ```                                                                          │
│                                                                              │
│ ~186 words                                                                   │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ ▸ Code Execution  (0.011s) ─────────────────────────────────────────────────╮
│ Code:                                                                        │
│ # Find Cersei's dialog in context                                            │
│                                                                              │
│ start = context.find('Cersei')                                               │
│ end = context.find('Ned', start + len("Cersei"))  # Find next "Ned" after    │
│ found "Cersei"                                                               │
│ if end == -1:                                                                │
│     # If Ned not found, look for last occurrence within large range from     │
│ Cersei                                                                       │
│     end = context.rfind('Ned')                                               │
│                                                                              │
│ cersei_quotes = []                                                           │
│ quote_start = start                                                          │
│                                                                              │
│ while quote_start != -1 and end > quote_start:                               │
│     next_cersei = context.find('Cersei', quote_start + len("Cersei"))  #     │
│ Look for Cersei dialogues sequentially                                       │
│     if next_cersei == -1:                                                    │
│         break                                                                │
│                                                                              │
│     cersei_text = context[quote_start:next_cersei].strip()                   │
│                                                                              │
│     # Filter for sentences directly addressing Ned or using tone words       │
│     warning_indicators = ["warning", "caution", "threaten"]                  │
│     for word in warning_indicators:                                          │
│         if word in cersei_text.lower():                                      │
│             final_quote_variable = context[quote_start+6 : next_cersei]  #   │
│ Trim to actual quote                                                         │
│             print(final_quote_variable)                                      │
│                                                                              │
│     quote_start = next_cersei + len("Cersei")                                │
│                                                                              │
│ Output:                                                                      │
│  and the children travel with them.”                                         │
│ “Robert will keep an easy pace for their sakes,” he said. “It is just as     │
│ well. That will give                                                         │
│ us more time to prepare.”                                                    │
│ “The queen’s brothers are also in the party,” she told him.                  │
│ Ned grimaced at that. There was small love between him and the queen’s       │
│ family, Catelyn                                                              │
│ knew. The Lannisters of Casterly Rock had come late to Robert’s cause, when  │
│ victory was                                                                  │
│ all but certain, and he had never forgiven them. “Well, if the price for     │
│ Robert’s company                                                             │
│ is an infestation of Lannisters, so be it. It sounds as though Robert is     │
│ bringing half his                                                            │
│ court.”                                                                      │
│ “Where the king goes, the realm follows,” she said.                          │
│ “It will be good to see the children. The youngest was still sucking at the  │
│ Lannister                                                                    │
│ woman’s teat the last time I saw him. He must be, what, five by now?”        │
│ “Prince Tommen is seven,” she told him. “The same age as Bran. Please, Ned,  │
│ guard your                                                                   │
│ tongue. The Lannister woman is our queen, and her pride is said to grow with │
│ every                                                                        │
│ passing year.”                                                               │
│ Ned squeezed her hand. “There must be a feast, of course, with singers, and  │
│ Robert will                                                                  │
│ want to hunt. I shall send Jory south with an honor guard to meet them on    │
│ the kingsroad                                                                │
│ and escort them back. Gods, how are we going to feed them all? On his way    │
│ already, you                                                                 │
│ said? Damn the man. Damn his royal hide.”                                    │
│                                                                              │
│ === PAGE 30 ===                                                              │
│ previous | Table of Contents | next                                          │
│                                                                              │
│ === PAGE 31 ===                                                              │
│ previous | Table of Contents | next                                          │
│ DAENERYS                                                                     │
│ Her brother held the gown up for her inspection. “This is beauty. Touch it.  │
│ Go on. Caress                                                                │
│ the fabric.”                                                                 │
│ Dany touched it. The cloth was so smooth that it seemed to run through her   │
│ fingers like                                                                 │
│ water. She could not remember ever wearing anything so soft. It frightened   │
│ her. She                                                                     │
│ pulled her hand away. “Is it really mine?”                                   │
│ “A gift from the Magister Illyrio,” Viserys said, smiling. Her brother was   │
│ in a high mood                                                               │
│ tonight. “The color will bring out the violet in your eyes. And you shall    │
│ have gold as well,                                                           │
│ and jewels of all sorts. Illyrio has promised. Tonight you must look like a  │
│ princess.”                                                                   │
│ A princess, Dany thought. She had forgotten what that was like. Perhaps she  │
│ had never                                                                    │
│ really known. “Why does he give us so much?” she asked. “What does he want   │
│ from us?”                                                                    │
│ For nigh on half a year, they had lived in the magister’s house, eating his  │
│ food, pampered                                                               │
│ by his servants. Dany was thirteen, old enough to know that such gifts       │
│ seldom come                                                                  │
│ without their price, here in the free city of Pentos.                        │
│ “Illyrio is no fool,” Viserys said. He was a gaunt young man with nervous    │
│ hands and a                                                                  │
│ feverish look in his pale lilac eyes. “The magister knows that I will not    │
│ forget my friends                                                            │
│ when I come into my throne.”                                                 │
│ Dany said nothing. Magister Illyrio was a dealer in spices, gemstones,       │
│ dragonbone, and                                                              │
│ other, less savory things. He had friends in all of the Nine Free Cities, it │
│ was said, and                                                                │
│ even beyond, in Vaes Dothrak and the fabled lands beside the Jade Sea. It    │
│ was also said                                                                │
│ that he’d never had a friend he wouldn’t cheerfully sell for the right       │
│ price. Dany listened                                                         │
│ to the talk in the streets, and she heard these things, but she knew better  │
│ than to                                                                      │
│ question her brother when he wove his webs of dream. His anger was a         │
│ terrible thing                                                               │
│ when roused. Viserys called it “waking the dragon.”                          │
│ Her brother hung the gown beside the door. “Illyrio will send the slaves to  │
│ bathe you. Be                                                                │
│ sure you wash off the stink of the stables. Khal Drogo has a thousand        │
│ horses, tonight he                                                           │
│ looks for a different sort of mount.” He studied her critically. “You still  │
│ slouch.                                                                      │
│ Straighten yourself” He pushed back her shoulders with his hands. “Let them  │
│ see that                                                                     │
│ you have a woman’s shape now.” His fingers brushed lightly over her budding  │
│ breasts                                                                      │
│ and tightened on a nipple. “You will not fail me tonight. If you do, it will │
│ go hard for you.                                                             │
│                                                                              │
│ === PAGE 32 ===                                                              │
│ You don’t want to wake the dragon, do you?” His fingers twisted her, the     │
│ pinch cruelly                                                                │
│ hard through the rough fabric of her tunic. “Do you?” he repeated.           │
│ “No,” Dany said meekly.                                                      │
│ Her brother smiled. “Good.” He touched her hair, almost with affection.      │
│ “When they                                                                   │
│ write the history of my reign, sweet sister, they will say that it began     │
│ tonight.”                                                                    │
│ When he was gone, Dany went to her window and looked out wistfully on the    │
│ waters of                                                                    │
│ the bay. The square brick towers of Pentos were black silhouettes outlined   │
│ against the                                                                  │
│ setting sun. Dany could hear the singing of the red priests as they lit      │
│ their night fires and                                                        │
│ the shouts of ragged children playing games beyond the walls of the estate.  │
│ For a                                                                        │
│ moment she wished she could be out there with them, barefoot and breathless  │
│ and                                                                          │
│ dressed in tatters, with no past and no future and no feast to attend at     │
│ Khal Drogo’s                                                                 │
│ manse.                                                                       │
│ Somewhere beyond the sunset, across the narrow sea, lay a land of green      │
│ hills and                                                                    │
│ flowered plains and great rushing rivers, where towers of dark stone rose    │
│ amidst                                                                       │
│ magnificent blue-grey mountains, and armored knights rode to battle beneath  │
│ the                                                                          │
│ banners of their lords. The Dothraki called that land Rhaesh Andahli, the    │
│ land of the                                                                  │
│ Andals. In the Free Cities, they talked of Westeros and the Sunset Kingdoms. │
│ Her                                                                          │
│ brother had a simpler name. “Our land,” he called it. The words were like a  │
│ prayer with                                                                  │
│ him. If he said them enough, the gods were sure to hear. “Ours by blood      │
│ right, taken                                                                 │
│ from us by treachery, but ours still, ours forever. You do not steal from    │
│ the dragon, oh,                                                              │
│ no. The dragon remembers.”                                                   │
│ And perhaps the dragon did remember, but Dany could not. She had never seen  │
│ this                                                                         │
│ land her brother said was theirs, this realm beyond the narrow sea. These    │
│ places he                                                                    │
│ talked of, Casterly Rock and the Eyrie, Highgarden and the Vale of Arryn,    │
│ Dorne and the                                                                │
│ Isle of Faces, they were just words to her. Viserys had been a boy of eight  │
│ when they fled                                                               │
│ King’s Landing to escape the advancing armies of the Usurper, but Daenerys   │
│ had been                                                                     │
│ only a quickening in their mother’s womb.                                    │
│ Yet sometimes Dany would picture the way it had been, so often had her       │
│ brother told her                                                             │
│ the stories. The midnight flight to Dragonstone, moonlight shimmering on the │
│ ship’s                                                                       │
│ black sails. Her brother Rhaegar battling the Usurper in the bloody waters   │
│ of the Trident                                                               │
│ and dying for the woman he loved. The sack of King’s Landing by the ones     │
│ Viserys called                                                               │
│ the Usurper’s dogs, the lords Lannister and Stark. Princess Elia of Dorne    │
│ pleading for                                                                 │
│ mercy as Rhaegar’s heir was ripped from her breast and murdered before her   │
│ eyes. The                                                                    │
│ polished skulls of the last dragons staring down sightlessly from the walls  │
│ of the throne                                                                │
│ room while the Kingslayer opened Father’s throat with a golden sword.        │
│                                                                              │
│ === PAGE 33 ===                                                              │
│ She had been born on Dragonstone nine moons after their flight, while a      │
│ raging summer                                                                │
│ storm threatened to rip the island fastness apart. They said that storm was  │
│ terrible. The                                                                │
│ Targaryen fleet was smashed while it lay at anchor, and huge stone blocks    │
│ were ripped                                                                  │
│ from the parapets and sent hurtling into the wild waters of the narrow sea.  │
│ Her mother                                                                   │
│ had died birthing her, and for that her brother Viserys had never forgiven   │
│ her.                                                                         │
│ She did not remember Dragonstone either. They had run again, just before the │
│ Usurper’s                                                                    │
│ brother set sail with his new-built fleet. By then only Dragonstone itself,  │
│ the ancient seat                                                             │
│ of their House, had remained of the Seven Kingdoms that had once been        │
│ theirs. It would                                                             │
│ not remain for long. The garrison had been prepared to sell them to the      │
│ Usurper, but one                                                             │
│ night Ser Willem Darry and four loyal men had broken into the nursery and    │
│ stolen them                                                                  │
│ both, along with her wet nurse, and set sail under cover of darkness for the │
│ safety of the                                                                │
│ Braavosian coast.                                                            │
│ She remembered Ser Willem dimly, a great grey bear of a man, half-blind,     │
│ roaring and                                                                  │
│ bellowing orders from his sickbed. The servants had lived in terror of him,  │
│ but he had                                                                   │
│ always been kind to Dany. He called her “Little Princess” and sometimes “My  │
│ Lady,” and                                                                   │
│ his hands were soft as old leather. He never left his bed, though, and the   │
│ smell of                                                                     │
│ sickness clung to him day and night, a hot, moist, sickly sweet odor. That   │
│ was when they                                                                │
│ lived in Braavos, in the big house with the red door. Dany had her own room  │
│ there, with                                                                  │
│ a lemon tree outside her window. After Ser Willem had died, the servants had │
│ stolen                                                                       │
│ what little money they had left, and soon after they had been put out of the │
│ big house.                                                                   │
│ Dany had cried when the red door closed behind them forever.                 │
│ They had wandered since then, from Braavos to Myr, from Myr to Tyrosh, and   │
│ on to                                                                        │
│ Qohor and Volantis and Lys, never staying long in any one place. Her brother │
│ would not                                                                    │
│ allow it. The Usurper’s hired knives were close behind them, he insisted,    │
│ though Dany                                                                  │
│ had never seen one.                                                          │
│ At first the magisters and archons and merchant princes were pleased to      │
│ welcome the                                                                  │
│ last Targaryens to their homes and tables, but as the years passed and the   │
│ Usurper                                                                      │
│ continued to sit upon the Iron Throne, doors closed and their lives grew     │
│ meaner. Years                                                                │
│ past they had been forced to sell their last few treasures, and now even the │
│ coin they had                                                                │
│ gotten from Mother’s crown had gone. In the alleys and wine sinks of Pentos, │
│ they called                                                                  │
│ her brother “the beggar king.” Dany did not want to know what they called    │
│ her.                                                                         │
│ “We will have it all back someday, sweet sister,” he would promise her.      │
│ Sometimes his                                                                │
│ hands shook when he talked about it. “The jewels and the silks, Dragonstone  │
│ and King’s                                                                   │
│ Landing, the Iron Throne and the Seven Kingdoms, all they have taken from    │
│ us, we will                                                                  │
│ have it back.” Viserys lived for that day. All that Daenerys wanted back was │
│ the big house                                                                │
│ with the red door, the lemon tree outside her window, the childhood she had  │
│ never                                                                        │
│ known.                                                                       │
│                                                                              │
│ === PAGE 34 ===                                                              │
│ There came a soft knock on her door. “Come,” Dany said, turning away from    │
│ the                                                                          │
│ window. Illyrio’s servants entered, bowed, and set about their business.     │
│ They were                                                                    │
│ slaves, a gift from one of the magister’s many Dothraki friends. There was   │
│ no slavery in                                                                │
│ the free city of Pentos. Nonetheless, they were slaves. The old woman, small │
│ and grey as                                                                  │
│ a mouse, never said a word, but the girl made up for it. She was Illyrio’s   │
│ favorite, a fair-                                                            │
│ haired, blue-eyed wench of sixteen who chattered constantly as she worked.   │
│ They filled her bath with hot water brought up from the kitchen and scented  │
│ it with                                                                      │
│ fragrant oils. The girl pulled the rough cotton tunic over Dany’s head and   │
│ helped her into                                                              │
│ the tub. The water was scalding hot, but Daenerys did not flinch or cry out. │
│ She liked the                                                                │
│ heat. It made her feel clean. Besides, her brother had often told her that   │
│ it was never too                                                             │
│ hot for a Targaryen. “Ours is the house of the dragon,” he would say. “The   │
│ fire is in our                                                               │
│ blood.”                                                                      │
│ The old woman washed her long, silver-pale hair and gently combed out the    │
│ snags, all in                                                                │
│ silence. The girl scrubbed her back and her feet and told her how lucky she  │
│ was. “Drogo                                                                  │
│ is so rich that even his slaves wear golden collars. A hundred thousand men  │
│ ride in his                                                                  │
│ khalasar, and his palace in Vaes Dothrak has two hundred rooms and doors of  │
│ solid                                                                        │
│ silver.” There was more like that, so much more, what a handsome man the     │
│ khal was, so                                                                 │
│ tall and fierce, fearless in battle, the best rider ever to mount a horse, a │
│ demon archer.                                                                │
│ Daenerys said nothing. She had always assumed that she would wed Viserys     │
│ when she                                                                     │
│ came of age. For centuries the Targaryens had married brother to sister,     │
│ since Aegon the                                                              │
│ Conqueror had taken his sisters to bride. The line must be kept pure,        │
│ Viserys had told                                                             │
│ her a thousand times; theirs was the kingsblood, the golden blood of old     │
│ Valyria, the                                                                 │
│ blood of the dragon. Dragons did not mate with the beasts of the field, and  │
│ Targaryens                                                                   │
│ did not mingle their blood with that of lesser men. Yet now Viserys schemed  │
│ to sell her                                                                  │
│ to a stranger, a barbarian.                                                  │
│ When she was clean, the slaves helped her from the water and toweled her     │
│ dry. The girl                                                                │
│ brushed her hair until it shone like molten silver, while the old woman      │
│ anointed her with                                                            │
│ the spiceflower perfume of the Dothraki plains, a dab on each wrist, behind  │
│ her ears, on                                                                 │
│ the tips of her breasts, and one last one, cool on her lips, down there      │
│ between her legs.                                                            │
│ They dressed her in the wisps that Magister Illyrio had sent up, and then    │
│ the gown, a                                                                  │
│ deep plum silk to bring out the violet in her eyes. The girl slid the gilded │
│ sandals onto her                                                             │
│ feet, while the old woman fixed the tiara in her hair, and slid golden       │
│ bracelets crusted                                                            │
│ with amethysts around her wrists. Last of all came the collar, a heavy       │
│ golden torc                                                                  │
│ emblazoned with ancient Valyrian glyphs.                                     │
│ “Now you look all a princess,” the girl said breathlessly when they were     │
│ done. Dany                                                                   │
│ glanced at her image in the silvered looking glass that Illyrio had so       │
│ thoughtfully                                                                 │
│ provided. A princess, she thought, but she remembered what the girl had      │
│ said, how Khal                                                               │
│ Drogo was so rich even his slaves wore golden collars. She felt a sudden     │
│ chill, and                                                                   │
│                                                                              │
│ === PAGE 35 ===                                                              │
│ gooseflesh pimpled her bare arms.                                            │
│ Her brother was waiting in the cool of the entry hall, seated on the edge of │
│ the pool, his                                                                │
│ hand trailing in the water. He rose when she appeared and looked her over    │
│ critically.                                                                  │
│ “Stand there,” he told her. “Turn around. Yes. Good. You look . . . ”        │
│ “Regal,” Magister Illyrio said, stepping through an archway. He moved with   │
│ surprising                                                                   │
│ delicacy for such a massive man. Beneath loose garments of flame-colored     │
│ silk, rolls of                                                               │
│ fat jiggled as he walked. Gemstones glittered on every finger, and his man   │
│ had oiled his                                                                │
│ forked yellow beard until it shone like real gold. “May the Lord of Light    │
│ shower you with                                                              │
│ blessings on this most fortunate day, Princess Daenerys,” the magister said  │
│ as he took                                                                   │
│ her hand. He bowed his head, showing a thin glimpse of crooked yellow teeth  │
│ through                                                                      │
│ the gold of his beard. “She is a vision, Your Grace, a vision,” he told her  │
│ brother. “Drogo                                                              │
│ will be enraptured.”                                                         │
│ “She’s too skinny,” Viserys said. His hair, the same silver-blond as hers,   │
│ had been pulled                                                              │
│ back tightly behind his head and fastened with a dragonbone brooch. It was a │
│ severe                                                                       │
│ look that emphasized the hard, gaunt lines of his face. He rested his hand   │
│ on the hilt of                                                               │
│ the sword that Illyrio had lent him, and said, “Are you sure that Khal Drogo │
│ likes his                                                                    │
│ women this young?”                                                           │
│ “She has had her blood. She is old enough for the khal,” Illyrio told him,   │
│ not for the first                                                            │
│ time. “Look at her. That silver-gold hair, those purple eyes . . . she is    │
│ the blood of old                                                             │
│ Valyria, no doubt, no doubt . . . and highborn, daughter of the old king,    │
│ sister to the new,                                                           │
│ she cannot fail to entrance our Drogo.” When he released her hand, Daenerys  │
│ found                                                                        │
│ herself trembling.                                                           │
│ “I suppose,” her brother said doubtfully. “The savages have queer tastes.    │
│ Boys, horses,                                                                │
│ sheep . . . ”                                                                │
│ “Best not suggest this to Khal Drogo,” Illyrio said.                         │
│ Anger flashed in her brother’s lilac eyes. “Do you take me for a fool?”      │
│ The magister bowed slightly. “I take you for a king. Kings lack the caution  │
│ of common                                                                    │
│ men. My apologies if I have given offense.” He turned away and clapped his   │
│ hands for                                                                    │
│ his bearers.                                                                 │
│ The streets of Pentos were pitch-dark when they set out in Illyrio’s         │
│ elaborately carved                                                           │
│ palanquin. Two servants went ahead to light their way, carrying ornate oil   │
│ lanterns with                                                                │
│ panes of pale blue glass, while a dozen strong men hoisted the poles to      │
│ their shoulders. It                                                          │
│ was warm and close inside behind the curtains. Dany could smell the stench   │
│ of Illyrio’s                                                                 │
│                                                                              │
│ === PAGE 36 ===                                                              │
│ pallid flesh through his heavy perfumes.                                     │
│ Her brother, sprawled out on his pillows beside her, never noticed. His mind │
│ was away                                                                     │
│ across the narrow sea. “We won’t need his whole khalasar,” Viserys said. His │
│ fingers                                                                      │
│ toyed with the hilt of his borrowed blade, though Dany knew he had never     │
│ used a sword                                                                 │
│ in earnest. “Ten thousand, that would be enough, I could sweep the Seven     │
│ Kingdoms                                                                     │
│ with ten thousand Dothraki screamers. The realm will rise for its rightful   │
│ king. Tyrell,                                                                │
│ Redwyne, Darry, Greyjoy, they have no more love for the Usurper than I do.   │
│ The                                                                          │
│ Dornishmen burn to avenge Elia and her children. And the smallfolk will be   │
│ with us.                                                                     │
│ They cry out for their king.” He looked at Illyrio anxiously. “They do,      │
│ don’t they?”                                                                 │
│ “They are your people, and they love you well,” Magister Illyrio said        │
│ amiably. “In                                                                 │
│ holdfasts all across the realm, men lift secret toasts to your health while  │
│ women sew                                                                    │
│ dragon banners and hide them against the day of your return from across the  │
│ water.” He                                                                   │
│ gave a massive shrug. “Or so my agents tell me.”                             │
│ Dany had no agents, no way of knowing what anyone was doing or thinking      │
│ across the                                                                   │
│ narrow sea, but she mistrusted Illyrio’s sweet words as she mistrusted       │
│ everything about                                                             │
│ Illyrio. Her brother was nodding eagerly, however. “I shall kill the Usurper │
│ myself,” he                                                                  │
│ promised, who had never killed anyone, “as he killed my brother Rhaegar. And │
│ Lannister too, the Kingslayer, for what he did to my father.”                │
│ “That would be most fitting,” Magister Illyrio said. Dany saw the smallest   │
│ hint of a smile                                                              │
│ playing around his full lips, but her brother did not notice. Nodding, he    │
│ pushed back a                                                                │
│ curtain and stared off into the night, and Dany knew he was fighting the     │
│ Battle of the                                                                │
│ Trident once again.                                                          │
│ The nine-towered manse of Khal Drogo sat beside the waters of the bay, its   │
│ high brick                                                                   │
│ walls overgrown with pale ivy. It had been given to the khal by the          │
│ magisters of Pentos,                                                         │
│ Illyrio told them. The Free Cities were always generous with the horselords. │
│ “It is not                                                                   │
│ that we fear these barbarians,” Illyrio would explain with a smile. “The     │
│ Lord of Light                                                                │
│ would hold our city walls against a million Dothraki, or so the red priests  │
│ promise . . . yet                                                            │
│ why take chances, when their friendship comes so cheap?”                     │
│ Their palanquin was stopped at the gate, the curtains pulled roughly back by │
│ one of the                                                                   │
│ house guards. He had the copper skin and dark almond eyes of a Dothraki, but │
│ his face                                                                     │
│ was hairless and he wore the spiked bronze cap of the Unsullied. He looked   │
│ them over                                                                    │
│ coldly. Magister Illyrio growled something to him in the rough Dothraki      │
│ tongue; the                                                                  │
│ guardsman replied in the same voice and waved them through the gates.        │
│ Dany noticed that her brother’s hand was clenched tightly around the hilt of │
│ his                                                                          │
│ borrowed sword. He looked almost as frightened as she felt. “Insolent        │
│ eunuch,” Viserys                                                             │
│                                                                              │
│ === PAGE 37 ===                                                              │
│ muttered as the palanquin lurched up toward the manse.                       │
│ Magister Illyrio’s words were honey. “Many important men will be at the      │
│ feast tonight.                                                               │
│ Such men have enemies. The khal must protect his guests, yourself chief      │
│ among them,                                                                  │
│ Your Grace. No doubt the Usurper would pay well for your head.”              │
│ “Oh, yes,” Viserys said darkly. “He has tried, Illyrio, I promise you that.  │
│ His hired knives                                                             │
│ follow us everywhere. I am the last dragon, and he will not sleep easy while │
│ I live.”                                                                     │
│ The palanquin slowed and stopped. The curtains were thrown back, and a slave │
│ offered a                                                                    │
│ hand to help Daenerys out. His collar, she noted, was ordinary bronze. Her   │
│ brother                                                                      │
│ followed, one hand still clenched hard around his sword hilt. It took two    │
│ strong men to                                                                │
│ get Magister Illyrio back on his feet.                                       │
│ Inside the manse, the air was heavy with the scent of spices, pinchfire and  │
│ sweet lemon                                                                  │
│ and cinnamon. They were escorted across the entry hall, where a mosaic of    │
│ colored glass                                                                │
│ depicted the Doom of Valyria. Oil burned in black iron lanterns all along    │
│ the walls.                                                                   │
│ Beneath an arch of twining stone leaves, a eunuch sang their coming.         │
│ “Viserys of the                                                              │
│ House Targaryen, the Third of his Name,” he called in a high, sweet voice,   │
│ “King of the                                                                 │
│ Andals and the Rhoynar and the First Men, Lord of the Seven Kingdoms and     │
│ Protector                                                                    │
│ of the Realm. His sister, Daenerys Stormborn, Princess of Dragonstone. His   │
│ honorable                                                                    │
│ host, Illyrio Mopatis, Magister of the Free City of Pentos.”                 │
│ They stepped past the eunuch into a pillared courtyard overgrown in pale     │
│ ivy. Moonlight                                                               │
│ painted the leaves in shades of bone and silver as the guests drifted among  │
│ them. Many                                                                   │
│ were Dothraki horselords, big men with red-brown skin, their drooping        │
│ mustachios                                                                   │
│ bound in metal rings, their black hair oiled and braided and hung with       │
│ bells. Yet among                                                             │
│ them moved bravos and sellswords from Pentos and Myr and Tyrosh, a red       │
│ priest even                                                                  │
│ fatter than Illyrio, hairy men from the Port of Ibben, and lords from the    │
│ Summer Isles                                                                 │
│ with skin as black as ebony. Daenerys looked at them all in wonder . . . and │
│ realized, with                                                               │
│ a sudden start of fear, that she was the only woman there.                   │
│ Illyrio whispered to them. “Those three are Drogo’s bloodriders, there,” he  │
│ said. “By the                                                                │
│ pillar is Khal Moro, with his son Rhogoro. The man with the green beard is   │
│ brother to                                                                   │
│ the Archon of Tyrosh, and the man behind him is Ser Jorah Mormont.”          │
│ The last name caught Daenerys. “A knight?”                                   │
│ “No less.” Illyrio smiled through his beard. “Anointed with the seven oils   │
│ by the High                                                                  │
│ Septon himself.”                                                             │
│ “What is he doing here?” she blurted.                                        │
│                                                                              │
│ === PAGE 38 ===                                                              │
│ “The Usurper wanted his head,” Illyrio told them. “Some trifling affront. He │
│ sold some                                                                    │
│ poachers to a Tyroshi slaver instead of giving them to the Night’s Watch.    │
│ Absurd law. A                                                                │
│ man should be able to do as he likes with his own chattel.”                  │
│ “I shall wish to speak with Ser Jorah before the night is done,” her brother │
│ said. Dany                                                                   │
│ found herself looking at the knight curiously. He was an older man, past     │
│ forty and                                                                    │
│ balding, but still strong and fit. Instead of silks and cottons, he wore     │
│ wool and leather.                                                            │
│ His tunic was a dark green, embroidered with the likeness of a black bear    │
│ standing on                                                                  │
│ two legs.                                                                    │
│ She was still looking at this strange man from the homeland she had never    │
│ known when                                                                   │
│ Magister Illyrio placed a moist hand on her bare shoulder. “Over there,      │
│ sweet princess,”                                                             │
│ he whispered, “there is the khal himself.”                                   │
│ Dany wanted to run and hide, but her brother was looking at her, and if she  │
│ displeased                                                                   │
│ him she knew she would wake the dragon. Anxiously, she turned and looked at  │
│ the man                                                                      │
│ Viserys hoped would ask to wed her before the night was done.                │
│ The slave girl had not been far wrong, she thought. Khal Drogo was a head    │
│ taller than                                                                  │
│ the tallest man in the room, yet somehow light on his feet, as graceful as   │
│ the panther in                                                               │
│ Illyrio’s menagerie. He was younger than she’d thought, no more than thirty. │
│ His skin                                                                     │
│ was the color of polished copper, his thick mustachios bound with gold and   │
│ bronze rings.                                                                │
│ “I must go and make my submissions,” Magister Illyrio said. “Wait here. I    │
│ shall bring                                                                  │
│ him to you.”                                                                 │
│ Her brother took her by the arm as Illyrio waddled over to the khal, his     │
│ fingers                                                                      │
│ squeezing so hard that they hurt. “Do you see his braid, sweet sister?”      │
│ Drogo’s braid was black as midnight and heavy with scented oil, hung with    │
│ tiny bells that                                                              │
│ rang softly as he moved. It swung well past his belt, below even his         │
│ buttocks, the end of it                                                      │
│ brushing against the back of his thighs.                                     │
│ “You see how long it is?” Viserys said. “When Dothraki are defeated in       │
│ combat, they cut                                                             │
│ off their braids in disgrace, so the world will know their shame. Khal Drogo │
│ has never                                                                    │
│ lost a fight. He is Aegon the Dragonlord come again, and you will be his     │
│ queen.”                                                                      │
│ Dany looked at Khal Drogo. His face was hard and cruel, his eyes as cold and │
│ dark as                                                                      │
│ onyx. Her brother hurt her sometimes, when she woke the dragon, but he did   │
│ not                                                                          │
│ frighten her the way this man frightened her. “I don’t want to be his        │
│ queen,” she heard                                                            │
│ herself say in a small, thin voice. “Please, please, Viserys, I don’t want   │
│ to, I want to go                                                             │
│                                                                              │
│ === PAGE 39 ===                                                              │
│ home.”                                                                       │
│ “Home?” He kept his voice low, but she could hear the fury in his tone. “How │
│ are we to                                                                    │
│ go home, sweet sister? They took our home from us!” He drew her into the     │
│ shadows, out                                                                 │
│ of sight, his fingers digging into her skin. “How are we to go home?” he     │
│ repeated,                                                                    │
│ meaning King’s Landing, and Dragonstone, and all the realm they had lost.    │
│ Dany had only meant their rooms in Illyrio’s estate, no true home surely,    │
│ though all they                                                              │
│ had, but her brother did not want to hear that. There was no home there for  │
│ him. Even                                                                    │
│ the big house with the red door had not been home for him. His fingers dug   │
│ hard into                                                                    │
│ her arm, demanding an answer. “I don’t know . . . ”she said at last, her     │
│ voice breaking.                                                              │
│ Tears welled in her eyes.                                                    │
│ “I do,” he said sharply. “We go home with an army, sweet sister. With Khal   │
│ Drogo’s                                                                      │
│ army, that is how we go home. And if you must wed him and bed him for that,  │
│ you will.”                                                                   │
│ He smiled at her. “I’d let his whole khalasar fuck you if need be, sweet     │
│ sister, all forty                                                            │
│ thousand men, and their horses too if that was what it took to get my army.  │
│ Be grateful it                                                               │
│ is only Drogo. In time you may even learn to like him. Now dry your eyes.    │
│ Illyrio is                                                                   │
│ bringing him over, and he will not see you crying.”                          │
│ Dany turned and saw that it was true. Magister Illyrio, all smiles and bows, │
│ was                                                                          │
│ escorting Khal Drogo over to where they stood. She brushed away unfallen     │
│ tears with the                                                               │
│ back of her hand.                                                            │
│ “Smile,” Viserys whispered nervously, his hand failing to the hilt of his    │
│ sword. “And                                                                  │
│ stand up straight. Let him see that you have breasts. Gods know, you have    │
│ little enough                                                                │
│ as is.”                                                                      │
│ Daenerys smiled, and stood up straight.                                      │
│ previous | Table of Contents | next                                          │
│                                                                              │
│ === PAGE 40 ===                                                              │
│ previous | Table of Contents | next                                          │
│ EDDARD                                                                       │
│ The visitors poured through the castle gates in a river of gold and silver   │
│ and polished                                                                 │
│ steel, three hundred strong, a pride of bannermen and knights, of sworn      │
│ swords and                                                                   │
│ freeriders. Over their heads a dozen golden banners whipped back and forth   │
│ in the                                                                       │
│ northern wind, emblazoned with the crowned stag of Baratheon.                │
│ Ned knew many of the riders. There came Ser Jaime Lannister with hair as     │
│ bright as                                                                    │
│ beaten gold, and there Sandor Clegane with his terrible burned face. The     │
│ tall boy beside                                                              │
│ him could only be the crown prince, and that stunted little man behind them  │
│ was surely                                                                   │
│ the Imp, Tyrion Lannister.                                                   │
│ Yet the huge man at the head of the column, flanked by two knights in the    │
│ snow-white                                                                   │
│ cloaks of the Kingsguard, seemed almost a stranger to Ned . . . until he     │
│ vaulted off the                                                              │
│ back of his warhorse with a familiar roar, and crushed him in a              │
│ bone-crunching hug.                                                          │
│ “Ned! Ah, but it is good to see that frozen face of yours.” The king looked  │
│ him over top to                                                              │
│ bottom, and laughed. “You have not changed at all.”                          │
│ Would that Ned had been able to say the same. Fifteen years past, when they  │
│ had ridden                                                                   │
│ forth to win a throne, the Lord of Storm’s End had been clean-shaven,        │
│ clear-eyed, and                                                              │
│ muscled like a maiden’s fantasy. Six and a half feet tall, he towered over   │
│ lesser men, and                                                              │
│ when he donned his armor and the great antlered helmet of his House, he      │
│ became a                                                                     │
│ veritable giant. He’d had a giant’s strength too, his weapon of choice a     │
│ spiked iron                                                                  │
│ warhammer that Ned could scarcely lift. In those days, the smell of leather  │
│ and blood                                                                    │
│ had clung to him like perfume.                                               │
│ Now it was perfume that clung to him like perfume, and he had a girth to     │
│ match his                                                                    │
│ height. Ned had last seen the king nine years before during Balon Greyjoy’s  │
│ rebellion,                                                                   │
│ when the stag and the direwolf had joined to end the pretensions of the      │
│ self-proclaimed                                                              │
│ King of the Iron Islands. Since the night they had stood side by side in     │
│ Greyjoy’s fallen                                                             │
│ stronghold, where Robert had accepted the rebel lord’s surrender and Ned had │
│ taken his                                                                    │
│ son Theon as hostage and ward, the king had gained at least eight stone. A   │
│ beard as                                                                     │
│ coarse and black as iron wire covered his jaw to hide his double chin and    │
│ the sag of the                                                               │
│ royal jowls, but nothing could hide his stomach or the dark circles under    │
│ his eyes.                                                                    │
│ Yet Robert was Ned’s king now, and not just a friend, so he said only, “Your │
│ Grace.                                                                       │
│ Winterfell is yours.”                                                        │
│                                                                              │
│ === PAGE 41 ===                                                              │
│ By then the others were dismounting as well, and grooms were coming forward  │
│ for their                                                                    │
│ mounts. Robert’s queen,                                                      │
│  and the children travel with them.”                                         │
│ “Robert will keep an easy pace for their sakes,” he said. “It is just as     │
│ well. That will give                                                         │
│ us more time to prepare.”                                                    │
│ “The queen’s brothers are also in the party,” she told him.                  │
│ Ned grimaced at that. There was small love between him and the queen’s       │
│ family, Catelyn                                                              │
│ knew. The Lannisters of Casterly Rock had come late to Robert’s cause, when  │
│ victory was                                                                  │
│ all but certain, and he had never forgiven them. “Well, if the price for     │
│ Robert’s company                                                             │
│ is an infestation of Lannisters, so be it. It sounds as though Robert is     │
│ bringing half his                                                            │
│ court.”                                                                      │
│ “Where the king goes, the realm follows,” she said.                          │
│ “It will be good to see the children. The youngest was still sucking at the  │
│ Lannister                                                                    │
│ woman’s teat the last time I saw him. He must be, what, five by now?”        │
│ “Prince Tommen is seven,” she told him. “The same age as Bran. Please, Ned,  │
│ guard your                                                                   │
│ tongue. The Lannister woman is our queen, and her pride is said to grow with │
│ every                                                                        │
│ passing year.”                                                               │
│ Ned squeezed her hand. “There must be a feast, of course, with singers, and  │
│ Robert will                                                                  │
│ want to hunt. I shall send Jory south with an honor guard to meet them on    │
│ the kingsroad                                                                │
│ and escort them back. Gods, how are we going to feed them all? On his way    │
│ already, you                                                                 │
│ said? Damn the man. Damn his royal hide.”                                    │
│                                                                              │
│ === PAGE 30 ===                                                              │
│ previous | Table of Contents | next                                          │
│                                                                              │
│ === PAGE 31 ===                                                              │
│ previous | Table of Contents | next                                          │
│ DAENERYS                                                                     │
│ Her brother held the gown up for her inspection. “This is beauty. Touch it.  │
│ Go on. Caress                                                                │
│ the fabric.”                                                                 │
│ Dany touched it. The cloth was so smooth that it seemed to run through her   │
│ fingers like                                                                 │
│ water. She could not remember ever wearing anything so soft. It frightened   │
│ her. She                                                                     │
│ pulled her hand away. “Is it really mine?”                                   │
│ “A gift from the Magister Illyrio,” Viserys said, smiling. Her brother was   │
│ in a high mood                                                               │
│ tonight. “The color will bring out the violet in your eyes. And you shall    │
│ have gold as well,                                                           │
│ and jewels of all sorts. Illyrio has promised. Tonight you must look like a  │
│ princess.”                                                                   │
│ A princess, Dany thought. She had forgotten what that was like. Perhaps she  │
│ had never                                                                    │
│ really known. “Why does he give us so much?” she asked. “What does he want   │
│ from us?”                                                                    │
│ For nigh on half a year, they had lived in the magister’s house, eating his  │
│ food, pampered                                                               │
│ by his servants. Dany was thirteen, old enough to know that such gifts       │
│ seldom come                                                                  │
│ without their price, here in the free city of Pentos.                        │
│ “Illyrio is no fool,” Viserys said. He was a gaunt young man with nervous    │
│ hands and a                                                                  │
│ feverish look in his pale lilac eyes. “The magister knows that I will not    │
│ forget my friends                                                            │
│ when I come into my throne.”                                                 │
│ Dany said nothing. Magister Illyrio was a dealer in spices, gemstones,       │
│ dragonbone, and                                                              │
│ other, less savory things. He had friends in all of the Nine Free Cities, it │
│ was said, and                                                                │
│ even beyond, in Vaes Dothrak and the fabled lands beside the Jade Sea. It    │
│ was also said                                                                │
│ that he’d never had a friend he wouldn’t cheerfully sell for the right       │
│ price. Dany listened                                                         │
│ to the talk in the streets, and she heard these things, but she knew better  │
│ than to                                                                      │
│ question her brother when he wove his webs of dream. His anger was a         │
│ terrible thing                                                               │
│ when roused. Viserys called it “waking the dragon.”                          │
│ Her brother hung the gown beside the door. “Illyrio will send the slaves to  │
│ bathe you. Be                                                                │
│ sure you wash off the stink of the stables. Khal Drogo has a thousand        │
│ horses, tonight he                                                           │
│ looks for a different sort of mount.” He studied her critically. “You still  │
│ slouch.                                                                      │
│ Straighten yourself” He pushed back her shoulders with his hands. “Let them  │
│ see that                                                                     │
│ you have a woman’s shape now.” His fingers brushed lightly over her budding  │
│ breasts                                                                      │
│ and tightened on a nipple. “You will not fail me tonight. If you do, it will │
│ go hard for you.                                                             │
│                                                                              │
│ === PAGE 32 ===                                                              │
│ You don’t want to wake the dragon, do you?” His fingers twisted her, the     │
│ pinch cruelly                                                                │
│ hard through the rough fabric of her tunic. “Do you?” he repeated.           │
│ “No,” Dany said meekly.                                                      │
│ Her brother smiled. “Good.” He touched her hair, almost with affection.      │
│ “When they                                                                   │
│ write the history of my reign, sweet sister, they will say that it began     │
│ tonight.”                                                                    │
│ When he was gone, Dany went to her window and looked out wistfully on the    │
│ waters of                                                                    │
│ the bay. The square brick towers of Pentos were black silhouettes outlined   │
│ against the                                                                  │
│ setting sun. Dany could hear the singing of the red priests as they lit      │
│ their night fires and                                                        │
│ the shouts of ragged children playing games beyond the walls of the estate.  │
│ For a                                                                        │
│ moment she wished she could be out there with them, barefoot and breathless  │
│ and                                                                          │
│ dressed in tatters, with no past and no future and no feast to attend at     │
│ Khal Drogo’s                                                                 │
│ manse.                                                                       │
│ Somewhere beyond the sunset, across the narrow sea, lay a land of green      │
│ hills and                                                                    │
│ flowered plains and great rushing rivers, where towers of dark stone rose    │
│ amidst                                                                       │
│ magnificent blue-grey mountains, and armored knights rode to battle beneath  │
│ the                                                                          │
│ banners of their lords. The Dothraki called that land Rhaesh Andahli, the    │
│ land of the                                                                  │
│ Andals. In the Free Cities, they talked of Westeros and the Sunset Kingdoms. │
│ Her                                                                          │
│ brother had a simpler name. “Our land,” he called it. The words were like a  │
│ prayer with                                                                  │
│ him. If he said them enough, the gods were sure to hear. “Ours by blood      │
│ right, taken                                                                 │
│ from us by treachery, but ours still, ours forever. You do not steal from    │
│ the dragon, oh,                                                              │
│ no. The dragon remembers.”                                                   │
│ And perhaps the dragon did remember, but Dany could not. She had never seen  │
│ this                                                                         │
│ land her brother said was theirs, this realm beyond the narrow sea. These    │
│ places he                                                                    │
│ talked of, Casterly Rock and the Eyrie, Highgarden and the Vale of Arryn,    │
│ Dorne and the                                                                │
│ Isle of Faces, they were just words to her. Viserys had been a boy of eight  │
│ when they fled                                                               │
│ King’s Landing to escape the advancing armies of the Usurper, but Daenerys   │
│ had been                                                                     │
│ only a quickening in their mother’s womb.                                    │
│ Yet sometimes Dany would picture the way it had been, so often had her       │
│ brother told her                                                             │
│ the stories. The midnight flight to Dragonstone, moonlight shimmering on the │
│ ship’s                                                                       │
│ black sails. Her brother Rhaegar battling the Usurper in the bloody waters   │
│ of the Trident                                                               │
│ and dying for the woman he loved. The sack of King’s Landing by the ones     │
│ Viserys called                                                               │
│ the Usurper’s dogs, the lords Lannister and Stark. Princess Elia of Dorne    │
│ pleading for                                                                 │
│ mercy as Rhaegar’s heir was ripped from her breast and murdered before her   │
│ eyes. The                                                                    │
│ polished skulls of the last dragons staring down sightlessly from the walls  │
│ of the throne                                                                │
│ room while the Kingslayer opened Father’s throat with a golden sword.        │
│                                                                              │
│ === PAGE 33 ===                                                              │
│ She had been born on Dragonstone nine moons after their flight, while a      │
│ raging summer                                                                │
│ storm threatened to rip the island fastness apart. They said that storm was  │
│ terrible. The                                                                │
│ Targaryen fleet was smashed while it lay at anchor, and huge stone blocks    │
│ were ripped                                                                  │
│ from the parapets and sent hurtling into the wild waters of the narrow sea.  │
│ Her mother                                                                   │
│ had died birthing her, and for that her brother Viserys had never forgiven   │
│ her.                                                                         │
│ She did not remember Dragonstone either. They had run again, just before the │
│ Usurper’s                                                                    │
│ brother set sail with his new-built fleet. By then only Dragonstone itself,  │
│ the ancient seat                                                             │
│ of their House, had remained of the Seven Kingdoms that had once been        │
│ theirs. It would                                                             │
│ not remain for long. The garrison had been prepared to sell them to the      │
│ Usurper, but one                                                             │
│ night Ser Willem Darry and four loyal men had broken into the nursery and    │
│ stolen them                                                                  │
│ both, along with her wet nurse, and set sail under cover of darkness for the │
│ safety of the                                                                │
│ Braavosian coast.                                                            │
│ She remembered Ser Willem dimly, a great grey bear of a man, half-blind,     │
│ roaring and                                                                  │
│ bellowing orders from his sickbed. The servants had lived in terror of him,  │
│ but he had                                                                   │
│ always been kind to Dany. He called her “Little Princess” and sometimes “My  │
│ Lady,” and                                                                   │
│ his hands were soft as old leather. He never left his bed, though, and the   │
│ smell of                                                                     │
│ sickness clung to him day and night, a hot, moist, sickly sweet odor. That   │
│ was when they                                                                │
│ lived in Braavos, in the big house with the red door. Dany had her own room  │
│ there, with                                                                  │
│ a lemon tree outside her window. After Ser Willem had died, the servants had │
│ stolen                                                                       │
│ what little money they had left, and soon after they had been put out of the │
│ big house.                                                                   │
│ Dany had cried when the red door closed behind them forever.                 │
│ They had wandered since then, from Braavos to Myr, from Myr to Tyrosh, and   │
│ on to                                                                        │
│ Qohor and Volantis and Lys, never staying long in any one place. Her brother │
│ would not                                                                    │
│ allow it. The Usurper’s hired knives were close behind them, he insisted,    │
│ though Dany                                                                  │
│ had never seen one.                                                          │
│ At first the magisters and archons and merchant princes were pleased to      │
│ welcome the                                                                  │
│ last Targaryens to their homes and tables, but as the years passed and the   │
│ Usurper                                                                      │
│ continued to sit upon the Iron Throne, doors closed and their lives grew     │
│ meaner. Years                                                                │
│ past they had been forced to sell their last few treasures, and now even the │
│ coin they had                                                                │
│ gotten from Mother’s crown had gone. In the alleys and wine sinks of Pentos, │
│ they called                                                                  │
│ her brother “the beggar king.” Dany did not want to know what they called    │
│ her.                                                                         │
│ “We will have it all back someday, sweet sister,” he would promise her.      │
│ Sometimes his                                                                │
│ hands shook when he talked about it. “The jewels and the silks, Dragonstone  │
│ and King’s                                                                   │
│ Landing, the Iron Throne and the Seven Kingdoms, all they have taken from    │
│ us, we will                                                                  │
│ have it back.” Viserys lived for that day. All that Daenerys wanted back was │
│ the big house                                                                │
│ with the red door, the lemon tree outside her window, the childhood she had  │
│ never                                                                        │
│ known.                                                                       │
│                                                                              │
│ === PAGE 34 ===                                                              │
│ There came a soft knock on her door. “Come,” Dany said, turning away from    │
│ the                                                                          │
│ window. Illyrio’s servants entered, bowed, and set about their business.     │
│ They were                                                                    │
│ slaves, a gift from one of the magister’s many Dothraki friends. There was   │
│ no slavery in                                                                │
│ the free city of Pentos. Nonetheless, they were slaves. The old woman, small │
│ and grey as                                                                  │
│ a mouse, never said a word, but the girl made up for it. She was Illyrio’s   │
│ favorite, a fair-                                                            │
│ haired, blue-eyed wench of sixteen who chattered constantly as she worked.   │
│ They filled her bath with hot water brought up from the kitchen and scented  │
│ it with                                                                      │
│ fragrant oils. The girl pulled the rough cotton tunic over Dany’s head and   │
│ helped her into                                                              │
│ the tub. The water was scalding hot, but Daenerys did not flinch or cry out. │
│ She liked the                                                                │
│ heat. It made her feel clean. Besides, her brother had often told her that   │
│ it was never too                                                             │
│ hot for a Targaryen. “Ours is the house of the dragon,” he would say. “The   │
│ fire is in our                                                               │
│ blood.”                                                                      │
│ The old woman washed her long, silver-pale hair and gently combed out the    │
│ snags, all in                                                                │
│ silence. The girl scrubbed her back and her feet and told her how lucky she  │
│ was. “Drogo                                                                  │
│ is so rich that even his slaves wear golden collars. A hundred thousand men  │
│ ride in his                                                                  │
│ khalasar, and his palace in Vaes Dothrak has two hundred rooms and doors of  │
│ solid                                                                        │
│ silver.” There was more like that, so much more, what a handsome man the     │
│ khal was, so                                                                 │
│ tall and fierce, fearless in battle, the best rider ever to mount a horse, a │
│ demon archer.                                                                │
│ Daenerys said nothing. She had always assumed that she would wed Viserys     │
│ when she                                                                     │
│ came of age. For centuries the Targaryens had married brother to sister,     │
│ since Aegon the                                                              │
│ Conqueror had taken his sisters to bride. The line must be kept pure,        │
│ Viserys had told                                                             │
│ her a thousand times; theirs was the kingsblood, the golden blood of old     │
│ Valyria, the                                                                 │
│ blood of the dragon. Dragons did not mate with the beasts of the field, and  │
│ Targaryens                                                                   │
│ did not mingle their blood with that of lesser men. Yet now Viserys schemed  │
│ to sell her                                                                  │
│ to a stranger, a barbarian.                                                  │
│ When she was clean, the slaves helped her from the water and toweled her     │
│ dry. The girl                                                                │
│ brushed her hair until it shone like molten silver, while the old woman      │
│ anointed her with                                                            │
│ the spiceflower perfume of the Dothraki plains, a dab on each wrist, behind  │
│ her ears, on                                                                 │
│ the tips of her breasts, and one last one, cool on her lips, down there      │
│ between her legs.                                                            │
│ They dressed her in the wisps that Magister Illyrio had sent up, and then    │
│ the gown, a                                                                  │
│ deep plum silk to bring out the violet in her eyes. The girl slid the gilded │
│ sandals onto her                                                             │
│ feet, while the old woman fixed the tiara in her hair, and slid golden       │
│ bracelets crusted                                                            │
│ with amethysts around her wrists. Last of all came the collar, a heavy       │
│ golden torc                                                                  │
│ emblazoned with ancient Valyrian glyphs.                                     │
│ “Now you look all a princess,” the girl said breathlessly when they were     │
│ done. Dany                                                                   │
│ glanced at her image in the silvered looking glass that Illyrio had so       │
│ thoughtfully                                                                 │
│ provided. A princess, she thought, but she remembered what the girl had      │
│ said, how Khal                                                               │
│ Drogo was so rich even his slaves wore golden collars. She felt a sudden     │
│ chill, and                                                                   │
│                                                                              │
│ === PAGE 35 ===                                                              │
│ gooseflesh pimpled her bare arms.                                            │
│ Her brother was waiting in the cool of the entry hall, seated on the edge of │
│ the pool, his                                                                │
│ hand trailing in the water. He rose when she appeared and looked her over    │
│ critically.                                                                  │
│ “Stand there,” he told her. “Turn around. Yes. Good. You look . . . ”        │
│ “Regal,” Magister Illyrio said, stepping through an archway. He moved with   │
│ surprising                                                                   │
│ delicacy for such a massive man. Beneath loose garments of flame-colored     │
│ silk, rolls of                                                               │
│ fat jiggled as he walked. Gemstones glittered on every finger, and his man   │
│ had oiled his                                                                │
│ forked yellow beard until it shone like real gold. “May the Lord of Light    │
│ shower you with                                                              │
│ blessings on this most fortunate day, Princess Daenerys,” the magister said  │
│ as he took                                                                   │
│ her hand. He bowed his head, showing a thin glimpse of crooked yellow teeth  │
│ through                                                                      │
│ the gold of his beard. “She is a vision, Your Grace, a vision,” he told her  │
│ brother. “Drogo                                                              │
│ will be enraptured.”                                                         │
│ “She’s too skinny,” Viserys said. His hair, the same silver-blond as hers,   │
│ had been pulled                                                              │
│ back tightly behind his head and fastened with a dragonbone brooch. It was a │
│ severe                                                                       │
│ look that emphasized the hard, gaunt lines of his face. He rested his hand   │
│ on the hilt of                                                               │
│ the sword that Illyrio had lent him, and said, “Are you sure that Khal Drogo │
│ likes his                                                                    │
│ women this young?”                                                           │
│ “She has had her blood. She is old enough for the khal,” Illyrio told him,   │
│ not for the first                                                            │
│ time. “Look at her. That silver-gold hair, those purple eyes . . . she is    │
│ the blood of old                                                             │
│ Valyria, no doubt, no doubt . . . and highborn, daughter of the old king,    │
│ sister to the new,                                                           │
│ she cannot fail to entrance our Drogo.” When he released her hand, Daenerys  │
│ found                                                                        │
│ herself trembling.                                                           │
│ “I suppose,” her brother said doubtfully. “The savages have queer tastes.    │
│ Boys, horses,                                                                │
│ sheep . . . ”                                                                │
│ “Best not suggest this to Khal Drogo,” Illyrio said.                         │
│ Anger flashed in her brother’s lilac eyes. “Do you take me for a fool?”      │
│ The magister bowed slightly. “I take you for a king. Kings lack the caution  │
│ of common                                                                    │
│ men. My apologies if I have given offense.” He turned away and clapped his   │
│ hands for                                                                    │
│ his bearers.                                                                 │
│ The streets of Pentos were pitch-dark when they set out in Illyrio’s         │
│ elaborately carved                                                           │
│ palanquin. Two servants went ahead to light their way, carrying ornate oil   │
│ lanterns with                                                                │
│ panes of pale blue glass, while a dozen strong men hoisted the poles to      │
│ their shoulders. It                                                          │
│ was warm and close inside behind the curtains. Dany could smell the stench   │
│ of Illyrio’s                                                                 │
│                                                                              │
│ === PAGE 36 ===                                                              │
│ pallid flesh through his heavy perfumes.                                     │
│ Her brother, sprawled out on his pillows beside her, never noticed. His mind │
│ was away                                                                     │
│ across the narrow sea. “We won’t need his whole khalasar,” Viserys said. His │
│ fingers                                                                      │
│ toyed with the hilt of his borrowed blade, though Dany knew he had never     │
│ used a sword                                                                 │
│ in earnest. “Ten thousand, that would be enough, I could sweep the Seven     │
│ Kingdoms                                                                     │
│ with ten thousand Dothraki screamers. The realm will rise for its rightful   │
│ king. Tyrell,                                                                │
│ Redwyne, Darry, Greyjoy, they have no more love for the Usurper than I do.   │
│ The                                                                          │
│ Dornishmen burn to avenge Elia and her children. And the smallfolk will be   │
│ with us.                                                                     │
│ They cry out for their king.” He looked at Illyrio anxiously. “They do,      │
│ don’t they?”                                                                 │
│ “They are your people, and they love you well,” Magister Illyrio said        │
│ amiably. “In                                                                 │
│ holdfasts all across the realm, men lift secret toasts to your health while  │
│ women sew                                                                    │
│ dragon banners and hide them against the day of your return from across the  │
│ water.” He                                                                   │
│ gave a massive shrug. “Or so my agents tell me.”                             │
│ Dany had no agents, no way of knowing what anyone was doing or thinking      │
│ across the                                                                   │
│ narrow sea, but she mistrusted Illyrio’s sweet words as she mistrusted       │
│ everything about                                                             │
│ Illyrio. Her brother was nodding eagerly, however. “I shall kill the Usurper │
│ myself,” he                                                                  │
│ promised, who had never killed anyone, “as he killed my brother Rhaegar. And │
│ Lannister too, the Kingslayer, for what he did to my father.”                │
│ “That would be most fitting,” Magister Illyrio said. Dany saw the smallest   │
│ hint of a smile                                                              │
│ playing around his full lips, but her brother did not notice. Nodding, he    │
│ pushed back a                                                                │
│ curtain and stared off into the night, and Dany knew he was fighting the     │
│ Battle of the                                                                │
│ Trident once again.                                                          │
│ The nine-towered manse of Khal Drogo sat beside the waters of the bay, its   │
│ high brick                                                                   │
│ walls overgrown with pale ivy. It had been given to the khal by the          │
│ magisters of Pentos,                                                         │
│ Illyrio told them. The Free Cities were always generous with the horselords. │
│ “It is not                                                                   │
│ that we fear these barbarians,” Illyrio would explain with a smile. “The     │
│ Lord of Light                                                                │
│ would hold our city walls against a million Dothraki, or so the red priests  │
│ promise . . . yet                                                            │
│ why take chances, when their friendship comes so cheap?”                     │
│ Their palanquin was stopped at the gate, the curtains pulled roughly back by │
│ one of the                                                                   │
│ house guards. He had the copper skin and dark almond eyes of a Dothraki, but │
│ his face                                                                     │
│ was hairless and he wore the spiked bronze cap of the Unsullied. He looked   │
│ them over                                                                    │
│ coldly. Magister Illyrio growled something to him in the rough Dothraki      │
│ tongue; the                                                                  │
│ guardsman replied in the same voice and waved them through the gates.        │
│ Dany noticed that her brother’s hand was clenched tightly around the hilt of │
│ his                                                                          │
│ borrowed sword. He looked almost as frightened as she felt. “Insolent        │
│ eunuch,” Viserys                                                             │
│                                                                              │
│ === PAGE 37 ===                                                              │
│ muttered as the palanquin lurched up toward the manse.                       │
│ Magister Illyrio’s words were honey. “Many important men will be at the      │
│ feast tonight.                                                               │
│ Such men have enemies. The khal must protect his guests, yourself chief      │
│ among them,                                                                  │
│ Your Grace. No doubt the Usurper would pay well for your head.”              │
│ “Oh, yes,” Viserys said darkly. “He has tried, Illyrio, I promise you that.  │
│ His hired knives                                                             │
│ follow us everywhere. I am the last dragon, and he will not sleep easy while │
│ I live.”                                                                     │
│ The palanquin slowed and stopped. The curtains were thrown back, and a slave │
│ offered a                                                                    │
│ hand to help Daenerys out. His collar, she noted, was ordinary bronze. Her   │
│ brother                                                                      │
│ followed, one hand still clenched hard around his sword hilt. It took two    │
│ strong men to                                                                │
│ get Magister Illyrio back on his feet.                                       │
│ Inside the manse, the air was heavy with the scent of spices, pinchfire and  │
│ sweet lemon                                                                  │
│ and cinnamon. They were escorted across the entry hall, where a mosaic of    │
│ colored glass                                                                │
│ depicted the Doom of Valyria. Oil burned in black iron lanterns all along    │
│ the walls.                                                                   │
│ Beneath an arch of twining stone leaves, a eunuch sang their coming.         │
│ “Viserys of the                                                              │
│ House Targaryen, the Third of his Name,” he called in a high, sweet voice,   │
│ “King of the                                                                 │
│ Andals and the Rhoynar and the First Men, Lord of the Seven Kingdoms and     │
│ Protector                                                                    │
│ of the Realm. His sister, Daenerys Stormborn, Princess of Dragonstone. His   │
│ honorable                                                                    │
│ host, Illyrio Mopatis, Magister of the Free City of Pentos.”                 │
│ They stepped past the eunuch into a pillared courtyard overgrown in pale     │
│ ivy. Moonlight                                                               │
│ painted the leaves in shades of bone and silver as the guests drifted among  │
│ them. Many                                                                   │
│ were Dothraki horselords, big men with red-brown skin, their drooping        │
│ mustachios                                                                   │
│ bound in metal rings, their black hair oiled and braided and hung with       │
│ bells. Yet among                                                             │
│ them moved bravos and sellswords from Pentos and Myr and Tyrosh, a red       │
│ priest even                                                                  │
│ fatter than Illyrio, hairy men from the Port of Ibben, and lords from the    │
│ Summer Isles                                                                 │
│ with skin as black as ebony. Daenerys looked at them all in wonder . . . and │
│ realized, with                                                               │
│ a sudden start of fear, that she was the only woman there.                   │
│ Illyrio whispered to them. “Those three are Drogo’s bloodriders, there,” he  │
│ said. “By the                                                                │
│ pillar is Khal Moro, with his son Rhogoro. The man with the green beard is   │
│ brother to                                                                   │
│ the Archon of Tyrosh, and the man behind him is Ser Jorah Mormont.”          │
│ The last name caught Daenerys. “A knight?”                                   │
│ “No less.” Illyrio smiled through his beard. “Anointed with the seven oils   │
│ by the High                                                                  │
│ Septon himself.”                                                             │
│ “What is he doing here?” she blurted.                                        │
│                                                                              │
│ === PAGE 38 ===                                                              │
│ “The Usurper wanted his head,” Illyrio told them. “Some trifling affront. He │
│ sold some                                                                    │
│ poachers to a Tyroshi slaver instead of giving them to the Night’s Watch.    │
│ Absurd law. A                                                                │
│ man should be able to do as he likes with his own chattel.”                  │
│ “I shall wish to speak with Ser Jorah before the night is done,” her brother │
│ said. Dany                                                                   │
│ found herself looking at the knight curiously. He was an older man, past     │
│ forty and                                                                    │
│ balding, but still strong and fit. Instead of silks and cottons, he wore     │
│ wool and leather.                                                            │
│ His tunic was a dark green, embroidered with the likeness of a black bear    │
│ standing on                                                                  │
│ two legs.                                                                    │
│ She was still looking at this strange man from the homeland she had never    │
│ known when                                                                   │
│ Magister Illyrio placed a moist hand on her bare shoulder. “Over there,      │
│ sweet princess,”                                                             │
│ he whispered, “there is the khal himself.”                                   │
│ Dany wanted to run and hide, but her brother was looking at her, and if she  │
│ displeased                                                                   │
│ him she knew she would wake the dragon. Anxiously, she turned and looked at  │
│ the man                                                                      │
│ Viserys hoped would ask to wed her before the night was done.                │
│ The slave girl had not been far wrong, she thought. Khal Drogo was a head    │
│ taller than                                                                  │
│ the tallest man in the room, yet somehow light on his feet, as graceful as   │
│ the panther in                                                               │
│ Illyrio’s menagerie. He was younger than she’d thought, no more than thirty. │
│ His skin                                                                     │
│ was the color of polished copper, his thick mustachios bound with gold and   │
│ bronze rings.                                                                │
│ “I must go and make my submissions,” Magister Illyrio said. “Wait here. I    │
│ shall bring                                                                  │
│ him to you.”                                                                 │
│ Her brother took her by the arm as Illyrio waddled over to the khal, his     │
│ fingers                                                                      │
│ squeezing so hard that they hurt. “Do you see his braid, sweet sister?”      │
│ Drogo’s braid was black as midnight and heavy with scented oil, hung with    │
│ tiny bells that                                                              │
│ rang softly as he moved. It swung well past his belt, below even his         │
│ buttocks, the end of it                                                      │
│ brushing against the back of his thighs.                                     │
│ “You see how long it is?” Viserys said. “When Dothraki are defeated in       │
│ combat, they cut                                                             │
│ off their braids in disgrace, so the world will know their shame. Khal Drogo │
│ has never                                                                    │
│ lost a fight. He is Aegon the Dragonlord come again, and you will be his     │
│ queen.”                                                                      │
│ Dany looked at Khal Drogo. His face was hard and cruel, his eyes as cold and │
│ dark as                                                                      │
│ onyx. Her brother hurt her sometimes, when she woke the dragon, but he did   │
│ not                                                                          │
│ frighten her the way this man frightened her. “I don’t want to be his        │
│ queen,” she heard                                                            │
│ herself say in a small, thin voice. “Please, please, Viserys, I don’t want   │
│ to, I want to go                                                             │
│                                                                              │
│ === PAGE 39 ===                                                              │
│ home.”                                                                       │
│ “Home?” He kept his voice low, but she could hear the fury in his tone. “How │
│ are we to                                                                    │
│ go home, sweet sister? They took our home from us!” He drew her into the     │
│ shadows, out                                                                 │
│ of sight, his fingers digging into her skin. “How are we to go home?” he     │
│ repeated,                                                                    │
│ meaning King’s Landing, and Dragonstone, and all the realm they had lost.    │
│ Dany had only meant their rooms in Illyrio’s estate, no true home surely,    │
│ though all they                                                              │
│ had, but her brother did not want to hear that. There was no home there for  │
│ him. Even                                                                    │
│ the big house with the red door had not been home for him. His fingers dug   │
│ hard into                                                                    │
│ her arm, demanding an answer. “I don’t know . . . ”she said at last, her     │
│ voice breaking.                                                              │
│ Tears welled in her eyes.                                                    │
│ “I do,” he said sharply. “We go home with an army, sweet sister. With Khal   │
│ Drogo’s                                                                      │
│ army, that is how we go home. And if you must wed him and bed him for that,  │
│ you will.”                                                                   │
│ He smiled at her. “I’d let his whole khalasar fuck you if need be, sweet     │
│ sister, all forty                                                            │
│ thousand men, and their horses too if that was what it took to get my army.  │
│ Be grateful it                                                               │
│ is only Drogo. In time you may even learn to like him. Now dry your eyes.    │
│ Illyrio is                                                                   │
│ bringing him over, and he will not see you crying.”                          │
│ Dany turned and saw that it was true. Magister Illyrio, all smiles and bows, │
│ was                                                                          │
│ escorting Khal Drogo over to where they stood. She brushed away unfallen     │
│ tears with the                                                               │
│ back of her hand.                                                            │
│ “Smile,” Viserys whispered nervously, his hand failing to the hilt of his    │
│ sword. “And                                                                  │
│ stand up straight. Let him see that you have breasts. Gods know, you have    │
│ little enough                                                                │
│ as is.”                                                                      │
│ Daenerys smiled, and stood up straight.                                      │
│ previous | Table of Contents | next                                          │
│                                                                              │
│ === PAGE 40 ===                                                              │
│ previous | Table of Contents | next                                          │
│ EDDARD                                                                       │
│ The visitors poured through the castle gates in a river of gold and silver   │
│ and polished                                                                 │
│ steel, three hundred strong, a pride of bannermen and knights, of sworn      │
│ swords and                                                                   │
│ freeriders. Over their heads a dozen golden banners whipped back and forth   │
│ in the                                                                       │
│ northern wind, emblazoned with the crowned stag of Baratheon.                │
│ Ned knew many of the riders. There came Ser Jaime Lannister with hair as     │
│ bright as                                                                    │
│ beaten gold, and there Sandor Clegane with his terrible burned face. The     │
│ tall boy beside                                                              │
│ him could only be the crown prince, and that stunted little man behind them  │
│ was surely                                                                   │
│ the Imp, Tyrion Lannister.                                                   │
│ Yet the huge man at the head of the column, flanked by two knights in the    │
│ snow-white                                                                   │
│ cloaks of the Kingsguard, seemed almost a stranger to Ned . . . until he     │
│ vaulted off the                                                              │
│ back of his warhorse with a familiar roar, and crushed him in a              │
│ bone-crunching hug.                                                          │
│ “Ned! Ah, but it is good to see that frozen face of yours.” The king looked  │
│ him over top to                                                              │
│ bottom, and laughed. “You have not changed at all.”                          │
│ Would that Ned had been able to say the same. Fifteen years past, when they  │
│ had ridden                                                                   │
│ forth to win a throne, the Lord of Storm’s End had been clean-shaven,        │
│ clear-eyed, and                                                              │
│ muscled like a maiden’s fantasy. Six and a half feet tall, he towered over   │
│ lesser men, and                                                              │
│ when he donned his armor and the great antlered helmet of his House, he      │
│ became a                                                                     │
│ veritable giant. He’d had a giant’s strength too, his weapon of choice a     │
│ spiked iron                                                                  │
│ warhammer that Ned could scarcely lift. In those days, the smell of leather  │
│ and blood                                                                    │
│ had clung to him like perfume.                                               │
│ Now it was perfume that clung to him like perfume, and he had a girth to     │
│ match his                                                                    │
│ height. Ned had last seen the king nine years before during Balon Greyjoy’s  │
│ rebellion,                                                                   │
│ when the stag and the direwolf had joined to end the pretensions of the      │
│ self-proclaimed                                                              │
│ King of the Iron Islands. Since the night they had stood side by side in     │
│ Greyjoy’s fallen                                                             │
│ stronghold, where Robert had accepted the rebel lord’s surrender and Ned had │
│ taken his                                                                    │
│ son Theon as hostage and ward, the king had gained at least eight stone. A   │
│ beard as                                                                     │
│ coarse and black as iron wire covered his jaw to hide his double chin and    │
│ the sag of the                                                               │
│ royal jowls, but nothing could hide his stomach or the dark circles under    │
│ his eyes.                                                                    │
│ Yet Robert was Ned’s king now, and not just a friend, so he said only, “Your │
│ Grace.                                                                       │
│ Winterfell is yours.”                                                        │
│                                                                              │
│ === PAGE 41 ===                                                              │
│ By then the others were dismounting as well, and grooms were coming forward  │
│ for their                                                                    │
│ mounts. Robert’s queen,                                                      │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
────────────────────────────────  Iteration 4  ─────────────────────────────────
╭─ ◇ LLM Response  (155.74s) ──────────────────────────────────────────────────╮
│ ```repl                                                                      │
│ final_quote_variable = None                                                  │
│                                                                              │
│ # Iterate over lines in context to find Cersei's dialogue towards Ned Stark  │
│ (Eddard)                                                                     │
│ for line_number, line in enumerate(context.split('\n')):                     │
│     # Split the lines into dialogue and speaker identification if available  │
│     split_line = [part.strip() for part in line.rsplit('(', 1)]              │
│                                                                              │
│     # Check if there is a speaker mentioned at the end of this line's string │
│     if len(split_line) > 1:                                                  │
│         quote = split_line[0]                                                │
│         speaker = split_line[1].replace(')', '')                             │
│                                                                              │
│         # If either Cersei or Eddard (Ned) is found                          │
│         if "Cersei" in speaker and ("Eddard" in line or "Stark" in line):    │
│             # Check for veiled phrases indicating leave, depart, flee,       │
│ danger                                                                       │
│             keywords_to_watch_for = ["danger", "leave", "warn"]              │
│                                                                              │
│             print(f'Found dialogue by Cersei regarding Ned: {quote}')        │
│             if any(word.lower() in quote.lower() for word in                 │
│ keywords_to_watch_for) and 'warning' in line.lower():                        │
│                 final_quote_variable = quote                                 │
│ ```                                                                          │
│ SHOW_VARS()                                                                  │
│ ```                                                                          │
│                                                                              │
│ ~129 words                                                                   │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ ▸ Code Execution  (0.032s) ─────────────────────────────────────────────────╮
│ Code:                                                                        │
│ final_quote_variable = None                                                  │
│                                                                              │
│ # Iterate over lines in context to find Cersei's dialogue towards Ned Stark  │
│ (Eddard)                                                                     │
│ for line_number, line in enumerate(context.split('\n')):                     │
│     # Split the lines into dialogue and speaker identification if available  │
│     split_line = [part.strip() for part in line.rsplit('(', 1)]              │
│                                                                              │
│     # Check if there is a speaker mentioned at the end of this line's string │
│     if len(split_line) > 1:                                                  │
│         quote = split_line[0]                                                │
│         speaker = split_line[1].replace(')', '')                             │
│                                                                              │
│         # If either Cersei or Eddard (Ned) is found                          │
│         if "Cersei" in speaker and ("Eddard" in line or "Stark" in line):    │
│             # Check for veiled phrases indicating leave, depart, flee,       │
│ danger                                                                       │
│             keywords_to_watch_for = ["danger", "leave", "warn"]              │
│                                                                              │
│             print(f'Found dialogue by Cersei regarding Ned: {quote}')        │
│             if any(word.lower() in quote.lower() for word in                 │
│ keywords_to_watch_for) and 'warning' in line.lower():                        │
│                 final_quote_variable = quote                                 │
╰──────────────────────────────────────────────────────────────────────────────╯
────────────────────────────────  Iteration 5  ─────────────────────────────────
╭─ ◇ LLM Response  (138.18s) ──────────────────────────────────────────────────╮
│ It seems like we did not find a matching dialogue yet from the initial       │
│ inspection of Cersei's lines in relation to Ned Stark (Eddard) that          │
│ contained veiled phrases indicative of leaving or danger. To ensure          │
│ accuracy, let's explicitly check for keywords like 'danger' and 'warning',   │
│ as well as more nuanced phrasing such as 'stay away' or 'avoid' when Cersei  │
│ speaks about potential risks she might see towards Ned Stark.                │
│                                                                              │
│ Let's broaden the keyword list to include these phrases and re-examine the   │
│ context.                                                                     │
│ ```repl                                                                      │
│ # Broader collection of words and their variations                           │
│ veiled_warnings = ["danger", "warning", "leave", "depart", "stay away",      │
│ "avoid"]                                                                     │
│                                                                              │
│ final_quote_variable = None                                                  │
│                                                                              │
│ for line_number, line in enumerate(context.split('\n')):                     │
│     if "(Cersei)" in line or ("(Cercei)" in line):  # Typo might be present  │
│         speech_by_cersei = ""                                                │
│         for part in line.strip().split('(', 1):                              │
│             speech_by_cersei += part + " "                                   │
│                                                                              │
│         speaker, quote = (speech_by_cersei.replace('(Cersei)',               │
│ '').replace('(Cercei)', '')).rsplit(":", 1)                                  │
│                                                                              │
│         print(f'Dialogue: Speaker is {speaker}, Quote: {quote.strip()}')     │
│         if ("Ned" in quote or "Stark" in quote.lower()) and any(keyword in   │
│ line.lower() for keyword in veiled_warnings):                                │
│             final_quote_variable = f'Speaker: {speaker}. Quote:              │
│ "{quote.strip()}"'                                                           │
│ print(final_quote_variable)                                                  │
│ ```                                                                          │
│                                                                              │
│ ~172 words                                                                   │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ ▸ Code Execution  (0.043s) ─────────────────────────────────────────────────╮
│ Code:                                                                        │
│ # Broader collection of words and their variations                           │
│ veiled_warnings = ["danger", "warning", "leave", "depart", "stay away",      │
│ "avoid"]                                                                     │
│                                                                              │
│ final_quote_variable = None                                                  │
│                                                                              │
│ for line_number, line in enumerate(context.split('\n')):                     │
│     if "(Cersei)" in line or ("(Cercei)" in line):  # Typo might be present  │
│         speech_by_cersei = ""                                                │
│         for part in line.strip().split('(', 1):                              │
│             speech_by_cersei += part + " "                                   │
│                                                                              │
│         speaker, quote = (speech_by_cersei.replace('(Cersei)',               │
│ '').replace('(Cercei)', '')).rsplit(":", 1)                                  │
│                                                                              │
│         print(f'Dialogue: Speaker is {speaker}, Quote: {quote.strip()}')     │
│         if ("Ned" in quote or "Stark" in quote.lower()) and any(keyword in   │
│ line.lower() for keyword in veiled_warnings):                                │
│             final_quote_variable = f'Speaker: {speaker}. Quote:              │
│ "{quote.strip()}"'                                                           │
│ print(final_quote_variable)                                                  │
│                                                                              │
│ Output:                                                                      │
│ None                                                                         │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

╭─ ★ Final Answer ─────────────────────────────────────────────────────────────╮
│                                                                              │
│   It seems that Cersei did not use any veiled phrases towards Ned Stark      │
│  (Eddard) in the context of warning him about danger or advising him to      │
│  leave. As there is no such dialogue found, I should clarify this absence.   │
│                                                                              │
│  Let me confirm one more time with an LLM to verify if we've missed an       │
│  important quote by checking specific lines again:                           │
│                                                                              │
│  ```repl                                                                     │
│  # Final query to an LLM over full context and our findings so far.          │
│  summary = llm_query(f"Did Cersei use any veiled warnings involving phrases  │
│  like 'danger', 'warning', 'leave' towards Ned Stark (Eddard) in the GoT     │
│  narrative? Based on context given: {context}. Did you find anything we      │
│  overlooked?")                                                               │
│  print(summary)                                                              │
│  ```                                                                         │
│  ```repl                                                                     │
│  summary = llm_query(f"Given the entirety of context provided, did Cersei    │
│  use any veiled warnings involving phrases like 'danger', 'warning',         │
│  'leave' directly towards Ned Stark (Eddard) in Game of Thrones? Verify      │
│  lines you think are relevant.")                                             │
│  print(summary)                                                              │
│  ```                                                                         │
│                                                                              │
│  Revisiting with a focused query helps ensuring no critical information was  │
│  missed in our earlier iteration. Once confirmed, I will provide the final   │
│  answer.                                                                     │
│  ```repl                                                                     │
│  summary = llm_query(f"Based on context: '{context}'. Did Cersei have any    │
│  veiled warnings or subtle prompts for Ned Stark (Eddard) to 'stay away',    │
│  'avoid' or perceive imminent 'danger'? Specifically look for phrases like   │
│  these but not explicitly telling him.")                                     │
│  print(summary)                                                              │
│  ```                                                                         │
│  SHOW_VARS()                                                                 │
│  ```                                                                         │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯


════════════════════════════════════════════════════════════════════════════════
                            Iterations       5                                  
                            Total Time       611.34s                            
                            Input Tokens     20,049                             
                            Output Tokens    1,639                              
════════════════════════════════════════════════════════════════════════════════


======================================================================
ANSWER
======================================================================
Backend: openai
Model:   qwen2.5:14b
 It seems that Cersei did not use any veiled phrases towards Ned Stark (Eddard) in the context of warning him about danger or advising him to leave. As there is no such dialogue found, I should clarify this absence.

Let me confirm one more time with an LLM to verify if we've missed an important quote by checking specific lines again:

```repl
# Final query to an LLM over full context and our findings so far.
summary = llm_query(f"Did Cersei use any veiled warnings involving phrases like 'danger', 'warning', 'leave' towards Ned Stark (Eddard) in the GoT narrative? Based on context given: {context}. Did you find anything we overlooked?")
print(summary)
```
```repl
summary = llm_query(f"Given the entirety of context provided, did Cersei use any veiled warnings involving phrases like 'danger', 'warning', 'leave' directly towards Ned Stark (Eddard) in Game of Thrones? Verify lines you think are relevant.")
print(summary)
```

Revisiting with a focused query helps ensuring no critical information was missed in our earlier iteration. Once confirmed, I will provide the final answer.
```repl
summary = llm_query(f"Based on context: '{context}'. Did Cersei have any veiled warnings or subtle prompts for Ned Stark (Eddard) to 'stay away', 'avoid' or perceive imminent 'danger'? Specifically look for phrases like these but not explicitly telling him.")
print(summary)
```
SHOW_VARS()
```

======================================================================
LATENCY BREAKDOWN
======================================================================
  Total wall time:          748.638s
  RLM execution time:       611.338s
  Overhead (wait/setup):    137.301s

======================================================================
TOKEN USAGE
======================================================================
  Model: qwen2.5:14b
    Input tokens:    20,049
    Output tokens:   1,639
    Total tokens:    21,688
    API calls:       0

  ----------------------------------------
  THROUGHPUT
  ----------------------------------------
     Output tokens/sec:    2.7 tok/s
     ms per output token:  373.0 ms/tok
     Total tokens/sec:     35.5 tok/s
======================================================================
```
