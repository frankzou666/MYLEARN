"""
Author:
Purpose:
Date：
"""

import argparse
from  models.Draw import *


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
    draw = Draw()


if __name__ == '__main__':
    main()
