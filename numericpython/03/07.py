"""
Author:
Purpose: equation
Date：
"""
import argparse
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


def main():
    """the entrance of this file"""
    x = sym.Symbol("x")
    y = sym.Symbol("y")
    exp1=x+2*y-1
    exp2 = x-y+1
    print(sym.solve([exp1,exp2],[x,y],dict=True))


if __name__ == '__main__':
    main()
