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
    return argparser.parse_args()


def getLogisticTest():
    """test logistic"""
    x = np.linspace(-50,50,100)
    y = 1/(1+np.e**(-x))
    plt.plot(x,y)
    plt.show()

def main():
    """the entrance of this file"""
    getLogisticTest()


if __name__ == '__main__':
    main()
