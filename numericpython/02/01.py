
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
    n1 = np.array(([1,2.2],[2,3.3],[9,6]),dtype=np.complex)
    print(n1.shape)
    print(n1.size)
    print(n1.dtype)

if __name__ == '__main__':
    main()