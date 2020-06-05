from includes import *
import preprocessing

def main():
    infile = open("Crime_and_Punishment.txt",'r')
    data = infile.read()
    infile.close()

    sequence, tokens =preprocessing.preprocessing(data)
    encoded_data = np.array(sequence)
    vocab = len(tokens)

    X, y= encoded_data[:, :-1],  encoded_data[:,-1]
    X_length = X.shape[1]

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
    # fit the model
    model.fit(X_tr, y_tr, epochs=100, verbose=2, validation_data=(X_val, y_val), batch_size=128)
    
    
    filename = "model"
    outfile = open(filename,'wb')
    pickle.dump((model,tokens),outfile)
    outfile.close()

if __name__ == "__main__":
    main()