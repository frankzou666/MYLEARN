"""
Author:
Purpose:
Date：
"""

import argparse
import  numpy as np
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
    x = np.linspace(1,100,100).reshape(1,-1)
    y = np.linspace(1,100,100).reshape(1,-1)
    z = (x*(100-x))
    q = z/2
    print(np.max(q))
    plt.scatter(x,q)
    plt.show()


if __name__ == '__main__':
    main()
