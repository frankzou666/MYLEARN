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
    x = sympy.Symbol("x")
    y = sympy.Symbol("y")
    n1= sympy.Rational(11,13)
    n2 = sympy.Rational(11, 13)
    print(n1*n2)



if __name__ == '__main__':
    main()
