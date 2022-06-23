
"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


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
    model = keras.Sequential(
        [
            keras.layers.Dense(2, activation="relu"),
            keras.layers.Dense(3, activation="relu"),
            keras.layers.Dense(4),
        ]
    )
    layer1 = keras.layers.Dense(3)
    print(layer1.weights)
    x = np.ones((1,4))
    layer1(x)
    print(layer1.weights)



if __name__ == '__main__':
    main()