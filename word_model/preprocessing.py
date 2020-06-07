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
