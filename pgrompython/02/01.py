
"""
Author:
Purpose:
Date：
"""


import argparse
import sys
import re
import os

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def main1():
    if sys.platform == 'win32':
        print('windows')
    else:
        print('ok')


def main2():
    filepath = r'C:\Users\Administrator\PycharmProjects\untitled\pgrompython\02\01.py'
    print("###")
    print(os.path.abspath(filepath))
    print(os.path.dirname(filepath))
    print(os.path.basename(filepath))

def main3():
    try:
        raise IndexError
    except :
        print(sys.exc_info())

def main():
    while True:
        print(os.popen('ping www.163.com').read())


if __name__ == '__main__':
    main()