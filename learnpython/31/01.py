"""
Author:
Purpose:
Date："""
import argparse


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


class Wrapper():
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, item):
        # getattr is a built-in funcion
        return getattr(self.wrapped, item)


def main():
    """the entrance of this file"""
    x = Wrapper([1, 2, 3])
    x.append(1)
    print(x.wrapped)


if __name__ == '__main__':
    main()
