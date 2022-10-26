"""
Author:
Purpose: calculus
Date：
"""
import argparse
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
    x=sym.Symbol('x')
    f = sym.Function('f')(x)
    print(f)
    print(sym.diff(f, x))
    print(sym.diff(f,x,2))
    print(sym.diff(f, x, 3))


if __name__ == '__main__':
    main()
