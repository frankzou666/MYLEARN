"""
Author:
Purpose:
Date：
"""

import argparse
from mxnet import autograd, gluon, init, np, npx
from mxnet.gluon import nn




npx.set_np()

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
    T = 1000  # Generate a total of 1000 points
    time = np.arange(1, T + 1, dtype=np.float32)
    x = np.sin(0.01 * time) + np.random.normal(0, 0.2, (T,))
    d2l.plot(time, [x], 'time', 'x', xlim=[1, 1000], figsize=(6, 3))



if __name__ == '__main__':
    main()
