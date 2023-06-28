"""
Author:
Purpose:
Date："""
import argparse
import  functools
from functools import wraps

def f(x, y):
    return x ** 2 * y + y + 2


def derivative(f, x, y, x_eps, y_eps):
    return (f(x + x_eps, y + y_eps) - f(x, y)) / (x_eps + y_eps)


def myDector(str):
    def fun1(f):
        print(str)
        return  f
    return fun1


@myDector("error")
def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()



@myDector("ok")
def main():
    """the entrance of this file"""

    df_dx = derivative(f, 3, 4, 0.00001, 0)
    df_dy = derivative(f, 3, 4, 0, 0.00001)
    getargs()
    print(df_dx)
    print(df_dy)


if __name__ == '__main__':
    main()
