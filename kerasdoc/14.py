"""
Author:
Purpose: transfer learning and fine tuning
Date：
"""

import argparse
import tensorflow as tf
import tensorflow.keras as keras
import numpy as np

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def trainablLayer():
    """

    :return:
    """
    layer1 = keras.layers.Dense(3, activation="relu")
    layer2 = keras.layers.Dense(3, activation="sigmoid")
    model = keras.Sequential([keras.Input(shape=(3,)), layer1, layer2])
    layer1.trainable = False
    startweights = layer1.get_weights()
    print('start weights')
    print(startweights)
    model.compile(optimizer="adam", loss="mse")
    model.fit(np.random.random((2, 3)), np.random.random((2, 3)))
    print('after weights')
    print(layer1.get_weights())
    return True


def main():
    """the entrance of this file"""
    dataset = np.arange(0,9).reshape(3,3)
    base_model = keras.applications.Xception(
        weights='imagenet',  # Load weights pre-trained on ImageNet.
        input_shape=(150, 150, 3),
        include_top=False)  # Do not include the ImageNet classifier at the top.
    # freezm base model
    base_model.trainale=False
    ##input layer
    inputlayer = keras.Input(shape=(150, 150, 3))
    x = base_model(inputlayer,training=False)
    gl = keras.layers.GlobalAvgPool2D()(x)
    ## output layer
    outputlayer = keras.layers.Dense(1)(gl)
    #new model
    model = keras.Model(inputlayer,outputlayer)
    #model.compile(optimizer=keras.optimizers.Adam(),
    #              loss=keras.losses.BinaryCrossentropy(from_logits=True),
    #              metrics=[keras.metrics.BinaryAccuracy()])
    lossfun = keras.losses.BinaryCrossentropy(from_logits=True)
    optimizerfun = keras.optimizers.Adam()

    for inputs, targets in dataset:
        with tf.GradientTape()  as tg:
            predictval = model(inputlayer)
            lossval = lossfun(predictval,targets)
        gradientval = tg.gradient(lossval, model.trainable_weights)
        optimizerfun.apply_gradients(gradientval,model.trainable_weights)


if __name__ == '__main__':
    main()
