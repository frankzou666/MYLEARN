"""
Author:
Purpose:
Date：
"""

import argparse
import numpy as np
import sympy as sym

sym.init_printing()

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def equationsSolv():
    """the entrance of this file
     3x(1) + 4x(2) = 18
     6x(1) + 9x(2) = 39
     4x(1) + 4x(2) = 20
     result = x(1)=2,X(2)=3
    """

    A = np.array([[3,4],[6,9],[4,4]])
    b = np.array([[18],[39],[20]])
    x = np.dot(np.dot(np.linalg.inv(np.dot(A.T,A)),A.T), b)
    print(x.T)

def main():
    X = sym.Symbol("X")
    Y = sym.Symbol("Y")
    expr = (X+1)*(X-2)
    print(expr)
    print(sym.expand(expr))
    print(sym.cos(X+Y).expand(trig=True,mul=True))


if __name__ == '__main__':
    main()
