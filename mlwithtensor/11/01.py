
"""
Author:
Purpose:
Date：
"""


import argparse
import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
import sklearn
from sklearn import datasets

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


class AutoCoder(keras.models.Model):
    def __init__(self,input_dim, hidden_dim):
        super(AutoCoder,self).__init__()
        self.encoder = keras.models.Sequential()
        self.decoder = keras.models.Sequential()
        self.encoder = tf.keras.Sequential([
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(hidden_dim, activation='tanh'),
        ])
        self.decoder = tf.keras.Sequential([
            tf.keras.layers.Dense(input_dim)
        ])
    def call(self,x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

def main():
    hidden_dim = 1
    x_train = datasets.load_iris().data
    input_dim = len(x_train[0])
    x_test = np.asarray([[8, 4, 6, 2]])
    ae = AutoCoder(input_dim, hidden_dim)
    ae.compile(optimizer='rmsprop', loss=keras.losses.MeanSquaredError())

if __name__ == '__main__':
    main()