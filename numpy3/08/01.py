
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
    return  argparser.parse_args()

def main():
    x = np.linspace(0,4,100)
    xx = np.outer(x,x)
    val = np.sin(xx)
    plt.imshow(val)
    plt.show()

if __name__ == '__main__':
    main()