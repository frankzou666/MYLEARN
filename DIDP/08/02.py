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
    x = np.linspace(-10,11,200)
    y = np.sin(x)
    z = np.zeros_like(x)

    for i in range(50):
        c = np.random.choice(x)
        n_inx = np.where(x == c)[0][0]
        z[n_inx] = np.sin(c)
    plt.plot(x,z)
    plt.show()



if __name__ == '__main__':
    main()
