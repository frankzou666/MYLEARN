"""
Author:
Purpose:
Date：
"""

import argparse
from scipy import interpolate
from numpy import polynomial
import matplotlib.pyplot as pyt
from scipy import linalg
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


def main():
    """the entrance of this file"""
    p1 = polynomial.Polynomial([1,2,3])
    print(p1.roots())
    print(p1(np.array((5))))


if __name__ == '__main__':
    main()
