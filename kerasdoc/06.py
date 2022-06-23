
"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow import keras
from  keras.preprocessing.text import  one_hot
from keras.datasets.mnist import  load_data
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()


def get_uncompiled_model():
    inputs = keras.Input(shape=(784,), name="digits")
    x = layers.Dense(64, activation="relu", name="dense_1")(inputs)
    x = layers.Dense(64, activation="relu", name="dense_2")(x)
    outputs = layers.Dense(10, activation="softmax", name="predictions")(x)
    model = keras.Model(inputs=inputs, outputs=outputs)
    return model


def get_compiled_model():
    model = get_uncompiled_model()
    model.compile(
        optimizer="rmsprop",
        loss="sparse_categorical_crossentropy",
        metrics=["sparse_categorical_accuracy"],
    )
    return model

def myLossFunc(ytrue,ypred):
    return tf.math.reduce_mean(tf.square(ytrue - ypred))

def main():
    (X_train,y_train),(X_test,y_test) = load_data()
    inputs = keras.Input(shape=(784,), name="digits")
    x = layers.Dense(64, activation="relu", name="dense_1")(inputs)
    x = layers.Dense(64, activation="relu", name="dense_2")(x)
    outputs = layers.Dense(10, activation="softmax", name="predictions")(x)

    model = keras.Model(inputs=inputs, outputs=outputs)
    x_train = X_train.reshape(60000, 784).astype("float32") / 255
    x_test = X_test.reshape(10000, 784).astype("float32") / 255

    y_train = y_train.astype("float32")
    y_test = y_test.astype("float32")
    x_val = x_train[-10000:]
    y_val = y_train[-10000:]
    x_train = x_train[:-10000]
    y_train = y_train[:-10000]
    model = get_uncompiled_model()
    model.compile(optimizer=keras.optimizers.Adam(), loss=myLossFunc)

    # We need to one-hot encode the labels to use MSE
    y_train_one_hot = tf.one_hot(y_train, depth=10)
    model.fit(x_train, y_train_one_hot, batch_size=64, epochs=1)

if __name__ == '__main__':
    main()