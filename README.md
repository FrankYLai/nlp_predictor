# nlp_predictor

My exparamentations with basic NLP, Initially made for the assessment posted by Pencil Learning Technologies but I 
might develop more features and make this this into an actual project :) 

The original project only mentions developing a word level next word predictor model but I also exparamented a 
little and trained a character level predictor model. Overall I'm supprised by the results given this is the my first
time trying an NLP project. **If you are from Pencil Learning Technologies, the submission for the ML assessment is in
/word_model.**

## character model
Can predict the next character in a sequence of of characters. This model was trained on the declairation of independance
using a GRU layer for recurrent neural network, and finally a dense layer. each input array is
29 characters long.

Overall this one does alright when presented with some characters. It successfully learned to follow the general rules of
English and knows to put spaces when a word should end. Might be able to use this model for autofilling words and such.

## word model
Can predict the next word in a sequence of words. There are two models currently saved. Argparse is currently added to both
the trainer and the predictor files. A sample of the command is as follows
<p align="center">
python predictor model=model2 n=10
</p>
model: select the model used for prediction
n: number of words the predictor should predict after input sequence

For both models, I trained them with 100 epoaches which may have caused some overfitting. After epoach 60, the validation
accuracy was no longer improving while the training set accuracy kept improving. I'm not sure but for projects like these
an accuracy of over 30% should be a symptom of overfitting right?

### model 1
Model 1 was created trained on the entire book of crime and punishment. Data cleaning eliminates all punctuation so the 
model wouldn't know when a sentance ends. The neural network for this one conisists of 2LSTM layers followed by 2 more dense
layers. The default input size it was trained on is 45 words. model 1 preforms alright under ideal conditions (large input, no 
unknown values), but it struggles when conditions are not ideal and the user requests multiple words. The model makes grammar 
mistakes and repeats certain words. Some of these issues are addressed by model 2

### model 2
Model 2 is similar to model one except for 2 key differences. Model 2 was trained on shelock holems so it had much more text to
work with. But more significantly, the last 300 words in its dictionary was deliberately "forgotten" by the model. This way, the
model can learn to deal with unknown input when training. Compaired to model 1, model 2 has much better preformance. It deals with 
unknown words much better and the repeating behavior has not yet been observed.
