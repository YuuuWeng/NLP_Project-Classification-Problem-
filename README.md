# NLP(Project) - Classification Problem
A bert-based classification model is implemented to distinguish the provided tweets are rumours or not.

## Data Preprocessing
Based on the provided tweets IDs, a python-based crawler is built to crawl the corresponding objects(the most essential one is the source and reply message).
For the steps of the data preprocesing

1. Concatenate each tweet event
2. Feature selection(tweet's text)
3. Text pre-processing (“@people”, emojis, URLs, punctuation and the “#” sign in hashtags are removed)


## Model 
1. LSTM, GRU, Bi-LSTM (TensorFlow Sequencial Keras Model)
2. Bert base (Pytorch - adding one linear classifier)

## Result 

The accuracy for Bert model achieves 0.91 for the test set.
