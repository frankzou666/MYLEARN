
"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
from tensorflow import keras

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
    model = keras.models.Sequential()
    model.add(keras.layers.LSTM(20,return_sequences = True,input_shape=[None,1]))
    model.add(keras.layers.LSTM(20,return_sequences = True))
    model.add(keras.layers.Dense(1))
    model.summary()



if __name__ == '__main__':
    main()