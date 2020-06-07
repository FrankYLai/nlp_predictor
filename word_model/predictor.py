from includes import *
import preprocessing
from keras.preprocessing.sequence import pad_sequences



def predict(seed_text, model, tokens):
    #data conditioning
    word_list = preprocessing.token_generate(seed_text)
    enumerated_list = []

    #converts words to their tokenized integer representation
    for w in word_list:
        if w in tokens:
            enumerated_list.append(tokens[w])
        else:
            enumerated_list.append(0)#defaults to 0 if the word is new to the model
        
    enumerated_list = pad_sequences([enumerated_list], maxlen=45, truncating='pre')

    #prediction
    yhat = model.predict_classes(enumerated_list, verbose=0)
    
    #translate prediction back to words
    for word, index in tokens.items():
        if yhat == index:
            return word
    
    print("prediction does not exist")
    return ""
    


#used for testing the trained model
def main():
    with open('model2', 'rb') as pickle_file:
        (model, tokens) = pickle.load(pickle_file)
    while True:
        seed_text = input()
        for i in range(10):
            nextword = predict(seed_text, model, tokens)
            seed_text = seed_text + " " + nextword
        print (seed_text)

        




if __name__ == "__main__":
    main()

