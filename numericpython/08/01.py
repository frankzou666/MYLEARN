"""
Author:
Purpose:
Date：
"""

import argparse

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import integrate
import sympy
import mpmath

sympy.init_printing()


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def f(x,a,b,c):
    return a*np.exp(-((x-b)/c)**2)

def main():
    """the entrance of this file"""
    val,err = integrate.quad(f,-1,1,(1,2,3))
    print(val)
    print(err)


if __name__ == '__main__':
    main()
