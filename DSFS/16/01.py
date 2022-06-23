"""
Author:
Purpose:
Date：
"""

import argparse
import math
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


def logisticFunction(item:float) -> float:
    """
    
    :param item: 
    :return: 
    """
    return 1/(1+math.exp(-item))

def main():
    """the entrance of this file"""
    x = [item for item in range(-10, 10)]
    y = [logisticFunction(item) for item in x]
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    main()
