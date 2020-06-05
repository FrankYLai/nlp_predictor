import string

SEQUENCE_LENGTH = 46

def token_generate(textdata):
    textdata = textdata.lower()
    word_list = textdata.split(" ")
    
    table = str.maketrans('', '', string.punctuation)
    word_list = [w.translate(table) for w in word_list]
    word_list = [word for word in word_list if word.isalpha()]
    return word_list

def sequence_from_tokens(tokens):
    sequences = []
    for i in range(SEQUENCE_LENGTH, len(tokens)):
        sequences.append([])
        for j in tokens[i-SEQUENCE_LENGTH:i]:  
            sequences[-1].append(j)
        # sequences[-1].append(tokens[i])
        # sequences[-1].append(tokens[i-SEQUENCE_LENGTH:i])
        # sequences[-1].append(tokens[i])
    print(sequences[0])
    return sequences

def preprocessing(data):
    #cleaning data and generating sequences
    tokens = token_generate(data)
    #tokenizing words
    existing_words = sorted(set(tokens))
    enumerated_dict = dict((w,i) for i, w in enumerate(existing_words))

    enumerated_tokens = []
    for i in tokens:
        enumerated_tokens.append(enumerated_dict[i])

    sequence = sequence_from_tokens(enumerated_tokens)

    return sequence, enumerated_dict




