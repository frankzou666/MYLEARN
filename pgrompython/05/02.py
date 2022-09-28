"""
Author:
Purpose: fork processes
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

def child():
    """
    :return:
    """
    print('i am child '+str(os.getpid()))
    os._exit(0)


def main():
    """the entrance of this file"""
    new_pid = os.fork()
    if new_pid == 0:
        child()
    else:
        print('i am parent '+str(os.getpid()))


if __name__ == '__main__':
    main()
