
"""
Author:
Purpose:
Date：
"""

import sklearn
from sklearn.datasets import load_sample_image
import tensorflow as tf

import argparse
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
    return  argparser.parse_args()

def main():
    # Load sample images
    china = load_sample_image("china.jpg") / 255
    flower = load_sample_image("flower.jpg") / 255
    images = np.array([china, flower])
    batch_size, height, width, channels = images.shape
    # Create 2 filters
    filters = np.zeros(shape=(14, 14, channels, 3), dtype=np.float32)
    filters[:, 3, :, 0] = 1  # vertical line
    filters[3, :, :, 1] = 1  # horizontal line
    outputs = tf.nn.conv2d(images, filters, strides=1, padding="VALID")
    plt.imshow(outputs[0, :, :, 1], cmap="gray")  # plot 1st image's 2nd feature map
    plt.show()

if __name__ == '__main__':
    main()