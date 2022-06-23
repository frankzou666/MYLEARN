"""
Author:
Purpose:
Date：
"""

import argparse

from scipy import stats
from scipy import  optimize
import numpy as np
import matplotlib.pyplot as plt


import seaborn as sn

#sn.set('style="whitegrid"')

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

def pharse2():
    """the entrance of this file"""
    x = np.array([3.5, 1.1, 3.2, 2.8, 6.7, 4.4, 0.9, 2.2])
    # mean
    print(x.mean())
    # variance
    print(x.var())
    # standard deviation
    print(x.std())

def randomNumber():
    """

    :return:
    """
    np1 = np.random.rand(5)
    print("uniform distributio:"+ np1.tolist().__str__())
    np2 = np.random.randn(5)
    print("standard normal distributio:" + np2.tolist().__str__())
    np3 = np.random.randint(1,10,6)
    print("uniform integer distributio:" + np3.tolist().__str__())
    np4 = np.random.randint(1, 10, size=(2,3))
    print("uniform integer distributio:" + np4.tolist().__str__())

def randomNumberwithPlot():
    """

    :return:
    """
    fig,axi = plt.subplots(1,3,figsize=(12,3))
    axi[0].hist(np.random.rand(10000))
    axi[1].hist(np.random.randn(10000))
    axi[2].hist(np.random.randint(low=1,high=10,size=10000))
    fig.show()

def randomWithStatsNorm():
    """

    :return:
    """

    x = stats.norm(1, 0.5)
    print(x.mean())
    print(x)


def main():
    """the entrance of this file"""
    randomWithStatsNorm()



if __name__ == '__main__':
    main()
