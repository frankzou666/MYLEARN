"""
Author:
Purpose: matrix
Date：
"""

import sympy as sym
sym.init_printing()

import argparse
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
    # define a matrix
    m = sym.Matrix([[2, 3], [4, 9]])


if __name__ == '__main__':
    main()
