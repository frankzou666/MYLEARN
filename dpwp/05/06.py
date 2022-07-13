"""
Author:
Purpose:
Date：
"""

import argparse
import glob
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


def mktest(src,dst):
    """
     copy src direct to des directory
    :param src:
    :param dst:
    :return:
    """
    for item in os.listdir(src):
        if os.path.isdir(os.path.join(src,item)):
            os.mkdir(os.path.join(dst,item))
            mktest(os.path.join(src,item), os.path.join(dst,item))
        else:
            os.path.

def main():
    """the entrance of this file"""
    src = r'c:\temp\119'
    dst = r'c:\temp\118'
    mktest(src, dst)




if __name__ == '__main__':
    main()
