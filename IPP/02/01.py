"""
Author:
Purpose:
Date：
"""

import argparse
import sys
import cProfile

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def loadfile():
    """
    load file as dict
    :arg
    :return:
    """
    file = 'a.txt'
    try:
        with open(file, 'r') as r:
            print(r.readlines())
    except IOError as e:
        print(e)
        sys.exit(1)


def main():
    """the entrance of this file"""
    loadfile()
    cProfile.run('loadfile()')


if __name__ == '__main__':
    main()
