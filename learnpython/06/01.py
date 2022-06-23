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


def main():
    """the entrance of this file"""
    sum = 1
    total =1
    for i in range(1,4):
        sum = sum*i
    for i in range(1):
        total = 24 * total
    print(sum)
    print(total)
    print(sum/total)


if __name__ == '__main__':
    main()
