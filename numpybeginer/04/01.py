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


def main():
    """the entrance of this file"""
    np1= np.random.randint(1,10,(3,3))
    print(np1)
    print(np.mean(np1, axis=0))
    print(np.median(np1,axis=0))
    print(np.std(np1, axis=0))
    # print(np.correlate(np1, axis=0))
    print(np.unique(np1, axis=0))
    plt.imshow(np1)
    plt.show()


if __name__ == '__main__':
    main()
