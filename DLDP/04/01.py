"""
Author:
Purpose:
Date：
"""

import argparse
import keras
from keras import backend
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


def main():
    """the entrance of this file"""
    x = [i for i in range(-100,100)]
    y = [6 for i in range(-100,100)]


    for j in range(1,len(x)):
        if (y[j]-y[0]) != 0:
           print((x[j]-x[0])/(y[j]-y[0]))


    plt.scatter(x,y)
    plt.show()


if __name__ == '__main__':
    main()
