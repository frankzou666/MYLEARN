"""
Author:
Purpose:
Date：
"""

import argparse
import keras
import keras.layers
from keras.layers import Layer
from  keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import time



def getMnist():
    """

    :return:
    """
    (traindata,trainlabel),(testdata,testlabel) = mnist.load_data()
    traindata = traindata.reshape((60000,28*28))
    traindata = traindata.astype('float32')/255
    testdata = testdata.reshape((10000, 28 * 28))
    testdata = testdata.astype('float32') / 255
    trainlabel = to_categorical(trainlabel)
    testlabel = to_categorical(testlabel)
    return traindata, trainlabel, testdata, testlabel



class MyLayer(Layer):
    """

    """
    def __init__(self, **kwargs):
        super(MyLayer, self).__init__(**kwargs)

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
    start_time = time.perf_counter()
    traindata, trainlabel, testdata, testlabel = getMnist()
    model = keras.models.Sequential(name="my hello model")
    model.add(keras.layers.Dense(units=512, activation='relu', input_shape=(28*28,)))
    model.add(keras.layers.Dense(units=10, activation='softmax'))
    model.add(MyLayer())
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    model.summary()
    #model.fit(traindata,trainlabel,epochs=10,batch_size=128)
    #testloss, testacc = model.evaluate(testdata, testlabel)
    end_time = time.perf_counter()
    print("use time(seconds):"+ str(end_time-start_time))


    #print(testloss)
    #print(testacc)


if __name__ == '__main__':
    main()
