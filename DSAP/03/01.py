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


def fun1(id:int):
    total = 0
    if id == 1:
        return 0
    return  id+fun1(id-1)

def main():
    """the entrance of this file"""
    print(fun1(10))


if __name__ == '__main__':
    main()
