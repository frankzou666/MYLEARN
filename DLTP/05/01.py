"""
Author:
Purpose:
Date：
"""

import argparse
import numpy as np
from tensorflow import keras
from tensorflow.keras.activations import relu
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def crossEntorpy(ytruth,ypred):
    if  ytruth == 1:
        return -np.log(ypred)
    else:
        return -np.log(1-ypred)

def main():
    """the entrance of this file"""
    print(crossEntorpy(10,9))
    activationfunction = relu()


if __name__ == '__main__':
    main()
