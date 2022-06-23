
"""
Author:
Purpose:
Date：
"""


import argparse
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,Dense,Flatten
from tensorflow.keras.preprocessing.text import one_hot,Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb
import pandas as pd
import matplotlib.pyplot as plt


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def toyFun():
    vocab = 'hello cat from dog china ok'
    texts = 'hello from china '
    testdict ={}
    for i,c in enumerate(vocab.split(' ')):
        testdict[c] = i
    r = np.zeros(shape=(1,len(testdict.keys())))
    for i in texts.split(' '):
        if i in testdict.keys():
            r[0][testdict[i]] = 1
    print(r)


def main():
    max_features = 10000
    maxlen = 20
    (x_train, y_train), (x_test, y_test) = imdb.load_data(
        num_words=max_features)
    x_train =  pad_sequences(x_train, maxlen=maxlen)
    x_test  =  pad_sequences(x_test, maxlen=maxlen)
    model = Sequential()
    model.add(Embedding(10000, 8, input_length=maxlen))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
    model.summary()
    history = model.fit(x_train, y_train,
                        epochs=10,
                        batch_size=32,
                        validation_split=0.2)

    pds = pd.DataFrame(history.history)
    pds.plot()
    plt.show()


if __name__ == '__main__':
    main()