"""
Author:
Purpose:
Date：
"""

import argparse
import contextlib
import os
import re

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()



def getPing():
    r = os.popen('ping 127.0.0.1 -t')



def testMatch():
    text = 'hello world'
    matchstring1 = re.match('helloA', text)
    print(matchstring1)
    matchstring2 = re.match('hello', text)
    print(matchstring2.group(2))
    print(matchstring2)

    return  True


def testPrecompile():
    """"""
    text = 'hello world'
    mycompile = re.compile('hello')
    print(mycompile.match(text))


def main():
    """the entrance of this file"""
    testPrecompile()



if __name__ == '__main__':
    main()
