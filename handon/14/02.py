"""
Author:
Purpose:
Date：
"""

import argparse
import tensorflow as tf
import  keras

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
    model = keras.models.Sequential([
        keras.layers.Conv2D(64, 7, activation="relu", padding="same",
                            input_shape=[28, 28, 1]),
        keras.layers.MaxPooling2D(2),
        keras.layers.Conv2D(128, 3, activation="relu", padding="same"),
        keras.layers.Conv2D(128, 3, activation="relu", padding="same"),
        keras.layers.MaxPooling2D(2),
        keras.layers.Conv2D(256, 3, activation="relu", padding="same"),
        keras.layers.Conv2D(256, 3, activation="relu", padding="same"),
        keras.layers.MaxPooling2D(2),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation="relu"),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(64, activation="relu"),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(10, activation="softmax")])
    model.summary()


if __name__ == '__main__':
    main()
