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

x=10
def func():
    global  x
    x =100

def main():
    """the entrance of this file"""
    print(x)
    func()
    print(x)

if __name__ == '__main__':
    main()
