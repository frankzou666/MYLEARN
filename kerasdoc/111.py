"""
Author:
Purpose:
Date：
"""

import argparse
import os
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
    dirname = 'testdir'
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    if os.path.exists(dirname):
        filelists = [name for name in os.listdir(dirname)]
    print(filelists)


if __name__ == '__main__':
    main()
