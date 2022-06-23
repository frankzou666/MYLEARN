
"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
#from tensorflow import keras
import keras
from keras.preprocessing.text import one_hot



from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.embeddings import Embedding

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def main():
    docs = ['Well done!',
            'Good work',
            'Great effort',
            'nice work',
            'Excellent!',
            'Weak',
            'Poor effort!',
            'not good',
            'poor work',
            'Could have done better.']
    # define class labels
    labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    vocabsize = 50
    encoded_docs = [one_hot(word,vocabsize) for word in docs]
    max_length = 4
    padded_docs = keras.preprocessing.sequence.pad_sequences(encoded_docs, maxlen=max_length, padding='post')
    model = keras.models.Sequential()
    model.add(keras.layers.Embedding(vocabsize, 8, input_length=max_length))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])
    model.fit(padded_docs,np.array(labels),epochs=48)

    loass, accuracy = model.evaluate(padded_docs,np.array(labels))
    print(accuracy)
    print(padded_docs)
    print(model.predict(np.array([[4, 32,  5 , 6]]).reshape((1,4))))
    


def main2():
    docs = ['Well done!',
            'Good work',
            'Great effort',
            'nice work',
            'Excellent!',
            'Weak',
            'Poor effort!',
            'not good',
            'poor work',
            'Could have done better.']
    # define class labels
    labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    # integer encode the documents
    vocab_size = 50
    encoded_docs = [one_hot(d, vocab_size) for d in docs]
    print(encoded_docs)
    # pad documents to a max length of 4 words
    max_length = 4
    padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
    print(padded_docs)
    # define the model
    model = Sequential()
    model.add(Embedding(vocab_size, 8, input_length=max_length))
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))
    # compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
    # summarize the model
    model.summary()
    # fit the model
    model.fit(padded_docs, np.array(labels), epochs=50, verbose=0)
    # evaluate the model
    loss, accuracy = model.evaluate(padded_docs, np.array(labels), verbose=0)
    print('Accuracy: %f' % (accuracy * 100))

if __name__ == '__main__':
    main()