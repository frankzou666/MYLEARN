
"""
Author:
Purpose: base mnsit dataset ,CNN,recognition hand write digitial
Date：
"""


import argparse
import tkinter as tk
from PIL import  Image,ImageDraw
import numpy as np
from tensorflow import keras
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
    return  argparser.parse_args()

def getMnist():
    """
        :arg
        :return  mnist data
        :date
    """
    (traindata,trainlabel),(testdata,testlabel) = mnist.load_data()
    traindata = traindata.reshape((60000, 28, 28, 1))
    traindata = traindata.astype('float32') / 255
    testdata = testdata.reshape((10000, 28, 28, 1))
    testdata = testdata.astype('float32') / 255
    trainlabel = to_categorical(trainlabel)
    testlabel = to_categorical(testlabel)
    return traindata,trainlabel,testdata,testlabel




def expentional_fn(epoch):
    """

    :return:
    """
    return 0.1*0.1**(epoch/20)

def main():
    traindata, trainlabel, testdata, testlabel = getMnist()
    model = keras.models.Sequential()
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(256, activation='relu',
                                 kernel_regularizer = keras.regularizers.l2(0.1)))
    model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.Dense(10, activation='softmax'))
    #optimizer = keras.optimizers.SGD(momentum=0.9, learning_rate=0.01, nesterov=True)
    rmspropOptimizer = keras.optimizers.RMSprop(rho=0.9, learning_rate=0.1)
    #model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.compile(loss='categorical_crossentropy', optimizer=rmspropOptimizer, metrics=['accuracy'])
    modelcallbacks =[]
    modelcallbacks.append(keras.callbacks.LearningRateScheduler(expentional_fn))
    model.fit(x=traindata[0:10000],y=trainlabel[0:10000], epochs=2, batch_size=128,callbacks = modelcallbacks)


if __name__ == '__main__':
    main()