import string

#constants:
LENGTH = 30
punctuations_delete = '''\n!()[]{};:'"\,<>./?@#$%^&*_~'''
punctuations_keep = "- '"
existing_characters = sorted(list(punctuations_keep+string.ascii_lowercase))
MAP = dict((c,i) for i, c in enumerate(existing_characters))





def dataCleaner(textdata):

    textdata = textdata.lower()
    for x in textdata: 
        if x in punctuations_delete: 
            textdata = textdata.replace(x, "") 
    word_list = textdata.split(" ")
    new_word_list = []

    #only keeps words that have more than 3 characters
    for i in word_list:
        if len(i)>=3:
            new_word_list.append(i)

    return (" ".join(new_word_list)).strip()

def sequence_create(text, append_to = None):
    sequences = list()
    if append_to is not None:
        sequneces = append_to
    
    for i in range (len(text) - LENGTH):
        sequences.append(text[i:i+LENGTH])
    
    print ("created ", len(sequences), " sequences")
    return sequences

def enumerate_seq(sequence):
    enumerated_sequence = []
    count = 0
    for i in sequence:
        enumerated_sequence.append([])
        for j in i:
            enumerated_sequence[-1].append(MAP[j])
        count +=1
    
    return enumerated_sequence


def preprocessing(data):

    dataText = dataCleaner(data)
    sequence = sequence_create(dataText)
    sequence = enumerate_seq(sequence)
    print("....")

    return sequence

            
    