
"""
Author:
Purpose:
Date：
"""


import argparse
import dbm

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def dbmFunc():
    dbmfile = dbm.open('test.dbm','c')
    dbmfile['hello'] ='ok'
    dbmfile.close()

def dbmGet():
    dbmfile = dbm.open('test.dbm','c')
    print(dbmfile['hello'].decode())
    dbmfile.close()


def f(x):
    return x**3

def getDerivate(func,h):
    if h == 0:
        print('error')
        return None
    return  (f(5 + h)-f(5))/h

def main():
    dbmFunc()
    print(getDerivate(f,.0001))

if __name__ == '__main__':
    main()