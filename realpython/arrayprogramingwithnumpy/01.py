
"""
Author:
Purpose:
Date：
"""


import argparse
from timeit import timeit
import time

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def helloWord():
    time.sleep(1)

def main():
    NUM = 10
    SETUP = 'from __main__ import helloWord'
    print(timeit('helloWord()',setup=SETUP, number=NUM))

if __name__ == '__main__':
    main()