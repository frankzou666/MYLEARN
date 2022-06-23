
"""
Author:
Purpose:
Date：
"""


import argparse

from tensorflow import keras
from keras.datasets.mnist import  load_data

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
    (Xtrain,Ytrain),(Xtest,Ytest) = load_data ()
    encoder = keras.models.Sequential([keras.layers.Flatten(input_shape=[28,28])])
    encoder.add(keras.layers.Dense(100,activation='selu'))
    encoder.add(keras.layers.Dense(30, activation='selu'))

    decoder = keras.models.Sequential([keras.layers.Dense(100, activation='selu',input_shape=[30])])
    decoder.add(keras.layers.Dense(28*28, activation='sigmoid'))
    decoder.add(keras.layers.Reshape([28*28]))


    autoencoder = keras.models.Sequential([encoder, decoder])
    autoencoder.compile(loss="binary_crossentropy", optimizer=keras.optimizers.SGD(lr=0.1))
    autoencoder.summary()
    autoencoder.fit(Xtrain,Ytrain,epochs=10,valid)

if __name__ == '__main__':
    main()