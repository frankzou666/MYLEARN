
"""
Author:
Purpose: Working with RNNs
Date：
"""


import argparse
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
#import keras

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
    model = keras.Sequential()

    model.add(
        layers.Bidirectional(layers.LSTM(64, return_sequences=True), input_shape=(5, 10))
    )
    model.add(layers.Bidirectional(layers.LSTM(32)))
    model.add(layers.Dense(10))

    model.summary()


if __name__ == '__main__':
    main()