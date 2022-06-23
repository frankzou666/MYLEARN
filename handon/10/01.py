
"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
from tensorflow import keras
import pandas as pd

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def perceptronTest():
    iris = load_iris()
    x = iris.data
    y = iris.target
    petclf = Perceptron()
    petclf.fit(x,y)
    print(petclf.predict([[1,5,4,3]]))

def kerasTest():
    fashion_mnist = keras.datasets.fashion_mnist
    (X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()
    X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:] / 255.0
    y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
    model = keras.models.Sequential()
    model.add(keras.layers.Flatten(input_shape=[28,28]))
    model.add(keras.layers.Dense(300, activation='relu'))
    model.add(keras.layers.Dense(100, activation='relu'))
    model.add(keras.layers.Dense(10,  activation='softmax'))
    model.compile(loss='sparse_categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])
    history = model.fit(X_train,y_train,epochs=30,batch_size=64 ,validation_data=(X_test,y_test))
    pd.DataFrame(history.history).plot()
    plt.gca().set_ylim(0,1)
    plt.show()


def main():
    """

    :return:
    """
    perceptronTest()

if __name__ == '__main__':
    main()