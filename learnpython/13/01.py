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


def main():
    """the entrance of this file"""
    x = 10
    """
    while True:
        if x<10: break
        print(x)
        x = x-1
    """
    """
    for i in range(5):
        print(i)
    else:
        print('good')
    """
    """
    # how to use enumerate
    x ='hello'
    for i,j in enumerate(x):
        print(i)
        print(j)
    """
    


if __name__ == '__main__':
    main()
