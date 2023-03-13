"""
Author:
Purpose: 3,EigenValue problem
Date："""
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
    eps,delta = sympy.symbols('eps,delta')
    h = sympy.Matrix([[eps,delta],[delta,-eps]])
    print(h.eigenvals())


if __name__ == '__main__':
    main()
