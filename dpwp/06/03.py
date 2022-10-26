
"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
import keras as keras
from  keras import layers
from tensorflow import keras
from keras.datasets.imdb import  load_data
#from keras.preprocessing import sequence
import matplotlib.pyplot as plt
import ssl



ssl._create_default_https_context = ssl._create_unverified_context

max_features = 5000
max_len = 500

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def loadImdb():

    print('Loading data...')
    (x_train, y_train), (x_test, y_test) = load_data(num_words=max_features)
    print(len(x_train), 'train sequences')
    print(len(x_test), 'test sequences')
    print('Pad sequences (samples x time)')
    x_train =  keras.preprocessing.sequence.pad_sequences(x_train, maxlen=max_len)
    x_test = keras.preprocessing.sequence.pad_sequences(x_test, maxlen=max_len)
    print('x_train shape:', x_train.shape)
    print('x_test shape:', x_test.shape)
    return  x_train, y_train, x_test, y_test


def plotHistory(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(acc) + 1)
    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.legend()
    plt.show()

def main():
    x_train, y_train, x_test, y_test = loadImdb()
    model = keras.models.Sequential()
    model.add(layers.Embedding(max_features, 128, input_length=max_len))
    model.add(layers.Conv1D(32, 7, activation='relu'))
    model.add(layers.MaxPooling1D(5))
    model.add(layers.Conv1D(32, 7, activation='relu'))
    model.add(layers.GRU(32))
    model.add(layers.Dense(1))
    model.summary()
    model.compile(optimizer=keras.optimizers.RMSprop(lr=1e-4),
                  loss='binary_crossentropy',
                  metrics=['acc'])
    history = model.fit(x_train,y_train,epochs=10,batch_size=128,validation_split=0.2)
    plotHistory(history)

if __name__ == '__main__':
    main()