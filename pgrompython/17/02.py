
"""
Author:
Purpose:
Date：
"""


import argparse
import matplotlib.pyplot as plt
import numpy as np

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
    x=np.array([1,2,3,4,5])
    y=np.square(x)
    z=x*6-9
    plt.plot(x,y,'bo')
    plt.plot(x, y)
    plt.plot(x,z)
    plt.show()

if __name__ == '__main__':
    main()