"""
Author:
Purpose:
Date：
"""

import argparse

import numpy as np
from typing import List

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def splidata(data,prob:float):
    data = data.copy()
    np.random.shuffle(data)
    cut = int(len(data)*prob)
    return data[:cut],data[cut:]


def main():
    """the entrance of this file"""
    n = [x for x in range(5)]
    print(n)
    x, y = splidata(n, 0.3)
    print(x)
    print(y)


if __name__ == '__main__':
    main()
