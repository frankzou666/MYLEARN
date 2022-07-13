"""
Author:
Purpose:
Date：
"""

import argparse
import os
import time

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
    # file = open('01.py','r',encoding='utf8')
    """
    for line in file.readlines():
        print(line,end='#')
    """
    """
    while True:
        line = file.read()
        if not line: break
        print(line)
    file.close()
    """
    """
    p = os.popen('ping www.163.com')
    i = iter(p)
    while True:
        try:
            print(next(i))
        except StopIteration:
            break
    """

    m = map(lambda  x: x+x, range(10))
    for x in m:
        print(x)


if __name__ == '__main__':
    main()
