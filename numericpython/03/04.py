"""
Author:
Purpose:
Date：
"""
import argparse
import sympy as sym
import numpy as np
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


def main():
    """the entrance of this file"""
    x = sym.Symbol("x")
    y = sym.Symbol("y")
    expr = x+20
    n1 = np.arange(0,100)
    expr_func=sym.lambdify(x,expr,'numpy')
    print(expr_func(n1))


if __name__ == '__main__':
    main()
