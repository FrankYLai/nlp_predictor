from includes import *
import preprocessing


def main():
    infile = open("model",'rb')
    model = pickle.load(infile)
    infile.close

    while True:
        print("enter input text: ")
        intext = input()
        print(intext)
        for i in range(30):
            #encode

            encoded = [preprocessing.MAP[char] for char in intext]
            encoded = pad_sequences([encoded], maxlen=29, truncating='pre')
            prediction = model.predict_classes(encoded, verbose=0)
            output = ''
            for char, index in preprocessing.MAP.items():
                if index == prediction:
                    output = char
                    break
            intext+=output

        print (intext)
if __name__ == "__main__":
    main()