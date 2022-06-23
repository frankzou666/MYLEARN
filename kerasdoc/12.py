
"""
Author:
Purpose: understanding mask and padding
Date：
"""


import argparse

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.linear_model import SGDRegressor



def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def testPadding():
    rowinputs = [
        [3, 3],
        [4, 6, 4],
        [4, 6, 4,5]
    ]
    paddedinputs = keras.preprocessing.sequence.pad_sequences(rowinputs, padding='post')
    embedding = layers.Embedding(input_dim=5000, output_dim=16, mask_zero=True)
    masked_output = embedding(paddedinputs)
    print(masked_output._keras_mask)


class MyLayer(layers.Layer):
    def __init__(self, **kwargs):
        super(MyLayer, self).__init__(**kwargs)
        self.embedding = layers.Embedding(input_dim=5000, output_dim=16, mask_zero=True)
        self.lstm = layers.LSTM(32)
    def call(self, inputs):
        outputs = self.embedding(inputs)
        return outputs




def getModel():
    #input
    input = keras.Input(shape=(None,))
    #hidden
    x = keras.layers.Embedding(input_dim=1500, output_dim=16, mask_zero=True)(input)
    #ouput
    ouput = layers.LSTM(32)(x)
    #model
    model = keras.Model(input, ouput)
    return  model

def main():
    rowinputs = [
        [3, 3],
        [4, 6, 4],
        [4, 6, 4, 5]
    ]
    paddedinputs = keras.preprocessing.sequence.pad_sequences(rowinputs, padding='post')
    myLayer = MyLayer()
    print(myLayer(paddedinputs))

if __name__ == '__main__':
    main()