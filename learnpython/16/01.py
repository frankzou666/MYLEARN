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
    return argparser.parse_args()


def Chager(x, y):
     x = 10
     y.append('hello')
     return x,y

def main():
    """the entrance of this file"""
    a = 5
    b = ['first']
    print(type(Chager(a,b)))
    print(Chager(a, b))



if __name__ == '__main__':
    main()
