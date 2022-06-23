


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

def main():
    n1 = np.mat([[1, 3], [4,5]])
    n2 = np.mat([[1, 3], [5,3]])
    n3 = n1.I

    print(n1*n3)
    print(n3*n1)

if __name__ == '__main__':
    main()
