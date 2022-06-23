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


def getSmall():
    A = [2,5,9,-6,7]
    key = A[0]
    count = 0
    for i in range(len(A)):
        for j in range(i,len(A)):
            if A[j] < key:
                key = A[j]
                tmp = A[i]
                A[i] = A[j]
                A[j] = tmp
            count = count + 1
    print(key)
    print(A)
    print(count)

def main():
    """the entrance of this file"""
    getSmall()


if __name__ == '__main__':
    main()

