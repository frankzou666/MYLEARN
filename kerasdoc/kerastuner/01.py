"""
Author:
Purpose: Getting started with KerasTuner
Date：
"""

import argparse

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import keras_tuner as kt
import numpy as np
import matplotlib.pyplot as plt

tf.get_logger().setLevel('DEBUG')
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def build_model(hp):
    model = keras.Sequential()
    model.add(layers.Flatten())
    model.add(
        layers.Dense(
            # Define the hyperparameter.
            units=hp.Int("units", min_value=32, max_value=512, step=32),
            activation="relu",
        )
    )
    model.add(layers.Dense(10, activation="softmax"))
    learning_rate = hp.Float("lr",min_value=1e-4,max_value=1e-2,sampling="log")
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate)
        , loss="categorical_crossentropy", metrics=["accuracy"],
    )
    return model


class MyHyperModel(kt.HyperModel):
    def build(self, hp):
        model = keras.Sequential()
        model.add(layers.Flatten())
        model.add(
            layers.Dense(
                units=hp.Int("units", min_value=32, max_value=512, step=32),
                activation="relu",
            )
        )
        model.add(layers.Dense(10, activation="softmax"))
        model.compile(
            optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"],
        )
        return model

    def fit(self, hp, model, x,y,*args, **kwargs):

        return model.fit(
            x,
            y,
            *args,
            # Tune whether to shuffle the data in each epoch.
            shuffle=hp.Boolean("shuffle"),
            **kwargs,
        )


def fun1():
    x = np.linspace(1,10,100).reshape(-1,1)
    y = np.power(x, 2)
    z = np.power(x, 2) + np.random.random(x.shape) * 10-np.random.random(x.shape) * 10
    plt.scatter(x, z, color='r')
    plt.plot(x, y )
    plt.show()

def main():
    """the entrance of this file"""
    hp = kt.HyperParameters()
    myHyperModel = MyHyperModel()
    tuner = kt.RandomSearch(
        MyHyperModel(), objective="accuracy",
        max_trials=3,
        overwrite=True, )
    tunerhp = tuner.get_best_models()[0]
    model = myHyperModel.build(tunerhp)


   # myHyperModel.fit(hp, model, np.random.rand(100, 28, 28), np.random.rand(100, 10))





if __name__ == '__main__':
    main()
