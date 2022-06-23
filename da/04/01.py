
"""
Author:
Purpose: python for data analysis ,chapter 04
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

def main():
    #create from list
    n1 = np.array([1,2,3,4])
    print(n1)
    # create 2 ndim
    n2 = np.array([[1, 2, 3, 4],[1, 2, 3, 4]])
    # compuation between ndarray and scalar
    n3 = n2+5
    print(n3)

if __name__ == '__main__':
    main()