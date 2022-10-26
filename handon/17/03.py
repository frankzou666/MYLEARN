"""
Author:
Purpose: stack autoencoders.
Date：
"""
import argparse

import keras.optimizers.optimizer_v1
from keras.models import Sequential
from keras.layers import Dense,Flatten,Reshape
from keras.datasets import fashion_mnist
from keras.datasets.mnist import  load_data
import ssl
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE

ssl._create_default_https_context = ssl._create_unverified_context


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def plotHistory(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(acc) + 1)
    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.legend()
    plt.show()

def plot_image(image):
    plt.imshow(image, cmap="binary")
    plt.axis("off")


def show_reconstructions(model, images, n_images=5):
    reconstructions = model.predict(images[:n_images])
    fig = plt.figure(figsize=(n_images * 1.5, 3))
    for image_index in range(n_images):
        plt.subplot(2, n_images, 1 + image_index)
        plot_image(images[image_index])
        plt.subplot(2, n_images, 1 + n_images + image_index)
        plot_image(reconstructions[image_index])


def plot_image(image):
    plt.imshow(image, cmap="binary")
    plt.axis("off")
    plt.show()




def main():
    """the entrance of this file"""

   # (X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()
    #X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:] / 255.0
    #y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

    (X_train_full, y_train_full), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
    X_train_full = X_train_full.astype(np.float32) / 255
    X_test = X_test.astype(np.float32) / 255
    X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]
    y_train, y_valid = y_train_full[:-5000], y_train_full[-5000:]
    print(X_train.shape)
    print(y_train.shape)

    # encoder
    encoder = Sequential()
    encoder.add(Flatten(input_shape=[28,28]))
    encoder.add(Dense(100,activation='selu'))
    # central
    encoder.add(Dense(30, activation='selu'))

    # decoder
    decoder = Sequential()
    decoder.add(Dense(100, activation='selu',input_shape=(30,)))
    decoder.add(Dense(28*28, activation='sigmoid'))
    decoder.add(Reshape([28,28]))

    # stacked
    stacked_autoencoder = Sequential([encoder,decoder])
    stacked_autoencoder.compile(loss='binary_crossentropy',optimizer=keras.optimizers.SGD(lr=0.1), metrics=['acc'])

    stacked_autoencoder.summary()
    history = stacked_autoencoder.fit(X_train, X_train, epochs=1,
                             validation_data=[X_valid, X_valid])
    #show_reconstructions(stacked_autoencoder,images=X_valid)


    encoder_pred = encoder.predict(X_valid)
    tsne = TSNE()
    X_valid_2D= tsne.fit_transform(encoder_pred)
    plt.scatter(X_valid_2D[:, 0], X_valid_2D[:, 1], c=y_valid, s=10, cmap="tab10")
    plt.show()




if __name__ == '__main__':
    main()
