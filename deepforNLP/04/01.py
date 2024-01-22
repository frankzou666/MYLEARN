
import keras
from keras.layers import Dense
import numpy as np
import tensorflow as tf

def getSequentail():
    X = np.random.randint(1, 10, (100, 10))
    y = np.random.randint(1, 10, (100, 1))
    #define model
    model = keras.models.Sequential()
    # add layers ,the output layer activation function is important, regression(none),binary(sigmoid),
    # multiclass (softmax)
    model.add(Dense(32,input_shape=(100,10)))
    model.add(Dense(1,activation='sigmoid'))
    #compile，loss,optimizer(rmsprop,adam,sgd),metric
    # you can define a instance object for optimizer
    model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
    #fit，verbose control the output
    history = model.fit(X,y,batch_size=32,epochs=16)
    print(model.summary())
    return  model


@tf.function()
def tf_cube(x):
    print('from tf_cube:' ,x)
    return  x**3


@tf.function()
def add10(x):
    for i in range(10):
        x = x +1
    return  x


def main2():
    #we first define input later
    inputlayer = keras.layers.Input(shape=(100,1))
    #connect each layer
    lstm1 = keras.layers.LSTM(10)(inputlayer)
    visible = keras.layers.Dense(32,activation='relu')(lstm1)
    outputlayer =  keras.layers.Dense(1,activation='sigmoid')(visible)

    # create model, we only get input layer name and the output layer name
    model = keras.models.Model(inputlayer,outputlayer)
    model.summary()


def main():
    x = np.array([1,2,3,4,5])
    y = np.array([0.2,0.4,0.6,0.8,1.0])
    #分子
    t1 = np.sum((x-x.mean()) * (y-y.mean()))
    #分母
    t2 = np.sum(np.square((x-x.mean())))
    #结果
    print(t1/t2)

if __name__ == '__main__':
    main()