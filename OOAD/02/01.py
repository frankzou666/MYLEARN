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
    return argparser.parse_args()


class Student():
    """test class"""
    name = 'hello'

    def __init__(self):
        print('object create from null')

    def __del__(self):
        print('I am be deleted')


def main():
    """the entrance of this file"""
    print(Student.name)
    Student.name = 'change new name '
    print(Student.name)


if __name__ == '__main__':
    main()
