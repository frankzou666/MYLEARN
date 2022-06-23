"""
Author:
Purpose:
Date：
"""

import argparse
import sympy


sympy.init_printing()

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
    x1 = sympy.Symbol('x_1')
    x2 = sympy.Symbol('x_2')
    f_x1 = 5*x1**4+x2**2
    print(f_x1)
    gradients = sympy.Matrix([ f_x1.diff(x_) for x_ in (x1,x2)])
    print(gradients)
    hess = sympy.Matrix([f_x1.diff(x1_, x2_) for x1_ in (x1,x2) for x2_ in  (x1,x2)])
    print(hess)

if __name__ == '__main__':
    main()
