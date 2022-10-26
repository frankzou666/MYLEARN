"""
Author:
Purpose:
Date：
"""

import argparse
import keras
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

np.random.seed(4)

def generate_3d_data(m, w1=0.1, w2=0.3, noise=0.1):
    angles = np.random.rand(m) * 3 * np.pi / 2 - 0.5
    data = np.empty((m, 3))
    data[:, 0] = np.cos(angles) + np.sin(angles)/2 + noise * np.random.randn(m) / 2
    data[:, 1] = np.sin(angles) * 0.7 + noise * np.random.randn(m) / 2
    data[:, 2] = data[:, 0] * w1 + data[:, 1] * w2 + noise * np.random.randn(m)
    return data

def main():
    """the entrance of this file"""
    X_train = generate_3d_data(60)
    X_train = X_train - X_train.mean(axis=0, keepdims=0)
    encoder = keras.models.Sequential(keras.layers.Dense(2,input_shape=(3,)))
    decoder = keras.models.Sequential(keras.layers.Dense(3, input_shape=(2,)))
    autoencoder = keras.models.Sequential([encoder,decoder])
    autoencoder.compile(optimizer=keras.optimizers.SGD(),loss="mse")
    history = autoencoder.fit(X_train, X_train, epochs=20)
    codings = encoder.predict(X_train)
    fig = plt.figure(figsize=(4, 3))
    plt.plot(codings[:, 0], codings[:, 1], "b.")
    plt.xlabel("$z_1$", fontsize=18)
    plt.ylabel("$z_2$", fontsize=18, rotation=0)
    plt.grid(True)
    plt.show()



if __name__ == '__main__':
    main()
