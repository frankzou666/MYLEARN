
"""
Author:
Purpose:
Date：
"""


import argparse
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

def f(x):
    return  2*x

def gradientDesen(gradient,numinter,learningrate,start):
    vector = start
    for n in range(numinter):
        diff = -learningrate*gradient(vector)
        vector =diff + vector
    return  vector

def main():
    print(gradientDesen(lambda v: 2 * v,80,0.01,(10)))

if __name__ == '__main__':
    main()