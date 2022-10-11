"""
Author:
Purpose: set and directary comprehensions
Date：
"""

import argparse
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


def setDict():
    s1 = {x for x in range(10)}
    s2 = set(x for x in range(10))
    print(s1)
    print(type(s1))
    print(s2)
    print(type(s2))

def timer():
    start = time.time()
    time.sleep(1)
    stop = time.time()
    print("time usage:%s"%(round((stop-start),5)))

def main():
    """the entrance of this file"""
    timer()



if __name__ == '__main__':
    main()
