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

def curve(CURVE_CENTER, grades):
    average = grades.mean()
    change = CURVE_CENTER - average
    new_grades = grades + change
    return np.clip(new_grades, grades, 100)


def fun1():
    CURVE_CENTER = 80
    grades = np.array([72, 35, 64, 88, 51, 90, 74, 12]).reshape(4, -1)
    score = np.array([1, 2]).reshape(1, 2)
    print(grades)
    gradesmask = grades > 44
    print(gradesmask)
    print(grades[gradesmask])


def normalTest():
    x = np.random.standard_normal(1000).reshape(1000,-1)
    y = np.random.standard_normal(1000).reshape(1000,-1)
    plt.scatter(x,y)
    plt.show()

def main():
    normalTest()




if __name__ == '__main__':
    main()
