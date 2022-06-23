
import numpy as np
import tensorflow as tf
import keras
from keras.layers import TextVectorization
from keras.layers import *
from keras import layers
from keras.datasets.mnist import load_data
import keras_tuner

def getModel():
    inputs = keras.Input(shape=(28, 28))
    x = layers.Rescaling(1.0 / 255)(inputs)
    x = layers.Flatten()(x)
    x = layers.Dense(128, activation="relu")(x)
    x = layers.Dense(128, activation="relu")(x)
    outputs = layers.Dense(10, activation="softmax")(x)
    model = keras.Model(inputs, outputs)
    # Compile the model
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", run_eagerly=True)
    return  model




def main():
    (x_train, y_train), (x_test, y_test) = load_data()

    # Build a simple model


if __name__ == '__main__':
    main()