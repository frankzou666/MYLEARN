
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


def main():
    filepath = r'C:\Users\Administrator\PycharmProjects\untitled\pgrompython\02\01.py'
    print(os.path.abspath(filepath))
    print(os.path.dirname(filepath))
    print(os.path.basename(filepath))

if __name__ == '__main__':
    main()