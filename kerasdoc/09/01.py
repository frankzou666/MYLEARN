
"""
Author:
Purpose:
Date：
"""
import numpy as np
import tensorflow as tf
from tensorflow import keras

import argparse

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
    PATH = r'c:/Users/Administrator/PycharmProjects/untitled/kerasdoc/09/11'
    model = keras.models.Sequential()
    layers = keras.layers.Dense(10,input_shape=(10,1))
    model.add(layers)
    conf = layers.get_config()

if __name__ == '__main__':
    main()