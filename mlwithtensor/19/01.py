"""
Author:
Purpose:
Date：
"""

import argparse
import tensorflow as tf
import matplotlib.pyplot as plt
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


def getData():
    x = np.random.rand(10, 2)
    y = np.random.rand(10, 2) + 1
    return x ,y

def plotData(x,y):
    """

    :return:
    """
    plt.scatter(x[:, 0], x[:, 1],c='r', marker='x')
    plt.scatter(y[:, 0], y[:, 1], c='g', marker='x')
    plt.show()

def main():
    """the entrance of this file"""
    x,y = getData()
    plotData(x, y)


if __name__ == '__main__':
    main()
