
"""
Author:
Purpose:
Date：
"""


import argparse
import random
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
    x = np.linspace(-1,1,1000)
    y=x
    z= np.cos(x)
    plt.plot(x,y)
    plt.plot(x,z)
    plt.plot(x, np.zeros_like(x),'red')
    plt.plot(np.zeros_like(x),x, 'red')
    plt.show()


if __name__ == '__main__':
    main()