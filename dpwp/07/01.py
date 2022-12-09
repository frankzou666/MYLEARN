
"""
Author:
Purpose:
Date：
"""

import tensorflow as tf
import argparse
import keras
import numpy as np

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def getSequential():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(128,activation='relu',input_shape=(64,)))
    model.add(keras.layers.Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    return  model

def getCustomModel():
    inputlayer = keras.Input(shape=64)
    hiden1 = keras.layers.Dense(128, activation='relu')(inputlayer)
    outputlayer = keras.layers.Dense(10, activation = 'softmax')(hiden1)
    model = keras.models.Model(inputlayer, outputlayer)
    model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
    return model

def getMultiInputModel():
    textinput = keras.Input(shape=(None,), dtype='int32', name='textinput')
    textembed = keras.layers.Embedding(64, 10000)(textinput)
    textlstm = keras.layers.LSTM(32)(textembed)

    questioninput = keras.Input(shape=(None,),dtype='int32',name='questioninput')
    questionembed = keras.layers.Embedding(64,10000)(questioninput)
    questionlstm = keras.layers.LSTM(32)(questionembed)
    #注意这里是最后一层
    concated = keras.layers.concatenate([textlstm,questionlstm],axis=-1)
    answer = keras.layers.Dense(100,activation = 'softmax')(concated)
    #model这里连接是第一层
    model = keras.models.Model([textinput,questioninput], answer)
    return model




def main():
    x = np.random.random((1000,64))
    y = np.random.random((1000,10))
    model = getCustomModel()
    model.summary()
    model.fit(x,y,epochs=128,batch_size=64)


if __name__ == '__main__':
    main()