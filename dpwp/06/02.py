
"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
import tensorflow.keras as keras
from keras.datasets.imdb import  load_data
from tensorflow.keras.preprocessing import sequence
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

def main1():
    times=100
    inputfeatures=32
    outputfeatures=64
    inputs = np.random.random((times,inputfeatures))
    stats_t = np.zeros((outputfeatures,))
    W = np.random.random((outputfeatures, inputfeatures))
    U = np.random.random((outputfeatures, outputfeatures))
    b = np.random.random((outputfeatures,))
    r = []
    for input in inputs:
        output = np.tanh(np.dot(W,input) + np.dot(U,stats_t) + b)
        r.append(output)
        stats_t = output

    print(r)

def loadImdbData(max_features):
    maxlen = 500
    (xtrain,ytrain),(xtest,ytest) = load_data(num_words=max_features)
    xtrain = sequence.pad_sequences(xtrain,maxlen=maxlen)
    xtest = sequence.pad_sequences(xtest, maxlen=maxlen)
    return  (xtrain,ytrain),(xtest,ytest)


def plotHistory(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(acc) + 1)
    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.show()

def main2():
    model = keras.models.Sequential()
    model.add(keras.layers.SimpleRNN(32,input_shape=(10000,32),return_sequences=True))
    model.add(keras.layers.SimpleRNN(32,return_sequences=True))
    model.add(keras.layers.SimpleRNN(32,return_sequences=True))
    model.add(keras.layers.SimpleRNN(32))
    model.summary()

def main():
    max_features = 10000
    (xtrain,ytrain),(xtest,ytest) = loadImdbData(max_features)
    model = keras.models.Sequential()
    model.add(keras.layers.Embedding(max_features,32))
    #model.add(keras.layers.SimpleRNN(32))
    model.add(keras.layers.GRU(32))
    model.add(keras.layers.Dense(1,activation='sigmoid'))
    model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['acc'])
    history = model.fit(xtrain,ytrain,epochs=10,batch_size=128,validation_split=0.2)
    plotHistory(history)

if __name__ == '__main__':
    main()