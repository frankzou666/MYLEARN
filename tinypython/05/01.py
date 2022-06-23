
"""
Author:
Purpose:
Date：
"""


import argparse
import os
import sys

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def main():
    path = 'C://Users//Administrator//PycharmProjects//untitled//tinypython//05//011.py'
    fh = open('1.txt','w')
    print('hello workd from adddbc', file=sys.stdout)
    print(fh)
    fh.close()


if __name__ == '__main__':
    main()