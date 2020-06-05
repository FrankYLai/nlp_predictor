from includes import *
import preprocessing
import data


def main():
    #conditioning the data for training
    encoded_data = np.array(preprocessing.preprocessing(data.dataText))

    #data splitting:
    possible_chars = len(preprocessing.existing_characters)
    X, y = encoded_data[:,:-1], encoded_data[:,-1]

    y = to_categorical(y, num_classes=possible_chars)
    X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.1, random_state=42)
    print('Train shape:', X_tr.shape, 'Val shape:', X_val.shape)

    #training
    model = Sequential()
    model.add(Embedding(possible_chars, 50, input_length=29, trainable=True))
    model.add(GRU(150, recurrent_dropout=0.1, dropout=0.1))
    model.add(Dense(possible_chars, activation='softmax'))
    print(model.summary())

    # compile the model
    model.compile(loss='categorical_crossentropy', metrics=['acc'], optimizer='adam')
    # fit the model
    model.fit(X_tr, y_tr, epochs=100, verbose=2, validation_data=(X_val, y_val))

    filename = "model"
    outfile = open(filename,'wb')
    pickle.dump(model,outfile)
    outfile.close()
    





if __name__ == "__main__":
    main()
