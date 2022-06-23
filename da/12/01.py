
"""
Author:
Purpose:
Date：
"""


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


def DFT(x):
    """
    Compute the discrete Fourier Transform of the 1D array x
    :param x: (array)
    """

    N = x.size
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, x)


def main():
    t = np.linspace(-10, 10,100)
    s = np.power(t,2)*np.sin(1/t)

    plt.plot(t, s)
    plt.show()


if __name__ == '__main__':
    main()