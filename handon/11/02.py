"""
Author:
Purpose:
Date：
"""

import argparse
import tkinter as tk
from PIL import  Image,ImageDraw
import numpy as np
import keras
from tensorflow.keras.layers import Dense
from keras.models import load_model
from keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from keras.preprocessing import image
import os
import matplotlib.pyplot as plt


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def main():
    """the entrance of this file"""
    optimizer = keras.optimizers.SGD(momentum=0.9, learning_rate=0.01,nesterov=True)
    layer1 = keras.layers.Dense(20,
                                activation='relu',
                                kernel_initializer="he_normal",
                                kernel_regularizer=keras.regularizers.l1(0.01))

    layer2 = keras.layers.Dense(20,
                                activation='relu',
                                kernel_initializer="he_normal",
                                kernel_regularizer=keras.regularizers.l2(0.01))

    layer1 = keras.layers.Dense(20,
                                activation='relu',
                                kernel_initializer="he_normal",
                                kernel_regularizer=keras.regularizers.l1(0.01))

    layerall = keras.layers.Dense(20,
                                activation='relu',
                                kernel_initializer="he_normal",
                                kernel_constraint=keras.constraints.max_norm(1.),
                                kernel_regularizer=keras.regularizers.l1_l2(0.01))
    layer_dropout = keras.layers.Dropout(rate=0.02)

if __name__ == '__main__':
    main()
