


import keras
from keras import layers
import tensorflow as tf

def main2():
    model = keras.models.Sequential()
    model.add(layers.LSTM(32,input_shape=(100,100),return_sequences=True))
    model.add(layers.LSTM(32, return_sequences=True))
    model.add(layers.LSTM(32))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy',optimizer='rmsprop')


def main3():
    distribution = tf.distribute.MirroredStrategy()
    with distribution.scope():
        model = keras.models.Sequential()
        model.add(layers.LSTM(32, input_shape=(100, 100), return_sequences=True))
        model.add(layers.LSTM(32, return_sequences=True))
        model.add(layers.LSTM(32))
        model.add(layers.Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='rmsprop')



def getDenseModel():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(32, activation='relu', input_shape=(30,)))
    model.add(keras.layers.Dense(32, activation='relu'))
    model.add(keras.layers.Dense(1, activation='sigmoid'))
    model.compile(loss='binary_entropy', optimizer='rmsprop', metrics=['accuracy'])
    return model

def getRNNModel():
    model = keras.models.Sequential()
    model.add(keras.layers.LSTM(32, input_shape=(30, 100), return_sequences=True))
    model.add(keras.layers.LSTM(128, return_sequences=True))
    model.add(keras.layers.LSTM(32))
    model.add(keras.layers.Dense(1, activation='sigmoid'))
    model.compile(loss='binary_entropy', optimizer='rmsprop', metrics=['accuracy'])
    return model


def main():
    model = getRNNModel()
    model.summary()


if __name__ == '__main__':
    main()