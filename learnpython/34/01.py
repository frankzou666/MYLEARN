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

class MyString(Exception):
    pass

def main():
    """the entrance of this file"""
    mystring="excpetion string"
    raise MyString(mystring)


if __name__ == '__main__':
    main()
