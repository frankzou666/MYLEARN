
"""
Author:
Purpose:
Date：
"""


import argparse

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def f(x):
    return x**2

def differentiation(f,x,epos):
    return  (f(x+epos) - f(x))/ epos

def main():
    print(f(10))
    print(differentiation(f,10,0.00001))

if __name__ == '__main__':
    main()