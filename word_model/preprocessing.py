import string

SEQUENCE_LENGTH = 46

def token_generate(textdata):
    textdata = textdata.lower()
    word_list = textdata.split(" ")
    
    table = str.maketrans('', '', string.punctuation)
    word_list = [w.translate(table) for w in word_list]
    word_list = [word for word in word_list if word.isalpha()]
    return word_list

def sequence_from_tokens(tokens, exparamental = False):
    sequences = []
    for i in range(SEQUENCE_LENGTH, len(tokens)):
        #ignores sequece if the expected output is an "unknown variable"
        if tokens[i-1] != 0 or not exparamental:
            sequences.append([])
            for j in tokens[i-SEQUENCE_LENGTH:i]:  
                sequences[-1].append(j)

    return sequences

def preprocessing(data, exparamental = False):
    #cleaning data and generating sequences
    tokens = token_generate(data)
    #tokenizing words
    existing_words = sorted(set(tokens))
    enumerated_dict = dict((w,i+1) for i, w in enumerate(existing_words)) #skips 0 index
    
    #teaches the model to account for unknown words, eliminates the last 400 words from the
    #vocabulary and sets them to an arbritrary value
    if exparamental==True:
        eliminate = len(enumerated_dict)-400
        delete = list (key for key in enumerated_dict if enumerated_dict[key]>eliminate)
        for key in delete:
            del enumerated_dict[key]
        # for key in enumerated_dict.keys():
        #     if enumerated_dict[key]>eliminate:
        #         del enumerated_dict[key]

    enumerated_tokens = []
    for i in tokens:
        enumerated_tokens.append(enumerated_dict[i] if i in enumerated_dict else 0)

    sequence = sequence_from_tokens(enumerated_tokens, exparamental)

    return sequence, enumerated_dict


test = '''On an exceptionally hot evening early in July a young man came out of the garret in which he lodged in. Place and walked slowly, as though in hesitation, towards K. bridge.

He had successfully avoided meeting his landlady on the staircase. His garret was under the roof of a high, house and was more like a cupboard than a room. The landlady who provided him with garret, dinners, and attendance, lived on the floor below, and every time he went out he was obliged to pass her kitchen, the door of which invariably stood open. And each time he passed, the young man had a sick, frightened feeling, which made him scowl and feel ashamed. He was hopelessly in debt to his landlady, and was afraid of meeting her.

This was not because he was cowardly and abject, quite the contrary; but for some time past he had been in an overstrained irritable condition, verging on hypochondria. He had become so completely absorbed in himself, and isolated from his fellows that he dreaded meeting, not only his landlady, but anyone at all. He was crushed by poverty, but the anxieties of his position had of late ceased to weigh upon him. He had given up attending to matters of practical importance; he had lost all desire to do so. Nothing that any landlady could do had a real terror for him. But to be stopped on the stairs, to be forced to listen to her trivial, irrelevant gossip, to pestering demands for payment, threats and complaints, and to rack his brains for excuses, to prevaricate, to lie�no, rather than that, he would creep down the stairs like a cat and slip out unseen.

This evening, however, on coming out into the street, he became acutely aware of his fears.

I want to attempt a thing like that and am frightened by these trifles, he thought, with an odd smile. Hm... yes, all is in a man's hands and he lets it all slip from cowardice, that's an axiom. It would be interesting to know what it is men are most afraid of. Taking a new step, uttering a new word is what they fear most.... But I am talking too much. It's because I chatter that I do nothing. Or perhaps it is that I chatter because I do nothing. I've learned to chatter this last month, lying for days together in my den thinking... of Jack the Giant-killer. Why am I going there now? Am I capable of that? Is that serious? It is not serious at all. It's simply a fantasy to amuse myself; a plaything! Yes, maybe it is a plaything.

The heat in the street was terrible: and the airlessness, the bustle and the plaster, scaffolding, bricks, and dust all about him, and that special Petersburg stench, so familiar to all who are unable to get out of town in summer all worked painfully upon the young man�s already overwrought nerves. The insufferable stench from the pot-houses, which are particularly numerous in that part of the town, and the drunken men whom he met continually, although it was a working day, completed the revolting misery of the picture. An expression of the profoundest disgust gleamed for a moment in the young man�s refined face. He was, by the way, exceptionally handsome, above the average in height, slim, well-built, with beautiful dark eyes and dark brown hair. Soon he sank into deep thought, or more accurately speaking into a complete blankness of mind; he walked along not observing what was about him and not caring to observe it. From time to time, he would mutter something, from the habit of talking to himself, to which he had just confessed. At these moments he would become conscious that his ideas were sometimes in a tangle and that he was very weak; for two days he had scarcely tasted food.'''
preprocessing(test, False)
preprocessing(test, True)

