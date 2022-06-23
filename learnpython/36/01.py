
"""
Author:
Purpose:
Date：
"""


import argparse
import traceback
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

def bye():
    sys.exit(40)

def main():
    try:
        bye()
    except:
        print('ok')
        print(traceback.print_stack())

if __name__ == '__main__':
    main()