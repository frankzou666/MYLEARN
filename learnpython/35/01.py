
"""
Author:
Purpose:
Date：
"""


import argparse
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

class Myexception(Exception):
    def __str__(self):
        return  'Myexception'

def main():
    try:
        1/0
    except Exception as e:
        print(sys.exc_info())

if __name__ == '__main__':
    main()