
"""
Author:
Purpose:
Date：
"""


import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def func():
    pass

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    u = np.linspace(-1, 1, 100)
    ax.plot_surface(u,u,u)
    plt.show()


if __name__ == '__main__':
    main()