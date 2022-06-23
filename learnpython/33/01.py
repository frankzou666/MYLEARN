
"""
Author:
Purpose:
Date：
"""


import argparse

def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()



class  Myexption(Exception):
    pass


def fun1():
    x = 'spam'
    try:
        y = x[4]
    except  IndexError as e:
        print('from IndexError')
        raise 
    else:
        print('from else')
    finally:
        print('from finally')

def main():
    fun1()


if __name__ == '__main__':
    main()