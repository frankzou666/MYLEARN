"""
Author:
Purpose:
Date：
"""

import argparse
import glob
import os
from keras.preprocessing.image import image
import numpy as np
from keras.models import  load_model,Model
import matplotlib.pyplot as plt
import keras.layers
from  keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def getMnist():
    (traindata,trainlabel),(testdata,testlabel) = mnist.load_data()
    traindata = traindata.reshape((60000, 28, 28, 1))
    traindata = traindata.astype('float32') / 255
    testdata = testdata.reshape((10000, 28, 28, 1))
    testdata = testdata.astype('float32') / 255
    trainlabel = to_categorical(trainlabel)
    testlabel = to_categorical(testlabel)
    return traindata,trainlabel,testdata,testlabel

def main():
    """the entrance of this file"""
    img = image.load_img('C:\\1\\dogandcat\\creative_commons_elephant.jpg', target_size=(150, 150))
    imgarray = image.img_to_array(img)
    imgarray = np.expand_dims(imgarray, axis=0)
    imgarray = imgarray / 225.

    traindata, trainlabel, testdata, testlabel = getMnist()
    model = load_model('C://Users//Administrator//PycharmProjects//untitled//tk//m.h5')
    test_img = np.expand_dims(traindata[0], axis=0)

    activaitons = [layer.output for layer in model.layers[:4]]
    new_model = Model(inputs=model.input,outputs=activaitons)
    acts = new_model.predict(test_img)
    for act in acts:
        print(act.shape)
    fig, axs = plt.subplots(nrows=5, ncols=6, constrained_layout=False)
    subplots = axs.tolist()
    subplots = [ item for plot in subplots for item in plot]
    print(len(subplots))
    for i in range(len(acts)):
        for j in range(7):
            subplots[(i*4)+j].imshow(acts[i][0, :, :, j], cmap='viridis')

    plt.show()





if __name__ == '__main__':
    main()
