"""
Author:
Purpose:
Date：
"""

import argparse
from  my1.hello import hellos

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()

import argparse
import  my1

def main():
    """the entrance of this file"""
    my1.hello.hellos()


if __name__ == '__main__':
    main()
