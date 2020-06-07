from includes import *
import preprocessing
import argparse

#parse args
parser = argparse.ArgumentParser()
parser.add_argument('data', help='path to training data file')
parser.add_argument('output', help = "name of the output file")
parser.add_argument('train_on_unknown', help ='if model will forget some of its vocab to learn how to deal with unknown input',type=bool, default=False )
args = parser.parse_args()



def main():
    #read input
    infile = open(args.data,'r')
    data = infile.read()
    infile.close()

    #condition data and generate 
    sequence, tokens =preprocessing.preprocessing(data,args.train_on_unknown)
    encoded_data = np.array(sequence)
    vocab = len(tokens)+1 #since we skip 0 array

    #generate x and y matricies, the y matrix is the last collumb of the sequence matrix
    X, y= encoded_data[:, :-1],  encoded_data[:,-1]
    X_length = X.shape[1]

    #one hot encoding
    y = to_categorical(y, num_classes=vocab)
    X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.1, random_state=42)
    print('Train shape:', X_tr.shape, 'Val shape:', X_val.shape)

    # define model
    model = Sequential()
    model.add(Embedding(vocab, 50, input_length=X_length))
    model.add(LSTM(100, return_sequences=True))
    model.add(LSTM(100))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(vocab, activation='softmax'))
    print(model.summary())

    # compile the model
    model.compile(loss='categorical_crossentropy', metrics=['acc'], optimizer='adam')
    # train the model
    model.fit(X_tr, y_tr, epochs=100, verbose=2, validation_data=(X_val, y_val), batch_size=128)
    
    #save the model
    filename = "model2"
    outfile = open(filename,'wb')
    pickle.dump((model,tokens),outfile)
    outfile.close()

if __name__ == "__main__":
    main()