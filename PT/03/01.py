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
    x= np.linspace(-10,10,200)
    y=np.tan(x)
    plt.plot(x,y)
    plt.show()



if __name__ == '__main__':
    main()
