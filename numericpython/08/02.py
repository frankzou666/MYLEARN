"""
Author:
Purpose:
Date："""
import argparse
import scipy
import sympy


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def main1():
    """the entrance of this file"""
    x = sympy.Symbol("x")
    f = 2*sympy.sqrt(1-x**2)
    a,b = -2,2
    value = sympy.integrate(f,(x,a,b))
    print(value)

def main():
   # s = sympy.symbols("s")
    a,t,w = sympy.symbols("a,t,omega")
    f = sympy.exp(-a*t**2)
    F = sympy.fourier_transform(f,t,w)
    print(F)


if __name__ == '__main__':
    main()

