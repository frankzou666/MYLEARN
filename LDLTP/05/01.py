"""
Author:
Purpose:
Date："""
import argparse
import idx2numpy
import numpy as np
import matplotlib.pyplot as plt

TRAIN_IMAGE_FILENAME = 'train-images-idx3-ubyte'
TRAIN_IMAGE_LABEL = 'train-labels-idx1-ubyte'
TEST_IMAGE_FILENAME = 't10k-images-idx3-ubyte'
TEST_IMAGE_LABEL = 't10k-labels-idx1-ubyte'


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

def read_minst():
    TRAIN_IMAGE = idx2numpy.convert_from_file(TRAIN_IMAGE_FILENAME)
    TRAIN_LABEL = idx2numpy.convert_from_file(TRAIN_IMAGE_LABEL)
    TEST_IMAGE = idx2numpy.convert_from_file(TEST_IMAGE_FILENAME)
    TEST_LABEL = idx2numpy.convert_from_file(TEST_IMAGE_LABEL)

    TRAIN_IMAGE = TRAIN_IMAGE.reshape(60000,784)
    X_TRAIN_IMAGE = (TRAIN_IMAGE-np.mean(TRAIN_IMAGE)) / np.std(TRAIN_IMAGE)

    TEST_IMAGE = TEST_IMAGE.reshape(10000, 784)
    X_TEST_IMAGE = (TEST_IMAGE - np.mean(TEST_IMAGE)) / np.std(TEST_IMAGE)

    y_train = np.zeros((60000, 10))
    y_test = np.zeros((10000, 10))

    for i, y in enumerate(TRAIN_LABEL):
        y_train[i][y] = 1
    for i, y in enumerate(TEST_LABEL):
        y_test[i][y] = 1
    return X_TRAIN_IMAGE, y_train, X_TEST_IMAGE, y_test


def layer_w(neuron_count, input_count):
    weights = np.zeros((neuron_count, input_count+1))
    for i in range(neuron_count):
        for j in range(1, (input_count+1)):
            weights[i][j] = np.random.uniform(-0.1, 0.1)
    return weights


def main():
    """the entrance of this file"""
    x_train_image, y_train, x_test_image, y_test = read_minst()
    weights = layer_w(25,784)
    hidden_layer_y = np.zeros(25)
    hidden_layer_error = np.zeros(25)

    output_layer_w = layer_w(10, 25)
    output_layer_y = np.zeros(10)
    output_layer_error = np.zeros(10)

    print(weights)






if __name__ == '__main__':
    main()
