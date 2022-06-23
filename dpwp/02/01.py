"""
Author:
Purpose:
Date：
"""

import argparse
import keras
import keras.layers
from  keras.datasets import mnist
from tensorflow.keras.utils import to_categorical



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
    traindata, trainlabel, testdata, testlabel = getMnist()
    model = keras.models.Sequential(name="my hello model")
    model.add(keras.layers.Dense(units=512, activation='relu', input_shape=(28*28,)))
    model.add(keras.layers.Dense(units=10, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    model.summary()
    model.fit(traindata,trainlabel,epochs=10,batch_size=128)
    #testloss, testacc = model.evaluate(testdata, testlabel)

    #print(testloss)
    #print(testacc)


if __name__ == '__main__':
    main()
