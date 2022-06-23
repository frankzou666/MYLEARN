
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



def getModel(filename):
    """
           :arg
           :return model
           :date
    """
    traindata, trainlabel, testdata, testlabel = getMnist()
    model = keras.models.Sequential()
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Dropout(0.25))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(256, activation='relu'))
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x=traindata,y=trainlabel, epochs=5, batch_size=128)
    model.save(filename)
    return  model



def main():
    """
         :arg
         :return main,get keras model,creat Tk object
        :date
    """
    traindata, trainlabel, testdata, testlabel = getMnist()
    img = image.array_to_img(traindata[8])
    print(trainlabel[8])
    plt.imshow(img)
    plt.show()



if __name__ == '__main__':
    """
        :arg
        :return app run
        :date
    """
    main()