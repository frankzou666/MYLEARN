"""
Author:
Purpose:
Date：
"""

import argparse
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d

tf._compat.disable_v2_behavior()

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
    W = 0.2
    B = 0.7
    x = []
    y = []
    for i in range(500):
        v = np.random.normal(0.0,0.5)
        x.append(v)
        y.append(W*v+B+np.random.normal(0.0,0.1))


    print(x[0:100])
    print(y[0:100])



if __name__ == '__main__':
    main()
