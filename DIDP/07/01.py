"""
Author:
Purpose:
Date：
"""

import argparse
from mxnet import np
from mxnet.gluon import nn

np.set_printoptions()

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
    model = nn.Sequential()
    model.add(nn.Conv2D(10, kernel_size=3, activation='relu'))
    model.add(nn.MaxPool2D(pool_size=2, strides=2))
    model.initialize()
    print('hello')



if __name__ == '__main__':
    main()
